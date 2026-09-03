# ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: LLM, Robotics, Vision-Language
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Consequently, MLLMs lack prior knowledge in this field while successful training for these tasks necessitates extensive data to achieve desired generalization ability.를 문제로 두고, Meanwhile, in real-world experiments, our method shows strong generalization ability, with or without TTA strategy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robot manipulation relies on accurately predicting contact points and end-effector directions to ensure successful operation.
- **p. 1 / Abstract - extractive body cue:** However, learning-based robot manipulation, trained on a limited category within a simulator, often struggles to achieve generalizability, especially when confronted with extensive categories.
- **p. 1 / Abstract - extractive body cue:** Therefore, we introduce an innovative approach for robot manipulation that leverages the robust reasoning capabilities of Multimodal Large Language Models (MLLMs) to enhance the stability ...
- **p. 1 / Abstract - extractive body cue:** By fine-tuning the injected adapters, we preserve the inherent common sense and reasoning ability of the MLLMs while equipping them with the ability for manipulation.
- **p. 1 / Abstract - extractive body cue:** The fundamental insight lies in the introduced fine-tuning paradigm, encompassing object category understanding, affordance prior reasoning, and object-centric pose prediction to stimulate the reasoning ability ...
- **p. 2 / 1. Introduction - extractive body cue:** Consequently, MLLMs lack prior knowledge in this field while successful training for these tasks necessitates extensive data to achieve desired generalization ability.
- **p. 1 / 1. Introduction - extractive body cue:** Additionally, ManipLLM predicts the gripper's up direction (xu, yu, zu) and forward direction (xf, yf, zf), forming the end-effector SO(3) rotation. demonstrate impressive performance, they ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Meanwhile, in real-world experiments, our method shows strong generalization ability, with or without TTA strategy.
- **p. 2 / 1. Introduction - extractive body cue:** Experiments show that in the simulator, our method achieves a promising manipulation success rate across 30 categories.
- **p. 6 / 3.3. Sim-to-real Transfer - extractive body cue:** Specifically, given the current test sample, we introduce an additional reasoning step to prompt the model to assess whether the predicted position can lead to ...
- **p. 3 / 3.1. Fine-tuning Strategy - extractive body cue:** 3.1.1 Model Architecture We adopt the MLLM, LLaMa-Adapter [38], as our backbone and follow its training strategy.
- **p. 3 / 3.1. Fine-tuning Strategy - extractive body cue:** After aligning visual and text feature representation with the multi-modal projection module, LLaMa is required to conduct multi-modal understanding and give correct answers.
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** This is supervised under cross-entropy loss LA, enabling the model aware where of the object region can be manipulated and facilitating the model latter predict ...
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** In the simulator, when pre-collecting training data, if the manipulation is successful, we record the RGB image and the corresponding end-effector pose, which are used ...
- **p. 5 / 3.1. Fine-tuning Strategy - extractive body cue:** During inference, we adopt chain-of-thought reasoning to simulate the model to generate a precise initial contact end-effector pose interpretively.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To deal with these difficulties, the proposed policy aims to adjust how we interact with things based on impedance force feedback, which can handle different scenarios effectively. | image/video, language instruction, proprioception과 history | p. 5 (3.2. Active Impedance Adaptation Policy), p. 5 (3.2. Active Impedance Adaptation Policy) |
| State/latent | deal, difficulties, policy, aims, adjust, interact, things, impedance, force, feedback, handle, different | language-grounded task state와 action-policy context | p. 5 (3.2. Active Impedance Adaptation Policy), p. 5 (3.2. Active Impedance Adaptation Policy), p. 1 (1. Introduction) |
| Output/action | Thus, the best forward direction is generated as the following to determine the current end-effector's pose: dopt, opt = arg max j∈{0,1,...,N} ∥δj∥ By doing so, we determine the optimal movement pose ... | continuous action, pose 또는 action chunk | p. 5 (3.2. Active Impedance Adaptation Policy), p. 1 (1. Introduction), p. 4 (3.1. Fine-tuning Strategy) |
| Objective/outcome | This is supervised under cross-entropy loss LA, enabling the model aware where of the object region can be manipulated and facilitating the model latter predict contact position that can promote a movement. | instruction following, task success, generalization과 latency | p. 4 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Meanwhile, in real-world experiments, our method shows strong generalization ability, with or without TTA strategy.
- **p. 2 / 1. Introduction - extractive body cue:** Experiments show that in the simulator, our method achieves a promising manipulation success rate across 30 categories.
- **p. 7 / 4.3. Ablation and Analysis - extractive body cue:** It thus significantly improves the manipulation success rate by +7%.
- **p. 6 / 4.1. Training Details - extractive body cue:** If successful manipulation is achieved, we record it as a successful sample.
- **p. 6 / 4.1. Training Details - extractive body cue:** We adopt the manipulation success rate to reflect the outcome of the manipulation which is the ratio of the number of successfully manipulated samples divided ...
- **p. 7 / 4.2. Quantitative Comparison - extractive body cue:** The success rate of VoxPoser is 14.0% while ours is 69.0%.
- **p. 8 / 4.4. Real-world Evaluation - extractive body cue:** The results of real-world experiments are shown in Table 3.
- **p. 8 / 4.4. Real-world Evaluation - extractive body cue:** Object Category Success/Total 4/5 5/5 4/5 3/5 4/5 4/5 4/5 Distance(m) 0.17 0.28 0.10 0.08 0.14 0.15 0.18 Table 3.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Ablation and Analysis), p. 6 (4.1. Training Details) |
| Embodiment/environment | 5, the devised TTA strategy addresses discrepancies arising from real-world hardware configurations. | hardware/simulator version and reset protocol | p. 8 (4.4. Real-world Evaluation), p. 6 (4.1. Training Details) |
| Dataset/benchmark | We conduct experiments that involve interacting with various real-world household objects. | role, split, size and leakage | p. 8 (4.4. Real-world Evaluation), p. 6 (4.1. Training Details), p. 8 (4.4. Real-world Evaluation), p. 6 (4.1. Training Details) |
| Metric | We adopt the manipulation success rate to reflect the outcome of the manipulation which is the ratio of the number of successfully manipulated samples divided by the total number of all test ... | definition, denominator, direction and uncertainty | p. 6 (4.1. Training Details), p. 7 (4.2. Quantitative Comparison), p. 7 (4.3. Ablation and Analysis) |
| Baseline/ablation | Table 1. Comparisons of our method against baseline methods. used to determine end-effector pose. Our current experimental settings involve training on a wider range of object categories. Consequently, this poses challenges in ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.2. Quantitative Comparison) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.4. Real-world Evaluation - extractive body cue:** Additionally, its head is relatively short, which presents a collision risk when interacting with the protruding handle.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Consequently, MLLMs lack prior knowledge in this field while successful training for these tasks necessitates extensive data to achieve desired generalization ability.를 문제로 두고, Meanwhile, in real-world experiments, our method shows strong generalization ability, with or without TTA strategy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 6 (3.3. Sim-to-real Transfer), p. 3 (3.1. Fine-tuning Strategy) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
