# Reading Priority

- Updated: 2026-06-29 KST
- Source registry: [PAPER.md](./PAPER.md)
- Purpose: category-level reading roadmap and foundation-gap checklist.

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

`Local` means the paper exists in the local registry with a paper folder, notes, and PDF when available. Priority ordering reflects both foundation value and current trend-flow relevance.

## 3D Equivariance, Calibration, and Registration

**우선 읽기**

- Local: [GaussReg: Fast 3D Registration with Gaussian Splatting](./2024/ECCV/2024_ECCV_GaussReg-Fast-3D-Registration-with-Gaussian-Splatting/01_overview.md)
- Local: [GeoCalib: Learning Single-image Calibration with Geometric Optimization](./2024/ECCV/2024_ECCV_GeoCalib-Learning-Single-image-Calibration-with-Geometric/01_overview.md)
- Local: [VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency](./2026/ICML/2026_ICML_VGGT-Motion-Motion-Aware-Calibration-Free-Monocular-SLAM-f/01_overview.md)
- Local: [Fully Convolutional Geometric Features](./2019/ICCV/2019_ICCV_Fully-Convolutional-Geometric-Features/01_overview.md)
- Local: [Deep Closest Point: Learning Representations for Point Cloud Registration](./2019/ICCV/2019_ICCV_Deep-Closest-Point-Learning-Representations-for-Point-Clou/01_overview.md)

**선정 이유:** registration, calibration, equivariance는 3D CV의 metric reliability를 결정하는 기반이다. FCGF/DCP는 learned correspondence foundation이고, GaussReg/GeoCalib/VGGT-Motion은 3DGS와 feed-forward geometry로 이어지는 최신 flow를 대표한다. 로봇에서는 sensor pose, map alignment, language map alignment가 모두 registration 문제로 귀결되므로 robotics 확장성이 높다.

## 3D Generative Modeling and Diffusion

**우선 읽기**

- Local: [ReconFusion: 3D Reconstruction with Diffusion Priors](./2024/CVPR/2024_CVPR_ReconFusion-3D-Reconstruction-with-Diffusion-Priors/01_overview.md)
- Local: [PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models](./2025/CVPR/2025_CVPR_PartGen-Part-level-3D-Generation-and-Reconstruction-with-M/01_overview.md)
- Local: [HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction](./2026/CVPR/2026_CVPR_HAD-Hallucination-Aware-Diffusion-Priors-for-3D-Reconstruc/01_overview.md)
- Local: [Score-Based Generative Modeling through Stochastic Differential Equations](./2021/ICLR/2021_ICLR_Score-Based-Generative-Modeling-through-Stochastic-Differe/01_overview.md)
- Local: [DreamFusion: Text-to-3D using 2D Diffusion](./2023/ICLR/2023_ICLR_DreamFusion-Text-to-3D-using-2D-Diffusion/01_overview.md)

**선정 이유:** 3D generation은 현재 3D reconstruction, shape completion, world model로 확장되고 있다. 연구 공백은 diffusion prior가 geometry-consistency와 observability를 보장하지 못한다는 점이다. 평가도 DTU, CO3D, ScanNet, ShapeNet, Objaverse 계열로 가능하므로 proposal화가 쉽다.

## 3D Large Multimodal Models

**우선 읽기**

- Local: [3D-LLM: Injecting the 3D World into Large Language Models](./2023/NeurIPS/2023_NeurIPS_3D-LLM-Injecting-the-3D-World-into-Large-Language-Models/01_overview.md)
- Local: [SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities](./2024/CVPR/2024_CVPR_SpatialVLM-Endowing-Vision-Language-Models-with-Spatial-Re/01_overview.md)
- Local: [SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models](./2025/CVPR/2025_CVPR_SpatialLLM-A-Compound-3D-Informed-Design-towards-Spatially/01_overview.md)
- Local: [GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models](./2026/ICLR/2026_ICLR_GPT4Scene-Understand-3D-Scenes-from-Videos-with-Vision-Lan/01_overview.md)
- Local: [Flamingo: a Visual Language Model for Few-Shot Learning](./2022/NeurIPS/2022_NeurIPS_Flamingo-a-Visual-Language-Model-for-Few-Shot-Learning/01_overview.md)
- Local: [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](./2023/ICML/2023_ICML_BLIP-2-Bootstrapping-Language-Image-Pre-training-with-Froz/01_overview.md)

**선정 이유:** 3D LMM은 3D scene understanding과 robot reasoning의 연결부다. Flamingo/BLIP-2는 2D LMM alignment foundation이고, 3D-LLM에서 SpatialVLM/SpatialLLM/GPT4Scene으로 이어지는 흐름은 최신 3D spatial reasoning flow를 보여준다. robotics 확장성은 embodied QA, planning, manipulation instruction으로 이어진다.

## 3D Reconstruction, Geometry, and SLAM

**우선 읽기**

- Local: [DUSt3R: Geometric 3D Vision Made Easy](./2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/01_overview.md)
- Local: [VGGT: Visual Geometry Grounded Transformer](./2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md)
- Local: [FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent](./2025/3DV/2025_3DV_FlowMap-High-Quality-Camera-Poses-Intrinsics-and-Depth-via/01_overview.md)
- Local: [Structure-from-Motion Revisited](./2016/CVPR/2016_CVPR_Structure-from-Motion-Revisited/01_overview.md)
- Local: [KinectFusion: Real-Time Dense Surface Mapping and Tracking](./2011/ISMAR/2011_ISMAR_KinectFusion-Real-Time-Dense-Surface-Mapping-and-Tracking/01_overview.md)
- Local: [BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Reintegration](./2017/TOG/2017_TOG_BundleFusion-Real-time-Globally-Consistent-3D-Reconstructi/01_overview.md)

**선정 이유:** feed-forward geometry가 빠르게 발전했지만, camera pose, bundle adjustment, TSDF fusion, dense SLAM의 원리를 모르면 최신 reconstruction model의 한계를 분석하기 어렵다. 데이터와 metric이 명확하고 robotics mapping으로 바로 확장된다.

## 3D Representation Learning and Foundation Models

**우선 읽기**

- Local: [UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting](./2025/CVPR/2025_CVPR_UniPre3D-Unified-Pre-training-of-3D-Point-Cloud-Models-wit/01_overview.md)
- Local: [Dens3R: A Foundation Model for 3D Geometry Prediction](./2026/ICLR/2026_ICLR_Dens3R-A-Foundation-Model-for-3D-Geometry-Prediction/01_overview.md)
- Local: [Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](./2025/NeurIPS/2025_NeurIPS_Object-X-Learning-to-Reconstruct-Multi-Modal-3D-Object-Rep/01_overview.md)
- Local: [PointContrast: Unsupervised Pre-training for 3D Point Cloud Understanding](./2020/ECCV/2020_ECCV_PointContrast-Unsupervised-Pre-training-for-3D-Point-Cloud/01_overview.md)
- Local: [ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding](./2023/CVPR/2023_CVPR_ULIP-Learning-a-Unified-Representation-of-Language-Images/01_overview.md)

**선정 이유:** 3D foundation model 연구는 representation transfer gap이 핵심 공백이다. points, voxels, meshes, Gaussians, images 사이의 representation alignment가 중요하며, downstream detection/segmentation/reconstruction으로 평가 가능하다.

## 3D Scene Graphs and Graph Reasoning

**우선 읽기**

- Local: [Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships](./2024/CVPR/2024_CVPR_Open3DSG-Open-Vocabulary-3D-Scene-Graphs-from-Point-Clouds/01_overview.md)
- Local: [MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning](./2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md)
- Local: [Clio: Real-time Task-Driven Open-Set 3D Scene Graphs](./2024/RA-L/2024_RA-L_Clio-Real-time-Task-Driven-Open-Set-3D-Scene-Graphs/01_overview.md)
- Local: [3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera](./2019/ICCV/2019_ICCV_3D-Scene-Graph-A-Structure-for-Unified-Semantics-3D-Space/01_overview.md)

**선정 이유:** 3D scene graph는 geometry, semantics, relations, robot memory를 압축하는 구조다. 2019년 formulation을 출발점으로 Open3DSG/Clio/MomaGraph까지 이어지는 flow가 명확하며, graph reasoning은 navigation, manipulation planning, change detection으로 확장성이 높다.

## 3D Scene Representations and Neural Fields

**우선 읽기**

- Local: [3D Gaussian Splatting for Real-Time Radiance Field Rendering](./2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md)
- Local: [SplatFormer: Point Transformer for Robust 3D Gaussian Splatting](./2025/ICLR/2025_ICLR_SplatFormer-Point-Transformer-for-Robust-3D-Gaussian-Splat/01_overview.md)
- Local: [ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting](./2026/CVPR/2026_CVPR_ExtrinSplat-Decoupling-Geometry-and-Semantics-for-Open-Voc/01_overview.md)
- Local: [Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields](./2021/ICCV/2021_ICCV_Mip-NeRF-A-Multiscale-Representation-for-Anti-Aliasing-Neu/01_overview.md)
- Local: [Instant Neural Graphics Primitives with a Multiresolution Hash Encoding](./2022/SIGGRAPH/2022_SIGGRAPH_Instant-Neural-Graphics-Primitives-with-a-Multiresolution/01_overview.md)

**선정 이유:** neural field와 Gaussian scene representation은 rendering을 넘어 mapping, semantic query, planning map으로 확장된다. 연구 공백은 photorealism과 task-usable geometry/semantics가 불일치한다는 점이다.

## 3D Semantic Understanding and Alignment

**우선 읽기**

- Local: [OpenScene: 3D Scene Understanding with Open Vocabularies](./2023/CVPR/2023_CVPR_OpenScene-3D-Scene-Understanding-with-Open-Vocabularies/01_overview.md)
- Local: [OpenMask3D: Open-Vocabulary 3D Instance Segmentation](./2023/NeurIPS/2023_NeurIPS_OpenMask3D-Open-Vocabulary-3D-Instance-Segmentation/01_overview.md)
- Local: [GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation](./2026/ICLR/2026_ICLR_GeoPurify-A-Data-Efficient-Geometric-Distillation-Framewor/01_overview.md)
- Local: [ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes](./2017/CVPR/2017_CVPR_ScanNet-Richly-annotated-3D-Reconstructions-of-Indoor-Scen/01_overview.md)
- Local: [SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences](./2019/ICCV/2019_ICCV_SemanticKITTI-A-Dataset-for-Semantic-Scene-Understanding-o/01_overview.md)

**선정 이유:** open-vocabulary 3D semantic understanding은 VLM을 3D로 올릴 때 발생하는 view inconsistency와 boundary leakage가 핵심 공백이다. mIoU, hIoU, open-vocabulary AP 등 평가가 명확하고 robot semantic mapping으로 이어진다.

## 3D Vision-Language Grounding

**우선 읽기**

- Local: [ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language](./2020/ECCV/2020_ECCV_ScanRefer-3D-Object-Localization-in-RGB-D-Scans-using-Natu/01_overview.md)
- Local: [ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes](./2020/ECCV/2020_ECCV_ReferIt3D-Neural-Listeners-for-Fine-Grained-3D-Object-Iden/01_overview.md)
- Local: [3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds](./2021/ICCV/2021_ICCV_3DVG-Transformer-Relation-Modeling-for-Visual-Grounding-on/01_overview.md)
- Local: [ScanQA: 3D Question Answering for Spatial Scene Understanding](./2022/CVPR/2022_CVPR_ScanQA-3D-Question-Answering-for-Spatial-Scene-Understandi/01_overview.md)

**선정 이유:** 3D grounding은 language-to-object, relation, spatial ambiguity를 직접 다룬다. 데이터 접근성이 좋고, robotics에서는 object search, manipulation target selection, clarification dialog로 확장된다.

## Benchmarks and Datasets

**우선 읽기**

- Local: [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](./2025/CVPR/2025_CVPR_RoboSpatial-Teaching-Spatial-Understanding-to-2D-and-3D-Vi/01_overview.md)
- Local: [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](./2025/ICCV/2025_ICCV_VLABench-A-Large-Scale-Benchmark-for-Language-Conditioned/01_overview.md)
- Local: [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](./2025/ICML/2025_ICML_EmbodiedBench-Comprehensive-Benchmarking-Multi-modal-Large/01_overview.md)
- Local: [Matterport3D: Learning from RGB-D Data in Indoor Environments](./2017/3DV/2017_3DV_Matterport3D-Learning-from-RGB-D-Data-in-Indoor-Environmen/01_overview.md)
- Local: [Habitat: A Platform for Embodied AI Research](./2019/ICCV/2019_ICCV_Habitat-A-Platform-for-Embodied-AI-Research/01_overview.md)

**선정 이유:** benchmark 논문은 연구 문제의 정의와 metric을 고정한다. Matterport3D/Habitat 같은 embodied foundation과 RoboSpatial/VLABench/EmbodiedBench 같은 최신 benchmark flow를 함께 읽으면, 3D spatial reasoning과 robotics evaluation을 같은 축에서 설계할 수 있다.

## Equivariance, Diffusion, and 3D Action

**우선 읽기**

- Local: [Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation](./2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md)
- Local: [EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation](./2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md)
- Local: [Transporter Networks: Rearranging the Visual World for Robotic Manipulation](./2020/CoRL/2020_CoRL_Transporter-Networks-Rearranging-the-Visual-World-for-Robo/01_overview.md)
- Local: [CLIPort: What and Where Pathways for Robotic Manipulation](./2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md)
- Local: [Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation](./2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md)

**선정 이유:** action geometry는 로봇 정책이 pose, contact, object frame을 어떻게 일반화하는지 결정한다. equivariance는 sample efficiency와 pose generalization을 직접 개선할 수 있어 contribution 가능성이 높다.

## Foundations: 3D Detection and BEV Perception

**우선 읽기**

- Local: [BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers](./2022/ECCV/2022_ECCV_BEVFormer-Learning-Bird-s-Eye-View-Representation-from-Mul/01_overview.md)
- Local: [BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation](./2023/ICRA/2023_ICRA_BEVFusion-Multi-Task-Multi-Sensor-Fusion-with-Unified-Bird/01_overview.md)
- Local: [VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection](./2018/CVPR/2018_CVPR_VoxelNet-End-to-End-Learning-for-Point-Cloud-Based-3D-Obje/01_overview.md)
- Local: [PointPillars: Fast Encoders for Object Detection from Point Clouds](./2019/CVPR/2019_CVPR_PointPillars-Fast-Encoders-for-Object-Detection-from-Point/01_overview.md)
- Local: [Lift, Splat, Shoot: Encoding Images from Arbitrary Camera Rigs by Implicitly Unprojecting to 3D](./2020/ECCV/2020_ECCV_Lift-Splat-Shoot-Encoding-Images-from-Arbitrary-Camera-Rig/01_overview.md)

**선정 이유:** autonomous 3D perception에서 BEV는 sensor fusion과 planning의 공통 좌표계다. 3D CV 중심성이 높고 nuScenes, Waymo, KITTI로 평가가 명확하다.

## Foundations: 3D Geometry and Point Clouds

**우선 읽기**

- Local: [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](./2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md)
- Local: [PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space](./2017/NeurIPS/2017_NeurIPS_PointNet++-Deep-Hierarchical-Feature-Learning-on-Point-Set/01_overview.md)
- Local: [ShapeNet: An Information-Rich 3D Model Repository](./2015/arxiv/2015_arxiv_ShapeNet-An-Information-Rich-3D-Model-Repository/01_overview.md)
- Local: [PointCNN: Convolution On X-Transformed Points](./2018/NeurIPS/2018_NeurIPS_PointCNN-Convolution-On-X-Transformed-Points/01_overview.md)

**선정 이유:** point cloud foundation은 거의 모든 3D recognition, segmentation, registration, manipulation representation의 출발점이다. 구현 난이도가 낮고 benchmark가 많아 빠르게 실험 baseline을 만들 수 있다.

## Foundations: 3D Representation Learning

**우선 읽기**

- Local: [Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling](./2022/CVPR/2022_CVPR_Point-BERT-Pre-training-3D-Point-Cloud-Transformers-with-M/01_overview.md)
- Local: [Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning](./2022/ECCV/2022_ECCV_Point-MAE-Masked-Autoencoders-for-Point-Cloud-Self-supervi/01_overview.md)
- Local: [PointContrast: Unsupervised Pre-training for 3D Point Cloud Understanding](./2020/ECCV/2020_ECCV_PointContrast-Unsupervised-Pre-training-for-3D-Point-Cloud/01_overview.md)
- Local: [Self-Supervised Pretraining of 3D Features on any Point-Cloud](./2021/ICCV/2021_ICCV_Self-Supervised-Pretraining-of-3D-Features-on-any-Point-Cl/01_overview.md)

**선정 이유:** 3D representation learning은 label scarcity와 domain shift 문제를 직접 다룬다. downstream transfer로 평가 가능하고, robotics에서는 sensor/viewpoint 변화에 대한 robustness와 연결된다.

## Foundations: 3D Scene Representations

**우선 읽기**

- Local: [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](./2020/ECCV/2020_ECCV_NeRF-Representing-Scenes-as-Neural-Radiance-Fields-for-Vie/01_overview.md)
- Local: [3D Gaussian Splatting for Real-Time Radiance Field Rendering](./2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/01_overview.md)
- Local: [Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields](./2022/CVPR/2022_CVPR_Mip-NeRF-360-Unbounded-Anti-Aliased-Neural-Radiance-Fields/01_overview.md)
- Local: [NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction](./2021/NeurIPS/2021_NeurIPS_NeuS-Learning-Neural-Implicit-Surfaces-by-Volume-Rendering/01_overview.md)

**선정 이유:** scene representation은 rendering보다 넓게 mapping, localization, semantic query, planning의 기반이 된다. NeRF/3DGS만으로는 surface, uncertainty, semantics의 차이를 설명하기 어려우므로 implicit surface foundation도 필요하다.

## Foundations: 3D Semantic Occupancy

**우선 읽기**

- Local: [VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion](./2023/CVPR/2023_CVPR_VoxFormer-Sparse-Voxel-Transformer-for-Camera-based-3D-Sem/01_overview.md)
- Local: [SSCNet: Semantic Scene Completion from a Single Depth Image](./2017/CVPR/2017_CVPR_SSCNet-Semantic-Scene-Completion-from-a-Single-Depth-Image/01_overview.md)
- Local: [MonoScene: Monocular 3D Semantic Scene Completion](./2022/CVPR/2022_CVPR_MonoScene-Monocular-3D-Semantic-Scene-Completion/01_overview.md)
- Local: [OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction](./2023/ICCV/2023_ICCV_OccFormer-Dual-path-Transformer-for-Vision-based-3D-Semant/01_overview.md)

**선정 이유:** occupancy는 robot navigation/planning에서 가장 직접적으로 쓰이는 3D representation이다. semantic occupancy는 collision risk, traversability, open-vocabulary map으로 확장된다.

## Foundations: Diffusion and Generative Models

**우선 읽기**

- Local: [Denoising Diffusion Probabilistic Models](./2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md)
- Local: [High-Resolution Image Synthesis with Latent Diffusion Models](./2022/CVPR/2022_CVPR_High-Resolution-Image-Synthesis-with-Latent-Diffusion-Mode/01_overview.md)
- Local: [Denoising Diffusion Implicit Models](./2021/ICLR/2021_ICLR_Denoising-Diffusion-Implicit-Models/01_overview.md)
- Local: [Classifier-Free Diffusion Guidance](./2022/arxiv/2022_arxiv_Classifier-Free-Diffusion-Guidance/01_overview.md)

**선정 이유:** 3D diffusion을 이해하려면 DDPM/LDM 외에 sampling, guidance, score formulation을 알아야 한다. 3D reconstruction에서 hallucination과 sensor consistency를 분석할 때 foundation 역할을 한다.

## Foundations: Equivariance and Geometry

**우선 읽기**

- Local: [SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks](./2020/NeurIPS/2020_NeurIPS_SE3-Transformers-3D-Roto-Translation-Equivariant-Attention/01_overview.md)
- Local: [E(n) Equivariant Graph Neural Networks](./2021/ICML/2021_ICML_En-Equivariant-Graph-Neural-Networks/01_overview.md)
- Local: [Tensor Field Networks: Rotation- and Translation-Equivariant Neural Networks for 3D Point Clouds](./2018/arxiv/2018_arxiv_Tensor-Field-Networks-Rotation-and-Translation-Equivariant/01_overview.md)
- Local: [Group Equivariant Convolutional Networks](./2016/ICML/2016_ICML_Group-Equivariant-Convolutional-Networks/01_overview.md)

**선정 이유:** equivariance는 3D에서 inductive bias를 명시하는 핵심 도구다. 로봇 manipulation, point registration, molecule/mesh geometry로 확장되며, sample efficiency와 pose generalization 측정이 가능하다.

## Foundations: Monocular Geometry

**우선 읽기**

- Local: [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](./2024/CVPR/2024_CVPR_Depth-Anything-Unleashing-the-Power-of-Large-Scale-Unlabel/01_overview.md)
- Local: [Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation](./2024/CVPR/2024_CVPR_Marigold-Repurposing-Diffusion-Based-Image-Generators-for/01_overview.md)
- Local: [Depth Map Prediction from a Single Image using a Multi-Scale Deep Network](./2014/NeurIPS/2014_NeurIPS_Depth-Map-Prediction-from-a-Single-Image-using-a-Multi-Sca/01_overview.md)
- Local: [Digging Into Self-Supervised Monocular Depth Estimation](./2019/ICCV/2019_ICCV_Digging-Into-Self-Supervised-Monocular-Depth-Estimation/01_overview.md)
- Local: [Vision Transformers for Dense Prediction](./2021/ICCV/2021_ICCV_Vision-Transformers-for-Dense-Prediction/01_overview.md)

**선정 이유:** monocular geometry는 camera-only robot perception과 sparse-view reconstruction의 핵심이다. scale ambiguity, domain shift, calibration error가 명확한 연구 공백이다.

## Foundations: RL and Imitation Learning

**우선 읽기**

- Local: [Decision Transformer: Reinforcement Learning via Sequence Modeling](./2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/01_overview.md)
- Local: [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](./2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md)
- Local: [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](./2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md)
- Local: [Generative Adversarial Imitation Learning](./2016/NeurIPS/2016_NeurIPS_Generative-Adversarial-Imitation-Learning/01_overview.md)
- Local: [Proximal Policy Optimization Algorithms](./2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md)

**선정 이유:** robotics/VLA 논문을 읽을 때 offline imitation, RL fine-tuning, trajectory modeling의 차이를 구분해야 한다. 구현 난이도는 다양하지만 evaluation protocol과 failure mode 분석에 중요하다.

## Foundations: SLAM and Sensor Geometry

**우선 읽기**

- Local: [ORB-SLAM: A Versatile and Accurate Monocular SLAM System](./2015/T-RO/2015_T-RO_ORB-SLAM-A-Versatile-and-Accurate-Monocular-SLAM-System/01_overview.md)
- Local: [DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](./2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md)
- Local: [PTAM: Parallel Tracking and Mapping for Small AR Workspaces](./2007/ISMAR/2007_ISMAR_PTAM-Parallel-Tracking-and-Mapping-for-Small-AR-Workspaces/01_overview.md)
- Local: [LSD-SLAM: Large-Scale Direct Monocular SLAM](./2014/ECCV/2014_ECCV_LSD-SLAM-Large-Scale-Direct-Monocular-SLAM/01_overview.md)
- Local: [ElasticFusion: Dense SLAM Without A Pose Graph](./2015/RSS/2015_RSS_ElasticFusion-Dense-SLAM-Without-A-Pose-Graph/01_overview.md)

**선정 이유:** SLAM은 robot 3D memory와 map update의 foundation이다. 최신 neural/GS SLAM의 한계를 이해하려면 feature-based, direct, dense fusion 계열을 같이 읽어야 한다.

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

- Local: [DINOv2: Learning Robust Visual Features without Supervision](./2023/TMLR/2023_TMLR_DINOv2-Learning-Robust-Visual-Features-without-Supervision/01_overview.md)
- Local: [Segment Anything](./2023/ICCV/2023_ICCV_Segment-Anything/01_overview.md)
- Local: [Masked Autoencoders Are Scalable Vision Learners](./2022/CVPR/2022_CVPR_Masked-Autoencoders-Are-Scalable-Vision-Learners/01_overview.md)
- Local: [Emerging Properties in Self-Supervised Vision Transformers](./2021/ICCV/2021_ICCV_Emerging-Properties-in-Self-Supervised-Vision-Transformers/01_overview.md)
- Local: [Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](./2024/ECCV/2024_ECCV_Grounding-DINO-Marrying-DINO-with-Grounded-Pre-Training-fo/01_overview.md)

**선정 이유:** 2D foundation features는 3D open-vocabulary segmentation, mapping, reconstruction quality checking의 teacher로 쓰인다. 3D consistency를 연구하려면 2D feature foundation을 알아야 한다.

## Foundations: Vision-Language Models

**우선 읽기**

- Local: [Learning Transferable Visual Models From Natural Language Supervision](./2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/01_overview.md)
- Local: [ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision](./2021/ICML/2021_ICML_ALIGN-Scaling-Up-Visual-and-Vision-Language-Representation/01_overview.md)
- Local: [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](./2022/ICML/2022_ICML_BLIP-Bootstrapping-Language-Image-Pre-training-for-Unified/01_overview.md)
- Local: [Visual Instruction Tuning](./2023/NeurIPS/2023_NeurIPS_Visual-Instruction-Tuning/01_overview.md)

**선정 이유:** CLIP과 VLM foundation은 open-vocabulary 3D perception의 근간이다. 다만 2D-language alignment만으로는 metric 3D reasoning이 되지 않는다는 gap이 거의 모든 3D-VL 연구의 출발점이다.

## Foundations: Vision-Language-Action and Robotics

**우선 읽기**

- Local: [RT-1: Robotics Transformer for Real-World Control at Scale](./2022/arxiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md)
- Local: [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](./2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md)
- Local: [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](./2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md)
- Local: [CLIPort: What and Where Pathways for Robotic Manipulation](./2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md)
- Local: [BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning](./2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/01_overview.md)

**선정 이유:** VLA foundation은 language-conditioned robotics의 data scaling, action tokenization, embodiment generalization 문제를 정의한다. 3D state가 약한 기존 VLA의 한계가 명확해 3D CV 기반 contribution을 만들기 좋다.

## Language-Embedded NeRF and Gaussian Fields

**우선 읽기**

- Local: [LERF: Language Embedded Radiance Fields](./2023/ICCV/2023_ICCV_LERF-Language-Embedded-Radiance-Fields/01_overview.md)
- Local: [LangSplat: 3D Language Gaussian Splatting](./2024/CVPR/2024_CVPR_LangSplat-3D-Language-Gaussian-Splatting/01_overview.md)
- Local: [CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory](./2023/RSS/2023_RSS_CLIP-Fields-Weakly-Supervised-Semantic-Fields-for-Robotic/01_overview.md)
- Local: [In-Place Scene Labelling and Understanding with Implicit Scene Representation](./2021/ICCV/2021_ICCV_In-Place-Scene-Labelling-and-Understanding-with-Implicit-S/01_overview.md)
- Local: [Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation](./2023/CoRL/2023_CoRL_Distilled-Feature-Fields-Enable-Few-Shot-Language-Guided-M/01_overview.md)

**선정 이유:** language field는 3D map을 queryable memory로 만드는 핵심 흐름이다. robotics에서는 object search, manipulation target selection, task-relevant exploration으로 연결된다.

## Navigation and Embodied AI

**우선 읽기**

- Local: [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](./2018/CVPR/2018_CVPR_Vision-and-Language-Navigation-Interpreting-Visually-Groun/01_overview.md)
- Local: [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](./2024/ICRA/2024_ICRA_VLFM-Vision-Language-Frontier-Maps-for-Zero-Shot-Semantic/01_overview.md)
- Local: [Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments](./2020/ECCV/2020_ECCV_Beyond-the-Nav-Graph-Vision-and-Language-Navigation-in-Con/01_overview.md)
- Local: [Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding](./2020/EMNLP/2020_EMNLP_Room-Across-Room-Multilingual-Vision-and-Language-Navigati/01_overview.md)
- Local: [VLMaps: Visual-Language Maps for Robot Navigation](./2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md)
- Local: [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](./2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md)

**선정 이유:** R2R/VLN이 task를 정의했고, VLN-CE/RxR이 continuous 및 dense grounding setting으로 확장했으며, VLFM/VLMaps/Splat-Nav는 zero-shot semantic navigation과 3D map 기반 navigation의 최신 핵심 flow를 대표한다. 최신 navigation 논문을 해석하려면 이 축이 먼저 필요하다.

## Open-Vocabulary 3D Mapping

**우선 읽기**

- Local: [ConceptFusion: Open-set Multimodal 3D Mapping](./2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md)
- Local: [OpenScene: 3D Scene Understanding with Open Vocabularies](./2023/CVPR/2023_CVPR_OpenScene-3D-Scene-Understanding-with-Open-Vocabularies/01_overview.md)
- Local: [CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory](./2023/RSS/2023_RSS_CLIP-Fields-Weakly-Supervised-Semantic-Fields-for-Robotic/01_overview.md)
- Local: [Language-driven Semantic Segmentation](./2022/ICLR/2022_ICLR_Language-driven-Semantic-Segmentation/01_overview.md)
- Local: [OpenSeg: Scaling Open-Vocabulary Image Segmentation with Image-Level Labels](./2022/ECCV/2022_ECCV_OpenSeg-Scaling-Open-Vocabulary-Image-Segmentation-with-Im/01_overview.md)
- Local: [Detecting Twenty-thousand Classes using Image-level Supervision](./2022/ECCV/2022_ECCV_Detecting-Twenty-thousand-Classes-using-Image-level-Superv/01_overview.md)

**선정 이유:** open-vocabulary 3D mapping은 2D VLM semantics를 metric map에 안정적으로 올리는 문제다. robotics 적용성이 높고, memory/latency/query accuracy까지 평가할 수 있어 contribution 가능성이 높다.

## Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception

**우선 읽기**

- Local: [V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection](./2025/CVPR/2025_CVPR_V2X-R-Cooperative-LiDAR-4D-Radar-Fusion-with-Denoising-Dif/01_overview.md)
- Local: [RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction](./2025/ICCV/2025_ICCV_RIOcc-Efficient-Cross-Modal-Fusion-Transformer-with-Collab/01_overview.md)
- Local: [nuScenes: A Multimodal Dataset for Autonomous Driving](./2020/CVPR/2020_CVPR_nuScenes-A-Multimodal-Dataset-for-Autonomous-Driving/01_overview.md)
- Local: [SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences](./2019/ICCV/2019_ICCV_SemanticKITTI-A-Dataset-for-Semantic-Scene-Understanding-o/01_overview.md)
- Local: [Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving](./2023/NeurIPS/2023_NeurIPS_Occ3D-A-Large-Scale-3D-Occupancy-Prediction-Benchmark-for/01_overview.md)

**선정 이유:** sensor fusion과 occupancy는 robot/autonomous driving에서 가장 평가가 명확한 축이다. 연구 공백은 modality alignment, uncertainty, calibration drift, semantic risk로 명확하다.

## Sensor Fusion, LiDAR, and Autonomous Driving

**우선 읽기**

- Local: [BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers](./2022/ECCV/2022_ECCV_BEVFormer-Learning-Bird-s-Eye-View-Representation-from-Mul/01_overview.md)
- Local: [BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation](./2023/ICRA/2023_ICRA_BEVFusion-Multi-Task-Multi-Sensor-Fusion-with-Unified-Bird/01_overview.md)
- Local: [Planning-oriented Autonomous Driving](./2023/CVPR/2023_CVPR_Planning-oriented-Autonomous-Driving/01_overview.md)
- Local: [Waymo Open Dataset: An Autonomous Driving Dataset](./2020/CVPR/2020_CVPR_Waymo-Open-Dataset-An-Autonomous-Driving-Dataset/01_overview.md)
- Local: [DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries](./2021/CoRL/2021_CoRL_DETR3D-3D-Object-Detection-from-Multi-view-Images-via-3D-t/01_overview.md)

**선정 이유:** BEV와 sensor fusion은 perception-to-planning의 핵심 중간 표현이다. autonomous driving benchmark가 잘 정립되어 있어 evaluation 가능성이 높고, calibration/alignment 공백이 명확하다.

## Vision-Language-Action and Robot Manipulation

**우선 읽기**

- Local: [Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation](./2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md)
- Local: [RVT: Robotic View Transformer for 3D Object Manipulation](./2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md)
- Local: [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](./2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/01_overview.md)
- Local: [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](./2024/CoRL/2024_CoRL_ReKep-Spatio-Temporal-Reasoning-of-Relational-Keypoint-Con/01_overview.md)
- Local: [OpenVLA: An Open-Source Vision-Language-Action Model](./2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md)
- Local: [Octo: An Open-Source Generalist Robot Policy](./2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md)
- Local: [CLIPort: What and Where Pathways for Robotic Manipulation](./2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md)

**선정 이유:** VLA/manipulation은 registry에서 가장 큰 카테고리지만, 3D CV 관점에서는 action이 image token에 갇혀 있는 한계가 크다. 3D state, affordance, contact, object-centric memory를 넣는 방향이 contribution으로 말하기 좋고 RLBench, CALVIN, LIBERO 등으로 평가 가능하다.
