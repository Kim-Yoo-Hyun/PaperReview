# Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=8xTDnj39Ti.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247589. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openreview.net/forum?id=8xTDnj39Ti
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247589
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 A: (E) remove the tomato from the blackpot and put it on the table.를 문제로 두고, Here we present the overall data scale and sources for each reasoning modality, while more details about the construction methodologies are provided in Appendix A.2.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** While significant research has focused on developing embodied reasoning capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs into Vision-Language-Action (VLA) models for end-to-end robot ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we take an initial step toward bridging embodied reasoning with VLA policy learning by introducing Vlaser - a VisionLanguage-Action Model with synergistic ...
- **p. 1 / ABSTRACT - extractive body cue:** Built upon the high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance across a range of embodied reasoning benchmarks-including spatial reasoning, embodied grounding, embodied QA, and task ...
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we systematically examine how different VLM initializations affect supervised VLA fine-tuning, offering novel insights into mitigating the domain shift between internet-scale pre-training data and ...
- **p. 1 / ABSTRACT - extractive body cue:** Based on these insights, our approach achieves state-of-the-art results on the WidowX benchmark and competitive performance on the Google Robot benchmark.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A: (E) remove the tomato from the blackpot and put it on the table.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this context, vision-language models (VLMs) (OpenAI, 2023; Liu et al., 2023; Chen et al., 2024; Bai et al., 2025; Team et al., 2023) emerge ...

## Core Idea

- **p. 4 / 2 METHOD - extractive body cue:** Here we present the overall data scale and sources for each reasoning modality, while more details about the construction methodologies are provided in Appendix A.2.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing foundation models that possess strong reasoning and control capabilities is therefore an important advancement toward general-purpose embodied AI.
- **p. 4 / 2 METHOD - extractive body cue:** General and Spatial Reasoning Data The Vlaser dataset integrates 1.2 million question-answer pairs dedicated to general Robotic Visual Question Answering (RoboVQA) tasks, along with an ...
- **p. 5 / 2 METHOD - extractive body cue:** Effective planning allows robots to combine basic skills and generalize to new scenarios.
- **p. 5 / 2 METHOD - extractive body cue:** 2.3 TRAINING RECIPE Vlaser adopts a two-stage training recipe, designed to optimize both embodied reasoning and robot control.
- **p. 5 / 2 METHOD - extractive body cue:** In the first training phase, we fine-tune InternVL3 using auto-regressive language modeling loss.
- **p. 5 / 2 METHOD - extractive body cue:** Ii t, lt and qt are encoded via corresponding encoders and then projected via a linear projection layer into the same embedding space. θ represents ...
- **p. 4 / 2 METHOD - extractive body cue:** During inference, we denoise the actions based on the image observation, language instruction, as well as the current robot state.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | During inference, we denoise the actions based on the image observation, language instruction, as well as the current robot state. | image/video, language instruction, proprioception과 history | p. 4 (2 METHOD), p. 5 (2 METHOD) |
| State/latent | During, inference, denoise, actions, image, observation, language, instruction, well, current, robot, state | language-grounded task state와 action-policy context | p. 4 (2 METHOD), p. 5 (2 METHOD), p. 5 (2 METHOD) |
| Output/action | The action expert is analogous to a mixture of experts(MoE) (Shazeer et al., 2017b; Du et al., 2022; Zhou et al., 2024) architecture with two mixture elements, while the original part of ... | continuous action, pose 또는 action chunk | p. 5 (2 METHOD), p. 5 (2 METHOD), p. 4 (2 METHOD) |
| Objective/outcome | In particular, given the input images x ∈Rt×h×w×3 and textual prompt y ∈Rl, the language modeling loss Llm can be defined by Llm = -log p(tN/Fv(x; θv), Ft(y), t0:N-1; Θ), (1) where ... | instruction following, task success, generalization과 latency | p. 5 (2 METHOD), p. 4 (2 METHOD), p. 6 (2 METHOD) |

## Main Claims and Actual Contribution

- **p. 4 / 2 METHOD - extractive body cue:** Here we present the overall data scale and sources for each reasoning modality, while more details about the construction methodologies are provided in Appendix A.2.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing foundation models that possess strong reasoning and control capabilities is therefore an important advancement toward general-purpose embodied AI.
- **p. 4 / 2 METHOD - extractive body cue:** General and Spatial Reasoning Data The Vlaser dataset integrates 1.2 million question-answer pairs dedicated to general Robotic Visual Question Answering (RoboVQA) tasks, along with an ...
- **p. 5 / 2 METHOD - extractive body cue:** Effective planning allows robots to combine basic skills and generalize to new scenarios.
- **p. 5 / 2 METHOD - extractive body cue:** 2.3 TRAINING RECIPE Vlaser adopts a two-stage training recipe, designed to optimize both embodied reasoning and robot control.
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** This suggests that pretraining with diverse in-domain multimodal data, spanning general QA, grounding, and spatial intelligence, could best facilitates transfer learning for VLA policy learning ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** When compared against current state-of-the-art embodied-specific VLMs, including RoboBrain2.0 (Team et al., 2025a) and Embodied-R1 (Yuan et al., 2025), our method, Vlaser still achieves superior ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: An illustration of Vlaser architecture. Vlaser includes two components and corresponding training phases: 1) the Multimodal Pretraining is for embodied reasoning enhancement based ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS) |
| Embodiment/environment | SimplerENV is an open-source suite of purpose-built simulated environments with nearly 150K episodes for evaluating real-world robot manipulation policies in a scalable, reproducible way. | hardware/simulator version and reset protocol | p. 8 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |
| Dataset/benchmark | 3.1 PERFORMANCE ON EMBODIED REASONING CAPABILITY Evaluation Datasets We conduct a comprehensive evaluation of embodied reasoning capabilities across a total of 12 benchmarks, covering a wide spectrum of tasks including embodied question ... | role, split, size and leakage | p. 8 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS) |
| Metric | Avg indicates the average success rate among the four tasks. | definition, denominator, direction and uncertainty | p. 7 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS) |
| Baseline/ablation | When compared against current state-of-the-art embodied-specific VLMs, including RoboBrain2.0 (Team et al., 2025a) and Embodied-R1 (Yuan et al., 2025), our method, Vlaser still achieves superior performance on the majority of benchmarks ... | fair input/data/compute/action matching | p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 3 EXPERIMENTS - extractive body cue:** These results indicate that Vlaser delivers a well-balanced and robust capability set, performing strongly across multiple dimensions of embodied intelligence - from embodied question answering ...
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Robotwin is a scalable framework for bimanual manipulation, which integrates scalable training sets and pre-defined tasks as benchmarks for comprehensive robust bimanual manipulation.
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** This conclusion is as same as the results in 3.2, which demonstrates great robustness of our method.
- **p. 27 / A.4 QUALITATIVE DEMONSTRATION - extractive body cue:** Carrot on the plate Put eggplant in basket InternVL3-2B Fail Vlaser Success Vlaser-QA Success Spoon on the towel Stack Cube InternVL3-2B Fail Vlaser Success Vlaser-QA ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 A: (E) remove the tomato from the blackpot and put it on the table.를 문제로 두고, Here we present the overall data scale and sources for each reasoning modality, while more details about the construction methodologies are provided in Appendix A.2.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (2 METHOD), p. 5 (2 METHOD), p. 4 (2 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
