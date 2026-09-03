# ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=6bKEWevgSd.
> PDF retrieval source: https://arxiv.org/pdf/2412.13211. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Benchmark, home rearrangement, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=6bKEWevgSd
- Full-text retrieval: https://arxiv.org/pdf/2412.13211
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Using these events lists, we define mutually exclusive, collectively exhaustive success and failure modes.를 문제로 두고, We present MS-HAB1, a holistic, open-sourced, home-scale manipulation benchmark with four key features: (1) fast simulation with realistic physics and manipulation, including low-level control, for efficient training, evaluation, and da ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** High-quality benchmarks are the foundation for embodied AI research, enabling significant advancements in long-horizon navigation, manipulation and rearrangement tasks.
- **p. 1 / ABSTRACT - extractive body cue:** However, as frontier tasks in robotics get more advanced, they require faster simulation speed, more intricate test environments, and larger demonstration datasets.
- **p. 1 / ABSTRACT - extractive body cue:** To this end, we present MS-HAB, a holistic benchmark for lowlevel manipulation and in-home object rearrangement.
- **p. 1 / ABSTRACT - extractive body cue:** First, we provide a GPUaccelerated implementation of the Home Assistant Benchmark (HAB).
- **p. 1 / ABSTRACT - extractive body cue:** We support realistic low-level control and achieve over 3x the speed of prior magical grasp implementations at a fraction of the GPU memory usage.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Using these events lists, we define mutually exclusive, collectively exhaustive success and failure modes.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, we provide trajectory categorization statistics for all baselines in Appendix A.6 so future work can gear its methodology to solve frequent failure modes discovered ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We present MS-HAB1, a holistic, open-sourced, home-scale manipulation benchmark with four key features: (1) fast simulation with realistic physics and manipulation, including low-level control, for ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Summary of Contributions: The contributions of MS-HAB are summarized as follows: 1) GPUaccelerated HAB implementation which supports realistic low-level control and achieves over 4300 SPS ...
- **p. 8 / 5 METHODOLOGY - extractive body cue:** (2016), then concatenated with state observations.
- **p. 8 / 5 METHODOLOGY - extractive body cue:** First, we define "events" which occur at any timestep t: 1) Contact: nonzero robot/target pairwise force, 2) Grasped: object not grasped at step t-1 and ...
- **p. 6 / 5 METHODOLOGY - extractive body cue:** Furthermore, the policy must learn action sequences which can reach these grasp poses and retrieve the target object within the specified horizon while keeping the ...
- **p. 6 / 5 METHODOLOGY - extractive body cue:** 5.1 TRAINING REINFORCEMENT LEARNING POLICIES We choose Reinforcement Learning (RL) to learn our subtask policies as RL does not require prior demonstration data, and it ...
- **p. 7 / 5 METHODOLOGY - extractive body cue:** Visual observations are encoded by a NatureCNN (Mnih et al., 2015) and concatenated with state observations.
- **p. 7 / 5 METHODOLOGY - extractive body cue:** Algorithms and Hyperparameters: We stack 3 consecutive frames for image observations to handle partial observability.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We provide brief descriptions of the subtasks below: • Pick[a, optional](xpose): pick object x (from articulation a, if provided). • Place[a, optional](xpose , gpos): place object x in goal g (in articulation ... | standardized observation, action, task state와 evaluation split | p. 4 (3 PRELIMINARIES), p. 6 (5 METHODOLOGY) |
| State/latent | provide, brief, descriptions, subtasks, below, Pick, optional, xpose, object, articulation, provided, Place | benchmark state/goal와 method decision | p. 4 (3 PRELIMINARIES), p. 6 (5 METHODOLOGY), p. 5 (3 PRELIMINARIES) |
| Output/action | Furthermore, the policy must learn action sequences which can reach these grasp poses and retrieve the target object within the specified horizon while keeping the robot under the cumulative collision force limit. | policy/controller trajectory 또는 measured result | p. 6 (5 METHODOLOGY), p. 5 (3 PRELIMINARIES), p. 7 (5 METHODOLOGY) |
| Objective/outcome | As a result, learning successful grasping for multiple objects with different geometries - in addition to whole body control with collision constraints - is difficult. | success metric, robustness, generalization과 reproducibility | p. 6 (5 METHODOLOGY), p. 6 (5 METHODOLOGY), p. 8 (5 METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We present MS-HAB1, a holistic, open-sourced, home-scale manipulation benchmark with four key features: (1) fast simulation with realistic physics and manipulation, including low-level control, for ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Summary of Contributions: The contributions of MS-HAB are summarized as follows: 1) GPUaccelerated HAB implementation which supports realistic low-level control and achieves over 4300 SPS ...
- **p. 8 / 6 RESULTS - extractive body cue:** Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and improving subtask success rate is the most ...
- **p. 10 / 6 RESULTS - extractive body cue:** Does training per-object Pick and Place policies improve subtask success rate compared to allobject policies?
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 8: SAC vs PPO subtask success once rate (%) curves on the train split. Lines are averaged across 3 seeds; since success rate can ...
- **p. 9 / 6 RESULTS - extractive body cue:** Futhermore, we provide an ‘upper bound' on performance based on the success rates of each subtask policy.
- **p. 8 / 6 RESULTS - extractive body cue:** First, our optimistic upper bound shows low expected success rate on the long-horizon tasks.
- **p. 10 / 6 RESULTS - extractive body cue:** So, per-object Pick and Place policies learn improved manipulation when grasping a greater variety of objects, or when manipulating objects in areas with tighter constraints.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (6 RESULTS), p. 10 (6 RESULTS) |
| Embodiment/environment | This is not an issue with magical grasping (Gu et al., 2023a), indicating that low-level control may need more scene diversity. pick_0 place_0 pick_1 place_1 pick_2 place_2 pick_3 place_3 pick_4 place_4 0 ... | hardware/simulator version and reset protocol | p. 9 (6 RESULTS), p. 18 (A.4.1 DATASET SIZE) |
| Dataset/benchmark | We generate 3 datasets with 500 demonstrations per object: 1) place in goal only, 2) drop in goal only, and 3) 50/50 split ("place", "drop", and "split"). | role, split, size and leakage | p. 9 (6 RESULTS), p. 18 (A.4.1 DATASET SIZE), p. 10 (6 RESULTS), p. 18 (A.4.1 DATASET SIZE) |
| Metric | Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and improving subtask success rate is the most direct way to improve overall task completion ... | definition, denominator, direction and uncertainty | p. 8 (6 RESULTS), p. 9 (6 RESULTS), p. 8 (6 RESULTS) |
| Baseline/ablation | Second, TidyHouse and SetTable RL baselines have some gap between upper bound and real completion rate, indicating potential handoff issues or disturbance to prior target objects in success states. | fair input/data/compute/action matching | p. 8 (6 RESULTS), p. 8 (6 RESULTS), p. 10 (6 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), excessive ...
- **p. 24 / A.6.2 DEFINITIONS - extractive body cue:** Eplace = () ∧eexcessive collisions̸ ∈Eplace viii Didn't reach goal failure: Agent grasps x, but cannot manipulate x to within 15cm of gpos. /Eplace/ > ...
- **p. 23 / A.6.2 DEFINITIONS - extractive body cue:** Epick = (econtact, egrasped, . . . , esuccess) ∧/Epick/ > 3 ∧eexcessive collisions̸ ∈Epick iii Success then drop: Agent successfully picks x and returns ...
- **p. 24 / A.6.2 DEFINITIONS - extractive body cue:** First, we define 1placed is latest sequence = (/Eplace/ ≤2 ∧dg x,0 ≤0.15) ∨(iplace,released at goal > iplace,released outside goal ∧iplace,released at goal > iplace,grasped) ...
- **p. 25 / A.6.2 DEFINITIONS - extractive body cue:** Previous failure modes are not applicable, and iopen,slightly opened > iopen,opened ∧ iopen,slightly opened > iopen,closed ∧eexcessive collisions̸ ∈Eopen viii Too slow failure: Agent is ...
- **p. 23 / A.6.2 DEFINITIONS - extractive body cue:** Epick = () vii Can't grasp failure: Agent reaches x, but cannot grasp it.
- **p. 25 / A.6.2 DEFINITIONS - extractive body cue:** If eevent = 1, we add it to Eclose. • Success Modes: if esuccess ∈Eclose, then categorize using the following success modes: i Close success: ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Using these events lists, we define mutually exclusive, collectively exhaustive success and failure modes.를 문제로 두고, We present MS-HAB1, a holistic, open-sourced, home-scale manipulation benchmark with four key features: (1) fast simulation with realistic physics and manipulation, including low-level control, for efficient training, evaluation, and da ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES), p. 8 (5 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
