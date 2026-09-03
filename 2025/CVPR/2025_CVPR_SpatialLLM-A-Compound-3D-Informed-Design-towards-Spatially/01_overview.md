# SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: LLM, spatial reasoning, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, a significant gap remains: previous works [2, 14, 16] have primarily focused on 3D distance relationships, overlooking the crucial role of 3D object orientation.를 문제로 두고, Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans naturally understand 3D spatial relationships, enabling complex reasoning like predicting collisions of vehicles from different directions.
- **p. 1 / Abstract - extractive body cue:** Current large multimodal models (LMMs), however, lack of this capability of 3D spatial reasoning.
- **p. 1 / Abstract - extractive body cue:** This limitation stems from the scarcity of 3D training data and the bias in current model designs toward 2D data.
- **p. 1 / Abstract - extractive body cue:** In this paper, we systematically study the impact of 3D-informed data, architecture, and training setups, introducing SpatialLLM, a large multi-modal model with advanced 3D spatial ...
- **p. 1 / Abstract - extractive body cue:** To address data limitations, we develop two types of 3D-informed training datasets: (1) 3D-informed probing data focused on object's 3D location and orientation, and (2) ...
- **p. 1 / 1. Introduction - extractive body cue:** However, a significant gap remains: previous works [2, 14, 16] have primarily focused on 3D distance relationships, overlooking the crucial role of 3D object orientation.
- **p. 1 / 1. Introduction - extractive body cue:** Collecting a small set of high-quality 3D-aware data to tackle the first challenge is feasible, albeit labor-intensive, using readily available tools.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model.
- **p. 2 / 1. Introduction - extractive body cue:** Third, we present the first comprehensive search over the LMM design space for spatial reasoning tasks and propose a roadmap towards developing state-of-the-art models in ...
- **p. 3 / 3. Methods - extractive body cue:** We present the task of reasoning 3D spatial relationships and explain the challenges LMMs face when answering these questions in Sec.
- **p. 3 / 3.1. Preliminary of LMMs - extractive body cue:** A standard LMM [39, 41] consists of a visual encoder to process the image, a multimodal connector to transform the visual feature to visual token, ...
- **p. 5 / 3.3.1. Design space - extractive body cue:** 3.2.1, we propose new training setups that aim to improve 3D awareness and advance the 3D spatial reasoning capabilities.
- **p. 5 / 3.3.1. Design space - extractive body cue:** We introduce the design space considered in our work, i.e., choices of training data, model architecture, and training setup that advance the 3D spatial reasoning ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive body cue:** This step enables the model to learn rich visual features solely from visual signals. • Noisy image-text pairs: Large-scale image-text pairs [20, 37, 52] are ...
- **p. 5 / 3.3.1. Design space - extractive body cue:** We consider two types of visual encoders: (i) Frozen & pretrained visual encoder CLIP [48] following [41] but with the option to mix a wider ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Existing pretraining and visual instruction tuning data for LMMs [41, 58] focused on detailed descriptions and conversations about scenes, appearances, and actions, while being vague about the 3D spatial relationships that build ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2.1. Challenges of 3D spatial reasoning), p. 3 (3.1. Preliminary of LMMs) |
| State/latent | Existing, pretraining, visual, instruction, tuning, data, LMMs, focused, detailed, descriptions, conversations, about | geometry, map, object/relationship state | p. 4 (3.2.1. Challenges of 3D spatial reasoning), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3. Compound 3D-Informed Design) |
| Output/action | At this stage, the model is trained to describe images in details to align visual and language representations in the same space. • Visual instruction tuning. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3. Compound 3D-Informed Design), p. 6 (3.3.1. Design space) |
| Objective/outcome | This stage focuses on developing foundational visual representations, often with reconstructionbased objectives (e.g., MAE [23], DINOv2 [47]). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model.
- **p. 2 / 1. Introduction - extractive body cue:** Third, we present the first comprehensive search over the LMM design space for spatial reasoning tasks and propose a roadmap towards developing state-of-the-art models in ...
- **p. 3 / 3. Methods - extractive body cue:** We present the task of reasoning 3D spatial relationships and explain the challenges LMMs face when answering these questions in Sec.
- **p. 3 / 3.1. Preliminary of LMMs - extractive body cue:** A standard LMM [39, 41] consists of a visual encoder to process the image, a multimodal connector to transform the visual feature to visual token, ...
- **p. 5 / 3.3.1. Design space - extractive body cue:** 3.2.1, we propose new training setups that aim to improve 3D awareness and advance the 3D spatial reasoning capabilities.
- **p. 7 / 4.2. Results - extractive body cue:** Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary model by 8.7% ...
- **p. 7 / 4.2. Results - extractive body cue:** In terms of architecture, integrating a mixed vision encoder can improve overall performance especially for the 3D orientation.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. We modernize a standard LLaVA-v1.5 towards the de- sign of a 3D-informed LMM. The bars are the answer accuracies on the SpatialVQA benchmark, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.2. Results), p. 7 (4.2. Results) |
| Embodiment/environment | We build our SpatialVQA on images from Omni3D [11], with 3D bounding box annotations on diverse objects from both urban [12, 21] and indoor scenes [9, 50, 54]. | hardware/simulator version and reset protocol | p. 4 (3.2.2. SpatialVQA for Evaluation), p. 4 (3.2.2. SpatialVQA for Evaluation) |
| Dataset/benchmark | In terms of 3D-informed data and training, we find that 3Dinformed instruction tuning with our proposed 3DI-Ft1M dataset yields a substantial performance boost of +10.7%. | role, split, size and leakage | p. 4 (3.2.2. SpatialVQA for Evaluation), p. 4 (3.2.2. SpatialVQA for Evaluation), p. 7 (4.2. Results), p. 7 (4.1. Experimental setup) |
| Metric | We follow [16, 58] and develop rule-based methods to generate visual question-answer pairs from the 3D groundtruths. | definition, denominator, direction and uncertainty | p. 4 (3.2.2. SpatialVQA for Evaluation), p. 4 (3.2.2. SpatialVQA for Evaluation), p. 7 (4.2. Results) |
| Baseline/ablation | Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary model by 8.7% and the best open-source model by 10.5%. | fair input/data/compute/action matching | p. 7 (4.2. Results), p. 7 (4.2. Results), p. 5 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive body cue:** Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different levels of 3D awareness and cannot be ...
- **p. 7 / 4.2. Results - extractive body cue:** Interestingly, although SpatialVLM [14] (implemented in SpaceLLaVA [2]) outperforms other open-source models in overall performance, it falls short in 3D orientation reasoning compared to LLaVA, ...
- **p. 7 / 4.2. Results - extractive body cue:** We will consider models with additional inputs in future work.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, a significant gap remains: previous works [2, 14, 16] have primarily focused on 3D distance relationships, overlooking the crucial role of 3D object orientation.를 문제로 두고, Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
