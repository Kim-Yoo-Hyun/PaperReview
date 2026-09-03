# Ov3R: Open-Vocabulary Semantic 3D Reconstruction from RGB Videos

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, semantic, alignment, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 As a result, a significant gap between existing SLAM methods and envisioned Spatial AI systems still persists.를 문제로 두고, Our main contributions are as follows: • We present Ov3R, a novel framework that unifies 3R models and open-vocabulary 3D semantic segmentation. • We design CLIP3R, a CLIP-informed 3D reconstruction model that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present Ov3R, a novel framework for open-vocabulary semantic 3D reconstruction from RGB video streams, designed to advance Spatial AI.
- **p. 1 / Abstract - extractive body cue:** The system features two key components: CLIP3R, a CLIP-informed 3D reconstruction module that predicts dense point maps from overlapping clips alongside object-level semantics; and 2D-3D ...
- **p. 1 / Abstract - extractive body cue:** Unlike prior methods, Ov3R incorporates CLIP semantics directly into the reconstruction process, enabling globally consistent geometry and fine-grained semantic alignment.
- **p. 1 / Abstract - extractive body cue:** Our framework achieves state-of-the-art performance in both dense 3D reconstruction and open-vocabulary 3D segmentation.
- **p. 1 / 1. Introduction - extractive body cue:** Spatial AI systems [10] aim to understand both the geometry and semantics of the surrounding environment from images in real-time, enabling an embedded AI agent ...
- **p. 1 / 1. Introduction - extractive body cue:** As a result, a significant gap between existing SLAM methods and envisioned Spatial AI systems still persists.
- **p. 1 / 1. Introduction - extractive body cue:** However, existing approaches largely rely on offline reconThis CVPR paper is the Open Access version, provided by the Computer Vision Foundation.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • We present Ov3R, a novel framework that unifies 3R models and open-vocabulary 3D semantic segmentation. • We design ...
- **p. 3 / 3.1. CLIP3R - extractive body cue:** We introduce CLIP3R, a CLIP-informed 3D reconstruction model that integrates the rich semantic understanding embedded in CLIP features and enables open-vocabulary semantic segmentation as a ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce Ov3R, an open-vocabulary semantic 3D reconstruction framework that processes RGBonly video streams.
- **p. 3 / 3. Method - extractive body cue:** It consists of two main components, highlighted in yellow and blue: (i) a CLIP-informed 3Rbased model (CLIP3R) and (ii) a 2D-3D OVS module.
- **p. 5 / 3.2. 2D-3D OVS - extractive body cue:** To address this limitation, we introduce 2D-3D fused descriptors, obtained as follows.
- **p. 5 / 3.2. 2D-3D OVS - extractive body cue:** Therefore, we introduce a 2D-3D fused descriptor that combines these three complementary feature types extracted from i) CLIP3R, ii) DINO, and iii) a 3D-CLIP encoder ...
- **p. 5 / 3.2. 2D-3D OVS - extractive body cue:** Dscene = Fscene CLIP3R + Fscene cat + softmax(Fscene CLIP3R · Fscene T cat √ d ) · Fscene cat (9) Dinst = Finst CLIP3R+Finst ...
- **p. 4 / 3.1. CLIP3R - extractive body cue:** These features are then processed by the keyframe decoder Dkey and the supporting decoder Dsup from the original I2P.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our main contributions are as follows: • We present Ov3R, a novel framework that unifies 3R models and open-vocabulary 3D semantic segmentation. • We design CLIP3R, a CLIP-informed 3D reconstruction model that ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | main, contributions, follows, present, Ov3R, novel, framework, unifies, models, open-vocabulary, semantic, segmentation | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.2. 2D-3D OVS) |
| Output/action | The latter flavor is the most suitable approach for developing Spatial AI systems, although it poses greater challenges compared to offline methods, as input images are collected incrementally rather than being available ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 5 (3.2. 2D-3D OVS), p. 7 (Method) |
| Objective/outcome | The former is similar to the loss used to supervise I2P: LL2W = L X i=1 Mi · ( ˆC · // ˆP ′ i -Pi//1 -α log ˆC) (5) while the ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.1. CLIP3R), p. 6 (Method), p. 4 (3.1. CLIP3R) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • We present Ov3R, a novel framework that unifies 3R models and open-vocabulary 3D semantic segmentation. • We design ...
- **p. 3 / 3.1. CLIP3R - extractive body cue:** We introduce CLIP3R, a CLIP-informed 3D reconstruction model that integrates the rich semantic understanding embedded in CLIP features and enables open-vocabulary semantic segmentation as a ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce Ov3R, an open-vocabulary semantic 3D reconstruction framework that processes RGBonly video streams.
- **p. 3 / 3. Method - extractive body cue:** It consists of two main components, highlighted in yellow and blue: (i) a CLIP-informed 3Rbased model (CLIP3R) and (ii) a 2D-3D OVS module.
- **p. 5 / 3.2. 2D-3D OVS - extractive body cue:** To address this limitation, we introduce 2D-3D fused descriptors, obtained as follows.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running on ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 7. Efficiency of each component in Ov3R. Measurements taken on a 2000-frame sequence. Total refers to the full framework running sequentially (SAM2 + CLIP3R ...
- **p. 6 / 4. Experiments - extractive body cue:** We evaluate 3D reconstruction performance on Replica [48] and 7Scenes [46].

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | For the 3D reconstruction task, we follow [35] and train CLIP3R on ScanNet++ [58], Aria Synthetic Environments [2], and CO3D-v2 [44], which provide diverse scenarios and objects from both real-world and synthetic ... | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Dataset/benchmark | For the 3D reconstruction task, we follow [35] and train CLIP3R on ScanNet++ [58], Aria Synthetic Environments [2], and CO3D-v2 [44], which provide diverse scenarios and objects from both real-world and synthetic ... | role, split, size and leakage | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Metric | We adopt standard metrics including Accuracy (cm), completion (cm) for 3D reconstruction, Absolute Trajectory Error (ATE RMSE) for tracking accuracy, and Frame Per Second (FPS) to assess efficiency. | definition, denominator, direction and uncertainty | p. 6 (4. Experiments), p. 8 (Figure/Table caption), p. 6 (4. Experiments) |
| Baseline/ablation | Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running on CLIP3R recon- structions. Here, "Ov3R" refers to ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 6 (4.1. 3D Reconstruction), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Ov3R inherits one of the limitations of 3R models, i.e., the suboptimal accuracy of the retrieved camera poses.
- **p. 8 / 5. Conclusion - extractive body cue:** Future research will aim to overcome this limitation by integrating techniques from the SLAM literature, such as global bundle adjustment.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. 2D-3D OVS Overview. After matching 2D and 3D segments across images and pointmaps, CLIP3R, DINO, and 3D-CLIP features are combined into a 2D-3D ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running on ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 As a result, a significant gap between existing SLAM methods and envisioned Spatial AI systems still persists.를 문제로 두고, Our main contributions are as follows: • We present Ov3R, a novel framework that unifies 3R models and open-vocabulary 3D semantic segmentation. • We design CLIP3R, a CLIP-informed 3D reconstruction model that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.2. 2D-3D OVS), p. 3 (3. Method), p. 3 (3.1. CLIP3R) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
