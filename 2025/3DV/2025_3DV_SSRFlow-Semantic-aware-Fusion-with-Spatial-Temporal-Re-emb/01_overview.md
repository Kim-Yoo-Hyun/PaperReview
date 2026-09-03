# SSRFlow: Semantic-aware Fusion with Spatial Temporal Re-embedding for Real-world Scene Flow

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=9abfUtE6iQ&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=9abfUtE6iQ&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames and further matches the all-to-all point-pairs globally ...를 문제로 두고, Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames and further matches the all-to-all point-pairs globally ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Scene flow, which provides the 3D motion field of the first frame from two consecutive point clouds, is vital for dynamic scene perception.
- **p. 1 / Abstract - extractive body cue:** However, contemporary scene flow methods face three major challenges.
- **p. 1 / Abstract - extractive body cue:** Firstly, they lack global flow embedding or only consider the context of individual point clouds before embedding, leading to embedded points struggling to perceive the ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we propose a novel approach called Dual Cross Attentive (DCA) for the latent fusion and alignment between two frames based on ...
- **p. 1 / Abstract - extractive body cue:** This is then integrated into Global Fusion Flow Embedding (GF) to initialize flow embedding based on global correlations in both contextual and Euclidean spaces.
- **p. 2 / 1 Introduction - extractive body cue:** Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames ...
- **p. 2 / 1 Introduction - extractive body cue:** Furthermore, as a point-level task, obtaining the ground truth (GT) of scene flow from real-world point clouds is difficultMenze et al.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames ...
- **p. 2 / 1 Introduction - extractive body cue:** (2023), we introduce the Dual Cross Attentive (DCA) Fusion to merge the semantic contexts of point clouds from two frames in latent space, which allows ...
- **p. 3 / 2 Methodology - extractive body cue:** 2.3 Global Fusion Flow Embedding The GF module is designed to capture the global relation between consecutive frames during the flow initialization.
- **p. 4 / 2 Methodology - extractive body cue:** The obtained coarse dense flow is directly accumulated onto the source frame Sl to generate the warped source frame WSl = {wsi}Nl i=1 = {wxi ...
- **p. 3 / 2 Methodology - extractive body cue:** (2019) as the feature extraction backbone to build a pyramid network.
- **p. 3 / 2 Methodology - extractive body cue:** 2.2 Hierarchical Feature Extraction The overview of our proposed network is shown in Figure 1.
- **p. 4 / 2 Methodology - extractive body cue:** During the dual cross-attentive fusion phase, the semantic context in the latent feature space is obtained for S∗and T ∗through linear networks Q K and ...
- **p. 6 / 2 Methodology - extractive body cue:** Cross-frame Feature Similarity (CFS) Loss The semantic features of the points in the warped source frame are similar to those in the surrounding target frame, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2.2 Hierarchical Feature Extraction The overview of our proposed network is shown in Figure 1. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (2 Methodology), p. 2 (1 Introduction) |
| State/latent | Hierarchical, Feature, Extraction, overview, network, Figure, rely, stereo, RGB-D, images, input, backbone | geometry, map, object/relationship state | p. 3 (2 Methodology), p. 2 (1 Introduction), p. 3 (2 Methodology) |
| Output/action | (2008) rely on stereo or RGB-D images as input. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 3 (2 Methodology), p. 4 (2 Methodology) |
| Objective/outcome | 3 Training Losses 3.1 Hierarchical Supervised Loss A supervised loss is directly hooked to the GT of scene flow, and we leverage multi-level loss functions as supervision to optimize the model across ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (2 Methodology), p. 6 (2 Methodology), p. 5 (2 Methodology) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames ...
- **p. 2 / 1 Introduction - extractive body cue:** (2023), we introduce the Dual Cross Attentive (DCA) Fusion to merge the semantic contexts of point clouds from two frames in latent space, which allows ...
- **p. 3 / 2 Methodology - extractive body cue:** 2.3 Global Fusion Flow Embedding The GF module is designed to capture the global relation between consecutive frames during the flow initialization.
- **p. 4 / 2 Methodology - extractive body cue:** The obtained coarse dense flow is directly accumulated onto the source frame Sl to generate the warped source frame WSl = {wsi}Nl i=1 = {wxi ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Illustration of results on other datasets of our proposed SSRFlow method. Colors mean the same as Figure 5. More visualization results are exhibited ...
- **p. 8 / 4 Experiments - extractive body cue:** The quantitative results presented in Table 1 indicate that SSRFlow outperforms the other methods by a large margin, especially in real-world datasets.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Illustration of the proposed network. Firstly, semantic features are hierarchically extracted and sent to GF to achieve global embedding between the two point ...
- **p. 7 / 4 Experiments - extractive body cue:** The best results for each dataset are marked in bold. * denotes the methods with an inference time exceeding 250 ms.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 8 (4 Experiments) |
| Embodiment/environment | (a) FT3Ds (b) KITTIs (c) SF-KITTI (d) LiDAR-KITTI Figure 4: Comparisons of scene flow datasets, including (a) synthetic stereo, (b) real-world stereo, and (c)(d) real-world LiDAR-scanned. | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Dataset/benchmark | The quantitative results presented in Table 1 indicate that SSRFlow outperforms the other methods by a large margin, especially in real-world datasets. | role, split, size and leakage | p. 7 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Metric | After removing the DCA Fusion, the model experienced a substantial decline in accuracy, primarily due to its capability to fuse point features with another frame context before embedding. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 14 (Figure/Table caption), p. 7 (4 Experiments) |
| Baseline/ablation | Figure 6: Illustration of results on other datasets of our proposed SSRFlow method. Colors mean the same as Figure 5. More visualization results are exhibited in Appendix, Sec F FT3Do and KITTIo ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 2 Methodology - extractive body cue:** The KNN+Radius search strategy effectively mitigates the influence of noise points resulting from occlusion and sparsity in point clouds, as demonstrated in Sec B.2 of ...
- **p. 8 / 4 Experiments - extractive body cue:** The experimental results are listed in Table 3, which reveal the good performance of our model even with occlusion.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 10: Ablation studies and analysis of adaption losses. From Figure 9 it can be observed that using only KNN introduces noise points that do ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 11: (a) The occlusion occurs between the source frame and the target frame. In this scenario, red bounding boxes delineate points in the source ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames and further matches the all-to-all point-pairs globally ...를 문제로 두고, Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames and further matches the all-to-all point-pairs globally ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (2 Methodology), p. 3 (2 Methodology), p. 4 (2 Methodology), p. 6 (2 Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
