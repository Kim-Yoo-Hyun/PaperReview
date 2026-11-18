# TASK-GEOMETRY — 입력 개입·평가·Docker 실행 준비 명세

Updated: 2026-11-18 KST. **N1 내부 비실험 검토·P0 코드 준비 완료 / PREPARED_UNEXECUTED.** [질문·판정](../내용/README.md#p0-preparation-result) · [원장 `task_geometry_n1` / `task_geometry_p0_preparation`](../../../sources/new_field_scout_2026-11-17.json). Docker recipe와 깊이 교체 probe를 작성했고 새 launcher는 daemon 연결 실패로 중단됐다. Image build·Docker 검사·native 호환은 미검증이다. 1번 주제의 모델 자료를 재사용하지만 실행 결과는 분리한다.

## 1. 공개 source와 pin

정적 source 읽기이며 import·설치·추론을 하지 않았다. 파일 hash/검토 범위는 원장에 남기고 payload는 받지 않았다.

| 자원 | 고정 revision / 확인 범위 | 경계 |
|---|---|---|
| [SpatialVLA GitHub](https://github.com/SpatialVLA/SpatialVLA/tree/18fd74b2a633ec8d9ec7aadcd803969555cc9fbd) | `18fd74b2a633ec8d9ec7aadcd803969555cc9fbd`; model·processor·config·finetune·README·requirements | 실제 HF remote module과 구별 |
| [SpatialVLA HF](https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt/tree/886c4557dfde53b44c0f74fde7d89bf83a26c3cd) | `886c4557dfde53b44c0f74fde7d89bf83a26c3cd`; modeling/config/processor 재확인 | GitHub modeling과 byte-different. Weight/나머지 파일 metadata는 [기존 PLAN](../../pose_active_perception/재현%20방법/PLAN.json) 참조; payload 검증 아님 |
| [robosuite](https://github.com/ARISE-Initiative/robosuite/tree/5ce6643f3092639d08f7b0f90ed1c6a84f50552c) | `5ce6643f3092639d08f7b0f90ed1c6a84f50552c`; camera helper·NutAssembly·TwoArmPegInHole·nut/arena XML | Task 시연·VLA action frame·접촉 호환 미검증 |
| [GeoPredict](https://github.com/jingjingqian75/GeoPredict/tree/5191756e8c4f16de2b63c28636341f2d4f5cdf2e) | `5191756e8c4f16de2b63c28636341f2d4f5cdf2e`; README·train 문서/entry·Gaussian·model loss | Training source 공개 확인으로 11/17 미확인 보완. 실행·라이선스 결합·훈련 자산 전수검증 아님 |
| [SimplerEnv wrapper](https://github.com/DelinQu/SimplerEnv-OpenVLA/tree/ccfe3809766839a2fcfb7a3d3c9abff585189188) | `ccfe3809766839a2fcfb7a3d3c9abff585189188`; SpatialVLA wrapper·README | 기존 task와 새 fixture의 통계/좌표가 자동 호환되지 않음 |

GeomVLA project의 code와 EDI dataset card의 code 링크는 이번 접근에서404였다. 원인은 미확인이다. EDI의 simulator asset/expert 목록도 현재 VLA task 성공 데이터로 쓰지 않는다. 이들과 Robo3R을 첫 P0의 필수 dependency로 고정하지 않는다.

<a id="geometry-contract"></a>
## 2. 실제 geometry 입력과 개입

확인한 경로는 `RGB → ZoeDepth → resize/crop → area 축소 P → K⁻¹·pixel_ray·depth → camera XYZ → frequency encoding → Ego3D MLP → SigLIP feature 합산 → VLA`다. [Model](https://github.com/SpatialVLA/SpatialVLA/blob/18fd74b2a633ec8d9ec7aadcd803969555cc9fbd/model/modeling_spatialvla.py#L308), [processor](https://github.com/SpatialVLA/SpatialVLA/blob/18fd74b2a633ec8d9ec7aadcd803969555cc9fbd/model/processing_spatialvla.py#L91).

- **Gradient 경계2개:** depth/backprojection의 `no_grad`와 `frequency_encoding` decorator. 앞 경계만 옮겨서는 depth adapter에 action-loss gradient가 전달되지 않는다. MLP weight 학습과 depth 입력 미분은 다르다. 실제 HF module까지 확인한 후 학습 분기를 별도 구현한다.
- **해상도:** patch14·`ego3d_patch_reso=2`. 224 입력이면16×16 patch에 각4개 XYZ,32×32 depth 집계다. Subpatch fine geometry가 소실될 수 있다. Source/config에서 계산한 구조이며 실측 민감도가 아니다.
- **좌표:** 원 구현은 camera XYZ이며 extrinsic 입력이 없다. Robot/world XYZ를 그대로 넣으면 안 된다. 고정K의 scalar depth 변경은 시선 방향 변위만 만든다. 횡방향 변위를 depth 오류로 부르지 않는다.
- **Intrinsic:** processor가 이미지 크기로K를 조정하고 `unnorm_key` 미지정 시 default K를 쓴다. 새 camera는 실제K·RGB resize/crop·orientation을 함께 맞춘다. Default가 정상 calibration이라는 보장은 없다.

| 개입 | 첫 구현 범위 | 해석 경계 |
|---|---|---|
| 항등·원 depth 재주입 | Post-resize/crop, pre-P에서 같은 shape/dtype/device로 교체 | 원 feature/logit 재현이 먼저 |
| Scale/bias | 양의 유한 depth에서 `sD+b` | Range 오류 진단이며 extrinsic 오류가 아님 |
| 물체/fixture 영역 | 같은 mask/support·같은 post-P XYZ RMS | GT mask는 offline 개입 도구, 배포 입력 아님 |
| Subpatch 상쇄 | P 뒤 차이가0인 음성 대조 | 원해상도 metric과 policy-visible error 구분 |
| Shape/pose/camera | 이후 별도 renderer·visibility·좌표 계약 필요 | Collision mesh 변경은 task 변경. Render-only 변경은 별도 관측 개입이며 실제 세계의 증거가 아님 |

**Hook 구현:** [DepthOverride](./geometry.py)가 실제 로드된 모델 instance의 `backproject_patch`를 일시적으로 감싸고 원 remote file은 유지한다. Post-crop/pre-area depth에 개입하고 원래 함수를 호출한다. No-grad 경계 두 개를 유지하며 prefill당 depth/projector 호출이 각각 1회인지 검사한다. 군마다 generation cache를 초기화하고 종료/예외 시 wrapper를 제거한다. 항등 조건은 baseline에서 저장한 depth를 재주입한다. 학습용 경계 수정·input gradient 검사는 후속이며 미구현이다.

**추가 source 검토:** 공개 custom `from_pretrained`는 반환값을 model로 가정하므로 `output_loading_info=True`의 tuple과 충돌한다. 새 [probe](./probe.py)는 HF base loader로 loading info를 확인한 뒤 원 override의 spatial-token weight copy를 명시적으로 수행한다. 실제 remote module SHA256도 검사한다. 또한 BF16에서 `uv_h` 광선 좌표가 반올림될 수 있어 원 buffer를 보존하고 nominal 좌표와의 차이를 기록한다. K는 float32로 모든 조건에 동일하게 준다. 이 변경 경로의 **native 호환은 아직 미검증**이며 1번 주제의 frozen 코드는 수정하지 않았다.

**오차량:** 공통 유효 support S에서 `E_inj = sqrt(mean_{p∈S} ||X′_p-X_p||²)`와 `E_gt = sqrt(mean_{p∈S} ||X′_p-X_GT,p||²)`를 P 뒤에 별도로 측정한다. 같은 `E_inj`라도 기존 추정 오류와 합쳐진 `E_gt`는 다를 수 있다. P0는 주입 크기의 검사이며, 이후 “같은 실제 3D 오차” 비교는 `E_gt`까지 사전에 정한 범위로 맞춘 pair에 한정한다. 둘을 동시에 맞추기 어렵다면 범위를 완화한 사실을 보고하고 동일 오차 주장을 하지 않는다. 원해상도 depth·전체/ROI·mask 수·K·invalid/occlusion도 보존한다. Clipping으로 목표 오차를 맞춘 척하지 않는다. Test label/mesh/정답 clearance를 배포 입력으로 사용하지 않는다.

## 3. 장면과 성공 평가기

첫 장면은 한 팔·같은 강체 물체의 **넓은 배치/방향 정렬**로 제한한다. 좁은 삽입은 기본 능력과 접촉 평가 확보 후다. POSE-ACTIVE fixture는 코드 구조 참고이며 본 주제의 성공 증거가 아니다.

[NutAssembly](https://github.com/ARISE-Initiative/robosuite/blob/5ce6643f3092639d08f7b0f90ed1c6a84f50552c/robosuite/environments/manipulation/nut_assembly.py#L375)는 중심XY3cm·높이와 reach/release 조건을 사용한다. [TwoArmPegInHole](https://github.com/ARISE-Initiative/robosuite/blob/5ce6643f3092639d08f7b0f90ed1c6a84f50552c/robosuite/environments/manipulation/two_arm_peg_in_hole.py#L488)의 d/t/cos threshold도 기계 공차에서 유도한 성공 정의와 같지 않다. 환경 이름이나 기본 success boolean을 정밀 삽입의 ground truth로 쓰지 않는다.

대체 evaluator는 object/fixture local frame의 위치·yaw·높이 signed margin, release 후 유지, contact/penetration을 별도 기록한다. 허용 범위는 collision shape·task definition에서 정하고 test 결과를 보고 바꾸지 않는다. 원 environment success도 따로 보존한다. **이 evaluator·시연·VLA 정상 성공은 아직 확보되지 않았다.**

[Camera helper](https://github.com/ARISE-Initiative/robosuite/blob/5ce6643f3092639d08f7b0f90ed1c6a84f50552c/robosuite/utils/camera_utils.py)는 normalized depth 변환과 camera-axis correction을 제공한다. Image orientation, optical z/Euclidean range, projection/unprojection, resize/crop을 각각 검사한다. Normalized action은 task normalizer와 controller frame 검증 전 물리 명령으로 보내지 않는다.

## 4. 공정한 비교 계약

| 항목 | 고정할 내용 |
|---|---|
| Policy-visible | 동일RGB·instruction·checkpoint·processor/K·명시한 depth 조건. Oracle pose/shape/tolerance·future success 미노출 |
| 평가자 전용 | Simulator pose/mesh·mask·margin·contact. Label/split 생성에만 사용 |
| Paired 실행 | 초기 물리/controller state·RNG·policy history. 첫 chunk와 persistent 오류 분리 |
| Normalizer | 새 fixture 전용 통계 미확보. Bridge/default로 물리 action 강제 실행 금지 |
| 비용 | Adapter parameter·train data·label/rollout 수·update·관측·추론 비용 동일 |
| 분할 | Object/fixture family별 분리. 같은 상태의 clean/perturbed pair가 split을 넘지 않게 함 |
| 지표 | Episode 성공과 signed margin이 주 지표. Token/logit은 보조; 정답 기반 점수는 oracle |

항등 wrapper→입력 소비→기본 조작 능력→paired 결과→작은 학습 순서다. 무반응/실패의 원인이 hook·resize·tokenization·task 능력·geometry 중 무엇인지 구분한다. Source가 있다는 사실을 실제 실행 완료로 표시하지 않는다.

<a id="p0-plan"></a>
## 5. 준비한 최소 검증: TASK-GEOMETRY-P0

아래는 **실행 상한 제안**이며 성능 측정 표본 수가 아니다.

1. Scene1·고정 camera1에서 RGB/metric depth/K/CV extrinsic·geom segmentation을 저장한다. 동일 강체 nut를 script로 배치하며 settling·성공 판정·제어는 하지 않는다. Orientation·양의 depth·projection roundtrip과 ROI 가시성을 검사한다. ROI가 없으면 다른 시점을 자동 검색하지 않는다.
2. 지시2×geometry4조건: 원본 통과/항등 재주입/ROI +2cm/7×7 cell 내부 depth 순열. 순열은 area 평균을 보존하는 음성 대조지만 실제 floating-point 잔차를 측정한다. 이 합성 오류를 자연 오류나 물체 pose 변경으로 부르지 않는다.
3. Query≤8·각12 token·총AR step≤96·setup physics≤10,000. 물리 VLA command0·optimizer0·학습0. 원본이 invalid action token을 내면 decode하지 않고 입력 진단만 기록한다. Token family를 강제로 맞추지 않는다.
4. `E_inj`와 `E_gt`, ROI 오차, 원해상도/축소 후 변화, 실제 camera XYZ, projected feature, 첫 token logits, 생성 token과 정상일 때 normalized action을 기록한다. 항등에서 feature/token/좌표가 다르면 비교를 중단한다. 변화 조건의 후속 token은 prefix도 달라질 수 있어 logit 직접 비교는 첫 token으로 제한한다.
5. 같은 input의 즉각적 반응 검사이며 closed-loop 성공·실패 label·통계적 효과 검증이 아니다. 두 gradient 경계는 유지한다. 큰 rollout·SFT·task-margin adapter를 자동 시작하지 않는다.

**작성한 실행 자료:** [PLAN](./PLAN.json), [Dockerfile](./Dockerfile), [공유 설정·build context](./config.py), [launcher](./resume.py), [깊이 개입](./geometry.py), [scene/strict loader/IO probe](./probe.py), [Docker 검사11개](./checks.py). 반복된 checkpoint/의존성 목록은 1번 주제의 PLAN·requirements·payload helper를 hash로 고정해 참조한다. Host에서는 작성한 source/config만 임시 build context에 복사하고, package·외부 source 설치와 weights 수신은 Docker 안에서 한다. 기존 1번 주제 파일은 변경하지 않았다.

## 6. 환경 설정과 현재 로컬 확인

11/18 이번 준비에서 `desktop-linux` local Unix socket을 다시 확인했다. 새 launcher의 `run`은 **[BLOCKED_DAEMON / exit3](./results/preparation/local_check.json)**에서 중단됐다. 내부 `docker info`는 exit1·daemon 연결 오류를 반환했다. Host는 Darwin arm64이며 server architecture/RAM·NVIDIA·CUDA/EGL은 이번에 확인하지 못했다. 오류 응답의 빈 server 값·Images0을 실제 자산 목록으로 읽지 않는다. Container/image 생성0·설치0·native 실행0. 실패 조건에서 payload 다운로드를 반복하지 않았다.

다른 컴퓨터의 잠정 시작 설정이다. 측정된 최소 사양·실행 보장은 아니다.

| 설정 | 준비 기준·남은 확인 |
|---|---|
| Host/Docker | Linux x86_64·local Unix socket·`linux/amd64`·NVIDIA Container Toolkit. Remote/cloud/MPS 우회 없음 |
| GPU | CUDA/BF16 NVIDIA·compute major≥8. 기존 P0의 VRAM12GiB는 잠정 loader 기준, 전체 학습 충분조건 아님 |
| RAM/disk | Docker RAM≥16GiB·여유 disk≥30GiB 잠정 기준. Peak/build/cache 공간 측정 필요 |
| Package | torch2.5.1·torchvision0.20.1·transformers4.47.0·numpy1.26.4·MuJoCo3.3.0. CUDA12.4 base digest와 robosuite revision을 recipe에 고정했다. 기존 requirements 참조와 직접 버전 pin은 resolved transitive/apt hash lock이 아니며 새 image build·`pip check`는 미실행 |
| Model/source | 위HF/GitHub pin. Weight digest·파일 목록은 기존 PLAN 참조 후 Docker 안에서 재검증 |
| Runtime | Batch1·224 image·BF16/eager attention. Deterministic algorithms·TF32 off·`CUBLAS_WORKSPACE_CONFIG=:4096:8`로 항등 비교를 준비한다. Flash Attention은 사용하지 않는다. EGL·driver/runtime·strict loader 호환은 native 실행에서 확인 |
| Cache/output | Dependency·weight·asset은 Docker image/전용 named volume. Host에는 준비 소스와 한정된 JSON/RGB/NumPy 진단 결과를 저장 |
| 미확보 | Image/native 호환·학습 경계 수정·task normalizer·기본 조작 능력·evaluator·시연/label |

<a id="resume"></a>
## 7. 다른 컴퓨터에서 재개

저장소 루트에서 아래를 실행한다. Host Python은 표준 라이브러리로 local Docker를 확인/호출한다. 필요한 Linux/NVIDIA driver·Docker·Container Toolkit은 해당 컴퓨터의 전제이며 launcher가 host에 설치하지 않는다.

```bash
python3 'work/research_topics/task_geometry_estimation/재현 방법/resume.py' check
python3 'work/research_topics/task_geometry_estimation/재현 방법/resume.py' run
```

`check`는 공유 파일 hash·endpoint·daemon·platform/RAM metadata까지다. `run`은 이를 다시 확인한 뒤 **base container GPU/BF16 → image build → Docker 검사11개 → 환경 → scene/EGL → payload hash → VLA 입력 검증** 순으로 진행한다. 실패 시 다음 단계로 넘어가지 않는다. Scene이 실패하면 weights를 받지 않는다. 주제 전용 cache volume은 `paperreview-task-geometry-cache-v1`, image는 `paperreview-task-geometry:p0-20261118`이다. Native container는 network none, build/fetch만 network를 사용한다.

기본 결과는 gitignore한 `runs/`의 새 폴더다. `--output`은 비어 있는 경로만 받는다. 성공 시 환경/package 목록·resolved PLAN·scene RGB/geometry/ROI·payload hash·condition별 depth/XYZ/feature/첫 logits/token·예산/peak VRAM이 남는다. 실패 시 해당 단계의 로그와 부분 결과를 보존한다. 이번 run 고유 이름의 container만 정리하며 image/cache는 재개용으로 유지한다. 기존 사용자 자원에 `prune`하지 않는다.

**실제로 확인한 것은 Python 정적 컴파일과 launcher의 daemon 실패 차단까지**다. Docker 검사11개는 코드 작성 상태이며 통과했다고 보고하지 않는다. 입력 probe가 통과해도 task 정상 능력·자연 오류·실제 로봇·방법 성능을 입증하지 않는다. 다음 TODO는 **TASK-GEOMETRY-P0 / NATIVE_RESOURCE_WAIT**이며, 전체 연구 방법은 별도 구현·검증이 남는다.
