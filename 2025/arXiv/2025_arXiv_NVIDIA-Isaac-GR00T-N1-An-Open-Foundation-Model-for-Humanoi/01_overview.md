# NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=0.875); canonical paper source: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots.
> PDF retrieval source: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, humanoid, Foundation Models, NVIDIA
- Official paper: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots
- Full-text retrieval: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots
- Code/Project: https://developer.nvidia.com/isaac/gr00t
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=0.875)

## Why This Paper Is Here

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 They demonstrate the effectiveness of training generalist models on web-scale data to enable strong generalization and fast adaptation to downstream tasks.를 문제로 두고, We introduce GR00T N1, an open foundation model for generalist humanoid robots.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** General-purpose robots need a versatile body and an intelligent mind.
- **p. 1 / Abstract - extractive body cue:** Recent advancements in humanoid robots have shown great promise as a hardware platform for building generalist autonomy in the human world.
- **p. 1 / Abstract - extractive body cue:** A robot foundation model, trained on massive and diverse data sources, is essential for enabling the robots to reason about novel situations, robustly handle real-world ...
- **p. 1 / Abstract - extractive body cue:** To this end, we introduce GR00T N1, an open foundation model for humanoid robots.
- **p. 1 / Abstract - extractive body cue:** GR00T N1 is a Vision-Language-Action (VLA) model with a dual-system architecture.
- **p. 1 / 1. Introduction - extractive body cue:** They demonstrate the effectiveness of training generalist models on web-scale data to enable strong generalization and fast adaptation to downstream tasks.
- **p. 2 / 1. Introduction - extractive body cue:** To mitigate the "data island" problem mentioned earlier, we structure the VLA training corpora as a data pyramid, illustrated in Fig.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We introduce GR00T N1, an open foundation model for generalist humanoid robots.
- **p. 2 / 1. Introduction - extractive body cue:** By unifying all data sources across the data pyramid, we construct a consistent dataset where the input consists of the robot state, visual observations, and ...
- **p. 3 / 2. GR00T N1 Foundation Model - extractive body cue:** 1) for generalization and robustness; • We train a massively multi-task, language-conditioned policy that supports a wide range of robot embodiments and enables rapid adaptation ...
- **p. 6 / 2.2. Training Data Generation - extractive body cue:** This enables generating training data that captures many more counterfactual scenarios in the real world without actually collecting teleoperation data for each of these cases ...
- **p. 1 / 1. Introduction - extractive body cue:** Recent progress in robotic hardware, artificial intelligence, and accelerated computing has collectively paved the ground for developing general-purpose robot autonomy.
- **p. 8 / 2.3. Training Details - extractive body cue:** Since the generated videos do not have action labels, we use either latent or inverse dynamics models (IDM) labeled actions (Baker et al., 2022) and ...
- **p. 5 / 2.2. Training Data Generation - extractive body cue:** After training, we take the encoder and use it as an inverse dynamics model; given an 𝑥𝑡and 𝑥𝑡+𝐻pair, we extract the continuous pre-quantized embedding and ...
- **p. 4 / 2.1. Model Architecture - extractive body cue:** To deal with different robot embodiment's state observation and action, we use DiT blocks with an embodiment-aware state and action encoder to embed the robot's ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | By unifying all data sources across the data pyramid, we construct a consistent dataset where the input consists of the robot state, visual observations, and language instruction, and the output is the ... | proprioception, reference pose/motion, visual or language command | p. 2 (1. Introduction), p. 3 (1. Introduction) |
| State/latent | unifying, data, sources, across, pyramid, construct, consistent, dataset, where, input, consists, robot | whole-body pose, balance/contact state와 skill/mode | p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (2. GR00T N1 Foundation Model) |
| Output/action | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots Robot State "Pick up the industry object and place in yellow bin." Joint Positions Joint Velocities Base Position EEF Poses … Tokenize ... | joint/whole-body action, motion target 또는 task trajectory | p. 3 (1. Introduction), p. 3 (2. GR00T N1 Foundation Model), p. 4 (2.1. Model Architecture) |
| Objective/outcome | Pre-training During the pre-training phase, GR00T N1 is trained via flow-matching loss (Equation 1) on a diverse collection of embodiments and data sources, encompassing various real and synthetic robot datasets as well ... | tracking, balance, skill/task success와 recovery | p. 8 (2.3. Training Details), p. 5 (2.1. Model Architecture), p. 5 (2.2. Training Data Generation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We introduce GR00T N1, an open foundation model for generalist humanoid robots.
- **p. 2 / 1. Introduction - extractive body cue:** By unifying all data sources across the data pyramid, we construct a consistent dataset where the input consists of the robot state, visual observations, and ...
- **p. 3 / 2. GR00T N1 Foundation Model - extractive body cue:** 1) for generalization and robustness; • We train a massively multi-task, language-conditioned policy that supports a wide range of robot embodiments and enables rapid adaptation ...
- **p. 6 / 2.2. Training Data Generation - extractive body cue:** This enables generating training data that captures many more counterfactual scenarios in the real world without actually collecting teleoperation data for each of these cases ...
- **p. 1 / 1. Introduction - extractive body cue:** Recent progress in robotic hardware, artificial intelligence, and accelerated computing has collectively paved the ground for developing general-purpose robot autonomy.
- **p. 15 / 4.4. Quantitative Results - extractive body cue:** GR00T-N1-2B, achieves a significantly higher success rate across all tasks, outperforming Diffusion Policy by 32.4% in the 10% Data setting and by 30.4% in the ...
- **p. 15 / 4.4. Quantitative Results - extractive body cue:** GR00T-N1-2B achieves a success rate of 76.6% (11.5/15) in the first coordinated setting and 73.3% (11/15) in the second setting involving novel object manipulation.
- **p. 14 / 4.3. Experiment Setup - extractive body cue:** Evaluation Protocol For simulated benchmark evaluation, we report the average success rate over 100 trials, taking the maximum score of the last 5 checkpoints, where ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 15 (4.4. Quantitative Results), p. 15 (4.4. Quantitative Results) |
| Embodiment/environment | We generate 1000 demonstrations for each task using the DexMimicGen data generation system and evaluate the model's ability to generalize to novel object configurations. • GR-1 Tabletop Tasks (24 tasks, GR-1) This ... | hardware/simulator version and reset protocol | p. 12 (4.1. Simulation Benchmarks), p. 14 (4.2. Real-World Benchmarks) |
| Dataset/benchmark | We trained the models for 100 epochs on a dataset comprising 3,000 real-world robot data samples with language annotations, each recorded at 480P resolution and consisting of 81 frames. | role, split, size and leakage | p. 12 (4.1. Simulation Benchmarks), p. 14 (4.2. Real-World Benchmarks), p. 10 (3.2. Synthetic Datasets), p. 17 (4.5. Qualitative Results) |
| Metric | Evaluation Protocol For simulated benchmark evaluation, we report the average success rate over 100 trials, taking the maximum score of the last 5 checkpoints, where checkpoints are written every 500 training steps, ... | definition, denominator, direction and uncertainty | p. 14 (4.3. Experiment Setup), p. 14 (4.3. Experiment Setup), p. 15 (4.4. Quantitative Results) |
| Baseline/ablation | GR00T N1 outperforms both baselines, especially on the GR-1 task where it outperforms by more than 17 %. | fair input/data/compute/action matching | p. 15 (4.4. Quantitative Results), p. 15 (4.4. Quantitative Results), p. 16 (4.5. Qualitative Results) |

## Explicit Limitations and Failure Boundary

- **p. 24 / 6. Conclusions - extractive body cue:** (Top) Post-trained GR00T-N1-2B successfully places the cucumber into the basket, whereas the Diffusion Policy fails due to an inaccurate grasp.
- **p. 17 / 4.6. Limitations - extractive body cue:** In future work, we aim to extend its capabilities to tackle long-horizon loco-manipulation, which will require advancements in humanoid hardware, model architecture, and training corpora.
- **p. 16 / 4.5. Qualitative Results - extractive body cue:** In contrast, the post-trained checkpoint fails in this scenario.
- **p. 17 / 4.6. Limitations - extractive body cue:** Furthermore, we plan to explore novel model architectures and pre-training strategies to improve the robustness and generalization capabilities of our generalist robot models.
- **p. 22 / 6. Conclusions - extractive body cue:** Videos that fail this criterion undergo re-captioning, with the videos downsampled to 16 frames at 256P resolution for this process.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: GR00T N1 Model Architecture. GR00T N1 is trained on a diverse set of embodiments ranging from single-arm robot arms to bimanual humanoid dexterous ...
- **p. 14 / 4.3. Experiment Setup - extractive body cue:** It employs a U-Net architecture that progressively removes noise from random samples to generate precise robot actions conditioned on observation sequences.

## Why Read It

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 They demonstrate the effectiveness of training generalist models on web-scale data to enable strong generalization and fast adaptation to downstream tasks.를 문제로 두고, We introduce GR00T N1, an open foundation model for generalist humanoid robots.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (2.1. Model Architecture), p. 8 (2.3. Training Details), p. 5 (2.2. Training Data Generation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (36 pages; PyMuPDF text; extraction quality: high; title-token overlap: 0.875). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** To mitigate the "data island" problem mentioned earlier, we structure the VLA training corpora as a data pyramid, illustrated in Fig. (p. 2, 1. Introduction).
- **Actual contribution:** We introduce GR00T N1, an open foundation model for generalist humanoid robots. (p. 2, 1. Introduction).
- **Evaluation boundary:** Figure 9: Average Success Rate (%) across 24 Tasks in simulation and 8 tasks in the real world. In the RoboCasa simulation, we show all post-training results using 30, 100, ... (p. 16, Figure/Table caption).
- **Explicit failure boundary:** (Top) Post-trained GR00T-N1-2B successfully places the cucumber into the basket, whereas the Diffusion Policy fails due to an inaccurate grasp. (p. 24, 6. Conclusions).
