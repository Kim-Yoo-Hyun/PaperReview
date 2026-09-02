# Long-Term Robotics Reading Plan

- Updated: 2026-09-02 KST
- Source registry: [PAPER.md](../PAPER.md)
- Full tier index: [READING_TIERS.csv](./READING_TIERS.csv)
- Reading tracker: [READING_STATUS.csv](./READING_STATUS.csv)
- Intensive-reading set: **311 papers** (CORE 77 + NEXT 234)
- Research stance: Robotics is the main axis; 3D Vision is selected when it changes robot state estimation, planning, control, or evaluation.

## Default Reading Policy — Core First, Topic Independent

이 문서는 연구 주제와 무관하게 동일한 기본 순서를 제공한다. 먼저 공통 foundation과 canonical formulation을 읽고, 그 뒤에 연구 질문에 맞는 전문화 논문으로 분기한다.

`observation → state/world model → task & motion decision → policy/control → contact → feedback/failure recovery`

1. **CORE 77편:** 아래의 CORE 순서를 공통 spine으로 사용한다. 연구 주제가 VLA, manipulation, locomotion, 3D perception 중 무엇이든 CORE를 먼저 읽는다.
2. **NEXT 234편:** CORE를 기본적으로 통과한 뒤 연구 질문과 직접 연결되는 branch를 선택한다. NEXT 내부의 track 순서는 탐색용이며 CORE보다 앞설 수 없다.
3. **REFERENCE 397편:** CORE/NEXT를 읽는 중 필요한 정의·baseline·benchmark가 생길 때 on-demand로 조회한다.
4. **ARCHIVE 242편:** 현재 순서에는 넣지 않고 검색·역사 자료로 보존한다.

### 운영 원칙

- 주제별 시간 배분은 CORE를 건너뛰는 근거가 아니다. 연구 주제는 CORE 이후 NEXT의 branch 선택에만 사용한다.
- CORE의 track 제목은 taxonomy와 navigation을 위한 것이며, 논문을 골라 읽기 위한 선택지가 아니다. 기본적으로 1번부터 77번까지 진행한다.
- 특정 프로젝트에 필요한 논문을 먼저 읽어야 하면 canonical order를 수정하지 않고 별도 project overlay로 기록한다.

## Priority Criteria

읽기 순서와 tier를 정할 때는 아래 순서를 우선하며 PDF 보유 여부는 고려하지 않는다.

1. 공통 foundation 또는 후속 연구의 핵심 prerequisite인가
2. 문제 formulation, state/action/control interface를 바꾸었는가
3. 여러 robotics 문제에 재사용 가능한 개념적 수명이 있는가
4. 실제 robot의 closed-loop decision, contact, adaptation, deployment와 연결되는가
5. 기존 접근의 bottleneck과 실패 조건을 명확히 드러내는가
6. evaluation protocol, metric, baseline이 비교 가능하고 재검증 가능한가
7. 최신 흐름에서 기존 foundation의 한계를 검증하거나 확장하는가
8. 현재 연구에서 반박·재사용·확장할 수 있는 명시적 contribution이 있는가

## Tier Definitions

| Tier | Papers | Use |
|---|---:|---|
| CORE | 77 | 연구 주제와 무관한 공통 spine. 기본 순서대로 먼저 정독한다. |
| NEXT | 234 | CORE 이후 연구 질문에 따라 branch를 선택한다. |
| REFERENCE | 397 | 설계·실험 중 필요한 논문만 찾아 읽는다. 완독 목표가 아니다. |
| ARCHIVE | 242 | 현재 robotics-first 범위 밖의 검색·역사 자료. 삭제하지 않지만 읽기 큐에서 제외한다. |

CORE와 NEXT만 장기 정독 대상이다. REFERENCE와 ARCHIVE의 개별 분류는 CSV에서 검색·필터링한다.

## Completion Rule

논문 하나를 완료 처리하려면 overview만 읽는 것으로 끝내지 않고 다음 네 가지를 남긴다.

1. 문제 설정과 기존 접근 대비 핵심 가정
2. observation/state/action/control interface
3. 실험의 embodiment, task, data, metric, failure mode
4. 현재 연구에 재사용할 요소와 반박하거나 확장할 지점

## Canonical Execution Order

1. **CORE 1–77:** 아래 CORE 목록의 전 논문을 공통 foundation spine으로 읽는다. 각 track heading은 탐색용 분류이며, 주제에 따라 CORE 일부를 생략하지 않는다.
2. **NEXT 1–234:** CORE 완료 후에만 연구 질문에 맞는 전문화 branch를 고른다. 같은 branch 안에서는 목록 순서와 prerequisite를 우선한다.
3. **REFERENCE:** CORE/NEXT에서 생긴 구체적인 정의·baseline·benchmark 요구를 해결할 때만 추가한다.
4. **Project documents:** 특정 project의 detector, benchmark, implementation contract는 `research/projects/`에서 별도로 관리하며 canonical sequence를 바꾸지 않는다.

## Dependency-Based Reading Batches

각 batch는 달력 기반 일정이 아니라 prerequisite 단위다. 한 batch 전체를 끝내야 다음으로 갈 필요는 없지만, 같은 계보에서는 왼쪽 논문을 먼저 읽는다.

| Batch | Core question | Required spine | Branch after the spine | Exit artifact |
|---|---|---|---|---|
| A. Decision, mechanics, and feasibility | partial observability 아래 robot action의 belief, feasibility와 constraint는 어떻게 표현되는가? | POMDP → Operational Space Control → PRM/RRT → CHOMP/TrajOpt → PDDLStream | HQP / Whole-Body NMPC / contact optimization | belief/state·planner·controller별 decision variable과 guarantee 표 |
| B. Learning objectives and data | policy가 expert, reward, value와 logged data에서 무엇을 학습하는가? | DAgger/GPS/GAIL → TRPO/PPO/SAC → RoboMimic → IBC/IQL | CQL/MOPO/TD3+BC, RLBench, MimicGen/DROID | objective × data-support × interaction 비교 표 |
| C. Generative action policies | multimodal continuous action을 어떤 생성 과정으로 나타내는가? | DDPM / Flow Matching → Diffusion Policy → π0 | Diffusion-EDFs, Reactive Diffusion Policy, FAST | sampling step·chunk·latency·feedback 비교 표 |
| D. Generalist VLA and scaling | semantic prior와 heterogeneous robot data가 action으로 어떻게 연결되는가? | CLIP/CLIPort/PaLM-E → RT-1/RT-2 → Open X-Embodiment → Octo/OpenVLA | OpenVLA-OFT, π0/π0.5, memory/planning VLA | data × embodiment × action interface 비교 표 |
| E. Contact, safety, and recovery | 접촉 변화와 실패를 얼마나 빨리 감지하고 수정하는가? | contact/grasp foundations → tactile dynamics/control → CBF/Recovery RL → FAIL-Detect/SAFE | ForceVLA2, WorldGym/WMPO | perturbation·force·intervention·recovery protocol |
| F. Embodiment specialization | 동일 학습 원리가 legged, humanoid와 mobile manipulation에서 무엇이 달라지는가? | RMA → perceptive locomotion/parkour → HumanoidBench/OmniH2O/Mobile ALOHA | LangWBC, ASAP, HWC-Loco, VIRAL | dynamics/contact/whole-body coupling 비교 표 |
| G. Action-relevant 3D | 더 좋은 geometry가 실제 robot decision을 언제 개선하는가? | PointNet → DROID-SLAM/3DGS → ConceptFusion/RVT/DUSt3R | VGGT/SUGAR, active 3D, PointVLA/Any3D-VLA | representation 고정 ablation과 downstream metric |

Batch exit artifact를 채우기 전에는 해당 계보를 `SYNTHESIZED`로 올리지 않는다. Batch는 CORE-first 기본 순서를 보완하는 비교 단위이며, 연구 주제가 다르다는 이유로 CORE보다 앞세우지 않는다.

## Research Lenses Across Tracks

- Robot learning을 behavior cloning으로 한정하지 않고 offline-to-online improvement, reward/value learning, failure/suboptimal data 활용까지 본다.
- Contact를 예외가 아니라 state, dynamics, constraint, feedback signal로 다룬다.
- Locomotion과 manipulation의 결합, balance와 task interaction의 공동 제어를 본다.
- Safety를 constraint, uncertainty, monitoring, intervention, recovery의 여러 시간 척도로 나눈다.
- Geometry가 learned policy 안에서 equivariance, 3D state, spatial memory, collision/contact structure로 어떤 역할을 하는지 본다.
- Architecture보다 data coverage, quality, curation, embodiment diversity와 scaling law를 함께 비교한다.
- Generative action model의 inference latency와 실제 closed-loop control frequency를 확인한다.
- Tabletop success rate를 넘어 long horizon, real-world disturbances, sensor degradation, compromised contact, recovery를 평가한다.

## CORE — 77 papers

### Planning, control, and whole-body foundations — 16

1. [A New Approach to Linear Filtering and Prediction Problems](../1960/Journal-of-Basic-Enginee/1960_Journal-of-Basic-Enginee_A-New-Approach-to-Linear-Filtering-and-Prediction-Problems/01_overview.md) — 1960 Journal of Basic Engineering.
2. [A Formal Basis for the Heuristic Determination of Minimum Cost Paths](../1968/IEEE-Transactions-on-Sys/1968_IEEE-Transactions-on-Sys_A-Formal-Basis-for-the-Heuristic-Determination-of-Minimum/01_overview.md) — 1968 IEEE Transactions on Systems Science and Cybernetics.
3. [Planning and Acting in Partially Observable Stochastic Domains](../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md) — 1998 Artificial Intelligence.
4. [A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation](../1987/IEEE-JRA/1987_IEEE-JRA_A-Unified-Approach-for-Motion-and-Force-Control-of-Robot-M/01_overview.md) — 1987 IEEE JRA.
5. [Hybrid Position/Force Control of Manipulators](../1981/Journal-of-Dynamic-Syste/1981_Journal-of-Dynamic-Syste_Hybrid-Position-Force-Control-of-Manipulators/01_overview.md) — 1981 Journal of Dynamic Systems, Measurement, and Control.
6. [Impedance Control: An Approach to Manipulation: Part I—Theory](../1985/Journal-of-Dynamic-Syste/1985_Journal-of-Dynamic-Syste_Impedance-Control-An-Approach-to-Manipulation-Part-ITheory/01_overview.md) — 1985 Journal of Dynamic Systems, Measurement, and Control.
7. [Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces](../1996/IEEE-T-RA/1996_IEEE-T-RA_Probabilistic-Roadmaps-for-Path-Planning-in-High-Dimension/01_overview.md) — 1996 IEEE T-RA.
8. [Rapidly-Exploring Random Trees: A New Tool for Path Planning](../1998/Technical-Report/1998_Technical-Report_Rapidly-Exploring-Random-Trees-A-New-Tool-for-Path-Plannin/01_overview.md) — 1998 Technical Report.
9. [CHOMP: Gradient Optimization Techniques for Efficient Motion Planning](../2009/ICRA/2009_ICRA_CHOMP-Gradient-Optimization-Techniques-for-Efficient-Motio/01_overview.md) — 2009 ICRA.
10. [TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning](../2013/IROS/2013_IROS_TrajOpt-A-Sequential-Convex-Optimization-Algorithm-for-Rob/01_overview.md) — 2013 IROS.
11. [MuJoCo: A Physics Engine for Model-Based Control](../2012/IROS/2012_IROS_MuJoCo-A-Physics-Engine-for-Model-Based-Control/01_overview.md) — 2012 IROS.
12. [Information Theoretic MPC for Model-Based Reinforcement Learning](../2017/ICRA/2017_ICRA_Information-Theoretic-MPC-for-Model-Based-Reinforcement-Le/01_overview.md) — 2017 ICRA.
13. [PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) — 2020 ICAPS.
14. [Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints](../2013/T-RO/2013_T-RO_Dynamic-Whole-Body-Motion-Generation-under-Rigid-Contacts/01_overview.md) — 2013 T-RO.
15. [Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation](../2014/IJRR/2014_IJRR_Hierarchical-Quadratic-Programming-Fast-Online-Humanoid-Ro/01_overview.md) — 2014 IJRR.
16. [Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md) — 2018 RA-L.

### RL, IL, and policy learning foundations — 20

17. [Learning to Predict by the Methods of Temporal Differences](../1988/Machine-Learning/1988_Machine-Learning_Learning-to-Predict-by-the-Methods-of-Temporal-Differences/01_overview.md) — 1988 Machine Learning.
18. [Q-Learning](../1992/Machine-Learning/1992_Machine-Learning_Q-Learning/01_overview.md) — 1992 Machine Learning.
19. [Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning](../1992/Machine-Learning/1992_Machine-Learning_Simple-Statistical-Gradient-Following-Algorithms-for-Conne/01_overview.md) — 1992 Machine Learning.
20. [Policy Gradient Methods for Reinforcement Learning with Function Approximation](../1999/NeurIPS/1999_NeurIPS_Policy-Gradient-Methods-for-Reinforcement-Learning-with-Fu/01_overview.md) — 1999 NeurIPS.
21. [PILCO: A Model-Based and Data-Efficient Approach to Policy Search](../2011/ICML/2011_ICML_PILCO-A-Model-Based-and-Data-Efficient-Approach-to-Policy/01_overview.md) — 2011 ICML.
22. [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) — 2011 AISTATS.
23. [Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics](../2016/JMLR/2016_JMLR_Learning-Neural-Network-Policies-with-Guided-Policy-Search/01_overview.md) — 2016 JMLR.
24. [Generative Adversarial Imitation Learning](../2016/NeurIPS/2016_NeurIPS_Generative-Adversarial-Imitation-Learning/01_overview.md) — 2016 NeurIPS.
25. [Trust Region Policy Optimization](../2015/ICML/2015_ICML_Trust-Region-Policy-Optimization/01_overview.md) — 2015 ICML.
26. [Proximal Policy Optimization Algorithms](../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) — 2017 arXiv.
27. [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](../2018/ICML/2018_ICML_Soft-Actor-Critic-Off-Policy-Maximum-Entropy-Deep-Reinforc/01_overview.md) — 2018 ICML.
28. [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](../2017/IROS/2017_IROS_Domain-Randomization-for-Transferring-Deep-Neural-Networks/01_overview.md) — 2017 IROS.
29. [What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md) — 2021 CoRL.
30. [Implicit Behavioral Cloning](../2022/CoRL/2022_CoRL_Implicit-Behavioral-Cloning/01_overview.md) — 2022 CoRL.
31. [Offline Reinforcement Learning with Implicit Q-Learning](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md) — 2022 ICLR.
32. [Decision Transformer: Reinforcement Learning via Sequence Modeling](../2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/01_overview.md) — 2021 NeurIPS.
33. [Denoising Diffusion Probabilistic Models](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) — 2020 NeurIPS.
34. [Flow Matching for Generative Modeling](../2023/ICLR/2023_ICLR_Flow-Matching-for-Generative-Modeling/01_overview.md) — 2023 ICLR.
35. [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](../2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md) — 2023 RSS.
36. [Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions](../2024/CoRL/2024_CoRL_Q-Transformer-Scalable-Offline-Reinforcement-Learning-via/01_overview.md) — 2024 CoRL.

### Manipulation, contact, tactile, and dexterity — 10

37. [Planning Optimal Grasps](../1992/ICRA/1992_ICRA_Planning-Optimal-Grasps/01_overview.md) — 1992 ICRA.
38. [GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force](../2017/Sensors/2017_Sensors_GelSight-High-Resolution-Robot-Tactile-Sensors-for-Estimat/01_overview.md) — 2017 Sensors.
39. [Contact-Invariant Optimization for Hand Manipulation](../2014/SIGGRAPH/2014_SIGGRAPH_Contact-Invariant-Optimization-for-Hand-Manipulation/01_overview.md) — 2014 SIGGRAPH.
40. [GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping](../2020/CVPR/2020_CVPR_GraspNet-1Billion-A-Large-Scale-Benchmark-for-General-Obje/01_overview.md) — 2020 CVPR.
41. [Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes](../2021/ICRA/2021_ICRA_Contact-GraspNet-Efficient-6-DoF-Grasp-Generation-in-Clutt/01_overview.md) — 2021 ICRA.
42. [Factory: Fast Contact for Robotic Assembly](../2022/RSS/2022_RSS_Factory-Fast-Contact-for-Robotic-Assembly/01_overview.md) — 2022 RSS.
43. [Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models](../2023/T-RO/2023_T-RO_Global-Planning-for-Contact-Rich-Manipulation-via-Local-Sm/01_overview.md) — 2023 T-RO.
44. [Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control](../2024/RSS/2024_RSS_Tactile-Driven-Non-Prehensile-Object-Manipulation-via-Extr/01_overview.md) — 2024 RSS.
45. [RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing](../2024/RSS/2024_RSS_RoboPack-Learning-Tactile-Informed-Dynamics-Models-for-Den/01_overview.md) — 2024 RSS.
46. [DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References](../2025/ICLR/2025_ICLR_DexTrack-Towards-Generalizable-Neural-Tracking-Control-for/01_overview.md) — 2025 ICLR.

### VLA and generalist robot policies — 11

47. [Learning Transferable Visual Models From Natural Language Supervision](../2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/01_overview.md) — 2021 ICML.
48. [CLIPort: What and Where Pathways for Robotic Manipulation](../2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md) — 2021 CoRL.
49. [PaLM-E: An Embodied Multimodal Language Model](../2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/01_overview.md) — 2023 ICML.
50. [RT-1: Robotics Transformer for Real-World Control at Scale](../2022/arxiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md) — 2022 arXiv.
51. [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](../2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md) — 2023 CoRL.
52. [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](../2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/01_overview.md) — 2023 CoRL.
53. [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md) — 2024 ICRA.
54. [Octo: An Open-Source Generalist Robot Policy](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md) — 2024 RSS.
55. [OpenVLA: An Open-Source Vision-Language-Action Model](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) — 2024 CoRL.
56. [π0: A Vision-Language-Action Flow Model for General Robot Control](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) — 2025 RSS.
57. [π0.5: a Vision-Language-Action Model with Open-World Generalization](../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md) — 2025 CoRL.

### Safety and robot world models — 5

58. [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) — 2018 NeurIPS Workshop.
59. [DayDreamer: World Models for Physical Robot Learning](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) — 2022 CoRL.
60. [TD-MPC2: Scalable, Robust World Models for Continuous Control](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) — 2024 ICLR.
61. [Control Barrier Function Based Quadratic Programs for Safety Critical Systems](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) — 2017 TAC.
62. [Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) — 2020 RA-L.

### Locomotion, mobile manipulation, and humanoid systems — 8

63. [Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point](../2003/ICRA/2003_ICRA_Biped-Walking-Pattern-Generation-by-using-Preview-Control/01_overview.md) — 2003 ICRA.
64. [AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control](../2021/ACM-Transactions-on-Grap/2021_ACM-Transactions-on-Grap_AMP-Adversarial-Motion-Priors-for-Stylized-Physics-Based-C/01_overview.md) — 2021 ACM Transactions on Graphics.
65. [RMA: Rapid Motor Adaptation for Legged Robots](../2021/RSS/2021_RSS_RMA-Rapid-Motor-Adaptation-for-Legged-Robots/01_overview.md) — 2021 RSS.
66. [Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild](../2022/Science-Robotics/2022_Science-Robotics_Learning-Robust-Perceptive-Locomotion-for-Quadrupedal-Robo/01_overview.md) — 2022 Science Robotics.
67. [ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots](../2024/Science-Robotics/2024_Science-Robotics_ANYmal-Parkour-Learning-Agile-Navigation-for-Quadrupedal-R/01_overview.md) — 2024 Science Robotics.
68. [HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation](../2024/RSS/2024_RSS_HumanoidBench-Simulated-Humanoid-Benchmark-for-Whole-Body/01_overview.md) — 2024 RSS.
69. [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md) — 2024 CoRL.
70. [Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md) — 2024 CoRL.

### Robotics-enabling 3D perception — 7

71. [A Method for Registration of 3-D Shapes](../1992/IEEE-Transactions-on-Pat/1992_IEEE-Transactions-on-Pat_A-Method-for-Registration-of-3-D-Shapes/01_overview.md) — 1992 IEEE Transactions on Pattern Analysis and Machine Intelligence.
72. [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](../2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) — 2017 CVPR.
73. [DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) — 2021 NeurIPS.
74. [3D Gaussian Splatting for Real-Time Radiance Field Rendering](../2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md) — 2023 SIGGRAPH.
75. [ConceptFusion: Open-set Multimodal 3D Mapping](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) — 2023 RSS.
76. [RVT: Robotic View Transformer for 3D Object Manipulation](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) — 2023 CoRL.
77. [DUSt3R: Geometric 3D Vision Made Easy](../2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md) — 2024 CVPR.

CORE 77편을 기본적으로 모두 읽은 뒤에 NEXT branch를 선택한다. 아래 NEXT track은 주제별 선택지이지 CORE를 대체하는 우선순위가 아니다.

## NEXT — 234 papers

### Planning, control, simulation, and TAMP extensions — 13

1. [Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning](../2015/IJCAI/2015_IJCAI_Logic-Geometric-Programming-An-Optimization-Based-Approach/01_overview.md) — 2015 IJCAI.
2. [FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning](../2018/The-International-Journa/2018_The-International-Journa_FFRob-Leveraging-Symbolic-Planning-for-Efficient-Task-and/01_overview.md) — 2018 The International Journal of Robotics Research.
3. [Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation](../2025/RSS/2025_RSS_Kinodynamic-Trajectory-Following-with-STELA-Simultaneous-T/01_overview.md) — 2025 RSS.
4. [Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation](../2025/AAAI/2025_AAAI_Instruction-Augmented-Long-Horizon-Planning-Embedding-Grou/01_overview.md) — 2025 AAAI.
5. [Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images](../2025/AAAI/2025_AAAI_Neural-Assembler-Learning-to-Generate-Fine-Grained-Robotic/01_overview.md) — 2025 AAAI.
6. [Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning](../2026/ICRA/2026_ICRA_Open-Vocabulary-Spatio-Temporal-Scene-Graph-for-Robot-Perc/01_overview.md) — 2026 ICRA.
7. [Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation](../2024/CVPR/2024_CVPR_Lookahead-Exploration-with-Neural-Radiance-Representation/01_overview.md) — 2024 CVPR.
8. [FOCI: Trajectory Optimization on Gaussian Splats](../2025/IROS/2025_IROS_FOCI-Trajectory-Optimization-on-Gaussian-Splats/01_overview.md) — 2025 IROS.
9. [Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness](../2024/RSS/2024_RSS_Partially-Observable-Task-and-Motion-Planning-with-Uncerta/01_overview.md) — 2024 RSS.
10. [Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control](../2024/RSS/2024_RSS_Parallel-and-Proximal-Linear-Quadratic-Methods-for-Real-Ti/01_overview.md) — 2024 RSS.
11. [Differentiable Robust Model Predictive Control](../2024/RSS/2024_RSS_Differentiable-Robust-Model-Predictive-Control/01_overview.md) — 2024 RSS.
12. [Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective](../2024/RSS/2024_RSS_Linear-time-Differential-Inverse-Kinematics-an-Augmented-L/01_overview.md) — 2024 RSS.
13. [NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](../2024/ICRA/2024_ICRA_NoMaD-Goal-Masked-Diffusion-Policies-for-Navigation-and-Ex/01_overview.md) — 2024 ICRA.

### RL, IL, offline learning, and robot data — 45

14. [Behavior Transformers: Cloning k modes with one stone](../2022/NeurIPS/2022_NeurIPS_Behavior-Transformers-Cloning-k-modes-with-one-stone/01_overview.md) — 2022 NeurIPS.
15. [R3M: A Universal Visual Representation for Robot Manipulation](../2022/CoRL/2022_CoRL_R3M-A-Universal-Visual-Representation-for-Robot-Manipulati/01_overview.md) — 2022 CoRL.
16. [Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?](../2023/arXiv/2023_arXiv_Where-are-we-in-the-search-for-an-Artificial-Visual-Cortex/01_overview.md) — 2023 arXiv.
17. [Maximum a Posteriori Policy Optimisation](../2018/ICLR/2018_ICLR_Maximum-a-Posteriori-Policy-Optimisation/01_overview.md) — 2018 ICLR.
18. [MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale](../2021/arXiv/2021_arXiv_MT-Opt-Continuous-Multi-Task-Robotic-Reinforcement-Learnin/01_overview.md) — 2021 arXiv.
19. [Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning](../2021/NeurIPS-Datasets-and-Ben/2021_NeurIPS-Datasets-and-Ben_Isaac-Gym-High-Performance-GPU-Based-Physics-Simulation-Fo/01_overview.md) — 2021 NeurIPS Datasets and Benchmarks.
20. [Eureka: Human-Level Reward Design via Coding Large Language Models](../2024/ICLR/2024_ICLR_Eureka-Human-Level-Reward-Design-via-Coding-Large-Language/01_overview.md) — 2024 ICLR.
21. [DrEureka: Language Model Guided Sim-To-Real Transfer](../2024/Robotics-Science-and-Sys/2024_Robotics-Science-and-Sys_DrEureka-Language-Model-Guided-Sim-To-Real-Transfer/01_overview.md) — 2024 Robotics: Science and Systems.
22. [Continuous Control with Deep Reinforcement Learning](../2016/ICLR/2016_ICLR_Continuous-Control-with-Deep-Reinforcement-Learning/01_overview.md) — 2016 ICLR.
23. [Addressing Function Approximation Error in Actor-Critic Methods](../2018/ICML/2018_ICML_Addressing-Function-Approximation-Error-in-Actor-Critic-Me/01_overview.md) — 2018 ICML.
24. [Hindsight Experience Replay](../2017/NeurIPS/2017_NeurIPS_Hindsight-Experience-Replay/01_overview.md) — 2017 NeurIPS.
25. [Constrained Policy Optimization](../2017/ICML/2017_ICML_Constrained-Policy-Optimization/01_overview.md) — 2017 ICML.
26. [Conservative Q-Learning for Offline Reinforcement Learning](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md) — 2020 NeurIPS.
27. [MOPO: Model-based Offline Policy Optimization](../2020/NeurIPS/2020_NeurIPS_MOPO-Model-based-Offline-Policy-Optimization/01_overview.md) — 2020 NeurIPS.
28. [A Minimalist Approach to Offline Reinforcement Learning](../2021/NeurIPS/2021_NeurIPS_A-Minimalist-Approach-to-Offline-Reinforcement-Learning/01_overview.md) — 2021 NeurIPS.
29. [Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations](../2018/RSS/2018_RSS_Learning-Complex-Dexterous-Manipulation-with-Deep-Reinforc/01_overview.md) — 2018 RSS.
30. [Learning Latent Plans from Play](../2020/CoRL/2020_CoRL_Learning-Latent-Plans-from-Play/01_overview.md) — 2020 CoRL.
31. [Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning](../2020/CoRL/2020_CoRL_Relay-Policy-Learning-Solving-Long-Horizon-Tasks-via-Imita/01_overview.md) — 2020 CoRL.
32. [RLBench: The Robot Learning Benchmark & Learning Environment](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) — 2020 RA-L.
33. [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../2023/CoRL/2023_CoRL_MimicGen-A-Data-Generation-System-for-Scalable-Robot-Learn/01_overview.md) — 2023 CoRL.
34. [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md) — 2024 RSS.
35. [Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](../2024/RSS/2024_RSS_Universal-Manipulation-Interface-In-The-Wild-Robot-Teachin/01_overview.md) — 2024 RSS.
36. [SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning](../2024/ICRA/2024_ICRA_SERL-A-Software-Suite-for-Sample-Efficient-Robotic-Reinfor/01_overview.md) — 2024 ICRA.
37. [Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning](../2024/ICRA/2024_ICRA_Robot-Fine-Tuning-Made-Easy-Pre-Training-Rewards-and-Polic/01_overview.md) — 2024 ICRA.
38. [RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning](../2025/RSS/2025_RSS_RLDG-Robotic-Generalist-Policy-Distillation-via-Reinforcem/01_overview.md) — 2025 RSS.
39. [Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3](../2025/RSS/2025_RSS_Demonstrating-GPU-Parallelized-Robot-Simulation-and-Render/01_overview.md) — 2025 RSS.
40. [RoboVerse: A Unified Platform, Benchmark and Dataset for Scalable and Generalizable Robot Learning](../2025/RSS/2025_RSS_RoboVerse-A-Unified-Platform-Benchmark-and-Dataset-for-Sca/01_overview.md) — 2025 RSS.
41. [DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies](../2025/RSS/2025_RSS_DexWild-Dexterous-Human-Interactions-for-In-the-Wild-Robot/01_overview.md) — 2025 RSS.
42. [Dex1B: Learning with 1B Demonstrations for Dexterous Manipulation](../2025/RSS/2025_RSS_Dex1B-Learning-with-1B-Demonstrations-for-Dexterous-Manipu/01_overview.md) — 2025 RSS.
43. [Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation](../2025/RSS/2025_RSS_Sim-and-Real-Co-Training-A-Simple-Recipe-for-Vision-Based/01_overview.md) — 2025 RSS.
44. [Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](../2025/RSS/2025_RSS_Novel-Demonstration-Generation-with-Gaussian-Splatting-Ena/01_overview.md) — 2025 RSS.
45. [You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations](../2025/RSS/2025_RSS_You-Only-Teach-Once-Learn-One-Shot-Bimanual-Robotic-Manipu/01_overview.md) — 2025 RSS.
46. [RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation](../2025/RSS/2025_RSS_RoboMIND-Benchmark-on-Multi-embodiment-Intelligence-Normat/01_overview.md) — 2025 RSS.
47. [Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization](../2025/RSS/2025_RSS_Bridging-Perception-and-Action-Spatially-Grounded-Mid-Leve/01_overview.md) — 2025 RSS.
48. [DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning](../2025/RSS/2025_RSS_DemoGen-Synthetic-Demonstration-Generation-for-Data-Effici/01_overview.md) — 2025 RSS.
49. [AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems](../2025/IROS/2025_IROS_AgiBot-World-Colosseo-A-Large-scale-Manipulation-Platform/01_overview.md) — 2025 IROS.
50. [Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](../2024/arXiv/2024_arXiv_Precise-and-Dexterous-Robotic-Manipulation-via-Human-in-th/01_overview.md) — 2024 arXiv.
51. [MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation](../2026/AAAI/2026_AAAI_MP1-MeanFlow-Tames-Policy-Learning-in-1-step-for-Robotic-M/01_overview.md) — 2026 AAAI.
52. [Efficient Online Reinforcement Learning with Offline Data](../2023/ICML/2023_ICML_Efficient-Online-Reinforcement-Learning-with-Offline-Data/01_overview.md) — 2023 ICML.
53. [Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning](../2024/RSS/2024_RSS_Diffusion-Meets-DAgger-Supercharging-Eye-in-hand-Imitation/01_overview.md) — 2024 RSS.
54. [Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation](../2024/RSS/2024_RSS_Consistency-Policy-Accelerated-Visuomotor-Policies-via-Con/01_overview.md) — 2024 RSS.
55. [Any-point Trajectory Modeling for Policy Learning](../2024/RSS/2024_RSS_Any-point-Trajectory-Modeling-for-Policy-Learning/01_overview.md) — 2024 RSS.
56. [Evaluating Real-World Robot Manipulation Policies in Simulation](../2024/CoRL/2024_CoRL_Evaluating-Real-World-Robot-Manipulation-Policies-in-Simul/01_overview.md) — 2024 CoRL.
57. [Benchmarking Knowledge Transfer for Lifelong Robot Learning](../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md) — 2023 NeurIPS.
58. [MimicPlay: Long-Horizon Imitation Learning by Watching Human Play](../2023/CoRL/2023_CoRL_MimicPlay-Long-Horizon-Imitation-Learning-by-Watching-Huma/01_overview.md) — 2023 CoRL.

### Contact-rich, deformable, force, and dexterous manipulation — 45

59. [Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation](../2018/CoRL/2018_CoRL_Dense-Object-Nets-Learning-Dense-Visual-Object-Descriptors/01_overview.md) — 2018 CoRL.
60. [UMPNet: Universal Manipulation Policy Network for Articulated Objects](../2022/RA-L/2022_RA-L_UMPNet-Universal-Manipulation-Policy-Network-for-Articulat/01_overview.md) — 2022 RA-L.
61. [Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation](../2023/CoRL/2023_CoRL_Distilled-Feature-Fields-Enable-Few-Shot-Language-Guided-M/01_overview.md) — 2023 CoRL.
62. [GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping](../2024/RA-L/2024_RA-L_GaussianGrasper-3D-Language-Gaussian-Splatting-for-Open-vo/01_overview.md) — 2024 RA-L.
63. [ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation](../2024/ECCV/2024_ECCV_ManiGaussian-Dynamic-Gaussian-Splatting-for-Multi-task-Rob/01_overview.md) — 2024 ECCV.
64. [Gaussian Splatting Visual MPC for Granular Media Manipulation](../2025/ICRA/2025_ICRA_Gaussian-Splatting-Visual-MPC-for-Granular-Media-Manipulat/01_overview.md) — 2025 ICRA.
65. [Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](../2025/ICRA/2025_ICRA_Persistent-Object-Gaussian-Splat-POGS-for-Tracking-Human-a/01_overview.md) — 2025 ICRA.
66. [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](../2020/IEEE-Robotics-and-Automa/2020_IEEE-Robotics-and-Automa_DIGIT-A-Novel-Design-for-a-Low-Cost-Compact-High-Resolutio/01_overview.md) — 2020 IEEE Robotics and Automation Letters.
67. [DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality](../2023/ICRA/2023_ICRA_DeXtreme-Transfer-of-Agile-In-hand-Manipulation-from-Simul/01_overview.md) — 2023 ICRA.
68. [Control-Limited Differential Dynamic Programming](../2014/ICRA/2014_ICRA_Control-Limited-Differential-Dynamic-Programming/01_overview.md) — 2014 ICRA.
69. [In-Hand Manipulation via Motion Cones](../2019/RSS/2019_RSS_In-Hand-Manipulation-via-Motion-Cones/01_overview.md) — 2019 RSS.
70. [Towards Tight Convex Relaxations for Contact-Rich Manipulation](../2024/RSS/2024_RSS_Towards-Tight-Convex-Relaxations-for-Contact-Rich-Manipula/01_overview.md) — 2024 RSS.
71. [Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization](../2025/RSS/2025_RSS_Physics-Driven-Data-Generation-for-Contact-Rich-Manipulati/01_overview.md) — 2025 RSS.
72. [Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation](../2025/RSS/2025_RSS_Complementarity-Free-Multi-Contact-Modeling-and-Optimizati/01_overview.md) — 2025 RSS.
73. [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](../2020/CoRL/2020_CoRL_SoftGym-Benchmarking-Deep-Reinforcement-Learning-for-Defor/01_overview.md) — 2020 CoRL.
74. [DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools](../2022/ICLR/2022_ICLR_DiffSkill-Skill-Abstraction-from-Differentiable-Physics-fo/01_overview.md) — 2022 ICLR.
75. [Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation](../2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md) — 2021 CoRL.
76. [Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation](../2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md) — 2024 CVPR.
77. [IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality](../2023/RSS/2023_RSS_IndustReal-Transferring-Contact-Rich-Assembly-Tasks-from-S/01_overview.md) — 2023 RSS.
78. [Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](../2024/CVPR/2024_CVPR_Binding-Touch-to-Everything-Learning-Unified-Multimodal-Ta/01_overview.md) — 2024 CVPR.
79. [DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) — 2025 ICLR.
80. [G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation](../2025/CVPR/2025_CVPR_G3Flow-Generative-3D-Semantic-Flow-for-Pose-aware-and-Gene/01_overview.md) — 2025 CVPR.
81. [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md) — 2025 RSS.
82. [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md) — 2026 CVPR.
83. [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md) — 2026 CVPR.
84. [Dexterous World Models](../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) — 2026 CVPR.
85. [EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation](../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) — 2026 ICLR.
86. [Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language](../2026/ICML/2026_ICML_Tabero-Learning-Gentle-Manipulation-with-Closed-Loop-Force/01_overview.md) — 2026 ICML.
87. [TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment](../2026/RSS/2026_RSS_TactAlign-Human-to-Robot-Policy-Transfer-via-Tactile-Align/01_overview.md) — 2026 RSS.
88. [DexterityGen: Foundation Controller for Unprecedented Dexterity](../2026/RSS/2026_RSS_DexterityGen-Foundation-Controller-for-Unprecedented-Dexte/01_overview.md) — 2026 RSS.
89. [V-HOP: Visuo-Haptic 6D Object Pose Tracking](../2025/RSS/2025_RSS_V-HOP-Visuo-Haptic-6D-Object-Pose-Tracking/01_overview.md) — 2025 RSS.
90. [PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands](../2025/RSS/2025_RSS_PP-Tac-Paper-Picking-Using-Omnidirectional-Tactile-Feedbac/01_overview.md) — 2025 RSS.
91. [GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty](../2025/RSS/2025_RSS_GeoDEx-A-Unified-Geometric-Framework-for-Tactile-Dexterous/01_overview.md) — 2025 RSS.
92. [Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly](../2025/RSS/2025_RSS_Demonstrating-REASSEMBLE-A-Multimodal-Dataset-for-Contact/01_overview.md) — 2025 RSS.
93. [Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation](../2025/RSS/2025_RSS_Robust-Peg-in-Hole-Assembly-under-Uncertainties-via-Compli/01_overview.md) — 2025 RSS.
94. [FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning](../2025/RSS/2025_RSS_FACTR-Force-Attending-Curriculum-Training-for-Contact-Rich/01_overview.md) — 2025 RSS.
95. [CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World](../2025/RSS/2025_RSS_CordViP-Correspondence-based-Visuomotor-Policy-for-Dextero/01_overview.md) — 2025 RSS.
96. [FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation](../2025/AAAI/2025_AAAI_FlowPolicy-Enabling-Fast-and-Robust-3D-Flow-Based-Policy-v/01_overview.md) — 2025 AAAI.
97. [Sparsh: Self-supervised touch representations for vision-based tactile sensing](../2024/CoRL/2024_CoRL_Sparsh-Self-supervised-touch-representations-for-vision-ba/01_overview.md) — 2024 CoRL.
98. [Octopi: Object Property Reasoning with Large Tactile-Language Models](../2024/RSS/2024_RSS_Octopi-Object-Property-Reasoning-with-Large-Tactile-Langua/01_overview.md) — 2024 RSS.
99. [OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation](../2024/CoRL/2024_CoRL_OPEN-TEACH-A-Versatile-Teleoperation-System-for-Robotic-Ma/01_overview.md) — 2024 CoRL.
100. [FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation](../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md) — 2023 RSS.
101. [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](../2023/RSS/2023_RSS_Learning-Fine-Grained-Bimanual-Manipulation-with-Low-Cost/01_overview.md) — 2023 RSS.
102. [Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching](../2024/CoRL/2024_CoRL_Learning-Robotic-Manipulation-Policies-from-Point-Clouds-w/01_overview.md) — 2024 CoRL.
103. [3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](../2024/RSS/2024_RSS_3D-Diffusion-Policy-Generalizable-Visuomotor-Policy-Learni/01_overview.md) — 2024 RSS.

### VLA, cross-embodiment, and long-horizon planning — 56

104. [A Generalist Agent](../2022/arXiv/2022_arXiv_A-Generalist-Agent/01_overview.md) — 2022 arXiv.
105. [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](../2022/RA-L/2022_RA-L_CALVIN-A-Benchmark-for-Language-Conditioned-Policy-Learnin/01_overview.md) — 2022 RA-L.
106. [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](../2024/arXiv/2024_arXiv_AutoRT-Embodied-Foundation-Models-for-Large-Scale-Orchestr/01_overview.md) — 2024 arXiv.
107. [RT-H: Action Hierarchies Using Language](../2024/Robotics-Science-and-Sys/2024_Robotics-Science-and-Sys_RT-H-Action-Hierarchies-Using-Language/01_overview.md) — 2024 Robotics: Science and Systems.
108. [Gemini Robotics: Bringing AI into the Physical World](../2025/arXiv/2025_arXiv_Gemini-Robotics-Bringing-AI-into-the-Physical-World/01_overview.md) — 2025 arXiv.
109. [NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots](../2025/arXiv/2025_arXiv_NVIDIA-Isaac-GR00T-N1-An-Open-Foundation-Model-for-Humanoi/01_overview.md) — 2025 arXiv.
110. [BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning](../2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/01_overview.md) — 2022 CoRL.
111. [Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation](../2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md) — 2023 CoRL.
112. [VIMA: General Robot Manipulation with Multimodal Prompts](../2023/ICML/2023_ICML_VIMA-General-Robot-Manipulation-with-Multimodal-Prompts/01_overview.md) — 2023 ICML.
113. [Inner Monologue: Embodied Reasoning through Planning with Language Models](../2022/CoRL/2022_CoRL_Inner-Monologue-Embodied-Reasoning-through-Planning-with-L/01_overview.md) — 2022 CoRL.
114. [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) — 2023 CoRL.
115. [XSkill: Cross Embodiment Skill Discovery](../2023/CoRL/2023_CoRL_XSkill-Cross-Embodiment-Skill-Discovery/01_overview.md) — 2023 CoRL.
116. [Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](../2024/NeurIPS/2024_NeurIPS_Scaling-Proprioceptive-Visual-Learning-with-Heterogeneous/01_overview.md) — 2024 NeurIPS.
117. [FAST: Efficient Action Tokenization for Vision-Language-Action Models](../2025/RSS/2025_RSS_FAST-Efficient-Action-Tokenization-for-Vision-Language-Act/01_overview.md) — 2025 RSS.
118. [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](../2025/RSS/2025_RSS_Fine-Tuning-Vision-Language-Action-Models-Optimizing-Speed/01_overview.md) — 2025 RSS.
119. [AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md) — 2026 CVPR.
120. [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](../2026/CVPR/2026_CVPR_PALM-Progress-Aware-Policy-Learning-via-Affordance-Reasoni/01_overview.md) — 2026 CVPR.
121. [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) — 2026 CVPR.
122. [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) — 2026 ICML.
123. [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](../2026/CVPR/2026_CVPR_Counterfactual-VLA-Self-Reflective-Vision-Language-Action/01_overview.md) — 2026 CVPR.
124. [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](../2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/01_overview.md) — 2026 ICML.
125. [MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) — 2026 ICLR.
126. [AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention](../2026/CVPR/2026_CVPR_AVA-VLA-Improving-Vision-Language-Action-Models-with-Activ/01_overview.md) — 2026 CVPR.
127. [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md) — 2026 ICML.
128. [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models](../2025/RSS/2025_RSS_SpatialVLA-Exploring-Spatial-Representations-for-Visual-La/01_overview.md) — 2025 RSS.
129. [From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors](../2026/ICLR/2026_ICLR_From-Spatial-to-Actions-Grounding-Vision-Language-Action-M/01_overview.md) — 2026 ICLR.
130. [Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks](../2025/RSS/2025_RSS_Uni-NaVid-A-Video-based-Vision-Language-Action-Model-for-U/01_overview.md) — 2025 RSS.
131. [Learning to Act Anywhere with Task-centric Latent Actions](../2025/RSS/2025_RSS_Learning-to-Act-Anywhere-with-Task-centric-Latent-Actions/01_overview.md) — 2025 RSS.
132. [CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision](../2025/RSS/2025_RSS_CLIP-RT-Learning-Language-Conditioned-Robotic-Policies-fro/01_overview.md) — 2025 RSS.
133. [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](../2025/RSS/2025_RSS_NaVILA-Legged-Robot-Vision-Language-Action-Model-for-Navig/01_overview.md) — 2025 RSS.
134. [ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy](../2025/RSS/2025_RSS_ConRFT-A-Reinforced-Fine-tuning-Method-for-VLA-Models-via/01_overview.md) — 2025 RSS.
135. [CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity](../2025/RSS/2025_RSS_CodeDiffuser-Attention-Enhanced-Diffusion-Policy-via-VLM-G/01_overview.md) — 2025 RSS.
136. [PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation](../2025/RSS/2025_RSS_PartInstruct-Part-level-Instruction-Following-for-Fine-gra/01_overview.md) — 2025 RSS.
137. [Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models](../2025/RSS/2025_RSS_Manual2Skill-Learning-to-Read-Manuals-and-Acquire-Robotic/01_overview.md) — 2025 RSS.
138. [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](../2025/arXiv/2025_arXiv_SmolVLA-A-Vision-Language-Action-Model-for-Affordable-and/01_overview.md) — 2025 arXiv.
139. [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](../2025/arXiv/2025_arXiv_Gemini-Robotics-1.5-Pushing-the-Frontier-of-Generalist-Rob/01_overview.md) — 2025 arXiv.
140. [GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.5-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) — 2025 Technical Report.
141. [GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.6-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) — 2025 Technical Report.
142. [Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy](../2026/AAAI/2026_AAAI_Grounding-Actions-in-Camera-Space-Observation-Centric-Visi/01_overview.md) — 2026 AAAI.
143. [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](../2024/CoRL/2024_CoRL_ReKep-Spatio-Temporal-Reasoning-of-Relational-Keypoint-Con/01_overview.md) — 2024 CoRL.
144. [VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation](../2024/CoRL/2024_CoRL_VoxAct-B-Voxel-Based-Acting-and-Stabilizing-Policy-for-Bim/01_overview.md) — 2024 CoRL.
145. [3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation](../2025/CoRL/2025_CoRL_3DS-VLA-A-3D-Spatial-Aware-Vision-Language-Action-Model-fo/01_overview.md) — 2025 CoRL.
146. [GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data](../2025/CoRL/2025_CoRL_GraspVLA-a-Grasping-Foundation-Model-Pre-trained-on-Billio/01_overview.md) — 2025 CoRL.
147. [Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation](../2025/CoRL/2025_CoRL_Long-VLA-Unleashing-Long-Horizon-Capability-of-Vision-Lang/01_overview.md) — 2025 CoRL.
148. [RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](../2025/ICLR/2025_ICLR_RDT-1B-a-Diffusion-Foundation-Model-for-Bimanual-Manipulat/01_overview.md) — 2025 ICLR.
149. [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](../2025/ICLR/2025_ICLR_AHA-A-Vision-Language-Model-for-Detecting-and-Reasoning-Ov/01_overview.md) — 2025 ICLR.
150. [SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models](../2026/CVPR/2026_CVPR_SIMPACT-Simulation-Enabled-Action-Planning-using-Vision-La/01_overview.md) — 2026 CVPR.
151. [Vision-Language Foundation Models as Effective Robot Imitators](../2024/ICLR/2024_ICLR_Vision-Language-Foundation-Models-as-Effective-Robot-Imita/01_overview.md) — 2024 ICLR.
152. [Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](../2024/ICLR/2024_ICLR_Unleashing-Large-Scale-Video-Generative-Pre-training-for-V/01_overview.md) — 2024 ICLR.
153. [RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation](../2024/NeurIPS/2024_NeurIPS_RoboMamba-Efficient-Vision-Language-Action-Model-for-Robot/01_overview.md) — 2024 NeurIPS.
154. [Latent Action Pretraining from Videos](../2025/ICLR/2025_ICLR_Latent-Action-Pretraining-from-Videos/01_overview.md) — 2025 ICLR.
155. [3D-VLA: A 3D Vision-Language-Action Generative World Model](../2024/ICML/2024_ICML_3D-VLA-A-3D-Vision-Language-Action-Generative-World-Model/01_overview.md) — 2024 ICML.
156. [VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions](../2024/NeurIPS/2024_NeurIPS_VLMimic-Vision-Language-Models-are-Visual-Imitation-Learne/01_overview.md) — 2024 NeurIPS.
157. [MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting](../2024/RSS/2024_RSS_MIRAGE-Cross-Embodiment-Zero-Shot-Policy-Transfer-with-Cro/01_overview.md) — 2024 RSS.
158. [Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation](../2024/RSS/2024_RSS_Pushing-the-Limits-of-Cross-Embodiment-Learning-for-Manipu/01_overview.md) — 2024 RSS.
159. [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](../2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/01_overview.md) — 2026 ECCV.

### World models, uncertainty, failure detection, and recovery — 30

160. [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../2025/CoRL/2025_CoRL_DreamGen-Unlocking-Generalization-in-Robot-Learning-throug/01_overview.md) — 2025 CoRL.
161. [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) — 2026 ICML.
162. [Learning Latent Dynamics for Planning from Pixels](../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) — 2019 ICML.
163. [Dream to Control: Learning Behaviors by Latent Imagination](../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) — 2020 ICLR.
164. [Mastering Diverse Domains through World Models](../2025/Nature/2025_Nature_Mastering-Diverse-Domains-through-World-Models/01_overview.md) — 2025 Nature.
165. [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](../2025/RSS/2025_RSS_PIN-WM-Learning-Physics-INformed-World-Models-for-Non-Preh/01_overview.md) — 2025 RSS.
166. [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) — 2025 RSS.
167. [FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation](../2025/arXiv/2025_arXiv_FlowDreamer-A-RGB-D-World-Model-with-Flow-based-Motion-Rep/01_overview.md) — 2025 arXiv.
168. [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) — 2025 RSS.
169. [SAFE: Multitask Failure Detection for Vision-Language-Action Models](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) — 2025 NeurIPS.
170. [WorldGym: World Model as An Environment for Policy Evaluation](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md) — 2026 ICLR.
171. [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) — 2026 ICLR.
172. [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) — 2026 CVPR.
173. [Can VLMs Diagnose and Recover from VLA Manipulation Faults?](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) — 2026 ICML.
174. [Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) — 2026 ICML.
175. [Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) — 2026 RSS.
176. [Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid](../2025/RSS/2025_RSS_Demonstrating-ViSafe-Vision-enabled-Safety-for-High-speed/01_overview.md) — 2025 RSS.
177. [Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation](../2025/RSS/2025_RSS_Learned-Perceptive-Forward-Dynamics-Model-for-Safe-and-Pla/01_overview.md) — 2025 RSS.
178. [Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift](../2025/RSS/2025_RSS_Certifiably-Correct-Mapping-for-Safe-Navigation-Despite-Od/01_overview.md) — 2025 RSS.
179. [Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos](../2025/RSS/2025_RSS_Particle-Grid-Neural-Dynamics-for-Learning-Deformable-Obje/01_overview.md) — 2025 RSS.
180. [Map Space Belief Prediction for Manipulation-Enhanced Mapping](../2025/RSS/2025_RSS_Map-Space-Belief-Prediction-for-Manipulation-Enhanced-Mapp/01_overview.md) — 2025 RSS.
181. [Unified Video Action Model](../2025/RSS/2025_RSS_Unified-Video-Action-Model/01_overview.md) — 2025 RSS.
182. [From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment](../2025/RSS/2025_RSS_From-Foresight-to-Forethought-VLM-In-the-Loop-Policy-Steer/01_overview.md) — 2025 RSS.
183. [Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins](../2025/RSS/2025_RSS_Prompting-with-the-Future-Open-World-Model-Predictive-Cont/01_overview.md) — 2025 RSS.
184. [Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight](../2025/AAAI/2025_AAAI_Self-Correcting-Robot-Manipulation-via-Gaussian-Splatted-F/01_overview.md) — 2025 AAAI.
185. [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](../2025/IROS/2025_IROS_WMNav-Integrating-Vision-Language-Models-into-World-Models/01_overview.md) — 2025 IROS.
186. [RoboDreamer: Learning Compositional World Models for Robot Imagination](../2024/ICML/2024_ICML_RoboDreamer-Learning-Compositional-World-Models-for-Robot/01_overview.md) — 2024 ICML.
187. [Learning Interactive Real-World Simulators](../2024/ICLR/2024_ICLR_Learning-Interactive-Real-World-Simulators/01_overview.md) — 2024 ICLR.
188. [SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation](../2025/RSS/2025_RSS_SafeMimic-Towards-Safe-and-Autonomous-Human-to-Robot-Imita/01_overview.md) — 2025 RSS.
189. [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](../2026/ICLR/2026_ICLR_Ctrl-World-A-Controllable-Generative-World-Model-for-Robot/01_overview.md) — 2026 ICLR.

### Locomotion, whole-body control, mobile manipulation, and humanoids — 26

190. [Perpetual Humanoid Control for Real-time Simulated Avatars](../2023/ICCV/2023_ICCV_Perpetual-Humanoid-Control-for-Real-time-Simulated-Avatars/01_overview.md) — 2023 ICCV.
191. [MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting](../2024/ACM-Transactions-on-Grap/2024_ACM-Transactions-on-Grap_MaskedMimic-Unified-Physics-Based-Character-Control-Throug/01_overview.md) — 2024 ACM Transactions on Graphics.
192. [HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots](../2025/ICRA/2025_ICRA_HOVER-Versatile-Neural-Whole-Body-Controller-for-Humanoid/01_overview.md) — 2025 ICRA.
193. [SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](../2026/Science-Robotics/2026_Science-Robotics_SONIC-Supersizing-Motion-Tracking-for-Natural-Humanoid-Who/01_overview.md) — 2026 Science Robotics.
194. [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](../2018/TOG-SIGGRAPH/2018_TOG-SIGGRAPH_DeepMimic-Example-Guided-Deep-Reinforcement-Learning-of-Ph/01_overview.md) — 2018 TOG / SIGGRAPH.
195. [Sim-to-Real: Learning Agile Locomotion For Quadruped Robots](../2018/RSS/2018_RSS_Sim-to-Real-Learning-Agile-Locomotion-For-Quadruped-Robots/01_overview.md) — 2018 RSS.
196. [Learning Quadrupedal Locomotion over Challenging Terrain](../2020/Science-Robotics/2020_Science-Robotics_Learning-Quadrupedal-Locomotion-over-Challenging-Terrain/01_overview.md) — 2020 Science Robotics.
197. [Extreme Parkour with Legged Robots](../2024/ICRA/2024_ICRA_Extreme-Parkour-with-Legged-Robots/01_overview.md) — 2024 ICRA.
198. [Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior](../2022/CoRL/2022_CoRL_Walk-These-Ways-Tuning-Robot-Control-for-Generalization-wi/01_overview.md) — 2022 CoRL.
199. [HumanPlus: Humanoid Shadowing and Imitation from Humans](../2024/CoRL/2024_CoRL_HumanPlus-Humanoid-Shadowing-and-Imitation-from-Humans/01_overview.md) — 2024 CoRL.
200. [ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](../2025/RSS/2025_RSS_ASAP-Aligning-Simulation-and-Real-World-Physics-for-Learni/01_overview.md) — 2025 RSS.
201. [LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning](../2025/RSS/2025_RSS_LangWBC-Language-Directed-Humanoid-Whole-Body-Control-via/01_overview.md) — 2025 RSS.
202. [RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity](../2025/RSS/2025_RSS_RoboPanoptes-The-All-Seeing-Robot-with-Whole-body-Dexterit/01_overview.md) — 2025 RSS.
203. [Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](../2024/RSS/2024_RSS_Demonstrating-OK-Robot-What-Really-Matters-in-Integrating/01_overview.md) — 2024 RSS.
204. [HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion](../2026/ICLR/2026_ICLR_HWC-Loco-A-Hierarchical-Whole-Body-Control-Approach-to-Rob/01_overview.md) — 2026 ICLR.
205. [VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation](../2026/CVPR/2026_CVPR_VIRAL-Visual-Sim-to-Real-at-Scale-for-Humanoid-Loco-Manipu/01_overview.md) — 2026 CVPR.
206. [Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation](../2024/RA-L/2024_RA-L_Language-Grounded-Dynamic-Scene-Graphs-for-Interactive-Obj/01_overview.md) — 2024 RA-L.
207. [Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation](../2025/RA-L/2025_RA-L_Dynamic-Open-Vocabulary-3D-Scene-Graphs-for-Long-term-Lang/01_overview.md) — 2025 RA-L.
208. [AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control](../2025/RSS/2025_RSS_AMO-Adaptive-Motion-Optimization-for-Hyper-Dexterous-Human/01_overview.md) — 2025 RSS.
209. [Demonstrating MOSART: Opening Articulated Structures in the Real World](../2025/RSS/2025_RSS_Demonstrating-MOSART-Opening-Articulated-Structures-in-the/01_overview.md) — 2025 RSS.
210. [HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](../2025/RSS/2025_RSS_HOMIE-Humanoid-Loco-Manipulation-with-Isomorphic-Exoskelet/01_overview.md) — 2025 RSS.
211. [Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning](../2025/RSS/2025_RSS_Flying-Hand-End-Effector-Centric-Framework-for-Versatile-A/01_overview.md) — 2025 RSS.
212. [SPIN: Simultaneous Perception, Interaction and Navigation](../2024/CVPR/2024_CVPR_SPIN-Simultaneous-Perception-Interaction-and-Navigation/01_overview.md) — 2024 CVPR.
213. [WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts](../2024/CoRL/2024_CoRL_WoCoCo-Learning-Whole-Body-Humanoid-Control-with-Sequentia/01_overview.md) — 2024 CoRL.
214. [ViNT: A Foundation Model for Visual Navigation](../2023/CoRL/2023_CoRL_ViNT-A-Foundation-Model-for-Visual-Navigation/01_overview.md) — 2023 CoRL.
215. [GOAT: GO to Any Thing](../2024/RSS/2024_RSS_GOAT-GO-to-Any-Thing/01_overview.md) — 2024 RSS.

### Active and embodied 3D Vision — 19

216. [Where2Act: From Pixels to Actions for Articulated 3D Objects](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md) — 2021 ICCV.
217. [FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md) — 2022 RSS.
218. [Ditto: Building Digital Twins of Articulated Objects from Interaction](../2022/CVPR/2022_CVPR_Ditto-Building-Digital-Twins-of-Articulated-Objects-from-I/01_overview.md) — 2022 CVPR.
219. [VLMaps: Visual-Language Maps for Robot Navigation](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) — 2023 ICRA.
220. [SUGAR: Pre-training 3D Visual Representations for Robotics](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md) — 2024 CVPR.
221. [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](../2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) — 2025 IROS.
222. [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](../2025/CVPR/2025_CVPR_RoboSpatial-Teaching-Spatial-Understanding-to-2D-and-3D-Vi/01_overview.md) — 2025 CVPR.
223. [PointVLA: Injecting the 3D World into Vision-Language-Action Models](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) — 2026 RA-L.
224. [Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics](../2025/RSS/2025_RSS_Vysics-Object-Reconstruction-Under-Occlusion-by-Fusing-Vis/01_overview.md) — 2025 RSS.
225. [Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery](../2021/ICCV/2021_ICCV_Act-the-Part-Learning-Interaction-Strategies-for-Articulat/01_overview.md) — 2021 ICCV.
226. [Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects](../2023/NeurIPS/2023_NeurIPS_Where2Explore-Few-shot-Affordance-Learning-for-Unseen-Nove/01_overview.md) — 2023 NeurIPS.
227. [Clio: Real-time Task-Driven Open-Set 3D Scene Graphs](../2024/RA-L/2024_RA-L_Clio-Real-time-Task-Driven-Open-Set-3D-Scene-Graphs/01_overview.md) — 2024 RA-L.
228. [HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](../2025/RA-L/2025_RA-L_HAMMER-Heterogeneous-Multi-Robot-Semantic-Gaussian-Splatti/01_overview.md) — 2025 RA-L.
229. [VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting](../2026/ICRA/2026_ICRA_VISTA-Open-Vocabulary-Task-Relevant-Robot-Exploration-with/01_overview.md) — 2026 ICRA.
230. [RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics](../2025/NeurIPS/2025_NeurIPS_RoboRefer-Towards-Spatial-Referring-with-Reasoning-in-Visi/01_overview.md) — 2025 NeurIPS.
231. [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](../2024/ICRA/2024_ICRA_VLFM-Vision-Language-Frontier-Maps-for-Zero-Shot-Semantic/01_overview.md) — 2024 ICRA.
232. [Volumetric Environment Representation for Vision-Language Navigation](../2024/CVPR/2024_CVPR_Volumetric-Environment-Representation-for-Vision-Language/01_overview.md) — 2024 CVPR.
233. [IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation](../2025/ICCV/2025_ICCV_IGL-Nav-Incremental-3D-Gaussian-Localization-for-Image-goa/01_overview.md) — 2025 ICCV.
234. [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](../2025/ICCV/2025_ICCV_Move-to-Understand-a-3D-Scene-Bridging-Visual-Grounding-an/01_overview.md) — 2025 ICCV.

## REFERENCE — On-Demand Reading

CORE/NEXT에는 포함되지 않지만 중요한 foundation, baseline, representation, dataset, benchmark 또는 Robotics/VLA 관련 논문이다. 연구 설계 중 필요할 때 찾아 읽으며 완독 목표로 삼지 않는다.

## ARCHIVE — Search Only

현재 robotics-first 방향과 직접 연결되지 않는 논문이다. 향후 연구축이 바뀌거나 특정 3D/VLM 배경이 필요할 때 다시 승격할 수 있으며, 레지스트리와 로컬 노트는 그대로 보존한다.
