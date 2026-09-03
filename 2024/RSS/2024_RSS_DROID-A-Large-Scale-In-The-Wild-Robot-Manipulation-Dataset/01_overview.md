# DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2403.12945.
> PDF retrieval source: https://arxiv.org/pdf/2403.12945. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Dataset, in-the-wild, robot manipulation, data diversity, generalist policy
- Official paper: https://arxiv.org/abs/2403.12945
- Full-text retrieval: https://arxiv.org/pdf/2403.12945
- Code/Project: https://droid-dataset.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and actions, which cannot be easily scraped fro ...를 문제로 두고, In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The creation of large, diverse, high-quality robot manipulation datasets is an important stepping stone on the path toward more capable and robust robotic manipulation policies.
- **p. 1 / Abstract - extractive body cue:** As a result, even the most general robot manipulation policies today are mostly trained on data collected in a small number of environments with limited ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a diverse robot manipulation dataset with ...
- **p. 2 / Abstract - extractive body cue:** 76k demonstration trajectories or 350 hours of interaction data, collected across 564 scenes and 86 tasks by 50 data collectors in North America, Asia, and ...
- **p. 2 / Abstract - extractive body cue:** We demonstrate that training with DROID leads to policies with higher performance and improved generalization ability.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Collecting robot manipulation data in diverse environments poses logistical and safety challenges when moving robots outside of controlled lab environments.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig.
- **p. 1 / 13 Institutions - extractive body cue:** 1: We introduce DROID (Distributed Robot Interaction Dataset), an "in-the-wild" robot manipulation dataset with 76k trajectories or 350 hours of interaction data, collected across 564 ...
- **p. 3 / III. DROID DATA COLLECTION SETUP - extractive body cue:** In this section, we introduce our hardware setup and the data collection protocol.
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** The setup consists of a Franka Panda 7DoF robot arm, two adjustable Zed 2 stereo cameras, a wristmounted Zed Mini stereo camera, and an Oculus ...
- **p. 3 / Dataset - extractive body cue:** Collecting such data "in-the-wild" is more common for robot navigation and autonomous driving [4, 18, 28, 48, 49, 55, 57, 64] and enables training of ...
- **p. 6 / IV. DROID DATASET ANALYSIS - extractive body cue:** We use the point of first gripper closing in every episode as a proxy for interactions in the dataset and visualize the 3D location of ...
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** We use the Polymetis controller [33] and record actions both in robot joint space and in end-effector space at a control frequency of 15Hz.
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** For each trajectory, we record the output of all RGB cameras, relevant low level state information from the robot, equivalent robot control commands from various ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For each trajectory, we record the output of all RGB cameras, relevant low level state information from the robot, equivalent robot control commands from various popular action spaces, a data collector ID, ... | multi-view observation, language/task label과 action trajectory | p. 4 (III. DROID DATA COLLECTION SETUP), p. 2 (I. INTRODUCTION) |
| State/latent | trajectory, record, output, RGB, cameras, relevant, level, state, information, robot, equivalent, control | shared representation, embodiment/task identity와 data distribution | p. 4 (III. DROID DATA COLLECTION SETUP), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and actions, which cannot be easily scraped fro ... | dataset sample 또는 learned policy action | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (Dataset) |
| Objective/outcome | We use the same hardware setup across all 13 institutions to streamline data collection while maximizing portability and flexibility. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 4 (III. DROID DATA COLLECTION SETUP), p. 4 (III. DROID DATA COLLECTION SETUP), p. 3 (III. DROID DATA COLLECTION SETUP) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig.
- **p. 1 / 13 Institutions - extractive body cue:** 1: We introduce DROID (Distributed Robot Interaction Dataset), an "in-the-wild" robot manipulation dataset with 76k trajectories or 350 hours of interaction data, collected across 564 ...
- **p. 3 / III. DROID DATA COLLECTION SETUP - extractive body cue:** In this section, we introduce our hardware setup and the data collection protocol.
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** The setup consists of a Franka Panda 7DoF robot arm, two adjustable Zed 2 stereo cameras, a wristmounted Zed Mini stereo camera, and an Oculus ...
- **p. 3 / Dataset - extractive body cue:** Collecting such data "in-the-wild" is more common for robot navigation and autonomous driving [4, 18, 28, 48, 49, 55, 57, 64] and enables training of ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Across the board, we find that DROID improves policy success rate while increasing robustness to scene changes like distractors or novel object instances.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Across all tasks, we find that DROID substantially improves policy performance compared to the diffusion policy trained on in-domain data only.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 7 (V. EXPERIMENTS) |
| Embodiment/environment | Overall, we find that DROID significantly increases diversity in tasks, objects, scenes, viewpoints and interaction locations over existing large scale robot manipulation datasets. | hardware/simulator version and reset protocol | p. 5 (IV. DROID DATASET ANALYSIS), p. 3 (Dataset) |
| Dataset/benchmark | To test how DROID and existing datasets affect policy robustness, we evaluate each task and method in two settings: "in-distribution," which reflects the distribution of tasks in the in-domain demonstrations with noise ... | role, split, size and leakage | p. 5 (IV. DROID DATASET ANALYSIS), p. 3 (Dataset), p. 8 (V. EXPERIMENTS), p. 3 (Dataset) |
| Metric | Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution and OOD performance over both no co-training ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 22 (Figure/Table caption) |
| Baseline/ablation | One of the unique benefits of DROID compared to existing robot datasets is its amount of scene diversity. | fair input/data/compute/action matching | p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / V. EXPERIMENTS - extractive body cue:** To test how DROID and existing datasets affect policy robustness, we evaluate each task and method in two settings: "in-distribution," which reflects the distribution of ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 11: DROID data collection GUI. Top left: Screen for entering feasible tasks for the current scene. Tasks can either be selected from a list ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 12: Qualitative examples of scenes in DROID. We use GPT-4V to categorize scenes into 9 scene types. DROID contains robot manipulation demonstrations in a ...
- **p. 9 / VI. DISCUSSION - extractive body cue:** Our policy learning evaluations show that DROID is a valuable data resource for improving policy performance and robustness, even in comparison to existing large robot ...
- **p. 3 / Dataset - extractive body cue:** Calibration Public Robot Collection MIME [50] 8.3k 20 1 ✗ ✗ ✓ human teleop RoboTurk [36] 2.1k 2 1 ✗ ✗ ✓ human teleop RoboNet ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The out of distribution variant consists of toasting novel objects.

## Why Read It

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and actions, which cannot be easily scraped fro ...를 문제로 두고, In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (IV. DROID DATASET ANALYSIS), p. 4 (III. DROID DATA COLLECTION SETUP), p. 4 (III. DROID DATA COLLECTION SETUP), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and actions, which cannot be easily ... (p. 2, I. INTRODUCTION).
- **Actual contribution:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution and OOD performance over both ... (p. 9, Figure/Table caption).
- **Explicit failure boundary:** Notably, when testing out of distribution performance, the No Co-training baseline performs quite poorly while the co-trained policies are much more effective. (p. 8, V. EXPERIMENTS).
