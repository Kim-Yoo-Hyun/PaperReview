# 작업에 필요한 물체 자세의 모호성을 해소하는 능동 관측 VLA

2026-11-18: 직접 선행의 정식 paper-note와 publication 경계는 [REG-R17 등록](../../../update/REGISTRY_MAINTENANCE_2026-11-18.md)으로 연결했다. 아래 연구 판단·실행 준비 상태는 유지한다.

Updated: 2026-11-17 KST. **N1/N2·P0 준비 완료 / native 검증 대기 / 좁은 탐색 CONTINUE / CURATION-HYPOTHESIS.** 물체의 6D pose를 다룬다. 직접 선행·네 사례·공개 source와 비교 계약을 확인했으며 독립 신규성·효과·native 실행은 미확립이다. [재현 준비 범위](../재현%20방법/README.md#p0-preparation) · [공통 근거 원장: pose_active_n1 / pose_active_n2 / pose_active_p0_preparation](../../../sources/new_field_scout_2026-11-17.json) · [현재 선택](../../../../TODO.md).

<a id="p0-preparation-result"></a>
## P0 구현 준비 결과

**Scene/evaluator·camera/제한된 상태 복원·SpatialVLA 후보/재채점 probe와 Docker 재개 경로를 작성했다.** 새 launcher를 현재 컴퓨터에서 호출했으나 로컬 daemon 연결 실패로 중단됐다. Host는 ARM64 Mac이며 이 recipe의 Linux/NVIDIA 경로와도 다르다. [준비 artifact·실제 실패·재개 명령](../재현%20방법/README.md#p0-preparation)에 구분해 기록했다. 코드 정적 컴파일만 확인했고 Docker image build·제어 검사 10개·native 실행은 하지 못했다.

이번 구현에서 연구 부담은 더 구체화됐다. 같은 물체의 PLACE/ALIGN을 검사하는 script는 있으나, 이는 정답 자세로 놓은 evaluator fixture다. **가림 때문에 행동 결정을 바꿔야 하는 실제 사례나 VLA 배치 능력을 확보한 것은 아니다.** 새 task의 normalizer가 없어 VLA는 normalized token/feature IO까지만 검사하도록 했고 FoundationPose registration·물리 시점 이동·counterfactual continuation label·성공 head 학습은 남겼다. 고정 시점 렌더링을 실제 active perception이나 로봇 시간 절약으로 세지 않는다.

연구 판단은 **좁은 탐색 CONTINUE, 효과·독립 신규성 미확립**을 유지한다. 다음은 호환 NVIDIA 로컬 Docker에서의 제한된 P0 검증이다. 내부 문헌/설계 검토를 다시 반복할 이유는 없으며, 자원 확보만으로 신규성이 해결되는 것도 아니다. P0 이후에는 실제 사례·공통 task 데이터·단순 lookup/분리 classifier 대비 추가 이득이 있는지를 확인해야 한다. 다른 주제의 보류·폐기 판단은 바꾸지 않았다.

<a id="n2-result"></a>
## N2 결과 — 다음은 작은 구현으로 확인

**현재 확보 가능한 내부 문헌·논리·비교 설계는 이번 범위에서 마친다.** SpatialVLA와 FoundationPose를 선택하고 같은 SquareNut의 느슨한 배치/손잡이 방향 배치, 행동 후보×자세 가설의 성공 label, 강한 단순 대안과 데이터·시간 통제를 명세했다. N2 당시 후속으로 P0-PREP를 선택했고, 위에 그 준비 결과를 기록했다. 같은 체크리스트의 N3 반복은 하지 않는다. 외부 연구자 피드백·구현 검증·연구 효과는 여전히 미확인이다.

핵심 발견은 다음과 같다.

- 공개 checkpoint의 실제 출력은 **4-step/12-token chunk**다. Tokenizer는 잘못된 ID를 clip하고 decoder는 짧은 출력을 pad할 수 있어, 후보별 유효성 검사·개별 decode·순차 재채점 계약을 추가했다. 전체 suffix를 잘못된 attention mask로 재채점하면 미래 action 누출이 생길 수 있어 native 일치 검증을 먼저 하기로 했다.
- 원 VLA에는 pose 조건 입력이 없다. 같은 RGB를 반복 입력해 얻은 점수를 ‘pose별 action KL’로 부를 수 없다. 같은 label로 학습할 pose-conditioned candidate BC를 **DISaM-inspired comparator**로 분리하며, 원 DISaM 재현으로 표시하지 않는다. 가장 직접적인 학습 대조는 동일 정보의 별도 성공 head다.
- 기존 너트 삽입 성공 판정을 빌려 쓰지 않고, release/support/dwell과 handle 방향을 갖는 **새 배치 evaluator**를 정의했다. 공개 geometry는 출발점이며 custom scene·정규화·해당 task의 VLA competence는 아직 없다. 삽입 성능이나 공개 benchmark 결과로 해석하지 않는다.

정확한 source·입출력·미구현 경계는 [단일 비교 계약](../재현%20방법/README.md#n2-contract)이 소유한다. 방법 후보는 여전히 **같은 VLA 표현에서 자세별 행동 성공 양립성을 학습하는 것**이다. Frozen feature+외부 head로 시작하면 모듈형 진단이며, 같은 VLA adapter를 행동 loss와 함께 갱신하기 전에는 unified 정책 학습이라고 부르지 않는다. RL은 후속 선택지다.

추가 발견한 [When to Make a Decision, arXiv 2026](https://arxiv.org/html/2610.23891v1)도 task-sufficient perception과 관측 중단을 제안한다. §3–6은 neuro-symbolic 개념 설계와 **예정된** 평가이며 구현/성공률 결과가 아니다. Venue acceptance는 미확인이다. 일반 ‘언제 충분히 봤는가’는 새 기여가 아니라는 경계를 보강하고, 방법이 이미 실증적으로 해결됐다는 근거로 과장하지 않는다. 신규 paper 등록 없이 source 원장에 직접 충돌 근거로 남겼다.

이 후보는 **제한된 첫 구현에 투자할 여지**가 있다. 다만 현재 가장 큰 위험은 새 label/evaluator·task adaptation 부담과 강한 별도 classifier 이후에 공유 VLA 학습의 이득이 남는지다. GPU가 없어서 신규성이 보이지 않는 상황으로 단순화할 수 없다. 1번이 2번보다 쉽다는 판단은 계속 유보하며, 구현 첫 산출물에서 이 부담을 다시 비교한다.

<a id="n1-result"></a>
## N1 결과와 연구 판단

**‘pose 불확실성이 남아도 성공할 수 있으면 관측을 멈춘다’는 원리는 기존 연구에 있다.** 별도 방법으로 남길 질문은 **VLA의 유한 행동 후보들에 대해, 여러 pose 가설에서의 성공 양립성을 학습하면 기존 action-disagreement·허용 오차 lookup보다 유용한 관측/행동 선택을 하는가**다. 단순한 robust action 선택이나 success classifier를 새 원리라고 부르지 않는다. 공유 VLA 표현에서 이 관계를 학습할 필요성과 held-out 물체/지시에서의 효과가 핵심 미검증 항목이다.

또한 **valid action multimodality만으로 DISaM의 실패를 예측했던 초기 직관을 수정한다.** DISaM은 원시 action sample variance 대신 context별 **분포 사이의 KL**을 사용한다. 같은 다봉 분포라면 관측 요청이 늘지 않을 수 있다. 아래 C3는 제안의 승리 사례가 아닌 음성 대조다. 이번 판단은 문헌·코드에서 도출한 설계 수정이며 실제 실패 측정은 아니다.

공개 코드에서 pose 후보 export, 카메라 시점 변경, VLA hidden feature 접근은 각각 확인했다. 그러나 posterior 갱신·후보 행동별 성공 label·물리 카메라 이동·VLA 공동 학습이 연결된 실행 패키지는 없다. **1번이 2번보다 구현상 쉽다는 평가는 유보한다.** 2번에는 SpatialVLA의 depth→3D feature라는 구체적 진단 지점이 확인됐다. 다음 선택을 1번 N2로 유지하는 이유는 질문을 좁혀 확인할 가치이지 구현 우위나 출판 가능성의 입증이 아니다.

## 질문과 중요성

**여러 물체 자세가 영상과 양립할 때, 그 모든 자세에서 성공할 공통 행동이 있으면 바로 행동하고, 없으면 필요한 모호성만 줄이는 관측을 VLA가 선택할 수 있는가?** 예를 들어 같은 용기를 단순히 옮길 때와 주둥이 방향을 맞춰 놓을 때는 알아야 할 자세 성분이 다르다. 목표는 pose 정확도 전반을 높이는 것이 아니라, 제한된 관측 시간 안에서 실제 조작 성공을 높이는 것이다.

처음에는 한 팔·한 물체·집기와 방향 정렬 두 과제로 제한한다. 알려진 카메라 calibration과 강체 물체를 가정하고, 관측 가림으로 생긴 물체 자세 모호성에 집중한다. 미지의 카메라 장착·변형체·접촉 물성·동적 SLAM을 동시에 풀지 않는다. 시각적으로 완전히 동일하고 물리적으로도 동등한 대칭은 추가 영상으로 해소할 수 없다. 가려진 손잡이·홈처럼 다른 시점에서 관측 가능한 단서와 구별한다.

## 선행이 이미 해결한 부분

아래는 논문이 지지하는 범위다. 본문 일부 확인과 공식 초록 확인을 원장에서 구분한다. `Learning to Look`은 CoRL 2024 행사 / PMLR 2025 출판이다.

| 직접 선행 | 이미 있는 기여 | 이번 후보에 요구하는 차이 |
|---|---|---|
| [Learning to Look / DISaM](https://proceedings.mlr.press/v270/dass25a.html), [§4.2–4.3·§6](https://arxiv.org/html/2410.18964v1) | IR을 GT context로 BC한 뒤, 추정/GT context의 action-distribution loss로 IS reward를 구성. 배포 시 sampled context별 IR 분포의 평균 pairwise KL과 threshold로 전환 | Pose entropy나 단일 분포의 다봉성과 혼동하지 않는다. 동일 행동 집합의 선호 확률 차이와 실제 성공 가능성 차이를 구별해야 함 |
| [ActivePose, arXiv 2025](https://arxiv.org/html/2509.11364v1), [ActiveODPE, IJRR 2026](https://journals.sagepub.com/doi/10.1177/02783649251411922) | 능동 6D 자세 추정·추적, pose ambiguity 또는 정보 기준의 시점 선택. ActivePose에는 조작 평가도 있음 | 정확한 pose를 얻은 뒤 행동하는 기존 방법과 동일 관측·이동 예산에서 비교 |
| [ActiveVLA, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html), [SaPaVe, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html) | 각각 가상 시점/3D 관심 영역 활용, 카메라 이동과 조작의 공동 학습 | 가상 재렌더링과 새로운 물리 관측을 구별. 카메라+조작을 한 모델에 넣는 것만으로 기여 주장 불가 |
| [RFMPose, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html), [Pose-VLA, RSS 2026](https://roboticsproceedings.org/rss22/p145.html) | 각각 생성적 다중 자세 가설, 공간·궤적 학습용 pose token | 다중 pose 또는 pose token의 존재 자체는 신규성이 아님. 생성 likelihood도 자동으로 보정된 불확실성은 아님 |
| [ATAP, arXiv 2026 §IV-C](https://arxiv.org/html/2609.23504v1) | Top-K registration을 reliability weight로 정규화. Feasible view를 entropy 감소+affordance 검증−이동 비용으로 순위화하고, 미검증 비율/entropy threshold 또는 예산으로 중단 | Multi-hypothesis·task-aware view·stop 모두 선행. Affordance point의 검증과 후보 행동의 closed-loop 성공은 다른 대상이지만 그 차이만으로 기여가 보장되지는 않음 |
| [Naik 등, Industrial Robot 2025](https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF), [preprint §IV–VI](https://arxiv.org/html/2403.10874v1) | Simulator에서 구한 허용 pose 오차 집합을 추정 오차 분포와 적분해 정한 grasp/base pose의 성공 가능성 평가. Grasp 실험은 미리 정한 8개 view 순서를 사용 | 성공 확률로 act/look을 결정하는 발상도 선행. 여러 행동에 lookup을 확장하는 단순 대안까지 비교. 지정 본문은 2024 preprint이며 2025 최종 본문 전체 대조는 아님 |
| [ActiveAlign, arXiv 2026 §III–V](https://arxiv.org/html/2610.23378v1) | 관측 이동 endpoint에서 성공적으로 이어지는 시연을 구성해 VLA를 적응. Matched-state/data-matched 비교와 단일 pre-contact 관측을 다룸 | 새 시점에서 원 VLA가 약해지는 현상을 새 발견으로 주장하지 않음. 동일 continuation 데이터 적응을 비교군에도 적용 |
| [EyeRobot 2.0, arXiv 2026](https://eyerobot2.github.io/) | 고정 stereo 영상의 fixation을 조절하고 gripper BC/action-prediction reward로 gaze 순서를 학습 | RL gaze sequencing 자체는 선행. 정보 filtering과 새 시점 획득은 구별하며 본 후보의 physical camera baseline으로 그대로 대체하지 않음 |

[FoundationPose, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html)는 pose/tracking 기준 모델 후보다. CAD 또는 reference 관측 조건을 맞춰야 하며 그 score를 그대로 posterior 확률로 취급하지 않는다. [AVA-VLA](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html)의 visual attention과 [ActiveScale](https://arxiv.org/html/2609.18514v1)의 카메라 행동 학습도 구별한다. Attention 재가중은 새 물리 관측 획득이 아니다.

## 연구자 해석 — 좁힌 기여 가설

핵심 후보는 **자세 가설 사이의 행동 양립 가능성을 학습하는 표현과 관측 선택**이다. 정책의 출력 분포가 다르더라도 여러 유효한 grasp 중 하나가 모든 자세에서 성공할 수 있다. 반대로 평균 행동이 비슷해도 특정 pose 가설에서는 정렬·삽입에 실패할 수 있다. 이러한 경우를 단순 pose entropy나 action-disagreement와 구별하는 것이 기여의 출발점이다.

설명용으로 언어 지시를 `l`, pose 가설을 `T_i`, **같은 관측과 로봇 시작 상태에서 제안한** 후보 행동을 `a_j`라 한다. `M_ij`는 `T_i`가 실제 상태일 때 `a_j`와 고정된 후속 정책이 목표를 달성하는지 나타낸다. 모든 행에서 성공하는 열이 있으면 현재 후보 안에 공통 행동이 있다. **각 가설의 object frame에서 같은 숫자를 갖는 동작을 실행하면 서로 다른 물리 행동이므로 같은 열로 세지 않는다.** Base-frame control, horizon, continuation, stochastic seed를 맞춰야 한다.

`M`은 사례를 설명하는 정답 표이며 배포 정책에 주어지는 입력이 아니다. 유한 후보에 공통 열이 없다는 사실은 모든 가능한 행동에 해법이 없다는 뜻도 아니다. 초기 deterministic 표는 성공 확률/안전 보증이 아니며, 실제 stochastic dynamics에서는 반복 성공률과 추정 불확실성을 분리한다. **Bayes decision·value of information·허용 오차 공간은 새 이론이 아니다.** `Cθ(history, language, T_i, a_j)` 같은 성공 양립성 예측을 공유 표현에서 학습할 수 있는지, 정확한 simulation lookup보다 무엇을 절약/일반화하는지가 다음 검토 대상이다.

방법 초안은 공유 VLA feature에서 pose 가설별 행동의 성공 양립성을 예측하고, 같은 정책의 행동 출력에서 관측 이동과 조작을 선택하는 것이다. 원시 action sample variance와 상태 추정의 불확실성을 분리한다. Pose estimator는 초기 teacher/비교군으로 쓸 수 있지만 외부 estimator→selector→VLA 연결만 구현했다면 단일 정책 공동 학습으로 표시하지 않는다. RL은 성공과 관측 비용을 학습하는 선택지이며, 먼저 지도 학습·고정 시점·간단한 규칙 대비 필요성을 확인한다.

## 구별 가능한 최소 사례

아래 표는 **손으로 정의한 논리 사례**이며 simulator/데이터 측정 결과가 아니다. `1/0`은 성공/실패를 가정한 표기다. 이 사례가 실제로 가능한지 확인할 asset·관측·기본 정책의 연결은 아직 남았다.

| 사례 | Pose별 성공 집합/관측 조건 | 다른 판단을 요구하는 이유·대조 |
|---|---|---|
| **C1 공통 행동은 있지만 선호가 다름** | 두 pose에서 `{a0,aL}`, `{a0,aR}`. 가설별 정책은 각각 aL/aR을 선호하지만 a0는 양쪽에서 성공 | 분포 KL은 클 수 있지만 a0를 실행할 수 있음. 제안만 가능한 결정은 아니며 **Naik식 후보별 성공 lookup**, shared-support rule도 풀 수 있어 필수 비교 |
| **C2 같은 초기 관측·다른 지시** | C1의 단순 이동 지시를 방향 정렬로 변경하면 `{aL}`, `{aR}`. 추가 view에서 숨은 홈/손잡이가 구별된다고 가정 | 관측 이득이 생길 수 있으나 DISaM/ATAP/task-axis rule도 대응할 수 있음. 지시 의존성/pose representation 검증 사례이며 독립 신규성 증거 아님 |
| **C3 유효한 action multimodality** | 한 pose 또는 모든 context에서 동일한 `{aL,aR}`와 같은 다봉 행동 분포 | Raw sample variance는 높아도 분포 간 KL은 0일 수 있음. **DISaM을 이겼다고 예측하지 않는 음성 대조**. 불필요한 관측 억제만으로 새 기여 주장 불가 |
| **C4 관측으로 해소할 수 없음** | C2처럼 후보 행동이 충돌하지만 허용 view 어디서도 두 상태를 구별할 수 없음 | 관측을 반복해 성공했다고 주장할 수 없음. 예산 종료·실패 보고 또는 명시한 robust 대안. 물리적으로 동등한 대칭이면 애초 목표를 구별하도록 정의하지 않음 |

추가 오류 점검: 서로 다른 pose에서 **똑같이 틀린 행동**을 내는 모델은 KL이 낮아도 실패할 수 있다. 이를 보완하려면 성공 label이 필요하므로 pose 정보의 이득과 extra supervision 효과를 맞춘다. 참 pose가 hypothesis set 밖으로 빠지는 경우도 기록한다. 점수 threshold를 높인 것만으로 proposal coverage/추정 calibration 문제가 해결되지 않는다.

**자산 확인:** 공개 robosuite `SquareNut`에 handle/center site와 pose sensor가 있고 manipulation 환경의 출발점으로 쓸 수 있다. 그러나 원 `on_peg`/success predicate는 위치·높이·EEF 이격으로 판정하며 explicit yaw/contact 조건이 없다. 이를 그대로 ‘정밀 방향 정렬 성공’으로 부르지 않는다. ‘같은 물체를 넓은 곳에 놓기’ 대응 task와 물리 관측 경로, VLA checkpoint competence도 미확보다. 자세별 label을 제대로 만드는 evaluator가 N2의 핵심이다. [고정 source 근거](../재현%20방법/README.md#n1-source-audit).

카메라를 옮기는 동안 물체를 밀거나 grasp 접근성이 달라지면 관측 효과와 물리 상태 변화가 섞인다. 초기에는 비접촉 관측 이동으로 제한하고, 같은 끝 자세·같은 시간의 이동 대조를 둔다. 특정 센서를 추가한 조건만의 이득을 active policy 효과로 주장하지 않는다.

## 비교·평가·수정 기준

- 비교군: 원 VLA/고정 view, 같은 예산의 random view, pose entropy/Fisher-information NBV, DISaM 방식의 context별 action KL, ATAP 방식의 affordance NBV, task-axis rule, 후보별 Naik식 성공 lookup, action probability shared-support rule. 동일 supervision의 별도 작은 성공 예측기와 공유 VLA head를 비교해 fusion의 필요성도 확인한다. 원 논문 재현과 이식 comparator를 구별한다.
- 공정성: 동일 관측 정보·history·checkpoint·학습 데이터·튜닝 예산, 물리 관측 수·이동 시간·추론 시간을 함께 보고한다. CAD/reference/깊이/정답 pose는 정보 수준별로 분리한다. 정답 pose는 evaluator·표시한 oracle에만 제공한다.
- 주요 지표: 동일 총 시간/이동 예산에서 task 성공, 불필요한 관측, 접촉 전 정렬 실패. Pose 오차·confidence calibration은 보조 지표다. 평균 action 거리만으로 양립성을 평가하지 않는다.
- 분할: 같은 mesh의 다른 view를 unseen object로 세지 않는다. 물체/가림/지시 조합을 나누고 모델 선택용 split과 최종 평가를 분리한다. 수치 상한·seed·trial 수는 N1 이후 실행 계약에서 정한다.
- **계속:** 단순 action disagreement와 다른 결정을 요구하는 현실적 사례가 있고 공개 자원으로 통제할 수 있으면 작은 pilot으로 진행한다. 효과 입증을 탐색 진입 조건으로 요구하지 않는다.
- **수정/축소:** task-axis rule이나 기존 허용 오차 평가만으로 충분하면 새 학습 방법 대신 원인 분석의 가치를 재심사한다. Ground-truth pose에서도 기본 정책이 작업을 못하면 먼저 competence/데이터 조건을 수정한다. GPU 부재는 반증이 아니다.

## 석사 연구로서 판단과 다음 행동

**N1는 완료, 방법 채택은 아직 미확립이다.** 네 사례와 source 경로가 생겨 소규모 후속 탐색은 계속할 만하다. ‘1번이 쉽다’는 가정 대신, 1번은 pose 집합·성공 label·물리 시점 제어, 2번은 geometry 개입·좌표 정합·정밀 task evaluator가 각각 부담임을 확인했다. 2번의 frozen depth 개입 진단은 오히려 더 짧은 경로일 수 있다. 연구 잠재력 순위나 실측 자원 비용으로 해석하지 않는다.

**N2에서 위 명세를 완료했다.** 새 배치 task와 고정 view 순서의 ACT/LOOK 비교를 선택했으며 learned NBV는 최초 범위에서 제외했다. P0-PREP에서 custom evaluator/camera/좌표 검증과 pinned VLA candidate IO 코드를 작성했다. 실제 통과 여부는 다음 native P0에서 확인한다. 정상화·기본 행동 능력이 없으면 VLA 명령을 보내지 않고 원인을 기록한다. 성공 label dataset과 방법 학습은 이 초기 검증 이후 별도 pilot이다. Oracle 표만 있고 native 행동 후보를 확보하지 못하면 VLA 방법 효과 주장은 보류하되 최소 사례 구축 자체를 반증으로 취급하지 않는다.

과거 [C1](../../../research_candidates/2026-10-20_vla_rl/C1_REVIEW.md)의 observation shift·이동 비용·기억 부재, [D3-R1](../../../research_candidates/2026-10-22_d3_buildup/R1_REVIEW.md)의 instance/관측/행동 능력 연결 원칙을 반영했다. C1/D3를 재개하거나 기존 HOLD를 해제한 것이 아니다. 실험·학습·외부 연구자 피드백은 미실행이며 N2 완료는 문헌/source 기반 비교 명세 완료만 뜻한다.
