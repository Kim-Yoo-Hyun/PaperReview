# E1-R1 — 두 로봇 비교와 효과 지표의 연구 자격 재심사

- 날짜: 2026-10-22 KST. 사용자 요청에 따른 후속 buildup. VLA 중심, RL은 사용하지 않는다.
- **검토 작업 DONE / 재개 gate NOT_MET / 연구 REVISE·진단 HOLD.** 자료·모델 후보는 구체화했지만 새 replay 방법의 투자 근거는 아직 부족하다. 실험적 반증이나 연구 효과 입증은 아니다.
- 이전 [1차 심사](./README.md), [해석적 계약](./CLAIM_CONTRACT.md)을 보존한다. 현재 재개 조건은 [R1 명세](./R1_EVIDENCE_REQUIREMENTS.json), 실제 metadata 계산은 [R1_METADATA_AUDIT.json](./R1_METADATA_AUDIT.json), 출처 identity는 [ledger](./r1_sources_2026-10-22.json), 저장소 검사는 [검증](VALIDATION.md#stage-1)에 둔다.
- 정책·simulation·FK·학습 실행 0회. 공개 text/metadata만 읽었고 dependency·모델 weight·trajectory/video·PDF는 설치/저장하지 않았다.

## 1. 이번에 해소한 것과 남은 것

| 최초 요건 | 이번 새 근거 | 판정 |
|---|---|---|
| R1-A 두 실제 로봇의 공통 task·정상 관측/행동 | RoboInter의 RH20T view key 82,920개를 파싱해 cfg3/5 공통 task ID **59개**, task 6/8의 구체적인 key 확보 | PARTIAL: task 존재는 확인. scene/object·원시 command·동기화·정상 pose까지 연결하지 못함 |
| R1-B 정상 정렬 후 다른 예측이 나오는 자연 사례 | X-VLA의 pose-native 출력에서는 단순 효과 거리가 이미 정렬된 pose 오차에 가까워짐을 확인. Contact/추종/다중 해법은 아직 조건부 가설 | NOT_MET: 좌표·padding 수정으로 만든 차이를 신규성으로 인정하지 않음 |
| R1-C 유효 effect 추정과 정보/비용 | 공개 X-VLA의 공통 EE target, loss, 시간 표본화 경로를 고정. 목표 pose의 표현은 확보 | PARTIAL: 의도한 pose의 차이와 실제 달성 효과는 다름. 검증된 forward dynamics는 없음 |
| R1-D 공정 비교 | Native loss/유효 arm만의 score/회전 거리/시간 간격/soft prompt 동결 대조를 추가 | PARTIAL: 설계 계약을 보완했으나 matched split·실제 비용·실행 recipe는 미확정 |
| R1-E 두 로봇을 지원하는 VLA와 native 평가 경로 | X-VLA-Pt의 공개 revision·Franka/UR handler 확보. RoboInter는 공개 VLM과 미공개 VLA executor를 구분 | PARTIAL: 해당 task pair의 model–controller–evaluator 연결은 미확보 |

핵심 진전은 **공통 task 부재라는 우려를 metadata 수준에서 해소하고, 실제 채택 가능한 model interface를 찾은 것**이다. 반대로 해당 interface에서는 “명령을 물리 공간으로 바꾸면 새 정보가 생긴다”는 설명이 약해졌다. 데이터 자격과 기여 자격을 별도로 판정한다.

## 2. 직접 문헌과 공개 release

| 연구/자산 | 확인한 상태와 역할 | E1에서의 경계 |
|---|---|---|
| **X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model** | ICLR 2026 공식 OpenReview 색인에 published 표기. 본문은 arXiv v1 §4.2·Appendix D.2/G, 공개 code/HF config를 직접 확인 | Pose 정렬·domain prompt는 선행 방법. Joint multi-domain adaptation 결과는 continual retention 결과가 아님 |
| **RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation** | ICLR 2026; 기존 registry에 이미 존재. arXiv v1 Appendix A.3, 공개 dataset/변환기 확인 | 로봇별 open-loop 수치는 closed-loop 망각이 아님. 최신 repo의 RoboInter1.5 technical report와 원 ICLR 논문을 합치지 않음 |
| **Table30 V2: Evaluating Generalized Models by Real Robots at Scale** | CVPR 2026 **Workshop**, main conference로 세지 않음. Table30v2 공개 card/변환기 확인 | 별도 robot/task 배치의 평가 자료. 동일 task의 두 로봇 matched pair를 확보하지 못함 |
| **TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks** | arXiv:2608.24101 **v2**, 학회 채택 미확인. §4.1에서 Panda→UR5, 동일 task/scene의 LIBERO-INTEGRAL 제안 | 이 논문의 공개 링크는 placeholder project 주소. 검토한 1차 자료에서 환경·checkpoint release를 식별하지 못함. 재현 가능한 benchmark로 채택하지 않음 |

직접 근거: [X-VLA 공식 색인 대상](https://openreview.net/pdf/d44409f253fba9242cb42be37ae0150dd3e01ddb.pdf), [X-VLA 본문](https://arxiv.org/html/2510.10274v1), [RoboInter 공식 forum](https://openreview.net/forum?id=PGUC3mmMoi), [RoboInter 본문](https://arxiv.org/html/2602.09973v1), [Table30 V2 공식 workshop 페이지](https://openaccess.thecvf.com/content/CVPR2026W/GigaBrainChallenge/html/Ma_Table30_V2_Evaluating_Generalized_Models_by_Real_Robots_at_Scale_CVPRW_2026_paper.html), [TrAct v2](https://arxiv.org/html/2608.24101v2). 이번 재조회 중 OpenReview는 browser verification, CVF는 403을 반환하기도 했다. 공식 검색 색인/앞선 조회와 실제 열람 본문을 구분하며, 우회 접근하지 않았다.

Memory Anchors·MIR·Never v3·ICML continual VLA·SPACE·HiMoE의 직접 충돌 판정은 [기존 비교](./CLOSEST_WORK.md)를 이어받는다. 이번 공개 자산 조사로 이들의 미공개 구현을 확보했다고 표시하지 않는다. 새 논문 등록이나 기존 paper note의 자동 재작성은 이번 범위에 포함하지 않았다.

Table30v2의 [고정 revision 변환기](https://huggingface.co/datasets/RoboChallenge/Table30v2/blob/c58ad2cc76ce722ea54de51f9fae03012a698f47/convert_to_lerobot.py)는 앞 시점의 joint/gripper를 state로, 뒤 시점의 기록된 EE/gripper를 action target으로 만든다. 따라서 action이라는 이름만으로 별도 controller command를 확보한 것이 아니다. 원격 실제 로봇 평가 서비스도 현재 컴퓨터에서만 실행한다는 범위에 포함되지 않아 사용하지 않았다.

## 3. RH20T의 공통 task를 실제 식별자로 연결

[공식 config](https://github.com/rh20t/rh20t_api/blob/aa3124434729ed622109a29b2cbb9f3bbb1c5eeb/configs/configs.json)에서 cfg3은 **UR5 + WSG-50**, cfg5는 **Franka**다. UR5+Robotiq의 논문 집계 열을 cfg3이라고 간주하지 않는다. 같은 로봇의 다른 센서 구성도 독립 embodiment로 세지 않는다.

[RoboInter-Data revision](https://huggingface.co/datasets/InternRobotics/RoboInter-Data/tree/0208b79c34eca4d214cdb5d07f5ae0f7cc634340)은 ungated 공개 자산이다. 다음 **text metadata**를 직접 파싱했다.

- `range_nop_rh20t_all.json`: 82,920 keys, 146 task IDs. cfg3은 66 task IDs, cfg5는 98, 교집합 59. Zero-padded ID를 정수로 정규화했다.
- `All_Keys_of_Primary.json`: 전체 65,515 keys 중 해당 RH20T key와 교집합. 이 파일에 속한다는 것이 모든 sensor/action의 정확성을 보증하지는 않는다.
- `val_video.json`: 전체 7,246 keys와 membership 대조. 이를 새 실험의 독립 train/test split으로 재사용하지 않는다.
- LeRobot `meta/info.json`: 82,894 episodes·146 tasks·10 fps, `episodes.jsonl`도 82,894행. 범위 key 수 82,920과 다르며, 일대일 변환 mapping을 확인하지 않아 26개를 임의로 실패 episode라고 해석하지 않는다.

| 후보 task | 공식 의미 | cfg3 view keys / Primary keys | cfg5 view keys / Primary keys |
|---|---|---:|---:|
| task_0006 | 작은 block을 왼쪽에서 오른쪽으로 밀기 | 31 / 6 | 57 / 8 |
| task_0008 | block을 집어 지정된 위치에 놓기 | 40 / 22 | 120 / 95 |

[공식 task 설명](https://rh20t.github.io/static/task_description.json)과 [계산 결과](./R1_METADATA_AUDIT.json). **위 수치는 camera serial을 포함한 view key 수이며 독립 trajectory/trial 수가 아니다.** 같은 `scene_0001`도 configuration 사이의 동일 scene을 의미한다고 가정하지 않는다.

구체적인 task_0008 후보 두 개:

- UR5: `RH20T_cfg3_task_0008_user_0016_scene_0001_cfg_0003_036422060909`, range metadata `[45, 228, 184]`.
- Franka: `RH20T_cfg5_task_0008_user_0007_scene_0001_cfg_0005_036422060215`, range metadata `[107, 482, 376]`.

위 range 값을 command timestamp나 event 시각으로 해석하지 않는다. 선택은 두 robot의 같은 task ID가 존재한다는 증거에 한정된다. 실제 물체, goal region, RGB visibility, 카메라 보정과 유효 action은 아직 검사하지 않았다.

### 변환된 action 필드가 해결하지 못한 부분

[RH20T→LeRobot converter](https://github.com/InternRobotics/RoboInter/blob/091548aa09d87c8987cec224c98bf23f1594e72b/RoboInterData/convert_to_lerobot/convert_rh20t_to_lerobot_anno_fast.py)는 LMDB의 `action`/`state`를 읽는다. 추가 `action_tcp_pose`, `action_delta_tcp_pose` 등의 누락에는 zero default가 있다. 이 변환기만으로 상류 action이 controller command인지 관측 displacement인지 확정할 수 없다. Frame timestamp를 명시하지 않으면 `frame_index/fps`로 만든다. 따라서 **필드 이름·fps 선언만으로 원시 시간 정렬이 검증된 것은 아니다**.

`episodes.jsonl`에는 index/task/length가 있고 source robot ID는 없다. Source view key→LeRobot episode index 연결은 미확보다. 큰 공개 Qsheet/raw-path mapping의 존재는 확인했지만 본문은 읽지 않았으므로 그 안에도 연결이 없다고 단정하지 않는다. 정책 실험 전에 필요한 것은 count 재집계가 아니라 이 source join과 command 생성 근거다.

RoboInter의 [VLA README](https://github.com/InternRobotics/RoboInter/blob/091548aa09d87c8987cec224c98bf23f1594e72b/RoboInterVLA/README.md)는 code release를 예고하는 상태다. 공개 [RoboInter-VLM](https://huggingface.co/InternRobotics/RoboInter-VLM)은 Qwen2.5-VL conditional-generation 모델이며 해당 DiT executor checkpoint가 아니다. 따라서 RH20T 자료와 공개 VLA native evaluator가 모두 준비됐다는 결론은 내리지 않는다.

## 4. X-VLA가 주는 구체적인 policy 경로

- GitHub commit: `6c4ecfb8be458ae7c0c96094e4b0add4174f4fe2`.
- HF `2toINF/X-VLA-Pt` revision: `c1c4a64a7e03ac5b95c468bf1578f3d03651b53b`.
- [Checkpoint config](https://huggingface.co/2toINF/X-VLA-Pt/blob/c1c4a64a7e03ac5b95c468bf1578f3d03651b53b/config.json): `ee6d`, `num_actions=30`, `use_proprio=true`, `num_domains=30`, `use_hetero_proj=false`.
- [RoboMIND handler](https://github.com/2toinf/X-VLA/blob/6c4ecfb8be458ae7c0c96094e4b0add4174f4fe2/datasets/domain_handler/robomind.py): Franka/UR 모두 `puppet/end_effector`의 xyz+Euler를 xyz+rotation6D로 바꾸고 gripper를 붙인 10D left arm, zero right arm을 만든다. [Domain config](https://github.com/2toinf/X-VLA/blob/6c4ecfb8be458ae7c0c96094e4b0add4174f4fe2/datasets/domain_config.py)는 Franka=11, UR=12다.

### 시간·pose·checkpoint의 범위

[Base handler](https://github.com/2toinf/X-VLA/blob/6c4ecfb8be458ae7c0c96094e4b0add4174f4fe2/datasets/domain_handler/base.py)는 timestamp가 없으면 index/30초로 구성한다. 현재 시점부터 최대 4초까지 `num_actions+1`개를 보간하고, episode 끝에서는 window를 줄인다. [action_slice](https://github.com/2toinf/X-VLA/blob/6c4ecfb8be458ae7c0c96094e4b0add4174f4fe2/datasets/utils.py)는 첫 pose를 proprio, 나머지를 target으로 쓴다. **30개 target은 원본 30 frame/1초와 같지 않다.** Full 4초 window이면 간격은 4/30초이며 끝부분은 더 짧다. 실제 기록 시간과 native 실행 간격은 별도 확인해야 한다.

RoboMIND 배포 측은 일부 UR 데이터의 거의 상수인 EE pose와 FK 대안을 [보고](https://github.com/Open-X-Humanoid/RoboMIND-dataset-utils/blob/77d7b311cbf2f16624c941f46b2a75042858ff06/README.md)했다. 해당 X-VLA handler에는 FK 보정이 없다. 다만 **발표된 X-VLA가 오류 데이터를 그대로 학습했다고 단정하지 않는다**. 학습 전 별도 처리 여부·실제 payload revision은 미확인이다. [FK helper](https://github.com/Open-X-Humanoid/RoboMIND-dataset-utils/blob/77d7b311cbf2f16624c941f46b2a75042858ff06/eepose/joint2pose.py)의 Franka TCP는 `panda_hand_tcp`, UR5e key는 `ur5_robot.urdf`/`ee_link`를 참조한다. 파일 이름만으로 잘못된 모델이라고 단정하지 않고 실제 hardware calibration·tool offset·joint order를 요구한다. FK는 실행하지 않았다.

Foundation model의 training mixture에는 Franka/UR가 모두 포함된다. 따라서 이 조합은 **이미 노출된 embodiment의 순차 재적응** 후보이며, pretraining에서 보지 못한 로봇으로의 전이 근거가 아니다. Held-out task/scene도 provenance 확인 전에는 unseen으로 부르지 않는다. 개별 LIBERO/WidowX/Google checkpoint의 점수를 합쳐 하나의 모델이 둘 다 잘한다고 주장할 수 없다. 논문 Appendix D.2의 joint adaptation은 참고할 upper reference이나 sequential stream 결과는 아니다.

### Loss와 score의 공정성

[Checkpoint-bundled action_hub](https://huggingface.co/2toINF/X-VLA-Pt/blob/c1c4a64a7e03ac5b95c468bf1578f3d03651b53b/action_hub.py)도 직접 읽었다. `ee6d`는 xyz MSE×500, rotation6D MSE×10, gripper BCE를 사용하며 두 arm의 항을 계산한다. 읽은 [forward 경로](https://huggingface.co/2toINF/X-VLA-Pt/blob/c1c4a64a7e03ac5b95c468bf1578f3d03651b53b/modeling_xvla.py)에는 arm-validity mask가 없다. `image_mask`는 action mask가 아니다. Single-arm의 zero right target은 실제 움직임이 아니므로, 그 오차를 포함한 native loss와 유효 arm score를 함께 보고해야 한다. Padding 제거로 얻는 차이는 구현 통제이며 연구 기여가 아니다.

그리퍼는 noisy action/proprio 입력에서 0으로 처리하고 target BCE는 남는다. 이를 일반 pose MSE와 그대로 더한 score의 scale 효과도 통제한다. 현재 checkpoint와 최신 GitHub 파일을 섞어 실행하지 않도록 revision을 분리했다. Weight 로드나 remote code 실행은 하지 않았다.

## 5. 차별적 예측을 더 엄격하게 좁힘

아래는 **새로운 연구자 분석·실험 전 예측**이다. 정책 결과가 아니다.

### 5.1 Pose-native 출력에서는 효과 거리만으로 충분하지 않음

X-VLA의 target이 미래 EE pose이면 `d(predicted_pose, demonstration_pose)`는 이미 정렬된 action residual이다. SO(3) geodesic으로 바꾸거나 task 축별 가중치를 주면 순위는 달라질 수 있지만, 이를 실제 효과에 대한 새 관측이라고 부를 수 없다. 올바른 rotation metric·시간·유효 arm으로 계산한 잔차를 강한 baseline으로 둔다. 특정 scalar loss보다 좋은 metric이 있을 가능성은 남지만 자동으로 새로운 forgetting 정보가 생기지는 않는다.

| 후보 상황 | 다른 예측을 낼 수 있는 추가 정보 | 왜 아직 R1-B를 통과하지 못했나 |
|---|---|---|
| 정상 target의 controller 추종 지연/접촉 compliance | 실행 history·controller 상태와 calibration된 forward response | Command–state 시간 연결과 calibration packet이 없음. EE target/FK만으로는 해당 정보가 안 생김 |
| 같은 goal에 이르는 여러 올바른 경로 | Goal/접촉 조건에 따른 성공 동등성 | 단일 demonstration 잔차는 실패 label이 아님. Task 8의 제목만으로 두 실제 경로가 동등하다고 판정할 수 없음 |
| 접촉 경계 근처의 작은 오차가 큰 실패를 유발 | Object geometry/contact cue와 독립 outcome | 보통 task-sensitive metric/기존 geometry 대안과 비교해야 함. 원래 E1보다 추가 sensing/model 비용이 생김 |

위 경우를 새 방법의 발견으로 주장하지 않는다. 특히 미실행 action의 결과를 demonstration의 다음 state로 채우지 않는다. 기존 [반례 A–C](./CLAIM_CONTRACT.md)의 경계를 유지한다.

### 5.2 Parameter sharing을 고정하지 않으면 망각 해석이 바뀜

모델을 `f(x; θ_shared, p_robot)`라 쓰자. B 적응 때 **B prompt만** 갱신하고 shared weights·A prompt·normalizer·다른 mutable state를 모두 고정하며 A routing/input이 같으면 A 함수는 그대로다. 초기 action residual이 커도 이 조건에서는 A 출력 변화가 없다. 이는 함수 의존성에 따른 도출이지 공식 PEFT script가 그대로 이 조건을 구현한다는 주장이 아니다.

따라서 H1은 update regime을 고정해 검사한다. Shared update와 prompt-only update를 섞어서 “effect score가 retention을 예측했다”고 평가하지 않는다. Prompt-only가 new competence도 충분히 보존하면 더 복잡한 replay의 실용적 headroom이 작다. 반대로 shared update가 유리한 경우에만 선택 문제를 계속 검토한다.

## 6. 비교 계약 보완과 최소 후속 검사

학습/정책 검증을 진행한다면 [기존 계약](./CLAIM_CONTRACT.md)에 아래를 추가한다. 아직 executable manifest는 아니다.

1. **Score 시점:** 업데이트 전 old archive의 같은 candidate pool에서 계산. Oracle future outcome은 선택 입력에서 제외한다. MIR 가상 update는 실제 optimizer/허용 parameter set을 반영하고 이를 추가 비용으로 센다.
2. **기준 score:** native denoising loss, 유효 arm의 aligned residual, 물리 시간·rotation geodesic residual, MIR. Memory Anchors는 공식 VLA recipe가 없으면 정확 재현으로 표시하지 않고 명시한 구현 variant로 분리한다.
3. **Noise/추론 예산:** 같은 noise draw·flow time·candidate 수로 비교하고 forward/backward, image embedding 재사용, calibration 비용·archive bytes를 기록한다. 값은 아직 측정하지 않았다.
4. **학습 대조:** replay 없음, uniform, robot/task-balanced, aligned conflict replay, MIR, B-prompt-only, joint-data reference. Update 수·old/new 노출·가용 archive와 resident buffer를 일치시킨다. Prompt-only는 가용 성능과 비용의 별도 trade-off로 평가한다.
5. **Split:** 같은 물리 demonstration의 camera view를 train/test에 나누지 않는다. Robot·task·scene/source grouping을 먼저 확인한다. 59 task IDs는 후보 집합이지 이미 확정한 실험 split이 아니다.
6. **Outcome:** H1은 score→held-out old closed-loop 성공 변화의 추가 예측력을 보며, loss 변화를 능력 저하로 대체하지 않는다. 여러 frame을 독립 표본으로 세지 않는다. H2는 H1 이후의 selector 개입이며 new-task 비열등성과 비용을 함께 본다.
7. **Stop/revise:** 시간/pose/padding 정리만으로 차이가 사라지면 data/metric 통제로 종료한다. Competence가 없거나 망각 headroom이 없으면 selector 학습을 시작하지 않는다. 추정 오차·비용이 이득보다 크면 forward model 추가를 기각한다. 수치 margin·sample size는 실제 task/runtime qualification 전에 임의로 정하지 않는다.

## 7. 연구 가치와 다음 행동

**E1을 본격 replay 방법 연구로 채택할 근거는 여전히 부족하다.** 문헌상의 중요성과 공개 다중 로봇 자산은 충분해졌지만, 정상 정렬 이후의 물리 효과가 retention에 추가 정보를 준다는 구체적인 사례는 확보하지 못했다. 이번 결과는 단순 GPU 대기가 아니다. X-VLA 경로는 구현을 구체화하는 동시에, 단순 effect-space 변환이라는 기여 주장을 더 약하게 만든다.

제한된 진단 질문은 남긴다: **같은 parameter-sharing 조건에서, 올바른 pose/time residual로 설명되지 않는 controller/contact 정보가 closed-loop retention을 추가 설명하는가?** 실제 추가 정보 없이 표현만 바꾸는 설계에는 투자하지 않는다.

다음은 **E1-R2 / WAITING_EVIDENCE**이며 같은 문헌 목록을 반복 조회하는 자동 작업은 아니다. 아래 중 일관된 하나의 경로를 확보한 후 재심사한다.

- **실제 데이터 경로:** RH20T task 8(보조 task 6)의 source view→physical episode→변환 action 연결, command 생성/시간/scene 근거, 해당 로봇의 native checkpoint–controller–evaluator packet. RoboMIND/X-VLA를 고르면 정상 pose 처리 provenance와 해당 pair의 evaluator가 대신 필요하다. 두 dataset의 서로 다른 장점을 합쳐 하나의 준비된 경로로 표시하지 않는다.
- **시뮬레이션으로 범위를 변경하는 경로:** TrAct의 동일 task Panda/UR5처럼 task·scene·controller·checkpoint가 공개되어야 한다. 두 물리 robot model의 진단으로 범위를 명시적으로 바꾸며 실제 로봇 검증이라고 부르지 않는다. 현재 검토 자료에서는 이 패키지가 확보되지 않았다.
- **차별적 예측:** 위 경로에서 정상 aligned residual과 다른 예측을 낼 추가 cue/추정식·오차 평가 방법·비용을 함께 제시한다. 실험 효과를 미리 증명하라는 요구가 아니라 비교를 성립시키는 조건이다.

R1 검토는 완료했다. 필요한 packet 없이 큰 학습·환경 이식·새 dynamics model 구현을 시작하지 않는다. E1-E1은 HOLD_RESEARCH, E1-F1 실제 외부 피드백은 NOT_STARTED다. E2로 자동 전환하거나 C/D 판정을 변경하지 않았다.

## 8. 기존 buildup 절차와의 대응

| Guide 단계 | 이번 R1 수행 | 남은 범위 |
|---|---|---|
| 1 중요성 | 순차 재적응 비용/기존 능력 보존으로 범위 유지 | 현장 필요성·headroom 실증 |
| 2 가까운 연구·반대 근거 | X-VLA·RoboInter·Table30 V2·TrAct와 기존 replay 대조 | 새 방법 우위 미검증 |
| 3 가정·interface | task key, pose/time/action loss, checkpoint provenance 추적 | 실제 trajectory qualification |
| 4 반증 가능한 가설 | Pose residual 환원·prompt 동결 대조, 추가 cue 조건 | 자연 사례와 차별적 예측의 자격 |
| 5 직접 본문·공개 구현 | 본문 해당 절과 pinned source/config 확인 | 미공개 executor/flow recipe |
| 6 주장–증거·baseline | §6에 공정 비교·stop rule 보완 | 실행 manifest·수치 margin |
| 7 가장 약한 고리 검사 | 공개 text metadata 파싱과 코드/해석적 검사 | Docker native competence/효과 |
| 8 비판·판정 | 내부 반박과 REVISE·HOLD | 실제 외부 연구자 피드백 |

이 표의 문서 작업 완료를 8단계 전체의 실험적 완료로 해석하지 않는다.
