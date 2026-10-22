# C4–C6: 질문, 직접 충돌, 최소 반증 설계

- Updated: 2026-10-21 KST
- 모든 후보: **CURATION-HYPOTHESIS**. 문헌이 뒷받침하는 문제와 미검증인 제안 가설을 구분한다.
- 아래는 후보 단계의 설계안이다. 환경·checkpoint·seed·예산 manifest와 실행 결과는 아직 없다.
- 근거 ID는 [LITERATURE.md](./LITERATURE.md)와 [SEARCH_AUDIT.json](./SEARCH_AUDIT.json)을 따른다.

## C4. 정책 개선에 필요한 보상 오류의 선택적 보정

**후속 판정:** [C4 buildup](../2026-10-21_c4_reward_audit/README.md)에서 ReQueST·IDRL 등과 추가 대조하고 실제 metadata를 확인했다. 현재의 새 acquisition method 주장은 NO-GO, 적용 조건을 비교하는 진단 연구는 보류다. 아래는 최초 제안·반증 설계를 보존한 것이며 채택된 실행 계획이 아니다.

**질문:** 고정된 검수 예산에서, 현재 VLA 정책이 높은 보상을 받으면서 반복하는 실패를 우선 보정하면 정적 reward 정확도나 일반적인 uncertainty sampling을 최적화하는 것보다 실제 RL 개선이 커지는가?

### 확인된 문제와 남은 가설

E01·E02는 reward quality와 downstream RL을 이미 함께 평가했다. E03은 실제 나쁜 행동 데이터의 필요성을 제기하고, E04는 rollout 중 reward refinement를 수행한다. 따라서 offline accuracy와 RL 성능을 비교하는 것, 실패 데이터를 쓰는 것, reward를 online으로 갱신하는 것 모두 기존 기여다.

남길 가설은 **label 선택의 효과가 현재 정책의 방문 분포와 함께 바뀐다**는 것이다. 예를 들어 정책이 목표 근처에 물체를 떨어뜨리는 행동으로 높은 보상을 받는다면, 드물게 발생하는 다른 오류보다 이 실패의 보정이 더 중요할 수 있다. 이는 예시이며 우리 정책에서 관찰한 결과가 아니다. 정확도가 같은 reward model의 정책 효과가 다를 수도 있지만 아직 입증하지 않았다.

**왜 VLA + RL인가:** 언어 조건부 시각 보상이 policy improvement의 목적함수가 되고, RL로 바뀐 행동이 다음 보상 학습 데이터를 만든다. 단순 video classification에서는 없는 이 feedback을 검증해야 한다. 하나의 데이터셋에서 reward accuracy만 개선하면 이 연구 질문을 충족하지 않는다.

### 후보 계약

| 요소 | 제안 범위 |
|---|---|
| Primary track | RL, IL, offline learning, and robot data; reward·uncertainty는 cross-track 연결 |
| 시작 task | 기존 native VLA가 일부 성공하며, 목표 물체·위치 오인 같은 **시각적으로 판정 가능한 실패**가 존재하는 manipulation task |
| 초기 고정 요소 | Native VLA/checkpoint/controller, RL algorithm, initial reward model, instruction, rollout budget, reward adaptation capacity |
| 바꿀 요소 | Label을 요청할 trajectory/prefix의 선택 규칙. 첫 단계에서는 RL algorithm을 새로 만들지 않음 |
| 후보 입력 | 현재까지의 RGB/history, instruction, reward predictions, policy version, 관측 가능한 rollout 통계 |
| 정답 접근 | Simulator predicate 또는 독립 human label은 query oracle에만 둠. Query하지 않은 학습 sample의 정답과 test label은 selector에 노출하지 않음 |
| 정책 입력 | Native interface 유지. Selector가 얻은 label·simulator state를 actor observation으로 추가하지 않음 |
| 비용 | 검수한 episode/prefix 수와 실제 annotation 시간 모두 기록. Dense frame label과 binary episode label을 같은 1 label로 세지 않음 |
| 일반화 | 먼저 다른 task/failure family. 로봇 확장은 reward calibration 재사용과 robot별 성능으로 평가하며 policy transfer와 구분 |

**검토할 방법 계열:** uncertainty만이 아니라 예상 방문 빈도·높은 예측 보상·오류 보정의 정책 영향에 따라 검수 우선순위를 정하고 reward를 갱신한다. 이는 아직 구현·추정식이 고정되지 않은 가설이며, active reward learning/expected value of information의 새로운 발명이라고 주장하지 않는다. 실제 label 없이 오류 여부를 아는 oracle acquisition과 deployable selector를 분리해야 한다.

### 반드시 이겨야 할 비교

| 비교 | 배제할 설명 |
|---|---|
| Frozen reward + 기존 RL | Online 보정 자체가 필요하지 않음 |
| Uniform trajectory audit + 같은 reward 갱신 | 좋은 sample을 고른 것이 아니라 label을 추가한 효과 |
| Uncertainty/disagreement, task-stratified audit | 표준 active learning이나 task balancing이면 충분 |
| PROGRESSOR 계열 online refinement | 이미 존재하는 OOD 보정으로 충분. Interface가 다르면 재구현 범위를 밝힘 |
| Synthetic negative / 실제 failure를 동일 검수 예산으로 추가 | 실제 데이터·coverage의 차이가 method 효과로 오인됨 |
| 같은 수집 경험의 success-filtered SFT 또는 return-weighted imitation | 개선이 RL 최적화보다 데이터 선별로 설명됨 |
| 독립 정답 reward + 기존 RL | 해당 base/환경에서 달성할 수 있는 개선 여지. 제안법에는 oracle 정답을 무료 제공하지 않음 |

새 reward model을 처음부터 pretrain하는 설계는 피한다. Initial weights와 adaptation capacity를 맞춰야 label 선택의 효과를 식별할 수 있다. Query 선택이 바뀌면 이후 policy와 데이터도 달라지므로, **공통 고정 pool에서의 선택 비교**와 **각 정책이 새 데이터를 만드는 closed-loop 비교**를 분리한다. 전자만으로 후자의 효과를 주장하지 않는다.

### 가장 작은 gate와 기각 기준

1. **문헌 gate:** E01–E04, E07, E15에 동일한 policy-dependent acquisition·matched-label closed-loop 실험이 있으면 새 selector 제안을 접거나 그 연구가 남긴 구체적 한계로 수정한다.
2. **데이터 gate:** Policy/checkpoint/시간 순서가 있는 실제 rollout와 독립 label, reward training과 분리할 task/episode가 있어야 한다. 영상·label이 있다는 것만으로 충족하지 않는다.
3. **정적 진단:** Early-policy에서 정한 error/uncertainty 기준이 later-policy의 잘못된 고보상을 예측하는지, 같은 예산에서 보정 후 independent held-out error가 줄어드는지 본다. 전체 episode 단위 split을 쓰고 frame을 독립 표본으로 취급하지 않는다.
4. **작은 closed-loop:** Native base와 oracle-reward baseline이 성립한 뒤, frozen/uniform/uncertainty/후보 선택을 동일 interaction·label·update 예산으로 비교한다. 단일 seed의 차이를 채택 근거로 삼지 않는다.

Primary metric은 **독립 정답으로 평가한 success–label-cost curve의 면적**이며 interaction budget은 고정한다. Curve의 label budget 구간과 계산법은 실행 전에 동결한다. Reward MAE·false-positive rate·calibration은 진단 지표다. CI는 episode/task 및 training seed 구조를 반영한다. Query에 쓴 label로 최종 성공률을 평가하지 않는다.

- Uniform/uncertainty audit와 차이가 없으면 새 acquisition method는 기각한다.
- Reward error가 시각적으로 구별되지 않는 contact force·stability 때문이면 label 선택만으로 해결할 수 없다. Sensor/interface 연구로 범위를 바꾸지 않는 한 해당 task를 제외한다.
- Reward만 좋아지고 독립 success가 개선되지 않으면 VLA RL 연구 claim을 기각한다.
- Reward model을 바꾸기만 해도 해결되면 큰 method 대신 model-selection 결과로 축소한다.

**혼동 방지:** E01은 reward와 success detection을 함께 사용한다. 보정이 rollout 종료·stage 전환도 바꾸면 label 선택 외에 데이터 길이가 바뀐다. 초기 비교에서는 종료 규칙을 공통으로 고정하고, 실제 운영 확장에서 이 coupling을 별도 ablation한다. Termination 개선 자체는 E19·E20와 충돌한다.

**판정:** 중요성은 문헌으로 뒷받침된다. Method 신규성은 아직 약한 부분이며, 가장 유망하다는 판단은 **다음 작은 정보 수집에 투자할 순서**다. 공개 reward interface와 failure data가 있어 C1/C2처럼 새 policy bootstrap부터 시작할 필요가 없다는 장점이 있다. 다만 동시 VLA·reward 실행 가능성은 미검증이다.

## C5. 자동 reset의 편향 아래에서 학습 범위 유지

> 아래는 최초 제안이다. 후속 사용자 요청에 따른 [C5 buildup](../2026-10-21_c5_reset_audit/README.md)에서 EARL·MEDAL·MiDAS와 공개 source/data를 대조했다. 일반 방법 주장은 NO-GO, 구체적 VLA 현상 진단은 조건부 보류로 갱신한다.

**질문:** 자동 reset의 성공 여부와 도착 상태가 현재 정책의 실패에 의존할 때, 자율 VLA RL이 목표 분포의 어려운 장면을 점점 덜 학습하는가? 같은 reset·human rescue 예산으로 그 손실을 줄일 수 있는가?

E08은 자동 평가·reset을 구현했고, E09는 자율 데이터 수집의 어려움을 실증했다. E10은 reset 다양성을 통한 RL을, E16은 VLA 적응에서 reset curriculum과 coverage를 이미 다룬다. “reset을 넓히면 일반화가 좋아진다”는 가설은 신규성이 없다.

남길 차이는 **원하는 reset 상태를 무료로 배치할 수 없는 physical reset**이다. 목표 시작 분포 `p_target(s0)`를 고정하되 실제 시작 분포는 `q(s0 | 이전 trajectory, reset policy, retry budget)`로 생긴다. Reset 실패로 빠진 장면을 denominator에서 지우면 개선을 과대평가할 수 있다는 것은 검증할 연구자 해석이다. 기존 AutoEval 결과가 실제로 편향되었다고 단정하지 않는다.

### 범위·비교·검증

- **Actor:** 검증된 native language-conditioned VLA + 동일 RL learner. 첫 실험에서 새로운 reset controller는 학습하지 않는다.
- **개입:** 기존 reset primitive/목표의 수집 scheduling, quota·coverage 유지, 제한된 human rescue 배분. 감독자는 관측 가능한 장면 descriptor와 성공·실패 이력만 사용한다.
- **비용:** task ticks + reset ticks + retry + rescue/annotation minutes. “성공한 reset 이후 task episode 수”만 맞추지 않는다.
- **비교:** native reset, task-stratified quota, uniform requested starts + capped retries, MiDAS식 widening curriculum, reset cost만 최적화한 schedule, 동일 비용의 human-assisted reset. 이상적인 simulator teleport는 진단용 기준이며 deployable baseline이 아니다.
- **평가:** 별도로 고정한 `p_target`의 success, worst-scene-group success, invalid start·reset failure·missing coverage, total uptime. 자연스럽게 나온 `q`에서의 success도 별도 보고한다.

가장 싼 검사는 **학습 전 연속 reset 로그 감사**다. Requested start와 achieved start, task outcome, reset attempts, invalid/rescue가 있어야 한다. 단순히 성공 reset만 저장한 데이터로 결측 장면의 성능을 복원할 수 없다. 이후 simulator에서 reset policy를 물리 실행해 selection을 분리할 수 있지만, 이것을 실제 로봇의 장기 효과라고 부르지 않는다.

**기각:** 고정 target 평가에서도 손실이 없거나, task-balanced quota만으로 충분하면 새 method를 만들지 않는다. 학습기의 성능 향상이 아니라 reset sample의 난도만 바뀌었다면 policy-improvement claim을 제거한다. Coverage 밖 성능을 importance weighting으로 알아낼 수 있다고 주장하지 않는다.

**판정:** RL의 데이터 생성 조건이라는 독립적인 문제다. C4보다 운영 비용이 크며 logged reset provenance가 필수다. 다양한 로봇에서는 reset 가능 영역과 비용이 다르므로 확장 가치가 있지만, 한 로봇에서 RL improvement가 다른 로봇으로 전이되는 이전 주제와 구분한다. Navigation에서는 복귀 가능 영역·배터리/도킹으로 확장할 수 있으나 이번에 이를 검증하지 않았다.

## C6. RL checkpoint 선택의 평가 오류

**후속 판정:** [C6 buildup](../2026-10-21_c6_checkpoint_audit/README.md)에서 A-OPS·STEP·N-SCORE 등과 code/data를 대조해 독립 신규 방법 채택을 NO-GO로 판정했다. 아래는 최초 가설이며 실행 계획이 아니다. 새로 확인한 기존 비교법과 데이터 전제는 [재개 조건](../2026-10-21_c6_checkpoint_audit/REOPEN_PROTOCOL.md)을 따른다.

**질문:** 같은 VLA의 RL checkpoint들이 비슷한 평균 성공률을 보일 때, 제한된 실제 평가로 더 좋은 checkpoint를 고르고 나빠진 checkpoint를 배제할 수 있는가?

E11은 active policy–task 평가, E12는 finite-trajectory value estimation, E13은 world-model 기반 policy ranking, E18은 현재 정책의 action-level OPE를 이미 다룬다. 단순히 OPE/active evaluation을 VLA에 적용하는 방향은 제외한다. E12의 학습 데이터 기반 value 평가를 임의의 새 target policy의 off-policy return 추정과 혼동하지 않는다.

남길 가능성은 **RL이 평가 모델과 공유하는 failure blind spot을 이용하는 동안**, static evaluator의 ranking과 독립 실측 ranking이 어긋나는 조건이다. 이는 C4와 연결되지만 별도 문제다: C4는 학습용 reward label을 고르고, C6는 고정된 checkpoint 집합을 평가·선택한다. 둘을 한 번에 학습시키면 원인을 분리하기 어렵다.

- Primary: fixed real-evaluation budget에서의 **selection regret** `J(best candidate) - J(selected)`와 나빠진 checkpoint를 승인한 비율. `J`는 독립된 고정 task distribution·horizon에서 정의한다.
- 비교: 마지막 checkpoint, uniform paired evaluation, standard best-arm racing, E11의 task selection, 고정 OPE/world-model evaluator, uncertainty/abstention. Best candidate의 reference score 자체에도 표본 불확실성이 있음을 보고한다.
- 최초 gate: checkpoint별 raw outcomes와 task/seed, 평가 predictor를 훈련한 데이터가 실제로 공개되어 있는지 확인한다. Paper의 평균 점수표만으로 simulated sequential selection 실험을 만들지 않는다.
- 반증: 단순 uniform paired evaluation 또는 표준 racing과 동등하면 새로운 method로 채택하지 않는다. 평가 모델을 더 크게 만드는 효과만 있으면 protocol 연구로 축소한다.

**판정:** 실용적이지만 선행 연구와 가장 가깝다. 현재는 C4의 검증 설계를 강화하는 보조 축으로 유지한다. 새로운 estimator나 이론 보장은 주장하지 않는다.

## 이번에 제외한 넓은 주제

| 제외한 주장 | 이유 |
|---|---|
| 실패 데이터로 general reward model을 만들자 | E01–E03가 직접 다룸 |
| Reward model을 online으로 고치자 | E04가 직접 다룸 |
| Uncertainty를 보고 act/ask/learn을 고르자 | E07가 직접 다룸 |
| Reward 모델로 성공 시 종료하자 | E19·E20 및 E01의 이미 존재하는 interface |
| Reset 다양성·curriculum으로 VLA RL 일반화를 높이자 | E10·E16의 직접 충돌 |
| 더 좋은 privileged critic을 VLA에 붙이자 | E14가 privileged signal 선택까지 다룸. VLA라는 적용 대상만으로 부족 |
| RL로 기존 능력의 forgetting을 줄이자 | E21 및 이전 continual-VLA 검토와 중복 |
| World model로 VLA를 평가하자 | E13의 직접 충돌 |

후보를 모두 실험에 넘길 필요는 없다. C4의 차별화·데이터 식별 심사는 [현재안 NO-GO / 진단 연구 보류](../2026-10-21_c4_reward_audit/README.md)로 마쳤다. 이후 사용자 요청으로 C5를 심사해 [일반 방법 NO-GO / 현상 진단 조건부 보류](../2026-10-21_c5_reset_audit/README.md)로 판정했다. C5의 재개 근거가 없어 C6까지 진행했으며 [독립 신규 방법 채택 NO-GO](../2026-10-21_c6_checkpoint_audit/README.md)로 종료했다. 세 후보의 정책 효과를 반증한 실험 결과와 혼동하지 않는다.
