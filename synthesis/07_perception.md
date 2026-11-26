# 3D 인식

- Updated: 2026-10-23 KST

## Scope

Rigid registration, point-cloud representation, feed-forward geometry, SLAM, dense correspondence, semantic mapping, 3D scene graphs, active perception, articulation flow와 3D-aware VLA를 downstream robot behavior 관점에서 비교한다.

### Taxonomy boundary and curation schema

- **Primary axis:** geometric state estimation → spatial/semantic memory → active perception → planning or policy interface.
- **In scope:** 3D perception and representation that changes robot localization, navigation, manipulation, active sensing, collision avoidance or policy input, plus the benchmark needed to evaluate that interface.
- **Out of scope:** reconstruction/rendering quality alone, language-vision representation without a robot downstream contract, 또는 generic 3D benchmark whose action consequence is not identified.
- **Inclusion test:** input geometry, spatial state, temporal update, semantic uncertainty, downstream action/planning interface와 robot-level consequence 중 최소 네 가지를 비교할 수 있어야 한다.
- **Role vocabulary:** `foundation`, `representation`, `state estimator`, `mapping`, `scene graph`, `active perception`, `policy`, `benchmark`, `dataset`, `system`을 사용한다.

공통 matrix/evidence 규약은 [synthesis 안내](./README.md#공통-비교-규약과-질문-분류)를 따른다.

## Reading Path

현재 읽기 우선순위는 [READING_PLAN.md](../research/READING_PLAN.md)를 따른다. 아래 계보는 비교 탐색용이며 전체 선행 완독 의무가 아니다.

2026-10-19 초점: ConceptFusion·RVT·VLFM·VLN-CE를 중심으로 spatial representation이 manipulation/navigation 실행을 바꾸는 조건을 비교한다. DP3·spatial VLA와 연결하되 reconstruction 점수만으로 priority를 올리지 않는다.

ICP → PointNet → DROID-SLAM/3DGS/DUSt3R/VGGT → Dense Object Nets/NDF/DenseMatcher → ConceptFusion/VLMaps/Open3DSG → Where2Act/FlowBot3D/RVT → PointVLA/Any3D-VLA/ActiveVLA.

### 2026-10-19 추가 논문 비교

아래는 등록된 abstract/project 근거에서 만든 **정독 전 비교 질문**이다. 직접 citation이나 실험 결론으로 취급하지 않으며, 읽기 순서와 tier는 READING_PLAN의 최신 값을 따른다.

| 비교할 논문 | 비교 축 | 본문에서 확인할 조건 |
|---|---|---|
| [LoGoPlanner](../2026/ICRA/2026_ICRA_LoGoPlanner-Localization-Grounded-Navigation-Policy-with-M/01_overview.md) / VLFM·VLN-CE ↔ [PointWorld](../2026/CVPR/2026_CVPR_PointWorld-Scaling-3D-World-Models-for-In-The-Wild-Robotic/01_overview.md) | Localization/metric geometry와 action-conditioned 3D dynamics | Pose 오차·scale·map 갱신이 navigation collision과 manipulation planning에 주는 효과를 비교한다. PointWorld의 primary queue는 world-model 트랙이다. |

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### Robotics-enabling 3D perception — 4

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [ConceptFusion: Open-set Multimodal 3D Mapping](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) | 2023 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [RVT: Robotic View Transformer for 3D Object Manipulation](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) | 2023 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](../2024/ICRA/2024_ICRA_VLFM-Vision-Language-Frontier-Maps-for-Zero-Shot-Semantic/01_overview.md) | 2024 / ICRA | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments](../2011-2020/2020/ECCV/2020_ECCV_Beyond-the-Nav-Graph-Vision-and-Language-Navigation-in-Con/01_overview.md) | 2020 / ECCV | `UNREAD` | `FULL_TEXT_CHECKED` |

### Active and embodied 3D Vision — 36

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| NEXT | [LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry](../2026/ICRA/2026_ICRA_LoGoPlanner-Localization-Grounded-Navigation-Policy-with-M/01_overview.md) | 2026 / ICRA | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](../2011-2020/2018/CVPR/2018_CVPR_Vision-and-Language-Navigation-Interpreting-Visually-Groun/01_overview.md) | 2018 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](../2011-2020/2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) | 2017 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) | 2021 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Where2Act: From Pixels to Actions for Articulated 3D Objects](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md) | 2021 / ICCV | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md) | 2022 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Ditto: Building Digital Twins of Articulated Objects from Interaction](../2022/CVPR/2022_CVPR_Ditto-Building-Digital-Twins-of-Articulated-Objects-from-I/01_overview.md) | 2022 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Visual Language Maps for Robot Navigation](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) | 2023 / ICRA | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SUGAR: Pre-training 3D Visual Representations for Robotics](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md) | 2024 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](../2025/T-RO/2025_T-RO_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) | 2025 / T-RO | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](../2025/CVPR/2025_CVPR_RoboSpatial-Teaching-Spatial-Understanding-to-2D-and-3D-Vi/01_overview.md) | 2025 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [PointVLA: Injecting the 3D World into Vision-Language-Action Models](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) | 2026 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics](../2025/RSS/2025_RSS_Vysics-Object-Reconstruction-Under-Occlusion-by-Fusing-Vis/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery](../2021/ICCV/2021_ICCV_Act-the-Part-Learning-Interaction-Strategies-for-Articulat/01_overview.md) | 2021 / ICCV | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects](../2023/NeurIPS/2023_NeurIPS_Where2Explore-Few-shot-Affordance-Learning-for-Unseen-Nove/01_overview.md) | 2023 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Clio: Real-time Task-Driven Open-Set 3D Scene Graphs](../2024/RA-L/2024_RA-L_Clio-Real-time-Task-Driven-Open-Set-3D-Scene-Graphs/01_overview.md) | 2024 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](../2025/RA-L/2025_RA-L_HAMMER-Heterogeneous-Multi-Robot-Semantic-Gaussian-Splatti/01_overview.md) | 2025 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting](../2026/RA-L/2026_RA-L_VISTA-Open-Vocabulary-Task-Relevant-Robot-Exploration-with/01_overview.md) | 2026 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics](../2025/NeurIPS/2025_NeurIPS_RoboRefer-Towards-Spatial-Referring-with-Reasoning-in-Visi/01_overview.md) | 2025 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Volumetric Environment Representation for Vision-Language Navigation](../2024/CVPR/2024_CVPR_Volumetric-Environment-Representation-for-Vision-Language/01_overview.md) | 2024 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation](../2025/ICCV/2025_ICCV_IGL-Nav-Incremental-3D-Gaussian-Localization-for-Image-goa/01_overview.md) | 2025 / ICCV | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](../2025/ICCV/2025_ICCV_Move-to-Understand-a-3D-Scene-Bridging-Visual-Grounding-an/01_overview.md) | 2025 / ICCV | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](../2025/ICCV/2025_ICCV_PhysTwin-Physics-Informed-Reconstruction-and-Simulation-of/01_overview.md) | 2025 / ICCV | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects](../2024/CVPR/2024_CVPR_FoundationPose-Unified-6D-Pose-Estimation-and-Tracking-of/01_overview.md) | 2024 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Active 6D pose estimation for textureless objects using multi-view RGB frames](../2026/IJRR/2026_IJRR_Active-6D-pose-estimation-for-textureless-objects-using-mu/01_overview.md) | 2026 / IJRR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [RFMPose: Generative Category-level Object Pose Estimation via Riemannian Flow Matching](../2025/NeurIPS/2025_NeurIPS_RFMPose-Generative-Category-level-Object-Pose-Estimation-v/01_overview.md) | 2025 / NeurIPS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction](../2026/RSS/2026_RSS_Robo3R-Enhancing-Robotic-Manipulation-with-Accurate-Feed-F/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Robotic task success evaluation under multi-modal non-parametric object pose uncertainty](../2025/Industrial-Robot/2025_Industrial-Robot_Robotic-task-success-evaluation-under-multi-modal-non-para/01_overview.md) | 2025 / Industrial Robot | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [ActivePose: Active 6D Object Pose Estimation and Tracking for Robotic Manipulation](../2025/arXiv/2025_arXiv_ActivePose-Active-6D-Object-Pose-Estimation-and-Tracking-f/01_overview.md) | 2025 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Imagine then Verify: Affordance-Targeted Active Perception for Task-Oriented Grasping in Cluttered Scenes](../2026/arXiv/2026_arXiv_Imagine-then-Verify-Affordance-Targeted-Active-Perception/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control](../2026/arXiv/2026_arXiv_Estimate-Don-t-Imitate-Reusing-Differentiable-State-Based/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Vision in Action: Learning Active Perception from Human Demonstrations](../2025/CoRL/2025_CoRL_Vision-in-Action-Learning-Active-Perception-from-Human-Dem/01_overview.md) | 2025 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Active Perception for Grasp Detection via Neural Graspness Field](../2024/NeurIPS/2024_NeurIPS_Active-Perception-for-Grasp-Detection-via-Neural-Graspness/01_overview.md) | 2024 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation](../2025/CoRL/2025_CoRL_UniTac2Pose-A-Unified-Approach-Learned-in-Simulation-for-C/01_overview.md) | 2025 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation](../2025/RSS/2025_RSS_ViTaSCOPE-Visuo-tactile-Implicit-Representation-for-In-han/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [ActiveMimic: Egocentric Video Pretraining with Active Perception](../2026/CoRL/2026_CoRL_ActiveMimic-Egocentric-Video-Pretraining-with-Active-Perce/01_overview.md) | 2026 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |

<!-- READING_QUEUE:END -->

## Historical curation — 2026-09-02

아래는 해당 날짜의 변경 이력이다. 현재 membership과 수량은 위 generated queue를 따른다.

`VLFM`, `Volumetric Environment Representation`, `IGL-Nav`, `Move to Understand`를 `NEXT`에 반영했다. 이들은 3D map/reconstruction을 navigation, image-goal localization, active exploration의 decision loop에 연결한다. 반대로 `VGGT`, `Open3DSG`, `EmbodiedSplat`은 generic geometry/scene representation의 가치가 크지만 현재 reported robot behavior contribution이 제한되어 `REFERENCE`로 이동했다.

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래는 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. `Paper` 링크는 local overview를 가리키고, official paper/project/code URL은 해당 note header에서 확인한다.
>
> Row convention: 한 행은 한 registry paper이다. `State / action / objective / timing`은 고정 순서로 기록하고, `Evaluation`은 `setup; data/split; metric; real/trials` 순서를 따른다. `Evidence / source`가 `CURATION-SEED`이면 수치나 세부 조건을 아직 주장하지 않는다.

| Paper | Year / Venue | Role | Facets | Problem | State / action / objective / timing | Why included / TL;DR | Evaluation (setup; data/split; metric; real/trials) | Evidence / source | Failure / assumption | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|---|
| [ICP](../1960-2010/1992/IEEE-Transactions-on-Pat/1992_IEEE-Transactions-on-Pat_A-Method-for-Registration-of-3-D-Shapes/01_overview.md) | 1992 / IEEE Transactions on Pattern Analysis and Machine Intelligence | foundation; formulation | generic 3D; point sets; model-based; registration | rigid alignment of partially matched 3D shapes | point/shape sets and rigid transform; pose/map estimate; alignment objective; iterative update | classical registration and pose-consistency baseline | shape registration; data/split=UNVERIFIED; metric=alignment error; real=no/trials=— | `CURATION-SEED`; overview + queue | initialization, overlap, outliers, local minima | learned geometry와 classical consistency를 비교 |
| [PointNet](../2011-2020/2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) | 2017 / CVPR | foundation; representation | generic 3D; point cloud; sim/real; point-set encoder | unordered point-set representation | point set feature; downstream action/state; classification/segmentation objective; per-observation | point-set encoder의 robotics input 기준점 | 3D classification/segmentation; data/split=benchmark splits; metric=accuracy/IoU; real/sim=UNVERIFIED/trials=— | `CURATION-SEED`; overview + queue | permutation handling, occlusion, domain shift | 동일 policy head로 2D와 3D input을 ablate |
| [RVT](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) | 2023 / CoRL | policy; representation | tabletop arm; RGB-D/multi-view; real/sim; manipulation policy | action-centric multi-view 3D manipulation | rendered multi-view tokens and task state; 3D action; imitation objective; per-step loop | 3D representation을 action prediction에 직접 연결 | tabletop manipulation; data/split=task/object splits; metric=task success; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | sensor/data confound, view coverage, calibration | representation과 policy head를 함께 비교 |
| [DROID-SLAM](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) | 2021 / NeurIPS | state estimator; method | mobile robot; monocular/stereo/RGB-D; real/sim; SLAM | online camera state estimation | image sequence; camera pose/depth/map; tracking/reconstruction objective; recurrent iterative update | robot state estimator와 downstream planning의 geometry baseline | SLAM datasets; data/split=sequence splits; metric=pose/depth; real/sim=UNVERIFIED/trials=— | `CURATION-SEED`; overview + queue | dynamic scenes, scale/calibration, stale state | pose uncertainty를 downstream decision에 전달 |
| [DUSt3R](../2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md) | 2024 / CVPR | foundation; representation | generic 3D; multi-view images; real/sim; feed-forward geometry | feed-forward multi-view geometry without calibrated setup | image pair/sequence; point map and camera geometry; geometric reconstruction objective; feed-forward inference | geometry accuracy와 latency의 새로운 state interface | multi-view geometry; data/split=benchmark splits; metric=pose/depth/reconstruction; real/sim=UNVERIFIED/trials=— | `CURATION-SEED`; overview + queue | scale, calibration, dynamic object, downstream freshness | feed-forward geometry를 robot state 후보로 평가 |
| [VGGT](../2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md) | 2025 / CVPR | foundation; state estimator | generic 3D; multi-view images; real/sim; transformer geometry | transformer-based visual geometry prediction | multi-view image tokens; camera/depth/point geometry; supervised geometry objective; feed-forward inference | geometry foundation을 robot state estimation과 연결 | multi-view geometry; data/split=benchmark splits; metric=pose/depth; real/sim=UNVERIFIED/trials=— | `CURATION-SEED`; overview + queue | dynamic scene, calibration, scale, computation | representation quality와 control consequence를 분리 |
| [ConceptFusion](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) | 2023 / RSS | mapping; representation | mobile robot; RGB-D+language; real/sim; semantic mapping | open-vocabulary 3D mapping | spatial map with language-aligned features; queried object/location target; map fusion objective; online update | semantic map을 navigation/manipulation target interface로 사용 | scene mapping; data/split=UNVERIFIED; metric=retrieval/localization/task success; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | semantic confidence, staleness, occlusion | language map에 uncertainty와 expiry를 추가 |
| [VLMaps](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) | 2023 / ICRA | mapping; system | mobile robot; RGB-D+language; real/sim; navigation | visual-language map for semantic navigation | map with language features; language query to navigation target; map alignment objective; online query/update | language grounding을 navigation action으로 닫는 기준 | navigation scenes; data/split=UNVERIFIED; metric=localization/navigation success; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | map alignment, semantic ambiguity, stale state | semantic retrieval과 path feasibility 분리 |
| [3D Gaussian Splatting](../2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md) | 2023 / SIGGRAPH | foundation; representation | generic 3D; multi-view images; simulation/rendering; scene representation | real-time radiance-field scene representation | multi-view images and Gaussians; rendered scene/query; reconstruction/rendering objective; optimized/offline update | rendering speed과 robot map use의 representation baseline | scene reconstruction; data/split=benchmark scenes; metric=rendering/geometry; real=no/trials=— | `CURATION-SEED`; overview + queue | visual fidelity vs free-space safety, dynamic scene, map query | neural rendering과 conservative occupancy를 분리 |
| [Splat-Nav](../2025/T-RO/2025_T-RO_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) | 2025 / T-RO | system; planner interface | mobile robot; RGB-D/3DGS; real/sim; navigation | safe real-time navigation in Gaussian maps | Gaussian scene and free-space state; collision-aware path; navigation/safety objective; online query/planning | 3D representation을 safety-aware navigation으로 연결 | navigation scenes; data/split=UNVERIFIED; metric=collision/success/latency; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | visual/free-space mismatch, dynamic objects, latency | representation quality와 collision certificate 분리 |
| [Perceiver-Actor](../2022/CoRL/2022_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md) | 2023 / CoRL | policy; representation | arm; RGB-D/3D tokens; simulation; multi-task action | multi-task 3D action prediction | voxel/3D token and task context; 6-DoF action; imitation objective; per-step loop | 3D token과 multi-task action interface 기준 | tabletop manipulation; data/split=task/object splits; metric=multi-task success; real=no/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | simulator bias, token resolution, task interference | common action head로 representation을 비교 |
| [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) | 2026 / CVPR | policy; active perception | arm; vision+language+3D; real/sim; active sensing | action-relevant view acquisition for manipulation | task-conditioned 3D observation; camera/view plus manipulation action; task success/value-of-information; active re-observation loop | perception–action loop을 sensing cost까지 포함해 평가 | precise manipulation; data/split=UNVERIFIED; metric=success/sensing cost/latency; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | sensing delay, occlusion, view/action coupling | value-of-information을 action change와 budget으로 정의 |


## Dependency and Evolution

아래 계보는 3D benchmark의 발전 자체보다 representation이 robot state와 action interface로 들어가는 과정을 나타낸다. 직접 citation 관계는 정독 시 확인한다.

### Relation type index

아래 label은 바로 다음 계보 표의 chain anchor에 적용한다. `formulation`, `method`, `data`, `evaluation`, `deployment`는 개념적 연결의 종류이며 citation 또는 직접 영향 관계를 뜻하지 않는다.

| Chain anchor | Relation type | Interpretation |
|---|---|---|
| ICP → DROID-SLAM/DUSt3R/VGGT | formulation → state estimator | rigid registration이 learned temporal/feed-forward geometry로 확장 |
| PointNet → RVT/SUGAR → PointVLA/Any3D-VLA | representation → policy interface | point-set representation이 3D robot policy input으로 확장 |
| DROID-SLAM/3DGS/DUSt3R → VGGT → Splat-Nav/EmbodiedSplat | representation → deployment | geometry foundation이 online map과 navigation safety로 연결 |
| ConceptFusion/VLMaps → Open3DSG → SayPlan/MomaGraph | mapping → planning/memory | semantic map이 relation graph와 language planning memory로 확장 |
| Where2Act → FlowBot3D → DenseMatcher/G3Flow/EquAct | affordance → policy transfer | articulation affordance가 correspondence와 equivariant action으로 확장 |
| Dense Object Nets → NDF → DenseMatcher | representation → correspondence method | dense descriptor가 equivariant category correspondence로 확장 |
| passive 3D input → ActiveVLA | perception → action | passive geometry가 view-selection decision loop로 확장 |
| RLBench → Perceiver-Actor/RVT | benchmark → policy evaluation | standardized task가 3D action representation 비교 substrate가 됨 |

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| [ICP](../1960-2010/1992/IEEE-Transactions-on-Pat/1992_IEEE-Transactions-on-Pat_A-Method-for-Registration-of-3-D-Shapes/01_overview.md) → feature/robust registration → [DROID-SLAM](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) / [DUSt3R](../2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md) / [VGGT](../2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md) | explicit closest-point correspondence와 rigid fitting에서 learned iterative state estimation 및 feed-forward multi-view pose/geometry prediction으로 확장된다. | learned geometry가 poor initialization, dynamic object, scale/calibration shift에서 classical failure를 실제로 줄이는가 |
| [PointNet](../2011-2020/2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) → [RVT](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) / [SUGAR](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md) → [PointVLA](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) / [Any3D-VLA](../2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/01_overview.md) | unordered point-set representation에서 action-centric 3D token, robotics pretraining과 generalist VLA input으로 확장된다. | representation, 추가 depth sensor와 data augmentation의 효과를 분리할 수 있는가 |
| [DROID-SLAM](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) / [3D Gaussian Splatting](../2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md) / [DUSt3R](../2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md) → [VGGT](../2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md) → [Splat-Nav](../2025/T-RO/2025_T-RO_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) / [EmbodiedSplat](../2026/CVPR/2026_CVPR_EmbodiedSplat-Online-Feed-Forward-Semantic-3DGS-for-Open-V/01_overview.md) | iterative state estimation, differentiable rendering과 pairwise geometry가 feed-forward multi-view geometry 및 online semantic map으로 수렴한다. | offline geometry quality가 dynamic online state, planning latency와 safety에 그대로 전달되는가 |
| [ConceptFusion](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) / [VLMaps](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) → [Open3DSG](../2024/CVPR/2024_CVPR_Open3DSG-Open-Vocabulary-3D-Scene-Graphs-from-Point-Clouds/01_overview.md) → [SayPlan](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) / [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) | open-vocabulary feature map에서 object/relation graph와 state-aware language planning memory로 확장된다. | semantic confidence, temporal freshness와 geometric feasibility가 plan에 함께 전달되는가 |
| [Where2Act](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md) → [FlowBot3D](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md) → [DenseMatcher](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) / [G3Flow](../2025/CVPR/2025_CVPR_G3Flow-Generative-3D-Semantic-Flow-for-Pose-aware-and-Gene/01_overview.md) / [EquAct](../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) | affordance point에서 articulation flow, semantic correspondence와 equivariant action policy로 확장된다. | semantic/geometric correspondence가 contact feasibility와 cross-category task success를 충분히 제약하는가 |
| [Dense Object Nets](../2011-2020/2018/CoRL/2018_CoRL_Dense-Object-Nets-Learning-Dense-Visual-Object-Descriptors/01_overview.md) → [Neural Descriptor Fields](../2022/ICRA/2022_ICRA_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md) → [DenseMatcher](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) | self-supervised dense image/surface descriptor가 SE(3)-equivariant object field와 category-level semantic correspondence로 확장된다. | correspondence metric 향상이 grasp/contact success와 recovery under occlusion에 인과적으로 연결되는가 |
| passive 3D input → [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) | 관측된 geometry를 소비하는 policy에서 task-relevant view를 직접 선택하는 perception–action loop로 이동한다. | 추가 view의 sensing cost와 action decision value를 동일 budget에서 평가하는가 |
| [RLBench](../2011-2020/2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) → [Perceiver-Actor](../2022/CoRL/2022_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md) / [RVT](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) | 표준화된 multi-task RGB-D manipulation suite가 voxel 및 multi-view 3D action representation을 비교하는 공통 evaluation substrate가 된다. | simulator success가 real sensing noise, calibration error와 contact robustness를 얼마나 예측하는가 |

## 2026-10-23 근거 통합

아래는 2026-10-22까지의 registry/source 감사와 후보 검토를 연결한 연구자 해석이다. 새 정독·효과 검증·직접 citation 관계의 확인을 뜻하지 않는다. Paper별 본문 확인 범위는 overview 및 연결된 dossier를 따른다.

| 비교 축 | 등록된 선행 | 현재 남길 구분 |
|---|---|---|
| C1: active perception의 직접 선행 | [ActiveAlign](../2026/arXiv/2026_arXiv_Look-Before-You-Act-Bridging-Active-Perception-and-Vision/01_overview.md) (2026 arXiv); [EyeRobot 2.0](../2026/arXiv/2026_arXiv_EyeRobot-2.0-Active-Gaze-for-Precise-Manipulation-without/01_overview.md) (2026 arXiv) | 추가 관측과 policy adaptation의 결합이 이미 있다. 이미지 개선을 native continuation 개선으로 자동 연결하지 않는다. |
| D1/D2: 행동에 필요한 geometry | [WBAG](../2026/arXiv/2026_arXiv_WBAG-A-Whole-Body-and-Attached-Geometry-Safety-Framework-f/01_overview.md) (2026 arXiv); [Cooperative Grasping](../2026/RA-L/2026_RA-L_Cooperative-Grasping-for-Collective-Object-Transport-in-Co/01_overview.md) (2026 RA-L) | 공간 표현의 완성도보다 correction 선택·collision·운반 가능한 grasp에 필요한 정보와 비용을 비교한다. |

### Registry 연결 갱신 — 2026-10-25

- [Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation](../2024/ECCV/2024_ECCV_Robo-ABC-Affordance-Generalization-Beyond-Categories-via-S/01_overview.md)

Robo-ABC는 contact correspondence를 실제 manipulation에 연결하는 참조다. 시각 대응의 정확도와 도달 가능성·파지 실행 성공을 분리한다.

이번 등록은 `ABSTRACT_CHECKED` 수준의 비교 연결이다. 기존 정독 matrix·reading status·연구 판단을 승격하지 않는다. [등록 범위와 source 경계](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/REGISTRY_REFRESH_2026-10-25.md).

### 2026-10-25 top-tier 보완 — 읽기 전 비교 연결

> Researcher interpretation / CURATION-HYPOTHESIS. 신규 노트는 abstract/project 기반이며 아래 연결은 정독·실험 결과나 직접 citation 관계의 확인이 아니다.

[PhysTwin](../2025/ICCV/2025_ICCV_PhysTwin-Physics-Informed-Reconstruction-and-Simulation-of/01_overview.md)을 AdaptiGraph·JIGGLE와 연결한다. 영상 재현에 맞는 geometry/appearance, 역추정된 물리 특성, 새로운 interaction의 예측, 실제 planning utility를 별도 축으로 읽는다.

동일한 영상 적합도를 갖는 모델들의 action ranking이 다른지 확인해야 reconstruction을 robot behavior의 근거로 연결할 수 있다. 새로운 state/material/boundary 증거 없이 GAP-DE의 종료된 자산 심사를 반복하지 않는다.

## Open Questions

<a id="pose-reconstruction-2026"></a>
### 물체 pose 모호성과 작업에 필요한 geometry — 2026-11-17

**CURATION-HYPOTHESIS / 추가 탐색, 새 정독·실험 결과 아님.** [DISaM](https://proceedings.mlr.press/v270/dass25a.html)은 행동 불확실성에 따른 관측, [ATAP](https://arxiv.org/html/2609.23504v1)은 affordance 가설의 다음 시점 검증, [Naik 등](https://arxiv.org/abs/2403.10874)은 pose 오차와 허용 오차 분포의 성공 평가를 이미 다룬다. 남을 수 있는 질문은 **여러 pose에서 공통으로 성공하는 행동의 존재**를 학습하면 pose entropy·action disagreement와 달리 불필요한 재관측을 줄일 수 있는가다. N1에서 **공통 성공 행동 선택 원리도 기존 허용 오차 평가의 확장으로 구현 가능**함을 확인해, 공유 VLA 표현의 성공 양립성 학습이 같은 label의 lookup/분리 classifier보다 유용한지로 좁혔다. DISaM은 context별 행동 분포 간 KL이므로 같은 다봉 분포는 높은 원시 분산에도 KL이 0일 수 있다. Valid multimodality는 승리 예측이 아닌 음성 대조다. 네 사례는 논리 명세이며 측정 결과가 아니다. [POSE-ACTIVE의 선행·사례·대안](../work/research_topics/pose_active_perception/내용/README.md). N2는 실제 VLA의 4-step 후보, pose 집합과 성공 label, 배치/방향 evaluator를 명세했다. 원 VLA에 pose 조건이 없으므로 같은 RGB 반복 점수를 pose별 KL로 쓰지 않는다. Frozen feature head는 진단이며 공동 정책 학습과 구별한다. [N2 결과](../work/research_topics/pose_active_perception/내용/README.md#n2-result)와 [P0 코드 준비](../work/research_topics/pose_active_perception/내용/README.md#p0-preparation-result)를 마쳤다. 현재 local daemon 연결 실패로 native 검증 대기이며, 작성한 evaluator fixture를 실제 pose ambiguity·정책 성공의 증거로 세지 않는다.

**2026-11-18 TASK-GEOMETRY-N1 / CURATION-HYPOTHESIS.** [Robo3R](https://roboticsproceedings.org/rss22/p056.html)·[GeoPredict](https://arxiv.org/html/2512.16811v1)·[PRISM](https://arxiv.org/html/2610.14704v1)에 더해 [Estimate, Don't Imitate](https://arxiv.org/html/2609.34018v1)의 정책 민감도 기반 추정 학습, [geometry 영향 분석](https://arxiv.org/html/2605.24642v1)의 reconstruction-quality/성공률 비교를 확인했다. 일반적인 task-aware geometry loss나 단순 상관 분석으로는 기여가 부족하다. 질문을 **동일 state·정책에서 입력 geometry 오류를 개입하고 ROI·보정·행동 일치 이후 작업별 잔여 실패를 설명할 수 있는가**로 좁혔다. [내용·판정](../work/research_topics/task_geometry_estimation/내용/README.md#n1-result)은 REVISE 후 작은 진단 CONTINUE다. SpatialVLA는 camera-depth·area 축소·두 no-grad 경계를 가지므로 임의 robot-frame XYZ나 바로 미분 가능한 geometry 경로로 간주하지 않는다. [P0 코드·재개 명령](../work/research_topics/task_geometry_estimation/재현%20방법/README.md#resume)까지 작성했다. Depth 입력 개입은 구현 준비, 기본 조작 능력·native 효과는 미확보다. 새 launcher는 daemon 실패로 중단됐으며 실험 결과는 없다. 1번보다 어렵다는 판단은 유보하며 C/D/E의 기존 gate·읽기 상태는 유지한다.

**2026-11-18 등록 연결 / CURATION-HYPOTHESIS.** [FoundationPose](../2024/CVPR/2024_CVPR_FoundationPose-Unified-6D-Pose-Estimation-and-Tracking-of/01_overview.md)·[RFMPose](../2025/NeurIPS/2025_NeurIPS_RFMPose-Generative-Category-level-Object-Pose-Estimation-v/01_overview.md)는 pose 가설의 생성/점수 가정, [ActiveODPE](../2026/IJRR/2026_IJRR_Active-6D-pose-estimation-for-textureless-objects-using-mu/01_overview.md)는 pose 정확도 중심 관측, [다봉 pose 불확실성의 task 성공 평가](../2025/Industrial-Robot/2025_Industrial-Robot_Robotic-task-success-evaluation-under-multi-modal-non-para/01_overview.md)는 성공 허용 집합의 직접 비교로 등록했다. [DISaM](../2024/CoRL/2024_CoRL_Learning-to-Look-Seeking-Information-for-Decision-Making-v/01_overview.md)·[ATAP](../2026/arXiv/2026_arXiv_Imagine-then-Verify-Affordance-Targeted-Active-Perception/01_overview.md)의 관측 목적을 함께 비교한다. 점수·likelihood를 보정된 posterior나 실제 행동 성공률로 간주하지 않는다. 추가/승격 문헌의 확인 범위는 [REG-R17](../work/update/REGISTRY.md#reg-r18)을 따른다.

### 미지의 손목 카메라 장착 변화와 행동 기반 적응 — 2026-11-17

**CURATION-HYPOTHESIS / R1 이력, R2 현재 선택에서 제외.** [CamVLA §5](https://arxiv.org/html/2607.05396v1#S5)는 손목 카메라 교란을 범위 밖으로 두며, [CoRe-VLA Fig.1](https://arxiv.org/html/2609.37150v1)은 외부 시점 변화 때 손목 장착을 유지한다. 알려지지 않은 wrist-to-EEF 변환을 영상·고유감각·행동 이력으로 추정하는 VLA가, 같은 시간의 고전적 보정/시점 증강보다 유용한가? 일반 능동 관측이나 hand–eye calibration 자체는 기존 방법이다. 외부 view만으로 충분한 경우와 구별하며 RL 필요성도 확인해야 한다. [새 분야 비교·최소 사례·대안](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/NEW_FIELD_SCOUT_2026-11-17.md#camera). 추가 확인한 [ICWM](https://arxiv.org/abs/2606.26025)은 짧은 자가 상호작용으로 시스템 구성을 추론해 카메라 변화에 적응하므로 기여 경계를 더 좁힌다. 아직 효과·독립 신규성을 검증하지 않았고 사용자 reading status는 바꾸지 않았다.

현재 후보 판정은 [주제별 요약](../work/research_topics/RESULTS.md)을 따른다. 아래 질문은 `CURATION-HYPOTHESIS`이며 재개 승인이 아니다.

| 질문 | 구별할 예측 | 최소 대조·중단 조건 | 근거/판정 |
|---|---|---|---|
| C1 정보/행동 비용 | 관측 primitive의 정보 이득이 같은 시간·자세의 wait/move 대조 이후에도 남는가? | 추가 sensor/data·aligned adaptation을 통제한다. Native base competence와 물리 관측 primitive 미확보 상태를 유지한다. | [검토 근거](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/research_candidates/2026-10-20_vla_rl/C1_REVIEW.md) |
| Stale spatial memory | Fresh/stale/masked memory에서 행동이 실제로 달라지고 uncertainty가 intervention threshold를 보정하는가? | Cache 존재를 visual memory로 해석하지 않는다. RP-3는 RETIRED이며 history·정보 비용·cause attribution을 다시 갖춰야 한다. | [검토 근거](../work/research_topics/RESULTS.md#rp3) |
| Geometry의 action utility | 동일 policy/planner에서 pose noise·scale error·map staleness를 분리하면 dense/object-centric/implicit state의 순위가 달라지는가? | Registration covariance·semantic correspondence 충돌을 downstream collision/contact·recovery로 평가한다. Reconstruction metric만으로 승격하지 않는다. | 기존 track 비교의 연구자 질문; native 효과 미검증 |

<a id="gap-geometry-2026"></a>
### GAP-GEOMETRY — 지도 안에서 안전한 경로가 실제 공간에서도 안전하려면 무엇이 필요한가?

- 갱신: 2026-10-23. `CURATION-HYPOTHESIS`; 3D vision·SLAM·uncertainty·motion planning 질문. [확장 조사·출처](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/BROAD_RESEARCH_GAP_SCOUT_2026-10-23.md).
- **직접 근거:** [VGGT, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html)는 feed-forward geometry를, [CG-SLAM, ECCV 2024](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3580_ECCV_2024_paper.php)은 uncertainty-aware tracking/mapping을 다룬다. [Splat-Nav, T-RO 2025](https://doi.org/10.1109/tro.2025.3552348)는 Gaussian map의 안전 corridor와 localization을 결합한다. [SAFER-Splat §VIII](https://arxiv.org/html/2409.09868v1)은 지도 정확성 가정과 dynamic object·pose error 한계를 직접 명시한다. Rendering/geometry confidence와 실제 collision probability는 같은 양이 아니다.
- **이미 존재하는 확장:** [POMATO, ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_POMATO_Marrying_Pointmap_Matching_with_Temporal_Motions_for_Dynamic_3D_ICCV_2025_paper.html)는 dynamic pointmap/temporal motion을, [VGGT outlier-view rejection, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Emergent_Outlier_View_Rejection_in_Visual_Geometry_Grounded_Transformers_CVPR_2026_paper.html)은 distractor view를 다룬다. [AirSplan](https://arxiv.org/abs/2609.21226)은 normalized splat과 continuous-time collision constraint를 결합한다(IROS 2026은 저자 표기). Dynamic mapping·confidence filtering·GSplat safety filter 자체는 새 공백으로 제안하지 않는다.
- **좁힐 질문 — 연구자 해석:** 보이지 않거나 얇은 장애물이 지도에서 빠진 경우와 관측한 표면의 위치 오차를 구별할 수 있는가? 동일 pose/scale 보정 아래 **free-space로 오판한 영역**의 위험을 예측하는 confidence가 새로운 scene·sensor에서도 유효한가? 완전히 미관측된 공간은 추가 가정 없이 안전하다고 식별할 수 없으므로 unknown으로 처리하거나 관측을 요구하는 선택도 포함한다.
- **최소 비교:** 동일 planner/controller·RGB/RGB-D 입력·map resolution·latency에서 occupancy/TSDF의 unknown-space 처리, raw geometry confidence, depth/pose calibration, conservative inflation, calibrated residual을 비교한다. Scene 단위 holdout과 thin/occluded/dynamic 조건을 분리하고 ground-truth geometry로 swept-volume false-free-space rate·collision·통과율·추가 관측/정지 비용을 측정한다. 영상 PSNR·평균 depth error만으로 판정하지 않는다.
- **기각·기여 가능성:** Localization correction이나 고정 margin만으로 같은 collision–progress 곡선을 얻으면 새 representation의 주장을 줄인다. 의미 있는 결과는 지도의 오류 종류와 action 위험의 관계, confidence를 사용할 수 있는 조건, 또는 실패를 줄이는 표현/보정이다. C1의 learned observation selector나 D2의 attached-object planning을 자동 재개하는 연구가 아니다.
- **GAP-W2 직접 비교 후 수정:** [PwC, CoRL 2024/PMLR 2025](https://proceedings.mlr.press/v270/dixit25a.html)는 환경 단위 calibration으로 closed-loop state shift를 다루고, [v2 §3–4·F.3](https://arxiv.org/html/2403.08185v2)은 unknown-space와 일반 occupancy predictor까지 다룬다. [SemSafe-3DGS §III–IV](https://arxiv.org/html/2609.19330v1)는 trajectory-relevant active perception을 이미 제안한다(preprint). 따라서 calibration·unknown-space·active sensing의 결합 자체를 신규 기여로 삼지 않는다. PwC가 포괄하는 policy/state 변화와 환경·sensor 분포 가정 밖의 변화를 혼동하지 않는다.
- **공정성 보강:** [AirSplan §IV-B3·V-B](https://arxiv.org/html/2609.21226v1)의 conformal inflation은 FRS 근사의 보정이며 지도 완전성 보정과 다르다. 그 실험의 depth supervision도 baseline 간 동일하지 않다. 같은 입력·nominal planner에서 독립 GT와 collision–progress 곡선을 비교해야 한다. Splat-Nav/PwC 공개 source는 확인했지만 scene payload·calibration coverage·native runtime은 미검증이다.
- **현재 판단·재검토:** **REVISE / 진단 후보 HOLD**. [GAP-W2 결과·비교 계약 초안](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/GAP_W2_COMPARATIVE_REVIEW_2026-10-23.md)에 지정 본문 5편과 공개 interface를 대조했다. 누락과 위치 오차를 분리한 scene–sensor–GT 구성 및 unknown/margin 기준으로 설명되지 않는 구체적 예측이 생기면 재검토한다. 같은 문헌 검색 반복·새 planner 구현은 현재 다음 행동이 아니다. 새로운 가설은 `CURATION-HYPOTHESIS`, 실제 안전 효과는 미검증이다.

**Metadata 정합 완료 (META-W1, 2026-10-23):** `pr-0284`의 canonical publication·경로를 T-RO 2025로 수정했다. IROS 2025 발표는 저자 연구실의 별도 기록이며 발표 형식은 미확인이다. 같은 paper ID·NEXT tier·기존 본문 분석과 읽기 상태를 보존했다. [출처·경로 이관 기록](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/SPLAT_NAV_METADATA_2026-10-23.md).
