# Robotics-Enabling 3D Perception

- Updated: 2026-08-28 KST

## Scope

Rigid registration, point-cloud representation, feed-forward geometry, SLAM, dense correspondence, semantic mapping, 3D scene graphs, active perception, articulation flow와 3D-aware VLA를 downstream robot behavior 관점에서 비교한다.

## Reading Path

ICP → PointNet → DROID-SLAM/3DGS/DUSt3R/VGGT → Dense Object Nets/NDF/DenseMatcher → ConceptFusion/VLMaps/Open3DSG → Where2Act/FlowBot3D/RVT → PointVLA/Any3D-VLA/ActiveVLA.

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### Robotics-enabling 3D perception — 7

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [A Method for Registration of 3-D Shapes](../1992/IEEE-Transactions-on-Pat/1992_IEEE-Transactions-on-Pat_A-Method-for-Registration-of-3-D-Shapes/01_overview.md) | 1992 / IEEE Transactions on Pattern Analysis and Machine Intelligence | `UNREAD` | `ABSTRACT_CHECKED` |
| CORE | [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](../2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) | 2017 / CVPR | `UNREAD` | `CURATION_ONLY` |
| CORE | [DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) | 2021 / NeurIPS | `UNREAD` | `CURATION_ONLY` |
| CORE | [3D Gaussian Splatting for Real-Time Radiance Field Rendering](../2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md) | 2023 / SIGGRAPH | `UNREAD` | `CURATION_ONLY` |
| CORE | [ConceptFusion: Open-set Multimodal 3D Mapping](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) | 2023 / RSS | `UNREAD` | `CURATION_ONLY` |
| CORE | [RVT: Robotic View Transformer for 3D Object Manipulation](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) | 2023 / CoRL | `UNREAD` | `CURATION_ONLY` |
| CORE | [DUSt3R: Geometric 3D Vision Made Easy](../2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md) | 2024 / CVPR | `UNREAD` | `CURATION_ONLY` |

### Active and embodied 3D Vision — 11

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| NEXT | [Where2Act: From Pixels to Actions for Articulated 3D Objects](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md) | 2021 / ICCV | `UNREAD` | `CURATION_ONLY` |
| NEXT | [FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md) | 2022 / RSS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Ditto: Building Digital Twins of Articulated Objects from Interaction](../2022/CVPR/2022_CVPR_Ditto-Building-Digital-Twins-of-Articulated-Objects-from-I/01_overview.md) | 2022 / CVPR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [VLMaps: Visual-Language Maps for Robot Navigation](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) | 2023 / ICRA | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships](../2024/CVPR/2024_CVPR_Open3DSG-Open-Vocabulary-3D-Scene-Graphs-from-Point-Clouds/01_overview.md) | 2024 / CVPR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [VGGT: Visual Geometry Grounded Transformer](../2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md) | 2025 / CVPR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [SUGAR: Pre-training 3D Visual Representations for Robotics](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md) | 2024 / CVPR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](../2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) | 2025 / IROS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding](../2026/CVPR/2026_CVPR_EmbodiedSplat-Online-Feed-Forward-Semantic-3DGS-for-Open-V/01_overview.md) | 2026 / CVPR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](../2025/CVPR/2025_CVPR_RoboSpatial-Teaching-Spatial-Understanding-to-2D-and-3D-Vi/01_overview.md) | 2025 / CVPR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [PointVLA: Injecting the 3D World into Vision-Language-Action Models](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) | 2026 / RA-L | `UNREAD` | `CURATION_ONLY` |

<!-- READING_QUEUE:END -->

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래 행은 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. 각 논문을 정독할 때 source location과 수치를 확인하고, 틀린 항목은 수정한 뒤 tracker를 갱신한다.

| Paper | Perception problem | Input/state representation | Temporal memory/update | Language/semantics | Action/planning interface | Online cost | Robot/task | Downstream metric | Failure mode | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|---|
| [ICP](../1992/IEEE-Transactions-on-Pat/1992_IEEE-Transactions-on-Pat_A-Method-for-Registration-of-3-D-Shapes/01_overview.md) | rigid alignment of partially matched 3D shapes | point/shape sets and rigid transform | iterative correspondence–transform update | none | pose/map estimate for localization or manipulation | iterative nearest-neighbor and fitting cost | registration substrate for mapping/object pose | alignment error; downstream control not in original protocol | initialization, overlap, outliers and local minima | learned geometry를 classical registration and pose-consistency baseline과 비교 |
| [PointNet](../2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) / [RVT](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) | unordered 3D representation → action-centric multi-view manipulation | point-set features / rendered multi-view tokens | mostly per-observation | task conditioning in robot policy | 3D action prediction | representation/rendering latency UNVERIFIED | tabletop manipulation | task success plus representation metrics | sensor/data benefit may be mistaken for representation benefit | 동일 policy head로 2D/3D ablation |
| [DROID-SLAM](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) → [DUSt3R](../2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md) / [VGGT](../2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md) | online state estimation → feed-forward multi-view geometry | camera pose, depth and point-map style geometry | recurrent/iterative update vs feed-forward reconstruction | limited direct language semantics | map/state for downstream planning | accuracy–latency trade-off | navigation/manipulation-enabling geometry | pose/depth plus downstream task should be paired | dynamic scene, scale/calibration and stale state | geometry model을 uncertain robot state estimator로 평가 |
| [ConceptFusion](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) / [VLMaps](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) | open-vocabulary 3D mapping | spatial map with language-aligned features | map fusion over observations | open-set object/location semantics | language query to navigation/manipulation target | map building and query cost | navigation and scene interaction | retrieval/localization plus task success | semantic confidence and temporal staleness | language map에 uncertainty/forgetting 추가 |
| [3DGS](../2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md) / [Splat-Nav](../2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) | fast scene representation → safe navigation map | differentiable Gaussian scene | optimized/offline map; online variants differ | semantics optional | collision-aware path planning | rendering/map-query speed is central | navigation in reconstructed scenes | geometry/rendering plus collision/success | visual fidelity need not imply safe free space | neural rendering과 conservative occupancy 분리 |
| [RLBench](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) → [Perceiver-Actor](../2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md) / [RVT](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) | standardized RGB-D multi-task manipulation | voxel/3D token or multi-view action state | per-step observation update | language task conditioning | 6-DoF action prediction | simulator inference cost | simulated tabletop manipulation | multi-task success | simulator/calibration/contact gap | 공통 substrate에서 representation을 비교 |
| [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) | action-relevant view acquisition | task-conditioned 3D observation | active re-observation | language-conditioned relevance | camera/view action coupled to manipulation | sensing motion and delay budget | precise manipulation | task success per sensing/time budget | more geometry can cost time and introduce occlusion | value-of-information을 action 변화로 정의 |


## Dependency and Evolution

아래 계보는 3D benchmark의 발전 자체보다 representation이 robot state와 action interface로 들어가는 과정을 나타낸다. 직접 citation 관계는 정독 시 확인한다.

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| [ICP](../1992/IEEE-Transactions-on-Pat/1992_IEEE-Transactions-on-Pat_A-Method-for-Registration-of-3-D-Shapes/01_overview.md) → feature/robust registration → [DROID-SLAM](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) / [DUSt3R](../2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md) / [VGGT](../2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md) | explicit closest-point correspondence와 rigid fitting에서 learned iterative state estimation 및 feed-forward multi-view pose/geometry prediction으로 확장된다. | learned geometry가 poor initialization, dynamic object, scale/calibration shift에서 classical failure를 실제로 줄이는가 |
| [PointNet](../2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) → [RVT](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) / [SUGAR](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md) → [PointVLA](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) / [Any3D-VLA](../2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/01_overview.md) | unordered point-set representation에서 action-centric 3D token, robotics pretraining과 generalist VLA input으로 확장된다. | representation, 추가 depth sensor와 data augmentation의 효과를 분리할 수 있는가 |
| [DROID-SLAM](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) / [3D Gaussian Splatting](../2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md) / [DUSt3R](../2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md) → [VGGT](../2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md) → [Splat-Nav](../2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) / [EmbodiedSplat](../2026/CVPR/2026_CVPR_EmbodiedSplat-Online-Feed-Forward-Semantic-3DGS-for-Open-V/01_overview.md) | iterative state estimation, differentiable rendering과 pairwise geometry가 feed-forward multi-view geometry 및 online semantic map으로 수렴한다. | offline geometry quality가 dynamic online state, planning latency와 safety에 그대로 전달되는가 |
| [ConceptFusion](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) / [VLMaps](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) → [Open3DSG](../2024/CVPR/2024_CVPR_Open3DSG-Open-Vocabulary-3D-Scene-Graphs-from-Point-Clouds/01_overview.md) → [SayPlan](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) / [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) | open-vocabulary feature map에서 object/relation graph와 state-aware language planning memory로 확장된다. | semantic confidence, temporal freshness와 geometric feasibility가 plan에 함께 전달되는가 |
| [Where2Act](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md) → [FlowBot3D](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md) → [DenseMatcher](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) / [G3Flow](../2025/CVPR/2025_CVPR_G3Flow-Generative-3D-Semantic-Flow-for-Pose-aware-and-Gene/01_overview.md) / [EquAct](../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) | affordance point에서 articulation flow, semantic correspondence와 equivariant action policy로 확장된다. | semantic/geometric correspondence가 contact feasibility와 cross-category task success를 충분히 제약하는가 |
| [Dense Object Nets](../2018/CoRL/2018_CoRL_Dense-Object-Nets-Learning-Dense-Visual-Object-Descriptors/01_overview.md) → [Neural Descriptor Fields](../2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md) → [DenseMatcher](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) | self-supervised dense image/surface descriptor가 SE(3)-equivariant object field와 category-level semantic correspondence로 확장된다. | correspondence metric 향상이 grasp/contact success와 recovery under occlusion에 인과적으로 연결되는가 |
| passive 3D input → [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) | 관측된 geometry를 소비하는 policy에서 task-relevant view를 직접 선택하는 perception–action loop로 이동한다. | 추가 view의 sensing cost와 action decision value를 동일 budget에서 평가하는가 |
| [RLBench](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) → [Perceiver-Actor](../2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md) / [RVT](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) | 표준화된 multi-task RGB-D manipulation suite가 voxel 및 multi-view 3D action representation을 비교하는 공통 evaluation substrate가 된다. | simulator success가 real sensing noise, calibration error와 contact robustness를 얼마나 예측하는가 |

## Open Questions

- Robot policy에 필요한 최소 3D state는 dense reconstruction인가, object-centric map인가, implicit memory인가?
- Spatial memory의 uncertainty와 stale state를 어떻게 표현하고 갱신할 것인가?
- 3D-aware VLA의 이득이 representation 때문인지 추가 sensor/data 때문인지 어떻게 분리할 것인가?
- Registration confidence와 pose covariance가 downstream planner/controller의 intervention threshold로 전달되는가?
- ICP식 geometric consistency와 learned semantic correspondence가 충돌할 때 어느 신호를 우선해야 하는가?

## Research Gaps

- 통합 gap은 [G-03: 3D→control causality](../research/RESEARCH_GAPS.md#g-03-3d-perception-향상이-control-향상으로-이어지는-인과성-부족), [G-04: memory staleness](../research/RESEARCH_GAPS.md#g-04-persistent-spatial-memory의-staleness와-uncertainty), [G-13: active perception value](../research/RESEARCH_GAPS.md#g-13-active-perception의-비용-대비-control-value-평가-부족)을 본다.
- 이 문서에는 perception metric과 downstream robot metric의 실제 대응만 정독 근거로 추가한다.
