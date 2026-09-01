# Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (62 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2510.03342.
> PDF retrieval source: https://arxiv.org/pdf/2510.03342. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, embodied reasoning, motion transfer, cross-embodiment, long-horizon, humanoid
- Official paper: https://arxiv.org/abs/2510.03342
- Full-text retrieval: https://arxiv.org/pdf/2510.03342
- Code/Project: https://deepmind.google/en/models/gemini-robotics/gemini-robotics/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (62 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 This allows the model to convert visual observations into language-based thoughts, simplify complex instructions, detect task success or failure, propose recovery behaviors, and make the robot's actions more interpretable to human users.를 문제로 두고, This multi-embodiment pre-training allows GR 1.5 to control multiple robots, including the ALOHA, Bi-arm Franka, and Apollo humanoid robots, without any robot-specific post-training, and it also enables zero-shot skill transfer from one ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** Truly general robots will require a deep understanding of the physical world.
- **p. 1 / 1. Introduction - extractive body cue:** Our previous work, Gemini Robotics (Gemini-Robotics-Team et al., 2025), established a strong foundation by leveraging Gemini's rich world knowledge to create a Vision-Language-Action (VLA) model ...
- **p. 1 / 1. Introduction - extractive body cue:** We now introduce the Gemini Robotics 1.5 (GR 1.5) family of robot foundation models, built on the latest generation of Gemini (Comanici et al., 2025).
- **p. 1 / 1. Introduction - extractive body cue:** The new model family significantly enhances the capabilities of Gemini Robotics and brings Gemini's advanced thinking and agentic paradigm to the physical world.
- **p. 1 / 1. Introduction - extractive body cue:** It includes Gemini Robotics 1.5, a multi-embodiment VLA model (Bjorck et al., 2025; Intelligence et al., 2025; Wen et al., 2025; Zitkovich et al., 2023) ...
- **p. 2 / 1. Introduction - extractive body cue:** This allows the model to convert visual observations into language-based thoughts, simplify complex instructions, detect task success or failure, propose recovery behaviors, and make the ...
- **p. 1 / 1. Introduction - extractive body cue:** We combine these two models into an agentic system that enables robots to solve complex problems by orchestrating user dialogue, high-level reasoning and planning, agentic ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** This multi-embodiment pre-training allows GR 1.5 to control multiple robots, including the ALOHA, Bi-arm Franka, and Apollo humanoid robots, without any robot-specific post-training, and it ...
- **p. 2 / 1. Introduction - extractive body cue:** ER thinking traces Gemini Robotics 1.5 Gemini Robotics-ER 1.5 Actions Text Figure 1 / The Gemini Robotics 1.5 family of models consists of Gemini Robotics ...
- **p. 3 / 2.1. Model & Architecture - extractive body cue:** The full agentic system consists of an orchestrator and an action model that are implemented by the VLM and the VLA, respectively: • Orchestrator: The ...
- **p. 4 / 2.2. Robot Data - extractive body cue:** The robot data consists of thousands of diverse tasks across these platforms covering a broad range of manipulation skills across a multitude of scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Secondly, GR 1.5 is a Thinking VLA 1See Contributions and Acknowledgments section for full author list.
- **p. 3 / 2.1. Model & Architecture - extractive body cue:** We use GR-ER 1.5 as the orchestrator. • Action model: The action model translates instructions issued by the orchestrator into lowlevel robot actions.
- **p. 10 / 4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model - extractive body cue:** We introduce Gemini Robotics-ER 1.5 (GR-ER 1.5), our most advanced multimodal thinking model for state-of-the-art embodied reasoning based on Gemini.
- **p. 13 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** By extending this ability to predict a set of points, a model can generate more complex outputs like motion trajectories and paths, providing precise action ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This allows the model to convert visual observations into language-based thoughts, simplify complex instructions, detect task success or failure, propose recovery behaviors, and make the robot's actions more interpretable to human users. | proprioception, reference pose/motion, visual or language command | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | allows, model, convert, visual, observations, language-based, thoughts, simplify, complex, instructions, detect, task | whole-body pose, balance/contact state와 skill/mode | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.1. Model & Architecture) |
| Output/action | execution code_blocks Search search Function calling data_object Proprioception precision_manufacturing Images image Text instruction short_text Inputs Speech mic Images photo_library Text chat ALOHA 2 Bi-arm Franka Apptronik Apollo Tas ... | joint/whole-body action, motion target 또는 task trajectory | p. 2 (1. Introduction), p. 3 (2.1. Model & Architecture), p. 3 (2.1. Model & Architecture) |
| Objective/outcome | It has additionally been optimized for complex embodied reasoning problems such as task planning, reasoning for spatial expertise, and task progress estimation. | tracking, balance, skill/task success와 recovery | p. 3 (2.1. Model & Architecture), p. 10 (3.3. Thinking Helps Acting), p. 13 (4.1. Generality) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** This multi-embodiment pre-training allows GR 1.5 to control multiple robots, including the ALOHA, Bi-arm Franka, and Apollo humanoid robots, without any robot-specific post-training, and it ...
- **p. 2 / 1. Introduction - extractive body cue:** ER thinking traces Gemini Robotics 1.5 Gemini Robotics-ER 1.5 Actions Text Figure 1 / The Gemini Robotics 1.5 family of models consists of Gemini Robotics ...
- **p. 3 / 2.1. Model & Architecture - extractive body cue:** The full agentic system consists of an orchestrator and an action model that are implemented by the VLM and the VLA, respectively: • Orchestrator: The ...
- **p. 4 / 2.2. Robot Data - extractive body cue:** The robot data consists of thousands of diverse tasks across these platforms covering a broad range of manipulation skills across a multitude of scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Secondly, GR 1.5 is a Thinking VLA 1See Contributions and Acknowledgments section for full author list.
- **p. 4 / 2.3. Evaluation - extractive body cue:** To improve research iteration speed, we have developed methods for evaluation without real robots in the loop.
- **p. 4 / 2.3. Evaluation - extractive body cue:** This has allowed us to massively scale up the breadth of our evaluations to new objects, scenes, and environments, and to rapidly iterate on architectural ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |
| Embodiment/environment | Over 90% of the evaluation episodes during the development of Gemini Robotics 1.5 were conducted in simulation. | hardware/simulator version and reset protocol | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |
| Dataset/benchmark | Over 90% of the evaluation episodes during the development of Gemini Robotics 1.5 were conducted in simulation. | role, split, size and leakage | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |
| Metric | We use the open-source MuJoCo simulator (Todorov et al., 2012) to generate evaluation scenes for the robot embodiments in this report. | definition, denominator, direction and uncertainty | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |
| Baseline/ablation | For all comparisons reported in this report, we perform A/B/n testing on real robots. | fair input/data/compute/action matching | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 22 / 7. Discussion - extractive body cue:** Its performance on tasks like visual and spatial thinking, task planning, progress estimation, and success detection is critical for robust, real-world robotic applications.

## Why Read It

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 This allows the model to convert visual observations into language-based thoughts, simplify complex instructions, detect task success or failure, propose recovery behaviors, and make the robot's actions more interpretable to human users.를 문제로 두고, This multi-embodiment pre-training allows GR 1.5 to control multiple robots, including the ALOHA, Bi-arm Franka, and Apollo humanoid robots, without any robot-specific post-training, and it also enables zero-shot skill transfer from one ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.1. Model & Architecture), p. 3 (2.1. Model & Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
