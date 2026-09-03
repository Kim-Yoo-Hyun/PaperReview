# G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: VLM, 3D reconstruction, spatial reasoning
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We argue that this limitation stems from how current VLMs acquire their physical world knowledge.를 문제로 두고, Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in a single vision-language model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language Models (VLMs) still lack robustness in spatial intelligence, demonstrating poor performance on spatial understanding and reasoning tasks.
- **p. 1 / Abstract - extractive body cue:** We attribute this gap to the absence of a visual geometry learning process capable of reconstructing 3D space from 2D images.
- **p. 1 / Abstract - extractive body cue:** We present G2VLM, a geometry grounded vision-language model that bridges two fundamental aspects of spatial intelligence: spatial 3D reconstruction and spatial understanding.
- **p. 1 / Abstract - extractive body cue:** G2VLM natively leverages learned 3D visual geometry features to directly predict 3D attributes and enhance spatial reasoning tasks via in-context learning and interleaved reasoning.
- **p. 1 / Abstract - extractive body cue:** Our unified design is highly scalable for spatial understanding: it trains on abundant multiview image and video data, while simultaneously leveraging the benefits of 3D ...
- **p. 2 / 1. Introduction - extractive body cue:** We argue that this limitation stems from how current VLMs acquire their physical world knowledge.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.
- **p. 3 / 1. Introduction - extractive body cue:** We present G2VLM, a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for multimodal understanding and ...
- **p. 4 / 3. Unified Spatial Vision-Language Model - extractive body cue:** We introduce G2VLM, a unified geometry-grounded VLM that integrates spatial 3D reconstruction and spatial understanding.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** Our model's input is a sequence (Ii)N i=1 of N RGB images Ii ∈R3×H×W , we present the detailed design for each expert as follows.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** As illustrated in Figure 3, G2VLM adopts a Mixture-ofTransformer-Experts (MoT) architecture [16] that consists of two transformer experts-one geometry perception expert dedicated to visual geometry ...
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** For joint-training, we use AdamW optimizer for 16K iterations with a lr of 2e-5 on 64 A800 GPUs over 3 days.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** For geometric perception expert, we incorporate a DINOV2 vision encoder to inject low-level visual information to LLM which further reasons the 3D-aware feature through global ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (1) where Ti ∈SE(3) ⊂R4×4 is the camera pose, Xi ∈ RH×W ×3 is the associated pixel-aligned 3D point map represented in its own camera coordinate system, each corresponding to the input ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.1. Model Architecture), p. 2 (1. Introduction) |
| State/latent | where, camera, pose, associated, pixel-aligned, point, represented, coordinate, system, corresponding, input, image | geometry, map, object/relationship state | p. 4 (3.1. Model Architecture), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | On visual geometry tasks, G2VLM achieves competitive results against state-of-theart (SOTA) feed-forward 3D reconstruction models, such as VGGT [52], across depth estimation, point estimation, and camera pose estimation tasks. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Model Architecture) |
| Objective/outcome | We explore three distinct joint-training strategies, where the semantic perception expert is, by default, optimized using a cross-entropy (CE) loss: • CE Loss Only: Freeze the geometric perception expert, only the semantic ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning), p. 5 (3.3. Spatial Reasoning Learning) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.
- **p. 3 / 1. Introduction - extractive body cue:** We present G2VLM, a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for multimodal understanding and ...
- **p. 4 / 3. Unified Spatial Vision-Language Model - extractive body cue:** We introduce G2VLM, a unified geometry-grounded VLM that integrates spatial 3D reconstruction and spatial understanding.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** Our model's input is a sequence (Ii)N i=1 of N RGB images Ii ∈R3×H×W , we present the detailed design for each expert as follows.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach over ...
- **p. 7 / 4.1. Visual Geometry Results - extractive body cue:** These results demonstrate that our method achieves on-par performance with VGGT in completion and comparable results in accuracy.
- **p. 7 / 4.1. Visual Geometry Results - extractive body cue:** As shown in Table 1a, our method achieves on-par performance on the RRA and RTA metrics and comparable results on the AUC metric when compared ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results) |
| Embodiment/environment | Following the evaluation settings in [55, 62], we evaluate the quality of reconstructed multiview point maps on the 7-Scenes [45] and ETH3D [44] datasets. | hardware/simulator version and reset protocol | p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results) |
| Dataset/benchmark | G2VLM effectively reconstructs a diverse set of open-domain images, spanning object-level, structure-level, indoor, and outdoor scenes, including both dynamic and static content. | role, split, size and leakage | p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results), p. 7 (4.2. Spatial Understanding & Reasoning Results) |
| Metric | These results demonstrate that our method achieves on-par performance with VGGT in completion and comparable results in accuracy. | definition, denominator, direction and uncertainty | p. 7 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results) |
| Baseline/ablation | Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach over the baselines. Notably, it con- firms a ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results), p. 7 (4.2. Spatial Understanding & Reasoning Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models.
- **p. 7 / 4.2. Spatial Understanding & Reasoning Results - extractive body cue:** We leave the scaling of our model to future work, as this is a promising direction to unlock even stronger performance.
- **p. 7 / 4.1. Visual Geometry Results - extractive body cue:** These results underscore our model's strong capabilities, particularly since it does not use camera tokens (like VGGT) which provides a strong camera pose prior or ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We argue that this limitation stems from how current VLMs acquire their physical world knowledge.를 문제로 두고, Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in a single vision-language model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (3.1. Model Architecture), p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.1. Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
