# 단일 VLA 정책의 강화학습과 가치 표현 공동 학습

**U1 투자 판단 — 2026-11-07 기록:** [8개 후보 비교](../../README.md#candidate-priority)의 우선 탐색이다. VLA+RL·단일 정책 방향에 맞지만 일반 actor–critic 간섭 이상의 설명이 남아야 한다. 조건부 실증·분석 가능성과 새 알고리즘 기여 미입증을 구별한다. 당시 후속은 U1 P0였으며, 현재 선택한 별도 보존 분석은 아래 LANGRET 및 [TODO](../../../../TODO.md)를 따른다.

- Updated: 2026-11-12 KST / 기존 U1 연구 검토: **11/06 GAP-UNIFIED-N2 — 내부 비실험 buildup 완료**
- 실행 후속: **11/07 P0-R1 자원 재확인·재개 안내 대조 완료**, native P0는 대기다. 현재 Mac ARM Docker는 대상 환경과 맞지 않으며 [재현 안내](../재현%20방법/README.md#resume)에 실제 경로·dependency·전달 조건을 보완했다. 연구 판단이나 실험 결과의 변경은 없다.
- 판정: **작은 실증 연구 탐색을 유지한다.** 선행 대비 질문·대안 설명·평가·결과별 판단을 정리했으며, 새 방법의 효과나 논문 기여를 입증한 상태는 아니다. 독립 연구자 피드백은 미수신이다.
- [출처와 확인 범위](./sources.json) · [재현 방법·남은 구현](../재현%20방법/README.md) · [전체 후보](../../README.md) · [다음 TODO](../../../../TODO.md)

**11/12 후속 보존 분석 — [LANGRET-N1](#langret-n1)·[N2 비교 설계](#langret-n2) 완료:** 단일 VLA의 RL 후학습에서 지시별 행동 보존을 분석한다. SimpleVLA-RL의 **병렬 이산 행동 토큰** 경로를 선택하고 목표별 평가·초기 능력·분할·단순 대안·비용을 정했다. 이는 공식 OFT의 L1 head나 기존 U1의 AR 정책과 다르다. [P0 실행 준비](../재현%20방법/README.md#langret-p0-preparation)까지 작성하고 Docker 제어 검사22개를 통과했다. 11/12 Mac의 NVIDIA 할당 실패로 native IO/능력/효과는 미검증이며 다음은 호환 local NVIDIA의 P0다. 기존 U1 routing 가설·P0 코드·상한은 그대로다. 아래 11/06 “내부 검토 종료”는 당시 U1 범위다.

## 이번에 바꾼 탐색 방향

사용자는 VLA와 별도 RL controller를 계층적으로 연결하는 방식 외에, **하나의 모델 자체가 보상으로 행동을 개선하는 방향**을 원한다. RL은 별도 모델의 종류가 아니라 학습 방식이다. 따라서 다음처럼 범위를 정한다.

```text
카메라 + 언어 지시 + 허용된 로봇 상태
                   ↓
        공유 VLA 표현 hψ(o, instruction)
             ↙                ↘
       행동 분포 πθ           가치 추정 Vw
             ↓                ↓
       로봇 행동·결과 → RL 학습 신호
                  ↘ 공유 파라미터 ψ 갱신
```

배포 시 행동을 결정하는 정책은 하나다. 학습용 value head, target snapshot, reward evaluator가 있다는 사실만으로 계층형 제어가 되지는 않는다. Head가 둘이라고 독립 controller가 둘인 것도 아니다. 반대로 frozen VLA 옆에 별도 residual policy를 학습하거나 planner의 명령만 RL로 바꾸는 방식은 이번 우선 탐색과 다르다. 모든 파라미터를 처음부터 학습할 필요는 없으며, 공유 backbone의 LoRA도 실제 RL gradient를 받으면 이 범위에 포함한다.

**더 강한 통합**은 같은 가중치가 행동·가치·보상까지 함께 산출하는 것이다. 이는 별도 후보 U2로 두며, 단일 행동 정책을 RL로 학습하는 U1과 혼동하지 않는다. Forward-pass 한 번, 모든 head의 동시 실행, 동일 optimizer 사용을 통합의 필수 조건으로 강제하지 않는다.

## 이미 해결된 것과 남은 질문

아래는 이번 확인 범위의 비교다. 논문에 어떤 분석이 없다고 단정하기보다, 지정한 본문·공식 abstract·code에서 확인한 답과 우리의 추가 질문을 구별한다. 2024–2026을 중심으로 조사했으며 일반 actor–critic 간섭의 원형인 PPG 2021도 대조했다. 출처 전체 목록·version·registry 연결은 `sources.json`에 있다.

| 직접 선행 | 확인한 답 | 이번 질문과의 경계 |
|---|---|---|
| [OpenVLA, CoRL 2024](https://proceedings.mlr.press/v270/kim25c.html), registry pr-0051 | 공개 VLA 정책이라는 출발점 | 단일 VLA 구조를 만드는 것 자체는 새 기여가 아님. 이번에 2024 본문을 재정독하지 않음 |
| [ConRFT, RSS 2025](https://www.roboticsproceedings.org/rss21/p019.html), pr-0885 / [SimpleVLA-RL, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html), pr-0957 | VLA를 RL로 직접 개선하는 선행 | “VLA 자체를 RL로 학습”을 신규성으로 주장할 수 없음 |
| [What Can RL Bring to VLA Generalization?, NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html), pr-0956 | [§4.2](https://arxiv.org/html/2505.19789v2#S4.SS2)는 공유 Transformer와 value head, 별도 critic 비교 및 일반화를 다룸 | Shared actor–critic도 이미 있음. 같은 관측의 목표 구분을 value gradient가 어떻게 바꾸는지는 별도 조건부 질문으로 좁혀야 함 |
| [RLinf-VLA, RSS 2026](https://www.roboticsproceedings.org/rss22/p089.html), pr-0958 | [§IV-C](https://arxiv.org/html/2510.06710v3)는 공유 value head와 action/chunk별 advantage·value 설계를 다룸 | “action별 credit”도 일반 공백이 아님. N1에서 공식 title로 정정하고 기존 ID·folder·검색 alias 유지 |
| [VLAC, ICML 2026](https://proceedings.mlr.press/v306/zhang26if.html) | **최종본 §3, §4.6–4.7, pp.8–9 대조 완료.** 단일 action/progress 구조, progress 사전학습 대조, reward·value·action logits를 이용한 PPO를 명시 | 2025 preprint의 2B actor·8B reward·별도 critic 설정을 최종본에 전사하면 안 됨. 통합 학습 자체는 선행이다. 최종본 문장만으로 모든 출력의 동일 optimizer·reward branch 갱신 여부까지 확정하지 않음 |
| [Actor–Critic Representation Interplay, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html) / [PPG, ICML 2021](https://proceedings.mlr.press/v139/cobbe21a.html) | 정책·가치 표현의 전문화와 공유/분리 trade-off, phasic optimization을 이미 연구 | 일반 gradient conflict 진단·detach·PPG 적용만으로 독립 기여라고 할 수 없음 |
| [Should the Action Expert Train the VLM?, 2026 preprint](https://arxiv.org/html/2611.05249v1) / [TEMPO, 2026 preprint](https://arxiv.org/html/2608.07314v1) | 전자는 action supervision×gradient routing, 후자는 frozen VLM·semantic/action 두 TD3 loop와 update frequency를 다룸 | Action-expert gradient와 state-value loss gradient는 다름. 그래도 “얼마나 함께 학습하나”라는 넓은 주장은 직접 충돌함 |
| [After Cooperation Is Learned, 2026 preprint](https://arxiv.org/abs/2610.01630) / [ADAPT, 2026 preprint §4.3·App.C](https://arxiv.org/html/2610.15956v1) | 전자는 shared value-gradient 유무와 reward scale을 통제. 후자는 audio-depth navigation에서 shared backbone의 critic stop-gradient를 사용 | Routing 대조 자체를 새 방법으로 포장하지 않음. VLA의 언어 목표 구분에서 추가로 설명할 조건·행동 근거가 필요 |

**중요한 구분:** VLAC의 progress reward, PPO의 state value, Q-function은 역할과 학습 target이 다르다. 이름에 critic이 있다는 이유로 같은 loss·같은 실험으로 취급하지 않는다. 공식 venue는 위 main-conference source로 확인했고 나머지는 preprint로 둔다. 블로그·AI 자동 리뷰의 평가를 근거로 채택하지 않았다.

**N2에서 확인한 추가 충돌:** RL4VLA의 [§5.1–5.3](https://arxiv.org/html/2505.19789v2#S5)은 이미 multi-object·instruction phrasing·semantic generalization을 평가한다. “두 물체 중 지시된 물체를 집는 평가”도 새로운 benchmark라고 부를 수 없다. ICLR 표현 연구의 [§5–6](https://arxiv.org/html/2503.06343v1#S6)은 value 표현의 도움과 데이터 다양성, critic에 의한 수집 분포 변화를 구별한다. 따라서 U1은 **동일 초기화·동일 행동 모델에서 value-gradient 경로를 바꿀 때 목표별 행동이 어떻게 달라지며, 그 차이를 무엇이 설명하는가**에 한정한다. 확인한 범위에서 남은 질문이며 세계 최초라는 판정은 아니다.

공개 코드도 범위를 확인했다. [VLAC revision](https://github.com/InternRobotics/VLAC/tree/0f302d020555e320347c55b09431afe17ef5cdd4)의 54-file tree와 action example/model utility는 추론 interface를 제공하지만 조사한 tree에서 최종 PPO 학습 경로는 식별하지 못했다. 이는 논문에 통합이 없다는 증거가 아니다. [ICLR 표현 연구 코드](https://github.com/francelico/deac-rep/tree/4dd611159eabd21b1a67cc80acbd09dafb38a3b3)의 shared/separate PPO entry를 대조했으며 별도 critic parameterization을 현재 B의 value-only detach와 동일시하지 않았다. 코드에 선언된 detach 인자의 존재만으로 실행 경로가 구현되었다고 추론하지 않는다. 확인 위치·hash는 `sources.json.nonexperimental_review`에 있다.

## 공백 후보 세 가지

| 순위·상태 | 질문 | 가능한 기여와 가장 큰 위험 |
|---|---|---|
| **U1 — 우선 탐색** | 공유 VLA에서 value loss가 표현을 바꾸는 것이 언제 목표에 맞는 행동을 돕고, 언제 장면 shortcut을 강화하는가? | 언어 지시가 실제 행동을 구분해야 하는 조건에서 공동 학습의 이득/손실을 설명하고, 필요하면 그 조건을 반영한 학습법으로 발전. 단순 loss scale·일반 actor–critic 현상의 재현에 그칠 위험 |
| **U2 — 더 강한 통합의 예비 후보** | 같은 가중치로 행동과 progress reward를 출력하면서 정책을 개선하면, 보상 판단도 함께 움직여 실제 성공과 어긋나는가? | Shared self-evaluation의 안정성·학습 분리 시점에 관한 지식. 독립 성공 evaluator 없이 자기 점수만 올라가면 판단 불가. 일반 reward hacking·self-rewarding의 반복이 될 위험 |
| **U3 — 낮은 우선순위** | 단일 VLA가 학습한 행동 중 실제 실행된 구간에 맞춰 RL credit을 주면, 고정 action/chunk credit보다 언제 유리한가? | 실행 horizon과 학습 신호 정합성. [Temporal GRPO](https://arxiv.org/html/2608.13026v1), [AtomicRL](https://arxiv.org/abs/2610.30097), RLinf-VLA와 직접 겹침. Stage decomposition이나 prefix mask만 추가해서는 부족 |

**추천은 U1의 작은 진단을 시작하는 것**이다. 이는 출판 가능성 확정이나 세 주제의 동시 구현 권고가 아니다. U2가 사용자가 원하는 가장 강한 의미의 통합에 더 가깝지만, 보상·정책의 공동 변화까지 식별해야 하므로 첫 석사 주제로는 구현과 검증 부담이 더 크다. U1에서는 외부 reward evaluator를 고정해 문제를 줄인다.

다음 넓은 방향은 현재 새 gap으로 채택하지 않는다: 일반 continual forgetting은 [Simple Recipe Works](https://arxiv.org/html/2603.11653v3)의 강한 단순 baseline이 있고, temporal critic은 [WCM](https://arxiv.org/html/2607.29613v1), instruction-grounded offline reward는 [CounterAlign](https://arxiv.org/html/2608.21740v1)이 직접 다룬다. 이들의 존재는 좁은 후속 질문을 금지하지 않지만 해당 기여를 다시 주장하는 것은 막는다.

## U1의 문제·질문·짧은 논문 이야기

**문제:** 같은 테이블에서 “빨간 컵을 옮겨라”와 “파란 컵을 옮겨라”는 서로 다른 행동을 요구한다. 보상으로 VLA를 개선할 때, 성공을 예측하는 표현이 목표 선택에 필요한 정보를 강화할 수도 있고 장면과 성공의 상관관계만 강화할 수도 있다. 한 모델로 효율적으로 학습하면서 이 차이를 알아야 한다.

**주 질문 — 연구자 가설:** 같은 pretrained VLA·trainable parameter 집합·reward에서, value gradient를 공유 표현까지 전달할 때의 효과는 **관측이 비슷해도 지시가 요구 행동을 바꾸는 정도**에 따라 달라지는가? 단순 학습률·value-loss 크기·reward scale 조정 이후에도 그 차이가 남는가?

**반대 가설도 열어 둔다.** 공유가 대부분 더 좋을 수 있고, LoRA·normalization·학습률 조정만으로 충분할 수 있다. RL이 언어를 반드시 망친다고 전제하지 않는다. 관측된 차이가 일반 actor–critic 간섭과 구별되지 않으면 기존 지식의 VLA 재현으로 범위를 줄인다.

**논문 기여 후보:** 단일 VLA 공동 학습에서 가치 예측 정확도와 목표별 행동 정확도가 함께 좋아지는 조건, 또는 서로 어긋나는 조건을 밝히는 실증 연구. 반복 가능한 조건이 보이면 그때 value supervision·parameter update의 개선을 제안한다. 새로운 head, stop-gradient, PCGrad 또는 loss 항 하나를 붙이는 행위 자체를 기여로 삼지 않는다. Robot goal selection·task success를 바꾸는 근거가 핵심이다.

<a id="nonexperimental-completion"></a>
## U1의 비실험 검토 결론과 비교 설계

**내부 설계 검토는 여기서 종료한다.** [7단계 buildup 과정](../../../../research/IDEA_BUILDUP_GUIDE.md)에 맞춰 다음 관측이 판단을 바꿀 수 있을 만큼 구체화했다. 아래 P1 이후는 **미실행 연구 설계**이며 P0 실행 계약을 확대하지 않는다. 환경·checkpoint·hash·P0 한도는 [재현 방법](../재현%20방법/README.md)의 기존 계약을 따른다.

| 항목 | 현재 정한 비교 |
|---|---|
| 시작 모델 | RL4VLA의 OpenVLA warm-up 계열 우선. 원 모델은 autoregressive action token 정책이며 OpenVLA-OFT·π0.5로 임의 대체하지 않음 |
| 모델 | `hψ(o,l) → πθ(·;h), Vw(h)`; 하나의 행동 정책. 같은 LoRA 위치/rank·행동/관측/normalizer 유지 |
| A — joint | 원 shared actor–critic loss. 정책 loss와 value loss가 모두 허용된 공유 ψ에 gradient 전달 |
| B — detached value | `Vw(stopgrad(hψ))`. Value head의 forward·target·optimizer는 유지하고 value loss의 ψ 경로만 차단. Policy gradient는 계속 ψ를 갱신 |
| C — 단순 조정 | A에서 value-loss coefficient/return normalization을 작은 개발용 범위로 조정. Parameter 수·추가 데이터는 동일. 일반 간섭의 대안으로 PPG/gradient surgery는 현상이 남을 때 추가 |
| 개발 사례 | 같은 물리 장면의 carrot/kitchen shovel과 plate, 두 유효 지시를 균등 평가. 이 한 쌍은 개발용이며 논문 범위 전체가 아님. 물체별 조작 난이도·초기 능력은 미확인 |
| 먼저 구별할 효과 | 같은 저장 transition·동일 old log-prob·고정 return/advantage로 짧은 update 비교: 직접 표현 갱신 효과. 이후 각 조건의 online rollout으로 전체 학습 효과. 둘을 같은 인과 추정이라고 쓰지 않음 |
| 목표 target | 잘못된 지시로 바꾼 transition에 원 return을 그대로 붙이지 않음. Value target은 해당 지시 아래의 continuation policy에 의존. 반사실 지시 쌍은 먼저 행동 평가용이며 값 label 생성은 별도 근거 필요 |
| 주 측정 | **목표 균등 native task success의 A−B 차이**. 최초 목표 선택·두 목표 동시 충족률·학습 곡선은 아래 정의의 보조 측정. Value error·policy KL·gradient 방향만으로 언어 손상을 주장하지 않음 |
| 공정성 | 같은 초기 가중치·reward·관측·trainable 집합·seed 체계·환경 interaction 수. Actor/critic의 실제 optimizer update 크기, clipping, 학습시간/메모리도 기록. Online 학습 후 방문 상태 차이는 결과의 일부 |
| 반복·분할 | 개발 장면과 평가 장면/목표 조합 분리. Pilot은 코드/현상 발견용, 최종 효과 주장은 새로운 평가 episode와 반복 training seed의 불확실성으로 판단. 프레임을 독립 trial로 세지 않음 |

여기서 value head를 없앤 GRPO와 A를 비교하면 estimator·sample 구성도 함께 바뀐다. 이는 routing의 직접 대조가 아니므로 1차 A/B를 대신하지 않는다. 별도 큰 critic도 정보량·capacity·compute가 달라 1차 비교에서 분리한다. 감도·gradient cosine만 달라지고 행동이 같으면 robot learning 개선을 주장하지 않는다.

### 평가 단위·지표·분할

1. `Y[m,s,j,g,r]`는 arm m·training seed s·물리 layout j·목표 g·rollout seed r의 native completion이다. **80 control-step horizon 내 한 번이라도 native success이면 1**, 아니면 0. 마지막 step 값도 별도 저장한다. Native contact 정의를 유지하며 release·안정적 placement 성공으로 확대하지 않는다. Crash/OOM/asset 누락은 정책 실패 0으로 섞지 않고 invalid 실행과 발생 수를 보고한다. 인프라 수정 후 영향받은 paired 비교를 함께 재실행하고 일방적인 성공 재시도는 금지한다.
2. 주 효과는 각 layout·seed에서 두 목표를 같은 비중으로 평균한 뒤 A−B를 계산한 값이다. 두 목표가 각각 성공했는지의 `Y[g0] × Y[g1]` 평균도 보고한다. 한 번의 rollout에서 두 물체를 모두 놓으라는 과제는 아니다. 한 목표만 잘해서 평균이 오른 경우가 드러나도록 목표별 표를 반드시 병기한다.
3. 최초 grasp event는 매 control step의 side-effect 없는 관측에서 **correct / wrong / simultaneous / no-grasp** 중 하나로 분류한다. 최초 둘 다 grasp면 simultaneous를 유지하고 나중에 단독이 된 순간을 최초 event로 바꾸지 않는다. 분모는 모든 valid rollout이며 “집기에 성공한 episode만”의 정확도를 주 지표로 쓰지 않는다. 현재 observer는 순간 상태만 구현되어 있어 event 집계는 P1 구현 대상이다.
4. 동일 물리 시작 상태·controller buffer·RNG를 검증해 두 지시 branch를 만든다. State fork가 검증되지 않으면 matched-scene이라고 부르지 않고 reset 매칭 오차부터 교정한다. 같은 장면의 지시 쌍, 연속 frame, 반복 결정적 rollout은 독립 scene 수가 아니다.
5. N1의 pos 0–3 dev / 4–19 train / 20–27 eval은 **후보 목록**이다. 실행 시 객체 identity·pose·robot/controller·camera·asset revision을 포함한 canonical state 기록을 만들고, goal label을 제외한 physical key로 중복을 묶는다. 역할만 바뀐 배치가 다른 split으로 새지 않도록 unordered geometry family도 함께 묶는다. 허용 오차는 dev의 reset 정밀도로 정해 eval 전 봉인한다. 부족하면 계획 수를 줄여 보고하고 eval 성공 여부로 보충하지 않는다. 실제 manifest·중복 제거는 아직 수행하지 않았다.
6. 발견용 고정-batch 진단과 설정 선택은 dev에서만 한다. 최종 비교의 policy training에는 train rollout만, 최종 평가는 봉인한 eval layout만 사용한다. 동일 object/scene family 내부의 배치 holdout이지 unseen object/embodiment 또는 pretraining 독립성 보장이 아니다. 논문 규모에서는 새 object pair·layout family를 추가하고, 발견에 쓴 pair의 결과와 분리한다.

### 단순 대안과 구별하는 순서

| 경쟁 설명 | 먼저 할 최소 대조 | 남겨야 할 해석 |
|---|---|---|
| Carrot만 원래 잘 다룸 / 다른 목표 불가능 | 학습 전 목표별 성공과 planner feasibility를 따로 확인. 두 목표·위치 역할을 균형화하고 능력 차이를 공개 | Oracle 성공은 VLA 능력의 증거가 아님. 초기 구분 능력이 없으면 retention 대신 acquisition 질문 |
| 새 value head의 초기 오차 때문에 생긴 일시적 간섭 | Cold-start 비교를 먼저 명시. 차이가 초기 구간에만 있으면 고정 base policy의 실제 rollout return으로 head만 준비한 공통 초기화도 비교 | Head 준비 데이터·update 비용을 모든 arm에 동일 계상하고 shared VLA는 이 단계에서 고정. 해결되면 초기화/스케줄 문제이며 지속적 언어 간섭이 아님 |
| Value loss가 단순히 너무 큼 | 먼저 A/B/C; 신호가 있으면 joint·detach 각각 λ={0.01,0.1,1}을 같은 dev 예산으로 비교 | C 하나만으로 모든 scale 대안을 배제하지 않음. λ는 head update도 바꾸므로 온라인 결과는 순수 방향 효과가 아님 |
| Clipping/AdamW가 actor step 크기를 바꿈 | 공통 group별 clipping, 실제 parameter delta·policy KL 기록; dev에서 actor lr 0.5×/1×/2× 감도와 joint-clip A0 비교 | Step 크기로 설명되면 optimizer recipe. Norm-matched 비교도 방향/전처리 효과를 완벽 분리하는 증거는 아님 |
| Return 단위·hidden history·critic 오차 | Train-only return normalization을 양쪽에 동일 적용; grasp 이력별 value error·행동 결과를 함께 분해 | 정규화된 old value/target/clipping 단위도 정합화. History를 critic에만 주는 진단은 privileged-information ablation이며 공정 주 baseline이 아님 |
| Critic이 advantage와 수집 분포를 바꿈 | 고정 genuine batch 한 update와 별도 on-policy 학습을 구분. 후자에서 목표별 방문·성공/실패·GAE 통계를 저장 | Detach여도 critic→advantage→policy 경로는 남음. Online 차이를 직접 shared gradient의 기제로만 설명하지 않음 |
| 일반 공유 표현 간섭 / 배치 다양성 차이 | 위 대조 후 신호가 남으면 PPG 및 별도 critic을 compute·입력·capacity와 함께 비교 | 기존 방법이 해결하면 해당 조건의 분석으로 축소. PPG는 sample reuse·batch 다양성도 바꾸므로 경로 하나의 대조가 아님 |
| 언어 문제가 아니라 두 물체의 혼잡·난이도 | 같은 장면에서 목표를 균등 전환하는 평가를 우선. Single-object 대조는 보조 진단 | Single/multi-object 차이는 geometry도 변하므로 “언어 필요성의 인과 효과”가 아님 |

모든 대조를 첫 pilot의 입장 조건으로 요구하지 않는다. **A/B/C → 신호·학습 유효성 확인 → scale/optimizer/이력 → 주장에 필요한 기존 방법** 순서로 진행한다. Tuning 설정 수·각 설정의 interaction 수·선택 기준을 두 routing 방식에 같게 배정한다. Head lr 추가 탐색이 필요하면 양쪽에 동일한 횟수를 제공한다. Return normalization은 기존 P0 코드에 구현된 것으로 표시하지 않는다.

### 언어 의존 조건을 더 강하게 주장하려면

첫 A/B 차이는 정해진 과제에서 routing의 행동 효과만 말한다. “언어가 필요한 조건이라서 효과가 달라진다”로 확대하려면 **routing × 목표 배정 규칙**을 후속 factorial로 비교한다. 같은 두 물체와 물리 배치 분포에서 H는 각 layout의 두 목표를 50:50 배정하고, L은 화면상 왼쪽 물체가 항상 목표가 되도록 배정한다. 객체의 좌우 배치를 균형화해 목표 identity의 주변 빈도는 같게 하고, instruction은 매번 진짜 목표를 서술한다. Tie는 dev의 사전 규칙으로 제외한다. 두 조건 모두 최종 평가는 같은 균등 목표 쌍에서 수행한다. 기존 transition의 지시·return을 바꾸는 방식으로 만들지 않는다.

`I = (success_A − success_B)_H − (success_A − success_B)_L`는 **훈련 중 목표와 장면의 상관을 바꾼 개입과 routing의 상호작용**이다. 언어 의미의 순수한 인과 효과나 shared 표현 내부 기제의 식별은 아니다. H/L별 실제 데이터·학습 난이도·초기 능력을 보고하고, 좌우 균형을 만들 수 없으면 이 실험을 미수행으로 남긴다. 현재 한 carrot/shovel 배치와 P0 adapter가 이 factorial을 지원한다고 가정하지 않는다. 이후 다른 shortcut 규칙이나 새 object pair에서 예측이 맞는지가 분석 기여의 확장 근거다.

### 반복·불확실성·예산

- Pilot은 3개 독립 training seed를 계획하며, 모든 seed 결과와 목표별 차이를 공개한다. 같은 seed 번호로 A/B를 짝짓되 RNG가 분기 후 같은 trajectory를 만든다고 가정하지 않는다. Seed는 학습 변동, layout은 조건 변동이므로 두 축을 분리해 보고한다. 한 checkpoint의 많은 frame으로 학습 반복 수를 늘리지 않는다.
- 확증 단계는 pilot과 분리한 새 seeds·eval을 사용한다. 목표 수/scene 수/seed 수는 pilot 분산과 **관심 최소 차이 5 percentage points**를 기준으로 고정한다. 5 pp는 이번 계획의 실용적 기준이지 문헌상의 표준·사전 power 계산 결과가 아니다. 3 seeds만으로 5 pp를 검출할 수 있다고 주장하지 않는다.
- 충분한 반복에서는 training seed와 layout을 각각 cluster로 재표집하고, 그 내부 goal/arm/rollout pairing을 유지하는 bootstrap 95% 구간을 계획한다. 적은 seed에서는 seed별 표·범위를 우선하고 bootstrap 정밀도를 과신하지 않는다. A−B native success를 주 contrast로 고정하고, 추가 metric/조건은 exploratory로 표기한다. 유의하지 않다는 이유로 동등·효과 없음이라 하지 않는다. 동등성은 사전 ±5 pp 범위 안으로 불확실성 구간이 충분히 좁아질 때만 별도 판단한다.
- 최초 P1 계획 한도는 **dev 4 layouts × 2 goals × (planner 1 + base policy 2 rollout seeds) = 24 episodes, 각 ≤80 control steps**다. 최소 feasibility 확인용이며 성공률 확증 표본이 아니다. 모델 query/physics/wall-time 상한은 P0의 실제 측정 후 P1 실행 계약으로 봉인해야 한다.
- 이후 고정-batch 진단은 개발 자료의 genuine transition을 사용해 **한 update 후** 행동 변화를 측정한다. 원 instruction·old logits/value·return/advantage·optimizer snapshot을 공유하고 head/LoRA 초기화를 매 arm 복원한다. P0의 인공 target은 재사용하지 않는다.
- On-policy의 첫 비용 점검은 A/B/C × 3 seeds × 최대 10,000 control steps = **90,000 training steps**를 계획 상한으로 둔다. 평가·tuning·oracle 비용은 별도 계상하며 full PPO run 허가나 수렴 보장이 아니다. 이 구간에서 두 목표 학습이 안 되면 “차이 없음” 대신 학습 기회 부족으로 판단한다. P0/P1 측정치로 GPU 시간·peak memory·저장량을 계산한 후 별도 runtime 계약을 만든다. RL4VLA가 보고한 A100 학습 시간을 우리 설정의 소요 시간으로 복제하지 않는다.

### 결과에 따른 투자 결정과 논문 이야기

| 관측될 수 있는 결과 | 판단·다음 행동 |
|---|---|
| 실행/feasibility 실패 | 환경·evaluator·목표 쌍 교정. 가설 반증으로 처리하지 않음 |
| 초기 한 목표 능력 부족 | Acquisition으로 문제를 명시적으로 수정하거나 dev에서 양쪽 능력을 갖춘 pair 선정. Eval 사례를 보고 고르지 않음 |
| A 또는 B가 안정적으로 유리하고 단순 조정 뒤에도 조건별 차이 존재 | 실증·분석 후보 유지. 새 object pair/학습 조건에서 예측 검증; 방법은 필요한 경우에만 개발 |
| C·lr/normalization만으로 충분 | 간단한 recipe 또는 조건부 분석으로 축소. 복잡한 새 방법을 만들 동기는 약해짐 |
| Value error/cosine만 다르고 행동은 같음 | 표현 진단만 기록. Robot learning 기여 근거는 부족 |
| 모든 조건에서 일반 actor–critic 결과를 반복 | 이 VLA 설정의 재현 결과로 보존. 언어 특이적 원리/새 방법 주장 중단 |
| 넓은 구간의 무차이 / 모든 arm 미학습 | 결론 불충분. GPU 부재와 구별해 표본·학습 예산의 판단 문제로 기록 |
| 충분한 정밀도로 작은 차이, 공동 학습이 안전한 범위가 반복됨 | 실용적인 negative/conditional result 가능. 중요 범위·비용·일반화가 있어야 논문 가치가 생기며 자동 GO는 아님 |

**가제:** *When Does Value Learning Help Instruction-Conditioned Action Selection in Vision-Language-Action Policies?*

**짧은 논문 이야기 — 결과 빈칸 유지:** 한 VLA를 보상으로 개선할 때 공유 value supervision은 계산 효율을 주지만 목표 구분 행동에 주는 영향은 설정별로 확인해야 한다. 같은 초기화와 실제 목표 쌍에서 gradient 경로를 대조하고, loss 규모·최적화·수집 분포·조작 능력으로 설명되는 범위를 구분한다. 결과가 뒷받침하면 어떤 조건에서 공동 학습을 선택해야 하는지와 적용 범위를 제시한다. 예정 그림은 ① 목표별 task success 및 두 목표 pair 결과, ② scale/optimizer 대조 뒤 남는 차이, ③ 새 조건에서의 예측 검증이다. 숫자·우월성·기제는 아직 채우지 않는다.

**석사 연구의 공수 점검:** GPU 확보 후 첫 1주를 native build/IO·gradient 및 P1 구현 가능성 점검 시점으로 잡는다. 완료 약속이 아니며 실패 지점과 추가 공수로 범위를 조절한다. 다음 단계도 최초 90,000-step 계획을 자동 실행하지 않고 측정된 비용으로 검토한다. 최소 탐색은 한 모델·한 플랫폼에서 시작하고, 일반 VLA 학습 원리로 확대할 때 다른 object/task family와 추가 모델의 근거를 요구한다. 실로봇 전이를 주장하려면 실로봇 평가가 필요하다. 논문 가치를 확보하려면 GPU 외에도 후속 trainer·event evaluator·state fork 구현과 연구실의 실험 지원이 필요하다.

## 기존 후보와의 관계

기존 **VRL**은 base 정책 교체와 residual 재사용 문제여서 이번 통합 선호와는 거리가 있다. 버리지 않고 준비 상태를 보존한다. **FEEDBACK**은 이미 RL로 개선된 VLA의 관측 활용을 평가하는 진단이므로 U1의 행동 평가에 참고할 수 있다. 다만 FEEDBACK의 공개 RL/SFT checkpoint 차이를 U1의 동일 초기화 학습 대조로 대체할 수 없다. **REVISION**은 VLA 단독 상호작용 대안, 나머지 후보도 기존 판단을 유지한다. 초기 cross-robot RL 전이 RETIRED 주제를 이름만 바꾸어 재개하는 작업이 아니다.

<a id="n1-review"></a>
## N1 결과 — 실험 전에 줄인 불확실성

**U1의 작은 탐색을 계속할 근거는 있다.** 공개 source에서 동일 모델의 공동/분리 gradient를 비교할 지점과 두 물체가 함께 있는 환경을 확인했다. 다만 목표 쌍의 실제 조작 가능성·초기 정책 능력은 아직 없다. 후속 P0-PREP에서 goal adapter·gradient probe 초안을 작성했지만 native 교정은 남아 있다.

1. **학습 초기화 연결:** RL4VLA warm-up의 HF revision, config/normalizer/processor 및 원격 weight hash를 고정했다. 공개 파일은 merged weight이며 기존 LoRA/optimizer state를 포함하지 않는다. 새 rank-32 LoRA와 value head로 A/B/C를 시작하는 controlled adaptation으로 규정하고 원 논문 학습의 정확한 재현이라고 부르지 않는다.
2. **Gradient 대조 보완:** 원 joint clipping은 detach 조건에서도 value-head gradient가 actor step 크기를 바꿀 수 있다. 주 비교는 세 조건에 같은 group별 clipping을 적용하고, 원 clipping을 별도 sensitivity로 둔다. Value head의 a0는 첫 action을 예측하기 전 위치여서 action-conditioned a6와 구별한다.
3. **목표 후보를 실제 asset에 연결:** `PutOnPlateInScene25MultiCarrot-v1`, episode 0의 carrot/kitchen shovel/plate를 선택했다. 목표마다 새 reset을 하면 배치가 달라진다. 하나의 상태에서 goal binding만 바꾸는 adapter가 필요하며, 이 후보를 양쪽 성공 witness로 승격하지 않는다. 초기 warm-up이 두 물체를 다루지 못하면 “능력 보존”보다 “목표 구분 습득” 질문으로 수정한다.
4. **평가기·추정 대상 분리:** native contact 기반 success와 최초 grasp의 목표 선택을 함께 본다. Native success는 release/stable placement와 다르다. 고정 batch 한 update와 arm별 on-policy 학습은 다른 효과를 추정한다. Instruction/return 재라벨링 금지, split dedup, simple loss-scale baseline, P0 상한까지 [재현 계약](../재현%20방법/README.md)에 기록했다.
5. **직접 선행 등록:** [VLAC, pr-1111](../../../../2026/ICML/2026_ICML_A-Generalist-Pair-wise-Progress-Critic-Model-for-Vision-La/01_overview.md), [actor–critic 표현 연구, pr-1112](../../../../2025/ICLR/2025_ICLR_Studying-the-Interplay-Between-the-Actor-and-Critic-Repres/01_overview.md)를 NEXT에 추가했다. 5-note는 공식 abstract 범위, 사용자 status는 UNREAD다. 이전 preprint에서 읽은 설정을 최종 ICML 결과로 전사하지 않았다.

**과학적 위험은 그대로다.** Shared critic·detach 자체는 기여가 아니며, C의 loss scale이나 일반적인 clipping 현상으로 설명되면 독립 방법 연구의 근거는 약하다. N2에서는 단일/다중 물체 차이만으로 언어 특이성을 주장하지 않도록 교정하고, 목표 배정과 routing의 상호작용을 별도 후속 설계로 두었다. 새 모듈을 먼저 만들지 않는다.

또한 원 reward는 grasp 이력을 누적하는 반면 value 입력은 단일 RGB+instruction이다. 숨은 과거 상태에 따른 value 오차가 의미 구분 문제처럼 보일 수 있다. 이를 대안 설명으로 남기며, value error만을 언어 손상의 증거로 사용하지 않는다.

<a id="langret-n1"></a>

## LANGRET-N1 — 지시별 행동 보존의 직접 선행·공개 비교 심사

- 검토일: 2026-11-12 / **N1 문헌·정적 source 심사 완료, 좁은 탐색 유지**. 독립 방법 GO나 전체 비실험 buildup 완료는 아니다.
- [탐색 당시 세 후보 비교](../../../update/VLA_MASTERS_GAP_SCOUT_2026-11-12.md), [공통 원장의 `n1_review`](../../../sources/vla_masters_gap_scout_2026-11-12.json), [목표쌍·입출력 확인 범위](../재현%20방법/README.md#langret-source-review)를 연결한다.

### 판정: 독립 방법 후보로 분리하지 않고 후속 분석으로 통합

**지금은 12번째 주제를 만들지 않는다.** 후학습 이후 다른 지시 수행 능력 보존은 RL’s Razor·DeLock·TEMPO·CounterAlign과 직접 연결되고, 단순 KL/replay·동결·목표별 데이터 구성 이상의 독립 방법은 아직 없다. 같은 장면의 목표 구분이라는 평가 기반도 U1과 겹친다. 따라서 단일 VLA 후학습이라는 기존 주제 안에서 보존 분석을 관리한다. 이는 GPU 부재나 코드 미공개로 연구를 기각한 판단이 아니다. 새 모듈 없이도 학습 선택을 바꾸는 조건 분석은 탐색할 수 있다.

**두 추정 대상은 구별한다.** U1은 동일 학습 설정에서 value-gradient routing의 차이를 묻고, LANGRET은 고정된 학습법으로 적응하기 전후 기존 목표 수행이 어떻게 달라지는지 묻는다. 한쪽의 결과를 다른 쪽의 인과 설명으로 쓰지 않는다. 먼저 보존 변화와 측정의 타당성을 확인한 뒤, routing은 가능한 설명 중 하나로만 비교한다. 기존 P0를 LIBERO로 바꾸거나 기존 carrot/shovel scene을 새로운 두 목표쌍으로 대체하지 않았다.

### 직접 충돌과 공개 구현의 실제 상태

| 선행·확인 위치 | 이번에 확인한 점 | 질문에 미치는 영향·구현 경계 |
|---|---|---|
| [RL’s Razor ICLR 최종본](https://proceedings.iclr.cc/paper_files/paper/2026/file/618c95f4557c15b253fb0e6f548ea0c0-Paper-Conference.pdf), §3–5, App.A, C.2 pp.22–23 | 최종본에서도 OpenVLA/SimplerEnv can 적응→drawer 보존, reward-normalized REINFORCE·명시적 KL 없음. Empirical predictor의 forward KL과 정리의 reverse KL을 구별해야 함 | 새 과제 성능을 맞춘 보존 비교는 선행이다. 로봇 설정은 이전 v1 B.2와 같은 범위로 확인했지만 전체 버전 diff는 아님. [저자 페이지](https://jyopari.github.io/posts/rl_razor)에서 공식 robot training code는 식별하지 못했으며 제3자 MNIST 재현을 대체 코드로 쓰지 않음 |
| [DeLock v1](https://arxiv.org/html/2604.23121v1), §3–4·App.A/C | SFT 이후 concept/spatial lock-in, visual weight-drift regularization·두 prompt의 flow guidance·frozen-visual ablation | 같은 물체/목적지 대비 자체가 새 평가가 아님. [저자 페이지](https://suninghuang19.github.io/delock_page/)는 **Code Coming Soon**. 알고리즘 대조와 실행 구현 확인을 구분 |
| [TEMPO v1](https://arxiv.org/html/2608.07314v1), §III·IV-B Table IV | Frozen VLM·semantic/action TD3 및 1/2/4/7/34개 학습 subtask 비교를 이미 수행. 5개 subtask rollout 중 선택한 task의 transition만 학습에 사용 | “후학습 목표 수·구성을 바꾸면 보존이 달라진다”는 broad 주장도 중복 위험. 동일 상태 목표쌍·동일 총비용·보존 기준의 충분성으로 좁힘. [공개 링크](https://anonymous.4open.science/r/TEMPO-RL/README.md)는 존재하지만 이번에 source body를 확보하지 못함; API 403. **미공개로 단정하지 않음** |
| [CounterAlign v1](https://arxiv.org/html/2608.21740v1), §3.2–3.3·App.2/6 | 의미가 모호한 negative를 구별하고, critic에는 near-positive 지시 재표기, actor에는 advantage-weighted flow matching 사용 | 다른 지시의 action을 모두 negative로 두지 않음. Flow의 log-likelihood를 직접 계산하기 어렵다고 논문도 명시. [연구실 페이지](https://research.airoa.io/publications/counteralign/)는 **Code Coming Soon**; OpenReview 재접속 실패는 기존 CoRL 기록을 취소하는 근거가 아님 |

**한층 좁힌 질문:** 같은 물리 상태에서 두 유효 목표를 수행할 수 있던 정책에 대해, 학습 분포의 정책 변화량과 일반 replay가 **지시별 보존을 판단하는 데 충분한가**? 평균 적응 성능·총비용을 맞춘 뒤에도 특정 목표를 놓치는 조건이 남는지 확인한다. 단지 분포 밖 일반화가 보장되지 않는다는 일반 사실을 재발견하는 것은 기여가 아니다. 실제로 어떤 checkpoint·학습 설정을 선택할지가 달라져야 한다. 논문 근거는 일반 RL 보존 이점을 지지하므로 “RL이 언어를 파괴한다”는 서사를 미리 정하지 않는다.

### 확인한 두 장면과 아직 확인하지 못한 능력

1. **물체 선택:** 같은 `libero_cf_spatial/01` 장면에서 cookie box 또는 ramekin을 같은 plate에 놓는 두 지시. 두 object·plate 선언, 초기 배치와 두 predicate가 source에 존재한다.
2. **목적지 선택:** 같은 `libero_cf_long/05` 장면에서 yellow/white mug를 left plate 또는 right plate에 놓는 두 지시. `plate_1/plate_2`와 좌우 region binding이 source에 존재한다.

이는 **source에 근거한 목표쌍 후보 두 종류**다. 두 prompt를 같은 상태에서 실행한 증거는 없다. 두 번째 prompt는 확인한 object/predicate에 맞춰 작성한 연구용 대조이며, 원 evaluation script가 두 prompt를 자동 평가하는 것은 아니다. 실제 reachability·가시성·좌우 기준·초기 policy competence는 미확인이다. 성공 기록이 없는 B의 낮은 성능을 “망각”으로 해석하지 않는다. 초기 양쪽 능력이 부족하면 이 pair의 보존 비교를 제외하거나 목표 구분 습득 질문으로 명시적으로 바꾼다.

### 평가·모델에서 발견한 세 가지 차이

- **Prompt ≠ 기본 BDDL goal.** Spatial/01은 cookie prompt에 bowl-on-plate goal, Long/05는 yellow mug/left prompt에 두 mug의 복합 goal이 남아 있다. 공개 evaluator는 여러 condition의 OR 종료와 condition별 결과로 counterfactual 행동을 분석한다. 그 목적을 무시하고 `done`·총 success를 언어 이행률로 읽으면 잘못된 목표도 성공으로 합쳐진다. 이는 해당 benchmark 자체를 오류라고 판정한 것이 아니라 우리의 보존 비교에 필요한 평가 변경이다.
- **정책 변화량 ≠ 모든 모델에 같은 KL.** LIBERO-CF의 OpenVLA-OFT 기본 server는 L1 continuous action head이고, π₀/π₀.₅는 flow sampling이다. 원 OpenVLA AR token 분포와 같지 않다. OFT의 중간 logits 또는 action L2를 executed-policy KL로 부르지 않는다. Flow vector-field 보존 loss도 정규화된 행동 분포 KL과 구분한다. Exact/estimated KL을 질문의 중심으로 유지할 경우 AR 지원 경로를 먼저 확인해야 한다.
- **같은 init 파일 ≠ 동일한 완전 상태.** 두 prompt가 같은 BDDL·같은 init row·settle 절차를 사용하도록 설계할 수 있지만, controller state·RNG·관측/cache·정책 noise까지 같다는 증거는 없다. 원 공개 benchmark 수치를 paired causal comparison의 결과로 재해석하지 않는다.

### 석사 연구 가치·다음 판단

**작은 분석 탐색의 가치는 남지만 독립 방법 기여는 약한 상태**다. 공개 scene/predicate가 있어 새 hardware·수집 없이 첫 질문을 좁힐 수 있다. 반면 완성된 retention runner, 목표 일치 reward/termination, 지원하는 확률 정책·RL 경로가 아직 연결되지 않았다. 초기 능력을 측정하지 않은 채 여러 학습법 sweep을 시작하지 않는다. 단순 baseline으로 충분하면 그 조건을 정리하고 방법 개발을 멈춘다.

**N1 당시 인계 → 아래 N2에서 처리:** 지원 모델·정책 변화 측정, target-specific reward/termination, 초기 능력·분할·비용·단순 대안을 결정한다. 코드가 있다는 이유로 서로 다른 normalizer·head·simulator를 합치지 않는다. 새 비교는 기존 U1 P0와 별개다.

실제 외부 피드백은 미수신, Docker·simulator·policy·학습 실행은 0이다. 원 source의 공개 text·metadata만 읽었고 weights/init payload/PDF cache·dependency는 설치하지 않았다. 기존 U1 runtime 파일과 과거 판정은 그대로 보존했다.

<a id="langret-n2"></a>

## LANGRET-N2 — 모델·측정·비교 설계

- 검토일: 2026-11-12 / **내부 비실험 비교 설계 완료**. 아래는 연구자가 정한 미실행 설계다. Native IO, 초기 능력, 학습 효과, 독립 연구자 피드백은 미검증이다.
- 질문: **단일 VLA를 한 지시에 RL로 적응시킬 때, 적응 성능과 학습 분포의 평균 정책 변화만으로 다른 지시의 행동 보존을 판단할 수 있는가?** 답은 checkpoint/보존 대책 선택을 바꿔야 한다. “분포 밖 보장은 없다”는 일반 사실이나 KL/replay 자체를 새 방법으로 주장하지 않는다.
- 기존 U1의 value-gradient routing 효과와 다른 추정 대상이다. 이번 기본 학습법은 critic-free GRPO이므로 U1의 actor–critic 원인을 설명하는 실험이 아니다.

### 1. 선택한 모델과 선택하지 않은 경로

**SimpleVLA-RL의 이산 토큰 OpenVLA-OFT + LIBERO-CF**를 선택한다. [ICLR 2026 최종본 §2.1/2.4·G.2–G.3](https://proceedings.iclr.cc/paper_files/paper/2026/file/cbfbcb4da14235bd69b134070898ae9d-Paper-Conference.pdf)는 공식 OFT의 MLP/L1 대신 LLaMA head·cross-entropy·병렬 decoding을 쓰며 전용 SFT checkpoint가 필요하다고 명시한다. [공개 모델/학습 코드](https://github.com/PRIME-RL/SimpleVLA-RL/tree/7c51662df27b586f9e8a1ab35fcf849f2b8852f9)에서도 256-way sampling과 같은 token slice의 재채점을 확인했다. Source 위치·hash·checkpoint는 [재현 문서](../재현%20방법/README.md#langret-n2-interface)에 모았다.

| 고정 항목 | N2 선택과 경계 |
|---|---|
| 초기 정책 | `Haozhan72/Openvla-oft-SFT-libero-spatial-trajall`, revision `0a051b39aaebd3fc509fe2aba8bc7e60100e09f5`. Public metadata/config/statistics만 확인; weight·load·CF competence 미확인 |
| 입력·행동 | 외부 RGB 1개 + 지시, proprio/wrist 입력 없음. 8×7개 행동 토큰을 병렬 출력 → 8개 7D 명령. Normalizer는 해당 checkpoint의 `libero_spatial_no_noops`만 사용 |
| 주 장면 | N1의 OBJ-01, A=cookie box→plate, B=ramekin→plate. A 적응/B 보존을 첫 방향으로 고정. DEST-05는 같은 정책의 초기 능력이 있을 때만 후속 복제하며 첫 pilot 예산에 넣지 않음 |
| 학습 | GRPO; LoRA rank32/alpha32/dropout0, 공개 `all-linear` 경로를 설계 기본으로 선택. 실제 trainable 이름·개수, actor/rollout 동기화는 P0에서 검증. Full fine-tuning의 선행 수치를 LoRA 결과로 전사하지 않음 |
| 고정 decode | 학습·주 행동 평가 모두 sampling, T=1.6, 동일 256-token support. 중간 temperature 변경·top-k/top-p 절단 없음. Greedy는 별도 진단이며 주 성공률과 합치지 않음 |
| 보류한 대안 | 기존 U1 AR/ManiSkill은 그대로 보존. N1 CF의 공식 OFT L1/π₀.₅ flow에는 이번 token KL을 적용하지 않음. 다른 checkpoint로 몰래 바꾸거나 새 SFT부터 시작하지 않음 |

**N1의 양자택일을 수정한 이유:** KL을 다룰 수 있는 경로가 AR에만 한정되지는 않는다. 선택한 공개 RL 변형에는 categorical 분포가 있지만 원 CF server의 L1 회귀 head에는 없다. 같은 OFT 이름을 공유해도 모델·관측·checkpoint가 다르다. 공개 코드의 지원과 CF로 연결한 구현의 완성도도 구분한다.

### 2. 목표별 평가 계약

각 rollout의 `prompt → target predicate → reward → termination`을 하나로 바인딩한다. A/B 모두 같은 BDDL·초기 row·reset/settle 절차를 사용한다. Actor에는 RGB와 지시만 주고 object ID·predicate·성공 여부는 evaluator/reward에서만 쓴다.

- **성공·보상:** 지정 목표 predicate가 처음 참이 되면 reward=1로 종료, 그 전에는 0. `set_success_any_conditions([target])`만 등록한다. 다른 목표를 달성해도 종료하거나 보상하지 않는다. 모든 목표의 상태는 별도 관찰한다. 기본 BDDL goal/OR success로 조용히 돌아가면 해당 실행은 무효다.
- **시간:** 10 settle steps 후 최대 **512 control steps**, query당 최대8 actions. Target 성공·환경 오류·timeout 시 남은 action queue를 버리고 실제 실행 prefix만 학습 mask에 포함한다. Physics step 수는 control step과 별개로 P0에서 확인한다. Native controller의 시간 단위는 아직 검증하지 않았다.
- **주 지표:** `S_g = P(target g 도달 ≤512 steps)`, `ΔS_g = S_g(after)−S_g(base)`. A/B를 각각 보고하고 두 목표의 평균과 최솟값을 보조로 쓴다. 초기 실패 episode도 분모에서 제거하지 않는다.
- **오목표·회복:** 첫 다른 목표 시각 `τ_other`, 지정 목표 시각 `τ_target`을 저장한다. `P(τ_other < τ_target)`와 `P(τ_other < τ_target ≤512)`를 보고한다. 후자는 전체 episode 분모의 회복 빈도다. 조건부 회복률은 분모와 함께 보조 보고한다. 동시 성립은 tie로 별도 표시한다. 다른 물체를 건드렸다는 이유만으로 실패를 추가하지 않는다.
- **지시 구분:** 목표 성공만으로는 지시와 무관하게 A/B를 차례로 모두 수행하는 정책을 걸러내지 못한다. 같은 초기 row에서 지시별 A/B 첫 성립의 2×2 표와 `C = 0.5[(P(first=A|lA)−P(first=A|lB)) + (P(first=B|lB)−P(first=B|lA))]`를 함께 보고한다. 여기서 first는 A/B 중 첫 성립이며 tie/둘 다 미성립은 별도 항목이다. 다른 목표 사건도 원 log에 남긴다. C는 지시가 첫 목표 선택을 바꾸는지 보는 진단이며 reward/성공 정의에 새 금지 조건을 넣는 것이 아니다. 초기 C가 구분을 보이지 않으면 이후 성공률 감소를 “지시 구분 능력의 상실”로 확대하지 않는다.
- **판정 범위:** `On`은 접촉/위치 predicate이며 gripper release·장기 안정성을 뜻하지 않는다. 초기 target가 이미 참이면 사전 무효 조건으로 기록한다. 안정적 placement를 추가하면 별도 결과와 새 성공 정의로 명시한다.
- **실패 처리:** timeout/정상 물리 실패는 0. 프로세스·렌더·NaN 등 인프라 오류는 과학적 실패와 분리하고 횟수·부분 비용을 기록한다. 같은 identity 재시도는 최대1회이며 조건별 누락이 생기면 비교를 멈춘다. 정책 성능이 나쁜 경우 재시도하지 않는다.

같은 row는 paired 조건의 출발점일 뿐 완전한 상태 복원의 증거가 아니다. 두 branch에서 reset 직후 state·첫 RGB·controller/cache·policy RNG를 검증한다. 결과는 초기 row별로 묶어 비교하고 서로 다른 후속 궤적을 같은 observation이라고 부르지 않는다.

### 3. 정책 변화의 정확한 의미

선택한 sampler를 `qθ,j(k|x,l,T)`로 두며 `j=1,…,56`, `k=1,…,256`이다. Action placeholder를 사용해 한 번에 계산한 logits에서 각 token을 독립 sampling하는 공개 경로가 실제 실행에서도 유지되는지 먼저 검사한다.

`D_tok(x,l) = (1/56) Σ_j Σ_k q0,j(k) [log q0,j(k) − log qθ,j(k)]`

이는 **기준 정책→후학습 정책의 forward token KL 평균**이다. 고정 조건에서 categorical 합은 정확히 계산할 수 있으나 상태 평균은 유한 표본 추정이다. 56배 값은 독립 token chunk 분포의 KL에 대응한다. Bin clipping·gripper binarization은 여러 token을 같은 명령으로 바꿀 수 있으므로 **실행된 명령·궤적 분포의 KL과 동일하다고 주장하지 않는다**. Greedy 정책의 KL도 아니다. RL’s Razor의 AR 실험·정리의 직접 재현으로 부르지 않는다.

학습 전에 T split의 base rollout으로 관측 bank를 고정한다. A와 B 각각 최대128개 비종료 query 관측을 episode별 균등하게 추출하고, bank identity·실제 수·중복·추출 seed를 기록한다. 같은 episode의 여러 frame을 독립 표본으로 세지 않는다. `D_A`와 `D_B`는 각 지시의 고정 bank에서 계산하고, 같은 초기 관측에 A/B를 넣은 결과도 따로 남긴다. Online A visitation의 KL은 보조 기록이며 고정 bank 값과 섞지 않는다. 이 bank를 만든 환경 비용도 센다.

**반증 가능한 탐색 질문:** 같은 적응 수준·비용에서 `D_A`가 낮은 checkpoint가 B를 더 잘 보존하는가? 목표별 `D_B`를 추가해도 실제 선택이 달라지지 않으면 별도 진단의 실용 가치는 약하다. 두 장면의 산점도만으로 예측 법칙·인과·일반적 calibration을 주장하지 않는다.

### 4. 초기 능력·분할과 정보 누출 방지

Payload는 아직 읽지 않았다. 이후 init row의 전체 state hash·중복 group을 확인한 뒤 **결과를 보기 전에** hash 순으로 D/T/V/H를 배정한다. Prompt A/B·동일 state 중복·그 파생 rollout은 같은 split에 둔다. 최소30개 독립 row group이 있으면 `6/12/6/6`, 50개 이상이면 첫50개를 `10/20/10/10`으로 쓰고 나머지는 보존한다. 30 미만이면 본 pilot 대신 실행/능력 확인까지만 한다. 이는 연구자가 정한 작은 pilot 상한이며, 실제 row 수나 학습 데이터와의 독립성을 확인한 결과가 아니다.

| Split | 역할·허용 정보 |
|---|---|
| D — 개발 | 평가기 교정·초기 능력 screen. 각 row A/B×고정 sampling seed2개. 최대40 episodes. 결과가 나쁜 개별 row만 골라 제거하지 않음 |
| T — 적응 | A에만 RL. Base replay bank는 T의 A/B에서 같은 수의 rollout을 받아 고정; 최대40 episodes. B를 replay하는 조건은 추가 보존 supervision으로 명시 |
| V — 선택 | 정해진 checkpoint 32/64 rollout 시점의 A/B·비용 비교. Loss/seed를 결과에 맞춰 추가 탐색하지 않음. 선택 규칙은 아래에 고정 |
| H — 평가 | 선택된 checkpoint와 base를 같은 row·sampling seed2개로 평가. Test B를 보고 checkpoint·계수·pair를 바꾸지 않음 |

**능력 screen:** D에서 각 목표가 최소4회, 최소2개 row에서 성공하면 보존 질문의 작은 pilot을 열 수 있다. 6-row 분할이면 목표당12회, 10-row면20회 중의 횟수다. 이 편의상 기준은 신뢰도 보장이나 학회 기준이 아니다. 부족하면 “망각 없음/있음”을 판단하지 않고 해당 pair/checkpoint의 기본 능력 문제로 기록한다. A의 표본 성공률이90% 이상이면 개선 여지가 작은 조건으로 표시하고, 어려운 row를 사후 골라 학습하지 않는다. H의 base 성공률은 선택 조건이 아니라 결과의 기준선이다. SFT train membership은 미확인이므로 H는 **이번 RL에서 보류한 초기 상태**이며 pretraining-unseen task/scene이라고 부르지 않는다.

### 5. 강한 단순 대안과 공정성

| 조건 | 같은 초기 정책에서 바꾸는 것 | 답할 수 있는 질문 |
|---|---|---|
| B0 frozen | 갱신 없음 | 처음부터 못하던 B를 망각으로 해석하는 오류 방지 |
| B1 RL | A-only GRPO, lr=5e-6 | 기본 적응/보존 변화 |
| B2 small update | 같은 GRPO, lr=1e-6 | 단순히 덜 갱신해도 충분한가? |
| B3 RL + KL | B1 + A의 현재 관측에서 기준 정책에 대한 **명시적 forward token-KL loss**, token 평균의 계수0.1 | 적응 분포를 보존하는 단순 regularization으로 충분한가? |
| B4 RL + replay | B1 + T의 base 행동 token을 A/B 균등 replay하는 CE, 평균 loss의 계수1.0 | 목표별 기존 행동을 직접 다시 학습하면 충분한가? |

계수는 pilot용 설계 선택이며 최적값·선행의 권장값이 아니다. B3/B4의 추가 loss는 **미구현**이다. 공개 `kl_coef`의 reward shaping·old/current PPO 진단을 이 loss로 대체 표기하지 않는다. Replay는 base가 실제 생성한 행동의 **behavior replay**이며 원 SFT 시연 replay와 다르다. 성공 필터 없이 같은 수의 A/B rollout을 쓰고 실패 포함 여부·행동 label provenance를 보존한다. 이 비교 하나로 “일반 experience replay가 모두 충분/불충분”하다고 결론내리지 않는다. 원 시연 replay는 동일 source/split이 확보된 후 확장한다.

네 학습 조건은 동일 LoRA·관측·행동·temperature·8개 group sample·clip[0.8,1.28]·보상·최대 rollout 수를 사용한다. Pilot은 **dynamic sampling 재충전 없음**: 모든 group 시도와 all-success/all-fail도 비용에 포함하며 zero-advantage group은 생략해도 그 수를 보고한다. 무제한 재수집으로 성공 가능 그룹만 채우지 않는다. 토큰별 sampled-action ratio를 사용하는 공개 GRPO 목적함수를 유지하며 이를 joint-chunk ratio와 혼동하지 않는다.

환경 상호작용 수를 맞춘다고 총 비용이 같아지는 것은 아니다. B3의 reference forward, B4의 추가 replay forward/backward·수집, evaluator query, reset/settle·physics, GPU-hours·peak memory를 별도 집계한다. 공통 bank 비용과 실제 조건별 비용을 모두 보고한다. 추가 비용을 뺀 “공짜 보존”을 주장하지 않는다.

### 6. 단계·예산·선택 규칙

**다음은 학습이 아니라 P0 준비**다. 그다음 단계의 상한까지 적되 자동 실행 지시로 해석하지 않는다.

| 단계 | 계획 상한·완료 조건 |
|---|---|
| P0 — IO/확률/평가기 | 새 source/환경 manifest와 Docker recipe가 필요. OBJ 한 dev row, 총 episode reset≤2(생성자 reset 포함), A/B query≤2, native actor 재채점≤2, backward≤1·optimizer0. 각 branch settle10+최대8 actions → 합계≤36 control steps·physics≤10,000. 두 query의 56×256 분포·sampling/재채점·normalizer·goal binding 검증. 최대2 GPU-hours. **아직 launcher 없음** |
| P1 — 능력 | 위 D screen≤40 episodes + T bank≤40. Base competence·측정/데이터 자격만 확인, RL0. Target 평가·state/RGB 일치가 실패하면 이 단계로 넘어가지 않음 |
| P2a — 작은 변화 확인 | 먼저 B1의 첫 training seed만 64 A rollout(8개 group)·최대4 optimizer update. 32/64 시점 저장. Headroom·nonzero advantage·구현 문제를 확인; 이 단계에서 차이가 없으면 아직 부정 결과로 확정하지 않음 |
| P2b — 조건부 비교 | P2a에서 비교가 가능할 때 B1–B4×training seed2개, **각64 A rollout·최대4 update**까지. 총512 train rollouts 안에 P2a 포함. Gradient accumulation·group batching은 구현 때 고정하며 update 수를 늘려 예산을 우회하지 않음 |

P2의 V 평가≤320 episodes(8학습 run×2checkpoint×2지시×10rows), H 평가≤680(base40 + 아래 두 선택 규칙이 고른 최대16checkpoint×2지시×10rows×sampling seed2). 같은 checkpoint는 중복 실행하지 않는다. P1까지 합친 최대 **1,592 episodes**, episode당512+10 steps → **831,024 control steps** 이하이며 P0의36 steps는 별도다. 오류 재시도·bank·추가 평가도 이 총 상한 안에서 차감한다. 각 전체 episode의 inference는 최대64회이고 총 상한은101,888회다. P0 이후 전체 GPU 비용 상한은64 GPU-hours로 두며 **실제 시간/VRAM 추정이 아니다**. P0 profiling에서 상한 내 수행이 어렵다면 시작 전에 범위/예산을 다시 정하고 기록한다. 공개 논문의 8×A800 full-training 자원을 단일 GPU 실행 보장으로 읽지 않는다.

V에서 각 학습 run의 A 최고 성공률로부터10 percentage points 이내인 checkpoint들을 후보로 정한다. **주 선택**은 그 안에서 `D_A`가 가장 작은 checkpoint, **목표별 진단 선택**은 `D_B`가 가장 작은 checkpoint다. 동률이면 A 성공률이 높은 것, 다시 동률이면32 시점을 고른다. H를 열기 전에 두 선택을 봉인하고 둘 다 평가한다. 실제 H의 A 성능 차이도 함께 보고한다. 조건 간 적응 수준도 V에서10pp 이내인 경우에만 “비슷한 적응 성능에서의 보존”을 탐색적으로 비교하고, 아니면 A/B/비용 곡선을 보고 trade-off로 남긴다. 10pp는 pilot의 임시 비교 폭이며 통계적 동등성 검정이 아니다. `D_A/D_B`는 앞서 정한 T bank에서 계산하며 V는 적응 자격/동률 판단에만 쓴다. H 사후 최적화를 금지한다.

각 training seed·goal·init row의 paired 결과를 공개하고 seed와 row의 변동을 구분한다. 두 training seed는 안정성 확증에 부족하므로 p-value·일반화 선언보다 효과 크기·개별 결과·row 단위 불확실성을 보고한다. 본 실험 표본 수는 pilot의 변동과 필요한 효과 크기로 별도 산정한다.

### 7. 결과에 따른 투자 판단과 남은 일

| 관측될 수 있는 결과 | 판단 |
|---|---|
| 평가기/분포 재채점/normalizer 불일치 | 구현 수정. 능력 보존 가설의 반증이 아님 |
| B의 초기 능력이 부족하거나 A에 학습 신호/개선 여지가 없음 | 이 pair의 retention 비교를 보류. “RL 때문에 언어를 잃었다”는 결론 없음. 다른 pair 전환은 별도 명시 |
| 작은 학습률·KL·behavior replay가 적응/비용까지 고려해 충분 | 그 단순 대안을 우선. 새 보존 알고리즘 개발의 근거는 약함 |
| D_A가 비슷해도 B가 달라지고 목표별 관찰이 checkpoint 선택을 개선 | 역방향 B→A, DEST 또는 별도 장면으로 복제 후 실증 기여 검토. 지금 두 pair만으로 top-tier 기여 확정 안 함 |
| 4 update/예산 내 변화가 거의 없음 | 단기 민감도만 보고; 장기 forgetting 부재의 증거 아님. 추가 비용의 정보 가치부터 재판단 |

문제·직접 선행·반대 설명·주장 범위·비교/분할·비용·실패 시 결정은 문서화했다. 외부 검토용 핵심 반론은 **“알려진 forgetting/support mismatch를 작은 LIBERO 예제로 반복하는 것 아닌가?”**다. 답이 기존 학습/선택 판단을 바꾸는지 동료에게 확인할 수 있도록 정리했지만 실제 연락/피드백은 없다. **N2를 반복하는 다음 문헌 TODO는 없다.** 후속 **GAP-LANGRET-P0-PREP는 준비 범위 완료**다. [실행 자료·실제 검사](../재현%20방법/README.md#langret-p0-preparation)를 기존 재현 폴더에 통합했다. Local Mac ARM64·daemon7.65GiB·GPU allocation exit125로 native 실행은0이며 Docker stdlib22검사만 통과했다. 제한된 paired IO runner·source/checkpoint pin·launcher를 작성했지만 image/dependency/payload·CUDA/EGL·native 확률/목표 교정은 미검증이다. 다음 **GAP-LANGRET-P0**에서 이 연결을 확인한다. P1 기본 능력·split 실체화와 P2 collector/추가 loss·연구 효과는 이후에 남는다. 준비 검사나 자원 실패로 연구 가설의 성숙도·독립 기여 판정을 바꾸지 않는다.

## U1의 7단계 완료 범위와 외부 검토 — 11/06 기록

| 단계 | 이번 완료 범위 | 남은 실질 작업 |
|---|---|---|
| 1. 문제·독자 | VLA 학습 설계자가 공유 value supervision을 선택할 때의 판단 문제로 정리 | 실제 행동 효과·배포 빈도는 미측정 |
| 2. 가까운 선행 | VLAC **최종본** §3/4.6–4.9, RL4VLA multi-object 평가, ICLR 표현 연구 §5–6 및 공개 코드 추가 대조 | 포괄적 최초성 인증 아님; 새 직접 선행이 나오면 변경 |
| 3. 질문·단순 대안 | 8개 경쟁 설명·대조 순서·측정 가능한 조건부 예측 정리 | 실제 원인/효과 크기는 실험 대상 |
| 4. 짧은 논문 이야기 | 실증 기여·그림 계획·결과별 투자 결정 작성 | 결과 빈칸은 실험 후 채움 |
| 5. 최소 비교 | 주 estimand·분모·first-event·분할/중복·tuning·불확실성·후속 factorial 설계 | Native evaluator/fork·manifest 실체화·실험·확증 표본 결정 |
| 6. 실행 부담 | 기존 P0 packet 유지, P1/작은 학습의 계획 예산·비용 산정과 1주 점검 시점 작성 | Native build·실제 자원 비용·P1 이후 구현 미완료 |
| 7. 외부 비판 | 전달 가능한 주장·가장 강한 반론·아래 질문 준비 **완료** | 독립 연구자에게 전달/응답 수신 **미완료** |

**외부 검토용 핵심:** 주장 후보는 “같은 VLA의 value supervision이 목표별 행동에 미치는 효과를 설명하고 선택 기준을 준다”이다. 가장 강한 반론은 “이미 알려진 actor–critic interference를 carrot/shovel 예제로 반복하는 것”이다. 검토자에게 (1) 위 선행 이후 남는 중요한 질문이 있는지, (2) H/L 상호작용이 geometry·능력·데이터 차이로 설명되는지, (3) λ/lr/normalization/PPG 중 빠진 강한 대안이 있는지, (4) 실증 논문에 필요한 최소 확장 범위가 무엇인지 묻는다. 응답이 오면 검토자·날짜·반론·변경한 비교/주장을 같은 문서에 기록한다. 실제 연락은 하지 않았고 AI 내부 검토를 독립 피드백으로 세지 않는다. 피드백 미수신은 작은 탐색의 금지 조건이 아니다.

**P0-PREP 결과:** [재개 코드·실행 범위](../재현%20방법/README.md#preparation-history)를 작성하고 local Docker에서 stdlib 제어 검사 15개를 통과했다. Value head 입력만 detach하는 경로, 동일 clipping group, reset 상태 goal binding, side-effect 없는 grasp observer, 0 control-step·query/forward/backward/update 상한을 구현했다. 검사 통과는 실제 PyTorch autograd·simulator 동작의 증거가 아니다. 준비 결과로 연구 가설의 성숙도를 올리지 않는다.

**N2 완료·판정:** 추가로 반복할 내부 비실험 TODO는 없다. 다음 실제 증거는 **GAP-UNIFIED-P0: 호환 NVIDIA Docker에서 check → build → prepare → 최소 IO/gradient 검증**이며, 외부 비판은 별도 미수신 상태다. 이번에는 문헌·공개 코드·설계 검토만 수행했고 Docker/정책 실험을 추가 실행하지 않았다. 직전 Mac 검사에서 ARM64·약 7.65 GiB로 자원이 부족했으며 새 컴퓨터에서는 재확인한다. GPU 외에도 native build·교정과 P1 이후 구현이 남아 있다. **분석 후보로는 계속할 가치가 있지만 독립 새 알고리즘이나 top-tier 출판 가능성은 아직 입증되지 않았다.** 다음 단계의 결정적인 불확실성은 문서 수가 아니라 목표 쌍의 실제 능력과 행동 결과다.
