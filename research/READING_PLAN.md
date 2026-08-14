# Long-Term Robotics Reading Plan

- Updated: 2026-08-12 KST
- Source registry: [PAPER.md](../PAPER.md)
- Full tier index: [READING_TIERS.csv](./READING_TIERS.csv)
- Reading tracker: [READING_STATUS.csv](./READING_STATUS.csv)
- Intensive-reading set: **140 papers** (CORE 60 + NEXT 80)
- Research stance: Robotics is the main axis; 3D Vision is selected when it changes robot state estimation, planning, control, or evaluation.

## How to Use This Plan

이 문서는 별도 priority 목록과 robotics roadmap을 합친 유일한 장기 reading roadmap이다. 논문은 다음 폐루프에서 맡는 역할을 기준으로 읽는다.

`observation → state/world model → task & motion decision → policy/control → contact → feedback/failure recovery`

- **Robotics:** planning, control, learning, physical interaction, deployment가 주 연구축이다.
- **VLA:** language 이해 자체보다 action representation, robot data, embodiment transfer, latency, memory, feedback, safety를 본다.
- **3D Vision:** 독립 benchmark보다 manipulation, navigation, SLAM, spatial memory, active perception에 주는 downstream 효과를 본다.
- **Humanoid:** 별도 축으로 분리하지 않고 locomotion, whole-body control, imitation, loco-manipulation 안에서 읽는다.

### Default reading budget

| Research track | Share | Focus |
|---|---:|---|
| Robot learning and control | 25% | RL/IL/offline RL, planning, optimal control, sim-to-real |
| Manipulation and physical interaction | 25% | grasping, contact, tactile/force, dexterity, deformables, assembly |
| VLA, world models, safety, and long horizon | 20% | generalist policies, predictive models, uncertainty, recovery, replanning |
| Locomotion, whole-body, and mobile robotics | 15% | legged/humanoid control, loco-manipulation, navigation |
| Robotics-enabling 3D Vision | 15% | geometry, SLAM, active perception, semantic/spatial memory |

이 비율은 registry 구성 비율이 아니라 장기 읽기·비교·재현 시간의 기본값이다. 연구 주제가 정해지면 해당 track을 50% 이상으로 높일 수 있다.

## Priority Criteria

위에서 아래 순서로 판단하되 PDF 보유 여부는 고려하지 않는다.

1. 실제 robot task와 closed-loop action/control에 직접 연결되는가
2. 해당 분야의 foundation 또는 후속 연구의 핵심 prerequisite인가
3. 해결하려는 연구 공백과 기존 접근의 한계가 명확한가
4. contact, partial observability, uncertainty, safety, failure recovery를 실질적으로 다루는가
5. real robot 또는 설득력 있는 physics evaluation이 있는가
6. 평가 protocol, metric, baseline이 명확하고 재검증 가능한가
7. 구현 난이도와 데이터·코드·하드웨어 접근성이 현실적인가
8. embodiment, task, object, environment generalization을 검증하는가
9. 최신 trend 중 후속 연구가 이어지는 핵심 flow를 형성하는가
10. 현재 연구에서 반박·재사용·확장 가능한 contribution이 있는가

## Tier Definitions

| Tier | Papers | Use |
|---|---:|---|
| CORE | 60 | 공통 기반과 주력 연구축. 순서대로 정독하고 비교 노트를 남긴다. |
| NEXT | 80 | CORE 이후 트랙별로 정독한다. 연구 주제에 따라 내부 순서는 바꿀 수 있다. |
| REFERENCE | 438 | 설계·실험 중 필요한 논문만 찾아 읽는다. 완독 목표가 아니다. |
| ARCHIVE | 233 | 현재 robotics-first 범위 밖의 검색·역사 자료. 삭제하지 않지만 읽기 큐에서 제외한다. |

CORE와 NEXT만 장기 정독 대상이다. REFERENCE와 ARCHIVE의 개별 분류는 CSV에서 검색·필터링한다.

## Completion Rule

논문 하나를 완료 처리하려면 overview만 읽는 것으로 끝내지 않고 다음 네 가지를 남긴다.

1. 문제 설정과 기존 접근 대비 핵심 가정
2. observation/state/action/control interface
3. 실험의 embodiment, task, data, metric, failure mode
4. 현재 연구에 재사용할 요소와 반박하거나 확장할 지점

## Long-Term Reading Sequence

1. **Mechanics and control:** Operational Space Control → PRM/RRT → CHOMP/TrajOpt → PDDLStream → whole-body/force control.
2. **Policy learning:** DAgger/GAIL → RoboMimic/RLBench → TRPO/PPO/SAC → offline RL → DDPM/Flow Matching → Diffusion Policy and scalable robot data.
3. **Physical interaction:** contact mechanics and grasping → tactile/force feedback → dexterous, deformable, tool, assembly tasks.
4. **Generalist policies:** CLIP/PaLM-E/CLIPort → RT-1/RT-2 → Open X-Embodiment → Octo/OpenVLA/π0 → FAST/OpenVLA-OFT/π0.5.
5. **Deployment:** World Models/Dreamer → DayDreamer/TD-MPC2 → FAIL-Detect/SAFE → safety filter and recovery.
6. **Embodiment specialization:** locomotion, whole-body, mobile manipulation을 선택하고 필요한 3D perception을 역으로 연결한다.
7. **Active spatial intelligence:** PointNet/3DGS/DUSt3R/VGGT → SLAM/semantic mapping → articulation, active perception, 3D-aware VLA.

## Dependency-Based Reading Batches

각 batch는 달력 기반 일정이 아니라 prerequisite 단위다. 한 batch 전체를 끝내야 다음으로 갈 필요는 없지만, 같은 계보에서는 왼쪽 논문을 먼저 읽는다.

| Batch | Core question | Required spine | Branch after the spine | Exit artifact |
|---|---|---|---|---|
| A. Mechanics and feasibility | 학습 이전에 robot action의 feasibility와 constraint는 어떻게 표현되는가? | Operational Space Control → PRM/RRT → CHOMP/TrajOpt → PDDLStream | HQP / Whole-Body NMPC / contact optimization | planner·controller별 state, decision variable, guarantee 표 |
| B. Learning objectives and data | policy가 expert, reward, value와 logged data에서 무엇을 학습하는가? | DAgger/GPS/GAIL → TRPO/PPO/SAC → RoboMimic → IBC/IQL | CQL/MOPO/TD3+BC, RLBench, MimicGen/DROID | objective × data-support × interaction 비교 표 |
| C. Generative action policies | multimodal continuous action을 어떤 생성 과정으로 나타내는가? | DDPM / Flow Matching → Diffusion Policy → π0 | Diffusion-EDFs, Reactive Diffusion Policy, FAST | sampling step·chunk·latency·feedback 비교 표 |
| D. Generalist VLA and scaling | semantic prior와 heterogeneous robot data가 action으로 어떻게 연결되는가? | CLIP/CLIPort/PaLM-E → RT-1/RT-2 → Open X-Embodiment → Octo/OpenVLA | OpenVLA-OFT, π0/π0.5, memory/planning VLA | data × embodiment × action interface 비교 표 |
| E. Contact, safety, and recovery | 접촉 변화와 실패를 얼마나 빨리 감지하고 수정하는가? | contact/grasp foundations → tactile dynamics/control → CBF/Recovery RL → FAIL-Detect/SAFE | ForceVLA2, WorldGym/WMPO | perturbation·force·intervention·recovery protocol |
| F. Embodiment specialization | 동일 학습 원리가 legged, humanoid와 mobile manipulation에서 무엇이 달라지는가? | RMA → perceptive locomotion/parkour → HumanoidBench/OmniH2O/Mobile ALOHA | LangWBC, ASAP, HWC-Loco, VIRAL | dynamics/contact/whole-body coupling 비교 표 |
| G. Action-relevant 3D | 더 좋은 geometry가 실제 robot decision을 언제 개선하는가? | PointNet → DROID-SLAM/3DGS → ConceptFusion/RVT/DUSt3R | VGGT/SUGAR, active 3D, PointVLA/Any3D-VLA | representation 고정 ablation과 downstream metric |

Batch exit artifact를 채우기 전에는 해당 계보를 `SYNTHESIZED`로 올리지 않는다. 세부 paper sequence는 아래 CORE/NEXT 목록의 순서를 따른다.

## Research Lenses Across Tracks

- Robot learning을 behavior cloning으로 한정하지 않고 offline-to-online improvement, reward/value learning, failure/suboptimal data 활용까지 본다.
- Contact를 예외가 아니라 state, dynamics, constraint, feedback signal로 다룬다.
- Locomotion과 manipulation의 결합, balance와 task interaction의 공동 제어를 본다.
- Safety를 constraint, uncertainty, monitoring, intervention, recovery의 여러 시간 척도로 나눈다.
- Geometry가 learned policy 안에서 equivariance, 3D state, spatial memory, collision/contact structure로 어떤 역할을 하는지 본다.
- Architecture보다 data coverage, quality, curation, embodiment diversity와 scaling law를 함께 비교한다.
- Generative action model의 inference latency와 실제 closed-loop control frequency를 확인한다.
- Tabletop success rate를 넘어 long horizon, real-world disturbances, sensor degradation, compromised contact, recovery를 평가한다.

## CORE — 60 papers

### Planning, control, and whole-body foundations — 9

1. [A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation](../1987/IEEE-JRA/1987_IEEE-JRA_A-Unified-Approach-for-Motion-and-Force-Control-of-Robot-M/01_overview.md) — 1987 IEEE JRA.
2. [Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces](../1996/IEEE-T-RA/1996_IEEE-T-RA_Probabilistic-Roadmaps-for-Path-Planning-in-High-Dimension/01_overview.md) — 1996 IEEE T-RA.
3. [Rapidly-Exploring Random Trees: A New Tool for Path Planning](../1998/Technical-Report/1998_Technical-Report_Rapidly-Exploring-Random-Trees-A-New-Tool-for-Path-Plannin/01_overview.md) — 1998 Technical Report.
4. [CHOMP: Gradient Optimization Techniques for Efficient Motion Planning](../2009/ICRA/2009_ICRA_CHOMP-Gradient-Optimization-Techniques-for-Efficient-Motio/01_overview.md) — 2009 ICRA.
5. [TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning](../2013/IROS/2013_IROS_TrajOpt-A-Sequential-Convex-Optimization-Algorithm-for-Rob/01_overview.md) — 2013 IROS.
6. [PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) — 2020 ICAPS.
7. [Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints](../2013/T-RO/2013_T-RO_Dynamic-Whole-Body-Motion-Generation-under-Rigid-Contacts/01_overview.md) — 2013 T-RO.
8. [Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation](../2014/IJRR/2014_IJRR_Hierarchical-Quadratic-Programming-Fast-Online-Humanoid-Ro/01_overview.md) — 2014 IJRR.
9. [Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md) — 2018 RA-L.

### RL, IL, and policy learning foundations — 15

1. [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) — 2011 AISTATS.
2. [Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics](../2016/JMLR/2016_JMLR_Learning-Neural-Network-Policies-with-Guided-Policy-Search/01_overview.md) — 2016 JMLR.
3. [Generative Adversarial Imitation Learning](../2016/NeurIPS/2016_NeurIPS_Generative-Adversarial-Imitation-Learning/01_overview.md) — 2016 NeurIPS.
4. [Trust Region Policy Optimization](../2015/ICML/2015_ICML_Trust-Region-Policy-Optimization/01_overview.md) — 2015 ICML.
5. [Proximal Policy Optimization Algorithms](../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) — 2017 arxiv.
6. [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](../2018/ICML/2018_ICML_Soft-Actor-Critic-Off-Policy-Maximum-Entropy-Deep-Reinforc/01_overview.md) — 2018 ICML.
7. [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](../2017/IROS/2017_IROS_Domain-Randomization-for-Transferring-Deep-Neural-Networks/01_overview.md) — 2017 IROS.
8. [What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md) — 2021 CoRL.
9. [Implicit Behavioral Cloning](../2022/CoRL/2022_CoRL_Implicit-Behavioral-Cloning/01_overview.md) — 2022 CoRL.
10. [Offline Reinforcement Learning with Implicit Q-Learning](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md) — 2022 ICLR.
11. [Decision Transformer: Reinforcement Learning via Sequence Modeling](../2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/01_overview.md) — 2021 NeurIPS.
12. [Denoising Diffusion Probabilistic Models](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) — 2020 NeurIPS.
13. [Flow Matching for Generative Modeling](../2023/ICLR/2023_ICLR_Flow-Matching-for-Generative-Modeling/01_overview.md) — 2023 ICLR.
14. [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](../2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md) — 2023 RSS.
15. [Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions](../2024/CoRL/2024_CoRL_Q-Transformer-Scalable-Offline-Reinforcement-Learning-via/01_overview.md) — 2024 CoRL.

### Manipulation, contact, tactile, and dexterity — 8

1. [Contact-Invariant Optimization for Hand Manipulation](../2014/SIGGRAPH/2014_SIGGRAPH_Contact-Invariant-Optimization-for-Hand-Manipulation/01_overview.md) — 2014 SIGGRAPH.
2. [GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping](../2020/CVPR/2020_CVPR_GraspNet-1Billion-A-Large-Scale-Benchmark-for-General-Obje/01_overview.md) — 2020 CVPR.
3. [Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes](../2021/ICRA/2021_ICRA_Contact-GraspNet-Efficient-6-DoF-Grasp-Generation-in-Clutt/01_overview.md) — 2021 ICRA.
4. [Factory: Fast Contact for Robotic Assembly](../2022/RSS/2022_RSS_Factory-Fast-Contact-for-Robotic-Assembly/01_overview.md) — 2022 RSS.
5. [Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models](../2023/T-RO/2023_T-RO_Global-Planning-for-Contact-Rich-Manipulation-via-Local-Sm/01_overview.md) — 2023 T-RO.
6. [Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control](../2024/RSS/2024_RSS_Tactile-Driven-Non-Prehensile-Object-Manipulation-via-Extr/01_overview.md) — 2024 RSS.
7. [RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing](../2024/RSS/2024_RSS_RoboPack-Learning-Tactile-Informed-Dynamics-Models-for-Den/01_overview.md) — 2024 RSS.
8. [DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References](../2025/ICLR/2025_ICLR_DexTrack-Towards-Generalizable-Neural-Tracking-Control-for/01_overview.md) — 2025 ICLR Poster.

### VLA and generalist robot policies — 11

1. [Learning Transferable Visual Models From Natural Language Supervision](../2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/01_overview.md) — 2021 ICML.
2. [CLIPort: What and Where Pathways for Robotic Manipulation](../2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md) — 2021 CoRL.
3. [PaLM-E: An Embodied Multimodal Language Model](../2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/01_overview.md) — 2023 ICML.
4. [RT-1: Robotics Transformer for Real-World Control at Scale](../2022/arxiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md) — 2022 arxiv.
5. [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](../2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md) — 2023 CoRL.
6. [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](../2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/01_overview.md) — 2023 CoRL.
7. [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md) — 2024 ICRA.
8. [Octo: An Open-Source Generalist Robot Policy](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md) — 2024 RSS.
9. [OpenVLA: An Open-Source Vision-Language-Action Model](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) — 2024 CoRL.
10. [π0: A Vision-Language-Action Flow Model for General Robot Control](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) — 2025 RSS.
11. [π0.5: a Vision-Language-Action Model with Open-World Generalization](../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md) — 2025 CoRL.

### Safety and robot world models — 5

1. [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) — 2018 NeurIPS Workshop.
2. [DayDreamer: World Models for Physical Robot Learning](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) — 2022 CoRL.
3. [TD-MPC2: Scalable, Robust World Models for Continuous Control](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) — 2024 ICLR.
4. [Control Barrier Function Based Quadratic Programs for Safety Critical Systems](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) — 2017 TAC.
5. [Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) — 2020 RA-L.

### Locomotion, mobile manipulation, and humanoid systems — 6

1. [RMA: Rapid Motor Adaptation for Legged Robots](../2021/RSS/2021_RSS_RMA-Rapid-Motor-Adaptation-for-Legged-Robots/01_overview.md) — 2021 RSS.
2. [Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild](../2022/Science-Robotics/2022_Science-Robotics_Learning-Robust-Perceptive-Locomotion-for-Quadrupedal-Robo/01_overview.md) — 2022 Science Robotics.
3. [ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots](../2024/Science-Robotics/2024_Science-Robotics_ANYmal-Parkour-Learning-Agile-Navigation-for-Quadrupedal-R/01_overview.md) — 2024 Science Robotics.
4. [HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation](../2024/RSS/2024_RSS_HumanoidBench-Simulated-Humanoid-Benchmark-for-Whole-Body/01_overview.md) — 2024 RSS.
5. [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md) — 2024 CoRL.
6. [Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md) — 2024 CoRL.

### Robotics-enabling 3D perception — 6

1. [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](../2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) — 2017 CVPR.
2. [DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) — 2021 NeurIPS.
3. [3D Gaussian Splatting for Real-Time Radiance Field Rendering](../2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md) — 2023 SIGGRAPH.
4. [ConceptFusion: Open-set Multimodal 3D Mapping](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) — 2023 RSS.
5. [RVT: Robotic View Transformer for 3D Object Manipulation](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) — 2023 CoRL.
6. [DUSt3R: Geometric 3D Vision Made Easy](../2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md) — 2024 CVPR.

## NEXT — 80 papers

### RL, IL, offline learning, and robot data — 13

1. [Continuous Control with Deep Reinforcement Learning](../2016/ICLR/2016_ICLR_Continuous-Control-with-Deep-Reinforcement-Learning/01_overview.md) — 2016 ICLR.
2. [Addressing Function Approximation Error in Actor-Critic Methods](../2018/ICML/2018_ICML_Addressing-Function-Approximation-Error-in-Actor-Critic-Me/01_overview.md) — 2018 ICML.
3. [Hindsight Experience Replay](../2017/NeurIPS/2017_NeurIPS_Hindsight-Experience-Replay/01_overview.md) — 2017 NeurIPS.
4. [Constrained Policy Optimization](../2017/ICML/2017_ICML_Constrained-Policy-Optimization/01_overview.md) — 2017 ICML.
5. [Conservative Q-Learning for Offline Reinforcement Learning](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md) — 2020 NeurIPS.
6. [MOPO: Model-based Offline Policy Optimization](../2020/NeurIPS/2020_NeurIPS_MOPO-Model-based-Offline-Policy-Optimization/01_overview.md) — 2020 NeurIPS.
7. [A Minimalist Approach to Offline Reinforcement Learning](../2021/NeurIPS/2021_NeurIPS_A-Minimalist-Approach-to-Offline-Reinforcement-Learning/01_overview.md) — 2021 NeurIPS.
8. [Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations](../2018/RSS/2018_RSS_Learning-Complex-Dexterous-Manipulation-with-Deep-Reinforc/01_overview.md) — 2018 RSS.
9. [Learning Latent Plans from Play](../2020/CoRL/2020_CoRL_Learning-Latent-Plans-from-Play/01_overview.md) — 2020 CoRL.
10. [Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning](../2020/CoRL/2020_CoRL_Relay-Policy-Learning-Solving-Long-Horizon-Tasks-via-Imita/01_overview.md) — 2020 CoRL.
11. [RLBench: The Robot Learning Benchmark & Learning Environment](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) — 2020 RA-L.
12. [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../2023/CoRL/2023_CoRL_MimicGen-A-Data-Generation-System-for-Scalable-Robot-Learn/01_overview.md) — 2023 CoRL.
13. [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md) — 2024 RSS.

### Contact-rich, deformable, force, and dexterous manipulation — 18

1. [Control-Limited Differential Dynamic Programming](../2014/ICRA/2014_ICRA_Control-Limited-Differential-Dynamic-Programming/01_overview.md) — 2014 ICRA.
2. [In-Hand Manipulation via Motion Cones](../2019/RSS/2019_RSS_In-Hand-Manipulation-via-Motion-Cones/01_overview.md) — 2019 RSS.
3. [Towards Tight Convex Relaxations for Contact-Rich Manipulation](../2024/RSS/2024_RSS_Towards-Tight-Convex-Relaxations-for-Contact-Rich-Manipula/01_overview.md) — 2024 RSS.
4. [Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization](../2025/RSS/2025_RSS_Physics-Driven-Data-Generation-for-Contact-Rich-Manipulati/01_overview.md) — 2025 RSS.
5. [Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation](../2025/RSS/2025_RSS_Complementarity-Free-Multi-Contact-Modeling-and-Optimizati/01_overview.md) — 2025 RSS.
6. [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](../2020/CoRL/2020_CoRL_SoftGym-Benchmarking-Deep-Reinforcement-Learning-for-Defor/01_overview.md) — 2020 CoRL.
7. [DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools](../2022/ICLR/2022_ICLR_DiffSkill-Skill-Abstraction-from-Differentiable-Physics-fo/01_overview.md) — 2022 ICLR.
8. [Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation](../2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md) — 2021 CoRL.
9. [Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation](../2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md) — 2024 CVPR.
10. [IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality](../2023/RSS/2023_RSS_IndustReal-Transferring-Contact-Rich-Assembly-Tasks-from-S/01_overview.md) — 2023 RSS.
11. [Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](../2024/CVPR/2024_CVPR_Binding-Touch-to-Everything-Learning-Unified-Multimodal-Ta/01_overview.md) — 2024 CVPR.
12. [DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) — 2025 ICLR Spotlight.
13. [G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation](../2025/CVPR/2025_CVPR_G3Flow-Generative-3D-Semantic-Flow-for-Pose-aware-and-Gene/01_overview.md) — 2025 CVPR.
14. [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md) — 2025 RSS.
15. [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md) — 2026 CVPR.
16. [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md) — 2026 CVPR.
17. [Dexterous World Models](../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) — 2026 CVPR.
18. [EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation](../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) — 2026 ICLR Poster.

### VLA, cross-embodiment, and long-horizon planning — 16

1. [BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning](../2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/01_overview.md) — 2022 CoRL.
2. [Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation](../2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md) — 2023 CoRL.
3. [VIMA: General Robot Manipulation with Multimodal Prompts](../2023/ICML/2023_ICML_VIMA-General-Robot-Manipulation-with-Multimodal-Prompts/01_overview.md) — 2023 ICML.
4. [Inner Monologue: Embodied Reasoning through Planning with Language Models](../2022/CoRL/2022_CoRL_Inner-Monologue-Embodied-Reasoning-through-Planning-with-L/01_overview.md) — 2022 CoRL.
5. [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) — 2023 CoRL.
6. [XSkill: Cross Embodiment Skill Discovery](../2023/CoRL/2023_CoRL_XSkill-Cross-Embodiment-Skill-Discovery/01_overview.md) — 2023 CoRL.
7. [Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](../2024/NeurIPS/2024_NeurIPS_Scaling-Proprioceptive-Visual-Learning-with-Heterogeneous/01_overview.md) — 2024 NeurIPS.
8. [FAST: Efficient Action Tokenization for Vision-Language-Action Models](../2025/RSS/2025_RSS_FAST-Efficient-Action-Tokenization-for-Vision-Language-Act/01_overview.md) — 2025 RSS.
9. [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](../2025/RSS/2025_RSS_Fine-Tuning-Vision-Language-Action-Models-Optimizing-Speed/01_overview.md) — 2025 RSS.
10. [AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md) — 2026 CVPR.
11. [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](../2026/CVPR/2026_CVPR_PALM-Progress-Aware-Policy-Learning-via-Affordance-Reasoni/01_overview.md) — 2026 CVPR.
12. [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) — 2026 CVPR.
13. [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) — 2026 ICML.
14. [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](../2026/CVPR/2026_CVPR_Counterfactual-VLA-Self-Reflective-Vision-Language-Action/01_overview.md) — 2026 CVPR.
15. [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](../2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/01_overview.md) — 2026 ICML.
16. [MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) — 2026 ICLR Oral.

### World models, uncertainty, failure detection, and recovery — 10

1. [Learning Latent Dynamics for Planning from Pixels](../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) — 2019 ICML.
2. [Dream to Control: Learning Behaviors by Latent Imagination](../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) — 2020 ICLR.
3. [Mastering Diverse Domains through World Models](../2025/Nature/2025_Nature_Mastering-Diverse-Domains-through-World-Models/01_overview.md) — 2025 Nature.
4. [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](../2025/RSS/2025_RSS_PIN-WM-Learning-Physics-INformed-World-Models-for-Non-Preh/01_overview.md) — 2025 RSS.
5. [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) — 2025 RSS.
6. [FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation](../2025/arXiv/2025_arXiv_FlowDreamer-A-RGB-D-World-Model-with-Flow-based-Motion-Rep/01_overview.md) — 2025 arXiv.
7. [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) — 2025 RSS.
8. [SAFE: Multitask Failure Detection for Vision-Language-Action Models](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) — 2025 NeurIPS.
9. [WorldGym: World Model as An Environment for Policy Evaluation](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md) — 2026 ICLR.
10. [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) — 2026 ICLR Poster.

### Locomotion, whole-body control, mobile manipulation, and humanoids — 12

1. [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](../2018/TOG-SIGGRAPH/2018_TOG-SIGGRAPH_DeepMimic-Example-Guided-Deep-Reinforcement-Learning-of-Ph/01_overview.md) — 2018 TOG / SIGGRAPH.
2. [Sim-to-Real: Learning Agile Locomotion For Quadruped Robots](../2018/RSS/2018_RSS_Sim-to-Real-Learning-Agile-Locomotion-For-Quadruped-Robots/01_overview.md) — 2018 RSS.
3. [Learning Quadrupedal Locomotion over Challenging Terrain](../2020/Science-Robotics/2020_Science-Robotics_Learning-Quadrupedal-Locomotion-over-Challenging-Terrain/01_overview.md) — 2020 Science Robotics.
4. [Extreme Parkour with Legged Robots](../2024/ICRA/2024_ICRA_Extreme-Parkour-with-Legged-Robots/01_overview.md) — 2024 ICRA.
5. [Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior](../2022/CoRL/2022_CoRL_Walk-These-Ways-Tuning-Robot-Control-for-Generalization-wi/01_overview.md) — 2022 CoRL.
6. [HumanPlus: Humanoid Shadowing and Imitation from Humans](../2024/CoRL/2024_CoRL_HumanPlus-Humanoid-Shadowing-and-Imitation-from-Humans/01_overview.md) — 2024 CoRL.
7. [ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](../2025/RSS/2025_RSS_ASAP-Aligning-Simulation-and-Real-World-Physics-for-Learni/01_overview.md) — 2025 RSS.
8. [LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning](../2025/RSS/2025_RSS_LangWBC-Language-Directed-Humanoid-Whole-Body-Control-via/01_overview.md) — 2025 RSS.
9. [RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity](../2025/RSS/2025_RSS_RoboPanoptes-The-All-Seeing-Robot-with-Whole-body-Dexterit/01_overview.md) — 2025 RSS.
10. [Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](../2024/RSS/2024_RSS_Demonstrating-OK-Robot-What-Really-Matters-in-Integrating/01_overview.md) — 2024 RSS.
11. [HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion](../2026/ICLR/2026_ICLR_HWC-Loco-A-Hierarchical-Whole-Body-Control-Approach-to-Rob/01_overview.md) — 2026 ICLR Poster.
12. [VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation](../2026/CVPR/2026_CVPR_VIRAL-Visual-Sim-to-Real-at-Scale-for-Humanoid-Loco-Manipu/01_overview.md) — 2026 CVPR.

### Active and embodied 3D Vision — 11

1. [Where2Act: From Pixels to Actions for Articulated 3D Objects](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md) — 2021 ICCV.
2. [FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md) — 2022 RSS.
3. [Ditto: Building Digital Twins of Articulated Objects from Interaction](../2022/CVPR/2022_CVPR_Ditto-Building-Digital-Twins-of-Articulated-Objects-from-I/01_overview.md) — 2022 CVPR.
4. [VLMaps: Visual-Language Maps for Robot Navigation](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) — 2023 ICRA.
5. [Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships](../2024/CVPR/2024_CVPR_Open3DSG-Open-Vocabulary-3D-Scene-Graphs-from-Point-Clouds/01_overview.md) — 2024 CVPR.
6. [VGGT: Visual Geometry Grounded Transformer](../2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md) — 2025 CVPR.
7. [SUGAR: Pre-training 3D Visual Representations for Robotics](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md) — 2024 CVPR.
8. [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](../2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) — 2025 IROS.
9. [EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding](../2026/CVPR/2026_CVPR_EmbodiedSplat-Online-Feed-Forward-Semantic-3DGS-for-Open-V/01_overview.md) — 2026 CVPR.
10. [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](../2025/CVPR/2025_CVPR_RoboSpatial-Teaching-Spatial-Understanding-to-2D-and-3D-Vi/01_overview.md) — 2025 CVPR.
11. [PointVLA: Injecting the 3D World into Vision-Language-Action Models](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) — 2026 RA-L.

## REFERENCE — On-Demand Reading

CORE/NEXT에는 포함되지 않지만 중요한 foundation, baseline, representation, dataset, benchmark 또는 Robotics/VLA 관련 논문이다. 연구 설계 중 필요할 때 찾아 읽으며 완독 목표로 삼지 않는다.

## ARCHIVE — Search Only

현재 robotics-first 방향과 직접 연결되지 않는 논문이다. 향후 연구축이 바뀌거나 특정 3D/VLM 배경이 필요할 때 다시 승격할 수 있으며, 레지스트리와 로컬 노트는 그대로 보존한다.
