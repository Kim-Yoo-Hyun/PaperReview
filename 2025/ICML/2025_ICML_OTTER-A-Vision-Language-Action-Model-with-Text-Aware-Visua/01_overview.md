# OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=UHF0km7R5M.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/167304. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=UHF0km7R5M
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/167304
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This approach requires the policy network to connect the vision and language information and conduct precise robot control, which often presents significant challenges, especially in unseen environments.를 문제로 두고, To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by language instructions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions.
- **p. 1 / Abstract - extractive body cue:** Existing approaches require fine-tuning pre-trained visionlanguage models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments.
- **p. 1 / Abstract - extractive body cue:** We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction.
- **p. 1 / Abstract - extractive body cue:** Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the ...
- **p. 1 / Abstract - extractive body cue:** This allows OTTER to keep the pre-trained vision-language encoders frozen.
- **p. 1 / 1. Introduction - extractive body cue:** This approach requires the policy network to connect the vision and language information and conduct precise robot control, which often presents significant challenges, especially in ...
- **p. 2 / 1. Introduction - extractive body cue:** Both physical and simulation experiments demonstrate that OTTER outperforms existing VLA models, showing strong generalization to novel objects and environments with less performance degradation (Figure ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by language ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose OTTER, a VLA model that leverages the semantic alignment capabilities of pre-trained VLMs for better generalization.
- **p. 3 / 3. Method - extractive body cue:** We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM.
- **p. 1 / 1. Introduction - extractive body cue:** OTTER exhibits better zero-shot generalization to unseen objects, maintaining strong performance across a variety of novel tasks.
- **p. 3 / 3. Method - extractive body cue:** We first describe how OTTER utilizes the vision-language alignment of pre-trained vision and language encoders to extract text-aware vision features, then provide a more detailed ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** Policy Network and Action Head OTTER uses a transformer as the policy network, consisting of 4 layers and 8 heads, with a hidden dimension of ...
- **p. 5 / 3.2. Model Architecture - extractive body cue:** OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction Figure 4: Example scenes in the simulation (left) and in the physical environments (right) using a ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** For each output token at a given timestep, we use a FFN to predict the next 12 actions.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Different input modalities are usually encoded into separate tokens: multi-view images encoded via visual feature extractors, along with tokenized language instructions, optionally with the robot's proprioceptive states, are fed into a ... | image/video, language instruction, proprioception과 history | p. 1 (1. Introduction), p. 4 (3.2. Model Architecture) |
| State/latent | Different, input, modalities, usually, encoded, separate, tokens, multi-view, images, visual, feature, extractors | language-grounded task state와 action-policy context | p. 1 (1. Introduction), p. 4 (3.2. Model Architecture), p. 3 (3. Method) |
| Output/action | This token serves as input to a policy network for action prediction. | continuous action, pose 또는 action chunk | p. 4 (3.2. Model Architecture), p. 3 (3. Method), p. 1 (1. Introduction) |
| Objective/outcome | Specifically, we use the similarity scores to select and combine visual features that best align with the task instruction, creating compact representations for downstream action prediction. | instruction following, task success, generalization과 latency | p. 3 (3.1. Text-Aware Visual Feature Extraction), p. 4 (3.2. Model Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by language ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose OTTER, a VLA model that leverages the semantic alignment capabilities of pre-trained VLMs for better generalization.
- **p. 3 / 3. Method - extractive body cue:** We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM.
- **p. 1 / 1. Introduction - extractive body cue:** OTTER exhibits better zero-shot generalization to unseen objects, maintaining strong performance across a variety of novel tasks.
- **p. 6 / 4.2. Baselines - extractive body cue:** OTTER achieves a similar success rate on the in-distribution training tasks and unseen tasks, significantly outperforming the baselines, highlighting the benefits of extracting text-aware visual ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Multi-primitive zero-shot generalization: We train models across four manipulation primitives (pouring, drawer manipulation, poking, and pick-and-place) with a total of 1,185 human tele-operated ...
- **p. 6 / 5.1. Real-world Experiments - extractive body cue:** For unseen pick up and place tasks, π0-Fast-Droid is able to achieve a success rate of 61%.
- **p. 7 / 5.1. Real-world Experiments - extractive body cue:** Finetuned π0-Fast-Droid achieves non-zero success rate on Drawer and Poking primitives, but still fails on the pouring primitive.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2. Baselines), p. 7 (Figure/Table caption) |
| Embodiment/environment | We collect robotic datasets on multi-task scenes using a Franka robot, where there are multiple tasks that can be completed in the same scene. | hardware/simulator version and reset protocol | p. 5 (4.1. Environment Setup), p. 6 (5.1. Real-world Experiments) |
| Dataset/benchmark | The results further suggest that OTTER's generalization capabilities can be enhanced through increased model capacity (OTTER-L) and pre-training on large robotic datasets (OTTER-OXE). on unseen tasks for each primitive, with 10 trials ... | role, split, size and leakage | p. 5 (4.1. Environment Setup), p. 6 (5.1. Real-world Experiments), p. 7 (5.1. Real-world Experiments), p. 2 (3. Empirical results suggest that OTTER's performance) |
| Metric | The overall performance is measured by calculating the average success rate with standard error across all trials for the training and unseen tasks. | definition, denominator, direction and uncertainty | p. 5 (4.1. Environment Setup), p. 7 (5.1. Real-world Experiments), p. 6 (5.1. Real-world Experiments) |
| Baseline/ablation | Table 3: Simulation results on LIBERO. We evaluate OTTER and other baselines on 30 in-distribution tasks in LIBERO- Spatial/Object/Goal and on 10 unseen tasks we constructed, each task 50 trials. The numbers ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 5 (4.2. Baselines), p. 6 (4.2. Baselines) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5.1. Real-world Experiments - extractive body cue:** As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length.
- **p. 6 / 5.1. Real-world Experiments - extractive body cue:** For a fair comparison, we extended the context history length of Octo to 10 (Octo cannot exceed a context length of 10 due to its ...
- **p. 7 / 5.1. Real-world Experiments - extractive body cue:** Finetuned π0-Fast-Droid achieves non-zero success rate on Drawer and Poking primitives, but still fails on the pouring primitive.
- **p. 7 / 5.1. Real-world Experiments - extractive body cue:** While π0-Fast-Droid achieves decent performance on the pick and place primitives, it fails on all the other three primitives as the majority of the Droid ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 6: The 10 in-distribution tasks and 7 unseen tasks we used in our real-world setting. For each experiment trial of poking and pouring, we ...
- **p. 8 / 2. OTTER w.o. f ′ - extractive body cue:** This suggests that pretrained VLM provides more robust and transferable visual representations.
- **p. 8 / 2. OTTER w.o. f ′ - extractive body cue:** However, we found that fine-tuning the pre-trained vision encoder actually degrades the model's vision-language understanding capabilities.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This approach requires the policy network to connect the vision and language information and conduct precise robot control, which often presents significant challenges, especially in unseen environments.를 문제로 두고, To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by language instructions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
