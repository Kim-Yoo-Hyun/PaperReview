# ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, grounding, LVLM
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Existing 3D visual grounding (3DVG) methods [7, 12, 13, 36] face challenges in open-vocabulary grounding and reasoning, primarily due to reliance on 3D annotations [37, 39] and mask proposals [2, 5], which ...를 문제로 두고, Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D visual grounding and reasoning aim to localize objects in a scene based on implicit language descriptions, even when they are occluded.
- **p. 1 / Abstract - extractive body cue:** This ability is crucial for tasks such as vision-language navigation and autonomous robotics.
- **p. 1 / Abstract - extractive body cue:** However, current methods struggle because they rely heavily on fine-tuning with 3D annotations and mask proposals, which limits their ability to handle diverse semantics and ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose ReasonGrounder, an LVLM-guided framework that uses hierarchical 3D feature Gaussian fields for adaptive grouping based on physical scale, enabling open-vocabulary ...
- **p. 1 / Abstract - extractive body cue:** ReasonGrounder interprets implicit instructions using large vision-language models (LVLM) and localizes occluded objects through 3D Gaussian splatting.
- **p. 2 / 1. Introduction - extractive body cue:** Existing 3D visual grounding (3DVG) methods [7, 12, 13, 36] face challenges in open-vocabulary grounding and reasoning, primarily due to reliance on 3D annotations [37, ...
- **p. 2 / 1. Introduction - extractive body cue:** However, challenges remain in interpreting user intent and handling occlusions during object localization.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations.
- **p. 2 / 1. Introduction - extractive body cue:** To achieve open-vocabulary 3D visual grounding and reasoning, this paper proposes ReasonGrounder, a novel LVLM-Guided Hierarchical Feature Splatting method that enables implicit instruction comprehension and ...
- **p. 6 / Method - extractive body cue:** To extract language features from each image, we use the OpenCLIP ViT-B/16 model.
- **p. 6 / Method - extractive body cue:** We then train the hierarchical feature Gaussian field by fixing all other parameters of the 3D Gaussians.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | LVLM aids in interpreting complex instructions and locating objects even when partially or fully occluded. • (4) Dataset Contributions: A new ReasoningGD dataset offers over 10K complex scenes with 2 million annotations, ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | LVLM, aids, interpreting, complex, instructions, locating, objects, even, when, partially, fully, occluded | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | For instance, simple commands like apple can be directly interpreted, while more complex instructions, such as Can you localize the red, round, sweet fruit on the table that is partially occluded by ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (Method) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations.
- **p. 2 / 1. Introduction - extractive body cue:** To achieve open-vocabulary 3D visual grounding and reasoning, this paper proposes ReasonGrounder, a novel LVLM-Guided Hierarchical Feature Splatting method that enables implicit instruction comprehension and ...
- **p. 6 / 4.1. Evaluation on Open-set 3D Visual Grounding - extractive body cue:** Our results show that ReasonGrounder outperforms 2D-based methods like ODISE [35] and OV-Seg [25], and significantly surpasses 3D-based methods, including Method bed bench room sofa ...
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** These results demonstrate that ReasonGrounder successfully achieves amodal perception, accurately localizing complete objects regardless of the occlusion level.
- **p. 6 / 4.1. Evaluation on Open-set 3D Visual Grounding - extractive body cue:** Quantitative results of mean IoU (%) across various scenes in the LERF, 3D-OVS, and ReasoningGD datasets, including both scene-specific scores and overall performance.
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** As shown in Table 5, our method outperforms in all edge cases.
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** Our ReasonGrounder achieves accurate 3D localization, even when the object is partially visible or fully occluded in novel views.
- **p. 5 / 4. Experiments - extractive body cue:** The performance of ReasonGrounder is evaluated using two main metrics: Localization Accuracy [16] and Intersection over Union (IoU).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 8 (4.2. Evaluation on 3D Reasoning) |
| Embodiment/environment | This paper introduces a novel dataset, ReasoningGD, which includes over 10K scenes of varying complexity and more than 263 types of common objects, with around 2 million annotations. | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 7 (4.2. Evaluation on 3D Reasoning) |
| Dataset/benchmark | To test robustness, we selected five challenging scenes with small proportions, including multi-hierarchical structures and similar objects, along with ten text queries per scene from the LERF and ReasoningGD datasets. | role, split, size and leakage | p. 5 (4. Experiments), p. 7 (4.2. Evaluation on 3D Reasoning), p. 7 (4.2. Evaluation on 3D Reasoning), p. 5 (4. Experiments) |
| Metric | Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is deemed successful if the pixel with the ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) |
| Baseline/ablation | Our ReasonGrounder demonstrates superior accuracy in open-vocabulary 3D localization compared to other state-of-the-art methods. | fair input/data/compute/action matching | p. 7 (4.2. Evaluation on 3D Reasoning), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Examples of open-vocabulary 3D visual grounding and reasoning. In a given scene, the user observes from a per- spective with occlusions and asks ...
- **p. 5 / 4. Experiments - extractive body cue:** The dataset features multiple object instances with varying levels of occlusion, making it ideal for evaluating the ability in open-vocabulary 3D reasoning, grounding, and amodal ...
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** Existing openvocabulary 3D visual grounding methods struggle with localizing complete objects in novel views with occlusion, limiting their real-world applicability.
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** To test robustness, we selected five challenging scenes with small proportions, including multi-hierarchical structures and similar objects, along with ten text queries per scene from ...
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** This highlights the robustness of our ReasonGrounder in complex situations.
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** For each query, the left column shows partial occlusion, and the right column shows full occlusion.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Existing 3D visual grounding (3DVG) methods [7, 12, 13, 36] face challenges in open-vocabulary grounding and reasoning, primarily due to reliance on 3D annotations [37, 39] and mask proposals [2, 5], which ...를 문제로 두고, Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 6 (Method), p. 6 (Method), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
