# Manipulation, Contact, Tactile, and Dexterity

- Updated: 2026-10-23 KST

## Scope

Analytic grasp planning, learned grasp/correspondence, contact-rich optimization, optical tactile hardware, force/tactile feedback, dexterous sim-to-real, deformables, tools와 assembly를 하나의 physical interaction 축에서 비교한다.

### Taxonomy boundary and curation schema

- **Primary axis:** object/contact representation → grasp or manipulation action → force/tactile feedback → contact-rich execution.
- **In scope:** grasp/contact planning, tactile or force sensing, dexterous/non-prehensile manipulation, contact dynamics, assembly와 manipulation policy가 robot contact outcome을 평가하는 경우.
- **Out of scope:** contact가 없는 generic object recognition, pure locomotion, 또는 robot execution과 연결되지 않는 pose/geometry benchmark. 3D representation은 downstream manipulation interface가 있을 때만 포함한다.
- **Inclusion test:** contact regime, action/control interface, feedback signal, physical assumption과 execution-level evaluation 중 최소 세 가지를 확인할 수 있어야 한다.
- **Role vocabulary:** `foundation`, `formulation`, `method`, `sensor`, `representation`, `dataset`, `benchmark`, `simulator`, `system`, `policy`를 사용한다.

공통 matrix/evidence 규약은 [synthesis 안내](./README.md#공통-비교-규약과-질문-분류)를 따른다.

## Reading Path

현재 읽기 우선순위는 [READING_PLAN.md](../research/READING_PLAN.md)를 따른다. 아래 계보는 비교 탐색용이며 전체 선행 완독 의무가 아니다.

2026-10-19 초점: ACT·DP3를 action representation 및 3D 입력의 기준으로 두고, VLA/RL 조작의 contact·force·reactivity 실패를 비교한다. Tactile hardware와 특수 dexterity는 해당 task와 sensor를 선택한 뒤 깊게 읽는다.

Planning Optimal Grasps → Contact-Invariant Optimization → GraspNet/Contact-GraspNet → Dense Object Nets/NDF/DenseMatcher → GelSight/DIGIT → tactile dynamics and slow–fast feedback → DeXtreme/DexTrack → deformable/tool/assembly → force-aware VLA.

### 2026-10-19 추가 논문 비교

아래는 등록된 abstract/project 근거에서 만든 **정독 전 비교 질문**이다. 직접 citation이나 실험 결론으로 취급하지 않으며, 읽기 순서와 tier는 READING_PLAN의 최신 값을 따른다.

| 비교할 논문 | 비교 축 | 본문에서 확인할 조건 |
|---|---|---|
| [Tac2Real](../2026/ECCV/2026_ECCV_Tac2Real-Reliable-and-GPU-Visuotactile-Simulation-for-Onli/01_overview.md) ↔ HIL-SERL·tactile/force policy | Visuotactile simulation과 실제 contact feedback | Insertion 성공을 범용 dexterity로 확대하지 않고 sensor·contact regime·transfer 조건을 비교한다. |

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### Manipulation, contact, tactile, and dexterity — 2

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](../2023/RSS/2023_RSS_Learning-Fine-Grained-Bimanual-Manipulation-with-Low-Cost/01_overview.md) | 2023 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](../2024/RSS/2024_RSS_3D-Diffusion-Policy-Generalizable-Visuomotor-Policy-Learni/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |

### Contact-rich, deformable, force, and dexterous manipulation — 49

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| NEXT | [Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment](../2026/ECCV/2026_ECCV_Tac2Real-Reliable-and-GPU-Visuotactile-Simulation-for-Onli/01_overview.md) | 2026 / ECCV | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping](../2020/CVPR/2020_CVPR_GraspNet-1Billion-A-Large-Scale-Benchmark-for-General-Obje/01_overview.md) | 2020 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes](../2021/ICRA/2021_ICRA_Contact-GraspNet-Efficient-6-DoF-Grasp-Generation-in-Clutt/01_overview.md) | 2021 / ICRA | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Factory: Fast Contact for Robotic Assembly](../2022/RSS/2022_RSS_Factory-Fast-Contact-for-Robotic-Assembly/01_overview.md) | 2022 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing](../2024/RSS/2024_RSS_RoboPack-Learning-Tactile-Informed-Dynamics-Models-for-Den/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation](../2018/CoRL/2018_CoRL_Dense-Object-Nets-Learning-Dense-Visual-Object-Descriptors/01_overview.md) | 2018 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [UMPNet: Universal Manipulation Policy Network for Articulated Objects](../2022/RA-L/2022_RA-L_UMPNet-Universal-Manipulation-Policy-Network-for-Articulat/01_overview.md) | 2022 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation](../2023/CoRL/2023_CoRL_Distilled-Feature-Fields-Enable-Few-Shot-Language-Guided-M/01_overview.md) | 2023 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping](../2024/RA-L/2024_RA-L_GaussianGrasper-3D-Language-Gaussian-Splatting-for-Open-vo/01_overview.md) | 2024 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation](../2024/ECCV/2024_ECCV_ManiGaussian-Dynamic-Gaussian-Splatting-for-Multi-task-Rob/01_overview.md) | 2024 / ECCV | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Gaussian Splatting Visual MPC for Granular Media Manipulation](../2025/ICRA/2025_ICRA_Gaussian-Splatting-Visual-MPC-for-Granular-Media-Manipulat/01_overview.md) | 2025 / ICRA | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](../2025/ICRA/2025_ICRA_Persistent-Object-Gaussian-Splat-POGS-for-Tracking-Human-a/01_overview.md) | 2025 / ICRA | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](../2020/IEEE-Robotics-and-Automa/2020_IEEE-Robotics-and-Automa_DIGIT-A-Novel-Design-for-a-Low-Cost-Compact-High-Resolutio/01_overview.md) | 2020 / IEEE Robotics and Automation Letters | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality](../2023/ICRA/2023_ICRA_DeXtreme-Transfer-of-Agile-In-hand-Manipulation-from-Simul/01_overview.md) | 2023 / ICRA | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Control-Limited Differential Dynamic Programming](../2014/ICRA/2014_ICRA_Control-Limited-Differential-Dynamic-Programming/01_overview.md) | 2014 / ICRA | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [In-Hand Manipulation via Motion Cones](../2019/RSS/2019_RSS_In-Hand-Manipulation-via-Motion-Cones/01_overview.md) | 2019 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Towards Tight Convex Relaxations for Contact-Rich Manipulation](../2024/RSS/2024_RSS_Towards-Tight-Convex-Relaxations-for-Contact-Rich-Manipula/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization](../2025/RSS/2025_RSS_Physics-Driven-Data-Generation-for-Contact-Rich-Manipulati/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation](../2025/RSS/2025_RSS_Complementarity-Free-Multi-Contact-Modeling-and-Optimizati/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](../2020/CoRL/2020_CoRL_SoftGym-Benchmarking-Deep-Reinforcement-Learning-for-Defor/01_overview.md) | 2020 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools](../2022/ICLR/2022_ICLR_DiffSkill-Skill-Abstraction-from-Differentiable-Physics-fo/01_overview.md) | 2022 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation](../2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md) | 2021 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation](../2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md) | 2024 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality](../2023/RSS/2023_RSS_IndustReal-Transferring-Contact-Rich-Assembly-Tasks-from-S/01_overview.md) | 2023 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](../2024/CVPR/2024_CVPR_Binding-Touch-to-Everything-Learning-Unified-Multimodal-Ta/01_overview.md) | 2024 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) | 2025 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation](../2025/CVPR/2025_CVPR_G3Flow-Generative-3D-Semantic-Flow-for-Pose-aware-and-Gene/01_overview.md) | 2025 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Dexterous World Models](../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation](../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) | 2026 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language](../2026/ICML/2026_ICML_Tabero-Learning-Gentle-Manipulation-with-Closed-Loop-Force/01_overview.md) | 2026 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment](../2026/RSS/2026_RSS_TactAlign-Human-to-Robot-Policy-Transfer-via-Tactile-Align/01_overview.md) | 2026 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DexterityGen: Foundation Controller for Unprecedented Dexterity](../2026/RSS/2026_RSS_DexterityGen-Foundation-Controller-for-Unprecedented-Dexte/01_overview.md) | 2026 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [V-HOP: Visuo-Haptic 6D Object Pose Tracking](../2025/RSS/2025_RSS_V-HOP-Visuo-Haptic-6D-Object-Pose-Tracking/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands](../2025/RSS/2025_RSS_PP-Tac-Paper-Picking-Using-Omnidirectional-Tactile-Feedbac/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty](../2025/RSS/2025_RSS_GeoDEx-A-Unified-Geometric-Framework-for-Tactile-Dexterous/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly](../2025/RSS/2025_RSS_Demonstrating-REASSEMBLE-A-Multimodal-Dataset-for-Contact/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation](../2025/RSS/2025_RSS_Robust-Peg-in-Hole-Assembly-under-Uncertainties-via-Compli/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning](../2025/RSS/2025_RSS_FACTR-Force-Attending-Curriculum-Training-for-Contact-Rich/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World](../2025/RSS/2025_RSS_CordViP-Correspondence-based-Visuomotor-Policy-for-Dextero/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation](../2025/AAAI/2025_AAAI_FlowPolicy-Enabling-Fast-and-Robust-3D-Flow-Based-Policy-v/01_overview.md) | 2025 / AAAI | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Sparsh: Self-supervised touch representations for vision-based tactile sensing](../2024/CoRL/2024_CoRL_Sparsh-Self-supervised-touch-representations-for-vision-ba/01_overview.md) | 2024 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Octopi: Object Property Reasoning with Large Tactile-Language Models](../2024/RSS/2024_RSS_Octopi-Object-Property-Reasoning-with-Large-Tactile-Langua/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation](../2024/CoRL/2024_CoRL_OPEN-TEACH-A-Versatile-Teleoperation-System-for-Robotic-Ma/01_overview.md) | 2024 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation](../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md) | 2023 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching](../2024/CoRL/2024_CoRL_Learning-Robotic-Manipulation-Policies-from-Point-Clouds-w/01_overview.md) | 2024 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models](../2026/RSS/2026_RSS_Contact-Anchored-Policies-Contact-Conditioning-Creates-Str/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |

<!-- READING_QUEUE:END -->

## Historical curation — 2026-09-02

아래는 해당 날짜의 변경 이력이다. 현재 membership과 수량은 위 generated queue를 따른다.

`Sparsh`, `Octopi`, `OPEN TEACH`를 `NEXT`에 반영했다. 세 논문은 각각 tactile representation, tactile-language reasoning, contact-rich teleoperation/data interface를 다루므로 단순 vision representation이 아니라 manipulation feedback과 data coverage의 문제로 비교한다.

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래는 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. `Paper` 링크는 local overview를 가리키고, official paper/project/code URL은 해당 note header에서 확인한다.
>
> Row convention: 한 행은 한 registry paper이다. `State / action / objective / timing`은 고정 순서로 기록하고, `Evaluation`은 `setup; data/split; metric; real/trials` 순서를 따른다. `Evidence / source`가 `CURATION-SEED`이면 수치나 세부 조건을 아직 주장하지 않는다.

| Paper | Year / Venue | Role | Facets | Problem | State / action / objective / timing | Why included / TL;DR | Evaluation (setup; data/split; metric; real/trials) | Evidence / source | Failure / assumption | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|---|
| [Planning Optimal Grasps](../1992/ICRA/1992_ICRA_Planning-Optimal-Grasps/01_overview.md) | 1992 / ICRA | foundation; formulation | gripper/hand; geometry+friction; model-based; grasp planning | analytic stable grasp selection | object geometry and contact set; finger/contact placement; wrench/quality criterion; planning-time | analytic contact feasibility를 learned grasp score의 기준으로 제공 | grasp examples; data/split=analytic cases; metric=grasp quality; real=no/trials=— | `CURATION-SEED`; overview + queue | geometry/friction, rigid contact, execution omitted | learned score와 wrench feasibility를 함께 평가 |
| [Contact-Invariant Optimization](../2014/SIGGRAPH/2014_SIGGRAPH_Contact-Invariant-Optimization-for-Hand-Manipulation/01_overview.md) | 2014 / SIGGRAPH | formulation; optimizer | hand/object; kinematics+contact; simulation; trajectory optimization | hand/object contact sequence discovery | articulated state and contact variables; optimized motion/contact trajectory; physics objective and constraints; iterative solve | contact sequence를 trajectory optimization의 결정변수로 만든 기준 | simulated hand/character; data/split=UNVERIFIED; metric=motion/contact quality; real=no/trials=— | `CURATION-SEED`; overview + queue | local minima, contact-model mismatch, initialization | contact mode를 explicit latent decision으로 다루기 |
| [GraspNet-1Billion](../2020/CVPR/2020_CVPR_GraspNet-1Billion-A-Large-Scale-Benchmark-for-General-Obje/01_overview.md) | 2020 / CVPR | dataset; benchmark | parallel-jaw arm; RGB-D; sim/analytic; grasp proposal | large-scale cluttered 6-DoF grasp data and evaluation | RGB-D scene and grasp pose; grasp proposal; analytic grasp success; offline inference | perception benchmark을 execution-oriented grasp metric과 연결 | cluttered grasp benchmark; data/split=dataset splits; metric=grasp AP/analytic success; real=no/trials=— | `CURATION-SEED`; overview + queue | synthetic-to-real gap, clutter, analytic contact assumptions | dataset metric과 physical execution을 분리 |
| [Contact-GraspNet](../2021/ICRA/2021_ICRA_Contact-GraspNet-Efficient-6-DoF-Grasp-Generation-in-Clutt/01_overview.md) | 2021 / ICRA | method; policy | parallel-jaw arm; RGB-D/point cloud; sim/real; grasp proposal | efficient scene-level grasp generation in clutter | point cloud and scene context; 6-DoF grasp proposal; learned contact feasibility; per-observation inference | point-cloud perception을 contact proposal interface로 연결 | cluttered grasp; data/split=UNVERIFIED; metric=grasp AP/execution success; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | perception-to-contact gap, unseen clutter, calibration | predicted grasp와 executed grasp를 분리 평가 |
| [Dense Object Nets](../2018/CoRL/2018_CoRL_Dense-Object-Nets-Learning-Dense-Visual-Object-Descriptors/01_overview.md) | 2018 / CoRL | representation; method | arm; RGB-D; real; correspondence | object-centric correspondence for manipulation | dense pixel/surface descriptor; correspondence-selected target; self-supervised correspondence objective; per-observation | correspondence가 contact target 선택으로 전달되는지 보는 기준 | real manipulation; data/split=multi-view/object transfer UNVERIFIED; metric=correspondence/manipulation success; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | occlusion, capture assumptions, category shift | representation metric을 downstream contact success와 연결 |
| [GelSight](../2017/Sensors/2017_Sensors_GelSight-High-Resolution-Robot-Tactile-Sensors-for-Estimat/01_overview.md) | 2017 / Sensors | sensor; foundation | fingertip; optical tactile; real; contact sensing | high-resolution contact geometry and force sensing | elastomer deformation image; tactile feature/force estimate; calibrated sensor objective; high-rate feedback | tactile observation contract의 hardware 기준점 | sensor characterization/application; data/split=UNVERIFIED; metric=geometry/force error; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | wear, calibration, shear/slip, sensor variation | tactile sensing과 controller contribution을 분리 |
| [DIGIT](../2020/IEEE-Robotics-and-Automa/2020_IEEE-Robotics-and-Automa_DIGIT-A-Novel-Design-for-a-Low-Cost-Compact-High-Resolutio/01_overview.md) | 2020 / IEEE Robotics and Automation Letters | sensor; system | fingertip/hand; optical tactile; real; contact sensing | compact high-resolution in-hand tactile sensing | deformation image; tactile feature/force estimate; sensing/calibration objective; high-rate feedback | portability와 resolution trade-off를 보는 sensor baseline | sensor characterization/application; data/split=UNVERIFIED; metric=force/geometry or task success; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | calibration drift, wear, shear/slip, sensor transfer | sensor form factor를 policy input과 별도 ablate |
| [RoboPack](../2024/RSS/2024_RSS_RoboPack-Learning-Tactile-Informed-Dynamics-Models-for-Den/01_overview.md) | 2024 / RSS | method; world model | manipulation platform; vision+tactile; real/sim; contact dynamics | dense packing with tactile-informed dynamics | visual-tactile state; planned/control action; learned dynamics objective; feedback loop | tactile state를 dynamics/planner interface로 승격 | packing task; data/split=UNVERIFIED; metric=task success/contact behavior; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | sensor/geometry shift, hidden contact, model bias | tactile dynamics와 task success를 함께 측정 |
| [Extrinsic Contact Control](../2024/RSS/2024_RSS_Tactile-Driven-Non-Prehensile-Object-Manipulation-via-Extr/01_overview.md) | 2024 / RSS | method; controller | manipulator; tactile+vision+proprioception; real/sim; non-prehensile control | non-prehensile object manipulation under contact-mode changes | contact mode/state; action/control from tactile state; mode-aware feedback objective; online loop | contact mode reasoning을 executable control interface로 비교 | non-prehensile manipulation; data/split=UNVERIFIED; metric=task success/contact mode; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | hidden contact, sensing delay, geometry shift | contact mode를 planner/controller state로 명시 |
| [Reactive Diffusion Policy](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md) | 2025 / RSS | policy; feedback method | contact manipulator; visual+tactile; real; dual-rate policy | contact-rich manipulation under fast disturbances | slow visual context and fast tactile state; nominal action chunk plus reactive action; imitation objective; slow/fast feedback | semantic policy와 high-rate contact correction의 분리 기준 | contact-rich tasks; data/split=UNVERIFIED; metric=success/reaction/force; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | sensor portability, residual instability, delay | slow semantic policy와 fast contact loop 분리 |
| [Factory](../2022/RSS/2022_RSS_Factory-Fast-Contact-for-Robotic-Assembly/01_overview.md) | 2022 / RSS | simulator; system | industrial arm; pose+contact; sim-to-real; assembly | fast contact simulation and robotic assembly transfer | object/robot/contact state; insertion/assembly control; simulation/transfer objective; online control | contact simulation throughput과 assembly transfer의 기준 | assembly tasks; data/split=UNVERIFIED; metric=assembly success/sim-to-real; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | simulator contact bias, calibration, model mismatch | physics/data pipeline을 execution baseline으로 사용 |
| [IndustReal](../2023/RSS/2023_RSS_IndustReal-Transferring-Contact-Rich-Assembly-Tasks-from-S/01_overview.md) | 2023 / RSS | system; sim-to-real | industrial arm; proprioception/vision; sim-to-real; assembly | transfer of contact-rich assembly from simulation | robot/object/contact state; assembly control policy; transfer objective; online execution | simulation scaling과 physical assembly protocol을 연결 | assembly tasks; data/split=UNVERIFIED; metric=success/transfer robustness; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | contact-model bias, calibration, task-specific tuning | simulator와 real contact failure를 함께 기록 |
| [DeXtreme](../2023/ICRA/2023_ICRA_DeXtreme-Transfer-of-Agile-In-hand-Manipulation-from-Simul/01_overview.md) | 2023 / ICRA | policy; system | Allegro Hand; proprioception+object pose; sim-to-real; dexterous RL | agile in-hand object reorientation transfer | hand state and estimated object pose; multi-finger joint policy; RL reward; high-rate control | perception-policy-transfer stack을 함께 평가하는 dexterity reference | in-hand reorientation; data/split=UNVERIFIED; metric=real success/robustness; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | pose estimator failure, object/setup specificity, sim contact bias | perception, policy와 transfer를 분리 ablate |
| [Diffusion-EDFs](../2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md) | 2024 / CVPR | representation; generative policy | tabletop arm; 3D geometry; sim/real; pose/action generation | pose-generalizable manipulation through equivariant generation | SE(3)-structured object/action representation; generative pose/action; diffusion objective; iterative inference | symmetry를 generative action distribution에 넣는 기준 | manipulation pose tasks; data/split=pose/task splits UNVERIFIED; metric=pose/task success; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | sensor/data confound, equivariance coverage, sampling cost | symmetry를 policy와 evaluation에 일관되게 적용 |
| [EquAct](../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) | 2026 / ICLR | policy; representation | tabletop arm; 3D vision; real/sim; multi-task action | SE(3)-equivariant multi-task robot policy | 3D object/action state; equivariant action policy; multi-task imitation objective; closed-loop action | geometric invariance와 multi-task action interface의 frontier | multi-task manipulation; data/split=UNVERIFIED; metric=task/pose generalization; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | sensor/data contribution, category shift, contact mismatch | equivariance와 contact feasibility를 함께 평가 |


## Dependency and Evolution

아래 계보는 mechanics, representation, policy와 feedback이 결합되는 순서를 보여 준다. 직접 citation 관계는 정독 시 확인한다.

### Relation type index

아래 label은 바로 다음 계보 표의 chain anchor에 적용한다. `formulation`, `method`, `data`, `evaluation`, `deployment`는 개념적 연결의 종류이며 citation 또는 직접 영향 관계를 뜻하지 않는다.

| Chain anchor | Relation type | Interpretation |
|---|---|---|
| Planning Optimal Grasps → GraspNet → Contact-GraspNet | formulation → data → policy | analytic grasp quality가 large-scale label과 scene proposal로 확장 |
| Contact-Invariant Optimization → Global Contact-Rich → Tight Convex | method → formulation/solver | contact sequence의 nonsmooth 문제를 optimization interface로 전개 |
| Dense Object Nets → NDF → DenseMatcher/G3Flow | representation → transfer method | descriptor가 equivariant correspondence와 task transfer로 확장 |
| NDF → Diffusion-EDFs → EquAct | representation → policy interface | SE(3) structure가 generative·multi-task action으로 전달 |
| GelSight → DIGIT → tactile dynamics → Reactive Policy → AT-VLA/ForceVLA2 | sensor → feedback → policy/deployment | optical tactile input이 high-rate feedback과 VLA interface로 확장 |
| GPU-sim dexterous RL → DeXtreme/IndustReal → DexTrack | simulation/data → deployment | randomized simulation이 physical dexterity와 reference transfer로 연결 |
| dexterous policy/demo → DexTrack → Dexterous World Models/DexterityGen | policy → prediction/controller | task policy가 reference generalization과 predictive contact model로 확장 |

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| [Planning Optimal Grasps](../1992/ICRA/1992_ICRA_Planning-Optimal-Grasps/01_overview.md) → [GraspNet-1Billion](../2020/CVPR/2020_CVPR_GraspNet-1Billion-A-Large-Scale-Benchmark-for-General-Obje/01_overview.md) → [Contact-GraspNet](../2021/ICRA/2021_ICRA_Contact-GraspNet-Efficient-6-DoF-Grasp-Generation-in-Clutt/01_overview.md) | analytic contact/wrench quality에서 large-scale grasp labels와 scene-level 6-DoF proposal로 이동한다. | learned score가 friction·compliance 변화와 실제 execution robustness를 얼마나 보존하는가 |
| [Contact-Invariant Optimization](../2014/SIGGRAPH/2014_SIGGRAPH_Contact-Invariant-Optimization-for-Hand-Manipulation/01_overview.md) → [Global Contact-Rich Planning](../2023/T-RO/2023_T-RO_Global-Planning-for-Contact-Rich-Manipulation-via-Local-Sm/01_overview.md) → [Tight Convex Relaxations](../2024/RSS/2024_RSS_Towards-Tight-Convex-Relaxations-for-Contact-Rich-Manipula/01_overview.md) / [Complementarity-Free Multi-Contact](../2025/RSS/2025_RSS_Complementarity-Free-Multi-Contact-Modeling-and-Optimizati/01_overview.md) | contact sequence의 combinatorial/nonsmooth 문제를 smoothing, relaxation, alternative modeling으로 다룬다. | solver success와 실제 model mismatch·online replanning 성능이 함께 유지되는가 |
| [Dense Object Nets](../2018/CoRL/2018_CoRL_Dense-Object-Nets-Learning-Dense-Visual-Object-Descriptors/01_overview.md) → [Neural Descriptor Fields](../2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md) → [DenseMatcher](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) / [G3Flow](../2025/CVPR/2025_CVPR_G3Flow-Generative-3D-Semantic-Flow-for-Pose-aware-and-Gene/01_overview.md) | dense 2D/surface descriptor에서 SE(3)-structured fields, category-level semantic correspondence와 temporal 3D flow를 이용한 task transfer로 확장된다. | correspondence accuracy가 contact feasibility와 long-horizon success를 보장하는가 |
| Neural Descriptor Fields → [Diffusion-EDFs](../2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md) → [EquAct](../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) | object representation의 SE(3) equivariance가 generative action distribution과 language-conditioned multi-task policy 전체로 확장된다. | pose generalization 이득과 추가 3D sensor/data 효과를 분리할 수 있는가 |
| [GelSight](../2017/Sensors/2017_Sensors_GelSight-High-Resolution-Robot-Tactile-Sensors-for-Estimat/01_overview.md) → [DIGIT](../2020/IEEE-Robotics-and-Automa/2020_IEEE-Robotics-and-Automa_DIGIT-A-Novel-Design-for-a-Low-Cost-Compact-High-Resolutio/01_overview.md) → tactile representation → [RoboPack](../2024/RSS/2024_RSS_RoboPack-Learning-Tactile-Informed-Dynamics-Models-for-Den/01_overview.md) / [Extrinsic Contact Mode Control](../2024/RSS/2024_RSS_Tactile-Driven-Non-Prehensile-Object-Manipulation-via-Extr/01_overview.md) → [Reactive Diffusion Policy](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md) → [AT-VLA](../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md) / [ForceVLA2](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md) | optical tactile hardware가 compact fingertip sensor, learned dynamics/contact mode, slow–fast residual correction과 VLA runtime feedback으로 확장된다. | sensor portability, calibration drift, 반응 속도, force-quality와 안정성을 어떤 공통 protocol로 비교할 것인가 |
| GPU-sim dexterous RL → [DeXtreme](../2023/ICRA/2023_ICRA_DeXtreme-Transfer-of-Agile-In-hand-Manipulation-from-Simul/01_overview.md) / [IndustReal](../2023/RSS/2023_RSS_IndustReal-Transferring-Contact-Rich-Assembly-Tasks-from-S/01_overview.md) → [DexTrack](../2025/ICLR/2025_ICLR_DexTrack-Towards-Generalizable-Neural-Tracking-Control-for/01_overview.md) | randomized simulation과 perception을 실제 in-hand/assembly에 transfer한 뒤 human-reference tracking과 broader object/motion generalization으로 확장된다. | simulator/contact randomization, pose estimator와 policy 중 실제 failure의 지배 요인은 무엇인가 |
| dexterous RL/demonstration → [DexTrack](../2025/ICLR/2025_ICLR_DexTrack-Towards-Generalizable-Neural-Tracking-Control-for/01_overview.md) → [Dexterous World Models](../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) / [DexterityGen](../2026/RSS/2026_RSS_DexterityGen-Foundation-Controller-for-Unprecedented-Dexte/01_overview.md) | task-specific reward와 tracking에서 demonstration flywheel, reference generalization, predictive dynamics와 RL primitive foundation controller로 확장된다. | human-reference tracking과 object-level task success, long-horizon contact stability가 언제 충돌하는가 |

## 2026-10-23 근거 통합

아래는 2026-10-22까지의 registry/source 감사와 후보 검토를 연결한 연구자 해석이다. 새 정독·효과 검증·직접 citation 관계의 확인을 뜻하지 않는다. Paper별 본문 확인 범위는 overview 및 연결된 dossier를 따른다.

| 비교 축 | 등록된 선행 | 현재 남길 구분 |
|---|---|---|
| D2: grasp와 후속 운반 | [Cooperative Grasping](../2026/RA-L/2026_RA-L_Cooperative-Grasping-for-Collective-Object-Transport-in-Co/01_overview.md) (2026 RA-L); [Grasp-Then-Plan](../2026/NeurIPS/2026_NeurIPS_Grasp-Then-Plan-with-Failure-Attribution-A-Closed-Two-Stag/01_overview.md) (2026 NeurIPS); [Foresight Residual RL](../2026/arXiv/2026_arXiv_Foresight-Residual-RL-for-Long-Horizon-Robot-Manipulation/01_overview.md) (2026 arXiv) | 파지 성공만으로 운반 가능성을 보증하지 않는다. 계획 실패·grasp 실패·후속 execution 실패의 label을 분리한다. |
| 보조 시스템과 회복 | [CarryOn](../2026/arXiv/2026_arXiv_CarryOn-A-Dual-Loop-Harness-for-Personalized-and-Reliable/01_overview.md) (2026 arXiv); [SafeLoop](../2026/arXiv/2026_arXiv_SafeLoop-Risk-Aware-Rollback-for-Vision-Language-Action-Ma/01_overview.md) (2026 arXiv) | 사용자 조정·rollback·monitoring을 새 VLA policy 능력과 혼동하지 않는다. 별도 정보/시도 예산을 기록한다. |

## Open Questions

현재 후보 판정은 [주제별 요약](../work/research_candidates/summaries/README.md)을 따른다. 아래 질문은 `CURATION-HYPOTHESIS`이며 재개 승인이 아니다.

| 질문 | 구별할 예측 | 최소 대조·중단 조건 | 근거/판정 |
|---|---|---|---|
| Grasp–transport–place | 동일 grasp 후보와 scene geometry에서 후속 운반을 고려한 선택이 supervised outcome ranking보다 필요한가? | Attachment/planner baseline과 실패 귀속을 고정한다. 공개 native task·executor가 없는 현재 D2는 HOLD다. | [검토 근거](../work/research_candidates/2026-10-22_d2_buildup/README.md) |
| Tactile/force feedback | 동일 contact task에서 고주파 feedback이 추가 sensing·adaptation data를 맞춘 뒤에도 slip/접촉 실패를 줄이는가? | 센서 교체·마모·calibration drift를 각각 분리한다. 성공률 외 force limit·intervention과 controller rate를 기록한다. | 기존 track 비교의 연구자 질문; native 효과 미검증 |
| Grasp metric의 행동 utility | Analytic contact score와 learned proposal의 순위가 compliant execution에서 언제 교차하는가? | 물체·접촉 mode별 held-out 조건과 실제 trial 분모를 확인한다. 단순 object/task 평균으로 dexterity 일반화를 주장하지 않는다. | 기존 track 비교의 연구자 질문; native 효과 미검증 |
