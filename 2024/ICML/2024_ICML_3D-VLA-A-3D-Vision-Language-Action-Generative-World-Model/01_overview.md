# 3D-VLA: A 3D Vision-Language-Action Generative World Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2024/poster/34575.
> PDF retrieval source: https://icml.cc/virtual/2024/poster/34575. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, 3D reasoning, world model, action tokens, Planning
- Official paper: https://icml.cc/virtual/2024/poster/34575
- Full-text retrieval: https://icml.cc/virtual/2024/poster/34575
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Another challenge for building such a generative world model lies in the lack of data.를 문제로 두고, Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world.
- **p. 1 / Abstract - extractive body cue:** Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between ...
- **p. 1 / Abstract - extractive body cue:** In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly.
- **p. 1 / Abstract - extractive body cue:** To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a ...
- **p. 1 / Abstract - extractive body cue:** Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the ...
- **p. 2 / 1. Introduction - extractive body cue:** Another challenge for building such a generative world model lies in the lack of data.
- **p. 1 / 1. Introduction - extractive body cue:** Secondly, existing embodied datasets mainly contain 2D images or videos, lacking 3D-related annotations for reasoning and planning in the 3D space.

## Core Idea

- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene.
- **p. 2 / 1. Introduction - extractive body cue:** To sum up, we have the following contributions: • We propose 3D-VLA, a new family of 3D vision-languageaction embodied foundation models that unify 3D perception, ...
- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** To enhance the model's comprehension of 3D scenes and facilitate interaction within these environments, we introduce a novel set of interaction tokens.
- **p. 1 / 1. Introduction - extractive body cue:** To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a ...
- **p. 2 / 1. Introduction - extractive body cue:** Recognizing the inadequacy of multimodal generation ability in embodied foundation models, we propose to inject the goal generation ability into 3D-VLA.
- **p. 5 / 4.3. Injecting Goal Generation Ability into 3D-VLA - extractive body cue:** We first pretrain the embodied diffusion models in terms of different modalities such as images, depths and point clouds, and then align the decoders of ...
- **p. 6 / 4.3.2. BRIDGING LLM AND GOAL GENERATION - extractive body cue:** Based on this, we can apply a transformer-based projector, which is capable of mapping the decoder features and embeddings from the Large Language Model (LLM) ...
- **p. 4 / 4.1. Overview - extractive body cue:** Next, we inject goal generation ability into 3D-VLA by first pretraining the embodied diffusion models and employing a projector for aligning the LLM and the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3D-VLA: A 3D Vision-Language-Action Generative World Model Robot: Actions are: [action tokens] Robot Control Projector Image / Point Cloud Diffusion Model Initial State Goal State Robot: Sure! | image/video, language instruction, proprioception과 history | p. 3 (1. Introduction), p. 3 (1. Introduction) |
| State/latent | D-VLA, Vision-Language-Action, Generative, World, Model, Robot, Actions, action, tokens, Control, Projector, Image | language-grounded task state와 action-policy context | p. 3 (1. Introduction), p. 3 (1. Introduction), p. 5 (4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS) |
| Output/action | This generated goal state can then be fed back to our model to guide the robot control. • Our 3D-VLA can conduct a series of tasks, including goal generation (in terms of ... | continuous action, pose 또는 action chunk | p. 3 (1. Introduction), p. 5 (4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS), p. 8 (5.3. Embodied Action Planning) |
| Objective/outcome | We minimize both the LLM and DM denoising loss. | instruction following, task success, generalization과 latency | p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION), p. 5 (4.3. Injecting Goal Generation Ability into 3D-VLA), p. 7 (5.3. Embodied Action Planning) |

## Main Claims and Actual Contribution

- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene.
- **p. 2 / 1. Introduction - extractive body cue:** To sum up, we have the following contributions: • We propose 3D-VLA, a new family of 3D vision-languageaction embodied foundation models that unify 3D perception, ...
- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** To enhance the model's comprehension of 3D scenes and facilitate interaction within these environments, we introduce a novel set of interaction tokens.
- **p. 1 / 1. Introduction - extractive body cue:** To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a ...
- **p. 2 / 1. Introduction - extractive body cue:** Recognizing the inadequacy of multimodal generation ability in embodied foundation models, we propose to inject the goal generation ability into 3D-VLA.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. Evaluation of action planning on CALVIN dataset. matches the baseline performance in most tasks within the RLBench action prediction, showing its planning capability. ...
- **p. 7 / 5.1. 3D Reasoning and Localization - extractive body cue:** In Tables 1, 3D-VLA outperforms all 2D VLM methods on language reasoning tasks.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of our 3D-VLA pipeline. The left part shows our goal-generation capability. Our model can imagine the final state image and point cloud ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (5.1. 3D Reasoning and Localization) |
| Embodiment/environment | The tasks include 1) embodied QA on RoboVQA dataset (Sermanet et al., 2023); 2) task captioning on 11 Open-X datasets (Padalkar et al., 2023), where we input the initial and final scenes ... | hardware/simulator version and reset protocol | p. 6 (5.1. 3D Reasoning and Localization), p. 4 (3.1. Dataset Collection) |
| Dataset/benchmark | We build several tasks on 3D embodied instruction tuning datasets for learning these abilities in the robotics domain. | role, split, size and leakage | p. 6 (5.1. 3D Reasoning and Localization), p. 4 (3.1. Dataset Collection), p. 6 (5.1. 3D Reasoning and Localization), p. 7 (5.1. 3D Reasoning and Localization) |
| Metric | In Table 2, 3D-VLA demonstrates a marked superiority over the 2D baseline methods in terms of localization performance. | definition, denominator, direction and uncertainty | p. 7 (5.1. 3D Reasoning and Localization), p. 6 (5. Experiments), p. 7 (5.1. 3D Reasoning and Localization) |
| Baseline/ablation | Figure 2. Overview of our 3D-VLA pipeline. The left part shows our goal-generation capability. Our model can imagine the final state image and point cloud based on the user's input. This generated ... | fair input/data/compute/action matching | p. 3 (Figure/Table caption), p. 6 (5.1. 3D Reasoning and Localization), p. 7 (5.1. 3D Reasoning and Localization) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS - extractive body cue:** FOR GOAL GENERATION To address the limitations of current diffusion models for goal generation in an embodied environment, we train RGBD to RGB-D and point-cloud ...
- **p. 4 / 3.2. Visual Annotations - extractive body cue:** Thus, for video segments where the camera pose does not change, we use optical flow to estimate which pixels are the unmoved background.
- **p. 7 / 5.2. Multi-modal Goal Generation - extractive body cue:** We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training process.
- **p. 7 / 3) LLMs with image generation ability NeXT-GPT (Wu - extractive body cue:** In these diverse and uncontrolled environments, our 3D-VLA model consistently and robustly demonstrated its efficacy.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Another challenge for building such a generative world model lies in the lack of data.를 문제로 두고, Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.3. Injecting Goal Generation Ability into 3D-VLA), p. 5 (4.2.2. INTERACTION TOKENS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Another challenge for building such a generative world model lies in the lack of data. (p. 2, 1. Introduction).
- **Actual contribution:** To sum up, we have the following contributions: • We propose 3D-VLA, a new family of 3D vision-languageaction embodied foundation models that unify 3D perception, reasoning, and action with a ... (p. 2, 1. Introduction).
- **Evaluation boundary:** Table 6. Evaluation of action planning on CALVIN dataset. matches the baseline performance in most tasks within the RLBench action prediction, showing its planning capability. It's worth noting that the ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training process. (p. 7, 5.2. Multi-modal Goal Generation).
