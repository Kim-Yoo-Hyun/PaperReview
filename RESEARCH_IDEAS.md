# Research Ideas from the 3D Vision + Robotics + Vision-Language Survey

This document derives research ideas from the categories in `PAPER.md`.

Each idea follows the same structure:

- **Limit**: the existing limitation that motivates the idea.
- **Problem**: the concrete research problem.
- **Why / Method**: why current approaches fail and why the proposed method form is needed.
- **Eval**: likely datasets, benchmarks, and metrics.
- **Refs**: reference papers from the local survey corpus.

Within each category, Idea 1, Idea 2, and Idea 3 are ranked in priority order. The ranking criteria are: clarity of the research gap, evaluability, implementation difficulty, dataset accessibility, and whether the result can be framed as a clear paper contribution.

## 3D Equivariance, Calibration, and Registration

### Idea 1. Uncertainty-aware equivariant registration for language-queryable 3D maps
- **Limit**: Point-cloud registration and 3DGS registration often optimize geometry only; semantic or language features are treated as noisy side information.
- **Problem**: Register partial scans or Gaussian maps under viewpoint, scale, and semantic ambiguity while preserving open-vocabulary query consistency.
- **Why / Method**: Pure feature matching fails when geometry is repetitive, and pure CLIP/VLM alignment fails because semantic features are not metric. Use SE(3)-equivariant geometric descriptors plus uncertainty-weighted language feature agreement, so unreliable semantic regions cannot dominate pose estimation.
- **Eval**: 3DMatch, 3DLoMatch, ScanNet, Replica, ScanNet++ style map alignment; metrics: registration recall, RTE/RRE, AUC, semantic consistency after alignment, open-vocabulary retrieval accuracy.
- **Refs**: GaussReg: Fast 3D Registration with Gaussian Splatting; GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion; RayI2P: Learning Rays for Image-to-Point Cloud Registration; C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion; Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds.

### Idea 2. Calibration-free monocular SLAM with self-checking geometric priors
- **Limit**: Calibration-free reconstruction models estimate geometry but rarely expose when intrinsics, scale, or motion assumptions are unreliable.
- **Problem**: Build monocular SLAM that jointly predicts camera calibration, depth, pose, and confidence under long sequences and dynamic objects.
- **Why / Method**: Feed-forward geometry models drift over time, while optimization-based SLAM is brittle under wrong intrinsics. Combine VGGT/DUSt3R-style dense geometry priors with a differentiable calibration layer and loop-level consistency tests.
- **Eval**: TUM RGB-D, EuRoC, ScanNet, Replica, KITTI/nuScenes monocular sequences; metrics: ATE, RPE, depth AbsRel, pose AUC, calibration error, loop-closure consistency.
- **Refs**: GeoCalib: Learning Single-image Calibration with Geometric Optimization; VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency; MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion; FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent; DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras; DUSt3R: Geometric 3D Vision Made Easy.

### Idea 3. Non-rigid registration with local equivariance and generative completion
- **Limit**: Non-rigid registration breaks when overlap is low, surfaces are deformable, or observations are sparse.
- **Problem**: Align partial deformable point clouds while simultaneously completing missing geometry.
- **Why / Method**: Equivariant models preserve transformations but cannot hallucinate missing regions; diffusion models complete shapes but ignore correspondence constraints. Use local SE(3)-equivariant kernels for reliable observed regions and conditional diffusion for missing geometry, tied by cycle-consistent correspondences.
- **Eval**: DeformingThings4D, Dynamic FAUST, ShapeNet partial scans, articulated object datasets; metrics: EPE, Chamfer, correspondence accuracy, cycle error, registration recall.
- **Refs**: CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences; Generative Point Cloud Registration; Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks; Flow Equivariant World Models: Structured Memory for Dynamic Environments; Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment.

## 3D Generative Modeling and Diffusion

### Idea 1. Geometry-verified diffusion for sparse-view 3D reconstruction
- **Limit**: Diffusion priors improve plausibility but can hallucinate geometry inconsistent with observed views.
- **Problem**: Generate complete 3D structure from few views while explicitly rejecting hallucinated surfaces.
- **Why / Method**: 2D/video diffusion models provide strong priors but lack metric observability. Add a visibility-aware verifier that scores generated geometry by multi-view reprojection, depth consistency, and uncertainty, then uses this score to guide denoising.
- **Eval**: DTU, Tanks and Temples, CO3D, RealEstate10K, ScanNet sparse-view splits; metrics: Chamfer, F-score, PSNR/SSIM/LPIPS, depth error, hallucination rate on unobserved regions.
- **Refs**: ReconFusion: 3D Reconstruction with Diffusion Priors; HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction; GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator; Dream-to-Recon: Monocular 3D Reconstruction with Diffusion-Depth Distillation from Single Images; Taming Video Diffusion Prior with Scene-Grounding Guidance for 3D Gaussian Splatting from Sparse Inputs.

### Idea 2. Part-aware 3D diffusion with physical assembly constraints
- **Limit**: Part-level 3D generation often produces plausible parts but weak global assembly, contact, and articulation.
- **Problem**: Generate editable object parts that satisfy geometric adjacency, symmetry, and articulation constraints.
- **Why / Method**: Point/mesh diffusion models optimize shape distribution but do not encode physical compatibility. Use a graph of part contacts and joints as a constraint field during denoising.
- **Eval**: PartNet, ShapeNetPart, Objaverse part annotations, articulated object datasets; metrics: part IoU, Chamfer, contact violation, joint plausibility, edit consistency.
- **Refs**: PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models; SeaLion: Semantic Part-Aware Latent Point Diffusion Models for 3D Generation; CraftsMan3D: High-fidelity Mesh Generation with 3D Native Diffusion and Interactive Geometry Refiner; Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation; Rethinking 3D Shape Generation: Diffusion over Superquadrics.

### Idea 3. Diffusion features as semantic geometry teachers for 3D perception
- **Limit**: Diffusion features are semantically rich but not guaranteed to be spatially stable across views.
- **Problem**: Distill diffusion features into 3D point/Gaussian representations that preserve semantic boundaries and metric geometry.
- **Why / Method**: Direct 2D feature lifting causes view-dependent semantic flicker. Introduce a multi-view consistency loss and geometry-aware feature smoothing that only propagates labels along likely surfaces.
- **Eval**: ScanNet200, S3DIS, Matterport3D, SemanticKITTI, nuScenes occupancy; metrics: mIoU, mAP, boundary F1, cross-view feature consistency, open-vocabulary class accuracy.
- **Refs**: Diffusion 3D Features (Diff3F): Decorating Untextured Shapes with Distilled Semantic Features; 3DiffTection: 3D Object Detection with Geometry-Aware Diffusion Features; GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation; PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting; Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models.

## 3D Large Multimodal Models

### Idea 1. Metric-aware 3D LMMs with calibrated spatial uncertainty
- **Limit**: 3D LMMs answer spatial questions but often overstate certainty for distance, pose, and containment.
- **Problem**: Make a 3D multimodal model return both answer and calibrated spatial uncertainty.
- **Why / Method**: LLM-style decoding optimizes language likelihood, not metric correctness. Attach a metric geometry head that predicts distributions over boxes, distances, and relations, and train with calibration losses.
- **Eval**: ScanQA, SQA3D, ScanRefer/Nr3D/Sr3D, MM-Spatial, RoboSpatial; metrics: QA accuracy, grounding Acc@0.25/0.5, ECE, distance error, relation accuracy.
- **Refs**: 3D-LLM: Injecting the 3D World into Large Language Models; 3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment; SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities; SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models; MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs; RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics; SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding; Uni3DL: A Unified Model for 3D Vision-Language Understanding.

### Idea 2. Reconstruction-reasoning co-training for 3D LMMs
- **Limit**: Many 3D LMMs consume frozen 3D tokens; if reconstruction is wrong, reasoning degrades silently.
- **Problem**: Couple 3D reconstruction quality with downstream language reasoning in a single training loop.
- **Why / Method**: Semantic QA losses alone do not force metric geometry. Jointly train pointmap/Gaussian reconstruction and language instruction tuning, with auxiliary losses for depth, normals, and object relations.
- **Eval**: ScanNet, ScanQA, 3R-Scan, Matterport3D, 3D object grounding; metrics: reconstruction F-score/Chamfer, QA accuracy, relation recall, robustness under pose noise.
- **Refs**: G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning; GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models; SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment; LIRA: Reasoning Reconstruction via Multimodal Large Language Models; LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning.

### Idea 3. Persistent 3D memory for long-horizon embodied reasoning
- **Limit**: 3D LMMs usually reason over a single scene snapshot, while robots need persistent memory over changing spaces.
- **Problem**: Maintain an updatable 3D semantic memory that supports language queries and temporal change reasoning.
- **Why / Method**: Context-window memory cannot track metric changes, and static maps cannot explain object movement. Use object-centric 3D memory slots with time-stamped geometry, language features, and uncertainty.
- **Eval**: Habitat, HM3D, Matterport3D, 3R-Scan, dynamic ScanNet-style sequences, object search tasks; metrics: query accuracy, change detection F1, localization error, memory update latency.
- **Refs**: 3D-SPATIAL MULTIMODAL MEMORY; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs.

## 3D Reconstruction, Geometry, and SLAM

### Idea 1. Active reconstruction with learned failure prediction
- **Limit**: Feed-forward reconstruction models are strong but do not know which next view would reduce uncertainty most.
- **Problem**: Select next views for 3D reconstruction that target failure-prone surfaces and occluded regions.
- **Why / Method**: Passive reconstruction inherits dataset view bias. Use reconstruction uncertainty, visibility gradients, and predicted surface error to drive next-best-view planning.
- **Eval**: ScanNet, Replica, Habitat, CO3D, DTU active-view splits; metrics: Chamfer/F-score versus number of views, coverage, PSNR/SSIM, planning cost.
- **Refs**: ActiveGS: Active Scene Reconstruction using Gaussian Splatting; WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting; Flash3D: Feed-Forward Generalisable 3D Scene Reconstruction from a Single Image; OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects; DUSt3R: Geometric 3D Vision Made Easy; VGGT: Visual Geometry Grounded Transformer.

### Idea 2. Dynamic-scene SLAM with semantic motion layers
- **Limit**: Dynamic objects are usually removed or treated as noise, losing useful semantic and interaction information.
- **Problem**: Reconstruct static background and dynamic objects jointly with separate motion and semantic layers.
- **Why / Method**: Rigid SLAM fails under moving foreground; full dynamic reconstruction is underconstrained. Use object-level motion segmentation, Gaussian/SDF layers, and temporal semantic consistency.
- **Eval**: TartanAir, KITTI/Waymo dynamic scenes, Argoverse, Dynamic Replica, indoor RGB-D dynamic sequences; metrics: ATE/RPE, dynamic object 3D IoU, scene flow EPE, rendering PSNR.
- **Refs**: MAPo: Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for High-Fidelity Dynamic Scene Reconstruction; DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction; 3D Geometry-Aware Deformable Gaussian Splatting for Dynamic View Synthesis; VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency; DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras.

### Idea 3. Self-diagnosing reconstruction under calibration and exposure shifts
- **Limit**: Reconstruction systems fail under exposure, rolling shutter, degraded lighting, and unknown camera parameters.
- **Problem**: Detect and correct image formation failures during online reconstruction.
- **Why / Method**: Geometry loss alone cannot separate photometric artifacts from geometry errors. Add latent nuisance variables for exposure, blur, rolling shutter, and intrinsics, plus a residual classifier that triggers correction modules.
- **Eval**: TUM RGB-D, EuRoC, ETH3D, ScanNet, in-the-wild drone/phone datasets; metrics: ATE/RPE, depth AbsRel, PSNR/SSIM, calibration error, failure detection AUROC.
- **Refs**: AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM; DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting; DroneSplat: 3D Gaussian Splatting for Robust 3D Reconstruction from In-the-Wild Drone Imagery; GeoCalib: Learning Single-image Calibration with Geometric Optimization; DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras.

## 3D Representation Learning and Foundation Models

### Idea 1. Unified 3D tokenization across points, voxels, meshes, and Gaussians
- **Limit**: Current 3D foundation models are tied to one representation, making transfer across tasks brittle.
- **Problem**: Learn a representation-agnostic tokenizer that maps points, voxels, meshes, depth maps, and Gaussian primitives to a shared 3D token space.
- **Why / Method**: Separate tokenizers lose cross-format correspondences. Use contrastive and masked modeling across paired representations generated from the same scene.
- **Eval**: ModelNet40, ShapeNet, ScanNet, S3DIS, Objaverse, downstream detection/segmentation/reconstruction; metrics: linear probing accuracy, mIoU, Chamfer, transfer gap.
- **Refs**: UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting; Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning; Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling; Dens3R: A Foundation Model for 3D Geometry Prediction; Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations.

### Idea 2. Geometry-language pretraining without object labels
- **Limit**: 3D representation learning still depends on labeled categories or synthetic captions.
- **Problem**: Pretrain 3D representations from raw RGB-D/video by aligning geometry changes with natural language-like event abstractions.
- **Why / Method**: CLIP-style labels capture semantics but not metric relations. Build pseudo-language from geometry events: support, containment, occlusion, motion, contact, and visibility.
- **Eval**: ScanNet, 3R-Scan, Aria/egocentric RGB-D, Habitat synthetic videos; metrics: relation classification, grounding, few-shot segmentation, retrieval.
- **Refs**: Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training; UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting; SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding; Spatial Understanding from Videos: Structured Prompts Meet Simulation Data; MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World; GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model.

### Idea 3. Continual 3D pretraining under sensor/domain shifts
- **Limit**: 3D foundation models degrade under new sensors, density, weather, or scanning trajectories.
- **Problem**: Continually adapt 3D representations without catastrophic forgetting.
- **Why / Method**: Fine-tuning on new scans erases old geometry priors. Use replay-free prototype constraints, geometry-preserving masked modeling, and uncertainty-weighted domain adapters.
- **Eval**: ScanNet to S3DIS, SemanticKITTI to nuScenes, indoor to outdoor LiDAR, synthetic to real; metrics: mIoU, retention, forward transfer, calibration.
- **Refs**: Test-Time Adaptation of 3D Point Clouds via Denoising Diffusion Models; Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training; DINOv2: Learning Robust Visual Features without Supervision; RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding; AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning.

## 3D Scene Graphs and Graph Reasoning

### Idea 1. Uncertainty-aware open-vocabulary 3D scene graphs
- **Limit**: Scene graph methods often output deterministic object and relation labels, even when geometry or semantics are ambiguous.
- **Problem**: Build 3D scene graphs with calibrated uncertainty for nodes, relations, and spatial predicates.
- **Why / Method**: VLM features hallucinate rare relations, while geometric rules fail for semantic relations. Use probabilistic relation factors combining geometry, language priors, and multi-view evidence.
- **Eval**: 3DSSG, 3R-Scan, ScanNet, Open3DSG-style tasks; metrics: Recall@K, mR@K, relation ECE, zero-shot relation accuracy, downstream grounding accuracy.
- **Refs**: Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships; 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding; Heterogeneous Graph Learning for Scene Graph Prediction in 3D Point Clouds; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation.

### Idea 2. Dynamic scene graphs as robot memory compression
- **Limit**: Dense maps are costly for long-horizon robots; scene graphs are compact but lose metric detail needed for action.
- **Problem**: Compress long-term 3D maps into scene graphs that still support navigation and manipulation queries.
- **Why / Method**: Pure graphs lose occupancy and pose uncertainty; pure maps are hard for LLM planning. Use hybrid graph nodes with local neural fields/Gaussians and explicit affordance edges.
- **Eval**: Habitat, AI2-THOR, Matterport3D, long-horizon object search/mobile manipulation; metrics: task success, SPL, object localization error, memory footprint, update time.
- **Refs**: MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning; MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs; FunGraph: Functionality Aware 3D Scene Graphs for Language-Prompted Scene Interaction; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs.

### Idea 3. Counterfactual graph reasoning for spatial instruction following
- **Limit**: Current graph reasoning answers what exists, but not how the scene would change after an action.
- **Problem**: Predict object-relation changes under language-described actions.
- **Why / Method**: LLM planning lacks grounded state transition; physics simulators lack semantic priors. Add counterfactual relation predictors trained on before/after scene graph pairs.
- **Eval**: ALFRED, Habitat rearrangement, RLBench, CALVIN, 3R-Scan temporal scenes; metrics: relation transition F1, action feasibility, task success, planning error.
- **Refs**: MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation; Point2Graph: An End-To-End Point Cloud-Based 3D Open-Vocabulary Scene Graph for Robot Navigation; 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models.

## 3D Scene Representations and Neural Fields

### Idea 1. Task-aware Gaussian primitives for perception, not only rendering
- **Limit**: 3DGS is optimized for photorealistic rendering but not necessarily for segmentation, localization, or planning.
- **Problem**: Learn Gaussian primitives whose attributes support both rendering and downstream 3D perception.
- **Why / Method**: Color/opacity gradients do not enforce semantic boundaries or metric uncertainty. Add task heads for occupancy, instance, normal, and uncertainty with multi-objective Gaussian densification.
- **Eval**: ScanNet, Replica, nuScenes, Waymo, Tanks and Temples; metrics: PSNR/SSIM/LPIPS, mIoU, occupancy IoU, localization error, memory/runtime.
- **Refs**: 3D Gaussian Splatting for Real-Time Radiance Field Rendering; SplatFormer: Point Transformer for Robust 3D Gaussian Splatting; Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images; ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting; GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction; PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting.

### Idea 2. Pose-free neural fields with online self-correction
- **Limit**: Pose-free 3DGS/NeRF works offline but struggles with online streams and drift.
- **Problem**: Build an online pose-free neural field that jointly refines camera motion and scene representation.
- **Why / Method**: Offline bundle adjustment is expensive; feed-forward pose estimates drift. Use a sliding-window neural field with local pose graph optimization and learned uncertainty for keyframe selection.
- **Eval**: ScanNet, TUM RGB-D, Replica, CO3D videos, casual phone videos; metrics: ATE/RPE, rendering PSNR, reconstruction Chamfer, runtime, failure rate.
- **Refs**: No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images; FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction; Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM; FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent; BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction; OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects.

### Idea 3. Neural-field compression with semantic guarantees
- **Limit**: Compressed radiance fields preserve pixels but often lose small semantic objects.
- **Problem**: Compress neural/Gaussian scene representations while preserving task-relevant semantics and geometry.
- **Why / Method**: Rate-distortion objectives ignore rare objects and boundaries. Add semantic rate allocation and object-aware reconstruction loss.
- **Eval**: ScanNet, Replica, Mip-NeRF 360, autonomous driving scenes; metrics: bitrate, PSNR/SSIM/LPIPS, mIoU, small-object recall, query latency.
- **Refs**: LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds; S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction; OpenGS-Fusion: Open-Vocabulary Dense Mapping with Hybrid 3D Gaussian Splatting for Refined Object-Level Understanding; LangSplat: 3D Language Gaussian Splatting; 3D Gaussian Splatting for Real-Time Radiance Field Rendering.

## 3D Semantic Understanding and Alignment

### Idea 1. Geometry-first open-vocabulary segmentation
- **Limit**: 2D VLM-lifted 3D segmentation often leaks labels across object boundaries.
- **Problem**: Segment open-vocabulary 3D scenes by enforcing geometry-first grouping before language alignment.
- **Why / Method**: Semantic features are view-dependent; geometry boundaries are stable but not semantic. Build superpoints/Gaussian clusters from normals, depth, and connectivity, then assign language labels with uncertainty.
- **Eval**: ScanNet200, S3DIS, Matterport3D, Replica; metrics: mIoU, hIoU, open-vocabulary AP, boundary F1, long-tail class accuracy.
- **Refs**: OpenScene: 3D Scene Understanding with Open Vocabularies; OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation; OpenMask3D: Open-Vocabulary 3D Instance Segmentation; Details Matter for Indoor Open-vocabulary 3D Instance Segmentation; GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation; PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting; OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection.

### Idea 2. Semantic alignment that separates object identity from viewpoint
- **Limit**: 3D semantic features change with camera view, lighting, and occlusion.
- **Problem**: Learn 3D features invariant to view but sensitive to object identity and part structure.
- **Why / Method**: Averaging multi-view CLIP features blurs object identity. Use contrastive multi-view alignment with view-specific nuisance tokens and part-aware pooling.
- **Eval**: ScanNet, Objaverse, 3D-FUTURE, CO3D, Open-Vocabulary instance segmentation; metrics: retrieval accuracy, instance AP, part mIoU, feature consistency.
- **Refs**: ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting; Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding; Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling; SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining; VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via View Alignment.

### Idea 3. Semantic-geometric collaboration for transparent and reflective objects
- **Limit**: Geometry estimators fail on transparent/reflective objects; semantic priors alone hallucinate shape.
- **Problem**: Estimate depth/normals/segments for optically difficult objects using semantic and physical priors.
- **Why / Method**: Photometric cues are invalid under refraction/reflection. Combine semantic object priors, polarization or multi-view cues, and diffusion-based normal/depth priors with physics losses.
- **Eval**: ClearGrasp, TransCG, transparent object normal/depth datasets, real robot tabletop scans; metrics: depth RMSE/AbsRel, normal error, mask IoU, grasp pose success.
- **Refs**: PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration; Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation; Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data; Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction.

## 3D Vision-Language Grounding

### Idea 1. Grounding with explicit ambiguity modeling
- **Limit**: 3D grounding datasets often assume one correct referent; real instructions can be ambiguous.
- **Problem**: Return a ranked set of plausible referents with clarification questions.
- **Why / Method**: Single-box prediction hides uncertainty and fails for underspecified language. Model grounding as posterior inference over objects and generate disambiguating questions from relation uncertainty.
- **Eval**: ScanRefer, Nr3D, Sr3D, ReferIt3D, IRef-VLA; metrics: Acc@0.25/0.5, top-k recall, clarification success, calibration.
- **Refs**: ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language; ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes; 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds; IRef-VLA: A Benchmark for Interactive Referential Grounding with Imperfect Language in 3D Scenes; VGMamba: Attribute-to-Location Clue Reasoning for Quantity-Agnostic 3D Visual Grounding; ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition.

### Idea 2. Temporal 3D grounding in changing scenes
- **Limit**: Most grounding models use static scenes; robots interact with changing objects.
- **Problem**: Ground language over object trajectories and temporal relations.
- **Why / Method**: Static object features cannot encode before/after, moved, hidden, or replaced. Use object-track memory and temporal relation graphs over 3D detections.
- **Eval**: 3R-Scan temporal scenes, egocentric RGB-D, dynamic ScanNet-style datasets, mobile manipulation logs; metrics: temporal grounding accuracy, track mAP, change F1.
- **Refs**: GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation; Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation; Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation.

### Idea 3. Physics-aware grounding for manipulation affordances
- **Limit**: Grounding identifies objects but not physically valid action regions.
- **Problem**: Ground instructions into actionable 3D regions with affordance and constraint estimates.
- **Why / Method**: VLM grounding can select semantically correct but unreachable or unstable regions. Add geometric affordance fields, contact priors, and robot reachability constraints.
- **Eval**: RLBench, CALVIN, LIBERO, RoboCasa/ManiSkill, real tabletop grasping; metrics: grounding IoU, affordance AP, success rate, collision rate.
- **Refs**: OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection; RoboGround: Robotic Manipulation with Grounded Vision-Language Priors; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping; ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning.

## Benchmarks and Datasets

### Idea 1. 3D spatial generalization benchmark for VLA and VLMs
- **Limit**: Existing benchmarks often test object/task success but not controlled spatial generalization.
- **Problem**: Measure whether models understand distance, occlusion, containment, support, and viewpoint shifts.
- **Why / Method**: High task success can come from memorized action priors. Build controlled scene perturbations with identical semantics but changed geometry.
- **Eval**: New benchmark built from RLBench/CALVIN/LIBERO/Habitat/ScanNet scenes; metrics: spatial consistency score, task success under perturbation, failure attribution.
- **Refs**: RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics; VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks; EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents; MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs; RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation; SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation.

### Idea 2. Open-vocabulary 3D mapping reproducibility benchmark
- **Limit**: Open-vocabulary mapping papers use different scenes, vocabularies, and evaluation protocols.
- **Problem**: Standardize map-building, query, and update evaluation for 3D semantic memory.
- **Why / Method**: mIoU alone ignores queryability and map maintenance. Provide fixed RGB-D/LiDAR streams, query sets, update events, and memory budgets.
- **Eval**: ScanNet, Replica, Matterport3D, 3R-Scan, SemanticKITTI; metrics: open-vocab mIoU/AP, query latency, memory, update cost, forgetting.
- **Refs**: ConceptFusion: Open-set Multimodal 3D Mapping; CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory; OpenScene: 3D Scene Understanding with Open Vocabularies; OpenMask3D: Open-Vocabulary 3D Instance Segmentation; FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs.

### Idea 3. Safety and failure benchmark for 3D VLA systems
- **Limit**: VLA benchmarks under-measure unsafe spatial behavior and perception failure.
- **Problem**: Test physical and semantic safety failures caused by 3D misperception.
- **Why / Method**: Success-rate-only evaluation misses near-collisions, unstable grasps, and semantic confusion. Add adversarial geometry, ambiguous language, transparent objects, and dynamic obstacles.
- **Eval**: LIBERO-Safety, RLBench, CALVIN, real robot safety suites; metrics: safe success rate, collision rate, intervention count, near-miss distance, policy calibration.
- **Refs**: LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models; SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning; Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics; VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks.

## Equivariance, Diffusion, and 3D Action

### Idea 1. Action uncertainty from diffusion score geometry
- **Limit**: Diffusion policies sample actions but rarely expose why alternatives are unsafe or low-confidence.
- **Problem**: Estimate action uncertainty and failure modes from the diffusion score landscape.
- **Why / Method**: Multimodal action distributions are useful only if the robot can choose safe modes. Analyze score curvature and collision/affordance constraints to rank modes.
- **Eval**: PushT, RLBench, CALVIN, real robot manipulation; metrics: success under distribution shift, uncertainty calibration, failure prediction AUROC, intervention reduction.
- **Refs**: Diffusion Policy: Visuomotor Policy Learning via Action Diffusion; RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation; HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model; ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation; FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation; SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning.

### Idea 2. Equivariant diffusion policy with semantic action frames
- **Limit**: Equivariant policies handle pose changes but do not know which object-centric frame matters semantically.
- **Problem**: Learn action diffusion in dynamically selected semantic frames.
- **Why / Method**: Global SE(3) equivariance is too rigid for articulated or multi-object tasks. Select frames from object parts and relations, then denoise actions in those local frames.
- **Eval**: RLBench, CALVIN, LIBERO, ManiSkill; metrics: success rate, pose generalization, few-shot transfer, collision rate.
- **Refs**: Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation; ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY; EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation; SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space; DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo; SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation.

### Idea 3. Consistency-regularized 4D action representation
- **Limit**: VLA policies often react frame-by-frame and lose temporal 3D consistency.
- **Problem**: Represent action as a trajectory field over 4D scene geometry.
- **Why / Method**: Token actions lack explicit spatial continuity. Use a 4D Gaussian/point field whose denoising process predicts future object and gripper motion jointly.
- **Eval**: LIBERO long-horizon, RLBench, BridgeData, real bimanual manipulation; metrics: success, trajectory smoothness, waypoint error, long-horizon completion.
- **Refs**: 4D-VLA:  Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration; DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation; RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation; Diffusion Policy: Visuomotor Policy Learning via Action Diffusion; G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation; ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation.

## Foundations: 3D Detection and BEV Perception

### Idea 1. BEV perception with explicit uncertainty transfer from depth
- **Limit**: BEV models fuse camera features but often hide depth uncertainty.
- **Problem**: Propagate depth uncertainty into BEV occupancy and detection decisions.
- **Why / Method**: Incorrect depth creates false BEV evidence. Learn distributions over depth bins and weight BEV features by calibrated uncertainty.
- **Eval**: nuScenes, Waymo, Argoverse, KITTI; metrics: NDS, mAP, occupancy IoU, calibration ECE, robustness under weather/night.
- **Refs**: BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers; BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation; BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection; PETR: Position Embedding Transformation for Multi-View 3D Object Detection; CenterPoint: Center-based 3D Object Detection and Tracking; RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction.

### Idea 2. Open-vocabulary 3D detection with geometric verification
- **Limit**: Open-vocabulary detection can hallucinate classes when 2D priors disagree with 3D geometry.
- **Problem**: Detect long-tail objects in 3D while verifying shape, size, and placement.
- **Why / Method**: Text-image priors are not enough for 3D boxes. Add category-agnostic geometric objectness and class-specific plausibility priors.
- **Eval**: nuScenes, Waymo, ScanNet200, OV-3D detection splits; metrics: mAP, open-vocab AP, false-positive rate, size/orientation error.
- **Refs**: OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection; Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection; OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation; OpenScene: 3D Scene Understanding with Open Vocabularies; Open-Vocabulary Octree-Graph for 3D Scene Understanding.

### Idea 3. Foundation BEV tokens for downstream planning
- **Limit**: BEV features are trained for detection/segmentation but not reusable for planning or VLA.
- **Problem**: Pretrain BEV tokens that encode occupancy, semantics, motion, and affordance.
- **Why / Method**: Detection supervision misses free-space and interaction geometry. Use masked BEV modeling across camera/LiDAR/radar and future prediction.
- **Eval**: nuScenes, Waymo, nuPlan, OpenScene driving; metrics: NDS, occupancy mIoU, motion ADE/FDE, planning collision/rule violation.
- **Refs**: BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers; Planning-oriented Autonomous Driving; V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection; WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving; UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction; Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving.

## Foundations: 3D Geometry and Point Clouds

### Idea 1. Point-cloud foundation models with density-invariant reasoning
- **Limit**: Point models are sensitive to sampling density and sensor pattern.
- **Problem**: Learn point features robust to nonuniform density, missing regions, and mixed sensors.
- **Why / Method**: Farthest-point sampling and fixed-radius neighborhoods encode sensor bias. Use density-normalized neighborhoods and self-supervised completion.
- **Eval**: ModelNet40, ShapeNetPart, ScanNet, SemanticKITTI, cross-sensor LiDAR datasets; metrics: accuracy, mIoU, robustness curves under downsampling/dropout.
- **Refs**: PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation; PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space; Dynamic Graph CNN for Learning on Point Clouds; KPConv: Flexible and Deformable Convolution for Point Clouds; Point Transformer; Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning.

### Idea 2. Geometry primitives as interpretable latent variables
- **Limit**: Deep point features are hard to inspect and transfer.
- **Problem**: Learn primitives such as planes, quadrics, symmetry axes, and part joints as latent structure.
- **Why / Method**: Dense embeddings capture correlations but not causal geometry. Add primitive discovery losses and use them as tokens for downstream reasoning.
- **Eval**: ABC, ShapeNet, ScanNet planes, indoor scenes; metrics: primitive fitting error, segmentation IoU, reconstruction Chamfer, downstream relation accuracy.
- **Refs**: PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space; QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction; PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-forward Planar Splatting; SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks; SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs.

### Idea 3. Self-supervised correspondence as the backbone for 3D reasoning
- **Limit**: Many 3D tasks relearn matching, grounding, and tracking separately.
- **Problem**: Pretrain a universal correspondence model across objects, scenes, and time.
- **Why / Method**: Classification-style pretraining ignores geometry equivalence. Use cycle consistency, scene flow, and multi-view reconstruction as pretext tasks.
- **Eval**: 3DMatch, KITTI scene flow, FlyingThings3D, ScanNet tracking; metrics: correspondence accuracy, EPE, registration recall, transfer performance.
- **Refs**: Dynamic Graph CNN for Learning on Point Clouds; Point Transformer; CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences; FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent; SSRFlow: Semantic-aware Fusion with Spatial Temporal Re-embedding for Real-world Scene Flow; U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching.

## Foundations: 3D Representation Learning

### Idea 1. Cross-representation masked modeling
- **Limit**: Masked point modeling improves point clouds but does not transfer cleanly to meshes, voxels, or Gaussians.
- **Problem**: Predict missing structure across representations, not only within one representation.
- **Why / Method**: Single-format masking learns format-specific shortcuts. Train with paired views of the same object as point, voxel, mesh, and Gaussian targets.
- **Eval**: ShapeNet, Objaverse, ScanNet; metrics: downstream classification, segmentation, reconstruction Chamfer, cross-format retrieval.
- **Refs**: Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling; Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning; UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting; Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training.

### Idea 2. Geometry-aware prompt tuning for 3D foundation models
- **Limit**: Prompting in 3D is less mature than in 2D VLMs.
- **Problem**: Adapt a 3D foundation model to new tasks using few geometric prompts.
- **Why / Method**: Text prompts alone are underspecified for 3D. Use geometric prompts: points, planes, boxes, paths, and symmetry axes.
- **Eval**: ScanNet, S3DIS, ShapeNetPart, object affordance datasets; metrics: few-shot mIoU, AP, prompt efficiency, cross-domain transfer.
- **Refs**: GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model; Segment Any 3D Object with Language; Segment Anything; DINOv2: Learning Robust Visual Features without Supervision; Uni3DL: A Unified Model for 3D Vision-Language Understanding.

### Idea 3. Scale-consistent 3D pretraining
- **Limit**: Models trained on object-scale data fail on room/city-scale scenes and vice versa.
- **Problem**: Learn scale-aware 3D representations that transfer across object, room, and street scenes.
- **Why / Method**: Fixed receptive fields cannot encode scale hierarchies. Use multi-scale tokens with explicit physical scale embeddings.
- **Eval**: ShapeNet/Objaverse, ScanNet/S3DIS, SemanticKITTI/nuScenes; metrics: transfer mIoU, detection mAP, scale generalization.
- **Refs**: PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space; KPConv: Flexible and Deformable Convolution for Point Clouds; 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks; Dens3R: A Foundation Model for 3D Geometry Prediction; VGGT: Visual Geometry Grounded Transformer; UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction.

## Foundations: 3D Scene Representations

### Idea 1. Scene representation with separate geometry, appearance, and semantics
- **Limit**: Neural fields often entangle color, density, and semantics.
- **Problem**: Factorize scenes into geometry, appearance, material, and semantic fields.
- **Why / Method**: Entanglement hurts editing, relighting, and open-vocabulary querying. Use structured latent factors with cross-factor consistency losses.
- **Eval**: Replica, ScanNet, DTU, NeRF synthetic, relighting datasets; metrics: PSNR/SSIM, normal error, edit consistency, semantic mIoU.
- **Refs**: NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis; 3D Gaussian Splatting for Real-Time Radiance Field Rendering; ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting; SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering; Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting; GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering.

### Idea 2. Neural field as active robot memory
- **Limit**: NeRF/3DGS scene representations are usually offline assets.
- **Problem**: Turn neural fields into incrementally updated robot memory.
- **Why / Method**: Robot memory needs update, query, uncertainty, and deletion. Add streaming updates and task-conditioned compression.
- **Eval**: Habitat, Replica, ScanNet, real RGB-D robot scans; metrics: update time, map accuracy, query accuracy, memory footprint.
- **Refs**: CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory; ConceptFusion: Open-set Multimodal 3D Mapping; OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting; S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction; VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs.

### Idea 3. Hybrid explicit-implicit maps for robust planning
- **Limit**: Dense implicit maps are hard to use for collision checking; explicit maps lose semantic detail.
- **Problem**: Combine explicit occupancy/mesh with implicit semantic/radiance fields.
- **Why / Method**: Planning needs fast conservative geometry, while reasoning needs rich semantics. Maintain both with consistency constraints.
- **Eval**: Habitat navigation, manipulation in Replica/ScanNet, real robot maps; metrics: collision rate, SPL, map IoU, query accuracy.
- **Refs**: NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis; 3D Gaussian Splatting for Real-Time Radiance Field Rendering; Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps; FOCI: Trajectory Optimization on Gaussian Splats; CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory; ConceptFusion: Open-set Multimodal 3D Mapping.

## Foundations: 3D Semantic Occupancy

### Idea 1. Occupancy uncertainty for planning-safe perception
- **Limit**: Occupancy maps typically produce point estimates, not risk-aware predictions.
- **Problem**: Estimate uncertainty over occupied/free/unknown space and semantic labels.
- **Why / Method**: Downstream planners need conservative risk bounds. Train occupancy with Bayesian or ensemble uncertainty calibrated by sensor visibility.
- **Eval**: nuScenes/Waymo occupancy, Habitat, robot navigation logs; metrics: IoU, ECE, risk-weighted collision rate, unknown-space recall.
- **Refs**: VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion; ODG: Occupancy Prediction Using Dual Gaussians; QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction; Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction; GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction.

### Idea 2. Open-vocabulary semantic occupancy from RGB-only streams
- **Limit**: Occupancy methods often use closed-set labels and/or LiDAR.
- **Problem**: Predict dense 3D occupancy with open-vocabulary semantics from RGB video.
- **Why / Method**: 2D semantics are rich but lack occluded structure. Use video geometry plus VLM feature lifting and occupancy completion priors.
- **Eval**: SemanticKITTI, nuScenes occupancy, Occ3D, ScanNet occupancy; metrics: occupancy IoU, semantic mIoU, open-vocab AP, occluded-region accuracy.
- **Refs**: VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion; AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting; EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding; RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction; Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction; LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering.

### Idea 3. Object-centric occupancy for manipulation
- **Limit**: Voxel occupancy is useful for navigation but too coarse for object manipulation.
- **Problem**: Represent occupancy at object-part resolution with affordance labels.
- **Why / Method**: Manipulation requires contact surfaces and part geometry. Use object-centric occupancy heads and part-level supervision.
- **Eval**: RLBench, ManiSkill, PartNet-Mobility, real RGB-D grasping; metrics: part IoU, affordance AP, grasp success, collision rate.
- **Refs**: VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion; OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection; GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping; Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction; PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models.

## Foundations: Diffusion and Generative Models

### Idea 1. Geometry-constrained latent diffusion for 3D perception
- **Limit**: Latent diffusion models are strong generators but weak metric estimators.
- **Problem**: Use diffusion as a prior while enforcing metric constraints from sensors.
- **Why / Method**: Pure denoising maximizes plausibility, not observability. Inject differentiable rendering, depth, and epipolar constraints into the denoising loop.
- **Eval**: DTU, CO3D, ScanNet, depth benchmarks; metrics: Chamfer, F-score, depth AbsRel, hallucination rate.
- **Refs**: Denoising Diffusion Probabilistic Models; High-Resolution Image Synthesis with Latent Diffusion Models; ReconFusion: 3D Reconstruction with Diffusion Priors; Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation; PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation.

### Idea 2. Diffusion uncertainty as a perception confidence measure
- **Limit**: Diffusion samples are diverse but uncertainty is rarely calibrated for downstream decisions.
- **Problem**: Convert sample diversity into calibrated geometric uncertainty.
- **Why / Method**: Multiple plausible outputs may reflect ambiguity or model noise. Decompose uncertainty into epistemic and aleatoric components using consistency across sensor constraints.
- **Eval**: NYUv2 depth, KITTI depth, ScanNet, sparse-view reconstruction; metrics: NLL, ECE, AUROC for error detection, depth/reconstruction error.
- **Refs**: Denoising Diffusion Probabilistic Models; Bayesian Diffusion Models for 3D Shape Reconstruction; HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction; Light Transport-aware Diffusion Posterior Sampling for Single-View Reconstruction of 3D Volumes.

### Idea 3. Multi-modal diffusion for sensor completion
- **Limit**: LiDAR/radar/camera completion methods are modality-specific.
- **Problem**: Complete missing geometry across RGB, depth, LiDAR, radar, and tactile inputs.
- **Why / Method**: Each sensor has different missingness patterns. A shared diffusion backbone with modality tokens can learn complementary priors.
- **Eval**: nuScenes, Waymo, SemanticKITTI, tactile reconstruction datasets; metrics: completion IoU, Chamfer, mIoU, robustness under sensor dropout.
- **Refs**: V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection; Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction; Scaling Diffusion Models to Real-World 3D LiDAR Scene Completion; L3DR: 3D-aware LiDAR Diffusion and Rectification; Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion.

## Foundations: Equivariance and Geometry

### Idea 1. Learned equivariance selection instead of fixed symmetry groups
- **Limit**: Fixed SE(3)/E(n) equivariance can be too restrictive or unnecessary for some tasks.
- **Problem**: Learn which transformations should be equivariant, invariant, or variant for each object/scene region.
- **Why / Method**: Scenes mix rigid objects, articulated parts, and semantic labels. Use a gating network over local symmetry groups.
- **Eval**: ModelNet, ShapeNetPart, molecular geometry, articulated object datasets; metrics: accuracy, equivariance error, sample efficiency.
- **Refs**: SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks; E(n) Equivariant Graph Neural Networks; GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks; Equivariant Neural Networks for General Linear Symmetries; Flow Equivariant World Models: Structured Memory for Dynamic Environments.

### Idea 2. Geometry-aware attention with physical coordinate frames
- **Limit**: Transformers treat 3D tokens as generic sequences unless positional encoding is carefully designed.
- **Problem**: Build attention that respects distances, rotations, and local frames.
- **Why / Method**: Absolute coordinates overfit to dataset frames. Use relative pose, local tangent frames, and invariant/equivariant attention kernels.
- **Eval**: ScanNet segmentation, 3DMatch, ShapeNetPart, molecular benchmarks; metrics: mIoU, registration recall, equivariance error.
- **Refs**: SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks; Point Transformer; GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks; Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks.

### Idea 3. Equivariant memory for dynamic environments
- **Limit**: Memory representations often fail when the same object is seen from new poses.
- **Problem**: Store object memories in canonical equivariant frames.
- **Why / Method**: View-specific memory duplicates objects and confuses tracking. Canonicalize local object states while preserving pose transforms.
- **Eval**: 3R-Scan, dynamic object tracking, Habitat object search; metrics: re-identification accuracy, pose error, memory size, query accuracy.
- **Refs**: Flow Equivariant World Models: Structured Memory for Dynamic Environments; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs.

## Foundations: Monocular Geometry

### Idea 1. Metric depth with scene-level scale reasoning
- **Limit**: Monocular depth models still struggle with absolute scale across domains.
- **Problem**: Infer metric depth using object size, camera height, horizon, and scene layout priors.
- **Why / Method**: Pixel-level depth alone is scale ambiguous. Add a scene-level scale graph and uncertainty calibration.
- **Eval**: NYUv2, KITTI, ETH3D, ScanNet, DIODE; metrics: AbsRel, RMSE, delta accuracy, scale error, cross-domain robustness.
- **Refs**: Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data; Depth Anything V2; UniDepth: Universal Monocular Metric Depth Estimation; Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation; GeoCalib: Learning Single-image Calibration with Geometric Optimization.

### Idea 2. Depth models that know when diffusion priors hallucinate
- **Limit**: Diffusion-based depth can produce smooth plausible maps that ignore small geometric evidence.
- **Problem**: Detect and correct hallucinated depth regions.
- **Why / Method**: Generative priors fill missing detail but may override image cues. Use edge/normal consistency and test-time photometric checks to flag hallucination.
- **Eval**: NYUv2, KITTI, ScanNet, transparent/reflective object depth; metrics: AbsRel, boundary F1, hallucination AUROC.
- **Refs**: Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation; GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion; PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation; PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration; Dream-to-Recon: Monocular 3D Reconstruction with Diffusion-Depth Distillation from Single Images.

### Idea 3. Monocular geometry as a reusable prior for robot mapping
- **Limit**: Monocular depth is often evaluated per-frame, not as a mapping prior.
- **Problem**: Use monocular geometry to initialize and regularize robot SLAM/3DGS maps.
- **Why / Method**: SLAM needs temporal consistency; depth models provide strong but noisy priors. Fuse them with pose graph uncertainty and reject inconsistent priors.
- **Eval**: TUM RGB-D, ScanNet, Replica, monocular robot sequences; metrics: ATE/RPE, depth RMSE, reconstruction F-score, map completeness.
- **Refs**: Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data; Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation; DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras; SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM; VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency; Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM.

## Foundations: RL and Imitation Learning

### Idea 1. 3D state abstraction for offline RL
- **Limit**: Offline RL often learns from pixels or low-dimensional states, missing reusable 3D structure.
- **Problem**: Learn compact 3D state abstractions for offline robot policies.
- **Why / Method**: Pixel policies overfit to camera placement; full 3D maps are too large. Use object-centric 3D tokens and relation features as policy state.
- **Eval**: D4RL-style robotics, BridgeData, LIBERO, CALVIN; metrics: success rate, return, cross-camera transfer, data efficiency.
- **Refs**: Decision Transformer: Reinforcement Learning via Sequence Modeling; Diffusion Policy: Visuomotor Policy Learning via Action Diffusion; VIP: Vision Instructed Pre-training for Robotic Manipulation; VIMA: General Robot Manipulation with Multimodal Prompts; Open X-Embodiment: Robotic Learning Datasets and RT-X Models.

### Idea 2. RL from VLM feedback grounded in 3D checks
- **Limit**: VLM feedback can reward semantically plausible but physically wrong behavior.
- **Problem**: Combine VLM feedback with 3D feasibility checks for RL.
- **Why / Method**: Text feedback misses collision, reachability, and contact geometry. Use geometric validators as reward filters.
- **Eval**: RLBench, ManiSkill, CALVIN, real manipulation; metrics: success, unsafe action rate, reward hacking rate, sample efficiency.
- **Refs**: Real-World Offline Reinforcement Learning from VLM Feedback; Do As I Can, Not As I Say: Grounding Language in Robotic Affordances; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning.

### Idea 3. Imitation learning with counterfactual view synthesis
- **Limit**: Demonstrations cover limited camera viewpoints and object poses.
- **Problem**: Augment demonstrations by synthesizing consistent alternative views and object poses.
- **Why / Method**: Naive image augmentation breaks 3D action correspondence. Use 3D reconstruction/GS maps to render counterfactual views and transform actions accordingly.
- **Eval**: BridgeData, LIBERO, RLBench, real robot imitation; metrics: success under novel views, pose generalization, sample efficiency.
- **Refs**: Diffusion Policy: Visuomotor Policy Learning via Action Diffusion; Open X-Embodiment: Robotic Learning Datasets and RT-X Models; Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps; GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting; pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction; 3D Gaussian Splatting for Real-Time Radiance Field Rendering.

## Foundations: SLAM and Sensor Geometry

### Idea 1. Multi-sensor SLAM with learned degeneracy detection
- **Limit**: LiDAR-camera-inertial fusion fails in degenerate geometry or sensor desynchronization.
- **Problem**: Detect sensor degeneracy and switch fusion weights online.
- **Why / Method**: Static fusion weights cannot handle tunnels, glass, rain, or motion blur. Predict per-sensor reliability and optimize pose with adaptive covariance.
- **Eval**: KITTI, nuScenes, Waymo, Newer College, UAV/UGV sequences; metrics: ATE/RPE, failure rate, calibration drift, robustness under dropout.
- **Refs**: BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation; TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving; LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments; FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry; LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping; V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection.

### Idea 2. Semantic loop closure with geometric verification
- **Limit**: Visual loop closure can confuse repeated places; semantic loop closure can hallucinate.
- **Problem**: Close loops using both object-level semantics and metric geometry.
- **Why / Method**: Appearance-only matching fails under lighting, while semantic labels are coarse. Use scene graph candidates and verify with geometric registration.
- **Eval**: TUM RGB-D, KITTI, Oxford RobotCar, ScanNet, 3R-Scan; metrics: loop precision/recall, ATE/RPE, false-loop rate.
- **Refs**: ORB-SLAM: A Versatile and Accurate Monocular SLAM System; DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras; SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs; LoopSplat: Loop Closure by Registering 3D Gaussian Splats; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs.

### Idea 3. SLAM maps that expose planning risk
- **Limit**: SLAM outputs maps but not task-specific risk for navigation/manipulation.
- **Problem**: Estimate traversability, collision, and semantic uncertainty directly from SLAM.
- **Why / Method**: Planners need conservative map risk. Attach risk heads to neural/Gaussian SLAM maps and calibrate with observed failures.
- **Eval**: Habitat, real robot navigation, SemanticKITTI traversability; metrics: SPL, collision rate, risk calibration, ATE/RPE.
- **Refs**: DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras; SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM; Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps; VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs.

## Foundations: Transformer and Language Models

### Idea 1. Geometry-aware context compression for long 3D scenes
- **Limit**: Transformers cannot attend to all tokens in large 3D scenes or long robot histories.
- **Problem**: Compress 3D context without losing task-relevant metric structure.
- **Why / Method**: Naive token pruning removes small objects and relations. Use geometry-aware token merging based on visibility, objectness, and query relevance.
- **Eval**: ScanQA, 3D grounding, Habitat long-horizon tasks, VLA manipulation; metrics: accuracy/success versus token budget, latency, memory.
- **Refs**: Attention Is All You Need; 3D-LLM: Injecting the 3D World into Large Language Models; SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models; VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching; Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning; MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation.

### Idea 2. Chain-of-geometry reasoning for LLM planners
- **Limit**: Chain-of-thought is linguistic and may not correspond to physical geometry.
- **Problem**: Make LLMs produce intermediate geometric variables before plans.
- **Why / Method**: Language-only reasoning misses reachability, occlusion, and spatial constraints. Force intermediate predictions: boxes, distances, support relations, free-space paths.
- **Eval**: ALFRED, Habitat, RLBench, CALVIN, RoboSpatial; metrics: plan success, geometric variable accuracy, collision rate.
- **Refs**: Attention Is All You Need; Language Models are Few-Shot Learners; Code as Policies: Language Model Programs for Embodied Control; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models; ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models.

### Idea 3. Retrieval-augmented 3D reasoning from paper-like scene memories
- **Limit**: LLMs need external memory for large environments but retrieval is usually text-only.
- **Problem**: Retrieve relevant 3D map fragments and prior episodes for reasoning.
- **Why / Method**: Text retrieval cannot capture geometry similarity. Build a multimodal retriever over scene graphs, Gaussian features, and language summaries.
- **Eval**: embodied QA, long-horizon navigation, object search; metrics: retrieval recall, QA accuracy, task success, token cost.
- **Refs**: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding; Language Models are Few-Shot Learners; 3D-SPATIAL MULTIMODAL MEMORY; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models.

## Foundations: Vision Foundation Models

### Idea 1. 2D foundation features with 3D consistency constraints
- **Limit**: DINO/SAM/CLIP features are powerful but not inherently multi-view consistent.
- **Problem**: Adapt 2D foundation features into stable 3D features.
- **Why / Method**: Direct feature lifting creates view-dependent noise. Use multi-view cycle consistency and surface-aware feature aggregation.
- **Eval**: ScanNet, CO3D, Replica, open-vocabulary segmentation; metrics: mIoU, feature consistency, retrieval accuracy.
- **Refs**: DINOv2: Learning Robust Visual Features without Supervision; Segment Anything; Learning Transferable Visual Models From Natural Language Supervision; OpenScene: 3D Scene Understanding with Open Vocabularies; ConceptFusion: Open-set Multimodal 3D Mapping; Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding.

### Idea 2. SAM-like prompting for 3D scenes
- **Limit**: 2D SAM prompts do not directly handle volumetric objects or occlusion.
- **Problem**: Segment 3D objects from point, box, mask, and language prompts.
- **Why / Method**: 2D prompts only observe visible surfaces. A 3D prompt encoder should propagate across geometry and infer occluded object extent.
- **Eval**: ScanNet, S3DIS, Objaverse, PartNet; metrics: 3D mask IoU, occluded IoU, prompt efficiency.
- **Refs**: Segment Anything; OpenMask3D: Open-Vocabulary 3D Instance Segmentation; Segment Any 3D Object with Language; OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation; Search3D: Hierarchical Open-Vocabulary 3D Segmentation.

### Idea 3. Foundation features for failure detection
- **Limit**: Foundation vision models are used for perception, less for detecting perception failure.
- **Problem**: Detect when 3D predictions conflict with 2D foundation features.
- **Why / Method**: A bad reconstruction often still renders plausible RGB. Compare rendered feature maps to 2D foundation feature maps to spot inconsistency.
- **Eval**: ScanNet, Replica, reconstruction benchmarks with injected pose/depth errors; metrics: failure AUROC, localization of bad regions, reconstruction correction.
- **Refs**: DINOv2: Learning Robust Visual Features without Supervision; Segment Anything; Exploiting Semantic Reconstruction to Mitigate Hallucinations in Vision-Language Models; HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction; SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment.

## Foundations: Vision-Language Models

### Idea 1. Spatially calibrated CLIP features
- **Limit**: CLIP aligns images and text but not metric 3D position.
- **Problem**: Learn CLIP-like features that preserve spatial relations and scale.
- **Why / Method**: Contrastive image-caption training ignores metric structure. Add depth, relative pose, and relation prediction losses.
- **Eval**: COCO+depth, ScanNet, RoboSpatial, 3D grounding; metrics: retrieval, relation accuracy, depth-aware grounding.
- **Refs**: Learning Transferable Visual Models From Natural Language Supervision; SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities; RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics; G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning; Grounded 3D-Aware Spatial Vision-Language Modeling.

### Idea 2. VLM feature debiasing for long-tail 3D classes
- **Limit**: VLMs favor frequent web concepts and fail long-tail indoor/robotic objects.
- **Problem**: Adapt VLM features for long-tail 3D object recognition without dense labels.
- **Why / Method**: Web priors underrepresent tool states, parts, and affordances. Use 3D clustering and pseudo-label reweighting to debias.
- **Eval**: ScanNet200, LVIS-style 3D classes, PartNet, robot household datasets; metrics: long-tail mIoU/AP, rare-class recall.
- **Refs**: Learning Transferable Visual Models From Natural Language Supervision; OpenScene: 3D Scene Understanding with Open Vocabularies; RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding; AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning; Details Matter for Indoor Open-vocabulary 3D Instance Segmentation; OpenMask3D: Open-Vocabulary 3D Instance Segmentation.

### Idea 3. VLMs with explicit geometric refusal
- **Limit**: VLMs answer spatial questions even when image evidence is insufficient.
- **Problem**: Make VLMs abstain or ask for a new view when geometry is underdetermined.
- **Why / Method**: Language likelihood rewards confident answers. Add observability prediction and ask-for-view policy.
- **Eval**: visual grounding, embodied QA, ambiguous scenes; metrics: selective accuracy, abstention calibration, view request efficiency.
- **Refs**: Learning Transferable Visual Models From Natural Language Supervision; SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities; MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs; Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation; ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination.

## Foundations: Vision-Language-Action and Robotics

### Idea 1. Affordance-grounded LLM planning with 3D value maps
- **Limit**: LLM planners reason semantically but not physically.
- **Problem**: Convert language plans into 3D affordance and constraint maps.
- **Why / Method**: Text plans can be infeasible. Couple LLM decomposition with learned 3D value maps and low-level policies.
- **Eval**: RLBench, CALVIN, real tabletop/mobile manipulation; metrics: task success, plan feasibility, recovery rate.
- **Refs**: Do As I Can, Not As I Say: Grounding Language in Robotic Affordances; Code as Policies: Language Model Programs for Embodied Control; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; RoboGround: Robotic Manipulation with Grounded Vision-Language Priors.

### Idea 2. Robot data curation by 3D novelty and failure
- **Limit**: Large robot datasets are expensive and often redundant.
- **Problem**: Select demonstrations that maximize 3D geometric and semantic coverage.
- **Why / Method**: Random data scaling wastes budget. Use 3D scene diversity, object relation novelty, and failure uncertainty for active data selection.
- **Eval**: Open X-Embodiment, BridgeData, LIBERO; metrics: success per data hour, coverage, generalization to novel scenes.
- **Refs**: Open X-Embodiment: Robotic Learning Datasets and RT-X Models; LLaRA: Supercharging Robot Learning Data for Vision-Language Policy; VIP: Vision Instructed Pre-training for Robotic Manipulation; RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation; RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation.

### Idea 3. 3D foundation policy interface standardization
- **Limit**: VLA models use incompatible action tokenization and 3D inputs.
- **Problem**: Define a standard intermediate 3D state-action interface for robot foundation models.
- **Why / Method**: End-to-end VLA hides embodiment-specific geometry. Use a common interface: object-centric 3D tokens, affordance maps, and action constraints.
- **Eval**: Open X-Embodiment, BridgeData, RLBench, CALVIN, LIBERO; metrics: cross-embodiment success, data efficiency, adaptation steps.
- **Refs**: RT-1: Robotics Transformer for Real-World Control at Scale; RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control; PaLM-E: An Embodied Multimodal Language Model; Open X-Embodiment: Robotic Learning Datasets and RT-X Models; OpenVLA: An Open-Source Vision-Language-Action Model; Octo: An Open-Source Generalist Robot Policy.

## Language-Embedded NeRF and Gaussian Fields

### Idea 1. Geometry-semantic disentanglement in language Gaussians
- **Limit**: Language Gaussians entangle appearance, geometry, and semantics.
- **Problem**: Separate semantic features from rendering attributes without losing localization.
- **Why / Method**: Joint optimization causes semantics to follow texture artifacts. Add extrinsic semantic field, geometry anchors, and feature consistency constraints.
- **Eval**: ScanNet, LERF datasets, Replica, open-vocabulary 3D segmentation; metrics: query AP, mIoU, PSNR, feature consistency.
- **Refs**: LangSplat: 3D Language Gaussian Splatting; ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting; CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting; CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting; Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation; Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration.

### Idea 2. Persistent language fields with temporal update rules
- **Limit**: Language fields are often static and degrade when objects move.
- **Problem**: Maintain language-embedded 3DGS/NeRF maps under dynamic scene changes.
- **Why / Method**: Static feature averaging cannot handle object removal or relocation. Use object-level feature slots with temporal confidence and forgetting.
- **Eval**: 3R-Scan, Replica dynamic variants, robot object search logs; metrics: query accuracy over time, change F1, map update latency.
- **Refs**: LERF: Language Embedded Radiance Fields; LangSplat: 3D Language Gaussian Splatting; CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation; OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting.

### Idea 3. Language fields for action affordance queries
- **Limit**: Language fields answer what/where but not what-action-is-possible.
- **Problem**: Extend language fields to affordance and manipulation constraints.
- **Why / Method**: Semantics alone cannot infer graspability, pushability, or support. Add affordance supervision from demonstrations and geometry-derived contact features.
- **Eval**: RLBench, CALVIN, PartNet-Mobility, real robot grasping; metrics: affordance AP, grounding IoU, manipulation success.
- **Refs**: CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory; OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection; GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; RoboGround: Robotic Manipulation with Grounded Vision-Language Priors.

## Navigation and Embodied AI

### Idea 1. Geometry-aware VLN with uncertainty-driven exploration
- **Limit**: VLN agents follow language but often explore inefficiently when object location is uncertain.
- **Problem**: Choose exploration actions that reduce uncertainty over grounded 3D goals.
- **Why / Method**: VLM priors guess likely locations but cannot verify occluded space. Use 3D belief maps with active perception and semantic priors.
- **Eval**: R2R, RxR, VLN-CE, Habitat ObjectNav, HM3D; metrics: SR, SPL, nDTW, explored area, goal localization error.
- **Refs**: VLMaps: Visual-Language Maps for Robot Navigation; D3D-VLP: Dynamic 3D Vision-Language-Planning Model for Embodied Grounding and Navigation; BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation; GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation; ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination; Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation.

### Idea 2. Gaussian-map navigation with safety envelopes
- **Limit**: 3DGS maps are attractive for navigation but not inherently safe for collision checking.
- **Problem**: Navigate using Gaussian maps with conservative free-space bounds.
- **Why / Method**: Rendering quality does not equal traversability certainty. Convert Gaussians to risk-aware occupancy and inflate uncertainty near thin structures.
- **Eval**: Habitat, Replica, real robot navigation, Gaussian map datasets; metrics: SPL, collision rate, map risk calibration, runtime.
- **Refs**: Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps; VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting; IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation; SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving; FOCI: Trajectory Optimization on Gaussian Splats; GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting.

### Idea 3. Object search with dynamic carrier relationships
- **Limit**: ObjectNav assumes static object locations, but objects move with carriers such as humans, trays, drawers, and tables.
- **Problem**: Search for objects using dynamic carrier-relation reasoning.
- **Why / Method**: Static semantic maps fail when target objects relocate. Model support/container/carrier relations and update beliefs after observations.
- **Eval**: Habitat ObjectNav with dynamic objects, AI2-THOR rearrangement, real home robot logs; metrics: SR, SPL, search time, relation prediction F1.
- **Refs**: OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph; Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation; Dual-Level Open-Vocabulary 3D Scene Representation.

## Open-Vocabulary 3D Mapping

### Idea 1. Open-vocabulary maps with memory budgets
- **Limit**: Dense feature maps are memory heavy.
- **Problem**: Maintain query performance under strict memory and compute budgets.
- **Why / Method**: Storing every feature is wasteful. Use object/region prototypes and uncertainty-driven feature retention.
- **Eval**: ScanNet, Matterport3D, long robot sequences; metrics: open-vocab AP/mIoU, memory, update latency, query latency.
- **Refs**: CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory; ConceptFusion: Open-set Multimodal 3D Mapping; FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models; LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds; S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction.

### Idea 2. Map-level vocabulary expansion through interaction
- **Limit**: Open-vocabulary maps depend on fixed text prompts and VLM priors.
- **Problem**: Let a robot expand and refine map vocabulary through interaction and user feedback.
- **Why / Method**: Static vocabularies miss local object names, functions, and aliases. Use user corrections and observation clusters to update semantic prototypes.
- **Eval**: Replica/ScanNet map queries, real robot deployment; metrics: query accuracy, new-label learning speed, forgetting, user correction count.
- **Refs**: ConceptFusion: Open-set Multimodal 3D Mapping; FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models; Search3D: Hierarchical Open-Vocabulary 3D Segmentation; Clio: Real-time Task-Driven Open-Set 3D Scene Graphs; OpenScene: 3D Scene Understanding with Open Vocabularies; OpenMask3D: Open-Vocabulary 3D Instance Segmentation.

### Idea 3. Cross-sensor open-vocabulary mapping
- **Limit**: Open-vocabulary mapping is mostly RGB-D/camera-centric.
- **Problem**: Fuse LiDAR, thermal, radar, and RGB for open-vocabulary 3D maps.
- **Why / Method**: Non-RGB sensors lack language supervision but add robust geometry. Align them through shared 3D anchors and RGB-derived pseudo-labels.
- **Eval**: SemanticKITTI, nuScenes, thermal/RGB-D datasets, outdoor robot maps; metrics: mIoU, open-vocab AP, robustness under lighting/weather.
- **Refs**: Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection; ThermalGaussian: Thermal 3D Gaussian Splatting; LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments; LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping; OpenScene: 3D Scene Understanding with Open Vocabularies.

## Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception

### Idea 1. Asynchronous fusion with learned temporal alignment
- **Limit**: Multi-sensor perception assumes synchronized sensors, but real robots have latency and rolling shutter.
- **Problem**: Fuse camera, LiDAR, radar, and IMU under asynchronous timestamps.
- **Why / Method**: Naive feature fusion creates ghost objects. Learn temporal flow alignment and per-sensor time-offset uncertainty.
- **Eval**: nuScenes, Waymo, Argoverse, real asynchronous sensor logs; metrics: 3D mAP/NDS, scene flow EPE, occupancy IoU, latency robustness.
- **Refs**: BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation; FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry; V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection; Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation; Rethinking Temporal Fusion with a Unified Gradient Descent View for 3D Semantic Occupancy Prediction.

### Idea 2. Occupancy prediction with semantic risk for planning
- **Limit**: Occupancy prediction treats all occupied cells similarly.
- **Problem**: Predict semantic occupancy plus risk for planning-critical objects and uncertain regions.
- **Why / Method**: A small pedestrian and a wall both occupy space but imply different planning risk. Add semantic risk calibration and future occupancy forecasting.
- **Eval**: nuScenes occupancy, Waymo occupancy, nuPlan; metrics: occupancy IoU, semantic mIoU, collision risk, planning score.
- **Refs**: RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction; Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction; QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction; ODG: Occupancy Prediction Using Dual Gaussians; BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers; Planning-oriented Autonomous Driving.

### Idea 3. Generative sensor simulation for robust 3D perception
- **Limit**: Sensor simulation often lacks realism for rare weather, lighting, and failure modes.
- **Problem**: Generate realistic LiDAR/radar/camera observations from 3D scene representations.
- **Why / Method**: Rule-based simulation misses sensor artifacts. Use Gaussian/neural scene representations with learned noise and material models.
- **Eval**: nuScenes/Waymo sim-to-real, sensor dropout benchmarks; metrics: perception transfer gap, FID-like sensor statistics, mAP/NDS under simulation training.
- **Refs**: SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving; SimULi: Real-Time LiDAR and Camera Simulation with Unscented Transforms; GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting; Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding; RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes.

## Sensor Fusion, LiDAR, and Autonomous Driving

### Idea 1. Robust calibration monitoring for autonomous perception
- **Limit**: Small calibration drift degrades sensor fusion and is hard to detect online.
- **Problem**: Monitor and correct extrinsic calibration drift using scene geometry.
- **Why / Method**: Offline calibration cannot cover vibration, temperature, and sensor motion. Use online geometric residuals and learned drift priors.
- **Eval**: KITTI, nuScenes, Waymo, custom calibration perturbations; metrics: calibration error, mAP/NDS recovery, drift detection delay.
- **Refs**: Robust LiDAR-Camera Calibration with 2D Gaussian Splatting; TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving; FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry; GeoCalib: Learning Single-image Calibration with Geometric Optimization; BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation.

### Idea 2. Language-guided sensor fusion diagnostics
- **Limit**: Fusion systems fail silently; engineers inspect logs manually.
- **Problem**: Generate language explanations for sensor disagreement and likely failure causes.
- **Why / Method**: Numeric confidence does not reveal whether LiDAR, camera, or calibration failed. Compare modality-specific predictions and summarize discrepancies.
- **Eval**: nuScenes/Waymo with injected calibration/dropout/weather faults; metrics: fault detection AUROC, explanation accuracy, mAP under correction.
- **Refs**: BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation; How Do Images Align and Complement LiDAR? Towards a Harmonized Multi-modal 3D Panoptic Segmentation; FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry; VLR-Driver: Large Vision-Language-Reasoning Models for Embodied Autonomous Driving; ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation.

### Idea 3. 3D driving world model with uncertainty-aware rendering
- **Limit**: Driving world models render plausible futures but may ignore 3D physical constraints.
- **Problem**: Predict future 3D scene states with geometry and sensor uncertainty.
- **Why / Method**: Video-only prediction misses metric occupancy and collision risk. Use a 3D latent world model with differentiable rendering to camera/LiDAR.
- **Eval**: nuScenes, Waymo, OpenScene driving, nuPlan; metrics: future occupancy IoU, motion ADE/FDE, planning collision rate, rendering metrics.
- **Refs**: Planning-oriented Autonomous Driving; WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving; Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling; Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving; ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation.

## Vision-Language-Action and Robot Manipulation

### Idea 1. Self-correcting VLA through 3D execution monitors
- **Limit**: VLA models often fail without recognizing the failure.
- **Problem**: Monitor execution using 3D state differences and trigger replanning.
- **Why / Method**: Language/image feedback can miss small pose errors. Compare expected and observed 3D object states, contact, and affordance satisfaction.
- **Eval**: RLBench, CALVIN, LIBERO, real robot failure recovery; metrics: recovery success, failure detection AUROC, intervention count, final task success.
- **Refs**: AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation; TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation; VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning Via Online Monte Carlo Tree Search; SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning; Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics.

### Idea 2. Geometry-gated action tokenization
- **Limit**: Action tokenizers are usually learned from trajectories without explicit geometric grounding.
- **Problem**: Tokenize actions according to object geometry, contact, and affordance regions.
- **Why / Method**: Same action vector has different meaning near different object parts. Use local object frames and contact surfaces to define action tokens.
- **Eval**: RLBench, LIBERO, BridgeData, real grasping; metrics: success, generalization to unseen objects, token efficiency, contact error.
- **Refs**: VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers; CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance; BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models; SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation; RoboGround: Robotic Manipulation with Grounded Vision-Language Priors; DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo.

### Idea 3. 3D memory-augmented VLA for long-horizon manipulation
- **Limit**: VLA models often map current observations to actions with weak persistent 3D memory.
- **Problem**: Use a persistent object-centric 3D memory to support long-horizon tasks with hidden objects and rearrangement.
- **Why / Method**: Current image tokens forget occluded objects and previous subgoals. Add memory slots for objects, poses, affordances, and task state.
- **Eval**: LIBERO-long, CALVIN, RLBench, VLABench, real tabletop/mobile manipulation; metrics: task success, subgoal completion, memory query accuracy.
- **Refs**: OpenVLA: An Open-Source Vision-Language-Action Model; Octo: An Open-Source Generalist Robot Policy; MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation; Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation; VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks; MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning; ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation.
