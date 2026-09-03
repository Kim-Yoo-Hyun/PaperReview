# Grounded 3D-Aware Spatial Vision-Language Modeling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language, 3D spatial, grounding
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Two challenges, in particular, are under-addressed.를 문제로 두고, We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present GR3D, a spatial vision language model equipped with three complementary grounding capabilities-explicit 2D grounding, implicit 2D grounding, and monocular 3D grounding-within a single ...
- **p. 1 / Abstract - extractive body cue:** GR3D introduces an implicit grounding mechanism that identifies entity mentions during generation and inserts the corresponding region tokens into the text stream, allowing the model ...
- **p. 1 / Abstract - extractive body cue:** In parallel, a 1Work done during an internship at NVIDIA. region-prompted monocular 3D grounding design predicts 3D bounding boxes in the camera view from grounded ...
- **p. 1 / Abstract - extractive body cue:** Together, these grounding capabilities enable GR3D to decompose complex spatial understanding problems into grounded 2D perception followed by 3D inference.
- **p. 1 / Abstract - extractive body cue:** GR3D achieves consistent improvements across grounded and non-grounded spatial benchmarks, demonstrating grounding as an effective inductive bias for strengthening spatial understanding in VLMs.
- **p. 2 / 1. Introduction - extractive body cue:** Two challenges, in particular, are under-addressed.
- **p. 2 / 1. Introduction - extractive body cue:** While explicit 2D grounding predicts the location of queried objects, it cannot handle free-form reasoning where spatial cues are implicit.

## Core Idea

- **p. 3 / 2.2. Grounding in the 2D Plane - extractive body cue:** We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model.
- **p. 2 / 1. Introduction - extractive body cue:** To address these limitations, we introduce (GR3D), a spatial VLM that integrates grounding as a core mechanism for learning spatial representations.
- **p. 3 / 2. Method - extractive body cue:** Building on this foundation, we introduce explicit and implicit 2D grounding (Sec.
- **p. 4 / 2.3. Monocular 3D Grounding via Region Prompt - extractive body cue:** To mitigate scale and depth ambiguity, we introduce an intrinsic-aware normalization strategy that rescales images according to focal length, yielding a consistent field of view ...
- **p. 2 / 1. Introduction - extractive body cue:** This enables reasoning to evolve directly over grounded visual evidence, yielding coherent spatial predictions without any separate detection phase.
- **p. 4 / 2.2.2. Implicit 2D Grounding - extractive body cue:** The model first predicts coordinates, then encodes the predicted region to obtain its embedding, which is inserted back into the ongoing sequence before the next ...
- **p. 4 / 2.2.2. Implicit 2D Grounding - extractive body cue:** Our stream-based grounding can be viewed abstractly as analogous to a twostep process, i.e., first grounding entities with a VLM, and then performing region-conditioned reasoning ...
- **p. 5 / 2.4. Data Construction and Composition - extractive body cue:** Our training data is composed of publicly available sources: 97K grounded CoT samples, 780K 3D detection samples from Omni3D [32] and EmbodiedScan [56], and 272K ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given an input instruction, the model generates its response in a chain-ofthought (CoT) fashion. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (2.2.2. Implicit 2D Grounding), p. 3 (2.1. Foundational Spatial VLM) |
| State/latent | Given, input, instruction, model, generates, response, chain-ofthought, CoT, fashion, framework, naturally, extends | geometry, map, object/relationship state | p. 4 (2.2.2. Implicit 2D Grounding), p. 3 (2.1. Foundational Spatial VLM), p. 2 (1. Introduction) |
| Output/action | Our framework naturally extends from single-view to multi-view inputs by embedding all image tokens with depth- and pixel-based positional cues in a unified spatial feature space. | point map, pose, scene graph, affordance 또는 query result | p. 3 (2.1. Foundational Spatial VLM), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | This token is detached from the computation graph (i.e., no gradient flows through it) but serves as a strong conditional cue for subsequent token prediction. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (2.2.2. Implicit 2D Grounding), p. 4 (2.3. Monocular 3D Grounding via Region Prompt) |

## Main Claims and Actual Contribution

- **p. 3 / 2.2. Grounding in the 2D Plane - extractive body cue:** We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model.
- **p. 2 / 1. Introduction - extractive body cue:** To address these limitations, we introduce (GR3D), a spatial VLM that integrates grounding as a core mechanism for learning spatial representations.
- **p. 3 / 2. Method - extractive body cue:** Building on this foundation, we introduce explicit and implicit 2D grounding (Sec.
- **p. 4 / 2.3. Monocular 3D Grounding via Region Prompt - extractive body cue:** To mitigate scale and depth ambiguity, we introduce an intrinsic-aware normalization strategy that rescales images according to focal length, yielding a consistent field of view ...
- **p. 2 / 1. Introduction - extractive body cue:** This enables reasoning to evolve directly over grounded visual evidence, yielding coherent spatial predictions without any separate detection phase.
- **p. 6 / 3.2. 3D Object Detection - extractive body cue:** Compared with vision specialists, our model achieves competitive results overall and delivers notably better performance on indoor datasets.
- **p. 6 / 3.3. Visual Question Answering - extractive body cue:** In contrast, Stage 2 finetuning focuses on learning the structure of CoT reasoning, and the results indicate that it does not significantly reduce general VQA ...
- **p. 7 / 3.4. Implicit Grounding CoT - extractive body cue:** We show results in Table 4, where our method outperforms baselines in all these metrics.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (3.2. 3D Object Detection), p. 6 (3.3. Visual Question Answering) |
| Embodiment/environment | The Omni3D dataset is highly imbalanced [44], with far fewer outdoor training samples compared to indoor scenes. | hardware/simulator version and reset protocol | p. 7 (3.5. Analysis and Ablation Study), p. 6 (3.2. 3D Object Detection) |
| Dataset/benchmark | It also naturally decomposes the task into two subproblems-2D grounding and 3D inference-where the former benefits from significantly larger amounts of training data across generic detection and grounding datasets. | role, split, size and leakage | p. 7 (3.5. Analysis and Ablation Study), p. 6 (3.2. 3D Object Detection), p. 7 (3.5. Analysis and Ablation Study), p. 6 (3. Experiments) |
| Metric | The Omni3D benchmark reports Average Precision (AP), where predictions are matched to ground-truth using 3D IoU with thresholds ranging from 0.05 to 0.50. | definition, denominator, direction and uncertainty | p. 6 (3.2. 3D Object Detection), p. 7 (3.4. Implicit Grounding CoT), p. 8 (3.5. Analysis and Ablation Study) |
| Baseline/ablation | 4, where our model outperforms all VLM baselines. | fair input/data/compute/action matching | p. 6 (3.2. 3D Object Detection), p. 6 (3.2. 3D Object Detection), p. 7 (3.5. Analysis and Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3.2. 3D Object Detection - extractive body cue:** This makes its 3D predictions unstable under changes in image size.
- **p. 6 / 3.3. Visual Question Answering - extractive body cue:** In contrast, Stage 2 finetuning focuses on learning the structure of CoT reasoning, and the results indicate that it does not significantly reduce general VQA ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Two challenges, in particular, are under-addressed.를 문제로 두고, We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.2. Grounding in the 2D Plane), p. 4 (2.2.2. Implicit 2D Grounding), p. 4 (2.2.2. Implicit 2D Grounding), p. 5 (2.4. Data Construction and Composition) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
