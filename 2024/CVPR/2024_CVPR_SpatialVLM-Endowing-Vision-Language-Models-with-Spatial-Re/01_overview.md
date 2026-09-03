# SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2401.12168.
> PDF retrieval source: https://arxiv.org/pdf/2401.12168. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, spatial reasoning, Robotics
- Official paper: https://arxiv.org/abs/2401.12168
- Full-text retrieval: https://arxiv.org/pdf/2401.12168
- Code/Project: https://spatial-vlm.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Automatic data generation and augmentation techniques are one approach to deal with the data limitation problem [38, 53, 56, 66].를 문제로 두고, To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning capabilities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1. Introduction - extractive body cue:** Vision language models (VLMs) have made significant progress in recent years across a variety of tasks including image captioning, visual question answering (VQA), embodied planning, ...
- **p. 2 / 1. Introduction - extractive body cue:** While VLMs are powerful general-purpose models for a wide range of tasks, most state-of-the-art VLMs still struggle with spatial reasoning, i.e. tasks that require understanding ...
- **p. 2 / 1. Introduction - extractive body cue:** Spatial reasoning capabilities are useful in their own right, but also for downstream applications such as in robotics or AR.
- **p. 2 / 1. Introduction - extractive body cue:** For example, a spatial reasoning-imbued VLM can be used as a better general-purpose reward annotator [54] and success detector [19].
- **p. 2 / 1. Introduction - extractive body cue:** The exploration of foundation models like VLMs is often inspired by human capabilities.
- **p. 2 / 1. Introduction - extractive body cue:** Automatic data generation and augmentation techniques are one approach to deal with the data limitation problem [38, 53, 56, 66].
- **p. 2 / 1. Introduction - extractive body cue:** This natural proficiency in direct spatial reasoning tasks contrasts with the current limitations of VLMs and thus prevents them from accomplishing real-world tasks that requires ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning capabilities.
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are: • We endow VLMs quantitative spatial reasoning capability, which is a fundamental capability of humans.
- **p. 1 / Body text (section not recovered) - extractive body cue:** To this end, we present a system to facilitate this approach.
- **p. 1 / Body text (section not recovered) - extractive body cue:** GPT-4V Spatial-VLM Figure 1 / We present SpatialVLM, a data synthesis and pre-training mechanism to enhance VLMs' spatial reasoning capabilities.
- **p. 4 / 3. SpatialVLM - extractive body cue:** To equip VLMs with both qualitatively and quantitatively spatial reasoning capabilities, we propose to generate a large-scale spatial VQA dataset, which is used to train ...
- **p. 4 / 3. SpatialVLM - extractive body cue:** Concretely, we design a comprehensive data generation framework which first leverages off-the-shelf computer vision models including open-vocabulary detection, metric depth estimation, semantic segmentation and objectcentric ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** We then investigate various factors in training recipe including data quality, training pipeline and VLM architecture.
- **p. 6 / 3.3. Learning Spatial Reasoning - extractive body cue:** Direct Spatial Reasoning is defined as following, a Vision-Language Model takes as input an image I and a query Q of a spatial task, and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Direct Spatial Reasoning is defined as following, a Vision-Language Model takes as input an image I and a query Q of a spatial task, and output an answer A, in the format ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3.3. Learning Spatial Reasoning), p. 1 (Body text (section not recovered)) |
| State/latent | Direct, Spatial, Reasoning, defined, following, Vision-Language, Model, takes, input, image, query, task | geometry, map, object/relationship state | p. 6 (3.3. Learning Spatial Reasoning), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction) |
| Output/action | We demonstrate that VLMs trained on our synthetic data exhibit strong spatial reasoning capabilities, and can generate metric distance estimation from 2D input images, addressing blind spots of current state-of-the-art VLMs like ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (Body text (section not recovered)), p. 2 (1. Introduction), p. 5 (3.1. Spatial Grounding from 2D Images) |
| Objective/outcome | For example, a spatial reasoning-imbued VLM can be used as a better general-purpose reward annotator [54] and success detector [19]. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (3.2. Large-Scale Spatial Reasoning VQA Dataset) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning capabilities.
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are: • We endow VLMs quantitative spatial reasoning capability, which is a fundamental capability of humans.
- **p. 1 / Body text (section not recovered) - extractive body cue:** To this end, we present a system to facilitate this approach.
- **p. 1 / Body text (section not recovered) - extractive body cue:** GPT-4V Spatial-VLM Figure 1 / We present SpatialVLM, a data synthesis and pre-training mechanism to enhance VLMs' spatial reasoning capabilities.
- **p. 4 / 3. SpatialVLM - extractive body cue:** To equip VLMs with both qualitatively and quantitatively spatial reasoning capabilities, we propose to generate a large-scale spatial VQA dataset, which is used to train ...
- **p. 9 / 4.1. Spatial VQA performance - extractive body cue:** Our approach SpatialVLM achieves significantly higher success rate than all baselines, achieving inrange results on almost half of the questions.
- **p. 8 / 4.1. Spatial VQA performance - extractive body cue:** It is shown that SpatialVLM is able to achieve significantly higher accuracy compared to all baselines that are not trained using the synthetic spatial VQA ...
- **p. 8 / 4.1. Spatial VQA performance - extractive body cue:** Therefore, to evaluate the performance of the VLMs, we use human raters to determine if an answer is correct, and show the success rates of ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance) |
| Embodiment/environment | It shows state-of-the-art performance in OKVQA benchmark, as well as being capable of robot planning tasks. | hardware/simulator version and reset protocol | p. 8 (4. Experiments), p. 9 (4.2. Effect of Spatial VQA Data to General VQA) |
| Dataset/benchmark | We train VLMs using the noisy datasets and evaluate them using a human annotated quantitative spatial VQA benchmark for manipulation. | role, split, size and leakage | p. 8 (4. Experiments), p. 9 (4.2. Effect of Spatial VQA Data to General VQA), p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers), p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers) |
| Metric | Therefore, to evaluate the performance of the VLMs, we use human raters to determine if an answer is correct, and show the success rates of the VLMs in Table. | definition, denominator, direction and uncertainty | p. 8 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance), p. 9 (4.1. Spatial VQA performance) |
| Baseline/ablation | To verify whether VLM's limitation in spatial reasoning is a data problem, we choose the following state-of-the-art VLMs as baselines, all trained on mixtures in which semantic-captioning tasks occupy a heavy weight, ... | fair input/data/compute/action matching | p. 7 (4. Experiments), p. 8 (4. Experiments), p. 8 (4.1. Spatial VQA performance) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4.1. Spatial VQA performance - extractive body cue:** Additionally, we find that state-of-the-art VLM GPT-4V often refrain from generating answers about distance in SI units with a disclaimer text "I'm sorry, but I ...
- **p. 7 / 4. Experiments - extractive body cue:** To verify whether VLM's limitation in spatial reasoning is a data problem, we choose the following state-of-the-art VLMs as baselines, all trained on mixtures in ...
- **p. 9 / 4.1. Spatial VQA performance - extractive body cue:** VLM answers that fall into half to twice of the ground truth value to represent how accurate the VLM's estimates are.
- **p. 10 / 4.2. Effect of Spatial VQA Data to General VQA - extractive body cue:** We train both models for 70k steps, and evaluate percentages of answers from both models that fall into various ranges of the ground truth value ...
- **p. 10 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** 5 compares how different Gaussian noise standard deviations affect the overall VLM performance on quantitative spatial VQA.
- **p. 11 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** It is shown that VLMs trained on datasets of different noise levels achieve similar spatial reasoning accuracy.
- **p. 11 / 4.4. Effect of Noisy Quantitative Spatial Answers - extractive body cue:** We find that our model can learn despite moderate amount of random noise. pick orange tea bottle put apple into the bowl pick up the ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Automatic data generation and augmentation techniques are one approach to deal with the data limitation problem [38, 53, 56, 66].를 문제로 두고, To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning capabilities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. SpatialVLM), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction), p. 6 (3.3. Learning Spatial Reasoning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
