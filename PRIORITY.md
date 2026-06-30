# Reading Priority

- Updated: 2026-06-30 KST
- Source registry: [PAPER.md](./PAPER.md)
- Purpose: category-level reading roadmap with recent-trend emphasis; Foundation sections mix historical cores with recent de-facto foundation papers when local registry coverage supports it.

## Priority Criteria

Reading priority is assigned by the following criteria:

- 해당 분야에서의 foundation 핵심
- 3D CV 중심성
- Robotics 확장 가능성
- 연구 공백 명확성
- 평가 가능성
- 구현 난이도
- 데이터 접근성
- 논문 contribution 가능성
- 최신 트렌드 중 핵심 flow가 되는 논문

`Local` means the paper exists in the local registry with a paper folder, notes, and PDF when available. Non-Foundation sections prioritize 2024-current trend-flow papers, while Foundation sections retain historical roots and add recent papers that became common baselines or starting points for current 3D CV/Robotics research.

## 3D Equivariance, Calibration, and Registration

**우선 읽기**

- Local: [VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency](./2026/ICML/2026_ICML_VGGT-Motion-Motion-Aware-Calibration-Free-Monocular-SLAM-f/01_overview.md)
- Local: [C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion](./2026/CVPR/2026_CVPR_C-GenReg-Training-Free-3D-Point-Cloud-Registration-by-Mult/01_overview.md)
- Local: [RayI2P: Learning Rays for Image-to-Point Cloud Registration](./2026/ICLR/2026_ICLR_RayI2P-Learning-Rays-for-Image-to-Point-Cloud-Registration/01_overview.md)
- Local: [GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion](./2025/NeurIPS/2025_NeurIPS_GeGS-PCR-Fast-and-Robust-Color-3D-Point-Cloud-Registration/01_overview.md)
- Local: [GaussReg: Fast 3D Registration with Gaussian Splatting](./2024/ECCV/2024_ECCV_GaussReg-Fast-3D-Registration-with-Gaussian-Splatting/01_overview.md)
- Local: [GeoCalib: Learning Single-image Calibration with Geometric Optimization](./2024/ECCV/2024_ECCV_GeoCalib-Learning-Single-image-Calibration-with-Geometric/01_overview.md)

**선정 이유:** 최신 흐름은 hand-crafted/feature correspondence보다 feed-forward geometry, SfM-free calibration, image-to-point registration, Gaussian-to-point alignment로 이동하고 있다. 로봇에서는 장기 SLAM, multimodal map alignment, 재방문 localization이 모두 calibration/registration failure에 민감하므로, 2024 이후 논문을 우선해 읽는 편이 연구 공백을 잡기 쉽다.

## 3D Generative Modeling and Diffusion

**우선 읽기**

- Local: [Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling](./2026/ICLR/2026_ICLR_Geometry-Forcing-Marrying-Video-Diffusion-and-3D-Represent/01_overview.md)
- Local: [WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving](./2026/ICLR/2026_ICLR_WorldSplat-Gaussian-Centric-Feed-Forward-4D-Scene-Generati/01_overview.md)
- Local: [G4Splat: Geometry-Guided Gaussian Splatting with Generative Prior](./2026/ICLR/2026_ICLR_G4Splat-Geometry-Guided-Gaussian-Splatting-with-Generative/01_overview.md)
- Local: [HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction](./2026/CVPR/2026_CVPR_HAD-Hallucination-Aware-Diffusion-Priors-for-3D-Reconstruc/01_overview.md)
- Local: [Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors](./2025/ICCV/2025_ICCV_Generative-Gaussian-Splatting-Generating-3D-Scenes-with-Vi/01_overview.md)
- Local: [PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models](./2025/CVPR/2025_CVPR_PartGen-Part-level-3D-Generation-and-Reconstruction-with-M/01_overview.md)
- Local: [ReconFusion: 3D Reconstruction with Diffusion Priors](./2024/CVPR/2024_CVPR_ReconFusion-3D-Reconstruction-with-Diffusion-Priors/01_overview.md)

**선정 이유:** 최근 3D diffusion은 text-to-3D보다 geometry-consistent world modeling, 4D Gaussian generation, part-level editability, 로봇 조작용 semantic flow로 무게가 이동했다. 핵심 공백은 diffusion prior의 hallucination, multi-view consistency, physical executability이며, reconstruction/scene generation/manipulation benchmark로 평가 가능하다.

## 3D Large Multimodal Models

**우선 읽기**

- Local: [SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models](./2026/ICML/2026_ICML_SpatioLM-Towards-General-Physical-Spatial-Intelligence-in/01_overview.md)
- Local: [G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning](./2026/CVPR/2026_CVPR_G2VLM-Geometry-Grounded-Vision-Language-Model-with-Unified/01_overview.md)
- Local: [SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning](./2026/CVPR/2026_CVPR_SpatialStack-Layered-Geometry-Language-Fusion-for-3D-VLM-S/01_overview.md)
- Local: [GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models](./2026/ICLR/2026_ICLR_GPT4Scene-Understand-3D-Scenes-from-Videos-with-Vision-Lan/01_overview.md)
- Local: [SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models](./2025/CVPR/2025_CVPR_SpatialLLM-A-Compound-3D-Informed-Design-towards-Spatially/01_overview.md)
- Local: [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](./2025/CVPR/2025_CVPR_RoboSpatial-Teaching-Spatial-Understanding-to-2D-and-3D-Vi/01_overview.md)
- Local: [SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities](./2024/CVPR/2024_CVPR_SpatialVLM-Endowing-Vision-Language-Models-with-Spatial-Re/01_overview.md)

**선정 이유:** 2025-2026 흐름은 3D-LMM 자체보다 geometry-grounded VLM, spatial reasoning benchmark, physical/spatial intelligence로 이동했다. 2D LMM foundation은 Foundation 섹션에서 읽고, 이 카테고리에서는 reconstruction, depth, spatial relation, embodied reasoning을 모델 내부에 어떻게 주입하는지에 집중한다.

## 3D Reconstruction, Geometry, and SLAM

**우선 읽기**

- Local: [Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation](./2025/NeurIPS/2025_NeurIPS_Fin3R-Fine-tuning-Feed-forward-3D-Reconstruction-Models-vi/01_overview.md)
- Local: [MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion](./2025/3DV/2025_3DV_MASt3R-SfM-a-Fully-Integrated-Solution-for-Unconstrained-S/01_overview.md)
- Local: [SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment](./2025/NeurIPS/2025_NeurIPS_SIU3R-Simultaneous-Scene-Understanding-and-3D-Reconstructi/01_overview.md)
- Local: [SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction](./2025/CVPR/2025_CVPR_SPARS3R-Semantic-Prior-Alignment-and-Regularization-for-Sp/01_overview.md)
- Local: [FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent](./2025/3DV/2025_3DV_FlowMap-High-Quality-Camera-Poses-Intrinsics-and-Depth-via/01_overview.md)
- Local: [BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction](./2026/CVPR/2026_CVPR_BA-GS-Bayesian-Adaptive-Gaussian-Splatting-for-SFM-Free-3D/01_overview.md)

**선정 이유:** DUSt3R/MASt3R/VGGT/GS-SLAM 같은 공통 출발점은 Foundation 섹션에만 남겼다. 이 섹션은 그 이후의 feed-forward model adaptation, unconstrained SfM, semantic-prior sparse reconstruction, pose/intrinsics/depth optimization, SFM-free Gaussian reconstruction처럼 최신 연구 아이디어와 직접 연결되는 확장 논문을 우선한다.

## 3D Representation Learning and Foundation Models

**우선 읽기**

- Local: [LaGeM: A Large Geometry Model for 3D Representation Learning and Diffusion](./2025/ICLR/2025_ICLR_LaGeM-A-Large-Geometry-Model-for-3D-Representation-Learnin/01_overview.md)
- Local: [Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training](./2025/NeurIPS/2025_NeurIPS_Point-MaDi-Masked-Autoencoding-with-Diffusion-for-Point-Cl/01_overview.md)
- Local: [Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](./2025/NeurIPS/2025_NeurIPS_Object-X-Learning-to-Reconstruct-Multi-Modal-3D-Object-Rep/01_overview.md)
- Local: [SUGAR: Pre-training 3D Visual Representations for Robotics](./2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md)

**선정 이유:** ULIP/UniPre3D/Dens3R은 Foundation 섹션에서만 다룬다. 이 섹션은 large geometry model, diffusion-based point pretraining, multi-modal object representation, robotics-oriented 3D representation처럼 후속 연구 아이디어와 직접 연결되는 최신 transfer gap을 우선한다.

## 3D Scene Graphs and Graph Reasoning

**우선 읽기**

- Local: [MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning](./2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md)
- Local: [Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning](./2026/ICRA/2026_ICRA_Open-Vocabulary-Spatio-Temporal-Scene-Graph-for-Robot-Perc/01_overview.md)
- Local: [FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images](./2025/ICCV/2025_ICCV_FROSS-Faster-Than-Real-Time-Online-3D-Semantic-Scene-Graph/01_overview.md)
- Local: [Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation](./2025/RA-L/2025_RA-L_Dynamic-Open-Vocabulary-3D-Scene-Graphs-for-Long-term-Lang/01_overview.md)
- Local: [MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs](./2025/IROS/2025_IROS_MR-COGraphs-Communication-efficient-Multi-Robot-Open-vocab/01_overview.md)
- Local: [Clio: Real-time Task-Driven Open-Set 3D Scene Graphs](./2024/RA-L/2024_RA-L_Clio-Real-time-Task-Driven-Open-Set-3D-Scene-Graphs/01_overview.md)
- Local: [Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships](./2024/CVPR/2024_CVPR_Open3DSG-Open-Vocabulary-3D-Scene-Graphs-from-Point-Clouds/01_overview.md)

**선정 이유:** 최근 3D scene graph는 offline graph prediction보다 open-vocabulary, task-driven, online, long-term, multi-robot, state-aware planning으로 이동했다. Foundation formulation은 별도 섹션에 두고, 여기서는 로봇 memory와 planning에 바로 연결되는 최신 graph flow를 우선한다.

## 3D Scene Representations and Neural Fields

**우선 읽기**

- Local: [ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting](./2026/CVPR/2026_CVPR_ExtrinSplat-Decoupling-Geometry-and-Semantics-for-Open-Voc/01_overview.md)
- Local: [Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](./2026/ICLR/2026_ICLR_Flash-Mono-Feed-Forward-Accelerated-Gaussian-Splatting-Mon/01_overview.md)
- Local: [SplatFormer: Point Transformer for Robust 3D Gaussian Splatting](./2025/ICLR/2025_ICLR_SplatFormer-Point-Transformer-for-Robust-3D-Gaussian-Splat/01_overview.md)
- Local: [SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images](./2025/ICCV/2025_ICCV_SpatialSplat-Efficient-Semantic-3D-from-Sparse-Unposed-Ima/01_overview.md)
- Local: [PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting](./2025/ICCV/2025_ICCV_PhysSplat-Efficient-Physics-Simulation-for-3D-Scenes-via-M/01_overview.md)
- Local: [DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction](./2025/ICCV/2025_ICCV_DeGauss-Dynamic-Static-Decomposition-with-Gaussian-Splatti/01_overview.md)
- Local: [SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering](./2024/CVPR/2024_CVPR_SuGaR-Surface-Aligned-Gaussian-Splatting-for-Efficient-3D/01_overview.md)

**선정 이유:** scene representation의 최신 흐름은 NeRF foundation에서 Gaussian-centric geometry, semantic decoupling, dynamic/static separation, physics simulation, feed-forward SLAM으로 이동했다. rendering quality보다 geometry/semantics/action usability가 연구 공백이므로, 3DGS 이후 논문을 중심으로 읽는 것이 효율적이다.

## 3D Semantic Understanding and Alignment

**우선 읽기**

- Local: [GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation](./2026/ICLR/2026_ICLR_GeoPurify-A-Data-Efficient-Geometric-Distillation-Framewor/01_overview.md)
- Local: [Search3D: Hierarchical Open-Vocabulary 3D Segmentation](./2025/RA-L/2025_RA-L_Search3D-Hierarchical-Open-Vocabulary-3D-Segmentation/01_overview.md)
- Local: [OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection](./2025/ICCV/2025_ICCV_OV-SCAN-Semantically-Consistent-Alignment-for-Novel-Object/01_overview.md)
- Local: [Open-Vocabulary Octree-Graph for 3D Scene Understanding](./2025/ICCV/2025_ICCV_Open-Vocabulary-Octree-Graph-for-3D-Scene-Understanding/01_overview.md)
- Local: [Details Matter for Indoor Open-vocabulary 3D Instance Segmentation](./2025/ICCV/2025_ICCV_Details-Matter-for-Indoor-Open-vocabulary-3D-Instance-Segm/01_overview.md)
- Local: [Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding](./2024/ECCV/2024_ECCV_Dense-Multimodal-Alignment-for-Open-Vocabulary-3D-Scene-Un/01_overview.md)
- Local: [OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation](./2024/ECCV/2024_ECCV_OpenIns3D-Snap-and-Lookup-for-3D-Open-vocabulary-Instance/01_overview.md)

**선정 이유:** open-vocabulary 3D semantic understanding은 2024 이후 segmentation, novel object discovery, hierarchical search, geometric distillation, graph-structured scene understanding으로 빠르게 확장됐다. 초기 OpenScene/OpenMask3D는 Foundation/배경으로 두고, 이 섹션은 view consistency, boundary precision, geometry-aware alignment 문제를 직접 다루는 최신 논문을 우선한다.

## 3D Vision-Language Grounding

**우선 읽기**

- Local: [Grounded 3D-Aware Spatial Vision-Language Modeling](./2026/CVPR/2026_CVPR_Grounded-3D-Aware-Spatial-Vision-Language-Modeling/01_overview.md)
- Local: [RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics](./2025/NeurIPS/2025_NeurIPS_RoboRefer-Towards-Spatial-Referring-with-Reasoning-in-Visi/01_overview.md)
- Local: [SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding](./2025/CVPR/2025_CVPR_SeeGround-See-and-Ground-for-Zero-Shot-Open-Vocabulary-3D/01_overview.md)
- Local: [ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition](./2025/ICCV/2025_ICCV_ViewSRD-3D-Visual-Grounding-via-Structured-Multi-View-Deco/01_overview.md)
- Local: [VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding](./2024/CoRL/2024_CoRL_VLM-Grounder-A-VLM-Agent-for-Zero-Shot-3D-Visual-Grounding/01_overview.md)
- Local: [Towards CLIP-driven Language-free 3D Visual Grounding via 2D-3D Relational Enhancement and Consistency](./2024/CVPR/2024_CVPR_Towards-CLIP-driven-Language-free-3D-Visual-Grounding-via/01_overview.md)

**선정 이유:** 3D grounding의 현재 핵심은 supervised ScanRefer-style localization보다 zero-shot/open-vocabulary grounding, multi-view decomposition, reasoning-based referring, real-robot perception/manipulation benchmark로 이동했다. ScanRefer/ReferIt3D는 foundation으로 남기되, 우선 독해는 2024 이후 논문을 중심으로 한다.

## Benchmarks and Datasets

**우선 읽기**

- Local: [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](./2026/ICML/2026_ICML_RoboTwin-2.0-A-Scalable-Data-Generator-and-Benchmark-with/01_overview.md)
- Local: [RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation](./2026/ICLR/2026_ICLR_RoboInter-A-Holistic-Intermediate-Representation-Suite-Tow/01_overview.md)
- Local: [RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation](./2026/CVPR/2026_CVPR_RealVLG-R1-A-Large-Scale-Real-World-Visual-Language-Ground/01_overview.md)
- Local: [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](./2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/01_overview.md)
- Local: [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](./2025/ICCV/2025_ICCV_VLABench-A-Large-Scale-Benchmark-for-Language-Conditioned/01_overview.md)
- Local: [IRef-VLA: A Benchmark for Interactive Referential Grounding with Imperfect Language in 3D Scenes](./2025/ICRA/2025_ICRA_IRef-VLA-A-Benchmark-for-Interactive-Referential-Grounding/01_overview.md)
- Local: [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](./2025/ICML/2025_ICML_EmbodiedBench-Comprehensive-Benchmarking-Multi-modal-Large/01_overview.md)
- Local: [EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI](./2024/CVPR/2024_CVPR_EmbodiedScan-A-Holistic-Multi-Modal-3D-Perception-Suite-To/01_overview.md)

**선정 이유:** benchmark 트렌드는 static scene QA에서 real-world grounding, long-horizon manipulation, safety, bimanual robustness, intermediate representation, imperfect language로 확장됐다. 최신 benchmark를 우선 읽어야 contribution claim과 evaluation protocol을 현실적으로 설계할 수 있다.

## Equivariance, Diffusion, and 3D Action

**우선 읽기**

- Local: [EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation](./2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md)
- Local: [ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY](./2025/ICLR/2025_ICLR_ET-SEED-EFFICIENT-TRAJECTORY-LEVEL-SE3-EQUIVARIANT-DIFFUSI/01_overview.md)
- Local: [DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo](./2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md)
- Local: [G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation](./2025/CVPR/2025_CVPR_G3Flow-Generative-3D-Semantic-Flow-for-Pose-aware-and-Gene/01_overview.md)
- Local: [GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation](./2025/ICLR/2025_ICLR_GravMAD-Grounded-Spatial-Value-Maps-Guided-Action-Diffusio/01_overview.md)

**선정 이유:** Diffusion-EDFs는 Foundation 섹션에만 남겼다. 이 섹션은 SE(3)-equivariant multi-task transformer, trajectory-level equivariant diffusion policy, semantic correspondence, spatial value map, pose-aware semantic flow처럼 최신 3D action representation과 generalization gap을 우선한다.

## Foundations: 3D Detection and BEV Perception

**우선 읽기**

- Local: [VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection](./2018/CVPR/2018_CVPR_VoxelNet-End-to-End-Learning-for-Point-Cloud-Based-3D-Obje/01_overview.md)
- Local: [PointPillars: Fast Encoders for Object Detection from Point Clouds](./2019/CVPR/2019_CVPR_PointPillars-Fast-Encoders-for-Object-Detection-from-Point/01_overview.md)
- Local: [DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries](./2021/CoRL/2021_CoRL_DETR3D-3D-Object-Detection-from-Multi-view-Images-via-3D-t/01_overview.md)
- Local: [Lift, Splat, Shoot: Encoding Images from Arbitrary Camera Rigs by Implicitly Unprojecting to 3D](./2020/ECCV/2020_ECCV_Lift-Splat-Shoot-Encoding-Images-from-Arbitrary-Camera-Rig/01_overview.md)
- Local: [BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers](./2022/ECCV/2022_ECCV_BEVFormer-Learning-Bird-s-Eye-View-Representation-from-Mul/01_overview.md)
- Local: [BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation](./2023/ICRA/2023_ICRA_BEVFusion-Multi-Task-Multi-Sensor-Fusion-with-Unified-Bird/01_overview.md)
- Local: [Planning-oriented Autonomous Driving](./2023/CVPR/2023_CVPR_Planning-oriented-Autonomous-Driving/01_overview.md)

**선정 이유:** autonomous 3D perception의 foundation은 LiDAR voxel/pillar detection에서 camera BEV, temporal BEV, multi-sensor fusion, planning-oriented perception으로 이어진다. nuScenes, Waymo, KITTI에서 평가가 명확하고, 로봇/자율주행 확장 시 perception-to-planning contribution을 만들기 좋다.

## Foundations: 3D Geometry and Point Clouds

**우선 읽기**

- Local: [ShapeNet: An Information-Rich 3D Model Repository](./2015/arxiv/2015_arxiv_ShapeNet-An-Information-Rich-3D-Model-Repository/01_overview.md)
- Local: [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](./2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md)
- Local: [PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space](./2017/NeurIPS/2017_NeurIPS_PointNet++-Deep-Hierarchical-Feature-Learning-on-Point-Set/01_overview.md)
- Local: [PointCNN: Convolution On X-Transformed Points](./2018/NeurIPS/2018_NeurIPS_PointCNN-Convolution-On-X-Transformed-Points/01_overview.md)
- Local: [Point Transformer](./2021/ICCV/2021_ICCV_Point-Transformer/01_overview.md)
- Local: [Fully Convolutional Geometric Features](./2019/ICCV/2019_ICCV_Fully-Convolutional-Geometric-Features/01_overview.md)
- Local: [Deep Closest Point: Learning Representations for Point Cloud Registration](./2019/ICCV/2019_ICCV_Deep-Closest-Point-Learning-Representations-for-Point-Clou/01_overview.md)
- Local: [DUSt3R: Geometric 3D Vision Made Easy](./2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md)
- Local: [Grounding Image Matching in 3D with MASt3R](./2024/ECCV/2024_ECCV_Grounding-Image-Matching-in-3D-with-MASt3R/01_overview.md)
- Local: [VGGT: Visual Geometry Grounded Transformer](./2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md)

**선정 이유:** point cloud foundation은 recognition/segmentation/registration/manipulation의 출발점이고, 최신 geometry foundation은 calibration/pose 없이 dense correspondence, camera, depth, point map을 직접 예측하는 방향으로 이동했다. PointNet 계열과 FCGF/DCP를 통해 고전 3D feature/registration을 잡고, DUSt3R-MASt3R-VGGT 흐름으로 현재 feed-forward geometric 3D vision을 이해할 수 있다.

## Foundations: 3D Representation Learning

**우선 읽기**

- Local: [PointContrast: Unsupervised Pre-training for 3D Point Cloud Understanding](./2020/ECCV/2020_ECCV_PointContrast-Unsupervised-Pre-training-for-3D-Point-Cloud/01_overview.md)
- Local: [Self-Supervised Pretraining of 3D Features on any Point-Cloud](./2021/ICCV/2021_ICCV_Self-Supervised-Pretraining-of-3D-Features-on-any-Point-Cl/01_overview.md)
- Local: [Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling](./2022/CVPR/2022_CVPR_Point-BERT-Pre-training-3D-Point-Cloud-Transformers-with-M/01_overview.md)
- Local: [Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning](./2022/ECCV/2022_ECCV_Point-MAE-Masked-Autoencoders-for-Point-Cloud-Self-supervi/01_overview.md)
- Local: [ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding](./2023/CVPR/2023_CVPR_ULIP-Learning-a-Unified-Representation-of-Language-Images/01_overview.md)
- Local: [UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting](./2025/CVPR/2025_CVPR_UniPre3D-Unified-Pre-training-of-3D-Point-Cloud-Models-wit/01_overview.md)
- Local: [Dens3R: A Foundation Model for 3D Geometry Prediction](./2026/ICLR/2026_ICLR_Dens3R-A-Foundation-Model-for-3D-Geometry-Prediction/01_overview.md)

**선정 이유:** 3D representation learning은 contrastive/masked point pretraining에서 image-language-point alignment, Gaussian-based cross-modal pretraining, geometry foundation model로 확장됐다. label scarcity, domain shift, sensor/viewpoint 변화가 명확한 문제라 downstream transfer와 robotics robustness로 평가하기 좋다.

## Foundations: 3D Scene Representations

**우선 읽기**

- Local: [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](./2020/ECCV/2020_ECCV_NeRF-Representing-Scenes-as-Neural-Radiance-Fields-for-Vie/01_overview.md)
- Local: [Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields](./2022/CVPR/2022_CVPR_Mip-NeRF-360-Unbounded-Anti-Aliased-Neural-Radiance-Fields/01_overview.md)
- Local: [Instant Neural Graphics Primitives with a Multiresolution Hash Encoding](./2022/SIGGRAPH/2022_SIGGRAPH_Instant-Neural-Graphics-Primitives-with-a-Multiresolution/01_overview.md)
- Local: [NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction](./2021/NeurIPS/2021_NeurIPS_NeuS-Learning-Neural-Implicit-Surfaces-by-Volume-Rendering/01_overview.md)
- Local: [3D Gaussian Splatting for Real-Time Radiance Field Rendering](./2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md)
- Local: [LERF: Language Embedded Radiance Fields](./2023/ICCV/2023_ICCV_LERF-Language-Embedded-Radiance-Fields/01_overview.md)
- Local: [LangSplat: 3D Language Gaussian Splatting](./2024/CVPR/2024_CVPR_LangSplat-3D-Language-Gaussian-Splatting/01_overview.md)

**선정 이유:** scene representation은 NeRF 기반 rendering에서 surface reconstruction, fast hash encoding, real-time 3DGS, language-embedded fields로 확장됐다. mapping/localization/semantic query/planning 모두 이 표현 위에서 정의되므로, geometry와 semantics가 분리되는 지점을 Foundation 단계에서 잡아야 한다.

## Foundations: 3D Semantic Occupancy

**우선 읽기**

- Local: [SSCNet: Semantic Scene Completion from a Single Depth Image](./2017/CVPR/2017_CVPR_SSCNet-Semantic-Scene-Completion-from-a-Single-Depth-Image/01_overview.md)
- Local: [MonoScene: Monocular 3D Semantic Scene Completion](./2022/CVPR/2022_CVPR_MonoScene-Monocular-3D-Semantic-Scene-Completion/01_overview.md)
- Local: [VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion](./2023/CVPR/2023_CVPR_VoxFormer-Sparse-Voxel-Transformer-for-Camera-based-3D-Sem/01_overview.md)
- Local: [OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction](./2023/ICCV/2023_ICCV_OccFormer-Dual-path-Transformer-for-Vision-based-3D-Semant/01_overview.md)
- Local: [Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving](./2023/NeurIPS/2023_NeurIPS_Occ3D-A-Large-Scale-3D-Occupancy-Prediction-Benchmark-for/01_overview.md)
- Local: [GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction](./2024/ECCV/2024_ECCV_GaussianFormer-Scene-as-Gaussians-for-Vision-Based-3D-Sema/01_overview.md)
- Local: [EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](./2025/ICCV/2025_ICCV_EmbodiedOcc-Embodied-3D-Occupancy-Prediction-for-Vision-ba/01_overview.md)

**선정 이유:** occupancy는 robot navigation/planning에서 가장 직접적인 3D representation이며, 최근 흐름은 semantic scene completion에서 large-scale occupancy benchmark, Gaussian occupancy, embodied online scene understanding으로 이동했다. collision risk, traversability, semantic planning으로 확장이 자연스럽다.

## Foundations: Diffusion and Generative Models

**우선 읽기**

- Local: [Denoising Diffusion Probabilistic Models](./2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md)
- Local: [Denoising Diffusion Implicit Models](./2021/ICLR/2021_ICLR_Denoising-Diffusion-Implicit-Models/01_overview.md)
- Local: [Score-Based Generative Modeling through Stochastic Differential Equations](./2021/ICLR/2021_ICLR_Score-Based-Generative-Modeling-through-Stochastic-Differe/01_overview.md)
- Local: [Classifier-Free Diffusion Guidance](./2022/arxiv/2022_arxiv_Classifier-Free-Diffusion-Guidance/01_overview.md)
- Local: [High-Resolution Image Synthesis with Latent Diffusion Models](./2022/CVPR/2022_CVPR_High-Resolution-Image-Synthesis-with-Latent-Diffusion-Mode/01_overview.md)
- Local: [DreamFusion: Text-to-3D using 2D Diffusion](./2023/ICLR/2023_ICLR_DreamFusion-Text-to-3D-using-2D-Diffusion/01_overview.md)

**선정 이유:** 3D diffusion을 이해하려면 DDPM/DDIM, score formulation, guidance, latent diffusion의 역할을 구분해야 한다. DreamFusion은 text-to-3D와 SDS 계열의 출발점이라, 현재 3D/4D generation과 diffusion-prior reconstruction의 hallucination/consistency 문제를 읽기 위한 공통 배경이다.

## Foundations: Equivariance and Geometry

**우선 읽기**

- Local: [Group Equivariant Convolutional Networks](./2016/ICML/2016_ICML_Group-Equivariant-Convolutional-Networks/01_overview.md)
- Local: [Tensor Field Networks: Rotation- and Translation-Equivariant Neural Networks for 3D Point Clouds](./2018/arxiv/2018_arxiv_Tensor-Field-Networks-Rotation-and-Translation-Equivariant/01_overview.md)
- Local: [SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks](./2020/NeurIPS/2020_NeurIPS_SE3-Transformers-3D-Roto-Translation-Equivariant-Attention/01_overview.md)
- Local: [E(n) Equivariant Graph Neural Networks](./2021/ICML/2021_ICML_En-Equivariant-Graph-Neural-Networks/01_overview.md)
- Local: [Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation](./2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md)
- Local: [Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation](./2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md)

**선정 이유:** equivariance는 3D에서 pose/rotation generalization을 구조적으로 넣는 핵심 inductive bias다. 최근에는 SE(3) representation이 object manipulation과 diffusion policy까지 연결되므로, group theory foundation과 robotics-facing equivariant representation을 함께 읽어야 한다.

## Foundations: Monocular Geometry

**우선 읽기**

- Local: [Depth Map Prediction from a Single Image using a Multi-Scale Deep Network](./2014/NeurIPS/2014_NeurIPS_Depth-Map-Prediction-from-a-Single-Image-using-a-Multi-Sca/01_overview.md)
- Local: [Digging Into Self-Supervised Monocular Depth Estimation](./2019/ICCV/2019_ICCV_Digging-Into-Self-Supervised-Monocular-Depth-Estimation/01_overview.md)
- Local: [Vision Transformers for Dense Prediction](./2021/ICCV/2021_ICCV_Vision-Transformers-for-Dense-Prediction/01_overview.md)
- Local: [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](./2024/CVPR/2024_CVPR_Depth-Anything-Unleashing-the-Power-of-Large-Scale-Unlabel/01_overview.md)
- Local: [Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation](./2024/CVPR/2024_CVPR_Marigold-Repurposing-Diffusion-Based-Image-Generators-for/01_overview.md)
- Local: [Depth Anything V2](./2024/NeurIPS/2024_NeurIPS_Depth-Anything-V2/01_overview.md)
- Local: [UniDepth: Universal Monocular Metric Depth Estimation](./2024/CVPR/2024_CVPR_UniDepth-Universal-Monocular-Metric-Depth-Estimation/01_overview.md)

**선정 이유:** monocular geometry는 supervised/self-supervised depth에서 transformer dense prediction, large-scale depth foundation, metric monocular depth로 이동했다. DUSt3R 계열 feed-forward geometry는 3D Geometry Foundation에만 남기고, 이 섹션은 camera-only depth/metric geometry의 scale ambiguity, domain shift, calibration error에 집중한다.

## Foundations: RL and Imitation Learning

**우선 읽기**

- Local: [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](./2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md)
- Local: [Generative Adversarial Imitation Learning](./2016/NeurIPS/2016_NeurIPS_Generative-Adversarial-Imitation-Learning/01_overview.md)
- Local: [Proximal Policy Optimization Algorithms](./2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md)
- Local: [Decision Transformer: Reinforcement Learning via Sequence Modeling](./2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/01_overview.md)
- Local: [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](./2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md)

**선정 이유:** robotics/VLA 논문을 읽을 때 imitation learning, adversarial imitation, policy-gradient RL, offline sequence modeling, action diffusion의 차이를 구분해야 한다. Octo는 VLA/Robotics Foundation에만 남기고, 이 섹션은 RL/IL algorithmic foundation을 담당한다.

## Foundations: SLAM and Sensor Geometry

**우선 읽기**

- Local: [PTAM: Parallel Tracking and Mapping for Small AR Workspaces](./2007/ISMAR/2007_ISMAR_PTAM-Parallel-Tracking-and-Mapping-for-Small-AR-Workspaces/01_overview.md)
- Local: [KinectFusion: Real-Time Dense Surface Mapping and Tracking](./2011/ISMAR/2011_ISMAR_KinectFusion-Real-Time-Dense-Surface-Mapping-and-Tracking/01_overview.md)
- Local: [LSD-SLAM: Large-Scale Direct Monocular SLAM](./2014/ECCV/2014_ECCV_LSD-SLAM-Large-Scale-Direct-Monocular-SLAM/01_overview.md)
- Local: [ORB-SLAM: A Versatile and Accurate Monocular SLAM System](./2015/T-RO/2015_T-RO_ORB-SLAM-A-Versatile-and-Accurate-Monocular-SLAM-System/01_overview.md)
- Local: [ElasticFusion: Dense SLAM Without A Pose Graph](./2015/RSS/2015_RSS_ElasticFusion-Dense-SLAM-Without-A-Pose-Graph/01_overview.md)
- Local: [Structure-from-Motion Revisited](./2016/CVPR/2016_CVPR_Structure-from-Motion-Revisited/01_overview.md)
- Local: [BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Reintegration](./2017/TOG/2017_TOG_BundleFusion-Real-time-Globally-Consistent-3D-Reconstructi/01_overview.md)
- Local: [DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](./2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md)
- Local: [GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting](./2024/CVPR/2024_CVPR_GS-SLAM-Dense-Visual-SLAM-with-3D-Gaussian-Splatting/01_overview.md)
- Local: [Continuous 3D Perception Model with Persistent State](./2025/CVPR/2025_CVPR_Continuous-3D-Perception-Model-with-Persistent-State/01_overview.md)

**선정 이유:** SLAM은 robot 3D memory와 map update의 foundation이다. sparse feature/direct/dense RGB-D/SfM/deep SLAM을 이해한 뒤 GS-SLAM과 persistent-state model을 읽어야, 최신 neural/GS SLAM이 어떤 failure mode와 map consistency 문제를 아직 남기는지 보인다.

## Foundations: Transformer and Language Models

**우선 읽기**

- Local: [Attention Is All You Need](./2017/NeurIPS/2017_NeurIPS_Attention-Is-All-You-Need/01_overview.md)
- Local: [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](./2019/NAACL/2019_NAACL_BERT-Pre-training-of-Deep-Bidirectional-Transformers-for-L/01_overview.md)
- Local: [Language Models are Few-Shot Learners](./2020/NeurIPS/2020_NeurIPS_Language-Models-are-Few-Shot-Learners/01_overview.md)
- Local: [Training language models to follow instructions with human feedback](./2022/NeurIPS/2022_NeurIPS_Training-language-models-to-follow-instructions-with-human/01_overview.md)
- Local: [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](./2022/NeurIPS/2022_NeurIPS_Chain-of-Thought-Prompting-Elicits-Reasoning-in-Large-Lang/01_overview.md)

**선정 이유:** 3D LMM/VLA reasoning은 Transformer, instruction tuning, CoT prompting의 연장선이다. 직접적인 3D CV 논문은 아니지만 planning, graph reasoning, language-conditioned action을 읽기 위한 배경이다.

## Foundations: Vision Foundation Models

**우선 읽기**

- Local: [Masked Autoencoders Are Scalable Vision Learners](./2022/CVPR/2022_CVPR_Masked-Autoencoders-Are-Scalable-Vision-Learners/01_overview.md)
- Local: [Emerging Properties in Self-Supervised Vision Transformers](./2021/ICCV/2021_ICCV_Emerging-Properties-in-Self-Supervised-Vision-Transformers/01_overview.md)
- Local: [DINOv2: Learning Robust Visual Features without Supervision](./2023/TMLR/2023_TMLR_DINOv2-Learning-Robust-Visual-Features-without-Supervision/01_overview.md)
- Local: [Segment Anything](./2023/ICCV/2023_ICCV_Segment-Anything/01_overview.md)
- Local: [SAM 2: Segment Anything in Images and Videos](./2025/ICLR/2025_ICLR_SAM-2-Segment-Anything-in-Images-and-Videos/01_overview.md)
- Local: [Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](./2024/ECCV/2024_ECCV_Grounding-DINO-Marrying-DINO-with-Grounded-Pre-Training-fo/01_overview.md)

**선정 이유:** 2D foundation features는 3D open-vocabulary segmentation, mapping, reconstruction quality checking의 teacher로 쓰인다. MAE/DINO/DINOv2는 feature foundation, SAM/SAM2는 image-video mask prior, Grounding DINO는 open-set detection prior라 3D consistency와 2D-to-3D distillation 연구의 공통 배경이다.

## Foundations: Vision-Language Models

**우선 읽기**

- Local: [Learning Transferable Visual Models From Natural Language Supervision](./2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/01_overview.md)
- Local: [ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision](./2021/ICML/2021_ICML_ALIGN-Scaling-Up-Visual-and-Vision-Language-Representation/01_overview.md)
- Local: [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](./2022/ICML/2022_ICML_BLIP-Bootstrapping-Language-Image-Pre-training-for-Unified/01_overview.md)
- Local: [Flamingo: a Visual Language Model for Few-Shot Learning](./2022/NeurIPS/2022_NeurIPS_Flamingo-a-Visual-Language-Model-for-Few-Shot-Learning/01_overview.md)
- Local: [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](./2023/ICML/2023_ICML_BLIP-2-Bootstrapping-Language-Image-Pre-training-with-Froz/01_overview.md)
- Local: [Visual Instruction Tuning](./2023/NeurIPS/2023_NeurIPS_Visual-Instruction-Tuning/01_overview.md)
- Local: [PaLM-E: An Embodied Multimodal Language Model](./2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/01_overview.md)

**선정 이유:** CLIP/ALIGN은 contrastive language-image alignment의 출발점이고, BLIP/Flamingo/BLIP-2/LLaVA는 generation, few-shot, frozen LLM bridging, instruction tuning 흐름을 만든다. PaLM-E는 VLM foundation이 embodied/robotics로 확장되는 early foundation이라 3D-VL/VLA gap을 이해하는 데 중요하다.

## Foundations: Vision-Language-Action and Robotics

**우선 읽기**

- Local: [CLIPort: What and Where Pathways for Robotic Manipulation](./2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md)
- Local: [BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning](./2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/01_overview.md)
- Local: [RT-1: Robotics Transformer for Real-World Control at Scale](./2022/arxiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md)
- Local: [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](./2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md)
- Local: [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](./2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md)
- Local: [VIMA: General Robot Manipulation with Multimodal Prompts](./2023/ICML/2023_ICML_VIMA-General-Robot-Manipulation-with-Multimodal-Prompts/01_overview.md)
- Local: [Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation](./2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md)
- Local: [RVT: Robotic View Transformer for 3D Object Manipulation](./2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md)
- Local: [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](./2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/01_overview.md)
- Local: [Octo: An Open-Source Generalist Robot Policy](./2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md)
- Local: [OpenVLA: An Open-Source Vision-Language-Action Model](./2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md)

**선정 이유:** VLA foundation은 language-conditioned manipulation, data scaling, action tokenization, embodiment generalization, 3D-aware manipulation representation으로 이어진다. RT-2/Open X/Octo/OpenVLA는 scaling과 open-source baseline의 축이고, PerAct/RVT/VoxPoser는 3D state와 action grounding의 축이라 3D CV 기반 contribution을 만들기 좋다.

## Language-Embedded NeRF and Gaussian Fields

**우선 읽기**

- Local: [EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding](./2026/CVPR/2026_CVPR_EmbodiedSplat-Online-Feed-Forward-Semantic-3DGS-for-Open-V/01_overview.md)
- Local: [LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds](./2026/CVPR/2026_CVPR_LightSplat-Fast-and-Memory-Efficient-Open-Vocabulary-3D-Sc/01_overview.md)
- Local: [CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](./2025/ICCV/2025_ICCV_CLIP-GS-Unifying-Vision-Language-Representation-with-3D-Ga/01_overview.md)
- Local: [SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining](./2025/ICCV/2025_ICCV_SceneSplat-Gaussian-Splatting-based-Scene-Understanding-wi/01_overview.md)
- Local: [ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](./2025/CVPR/2025_CVPR_ReasonGrounder-LVLM-Guided-Hierarchical-Feature-Splatting/01_overview.md)
- Local: [Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](./2025/CVPR/2025_CVPR_Dr.-Splat-Directly-Referring-3D-Gaussian-Splatting-via-Dir/01_overview.md)

**선정 이유:** LERF/LangSplat은 Foundation 섹션에만 남겼다. 이 섹션은 3DGS 기반 language field의 online/feed-forward construction, memory efficiency, LVLM-guided reasoning, direct referring, open-vocabulary scene understanding을 우선하며, robot memory와 navigation/manipulation query로 바로 확장된다.

## Navigation and Embodied AI

**우선 읽기**

- Local: [MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation](./2026/CVPR/2026_CVPR_MSGNav-Unleashing-the-Power-of-Multi-modal-3D-Scene-Graph/01_overview.md)
- Local: [GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation](./2026/CVPR/2026_CVPR_GA-VLN-Geometry-Aware-BEV-Representation-for-Efficient-Vis/01_overview.md)
- Local: [D3D-VLP: Dynamic 3D Vision-Language-Planning Model for Embodied Grounding and Navigation](./2026/CVPR/2026_CVPR_D3D-VLP-Dynamic-3D-Vision-Language-Planning-Model-for-Embo/01_overview.md)
- Local: [Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation](./2025/NeurIPS/2025_NeurIPS_Dynam3D-Dynamic-Layered-3D-Tokens-Empower-VLM-for-Vision-a/01_overview.md)
- Local: [BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation](./2025/NeurIPS/2025_NeurIPS_BeliefMapNav-3D-Voxel-Based-Belief-Map-for-Zero-Shot-Objec/01_overview.md)
- Local: [Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation](./2025/ICRA/2025_ICRA_Graph2Nav-3D-Object-Relation-Graph-Generation-to-Robot-Nav/01_overview.md)
- Local: [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](./2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md)
- Local: [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](./2024/ICRA/2024_ICRA_VLFM-Vision-Language-Frontier-Maps-for-Zero-Shot-Semantic/01_overview.md)

**선정 이유:** VLN foundation은 이미 확인했으므로 이 섹션은 최신 navigation flow에 집중한다. 최근 핵심은 frontier map에서 3D token, BEV geometry, 3D scene graph, belief map, Gaussian map, dynamic 3D planning으로 이동했으며, zero-shot object/VLN/navigation 성능과 실제 robot safety를 함께 평가할 수 있다.

## Open-Vocabulary 3D Mapping

**우선 읽기**

- Local: [AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting](./2025/ICCV/2025_ICCV_AutoOcc-Automatic-Open-Ended-Semantic-Occupancy-Annotation/01_overview.md)
- Local: [LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering](./2025/3DV/2025_3DV_LangOcc-Open-Vocabulary-Occupancy-Estimation-via-Volume-Re/01_overview.md)
- Local: [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](./2024/RA-L/2024_RA-L_FM-Fusion-Instance-aware-Semantic-Mapping-Boosted-by-Visio/01_overview.md)
- Local: [ConceptFusion: Open-set Multimodal 3D Mapping](./2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md)

**선정 이유:** EmbodiedSplat/LightSplat은 Language-Embedded 섹션에만 남겼다. 이 섹션은 2D CLIP/OpenSeg teacher의 단순 투영을 넘어 occupancy, Gaussian-guided annotation, instance-aware semantic mapping, open-set multimodal map construction과 query efficiency에 집중한다.

## Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception

**우선 읽기**

- Local: [RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction](./2025/ICCV/2025_ICCV_RIOcc-Efficient-Cross-Modal-Fusion-Transformer-with-Collab/01_overview.md)
- Local: [GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting](./2025/ICCV/2025_ICCV_GaussianOcc-Fully-Self-supervised-and-Efficient-3D-Occupan/01_overview.md)
- Local: [ODG: Occupancy Prediction Using Dual Gaussians](./2025/NeurIPS/2025_NeurIPS_ODG-Occupancy-Prediction-Using-Dual-Gaussians/01_overview.md)
- Local: [QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction](./2025/NeurIPS/2025_NeurIPS_QuadricFormer-Scene-as-Superquadrics-for-3D-Semantic-Occup/01_overview.md)
- Local: [V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection](./2025/CVPR/2025_CVPR_V2X-R-Cooperative-LiDAR-4D-Radar-Fusion-with-Denoising-Dif/01_overview.md)
- Local: [Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding](./2025/NeurIPS/2025_NeurIPS_Spiral-Semantic-Aware-Progressive-LiDAR-Scene-Generation-a/01_overview.md)
- Local: [Scaling Diffusion Models to Real-World 3D LiDAR Scene Completion](./2024/CVPR/2024_CVPR_Scaling-Diffusion-Models-to-Real-World-3D-LiDAR-Scene-Comp/01_overview.md)

**선정 이유:** Occ3D는 Foundation 섹션에만 남겼다. 이 섹션은 dense occupancy, Gaussian occupancy, self-supervised occupancy, LiDAR generation/completion, radar/LiDAR/camera cooperative fusion처럼 2025 이후 modality alignment, uncertainty, semantic occupancy efficiency가 뚜렷한 최신 흐름을 우선한다.

## Sensor Fusion, LiDAR, and Autonomous Driving

**우선 읽기**

- Local: [SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving](./2025/CVPR/2025_CVPR_SplatAD-Real-Time-Lidar-and-Camera-Rendering-with-3D-Gauss/01_overview.md)
- Local: [RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes](./2025/ICCV/2025_ICCV_RadarSplat-Radar-Gaussian-Splatting-for-High-Fidelity-Data/01_overview.md)
- Local: [TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving](./2024/ECCV/2024_ECCV_TCLC-GS-Tightly-Coupled-LiDAR-Camera-Gaussian-Splatting-fo/01_overview.md)

**선정 이유:** BEVFusion/UniAD 계열은 Foundation 섹션에만 남겼다. 이 섹션은 Gaussian rendering/reconstruction, occupancy, camera-LiDAR-radar fusion, 4D world generation처럼 differentiable rendering, sensor simulation, closed-loop planning relevance가 더 뚜렷한 최신 autonomous 3D perception 흐름을 우선한다.

## Vision-Language-Action and Robot Manipulation

**우선 읽기**

- Local: [PointVLA: Injecting the 3D World into Vision-Language-Action Models](./2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md)
- Local: [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](./2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/01_overview.md)
- Local: [ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation](./2026/CVPR/2026_CVPR_ConsisVLA-4D-Advancing-Spatiotemporal-Consistency-in-Effic/01_overview.md)
- Local: [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](./2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md)
- Local: [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](./2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md)
- Local: [3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation](./2025/CoRL/2025_CoRL_3DS-VLA-A-3D-Spatial-Aware-Vision-Language-Action-Model-fo/01_overview.md)
- Local: [GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](./2025/ICCV/2025_ICCV_GWM-Towards-Scalable-Gaussian-World-Models-for-Robotic-Man/01_overview.md)
- Local: [π0.5: a Vision-Language-Action Model with Open-World Generalization](./2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md)

**선정 이유:** OpenVLA는 Foundation 섹션에만 남겼다. 이 섹션은 3D state injection, 4D consistency, active perception, spatial memory, Gaussian world model, point-cloud robustness처럼 2025-2026 3D-aware VLA 계열을 우선한다.
