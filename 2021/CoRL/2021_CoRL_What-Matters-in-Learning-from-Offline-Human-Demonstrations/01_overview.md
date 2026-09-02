# What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v164/mandlekar22a.html.
> PDF retrieval source: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2021 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Imitation Learning, offline learning, robot dataset, Benchmark, robomimic
- Aliases: RoboMimic
- Official paper: https://proceedings.mlr.press/v164/mandlekar22a.html
- Full-text retrieval: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf
- Code/Project: https://robomimic.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Unfortunately, a lack of suitable benchmark and human datasets have made studying this setting difficult.를 문제로 두고, We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Imitating human demonstrations is a promising approach to endow robots with various manipulation capabilities.
- **p. 1 / Abstract - extractive body cue:** While recent advances have been made in imitation learning and batch (offline) reinforcement learning, a lack of open-source human datasets and reproducible learning methods make ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we conduct an extensive study of six offline learning algorithms for robot manipulation on five simulated and three real-world multi-stage manipulation tasks ...
- **p. 1 / Abstract - extractive body cue:** Our study analyzes the most critical challenges when learning from offline human data for manipulation.
- **p. 1 / Abstract - extractive body cue:** Based on the study, we derive a series of lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of the ...
- **p. 2 / 1 Introduction - extractive body cue:** Unfortunately, a lack of suitable benchmark and human datasets have made studying this setting difficult.
- **p. 2 / 1 Introduction - extractive body cue:** Studying these challenges in the context of robot manipulation and human-provided datasets could be a stepping stone to closing the gap between robot and human ...

## Core Idea

- **p. 3 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.
- **p. 2 / 1 Introduction - extractive body cue:** We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle to learn from ...
- **p. 3 / Dataset - extractive body cue:** Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers ...
- **p. 4 / Dataset - extractive body cue:** We collected these datasets by first training a state-of-the-art RL algorithm [30] on the Lift and Can task, taking agent checkpoints that are saved regularly ...
- **p. 3 / Dataset - extractive body cue:** In our study, we explore how agent design decisions affect policy performances, including the choice of agent architecture, agent observation space, and hyperparameter choices per ...
- **p. 1 / Abstract - extractive body cue:** Based on the study, we derive a series of lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of the ...
- **p. 2 / 1 Introduction - extractive body cue:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, ...
- **p. 1 / Abstract - extractive body cue:** While recent advances have been made in imitation learning and batch (offline) reinforcement learning, a lack of open-source human datasets and reproducible learning methods make ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Offline policy learning is sensitive to the state and action space coverage in the dataset, and by extension, the size of the dataset itself. | standardized observation, action, task state와 evaluation split | p. 3 (Dataset), p. 4 (Dataset) |
| State/latent | Offline, policy, learning, sensitive, state, action, space, coverage, dataset, extension, size, itself | benchmark state/goal와 method decision | p. 3 (Dataset), p. 4 (Dataset), p. 2 (1 Introduction) |
| Output/action | To study the effect of observation modalities, we capture a diverse set of sensor streams when collecting the dataset, including end-effector, gripper fingers, and joints, groundtruth object poses, and images from an ... | policy/controller trajectory 또는 measured result | p. 4 (Dataset), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers from the fact that the training objective ... | success metric, robustness, generalization과 reproducibility | p. 3 (Dataset), p. 1 (Abstract), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.
- **p. 3 / Dataset - extractive body cue:** Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers ...
- **p. 6 / 4 Experiments - extractive body cue:** However, BC-RNN outperforms BC on all datasets (7%-35% improvement).
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: (left) Effect of Policy Selection Criteria. We compare how performance decreases when choosing the policy to evaluate by using the lowest validation loss, ...
- **p. 5 / 4 Experiments - extractive body cue:** 4.1 Algorithm Comparison on Single and Multi-Human Demonstrations (C1, C2) We trained and evaluated all algorithms on the Proficient-Human (PH) and Multi-Human (MH) datasets and ...
- **p. 7 / 4 Experiments - extractive body cue:** We first note that less complex tasks (Lift, Can) can yield proficient policies (75%-100% success rate) using a small fraction of the data (20%).
- **p. 8 / 4 Experiments - extractive body cue:** We train BC-RNN and report the final policy checkpoint success rate, over 30 rollouts, due to the time-consuming nature of real world policy evaluation.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 3 (Dataset), p. 6 (4 Experiments) |
| Embodiment/environment | We collected 3 additional real-world datasets with a Franka robotic arm - Lift (Real), Can (Real), and Tool Hang (Real). | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 4 (Dataset) |
| Dataset/benchmark | Appendix B shows the average trajectory lengths in each data subset - lower quality datasets contain demonstrations that take more time to solve the task. | role, split, size and leakage | p. 8 (4 Experiments), p. 4 (Dataset), p. 6 (4 Experiments), p. 4 (Dataset) |
| Metric | Figure 3: Effect of Dataset Size. We study how the BC-RNN success rate changes when lowering the quantity of data to 20% and 50%. Results show that less complex tasks (Lift, Can) ... | definition, denominator, direction and uncertainty | p. 5 (Figure/Table caption), p. 3 (Dataset), p. 3 (Figure/Table caption) |
| Baseline/ablation | BC-RNN is a strong baseline on suboptimal human data, but there is room for improvement. | fair input/data/compute/action matching | p. 6 (4 Experiments), p. 4 (Dataset), p. 5 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", ...
- **p. 6 / 4 Experiments - extractive body cue:** There is a strong expectation for batch RL algorithms to be able to distinguish between actions leading to successful placement and actions leading to task ...
- **p. 6 / 4 Experiments - extractive body cue:** The final row of Table 2 shows additional results on a diagnostic dataset termed Can-Paired, where a single operator collected 2 demonstrations for each of ...
- **p. 8 / 5 Discussion - extractive body cue:** In this section, we summarize the lessons from our study and make recommendations for future work.
- **p. 3 / Dataset - extractive body cue:** Differences in supervisor proficiency can manifest in many ways, such as large variations in trajectory length and noise in robot movement or mistakes (e.g. missed ...
- **p. 3 / Dataset - extractive body cue:** While recent batch RL algorithms have shown an excellent ability to learn from mixed quality machine-generated datasets [26, 27], we empirically find that they fail ...

## Why Read It

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Unfortunately, a lack of suitable benchmark and human datasets have made studying this setting difficult.를 문제로 두고, We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (Dataset) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
