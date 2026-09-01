# HumanPlus: Humanoid Shadowing and Imitation from Humans

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=WnSl42M9Z4.
> PDF retrieval source: https://arxiv.org/pdf/2406.10454. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, human-to-humanoid, Imitation Learning, teleoperation
- Official paper: https://openreview.net/forum?id=WnSl42M9Z4
- Full-text retrieval: https://arxiv.org/pdf/2406.10454
- Code/Project: https://humanoid-ai.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms.를 문제로 두고, In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** One of the key arguments for building robots that have similar form factors to human beings is that we can leverage the massive human data ...
- **p. 1 / Abstract - extractive body cue:** Yet, doing so has remained challenging in practice due to the complexities in humanoid perception and control, lingering physical gaps between humanoids and humans in ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a full-stack system for humanoids to learn motion and autonomous skills from human data.
- **p. 1 / Abstract - extractive body cue:** We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets.
- **p. 1 / Abstract - extractive body cue:** This policy transfers to the real world and allows humanoid robots to follow hu1 arXiv:2406.10454v1 [cs.RO] 15 Jun 2024
- **p. 2 / 1. Introduction - extractive body cue:** This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms.
- **p. 2 / 1. Introduction - extractive body cue:** Traditional approaches, such as decoupling the problem into perception, planning and tracking, and separate modularization of control for arms and legs [10, 10, 23, 40], ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.
- **p. 3 / 1. Introduction - extractive body cue:** Core to this system is both (1) a real-time shadowing system that allows human operators to whole-body control humanoids using a single RGB camera and ...
- **p. 3 / 1. Introduction - extractive body cue:** Using forward dynamics prediction on image features, our method shows improved performance by regularizing on image feature spaces and preventing the vision-based skill policy from ...
- **p. 4 / 4. Human Body and Hand Data - extractive body cue:** Each of the humanoid hip and shoulder joints consists of 3 orthogonal revolute joints, so can be viewed as one spherical joints.
- **p. 5 / 5. Shadowing of Human Motion - extractive body cue:** The humanoid target pose consists of target forward and lateral velocities, target roll and pitch, target yaw velocity and target joint angles, and is retargeted ...
- **p. 2 / 1. Introduction - extractive body cue:** We leverage this dataset by first retargeting human poses to humanoid poses and then training a task-agnostic low-level policy called Humanoid Shadowing Transformer conditioning on ...
- **p. 7 / 6. Imitation of Human Skills - extractive body cue:** In this work, we modify the Action Chunking Transformer [104] by removing its encoder-decoder architecture to develop a decoder-only Humanoid Imitation Transformer (HIT) for skill ...
- **p. 3 / 1. Introduction - extractive body cue:** We build upon the recent success of imitation learning from human-provided demonstrations [11, 104], and introduce a transformer-based architecture that blends action prediction and forward ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Using state-of-the-art human body and hand pose estimation algorithms [58, 81], we can estimate real-time human motion and retarget it to humanoid motion, which is passed as input to the low-level policy. | proprioception, reference pose/motion, visual or language command | p. 2 (1. Introduction), p. 5 (5. Shadowing of Human Motion) |
| State/latent | state-of-the-art, human, body, hand, pose, estimation, algorithms, estimate, real-time, motion, retarget, humanoid | whole-body pose, balance/contact state와 skill/mode | p. 2 (1. Introduction), p. 5 (5. Shadowing of Human Motion), p. 2 (1. Introduction) |
| Output/action | At each time step, the input to the policy is humanoid proprioception and a humanoid target pose. | joint/whole-body action, motion target 또는 task trajectory | p. 5 (5. Shadowing of Human Motion), p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Objective/outcome | We use PPO [74] to train our Humanoid Shadowing Transformer in simulation by maximizing discounted expected return E hPT-1 t=0 γtrt i , where rt is the reward at time step t, ... | tracking, balance, skill/task success와 recovery | p. 6 (5. Shadowing of Human Motion), p. 2 (1. Introduction), p. 5 (4. Human Body and Hand Data) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.
- **p. 3 / 1. Introduction - extractive body cue:** Core to this system is both (1) a real-time shadowing system that allows human operators to whole-body control humanoids using a single RGB camera and ...
- **p. 3 / 1. Introduction - extractive body cue:** Using forward dynamics prediction on image features, our method shows improved performance by regularizing on image feature spaces and preventing the vision-based skill policy from ...
- **p. 4 / 4. Human Body and Hand Data - extractive body cue:** Each of the humanoid hip and shoulder joints consists of 3 orthogonal revolute joints, so can be viewed as one spherical joints.
- **p. 5 / 5. Shadowing of Human Motion - extractive body cue:** The humanoid target pose consists of target forward and lateral velocities, target roll and pitch, target yaw velocity and target joint angles, and is retargeted ...
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Our HIT achieves higher success rates than other baselines across all tasks.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5: Comparisons on Imitation. We show success rates of Humanoid Imitation Transformer (Ours), HIT with monocular input, ACT and open-loop trajectory replay across all ...
- **p. 9 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** We also record the average success rates of stable standing during teleoperation 9

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (9. Experiments on Imitation), p. 9 (Figure/Table caption) |
| Embodiment/environment | Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT [104], and Open-loop trajectory replay, across all tasks: ... | hardware/simulator version and reset protocol | p. 10 (9. Experiments on Imitation), p. 10 (8.1. Comparisons with Other Teleoperation) |
| Dataset/benchmark | The participants are tasked to perform the Rearrange Objects task and its variant, Rearrange Lower Objects, where an object is placed on a lower table of height 0.55m, requiring the robot to ... | role, split, size and leakage | p. 10 (9. Experiments on Imitation), p. 10 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation) |
| Metric | In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is the only method that can be used for whole-body teleoperation, solving the Rearrange Lower ... | definition, denominator, direction and uncertainty | p. 10 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation), p. 9 (8. Experiments on Shadowing) |
| Baseline/ablation | Overall HIT (Ours) outperforms others. | fair input/data/compute/action matching | p. 9 (8. Experiments on Shadowing), p. 9 (8.1. Comparisons with Other Teleoperation), p. 10 (9. Experiments on Imitation) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. target poses while saving energy and avoiding ...
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Throughout the development of our system, we encountered several limitations.
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms.를 문제로 두고, In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 7 (6. Imitation of Human Skills), p. 5 (4. Human Body and Hand Data) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
