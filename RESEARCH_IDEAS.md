# Research Ideas

- Updated: 2026-06-30 KST
- Basis: `PAPER.md` 전체 registry, `PRIORITY.md` 최신 reading priority, 최근 추가된 SAM 2 및 2025-2026 3D CV/Robotics/Vision-Language 흐름
- Ranking: 각 카테고리 안에서 Idea 1 -> Idea 2 -> Idea 3 순서가 우선순위다.
- Ranking criteria: 연구 공백의 명확성, 평가 가능성, 구현 난이도, 데이터 접근성, 논문 contribution 가능성, 최신 트렌드 중 핵심 flow 여부
- Format: 기존 한계, 문제 정의, 왜 안 되는가와 필요한 방법 형태, 예상 평가, reference paper full name을 함께 기록한다.

## 3D Equivariance, Calibration, and Registration

### Idea 1. Self-diagnosing calibration-free 3D registration
- **Limit**: 최신 registration/SLAM은 calibration-free 또는 training-free를 내세우지만, 실패 시점과 실패 원인을 스스로 판단하지 못한다.
- **Problem**: camera-point cloud, color point cloud, monocular video를 대상으로 registration 결과의 degeneracy, drift, calibration mismatch를 함께 예측한다.
- **Why / Method**: visual feature, geometry, Gaussian map이 서로 맞는 것처럼 보여도 thin structure, 반복 패턴, 낮은 parallax에서 잘못 정렬된다. pose estimate와 함께 correspondence uncertainty, view-consistency residual, calibration residual을 출력하는 self-diagnostic registration module이 필요하다.
- **Eval**: 3DMatch, KITTI, nuScenes, ScanNet, ETH3D, custom perturbation; metrics: registration recall, RTE/RRE, calibration error, failure AUROC, drift recovery.
- **Refs**: VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency; C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion; RayI2P: Learning Rays for Image-to-Point Cloud Registration; GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion; GeoCalib: Learning Single-image Calibration with Geometric Optimization.

### Idea 2. Open-vocabulary map registration with semantic-geometric consistency
- **Limit**: 3D map alignment은 주로 geometric overlap을 기준으로 하며, language-queryable map이나 open-vocabulary map 간의 semantic consistency는 약하다.
- **Problem**: 서로 다른 시간, 센서, 로봇이 만든 open-vocabulary 3D map을 semantic identity와 geometry가 동시에 일치하도록 정렬한다.
- **Why / Method**: CLIP/VLM feature는 viewpoint와 texture에 흔들리고, pure geometry는 symmetric object에서 ambiguous하다. Gaussian/point correspondence에 object-level text prototypes와 3D relation constraints를 결합하는 two-level alignment가 필요하다.
- **Eval**: ScanNet, 3RScan, Replica, multi-robot RGB-D logs; metrics: alignment RTE/RRE, object match F1, open-vocabulary query AP, relation consistency.
- **Refs**: GaussReg: Fast 3D Registration with Gaussian Splatting; GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion; Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships; MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs; ConceptFusion: Open-set Multimodal 3D Mapping.

### Idea 3. Local equivariance for non-rigid and articulated registration
- **Limit**: SE(3)-equivariant registration은 rigid scene/object에는 강하지만 articulated object, deformable part, moving human-object interaction에는 부족하다.
- **Problem**: object part 단위의 local frame을 추정하고, part-wise equivariant correspondence를 통해 non-rigid alignment를 수행한다.
- **Why / Method**: global equivariance는 articulated motion을 하나의 rigid transform으로 압축한다. part graph, local symmetry, generative completion prior를 결합해 보이지 않는 part까지 정렬하는 구조가 필요하다.
- **Eval**: PartNet-Mobility, ShapeNetPart, DeformingThings4D, articulated manipulation logs; metrics: correspondence accuracy, part pose error, Chamfer, downstream manipulation success.
- **Refs**: EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation; DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo; G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation; PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models; Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation.

## 3D Generative Modeling and Diffusion

### Idea 1. Geometry-verified diffusion for sparse-view reconstruction
- **Limit**: video/2D diffusion prior 기반 3D generation은 plausible geometry를 만들지만, 관측 가능한 metric geometry와 충돌하는 hallucination이 남는다.
- **Problem**: sparse-view reconstruction에서 diffusion prior가 만든 구조를 multi-view geometry와 visibility로 검증하고, 불확실한 영역을 명시한다.
- **Why / Method**: denoising objective는 likelihood를 높일 뿐 observed rays, scale, epipolar consistency를 보장하지 않는다. diffusion sampling loop 안에 depth, silhouette, normal, ray consistency verifier를 넣고 hallucination map을 함께 예측해야 한다.
- **Eval**: DTU, CO3D, RealEstate10K, ScanNet, Tanks and Temples; metrics: Chamfer/F-score, PSNR/SSIM, depth AbsRel, hallucination precision/recall.
- **Refs**: HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction; G4Splat: Geometry-Guided Gaussian Splatting with Generative Prior; ReconFusion: 3D Reconstruction with Diffusion Priors; Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling; Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors.

### Idea 2. Controllable 4D world generation with physically checkable state
- **Limit**: 4D world generation은 scene dynamics를 생성하지만, downstream planning에서 필요한 occupancy, collision, object permanence를 직접 보장하지 않는다.
- **Problem**: generated future scene을 camera video가 아니라 4D Gaussian/occupancy state로 만들고, planning-relevant physical validity를 평가한다.
- **Why / Method**: visually plausible future라도 object size, free space, ego-motion consistency가 깨지면 robot/autonomous planning에는 쓸 수 없다. geometry-forced diffusion과 Gaussian-centric representation에 collision and visibility constraints를 결합해야 한다.
- **Eval**: nuScenes, Waymo, nuPlan, OpenScene driving; metrics: future occupancy IoU, motion ADE/FDE, collision rate, rendering metric, planning score.
- **Refs**: WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving; Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling; Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors; SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving; Planning-oriented Autonomous Driving.

### Idea 3. Part-level generative priors for manipulation-ready reconstruction
- **Limit**: object generation은 shape quality를 높이지만 robot manipulation에 필요한 part boundary, joint, contact affordance는 약하다.
- **Problem**: multi-view partial observation에서 part-level geometry와 affordance를 동시에 복원한다.
- **Why / Method**: single object mesh나 Gaussian은 actionable part를 숨긴다. part diffusion, semantic flow, contact-aware reconstruction을 결합해 grasp/push/open action으로 평가 가능한 representation이 필요하다.
- **Eval**: PartNet-Mobility, ShapeNetPart, RLBench, ManiSkill, real RGB-D manipulation; metrics: part IoU, joint axis error, affordance AP, manipulation success.
- **Refs**: PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models; G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation; SeaLion: Semantic Part-Aware Latent Point Diffusion Models; Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction; Diffusion Policy: Visuomotor Policy Learning via Action Diffusion.

## 3D Large Multimodal Models

### Idea 1. Geometry-grounded VLM with metric uncertainty and refusal
- **Limit**: 3D/Spatial VLM은 relative spatial question에는 강해졌지만 metric distance, support, containment, visibility 판단의 confidence calibration이 약하다.
- **Problem**: 3D scene question answering에서 답, 근거 geometry, uncertainty, refusal를 함께 출력하는 model을 만든다.
- **Why / Method**: LMM은 language prior로 답을 채우는 경향이 있고, 3D token이 실제 metric constraint를 위반해도 설명은 그럴듯하다. reconstruction-backed spatial verifier와 uncertainty head가 필요하다.
- **Eval**: ScanNet, EmbodiedScan, ScanQA/SQA3D, RoboSpatial, RealVLG-R1; metrics: QA accuracy, metric error, calibration ECE, hallucination/refusal accuracy.
- **Refs**: G2VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning; SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning; SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models; RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics; SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities.

### Idea 2. Video-to-3D LMM memory with reconstruction-reasoning feedback
- **Limit**: video-based LMM은 장면을 이해하지만, persistent 3D state가 없으면 long video에서 object identity와 spatial relation이 drift한다.
- **Problem**: video observations를 3D memory로 축적하고, reasoning result가 reconstruction update를 다시 수정하는 closed-loop LMM을 설계한다.
- **Why / Method**: frame-level captions나 masks는 occlusion 이후 identity를 잃는다. SAM 2 style memory, feed-forward geometry, scene graph memory, LMM reasoning을 연결하는 persistent state가 필요하다.
- **Eval**: 3RScan, ScanNet videos, Ego4D/EPIC-KITCHENS derived 3D tasks, robot exploration logs; metrics: object persistence F1, relation accuracy, 3D QA, update latency.
- **Refs**: GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models; SAM 2: Segment Anything in Images and Videos; Continuous 3D Perception Model with Persistent State; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images.

### Idea 3. Physical spatial intelligence benchmark for LMMs
- **Limit**: 기존 spatial VLM benchmark는 static QA 중심이라 robot action으로 이어지는 physical constraint를 충분히 측정하지 않는다.
- **Problem**: support, stability, reachability, occlusion, free-space, collision을 포함하는 3D physical reasoning benchmark를 만든다.
- **Why / Method**: VLM은 "위/아래/가까움"은 맞혀도 실제 놓기, 열기, 지나가기 가능성은 틀린다. 3D scene state와 executable simulator를 묶은 evaluation protocol이 필요하다.
- **Eval**: Habitat, AI2-THOR, ManiSkill, RLBench, EmbodiedBench; metrics: physical QA accuracy, executable success, collision/stability violation, explanation grounding.
- **Refs**: SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models; RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics; SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models; EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents; VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks.

## 3D Reconstruction, Geometry, and SLAM

### Idea 1. Semantic-prior feed-forward reconstruction with uncertainty
- **Limit**: DUSt3R/VGGT 계열 feed-forward reconstruction은 빠르지만, sparse/unposed images에서 semantic prior가 잘못 들어가면 geometry가 조용히 망가진다.
- **Problem**: semantic prior를 reconstruction에 쓰되, prior-induced error와 observed geometry error를 분리해 예측한다.
- **Why / Method**: semantic completion은 textureless/occluded region을 보완하지만, category prior가 실제 instance shape를 덮어쓸 수 있다. geometry residual과 semantic residual을 분리한 uncertainty-aware reconstruction이 필요하다.
- **Eval**: DTU, ETH3D, ScanNet, CO3D, Tanks and Temples; metrics: Chamfer/F-score, pose ATE, depth error, uncertainty calibration, semantic consistency.
- **Refs**: SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction; SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment; Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation; MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion; VGGT: Visual Geometry Grounded Transformer.

### Idea 2. Persistent-state SLAM for dynamic scenes
- **Limit**: SLAM은 static-world assumption에 기대고, 최신 feed-forward geometry도 long-range dynamic consistency가 약하다.
- **Problem**: camera pose, static map, dynamic object layer, semantic memory를 persistent state로 유지하는 SLAM을 만든다.
- **Why / Method**: moving objects를 outlier로 제거하면 robot task에 필요한 object state를 잃고, 모두 map에 넣으면 drift가 커진다. dynamic-static decomposition과 object-level memory가 함께 필요하다.
- **Eval**: TUM RGB-D dynamic, 3RScan, ScanNet video, KITTI/nuScenes dynamic sequences; metrics: ATE/RPE, dynamic object tracking, map IoU, long-range loop consistency.
- **Refs**: VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency; Continuous 3D Perception Model with Persistent State; DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction; DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras; GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting.

### Idea 3. SFM-free Gaussian reconstruction with risk-aware map quality
- **Limit**: SFM-free Gaussian reconstruction은 accessibility가 좋지만 pose/scale uncertainty가 downstream navigation에 어떻게 영향을 주는지 덜 다룬다.
- **Problem**: Gaussian reconstruction이 rendering quality뿐 아니라 collision/free-space risk까지 예측하도록 한다.
- **Why / Method**: PSNR이 높아도 thin object, glass, reflective region의 geometry가 틀리면 robot planning에서는 위험하다. Bayesian Gaussian parameters와 occupancy conversion을 함께 평가하는 framework가 필요하다.
- **Eval**: Replica, ScanNet, Tanks and Temples, Habitat navigation maps; metrics: PSNR/SSIM, depth error, collision false negative, SPL, uncertainty ECE.
- **Refs**: BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction; Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM; FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent; Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps; GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting.

## 3D Representation Learning and Foundation Models

### Idea 1. Task-aware 3D representation benchmark for robotics transfer
- **Limit**: 3D representation learning은 classification/segmentation transfer로 평가되지만, robot perception/action transfer와의 상관관계가 불명확하다.
- **Problem**: 3D foundation representation을 object reconstruction, semantic grounding, grasp/manipulation, navigation memory로 동일 protocol에서 평가한다.
- **Why / Method**: 좋은 point feature가 반드시 robot action에 좋은 feature는 아니다. task-conditioned probing, frozen encoder evaluation, low-data finetuning을 분리한 benchmark가 필요하다.
- **Eval**: ScanNet, Objaverse, RLBench, LIBERO, ManiSkill, EmbodiedScan; metrics: mIoU, retrieval, reconstruction Chamfer, success rate, sample efficiency.
- **Refs**: SUGAR: Pre-training 3D Visual Representations for Robotics; LaGeM: A Large Geometry Model for 3D Representation Learning and Diffusion; Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations; UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting; Dens3R: A Foundation Model for 3D Geometry Prediction.

### Idea 2. Unified 3D tokenizer across points, Gaussians, voxels, and images
- **Limit**: 최신 3D model은 representation별 tokenizer가 달라 downstream task 간 재사용이 어렵다.
- **Problem**: point cloud, Gaussian, voxel, multi-view image를 공통 3D token space로 정렬한다.
- **Why / Method**: representation-specific token은 modality shortcut을 학습한다. cross-representation masked prediction과 contrastive geometric consistency를 결합해 representation-agnostic token을 학습해야 한다.
- **Eval**: ShapeNet, Objaverse, ScanNet, SemanticKITTI, 3DGS reconstruction datasets; metrics: cross-format retrieval, transfer mIoU, reconstruction error, token efficiency.
- **Refs**: UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting; Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations; Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training; Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning; SplatFormer: Point Transformer for Robust 3D Gaussian Splatting.

### Idea 3. Continual 3D pretraining under sensor and domain shifts
- **Limit**: 3D foundation models는 dataset shift, sensor sparsity, outdoor/indoor scale 변화에서 성능 저하가 크다.
- **Problem**: 새로운 sensor distribution에 catastrophic forgetting 없이 적응하는 continual 3D pretraining 방법을 만든다.
- **Why / Method**: fixed pretraining corpus는 robot deployment의 lighting, LiDAR pattern, missing depth를 포괄하지 못한다. uncertainty-guided replay와 geometry consistency adaptation이 필요하다.
- **Eval**: ScanNet-to-S3DIS, SemanticKITTI-to-nuScenes, synthetic-to-real RGB-D; metrics: transfer mIoU, forgetting, robustness under dropout/noise, adaptation compute.
- **Refs**: U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching; Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training; Dens3R: A Foundation Model for 3D Geometry Prediction; Depth Anything V2; Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data.

## 3D Scene Graphs and Graph Reasoning

### Idea 1. Uncertainty-aware open-vocabulary 3D scene graph memory
- **Limit**: 3D scene graph는 object/relation을 구조화하지만 open-vocabulary label과 relation confidence가 robot planning에서 충분히 calibrated 되지 않는다.
- **Problem**: object, state, affordance, relation, uncertainty를 포함하는 queryable 3D scene graph memory를 만든다.
- **Why / Method**: VLM-derived relations는 hallucination이 있고, RGB-D graph update는 occlusion과 tracking failure가 있다. graph node/edge마다 evidence source, temporal confidence, geometric support를 저장해야 한다.
- **Eval**: 3RScan, ScanNet, Replica, robot mobile manipulation logs; metrics: object F1, relation F1, query AP, planning success, uncertainty ECE.
- **Refs**: MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation; Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs.

### Idea 2. Real-time RGB-D scene graph generation for active robots
- **Limit**: scene graph method는 offline reconstruction이나 느린 2D-to-3D fusion에 의존해 online robot control loop에 넣기 어렵다.
- **Problem**: RGB-D stream에서 real-time graph update와 task-relevant graph pruning을 동시에 수행한다.
- **Why / Method**: 모든 object/relation을 유지하면 memory와 latency가 커지고, pruning을 잘못하면 task evidence를 잃는다. task-conditioned graph sparsification과 incremental relation update가 필요하다.
- **Eval**: ScanNet streaming, Habitat, real RGB-D mobile robot; metrics: graph update FPS, relation F1, query latency, navigation/manipulation success.
- **Refs**: FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs; MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs; Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships; Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning.

### Idea 3. Counterfactual graph reasoning for language-conditioned planning
- **Limit**: graph reasoning은 현재 scene description에는 강하지만, "컵을 치우면 문이 열리는가" 같은 counterfactual planning에는 약하다.
- **Problem**: 3D scene graph에서 object state/action을 바꿨을 때 relation과 affordance가 어떻게 변하는지 예측한다.
- **Why / Method**: static relation graph는 action consequence를 표현하지 않는다. causal edge, state transition, geometric feasibility check를 가진 graph simulator가 필요하다.
- **Eval**: AI2-THOR, Habitat rearrangement, RLBench, VLABench; metrics: counterfactual QA, plan success, relation transition accuracy, intervention count.
- **Refs**: MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks.

## 3D Scene Representations and Neural Fields

### Idea 1. Task-usable Gaussian representation beyond rendering quality
- **Limit**: 3DGS 계열은 rendering PSNR 중심으로 발전했지만, perception/planning에 필요한 geometry, semantics, uncertainty가 분리되어 있지 않다.
- **Problem**: Gaussian primitive를 rendering, geometry, semantics, physical risk로 factorize한 task-usable scene representation을 만든다.
- **Why / Method**: color-density-semantic entanglement는 open-vocabulary query와 collision check를 동시에 망가뜨린다. geometry anchor와 semantic feature field를 분리하고, uncertainty를 planning map으로 변환해야 한다.
- **Eval**: ScanNet, Replica, LERF datasets, Habitat navigation; metrics: PSNR/SSIM, depth/normal error, open-vocabulary mIoU, collision false negative, query AP.
- **Refs**: ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting; PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting; SplatFormer: Point Transformer for Robust 3D Gaussian Splatting; SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering; Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps.

### Idea 2. Dynamic-static Gaussian memory for robot perception
- **Limit**: static Gaussian maps는 moving distractor나 object relocation이 있을 때 map corruption을 만든다.
- **Problem**: static background, movable object, transient distractor를 분리하고 object-level Gaussian memory를 업데이트한다.
- **Why / Method**: dynamic object를 제거만 하면 robot task의 핵심 object를 잃는다. dynamic-static decomposition, temporal object identity, forgetting/reinsertion rule이 필요하다.
- **Eval**: 3RScan, ScanNet dynamic, Replica dynamic, real indoor robot logs; metrics: reconstruction quality, change detection F1, object persistence, query accuracy over time.
- **Refs**: DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction; GWM: Towards Scalable Gaussian World Models for Robotic Manipulation; Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM; OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation.

### Idea 3. Sparse unposed image to semantic 3D field
- **Limit**: feed-forward 3DGS는 pose 없이 빠르게 scene을 만들 수 있지만 semantic query와 geometry faithfulness가 동시에 약하다.
- **Problem**: sparse unposed images에서 semantic Gaussian field를 만들고, map query/reconstruction을 동시에 평가한다.
- **Why / Method**: pose-free reconstruction은 geometry ambiguity가 크고, 2D feature lifting은 multi-view inconsistency가 있다. feed-forward pose estimation, semantic feature distillation, cross-view query consistency를 결합해야 한다.
- **Eval**: CO3D, RealEstate10K, ScanNet sparse views, LERF datasets; metrics: pose error, depth error, open-vocabulary AP, query consistency, runtime.
- **Refs**: SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images; Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM; EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding; LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds; LERF: Language Embedded Radiance Fields.

## 3D Semantic Understanding and Alignment

### Idea 1. Geometry-first open-vocabulary 3D segmentation with SAM 2 consistency
- **Limit**: open-vocabulary 3D segmentation은 2D foundation features를 투영하지만, mask boundary와 3D geometry가 어긋나는 문제가 크다.
- **Problem**: SAM 2 video masks, 3D geometry, open-vocabulary text features를 함께 사용해 temporally and geometrically consistent 3D segmentation을 만든다.
- **Why / Method**: frame별 2D masks는 viewpoint마다 identity가 흔들리고, point-only segmentation은 long-tail semantics가 약하다. video mask memory와 3D surface consistency를 묶어야 한다.
- **Eval**: ScanNet200, Matterport3D, Replica, 3RScan; metrics: open-vocabulary mIoU, mask boundary F-score, temporal consistency, novel class AP.
- **Refs**: SAM 2: Segment Anything in Images and Videos; GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation; Details Matter for Indoor Open-vocabulary 3D Instance Segmentation; Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding; OpenMask3D: Open-Vocabulary 3D Instance Segmentation.

### Idea 2. Novel object discovery with semantic consistency and geometric hierarchy
- **Limit**: open-vocabulary detection/segmentation은 novel object를 찾지만, unknown object가 part인지 instance인지 clutter인지 구분이 어렵다.
- **Problem**: open-vocabulary 3D object discovery에서 object-part-scene hierarchy를 동시에 예측한다.
- **Why / Method**: language similarity만으로는 "handle", "drawer", "cabinet"의 계층 관계를 구분하기 어렵다. geometric grouping, affordance prior, semantic hierarchy를 함께 학습해야 한다.
- **Eval**: ScanNet200, Replica, ARKitScenes, PartNet-Mobility; metrics: novel AP, hierarchy F1, part-instance consistency, open-vocabulary retrieval.
- **Refs**: OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection; Search3D: Hierarchical Open-Vocabulary 3D Segmentation; Open-Vocabulary Octree-Graph for 3D Scene Understanding; OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation; OpenScene: 3D Scene Understanding with Open Vocabularies.

### Idea 3. Transparent and reflective object semantic-geometric alignment
- **Limit**: RGB-D/NeRF/3DGS 기반 semantic mapping은 glass, mirror, reflective object에서 depth와 appearance prior가 동시에 실패한다.
- **Problem**: transparent/reflective region을 탐지하고, semantic label과 corrected geometry를 함께 복원한다.
- **Why / Method**: depth sensor의 missing value와 image feature의 reflection bias가 semantic hallucination을 만든다. uncertainty-aware depth completion과 semantic consistency check가 필요하다.
- **Eval**: ClearGrasp, TransCG, ScanNet reflective subsets, custom robot scenes; metrics: depth RMSE, normal error, segmentation mIoU, grasp success.
- **Refs**: Details Matter for Indoor Open-vocabulary 3D Instance Segmentation; GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation; Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation; Depth Anything V2; ConceptFusion: Open-set Multimodal 3D Mapping.

## 3D Vision-Language Grounding

### Idea 1. Ambiguity-aware 3D grounding for real robots
- **Limit**: 3D visual grounding은 top-1 object를 선택하지만, 실제 robot instruction은 ambiguity와 imperfect language가 많다.
- **Problem**: grounding candidate, ambiguity reason, clarification question, robot action risk를 함께 예측한다.
- **Why / Method**: "저 컵" 같은 표현은 viewpoint, user intent, object similarity에 따라 여러 후보가 된다. 3D relation reasoning과 uncertainty-driven interaction이 필요하다.
- **Eval**: RealVLG-R1, IRef-VLA, ScanRefer, Nr3D/Sr3D, real tabletop manipulation; metrics: grounding accuracy, ambiguity detection AUROC, clarification efficiency, task success.
- **Refs**: RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics; RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation; IRef-VLA: A Benchmark for Interactive Referential Grounding with Imperfect Language in 3D Scenes; Grounded 3D-Aware Spatial Vision-Language Modeling; SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding.

### Idea 2. Structured multi-view decomposition for grounding small and occluded objects
- **Limit**: multi-view 3D grounding은 view aggregation으로 성능을 높이지만, small object와 occluded target에서는 evidence가 희석된다.
- **Problem**: language query를 relation, attribute, viewpoint evidence로 분해하고, 각 evidence가 어느 view/3D region에서 나왔는지 추적한다.
- **Why / Method**: global feature pooling은 "behind the monitor" 같은 relation을 잃는다. structured view selection과 3D relation decomposition이 필요하다.
- **Eval**: ScanRefer, Nr3D/Sr3D, Multi3DRefer, ScanNet hidden-object splits; metrics: Acc@0.25/0.5, small-object accuracy, occlusion robustness, explanation grounding.
- **Refs**: ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition; SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding; VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding; Towards CLIP-driven Language-free 3D Visual Grounding via 2D-3D Relational Enhancement; 3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment.

### Idea 3. Physics-aware grounding for manipulation affordances
- **Limit**: object grounding은 target localization에 집중하고, " 잡을 수 있는 손잡이", "밀 수 있는 면" 같은 action-grounded phrase는 약하다.
- **Problem**: referring expression을 object, part, contact region, feasible action으로 ground한다.
- **Why / Method**: semantic label만으로는 action feasibility를 판단할 수 없다. geometry-derived contact feature와 language-conditioned affordance map을 grounding head에 넣어야 한다.
- **Eval**: PartNet-Mobility, RLBench, ManiSkill, real grasping; metrics: part grounding IoU, affordance AP, execution success, contact error.
- **Refs**: RoboGround: Robotic Manipulation with Grounded Vision-Language Priors; DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection; GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping.

## Benchmarks and Datasets

### Idea 1. Unified 3D spatial VLA benchmark with imperfect language
- **Limit**: VLA benchmark는 manipulation success를 보지만 3D grounding, ambiguity, safety, spatial memory를 분리 측정하기 어렵다.
- **Problem**: imperfect instruction, occlusion, ambiguous referring, safety constraint를 포함하는 unified 3D VLA benchmark를 만든다.
- **Why / Method**: single success metric은 perception failure와 policy failure를 섞는다. grounding, planning, action, recovery를 단계별로 기록하는 benchmark가 필요하다.
- **Eval**: simulator plus real subset; metrics: grounding accuracy, clarification success, safety violation, task success, recovery rate.
- **Refs**: RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation; RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation; RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation; LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models; IRef-VLA: A Benchmark for Interactive Referential Grounding with Imperfect Language in 3D Scenes.

### Idea 2. Open-vocabulary 3D mapping reproducibility benchmark
- **Limit**: open-vocabulary 3D mapping 논문은 서로 다른 prompts, 2D teachers, view selection, annotation protocol을 사용해 비교가 어렵다.
- **Problem**: 3D open-vocabulary mapping의 standard split, query set, memory/runtime budget, prompt protocol을 정의한다.
- **Why / Method**: map quality는 mIoU뿐 아니라 query speed, update speed, memory, novel class discovery로 결정된다. reproducible evaluation harness가 필요하다.
- **Eval**: ScanNet200, Matterport3D, Replica, EmbodiedScan; metrics: open-vocabulary mIoU/AP, memory, update latency, query latency, prompt sensitivity.
- **Refs**: EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI; ConceptFusion: Open-set Multimodal 3D Mapping; OpenScene: 3D Scene Understanding with Open Vocabularies; OpenMask3D: Open-Vocabulary 3D Instance Segmentation; FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models.

### Idea 3. Failure and safety benchmark for 3D-aware VLA
- **Limit**: VLA safety benchmark는 language refusal와 task success를 보지만, 3D geometry failure를 세부적으로 기록하지 않는다.
- **Problem**: collision, occlusion, unstable support, hidden object, calibration error, sensor dropout을 포함한 failure taxonomy를 만든다.
- **Why / Method**: 안전 실패는 language policy보다 perception/map uncertainty에서 시작되는 경우가 많다. 3D state difference와 failure cause annotation이 필요하다.
- **Eval**: LIBERO-Safety, VLABench, RLBench, real robot failure logs; metrics: safety violation rate, failure detection AUROC, recovery success, explanation accuracy.
- **Refs**: LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models; VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks; EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents; AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation; SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning.

## Equivariance, Diffusion, and 3D Action

### Idea 1. SE(3)-equivariant action diffusion with semantic correspondence
- **Limit**: diffusion policy는 action multimodality를 잘 다루지만, pose/rotation generalization과 object semantic correspondence를 구조적으로 보장하지 않는다.
- **Problem**: object local frame과 semantic correspondence를 기준으로 trajectory-level SE(3)-equivariant diffusion policy를 만든다.
- **Why / Method**: same task라도 object pose가 바뀌면 action distribution 전체가 rigid transform되어야 한다. equivariant denoising과 correspondence-conditioned action frame이 필요하다.
- **Eval**: RLBench, ManiSkill, LIBERO, category-level manipulation; metrics: success, unseen pose generalization, sample efficiency, trajectory error.
- **Refs**: EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation; ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY; DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo; Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation; Diffusion Policy: Visuomotor Policy Learning via Action Diffusion.

### Idea 2. Grounded value-map action diffusion
- **Limit**: value-map planning은 interpretable하지만 continuous trajectory generation에는 약하고, diffusion policy는 interpretable grounding이 약하다.
- **Problem**: 3D spatial value map을 diffusion policy의 condition으로 사용해 action generation과 grounding을 결합한다.
- **Why / Method**: VLM/LLM이 만든 spatial constraints는 discrete symbolic plan에 머무르기 쉽다. value map을 score guidance로 넣어 denoising trajectory가 relation/keypoint constraint를 만족하게 해야 한다.
- **Eval**: RLBench, CALVIN, LIBERO, real tabletop; metrics: success, constraint satisfaction, collision rate, explanation-grounding consistency.
- **Refs**: GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation; RoboGround: Robotic Manipulation with Grounded Vision-Language Priors.

### Idea 3. Active perception for equivariant manipulation policies
- **Limit**: equivariant manipulation policy는 관측된 point cloud에는 강하지만 occlusion이 큰 경우 어느 view를 더 봐야 하는지 모른다.
- **Problem**: action uncertainty와 equivariance error를 기준으로 next-best-view를 선택하는 active 3D manipulation policy를 만든다.
- **Why / Method**: pose ambiguity는 추가 view로 줄일 수 있지만, random view acquisition은 cost가 크다. action score variance와 correspondence uncertainty를 view selection reward로 사용해야 한다.
- **Eval**: RLBench active view, ManiSkill, real wrist-camera robot; metrics: success per view, view count, action uncertainty reduction, execution time.
- **Refs**: ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation; EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation; DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo; DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation; SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics.

## Foundations: 3D Detection and BEV Perception

### Idea 1. BEV perception with explicit depth and calibration uncertainty
- **Limit**: BEV fusion model은 camera/LiDAR/radar feature를 잘 합치지만 depth와 calibration uncertainty가 downstream decision에 명시적으로 전달되지 않는다.
- **Problem**: BEV detection/occupancy output과 함께 per-cell uncertainty source를 예측한다.
- **Why / Method**: wrong depth나 extrinsic drift는 BEV false evidence를 만든다. depth distribution, calibration residual, modality agreement를 BEV token에 보존해야 한다.
- **Eval**: nuScenes, Waymo, Argoverse, KITTI perturbation; metrics: NDS, mAP, occupancy IoU, ECE, fault detection AUROC.
- **Refs**: BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers; BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation; BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection; RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction; GeoCalib: Learning Single-image Calibration with Geometric Optimization.

### Idea 2. Open-vocabulary 3D detection with geometric verification
- **Limit**: open-vocabulary 3D detection은 2D/LLM priors에 의존해 geometry와 맞지 않는 class hallucination이 발생한다.
- **Problem**: long-tail object를 detect하면서 shape, size, support, free-space plausibility를 검증한다.
- **Why / Method**: text-image similarity는 objectness를 보장하지 않는다. category-agnostic geometry proposal과 class-conditioned physical plausibility check가 필요하다.
- **Eval**: ScanNet200, nuScenes, Waymo, OV-3D detection splits; metrics: open-vocabulary AP, false-positive rate, size/orientation error, geometry consistency.
- **Refs**: OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection; Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection; OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation; OpenScene: 3D Scene Understanding with Open Vocabularies; Open-Vocabulary Octree-Graph for 3D Scene Understanding.

### Idea 3. Foundation BEV tokens for planning transfer
- **Limit**: BEV features는 detection/segmentation에 최적화되어 planning이나 VLA의 reusable state로 바로 쓰기 어렵다.
- **Problem**: occupancy, semantics, motion, affordance, risk를 담는 general BEV token을 pretrain한다.
- **Why / Method**: detection label은 free-space와 interaction geometry를 충분히 감독하지 않는다. masked BEV modeling, future occupancy, language-conditioned scene query를 결합해야 한다.
- **Eval**: nuScenes, Waymo, nuPlan, OpenScene driving; metrics: detection NDS, occupancy mIoU, motion ADE/FDE, collision/rule violation, planning score.
- **Refs**: BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers; Planning-oriented Autonomous Driving; V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection; WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving; Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving.

## Foundations: 3D Geometry and Point Clouds

### Idea 1. Density-invariant point-cloud foundation features
- **Limit**: point cloud foundation features는 sampling density, LiDAR scan pattern, RGB-D noise에 민감하다.
- **Problem**: nonuniform density와 missing region에서도 stable한 3D feature를 학습한다.
- **Why / Method**: fixed radius neighborhood와 FPS는 sensor bias를 encode한다. density-normalized local frame, masked completion, cross-sensor contrastive learning이 필요하다.
- **Eval**: ModelNet40, ShapeNetPart, ScanNet, S3DIS, SemanticKITTI, nuScenes; metrics: accuracy, mIoU, robustness curve under dropout/downsampling, transfer performance.
- **Refs**: PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation; PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space; Dynamic Graph CNN for Learning on Point Clouds; KPConv: Flexible and Deformable Convolution for Point Clouds; Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning.

### Idea 2. Geometry primitives as interpretable tokens
- **Limit**: deep 3D embeddings는 강력하지만 plane, quadric, symmetry, joint 같은 interpretable geometry를 명시적으로 제공하지 않는다.
- **Problem**: scene/object를 primitive token으로 분해하고, downstream graph reasoning과 manipulation에 연결한다.
- **Why / Method**: dense features는 causal geometry를 숨긴다. primitive fitting objective와 semantic relation objective를 함께 사용해야 한다.
- **Eval**: ABC, ShapeNet, ScanNet planes, PartNet-Mobility; metrics: primitive fitting error, segmentation IoU, reconstruction Chamfer, relation accuracy.
- **Refs**: PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space; QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction; PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-forward Planar Splatting; SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks; SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs.

### Idea 3. Universal 3D correspondence pretraining
- **Limit**: registration, tracking, grounding, manipulation correspondence가 각각 따로 학습되어 data efficiency가 낮다.
- **Problem**: object, scene, time을 가로지르는 universal 3D correspondence backbone을 만든다.
- **Why / Method**: classification-style pretraining은 equivalence relation을 배우지 않는다. cycle consistency, scene flow, multi-view reconstruction, semantic part matching을 동시에 학습해야 한다.
- **Eval**: 3DMatch, KITTI scene flow, FlyingThings3D, ScanNet tracking, DenseMatcher tasks; metrics: correspondence accuracy, EPE, registration recall, transfer success.
- **Refs**: Deep Closest Point: Learning Representations for Point Cloud Registration; CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences; FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent; DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo; G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation.

## Foundations: 3D Representation Learning

### Idea 1. Cross-representation masked modeling
- **Limit**: masked point modeling은 point cloud 성능을 높이지만 mesh, voxel, Gaussian, multi-view image로의 transfer가 제한적이다.
- **Problem**: 동일 3D object/scene을 여러 representation으로 보고 missing structure를 cross-format으로 예측한다.
- **Why / Method**: single-format mask는 format shortcut을 만든다. point-to-Gaussian, image-to-point, voxel-to-mesh reconstruction target을 섞어야 한다.
- **Eval**: ShapeNet, Objaverse, ScanNet, CO3D; metrics: classification/segmentation transfer, reconstruction Chamfer, cross-format retrieval, few-shot adaptation.
- **Refs**: Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling; Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning; UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting; Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training; Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations.

### Idea 2. Geometry-aware prompting for 3D foundation models
- **Limit**: 3D prompting은 2D SAM/CLIP prompt에 비해 point, plane, path, relation prompt가 체계화되지 않았다.
- **Problem**: few-shot 3D tasks를 geometric prompt로 제어하는 prompt interface를 정의한다.
- **Why / Method**: text prompt만으로는 scale, orientation, hidden surface가 불명확하다. point/box/plane/path/symmetry prompt를 token화해야 한다.
- **Eval**: ScanNet, S3DIS, ShapeNetPart, object affordance datasets; metrics: few-shot mIoU, prompt efficiency, cross-domain transfer, user correction count.
- **Refs**: GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model; Segment Any 3D Object with Language; Segment Anything; SAM 2: Segment Anything in Images and Videos; Uni3DL: A Unified Model for 3D Vision-Language Understanding.

### Idea 3. Scale-consistent 3D pretraining
- **Limit**: object-scale model은 room/city-scale scene에 약하고, outdoor LiDAR model은 object part geometry에 약하다.
- **Problem**: physical scale embedding과 hierarchical token을 가진 scale-consistent 3D representation을 학습한다.
- **Why / Method**: fixed receptive field는 scale shortcut을 만든다. metric-aware positional encoding과 multi-scale reconstruction target이 필요하다.
- **Eval**: Objaverse, ScanNet/S3DIS, SemanticKITTI/nuScenes; metrics: transfer mIoU, detection mAP, scale generalization, robustness to unit/scale perturbation.
- **Refs**: PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space; KPConv: Flexible and Deformable Convolution for Point Clouds; 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks; Dens3R: A Foundation Model for 3D Geometry Prediction; UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction.

## Foundations: 3D Scene Representations

### Idea 1. Factorized scene representation for geometry, appearance, semantics, and physics
- **Limit**: NeRF/3DGS scene representation은 color, density, semantics가 entangled되어 editing, querying, planning이 서로 방해된다.
- **Problem**: geometry, appearance, material, semantic, physical affordance field를 분리한 scene representation을 만든다.
- **Why / Method**: rendering objective만으로는 surface correctness와 semantic consistency를 보장하지 않는다. factor-specific loss와 cross-factor consistency가 필요하다.
- **Eval**: Replica, ScanNet, DTU, NeRF synthetic, LERF datasets; metrics: PSNR/SSIM, depth/normal error, edit consistency, semantic mIoU, query AP.
- **Refs**: NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis; 3D Gaussian Splatting for Real-Time Radiance Field Rendering; ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting; SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering; PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting.

### Idea 2. Neural field as active robot memory
- **Limit**: neural fields는 offline asset로 쓰이는 경우가 많고, robot memory처럼 update, delete, query, uncertainty를 갖추지 못했다.
- **Problem**: streaming observations로 업데이트되는 task-conditioned neural/Gaussian memory를 만든다.
- **Why / Method**: robot은 scene change와 new instruction에 대응해야 한다. online update, memory compression, uncertainty-guided exploration이 필요하다.
- **Eval**: Habitat, Replica, ScanNet, real RGB-D robot scans; metrics: update time, map accuracy, query accuracy, memory footprint, task success.
- **Refs**: CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory; ConceptFusion: Open-set Multimodal 3D Mapping; OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting; S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction; VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting.

### Idea 3. Hybrid explicit-implicit maps for conservative planning
- **Limit**: implicit map은 rich query에는 좋지만 collision check에는 위험하고, explicit occupancy는 semantics가 부족하다.
- **Problem**: occupancy/mesh의 conservative free space와 neural/Gaussian semantic field를 동기화한다.
- **Why / Method**: planning은 빠른 conservative geometry가 필요하고 reasoning은 rich semantics가 필요하다. dual map과 consistency constraint가 필요하다.
- **Eval**: Habitat navigation, Replica/ScanNet manipulation, real robot maps; metrics: collision rate, SPL, map IoU, open-vocabulary query AP, runtime.
- **Refs**: NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis; 3D Gaussian Splatting for Real-Time Radiance Field Rendering; Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps; FOCI: Trajectory Optimization on Gaussian Splats; ConceptFusion: Open-set Multimodal 3D Mapping.

## Foundations: 3D Semantic Occupancy

### Idea 1. Planning-safe semantic occupancy uncertainty
- **Limit**: semantic occupancy는 occupied/free/semantic point estimate를 주지만, planner가 필요한 risk bound는 부족하다.
- **Problem**: visibility, sensor noise, semantic confusion을 반영한 occupancy uncertainty를 예측한다.
- **Why / Method**: unknown space와 false free space를 구분하지 못하면 collision risk가 커진다. Gaussian occupancy와 ensemble/Bayesian calibration을 결합해야 한다.
- **Eval**: Occ3D, SemanticKITTI, nuScenes occupancy, Habitat; metrics: occupancy IoU, semantic mIoU, ECE, risk-weighted collision rate, unknown recall.
- **Refs**: VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion; OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction; GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction; ODG: Occupancy Prediction Using Dual Gaussians; QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction.

### Idea 2. Open-vocabulary semantic occupancy from RGB video
- **Limit**: occupancy estimation은 closed-set label과 LiDAR supervision에 의존하는 경우가 많다.
- **Problem**: RGB video만으로 dense occupancy와 open-vocabulary semantic label을 함께 예측한다.
- **Why / Method**: 2D semantics는 rich하지만 occluded 3D structure를 모른다. monocular/video geometry, VLM feature lifting, occupancy completion prior를 묶어야 한다.
- **Eval**: Occ3D, ScanNet occupancy, SemanticKITTI, EmbodiedOcc splits; metrics: occupancy IoU, open-vocabulary mIoU/AP, occluded-region accuracy, temporal consistency.
- **Refs**: AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting; LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering; EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding; MonoScene: Monocular 3D Semantic Scene Completion; VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion.

### Idea 3. Object-centric occupancy for manipulation
- **Limit**: voxel occupancy는 navigation에는 유용하지만 manipulation의 part/contact resolution에는 거칠다.
- **Problem**: object-part-level occupancy와 affordance label을 함께 예측한다.
- **Why / Method**: grasp/open/push는 surface contact와 joint geometry가 필요하다. object-centric occupancy heads와 part supervision이 필요하다.
- **Eval**: PartNet-Mobility, RLBench, ManiSkill, real RGB-D grasping; metrics: part IoU, affordance AP, grasp success, collision rate.
- **Refs**: SSCNet: Semantic Scene Completion from a Single Depth Image; OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection; GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping; Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction; PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models.

## Foundations: Diffusion and Generative Models

### Idea 1. Metric-constrained diffusion prior for 3D perception
- **Limit**: diffusion prior는 strong generator지만 metric estimator로는 hallucination 위험이 있다.
- **Problem**: diffusion posterior를 sensor observation, ray consistency, scale constraint로 제어한다.
- **Why / Method**: pure denoising은 plausible output을 만들지만 관측 데이터와의 물리적 일치를 강제하지 않는다. differentiable rendering과 geometric optimization을 sampling loop에 넣어야 한다.
- **Eval**: DTU, CO3D, ScanNet, KITTI/NYUv2 depth; metrics: Chamfer/F-score, depth AbsRel, hallucination rate, uncertainty calibration.
- **Refs**: Denoising Diffusion Probabilistic Models; Denoising Diffusion Implicit Models; Score-Based Generative Modeling through Stochastic Differential Equations; High-Resolution Image Synthesis with Latent Diffusion Models; DreamFusion: Text-to-3D using 2D Diffusion.

### Idea 2. Diffusion uncertainty as downstream perception confidence
- **Limit**: diffusion sample diversity는 많지만 robot/autonomous decision에 쓸 수 있는 calibrated uncertainty로 변환되지 않는다.
- **Problem**: diffusion samples의 다양성을 geometric ambiguity와 model uncertainty로 분리한다.
- **Why / Method**: 여러 sample이 다르면 실제 ambiguity인지 model artifact인지 알기 어렵다. sensor consistency와 posterior variance decomposition이 필요하다.
- **Eval**: NYUv2, KITTI, ScanNet, sparse-view reconstruction; metrics: NLL, ECE, AUROC for error detection, downstream risk reduction.
- **Refs**: Denoising Diffusion Probabilistic Models; Bayesian Diffusion Models for 3D Shape Reconstruction; HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction; Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation; ReconFusion: 3D Reconstruction with Diffusion Priors.

### Idea 3. Multi-modal diffusion for sensor completion
- **Limit**: RGB, depth, LiDAR, radar, tactile completion 방법이 분리되어 있고 missingness pattern을 공유하지 못한다.
- **Problem**: modality token을 가진 shared diffusion backbone으로 missing geometry와 semantics를 완성한다.
- **Why / Method**: 각 센서는 서로 다른 blind spot을 가진다. common 3D latent와 modality-specific noise model을 함께 학습해야 한다.
- **Eval**: nuScenes, Waymo, SemanticKITTI, tactile reconstruction datasets; metrics: completion IoU, Chamfer, mIoU, robustness under sensor dropout.
- **Refs**: V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection; Scaling Diffusion Models to Real-World 3D LiDAR Scene Completion; Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion; Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction; L3DR: 3D-aware LiDAR Diffusion and Rectification.

## Foundations: Equivariance and Geometry

### Idea 1. Learned equivariance selection for mixed 3D scenes
- **Limit**: fixed SE(3)/E(n) equivariance는 rigid object에는 적합하지만 articulated parts, gravity-dependent semantics, deformable objects에는 과하거나 부족할 수 있다.
- **Problem**: scene region별로 equivariant, invariant, variant transformation을 선택하는 model을 만든다.
- **Why / Method**: 모든 feature를 같은 symmetry group으로 묶으면 semantic labels와 physical constraints가 깨진다. local symmetry gating과 group-specific attention이 필요하다.
- **Eval**: ModelNet, ShapeNetPart, PartNet-Mobility, RLBench; metrics: accuracy, equivariance error, sample efficiency, out-of-pose generalization.
- **Refs**: Group Equivariant Convolutional Networks; Tensor Field Networks: Rotation- and Translation-Equivariant Neural Networks for 3D Point Clouds; SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks; E(n) Equivariant Graph Neural Networks; EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation.

### Idea 2. Geometry-aware attention with local physical frames
- **Limit**: transformer attention은 3D tokens를 sequence로 처리해 metric distance와 local frame을 잃기 쉽다.
- **Problem**: local tangent frame, gravity frame, object frame을 attention kernel에 넣어 geometry-aware transformer를 만든다.
- **Why / Method**: absolute coordinates는 dataset frame에 overfit된다. relative pose와 invariant/equivariant kernels가 필요하다.
- **Eval**: ScanNet segmentation, 3DMatch registration, ShapeNetPart, manipulation correspondence; metrics: mIoU, correspondence accuracy, generalization under rotation/scale.
- **Refs**: Point Transformer; SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks; E(n) Equivariant Graph Neural Networks; Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation; DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo.

### Idea 3. Equivariant memory for dynamic environments
- **Limit**: equivariant model은 single object/action에는 좋지만 long-term dynamic scene memory에는 덜 적용됐다.
- **Problem**: object pose changes에 equivariant하게 업데이트되는 scene memory를 만든다.
- **Why / Method**: memory slot이 world coordinate에 고정되면 object motion마다 feature가 바뀐다. object-centric canonical memory와 pose-conditioned update가 필요하다.
- **Eval**: 3RScan, dynamic ScanNet, mobile manipulation logs; metrics: object re-identification, relation consistency, memory drift, downstream task success.
- **Refs**: Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation; Flow Equivariant World Models: Structured Memory for Dynamic Environments; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; GWM: Towards Scalable Gaussian World Models for Robotic Manipulation.

## Foundations: Monocular Geometry

### Idea 1. Metric monocular depth with calibration-aware scale reasoning
- **Limit**: monocular depth foundation models는 relative depth는 강하지만 camera intrinsics, scale, domain에 따른 metric error가 남는다.
- **Problem**: single image에서 metric depth와 camera calibration uncertainty를 함께 예측한다.
- **Why / Method**: focal length와 scene scale ambiguity가 depth error의 핵심이다. depth model과 geometric optimization/calibration head를 함께 학습해야 한다.
- **Eval**: NYUv2, KITTI, ETH3D, ScanNet, zero-shot depth benchmarks; metrics: AbsRel, RMSE, scale error, calibration error, ECE.
- **Refs**: Depth Map Prediction from a Single Image using a Multi-Scale Deep Network; Digging Into Self-Supervised Monocular Depth Estimation; UniDepth: Universal Monocular Metric Depth Estimation; Depth Anything V2; GeoCalib: Learning Single-image Calibration with Geometric Optimization.

### Idea 2. Diffusion depth models that expose hallucination
- **Limit**: diffusion-based depth는 visually plausible하고 sharp하지만 unseen/reflective/textureless region에서 hallucination을 만들 수 있다.
- **Problem**: diffusion depth output에 hallucination risk map과 sensor-consistency score를 붙인다.
- **Why / Method**: image prior가 strong할수록 실제 metric geometry와 충돌할 수 있다. denoising trajectory variance와 multi-view/depth sensor check가 필요하다.
- **Eval**: NYUv2, KITTI, ScanNet, transparent/reflective subsets; metrics: depth error, hallucination AUROC, uncertainty ECE, downstream reconstruction quality.
- **Refs**: Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation; Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data; Depth Anything V2; PRISM: Learning Realistic Depth via Physics-Grounded Noise; HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction.

### Idea 3. Monocular geometry as reusable robot mapping prior
- **Limit**: monocular depth는 standalone depth metric으로 평가되지만 robot mapping에서 uncertainty-aware prior로 쓰이는 방식은 덜 정리됐다.
- **Problem**: monocular geometry를 RGB-D/LiDAR sparse observations와 융합하는 prior adapter를 만든다.
- **Why / Method**: monocular prior는 dense하지만 scale-ambiguous하고, sparse sensor는 accurate하지만 incomplete하다. confidence-weighted fusion이 필요하다.
- **Eval**: ScanNet, Replica, Matterport3D, real robot RGB-D with missing depth; metrics: map IoU, depth RMSE, collision rate, mapping update latency.
- **Refs**: Vision Transformers for Dense Prediction; UniDepth: Universal Monocular Metric Depth Estimation; Depth Anything V2; EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding; FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models.

## Foundations: RL and Imitation Learning

### Idea 1. 3D state abstraction for offline robot learning
- **Limit**: offline RL/IL은 image/action sequence에 의존해 3D state abstraction과 contact geometry를 충분히 쓰지 못한다.
- **Problem**: object-centric 3D state를 offline trajectory learning의 intermediate representation으로 사용한다.
- **Why / Method**: raw image tokens는 viewpoint shift와 occlusion에 취약하다. object pose, affordance, contact, free-space token을 action model에 제공해야 한다.
- **Eval**: Open X-Embodiment, BridgeData, LIBERO, RLBench; metrics: success, data efficiency, out-of-view robustness, embodiment transfer.
- **Refs**: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning; Generative Adversarial Imitation Learning; Decision Transformer: Reinforcement Learning via Sequence Modeling; Diffusion Policy: Visuomotor Policy Learning via Action Diffusion; Open X-Embodiment: Robotic Learning Datasets and RT-X Models.

### Idea 2. RL from VLM feedback grounded in 3D checks
- **Limit**: VLM feedback는 language plausibility에 흔들리고 physical feasibility를 잘못 평가할 수 있다.
- **Problem**: VLM reward를 3D geometry check, contact check, safety check로 보정한다.
- **Why / Method**: VLM은 "성공처럼 보이는" image를 reward할 수 있다. 3D state difference와 physical constraints를 reward verifier로 넣어야 한다.
- **Eval**: RLBench, ManiSkill, CALVIN, LIBERO-Safety; metrics: reward correlation, success, safety violation, sim-to-real transfer.
- **Refs**: Proximal Policy Optimization Algorithms; Training language models to follow instructions with human feedback; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models.

### Idea 3. Imitation learning with counterfactual view synthesis
- **Limit**: demonstration data는 camera viewpoint와 occlusion bias를 포함하며, policy가 이를 shortcut으로 학습한다.
- **Problem**: 3D scene representation으로 counterfactual views를 생성해 IL policy를 regularize한다.
- **Why / Method**: same state를 다른 view에서 보아도 action이 일관되어야 한다. Gaussian/NeRF view synthesis와 action consistency loss가 필요하다.
- **Eval**: RLBench, BridgeData, CALVIN, real robot demos; metrics: view generalization, success, action consistency, data efficiency.
- **Refs**: Diffusion Policy: Visuomotor Policy Learning via Action Diffusion; Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation; RVT: Robotic View Transformer for 3D Object Manipulation; DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation; GWM: Towards Scalable Gaussian World Models for Robotic Manipulation.

## Foundations: SLAM and Sensor Geometry

### Idea 1. Multi-sensor SLAM with learned degeneracy detection
- **Limit**: SLAM/odometry는 textureless, corridor, fast motion, calibration drift에서 failure를 일으키지만 online degeneracy 판단이 약하다.
- **Problem**: LiDAR-camera-IMU-GNSS SLAM에서 degeneracy type과 recovery action을 예측한다.
- **Why / Method**: residual이 커졌을 때 원인이 motion blur, lack of parallax, LiDAR sparsity, calibration인지 구분해야 한다. sensor-specific residual attribution이 필요하다.
- **Eval**: KITTI, EuRoC, TUM RGB-D, nuScenes, custom perturbation; metrics: ATE/RPE, failure detection AUROC, recovery time, calibration drift error.
- **Refs**: PTAM: Parallel Tracking and Mapping for Small AR Workspaces; ORB-SLAM: A Versatile and Accurate Monocular SLAM System; DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras; FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry; VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency.

### Idea 2. Semantic loop closure with geometric verification
- **Limit**: semantic loop closure는 perceptual aliasing에 취약하고, pure geometry loop closure는 scene change에 약하다.
- **Problem**: object/relation graph와 local geometry descriptor를 함께 사용해 loop closure를 검증한다.
- **Why / Method**: 같은 category object가 반복되는 indoor scene에서 semantic만으로는 false loop가 많다. relation topology, metric layout, feature correspondence를 함께 확인해야 한다.
- **Eval**: ScanNet, 3RScan, Matterport3D, robot mapping logs; metrics: loop precision/recall, ATE improvement, false loop rate, map consistency.
- **Refs**: Structure-from-Motion Revisited; ElasticFusion: Dense SLAM Without A Pose Graph; BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Reintegration; SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs; Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships.

### Idea 3. SLAM maps that expose planning risk
- **Limit**: SLAM map은 localization/reconstruction accuracy 중심이며, planner가 map risk를 직접 알기 어렵다.
- **Problem**: map cell/surface마다 observation support, dynamic risk, semantic collision risk를 기록한다.
- **Why / Method**: thin object나 recently changed object는 reconstruction metric이 좋아도 위험하다. observation provenance와 uncertainty-aware occupancy conversion이 필요하다.
- **Eval**: Habitat, real indoor navigation, Replica/ScanNet maps; metrics: ATE, map IoU, collision rate, risk calibration, SPL.
- **Refs**: KinectFusion: Real-Time Dense Surface Mapping and Tracking; ElasticFusion: Dense SLAM Without A Pose Graph; GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting; Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps; Continuous 3D Perception Model with Persistent State.

## Foundations: Transformer and Language Models

### Idea 1. Geometry-aware context compression for long 3D scenes
- **Limit**: LLM/VLM context는 long 3D scene memory를 모두 넣기 어렵고, naive summarization은 geometry relation을 잃는다.
- **Problem**: 3D scene graph와 spatial tokens를 LLM context에 맞게 압축하는 geometry-aware summarizer를 만든다.
- **Why / Method**: text summary는 metric relation과 visibility를 보존하지 않는다. object relation graph, spatial cluster, uncertainty를 보존하는 retrieval/compression이 필요하다.
- **Eval**: ScanQA/SQA3D, EmbodiedBench, VLABench, navigation instruction tasks; metrics: QA accuracy, relation preservation, token budget, planning success.
- **Refs**: Attention Is All You Need; Language Models are Few-Shot Learners; Chain-of-Thought Prompting Elicits Reasoning in Large Language Models; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models.

### Idea 2. Chain-of-geometry reasoning for LLM planners
- **Limit**: chain-of-thought는 symbolic reasoning에는 유용하지만 3D geometry verification 없이 plausible plan을 만든다.
- **Problem**: LLM plan step마다 distance, visibility, support, collision, reachability check를 호출하는 reasoning protocol을 만든다.
- **Why / Method**: language-only reasoning은 physical constraint를 검산하지 못한다. external 3D tools와 structured verifier가 필요하다.
- **Eval**: Habitat, ALFRED, RLBench, VLABench; metrics: plan success, geometric violation rate, tool-call efficiency, explanation accuracy.
- **Refs**: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models; Training language models to follow instructions with human feedback; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models.

### Idea 3. Retrieval-augmented 3D reasoning from persistent scene memories
- **Limit**: LLM planner는 현재 observation만 보고 과거 scene changes와 hidden object를 잊기 쉽다.
- **Problem**: persistent 3D scene memory에서 relevant object/relation/history를 검색해 LLM reasoning에 주입한다.
- **Why / Method**: text-only memory는 spatial grounding이 약하다. object-centric 3D memory와 graph retrieval이 필요하다.
- **Eval**: 3RScan, AI2-THOR rearrangement, mobile manipulation logs; metrics: retrieval recall, task success, hidden-object query accuracy, hallucination rate.
- **Refs**: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding; Visual Instruction Tuning; PaLM-E: An Embodied Multimodal Language Model; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action.

## Foundations: Vision Foundation Models

### Idea 1. SAM 2 based temporally consistent 3D segmentation teacher
- **Limit**: SAM/SAM 2는 2D/video mask quality가 뛰어나지만, 3D geometry consistency와 open-vocabulary labels를 직접 보장하지 않는다.
- **Problem**: SAM 2 mask memory를 3D semantic map의 temporal teacher로 사용하고, mask identity drift를 geometry로 보정한다.
- **Why / Method**: video masks는 occlusion 이후 identity drift가 있고, 3D projection은 calibration/depth noise가 있다. mask memory, 3D surface clustering, open-set label assignment를 함께 사용해야 한다.
- **Eval**: ScanNet videos, 3RScan, Replica, open-vocabulary 3D segmentation; metrics: mIoU/AP, temporal IDF1, boundary F-score, query consistency.
- **Refs**: Segment Anything; SAM 2: Segment Anything in Images and Videos; Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection; OpenMask3D: Open-Vocabulary 3D Instance Segmentation; GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation.

### Idea 2. Foundation feature agreement as reconstruction failure detector
- **Limit**: reconstruction method는 geometric metrics 없이 deployment에서 실패를 알기 어렵다.
- **Problem**: DINOv2/SAM/Grounding DINO feature consistency로 3D reconstruction/map failure를 감지한다.
- **Why / Method**: feature disagreement across views often indicates wrong geometry, occlusion, or dynamic object. Multi-view feature reprojection residual can serve as a self-supervised failure signal.
- **Eval**: DTU, ScanNet, Replica, robot mapping logs; metrics: failure AUROC, depth error correlation, map correction gain, runtime.
- **Refs**: DINOv2: Learning Robust Visual Features without Supervision; Segment Anything; SAM 2: Segment Anything in Images and Videos; Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection; VGGT: Visual Geometry Grounded Transformer.

### Idea 3. Promptable 3D interaction from 2D foundation prompts
- **Limit**: 2D promptable segmentation은 robot이 실제 3D point, surface, action region으로 쓰기 어렵다.
- **Problem**: point/click/box/text prompt를 3D surface prompt로 lift하고, robot action primitive와 연결한다.
- **Why / Method**: 2D prompt는 view-dependent이다. multi-view prompt fusion과 3D uncertainty-aware prompt propagation이 필요하다.
- **Eval**: ScanNet, LERF, RLBench, real tabletop; metrics: 3D prompt IoU, required clicks, action success, cross-view consistency.
- **Refs**: Segment Anything; SAM 2: Segment Anything in Images and Videos; Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection; Segment Any 3D Object with Language; RoboGround: Robotic Manipulation with Grounded Vision-Language Priors.

## Foundations: Vision-Language Models

### Idea 1. Spatially calibrated CLIP/VLM features for 3D maps
- **Limit**: CLIP-style feature는 semantic alignment는 강하지만 3D scale, viewpoint, occlusion에 대한 calibration이 약하다.
- **Problem**: 2D VLM feature를 3D map에 lift할 때 feature confidence와 spatial support를 함께 추정한다.
- **Why / Method**: high CLIP similarity가 object localization correctness를 의미하지 않는다. multi-view feature agreement와 geometric support weighting이 필요하다.
- **Eval**: ScanNet200, LERF, Replica, Matterport3D; metrics: open-vocabulary mIoU/AP, feature ECE, query localization error, prompt sensitivity.
- **Refs**: Learning Transferable Visual Models From Natural Language Supervision; ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision; OpenScene: 3D Scene Understanding with Open Vocabularies; ConceptFusion: Open-set Multimodal 3D Mapping; LangSplat: 3D Language Gaussian Splatting.

### Idea 2. VLM debiasing for long-tail 3D classes
- **Limit**: VLM features overfit common internet categories and indoor/outdoor 3D long-tail classes에서 bias가 크다.
- **Problem**: 3D geometry와 scene context로 VLM class bias를 보정한다.
- **Why / Method**: text-image prior는 rare objects를 common category로 끌어당긴다. shape, support relation, scene prior, negative prompts를 결합해야 한다.
- **Eval**: ScanNet200, Matterport3D, nuScenes long-tail, open-vocabulary splits; metrics: long-tail AP/mIoU, confusion reduction, novel class discovery.
- **Refs**: BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation; BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models; Open-Vocabulary Octree-Graph for 3D Scene Understanding; OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection; Details Matter for Indoor Open-vocabulary 3D Instance Segmentation.

### Idea 3. Explicit geometric refusal for VLM spatial answers
- **Limit**: VLM은 spatial question에 대해 evidence가 부족해도 답을 생성한다.
- **Problem**: view/geometry evidence가 부족할 때 answer 대신 "need more view" 또는 clarification을 출력하게 한다.
- **Why / Method**: language prior가 confidence를 과대평가한다. visibility coverage, triangulation confidence, relation ambiguity를 refusal signal로 넣어야 한다.
- **Eval**: SQA3D, ScanQA, RoboSpatial, RealVLG-R1; metrics: QA accuracy, selective risk, refusal precision/recall, active view success.
- **Refs**: Flamingo: a Visual Language Model for Few-Shot Learning; Visual Instruction Tuning; PaLM-E: An Embodied Multimodal Language Model; RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics; G2VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning.

## Foundations: Vision-Language-Action and Robotics

### Idea 1. 3D value-map interface between LLM planning and robot control
- **Limit**: LLM planner는 symbolic subgoal을 만들지만 continuous 3D robot control과의 interface가 약하다.
- **Problem**: language instruction을 object-centric 3D value maps와 action constraints로 변환한다.
- **Why / Method**: direct action token prediction은 failure 원인 분석이 어렵고, symbolic plan은 geometry를 모른다. interpretable 3D value map interface가 필요하다.
- **Eval**: RLBench, CALVIN, LIBERO, real tabletop; metrics: success, constraint satisfaction, intervention count, interpretability.
- **Refs**: CLIPort: What and Where Pathways for Robotic Manipulation; Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation; RVT: Robotic View Transformer for 3D Object Manipulation; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation.

### Idea 2. Robot data curation by 3D novelty and failure uncertainty
- **Limit**: large robot datasets는 scale이 커졌지만, 어떤 3D situations가 모델을 개선하는지 선별 기준이 약하다.
- **Problem**: 3D novelty, uncertainty, failure cause를 기준으로 demonstration/data를 선택한다.
- **Why / Method**: random data scaling은 redundant views/actions를 많이 포함한다. geometry coverage와 failure diversity 기반 curation이 필요하다.
- **Eval**: Open X-Embodiment, BridgeData, LIBERO, RoboTwin 2.0; metrics: success per data hour, coverage, generalization, annotation cost.
- **Refs**: RT-1: Robotics Transformer for Real-World Control at Scale; Open X-Embodiment: Robotic Learning Datasets and RT-X Models; Octo: An Open-Source Generalist Robot Policy; RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation; RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation.

### Idea 3. Standard 3D state-action interface for generalist robot policies
- **Limit**: VLA models마다 3D input, action token, memory format이 달라 비교와 transfer가 어렵다.
- **Problem**: object-centric 3D tokens, affordance maps, action constraints를 포함하는 common interface를 정의한다.
- **Why / Method**: end-to-end VLA는 embodiment-specific geometry를 숨긴다. shared 3D intermediate representation이 필요하다.
- **Eval**: Open X-Embodiment, RLBench, CALVIN, LIBERO; metrics: cross-embodiment success, adaptation steps, token efficiency, implementation cost.
- **Refs**: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control; VIMA: General Robot Manipulation with Multimodal Prompts; OpenVLA: An Open-Source Vision-Language-Action Model; Octo: An Open-Source Generalist Robot Policy; 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation.

## Language-Embedded NeRF and Gaussian Fields

### Idea 1. Online language Gaussian map with memory budget guarantees
- **Limit**: language-embedded Gaussian fields는 query 성능이 좋지만 memory와 update latency가 robot deployment에서 병목이다.
- **Problem**: fixed memory budget 안에서 open-vocabulary query performance를 유지하는 online semantic 3DGS를 만든다.
- **Why / Method**: 모든 Gaussian에 dense language feature를 저장하면 비싸고 noisy하다. object/region prototype, uncertainty-driven feature retention, query-aware compression이 필요하다.
- **Eval**: ScanNet, Replica, LERF, real robot sequences; metrics: open-vocabulary AP/mIoU, memory, update latency, query latency, degradation under long sequence.
- **Refs**: EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding; LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds; CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting; SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining; LangSplat: 3D Language Gaussian Splatting.

### Idea 2. Direct referring and reasoning over Gaussian fields
- **Limit**: language fields는 "what/where" query는 가능하지만 compositional referring과 reasoning query는 약하다.
- **Problem**: 3D Gaussian field에서 relation, hierarchy, reasoning chain을 직접 수행한다.
- **Why / Method**: feature similarity만으로 "left of", "inside", "reachable from"을 처리하기 어렵다. hierarchical feature splatting과 geometric relation executor가 필요하다.
- **Eval**: LERF, ScanNet, ReferIt3D, RealVLG-R1; metrics: query AP, relation grounding accuracy, reasoning accuracy, runtime.
- **Refs**: ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning; Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration; CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting; SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining; SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding.

### Idea 3. Geometry-semantic disentanglement for robust language fields
- **Limit**: language Gaussian feature가 appearance texture에 끌려 geometry boundary와 object identity가 흔들린다.
- **Problem**: semantic feature field를 geometry/radiance parameter와 분리하고, cross-view identity consistency를 보장한다.
- **Why / Method**: joint optimization은 feature leakage를 만든다. extrinsic semantic field, object anchors, feature contrastive loss가 필요하다.
- **Eval**: ScanNet, Replica, LERF, open-vocabulary 3D segmentation; metrics: mIoU/AP, boundary F-score, feature consistency, rendering quality tradeoff.
- **Refs**: ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting; CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting; CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting; Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation; Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration.

## Navigation and Embodied AI

### Idea 1. 3D scene-graph and Gaussian map navigation with active uncertainty
- **Limit**: VLN/ObjectNav는 semantic prior를 쓰지만 occlusion, dynamic object, map uncertainty를 active하게 줄이는 구조가 약하다.
- **Problem**: 3D scene graph, Gaussian/occupancy map, belief map을 결합해 next-best-action을 선택한다.
- **Why / Method**: VLM prior만으로 frontier를 고르면 likely location을 과신한다. uncertainty reduction과 geometric feasibility를 reward에 넣어야 한다.
- **Eval**: R2R, RxR, VLN-CE, Habitat ObjectNav, HM3D; metrics: SR, SPL, nDTW, goal localization error, explored area, collision.
- **Refs**: MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation; Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps; BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation; VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation; Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation.

### Idea 2. Geometry-aware VLN with dynamic 3D tokens
- **Limit**: VLN agents는 instruction-language alignment는 좋아졌지만 path planning에 필요한 metric geometry와 free space representation이 부족하다.
- **Problem**: BEV/voxel/Gaussian 3D tokens를 instruction following policy의 persistent state로 사용한다.
- **Why / Method**: 2D view history는 long-horizon route와 unseen obstacle을 표현하기 어렵다. geometry-aware BEV and dynamic 3D token memory가 필요하다.
- **Eval**: R2R, RxR, VLN-CE, Habitat, Matterport3D; metrics: SR, SPL, nDTW, collision rate, path efficiency.
- **Refs**: GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation; Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation; D3D-VLP: Dynamic 3D Vision-Language-Planning Model for Embodied Grounding and Navigation; VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation; Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments.

### Idea 3. Dynamic carrier-relation search for ObjectNav
- **Limit**: ObjectNav는 static object location prior에 기대지만 실제 환경에서는 object가 drawer, tray, human, robot에 의해 이동한다.
- **Problem**: support/container/carrier relation을 추론해 target object belief를 업데이트한다.
- **Why / Method**: static semantic map은 relocated object search에 실패한다. dynamic scene graph와 carrier-relation transition model이 필요하다.
- **Eval**: AI2-THOR rearrangement, Habitat dynamic ObjectNav, real home robot logs; metrics: SR, SPL, search time, relation prediction F1, belief calibration.
- **Refs**: OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation; Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning.

## Open-Vocabulary 3D Mapping

### Idea 1. Open-vocabulary occupancy map with online language updates
- **Limit**: open-vocabulary mapping은 object surface query에는 강해졌지만 occupancy/free-space와 language semantics가 통합된 경우는 적다.
- **Problem**: occupancy, instance, language feature, confidence를 하나의 map에서 online update한다.
- **Why / Method**: robot planning은 free-space와 semantic target을 동시에 필요로 한다. Gaussian/voxel occupancy와 VLM feature prototype을 동기화해야 한다.
- **Eval**: ScanNet, Replica, Matterport3D, robot navigation logs; metrics: occupancy IoU, open-vocabulary AP, memory, update latency, navigation success.
- **Refs**: AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting; LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering; FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models; ConceptFusion: Open-set Multimodal 3D Mapping; EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding.

### Idea 2. Interaction-driven vocabulary expansion in 3D maps
- **Limit**: open-vocabulary map은 fixed prompts와 pretrained VLM vocabulary에 의존한다.
- **Problem**: user correction, robot interaction, local object clusters로 map vocabulary를 지속적으로 확장한다.
- **Why / Method**: 실제 환경의 object names, aliases, functional labels는 pretrained text prompt에 없을 수 있다. prototype update와 forgetting control이 필요하다.
- **Eval**: Replica/ScanNet map queries, real robot deployment; metrics: new-label learning speed, query accuracy, forgetting, correction count.
- **Refs**: ConceptFusion: Open-set Multimodal 3D Mapping; FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models; Search3D: Hierarchical Open-Vocabulary 3D Segmentation; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs; SAM 2: Segment Anything in Images and Videos.

### Idea 3. Cross-sensor open-vocabulary mapping
- **Limit**: open-vocabulary 3D mapping은 RGB-D/camera 중심이고 LiDAR/radar/thermal 같은 robust sensor의 semantic 활용이 부족하다.
- **Problem**: RGB language features를 3D anchors로 LiDAR/radar/thermal geometry에 distill한다.
- **Why / Method**: non-RGB sensors에는 language supervision이 없지만 geometry와 adverse-condition robustness가 있다. shared 3D anchors와 pseudo-label confidence가 필요하다.
- **Eval**: SemanticKITTI, nuScenes, thermal RGB-D datasets, outdoor robot maps; metrics: open-vocabulary AP/mIoU, robustness under night/weather, map completeness.
- **Refs**: Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection; ThermalGaussian: Thermal 3D Gaussian Splatting; LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments; LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping; OpenScene: 3D Scene Understanding with Open Vocabularies.

## Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception

### Idea 1. Uncertainty-aware multimodal semantic occupancy for planning
- **Limit**: 최신 occupancy model은 camera/LiDAR feature fusion과 Gaussian occupancy를 사용하지만 planning risk로 직접 연결되는 uncertainty가 약하다.
- **Problem**: semantic occupancy, modality confidence, future occupancy risk를 함께 예측한다.
- **Why / Method**: pedestrian, curb, wall의 occupancy error는 planning risk가 다르다. semantic risk calibration과 modality disagreement modeling이 필요하다.
- **Eval**: nuScenes occupancy, Waymo occupancy, Occ3D, nuPlan; metrics: occupancy IoU, semantic mIoU, risk-weighted collision, ECE, planning score.
- **Refs**: RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction; GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting; ODG: Occupancy Prediction Using Dual Gaussians; QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction; GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction.

### Idea 2. Generative LiDAR/radar completion under sensor dropout
- **Limit**: LiDAR scene completion과 radar fusion은 rare weather/dropout/failure mode에 대한 robust completion이 부족하다.
- **Problem**: LiDAR, 4D radar, camera를 결합해 missing geometry와 object hypotheses를 diffusion으로 완성한다.
- **Why / Method**: sensor dropout은 deterministic fusion을 collapse시킨다. modality-aware diffusion prior와 uncertainty-aware posterior sampling이 필요하다.
- **Eval**: nuScenes, Waymo, SemanticKITTI, V2X datasets; metrics: 3D mAP/NDS, completion IoU, scene flow, dropout robustness, calibration ECE.
- **Refs**: V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection; Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding; Scaling Diffusion Models to Real-World 3D LiDAR Scene Completion; Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion; Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation.

### Idea 3. Asynchronous fusion with learned temporal alignment
- **Limit**: real autonomous/robot systems는 sensor timestamp, rolling shutter, network latency가 불일치하지만 benchmark model은 synchronization을 가정한다.
- **Problem**: camera/LiDAR/radar/IMU의 time offset과 motion compensation uncertainty를 학습한다.
- **Why / Method**: naive fusion은 ghost object와 duplicated occupancy를 만든다. temporal flow alignment와 per-modality time-offset estimation이 필요하다.
- **Eval**: nuScenes, Waymo, Argoverse, custom asynchronous logs; metrics: mAP/NDS, occupancy IoU, scene flow EPE, latency robustness.
- **Refs**: BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation; FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry; Rethinking Temporal Fusion with a Unified Gradient Descent View for 3D Semantic Occupancy Prediction; V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection; RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction.

## Sensor Fusion, LiDAR, and Autonomous Driving

### Idea 1. Differentiable multi-sensor simulation with Gaussian splats
- **Limit**: autonomous driving simulation은 camera rendering, LiDAR simulation, radar artifacts를 따로 다루는 경우가 많다.
- **Problem**: 3D Gaussian scene representation에서 camera, LiDAR, radar observation을 jointly render한다.
- **Why / Method**: modality-specific simulators는 cross-sensor consistency를 보장하지 않는다. material-aware Gaussian primitives와 learned sensor noise model이 필요하다.
- **Eval**: nuScenes, Waymo, PandaSet; metrics: rendering metrics, LiDAR Chamfer, radar detection statistics, downstream mAP transfer gap.
- **Refs**: SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving; RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes; TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving; GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting; WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving.

### Idea 2. Online calibration monitoring for LiDAR-camera-radar fusion
- **Limit**: calibration drift는 fusion perception을 크게 망가뜨리지만 online detection/correction은 아직 제한적이다.
- **Problem**: scene geometry와 cross-modal residual로 extrinsic drift를 감지하고 보정한다.
- **Why / Method**: offline calibration은 vibration, temperature, sensor replacement에 취약하다. differentiable Gaussian map과 multi-modal alignment residual이 필요하다.
- **Eval**: KITTI, nuScenes, Waymo, custom perturbation; metrics: calibration error, drift detection delay, mAP/NDS recovery, false alarm rate.
- **Refs**: TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving; GeoCalib: Learning Single-image Calibration with Geometric Optimization; Robust LiDAR-Camera Calibration with 2D Gaussian Splatting; BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation; FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry.

### Idea 3. Closed-loop 3D driving world model with uncertainty-aware rendering
- **Limit**: driving world model은 plausible future video를 만들지만 closed-loop planning risk와 metric occupancy를 충분히 반영하지 않는다.
- **Problem**: future 3D state, rendered sensor observation, occupancy uncertainty를 함께 예측한다.
- **Why / Method**: video-only future는 collision risk를 숨긴다. 4D Gaussian/occupancy latent와 planner feedback이 필요하다.
- **Eval**: nuScenes, Waymo, nuPlan; metrics: future occupancy IoU, ADE/FDE, collision rate, planning score, sensor rendering quality.
- **Refs**: Planning-oriented Autonomous Driving; WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving; Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling; ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation; Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving.

## Vision-Language-Action and Robot Manipulation

### Idea 1. 3D execution monitor for self-correcting VLA
- **Limit**: 최신 VLA는 3D state injection을 시작했지만, 실행 중 실패를 감지하고 재계획하는 구조는 약하다.
- **Problem**: predicted action의 expected 3D state와 observed 3D state를 비교해 failure, cause, recovery action을 출력한다.
- **Why / Method**: image-level feedback은 small pose/contact error를 놓친다. object pose, contact, affordance, scene graph 변화의 residual을 monitor로 사용해야 한다.
- **Eval**: RLBench, LIBERO, CALVIN, VLABench, real robot failure recovery; metrics: success, recovery success, failure AUROC, intervention count, safety violation.
- **Refs**: PointVLA: Injecting the 3D World into Vision-Language-Action Models; ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation; 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation; AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation.

### Idea 2. Active 3D perception and spatial memory for out-of-view manipulation
- **Limit**: VLA는 현재 view 밖 object와 previous subgoal state를 잊기 쉽다.
- **Problem**: active view selection과 persistent 3D spatial memory를 결합한 VLA policy를 만든다.
- **Why / Method**: hidden object나 occluded target은 single-frame image tokens로 해결되지 않는다. memory slot, uncertainty-driven camera motion, task-state graph가 필요하다.
- **Eval**: LIBERO-long, VLABench, RLBench with occlusion, real tabletop/mobile manipulation; metrics: long-horizon success, memory query accuracy, view count, recovery rate.
- **Refs**: ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation; Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action; Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds; GWM: Towards Scalable Gaussian World Models for Robotic Manipulation; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning.

### Idea 3. Open-world VLA with Gaussian world model and safety constraints
- **Limit**: open-world VLA는 generalization을 목표로 하지만, 3D world model과 safety constraint가 policy 내부에서 분리되어 있다.
- **Problem**: Gaussian world model이 predicted outcome과 unsafe geometry를 시뮬레이션하고, VLA action을 constrain한다.
- **Why / Method**: web-scale/VLA prior는 novel object action을 제안할 수 있지만 collision, instability, semantic safety를 보장하지 않는다. action proposal, world model rollout, safety verifier를 묶어야 한다.
- **Eval**: LIBERO-Safety, VLABench, RoboTwin 2.0, real robot open-world tasks; metrics: success, safety violation, rollout prediction error, novel object generalization.
- **Refs**: pi0.5: a Vision-Language-Action Model with Open-World Generalization; GWM: Towards Scalable Gaussian World Models for Robotic Manipulation; PointVLA: Injecting the 3D World into Vision-Language-Action Models; Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds; LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models.
