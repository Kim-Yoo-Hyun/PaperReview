# 능동 자세 추정 재현

Updated: 2026-11-17 KST. **N1/N2 내부 비실험 검토 완료, P0 준비 코드 작성 / PREPARED_UNEXECUTED.** [질문·선행·네 사례](../내용/README.md) · [공통 source ledger의 pose_active_n1 / pose_active_n2 / pose_active_p0_preparation](../../../sources/new_field_scout_2026-11-17.json). 현재 launcher는 로컬 daemon 연결 실패로 중단됐다. Docker recipe와 제한된 scene/IO probe는 작성했지만 image build·Docker 검사·native 호환은 미검증이다. 아래 N1/N2는 당시 설계 이력이며 최신 구현 범위는 [P0 준비](#p0-preparation)가 소유한다. 파일별 source/hash·확인 범위는 원장에 남기고 읽기용 임시 사본은 제거한다.

<a id="n1-source-audit"></a>
## N1 — source 수준의 확보·미구현 경계

아래 revision은 **서로 독립적인 source 감사 기준**이다. 함께 설치되는 환경 lock이나 호환성 확인이 아니다. 특히 l2l README의 robosuite pin과 아래 robosuite revision은 다르다.

| 자원·revision | 실제 확인한 경로 | 재사용 판단·추가 구현 |
|---|---|---|
| FoundationPose `a1b694b83e633c2cb6115b9063d940a687759392` | [estimater.py register/track_one](https://github.com/NVlabs/FoundationPose/blob/a1b694b83e633c2cb6115b9063d940a687759392/estimater.py#L159): 정렬된 `self.poses`·`self.scores` 보존, 반환값은 best pose. [predict_score.py](https://github.com/NVlabs/FoundationPose/blob/a1b694b83e633c2cb6115b9063d940a687759392/learning/training/predict_score.py#L161)는 순위 score | 다중 후보 export는 가능하다. 다만 `self.poses`는 centered mesh frame이고 반환 best pose는 원 mesh frame이므로 **모든 후보에** `get_tf_to_centered_mesh()`를 적용한 뒤 camera→base 변환해야 한다. Score를 posterior로 사용하지 않음. Invalid depth 조기 반환 때 stale 후보를 금지할 valid flag, symmetry·후보 coverage·관측 간 갱신 필요. `track_one`은 단일 pose 추적 |
| Learning to Look / DISaM `37382315d4e262d381862752931fe7445c2a0594` | [image_model.py](https://github.com/UT-Austin-RobIn/l2l/blob/37382315d4e262d381862752931fe7445c2a0594/l2l/modules/image_model.py#L224): context 샘플의 categorical/GMM action 분포 간 KL. [policy_wrappers.py](https://github.com/UT-Austin-RobIn/l2l/blob/37382315d4e262d381862752931fe7445c2a0594/l2l/wrappers/policy_wrappers.py#L60): encoded privileged feature 교체 | 원시 행동 분산과 구별할 comparator를 확인했다. Pose matrix를 이 feature나 VLA에 바로 연결할 수 없다. Source의 task별 threshold도 새 task에 보정된 값이 아님. 원본 재현과 VLA 이식 comparator를 구별해야 함 |
| 같은 l2l의 camera/task | [walled_multi_stage.py rotate_camera](https://github.com/UT-Austin-RobIn/l2l/blob/37382315d4e262d381862752931fe7445c2a0594/l2l/envs/robosuite/walled_multi_stage.py#L704), [two_arm.py](https://github.com/UT-Austin-RobIn/l2l/blob/37382315d4e262d381862752931fe7445c2a0594/l2l/envs/robosuite/two_arm.py#L648): pan/tilt/위치 변경 뒤 관측 | `CameraMover.set_camera_pose`로 시점을 바꾸며 해당 함수 안에서 실제 카메라 actuator 경로/이동 시간이 구현되는 것은 아니다. 색상 region/peg 선택 성공 조건도 새 pose 사례가 아님. Depth 기본 비활성·history 입력·물리 이동 비용 별도 확인 필요 |
| SpatialVLA `18fd74b2a633ec8d9ec7aadcd803969555cc9fbd` | [modeling_spatialvla.py](https://github.com/SpatialVLA/SpatialVLA/blob/18fd74b2a633ec8d9ec7aadcd803969555cc9fbd/model/modeling_spatialvla.py#L308): depth→K 기반 camera XYZ→3D embedding+vision feature. `forward` hidden states 선택 가능. [processing_spatialvla.py](https://github.com/SpatialVLA/SpatialVLA/blob/18fd74b2a633ec8d9ec7aadcd803969555cc9fbd/model/processing_spatialvla.py#L186): intrinsics 선택·action 복원 | Pose belief·camera action 입력은 없다. `predict_action` 기본 `do_sample=False`여서 반복 호출만으로 다양한 후보가 생기지 않는다. Decoder는 첫 generation을 사용하므로 다중 후보 decoding/재채점 adapter 필요. q01/q99·mask·action frame·데이터셋별 intrinsic을 확인해야 함. 기존 depth 추론은 `no_grad`; 후보 2의 **frozen depth 개입** 지점은 있으나 geometry 공동 학습 경로는 별도 변경 필요 |
| RFMPose — 공식 repo 이름은 **RMFPose**, `cc0d955645e590f10ac16d7bea514bbbfdccfccb` | [posenet_agent.py pred_func](https://github.com/shabiouyang/RMFPose/blob/cc0d955645e590f10ac16d7bea514bbbfdccfccb/networks/posenet_agent.py#L481), [evaluation_fm.py](https://github.com/shabiouyang/RMFPose/blob/cc0d955645e590f10ac16d7bea514bbbfdccfccb/runners/evaluation_fm.py#L143): 반복 생성 후보를 보존한 뒤 선택/평균 | 다중 생성의 대안. 검토한 evaluation 경로의 optional energy/균등 score를 calibrated likelihood라 부를 수 없다. README·eval script에서 checkpoint 다운로드를 식별하지 못했고 script에는 절대 경로가 있음. 프로젝트 전체의 likelihood 구현 부재·weight 미공개를 단정하지 않음 |
| robosuite `5ce6643f3092639d08f7b0f90ed1c6a84f50552c` | [NutAssemblySquare](https://github.com/ARISE-Initiative/robosuite/blob/5ce6643f3092639d08f7b0f90ed1c6a84f50552c/robosuite/environments/manipulation/nut_assembly.py#L700), [square-nut.xml](https://github.com/ARISE-Initiative/robosuite/blob/5ce6643f3092639d08f7b0f90ed1c6a84f50552c/robosuite/models/assets/objects/square-nut.xml), [camera_utils.py](https://github.com/ARISE-Initiative/robosuite/blob/5ce6643f3092639d08f7b0f90ed1c6a84f50552c/robosuite/utils/camera_utils.py#L291) | Pose sensor·handle/box collision geometry·camera K/extrinsic API 존재. 그러나 `on_peg`는 x/y/z 위치 범위, `_check_success`는 여기에 EEF 이격을 추가한다. 명시적 yaw/contact 성공 판정이 아니다. 물리 충돌이 방향을 제약하는지는 실행 확인 필요. 손잡이가 있어 완전 대칭 물체가 아니며 초기 가림은 별도 구성. Mocap 시점 변경은 물리 카메라 제어가 아님 |
| EyeRobot 2.0 `c5f21cc7f3fa166395bda862745de955f16932e4` | [공식 repo README](https://github.com/kerrj/eyerobot2/tree/c5f21cc7f3fa166395bda862745de955f16932e4), [project](https://eyerobot2.github.io/) | 확인 당시 tree는 README만 있고 code/data 예정 표기. 고정 stereo의 gaze/foveation 방법을 실제 카메라 이동 comparator로 쓰지 않음 |

SaPaVe·ATAP·Naik·ActiveAlign은 이번에 본 공식 project/지정 본문에서 실행 release를 식별하지 못했다. 논문 기반 comparator 설계와 실행 가능한 원 코드 확보는 구별한다. RFMPose README의 Ubuntu20.04/Python3.10.14/PyTorch2.1.0/CUDA11.8은 **그 프로젝트 설명**이며 본 후보의 확정 환경이 아니다. 모든 weight·라이선스 간 호환·native IO는 아직 검증하지 않았다.

## 입출력과 비교 계약의 초안

1. **관측:** RGB/depth·intrinsic·camera-to-base·시각/robot state·언어·시간 stamp. 알려진 CAD/reference·object mask를 쓰는 최초 범위라면 모든 비교군의 정보량을 맞춘다. 새 관측이 기존 posterior에 반영되는 association/history cache는 미구현이다.
2. **Pose 집합:** 원 mesh 기준 camera/object 변환과 base/object 변환을 구별하고 symmetry·valid mask·candidate coverage를 기록한다. 초기에는 calibrated posterior를 주장하지 않는 유한 집합 비교도 가능하다. Top-K 밖 정답을 가설 내 높은 confidence로 숨기지 않는다.
3. **행동 후보:** 모든 pose 가설에서 **같은 base-frame 물리 행동과 같은 continuation**을 실행했을 때 성공하는지 정의한다. 가설별 object frame으로 행동을 재변환하면 서로 다른 행동이 되어 공통 성공 표가 아니다. 후보에 공통 행동이 없다는 사실만으로 실제 공통 해가 없다고 결론내리지 않는다.
4. **정답 경계:** 후보×pose 성공 표는 simulator/teacher 평가용이다. Test-time에는 실제 pose·성공 정답을 정책에 전달하지 않는다. Compatibility head·분리 classifier·허용 오차 lookup은 같은 label/학습 예산으로 비교한다. Candidate 생성 확률과 행동 성공 확률은 다른 값이다.
5. **관측 행동:** 최초에는 같은 고정 view 순서에서 stop/continue만 비교할 수 있다. Learned next-best-view까지 동시에 구현할 필요는 없다. Camera teleport는 관측 진단으로만 표시하고 실제 wrist 이동은 joint/approach 상태·시간·복귀·충돌 비용을 포함한다. ActiveAlign식 view-aligned SFT 효과도 통제한다.

<a id="n2-contract"></a>
## N2 — 최소 비교 계약 (2026-11-17)

**DONE_NONEXPERIMENTAL / executable=false.** 아래는 선택한 설계이며 source가 이미 이 기능을 구현했다는 뜻이 아니다. N1의 source pin을 유지하고 추가 7개 source/config 및 Hugging Face 설정·remote code 8개를 확인했다. 이번 N2에서 읽은 repository 파일은 재확인 포함 20개다. 파일별 hash와 지정 읽기 범위는 공통 원장 `pose_active_n2`에 둔다. 다음은 같은 문헌 검토를 반복하는 N3가 아니라 작은 **P0 구현 준비**다.

### 1. 선택한 모델·task와 미확보 자산

| 항목 | N2 선택 | 확인 수준·차단 조건 |
|---|---|---|
| VLA | SpatialVLA 4B, GitHub source는 N1 pin. 초기 weight 후보 [IPEC-COMMUNITY/spatialvla-4b-224-pt](https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt/tree/886c4557dfde53b44c0f74fde7d89bf83a26c3cd), revision `886c4557dfde53b44c0f74fde7d89bf83a26c3cd` | Weight **미수신·미실행**. HF의 processor/tokenizer source는 GitHub와 byte 일치, model/config source는 module docstring 차이만 확인. 이는 weight 로딩 성공 증거가 아님 |
| 실제 processor 설정 | [고정 설정](https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt/blob/886c4557dfde53b44c0f74fde7d89bf83a26c3cd/processor_config.json): 관측 1장, chunk 4, 동작당 translation/rotation/gripper 3토큰 → chunk 12토큰 | N1의 class 기본값 1-step을 이 checkpoint의 chunk 길이로 사용하지 않음. Intrinsic preset은 bridge/default뿐이며 여러 dataset의 action stats가 Panda 새 과제와 호환된다는 뜻도 아님 |
| 환경·로봇 | robosuite N1 pin의 Panda/OSC_POSE 및 SquareNut geometry로 **새 배치 task** 구성 | 원 NutAssembly 성공률과 비교하지 않음. Peg insertion은 첫 범위에서 제외. Target patch·가림 구조·view fixture·배치 evaluator는 **미구현** |
| 언어 쌍 | 같은 장면에서 `Place the nut on the marked area.` / `Place the nut on the marked area with its handle pointing toward the arrow.` | Target/arrow는 두 지시 모두 같은 곳에 보임. 정확한 CAD의 handle 방향이 있으므로 90/180도 대칭을 임의로 동치 처리하지 않음. 실제로 첫 시점에서 가려지고 다른 시점에서 식별되는지는 rendering으로 확인해야 함 |
| 적응 데이터·정규화 | 새 task의 공통 SFT/통계가 필요할 수 있음. 키 `pose_active_panda_v1`은 **예약 이름일 뿐 현재 없음** | Training split에서만 action q01/q99·mask·camera K를 만들고 모든 비교군에 공유. Bridge/Fractal stats를 임의 대입해 Panda competence를 주장하지 않음. 새 시연·SFT checkpoint 미확보 |

[공식 SimplerEnv adapter](https://github.com/DelinQu/SimplerEnv-OpenVLA/blob/ccfe3809766839a2fcfb7a3d3c9abff585189188/simpler_env/policies/spatialvla/spatialvla_model.py)는 WidowX/Google 경로, action ensemble·sticky gripper·Euler→axis-angle 변환을 가진다. 이를 Panda에 그대로 이식하지 않는다. 초기 실험은 새 controller/normalizer를 검증한 뒤에만 VLA 명령을 보낸다. 공개 pretraining weight는 이 task의 baseline competence 인증이 아니다.

### 2. 행동 후보와 재채점

**선택:** 같은 현재 RGB·언어로 만든 후보 집합을 모든 비교군에 공유한다. 첫 진단의 상한은 후보 4개(유효한 원 greedy 1개 포함), pose 4개, 관측 3장이다. Greedy도 기본 wrapper의 최대 256토큰을 전부 생성하지 않고 동일 decoding 설정으로 필요한 첫 12토큰까지만 생성한다. 제약 sampling은 최초 temperature=1/top-p=1/top-k 해제, 최대 3회 제안으로 고정하고 중복이면 후보 수를 줄인다. P0 seed=0, 초기 attention은 eager 경로로 고정할 설계다. 이는 최적 hyperparameter·호환 환경 lock·실행 완료 수치가 아니다. 원 greedy 결과와 제약 생성 결과를 구별해 기록한다.

- 새 proposal adapter는 `predict_action` 대신 12개 suffix token을 제한적으로 생성한다. 3토큰 주기의 각 위치에 해당 translation/rotation/gripper vocabulary만 허용한다. Sampling seed·temperature·mask를 저장하고 중복 candidate를 제거하되 무한 재추출하지 않는다. 불완전 suffix·범위 밖 token·NaN은 `INVALID`, 실패 행동 label로 위조하지 않는다. 원 decoder의 token clipping/짧은 출력 zero-padding에 의존하면 오류가 정상 행동으로 바뀌므로 **decode 전에 검사**한다. 근거: [action_tokenizer.py](https://github.com/SpatialVLA/SpatialVLA/blob/18fd74b2a633ec8d9ec7aadcd803969555cc9fbd/model/action_tokenizer.py#L121), [processor](https://github.com/SpatialVLA/SpatialVLA/blob/18fd74b2a633ec8d9ec7aadcd803969555cc9fbd/model/processing_spatialvla.py#L216).
- 각 candidate는 `[1,12]`로 별도 decode한다. 원본 token ID·normalized 4×7·unnormalized 명령·controller 명령을 모두 남긴다. 서로 다른 token이 같은 명령으로 clipping되면 별도 물리 후보로 세지 않는다. Log probability는 **token sequence의 확률**이며 continuous action density가 아니다.
- 재채점은 원 candidate token을 prefix 뒤에 **순차 강제 입력**하며 각 다음 토큰의 조건부 log probability를 더하는 경로로 정한다. 원시 vocabulary 확률과 제약 mask 적용 확률은 별도 저장한다. 전체 candidate suffix를 한 번에 넣고 `labels=None`인 logits를 읽는 방식은 금지한다. [모델의 mask 분기](https://github.com/SpatialVLA/SpatialVLA/blob/18fd74b2a633ec8d9ec7aadcd803969555cc9fbd/model/modeling_spatialvla.py#L263)는 일반 inference의 여러 입력 토큰을 prefix처럼 처리할 수 있어 미래 suffix 누출 위험이 있다. Cache/attention 구현을 고정하고 생성 때의 점수와 forced replay 점수가 맞는지는 native P0에서 확인한다. 현재 동일성 미검증이다.
- Head용 `h`는 **candidate·정답 pose를 붙이기 전** RGB/언어 prefix의 마지막 유효 위치 hidden state다. Pose/action embedding을 head에 별도로 주며 true pose·성공 label을 prompt에 넣지 않는다. 원 SpatialVLA에는 pose 조건 입력이 없으므로 같은 prefix를 복사한 `p(a|o,l)`를 `p(a|o,l,T_i)`라 부르지 않는다.

**물리 명령:** 선택한 chunk의 4개 명령을 끝까지 실행한 뒤 공통 continuation 정책으로 재관측·재계획한다. 매 1-step 재계획으로 바꿨다면 다른 비교로 기록한다. 새 데이터 convention은 base-frame translation delta(m), base-frame left-multiplied rotation increment의 Euler XYZ(rad), open fraction으로 명시하고 학습/역변환에 똑같이 사용한다. Controller에는 Euler→rotation matrix→rotation vector를 거쳐 넣는다. [OSC 설정](https://github.com/ARISE-Initiative/robosuite/blob/5ce6643f3092639d08f7b0f90ed1c6a84f50552c/robosuite/controllers/config/default/parts/osc_pose.json)의 translation 0.05m/rotation 0.5rad scaling을 역으로 적용하고, 초과 명령은 숨겨 clipping하지 않는다. Gripper 방향은 asset에서 open/close를 확인한 뒤 변환한다. Control rate는 새 task/SFT 데이터에서 20Hz, goal 갱신은 achieved pose 기준으로 정한 설계다. 이때 4-step은 0.2초이고 inference 지연은 별도다. Base/world·goal 모드는 [OSC source](https://github.com/ARISE-Initiative/robosuite/blob/5ce6643f3092639d08f7b0f90ed1c6a84f50552c/robosuite/controllers/parts/arm/osc.py#L306)를 기준으로 고정한다. 이것은 새 task용 convention이며 OXE 전체가 같다는 주장도 아니다.

### 3. Pose 집합·관측 이력

관측 중에는 물체가 정지한 강체라고 제한한다. `T_A_B`는 B좌표를 A로 옮기는 변환이다. FoundationPose의 centered 후보를 원 mesh frame으로 복원해 `T_base_obj = T_base_cam × T_cam_centered × T_centered_obj`를 만든다. Camera extrinsic의 CV 축 보정·depth buffer→m·RGB/depth 수직 방향·resize K를 함께 검증한다. [robosuite camera API](https://github.com/ARISE-Initiative/robosuite/blob/5ce6643f3092639d08f7b0f90ed1c6a84f50552c/robosuite/utils/camera_utils.py#L39)는 이미 축 보정을 하므로 무조건 두 번 뒤집지 않는다.

초기 baseline은 **posterior가 아닌 유한 pose 집합**이다. 새 view에서 registration 후보와 기존 base-frame 후보를 합치고, 동일 world pose를 각 과거 camera frame으로 옮겨 [공개 scorer](https://github.com/NVlabs/FoundationPose/blob/a1b694b83e633c2cb6115b9063d940a687759392/learning/training/predict_score.py#L161)에 다시 넣는 adapter를 만든다. Scorer에 FoundationPose의 centered mesh를 주면 pose도 `T_cam_centered = T_cam_obj × inverse(T_centered_obj)`로 되돌려야 한다. View마다 같은 union 안에서 순위를 구해 평균 순위로 상위 K를 유지하는 단순 rule을 먼저 쓴다. Calibrated likelihood/Bayes update로 부르지 않는다. Scorer의 입력 집합 의존성 때문에 raw logit의 view 간 곱/합도 확률 갱신이 아니다.

유효 depth/mask가 없는 view는 증거에서 제외하고 `UNKNOWN`을 남긴다. Pose merging은 full object의 실제 symmetry·고정 거리 threshold를 사용하며 가려진 handle을 임의 symmetry로 삭제하지 않는다. 정답 pose의 후보 내 거리/coverage는 evaluator에서만 기록한다. 정답이 빠진 결과를 삭제해 성공률을 높이지 않는다. GT segmentation을 최초 진단에 쓴다면 `ORACLE_MASK` 조건으로 모든 비교군에 동일 제공하고 현실 segmentation 성능으로 일반화하지 않는다. 로봇이 물체에 접촉한 뒤에는 이 static update를 계속 쓰지 않는다.

History는 `(RGB, depth, K, T_base_cam, time, robot state)` 목록과 pose set 갱신에만 먼저 쓴다. 원 checkpoint는 1장 입력이므로 history 전체를 이미 이해한다고 가정하지 않는다. Head에 history feature pooling을 추가할 때는 별도 classifier도 같은 이력을 받는다.

### 4. 성공 판정·counterfactual label

**새 evaluator의 정의:** `PLACE`는 object collision footprint가 target patch 안에 들어가고, table support·gripper release·EEF 이격·낮은 속도가 dwell 동안 유지되는 조건이다. `ALIGN`은 PLACE에 `handle_site − center_site`의 table-plane 방향과 화살표 방향 사이 각도 오차 조건을 추가한다. 수치 tolerance는 mesh·sensor/physics 검증 뒤 calibration split에서 고정하며, final test 성능에 맞춰 바꾸지 않는다. 위치만 맞고 아직 들고 있는 상태·지나가며 영역을 통과한 상태·뒤집힘·접촉 중 흔들림·잘못된 handle 방향을 evaluator 음성 사례로 둔다. 기존 `on_peg`를 재사용한 성공 label이 아니다. 초기에는 삽입이나 접촉 정밀도 개선으로 주장하지 않는다.

`Y_ij = success(a_j[4 steps] → π_cont, object pose T_i)`로 정의한다. Robot state/controller/history/RNG와 target/occluder는 고정하고 object pose만 바꾼 counterfactual branch를 구성한다. 모든 행에서 **같은 base-frame 명령열**을 쓰되 contact 이후 실제 trajectory까지 같다고 가정하지 않는다. Continuation은 같은 checkpoint·언어·view schedule과 종료 시간으로 동결하고 실제 branch 관측에 반응한다. 정답 pose를 continuation에 넣지 않는다. 뒤의 정상 feedback만으로 모호성이 해소되어 공통 성공 행동이 있다면 그것도 유효한 단순 해법이다.

초기 pose 교체가 interpenetration·동역학 불안정·관측 불일치를 만들면 `INVALID_COUNTERFACTUAL`이며 실패0과 구별한다. 초기 가림에서 정말 서로 구별하기 어려운지와 다음 view에서 구별되는지는 rendering/registration 결과로 따로 확인한다. Counterfactual label은 simulator 가정하의 값이고 실제 episode의 true-state success와 별도다. Full reset은 qpos뿐 아니라 qvel/actuator/controller goal·gripper latch·관측 cache·policy cache·RNG까지 포함한다. 복원 검증 전 paired causal effect를 주장하지 않는다.

한 chunk와 특정 continuation에서 실패했다고 모든 가능한 정책에 공통 해가 없다는 뜻은 아니다. 여러 번 실행해 얻은 성공 빈도도 이 task/controller/continuation 조건부다. 따라서 보고 단위는 이미지 frame이나 후보 수가 아니라 **원 장면 family × instruction**이다. 같은 scene의 pose/view/candidate branch는 같은 train/calibration/test split에 묶는다. 최초 한 mesh 실험에는 unseen-object generalization 주장을 붙이지 않는다.

### 5. 비교군과 학습의 경계

| 비교 | 같은 것으로 맞출 것 | 이 비교로 알 수 있는 것 |
|---|---|---|
| 고정 1-view / 최대 view / 고정 개수 view | 동일 후보 생성기·continuation·task 데이터, 같은 최대 관측 상한 | Active stopping 자체의 이득. Max-view가 잘하면 추가 관측 필요성이 사라진 것은 아님; 비용과 함께 판단 |
| Pose spread·task-axis tolerance rule | 동일 추정 pose set·CAD·history·view 순서 | 새 classifier 없이도 충분한지. 균등 가중 집합의 entropy를 calibrated posterior entropy라 부르지 않음 |
| Naik식 후보별 성공 lookup | 같은 학습용 rollout/label 예산으로 만든 lookup·기하학적 approximation | Learned compatibility의 일반화/계산 절약 필요성. Test pose에서 완전 physics rollout을 하는 lookup은 **oracle 상한**으로 분리하고 배포 비교에서 제외 |
| Candidate-conditioned BC의 KL/shared support | 같은 `h,T_i,A,Y`에서 성공한 후보의 정규화 분포를 학습. 성공 후보가 없는 row는 confidence fallback | 명시적 pose-conditioned 분포가 있어야 가능한 **DISaM-inspired 이식 comparator**. 원 DISaM 재현도 아니고 기존 SpatialVLA의 native 기능도 아님 |
| 독립 성공 head / 공유 VLA 표현의 성공 head | 같은 label·pose/history·candidate·학습/튜닝 예산, parameter·compute 보고 | Pose 정보나 추가 label만의 효과와 representation 공유의 효과를 분리 |

연구 변수는 `Cθ(h,T_i,a_j)`의 성공 예측과 VLA 표현 공유다. 첫 head는 binary success supervision으로 학습하고 `max_j min_i Cθ`와 validation threshold로 ACT/LOOK을 고른다. Min은 유한 가설 안의 보수적 rule일 뿐 안전 보증이 아니다. 마지막 view에서도 기준 미달이면 DEFER/실패로 기록하고 성공한 trial만 분모에 남기지 않는다. 낮은 KL이어도 후보가 모두 실패할 수 있어 KL comparator에도 동일한 예산 종료/실패 처리를 둔다.

Frozen VLA feature+외부 head는 **진단/모듈형 baseline**이다. 이후 공통 SFT loss와 compatibility loss로 같은 VLA adapter를 갱신하고 행동 변화·보존을 확인해야 공동 학습 주장으로 나아간다. Candidate set을 고정한 head 비교와 actor까지 변해 후보 분포가 달라지는 비교는 분리한다. 현재 양쪽 학습 코드·데이터 모두 없으며 RL이 반드시 필요하다는 근거도 없다.

### 6. 관측·시간·다음 구현 범위

첫 진단은 고정한 3개 view prefix에서 ACT/LOOK만 비교한다. View를 바꾸어 얻은 영상과 동일한 마지막 control view로 돌아온 영상을 구별하고, 모든 조건은 같은 robot 시작 상태에서 조작한다. 시점을 직접 바꾸는 최초 rendering 검사에는 실제 이동 시간을 가정해 붙이지 않는다. 이후 physical wrist path를 쓸 때 이동·복귀·dwell과 state 변화, 모델/pose 추론 wall time을 별도 측정한다. Synthetic camera lookup의 view 수 절약은 실제 로봇 시간 절약의 증거가 아니다.

**N2에서 정한 POSE-ACTIVE-P0-PREP 범위:** 로컬 Docker 조건을 확인하고, (A) custom scene/evaluator·camera/depth/frame/복원 검증, (B) pinned SpatialVLA loader·12-token 후보/순차 재채점·hidden feature 검증을 구현한다. 최초 최소 실행은 scene 1개·지시 2개·view≤2·pose≤2·candidate≤2, 전체 실행의 물리 제어≤20회/physics step≤10,000·autoregressive model step≤96·FoundationPose register≤1·학습/optimizer0으로 제한한다. Source의 register 내부 refinement 수와 실행 시간도 따로 기록한다. 이 상한은 task 성공률 시험이나 label dataset 구축 승인이 아니다. Candidate-specific continuation rollout은 다음 별도 pilot 범위다.

Task 정상화·명령 변환이 아직 없으면 B는 token/feature IO까지만 하고 VLA 명령을 물리에 보내지 않는다. A의 scripted controller 동작을 VLA competence로 세지 않는다. 첫 구현 산출물을 확인한 뒤 실제로 관측이 다른 성공 결정을 만드는 사례가 있는지 판단한다. 단순 baseline이 충분하면 질문을 수정할 수 있으나, 자원·기본 능력 미확인은 가설 반증이 아니다. 문헌·설계 검토는 현재 N2 범위로 마치며 추가 N3 문서 작업을 자동 생성하지 않는다.

## 이후 실행 조건

실험 요청 시 현재 컴퓨터의 **로컬 Docker** endpoint·daemon·architecture·NVIDIA allocation·CUDA/graphics를 새로 확인한다. 충족하면 확정한 P0만 Docker 안에서 실행하고, 충족하지 않으면 clone 후 재개 가능한 recipe와 실패 근거를 남긴다. Host package/weights/assets 설치나 host Python/MPS 추론은 하지 않는다.

N2 당시에는 image/launcher가 없었다. 아래 P0-PREP에서 recipe·launcher·제한된 probe를 작성했으며, clone 후 호환 NVIDIA 컴퓨터의 로컬 Docker에서 빌드·검사를 시작할 수 있다. **실행 성공을 검증한 패키지는 아직 아니다.**

<a id="p0-preparation"></a>
## P0 준비 결과 — 코드 작성과 실행 확인을 분리

**준비 완료 범위:** [PLAN.json](./PLAN.json), [Dockerfile](./Dockerfile), [의존성](./requirements.txt), [launcher](./resume.py), [scene·VLA probe](./probe.py), [제어 검사 10개](./checks.py)를 작성했다. Python 정적 컴파일은 실행했으며 Docker 검사는 실행하지 않았다. 이는 최초 interface 검증 준비이고 전체 ACT/LOOK 연구 방법의 구현 완료가 아니다.

**실제 확인 범위:** 2026-11-17 현재 host는 Darwin ARM64·16GiB, Docker CLI 28.3.3이다. `desktop-linux`의 로컬 Unix socket을 확인했으나 daemon 연결이 실패했다. 새 launcher의 `run` 호출도 [BLOCKED_DAEMON / exit 3](./results/preparation/local_check.json)에서 끝났다. 이 결과의 daemon 숫자 0/null은 연결 실패 시 반환값이며 실제 container/image 수나 RAM 측정이 아니다. GPU 할당·image build·제어 검사·native physics/정책 실행·학습은 모두 0이다. Host package/weights/assets를 설치하지 않았고 새 Docker 자원도 생성하지 않았다.

| 준비한 검사 | 실행 시 판정할 것 | 이 검사로 입증하지 못하는 것 |
|---|---|---|
| Scene·evaluator | SquareNut geometry, peg collision 제거, 공통 target/arrow·occluder. Collision footprint·실제 support contact force·gripper release/이격·upright/속도/dwell과 handle 방향 판정. Script로 배치한 0°/180° fixture 구별 | VLA의 집기/배치 성공, 원 NutAssembly 성능, pose ambiguity 사례의 성립. 수치 tolerance는 미보정 P0 기본값 |
| Camera·복원 | 두 고정 view의 RGB·metric depth·K·CV camera-to-world 저장, 실제 camera 기하의 projection roundtrip. Physics/controller/gripper/RNG 복원 뒤 같은 hold/open 3-step trajectory 대조 | 물리 카메라 이동, 관측에 따른 정보 이득, 모든 policy/observable history를 포함한 counterfactual 복원. Algebraic roundtrip만으로 depth/가림 품질을 보증하지 않음 |
| VLA IO | Pin/hash 확인→strict load→지시별 최대 2회 제안(12토큰)→family 검사·중복 구별→normalized 4×7 decode→prefix hidden feature·강제 순차 재채점 | `pose_active_panda_v1` normalizer·Panda 행동 능력·pose 조건 입력·학습 head. **VLA 출력은 simulator로 보내지 않음** |
| 제어 검사 10개 | Dwell/음성 fixture 조건·NaN/누락·잘못된 token·전역 예산 거부 | MuJoCo/CUDA/EGL·checkpoint 의미 호환. 현재는 검사 코드만 작성 |

VLA 재채점은 Transformers 4.47의 [generation loop](https://github.com/huggingface/transformers/blob/v4.47.0/src/transformers/generation/utils.py#L3267)와 [minimum-length processor](https://github.com/huggingface/transformers/blob/v4.47.0/src/transformers/generation/logits_process.py)를 대조했다. 생성 시의 raw logits를 in-place 변경하지 않는 mask를 쓰며, vocabulary log probability와 family 내 정규화 점수를 따로 저장한다. 점수 일치는 **native 실행 대기**다. 이 점수는 행동 성공 확률이 아니다.

FoundationPose는 N2의 선택 모델을 유지하지만 **이 P0 recipe에는 의존성·weights·registration을 넣지 않았다(register=0)**. 먼저 scene/카메라와 VLA IO를 나눠 확인한다. Centered-mesh 후보 변환·관측 간 rank 갱신·coverage·물리 wrist path·counterfactual continuation label·공통 SFT/normalizer·성공 head/BC comparator·RL은 미구현이다. 준비 코드가 있어도 이 항목이 자동 해제되지 않는다.

### 환경과 고정 자산

| 항목 | 설정·확인 경계 |
|---|---|
| 실행 host | **Linux x86_64 + 로컬 Docker + NVIDIA GPU/driver + NVIDIA Container Toolkit**. Launcher는 원격 endpoint/DOCKER_HOST override·ARM host를 거부한다. [NVIDIA 공식 설치 조건](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html). Mac Docker의 일반 CUDA `--gpus` 경로와 별도 Model Runner 가속을 혼동하지 않는다([Docker GPU 문서](https://docs.docker.com/desktop/features/gpu/)) |
| Base image | `pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime`, digest `sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755`. Registry manifest/config에서 linux/amd64 확인. Layer pull·실행은 안 함 |
| 주요 package | Torch 2.5.1/CUDA 12.4 base, Transformers 4.47.0, NumPy 1.26.4, MuJoCo 3.3.0, robosuite `5ce6643f3092639d08f7b0f90ed1c6a84f50552c`. [requirements](./requirements.txt)의 직접 버전은 고정했지만 transitive/apt hash lock과 설치 호환은 미확인. 빌드 시 `pip check`, freeze·dpkg 목록을 결과에 저장 |
| Rendering·attention | `MUJOCO_GL=egl`, `PYOPENGL_PLATFORM=egl`, NVIDIA capabilities `compute,utility,graphics`; BF16/eager attention. CUDA availability와 EGL 렌더링은 별도 검사. FlashAttention/DeepSpeed/학습 stack은 이번 범위에 필요 없음 |
| 임시 자원 하한 | Docker RAM 16GiB, GPU VRAM 12GiB/compute capability major≥8/BF16, cache 여유 30GiB. **운영상의 보수적 진입 조건이지 측정한 최소·충분 사양이 아님**. 이미지/빌드 저장 공간은 Docker data root에도 필요. 실제 peak/OOM/EGL은 첫 실행에서 기록 |
| Checkpoint | SpatialVLA HF revision `886c4557dfde53b44c0f74fde7d89bf83a26c3cd`. [PLAN](./PLAN.json)에 15개 파일 identity·size·LFS SHA256/일반 Git blob SHA1 고정. 합계 8,094,124,824 bytes는 원격 metadata이며 수신량이 아님. Custom `modeling_gemma2.py`도 포함; `trust_remote_code`는 이 pin·hash 검증 후에만 사용 |
| 저장·mount | Package/source는 Docker image, weights/cache는 named volume `paperreview-pose-active-cache-v1`의 `/cache`; 결과만 host output↔`/out` bind. 기본 `runs/`는 gitignore. CUDA·EGL·model native run은 network none. Payload fetch만 network 사용 |

<a id="resume"></a>
### 다른 컴퓨터에서 재개

저장소를 clone한 루트에서 아래를 실행한다. Host Python은 표준 라이브러리로 Docker를 호출할 뿐 package나 simulator를 import하지 않는다. 먼저 Linux/NVIDIA driver·Docker·Container Toolkit을 해당 컴퓨터에서 준비해야 한다. Launcher는 이 시스템 설치를 대신하지 않는다.

```bash
python3 'work/research_topics/pose_active_perception/재현 방법/resume.py' check
python3 'work/research_topics/pose_active_perception/재현 방법/resume.py' run
```

`check`는 endpoint/daemon/platform/RAM metadata까지만 확인한다. `run`은 이를 다시 확인하고 **base container GPU/BF16 → image build → Docker 제어 검사 → package 환경 → payload 수신/hash → scene/IO 검사** 순서로 진행한다. 실패하면 다음 단계를 실행하지 않는다. 기존 결과를 덮어쓰지 않고 새 run 폴더를 만들며 `--output`에는 비어 있는 경로만 지정할 수 있다. Build/fetch는 network와 디스크 용량에 따라 시간이 걸릴 수 있다.

전역 상한은 scene1·지시2·view≤2·pose fixture≤2·지시별 후보≤2, control≤20/physics≤10,000/AR step≤96/register0/optimizer0이다. 초기화의 `MjSim.step/step2`도 physics 예산에 포함한다. VLA invalid token은 실패 행동으로 label하지 않으며, 중복은 새 후보로 세지 않는다. 4-step 제어 replay용 normalizer가 없으므로 이 run은 **normalized IO에서 종료**한다.

성공 시 `launcher_result.json`, `checks.json`, `environment.json`, package 목록·image inspect, `payload.json`, `scene.json`, RGB/depth/좌표, `vla.json`, prefix feature, `result.json`이 남는다. 실패 시 해당 단계 로그·부분 결과를 보존한다. 컨테이너는 `--rm`과 이번 run의 고유 이름으로만 정리한다. 준비 image/cache volume은 재개용으로 유지하며 사용자 자산에 대한 `prune`은 하지 않는다. **현재 생성한 image/container/volume은 없다.**

다음 TODO는 **POSE-ACTIVE-P0 / NATIVE_RESOURCE_WAIT**다. Native 호환·렌더링·fixture/replay·후보 IO를 먼저 확인하고, 그 결과에 따라 FoundationPose adapter와 새 task의 정규화·기본 능력을 구현할 별도 pilot을 결정한다. 현 자료만으로 가림 해소·ACT/LOOK 효과나 통합 VLA 학습 기여를 주장하지 않는다.
