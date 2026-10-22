# C1 최소 진단 계약 — 선택적 관측의 순이득

- 2026-10-20 / 연구자 설계, branch 실험 미실행
- [문헌·source 판단](./C1_REVIEW.md)
- 고정 완료 범위는 아래 G0의 bounded native probe다. G1 이후는 관측 primitive의 실측 reachability와 비용이 없으므로 **실행 freeze가 아니다**.

## 질문·estimand

VLA weights·native preprocessing·controller를 고정한다. 시작 상태에서 `execute` 또는 물리적으로 실행 가능한 `look`을 고르는 supervisor만 나중에 학습할 수 있다.

초기 history를 h, native budget을 B, sensing primitive m의 실제 control-step 비용을 c(m)라 하자. Primary 비교는 다음이다.

`Δ_net(h,m;B) = P(success | m → frozen VLA, remaining B−c(m)) − P(success | frozen VLA immediately, budget B)`

이 값은 **정보+자세 변화+시간 소비의 총효과**다. 관측 자체의 효과라고 명명하지 않는다. C1의 첫 empirical prerequisite는 어떤 admissible m에서 양의 순이득이 있고, 다른 상태에서는 불필요하거나 해로운 관측이 있어 선택의 가치가 생기는 것이다.

이는 연구를 위한 operational contrast이며 새 value estimator가 아니다. Budget-conditioned intervention value·paired branching의 직접 선행인 [RESCUE §III](https://arxiv.org/html/2610.13516)와 구별되는 현상이 없으면, sensing option을 추가했다는 이유만으로 evaluation contribution을 주장하지 않는다.

`wait c(m) → VLA`는 시간 비용을 맞추는 별도 control이다. 모든 조건에서 task horizon은 같으며 wait가 time-free comparator가 되지 않게 한다. Passive waiting에도 dynamics 변화가 있으므로 원인 분리를 완성했다고 단정하지 않는다.

## G0: native compatibility와 base competence

첫 작은 probe의 고정 조건·실행 코드는 [native probe](../../experiments/vla_rl_active_handoff/README.md)에 있다. Policy strict load와 실제 task observation을 확인하며, 소수 episode 성공을 competence 증거로 과장하지 않는다.

다음 competence 검사로 넘어갈 경우:

- Tasks: `libero_spatial/0` = black bowl between plate/ramekin → plate, `libero_goal/0` = open middle drawer.
- 20개 prescribed initial states **각 task index 0–19**, training 없음. Policy RNG는 각각 `71000+i`, `72000+i`.
- Native control-step horizon은 spatial 280 / goal 300. Reset settle 10 steps는 모든 조건 공통이며 별도 기록.
- Task별 최소 14/20 successful completions를 운영 gate로 제안한다. 통계적 안정성이나 논문 수준 성능 보장은 아니다.
- 둘 중 하나가 미달이면 input/control contract를 한 번 재감사한다. 미달 task를 조용히 제외하거나 toy head 학습으로 이어가지 않는다. Suite/task 선정 변경은 protocol revision으로 기록한다.
- Runtime이 이 40 episodes와 후속 branch 비교를 감당하는지 실제 처리량으로 산정한다. 추론 주기·해상도를 바꾸어 예산을 줄이면 같은 base라는 비교를 재검증한다.

G0는 새로운 가림·카메라 이동·reward·RL을 포함하지 않는다.

## G1: 추가 관측에 선택 가치가 있는지

후보 option은 `execute`, `left-view`, `right-view`, `closer-view`다. 이 이름만으로 primitive를 구현 완료로 간주하지 않는다. 실행 전에 목표 상대 pose, 속도, 최대 ticks, IK/controller, 허용 contact, 실패 처리를 고정해야 한다.

**필수 제약**

- 새로운 scene camera, privileged object pose, ground-truth occlusion mask를 deployable supervisor 입력에 추가하지 않는다.
- Native scene+wrist observation과 proprio, instruction, 선택 history, remaining budget만 허용한다.
- Sensing motion은 매 control step을 실제 환경에 적용한다. IK teleport를 비용 1의 look으로 기록하지 않는다.
- 접촉·object displacement가 발생하면 기록한다. 그런 branch의 이득은 순수 sensing evidence에서 제외하되 전체 failure 비용에서는 삭제하지 않는다.
- `execute` 후에는 native VLA가 remaining budget 동안 실행한다. 처음에는 manipulation 중 재관측/recovery를 섞지 않는다.

**Comparators**

| 조건 | 판단할 설명 |
|---|---|
| Immediate native execution | 원래 정책만으로 충분 |
| Fixed one-look / fixed scan | 상태별 선택 없이 같은 동작으로 충분 |
| Cost-matched wait | 관측 이동과 시간 경과의 차이 |
| Visibility/confidence threshold, visibility-convergence | AAWR/EgoReveal식 종료 기준으로 충분 |
| Same-data outcome classifier / contextual bandit | 다단계 TD 없이 one-step prediction으로 충분 |
| BC / return-weighted supervisor | 경험 복제·선택으로 충분 |
| Task-success minus measured-cost의 표준 option RL | 새 estimator 없이 표준 RL로 충분 |
| Observation-aligned SFT + same AP path | ActiveAlign의 continuation adaptation으로 충분. 실제 수행 가능한 데이터·compute 범위를 먼저 확인; 생략하면 그 방식보다 우수하다고 주장하지 않음 |

마지막 세 learned controls는 G1에 선택 여지가 확인된 뒤에만 구현한다. Fixed/heuristic보다 유리한 배포 가능한 선택이 없다면 RL 학습을 시작하지 않는다.

## Split·paired control·선택 편향

- Development branch의 제안 index는 20–29, selector validation 30–39, final 40–49다. 실제 init-state 파일이 50개 이상인지 확인하기 전에는 유효한 split으로 취급하지 않는다.
- Index 0–19는 base qualification에 이미 사용했으므로 final에 재사용하지 않는다.
- 하나의 initial state에서 나온 모든 branch·RNG repeat는 같은 split에 둔다.
- Initial state뿐 아니라 robot/controller/cache·policy noise도 맞춘다. Simulator 재생 검사에서 tolerances와 첫 관측 hash를 확인한 뒤 paired라고 부른다.
- 한 번 성공한 branch를 최고 oracle로 선택해 그 동일 rollout에서 점수를 계산하지 않는다. Branch selection용과 outcome 평가용 RNG를 나누고 반복수에 따른 불확실성을 보고한다.
- Hyperparameter, sensing-cost weight, task selection을 final 결과로 조정하지 않는다.
- 서로 다른 새로운 occluder family의 일반화는 이 native pilot 이후 별도 split으로 확장한다. 인위적 가림이 task geometry를 바꾸면 새 benchmark 조건임을 표시한다.

## 판단 지표·반증

Primary는 **동일 total control budget의 성공률 차이**다. Paired confidence interval, sensing 비용, VLA 호출 수, contact, failed-look 비율과 worst-group 결과를 분리해서 보고한다. 평균 성공률과 비용을 하나의 임의 가중 점수로만 숨기지 않는다.

| 관찰 | 결론 |
|---|---|
| Native base가 input contract를 맞춰도 미달 | 해당 실행 기반으로 C1 평가 중단 |
| 모든 look이 손해 | Fixed VLA에 sensing supervisor를 붙이는 현재 구성 기각 |
| 항상 같은 look이 최선 | Adaptive 선택의 필요성 기각 |
| Oracle branch는 낫지만 관측에서 구별 불가 | Deployable selector 주장 기각; privileged labels로 감추지 않음 |
| One-step predictor로 충분 | Multi-step RL 필요성 기각 |
| Native base는 잘하지만 AP endpoint에서만 모두 실패 | ActiveAlign이 이미 다루는 continuation support 문제와 대조. 새 gap 발견으로 세지 않음 |
| Same-state diagnostic에서 차이 없고 pose 이동만 유리 | Active perception claim 제거, pre-positioning/control로 재정의 |
| 표준 RL 또는 aligned SFT로 충분 | 새 방법 claim 제거. 반복 가능한 조건 분석이 남을 때만 empirical study 검토 |

**학습을 시작할 필요조건:** base competence, reachable primitive, heterogeneity, deployable observability, strong-baseline comparison이 모두 성립해야 한다. 이 문서는 그 조건의 검사를 정의하며 통과를 선언하지 않는다.
