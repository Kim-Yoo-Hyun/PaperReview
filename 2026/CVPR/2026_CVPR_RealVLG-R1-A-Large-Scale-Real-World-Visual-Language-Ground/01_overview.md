# RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Visual-Language Grounding, Benchmark, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 In summary, current VLG and grasping research highlight a clear gap between semantic understanding and manipulation reasoning, making them insufficient for real-world robotic scenarios that require fine-grained, multi-modal perception.를 문제로 두고, 1, we propose the RealVLG framework, which unifies visuallanguage grounding and grasping tasks within a single research paradigm.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Visual-language grounding aims to establish semantic correspondences between natural language and visual entities, enabling models to accurately identify and localize target objects based on textual ...
- **p. 1 / Abstract - extractive body cue:** Existing VLG approaches focus on coarse-grained, object-level localization, while traditional robotic grasping methods rely predominantly on geometric cues and lack language guidance, which limits their ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose the RealVLG framework, which integrates the RealVLG11B dataset and the RealVLG-R1 model to unify real-world visual-language grounding and grasping ...
- **p. 1 / Abstract - extractive body cue:** RealVLG11B dataset provides multi-granularity annotations including bounding boxes, segmentation masks, grasp poses, contact points, and human-verified fine-grained language descriptions, covering approximately 165,000 images, over 800 ...
- **p. 1 / Abstract - extractive body cue:** Experimental results demonstrate that RealVLG supports zeroshot perception and manipulation in real-world unseen environments, establishing a unified semantic-visual multimodal benchmark that provides a comprehensive data ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, current VLG and grasping research highlight a clear gap between semantic understanding and manipulation reasoning, making them insufficient for real-world robotic scenarios that ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, as shown in Fig.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** 1, we propose the RealVLG framework, which unifies visuallanguage grounding and grasping tasks within a single research paradigm.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • RealVLG-11B Dataset: The largest real-world grounding and grasping dataset with multi-granularity annotations from semantic localization to ...
- **p. 5 / 4.1. Overview - extractive body cue:** 3, we propose a unified framework, RealVLG-R1, which fine-tunes pretrained LVLMs using a reinforcement-style optimization strategy inspired by DeepSeek-R1 [22].
- **p. 5 / 4.1. Overview - extractive body cue:** Furthermore, we introduce a Verifiable Reward Mechanism that dynamically evaluates and guides model predictions in terms of both semantic correctness and physical feasibility.
- **p. 8 / Method - extractive body cue:** Building upon this, our proposed RealVLG-R1 model employs Qwen2.5-VL as its backbone and is developed within the VERL framework [68].
- **p. 6 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive body cue:** 3, the policy model receives an image and a task prompt, then generates structured outputs according to task requirements.
- **p. 6 / 4.2. Policy Optimization with Verifiable Rewards - extractive body cue:** Grasp Contact SAM2 Answer Reference Model Reinforcement Fine-tuning KL Reward Policy Model (LVLMs) Figure 3.
- **p. 7 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive body cue:** The predicted contact points P p 1 , P p 2 are first converted into a rectangular grasp pose Gp with fixed width, and then ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | During training, input images and task prompts are processed through a policy optimization module to generate candidate outputs, which are then updated using verifiable reward signals. | standardized observation, action, task state와 evaluation split | p. 2 (1. Introduction), p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards) |
| State/latent | During, training, input, images, task, prompts, processed, through, policy, optimization, module, generate | benchmark state/goal와 method decision | p. 2 (1. Introduction), p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards) |
| Output/action | The core of RealVLG-R1 is its composite reward function R(q, o), providing hierarchical and verifiable feedback by combining output format compliance with task-specific geometric accuracy: R( q, o) = R_ { \text ... | policy/controller trajectory 또는 measured result | p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 2 (1. Introduction) |
| Objective/outcome | Furthermore, the objective of RealVLG-R1 aims to maximize the expected reward while introducing a KL-divergence regularization 42400 | success metric, robustness, generalization과 reproducibility | p. 5 (4.2. Policy Optimization with Verifiable Rewards), p. 8 (Method), p. 5 (4.2. Policy Optimization with Verifiable Rewards) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** 1, we propose the RealVLG framework, which unifies visuallanguage grounding and grasping tasks within a single research paradigm.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • RealVLG-11B Dataset: The largest real-world grounding and grasping dataset with multi-granularity annotations from semantic localization to ...
- **p. 5 / 4.1. Overview - extractive body cue:** 3, we propose a unified framework, RealVLG-R1, which fine-tunes pretrained LVLMs using a reinforcement-style optimization strategy inspired by DeepSeek-R1 [22].
- **p. 5 / 4.1. Overview - extractive body cue:** Furthermore, we introduce a Verifiable Reward Mechanism that dynamically evaluates and guides model predictions in terms of both semantic correctness and physical feasibility.
- **p. 8 / Method - extractive body cue:** Building upon this, our proposed RealVLG-R1 model employs Qwen2.5-VL as its backbone and is developed within the VERL framework [68].
- **p. 7 / 5.2. RealVLG Benchmark - extractive body cue:** In rectangular grasp pose prediction, performance relies on mean IoU (mIoU) and Grasp Accuracy (gAcc) [26], where gAcc is achieved when the IoU exceeds 0.25 ...
- **p. 7 / 5.1. Data Quality Evaluation - extractive body cue:** Specifically, since the language descriptions in RealVLG-11B encompass not only object categories but also rich attributes and spatial relations, it achieves a higher MTLD score, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. RealVLG benchmark comprehensive results. All metrics are reported in percentage format. to quantify the proportion of valid outputs, defined as pre- dictions that ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (5.2. RealVLG Benchmark), p. 7 (5.1. Data Quality Evaluation) |
| Embodiment/environment | The dataset contains approximately 165,000 images, over 800 object instances, 1.3 million segmentation, detection, and language annotations, and 11 billion grasp examples, providing a high-quality benchmark for multi-granularity percept ... | hardware/simulator version and reset protocol | p. 4 (3.1. Overview), p. 4 (3.2. Data Source) |
| Dataset/benchmark | To address these issues, as shown in Table 1, we introduce RealVLG11B, a large-scale, real-world, multimodal, and multigranularity visual-language grounding and grasping dataset. | role, split, size and leakage | p. 4 (3.1. Overview), p. 4 (3.2. Data Source), p. 3 (3.1. Overview), p. 3 (3.1. Overview) |
| Metric | In rectangular grasp pose prediction, performance relies on mean IoU (mIoU) and Grasp Accuracy (gAcc) [26], where gAcc is achieved when the IoU exceeds 0.25 and the angular deviation is below 30◦. | definition, denominator, direction and uncertainty | p. 7 (5.2. RealVLG Benchmark), p. 7 (5.1. Data Quality Evaluation), p. 8 (Figure/Table caption) |
| Baseline/ablation | As shown in Table 3, benefiting from our carefully designed LVLM-assisted and human double-review annotation pipeline, RealVLG-11B consistently outperforms existing datasets across all comparable metrics. | fair input/data/compute/action matching | p. 7 (5.1. Data Quality Evaluation), p. 7 (5.1. Data Quality Evaluation), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusions - extractive body cue:** Future work will extend RealVLG to 3D space, and explore efficient models such as SmolVLM [43] to improve runtime without extra fine-tuning.
- **p. 3 / 3.1. Overview - extractive body cue:** Existing grasping datasets generally suffer from two major limitations.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Dataset split for RealVLG-11B. age instance. 5 Based on the resulting Rect Grasp Poses and segmentation masks, grasp contact points are subse- quently ...
- **p. 7 / 5.1. Data Quality Evaluation - extractive body cue:** Linguistic and grounding quality comparison. grasp points located within segmentation masks (Rg), and proportion of contact centers falling inside segmentation masks (Rc).

## Why Read It

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 In summary, current VLG and grasping research highlight a clear gap between semantic understanding and manipulation reasoning, making them insufficient for real-world robotic scenarios that require fine-grained, multi-modal perception.를 문제로 두고, 1, we propose the RealVLG framework, which unifies visuallanguage grounding and grasping tasks within a single research paradigm.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 5 (4.1. Overview), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
