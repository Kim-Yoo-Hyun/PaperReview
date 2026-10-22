# C4 재개 시 진단 계약 — NOT IMPLEMENTATION READY

- Updated: 2026-10-21 KST
- 상태: **설계 초안 / 실행 전제 미충족**. 연구 효과·새 방법의 증거 수준은 CURATION-HYPOTHESIS다.
- 범위: 새로운 acquisition algorithm을 구현하지 않고, 기존 선택법이 native VLA RL에 유효한 조건을 비교한다.

## 1. 하나의 primary claim과 경쟁 설명

**검증할 주장:** 고정된 검수·interaction·update 비용에서 기존 high-reward/policy-value 선택이 uncertainty 선택보다 독립적인 실제 성공률을 개선하는 조건이 있고, 그 조건을 query 전 관측 가능한 통계로 구별할 수 있다.

이는 현재 입증되지 않았다. 단순 high-reward 우위나 reward-accuracy와 success의 불일치 자체는 선행 연구가 다룬다. 독립적인 기여가 되려면 조건이 무엇이며 여러 native policy/task에서 왜 성립하는지 보여야 한다.

| 경쟁 설명 | 구별할 비교 |
|---|---|
| Label을 더 얻기만 하면 된다 | Uniform + 동일 reward 업데이트 |
| 기존 uncertainty/diversity 기준으로 충분하다 | Entropy/disagreement + task-stratified + 중복 억제 |
| 새로운 acquisition이 아니라 기존 active reward learning이다 | High-reward(ReQueST-inspired) 및 IDRL 계열을 포함. 동일 구현이 아니면 adaptation이라고 표시 |
| 성공 사례만 선택한 것이 이득이다 | 같은 경험·같은 유료 label로 success-filtered SFT/return-weighted IL |
| 보상 교정이 아니라 종료 시점이 바뀌었다 | 공통 horizon/termination을 먼저 고정; adaptive termination은 별도 실험 |
| Reward model을 더 좋게 선택하면 끝난다 | 고정된 더 강한 reward model + 동일 RL |
| Push-back이 유효한 새 행동까지 억제한다 | Independent success를 보존하는지 따로 측정. 낮은 reward error만으로 개선 판정 금지 |

## 2. 가장 먼저 확보할 로그

아래는 **요구 필드 목록**이다. 이미 생성·검증한 rollout manifest가 아니다.

| 구분 | 필수 내용 |
|---|---|
| Identity | `episode_id`, 원 수집 episode/view group, task instruction/ID, robot/controller/camera 설정 |
| Policy | Repository commit, checkpoint hash, parent checkpoint, RL update round, actor input/action contract |
| Observation/action | RGB timestamps, 실행 action과 action chunk 경계, intervention 여부; logits는 해당 estimator가 요구할 때만 |
| Reward | Reward checkpoint hash, 입력 prefix 경계, 당시 prediction, 학습 사용 여부, label 요청 이전 시점 |
| Label | Query round, oracle outcome, label 출처/수정 이력, annotation seconds, uncertain/abstain 표시 |
| Split | Original episode/task/seed grouping, RM training overlap, development/query/evaluation 분리 |
| Cost | Env ticks·추가 candidate-policy rollout·reward inference·학습 updates·human seconds·reset 비용 |

동일 base에서 적어도 두 연속 update 구간과 별도 평가 episode가 있어야 시간에 따른 shift를 검사할 수 있다. 이는 충분한 통계 검정력의 표본 수가 아니라 identity의 최소 조건이다. Task와 seed의 규모는 실제 비용·관측 분산을 보고 본 실험 전에 정한다. 파일 이름 순서나 품질 label 순서로 policy round를 만들지 않는다.

## 3. Policy-visible input과 label 경계

- Actor는 native RGB/language/proprio interface를 유지한다. Simulator state나 label을 actor observation에 추가하지 않는다.
- Query unit의 첫 선택은 **완료 episode의 binary success 판정**이다. Prefix/dense progress·pair preference·language correction으로 바꿀 때는 별도 cost contract를 만든다.
- Selector는 instruction, query 전 observation/history, 모델 prediction, policy version, 이전에 실제 구입한 label만 사용한다. `quality_label`, `reward`, `gpt5_mini_check`, failure를 드러내는 filename은 숨긴다.
- Oracle outcome은 query 선택을 마친 뒤 해당 sample에 대해서만 공개한다. Test oracle은 학습·threshold tuning과 분리한다.
- Unknown/시야 밖 결과를 억지로 success/failure로 붙이지 않는다. RGB로 판정 불가능하면 해당 task는 이 설계에서 제외한다.

## 4. 먼저 고정 pool, 그다음 closed-loop

**A. 정적 진단:** 동일한 실제 native rollout pool·initial reward weights에서 uniform, task-stratified, disagreement, predicted-high-reward 선택을 비교한다. 공통 batch와 label budget을 쓰고 선택 후 같은 adaptation steps로 reward를 갱신한다. 미래 checkpoint의 독립 episode에서 잘못된 고보상 비율과 calibration을 평가한다. 여기서는 policy improvement나 학습 인과 효과를 주장하지 않는다.

**B. Closed-loop:** Native base의 부분 성공과 oracle-reward RL의 headroom을 먼저 확인한다. 그다음 같은 초기 checkpoint·seed 묶음에서 frozen, uniform, uncertainty, high-reward, policy-value 계열을 비교한다. 각 방법의 이후 경험이 달라지는 것은 intervention의 일부이므로, 공통 pool 결과와 따로 보고한다. Extra candidate policies를 쓰는 IDRL에는 추가 interaction·학습·추론 비용을 청구한다.

PROGRESSOR는 expert/goal image를 요구하는 다른 정보 조건의 baseline이다. 모든 조건에 같은 추가 정보를 제공하거나 별도 비교군으로 보고한다. UPS의 action intervention과 IJRR의 language feedback은 binary label과 같은 예산으로 둔 채 직접 우열을 주장하지 않는다. Synthetic negatives는 생성/검증 비용과 별도 coverage 효과를 기록한다.

**현재 구현 동결 상태:**

- [ ] Native environment/repository commit과 task ID 고정
- [ ] VLA·reward checkpoint hash 및 학습 contamination 확인
- [ ] 동일 task에서 base rollout·oracle reward pilot 성공
- [ ] Query unit/cost, seed, interaction/update 수, reward adaptation architecture 고정
- [ ] IDRL/PROGRESSOR adaptation의 실제 estimator·objective·추가 정보 조건 고정
- [ ] Trial manifest, leakage checker, acquisition 구현, test report 생성

현재 완료된 metadata audit를 위 체크박스의 실행 결과로 대체하지 않는다.

## 5. Estimator와 공정성의 논리 점검

**Primary:** budget별 독립 평가 성공률 `J(B)`의 normalized AUC. 본 실험 전에 `0=B₀<…<Bₘ=Bmax`와 budget 단위를 동결하고, `Σ(J(Bᵢ)+J(Bᵢ₋₁))/2 × (Bᵢ−Bᵢ₋₁)/Bmax`로 계산한다. Binary query 수와 실제 annotation seconds를 모두 보고하되 비교의 primary cost 축은 미리 하나로 정한다. Interaction budget과 학습 update 수도 공통이다.

**Diagnostics:** Independent false-positive rate, predicted-success 집합의 실제 failure 비율, true-success 감소, calibration, query당 발견 오류 수, 원 episode 중복률. 이들은 RL success의 대체 지표가 아니다. 관측 episode/학습 seed를 단위로 uncertainty를 계산하고 frame IID CI를 쓰지 않는다.

**방문 빈도 중복 가중 주의:** Current-policy pool의 cluster `c`에 이미 `n_c`개 episode가 있으면 uniform episode query도 cluster 확률이 `n_c/N`이다. 각 episode에 다시 `n_c`를 곱해 sampling하면 cluster 확률은 `n_c²/Σn_j²`가 된다. 따라서 “occupancy-aware”라는 이름만으로 새 정보를 쓰는 것이 아니며 흔한 실패를 과도하게 반복 검수할 수 있다. Cluster 단위 선택/중복 억제를 비교하고 occupancy를 한 번만 반영한다. 이 계산은 설계상 반례이며 로봇 실험 결과가 아니다.

**오류를 query 전에 알 수 없음:** `predicted reward × true failure × future policy impact`는 oracle 진단 점수다. Actual label 없는 deployable acquisition이라고 주장하지 않는다. 오류 확률·정책 영향 추정기를 새로 만들려면 먼저 기존 IDRL/CARE와 다른 식별 가능한 이점을 제시해야 한다. 현재 그런 estimator를 확정하지 않았다.

## 6. Go / revise / reject

- **현상 gate:** 실제 RL 과정에서 독립 success와 proxy reward가 벌어지지 않으면 reward-exploitation 연구를 기각한다. 정적 실패 sample을 임의로 모아서 현상을 만들지 않는다.
- **Headroom gate:** Native base가 작동하지 않거나 oracle-reward learner도 개선하지 못하면 acquisition 학습을 시작하지 않는다.
- **간단한 설명 gate:** Uniform/task balance/high-reward audit만으로 충분하면 새 selector를 만들지 않는다. 기존법의 활용 결과로 축소한다.
- **연구 효과 gate:** Primary AUC 개선이 재현되고 annotation·추가 rollout 비용으로 설명되지 않아야 한다. 효과크기·CI·held-out task를 함께 판단한다. 성공을 판정할 최소 차이와 power는 pilot 이후 본 실험 전에 고정하며 지금 임의 숫자를 성공 근거로 넣지 않는다.
- **메커니즘 gate:** 같은 경험의 SFT/weighted imitation이 같은 효과를 내면 RL만의 이득 주장을 삭제한다. 둘 다 유용할 수 있으나 다른 claim이다.
- **현재 판정:** 문헌상의 넓은 method claim은 기각, 데이터 identity gate는 미충족, 정책 효과 gate는 미실행. 이 구분을 유지하고 C4를 구현 직전 project로 승격하지 않는다.
