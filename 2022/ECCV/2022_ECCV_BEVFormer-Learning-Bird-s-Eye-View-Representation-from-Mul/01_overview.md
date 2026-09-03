# BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2203.17270.
> PDF retrieval source: https://arxiv.org/pdf/2203.17270. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: sensor fusion, 3D perception, Planning
- Official paper: https://arxiv.org/abs/2203.17270
- Full-text retrieval: https://arxiv.org/pdf/2203.17270
- Code/Project: https://github.com/fundamentalvision/BEVFormer
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the existing state-of-the-art multi-camera 3D detection methods rarely exploit temporal information.를 문제로 두고, Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D visual perception tasks, including 3D detection and map segmentation based on multi-camera images, are essential for autonomous driving systems.
- **p. 1 / Abstract - extractive body cue:** In this work, we present a new framework termed BEVFormer, which learns unified BEV representations with spatiotemporal transformers to support multiple autonomous driving perception tasks.
- **p. 1 / Abstract - extractive body cue:** In a nutshell, BEVFormer exploits both spatial and temporal information by interacting with spatial and temporal space through predefined grid-shaped BEV queries.
- **p. 1 / Abstract - extractive body cue:** To aggregate spatial information, we design spatial cross-attention that each BEV query extracts the spatial features from the regions of interest across camera views.
- **p. 1 / Abstract - extractive body cue:** For temporal information, we propose temporal selfattention to recurrently fuse the history BEV information.
- **p. 2 / 1 Introduction - extractive body cue:** However, the existing state-of-the-art multi-camera 3D detection methods rarely exploit temporal information.
- **p. 2 / 1 Introduction - extractive body cue:** The downside of this framework is that it processes different views separately and cannot capture information across cameras, leading to low performance and efficiency [32, ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations.
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a transformer-based bird's-eye-view (BEV) encoder, termed BEVFormer, which can effectively aggregate spatiotemporal features from multi-view cameras and history BEV features.
- **p. 3 / 1 Introduction - extractive body cue:** • We designed learnable BEV queries along with a spatial cross-attention layer and a temporal self-attention layer to lookup spatial features from cross cameras and ...
- **p. 16 / A.3 Task Heads - extractive body cue:** Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference.
- **p. 16 / A.3 Task Heads - extractive body cue:** Map Query BEV Feature 𝐵𝑡 Mask Result Multi-Head Attention Add & Norm Feed Forward Refined Query Add & Norm Query Next Layer Attention Maps Figure ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | main, contributions, follows, BEVFormer, spatiotemporal, transformer, encoder, projects, multi-camera, and/or, timestamp, input | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | For the human visual perception system, temporal information plays a crucial role in inferring the motion state of objects and identifying occluded objects, and many works in vision fields have demonstrated the ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | Only L1 loss and L1 cost are used during training phase. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 16 (A.3 Task Heads), p. 16 (A.4 Spatial Cross-Attention) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations.
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a transformer-based bird's-eye-view (BEV) encoder, termed BEVFormer, which can effectively aggregate spatiotemporal features from multi-view cameras and history BEV features.
- **p. 3 / 1 Introduction - extractive body cue:** • We designed learnable BEV queries along with a spatial cross-attention layer and a temporal self-attention layer to lookup spatial features from cross cameras and ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 3: The detection results of subsets with different visibilities. We divide the nuScenes val set into four subsets based on the visibility that {0-40%, ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 4: Visualization results of BEVFormer on nuScenes val set. We show the 3D bboxes predictions in multi-camera images and the bird's-eye-view. predicted boxes is ...
- **p. 7 / 4 Experiments - extractive body cue:** On the test set, our model achieves 56.9% NDS without bells and whistles, 9.0 points 7
- **p. 7 / 4 Experiments - extractive body cue:** Our method outperforms previous best method DETR3D [47] over 9.2 points on val set (51.7% NDS vs.
- **p. 11 / Figure/Table caption - extractive body cue:** Tab. 6. We ablate the scales of BEVFormer in three aspects, including whether to use multi-scale view features, the shape of BEV queries, and the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 11 (Figure/Table caption) |
| Embodiment/environment | The nuScenes dataset [4] contains 1000 scenes of roughly 20s duration each, and the key samples are annotated at 2Hz. | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | 0.517 0.511 0.494 0.471 0.443 0.508 0.505 0.494 0.479 0.463 0.448 0.442 0.424 0.402 0.380 0.404 0.400 0.397 0.392 0.388 0.423 0.414 0.395 0.373 0.350 0.350 0.400 0.450 0.500 0.550 0 1 ... | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 17 (A.4 Spatial Cross-Attention), p. 16 (A.2 VPN and Lift-Splat) |
| Metric | The mean average precision (mAP) of nuScenes is computed using the center distance on the ground plane rather than the 3D Intersection over Union (IoU) to match the predicted results and ground ... | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 10 (Figure/Table caption), p. 7 (4 Experiments) |
| Baseline/ablation | Our method outperforms previous best method DETR3D [47] over 9.2 points on val set (51.7% NDS vs. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 10 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: 3D detection results on nuScenes test set. ∗notes that VoVNet-99 (V2-99) [21] was pre-trained on the depth estimation task with extra data [31]. ...
- **p. 9 / C R101 - extractive body cue:** However, the jointly trained model does not perform as well as individually trained models for road and lane segmentation, which is a common phenomenon called ...
- **p. 10 / C R101 - extractive body cue:** Temporal information does not work to benefit an object's scale prediction. attention significantly outperforms other attention mechanisms under a comparable model scale.
- **p. 16 / A.4 Spatial Cross-Attention - extractive body cue:** The most straightforward way to employ global attention is making each BEV query interact with all multi-camera features, and this conceptual implementation does not require ...
- **p. 10 / C R101 - extractive body cue:** To evaluate the performance of BEVFormer on objects with different occlusion levels, we divide the validation set of nuScenes into four subsets according to the ...
- **p. 16 / A.4 Spatial Cross-Attention - extractive body cue:** Notably, compared to other attention mechanisms that rely on precise camera intrinsic and extrinsic, global attention is more robust to camera calibration.
- **p. 17 / A.4 Spatial Cross-Attention - extractive body cue:** 0.517 0.511 0.494 0.471 0.443 0.508 0.505 0.494 0.479 0.463 0.448 0.442 0.424 0.402 0.380 0.404 0.400 0.397 0.392 0.388 0.423 0.414 0.395 0.373 0.350 ...

## Why Read It

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the existing state-of-the-art multi-camera 3D detection methods rarely exploit temporal information.를 문제로 두고, Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 16 (A.3 Task Heads), p. 16 (A.3 Task Heads), p. 10 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
