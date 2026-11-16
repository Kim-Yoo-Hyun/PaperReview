# 물체 집합·수량 — 재현 방법

2026-11-03 폴더 정리: 과거 실행 JSON의 명령·hash는 당시 기록을 유지한다. 현재 실행은 이 문서의 명령을 사용하고, 이전 경로는 [이동·병합 대응표](../../ORGANIZATION.json)에서 찾는다.

환경·명령·미구현 항목을 관리하는 단일 안내다. 아래 날짜별 점검은 당시 결과이며 현재 GPU 또는 정책 성공의 증거가 아니다. 실행 범위와 설정은 RESUME_PLAN.json을 따른다.

[연구 내용](../내용/README.md) · [재현 방법](../재현%20방법/README.md)

<a id="execution"></a>

<a id="execution-물체-집합수량-지시-연구를-위한-기본-조작-검증-준비"></a>
## 물체 집합·수량 지시 연구를 위한 기본 조작 검증 준비

- Updated: 2026-11-01 KST
- **준비 코드 작성 / image 미빌드 / native 실행 0 / WAITING_RESOURCE.** 현재 컴퓨터의 [실측](LOCAL_CHECK_2026-11-01.json)은 Docker Linux ARM64, 약 7.65 GiB, NVIDIA GPU allocation 실패(exit 125)다. 이 실패는 연구 가설의 반증이 아니다.
- Canonical 실행 설정: [RESUME_PLAN.json](RESUME_PLAN.json). 공개 source·29개 checkpoint 파일의 identity/hash·장면: [ARTIFACTS.json](ARTIFACTS.json). 연구 질문과 선행 충돌은 [source 심사](../내용/README.md#source-review)에 보존한다.
- 후속 [재개 점검](README.md#preparation-history): local `check`는 다시 ARM64에서 exit 3이었다. 기존 실패 GPU 할당은 반복하지 않았다. Recipe 일치·결과 분류의 **준비 코드 검사 10개만 기존 ARM64 Docker에서 통과**했으며 target image·CUDA/EGL·정책 검증은 아니다. [명령·source·검사 기록](READINESS_REVIEW_2026-11-01.json).

<a id="execution-범위와-준비-상태"></a>
### 범위와 준비 상태

VLABench `select_fruit`의 **배를 접시에 넣기** 한 장면으로 공개 π0 checkpoint의 입출력과 기본 조작을 확인한다. 원 지시·나열·집합 규칙의 효과 비교나 Q1–Q8 검증은 아니다. 1회 성공도 여러 물체·새 속성 조합의 능력을 보장하지 않는다.

| 구분 | 현재 상태 |
|---|---|
| 준비됨 | Source/checkpoint/normalizer/scene 고정, Dockerfile, 두 Python 환경, Docker volume 저장, bounded adapter·관측/행동 검사·결과 저장 코드 |
| 실제 확인됨 | 현재 local daemon/ARM64/메모리, GPU allocation 실패, launcher의 ARM64 차단, source·metadata 정합성 및 구문 검사 |
| 후속 준비 코드 검사 | 빌드된 recipe와 로컬 8개 실행 파일의 일치 검사·미완성/실패 결과 분류, Docker 내부 10개 검사. 실제 image build·native 연결은 미확인 |
| GPU 컴퓨터에서 확인할 것 | Image build와 transitive dependency resolution, payload checksum, CUDA device·EGL image, model restore, IK/control, 단일 dev 결과 |
| 아직 구현하지 않음 | 임의 k개/비대상 제외/최종 안정 집합 evaluator, Q1–Q8 native task, 동일 상태 대조군·효과 비교·독립 holdout |

<a id="execution-다른-컴퓨터의-환경-설정"></a>
### 다른 컴퓨터의 환경 설정

- 사용자 선택 컴퓨터의 **로컬 Linux x86-64 Docker + NVIDIA Container Toolkit**, CUDA12 호환 driver와 `compute,graphics,utility` 지원이 필요하다. [JAX 공식 안내](https://docs.jax.dev/en/latest/installation.html#nvidia-gpu)의 CUDA12 driver 기준은 Linux 525 이상이지만, 이것만으로 이 고정 JAX 0.5.0 recipe의 실제 실행을 보장하지 않는다. Container 안의 JAX 장치 확인과 EGL 렌더가 최종 확인이다. 이 packet은 host driver/toolkit를 설치하지 않는다.
- 계획 자원은 GPU VRAM 24 GiB·RAM 32 GiB·Docker 저장공간 여유 100 GiB다. **측정된 최소 사양이 아니며** image/asset 크기와 peak memory는 첫 실행에서 기록한다. Checkpoint의 선택된 29파일은 공개 metadata 합계 12,014,184,286 bytes다. 대형 학습 데이터·optimizer/train_state는 받지 않는다. Asset archive 크기는 미확인이다.
- Python 3.11.13. Simulator: MuJoCo 3.2.2, dm_control 1.0.22, NumPy 1.25.0. 정책 서버: 별도 venv의 upstream `uv.lock`, JAX 0.5.0/CUDA12. NumPy 요구가 다른 두 환경을 합치지 않는다.
- `MUJOCO_GL=egl`, `PYOPENGL_PLATFORM=egl`, `CUDA_VISIBLE_DEVICES=0`, `MUJOCO_EGL_DEVICE_ID=0`, `NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility`. Host DISPLAY/X11 mount·외부 API key·원격 inference server는 사용하지 않는다.
- GPU 선택은 `SET_GPU_DEVICE=0` 기본값이며 다른 장치면 한 숫자로 지정한다. 실제 할당된 GPU의 UUID/driver/VRAM은 결과에 기록한다. Native 단계는 `--network none`이고 server/client가 같은 container의 loopback으로 통신한다.

<a id="execution-재개-명령"></a>
### 재개 명령

이 폴더와 연결 문서가 포함된 Git revision을 clone하고 저장소 루트에서 실행한다. 현재 dirty worktree를 clone한 것으로 가정하지 않는다. 준비 파일을 실제로 포함한 revision인지 먼저 확인해야 한다.

```bash
sh "work/research_topics/object_set/재현 방법/resume.sh" check
sh "work/research_topics/object_set/재현 방법/resume.sh" gpu
sh "work/research_topics/object_set/재현 방법/resume.sh" build
sh "work/research_topics/object_set/재현 방법/resume.sh" assets
sh "work/research_topics/object_set/재현 방법/resume.sh" smoke
sh "work/research_topics/object_set/재현 방법/resume.sh" results
```

한 단계가 실패하면 후속을 실행하지 않는다. Check는 read-only 자원 확인이며 성공해도 GPU/EGL 통과를 뜻하지 않는다. Build는 이미지 내부에서만 source와 dependency를 설치한다. Sim의 transitive lock은 아직 풀지 않았으며 첫 build의 `sim-resolved.txt`와 image digest·package freeze를 결과에 보존한다. Recipe의 구문 검사는 dependency 해결이나 native 성공을 대신하지 않는다.

Build는 Dockerfile·launcher·requirements·plan·artifact 목록·두 실행 Python 파일·검사 모듈의 SHA256을 `recipe_sha256.json`에 남긴다. `assets`/`smoke`는 현재 폴더를 읽기 전용으로 연결해 image 안의 8개 파일과 비교하며, 하나라도 바뀌거나 빠졌으면 volume 생성 전에 중단한다. 수정 후에는 `build`부터 다시 실행한다. 이 검사는 recipe 일치만 확인하며 dependency/ABI 적합성을 보장하지 않는다. `results`는 이전 실행의 당시 결과를 읽을 수 있도록 이 검사를 요구하지 않는다.

Assets는 `paper-object-set-p0-data` volume의 `/data/checkpoint`, `/data/assets`, `/data/openpi-cache`, `/data/archives`에 저장한다. Git에 포함된 기본 자산과 두 공식 Drive archive를 조합한다. 공식 archive의 고정 checksum은 공개 source에서 확보하지 못했으므로 **최초 다운로드의 SHA256을 봉인하고 이후 같은 파일인지 검증**한다. 이는 논문 출판 당시 archive와 같다는 증거가 아니다. Archive와 checkpoint 다운로드·압축 해제·검증은 모두 Docker 내부다. 기존 receipt가 있으면 덮어쓰지 않는다.

Smoke는 단일 attempt만 허용하며 자동 재시도하지 않는다. `paper-object-set-p0-runs`의 `/runs/attempt-1/`에 runtime/단계 실패, source 계획, package 목록, 최초 관측 그림·physics state, action trace, 종료 조건·최종 그림을 남긴다. Runtime 오류와 task 실패를 합산하지 않는다. Container는 종료 후 제거되고 image/volume은 재개 자산으로 남는다. 다른 task의 image/volume은 변경하지 않는다.

<a id="execution-고정된-공개-경로와-주요-수정"></a>
### 고정된 공개 경로와 주요 수정

1. VLABench `cf588fe6…`의 submodule `c0b0bd4b…`에는 선택 checkpoint의 `pi0_ft_vlabench_primitive` config가 없다. [모델 카드](https://huggingface.co/VLABench/pi0-primitive-10task)가 가리킨 저자 fork의 `4483d1da…`를 별도로 고정했다. 카드의 shell script 경로는 해당 revision에서 404이며, 실제 존재하는 `scripts/serve_policy.py`에 config와 checkpoint root를 명시한다. Default VLABENCH 모드는 다른 checkpoint 경로를 가리키므로 사용하지 않는다.
2. 공개 model root에 `params/`와 `assets/`가 있다. 카드 예시의 `/29999`를 경로에 임의 추가하지 않는다. Normalizer는 같은 model revision의 `assets/vlabench/vlabench_ft_primitive/norm_stats.json`, SHA256 `333f238a…`다. Libero나 구형 LoRA 통계를 재사용하지 않는다.
3. 현 fork는 front·right·wrist **세 이미지**와 7차원 EE state를 받는다. 구버전 두 이미지 adapter는 쓰지 않는다. [현 adapter](https://github.com/Shiduo-zh/openpi/blob/4483d1da6332da44115fe530e4e6fdd89bd57b13/examples/vlabench/eval.py)의 camera index 2/0/3, robot offset, absolute action과 gripper threshold를 따른다. Pose slice는 copy하여 관측 원본을 변경하지 않는다.
   - 고정 [Franka source](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/robots/single_arm/franka.py)의 `get_ee_open_state`는 두 finger qpos가 0.035 미만일 때 True를 반환하며 upstream BUG 주석이 있다. 이름만 보고 ‘열림’으로 해석하지 않는다. Checkpoint 입력을 임의 반전하지 않고 원래 raw flag와 초기 EE state를 기록한다. 학습 당시 규약·물체 release는 별도 확인 대상이다.
4. Track 1의 앞 세 `select_fruit` 장면에는 task config상 unseen 과일 distractor가 있다. 결과를 보지 않고 **모든 과일 category가 seen인 첫 장면 index 3**을 골랐다. Pear/orange/apple·plate_seen이며 mesh instance 자체의 학습 노출은 확인하지 못했다. 공개 평가 장면을 dev로 사용했으므로 독립 test로 재사용하지 않는다.

<a id="execution-실행-한도와-해석"></a>
### 실행 한도와 해석

- **1 checkpoint·1 scene·1 rollout**; scene seed 7, 정책 RNG는 upstream 기본 0. Replan 5, 최대 200 policy/control step·40 inference. 출력 chunk 50×7 중 첫 5개만 사용한다. Step당 `env.step` 1회다.
- `load_env`의 reset을 재사용하며 추가 reset하지 않는다. `reset_wait_step=10`은 source상 두 settling loop, 명시적 초기화 step 20회다. Source의 control/physics 비는 100이며 실제 timestep과 초기화 sim time을 기록한다. 200 control step을 MuJoCo physics tick 200회나 정확한 wall time으로 해석하지 않는다.
- Server 시작 대기 최대 300초, 자산 검증 이후 precheck·server·native 전체 실행 예산 900초. 한 번의 bounded 실패 뒤 checkpoint/scene sweep이나 학습을 자동 수행하지 않는다.
- IK 실패·non-finite/IO mismatch는 즉시 중지한다. 이는 upstream이 IK flag를 무시하는 것과 다르며 benchmark 성공률 재현을 주장하지 않는다.
- IK 실패는 nonzero 종료와 `IK_FAILURE`로 남긴다. Runtime은 exit code만으로 통과시키지 않고 probe 상태와 native condition의 일관성을 검사한다. 조건 없이 정상 terminal에 도달하거나 step 예산을 소진한 경우는 완료 rollout 1회·containment 미관측이며, IK/실행 오류·결과 누락은 완료로 세지 않는다. 어느 경우도 연구 효과 검증으로 승격하지 않는다.
- `timestep.last()`와 `task.conditions.is_met`를 따로 기록한다. Native containment는 물체 기준점의 첫 진입일 수 있다. **release·안정 유지·비대상 제외·최종 집합 성공은 미검증**으로 출력한다. 1회 결과를 성공률 추정·원인 확인·새 방법의 효과로 확대하지 않는다.

다음은 호환 local Docker의 최소 실행이다. 성공하면 최초/최종 영상과 trace를 확인해 제한된 후속 비교를 설계하고, 실패하면 자원·설치·관측/제어·task 실패 중 어느 단계인지 먼저 구분한다. 기존 REVISION 우선순위와 HANDOFF 및 과거 후보의 과학적 gate는 바뀌지 않는다.

<a id="preparation-history"></a>

<a id="preparation-history-실제로-보완한-재개-코드"></a>
### 실제로 보완한 재개 코드

| 발견한 문제 | 수정·경계 |
|---|---|
| Plan의 `max_rollouts_authorized=2`가 실제 1회 launcher·문서와 불일치 | 1로 일치시켰다. 1 checkpoint·공개 dev index 3·200 control step·40 inference·자동 retry 금지 유지 |
| 준비 파일 수정 후 이전 image로 assets/smoke를 실행할 수 있음 | Build 때 실행 recipe 8파일을 SHA256으로 봉인. 실행 전 현재 파일과 비교해 오래된 image·누락 파일을 거부. 실제 target image build는 아직 하지 않음 |
| IK 실패가 client exit 0으로 끝나 정상 완료처럼 보일 수 있음 | `IK_FAILURE`를 보존하며 nonzero 종료. Runtime은 결과 상태·native condition도 검사하며 누락/알 수 없는 상태/모순은 실패로 남김 |
| 정상 terminal이지만 condition=false인 rollout이 완료 수에서 빠짐 | 기술적 완료 수와 containment 관측을 분리. 이 terminal과 budget exhaustion은 완료 1회·containment 미관측, IK/runtime failure는 미완료 |
| State의 gripper flag를 ‘열림’으로 부를 근거 부족 | [고정 Franka source](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/robots/single_arm/franka.py)는 finger qpos<0.035를 True로 반환하고 BUG 주석을 포함한다. Raw convention을 유지하고 초기 EE state를 저장하며 release 판정에 재사용하지 않음 |

고정 [IK interface](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/robots/single_arm/base.py), [환경 관측/파지 조회](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/envs/dm_env.py), [policy client](https://github.com/Shiduo-zh/openpi/blob/4483d1da6332da44115fe530e4e6fdd89bd57b13/packages/openpi-client/src/openpi_client/websocket_client_policy.py)와 server entry도 공개 text로 대조했다. Source는 읽기 검토만 했으며 패키지나 upstream source tree를 host에 설치하지 않았다. Gripper 입력의 부호를 바꾼 것이 아니며 학습 데이터 규약을 새로 검증한 것도 아니다.

<a id="preparation-history-수행한-검사와-수행하지-않은-검증"></a>
### 수행한 검사와 수행하지 않은 검증

기존 ARM64 Python image를 변경 없이 사용하고 network none·저장소 read-only·임시 tmpfs인 Docker container에서 [준비 코드 검사](test_packet_checks.py) **10개를 통과**했다. 오래된 image, image 내부 파일 변경, clone 파일 누락, IK 실패의 zero exit, stale 성공 JSON과 nonzero exit, 결과 누락/모순, 정상 실패 rollout의 분모와 실행 예산을 검사했다. 이 과정은 표준 라이브러리의 파일 hash·결과 분류 검사이며 **CPU 정책 대체 실험·simulation·성능 측정이 아니다**.

검사 container는 종료 후 제거했다. 새 image·volume·host dependency·checkpoint/asset payload는 없고 기존 사용자 image와 minikube volume은 보존했다. Native 전용 image의 dependency 해결·source import·CUDA/EGL·실제 controller·model load는 여전히 미검증이다.
