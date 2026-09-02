# BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2202.02005.
> PDF retrieval source: https://arxiv.org/pdf/2202.02005. Reading tracker status/evidence was not changed.

- Year/Venue: 2022 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Imitation Learning, Vision-Language-Action
- Official paper: https://arxiv.org/abs/2202.02005
- Full-text retrieval: https://arxiv.org/pdf/2202.02005
- Code/Project: https://sites.google.com/view/bc-z/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, zero-shot generalization to new tasks remains a challenge, particularly when considering vision-based manipulation tasks that cover a breadth of skills (e.g., wiping, pushing, pick-and-place) with diverse objects.를 문제로 두고, These properties have been explored previously; our aim is to empirically study whether these ideas scale to a broad range of real-world tasks. *Equal Contribution †Work done while author was at Google ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning.
- **p. 1 / Abstract - extractive body cue:** We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization.
- **p. 1 / Abstract - extractive body cue:** To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on ...
- **p. 1 / Abstract - extractive body cue:** When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks ...
- **p. 1 / Abstract - extractive body cue:** Keywords: Zero-Shot Imitation Learning, Multi-Task Imitation, Deep Learning
- **p. 1 / 1 Introduction - extractive body cue:** However, zero-shot generalization to new tasks remains a challenge, particularly when considering vision-based manipulation tasks that cover a breadth of skills (e.g., wiping, pushing, pick-and-place) ...
- **p. 1 / 1 Introduction - extractive body cue:** Achieving such generalization depends on solving challenges relating to scaling up data collection and learning algorithms for diverse data.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** These properties have been explored previously; our aim is to empirically study whether these ideas scale to a broad range of real-world tasks. *Equal Contribution ...
- **p. 2 / 1 Introduction - extractive body cue:** Our main contribution is an empirical study of a large-scale interactive imitation learning system that solves a breadth of tasks, including zero-shot and few-shot generalization ...
- **p. 8 / 7 Discussion - extractive body cue:** We presented a multi-task imitation learning system that combines flexible task embeddings with large-scale training on a 100-task demonstration dataset, enabling it to generalize to ...
- **p. 2 / 1 Introduction - extractive body cue:** We show this system produces a policy that is capable of generalizing zero-shot to new unseen tasks.
- **p. 1 / 1 Introduction - extractive body cue:** We develop an interactive imitation learning system with two key properties that enable high-quality data collection and generalization to entirely new tasks.
- **p. 1 / 1 Introduction - extractive body cue:** End-to-end learning from pixels is a flexible choice for modeling the behavior of such generalist robots, as it has minimal assumptions about the state representation ...
- **p. 8 / 7 Discussion - extractive body cue:** Another limitation is the lower performance of the video-conditioned policy, which encourages future research on improving the generalization of video-based task representations and enhancing the ...
- **p. 1 / 1 Introduction - extractive body cue:** First, our system incorporates shared autonomy into teleoperation to allow us to collect both raw demonstration data and human interventions to correct the robot's current ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Second, our system flexibly conditions the policy on different forms of task specification, including a language instruction or a video of a person performing the task. | image/video, language instruction, proprioception과 history | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | Second, system, flexibly, conditions, policy, different, forms, task, specification, including, language, instruction | language-grounded task state와 action-policy context | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 8 (7 Discussion) |
| Output/action | We collect a large-scale dataset (25,877 episodes) of 100 diverse manipulation tasks, and train a 7-DoF multi-task policy that conditions on task language strings or human video. | continuous action, pose 또는 action chunk | p. 2 (1 Introduction), p. 8 (7 Discussion), p. 1 (1 Introduction) |
| Objective/outcome | instruction following, task success, generalization과 latency | instruction following, task success, generalization과 latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** These properties have been explored previously; our aim is to empirically study whether these ideas scale to a broad range of real-world tasks. *Equal Contribution ...
- **p. 2 / 1 Introduction - extractive body cue:** Our main contribution is an empirical study of a large-scale interactive imitation learning system that solves a breadth of tasks, including zero-shot and few-shot generalization ...
- **p. 8 / 7 Discussion - extractive body cue:** We presented a multi-task imitation learning system that combines flexible task embeddings with large-scale training on a 100-task demonstration dataset, enabling it to generalize to ...
- **p. 2 / 1 Introduction - extractive body cue:** We show this system produces a policy that is capable of generalizing zero-shot to new unseen tasks.
- **p. 1 / 1 Introduction - extractive body cue:** We develop an interactive imitation learning system with two key properties that enable high-quality data collection and generalization to entirely new tasks.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Success rates for zero-shot (language) and few-shot (video) generalization to tasks not in the training dataset. The first 4 tasks only use objects ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Mean number of interventions vs. task success rate. Each point represents a pol- icy evaluated during HG-DAgger data collection. There is a clear ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Ablation Studies. Left: Multi-task vs. single task models on the ‘place the bottle in the ceramic bowl' task. Training across tasks and with ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | Our evaluation covered 29 unseen vision-based manipulation tasks with a variety of objects and scenes. | hardware/simulator version and reset protocol | p. 8 (7 Discussion), p. 8 (7 Discussion) |
| Dataset/benchmark | Our evaluation covered 29 unseen vision-based manipulation tasks with a variety of objects and scenes. | role, split, size and leakage | p. 8 (7 Discussion), p. 8 (7 Discussion) |
| Metric | Table 2: Success rates for zero-shot (language) and few-shot (video) generalization to tasks not in the training dataset. The first 4 tasks only use objects from the 79-task family. The remaining tasks ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 14 (Figure/Table caption) |
| Baseline/ablation | Table 6: Ablations of video encoder batch composition. In the ablations below, we control for the same architecture, dataset, hyperparameters, and training time, changing only the sampling strategy for each batch. The ... | fair input/data/compute/action matching | p. 17 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 20 / Figure/Table caption - extractive body cue:** Figure 13: An example of adapting a sim image (left) to look real (right) using RetinaGAN [51]. environment (including the door). Further, any collision of ...
- **p. 8 / 7 Discussion - extractive body cue:** Our system does have a number of limitations.
- **p. 8 / 7 Discussion - extractive body cue:** A direction to address this limitation is to relabel the dataset with a variety of human-provided annotations [24], which could enable the system to handle ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Teleoperation buttons and controls. Control Function Right Controller (Arm) A Start recording, or mark demo as success if already recording B Stops current ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative examples of BC-Z successfully performing held-out tasks. push open a door while avoiding collisions. Both tasks use the architecture in Figure 3, ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 8: Human demonstrations of the task (left) are augmented with random distortions and reflec- tions (right), then trained to match language features for the ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, zero-shot generalization to new tasks remains a challenge, particularly when considering vision-based manipulation tasks that cover a breadth of skills (e.g., wiping, pushing, pick-and-place) with diverse objects.를 문제로 두고, These properties have been explored previously; our aim is to empirically study whether these ideas scale to a broad range of real-world tasks. *Equal Contribution †Work done while author was at Google ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 8 (7 Discussion), p. 1 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
