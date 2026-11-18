# Manipulation, Contact, Tactile, and Dexterity

- Updated: 2026-10-24 KST

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

### Contact-rich, deformable, force, and dexterous manipulation — 58

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
| NEXT | [FMB: A functional manipulation benchmark for generalizable robotic learning](../2025/IJRR/2025_IJRR_FMB-A-functional-manipulation-benchmark-for-generalizable/01_overview.md) | 2025 / IJRR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions](../2025/CoRL/2025_CoRL_Learning-Visuotactile-Estimation-and-Control-for-Non-prehe/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation](../2026/RSS/2026_RSS_Force-Policy-Learning-Hybrid-Force-Position-Control-Policy/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning](../2026/ICLR/2026_ICLR_Emergent-Dexterity-Via-Diverse-Resets-and-Large-Scale-Rein/01_overview.md) | 2026 / ICLR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation Under Uncertainty](../2025/RA-L/2025_RA-L_FORGE-Force-Guided-Exploration-for-Robust-Contact-Rich-Man/01_overview.md) | 2025 / RA-L | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation](../2026/arXiv/2026_arXiv_ContactBench-1.0-A-Benchmark-for-Everyday-Contact-Rich-Rob/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Tune to Learn: How Controller Gains Shape Robot Policy Learning](../2026/RSS/2026_RSS_Tune-to-Learn-How-Controller-Gains-Shape-Robot-Policy-Lear/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation](../2026/CVPR/2026_CVPR_Action-Geometry-Prediction-with-3D-Geometric-Prior-for-Bim/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Guiding real-world reinforcement learning for in-contact manipulation tasks with Shared Control Templates](../2024/Autonomous-Robots/2024_Autonomous-Robots_Guiding-real-world-reinforcement-learning-for-in-contact-m/01_overview.md) | 2024 / Autonomous Robots | `UNREAD` | `ABSTRACT_CHECKED` |

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

### Registry 연결 갱신 — 2026-10-25

- [JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments](../2024/RSS/2024_RSS_JIGGLE-An-Active-Sensing-Framework-for-Boundary-Parameters/01_overview.md)
- [AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation](../2024/RSS/2024_RSS_AdaptiGraph-Material-Adaptive-Graph-Based-Neural-Dynamics/01_overview.md)

Attachment와 material adaptation의 직접 선행을 연결한다. 정보 이득이나 예측 오차 감소를 task 성공 개선으로 대체하지 않으며 GAP-DE의 기존 HOLD를 유지한다.

이번 등록은 `ABSTRACT_CHECKED` 수준의 비교 연결이다. 기존 정독 matrix·reading status·연구 판단을 승격하지 않는다. [등록 범위와 source 경계](../work/update/REGISTRY_REFRESH_2026-10-25.md).

### 2026-10-25 top-tier 보완 — 읽기 전 비교 연결

> Researcher interpretation / CURATION-HYPOTHESIS. 신규 노트는 abstract/project 기반이며 아래 연결은 정독·실험 결과나 직접 citation 관계의 확인이 아니다.

[FMB](../2025/IJRR/2025_IJRR_FMB-A-functional-manipulation-benchmark-for-generalizable/01_overview.md)는 개별 grasp·reorientation·assembly와 skill 조합을 나누어 비교할 실환경 benchmark다. [Visuotactile estimation/control](../2025/CoRL/2025_CoRL_Learning-Visuotactile-Estimation-and-Control-for-Non-prehe/01_overview.md)은 가림 하 상태 추정과 uncertainty-aware control을 함께 다루므로 tactile VLA를 제안할 때 직접 대안이 된다.

[Process-centric tactile skill taxonomy](../2025/Nature-Machine-Intellige/2025_Nature-Machine-Intellige_A-process-centric-manipulation-taxonomy-for-the-organizati/01_overview.md)는 전문가 공정 명세가 주어진 skill/controller 비교 기준이다. 센서 추가, 명시적 성공/실패 조건, controller 개선을 모두 language model의 기여로 합치지 않는다. 같은 정보를 가진 단순 skill 조건·point-estimate control 이후 남는 효과를 먼저 검토한다. GAP-CONTACT·GAP-DE의 재개 조건은 바뀌지 않는다.

## Open Questions

### Controller gain과 정책 학습의 기여 분리

**2026-11-12 / 초록 기반 CURATION-HYPOTHESIS.** [Tune to Learn, RSS 2026](https://www.roboticsproceedings.org/rss22/p139.html)은 controller gain이 robot policy learning과 sim-to-real 결과에 미치는 영향을 직접 다룬다. [등록 근거](../work/update/FOUNDATION_FRONTIER_SUPPLEMENT_2026-11-12.md)의 공식 제목은 *How Controller Gains Shape Robot Policy Learning*이다. 저자 페이지의 *Affect* 표기는 별도 논문으로 추가하지 않았다.

CONTACT-RL의 gain 적응을 비교할 때는 nominal gain 한 가지보다 **동일 튜닝 비용의 고정 gain, task별 gain, 단순 feedback rule**을 먼저 대조해야 한다. BC/RL·controller authority·접촉 stiffness·sensor/loop rate 중 무엇을 바꾼 실험인지 본문에서 확인한다. 이는 gain-aware 학습의 일반 동기를 이미 다룬 선행이라는 뜻이며, 현재 후보의 구체적 동적 적응을 해결했거나 부정했다는 판정은 아니다. 기존 physics P0 상한·재개 조건을 유지한다.

<a id="gap-contact-rl-2026"></a>
### 접촉 조작에서 VLA RL과 가변 임피던스 제어

**2026-11-09 / GAP-CONTACT-RL-N2 내부 비실험 설계 완료 / 좁은 탐색 유지 / CURATION-HYPOTHESIS.** [선행 비교·과제·계약](../work/research_topics/contact_adaptation/내용/README.md)에 상세 내용을 통합했다. N1의 TacCoRL·CompVLA·TORL·ForceRFT·FORGE·ContactBench·Facet-0·CG-RL 지정 본문 대조에 CompliantVLA-adaptor 방법과 RLinf/ContactBench/Newton 선택 source 확인을 더했다. 이력 기반 VLA RL·동작/강성 공동 학습·정책/controller 효과 분리 자체의 신규성은 주장하지 않는다. 원장의 [contact_n1·contact_n2](../work/sources/vla_rl_additional_gaps_2026-11-09.json)에 확인 구간과 계약을 기록했다.

[REG-R13](../work/update/REGISTRY_MAINTENANCE_2026-11-09.md#admissions)에서 직접 선행 10편의 registry identity를 연결했다. 최신 초록과 N1 지정 본문 버전의 차이는 [주제의 source 경계](../work/research_topics/contact_adaptation/내용/README.md#registry-sync)를 따른다.

**남은 질문:** 같은 관측·실행 제약에서 동작과 강성을 함께 후학습한 VLA가, 동작만 RL로 학습하고 잘 조정한 impedance controller를 쓰는 경우보다 언제 유용한가? 단일 학습 actor를 우선하며 고정 servo는 허용한다. 작은 charger 삽입으로 현상을 먼저 살피되 VLA의 언어/작업 공유 이득과 독립 방법 기여는 미확인이다.

**N2 구체화·반론:** π₀ Flow-SDE/PPO에서 동작만 RL과 동작/관절 강성 배율 공동 RL을 동일 상호작용 비용으로 비교하고, 이득이 있으면 force-rule·7D scoring 대안을 확인한다. Task는 charger block1 삽입/손 떼기의 부분 과제이며 공식 benchmark 전체 성공률이 아니다. 강한 스프링에서 실패하는 원인이 grasp slip·접촉 방식일 수도 있다. Scripted 상단 누르기·정답 object pose/depth를 actor에 넣지 않으며 fingertip force는 모든 actor에 같은 방식으로 준다. [32D state/8D action·gain 동기화](../work/research_topics/contact_adaptation/재현%20방법/README.md#n2-interface)를 정적으로 추적했지만 runtime 연결은 미구현이다. 기존 GAP-CONTACT 센서 필요성 진단 HOLD는 유지한다.

**P0-PREP 완료·다음 P0-A:** 현재 Mac ARM64 local Docker의 NVIDIA allocation 실패를 확인하고 physics recipe·bounded sensor/gain probe·launcher를 작성했다. Docker stdlib16검사는 통과했지만 native physics/RGB/gain·정책 효과는 미검증이다. [호환 local NVIDIA 재개 경로](../work/research_topics/contact_adaptation/재현%20방법/README.md#resume)를 사용하며 전체 RL 환경·SFT/normalizer는 별도다. 내부 설계·준비 완료를 독립 기여 확인으로 확대하지 않는다. 현행 행동은 [TODO](../TODO.md)를 따른다.

현재 후보 판정은 [주제별 요약](../work/research_candidates/summaries/README.md)을 따른다. 아래 질문은 `CURATION-HYPOTHESIS`이며 재개 승인이 아니다.

**2026-10-27 GAP-S2 양팔 심사:** 양팔 marginal mode의 결합 실패는 가능한 사고실험이나 실제 VLA의 독립성 가정·실패율을 뜻하지 않는다. [TwinVLA, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/65475a59e2a2cb707c9462e8a308e980-Abstract-Conference.html)와 RDT·imaginative coordination 이후에는 joint action head·공통 mode baseline 뒤의 실제 잔여 오류가 필요하다. 이번 일반 방법은 **미채택**이며 E1 좌표/effect 정렬, D2 grasp–transport 질문으로 바뀌면 기존 gate를 따른다. [세부 비교](../work/update/VLA_GAP_RESELECTION_2026-10-27.md#3-세-질문의-채택-심사).


| 질문 | 구별할 예측 | 최소 대조·중단 조건 | 근거/판정 |
|---|---|---|---|
| Grasp–transport–place | 동일 grasp 후보와 scene geometry에서 후속 운반을 고려한 선택이 supervised outcome ranking보다 필요한가? | Attachment/planner baseline과 실패 귀속을 고정한다. 공개 native task·executor가 없는 현재 D2는 HOLD다. | [검토 근거](../work/research_candidates/2026-10-22_d2_buildup/README.md) |
| Tactile/force feedback | 실제 접촉 정보, 학습 supervision, 실행 controller 중 무엇이 개선을 설명하는가? | 단순 센서 추가·고주파화·missing-modality 처리는 이미 선행이 있다. 아래 GAP-CONTACT의 범위와 기각 조건으로 좁힌다. | 2026-10-23 외부 문헌 대조; native 효과 미검증 |
| Grasp metric의 행동 utility | Analytic contact score와 learned proposal의 순위가 compliant execution에서 언제 교차하는가? | 물체·접촉 mode별 held-out 조건과 실제 trial 분모를 확인한다. 단순 object/task 평균으로 dexterity 일반화를 주장하지 않는다. | 기존 track 비교의 연구자 질문; native 효과 미검증 |

<a id="gap-contact-2026"></a>
### GAP-CONTACT — 접촉 센서가 필요한 조건과 제어 개선으로 충분한 조건

- 갱신: **2026-10-23 GAP-R2**. 상태: **REVISE / 진단 후보 HOLD / CURATION-HYPOTHESIS**. [직접 비교 완료 기록](../work/update/CONTACT_INTERFACE_REVIEW_2026-10-23.md). 문헌 작업 완료이며 새 방법 채택이나 기존 후보 재개가 아니다.
- 질문: **관측 이력으로 구별하기 어려운 접촉 조건에서, 실측 접촉 정보가 필요한 경우와 기존 관측의 학습·controller 개선으로 충분한 경우를 실험 전에 구분할 수 있는가?**
- 가치: 답에 따라 sensor 위치·종류, 데이터 수집, VLA 입력, 저수준 controller 중 어디에 투자할지 달라져야 한다. 단순 tactile-VLA 성능 비교로 끝나면 독립 기여가 약하다.

**논문이 지지하는 범위.** [Visuotactile estimation/control, CoRL 2024](https://proceedings.mlr.press/v270/ferrandis25a.html)는 occlusion 아래 추정과 uncertainty-aware control을 연결한 VLA 밖의 비교 대상이다. [ForceVLA](https://papers.nips.cc/paper_files/paper/2025/hash/8633b46e12cc5f2ee1f05a6ca2c65b38-Abstract-Conference.html)는 force fusion, [ForceVLA2](https://arxiv.org/html/2603.15169v1)는 hybrid force-position 출력, [AT-VLA §3–4](https://arxiv.org/html/2605.07308v1)는 fast tactile feedback과 modality ablation을 이미 다룬다. [FD-VLA §III](https://arxiv.org/html/2602.02142v1)는 학습 때의 force를 vision/state-conditioned representation으로 증류한다. [ForceDelta-VLA abstract](https://arxiv.org/abs/2609.18242)는 force-conditioned action correction 증류이며 실행 중 force를 사용하므로 FD-VLA의 sensor-free inference와 구분한다.

[ContactBench 1.0 §V-A–D](https://arxiv.org/html/2610.24512v1)는 6개 실제 task 중 tactile을 수집한 4개에서 일관된 기본 성능 개선을 얻지 못했지만, 일부 숨은 기계 조건 변화에서는 RDP의 적응 이득을 보고한다. 센서 coverage·incidental cue·feedback 통합 방식까지 이미 분석하므로 **“촉각도 실패한다”와 “hidden mechanics를 시험한다” 자체는 새 공백이 아니다.** 또한 task별 specialist fine-tuning 평가이며 language-conditioned generalist 효과는 남겨 둔다. 이 결과를 ForceVLA2와 같은 조건의 상충 결과로 취급하지 않는다. ContactBench는 2026-10-17 preprint이고 채택 여부는 미확인이다.

**아직 검증되지 않은 공백 해석.** 위 연구들이 제시한 개별 설명을 넘어, 가용 관측의 구별 능력과 실행 가능한 행동의 차이로 **어떤 개입이 유효할지 다른 task에서도 예측하는 규칙**이 남는지 확인한다. 다음 세 구분이 기준이다.

| 구분할 원인 | 필요한 증거 | 설명을 무너뜨릴 대조 |
|---|---|---|
| 기존 관측에 필요한 정보가 없음 | 비슷한 RGB·proprio history에서도 요구 행동이 달라지는 물리 조건과 feasible witness | 충분한 history 또는 단순 proprio baseline만으로 같은 결정을 내릴 수 있음 |
| 센서는 정보를 갖지만 정책이 활용하지 못함 | 센서 위치·접촉 이벤트·timestamp를 확인하고 실제 입력과 조건부 shuffle을 대조 | 센서가 접촉 부위를 관측하지 못하거나 shuffle이 비현실적 분포만 만듦 |
| 정책 정보보다 실행 controller가 병목 | 같은 observation·시간·action 제한에서 controller만 바꾼 비교 | 고전적인 compliance/force controller로 차이가 모두 설명됨 |

향후 비교는 **학습 force supervision / VLA의 실행 입력 / 저수준 controller의 실행 입력**을 별도 열로 둔다. VLA에 force를 안 넣어도 하위 force controller가 센서를 사용하면 전체 시스템은 sensor-free가 아니다. Fingertip tactile과 wrist F/T는 다른 관측이며 대체 가능한 modality로 묶지 않는다. 같은 task·robot·train split·backbone·학습/추론 예산을 먼저 맞추고, 센서 미사용·force-distilled·실측 입력 및 단순 controller를 비교한다. Privileged mechanics는 원인 진단용으로만 쓰며 policy-visible input에 섞지 않는다.

**중단 조건.** ContactBench/AT-VLA/ForceVLA2 등의 부록·code가 이미 같은 개입과 held-out 예측을 제시하거나, 결과가 기존 관측 가능성·고전 제어의 설명을 반복하면 새 연구로 채택하지 않는다. 유용한 예측 규칙 없이 sensor/backbone별 평균 순위만 남아도 축소한다. 공개 task·센서 log·동일 controller를 묶은 실행 구성은 미확보이며 runtime은 미검증이다.

**GAP-R2 판단:** 8편의 지정 본문/부록과 공개 interface를 대조했다. 기존 연구와 다른 예측을 확보하지 못해 새 방법 착수는 보류한다. 문헌상 task 후보인 doorknob variation도 모든 조건에 통하는 보수적 행동을 배제하지 않으면 센서의 필요성을 증명하지 못한다는 것이 **이번 연구자 해석**이다. [검토의 task 계약·기각 조건](../work/update/CONTACT_INTERFACE_REVIEW_2026-10-23.md#6-task-하나를-골라도-곧바로-센서-필요성을-증명할-수는-없다). 충분한 history/proprio·고전 feedback과 달리 미관측 task/기계 조건에서 개입 선택을 예측할 근거가 생길 때만 재검토한다. Hardware·동기화·calibration·공정한 실행 자산도 필요해 GPU만으로 재개하지 않는다. 후속 심사와 현재 인계는 [TODO](../TODO.md)를 따른다.

**공개 자산 경계:** [GAP-R2 code/source audit](../work/sources/contact_interface_review_2026-10-23.json)에서 ForceVLA의 force 입력 경로·추론 코드 불일치, TaF-VLA의 공개 tactile dataset과 미확보 정책 구현을 구분했다. Code 정적 검토는 실행 검증이 아니다. TaF-VLA의 journal status는 독립 확인하지 못해 preprint로 유지한다. 범용 VLA로 확장하려면 instruction/task별 utility가 필요하며 specialist contact 성능만으로 대체할 수 없다. [GAP-LATENT](./04_vla_generalist.md#gap-latent-2026)는 학습용 영상 표현/추가 supervision, 이 질문은 실행 시 정보와 controller 투자 선택이 중심이다.

<a id="gap-deform-2026"></a>
### GAP-DEFORM — 물성·고정 조건의 모호성이 언제 추가 탐색을 필요로 하는가?

- 갱신: **2026-10-24, GAP-DE2 DONE**. **현재 공개 자산 기반 설계 종료·문헌 진단 HOLD / 일반 방법 NO-GO / native VLA HOLD**. [DE1 문헌 비교](../work/update/DEFORMABLE_IDENTIFICATION_REVIEW_2026-10-24.md) 뒤 [DE2 자료 충분성 심사](../work/update/DEFORMABLE_ASSET_SUFFICIENCY_REVIEW_2026-10-24.md)를 완료했다. 직접 충돌 판단은 지정 본문에 근거하며 조건 예측은 여전히 `CURATION-HYPOTHESIS`다. 실험으로 가설을 반박하거나 읽기 status를 승격한 것은 아니다.
- **기존 질문의 수정:** [JIGGLE §IV-C·VI](https://arxiv.org/html/2405.09743v1)의 joint는 state와 boundary다. [AdaptiGraph Appendix C.1](https://arxiv.org/html/2407.07889v1)과 [DPSI](https://journals.sagepub.com/doi/full/10.1177/02783649251334661)는 물성과 마찰의 공동 추정을 이미 다룬다. Material·friction·attachment 위치/강도·현재 state·model class를 구분하며, 일반 joint estimation의 부재를 주장하지 않는다.
- **가장 강한 충돌:** [IJRR 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4324691/)에 boundary active exploration, [RSS 2020](https://roboticsproceedings.org/rss16/p085.html)에 task-oriented exploration이 있다. AdaptiGraph Appendix C.2는 uncertainty probe와 최대 변위 heuristic 사이의 사후 분산 우위가 일관되지 않음을 보고한다. “task에 필요한 정보만 얻자”는 원리 자체도 새 기여가 아니다.
- **남겨 둔 질문 — 연구자 해석:** 같은 행동 전 관측 이력에 부합하는 material–attachment 조합에서, **목표/제약에 따른 feasible 행동 불일치**가 추가 probe의 순이득을 예측하는가? 새로운 조합에서도 fixed/max-displacement probe·충분한 history feedback·기존 task-oriented exploration·[robust control](https://roboticsproceedings.org/rss22/p061.html)·[ILC](https://roboticsproceedings.org/rss22/p126.html) 이후에 남는 조건 예측이 필요하다. 관측상 유사성과 실제 행동 차이를 연결한 사례는 아직 미확보다.
- **최소 비교·기각:** benign elastic object에서 material/attachment/task를 분리하고 정책이 보는 history·proprio·force까지 맞춘다. 공통 안전 행동이 있으면 식별 필요성을 주장하지 않는다. Probe의 직접 작업 진행 효과와 정보 효과를 분리하고 force·변위·시간·reset·계산 비용을 기록한다. Task success/제약 위반을 주 지표로 두며 parameter error는 보조다. Oracle에서도 실패하면 정책/제어 전제를 먼저 수정한다. [비교 계약 초안](../work/update/DEFORMABLE_IDENTIFICATION_REVIEW_2026-10-24.md#6-최소-비교-계약-초안--실행-manifest가-아님)은 executable=false다.
- **VLA·공개 자산 경계:** PGND의 text는 확인한 code에서 segmentation 입력이며 instruction-conditioned policy 근거가 아니다. FORM의 일부 positions-only 비교는 탄성값을 가정한다. PhysCoRe의 CoRL 2026 표기는 독립 확인하지 못했다. Native VLA에는 실제 목표/제약을 바꾸는 task pair와 정책 기본 능력이 추가로 필요하다. GPU만으로 fixture·동기화·공정 비교가 해결되지 않는다.
- **DE2에서 확인한 자료 경계:** AdaptiGraph의 cloth 생성은 물성과 마찰을 결합하고 `boundary_points`는 grasp 후보인 가장자리다. H5 timestamp는 frame 수이며 실행 후 버리는 시도의 총 비용 보존이 불충분하다. PGND는 버전 고정 데이터/모델을 제공하지만 trajectory window를 독립 시행으로 세지 않아야 하며, 지정 전처리에는 선택한 camera timestamp와 복사 image index가 달라질 수 있는 경로가 있다. 실제 payload의 영향은 미측정이다. DPSI의 workspace/table boundary와 JIGGLE의 환경 attachment도 구분했다. [고정 source·구간·한계](../work/sources/deformable_asset_sufficiency_review_2026-10-24.json).
- **종료·재개:** 독립 material/anchor 조건과 행동 전 관측·실제 command/시간/시도 비용·goal evaluator가 함께 있는 비교 구성은 미확보다. [재사용/새 수집 범위](../work/update/DEFORMABLE_ASSET_SUFFICIENCY_REVIEW_2026-10-24.md#6-무엇을-재사용하고-무엇을-새로-만들어야-하는가)를 남기고 현재 설계를 종료했다. 새 source 또는 구체 수집 계획과 단순 대안 이후 차별적 예측이 있을 때 재심사한다. 효과를 미리 입증할 필요는 없지만 GPU·같은 metadata 재조회로 DE3/학습을 자동 시작하지 않는다. [GAP-S1 중간 종합](../work/update/VLA_GAP_SELECTION_REVIEW_2026-10-24.md)은 현재 채택 후보 없음으로 완료했다. 현재 인계는 [TODO](../TODO.md)의 GAP-N1 WAITING_EVIDENCE다.
