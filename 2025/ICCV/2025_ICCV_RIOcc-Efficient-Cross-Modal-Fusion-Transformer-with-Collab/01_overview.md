# RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fan_RIOcc_Efficient_Cross-Modal_Fusion_Transformer_with_Collaborative_Feature_Refinement_for_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fan_RIOcc_Efficient_Cross-Modal_Fusion_Transformer_with_Collaborative_Feature_Refinement_for_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Fan_RIOcc_Efficient_Cross-Modal_Fusion_Transformer_with_Collaborative_Feature_Refinement_for_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Fan_RIOcc_Efficient_Cross-Modal_Fusion_Transformer_with_Collaborative_Feature_Refinement_for_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the task of semantic occupancy prediction [2, 9, 10, 12, 39, 40, 49] also faces significant computational challenges, especially when it involves real-time processing of large-scale voxel data, which demands high ...를 문제로 두고, Our contributions are summarized as follows: • We propose a novel multi-modal 3D semantic occupancy prediction framework, RIOcc.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The multi-modal 3D semantic occupancy task provides a comprehensive understanding of the scene and has received considerable attention in the field of autonomous driving.
- **p. 1 / Abstract - extractive body cue:** However, existing methods mainly focus on processing large-scale voxels, which bring high computational costs and degrade details.
- **p. 1 / Abstract - extractive body cue:** Additionally, they struggle to accurately capture occluded targets and distant information.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a novel LiDAR-Camera 3D semantic occupancy prediction framework called RIOcc, with collaborative feature refinement and multi-scale cross-modal fusion transformer.
- **p. 1 / Abstract - extractive body cue:** Specifically, RIOcc encodes multi-modal data into a unified Bird's Eye View (BEV) space, which reduces computational complexity and enhances the efficiency of feature alignment.
- **p. 2 / C Vox - extractive body cue:** However, the task of semantic occupancy prediction [2, 9, 10, 12, 39, 40, 49] also faces significant computational challenges, especially when it involves real-time processing ...
- **p. 1 / C Vox - extractive body cue:** In various 3D perception tasks, effectively combining data from cameras and LiDAR presents a crucial challenge for achieving high-precision predictions.

## Core Idea

- **p. 2 / C Vox - extractive body cue:** Our contributions are summarized as follows: • We propose a novel multi-modal 3D semantic occupancy prediction framework, RIOcc.
- **p. 2 / C Vox - extractive body cue:** To address the aforementioned issues, we propose RIOcc, a novel multi-modal 3D semantic occupancy prediction method.
- **p. 4 / 3.4.2. Semantic Encoder - extractive body cue:** To enhance the semantic expressiveness of the BEV features, we propose a lightweight 2D Semantic Encoder for efficiently extracting rich semantic information.
- **p. 5 / 3.6. Occupancy Prediction Module - extractive body cue:** In our framework, the BEV features obtain from the multiscale fusion stage are input into the occupancy prediction module.
- **p. 5 / 3.4.2. Semantic Encoder - extractive body cue:** Additionally, we introduce an Auxiliary Semantic Loss at the output stage to enhance the semantic consistency of the features and improve the model's understanding of ...
- **p. 4 / 3.3. Dual-branch Pooling - extractive body cue:** Then, the features are passed through the Channel-wise Attention and Grid-wise Attention modules, optimizing information representation across different dimensions.
- **p. 6 / 3.7. Loss - extractive body cue:** Additionally, we introduce an Auxiliary Semantic Loss Laux to optimize the refined semantic features extracted by the semantic encoder.
- **p. 3 / 3.1. Overall Architecture - extractive body cue:** Then, we design the Deformable Dual-Attention (DDA) to strengthen the interaction of BEV features at different scales between modalities (Sec 3.5).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | During the feature extraction stage, we design LiDAR and camera branches to encode multi-modal input, following the BEVFusion [25] setup. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.2. Features Extraction), p. 4 (3.3. Dual-branch Pooling) |
| State/latent | During, feature, extraction, stage, design, LiDAR, camera, branches, encode, multi-modal, input, following | geometry, map, object/relationship state | p. 3 (3.2. Features Extraction), p. 4 (3.3. Dual-branch Pooling), p. 3 (3.1. Overall Architecture) |
| Output/action | The output from the Channel-wise Attention are given by: F_{cha n n el}= \sigma \le ft (M L P\left (F_{A v g}\right )+M L P\left (F_{M a x}\right )\right ) (1) To ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.3. Dual-branch Pooling), p. 3 (3.1. Overall Architecture), p. 6 (3.7. Loss) |
| Objective/outcome | The cross-entropy loss Lce and Lovasz-Softmax loss Lls are used to optimize the overall framework. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.7. Loss), p. 6 (3.7. Loss), p. 5 (3.4.2. Semantic Encoder) |

## Main Claims and Actual Contribution

- **p. 2 / C Vox - extractive body cue:** Our contributions are summarized as follows: • We propose a novel multi-modal 3D semantic occupancy prediction framework, RIOcc.
- **p. 2 / C Vox - extractive body cue:** To address the aforementioned issues, we propose RIOcc, a novel multi-modal 3D semantic occupancy prediction method.
- **p. 4 / 3.4.2. Semantic Encoder - extractive body cue:** To enhance the semantic expressiveness of the BEV features, we propose a lightweight 2D Semantic Encoder for efficiently extracting rich semantic information.
- **p. 5 / 3.6. Occupancy Prediction Module - extractive body cue:** In our framework, the BEV features obtain from the multiscale fusion stage are input into the occupancy prediction module.
- **p. 5 / 3.4.2. Semantic Encoder - extractive body cue:** Additionally, we introduce an Auxiliary Semantic Loss at the output stage to enhance the semantic consistency of the features and improve the model's understanding of ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison between OpenOccupancy and the pro- posed RIOcc. Instead of processing voxel features like OpenOc- cupancy, we choose BEV features to achieve higher ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The overall framework of RIOcc. This framework includes three main branches: LiDAR, Camera, and Interaction Branch. The LiDAR Branch processes LiDAR points through ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. The schema of Dual-branch Pooling (DBP). LiDAR feature representation is improved by adaptively highlighting im- portant semantic channels and significant geometric regions. hance ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Embodiment/environment | Both datasets inherit the data format of nuScenes, containing 700 training scenes and 150 validation scenes, with annotations for 17 categories. | hardware/simulator version and reset protocol | p. 6 (4.1. Dataset and Metrics), p. 6 (4.1. Dataset and Metrics) |
| Dataset/benchmark | For the LiDAR branch, we voxelize 10 LiDAR sweeps and employ a voxel encoder for the nuScenes dataset. | role, split, size and leakage | p. 6 (4.1. Dataset and Metrics), p. 6 (4.1. Dataset and Metrics), p. 7 (4.2. Implementation Details), p. 7 (4.1. Dataset and Metrics) |
| Metric | Figure 4. Detailed structure diagram of the wavelet encoder. The input BEV features undergo DWT and IWT to obtain richer structure and details. noise impact, and decrease computational burden, we de- sign ... | definition, denominator, direction and uncertainty | p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Baseline/ablation | In comparison, the data coverage for Occ3D-nuScenes is [-40 m, 40 m] in the X and Y directions, and [-1 m, 5.4 m] in the Z direction, with 25856 | fair input/data/compute/action matching | p. 6 (4.1. Dataset and Metrics), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Detailed structure diagram of the wavelet encoder. The input BEV features undergo DWT and IWT to obtain richer structure and details. noise impact, ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the task of semantic occupancy prediction [2, 9, 10, 12, 39, 40, 49] also faces significant computational challenges, especially when it involves real-time processing of large-scale voxel data, which demands high ...를 문제로 두고, Our contributions are summarized as follows: • We propose a novel multi-modal 3D semantic occupancy prediction framework, RIOcc.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (C Vox), p. 1 (Abstract), p. 1 (C Vox), p. 4 (3.3. Dual-branch Pooling), p. 4 (3.3. Dual-branch Pooling), p. 4 (3.3. Dual-branch Pooling) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
