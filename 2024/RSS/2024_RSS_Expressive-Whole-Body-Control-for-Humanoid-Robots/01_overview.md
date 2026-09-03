# Expressive Whole-Body Control for Humanoid Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p107.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p107.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, whole-body control, motion imitation, sim-to-real
- Official paper: https://www.roboticsproceedings.org/rss20/p107.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p107.pdf
- Code/Project: https://expressive-humanoid.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 The root movement goal gm can also be intuitively given by joystick commands, enabling convenient deployment in the real world. methods on both of these two form factors tend to produce singular ...를 문제로 두고, We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach that relaxes the constraints indeed leads to better ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Can we enable humanoid robots to generate rich, diverse, and expressive motions in the real world?
- **p. 1 / Abstract - extractive body cue:** We propose to learn a whole-body control policy on a human-sized robot to mimic human motions as realistic as possible.
- **p. 1 / Abstract - extractive body cue:** To train such a policy, we leverage the large-scale human motion capture data from the graphics community in a Reinforcement Learning framework.
- **p. 1 / Abstract - extractive body cue:** However, directly performing imitation learning with the motion capture dataset would not work on the real humanoid robot, given the large gap in degrees of ...
- **p. 1 / Abstract - extractive body cue:** Our method Expressive Whole-Body Control (ExBody) tackles this problem by encouraging the upper humanoid body to imitate a reference motion, while relaxing the imitation constraint ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The root movement goal gm can also be intuitively given by joystick commands, enabling convenient deployment in the real world. methods on both of these ...
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** However, our proposed approach should generalize to similar body forms that differ in the exact number of actuated degrees of freedom. a) Command-conditioned Locomotion Control: ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach that ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose to train a novel controller that takes both a reference motion and a root movement command as inputs for real humanoid robot control.
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We assume in the rest of this paper, without loss of generality, that the observation and action space are given by the H1 humanoid robot ...
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We consider humanoid motion control as learning a goalconditioned motor policy π : G ×S 7→A, where G is the goal space that specifies the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We consider humanoid motion control as learning a goalconditioned motor policy π : G ×S 7→A, where G is the goal space that specifies the behavior, S is the observation space, and ... | proprioception, reference pose/motion, visual or language command | p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION) |
| State/latent | consider, humanoid, motion, control, learning, goalconditioned, motor, policy, where, goal, space, specifies | whole-body pose, balance/contact state와 skill/mode | p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION) |
| Output/action | However, our proposed approach should generalize to similar body forms that differ in the exact number of actuated degrees of freedom. a) Command-conditioned Locomotion Control: We aim to produce a robust control ... | joint/whole-body action, motion target 또는 task trajectory | p. 3 (II. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | We assume in the rest of this paper, without loss of generality, that the observation and action space are given by the H1 humanoid robot design. | tracking, balance, skill/task success와 recovery | p. 3 (II. PROBLEM FORMULATION) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach that ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose to train a novel controller that takes both a reference motion and a root movement command as inputs for real humanoid robot control.
- **p. 6 / IV. RESULTS - extractive body cue:** V, our method achieves the best linear velocity tracking performance (MELV).
- **p. 6 / IV. RESULTS - extractive body cue:** However, even with a reduced sampling range, the performance is significantly worse than ours, indicating ExBody's advantage in overcoming conflicts of objectives problems.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 11: Text2Motion trajectories replay. A motion sequence is prompted offline with the input "a man mimics boxing punches" through MDM [64]. Our robot presents ...
- **p. 5 / IV. RESULTS - extractive body cue:** 5, we study whether velocity goal vx will affect the performance of other goals.
- **p. 5 / IV. RESULTS - extractive body cue:** The average performance is not directly implied from the heatmap and is further discussed in Tab.
- **p. 7 / IV. RESULTS - extractive body cue:** We also added the O.O.D. motions to the evaluation on the tracking performance in Tab.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Embodiment/environment | In this section we aim to answer the following questions through extensive experiments both in sim and the real world: • How well does ExBody perform on tracking ge and gm? • ... | hardware/simulator version and reset protocol | p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Dataset/benchmark | II. • No RSI: Initialize the environment with default DoF positions and root states instead of sampling from the motion dataset. • Full body tracking: Instead of tracking only the upper body ... | role, split, size and leakage | p. 5 (IV. RESULTS), p. 6 (IV. RESULTS), p. 5 (IV. RESULTS), p. 7 (IV. RESULTS) |
| Metric | However, it has even worse performance, demonstrating a high-frequency jittery movement that is not feasible for sim-to-real transfer, indicating for such a complex system, AMP reward itself is not sufficient. | definition, denominator, direction and uncertainty | p. 7 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Baseline/ablation | We compare with baselines to show that our approach ExBody is superior compared with other design choices. | fair input/data/compute/action matching | p. 6 (IV. RESULTS), p. 8 (IV. RESULTS), p. 7 (IV. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / VII. LIMITATIONS - extractive body cue:** Auto recovery and initialization could be explored to reduce the cost of doing experiments.
- **p. 9 / VI. DISCUSSIONS - extractive body cue:** We introduce a method designed to enable a humanoid robot to track expressive upper body motions while ensuring the maintenance of robust locomotion capabilities in ...
- **p. 5 / IV. RESULTS - extractive body cue:** Note that although Random Sample looks better than Motion Sample, the heatmap does not consider the sample density.
- **p. 6 / IV. RESULTS - extractive body cue:** Why does not ExBody do full DoF tracking?
- **p. 6 / IV. RESULTS - extractive body cue:** Again our method does not require such manual tuning of curriculum to work.
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 13: Policy's state distribution under different sampling strategies. The green dots are the policy rollout's states. For dataset sampling, we record 20 data points ...
- **p. 7 / IV. RESULTS - extractive body cue:** Unified policy is more robust than separate ones.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 The root movement goal gm can also be intuitively given by joystick commands, enabling convenient deployment in the real world. methods on both of these two form factors tend to produce singular ...를 문제로 두고, We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach that relaxes the constraints indeed leads to better ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 3 (II. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
