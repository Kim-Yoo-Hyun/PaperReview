# Details Matter for Indoor Open-vocabulary 3D Instance Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, ours has unique features to improve the limitations of existing works.를 문제로 두고, Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions and applying robust 3D tracking for aggregation. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Unlike closed-vocabulary 3D instance segmentation that is often trained end-to-end, open-vocabulary 3D instance segmentation (OV-3DIS) often leverages vision-language models (VLMs) to generate 3D instance proposals ...
- **p. 1 / Abstract - extractive body cue:** While various concepts have been proposed from existing research, we observe that these individual concepts are not mutually exclusive but complementary.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a new state-of-the-art solution for OV-3DIS by carefully designing a recipe to combine the concepts together and refining them to ...
- **p. 1 / Abstract - extractive body cue:** Our solution follows the two-stage scheme: 3D proposal generation and instance classification.
- **p. 1 / Abstract - extractive body cue:** We employ robust 3D tracking-based proposal aggregation to generate 3D proposals and remove overlapped or partial proposals by iterative merging/removal.
- **p. 2 / 1. Introduction - extractive body cue:** However, ours has unique features to improve the limitations of existing works.
- **p. 1 / 1. Introduction - extractive body cue:** This paper carefully combines the concepts and refines each step to address key challenges, achieving state-of-theart (SoTA) performance in existing benchmarks.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions and ...
- **p. 1 / 1. Introduction - extractive body cue:** Examples of open-vocabulary predictions from our method in the ScanNet200 dataset [7].
- **p. 1 / 1. Introduction - extractive body cue:** Our method effectively retrieves instances based on functional descriptions (e.g., drink water, heat mac & cheese) and object attributes (e.g., red chair). dicted proposals into ...
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** With refinement, irrelevant 3D superpoints are removed, and our method successfully removes 3D superpoints that do not belong to the object, resulting in geometrically consistent ...
- **p. 3 / 3.1. Image-based Proposal Generation - extractive body cue:** Leveraging VFMs [28, 35, 43], image-based proposals provide a complementary approach for detecting novel classes not covered during the training of the 3D instance segmentation ...
- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset of images with ...
- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** Alpha-CLIP incorporates object masks as an additional input to guide the model's attention.
- **p. 3 / 3. Method - extractive body cue:** For point cloudbased 3D proposals, we utilize pre-trained 3D instance segmentation models [38, 45] and discard the class predictions, retaining only the class-agnostic masks.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset of images with the highest visibility for multiscale visual feature ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3.2. Open-Vocabulary Instance Classification), p. 4 (3.1. Image-based Proposal Generation) |
| State/latent | Given, proposal, visual, encoder, Alpha-CLIP, project, onto, images, select, subset, highest, visibility | geometry, map, object/relationship state | p. 5 (3.2. Open-Vocabulary Instance Classification), p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation) |
| Output/action | Matching tracklets with a new observation. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation), p. 5 (3.2. Open-Vocabulary Instance Classification) |
| Objective/outcome | Using this ratio, we construct an inclusion cost matrix Cincl ∈[0, 1]K×K, which is a full matrix since the inclusion ratio is asymmetric. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.1. Image-based Proposal Generation), p. 5 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions and ...
- **p. 1 / 1. Introduction - extractive body cue:** Examples of open-vocabulary predictions from our method in the ScanNet200 dataset [7].
- **p. 1 / 1. Introduction - extractive body cue:** Our method effectively retrieves instances based on functional descriptions (e.g., drink water, heat mac & cheese) and object attributes (e.g., red chair). dicted proposals into ...
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** With refinement, irrelevant 3D superpoints are removed, and our method successfully removes 3D superpoints that do not belong to the object, resulting in geometrically consistent ...
- **p. 3 / 3.1. Image-based Proposal Generation - extractive body cue:** Leveraging VFMs [28, 35, 43], image-based proposals provide a complementary approach for detecting novel classes not covered during the training of the 3D instance segmentation ...
- **p. 7 / 4.3. Qualitative Results - extractive body cue:** These visual results are consistent with the recall metrics: Open3DIS and OpenYOLO3D achieve the mAR of 43.3% and 47.7%, respectively, whereas our method significantly outperforms ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. OV-3DIS results on the ScanNet200 validation set [7]. Top-1 evaluation protocol refers to assigning one predicted class per instance mask, and Top-K evaluation ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** As shown, using Alpha-CLIP improves the performance from 27.5 to 30.5 mAP, proving the importance of considering object-centric representation in instance classification.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Qualitative Results), p. 6 (Figure/Table caption) |
| Embodiment/environment | Replica is a synthetic dataset created from digital replicas of real-world scenes, featuring 48 object classes across 8 different scenes. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | Qualitative comparisons on the ScanNet200 dataset. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Results), p. 7 (4.2. Quantitative Results) |
| Metric | We measure mean average precision (mAP) and mean average recall (mAR) at IOU thresholds of 25% and 50%. | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Results) |
| Baseline/ablation | As reported in Table 2, our method consistently outperforms the baselines by a large margin in each experiment setting: 2D-only, 3D-only, and 2D+3D. | fair input/data/compute/action matching | p. 7 (4.2. Quantitative Results), p. 7 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Improving such limitations remains our future work.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Failure cases of using CLIP for instance classification. CLIP fails when the shape of the object gets distorted or when other objects are ...
- **p. 8 / 5. Conclusion - extractive body cue:** Also, we found that our method fails to improve performance on small objects (e.g., ScanNet++ in the supplementary) but rather remain similar to existing approaches.
- **p. 7 / 4.2. Quantitative Results - extractive body cue:** However, it lags behind OpenYOLO3D [2] in terms of mAP, which does not use CLIP for instance classification.
- **p. 7 / 4.2. Quantitative Results - extractive body cue:** We hypothesize that the domain gap between real-world data and synthetic data from Replica may degrade the performance of Alpha-CLIP.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, ours has unique features to improve the limitations of existing works.를 문제로 두고, Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions and applying robust 3D tracking for aggregation. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.2. Open-Vocabulary Instance Classification), p. 3 (3.1. Image-based Proposal Generation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
