# AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://opendrivelab.com/AgiBot-World/.
> PDF retrieval source: https://arxiv.org/pdf/2503.06669. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Dataset, multi-embodiment, long-horizon manipulation, robot data, humanoid, generalist policy
- Official paper: https://opendrivelab.com/AgiBot-World/
- Full-text retrieval: https://arxiv.org/pdf/2503.06669
- Code/Project: https://github.com/OpenDriveLab/AgiBot-World
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 humanoid 문제를 이해하기 위해 읽는다. 본문은 While significant progress has been made in general-purpose foundational models for natural language processing [1] and computer vision [2], robotics lags behind due to the difficulty of (high-quality) data collection.를 문제로 두고, Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes latent action ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We explore how scalable robot data can address real-world challenges for generalized robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** Introducing AgiBot World, a large-scale platform comprising over 1 million trajectories across 217 tasks in five deployment scenarios, we achieve an order-of-magnitude increase in data ...
- **p. 1 / Abstract - extractive body cue:** Accelerated by a standardized collection pipeline with human-in-the-loop verification, AgiBot World guarantees high-quality and diverse data distribution.
- **p. 1 / Abstract - extractive body cue:** It is extensible from grippers to dexterous hands and visuo-tactile sensors for fine-grained skill acquisition.
- **p. 1 / Abstract - extractive body cue:** Building on top of data, we introduce Genie Operator-1 (GO-1), a novel generalist policy that leverages latent action representations to maximize data utilization, demonstrating predictable ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While significant progress has been made in general-purpose foundational models for natural language processing [1] and computer vision [2], robotics lags behind due to the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge [5].

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data.
- **p. 7 / 2) Implementation Details - extractive body cue:** The inclusion of the latent planner yields an average improvement of 0.12 task completion score.
- **p. 7 / 2) Implementation Details - extractive body cue:** We choose the open-source RDT [10] model to study how much the AgiBot World dataset can help policy learning.
- **p. 8 / 2) Implementation Details - extractive body cue:** How does data quality impact policy learning?
- **p. 8 / 2) Implementation Details - extractive body cue:** Specifically, we provide an ablation study by fine-tuning an RDT model using both verified (528 trajectories) and unverified (482 trajectories) data from the "Wipe Table" ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes latent action ... | proprioception, reference pose/motion, visual or language command | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| State/latent | Following, dataset, address, limitations, previous, robot, foundation, models, heavily, rely, indomain, datasets | whole-body pose, balance/contact state와 skill/mode | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/action | 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data. | joint/whole-body action, motion target 또는 task trajectory | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 7 (2) Implementation Details) |
| Objective/outcome | For GO1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps. | tracking, balance, skill/task success와 recovery | p. 7 (2) Implementation Details) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Further analysis on: a) how model performance scales with data size, and b) the impact of filtering undesir- able data through manual review ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Is GO-1 a more powerful robot generalist policy? We evaluate GO-1 against previous generalist policy RDT-1B and our baseline without the latent planner, ...
- **p. 8 / 2) Implementation Details - extractive body cue:** 7(b), being larger in quantity does not necessarily translate to improved performance, while a smaller set of human-verified data yields a 0.18 boost in the ...
- **p. 6 / 1) Evaluation Tasks - extractive body cue:** Each episode scores 1.0 for full success, with fractional scores for partial success, enabling a nuanced performance assessment.
- **p. 3 / Dataset - extractive body cue:** The deployment results are adopted as feedback to improve the collection protocol. suffers from significant variability in embodiments, observation perspectives, and inconsistent data quality, limiting ...
- **p. 4 / Dataset - extractive body cue:** This feedback-driven methodology ensures continuous improvement in data quality.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | Based on the hardware platform developed by us, AgiBot G1, we construct AgiBot Worldan open-source robot manipulation dataset collected by more than 100 homogeneous robots, providing high-quality data for challenging tasks spanning ... | hardware/simulator version and reset protocol | p. 3 (Dataset), p. 5 (Dataset) |
| Dataset/benchmark | Prior datasets above generally face limitations in data scale, task practicality, and scenario naturalness, compounded by inadequate quality assurance and hardware restrictions, which impedes generalist policy training. | role, split, size and leakage | p. 3 (Dataset), p. 5 (Dataset), p. 3 (Dataset), p. 4 (Dataset) |
| Metric | Fig. 7: Further analysis on: a) how model performance scales with data size, and b) the impact of filtering undesir- able data through manual review on policy learning. World alpha dataset, despite ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 6 (1) Evaluation Tasks), p. 7 (2) Implementation Details) |
| Baseline/ablation | Across all tasks and comparisons, GO-1 outperforms baselines by a large margin. | fair input/data/compute/action matching | p. 7 (1) Evaluation Tasks), p. 7 (1) Evaluation Tasks), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Dataset - extractive body cue:** Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error states) and tasks with dexterous hands.
- **p. 3 / Dataset - extractive body cue:** Hand Failure Recovery Human-inthe-loop Collection RoboNet [11] 162k n/a 10 ✗ ✗ Single ✗ ✗ ✗ scripted BridgeData [12] 7.2k 4 12 ✗ ✗ Single ...
- **p. 4 / Dataset - extractive body cue:** These trajectories, referred to as failure recovery data, constitute approximately one percent of the dataset.
- **p. 4 / Dataset - extractive body cue:** Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: Discard Edge-side Cloud-side Task Succeed Failed No ...
- **p. 8 / 2) Implementation Details - extractive body cue:** 7(b), being larger in quantity does not necessarily translate to improved performance, while a smaller set of human-verified data yields a 0.18 boost in the ...
- **p. 5 / Dataset - extractive body cue:** This ensures that our dataset adequately represents a broad spectrum of skills, providing sufficient data for each to support robust policy learning.
- **p. 7 / 1) Evaluation Tasks - extractive body cue:** 0.47) and out-of-distribution scenarios (0.67 v.s.

## Why Read It

RL, IL, offline learning, and robot data의 humanoid 문제를 이해하기 위해 읽는다. 본문은 While significant progress has been made in general-purpose foundational models for natural language processing [1] and computer vision [2], robotics lags behind due to the difficulty of (high-quality) data collection.를 문제로 두고, Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes latent action ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (2) Implementation Details), p. 7 (2) Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge [5]. (p. 1, I. INTRODUCTION).
- **Actual contribution:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 1: Introducing AgiBot World Colosseo, an open-sourced large-scale manipulation platform comprising data, models, benchmarks and ecosystem. AgiBot World stands out for its unparalleled scale and diversity compared to prior ... (p. 1, Figure/Table caption).
- **Explicit failure boundary:** Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: Discard Edge-side Cloud-side Task Succeed Failed No Yes Validity Varification Model Training ... (p. 4, Dataset).
