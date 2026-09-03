# XSkill: Cross Embodiment Skill Discovery

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v229/xu23a.html.
> PDF retrieval source: https://arxiv.org/pdf/2307.09955. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, cross-embodiment, skill discovery, human video, Imitation Learning, Diffusion
- Official paper: https://proceedings.mlr.press/v229/xu23a.html
- Full-text retrieval: https://arxiv.org/pdf/2307.09955
- Code/Project: https://xskill.cs.columbia.edu/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 il 문제를 이해하기 위해 읽는다. 본문은 With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite the embodiment difference and unexpected execution failures.를 문제로 두고, Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first attempt toward this task XSkill that consists ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Human demonstration videos are a widely available data source for robot learning and an intuitive user interface for expressing desired behavior.
- **p. 1 / Abstract - extractive body cue:** However, directly extracting reusable robot manipulation skills from unstructured human videos is challenging due to the big embodiment difference and unobserved action parameters.
- **p. 1 / Abstract - extractive body cue:** To bridge this embodiment gap, this paper introduces XSkill, an imitation learning framework that 1) discovers a cross-embodiment representation called skill prototypes purely from unlabeled ...
- **p. 1 / Abstract - extractive body cue:** Our experiments in simulation and real-world environments show that the discovered skill prototypes facilitate both skill transfer and composition for unseen tasks, resulting in a ...
- **p. 1 / Abstract - extractive body cue:** The benchmark, code, and qualitative results are on project website.
- **p. 2 / 1 Introduction - extractive body cue:** With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite the embodiment difference ...
- **p. 2 / 1 Introduction - extractive body cue:** Meanwhile, our approach differs from existing work on single-embodiment skill discovery [7, 8, 9], which solely relies on on-robot demonstration data.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first ...
- **p. 1 / 1 Introduction - extractive body cue:** We refer to the task as "Cross-Embodiment Skill Discovery" and introduce our method 7th Conference on Robot Learning (CoRL 2023), Atlanta, USA.
- **p. 2 / 1 Introduction - extractive body cue:** To encourage across-embodiment alignment, we introduce a set of learnable skill prototypes through feature clustering.
- **p. 3 / 3 Approach - extractive body cue:** The XSkill framework consists of three phases: Discover §3.1, Transfer §3.2, and Compose §3.3 that uses three different data sources.
- **p. 1 / 1 Introduction - extractive body cue:** 3) Compose, performing novel compositions of the learned skills to accomplish new tasks.
- **p. 3 / 3 Approach - extractive body cue:** From this video prompt, the algorithm first identifies the order of skills used in the prompt and then composes the skills using the learned policy ...
- **p. 4 / 3 Approach - extractive body cue:** Then, we extract the skill representation zij = ftemporal(vij) from each video clip with a temporal skill encoder consisting of a vision backbone and a ...
- **p. 3 / 3 Approach - extractive body cue:** In the Compose phase, the algorithm takes as input a single human prompt video τ h prompt for a new task that requires an unseen ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the transfer phase, the algorithm uses the robot teleoperation dataset Dr to learn the skill-conditioned visuomotor policy P(a/s, z), where z ∈Z and s includes both robot proprioception and visual observation ... | observation history와 expert trajectory/action | p. 3 (3 Approach), p. 3 (3 Approach) |
| State/latent | transfer, phase, algorithm, uses, robot, teleoperation, dataset, learn, skill-conditioned, visuomotor, policy, where | behavior policy와 temporal action context | p. 3 (3 Approach), p. 3 (3 Approach), p. 2 (1 Introduction) |
| Output/action | From this video prompt, the algorithm first identifies the order of skills used in the prompt and then composes the skills using the learned policy P(a/s, z). | predicted action 또는 action chunk | p. 3 (3 Approach), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | Both ftemporal and fprototype are trained jointly to minimize the CorssEntropy loss between the predicted pij and target qij skill prototypes distributions: Lprototype = | imitation error, task success, robustness와 compounding error | p. 4 (3 Approach), p. 4 (3 Approach) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first ...
- **p. 1 / 1 Introduction - extractive body cue:** We refer to the task as "Cross-Embodiment Skill Discovery" and introduce our method 7th Conference on Robot Learning (CoRL 2023), Atlanta, USA.
- **p. 2 / 1 Introduction - extractive body cue:** To encourage across-embodiment alignment, we introduce a set of learnable skill prototypes through feature clustering.
- **p. 3 / 3 Approach - extractive body cue:** The XSkill framework consists of three phases: Discover §3.1, Transfer §3.2, and Compose §3.3 that uses three different data sources.
- **p. 1 / 1 Introduction - extractive body cue:** 3) Compose, performing novel compositions of the learned skills to accomplish new tasks.
- **p. 7 / 4 Evaluation - extractive body cue:** [XSkill] achieves 70.2% and 60% success (Tab.
- **p. 7 / 4 Evaluation - extractive body cue:** 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Transfer & Composition: During inference, a human demonstration of a new task is given, XSkill first extracts a sequence of skills, which can ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4 Evaluation), p. 7 (4 Evaluation) |
| Embodiment/environment | During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. • Realworld Kitchen: is a new benchmark we introduce to ... | hardware/simulator version and reset protocol | p. 6 (4 Evaluation), p. 6 (4 Evaluation) |
| Dataset/benchmark | For instance, the robot struggles to complete tasks involving grasping the cloth followed by closing the drawer, since no such transition dynamics are present in the collected robot teleoperation dataset. | role, split, size and leakage | p. 6 (4 Evaluation), p. 6 (4 Evaluation), p. 7 (4 Evaluation), p. 7 (4 Evaluation) |
| Metric | The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of completion. | definition, denominator, direction and uncertainty | p. 6 (4 Evaluation), p. 8 (Figure/Table caption), p. 6 (4 Evaluation) |
| Baseline/ablation | 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines. | fair input/data/compute/action matching | p. 7 (4 Evaluation), p. 6 (4 Evaluation), p. 6 (4 Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of a novel task, identifying skills for each ...

## Why Read It

VLA and generalist robot policies의 il 문제를 이해하기 위해 읽는다. 본문은 With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite the embodiment difference and unexpected execution failures.를 문제로 두고, Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first attempt toward this task XSkill that consists ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Approach), p. 4 (3 Approach), p. 3 (3 Approach), p. 4 (3 Approach) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Meanwhile, our approach differs from existing work on single-embodiment skill discovery [7, 8, 9], which solely relies on on-robot demonstration data. (p. 2, 1 Introduction).
- **Actual contribution:** Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first attempt toward this task XSkill ... (p. 2, 1 Introduction).
- **Evaluation boundary:** During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. • Realworld Kitchen: is a new benchmark we ... (p. 6, 4 Evaluation).
- **Explicit failure boundary:** However, directly following the skill sequence ˜z for execution often results in a fragile system that is sensitive to unexpected failures or speed mismatch. (p. 5, B P).
