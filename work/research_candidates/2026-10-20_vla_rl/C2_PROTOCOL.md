# C2 제한 진단 설계 — 실행 freeze 이전

- Updated: **2026-10-21 KST**
- 상태: **G0·G1 1차 검사 후 현재 설계 NO-GO. 학습·추론·rollout 미실행.** [실측 결과](../../experiments/vla_rl_c2_first_pass/RESULTS.md) · [연구 가치 판단](./C2_BUILDUP_RESULT.md).
- [연구 판단](./C2_REVIEW.md) · [평가 감사](./C2_DATA_AUDIT.md) · [실제 task 분할 초안](./C2_SPLIT_DRAFT.json)
- 실험 장소: 현재 컴퓨터의 Docker만 허용. Host/MPS·원격 GPU로 우회하지 않는다.

## 1. 질문과 주장 범위

**관측된 atomic/pair coverage를 맞추고 trajectory·annotation 예산을 통제했을 때, 수행 제약을 포함한 RL objective가 balanced SFT와 return-weighted imitation보다 새로운 object×waypoint×orientation 조합에서 유리한가?**

첫 대상은 RoboFollow Scene 3의 right arm 8개 native task다. `source→blue label 6`을 goal로 두고, 거치는 waypoint와 최종 orientation을 how로 둔다. Task pair는 source·destination·초기 물리 상태가 같고 how만 달라야 한다. 새 backbone·reward learner·hierarchical policy를 먼저 만들지 않는다.

이 선택은 seed를 공유하는 실제 상태 쌍의 feasibility가 확인되어야 유효하다. 공개 task 이름이 있다는 사실만으로 양쪽이 같은 초기 상태에서 가능하다고 판정하지 않는다.

## 2. 입력·평가 계약

| 항목 | 설계 |
|---|---|
| Policy input | Native RGB views, proprioception, full instruction. History 사용 여부는 선택 checkpoint의 native contract로 고정 |
| 숨길 정보 | Task ID, split label, object poses, waypoint/orientation 판정, success bit, expert phase는 actor 입력에서 제외 |
| Action | 선택 checkpoint의 native 14D robot action과 adapter convention 유지. Primitive/controller 변경을 RL 이득에 섞지 않음 |
| 시간 | Action targets, policy calls, physics time, wall time을 각각 기록. Timeout을 실패나 완료 episode로 임의 치환하지 않음 |
| Goal `G` | 해당 object의 destination 도달·안정 배치. Waypoint와 orientation을 빼고 별도로 정의 |
| Waypoint `Cw` | Native evaluator의 object-trajectory 의미를 명시. 실제 contact avoidance로 바꾸지 않음 |
| Orientation `Cr` | 명시된 좌표계·대칭성·허용 오차·평가 시점에 따른 최종 orientation |
| Primary `J` | 모든 평가 trials에 대해 `mean(G ∧ Cw ∧ Cr)`. `G`, `Cw`, `Cr`, 실패 유형도 별도 공개 |
| Supplementary | Native intent/execution/completion score를 원 정의로 보고. Native completion을 `J`로 간주하지 않음 |

현재 `G`의 독립 구현과 full-trace label validator는 생성하지 않았다. 원 evaluator의 gating된 stage 점수만으로 독립 goal bit를 역산하면 실패 원인을 혼합할 수 있으므로, 구현 전에 명확한 predicate가 필요하다.

Instruction sensitivity는 raw action distance가 아니라 **동일 초기 상태의 지시 쌍을 각각 실행해 두 요구를 모두 올바르게 만족하는 비율**로 검사한다. 단순히 행동이 달라졌다는 것은 instruction following의 증거가 아니다.

## 3. 데이터·split 통제

1. 초안의 4개 train triple만 adaptation에 사용한다. 그중 검증에 쓸 episode는 학습에서 제외한다. Holdout triple 4개는 별도 평가다.
2. 동일 초기 scene/state의 pair, 한 trajectory에서 파생한 relabel, segment와 paraphrase는 같은 data partition에 묶는다.
3. 최종 평가에서는 **새로운 scene seeds**에 대해 seen triple의 ID 결과와 unseen triple 결과를 함께 측정한다. 이 평가 내에서 instruction pair를 구성하므로 train/test 간 scene 중복이 필요하지 않다.
4. Counterfactual relabel은 물리 scene·dynamics·goal이 같고 기록된 전체 trace로 참/거짓을 판정할 수 있을 때만 한다. Action chunk를 바꾸고 기존 next observation을 붙이지 않는다.
5. SFT는 만족하는 instruction–trajectory pair만 사용한다. Negative label은 단순 SFT의 정답 action으로 넣지 않는다. Label 예산이 같다는 말과 loss가 같은 supervision을 소비한다는 말을 구분한다.
6. Positive·violation·ambiguous trajectory 수, 각 factor/pair frequency, contact/geometry 근거, annotation 비용을 기록한다. Unknown을 negative로 강제하지 않는다.
7. Pretraining data가 불명확하면 **post-training에서 제외한 조합**이라고만 표현한다. 모델이 생애 처음 보는 조합이라는 주장은 금지한다. 전체 RoboFollow로 학습된 checkpoint를 가져오면 이 holdout의 의미를 재설정해야 한다.
8. 원 지시에 모두 성공·준수하는 demonstrations만 있으면 두 terminal reward가 같다. 동일 goal의 다른 **training instruction**에 대한 유효한 relabel 또는 실제 위반 trajectory로 reward contrast가 있는지 먼저 검사한다. Holdout instruction을 relabel에 사용하면 이 연구의 instruction-combination holdout을 오염시키므로 제외한다. Negative가 없으면 reward 효과의 식별을 주장하지 않는다.

Paraphrase와 실제 constraint 변경은 별도 축이다. 4/4 구조가 보장하는 것은 task-level pair coverage뿐이다. 작은 정적 설계의 통과를 continuous state/action coverage 통과로 바꾸지 않는다.

## 4. 비교군과 무엇을 식별하는가

첫 비교는 **고정 offline dataset**이다. 같은 초기 checkpoint·actor 구조·학습 가능 parameter·optimizer budget 범위·train/validation membership을 사용한다.

| 비교군 | 목적 |
|---|---|
| Native base | 원래 goal/constraint competence와 불균형 확인 |
| Balanced SFT / segment-enriched SFT | 동일 demonstrations의 coverage·annotation만으로 해결되는지 |
| Return-weighted imitation | 같은 trajectory에 complete reward로 계산한 return을 주었을 때 단순 선택/가중으로 설명되는지 |
| Goal-only offline RL | Terminal `r=G`를 최적화하는 비교 |
| Complete-reward offline RL | 같은 RL algorithm에서 terminal `r=G∧Cw∧Cr`로 변경한 비교 |
| Standard constrained RL | Goal objective와 constraint cost를 분리한 표준 방법으로 충분한지 |
| CounterAlign-style alignment reward | 학습 reward가 privileged predicate와 다른 일반화를 보이는지. 원 code 재현과 자체 adaptation을 구별 |

첫 RL 비교 algorithm은 IQL 계열을 우선 검토하지만, 해당 native actor와 compatible한 구현·설정이 없으므로 아직 확정하지 않았다. Flow matching이면 actor extraction과 return-weighted baseline의 표현력을 맞춰야 한다. Complete reward를 새 objective 기여로 주장하지 않는다.

LangForce/RSS 및 ExecVLA는 중요한 외부 비교다. Backbone·데이터·입출력이 다르면 matched ablation과 별도 표로 보고한다. CounterAlign에는 추가 annotation이 없다는 장점이 있으므로 privileged label을 사용하는 후보가 같은 비용이라고 주장하지 않는다.

Online 단계가 필요하면 **동일 exploration data를 imitation에도 제공하는 비교**와 각 방법이 자기 rollout을 모으는 comparison을 분리한다. 성능 차이를 interaction과 optimizer 중 어느 하나로 섣불리 귀속하지 않는다. 이번에는 online 단계에 진입하지 않는다.

## 5. 순서와 중단 기준

| Gate | 확인 사항 | 현재 상태 / 실패 시 처리 |
|---|---|---|
| **G0 데이터·predicate** | 선택 8개 task의 실제 episode manifest, 양성/위반/unknown label과 reward contrast, 같은 scene의 instruction pair, train/test leakage | **검사 완료·원 계약 미충족.** Inventory 400개, payload 12개 및 training route 50개 확인. 완전한 goal/orientation 판정·coverage·state grouping은 확보하지 못함 |
| **G1 native 실행** | 정확한 checkpoint revision·전처리·action convention·Docker image·환경 commit·seed·bounded runtime | **Reference 경로 미충족.** ARM64의 pinned binary resolver와 GPU 할당 실패, compatible trained checkpoint 미식별. Data reader 실행 성공과 구분 |
| **G2 support 확인** | 양쪽 지시의 feasible expert trace, native base goal competence, constraint 행동의 지원 | **미실행.** G0·G1 미충족으로 진입하지 않음 |
| **G3 offline 비교** | 같은 data/labels에서 SFT·return weighting·goal-only/complete RL 비교 | **미실행.** 현재 1차 검증의 pending TODO가 아니라 재개 조건 이후의 단계 |
| **G4 설명·외적 타당성** | 예산을 맞춘 coverage intervention, 다른 heldout split·task 조건에서 같은 설명 성립 | **미실행.** 현재 결과를 정책 효과나 다양한 로봇의 일반화 증거로 사용하지 않음 |

데이터 검사용 episode inventory와 Docker image digest는 [1차 실행 기록](../../experiments/vla_rl_c2_first_pass/RESULTS.md)에 생성했다. Policy checkpoint, 실행 가능한 train/test episode split, 학습·평가 예산, evaluation seeds/trials, 독립 goal/orientation predicate는 **미고정**이다. 따라서 이 문서는 executable policy project specification이 아니다.

| 결과가 관찰되면 | 연구 판단 |
|---|---|
| Balanced SFT로 해결 | RL 필요성 주장 중단 |
| Return weighting과 RL 차이가 없음 | 선택/가중을 넘는 RL 효과 미입증 |
| Complete-reward standard RL로 해결 | 새 RL 알고리즘 구현 중단; reward 조건에 대한 설명의 일반성을 따로 평가 |
| Pair coverage를 보강하면 방법 차이가 사라짐 | 데이터 지원 설명을 우선 |
| Goal은 낮아지고 compliance만 상승 | joint improvement claim 기각 |
| 완전한 reward에서도 모든 방법이 실패 | Representation/support/optimization을 구분해야 하며 reward omission만의 문제라고 할 수 없음 |
| Reward fitting 또는 checkpoint에 holdout이 포함됨 | Compositional generalization 주장 철회·split 재설계 |
| 현재 Docker 환경에서 native pilot 불성립 | Toy policy의 성공으로 대체하지 않고 실행 gate 미충족으로 종료 |

최종 방법 비교에서는 training seed와 scene/task cluster를 구분해 uncertainty를 산출한다. Paraphrase 여러 개나 동일 rollout의 relabel을 독립 trial 수로 세지 않는다. 효과 크기·goal 비열등성 허용치·확장 예산은 G1 비용 측정 후, G3 test 결과를 보기 전에 고정한다.
