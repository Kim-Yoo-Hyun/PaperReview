# OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, semantic mapping, open-vocabulary
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these approaches are predominantly offline and lack support for online instance-level panoptic perception, hindering their applications in embodied tasks.를 문제로 두고, Overall, the technical contributions of our approach are summarized as follows: • We propose an online open-vocabulary panoptic mapping framework that unifies geometric reconstruction and semantic understanding in a local-to-global para ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary scene understanding with online panoptic mapping is essential for embodied applications to perceive and interact with environments.
- **p. 1 / Abstract - extractive body cue:** However, existing methods are predominantly offline or lack instance-level understanding, limiting their applicability to real-world robotic tasks.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose OnlinePG, a novel and effective system that integrates geometric reconstruction and open-vocabulary perception using 3D Gaussian Splatting in an online ...
- **p. 1 / Abstract - extractive body cue:** Technically, to achieve online panoptic mapping, we employ an efficient local-to-global paradigm with a sliding window.
- **p. 1 / Abstract - extractive body cue:** To build local consistency map, we construct a 3D segment clustering graph that jointly leverages geometric and semantic cues, fusing inconsistent segments within sliding window ...
- **p. 1 / 1. Introduction - extractive body cue:** However, these approaches are predominantly offline and lack support for online instance-level panoptic perception, hindering their applications in embodied tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Current online open-vocabulary scene understanding approaches [42, 52] cannot distinguish individual 3D instances based on text queries, while offline instanceaware approaches [19, 39, 50, 58] ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Overall, the technical contributions of our approach are summarized as follows: • We propose an online open-vocabulary panoptic mapping framework that unifies geometric reconstruction and ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we present OnlinePG, an efficient online open-vocabulary panoptic mapping system based on 3D Gaussian Splatting that integrates geometric reconstruction with semantic understanding.
- **p. 3 / 3. Method - extractive body cue:** To mitigate the inconsistencies of 2D segmentation results, we propose an effective segment clustering algorithm that synergistically leverages geometric and semantic cues to obtain consistent ...
- **p. 3 / 3.2. Local Consistent Map Construction - extractive body cue:** For i-th keyframe inside the sliding window W, we use LSeg [17] and EntitySeg [21] to extract its 2D feature map fi ∈RH×W ×Df and ...
- **p. 4 / 3.2. Local Consistent Map Construction - extractive body cue:** The semantic cue is then computed as the cosine similarity between language features: X(Si, Sj) = zi · zj/(//zi// · //zj//).
- **p. 4 / 3.2. Local Consistent Map Construction - extractive body cue:** Through this multi-cue graph clustering algorithm, we obtain geometrically and semantically consistent 3D Gaussian instances I from the local sliding window.
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive body cue:** For each voxel v occupied by a clustered instance I, we update the global feature grid Ft g and confidence grid Ct g using weighted ...
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive body cue:** construct a forward correspondence score matrix Ml→g ∈ Rnl×ng: Ml→g = zl · zg //zl// · //zg// + /Il ∩Ig/ Cont.(Il, Ig), (10) where nl ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For each voxel v occupied by instance Ii, we assign the local instance label and weight grids: T t l (v) = IDi, Kt l(v) = Ni, (8) where t denotes the ... | camera/depth stream, pose, map와 language goal | p. 4 (3.2. Local Consistent Map Construction), p. 1 (1. Introduction) |
| State/latent | voxel, occupied, instance, assign, local, label, weight, grids, IDi, where, denotes, time | robot pose, free-space/semantic map와 local goal | p. 4 (3.2. Local Consistent Map Construction), p. 1 (1. Introduction), p. 3 (3.2. Local Consistent Map Construction) |
| Output/action | Open-vocabulary 3D scene understanding is fundamental for embodied tasks, enabling robots to perceive, reason about, and interact with complex environments using natural language and instruction [9, 31, 33, 38]. | collision-free trajectory 또는 velocity command | p. 1 (1. Introduction), p. 3 (3.2. Local Consistent Map Construction), p. 4 (3.2. Local Consistent Map Construction) |
| Objective/outcome | Following previous works [11, 23], we adopt the L1 loss terms for appearance and geometry optimization: L = α · Lc + (1 -α) · Ld, (2) where α is the weight ... | goal reach, safety, localization error와 replanning latency | p. 3 (3.1. Scene Representation), p. 5 (3.3. Local-to-Global Map Fusion), p. 3 (3.1. Scene Representation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Overall, the technical contributions of our approach are summarized as follows: • We propose an online open-vocabulary panoptic mapping framework that unifies geometric reconstruction and ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we present OnlinePG, an efficient online open-vocabulary panoptic mapping system based on 3D Gaussian Splatting that integrates geometric reconstruction with semantic understanding.
- **p. 3 / 3. Method - extractive body cue:** To mitigate the inconsistencies of 2D segmentation results, we propose an effective segment clustering algorithm that synergistically leverages geometric and semantic cues to obtain consistent ...
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** Compared to single-cue clustering, multi-cue clustering achieves 8 to 18 PRQ improvement with only ∼40 33275
- **p. 6 / 4.2. Main Experiments - extractive body cue:** 1, our method achieves the best 3D semantic segmentation results among online approaches on the mIoU and mAcc metrics of two datasets.
- **p. 6 / 4.2. Main Experiments - extractive body cue:** Compared to O2V-Mapping [42] and OnlineAnySeg [41], by maintaining and updating voxellevel spatial language feature grid F, we can achieve more fine-grained 3D scene understanding ...
- **p. 7 / 4.2. Main Experiments - extractive body cue:** Our method can achieve more consistent segmentation results among online approaches.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Comparing #2 and #3, we can know that our spatial attribute module can improve the open-vocabulary scene understanding performance of our system.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.3. Ablation Studies), p. 6 (4.2. Main Experiments) |
| Embodiment/environment | Following [50, 58], we take the commonly-used 8 scenes {room0-2,office0-4} for Replica dataset. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings) |
| Dataset/benchmark | For Scene0645 in the ScanNetV2 dataset, our method takes an average of 410 ms to perform rendering optimization for 5 keyframes with 20 iterations, 350 ms for clustering the 12 keyframes in ... | role, split, size and leakage | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), p. 7 (4.2. Main Experiments), p. 6 (4.1. Experimental Settings) |
| Metric | 2, we show the performance of different matching strategies for fusing local map from the sliding window into global map. #1 represents using the basic nearest neighbor matching algorithm based on the ... | definition, denominator, direction and uncertainty | p. 8 (4.3. Ablation Studies), p. 5 (4.1. Experimental Settings), p. 8 (4.3. Ablation Studies) |
| Baseline/ablation | Figure 3. Qualitative 3D Semantic Segmentation Comparison of ScanNetV2 Dataset. Our approach outperforms recent online ap- proaches, O2V-Mapping [42] and OnlineAnySeg [41], by a large margin. Compared with the offline SOTA PanoGS ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 7 (4.2. Main Experiments), p. 7 (4.2. Main Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Limitations: (1) Our method currently cannot reconstruct dynamic objects.
- **p. 8 / 5. Conclusion - extractive body cue:** Our future work will explore feed-forward approaches [20, 46, 47] that eliminate these requirements for fully pose-free and depth-free openvocabulary reconstruction.
- **p. 5 / 4.1. Experimental Settings - extractive body cue:** Since the baselines [31, 33, 50] marked with ∗ cannot obtain 3D panoptic results, we use the performance reported in [58], which uses a supervised ...
- **p. 7 / 4.2. Main Experiments - extractive body cue:** While OnlineAnySeg can handle simple queries (e.g., "television"), it fails on some fine-grained and multi-instance queries (e.g., "pillow", "toilet paper", "bag") due to inaccurate 3D ...
- **p. 7 / 4.2. Main Experiments - extractive body cue:** Since some offline baselines (LangSplat [33], OpenGaussian [50], OpenScene [31]) marked with ∗cannot inherently output 3D instances, PanoGS [58] provides supervised instance annotations [44] for ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of OnlinePG, which integrates geometric reconstruction and open-vocabulary panoptic perception built upon 3D Gaussian Splatting. Given the posed video stream and 2D ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these approaches are predominantly offline and lack support for online instance-level panoptic perception, hindering their applications in embodied tasks.를 문제로 두고, Overall, the technical contributions of our approach are summarized as follows: • We propose an online open-vocabulary panoptic mapping framework that unifies geometric reconstruction and semantic understanding in a local-to-global para ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Local Consistent Map Construction), p. 3 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
