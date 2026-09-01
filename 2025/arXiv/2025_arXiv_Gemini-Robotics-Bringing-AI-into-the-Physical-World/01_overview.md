# Gemini Robotics: Bringing AI into the Physical World

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (64 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.20020.
> PDF retrieval source: https://arxiv.org/abs/2503.20020. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, Foundation Models, dexterous manipulation, Google DeepMind
- Official paper: https://arxiv.org/abs/2503.20020
- Full-text retrieval: https://arxiv.org/abs/2503.20020
- Code/Project: https://deepmind.google/models/gemini-robotics/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (64 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed to connect the model's innate embodied reasoning capabilities to robotic ...를 문제로 두고, To this end, we introduce the Gemini Robotics family of embodied AI models, built on top of Gemini 2.0, our most advanced multimodal foundation model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** The remarkable progress of modern artificial intelligence (AI) models - with pre-training on largescale datasets - has redefined information processing, demonstrating proficiency and generalization across ...
- **p. 1 / 1. Introduction - extractive body cue:** This has opened a vast landscape of opportunities for interactive and assistive systems within the digital realm, ranging from multimodal chatbots to virtual assistants.
- **p. 1 / 1. Introduction - extractive body cue:** However, realizing the potential of general-purpose autonomous AI in the physical world requires a substantial shift from the digital world, where physically grounded AI agents ...
- **p. 1 / 1. Introduction - extractive body cue:** While, as humans, we take for granted our embodied reasoning abilities - such as perceiving the 3D structure of environments, interpreting complex inter-object relationships, or ...
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, an embodied AI agent must also go beyond passively understanding the spatial and physical concepts of the real world; it must also learn to ...
- **p. 13 / 2.0 Flash - extractive body cue:** However, as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed to connect the ...
- **p. 3 / 1. Introduction - extractive body cue:** To emphasize the flexibility and generality of the Gemini Robotics models, we also introduce an optional specialization stage, which demonstrates how Gemini Robotics can be ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce the Gemini Robotics family of embodied AI models, built on top of Gemini 2.0, our most advanced multimodal foundation model.
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** To capture progress in embodied reasoning for VLMs, we introduce ERQA, short for Embodied Reasoning Question Answering, a benchmark that focuses specifically on capabilities likely ...
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** ERQA consists of 400 multiple choice Visual Question Answering (VQA)-style questions across a wide variety of categories, including spatial reasoning, trajectory reasoning, action reasoning, state ...
- **p. 7 / 2.0 Flash. Predicted point labels are not visualized - extractive body cue:** Below we present detailed quantitative and qualitative evaluations of these capabilities with Gemini 2.0 models (Flash, and Pro Experimental), as well as comparisons with other ...
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, an embodied AI agent must also go beyond passively understanding the spatial and physical concepts of the real world; it must also learn to ...
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini Robotics ...
- **p. 13 / 3. Robot Actions with Gemini Robotics - extractive body cue:** We first study the model after training on a large and diverse dataset consisting of action-labeled robot data as well as other multimodal data.
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** It consists of two components: a VLA backbone hosted in the cloud (Gemini Robotics backbone) and a local action decoder running on the robot's onboard ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini Robotics model. | image/video, language instruction, proprioception과 history | p. 14 (3. Robot Actions with Gemini Robotics), p. 7 (2.0 Flash. Predicted point labels are not visualized) |
| State/latent | backbone, Local, action, decoder, computer, Robot, images, state, image, Figure, Overview, architecture | language-grounded task state와 action-policy context | p. 14 (3. Robot Actions with Gemini Robotics), p. 7 (2.0 Flash. Predicted point labels are not visualized), p. 11 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control) |
| Output/action | While it is possible to create expert models for each of these tasks individually, fusing them in a single foundation model, such as Gemini 2.0, allows the model to perform embodied reasoning ... | continuous action, pose 또는 action chunk | p. 7 (2.0 Flash. Predicted point labels are not visualized), p. 11 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 13 (2.0 Flash) |
| Objective/outcome | To this end, we study a fine-tuning process that utilizes a re-labeled version of the robot action dataset in Section 3.1, bringing action prediction closer to the newly introduced embodied reasoning capabilities: ... | instruction following, task success, generalization과 latency | p. 22 (4.2. Enhanced reasoning and generalization), p. 23 (4.2. Enhanced reasoning and generalization), p. 14 (3. Robot Actions with Gemini Robotics) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce the Gemini Robotics family of embodied AI models, built on top of Gemini 2.0, our most advanced multimodal foundation model.
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** To capture progress in embodied reasoning for VLMs, we introduce ERQA, short for Embodied Reasoning Question Answering, a benchmark that focuses specifically on capabilities likely ...
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** ERQA consists of 400 multiple choice Visual Question Answering (VQA)-style questions across a wide variety of categories, including spatial reasoning, trajectory reasoning, action reasoning, state ...
- **p. 7 / 2.0 Flash. Predicted point labels are not visualized - extractive body cue:** Below we present detailed quantitative and qualitative evaluations of these capabilities with Gemini 2.0 models (Flash, and Pro Experimental), as well as comparisons with other ...
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, an embodied AI agent must also go beyond passively understanding the spatial and physical concepts of the real world; it must also learn to ...
- **p. 10 / 2.0 Pro Experimental - extractive body cue:** (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (2.0 Pro Experimental) |
| Embodiment/environment | Gemini Robotics: Bringing AI into the Physical World Gemini GPT Claude Benchmark | hardware/simulator version and reset protocol | p. 5 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark) |
| Dataset/benchmark | Spatial Reasoning 84 Action Reasoning 72 Trajectory Reasoning 66 State Estimation 55 Task Reasoning 38 Multi-view Reasoning 37 Pointing 34 Other 14 Figure 4 / ERQA question categories. | role, split, size and leakage | p. 5 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark) |
| Metric | (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories). | definition, denominator, direction and uncertainty | p. 10 (2.0 Pro Experimental) |
| Baseline/ablation | For each image pair, the left image with the point coordinates and the right image without coordinates are given, and the model predicts which of the labeled points in the left image ... | fair input/data/compute/action matching | p. 10 (2.0 Pro Experimental), p. 10 (2.0 Pro Experimental) |

## Explicit Limitations and Failure Boundary

- **p. 28 / 6. Discussion - extractive body cue:** In addition, while our initial results with Gemini Robotics demonstrate promising generalization capabilities, future work will focus on several key areas.
- **p. 28 / 6. Discussion - extractive body cue:** Robust human-level embodied reasoning is critical for robots and other physically grounded agents.
- **p. 29 / 6. Discussion - extractive body cue:** This involves developing techniques to seamlessly integrate abstract reasoning with precise execution, leading to more robust and generalizable performance.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed to connect the model's innate embodied reasoning capabilities to robotic ...를 문제로 두고, To this end, we introduce the Gemini Robotics family of embodied AI models, built on top of Gemini 2.0, our most advanced multimodal foundation model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 13 (2.0 Flash), p. 3 (1. Introduction), p. 8 (3.5 Sonnet), p. 12 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 2 (1. Introduction), p. 14 (3. Robot Actions with Gemini Robotics) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
