# Problem - RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.00595; PDF retrieval source: https://arxiv.org/pdf/2307.00595. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Firstly, there is a lack of large and diverse robotic manipulation datasets in this field [B]], despite the community's long-standing eagerness for such datasets.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** A key challenge for robotic manipulation in open domains is how to acquire diverse and generalizable skills for robots.
- **p. 1 / Abstract - extractive body cue:** Recent progress in one-shot imitation learning and robotic foundation models have shown promise in transferring trained policies to new tasks based on demonstrations.
- **p. 1 / Abstract - extractive body cue:** This feature is attractive for enabling robots to acquire new skills and improve their manipulative ability.
- **p. 1 / Abstract - extractive body cue:** However, due to limitations in the training dataset, the current focus of the community has mainly been on simple cases, such as push or pick-place ...
- **p. 1 / Abstract - extractive body cue:** In reality, there are many complex skills, some of which may even require both visual and tactile perception to solve.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Firstly, there is a lack of large and diverse robotic manipulation datasets in this field [B]], despite the community's long-standing eagerness for such datasets.
- **p. 1 / I. INTRODUCTION - extractive body cue:** These challenges include the arduous task of configuring diverse robot platforms, creating varied environments, and gathering manipulation trajectories, which require significant effort and resources.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Firstly, there is a lack of large and diverse robotic manipulation datasets in this field [B]], despite the community's long-standing eagerness for ... | 여러 로봇팔의 시연 데이터와 Flexiv 블록 옮기기 | body wording is the source claim |
| Observation / input | Proprioception encompasses joint angles/torques, end-effector Cartesian pose and gripper states. | 기체별 RGB-D·힘·관절·소리 및 일부 촉각 기록, ACT 평가의 RGB·행동 시연 | exact sensor/frame/preprocessing from PDF body |
| State / latent | Proprioception, encompasses, joint, angles/torques, end-effector, Cartesian, pose, gripper, states, sequence | 보정된 카메라·로봇 좌표와 시간 정렬 시연 | notation and tensor shape require body check |
| Output / action | Additionally, tele-operation, without, force, feedback, degrades, manipulation, efficiency | RH20T 시연 및 ACT의 팔·그리퍼 행동 | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | 시연 수별 도달·집기·놓기 성공 | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: Proprioception, encompasses, joint, angles/torques, end-effector, Cartesian, pose, gripper, states, sequence | p. 3 (III. RH20T DATASET), p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Decision / output variable | normalized sample or downstream action; body terms: introduce, robotic, manipulation, dataset, RobotHuman, demonstration, RH20T, community | p. 3 (III. RH20T DATASET), p. 3 (III. RH20T DATASET) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: Properties, RH20T, designed, objective, enabling, general, robotic, manipulation | p. 3 (III. RH20T DATASET), p. 3 (III. RH20T DATASET) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. RH20T DATASET), p. 3 (III. RH20T DATASET), p. 1 (Abstract) |
| Success / guarantee | cross-domain transfer and task performance | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** These challenges include the arduous task of configuring diverse robot platforms, creating varied environments, and gathering manipulation trajectories, which require significant effort and resources.

## What the Paper Changes

PDF body contribution framing (p. 3 (III. RH20T DATASET), p. 3 (III. RH20T DATASET)): We introduce our robotic manipulation dataset, RobotHuman demonstration in 20TB (RH20T), to the community.

- **p. 3 / III. RH20T DATASET - extractive body cue:** [TM1 c) Scale: Our dataset consists of over 110,000 robot sequences and an equal number of human sequences, with more than 50 million images collected ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | The current limitations of this paper are that (i) the cost of data collection is expensive and (ii) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | These results demonstrate that leveraging the diverse training data from our dataset enhances the adaptability and robustness of ... | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. RH20T DATASET), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (III. RH20T DATASET). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. RH20T DATASET), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (III. RH20T DATASET), objective p. 3 (III. RH20T DATASET), p. 3 (III. RH20T DATASET).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
