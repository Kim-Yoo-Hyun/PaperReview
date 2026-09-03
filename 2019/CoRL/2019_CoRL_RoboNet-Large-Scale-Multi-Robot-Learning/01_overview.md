# RoboNet: Large-Scale Multi-Robot Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v100/dasari20a.html.
> PDF retrieval source: https://proceedings.mlr.press/v100/dasari20a.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Dataset, multi-robot, manipulation
- Official paper: https://proceedings.mlr.press/v100/dasari20a.html
- Full-text retrieval: https://proceedings.mlr.press/v100/dasari20a.html
- Code/Project: https://www.robonet.wiki/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 However, when trained in a single environment, robot learning algorithms, including visual foresight and inverse models, do not generalize to large domain variations, such as different robot arms, grippers, viewpoints, and backgrounds, ...를 문제로 두고, Our main contributions therefore consist of the RoboNet dataset, and an experimental evaluation that studies our framework for multi-robot, multi-domain model-based reinforcement learning based on extensions of the visual foresight algo ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robot learning has emerged as a promising tool for taming the complexity and diversity of the real world.
- **p. 1 / Abstract - extractive body cue:** Methods based on high-capacity models, such as deep networks, hold the promise of providing effective generalization to a wide range of open-world environments.
- **p. 1 / Abstract - extractive body cue:** However, these same methods typically require large amounts of diverse training data to generalize effectively.
- **p. 1 / Abstract - extractive body cue:** In contrast, most robotic learning experiments are small-scale, single-domain, and single-robot.
- **p. 1 / Abstract - extractive body cue:** This leads to a frequent tension in robotic learning: how can we learn generalizable robotic controllers without having to collect impractically large amounts of data ...
- **p. 2 / 1 Introduction - extractive body cue:** However, when trained in a single environment, robot learning algorithms, including visual foresight and inverse models, do not generalize to large domain variations, such as ...
- **p. 2 / 1 Introduction - extractive body cue:** We use RoboNet to study the viability of large-scale data-driven robot learning, as a means to attain broad generalization across robots and scenes. show that ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions therefore consist of the RoboNet dataset, and an experimental evaluation that studies our framework for multi-robot, multi-domain model-based reinforcement learning based on ...
- **p. 1 / 1 Introduction - extractive body cue:** Instead, we propose the opposite - using dramatically larger and more varied datasets collected in the real world.
- **p. 1 / 1 Introduction - extractive body cue:** Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action sequences recorded from ...
- **p. 2 / 1 Introduction - extractive body cue:** We show that, when trained on RoboNet, we can acquire models that generalize in zero shot to novel objects, novel viewpoints, and novel table surfaces.
- **p. 12 / C Database Implementation Details - extractive body cue:** We provide code infrastructure that allows a user to filter certain subsets of attributes for training and testing.
- **p. 13 / C Database Implementation Details - extractive body cue:** We collected 300 new trajectories with a Robotiq 2-finger gripper, which differs significantly in visual appearance and dimensions from the Weiss Robotics gripper used in ...
- **p. 13 / C Database Implementation Details - extractive body cue:** executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is determined by human ...
- **p. 12 / C Database Implementation Details - extractive body cue:** New trajectory attributes can be added easily.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action sequences recorded from 7 robots, interacting with hundreds of objects, ... | multi-view observation, language/task label과 action trajectory | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | Inspired, breadth, ImageNet, dataset, introduce, RoboNet, containing, roughly, trajectories, video, action, sequences | shared representation, embodiment/task identity와 data distribution | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | Visual foresight uses an action-conditioned video prediction model trained on the collected data to plan actions that achieve user-specified goals. | dataset sample 또는 learned policy action | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 13 (C Database Implementation Details) |
| Objective/outcome | coverage, cross-embodiment transfer, data efficiency와 task success | coverage, cross-embodiment transfer, data efficiency와 task success | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions therefore consist of the RoboNet dataset, and an experimental evaluation that studies our framework for multi-robot, multi-domain model-based reinforcement learning based on ...
- **p. 1 / 1 Introduction - extractive body cue:** Instead, we propose the opposite - using dramatically larger and more varied datasets collected in the real world.
- **p. 1 / 1 Introduction - extractive body cue:** Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action sequences recorded from ...
- **p. 2 / 1 Introduction - extractive body cue:** We show that, when trained on RoboNet, we can acquire models that generalize in zero shot to novel objects, novel viewpoints, and novel table surfaces.
- **p. 12 / C Database Implementation Details - extractive body cue:** We provide code infrastructure that allows a user to filter certain subsets of attributes for training and testing.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 5: Evaluation results for adaptation to an unseen Baxter robot. The model pre-trained on RoboNet's Sawyer data, achieves the best performance when fine- tuned ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Example task of grasping and moving a thin plastic cup with the Franka robot, using visual foresight pre-trained on RoboNet w/o Franka and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 6: Inverse model results on 5 reaching tasks. The model is success- ful across multiple robot platforms and generalizes to a new viewpoint. To ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | However, these results do demonstrate that visual foresight models can adapt to moderate morphological changes using a modest amount of data. t = 0 t = 3 t = 6 t = ... | hardware/simulator version and reset protocol | p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details) |
| Dataset/benchmark | D Description of Benchmarking Tasks For all control benchmarks we used object relocation tasks from a set of fixed initial positions towards a set of fixed goal positions marked on a table. | role, split, size and leakage | p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details), p. 12 (C Database Implementation Details), p. 12 (C Database Implementation Details) |
| Metric | Table 2: Evaluation of viewpoint generalization, showing the average distance to the goal after ex- ecuting the action sequence and standard error. A model trained on multiple views can better gener- alize ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 13 (C Database Implementation Details), p. 6 (Figure/Table caption) |
| Baseline/ablation | Table 4: Results for adapta- tion to an unseen Franka robot. The model pre-trained on RoboNet without the Franka, R3, and Fetch data, achieves the best performance when fine-tuned with 400 trajecto- ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 13 (Figure/Table caption), p. 13 (C Database Implementation Details) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6 Discussion - extractive body cue:** Next, we discuss limitations of the dataset and evaluation, and additional directions for future work.
- **p. 8 / 6 Discussion - extractive body cue:** While our results demonstrated a large degree of generalization, a number of important limitations remain, which we aim to study in future work.

## Why Read It

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 However, when trained in a single environment, robot learning algorithms, including visual foresight and inverse models, do not generalize to large domain variations, such as different robot arms, grippers, viewpoints, and backgrounds, ...를 문제로 두고, Our main contributions therefore consist of the RoboNet dataset, and an experimental evaluation that studies our framework for multi-robot, multi-domain model-based reinforcement learning based on extensions of the visual foresight algo ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
