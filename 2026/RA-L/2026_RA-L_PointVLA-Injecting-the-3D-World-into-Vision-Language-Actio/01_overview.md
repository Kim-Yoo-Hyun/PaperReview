# PointVLA: Injecting the 3D World into Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.07511.
> PDF retrieval source: https://arxiv.org/pdf/2503.07511. Reading tracker status/evidence was not changed.

- Year/Venue: 2026 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: VLA, Vision-Language Model, 3D Vision, Reinforcement Learning
- Official paper: https://arxiv.org/abs/2503.07511
- Full-text retrieval: https://arxiv.org/pdf/2503.07511
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 vla 문제를 이해하기 위해 읽는다. 본문은 This represents a crucial limitation because humans perceive and interact with the world in three dimensions.를 문제로 두고, In this paper, we introduce PointVLA, a novel framework that integrates point clouds into pre-trained visionlanguage-action models.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models excel at robotic tasks by leveraging large-scale 2D vision-language pretraining, but their reliance on RGB images limits spatial reasoning critical for real-world ...
- **p. 1 / Abstract - extractive body cue:** Retraining these models with 3D data is computationally prohibitive, while discarding existing 2D datasets wastes valuable resources.
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we propose PointVLA, a framework that enhances pre-trained VLAs with point cloud inputs without requiring retraining.
- **p. 1 / Abstract - extractive body cue:** Our method freezes the vanilla action expert and injects 3D features via a lightweight modular block.
- **p. 1 / Abstract - extractive body cue:** To identify the most effective way of integrating point cloud representations, we conduct a skip-block analysis to pinpoint less useful blocks in the vanilla action ...
- **p. 2 / 1. Introduction - extractive body cue:** This represents a crucial limitation because humans perceive and interact with the world in three dimensions.
- **p. 2 / 1. Introduction - extractive body cue:** The lack of comprehensive 3D spatial information in training data hinders a robot's ability to develop a deep understanding of its environment.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce PointVLA, a novel framework that integrates point clouds into pre-trained visionlanguage-action models.
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose a 3D modular block that injects point cloud information directly into the action expert.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** To circumvent these issues, we propose a paradigm that treats 3D point cloud data as a complementary conditioning signal rather than a primary input modality.
- **p. 3 / 3. Methodology - extractive body cue:** This training enables effective alignment of image and text representations within a shared embedding space.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** However, as this is not the core novelty of our approach, we leave it for future discussion.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** For selected blocks in the action expert, we first apply an MLP layer as an adapter for each block, followed by an addition operation to ...
- **p. 3 / 3. Methodology - extractive body cue:** Subsequently, an 'action expert' module translates the VLM's state information into robot actions.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** The vanilla action expert remains frozen, while the new point cloud representation is integrated into the action expert through a modular network.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | PointVLA Framework Vision-Language Model Action Expert Point Cloud Injector Robot Action Block_12 Block_13 Block_16 Block_1 Injection Block_1 Injection Block_2 Injection Block_5 Zero Linear Adapter Zero Linear Point Cloud Injector Zero ... | image/video, language instruction, proprioception과 history | p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology) |
| State/latent | PointVLA, Framework, Vision-Language, Model, Action, Expert, Point, Cloud, Injector, Robot, Block_12, Block_13 | language-grounded task state와 action-policy context | p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology), p. 4 (3.2. Injecting Point Cloud into VLA) |
| Output/action | The VLM acts as the model's 'brain,' processing instructions and current visual input to understand the task state. | continuous action, pose 또는 action chunk | p. 3 (3. Methodology), p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology) |
| Objective/outcome | First, the computational cost would be prohibitively high due to the required conditioning blocks. | instruction following, task success, generalization과 latency | p. 4 (3.2. Injecting Point Cloud into VLA), p. 4 (3.2. Injecting Point Cloud into VLA), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce PointVLA, a novel framework that integrates point clouds into pre-trained visionlanguage-action models.
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose a 3D modular block that injects point cloud information directly into the action expert.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** To circumvent these issues, we propose a paradigm that treats 3D point cloud data as a complementary conditioning signal rather than a primary input modality.
- **p. 3 / 3. Methodology - extractive body cue:** This training enables effective alignment of image and text representations within a shared embedding space.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** However, as this is not the core novelty of our approach, we leave it for future discussion.
- **p. 8 / 4.6. Experimental Results on Simulation Bench - extractive body cue:** Notably, across all tasks and diverse settings, our proposed PointVLA achieves the highest average success rate, regardless of whether it is trained on 20 or ...
- **p. 8 / 4.6. Experimental Results on Simulation Bench - extractive body cue:** The mean and standard deviation of these success rates were computed to obtain the experimental results presented below.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** We show experimental results on the bottom table. sented in Table 6, where our method outperforms all baselines in this scenario.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.6. Experimental Results on Simulation Bench), p. 8 (4.6. Experimental Results on Simulation Bench) |
| Embodiment/environment | Following the training setup in RoboTwin, the policy was trained using three random seeds (0, 1, 2) without cherry picking for each experiment. | hardware/simulator version and reset protocol | p. 8 (4.6. Experimental Results on Simulation Bench), p. 5 (4. Experiment) |
| Dataset/benchmark | These tasks assess the model's capability to manage both independent and coordinated robot movements across diverse scenarios. | role, split, size and leakage | p. 8 (4.6. Experimental Results on Simulation Bench), p. 5 (4. Experiment), p. 6 (4.2. Few-Shot Multi-Tasking), p. 6 (4.2. Few-Shot Multi-Tasking) |
| Metric | The mean and standard deviation of these success rates were computed to obtain the experimental results presented below. | definition, denominator, direction and uncertainty | p. 8 (4.6. Experimental Results on Simulation Bench), p. 6 (4.2. Few-Shot Multi-Tasking), p. 7 (4.2. Few-Shot Multi-Tasking) |
| Baseline/ablation | Figure 6. Experimental results on few-shot multi-tasking on bimanual AgileX. last checkpoint for evaluation to avoid cherry picking. We set chunk size to 50 for all tasks. Baseline. In our experiments, we ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 6 (4.1. Implementation Details), p. 7 (4.2. Few-Shot Multi-Tasking) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** Notably, the Diffusion Policy fails in most cases, likely because the sample size for each task is too small, causing the action representation space to ...
- **p. 8 / 4.4. Real-vs-Photo Discrimination - extractive body cue:** Since the model believes the object is present but continuously fails to grasp it, it enters a repetitive grasping loop.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** Furthermore, even increasing the model size (ScaleDP-1B) does not lead to significant improvement.
- **p. 8 / 4.5. Height Adaptability - extractive body cue:** Our observations show that conventional 2D-based VLA models, such as OpenVLA [25], DP [9], ScaleDP-1B [57], and DexVLA [46] all failed in this scenario.

## Why Read It

Robotics-enabling 3D perception의 vla 문제를 이해하기 위해 읽는다. 본문은 This represents a crucial limitation because humans perceive and interact with the world in three dimensions.를 문제로 두고, In this paper, we introduce PointVLA, a novel framework that integrates point clouds into pre-trained visionlanguage-action models.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology), p. 4 (3.2. Injecting Point Cloud into VLA), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
