# CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, their reliance on exhaustive multi-scale rendering leads to inefficiency, and patch-based feature extraction often fails to capture precise object boundaries, resulting in scale misalignment and performance degradation.를 문제로 두고, The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable the reconstruction of 3D Gaussian semantic fields. ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in 3D reconstruction techniques and vision-language models have fueled significant progress in 3D semantic understanding, a capability critical to robotics, autonomous driving, and ...
- **p. 1 / Abstract - extractive body cue:** However, methods that rely on 2D priors are prone to a critical challenge: cross-view semantic inconsistencies induced by occlusion, image blur, and view-dependent variations.
- **p. 1 / Abstract - extractive body cue:** These inconsistencies, when propagated via projection supervision, deteriorate the quality of 3D Gaussian semantic fields and introduce artifacts in the rendered outputs.
- **p. 1 / Abstract - extractive body cue:** To mitigate this limitation, we propose CCL-LGS, a novel framework that enforces view-consistent semantic supervision by integrating multi-view semantic cues.
- **p. 1 / Abstract - extractive body cue:** Specifically, our approach first employs a zero-shot tracker to
- **p. 2 / 1. Introduction - extractive body cue:** However, their reliance on exhaustive multi-scale rendering leads to inefficiency, and patch-based feature extraction often fails to capture precise object boundaries, resulting in scale misalignment ...
- **p. 2 / 1. Introduction - extractive body cue:** This makes it difficult to maintain semantic coherence across views and often leads to artifacts in the rendered novel views.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable ...
- **p. 2 / 1. Introduction - extractive body cue:** Owing to its proficiency in 3D open-vocabulary scene understanding, our method could benefit a variety of downstream applications.
- **p. 3 / 3. Method - extractive body cue:** In this section, we present our proposed framework, CCLLGS, for view-consistent 3D semantic reconstruction.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** In our method, a uniform 32×32 point prompt is provided to SAM to generate three types of masks corresponding to the semantic scales of subparts, ...
- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** To mitigate the limitations of directly using features derived from imperfect masks, we introduce a codebookbased contrastive learning approach.
- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** This approach consists of two key steps: (1) mask association via IoU matching and (2) applying contrastive losses to improve feature representation.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** Although LangSplat [20] extracts object-level features with clear boundaries by generating masks for subparts, parts, and whole objects, its dependence on multiple models increases data ...
- **p. 5 / 3.4. 3D Gaussian Semantic Field - extractive body cue:** To jointly optimize the semantic features of 3D Gaussians and the parameters of the MLP decoder, we minimize the cross-entropy loss: \ m ath c ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For each pixel v, its semantic feature Fi(v) can be expressed as: F_i ( v) = \t e xt {CLIP}(I_t \odot M_i(v)), \label {supervised_f} (3) where It is the input image, and ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 2 (1. Introduction) |
| State/latent | pixel, semantic, feature, expressed, F_i, CLIP, I_t, odot, M_i, label, supervised_f, where | geometry, map, object/relationship state | p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 2 (1. Introduction), p. 3 (3.2. Two-Level Semantic Feature Extraction) |
| Output/action | The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable the reconstruction of 3D Gaussian semantic fields. ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction) |
| Objective/outcome | To jointly optimize the semantic features of 3D Gaussians and the parameters of the MLP decoder, we minimize the cross-entropy loss: \ m ath c al {L}_{\text {CE}} = \text {CE}(\hat {\mathcal ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. 3D Gaussian Semantic Field), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable ...
- **p. 2 / 1. Introduction - extractive body cue:** Owing to its proficiency in 3D open-vocabulary scene understanding, our method could benefit a variety of downstream applications.
- **p. 3 / 3. Method - extractive body cue:** In this section, we present our proposed framework, CCLLGS, for view-consistent 3D semantic reconstruction.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** In our method, a uniform 32×32 point prompt is provided to SAM to generate three types of masks corresponding to the semantic scales of subparts, ...
- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** To mitigate the limitations of directly using features derived from imperfect masks, we introduce a codebookbased contrastive learning approach.
- **p. 6 / 4.1. Experiments on LERF - extractive body cue:** We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all four scenes, outperforming ...
- **p. 7 / 4.1. Experiments on LERF - extractive body cue:** Our method achieves consistent multi-view segmentation and accurately captures challenging objects like the cabinet, outperforming prior approaches. glass of water kamaboko RGB GT Ours w/ ...
- **p. 8 / 4.2. Experiments on 3D-OVS - extractive body cue:** While our approach achieves comparable performance, it underperforms 3D VL-GS.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF) |
| Embodiment/environment | The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments. | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Dataset/benchmark | Evaluations are conducted on four LERF scenes. | role, split, size and leakage | p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF) |
| Metric | Note that the Room scene contains a significant annotation error; thus, we exclude it from quantitative evaluation and provide qualitative results only in the supplementary material. | definition, denominator, direction and uncertainty | p. 6 (4. Experiments), p. 6 (4.1. Experiments on LERF), p. 1 (Figure/Table caption) |
| Baseline/ablation | Our method achieves consistent multi-view segmentation and accurately captures challenging objects like the cabinet, outperforming prior approaches. glass of water kamaboko RGB GT Ours w/ 𝓛𝓛𝒑𝒑𝒑𝒑𝒍𝒍𝒍𝒍 w/ 𝓛𝓛𝒑𝒑𝒑𝒑𝒔𝒔𝒔𝒔 baseline Figure 5. | fair input/data/compute/action matching | p. 7 (4.1. Experiments on LERF), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results.
- **p. 8 / 5. Conclusion - extractive body cue:** Future work will refine masks for greater robustness.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Quantitative comparison of our method and LangSplat under three challenging scenarios: Occlusion, Image Blur, and View- Dependent Variations. The results clearly demonstrate the ...
- **p. 6 / 4. Experiments - extractive body cue:** The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments.
- **p. 6 / 4.1. Experiments on LERF - extractive body cue:** In the kitchen scene, we specifically focus on the cabinet, a challenging object that other methods frequently fail to segment correctly.
- **p. 7 / 4.1. Experiments on LERF - extractive body cue:** Combining both ensures robust, discriminative 3D semantic segmentation in challenging scenes.
- **p. 7 / 4.1. Experiments on LERF - extractive body cue:** 2, both losses are essential for optimal performance-removing either causes noticeable degradation, though all variants still surpass the baseline.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, their reliance on exhaustive multi-scale rendering leads to inefficiency, and patch-based feature extraction often fails to capture precise object boundaries, resulting in scale misalignment and performance degradation.를 문제로 두고, The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable the reconstruction of 3D Gaussian semantic fields. ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Contrastive Codebook Learning), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.4. 3D Gaussian Semantic Field), p. 3 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
