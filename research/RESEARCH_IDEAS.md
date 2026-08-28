# Robotics Research Ideas

- Updated: 2026-08-28 KST
- Research stance: Robotics가 주축이며 VLA와 3D perception은 실제 closed-loop behavior를 개선하는 구성요소로 다룬다.
- Gap source: [RESEARCH_GAPS.md](./RESEARCH_GAPS.md)
- Lineage source: [synthesis/](../synthesis/README.md)
- Literature basis: 12개 아이디어는 기존 gap의 `READING-SUPPORTED` 원문 감사에 근거하며, 2026-08-26 gap closure audit의 venue-confirmed paper와 preprint collision check를 구분해 반영한다.
- Gap-method alignment: 2026-08-26에 6개 macro-gap과 robotics `R-M-C-O-T-S` 범위로 재검토했다. 13개 gap 중 11개는 `narrowed`, 2개는 `partially addressed`이므로 broad novelty claim은 사용하지 않는다.
- Hypothesis status: 모든 아이디어는 아직 `UNTESTED`다. 문헌 근거가 있다는 사실과 제안 가설이 실험적으로 지지됐다는 사실을 구분한다.
- Project specs: [RP-2 Same-Onset Failure Recovery Arbitration](./projects/RP-2_FAILURE_RECOVERY.md), [RP-3 Phase-Aware Memory Expiry](./projects/RP-3_MEMORY_EXPIRY.md)
- RP-2 reading spine: [P0–P4 priority reading sequence](#rp-2-i-02-priority-reading-spine) — 전체 dependency는 [READING_PLAN.md](./READING_PLAN.md#rp-2-i-02-priority-reading-sequence)를 canonical source로 둔다.
- RP-2 novelty status: `CONDITIONALLY_FIT / CURRENT FOCUS` — 현재 가장 강한 P1 방향이지만, novelty는 same-onset counterfactual option crossing과 matched-budget selector regret로 입증해야 한다.

## 이 문서의 역할

`RESEARCH_GAPS.md`가 원문 비교 후 남은 문제를 기록한다면, 이 문서는 그 문제를 **기존 논문에서 검증된 방법 요소를 조합한 반증 가능한 연구 가설**로 바꾼다. 13개 gap을 12개 독립 project로 해석하지 않고, 6개 macro-gap에 대응하는 연구 프로그램 안의 decision experiment로 취급한다. 방법론은 임의로 발명하지 않고 아래 네 층으로 구분한다.

1. **방법론 근거:** 어떤 논문의 어떤 요소를 가져오는가.
2. **Gap alignment:** 어떤 macro/sub-gap의 claim을 어떤 `R-M-C-O-T-S`에서 검사하는가.
3. **새 연구 단위:** 선행 연구가 각각 다룬 요소 사이에서 무엇을 새로 연결하거나 통제하는가.
4. **Decision rule:** 어떤 결과에서 가설을 지지·축소·기각하는가.

논문의 module 이름만 바꾸거나 이미 입증된 결합을 반복하지 않는다. 예를 들어 slow–fast tactile VLA 자체는 Reactive Diffusion Policy와 AT-VLA가, hybrid force–position VLA는 ForceVLA2가 이미 다룬다. 새 연구는 cross-sensor transfer, calibration, uncertainty 또는 safety처럼 원문에서 남긴 경계를 검증해야 한다.

## 2026-08-26 gap-to-idea reassessment

최신 논문이 이미 닫은 broad claim은 아이디어에서 제거했다. 아래 표의 `잔여 연구 단위`만 active hypothesis로 취급하며, 관련 최신 연구는 새 module의 motivation이 아니라 strong baseline 또는 novelty-collision evidence로 사용한다.

| Macro / ideas | 최신 연구가 이미 해결한 범위 | 아이디어에 남긴 잔여 연구 단위 | Portfolio decision |
|---|---|---|---|
| M-1 / I-01 | AT-VLA·ForceVLA2·TACTIC은 fast/contact-centric control을, TactAlign·UniForce는 heterogeneous tactile alignment를 보여줌 | sensor-OOD에서 contact-state uncertainty에 따라 fast-control authority를 줄이거나 차단하는 calibration | `RETAIN / E1`, hardware dependency |
| M-2 / I-02·I-12·I-06 | FLARE, ViFailback, AgentChord, UPS와 SPR·FAR·CoRe·VLCP가 서로 다른 recovery family를 직접 다룸 | 동일 cloned onset에서 abstraction-level option value를 비교하는 budgeted arbitration; option-outcome table과 common event schema | **`FOCUS`**: I-12 → I-02 → optional I-06 |
| M-3 / I-03·I-07·I-09 | AFI/HALO가 drift·memory trap을, ActiveVLA·SaPaVe가 active view/camera action을 직접 완화 | memory expiry risk calibration, compute-matched 3D control utility, physical camera cost를 포함한 value-of-information stopping | `RETAIN`, I-07 E1 후 I-09 E2 |
| M-4 / I-04 | WorldGym·PolaRiS·Interactive World Simulator가 policy ranking을, WMPO·RISE·Visual Verification이 policy improvement를 입증 | contact/rare-failure subgroup false-safe calibration과 predicted-real gain 기반 update abstention | `RETAIN / SECONDARY` |
| M-5 / I-05·I-10 | WholeBodyVLA·Humanoid Pixel-to-Action·HAIC가 loco-manipulation을, KDMR·Rhythm이 dynamics/contact-aware retargeting을 직접 다룸 | transition-conditioned objective/risk allocation, cross-morphology feasibility–coverage–hardware-safety calibration | `DEFER / P2`; broad method claim 금지 |
| M-6 / I-08·I-11 | large-scale co-training study와 human-to-robot transfer가 modality/diversity 효과를 직접 비교 | joint coverage allocation과 worst-group scaling; morphology adapter는 bottleneck 확인 후에만 | I-08 `RETAIN`, I-11 `CONDITIONAL BACKLOG` |

이 표의 최신 근거는 [RESEARCH_GAPS.md의 source/status audit](./RESEARCH_GAPS.md#evidence-audit-ledger)을 따른다. `SOURCE-VERIFIED` paper는 broad gap을 축소하는 근거로만 사용하며, method card의 `READING-SUPPORTED`를 자동 승격하지 않는다.

## 프로젝트 승격 기준

아이디어를 `SCOPED` 프로젝트로 올리려면 다음 조건을 만족해야 한다.

1. 최소 두 개의 강한 paper baseline과 비교 가능하다.
2. 가져올 기존 method component와 새 contribution이 분리되어 있다.
3. perception/representation metric이 아니라 robot success, recovery, contact, safety 또는 control 품질로 판정한다.
4. 첫 실험은 새 foundation model이나 대형 dataset 학습 없이 수행할 수 있다.
5. 성공뿐 아니라 latency, intervention cost, contact violation, failure severity 중 관련 지표를 함께 측정한다.
6. negative result가 나와도 어느 가정이 틀렸는지 알 수 있는 ablation이 있다.
7. 가설이 연결된 gap의 `R-M-C-O-T-S`를 벗어나지 않고, 넓혀야 하면 별도 후속 가설로 둔다.

실험 전에 primary outcome, equivalence/safety margin, subgroup, seed/trial 수를 사전 등록한다. `SUPPORTED`는 주 outcome의 개선과 safety non-degradation이 함께 확인될 때만 쓴다. 특정 subgroup에서만 성립하면 `REVISED`, oracle/upper-bound 조건에서도 주 비교군을 이기지 못하면 `REJECTED`다.

## Research program map

| Program | Macro-gap | Decision experiments | 선행 관계 |
|---|---|---|---|
| RP-1 Contact feedback transfer | M-1 | I-01 | G-01의 dual-rate transfer와 G-05의 contact-state calibration을 하나의 controller audit에서 검사 |
| RP-2 Failure-to-recovery loop | M-2 | I-12 → I-02 → I-06 optional | 공통 event/clone protocol과 option-outcome table을 만든 뒤 counterfactual recovery arbitration을 검증하고, 지지될 때만 policy reuse로 확장 |
| RP-3 Task-effective state | M-3 | I-07 → I-09; I-03 parallel | representation의 순수 control value와 추가 관측을 먼저 연결하고, memory는 공통 state instrumentation으로 독립 검사 |
| RP-4 Model-based decision | M-4 | I-04A → I-04B | world-model ranking calibration을 먼저 검증한 뒤 policy update로 진행 |
| RP-5 Embodied deployment | M-5 | I-10; I-05 parallel, then integration | cross-morphology feasibility calibration과 transition-conditioned risk interface를 각각 검증한 뒤 결합 |
| RP-6 Data and evidence | M-6 | I-08 → I-11 conditional | joint coverage audit 후 morphology가 실제 worst-group bottleneck일 때만 adapter로 확장 |

## Decision experiment portfolio

`E1/E2`는 gap의 중요도가 아니라 첫 decision experiment의 dependency다. `INFRA`는 method claim이 아닌 공통 평가 도구다.

| Idea | Program | Execution | Primary gap | 핵심 연구 단위 | 첫 검증 환경 |
|---|---|---|---|---|---|
| I-01 | RP-1 | E1 | G-01; G-05 secondary | slow–fast contact control의 sensor/embodiment transfer | contact-rich real robot 또는 high-fidelity setup |
| I-02 | RP-2 | E1 | G-02; G-10 evaluation dependency | same-onset counterfactual option value → matched-budget recovery arbitration | LIBERO perturbation/clone wrapper, CALVIN transfer |
| I-03 | RP-3 | E1 | G-04 | phase-aware memory update와 confidence-based expiry | RoboCasa/RLBench dynamic scene |
| I-04 | RP-4 | E1→E2 | G-07 → G-08 | contact-calibrated ranking 후 policy update | existing rollout dataset + 소규모 real validation |
| I-05 | RP-5 | E2 | G-09 | whole-body controller에 task risk budget 전달 | HumanoidBench |
| I-06 | RP-2 | E2 | G-06; G-02 data dependency | selected correction이 아니라 matched alternative option outcome을 이용한 conservative reuse | I-02 cloned-onset option table |
| I-07 | RP-3 | E1 | G-03 | compute-matched 2D/3D control utility | RLBench/FlowBot-style articulation |
| I-08 | RP-6 | E1 | G-12 | condition coverage를 최적화하는 data subset | DROID/OXE-style metadata |
| I-09 | RP-3 | E2 | G-13; G-03 control | action value에 따른 active-perception stopping | occluded grasp/articulation |
| I-10 | RP-5 | E1 | G-11 | cross-morphology feasibility–coverage–safety calibration | 3개 simulated morphology, leave-one-morphology-out |
| I-11 | RP-6 | E2 | G-12 | morphology graph 기반 cross-embodiment value adapter | 2개 이상 embodiment |
| I-12 | RP-2 | INFRA | G-10; G-02 support | benchmark-independent recovery event·clone·budget protocol | LIBERO first, second-suite adapter after validity gate |

## Hypothesis cards I-01–I-06

### I-01. Transfer-calibrated dual-rate contact executor

- **Program / execution:** RP-1 / E1.
- **Gap:** [G-01](./RESEARCH_GAPS.md#g-01-vla와-접촉-제어의-시간-척도-불일치), [G-05](./RESEARCH_GAPS.md#g-05-contact-state의-불완전한-observability와-sensor-종속성)
- **`R-M-C-O-T-S`:** multi-sensor manipulator / uncertainty-calibrated slow–fast fusion·authority scheduling / vision-only·early fusion·gated dual stream / success·peak force·reaction latency·calibration / contact event, delay·dropout sweep / peg insertion·wiping on real or high-fidelity contact setup.
- **방법론 근거:** AT-VLA의 Adaptive Tactile Injection·slow/fast stream, ForceVLA2의 hybrid force–position action, TACTIC의 learned contact dynamics+analytic contact Jacobian MPC, Tabero의 process-aware force metrics, TactAlign의 unpaired tactile alignment를 사용한다. UniForce는 heterogeneous sensor shared-force latent가 이미 탐색 중임을 보여주는 `PREPRINT-ONLY` counter-evidence다.
- **선행 연구가 해결한 것:** gated multimodal injection, fast tactile/force pathway, contact-centric predictive control, cross-sensor/shared tactile representation은 이미 직접 다뤄졌다. 따라서 slow–fast architecture나 shared latent 자체를 contribution으로 주장하지 않는다.
- **새 연구 단위:** sensor가 바뀌거나 stiffness·latency·calibration이 달라질 때 fast stream의 confidence를 추정하고, confidence가 낮으면 residual authority를 줄이거나 safe position control로 전환한다.
- **가설:** gated slow–fast controller에 sensor-calibrated uncertainty와 authority scheduling을 추가하면, 단순 slow–fast 구조보다 unseen sensor/delay에서 peak force를 늘리지 않고 성공률을 유지한다.
- **최소 실험:** peg insertion과 wiping에서 vision-only, naïve force concatenation, AT-VLA식 gated dual stream, uncertainty-gated dual stream을 비교한다. 같은 demonstration과 backbone을 사용하고 sensor delay, dropout, stiffness 또는 sensor model을 독립적으로 바꾼다.
- **판정 지표:** success, peak/impulse force, reaction latency, force tracking error, unsafe residual activation, calibration error.
- **Reject criterion:** uncertainty gate가 unseen condition에서 naïve gated dual stream보다 safety–success Pareto frontier를 개선하지 못하면 별도 architecture 연구를 중단하고 calibration/data augmentation 문제로 축소한다.
- **Paper basis:** [AT-VLA](../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md), [ForceVLA2](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md), [Tabero](../2026/ICML/2026_ICML_Tabero-Learning-Gentle-Manipulation-with-Closed-Loop-Force/01_overview.md), [TactAlign](../2026/RSS/2026_RSS_TactAlign-Human-to-Robot-Policy-Transfer-via-Tactile-Align/01_overview.md), [Tactile-Driven Non-Prehensile Manipulation](../2024/RSS/2024_RSS_Tactile-Driven-Non-Prehensile-Object-Manipulation-via-Extr/01_overview.md), [Reactive Diffusion Policy](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md), [TACTIC](https://roboticsconference.org/program/papers/60/), [UniForce](https://arxiv.org/abs/2602.01153) `PREPRINT`.

<a id="i-02-risk-budgeted-typed-recovery-for-vla"></a>

### I-02. Same-onset counterfactual recovery arbitration for VLA

- **Program / execution:** RP-2 / E1; [project spec](./projects/RP-2_FAILURE_RECOVERY.md)의 I-12 event protocol을 먼저 사용한다.
- **Gap:** [G-02](./RESEARCH_GAPS.md#g-02-detection에서-recovery까지-닫히지-않은-loop), [G-10](./RESEARCH_GAPS.md#g-10-long-horizon-평가의-낮은-failure-resolution)
- **`R-M-C-O-T-S`:** VLA manipulator / option-conditioned value와 risk-constrained budgeted selector / abort·retry·reobserve·state reset·subgoal rewind·task replan·human escalation / final completion·irreversible failure·intervention cost·regret-to-oracle / cloned failure onset에서 post-recovery까지 / LIBERO perturbation wrapper와 CALVIN transfer.
- **방법론 근거:** POMDP의 belief-state와 finite-memory decision formulation, SAFE의 calibrated failure score, Recovery RL의 task/recovery policy 분리와 safety critic, PDDLStream의 symbolic–continuous replanning interface를 사용한다. FLARE의 Retry/Reset, ViFailback의 diagnosis/correction, AgentChord의 recovery-augmented task graph, UPS의 calibrated act/ask/intervene를 strong baseline으로 둔다. SPR의 rewind, FAR의 retry/adaptation, CoRe의 imagined realignment, VLCP의 code replan은 `PREPRINT-ONLY` novelty-collision set으로 비교한다.
- **범위 경계:** RP-2는 torque/force law를 새로 학습하는 실로봇 저수준 제어 연구가 아니라, frozen VLA와 fixed skill/controller 위의 high-level runtime recovery supervisor다. LIBERO/CALVIN에서 C1/C2를 먼저 검증하고, hardware latency·contact force·emergency stop은 별도 `C3` real-robot phase에서만 주장한다.
- **선행 연구가 해결한 것:** detection, Retry/Reset, visual correction, rollback/rewind, precompiled recovery branch, act/ask/intervene, retry adaptation은 각각 이미 다뤄졌다. 따라서 새 failure type을 정의하거나 기존 option 하나를 추가하는 것은 새 연구 단위가 아니다.
- **새 연구 단위:** 동일한 cloned post-failure state에서 고정된 option library를 모두 실행해 `Q(o | belief, cause, recoverability, budget)`와 risk/cost를 관찰한다. 서로 다른 abstraction level의 option이 만드는 outcome crossing을 학습하고, 동일 정보·horizon·budget에서 하나를 선택한다. detector, option-value estimator, selector, skill-library 오류는 oracle decomposition으로 분리한다.
- **가설:** scalar alert가 비슷한 failure 사이에서도 optimal option이 달라지고 remaining budget에 따라 option ranking이 교차한다. 이 crossing을 학습한 risk-constrained selector는 strongest non-privileged baseline보다 IFR을 악화시키지 않으면서 BRCR을 높이고 regret-to-oracle을 줄인다.
- **최소 실험:** LIBERO-Long 4개 task에 observation, execution/contact, world-state, plan-semantic perturbation을 event landmark에서 삽입한다. fit/calibration/test task를 분리한 frozen-base rollout의 각 cloned onset에서 abort, blind retry, reobserve, state reset, subgoal rewind, privileged task replan을 모두 실행해 option-outcome table을 만든다. scalar trigger, FLARE-style Retry/Reset, type-only heuristic, uniform-feasible selector, learned option-value selector를 600-step native horizon과 동일한 vector recovery budget에서 비교한다. 이후 selector를 재학습하지 않고 CALVIN 또는 held-out failure family로 transfer한다.
- **판정 지표:** primary는 `Budgeted Recovery Completion Rate (BRCR)`, safety gate는 `Irreversible Failure Rate (IFR)`다. secondary로 event-level detection delay/AUPRC, cause·recoverability macro-F1, per-option Brier/ECE, O3 대비 option regret, false intervention, recovery cost, p95 selector latency, task/cause/onset worst-group BRCR·IFR를 paired cluster-bootstrap CI와 함께 보고한다.
- **Reject criterion:** 먼저 crossing prevalence가 사전 기준보다 낮거나 best fixed option의 regret가 learned selector와 동률이면 arbitration claim을 기각한다. crossing이 존재해도 strongest non-privileged baseline보다 BRCR이 5 pp 이상 개선되지 않거나 IFR upper CI가 baseline+1 pp를 초과하면 method claim을 기각한다. oracle option outcome에서도 이득이 없으면 selector가 아니라 skill-library/interface expressivity 문제로 판정한다.
- **Paper basis:** [POMDP](../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md), [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md), [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md), [PDDLStream](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md), [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md), [FLARE](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md), [VLA-FixBench/FaultEval](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md), [TD calibration](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md). **External source-verified baselines:** [ViFailback](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.html), [AgentChord](https://roboticsconference.org/program/papers/180/), [When to Act, Ask, or Learn](https://roboticsconference.org/program/papers/142/); preprint collision set은 [gap audit](./RESEARCH_GAPS.md#2026-preprint-only-novelty-collision-check)을 따른다.

## RP-2 I-02 priority reading spine

이 목록은 전체 CORE/NEXT tier가 아니라 **RP-2를 실제로 설계·구현하기 위한 dependency 순서**다. P0–P2는 첫 decision experiment의 필수 spine이고, P3는 frozen policy adapter를 고정하기 위한 implementation branch, P4는 transfer와 후속 확장이다. 15편 hard cap은 두지 않는다. 각 paper를 읽은 뒤에는 단순 요약 대신 아래 exit artifact를 남긴다.

| Phase | 읽기 목적 | Exit artifact | 구현 의존성 |
|---|---|---|---|
| `P0` | partial observation, recovery, safety, planning의 문제 formulation 고정 | belief/state/action/budget 정의와 failure-state causal map | method 설계 전 필수 |
| `P1` | detector·diagnosis와 recovery abstraction별 실제 한계 확인 | detector/selector audit, option-family map, novelty-collision matrix | Phase 0 wrapper 전에 필수 |
| `P2` | benchmark·termination·event metric의 의미 고정 | benchmark adapter와 `rp2.event.v2` mapping 표 | Phase 1 전에 필수 |
| `P3` | frozen VLA와 offline/value branch 선택 | base checkpoint, action interface, inference budget 결정 | pilot 구현 branch |
| `P4` | long-horizon·world-model·memory·data extension 판단 | transfer/revise/defer 결정 memo | pilot 결과 후 읽기 |

### P0 — Concept prerequisites (10)

1. [Planning and Acting in Partially Observable Stochastic Domains](../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md) — belief state, partial observability, finite-memory decision.
2. [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) — learner-induced failure states와 covariate shift.
3. [Proximal Policy Optimization Algorithms](../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) — policy optimization과 trust-region 직관.
4. [Trust Region Policy Optimization](../2015/ICML/2015_ICML_Trust-Region-Policy-Optimization/01_overview.md) — constrained/stable policy update.
5. [Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) — task/recovery policy 분리와 safety critic.
6. [Failure Prediction with Statistical Guarantees for Vision-Based Robot Control](../2022/RSS/2022_RSS_Failure-Prediction-with-Statistical-Guarantees-for-Vision/01_overview.md) — runtime monitoring과 failure prediction.
7. [Control Barrier Function Based Quadratic Programs for Safety Critical Systems](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) — safe set, constraint violation, irreversible event.
8. [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](../2023/CoRL/2023_CoRL_Robots-That-Ask-For-Help-Uncertainty-Alignment-for-Large-L/01_overview.md) — uncertainty-aligned escalation.
9. [PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) — symbolic–continuous replanning interface.
10. [Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning](../2020/CoRL/2020_CoRL_Relay-Policy-Learning-Solving-Long-Horizon-Tasks-via-Imita/01_overview.md) — long-horizon skill decomposition과 relaying.

### P1 — Direct detector and recovery baselines (8)

1. [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) — failure-data-free uncertainty detector.
2. [SAFE: Multitask Failure Detection for Vision-Language-Action Models](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) — frozen VLA latent score와 conformal alert threshold.
3. [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) — binary Retry/Reset dispatcher.
4. [Can VLMs Diagnose and Recover from VLA Manipulation Faults?](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) — fault taxonomy, diagnosis, rollback recovery.
5. [Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) — sequential success-confidence calibration.
6. [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](../2025/ICLR/2025_ICLR_AHA-A-Vision-Language-Model-for-Detecting-and-Reasoning-Ov/01_overview.md) — VLM failure detection/reasoning alternative.
7. [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](../2026/CVPR/2026_CVPR_Counterfactual-VLA-Self-Reflective-Vision-Language-Action/01_overview.md) — self-reflection과 test-time recovery comparison.
8. [SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](../2025/NeurIPS/2025_NeurIPS_SafeVLA-Towards-Safety-Alignment-of-Vision-Language-Action/01_overview.md) — constrained VLA safety alignment.

#### P1.5 — 2026 option-family collision check

아래 자료는 현재 registry 정독 상태와 별개인 source-verified frontier check다. 각 논문을 “recovery system”으로 한데 묶지 말고, 어떤 option abstraction과 정보·budget·oracle을 쓰는지 표로 비교한다.

1. [ViFailback](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.html) — diagnosis와 visual/text correction; real failure data.
2. [AgentChord](https://roboticsconference.org/program/papers/180/) — precompiled recovery branch와 low-latency orchestration.
3. [When to Act, Ask, or Learn](https://roboticsconference.org/program/papers/142/) — calibrated act/clarify/intervene selection; 가장 강한 selector counter-baseline.
4. [See, Plan, Rewind](https://arxiv.org/abs/2603.09292) `PREPRINT` — progress-aware subgoal rewind.
5. [FAR](https://arxiv.org/abs/2607.01111) `PREPRINT` — retry perturbation과 failure-preference adaptation.
6. [Imagining Recovery / CoRe](https://arxiv.org/abs/2608.14822) `PREPRINT` — imagined continuation과 state realignment.
7. [VLCP](https://arxiv.org/abs/2608.16978) `PREPRINT` — control-code abstraction에서 closed-loop replanning.

이 collision check의 exit artifact는 `paper → detection signal → intervention abstraction → option set → budget → outcome → unavailable counterfactual` matrix다. 어떤 한 방법이 이미 same-onset matched-option comparison을 제공하면 I-02의 novelty claim을 다시 축소한다.

### P2 — Benchmark and metric semantics (8)

1. [Benchmarking Knowledge Transfer for Lifelong Robot Learning](../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md) — LIBERO fixed states와 goal predicates.
2. [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](../2022/RA-L/2022_RA-L_CALVIN-A-Benchmark-for-Language-Conditioned-Policy-Learnin/01_overview.md) — language-conditioned long-horizon sequence.
3. [AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md) — termination semantics와 post-failure continuation.
4. [FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation](../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md) — phase/skill progress beyond final success.
5. [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](../2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/01_overview.md) — physical/semantic safety perturbation.
6. [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md) — safety, distractor, extrapolation, long-horizon stress axes.
7. [BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation](../2022/CoRL/2022_CoRL_BEHAVIOR-1K-A-Benchmark-for-Embodied-AI-with-1000-Everyday/01_overview.md) — embodied long-horizon evaluation context.
8. [RLBench: The Robot Learning Benchmark & Learning Environment](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) — task suite와 simulator design 비교.

#### P2.5 — Recovery-aware evaluation collision check

- [SO-101 Failure and Recovery Analysis](https://arxiv.org/abs/2606.08881) `PREPRINT` — low-cost real-robot failure taxonomy와 recovery-aware metric.
- [Beyond Binary Success](https://roboticsconference.org/program/papers/76/) — fine-grained progress metric의 sample-efficient sequential comparison.
- [Discounted Liveness OPE](https://roboticsconference.org/program/papers/154/) — recovery 때문에 non-monotonic한 task progress와 finite-horizon truncation.

이 자료들 때문에 I-12는 “binary success를 넘는 metric이 없다”고 주장하지 않는다. contribution은 cloned onset ID, matched option budget, irreversibility, post-recovery outcome을 suite 간 동일 schema로 정렬하는 데 한정한다.

### P3 — Frozen VLA and implementation branch (11)

1. [OpenVLA: An Open-Source Vision-Language-Action Model](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) — 첫 pilot의 frozen base 후보.
2. [Octo: An Open-Source Generalist Robot Policy](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md) — generalist policy/action conditioning 대안.
3. [RT-1: Robotics Transformer for Real-World Control at Scale](../2022/arxiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md) — robot policy/action-token lineage.
4. [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](../2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md) — language-to-action VLA lineage.
5. [π0: A Vision-Language-Action Flow Model for General Robot Control](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) — flow-based VLA alternative.
6. [π0.5: a Vision-Language-Action Model with Open-World Generalization](../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md) — open-world VLA extension.
7. [Decision Transformer: Reinforcement Learning via Sequence Modeling](../2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/01_overview.md) — trajectory-conditioned sequence modeling.
8. [Offline Reinforcement Learning with Implicit Q-Learning](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md) — selector value-learning branch.
9. [Conservative Q-Learning for Offline Reinforcement Learning](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md) — conservative offline recovery/value baseline.
10. [Implicit Behavioral Cloning](../2022/CoRL/2022_CoRL_Implicit-Behavioral-Cloning/01_overview.md) — multimodal behavior-cloning alternative.
11. [Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions](../2024/CoRL/2024_CoRL_Q-Transformer-Scalable-Offline-Reinforcement-Learning-via/01_overview.md) — autoregressive action-value extension.

### P4 — Optional extensions and transfer checks (11)

1. [Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation](../2025/CoRL/2025_CoRL_Long-VLA-Unleashing-Long-Horizon-Capability-of-Vision-Lang/01_overview.md) — long-horizon VLA context.
2. [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](../2026/CVPR/2026_CVPR_PALM-Progress-Aware-Policy-Learning-via-Affordance-Reasoni/01_overview.md) — progress-aware state.
3. [Learning to Be Uncertain: Pre-training World Models with Horizon-Calibrated Uncertainty](../2026/ICLR/2026_ICLR_Learning-to-Be-Uncertain-Pre-training-World-Models-with-Ho/01_overview.md) — horizon-calibrated uncertainty.
4. [WorldGym: World Model as An Environment for Policy Evaluation](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md) — world-model policy evaluation.
5. [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) — imagined policy improvement/calibration.
6. [Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) — memory/retrieval effects.
7. [Inner Monologue: Embodied Reasoning through Planning with Language Models](../2022/CoRL/2022_CoRL_Inner-Monologue-Embodied-Reasoning-through-Planning-with-L/01_overview.md) — language-mediated replanning and feedback.
8. [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) — scene-graph task planning.
9. [MimicPlay: Long-Horizon Imitation Learning by Watching Human Play](../2023/CoRL/2023_CoRL_MimicPlay-Long-Horizon-Imitation-Learning-by-Watching-Huma/01_overview.md) — long-horizon imitation/play data.
10. [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../2023/CoRL/2023_CoRL_MimicGen-A-Data-Generation-System-for-Scalable-Robot-Learn/01_overview.md) — recovery-data augmentation.
11. [Data Scaling Laws in Imitation Learning for Robotic Manipulation](../2025/ICLR/2025_ICLR_Data-Scaling-Laws-in-Imitation-Learning-for-Robotic-Manipu/01_overview.md) — data coverage and failure-data curation.

P0–P2를 읽고 pilot을 수행한 뒤에도 `same alert score → different optimal recovery`, `remaining budget에 따른 option crossing`, `best fixed option 대비 selector regret 감소`를 관찰하지 못하면 I-02의 counterfactual arbitration formulation을 유지하지 않는다. 그 경우 scalar risk-triggered recovery 또는 event/option-outcome protocol contribution으로 범위를 축소한다.

### RP-2 novelty audit

[Motivation ≠ Novelty](https://gisbi-kim.github.io/motivation-is-not-novelty/)의 기준으로 보면, “VLA가 실패한다”, “여러 recovery가 필요하다”, “그래서 selector를 추가한다”는 아직 motivation이다. I-02가 연구 아이디어로 남으려면 다음 한 문장으로 설명할 수 있어야 한다.

> 동일 post-failure state에서 recovery option의 success·risk·cost가 cause와 remaining budget에 따라 교차하므로, scalar alert나 fixed dispatcher로는 best option을 식별할 수 없다. cloned-state counterfactual outcome으로 학습한 risk-constrained selector는 matched-budget baseline보다 regret-to-oracle을 줄여야 한다.

이 문장이 실제 failure table·수식·ablation으로 지지되지 않으면 module 조합의 novelty를 주장하지 않는다. 최소 검증은 (1) naive baseline의 원인별 failure census, (2) same alert/different optimal option, (3) budget 감소에 따른 policy crossing, (4) scalar/type-only/heuristic selector와의 matched comparison, (5) hold-out failure family 또는 CALVIN transfer다. 이 조건을 통과하기 전까지 I-02의 상태는 `CONDITIONALLY_FIT`이다.

### I-03. Phase-aware spatial memory with learned expiry

- **Program / execution:** RP-3 / E1; [project spec](./projects/RP-3_MEMORY_EXPIRY.md). I-07의 state comparison protocol을 가능하면 재사용한다.
- **Gap:** [G-04](./RESEARCH_GAPS.md#g-04-persistent-spatial-memory의-staleness와-uncertainty)
- **`R-M-C-O-T-S`:** mobile/manipulation VLA / phase·confidence·expiry memory / no memory·persistent memory·similarity refinement / stale read·unsafe action·success·rescan / multi-step state transition / RoboCasa·RLBench relocation·removal·delay.
- **방법론 근거:** MomaGraph의 observed state-transition graph update, SOMA의 dynamic refinement/retrieval, Memory Retrieval/HALO의 task-relevant sparse retrieval, AFI의 proprioceptive memory-trap detection과 high-affordance rollback을 사용한다.
- **선행 연구가 해결한 것:** out-of-view memory, sparse retrieval, accumulated drift 완화, memory-trap detection과 rollback은 가능하다. 따라서 “persistent memory가 stale해진다”는 관찰이나 rollback 자체는 contribution이 아니다.
- **새 연구 단위:** memory token에 phase-transition probability, geometric confidence, age를 붙이고 `retain / refresh / expire / actively verify`를 선택한다.
- **가설:** similarity-only update보다 phase-aware confidence와 expiry를 쓰면 relocation·object removal에서 stale-memory-induced action을 줄이면서 불필요한 re-scan 증가를 제한한다.
- **최소 실험:** RoboCasa 또는 RLBench에서 object relocation, disappearance, drawer state change, delayed observation을 통제한다. no-memory, SOMA-style refinement, phase+expiry memory를 같은 policy에 연결한다.
- **판정 지표:** stale read rate, phase-state accuracy, expiry Brier/ECE, selective unsafe-action risk, task success, unsafe grasp/placement, re-scan count, latency.
- **Reject criterion:** oracle phase label에서도 expiry가 persistent memory보다 이득이 없으면 memory update가 아니라 downstream policy의 memory usage가 병목이라고 판정한다.
- **Paper basis:** [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md), [Spatial Memory for Out-of-Vision Manipulation](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md), [Memory Retrieval/HALO](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md), [ConceptFusion](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md), [Affordance Field Intervention](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Affordance_Field_Intervention_Enabling_VLAs_to_Escape_Memory_Traps_in_CVPR_2026_paper.html).

### I-04. Contact-calibrated world model for policy ranking and improvement

- **Program / execution:** RP-4 / I-04A E1 ranking audit → I-04B E2 policy update.
- **Gap:** [G-07](./RESEARCH_GAPS.md#g-07-world-model의-visual-fidelity와-control-fidelity-불일치), [G-08](./RESEARCH_GAPS.md#g-08-imagined-policy-improvement의-보수성과-calibration)
- **`R-M-C-O-T-S`:** VLA checkpoints·candidate chunks / contact-event-calibrated world-model OPE·conservative update / visual-only ranking·no update·offline DPO / subgroup rank·false-safe·predicted-real gain / rollout horizon·update-size sweep / paired ID·OOD·contact rollouts and small real validation.
- **방법론 근거:** WorldGym의 action-conditioned evaluation, PolaRiS의 paired real-to-sim ranking, Interactive World Simulator의 long-horizon interactive surrogate, MOPO의 uncertainty penalty, WMPO·RISE의 imagined update, Visual Verification의 verified-rollout improvement를 사용한다.
- **선행 연구가 해결한 것:** 평균 real-world success와 policy ranking 보존, world-model/verified data에 의한 policy improvement는 여러 method family에서 입증됐다. 따라서 world model을 evaluator나 trainer로 쓰는 것 자체는 contribution이 아니다.
- **새 연구 단위:** pixel/reward uncertainty와 별도로 contact transition, jamming, slip, constraint violation의 event probability를 예측하고 이 uncertainty로 ranking과 policy update를 보수화한다.
- **가설 A — ranking:** contact-event head와 subgroup calibration을 추가하면 visual-only WorldGym보다 contact-rich/OOD condition의 false-safe ranking을 낮춘다.
- **가설 B — update:** A의 calibration이 성립한 subgroup에서만 update하고 나머지는 abstain하면, always-update WMPO/RISE-style procedure보다 false improvement와 predicted-real gain error를 낮춘다.
- **최소 실험:** 먼저 여러 policy checkpoint의 action chunk를 동일 initial state에서 평가해 world-model/real pairwise ranking을 visual OOD, free-space, contact-rich subgroup으로 나눈다. A가 성립한 뒤에만 작은 trust-region update를 high-fidelity environment와 소규모 real trial에서 검증한다.
- **판정 지표:** subgroup rank correlation, event calibration, false-safe/selective risk, update coverage, predicted gain–real gain error, false improvement, unsafe proposal rate.
- **Reject criterion:** oracle contact label을 학습해도 ranking 또는 real-gain calibration이 개선되지 않으면 별도 contact model이 아니라 dynamics horizon/representation 문제로 축소한다.
- **Paper basis:** [WorldGym](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md), [MOPO](../2020/NeurIPS/2020_NeurIPS_MOPO-Model-based-Offline-Policy-Optimization/01_overview.md), [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md), [Unified World Models](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md), [PolaRiS](https://roboticsconference.org/program/papers/62/), [Interactive World Simulator](https://roboticsconference.org/program/papers/18/), [RISE](https://roboticsconference.org/program/papers/12/), [Visual Verification](https://roboticsconference.org/program/papers/79/).

### I-05. Risk-budget interface for whole-body loco-manipulation

- **Program / execution:** RP-5 / E2; I-10의 feasible prior가 없어도 G-09 interface를 독립 검사할 수 있어야 한다.
- **Gap:** [G-09](./RESEARCH_GAPS.md#g-09-locomotion과-manipulation의-bandwidthobjective-충돌)
- **`R-M-C-O-T-S`:** mobile manipulator/humanoid / transition-conditioned risk/objective budget to whole-body controller / decoupled·monolithic·fixed hierarchy / stage completion·fall·support margin·torque·latency·recovery / locomotion·pre-contact·contact·post-contact phases / HumanoidBench door·carry with payload·push.
- **방법론 근거:** Whole-Body NMPC의 contact/timing optimization, WholeBodyVLA의 unified latent+locomotion-oriented controller, Humanoid Pixel-to-Action의 staged reset·closed-loop sim-to-real, HAIC의 dynamics-aware world model을 strong baselines로 사용한다.
- **선행 연구가 해결한 것:** end-to-end vision-based humanoid loco-manipulation과 manipulation-aware locomotion은 이미 구현됐다. 따라서 hierarchy를 결합하거나 pixel-to-action policy를 만드는 것 자체는 contribution이 아니다.
- **새 연구 단위:** locomotion→contact transition을 online 검출하고 phase마다 support margin, allowed base motion, peak torque/contact, perception/control latency, recovery reserve의 priority를 바꾸는 risk/objective budget을 전달한다.
- **가설:** fixed-weight monolithic policy나 decoupled skill보다 risk-budget hierarchy가 disturbance와 payload 변화에서 fall을 줄이면서 manipulation progress를 유지한다.
- **최소 실험:** HumanoidBench door/carry/reach 계열에서 decoupled, monolithic, fixed hierarchy, transition-conditioned risk-budget hierarchy를 비교하고 phase별 payload·external push·observation latency를 sweep한다.
- **판정 지표:** stage completion, fall, support-margin violation, peak torque, recovery time, end-effector error, energy.
- **Reject criterion:** oracle risk budget에서도 fixed hierarchy 대비 Pareto 개선이 없으면 high-level budget interface가 아니라 low-level controller capacity가 병목이다.
- **Paper basis:** [Whole-Body NMPC](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md), [HumanoidBench](../2024/RSS/2024_RSS_HumanoidBench-Simulated-Humanoid-Benchmark-for-Whole-Body/01_overview.md), [OmniH2O](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md), [Mobile ALOHA](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md), [WholeBodyVLA](https://openreview.net/pdf/3067651d96704608727027ec28fda2eb8c2a7c4a.pdf), [Humanoid Pixel-to-Action](https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html), [HAIC](https://roboticsconference.org/program/papers/13/).

### I-06. Conservative policy reuse from counterfactual recovery outcomes

- **Program / execution:** RP-2 / E2; I-12와 I-02에서 same-onset option table과 selector crossing이 먼저 확인된 뒤에만 진행한다.
- **Gap:** [G-06](./RESEARCH_GAPS.md#g-06-failure와-suboptimal-data의-안전한-재사용), with G-02 data dependency.
- **`R-M-C-O-T-S`:** frozen-base manipulation/VLA recovery data / counterfactual option-value weighting·conservative policy update / success-only·chosen-correction-only·naïve recovery mix·IQL·CQL / post-update BRCR·IFR·harmful update·option-value calibration / onset-to-post-recovery segment / I-02 LIBERO cloned-state table with held-out failure family.
- **방법론 근거:** CQL의 conservative Q regularization, IQL의 in-sample value/advantage weighting, Visual Verification의 verified-rollout post-training, FAR의 recovered trajectory reuse를 사용한다. ViFailback·FailSafe·RoboFAC의 failure–correction pair는 strong data baseline이지만, unavailable alternative outcome이 없는 chosen-correction-only 조건으로 취급한다.
- **선행 연구가 해결한 것:** failure/correction data와 verified/recovered rollout을 policy improvement에 재사용하는 broad 방향은 이미 제시됐다. 따라서 failure type label을 더해 unsuccessful data를 섞는 것만으로는 새 연구 단위가 아니다.
- **새 연구 단위:** 동일 onset에서 실행한 여러 recovery option의 success·risk·cost를 이용해 chosen action뿐 아니라 rejected alternative의 상대가치를 추정한다. `recoverable prefix / harmful action / irreversible terminal` semantics는 독립 novelty가 아니라 counterfactual target을 stratify하는 변수로만 쓴다.
- **가설:** matched option-outcome weighting을 적용한 conservative update가 chosen-correction-only와 naïve recovered-rollout mix보다 IFR을 악화시키지 않으면서 post-update BRCR과 worst-failure-family 성능을 높인다.
- **최소 실험:** I-02 option table을 train/calibration/held-out failure family로 나눈다. no update, success-only, chosen-correction-only, naïve recovery mix, IQL/CQL, counterfactual option weighting을 동일 update/data budget에서 비교한다.
- **판정 지표:** post-update BRCR/IFR, harmful update rate, per-option Brier/ECE, option regret, worst-failure-family performance, update compute/data cost.
- **Reject criterion:** oracle option outcome을 제공해도 chosen-correction-only IQL/CQL보다 이득이 없으면 G-06을 별도 learning contribution으로 유지하지 않고 I-02 evaluator/data artifact로만 남긴다.
- **Paper basis:** [CQL](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md), [IQL](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md), [DROID](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md), [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md), [Visual Verification](https://roboticsconference.org/program/papers/79/), [FAR](https://arxiv.org/abs/2607.01111) `PREPRINT`.

## Hypothesis cards I-07–I-11

### I-07. Compute-matched task-conditioned 3D control bottleneck

- **Program / execution:** RP-3 / E1.
- **Gap:** [G-03](./RESEARCH_GAPS.md#g-03-3d-perception-향상과-control-향상의-compute-matched-인과성)
- **`R-M-C-O-T-S`:** vision-based manipulator / RGB·dense 3D·task-conditioned state / matched backbone·data·view·runtime / success·collision·contact error·latency / per-action inference / articulation·occluded grasp with pose·calibration perturbation.
- **방법론 근거:** FlowBot3D의 task-specific 3D flow, ActiveVLA의 critical-region/view/zoom ablation, SaPaVe의 decoupled camera/manipulation action, CLAMP의 action-conditioned 3D pretraining을 비교 대상으로 사용한다.
- **선행 연구가 해결한 것:** 3D flow·pretraining·active view가 articulation과 precise manipulation에 유용하다는 증거는 충분해졌다. 따라서 “3D가 control에 유용하다”는 것을 다시 보이는 것은 contribution이 아니다.
- **새 연구 단위:** RGB, dense 3D, task-conditioned object/contact state가 같은 view·parameter·runtime budget에서 control에 주는 순수 이득을 비교한다.
- **가설:** dense point cloud 전체보다 task-conditioned pose, affordance/flow, contact surface, uncertainty bottleneck이 같은 compute에서 더 높은 control success를 낸다.
- **최소 실험:** articulation 또는 occluded grasp task에서 동일 policy head와 training data를 유지하고 representation만 바꾼다. latency-matched와 unconstrained 두 setting을 모두 보고한다.
- **판정 지표:** success, collision, contact error, latency, memory, representation perturbation sensitivity.
- **Reject criterion:** compute를 맞춘 뒤 task-conditioned bottleneck이 raw RGB 또는 dense 3D보다 이득이 없으면 별도 representation contribution을 주장하지 않는다.
- **Paper basis:** [FlowBot3D](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md), [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md), [SUGAR](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md), [SaPaVe](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html), [CLAMP](https://roboticsconference.org/program/papers/127/).

### I-08. Coverage-aware robot data subset scaling

- **Program / execution:** RP-6 / E1.
- **Gap:** [G-12](./RESEARCH_GAPS.md#g-12-data-scale와-data-coverage의-혼동)
- **`R-M-C-O-T-S`:** heterogeneous robot datasets / multi-axis coverage-aware subset / equal-budget random·scene-only balanced subset / average·worst-group·new-condition gain / training scale curve / DROID·OXE-style task×embodiment×sensor×operator×outcome metadata.
- **방법론 근거:** Data Scaling Laws의 diversity control과 power-law evaluation, DROID의 matched-size scene-diversity experiment, RSS 2026 Systematic Co-training Study의 modality/training-strategy comparison, Emergence of Human-to-Robot Transfer의 diversity threshold 분석을 사용한다.
- **선행 연구가 해결한 것:** environment/object diversity, co-training modality, human/cross-embodiment data의 효과는 대규모 비교로 직접 다뤄졌다. 따라서 scene balance나 modality 추가 자체는 contribution이 아니다.
- **새 연구 단위:** environment/object뿐 아니라 task, operator, embodiment, outcome condition을 coverage cell로 정의하고 같은 trajectory budget에서 subset allocation을 최적화한다.
- **가설:** random 또는 scene-only diversity보다 multi-axis worst-covered-cell sampling이 평균 성능을 크게 희생하지 않고 worst-group·new-condition 성능을 높인다.
- **최소 실험:** DROID/OXE-style metadata에서 random, scene-balanced, single-axis modality/embodiment-balanced, failure-aware, joint worst-covered-cell subset을 같은 크기로 구성해 동일 policy를 학습한다.
- **판정 지표:** average success, worst-group success, new-scene/task/embodiment performance, effective coverage, marginal gain per trajectory.
- **Reject criterion:** metadata cell을 oracle로 제공해도 random sampling과 차이가 없으면 coverage optimizer보다 representation/model capacity가 우선이다.
- **Paper basis:** [Data Scaling Laws](../2025/ICLR/2025_ICLR_Data-Scaling-Laws-in-Imitation-Learning-for-Robotic-Manipu/01_overview.md), [DROID](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md), [Open X-Embodiment](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md), [Systematic Co-training Study](https://roboticsconference.org/program/papers/7/), [Emergence of Human-to-Robot Transfer](https://roboticsconference.org/program/papers/72/).

### I-09. Action-value stopping policy for active perception

- **Program / execution:** RP-3 / E2; I-07의 compute-matched state baseline 이후 진행한다.
- **Gap:** [G-03](./RESEARCH_GAPS.md#g-03-3d-perception-향상과-control-향상의-compute-matched-인과성), [G-13](./RESEARCH_GAPS.md#g-13-active-perception의-비용-대비-control-value)
- **`R-M-C-O-T-S`:** active-camera manipulator / action-value·disagreement stopping / fixed view·fixed count·geometry entropy·SaPaVe-style camera policy / success gain per second·physical travel·collision·unnecessary view / pre-action·mid-task acquisition / occluded grasp·articulation with physical camera budget.
- **방법론 근거:** ActiveVLA의 active viewpoint/3D zoom, AVA-VLA의 recurrent attention, SaPaVe의 decoupled camera/manipulation decoder와 ActiveManip-Bench, Where2Act의 actionability score를 사용한다.
- **선행 연구가 해결한 것:** active viewpoint selection, camera action learning, benchmark, recurrent state는 이미 존재한다. 따라서 camera head나 active-view dataset을 추가하는 것은 새 연구 단위가 아니다.
- **새 연구 단위:** geometry uncertainty가 아니라 새 view가 action distribution 또는 predicted task value를 얼마나 바꿀지를 추정해 `observe / act`를 결정한다.
- **가설:** physical action-value stopping이 fixed count·geometry entropy·learned camera policy보다 적은 travel/latency/risk cost로 같은 success를 내거나 같은 budget에서 더 높은 success를 낸다.
- **최소 실험:** physical movable camera 또는 calibrated motion-cost setup의 occluded grasp/articulation에서 fixed-view, fixed-three-view, entropy, SaPaVe-style camera policy, action-disagreement/value-of-information을 비교한다.
- **판정 지표:** success, views, sensing latency, physical camera travel, camera-arm interference/collision, unnecessary-view rate, stopping calibration.
- **Reject criterion:** oracle future-view outcome으로도 adaptive stopping 이득이 작으면 해당 task에서는 active sensing보다 robust policy training이 더 적합하다.
- **Paper basis:** [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md), [AVA-VLA](../2026/CVPR/2026_CVPR_AVA-VLA-Improving-Vision-Language-Action-Models-with-Activ/01_overview.md), [Where2Act](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md), [FlowBot3D](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md), [SaPaVe](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html).

### I-10. Cross-morphology feasibility-calibrated humanoid retargeting

- **Program / execution:** RP-5 / E1.
- **Gap:** [G-11](./RESEARCH_GAPS.md#g-11-human-motion-prior와-contact-feasibility의-충돌)
- **`R-M-C-O-T-S`:** multiple humanoid morphologies / calibrated preserve·modify·reject decision over contact·dynamics-aware retargeting / kinematic-only·hard filter·per-morph dynamics optimizer / downstream success·fall·torque/contact violation·coverage·calibration / clip-to-long-horizon tracking / leave-one-morphology-out simulation with optional selected hardware validation.
- **방법론 근거:** DeepMimic·HumanPlus·OmniH2O의 motion-prior/tracking lineage와 KDMR의 multi-contact whole-body trajectory optimization, Rhythm의 interaction-aware retargeting을 strong baselines로 사용한다.
- **선행 연구가 해결한 것:** physics tracking, infeasible-motion filtering, dynamics/contact-constrained retargeting, real interaction-aware retargeting은 이미 다뤄졌다. 따라서 contact constraint를 retargeting에 넣는 것 자체는 contribution이 아니다.
- **새 연구 단위:** 동일 human motion을 두 개 이상 robot morphology에 옮길 때 predicted feasibility와 실제 tracking/task outcome을 calibration하고, motion을 preserve·modify·reject하는 threshold가 coverage–safety trade-off를 어떻게 바꾸는지 검증한다.
- **가설:** morphology-conditioned feasibility calibration이 kinematic·hard-filter·single-morph dynamics optimization보다 worst-morphology task success를 높이고 violation을 줄이면서 retained coverage를 사전 margin 안에 유지한다.
- **최소 실험:** 동일 human motion library와 구조·actuation range가 다른 3개 simulated morphology에 kinematic, hard-filtered, KDMR-style per-morph dynamics optimization, morphology-conditioned calibrated select/modify/reject를 적용한다. 두 morphology에서 threshold를 정하고 세 번째를 held-out test로 두는 leave-one-morphology-out 평가 후, 같은 tracking policy budget으로 비교한다.
- **판정 지표:** feasibility Brier/ECE, retained/rejected coverage, worst-morphology training steps·tracking error·fall·torque/contact violation·downstream success.
- **Reject criterion:** held-out morphology에서 calibration error와 safety–coverage Pareto frontier가 per-morph hard filter 또는 dynamics optimizer보다 개선되지 않거나 threshold ordering이 morphology마다 뒤집히면 cross-morphology calibration claim을 기각한다. 그 경우 morphology-specific feasibility model 또는 soft residual correction으로 범위를 축소한다.
- **Paper basis:** [DeepMimic](../2018/TOG-SIGGRAPH/2018_TOG-SIGGRAPH_DeepMimic-Example-Guided-Deep-Reinforcement-Learning-of-Ph/01_overview.md), [HumanPlus](../2024/CoRL/2024_CoRL_HumanPlus-Humanoid-Shadowing-and-Imitation-from-Humans/01_overview.md), [OmniH2O](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md), [KDMR](https://arxiv.org/abs/2603.09956) `PREPRINT`, [Rhythm](https://roboticsconference.org/program/papers/34/).

### I-11. Morphology-graph-conditioned cross-embodiment value adapter

- **Program / execution:** RP-6 / E2; I-08에서 morphology coverage가 실제 bottleneck임이 확인된 후 진행한다.
- **Gap:** [G-12](./RESEARCH_GAPS.md#g-12-data-scale와-data-coverage의-혼동)
- **`R-M-C-O-T-S`:** at least two arm/legged morphologies / graph-conditioned feasibility·value adapter / no adapter·action adapter·graph policy / worst-embodiment success·calibration·OOD action·data efficiency / transfer and fine-tuning horizon / normalized heterogeneous-action dataset.
- **방법론 근거:** Body Transformer의 sensor/actuator graph와 body-induced masked attention, CQL/IQL의 conservative/in-sample value learning, Open X-Embodiment의 heterogeneous action normalization setting을 사용한다.
- **선행 연구가 해결한 것:** morphology graph bias와 heterogeneous action normalization뿐 아니라, Systematic Co-training Study와 Emergence of Human-to-Robot Transfer가 modality·diversity·cross-embodiment transfer 효과를 대규모로 직접 비교했다. 따라서 graph adapter나 embodiment data 추가 자체는 contribution이 아니다.
- **새 연구 단위:** shared morphology-graph encoder 위에 embodiment-conditioned feasibility/value head를 두어, normalized action이 각 robot에서 실행 가능한지와 dataset support 안에 있는지를 함께 추정한다.
- **가설:** I-08의 matched-budget audit에서 morphology가 worst-group bottleneck으로 확인된 경우에 한해, action adapter보다 graph-conditioned value/feasibility adapter가 negative transfer와 worst-embodiment degradation을 줄인다.
- **최소 실험:** 구조가 다른 두 arm 또는 legged embodiment에서 no adapter, action adapter, graph policy, graph+value adapter를 비교한다.
- **판정 지표:** per-embodiment/worst-group success, feasibility calibration, OOD action rate, fine-tuning data efficiency.
- **Reject criterion:** embodiment oracle ID와 exact morphology graph를 제공해도 value adapter 이득이 없으면 negative transfer 원인은 morphology가 아니라 task/data mismatch다.
- **Paper basis:** [Body Transformer](../2024/CoRL/2024_CoRL_Body-Transformer-Leveraging-Robot-Embodiment-for-Policy-Le/01_overview.md), [CQL](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md), [IQL](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md), [Open X-Embodiment](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md), [Systematic Co-training Study](https://roboticsconference.org/program/papers/7/), [Emergence of Human-to-Robot Transfer](https://roboticsconference.org/program/papers/72/).

## Evaluation infrastructure card

### I-12. Recovery event protocol for existing long-horizon benchmarks

- **Program / execution:** RP-2 / INFRA; [구체 명세](./projects/RP-2_FAILURE_RECOVERY.md)를 따르며 I-02와 독립 논문으로 확대하기보다 공통 evaluator로 유지한다.
- **Gap:** [G-02](./RESEARCH_GAPS.md#g-02-detection에서-recovery까지-닫히지-않은-loop), [G-10](./RESEARCH_GAPS.md#g-10-long-horizon-평가의-낮은-failure-resolution)
- **`R-M-C-O-T-S`:** long-horizon manipulation/VLA / shared perturbation·event·clone·budget schema / native final-success·suite-specific recovery metric / onset consistency·option outcome·phase progress·irreversible event / full episode after first failure / LIBERO first, then one of CALVIN·FurnitureBench.
- **방법론 근거:** FurnitureBench의 phase progress, BEHAVIOR-1K의 failure taxonomy, AtomicVLA의 post-failure termination critique, VLA-Arena의 stress axes, SO-101의 recovery-aware evaluation, Beyond Binary Success의 sequential partial-progress comparison, Discounted Liveness OPE의 non-monotonic progress formulation을 사용한다.
- **선행 연구가 해결한 것:** fine-grained progress, failure taxonomy, recovery-aware metric, statistically efficient comparison, non-monotonic progress evaluation은 이미 제시됐다. 따라서 “binary success를 넘는 metric” 자체는 contribution이 아니다.
- **새 연구 단위:** 기존 benchmark에 공통 `event_id`, cloned `onset_state_id`, perturbation provenance, option abstraction, vector recovery budget, irreversibility, post-recovery outcome을 붙여 same-onset option comparison이 가능하게 한다.
- **가설:** clean-start final-success ranking과 native recovery metric만으로는 option selector의 regret와 failure-family별 budget sensitivity를 설명하지 못하며, common onset/option schema가 그 차이를 재현 가능하게 분리한다.
- **최소 실험:** LIBERO에서 occlusion, object displacement, grasp slip, sensor dropout, instruction correction을 event landmark에 삽입하고 deterministic clone/restore validity를 먼저 통과한다. 두 번째 suite는 I-02의 crossing과 selector signal이 확인된 뒤 동일 schema adapter만 추가한다.
- **판정 지표:** restore determinism, onset consistency, event completeness, option-sweep stability, failure-conditioned completion, phase progress, recovery cost, irreversible failure, regret-to-oracle, adapter agreement.
- **Reject criterion:** clone/restore와 event annotation 신뢰도가 기준을 통과하지 못하면 I-02 학습 전에 protocol을 수정한다. protocol이 유효해도 native metric이 option regret와 budget crossing을 충분히 설명하면 독립 evaluator contribution은 주장하지 않는다.
- **산출물:** perturbation/clone wrapper, `rp2.event.v2` schema, vector-budget evaluator, option-outcome table, second-suite adapter template.
- **Paper basis:** [FurnitureBench](../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md), [BEHAVIOR-1K](../2022/CoRL/2022_CoRL_BEHAVIOR-1K-A-Benchmark-for-Embodied-AI-with-1000-Everyday/01_overview.md), [AtomicVLA](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md), [VLA-Arena](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md), [RLBench](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md), [SO-101 Failure and Recovery](https://arxiv.org/abs/2606.08881) `PREPRINT`, [Beyond Binary Success](https://roboticsconference.org/program/papers/76/), [Discounted Liveness OPE](https://roboticsconference.org/program/papers/154/).

## 실행 순서

하나의 전체 순위를 고정하지 않는다. hardware·data·simulator 준비 상태에 따라 아래 dependency path 중 하나를 선택한다.

1. **RP-2 Recovery:** I-12로 event·clone·budget schema와 option-outcome table을 고정한 뒤 I-02의 counterfactual option crossing과 selector regret를 검증한다. I-02가 지지될 때만 I-06 policy reuse로 확장한다.
2. **RP-6 Data:** I-08로 joint coverage cell과 split을 고정한다. morphology가 실제 worst-group bottleneck일 때만 I-11로 확장한다.
3. **RP-3 State:** I-07로 compute-matched representation baseline을 만든 뒤 I-09의 active-view value를 측정한다. I-03은 공통 state instrumentation을 쓰되 독립적으로 진행할 수 있다.
4. **RP-4 World model:** I-04A ranking calibration이 subgroup에서 성립한 후에만 I-04B imagined policy update를 허용한다.
5. **RP-5 Whole body:** I-10 retargeting과 I-05 runtime hierarchy를 각각 반증한 뒤, 둘 다 지지되는 경우에만 통합한다.
6. **RP-1 Contact:** 두 종류 이상 sensor/contact setup을 준비할 수 있을 때 I-01을 시작한다. 단일 sensor만으로는 transfer claim을 검증할 수 없다.

현재 우선 scoping 단위는 I-12의 LIBERO clone/restore validity와 20–50개 onset의 pilot option sweep이다. 여기서 option crossing이 관찰되어야 I-02 learned selector로 넘어간다. I-08 metadata coverage audit과 I-07 compute-matching protocol은 RP-2와 독립적으로 수행 가능한 secondary scoping이다.

## 아이디어 승격 기록

| Idea | Program | Execution | Project state | Literature basis | Hypothesis evidence | 다음 결정 |
|---|---|---|---|---|---|---|
| I-01 | RP-1 | E1 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | 두 sensor·contact shift와 safety authority 변수 확정 |
| I-02 | RP-2 | E1 | `SCOPED / FOCUS` | `READING-SUPPORTED` | `UNTESTED` | LIBERO cloned onset에서 option crossing·best-fixed regret pilot |
| I-03 | RP-3 | E1 | `SCOPED / NEXT` | `READING-SUPPORTED` | `UNTESTED` | RoboCasa base-policy/memory competence와 20–50 onset causality pilot |
| I-04 | RP-4 | E1→E2 | `HYPOTHESIS / SECONDARY` | `READING-SUPPORTED` | `UNTESTED` | subgroup false-safe ranking audit; update branch는 hold |
| I-05 | RP-5 | E2 | `DEFERRED` | `READING-SUPPORTED` | `UNTESTED` | transition phase·risk vector와 strongest 2026 baseline 구현 가능성 확인 |
| I-06 | RP-2 | E2 | `CONDITIONAL` | `READING-SUPPORTED` | `UNTESTED` | I-02 crossing과 option-outcome signal 확인 전 hold |
| I-07 | RP-3 | E1 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | compute·view·parameter matching protocol 확정 |
| I-08 | RP-6 | E1 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | metadata coverage cell과 held-out split 정의 |
| I-09 | RP-3 | E2 | `BACKLOG` | `READING-SUPPORTED` | `UNTESTED` | oracle value-of-information upper bound 확인 |
| I-10 | RP-5 | E1 | `DEFERRED` | `READING-SUPPORTED` | `UNTESTED` | 3개 simulated morphology의 leave-one-out feasibility calibration 가능성 확인 |
| I-11 | RP-6 | E2 | `BACKLOG` | `READING-SUPPORTED` | `UNTESTED` | I-08에서 morphology bottleneck 먼저 확인 |
| I-12 | RP-2 | INFRA | `INFRASTRUCTURE / ACTIVE` | `READING-SUPPORTED` | `UNTESTED` | `rp2.event.v2` logger, LIBERO clone/restore, pilot option table 구현 |

Method card의 project state는 `HYPOTHESIS → SCOPED → RUNNING → SUPPORTED / REJECTED / REVISED` 순서로 갱신한다. `INFRASTRUCTURE`는 방법 가설이 아니라 공통 평가 산출물임을 뜻한다. `Literature basis`는 문헌 근거 수준이고, `Hypothesis evidence`는 직접 실험 근거다. 아이디어가 반증되면 삭제하지 않고 reject criterion과 결과를 기록해 `REJECTED` 또는 `REVISED`로 남긴다.
