# Planning and Control

## Scope

Configuration-space planning, trajectory optimization, task-space motion/force control, MPC, hierarchical whole-body control을 비교한다. 핵심 질문은 학습 정책이 model-based component를 무엇까지 대체할 수 있고, 어떤 constraint와 contact structure는 명시적으로 유지해야 하는가이다.

## Reading Path

POMDP belief-state planning → Operational Space Control → PRM/RRT → CHOMP/TrajOpt → PDDLStream task-and-motion planning → Dynamic Whole-Body Control/HQP → Whole-Body NMPC → contact-aware planning and optimization.

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### Planning, control, and whole-body foundations — 10

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [Planning and Acting in Partially Observable Stochastic Domains](../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md) | 1998 / Artificial Intelligence | `UNREAD` | `CURATION_ONLY` |
| CORE | [A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation](../1987/IEEE-JRA/1987_IEEE-JRA_A-Unified-Approach-for-Motion-and-Force-Control-of-Robot-M/01_overview.md) | 1987 / IEEE JRA | `UNREAD` | `CURATION_ONLY` |
| CORE | [Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces](../1996/IEEE-T-RA/1996_IEEE-T-RA_Probabilistic-Roadmaps-for-Path-Planning-in-High-Dimension/01_overview.md) | 1996 / IEEE T-RA | `UNREAD` | `CURATION_ONLY` |
| CORE | [Rapidly-Exploring Random Trees: A New Tool for Path Planning](../1998/Technical-Report/1998_Technical-Report_Rapidly-Exploring-Random-Trees-A-New-Tool-for-Path-Plannin/01_overview.md) | 1998 / Technical Report | `UNREAD` | `CURATION_ONLY` |
| CORE | [CHOMP: Gradient Optimization Techniques for Efficient Motion Planning](../2009/ICRA/2009_ICRA_CHOMP-Gradient-Optimization-Techniques-for-Efficient-Motio/01_overview.md) | 2009 / ICRA | `UNREAD` | `CURATION_ONLY` |
| CORE | [TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning](../2013/IROS/2013_IROS_TrajOpt-A-Sequential-Convex-Optimization-Algorithm-for-Rob/01_overview.md) | 2013 / IROS | `UNREAD` | `CURATION_ONLY` |
| CORE | [PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) | 2020 / ICAPS | `UNREAD` | `CURATION_ONLY` |
| CORE | [Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints](../2013/T-RO/2013_T-RO_Dynamic-Whole-Body-Motion-Generation-under-Rigid-Contacts/01_overview.md) | 2013 / T-RO | `UNREAD` | `CURATION_ONLY` |
| CORE | [Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation](../2014/IJRR/2014_IJRR_Hierarchical-Quadratic-Programming-Fast-Online-Humanoid-Ro/01_overview.md) | 2014 / IJRR | `UNREAD` | `CURATION_ONLY` |
| CORE | [Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md) | 2018 / RA-L | `UNREAD` | `CURATION_ONLY` |

<!-- READING_QUEUE:END -->

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래 행은 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. 각 논문을 정독할 때 source location과 수치를 확인하고, 틀린 항목은 수정한 뒤 tracker를 갱신한다.

| Paper | Problem | State/model | Decision/action | Objective/constraints | Online rate/horizon | Robot/task | Evaluation | Main failure/assumption | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|
| [POMDP](../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md) | planning under partial observability | belief state over hidden robot/world state | finite-memory policy or belief-conditioned action | expected return under transition/observation uncertainty | decision horizon; exact settings UNVERIFIED | stochastic planning and embodied action | solution quality/complexity; exact protocol UNVERIFIED | belief approximation, partial observability and computational complexity | RP-2 recovery selector를 observation만이 아니라 belief/progress/budget state로 정의 |
| [Operational Space Control](../1987/IEEE-JRA/1987_IEEE-JRA_A-Unified-Approach-for-Motion-and-Force-Control-of-Robot-M/01_overview.md) | task-space motion/force control | rigid-body dynamics and task-space state | torque / task acceleration and wrench | dynamic consistency and task objectives | feedback-control timescale; exact rate UNVERIFIED | manipulator motion and contact | controller behavior; exact protocol UNVERIFIED | model/contact accuracy and singularities | learned policy 아래에 explicit task-space controller 유지 |
| [PRM](../1996/IEEE-T-RA/1996_IEEE-T-RA_Probabilistic-Roadmaps-for-Path-Planning-in-High-Dimension/01_overview.md) / [RRT](../1998/Technical-Report/1998_Technical-Report_Rapidly-Exploring-Random-Trees-A-New-Tool-for-Path-Plannin/01_overview.md) | high-dimensional feasible path search | configuration space and collision checker | sampled nodes/edges or expanding tree | collision-free reachability | offline multi-query / anytime single-query | motion planning | success, time, path quality; exact settings UNVERIFIED | sampling difficulty and narrow passages | global exploration과 local refinement를 분리 |
| [CHOMP](../2009/ICRA/2009_ICRA_CHOMP-Gradient-Optimization-Techniques-for-Efficient-Motio/01_overview.md) / [TrajOpt](../2013/IROS/2013_IROS_TrajOpt-A-Sequential-Convex-Optimization-Algorithm-for-Rob/01_overview.md) | smooth constrained trajectory optimization | discretized trajectory and geometry | waypoint trajectory | smoothness, collision and feasibility constraints | local iterative optimization | arm/mobile motion | solve time, cost, success; exact settings UNVERIFIED | initialization and local minima | differentiable cost와 hard constraint의 interface |
| [PDDLStream](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) | discrete task planning with continuous feasibility | symbolic facts plus black-box continuous samplers | action skeleton and sampled continuous values | symbolic goal and geometric feasibility | long-horizon planning; replanning rate UNVERIFIED | task-and-motion manipulation | planning success/time and domains; exact values UNVERIFIED | predicate/sampler coverage and expensive feasibility checks | learned perception/planner와 geometric sampler 연결 |
| [HQP](../2014/IJRR/2014_IJRR_Hierarchical-Quadratic-Programming-Fast-Online-Humanoid-Ro/01_overview.md) / [Whole-Body NMPC](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md) | prioritized whole-body control through contacts | whole-body dynamics, contacts and task hierarchy | joint torque/contact force/trajectory | hierarchy, dynamics and inequality constraints | online control / receding horizon | humanoid or legged whole-body motion | tracking, feasibility and runtime; exact setup UNVERIFIED | contact switching, model error and compute | learned skill을 constraint-aware whole-body layer로 감싸기 |


## Dependency and Evolution

아래 표는 읽기 순서를 위한 **개념적 계보**다. 논문이 후속 논문을 직접 인용했다는 뜻은 아니며, 직접 영향 관계는 정독 시 별도로 확인한다.

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| [Operational Space Formulation](../1987/IEEE-JRA/1987_IEEE-JRA_A-Unified-Approach-for-Motion-and-Force-Control-of-Robot-M/01_overview.md) → [Dynamic Whole-Body Motion Generation](../2013/T-RO/2013_T-RO_Dynamic-Whole-Body-Motion-Generation-under-Rigid-Contacts/01_overview.md) / [HQP](../2014/IJRR/2014_IJRR_Hierarchical-Quadratic-Programming-Fast-Online-Humanoid-Ro/01_overview.md) → [Whole-Body NMPC](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md) | task-space motion/force 관계에서 출발해 multi-contact dynamics, inequality constraint, task hierarchy와 predictive control로 확장된다. | contact switching과 model error가 있을 때 feasibility와 real-time rate가 함께 유지되는가 |
| [PRM](../1996/IEEE-T-RA/1996_IEEE-T-RA_Probabilistic-Roadmaps-for-Path-Planning-in-High-Dimension/01_overview.md) / [RRT](../1998/Technical-Report/1998_Technical-Report_Rapidly-Exploring-Random-Trees-A-New-Tool-for-Path-Plannin/01_overview.md) → [CHOMP](../2009/ICRA/2009_ICRA_CHOMP-Gradient-Optimization-Techniques-for-Efficient-Motio/01_overview.md) / [TrajOpt](../2013/IROS/2013_IROS_TrajOpt-A-Sequential-Convex-Optimization-Algorithm-for-Rob/01_overview.md) | feasible configuration-space exploration에서 smooth cost와 constraint를 직접 최적화하는 trajectory representation으로 이동한다. | 초기화, narrow passage, dynamic obstacle와 빠른 replanning의 trade-off |
| [POMDP](../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md) → PRM/RRT/trajectory optimization → [PDDLStream](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) → [SayPlan](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) / [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) | hidden state/belief를 전제로 하는 stochastic decision에서 continuous feasibility, symbolic planning, language-conditioned scene abstraction과 장기 계획으로 이어진다. | learned scene state와 symbolic predicate가 실제 기하 feasibility·failure recoverability 및 실행 후 상태를 얼마나 충실히 반영하는가 |
| CHOMP/TrajOpt → [Contact-Invariant Optimization](../2014/SIGGRAPH/2014_SIGGRAPH_Contact-Invariant-Optimization-for-Hand-Manipulation/01_overview.md) → [Global Contact-Rich Planning](../2023/T-RO/2023_T-RO_Global-Planning-for-Contact-Rich-Manipulation-via-Local-Sm/01_overview.md) / [Tight Convex Relaxations](../2024/RSS/2024_RSS_Towards-Tight-Convex-Relaxations-for-Contact-Rich-Manipula/01_overview.md) | collision 회피 중심 trajectory optimization에서 contact sequence와 nonsmooth dynamics를 결정변수로 다루는 방향으로 확장된다. | globality/relaxation quality가 실제 고차원 dexterous task에서도 계산 비용을 정당화하는가 |
| Operational-space force control → contact optimization → [ForceVLA2](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md) | 명시적 force/position objective가 language-conditioned learned policy의 action interface로 들어간다. | high-level semantic policy와 고주파 안정성 보장의 책임을 어디서 나눌 것인가 |

정독 시 sampling/optimization/control을 승패로 비교하지 않고, 각 component가 `global search`, `local refinement`, `constraint enforcement`, `feedback stabilization` 중 무엇을 맡는지 기록한다.

## Open Questions

- Learned policy와 optimization-based controller 사이의 가장 안정적인 interface는 무엇인가?
- Contact-rich task에서 빠른 replanning과 physical feasibility를 어떻게 동시에 보장하는가?
- Foundation policy가 embodiment-specific dynamics와 constraint를 얼마나 내부화해야 하는가?

## Research Gaps

- 통합 gap은 [G-01: VLA–contact 시간 척도](../research/RESEARCH_GAPS.md#g-01-vla와-접촉-제어의-시간-척도-불일치), [G-09: locomotion–manipulation coupling](../research/RESEARCH_GAPS.md#g-09-locomotion과-manipulation의-bandwidth와-objective-충돌)을 본다.
- 이 문서에는 정독 후 확인된 planner/controller별 가정과 반례만 추가하고, gap 설명과 아이디어는 복제하지 않는다.
