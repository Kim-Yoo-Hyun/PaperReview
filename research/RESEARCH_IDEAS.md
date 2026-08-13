# Robotics Research Ideas

- Updated: 2026-08-13 KST
- Research stance: Robotics가 주축이며 VLA와 3D perception은 실제 closed-loop behavior를 개선하는 구성요소로 다룬다.
- Gap source: [RESEARCH_GAPS.md](./RESEARCH_GAPS.md)
- Lineage source: [synthesis/](../synthesis/README.md)
- Literature basis: 12개 아이디어 모두 관련 gap의 `READING-SUPPORTED` 원문 감사에 근거한다.
- Gap-method alignment: 2026-08-13에 6개 macro-gap과 robotics `R-M-C-O-T-S` 범위로 재검토했다.
- Hypothesis status: 모든 아이디어는 아직 `UNTESTED`다. 문헌 근거가 있다는 사실과 제안 가설이 실험적으로 지지됐다는 사실을 구분한다.
- Active project spec: [RP-2 Failure-to-Recovery Loop](./projects/RP-2_FAILURE_RECOVERY.md)

## 이 문서의 역할

`RESEARCH_GAPS.md`가 원문 비교 후 남은 문제를 기록한다면, 이 문서는 그 문제를 **기존 논문에서 검증된 방법 요소를 조합한 반증 가능한 연구 가설**로 바꾼다. 13개 gap을 12개 독립 project로 해석하지 않고, 6개 macro-gap에 대응하는 연구 프로그램 안의 decision experiment로 취급한다. 방법론은 임의로 발명하지 않고 아래 네 층으로 구분한다.

1. **방법론 근거:** 어떤 논문의 어떤 요소를 가져오는가.
2. **Gap alignment:** 어떤 macro/sub-gap의 claim을 어떤 `R-M-C-O-T-S`에서 검사하는가.
3. **새 연구 단위:** 선행 연구가 각각 다룬 요소 사이에서 무엇을 새로 연결하거나 통제하는가.
4. **Decision rule:** 어떤 결과에서 가설을 지지·축소·기각하는가.

논문의 module 이름만 바꾸거나 이미 입증된 결합을 반복하지 않는다. 예를 들어 slow–fast tactile VLA 자체는 Reactive Diffusion Policy와 AT-VLA가, hybrid force–position VLA는 ForceVLA2가 이미 다룬다. 새 연구는 cross-sensor transfer, calibration, uncertainty 또는 safety처럼 원문에서 남긴 경계를 검증해야 한다.

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
| RP-2 Failure-to-recovery loop | M-2 | I-12 → I-02 | 먼저 공통 event protocol을 만든 뒤 typed recovery를 비교 |
| RP-3 Task-effective state | M-3 | I-07 → I-09; I-03 parallel | representation의 순수 control value와 추가 관측을 먼저 연결하고, memory는 공통 state instrumentation으로 독립 검사 |
| RP-4 Model-based decision | M-4 | I-04A → I-04B | world-model ranking calibration을 먼저 검증한 뒤 policy update로 진행 |
| RP-5 Embodied deployment | M-5 | I-10; I-05 parallel, then integration | feasible motion prior와 runtime risk interface를 각각 검증한 뒤 결합 |
| RP-6 Data and evidence | M-6 | I-08 → I-06 → I-11 | coverage audit, typed failure reuse, cross-embodiment adapter 순으로 범위를 넓힘 |

## Decision experiment portfolio

`E1/E2`는 gap의 중요도가 아니라 첫 decision experiment의 dependency다. `INFRA`는 method claim이 아닌 공통 평가 도구다.

| Idea | Program | Execution | Primary gap | 핵심 연구 단위 | 첫 검증 환경 |
|---|---|---|---|---|---|
| I-01 | RP-1 | E1 | G-01; G-05 secondary | slow–fast contact control의 sensor/embodiment transfer | contact-rich real robot 또는 high-fidelity setup |
| I-02 | RP-2 | E1 | G-02; G-10 evaluation dependency | calibrated failure detection → typed recovery selection | LIBERO/CALVIN perturbation wrapper |
| I-03 | RP-3 | E1 | G-04 | phase-aware memory update와 confidence-based expiry | RoboCasa/RLBench dynamic scene |
| I-04 | RP-4 | E1→E2 | G-07 → G-08 | contact-calibrated ranking 후 policy update | existing rollout dataset + 소규모 real validation |
| I-05 | RP-5 | E2 | G-09 | whole-body controller에 task risk budget 전달 | HumanoidBench |
| I-06 | RP-6 | E1 | G-06 | unsuccessful trajectory의 typed conservative reuse | DROID/offline robot data |
| I-07 | RP-3 | E1 | G-03 | compute-matched 2D/3D control utility | RLBench/FlowBot-style articulation |
| I-08 | RP-6 | E1 | G-12 | condition coverage를 최적화하는 data subset | DROID/OXE-style metadata |
| I-09 | RP-3 | E2 | G-13; G-03 control | action value에 따른 active-perception stopping | occluded grasp/articulation |
| I-10 | RP-5 | E1 | G-11 | contact-feasible human-to-humanoid retargeting | humanoid simulation |
| I-11 | RP-6 | E2 | G-12 | morphology graph 기반 cross-embodiment value adapter | 2개 이상 embodiment |
| I-12 | RP-2 | INFRA | G-10; G-02 support | benchmark-independent recovery event protocol | 기존 2개 benchmark wrapper |

## Hypothesis cards I-01–I-06

### I-01. Transfer-calibrated dual-rate contact executor

- **Program / execution:** RP-1 / E1.
- **Gap:** [G-01](./RESEARCH_GAPS.md#g-01-vla와-접촉-제어의-시간-척도-불일치), [G-05](./RESEARCH_GAPS.md#g-05-contact-state의-불완전한-observability와-sensor-종속성)
- **`R-M-C-O-T-S`:** multi-sensor manipulator / uncertainty-calibrated slow–fast fusion·authority scheduling / vision-only·early fusion·gated dual stream / success·peak force·reaction latency·calibration / contact event, delay·dropout sweep / peg insertion·wiping on real or high-fidelity contact setup.
- **방법론 근거:** AT-VLA의 Adaptive Tactile Injection·Tactile Gate·slow visual/fast tactile dual stream, ForceVLA2의 Cross-Scale MoE와 hybrid force–position action, Tactile-Driven Non-Prehensile Manipulation의 explicit contact/friction constraint를 사용한다.
- **선행 연구가 해결한 것:** gated multimodal injection이 naïve fusion보다 낫고, 빠른 tactile/force pathway가 contact-rich task success를 높일 수 있다는 점은 이미 입증됐다.
- **새 연구 단위:** sensor가 바뀌거나 stiffness·latency·calibration이 달라질 때 fast stream의 confidence를 추정하고, confidence가 낮으면 residual authority를 줄이거나 safe position control로 전환한다.
- **가설:** gated slow–fast controller에 sensor-calibrated uncertainty와 authority scheduling을 추가하면, 단순 slow–fast 구조보다 unseen sensor/delay에서 peak force를 늘리지 않고 성공률을 유지한다.
- **최소 실험:** peg insertion과 wiping에서 vision-only, naïve force concatenation, AT-VLA식 gated dual stream, uncertainty-gated dual stream을 비교한다. 같은 demonstration과 backbone을 사용하고 sensor delay, dropout, stiffness 또는 sensor model을 독립적으로 바꾼다.
- **판정 지표:** success, peak/impulse force, reaction latency, force tracking error, unsafe residual activation, calibration error.
- **Reject criterion:** uncertainty gate가 unseen condition에서 naïve gated dual stream보다 safety–success Pareto frontier를 개선하지 못하면 별도 architecture 연구를 중단하고 calibration/data augmentation 문제로 축소한다.
- **Paper basis:** [AT-VLA](../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md), [ForceVLA2](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md), [Tactile-Driven Non-Prehensile Manipulation](../2024/RSS/2024_RSS_Tactile-Driven-Non-Prehensile-Object-Manipulation-via-Extr/01_overview.md), [Reactive Diffusion Policy](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md).

### I-02. Risk-budgeted typed recovery for VLA

- **Program / execution:** RP-2 / E1; [project spec](./projects/RP-2_FAILURE_RECOVERY.md)의 I-12 event protocol을 먼저 사용한다.
- **Gap:** [G-02](./RESEARCH_GAPS.md#g-02-detection에서-recovery까지-닫히지-않은-loop), [G-10](./RESEARCH_GAPS.md#g-10-long-horizon-평가의-낮은-failure-resolution)
- **`R-M-C-O-T-S`:** VLA manipulator / typed recovery selector / abort·blind retry·replan / final completion·irreversible failure·intervention cost / failure onset에서 post-recovery까지 / LIBERO·CALVIN perturbation wrapper.
- **방법론 근거:** SAFE의 VLA latent-feature failure score와 conformal threshold, Recovery RL의 task/recovery policy 분리와 safety critic, PDDLStream의 symbolic–continuous replanning interface를 사용한다. FLARE의 Retry/Reset taxonomy는 피해야 할 중복이자 strong baseline이다.
- **선행 연구가 해결한 것:** SAFE는 unseen-task failure detection을, Recovery RL은 learned recovery zone을, FLARE는 ID/OOD 오류에 대한 Retry/Reset recovery를 이미 다룬다. 따라서 단순히 type을 붙여 retry/reset하는 것은 새 연구 단위가 아니다.
- **새 연구 단위:** 공통 event schema에서 scalar alert를 `failure cause × operational recoverability × remaining budget`으로 변환하고, 동일한 skill library와 budget 아래 retry, reobserve, retreat/reset, replan, ask-for-help 중 option을 선택한다. detector와 selector 오류는 oracle ablation으로 분리한다.
- **가설:** detector와 recovery selector를 분리해 각각 calibration하면 binary abort, blind retry, FLARE-style binary retry/reset보다 irreversible failure를 늘리지 않으면서 recoverable failure의 budgeted completion을 높인다.
- **최소 실험:** LIBERO-Long 4개 task에 observation, execution/contact, world-state, plan-semantic perturbation을 event landmark에서 삽입한다. abort, blind retry, privileged replan, binary retry/reset, typed selector를 600-step native horizon과 같은 recovery budget에서 비교하고 이후 CALVIN으로 옮긴다.
- **판정 지표:** detection lead time, false intervention, type accuracy, recovery success, irreversible failure, added action cost, final completion.
- **Reject criterion:** oracle failure type을 제공해도 typed recovery가 retry/replan baseline을 이기지 못하면 detector 연구가 아니라 recovery skill library의 expressivity 문제로 판정한다.
- **Paper basis:** [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md), [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md), [PDDLStream](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md), [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md), [FLARE (CVPR 2026)](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html).

### I-03. Phase-aware spatial memory with learned expiry

- **Program / execution:** RP-3 / E1; I-07의 state comparison protocol을 가능하면 재사용한다.
- **Gap:** [G-04](./RESEARCH_GAPS.md#g-04-persistent-spatial-memory의-staleness와-uncertainty)
- **`R-M-C-O-T-S`:** mobile/manipulation VLA / phase·confidence·expiry memory / no memory·persistent memory·similarity refinement / stale read·unsafe action·success·rescan / multi-step state transition / RoboCasa·RLBench relocation·removal·delay.
- **방법론 근거:** MomaGraph의 observed state transition 기반 graph-edge update, SOMA의 Spatial Memory Construction·Dynamic Memory Refinement·Contextual Memory Retrieval을 사용한다.
- **선행 연구가 해결한 것:** out-of-view object memory와 interaction 후 graph update는 가능하다. 그러나 SOMA는 object-level refinement가 drawer open/closed 같은 task phase를 구분하지 못하고, stale/incorrect memory의 safety risk를 명시한다.
- **새 연구 단위:** memory token에 phase-transition probability, geometric confidence, age를 붙이고 `retain / refresh / expire / actively verify`를 선택한다.
- **가설:** similarity-only update보다 phase-aware confidence와 expiry를 쓰면 relocation·object removal에서 stale-memory-induced action을 줄이면서 불필요한 re-scan 증가를 제한한다.
- **최소 실험:** RoboCasa 또는 RLBench에서 object relocation, disappearance, drawer state change, delayed observation을 통제한다. no-memory, SOMA-style refinement, phase+expiry memory를 같은 policy에 연결한다.
- **판정 지표:** stale read rate, phase-state accuracy, task success, unsafe grasp/placement, re-scan count, latency.
- **Reject criterion:** oracle phase label에서도 expiry가 persistent memory보다 이득이 없으면 memory update가 아니라 downstream policy의 memory usage가 병목이라고 판정한다.
- **Paper basis:** [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md), [Spatial Memory for Out-of-Vision Manipulation](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md), [ConceptFusion](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md).

### I-04. Contact-calibrated world model for policy ranking and improvement

- **Program / execution:** RP-4 / I-04A E1 ranking audit → I-04B E2 policy update.
- **Gap:** [G-07](./RESEARCH_GAPS.md#g-07-world-model의-visual-fidelity와-control-fidelity-불일치), [G-08](./RESEARCH_GAPS.md#g-08-imagined-policy-improvement의-보수성과-calibration)
- **`R-M-C-O-T-S`:** VLA checkpoints·candidate chunks / contact-event-calibrated world-model OPE·conservative update / visual-only ranking·no update·offline DPO / subgroup rank·false-safe·predicted-real gain / rollout horizon·update-size sweep / paired ID·OOD·contact rollouts and small real validation.
- **방법론 근거:** WorldGym의 action-conditioned video rollout·VLM reward·policy ranking protocol, MOPO의 uncertainty-penalized imagined reward, WMPO의 world-model on-policy optimization을 사용한다.
- **선행 연구가 해결한 것:** 평균 real-world success와 policy ranking을 world model이 보존할 수 있고, imagined on-policy update가 실제 robot 성능을 높일 수 있다는 증거가 있다.
- **새 연구 단위:** pixel/reward uncertainty와 별도로 contact transition, jamming, slip, constraint violation의 event probability를 예측하고 이 uncertainty로 ranking과 policy update를 보수화한다.
- **가설 A — ranking:** contact-event head와 subgroup calibration을 추가하면 visual-only WorldGym보다 contact-rich/OOD condition의 false-safe ranking을 낮춘다.
- **가설 B — update:** A의 calibration이 성립한 subgroup에서만 uncertainty-penalized update를 허용하면 WMPO-style imagined gain의 real-gain overestimation을 낮춘다.
- **최소 실험:** 먼저 여러 policy checkpoint의 action chunk를 동일 initial state에서 평가해 world-model/real pairwise ranking을 visual OOD, free-space, contact-rich subgroup으로 나눈다. A가 성립한 뒤에만 작은 trust-region update를 high-fidelity environment와 소규모 real trial에서 검증한다.
- **판정 지표:** subgroup rank correlation, event calibration, false-safe rate, predicted gain–real gain error, unsafe proposal rate.
- **Reject criterion:** oracle contact label을 학습해도 ranking 또는 real-gain calibration이 개선되지 않으면 별도 contact model이 아니라 dynamics horizon/representation 문제로 축소한다.
- **Paper basis:** [WorldGym](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md), [MOPO](../2020/NeurIPS/2020_NeurIPS_MOPO-Model-based-Offline-Policy-Optimization/01_overview.md), [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md), [Unified World Models](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md).

### I-05. Risk-budget interface for whole-body loco-manipulation

- **Program / execution:** RP-5 / E2; I-10의 feasible prior가 없어도 G-09 interface를 독립 검사할 수 있어야 한다.
- **Gap:** [G-09](./RESEARCH_GAPS.md#g-09-locomotion과-manipulation의-bandwidthobjective-충돌)
- **`R-M-C-O-T-S`:** mobile manipulator/humanoid / high-level risk budget to whole-body controller / decoupled·monolithic·fixed hierarchy / stage completion·fall·support margin·torque·recovery / locomotion-to-contact transition / HumanoidBench door·carry with payload·push.
- **방법론 근거:** Whole-Body NMPC의 contact/timing optimization과 receding-horizon replanning, HumanoidBench의 reusable low-level reaching hierarchy, OmniH2O의 kinematic pose interface와 robust whole-body tracking을 사용한다.
- **선행 연구가 해결한 것:** fast contact-aware whole-body control과 hierarchy는 각각 가능하지만, manipulation progress와 balance/recovery 우선순위를 task planner가 명시적으로 조절하는 interface는 부족하다.
- **새 연구 단위:** high-level subgoal에 end-effector target뿐 아니라 support margin, allowed base motion, peak torque/contact, recovery reserve를 포함한 risk budget을 전달한다.
- **가설:** fixed-weight monolithic policy나 decoupled skill보다 risk-budget hierarchy가 disturbance와 payload 변화에서 fall을 줄이면서 manipulation progress를 유지한다.
- **최소 실험:** HumanoidBench door/carry/reach 계열에서 decoupled, monolithic, fixed hierarchy, risk-budget hierarchy를 비교하고 payload·external push를 sweep한다.
- **판정 지표:** stage completion, fall, support-margin violation, peak torque, recovery time, end-effector error, energy.
- **Reject criterion:** oracle risk budget에서도 fixed hierarchy 대비 Pareto 개선이 없으면 high-level budget interface가 아니라 low-level controller capacity가 병목이다.
- **Paper basis:** [Whole-Body NMPC](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md), [HumanoidBench](../2024/RSS/2024_RSS_HumanoidBench-Simulated-Humanoid-Benchmark-for-Whole-Body/01_overview.md), [OmniH2O](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md), [Mobile ALOHA](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md).

### I-06. Typed conservative learning from unsuccessful robot trajectories

- **Program / execution:** RP-6 / E1; I-08 coverage stratification을 data split에 사용한다.
- **Gap:** [G-06](./RESEARCH_GAPS.md#g-06-failure와-suboptimal-data의-안전한-재사용)
- **`R-M-C-O-T-S`:** offline manipulation/VLA data / typed-failure weighting·conservative value learning / success-only BC·naïve mix·IQL·CQL / success·harmful action·recovery·worst group / pre-onset에서 post-recovery까지 / DROID or controllable simulator held-out conditions.
- **방법론 근거:** CQL의 conservative Q regularization, IQL의 in-sample value learning과 advantage-weighted BC, DROID가 공개한 successful/unsuccessful outcome metadata, SAFE의 failure representation을 사용한다.
- **선행 연구가 해결한 것:** OOD action value overestimation은 완화할 수 있고 실패 trajectory도 수집돼 있다. 하지만 DROID의 주 policy 실험은 successful subset을 사용하며 failure cause·severity는 objective에 들어가지 않는다.
- **새 연구 단위:** unsuccessful trajectory를 전부 negative로 취급하지 않고 `recoverable prefix / harmful action / irreversible terminal`로 분할해 서로 다른 conservative weight와 target을 준다.
- **가설:** typed weighting을 적용한 IQL/CQL이 success-only와 naïve mixed training보다 harmful update를 줄이고 recovery 가능 state의 유용한 행동은 보존한다.
- **최소 실험:** DROID unsuccessful trajectory의 작은 수동 분류 subset 또는 controllable simulator data로 success-only BC, mixed BC, IQL/CQL, typed conservative learning을 비교한다.
- **판정 지표:** task success, recovery success, harmful action rate, value calibration, worst-failure-group performance.
- **Reject criterion:** oracle failure segmentation을 사용해도 standard IQL/CQL을 이기지 못하면 새로운 loss보다 reward relabeling 또는 data coverage 문제가 우선이다.
- **Paper basis:** [CQL](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md), [IQL](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md), [DROID](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md), [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md).

## Hypothesis cards I-07–I-11

### I-07. Compute-matched task-conditioned 3D control bottleneck

- **Program / execution:** RP-3 / E1.
- **Gap:** [G-03](./RESEARCH_GAPS.md#g-03-3d-perception-향상과-control-향상의-compute-matched-인과성)
- **`R-M-C-O-T-S`:** vision-based manipulator / RGB·dense 3D·task-conditioned state / matched backbone·data·view·runtime / success·collision·contact error·latency / per-action inference / articulation·occluded grasp with pose·calibration perturbation.
- **방법론 근거:** FlowBot3D의 task-specific 3D articulation flow와 analytic execution policy, ActiveVLA의 3D critical-region localization·active view·zoom ablation을 사용한다.
- **선행 연구가 해결한 것:** 3D flow와 active view가 articulation·precise manipulation에 유용할 수 있다는 증거는 있지만, representation·view·compute의 기여가 같은 budget에서 분리되지 않았다.
- **새 연구 단위:** RGB, dense 3D, task-conditioned object/contact state가 같은 view·parameter·runtime budget에서 control에 주는 순수 이득을 비교한다.
- **가설:** dense point cloud 전체보다 task-conditioned pose, affordance/flow, contact surface, uncertainty bottleneck이 같은 compute에서 더 높은 control success를 낸다.
- **최소 실험:** articulation 또는 occluded grasp task에서 동일 policy head와 training data를 유지하고 representation만 바꾼다. latency-matched와 unconstrained 두 setting을 모두 보고한다.
- **판정 지표:** success, collision, contact error, latency, memory, representation perturbation sensitivity.
- **Reject criterion:** compute를 맞춘 뒤 task-conditioned bottleneck이 raw RGB 또는 dense 3D보다 이득이 없으면 별도 representation contribution을 주장하지 않는다.
- **Paper basis:** [FlowBot3D](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md), [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md), [SUGAR](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md).

### I-08. Coverage-aware robot data subset scaling

- **Program / execution:** RP-6 / E1.
- **Gap:** [G-12](./RESEARCH_GAPS.md#g-12-data-scale와-data-coverage의-혼동)
- **`R-M-C-O-T-S`:** heterogeneous robot datasets / multi-axis coverage-aware subset / equal-budget random·scene-only balanced subset / average·worst-group·new-condition gain / training scale curve / DROID·OXE-style task×embodiment×sensor×operator×outcome metadata.
- **방법론 근거:** Data Scaling Laws의 environment/object diversity control과 power-law evaluation, DROID의 matched-size scene-diversity experiment를 사용한다.
- **선행 연구가 해결한 것:** environment/object diversity가 demonstrations-per-condition보다 중요하고 scene diversity가 전이에 도움이 된다는 결과는 있지만, multi-embodiment·outcome coverage의 효과는 아직 분리되지 않았다.
- **새 연구 단위:** environment/object뿐 아니라 task, operator, embodiment, outcome condition을 coverage cell로 정의하고 같은 trajectory budget에서 subset allocation을 최적화한다.
- **가설:** random 또는 scene-only diversity보다 multi-axis worst-covered-cell sampling이 평균 성능을 크게 희생하지 않고 worst-group·new-condition 성능을 높인다.
- **최소 실험:** DROID/OXE-style metadata에서 random, scene-balanced, multi-axis balanced, failure-aware subset을 같은 크기로 구성해 동일 policy를 학습한다.
- **판정 지표:** average success, worst-group success, new-scene/task/embodiment performance, effective coverage, marginal gain per trajectory.
- **Reject criterion:** metadata cell을 oracle로 제공해도 random sampling과 차이가 없으면 coverage optimizer보다 representation/model capacity가 우선이다.
- **Paper basis:** [Data Scaling Laws](../2025/ICLR/2025_ICLR_Data-Scaling-Laws-in-Imitation-Learning-for-Robotic-Manipu/01_overview.md), [DROID](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md), [Open X-Embodiment](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md).

### I-09. Action-value stopping policy for active perception

- **Program / execution:** RP-3 / E2; I-07의 compute-matched state baseline 이후 진행한다.
- **Gap:** [G-03](./RESEARCH_GAPS.md#g-03-3d-perception-향상과-control-향상의-compute-matched-인과성), [G-13](./RESEARCH_GAPS.md#g-13-active-perception의-비용-대비-control-value)
- **`R-M-C-O-T-S`:** active-camera manipulator / action-value·disagreement stopping / fixed view·fixed count·geometry entropy / success gain per second·travel·collision·unnecessary view / pre-action·mid-task acquisition / occluded grasp·articulation with physical/virtual camera budget.
- **방법론 근거:** ActiveVLA의 active viewpoint scoring과 3D zoom, Where2Act의 actionability score, FlowBot3D의 re-observation-based flow execution을 사용한다.
- **선행 연구가 해결한 것:** 여러 view가 성공을 높이지만 ActiveVLA에서 세 view 이후 포화되고 inference time이 늘어난다.
- **새 연구 단위:** geometry uncertainty가 아니라 새 view가 action distribution 또는 predicted task value를 얼마나 바꿀지를 추정해 `observe / act`를 결정한다.
- **가설:** action-value stopping이 fixed three-view와 geometry-entropy selection보다 적은 sensing/motion cost로 같은 success를 낸다.
- **최소 실험:** occluded grasp와 articulated-object task에서 fixed-view, fixed-three-view, entropy, action-disagreement/value-of-information을 비교한다.
- **판정 지표:** success, views, sensing latency, physical/virtual camera travel, unnecessary-view rate, collision.
- **Reject criterion:** oracle future-view outcome으로도 adaptive stopping 이득이 작으면 해당 task에서는 active sensing보다 robust policy training이 더 적합하다.
- **Paper basis:** [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md), [Where2Act](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md), [FlowBot3D](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md).

### I-10. Contact-feasible human-to-humanoid retargeting

- **Program / execution:** RP-5 / E1.
- **Gap:** [G-11](./RESEARCH_GAPS.md#g-11-human-motion-prior와-contact-feasibility의-충돌)
- **`R-M-C-O-T-S`:** multiple humanoid morphologies / contact·dynamics-aware retargeting / kinematic-only·hard feasibility filter / downstream success·fall·torque/contact violation·coverage / clip-to-long-horizon tracking / simulation with selected hardware validation.
- **방법론 근거:** DeepMimic의 physics-based imitation objective와 reference-state initialization, HumanPlus의 fixed human-to-robot pose mapping, OmniH2O의 large-scale retargeting·infeasible-motion filtering·teacher/student tracking을 사용한다.
- **선행 연구가 해결한 것:** retargeted motion을 physics policy로 안정화하고 infeasible clip을 filtering하는 방향은 검증됐지만, morphology별 contact/torque feasibility와 downstream task utility를 동시에 최적화하지는 않았다.
- **새 연구 단위:** 사후 RL이 해결하도록 두지 않고 retarget 단계에서 support, torque, self/object collision, intended contact를 jointly score해 demonstration을 수정·선택한다.
- **가설:** contact-feasible retarget data가 kinematic-only data보다 tracking learner의 sample efficiency와 downstream task success를 높이고 safety violation을 줄인다.
- **최소 실험:** 동일 human motion library를 kinematic, hard-filtered, optimization-refined 세 방식으로 retarget한 뒤 같은 tracking policy를 학습한다.
- **판정 지표:** retained coverage, training steps, tracking error, fall, torque/contact violation, downstream success.
- **Reject criterion:** feasibility filtering이 안전성은 높이지만 motion coverage와 task success를 더 크게 낮추면 hard filter를 버리고 soft constraint/residual correction으로 수정한다.
- **Paper basis:** [DeepMimic](../2018/TOG-SIGGRAPH/2018_TOG-SIGGRAPH_DeepMimic-Example-Guided-Deep-Reinforcement-Learning-of-Ph/01_overview.md), [HumanPlus](../2024/CoRL/2024_CoRL_HumanPlus-Humanoid-Shadowing-and-Imitation-from-Humans/01_overview.md), [OmniH2O](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md).

### I-11. Morphology-graph-conditioned cross-embodiment value adapter

- **Program / execution:** RP-6 / E2; I-08에서 morphology coverage가 실제 bottleneck임이 확인된 후 진행한다.
- **Gap:** [G-12](./RESEARCH_GAPS.md#g-12-data-scale와-data-coverage의-혼동)
- **`R-M-C-O-T-S`:** at least two arm/legged morphologies / graph-conditioned feasibility·value adapter / no adapter·action adapter·graph policy / worst-embodiment success·calibration·OOD action·data efficiency / transfer and fine-tuning horizon / normalized heterogeneous-action dataset.
- **방법론 근거:** Body Transformer의 sensor/actuator graph와 body-induced masked attention, CQL/IQL의 conservative/in-sample value learning, Open X-Embodiment의 heterogeneous action normalization setting을 사용한다.
- **선행 연구가 해결한 것:** morphology graph bias는 single-morphology policy에서 유효하지만 Body Transformer는 per-node tokenizer를 쓰며 multi-embodiment transfer를 직접 해결하지 않는다.
- **새 연구 단위:** shared morphology-graph encoder 위에 embodiment-conditioned feasibility/value head를 두어, normalized action이 각 robot에서 실행 가능한지와 dataset support 안에 있는지를 함께 추정한다.
- **가설:** action adapter만 쓰는 것보다 graph-conditioned value/feasibility adapter가 heterogeneous data의 negative transfer와 worst-embodiment degradation을 줄인다.
- **최소 실험:** 구조가 다른 두 arm 또는 legged embodiment에서 no adapter, action adapter, graph policy, graph+value adapter를 비교한다.
- **판정 지표:** per-embodiment/worst-group success, feasibility calibration, OOD action rate, fine-tuning data efficiency.
- **Reject criterion:** embodiment oracle ID와 exact morphology graph를 제공해도 value adapter 이득이 없으면 negative transfer 원인은 morphology가 아니라 task/data mismatch다.
- **Paper basis:** [Body Transformer](../2024/CoRL/2024_CoRL_Body-Transformer-Leveraging-Robot-Embodiment-for-Policy-Le/01_overview.md), [CQL](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md), [IQL](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md), [Open X-Embodiment](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md).

## Evaluation infrastructure card

### I-12. Recovery event protocol for existing long-horizon benchmarks

- **Program / execution:** RP-2 / INFRA; [구체 명세](./projects/RP-2_FAILURE_RECOVERY.md)를 따르며 I-02와 독립 논문으로 확대하기보다 공통 evaluator로 유지한다.
- **Gap:** [G-02](./RESEARCH_GAPS.md#g-02-detection에서-recovery까지-닫히지-않은-loop), [G-10](./RESEARCH_GAPS.md#g-10-long-horizon-평가의-낮은-failure-resolution)
- **`R-M-C-O-T-S`:** long-horizon manipulation/VLA / shared perturbation·event schema·recovery budget / native final-success metric / phase progress·time-to-failure·recovery·irreversible event / full episode after first failure / at least two of CALVIN·LIBERO·FurnitureBench.
- **방법론 근거:** FurnitureBench의 skill/phase progress, BEHAVIOR-1K의 planning/grasp/place/detection failure taxonomy, AtomicVLA가 지적한 failure 후 benchmark termination 문제를 사용한다.
- **선행 연구가 해결한 것:** benchmark 내부의 phase progress와 failure taxonomy는 있지만, 동일한 recovery budget과 event semantics로 여러 suite를 비교하지는 못한다.
- **새 연구 단위:** 새 task suite를 만드는 대신 기존 benchmark에 동일한 perturbation, recovery budget, event log schema를 붙여 model ranking 변화를 측정한다.
- **가설:** clean-start final success 순위는 perturbation과 bounded recovery를 포함하면 유의미하게 달라지며, phase progress와 irreversible event가 그 차이를 설명한다.
- **최소 실험:** CALVIN/LIBERO/FurnitureBench 중 두 suite에 occlusion, object displacement, grasp slip, sensor dropout, instruction correction을 삽입한다.
- **판정 지표:** failure-conditioned success, phase progress, detection lead time, recovery attempts/time, intervention cost, irreversible failure, total execution cost.
- **Reject criterion:** 여러 perturbation에서도 기존 final-success ranking이 안정적이고 event metric이 추가 설명력을 주지 못하면 독립 benchmark 연구로 확대하지 않는다.
- **산출물:** perturbation wrapper, event schema, evaluator, cross-benchmark report template.
- **Paper basis:** [FurnitureBench](../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md), [BEHAVIOR-1K](../2022/CoRL/2022_CoRL_BEHAVIOR-1K-A-Benchmark-for-Embodied-AI-with-1000-Everyday/01_overview.md), [AtomicVLA](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md), [RLBench](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md).

## 실행 순서

하나의 전체 순위를 고정하지 않는다. hardware·data·simulator 준비 상태에 따라 아래 dependency path 중 하나를 선택한다.

1. **RP-2 Recovery:** I-12로 event/perturbation schema를 고정한 뒤 I-02의 oracle recovery upper bound와 typed selector를 비교한다.
2. **RP-6 Data:** I-08로 coverage cell과 split을 고정한 뒤 I-06의 failure reuse를 검사한다. morphology가 주요 bottleneck일 때만 I-11로 확장한다.
3. **RP-3 State:** I-07로 compute-matched representation baseline을 만든 뒤 I-09의 active-view value를 측정한다. I-03은 공통 state instrumentation을 쓰되 독립적으로 진행할 수 있다.
4. **RP-4 World model:** I-04A ranking calibration이 subgroup에서 성립한 후에만 I-04B imagined policy update를 허용한다.
5. **RP-5 Whole body:** I-10 retargeting과 I-05 runtime hierarchy를 각각 반증한 뒤, 둘 다 지지되는 경우에만 통합한다.
6. **RP-1 Contact:** 두 종류 이상 sensor/contact setup을 준비할 수 있을 때 I-01을 시작한다. 단일 sensor만으로는 transfer claim을 검증할 수 없다.

현재 가장 작은 scoping 단위는 I-12의 event schema, I-08의 metadata coverage audit, I-07의 compute-matching protocol이다. 이 세 가지는 신규 foundation model 학습 없이 후속 가설의 비교 가능성을 먼저 판단한다.

## 아이디어 승격 기록

| Idea | Program | Execution | Project state | Literature basis | Hypothesis evidence | 다음 결정 |
|---|---|---|---|---|---|---|
| I-01 | RP-1 | E1 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | 두 sensor·contact shift와 safety authority 변수 확정 |
| I-02 | RP-2 | E1 | `SCOPED` | `READING-SUPPORTED` | `UNTESTED` | LIBERO wrapper에서 B1–B4와 O3 upper bound 구현 |
| I-03 | RP-3 | E1 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | phase/age/confidence token ablation 설계 |
| I-04 | RP-4 | E1→E2 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | A용 paired ranking rollout 구성; B는 hold |
| I-05 | RP-5 | E2 | `BACKLOG` | `READING-SUPPORTED` | `UNTESTED` | HumanoidBench task와 risk vector 정의 |
| I-06 | RP-6 | E1 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | unsuccessful trajectory labeling cost·agreement 측정 |
| I-07 | RP-3 | E1 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | compute·view·parameter matching protocol 확정 |
| I-08 | RP-6 | E1 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | metadata coverage cell과 held-out split 정의 |
| I-09 | RP-3 | E2 | `BACKLOG` | `READING-SUPPORTED` | `UNTESTED` | oracle value-of-information upper bound 확인 |
| I-10 | RP-5 | E1 | `HYPOTHESIS` | `READING-SUPPORTED` | `UNTESTED` | feasibility score와 coverage trade-off 설계 |
| I-11 | RP-6 | E2 | `BACKLOG` | `READING-SUPPORTED` | `UNTESTED` | I-08에서 morphology bottleneck 먼저 확인 |
| I-12 | RP-2 | INFRA | `INFRASTRUCTURE` | `READING-SUPPORTED` | `UNTESTED` | `rp2.event.v1` logger와 LIBERO clone/restore test 구현 |

Method card의 project state는 `HYPOTHESIS → SCOPED → RUNNING → SUPPORTED / REJECTED / REVISED` 순서로 갱신한다. `INFRASTRUCTURE`는 방법 가설이 아니라 공통 평가 산출물임을 뜻한다. `Literature basis`는 문헌 근거 수준이고, `Hypothesis evidence`는 직접 실험 근거다. 아이디어가 반증되면 삭제하지 않고 reject criterion과 결과를 기록해 `REJECTED` 또는 `REVISED`로 남긴다.
