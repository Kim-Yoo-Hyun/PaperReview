# E2 공개 source·interface 감사

- 2026-10-22, **read-only text/API 검사**. 외부 코드를 import/실행하지 않았고 설치·clone·weights·trajectory·video·PDF 저장 없음.
- [Source ledger](./sources_2026-10-22.json)는 text 응답의 URL/hash와 별도 web 확인 경계를 기록한다. Hash는 검토한 파일 identity이며 재현 성공 증거가 아니다.
- 아래는 일부 대표 경로의 정적 추적이다. Repository 전체·hardware firmware·측정된 timing까지 감사했다는 뜻이 아니다.

## 1. RTR — frequency 이름과 실제 control interface

Repo: [tars-robotics/RTR @ 0589f847bf4f61e1fb959f23cf3a0329de9bb9b3](https://github.com/tars-robotics/RTR/tree/0589f847bf4f61e1fb959f23cf3a0329de9bb9b3).

| 비교 지점 | 15 Hz 경로 | 60 Hz 경로 |
|---|---|---|
| π0.5 wipe-vase launch | [15 Hz script](https://github.com/tars-robotics/RTR/blob/0589f847bf4f61e1fb959f23cf3a0329de9bb9b3/scripts/eval/xarm/closedloop/wipe_vase_15hz/pi05/pi05_15hz_nonservo_sync_closedloop_launch_system.sh) | [60 Hz script](https://github.com/tars-robotics/RTR/blob/0589f847bf4f61e1fb959f23cf3a0329de9bb9b3/scripts/eval/xarm/closedloop/wipe_vase_60hz/pi05/pi05_60hz_sync_closedloop_launch_system.sh) |
| `horizon` | 12 | 48 |
| 설정 `control_hz` / `execute_hz` | 60 / 50 | 60 / 50 |
| `servo_mode` | False | True |
| env 명령 경로 | mode 0, blocking `set_position(...wait=True)` | mode 1, `set_servo_cartesian(...)` |

마지막 행은 [xarm_env.py L291–345](https://github.com/tars-robotics/RTR/blob/0589f847bf4f61e1fb959f23cf3a0329de9bb9b3/src/rtr_async_sys/env/xarm_env.py#L291)의 실제 branch로 확인했다. DP peel-cucumber 대표 recipe도 같은 mode 구분이다. `async_servo_executor.py` 추정 경로 조회 하나는 404였으며 해당 파일을 읽었다고 간주하지 않는다.

**도출:** 파일 이름의 15/60 Hz, 내부 scheduler 설정, 실제 명령 도착률을 같은 변수로 쓰면 안 된다. 공개 recipe는 controller mode도 바꾸므로 representation만의 causal 비교가 아니다. 반대로 이 차이가 원 논문의 결과를 무효화한다거나 이득을 전부 설명한다고 말할 수 없다. Real-system co-design 목적과 새 attribution 실험을 구분한다. Actual command timestamps·물리 trajectory·통제된 반사실 결과는 없다.

공개 closed-loop 문서는 플랫폼에 맞는 env 구현을 요구한다. 현재 컴퓨터만으로 xArm real-world 결과가 재현 가능하다고 판정하지 않는다. Simulator 포팅은 동등한 baseline이 자동으로 되지 않으며 지금 시작하지 않았다.

## 2. AAC — uncertainty로 실행 길이를 고르는 실제 위치

- [Server @ 11e926b0f34cf6acfcb92c0fe6127a1bdc7b856a](https://github.com/Adaptive-Action-Chunking/gr00t-multi-sample/tree/11e926b0f34cf6acfcb92c0fe6127a1bdc7b856a): README는 GR00T 다중 candidate 생성 server와 entropy를 계산하는 client를 분리한다. Website repo를 method code로 오인하지 않았다.
- [LIBERO client @ ff8c8e421f7805b5845a72d07fbd8f1171df74bf](https://github.com/Adaptive-Action-Chunking/libero/tree/ff8c8e421f7805b5845a72d07fbd8f1171df74bf): README는 upstream LIBERO revision `8f1084e3132a39270c3a13ebe37270a43ece2a01`을 제시한다. 이 revision의 native 실행은 미검증이다.
- [action_entropy_v2.py](https://github.com/Adaptive-Action-Chunking/libero/blob/ff8c8e421f7805b5845a72d07fbd8f1171df74bf/action_optimization/action_entropy_v2.py#L244): covariance entropy와 gripper entropy, 누적 평균의 차이, movement lower bound로 `select_chunk_size`를 계산한다.
- [inference_client_action_entropy.py L187–253](https://github.com/Adaptive-Action-Chunking/libero/blob/ff8c8e421f7805b5845a72d07fbd8f1171df74bf/gr00t_benchmark/inference_client_action_entropy.py#L187): 관측 수집→server `get_action`→길이 선택→선택된 행동들의 `env.step`. 이 loop에서 추론 중 비동기로 simulator를 진행시키는 경로를 확인하지 못했다.

**도출:** short horizon은 더 잦은 policy call을 동반한다. Candidate sample 수·실제 처리 시간·policy 호출 수를 비교 비용에 넣어야 한다. 이 client만으로 wall-clock deadline을 만족한다고 주장할 수 없다. 별도 π0.5 client 파일의 존재는 확인했지만 server/checkpoint까지 qualification한 것은 아니다. Public code는 확보했지만 checkpoint·normalizer·task competence는 미확보다.

## 3. A2C2 — E2와 가장 가까운 feedback 대안

Repo: [k1000dai/a2c2-libero @ 54dd088302a0ef3f50c4add3ec927ab94d76a406](https://github.com/k1000dai/a2c2-libero/tree/54dd088302a0ef3f50c4add3ec927ab94d76a406).

[eval_libero/evaluation_libero.py](https://github.com/k1000dai/a2c2-libero/blob/54dd088302a0ef3f50c4add3ec927ab94d76a406/eval_libero/evaluation_libero.py):

- L33–34: base/residual checkpoint가 `policy/to/...` placeholder다. 이 파일에서 public checkpoint ID를 확보하지 못했다.
- L64–68: `execute_horizon`과 `inference_delay`를 따로 받으며 chunk 길이 제약을 확인한다.
- L199–226: 매 env step 최신 RGB·proprio·task를 준비한다.
- L228–262: chunk를 갱신하고 이전 pending prefix와 새 chunk의 delayed suffix를 조합한다. 첫 chunk는 별도 초기화 규칙이다.
- L287–313: 현재 base action, **전체 base chunk**, chunk phase의 sin/cos, VLM hidden을 residual 입력에 넣고 최신 관측에서 보정한 action으로 `env.step`한다.

**도출:** 고정 step-delay를 emulation하는 queue 구현이며 실제 asynchronous GPU/network wall-time의 측정 결과가 아니다. 이미 delay/horizon을 분리하므로 E2가 그 설계 자체를 새 기여로 삼을 수 없다. 추가 residual이 보는 전체 chunk·학습 비용까지 matched 대조에 반영해야 한다. Pinned source와 논문 버전의 실험 recipe가 항상 동일하다고 가정하지 않는다.

README의 Docker 경로는 존재하지만 실행하지 않았다. `.gitmodules`는 upstream LIBERO를 가리킨다. Dataset 생성 파일도 dataset/base-model 경로가 placeholder다. 공개 code는 native task 성능이나 공개 trained residual 확보와 다르다.

## 4. 논문 부록에서 추가로 확인한 공정성 경계

- [SAIL v2 App. C.1/D.1](https://arxiv.org/html/2506.11948v2): simulation의 torque-limit 선택과 일부 baseline의 예외를 명시하며 real robot의 policy/target/torque/camera 주기를 분리한다. “기존 연구는 controller를 고려하지 않는다”는 비판을 배제한다.
- [PaceVLA v2 §3.5/App. C.3](https://arxiv.org/html/2610.25961v2): acceleration methods끼리의 gain 통제와 default GR00T 비교의 조건은 다르다. 이는 저자가 밝힌 설정 경계이며 비교 부정의 단정 근거가 아니다.
- [Vela v1 §4.4/App. B.2](https://arxiv.org/html/2610.05230v1): post-hoc spline fitting과 execution-horizon 대조가 이미 있다. 단순 curve baseline 추가만으로 novelty가 생기지 않는다.

## 5. 실행 자격 판정

| 후보 | 문헌·source 자격 | 아직 없는 연결 | 현재 사용법 |
|---|---|---|---|
| A2C2 / SmolVLA / LIBERO Spatial | 관측·queue·residual 경로 확인 | 정확한 trained base/residual artifact·정규화·runtime·유효 task·timestamp | 가장 가까운 learned-feedback 대안, 실행 HOLD |
| AAC / GR00T / LIBERO | selector·client/server·upstream revision 확인 | 선택 task의 정확한 weight/normalizer, physical-time/latency 계측 | Adaptive horizon baseline 후보, 실행 HOLD |
| RTR / π0.5 / xArm | 대표 mode branch·recipe 확인 | hardware/controller/timestamp·공통 evaluator, 현재 컴퓨터 실행 경로 | 시스템 비교의 문헌/코드 근거; 즉시 simulator baseline으로 이식하지 않음 |

이 세 경로의 장점만 합쳐서 하나의 qualified packet으로 취급하지 않는다. 기존 D1의 OFT 자원 결과를 다른 E2 모델의 불가능성 증거로 재사용하지 않는다. **현재는 연구 설계·자산 자격의 보류이며 GPU 하나만의 blocker가 아니다.**
