# Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Shi_Language_Embedded_3D_Gaussians_for_Open-Vocabulary_Scene_Understanding_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Shi_Language_Embedded_3D_Gaussians_for_Open-Vocabulary_Scene_Understanding_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, open-vocabulary, semantic
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Shi_Language_Embedded_3D_Gaussians_for_Open-Vocabulary_Scene_Understanding_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Shi_Language_Embedded_3D_Gaussians_for_Open-Vocabulary_Scene_Understanding_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, accurately incorporating language embedding into current 3D scene representations, while maintaining their efficiency and visual quality, presents a significant challenge.를 문제로 두고, In summary, our contributions include: • We introduce a novel quantization scheme that efficiently compresses and integrates semantic features into dense 3D Gaussians, ensuring efficient optimization and rendering on consumer devices wh ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary querying in 3D space is challenging but essential for scene understanding tasks such as object localization and segmentation.
- **p. 1 / Abstract - extractive body cue:** Language-embedded scene representations have made progress by incorporating language features into 3D spaces.
- **p. 1 / Abstract - extractive body cue:** However, their efficacy heavily depends on neural networks that are resourceintensive in training and rendering.
- **p. 1 / Abstract - extractive body cue:** Although recent 3D Gaussians offer efficient and high-quality novel view synthesis, directly embedding language features in them leads to prohibitive memory usage and decreased performance.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary query tasks.
- **p. 2 / 1. Introduction - extractive body cue:** However, accurately incorporating language embedding into current 3D scene representations, while maintaining their efficiency and visual quality, presents a significant challenge.
- **p. 2 / 1. Introduction - extractive body cue:** However, the quality of semantic features heavily relies on scene representation, and trivially expanding the output channels poses significant challenges in recovering high-precision and robust ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions include: • We introduce a novel quantization scheme that efficiently compresses and integrates semantic features into dense 3D Gaussians, ensuring efficient ...
- **p. 2 / 1. Introduction - extractive body cue:** Our extensive experiments demonstrate that our method achieves state-of-the-art quality in both novel view synthesis and open-vocabulary querying tasks, while allowing real-time rendering on consumer-level ...
- **p. 4 / 3.4. Language Embedded 3D Gaussians - extractive body cue:** To address semantic ambiguity arising from visual disparities across various viewpoints, we introduce a novel mechanism to reduce the spatial frequency of language embeddings through ...
- **p. 3 / 3. Method - extractive body cue:** In this section, we introduce our training process of Language Embedded 3D Gaussians, including (1) a recap of 3D Gaussian Splatting [20] (Sec.
- **p. 3 / 3.3. Quantization of Language Features - extractive body cue:** We propose a dedicated quantization scheme to effectively compress the language features extracted from multiple viewpoints, resulting in a more efficient and compact representation of ...
- **p. 3 / 3.2. Dense Language Feature Extraction - extractive body cue:** We first extract pixel-level dense language features from visual-language models.
- **p. 5 / 3.4. Language Embedded 3D Gaussians - extractive body cue:** We then render these compact semantic feature vectors into a 2D feature map with rasterization and alpha blending, and decode the 2D feature map into ...
- **p. 5 / 3.4. Language Embedded 3D Gaussians - extractive body cue:** Consequently, we introduce a smoothing strategy that limits the spatial frequency of semantic features on 3D Gaussians.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | During training process, a softmax operation is applied to the decoder's output, yielding the language feature index distribution ˆ M ∈RH×W ×N, where H and W denote the height and width of ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3.4. Language Embedded 3D Gaussians), p. 2 (1. Introduction) |
| State/latent | During, training, process, softmax, operation, applied, decoder, output, yielding, language, feature, index | geometry, map, object/relationship state | p. 5 (3.4. Language Embedded 3D Gaussians), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Recent techniques [21, 22, 27] extract dense language features from multi-view 2D images and incorporate additional output branches in scene representation to predict semantic features. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective/outcome | During the quantization of all language features extracted from multi-view images, the optimization of the discrete feature space S is simultaneously accomplished by minimizing the cosine similarity loss between the language features ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.3. Quantization of Language Features), p. 5 (3.4. Language Embedded 3D Gaussians), p. 5 (3.4. Language Embedded 3D Gaussians) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions include: • We introduce a novel quantization scheme that efficiently compresses and integrates semantic features into dense 3D Gaussians, ensuring efficient ...
- **p. 2 / 1. Introduction - extractive body cue:** Our extensive experiments demonstrate that our method achieves state-of-the-art quality in both novel view synthesis and open-vocabulary querying tasks, while allowing real-time rendering on consumer-level ...
- **p. 4 / 3.4. Language Embedded 3D Gaussians - extractive body cue:** To address semantic ambiguity arising from visual disparities across various viewpoints, we introduce a novel mechanism to reduce the spatial frequency of language embeddings through ...
- **p. 3 / 3. Method - extractive body cue:** In this section, we introduce our training process of Language Embedded 3D Gaussians, including (1) a recap of 3D Gaussian Splatting [20] (Sec.
- **p. 3 / 3.3. Quantization of Language Features - extractive body cue:** We propose a dedicated quantization scheme to effectively compress the language features extracted from multiple viewpoints, resulting in a more efficient and compact representation of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Images of various open-vocabulary queries. ner effectively diminishes ambiguity and enhances the mean average precision (mAP) metric. Furthermore, integrating DINO features significantly improves ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We present Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary querying. The top row visualizes the original image, novel view synthesis ...
- **p. 6 / 5.2. Comparisons - extractive body cue:** Our approach outperforms others in ren5338

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Embodiment/environment | For a simultaneous evaluation of visual and semantic embedding quality, we select six scenes (excluding Stump) from the Mip-NeRF360 dataset [3] and manually annotate segmentation maps for each scene in the evaluation ... | hardware/simulator version and reset protocol | p. 6 (5.1. Basic Setups), p. 6 (5.2. Comparisons) |
| Dataset/benchmark | We use a diverse range of vocabulary categories to identify objects in scenes, such as visual attribute terms like "green", and subjective adjectives like "cute". | role, split, size and leakage | p. 6 (5.1. Basic Setups), p. 6 (5.2. Comparisons), p. 7 (5.3. Open-vocabulary Query), p. 7 (5.2. Comparisons) |
| Metric | For the accuracy of language embedding, we measure the mean intersection over union (mIoU), mean pixel accuracy (mPA), mean precision (mP), and mean average precision (mAP) based on our annotations. | definition, denominator, direction and uncertainty | p. 6 (5.1. Basic Setups), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Baseline/ablation | Our approach outperforms others in ren5338 | fair input/data/compute/action matching | p. 6 (5.2. Comparisons), p. 7 (5.2. Comparisons), p. 8 (5.4. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** These limitations might be overcome with more advanced visual-language models and native per-pixel semantic features.
- **p. 8 / 6. Conclusion - extractive body cue:** Although DINO features improve object boundary detection, they fall short in pinpointing fine-grained object geometries at high resolutions when using CLIP-derived semantics.
- **p. 6 / 5.2. Comparisons - extractive body cue:** Specifically, DFF [22] fails to identify "asphalt ground" in scene "bicycle" and "flower" in scene "garden".
- **p. 6 / 5.2. Comparisons - extractive body cue:** This may be caused by its use of LSeg [24], which is unstable to compute correct features in complex scenes.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, accurately incorporating language embedding into current 3D scene representations, while maintaining their efficiency and visual quality, presents a significant challenge.를 문제로 두고, In summary, our contributions include: • We introduce a novel quantization scheme that efficiently compresses and integrates semantic features into dense 3D Gaussians, ensuring efficient optimization and rendering on consumer devices wh ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.3. Quantization of Language Features), p. 3 (3.2. Dense Language Feature Extraction), p. 5 (3.4. Language Embedded 3D Gaussians) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
