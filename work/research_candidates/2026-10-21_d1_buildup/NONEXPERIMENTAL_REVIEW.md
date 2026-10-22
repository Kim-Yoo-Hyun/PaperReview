# D1 비실험 재심사 — 우선순위 1–4 완료

- 검토일: 2026-10-22 KST. 대상: 현재 D1의 관측 보정 질문과 OFT/LIBERO 설계.
- 결정: **현재 D1을 독립적인 VLA+RL 신규 방법으로 채택하는 것은 NO-GO. 조건부 robustness 진단은 HOLD.** GPU 확보만으로 실험을 자동 재개하지 않는다.
- 완료 범위: 문헌 충돌, 필요 조건의 논리적 분석, task·평가 설계 반박, RL 필요성 심사. **새 정책 추론·simulator·학습·수치 실험은 0회**다. 실제 효과의 반증이나 논문 불가능성의 증명이 아니다.
- 절차: [기존 buildup 가이드](../../../research/IDEA_BUILDUP_GUIDE.md)의 3–6단계와 내부 반박을 보강했다. 7단계 native 효과 검증과 8단계 실제 외부 피드백은 미완료다.
- 근거 경계: [source 기록](./nonexperimental_sources_2026-10-22.json), [기존 task 감사](./TASK_OBSERVABILITY_AUDIT.md), [L4 설계](./PRE_EXPERIMENT_CONTRACT.md). 아래 논문 보고와 연구자 판단·도출을 구별한다.

## 1. D1-N1 — 주장·실험 단위 직접 충돌 재심사

### 1.1 논문에서 확인한 근거

**GAP — ICLR 2026, pr-0989.** §5.1은 초기 gripper 위치를 고정하고 target 위치를 바꾸며, simulation 100회·real task 20회 평가를 기술한다. Table 1의 simulation은 5 seeds다. Table 3의 Octo threading 성공률은 V/VP/VP+GAP 각각 69/57/78%다. Fig. 4는 시간 구간별 policy intervention, App. B Tables 6–11은 phase decomposition·temporal predictor·hyperparameter ablation, App. C.1 Table 12는 frozen visual feature의 action probing을 다룬다. Modality 역할·phase·단순 masking/gradient 대조까지 이미 비교한다. [공식 원문 §5, App. B–C](https://proceedings.iclr.cc/paper_files/paper/2026/file/2b3bb2c95195130977a51b3bb251c40a-Paper-Conference.pdf).

**G-PSMR — Entropy 2026, pr-0990; top-tier로 집계하지 않음.** Frozen OFT의 state orientation을 `C P0⁻¹ Pt`로 바꾸며 최초 query의 0.07 rad gate를 episode 동안 고정한다. Suite별 clean 25개로 reference를 추정한다. §4.1–4.4는 개발에 사용한 280개, 독립 1120개, 별도 gate-active 600개를 구분한다. 마지막 비교에서 M0→M2는 26.3→32.2%, 회복 52·손실 17회, 차이 +5.8 pp의 CI [+3.2,+8.5]다. 이는 gate-active 조건부 효과다. §4.5는 reference 민감도·gate·충돌·비용을 이미 감사한다. Clean reference 최대 편차 0.0036 rad, blind RI gate 153/160; M2는 query당 1 forward다. 직접 HTML은 429였으며 **publisher의 검색 색인에 노출된 지정 본문 절**을 읽었다. 표 이미지의 전체 cell이나 trial manifest를 확보한 것은 아니다. [Publisher §3.5, §4.1–4.5](https://www.mdpi.com/1099-4300/28/9/975).

**ReViP — pr-0981; accepted venue 미확인.** arXiv 최신 표시는 v3(2026-03-12)다. v3 Table 7은 observer 변경, Table 8은 FiLM 계수 대조이며 drop subset의 고정 0.5/learnable은 62.4/65.2%다. 이는 cause-conditioned restoration 실험이 아니다. [v3 §5.6](https://arxiv.org/html/2601.16667v3), [version 기록](https://arxiv.org/abs/2601.16667). 최신 저자 project는 8개 drop/swap/relayout task, visual stage cue·attention rebalance·Flash distillation을 설명하고 OFT FCSR 19→41%를 보고한다. 따라서 v3의 FiLM만으로 최신 방법을 대표시키면 불충분하다. Project의 manuscript/supplement 링크는 이번에도 도구에서 본문을 열지 못했고 code는 coming soon이다. 최신 원문 전체·ablation·학습 조건은 **미확인**이다. [저자 project](https://isee-laboratory.github.io/ReViP/).

위 수치는 각 논문의 조건부 보고다. 서로 다른 task·checkpoint·학습·분모의 수치로 방법 순위를 만들거나 D1의 예상 효과를 채우지 않는다. GAP 공개 code와 공식 수식의 불일치는 [L1 감사](./BASELINE_METHOD_AUDIT.md)에 남아 있으며 code 문제를 논문 현상 자체의 반증으로 쓰지 않는다.

### 1.2 주장별 차이와 판정 — 연구자 판단

| D1 잠정 주장 | 직접 겹침 / 반대 설명 | 판정 |
|---|---|---|
| Proprioception 의존 때문에 시각 변화에 반응하지 못한다 | GAP의 시간별 intervention·feature probing, ReViP의 progress-conflict | 신규 발견으로 제외 |
| Frozen VLA에서 stream별 오류를 감지·보정한다 | G-PSMR gate·orientation 복원·결합 비교 | 신규 메커니즘으로 제외 |
| 실제 자세 변화에는 보정하면 안 된다 | G-PSMR이 실제 initial-pose shift에서도 이득을 보고 | 전제 철회. 원인보다 task utility로 판단 |
| 평균 이득에 가려진 harmful correction을 처음 감사한다 | G-PSMR의 recovered/lost pairs·reference 민감도 | 손해 사례의 존재만으로 새 기여 부족 |
| Task별 reference를 쓰면 해결된다 | 기존 suite reference를 세분한 대안일 수 있음 | 필수 단순 baseline; 기여로 승격하지 않음 |
| Mid-episode에 gate를 다시 열면 된다 | 초기 고정 gate의 직접 변경; causal residual/재보정으로 설명 가능 | 동적 gate 추가만으로 신규성 부족 |
| 동일 정보·비용에서 보정 선택이 필요한 조건을 설명한다 | 위 자료가 모든 조건을 답한 것은 아님 | 미개척 gap으로 확정하지 않음. 실제 witness 필요 |

**남는 차이는 아직 현상이 아니라 질문이다.** Report-only 오류 R과 실제 초기 자세 변화 P에서 이득이 다르다는 것만으로 cause classifier가 필요하지는 않다. 분포 난이도, calibration mismatch, 추가 관측·query, 일반 adaptation이 대안이다. 단순 복원이 양쪽에서 모두 좋으면 현재 method motivation은 사라진다. 손해 사례가 있어도 사전에 구별 가능하고 다른 선택으로 회복되는지 확인해야 한다.

**N1 완료:** broad claim들은 충돌하며 좁은 claim은 empirical witness 미확보다. 구현·최신 원문 일부의 미공개/접근 불가는 연구 가치를 긍정하는 근거가 아니다. 남은 release 의존성은 TODO D1-R1에 보존한다.

## 2. D1-N2 — 보정 선택이 필요한 조건

아래는 기존 의사결정 이론을 D1에 적용한 **연구자 도출**이다. 새로운 정리나 실험 결과가 아니다. Belief가 history의 충분통계가 되는 표준 POMDP 전제와 계획 관점은 [Kaelbling·Littman·Cassandra, Artificial Intelligence 1998, §3.3–3.4](https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf)를 따른다. 실제 VLA가 정확한 belief/model을 갖는다고 가정하지 않는다.

### 2.1 원인 label 대신 선택에 필요한 정보

`h`는 허용한 두 RGB view, raw proprioception, goal g, query 시점까지의 command/관측 history, calibration을 모두 포함한다. Wrapper가 볼 수 없는 controller memory·true pose·fault label·미래 결과는 제외한다. `z`는 h와 양립하는 실제 상태·오류 가설이다. 편의를 위해 후보 z와 선택 집합 U를 유한하게 두고 reward/cost가 유계라고 가정한다.

`u ∈ U`는 비보정, 정해진 orientation 보정, causal 재보정처럼 **명세가 고정된 선택**이다. `Q(z,g,u)`는 같은 horizon·비용·고정 continuation 정책에서 u를 택했을 때의 기대 task utility다. 서로 다른 continuation을 섞거나 classifier 정확도를 Q로 대신하지 않는다.

```text
Aε(z,g) = {u : Q(z,g,u) ≥ max_v Q(z,g,v) − ε}.
```

1. **공통 선택이 충분:** `∩z Aε(z,g)`가 비어 있지 않으면 공통 선택은 모든 양립 조건에서 ε 이내다. 정확한 원인 분류는 이 선택 문제에 필수가 아니다. 공통 선택을 실제로 찾는 계산·학습 문제는 남는다.
2. **선택이 다르고 식별 가능:** 공통 선택이 없고 가용 h가 조건별 utility를 예측할 정보를 주면 조건부 선택을 검토할 수 있다. 원인 이름보다 `Q(u)−Q(v)`의 부호가 직접적인 목표다. 단순 residual도 이 역할을 할 수 있다.
3. **선택은 다른데 정보 부족:** 동일 h에 양립하는 조건의 공통 선택이 없으면 h만 쓰는 결정적 selector는 모두를 만족시킬 수 없다. Classifier/RL을 붙여 정보 부족을 제거할 수 없다. 확률적·보수적 선택이나 추가 정보의 비용을 평가한다.

한정된 반례로 z1에서 u1, z2에서 u2만 최적이고 잘못 고르면 손실 Δ>0인 이진 문제를 보자. 같은 h에서 u1을 확률 p로 고르면 regret는 각각 `(1−p)Δ`, `pΔ`다. 최악 regret는 적어도 Δ/2이며 p=1/2에서 달성된다. **분석용 반례이며 LIBERO 측정값이 아니다.** 미래의 다른 관측을 얻는다면 당시의 정보 경계를 다시 계산한다.

### 2.2 분류가 아니라 정보 가치가 양수여야 함

Posterior b(z|h,g)가 주어졌다고 가정하면:

```text
Vblind = max_u Σz b(z) Q(z,g,u)
Vperfect = Σz b(z) max_u Q(z,g,u)
EVPI = Vperfect − Vblind ≥ 0.
```

유한 U에서 b가 양수인 모든 조건에 공통 최적 선택이 있으면 EVPI=0이다. 반대로 EVPI=0을 달성하는 blind 선택은 각 조건에서도 최적이어야 하므로 공통 최적 선택이 있다. 이는 **완전 정보의 이론적 가치**다. GT를 줘도 frozen policy가 활용하지 못할 수 있는 기존 D0를 Vperfect와 동일시하지 않는다.

실제 추가 측정 y의 정보 가치는 `E_y[max_u E(Q|h,g,y)]−max_u E(Q|h,g)`다. 세계 상태·선택 집합이 그대로이고 측정을 무시할 수 있는 무료 정보라면 음수가 아니다. 능동 probing은 상태·시간·contact risk를 바꾸므로 이 부등식을 그대로 적용할 수 없다. 전체 return에서 측정·행동 비용을 빼야 한다. 관측 가능성만으로 유익한 보정이나 RL 필요성이 따라오지 않는다.

### 2.3 Frozen policy 적응과 정보 보존의 구별

보정 T(h)가 h의 결정적 함수이고 추가 정보를 쓰지 않는다면, h를 보는 자유로운 정책은 T와 후속 정책을 내부에서 그대로 모사할 수 있다. 따라서 최적으로 설계할 수 있는 전체 정책 집합에서는 전처리 자체가 새 정보를 만들지 않는다. 반면 **고정된 πθ**에서는 `πθ(T(h))`가 `πθ(h)`보다 좋을 수 있다. Training distribution에 더 맞는 표현을 주기 때문이다.

Frozen OFT에서 보정이 유익/유해하다는 증거는 먼저 **그 checkpoint의 representation 적합성**에 대한 증거다. Task 자체의 근본적인 원인 식별 필요성이나 모든 VLA의 정보 손실을 바로 뜻하지 않는다. Wrapper가 raw h를 보존했다면 backbone state가 바뀌어도 전체 system이 원정보를 잃었다고 할 수 없다.

### 2.4 SO(3) 특수식에서 남는 조건

[L2의 도출](./CLAIM_EVIDENCE_CONTRACT.md#2-수식으로-먼저-제거할-약한-주장)을 더 분리하면:

```text
Pt = B Rt, B는 episode 내 고정
T(Pt) = C P0⁻¹ Pt = C R0⁻¹ Rt = A Rt,  A = C R0⁻¹.
```

Gate ON이면 report bias B는 사라지지만 **reference 오차 A는 남는다**. C=R0일 때만 true Rt를 얻는다. 이득이 A에 좌우된다면 원인 분류보다 reference 추정이 병목이다. Gate OFF이면 소거가 적용되지 않으며 B가 gate 결정을 바꾸므로 **전체 gated system이 B-invariant라는 주장은 성립하지 않는다**. Axis-angle 변환 뒤 clipping도 행렬 단계의 등식과 frozen-policy 효과를 구분해야 하는 이유다.

물리 변화 조건에서는 T(P0)=C여도 RGB·position·gripper·controller truth가 남을 수 있다. Absolute orientation goal이 없다는 사실은 모든 회전에 대한 invariance의 증명이 아니다. Absolute orientation이 필요한 task 역시 cause label의 필요성을 자동으로 증명하지 않는다.

**N2 완료:** 필요 조건은 `선택 utility 차이 + 가용 정보로 그 차이 예측 + 비용을 제하고도 남는 이득 + 단순 대안 이후 잔여 차이`다. 이를 실제 D1에서 모두 만족한다는 증거는 없다. 수식의 타당성과 empirical 존재를 분리했다.

## 3. D1-N3 — 현재 task의 적합성 반대 심사

### 3.1 Task별 source와 판정

고정 commit의 task 3개, predicate, object-state, OSC controller **6개 파일을 다시 읽었고 기존 hash와 모두 일치**했다. Source 실행은 하지 않았다. Goal predicate가 EEF orientation을 직접 요구하지 않는다는 기존 결과를 유지한다. Contact 경로에서 orientation이 중요할 가능성까지 부정하지 않는다.

| 후보 | Source가 보장하는 것 | 가장 강한 반대 설명 | 역할 판정 |
|---|---|---|---|
| Goal 0: middle drawer | Open wooden_cabinet_1_middle_region; cabinet open 상태 검사 | 손잡이 접근·grasp geometry는 중요할 수 있지만 small yaw 변화에 다른 보정이 필요한지는 모름. RGB feedback·동일 canonical approach로 충분할 수 있음 | 재개 시 조건부 articulated-task 진단 후보. Cause-necessity primary로 미채택 |
| Goal 8: bowl on plate | On bowl plate; contact·상대 위치 검사 | Bowl yaw가 placement 목표와 크게 무관할 수 있음. 손해도 grasp 실패·clipping·OOD로 설명 가능 | Placement 대조 후보. 핵심 novelty task로 미자격 |
| Goal 1: bowl on stove | On bowl stove-cook-region; Goal 8과 target이 다름 | Instruction에 따라 target을 바꾸는 능력과 orientation 보정 선택은 다른 문제 | Language/target contrast 전용. Cause identification 증거 아님 |
| Goal 7: turn on stove | 기존 L3의 joint-based Turnon 정의 | Articulation이라는 이유만으로 orientation 보정 gap이 생기지 않음 | 보조 후보 유지, 기본 schedule 추가 안 함 |

근거: [drawer BDDL](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/bddl_files/libero_goal/open_the_middle_drawer_of_the_cabinet.bddl#L123), [plate BDDL](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/bddl_files/libero_goal/put_the_bowl_on_the_plate.bddl#L124), [stove BDDL](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/bddl_files/libero_goal/put_the_bowl_on_the_stove.bddl#L124), [predicate](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/envs/predicates/base_predicates.py#L62), [object/site 판정](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/envs/object_states/base_object_states.py#L78). Goal 7은 [L3 기존 확인](./TASK_OBSERVABILITY_AUDIT.md)을 재사용했다.

### 3.2 L4에서 가능한 해석과 불가능한 해석

**R/P는 원인만 바꾼 동일 관측 쌍이 아니다.** R은 policy report orientation만 바꾼다. P의 OSC prelude는 실제 pose와 wrist image, 경우에 따라 position/contact/controller 목표를 바꾼다. 같은 initial-state ID와 action step 수로 맞춰도 차이는 남는다. 각 stratum 내부의 동일 reset에서 보정/비보정을 비교하면 operator의 조건부 효과를 볼 수 있지만 stratum 차이가 원인 식별의 필요성을 뜻하지 않는다.

**Native controller의 완충 가능성을 배제하지 못했다.** Policy report와 별도로 OSC는 true feedback을 사용한다. Zero-rotation command가 직전 orientation goal을 유지할 수도 있다. P prelude 뒤 dummy step이 중립 자세로 되돌린다고 가정하면 안 되며, report 보정 없이 feedback으로 충분할 가능성도 있다. [Controller set_goal](https://github.com/ARISE-Initiative/robosuite/blob/c848ca848020d0c4ccdd10c5056bd06f2a195ba2/robosuite/controllers/osc.py#L254). 실제 충분성은 미측정이다.

**G1 통과는 유용한 proprioception의 증명이 아니다.** Clean competence와 corruption 손실은 진입 screening이다. 비정상 입력에 깨지는 모델과 그 입력에서 유용한 정보를 얻는 모델은 같지 않다. 정답 inverse로 R을 취소하는 D0도 원입력을 되돌리는 sanity check다. Matched training의 vision-only 대조나 물리적으로 유효한 state 정보의 추가/제거 비교가 없으면 proprioception 필수성을 주장하지 않는다. Normalized-zero B1도 OOD 진단에 한정한다.

**Language contrast도 보정 interaction을 요구한다.** Goal g, stratum z에서:

```text
Δ(g,z) = J(g,z,correct) − J(g,z,identity)
I = [Δ(gA,R) − Δ(gA,P)] − [Δ(gB,R) − Δ(gB,P)].
```

Correct/wrong prompt 성공률 차이는 goal 활용의 screening이다. I와 같은 보정×조건×goal 관계를 보지 않고 goal-conditioned correction을 주장할 수 없다. I≠0이어도 인과 해석은 별도이며 goal별 난이도·horizon·현재 task-state 차이를 통제해야 한다. 이는 **추정량의 개념 정의**이며 실제 값·유의성·confirmatory threshold는 없다. 8/1의 동일 물리 장면과 두 goal의 시작 시 미달성을 확인하는 reset gate도 미충족이다.

**Holdout의 범위를 좁힌다.** 같은 세 task에서 초기 상태/perturbation만 나눈 split은 held-out task 검증이 아니다. 0/8/1에서 좋은 결과가 나와도 새 task·embodiment로 일반화하지 않는다. DEFAULT .pruned_init 경로는 추가적인 expert-success filtering을 피하지만 원본 asset 자체의 선택 편향을 제거하는 것은 아니다.

**N3 완료:** 현재 task는 제한된 operator 진단 후보지만 핵심 novelty를 입증할 task로는 아직 자격이 없다. 모든 task를 부적합하다고 단정하거나 새 환경을 만드는 대신 기존 후보·설계는 **재심사 전용 보존본**으로 남긴다.

## 4. D1-N4 — RL 필요성과 최종 연구 위치

### 4.1 학습할 문제가 무엇인지 분리

| 남은 문제 | 먼저 고려할 해법 | RL 판단 |
|---|---|---|
| 고정 bias/reference mismatch 추정 | Algebraic calibration, geometry/visual residual, supervised state estimation | 가장 직접적인 대안. RL 필요 근거 없음 |
| 현재 관측에서 보정 후보 utility 순위 예측 | Outcome-labelled predictor, validation 기반 규칙. Paired outcome은 실제 비교로 얻어야 함 | Label 생성 비용은 남지만 순차 RL이라고 자동 분류하지 않음 |
| Episode 시작에 고정 wrapper 하나 선택 | Episode return을 보상으로 하는 contextual decision/bandit formulation 가능 | 내부 robot trajectory가 길어도 selector가 multi-step RL일 필요는 없음 |
| 매 query 보정·보류가 미래 상태/관측을 바꿈 | Belief/model-based planning, history-conditioned policy, RL 비교 | 순차 objective의 근거는 될 수 있음. RL algorithm의 독점적 필요성은 아님 |
| 움직여 정보를 얻고 미래 task 성공을 높임 | Active diagnosis/control와 정보·위험 비용 비교 | 선행이 있음. 새 이름으로 기존 보류 주제를 재개하지 않음 |

POMDP는 불완전 관측의 모델이지 RL 학습 의무가 아니다. 알려진 모델에서는 planning, 충분한 행동 supervision이 있으면 IL도 후보가 된다. [POMDP 원문 Introduction, §3.4](https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf). 인접 분야는 이미 Bayesian fault-hypothesis update, 정보 이득과 tracking penalty, MCTS 기반 active diagnosis를 다룬다. **Active probing 자체도 신규성이 아니다.** [Han et al., arXiv v1 §V, Eq. 11–14](https://arxiv.org/html/2509.18460v1).

현재 L4에는 능동 probe action set·비용·안전 제약이 없고, 즉시 손해를 감수해 미래 이득을 얻어야 한다는 witness도 없다. 모든 robot 행동이 미래 상태를 바꾼다는 일반론으로 RL을 정당화할 수 없다. 반대로 RL이 절대로 유용하지 않다는 결론도 아니다.

RL 후보로 재심사하려면 **비근시적 선택의 실제 이득**, 동일 관측/상호작용/학습/추론 예산의 규칙·추정·IL·planning 대조, 기존 연구와의 차이가 필요하다. Fault label·미래 return을 배포 selector의 입력으로 주면 안 된다. 한 embodiment의 이득을 여러 로봇에 대한 RL 전이로 확대하지 않는다.

### 4.2 Buildup 기준에 따른 최종 심사

| 검사 | 근거 상태 | 판단 |
|---|---|---|
| VLA 관측 불일치의 존재 | 문헌 지지 | 있음 |
| D1이 추가하는 중요한 질문 | 조건부 선택 필요성이라는 질문 구체화 | 실제 witness·재사용할 발견 미확보 |
| 가까운 연구 이후 차별성 | Broad claim 직접 충돌; reference/gate 확장은 단순 대안 | 현재 method 채택 근거 부족 |
| 가설의 식별 가능성 | 일반 필요 조건 도출; R/P·task 대비는 강한 인과 주장 미지원 | 진단 범위로 제한 |
| 강한 baseline 이후 개선 여지 | Native competence·utility·residual gap 미실행 | 미확인 |
| RL 필요성 | 고정 보정/추정 대안, 순차 이득 미확인 | RL method 투자 근거 없음 |
| 실행 자원 | 기존 E1 resource gate 미충족 | 별도 제약. 위 연구 약점의 원인은 아님 |
| 외부 비판 | 내부 반박만 완료 | F1 실제 피드백 미완료 |

**현재 설계에 대한 투자 NO-GO**다. D1 전체 분야가 해결됐거나 empirical hypothesis가 거짓이라는 뜻은 아니다. 본격 RL·learned selector 구현 대신 문헌·수식·baseline·평가 계약을 재사용 가능한 기록으로 보존한다. 조건부 진단은 HOLD이며 GPU만 확보됐다고 E1/G2를 자동 재개하지 않는다.

### 4.3 다음 행동과 재개 조건

**D1-R2 — 재개 근거 심사(WAITING_EVIDENCE)**를 다음 gate로 둔다. 공개 source나 구체적인 task 분석에서 아래 세 가지를 함께 제시할 때 제한된 진단 pilot을 재검토한다.

1. 물리적으로 타당한 task/조건에서 두 보정 선택의 예측이 갈리는 구체적 사례. 오류 크기 증가·task 이름 교체로 대체하지 않는다.
2. 그 차이를 실행 전에 예측할 native observation/history cue와 정보·비용 계약. Cause label·미래 정보는 제외한다.
3. Canonicalization·reference 추정·causal residual로 이미 설명되지 않을 근거와 반증 가능한 최소 비교.

이는 pilot 재개를 위한 **검증 가능한 예측**을 요구하며 실험 전에 효과를 증명하라는 순환 조건이 아니다. 재개 후에도 native G0/G1과 paired reset qualification부터 통과해야 한다. Learned method/RL 승격에는 실제 residual gap과 비용을 포함한 이득이 추가로 필요하다.

R1은 공개 자산의 source follow-up으로 남긴다. E1 자원 미확보 기록은 유지하되 실행 queue는 연구 근거 보류로 바꾼다. 새 주제 탐색·외부 발송은 이번 작업에 포함하지 않았다. Registry·tier·사용자 읽기 상태는 변경하지 않았다.
