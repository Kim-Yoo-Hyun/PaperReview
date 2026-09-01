# HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p070.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p070.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, loco-manipulation, teleoperation, exoskeleton
- Official paper: https://www.roboticsproceedings.org/rss21/p070.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p070.pdf
- Code/Project: https://homietele.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (21 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose acquisition.를 문제로 두고, We introduce the training settings and three key techniques of our framework in this section를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Generalizable humanoid loco-manipulation poses significant challenges, requiring coordinated whole-body control and precise, contact
- **p. 1 / Abstract - extractive body cue:** this paper introduces HOMIE, a semi-autonomous teleoperation and its affordability, with a price of just $500.
- **p. 1 / Abstract - extractive body cue:** The system is fully system that combines a reinforcement learning poliey for body open-source, demos and code can be found in our websit control mapped ...
- **p. 1 / Abstract - extractive body cue:** m-sensing gloves for hand control, forming I.
- **p. 1 / Abstract - extractive body cue:** ‘arm control, and mot ‘8 uniled cockpit to freely operate humas data flywheel.
- **p. 2 / A. Teleoperation Systems - extractive body cue:** However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose ...
- **p. 1 / Abstract - extractive body cue:** However, the field currently faces a significant

## Core Idea

- **p. 4 / B. Humanoid Whole-body Control - extractive body cue:** We introduce the training settings and three key techniques of our framework in this section
- **p. 2 / Abstract - extractive body cue:** Unlike previous whole-body contro! methods that depend on motion priors derived from MoCap data [12], our framework eliminates this dependency, resulting in a more cfficient ...
- **p. 2 / Abstract - extractive body cue:** In responce, we introduce HOMIE, a semi-autonomous humanoid teleoperation system that integrates a RL policy for body control mapped to a pedal, an isomorphic exoskeleton ...
- **p. 4 / A. System Overview - extractive body cue:** 2, HOMIE consists of low-level policy Toco and an exoskeleton-based hardware system.
- **p. 3 / A. Teleoperation Systems - extractive body cue:** HOMIE is designed to combine all the advantages mentioned above, integrating isomorphic exoskeleton arms with a pair of novel motionsensing gloves.
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Symmetry Utilization, We introduce three algorithmic variants for comparison with ours in terms of symmetry ut tion: w/ aug, which uses only symmetrical data augmentation; ...
- **p. 3 / B. Whole-body Loco-Manipulation - extractive body cue:** Reinforcement Learning (RL)-based algorithms, especially those based on Proximal Policy Optimization (PPO) [32], offer a more powerful altemative.
- **p. 2 / Abstract - extractive body cue:** Our RL-based training framework features three core techrniques: upper-body pose curriculum for dynamic balance adaptation, height-tracking reward for precise squatting, and symmetry utilization for action ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 1) Training Settings: ‘The observations of one step are defined as O, = [Cry tes dts des de» ei], Where Cy is the command, «is the body's angular velocity, gis the projection ... | proprioception, reference pose/motion, visual or language command | p. 4 (B. Humanoid Whole-body Control), p. 4 (B. Humanoid Whole-body Control) |
| State/latent | Training, Settings, observations, step, defined, Cry, Where, command, body, angular, velocity, projection | whole-body pose, balance/contact state와 skill/mode | p. 4 (B. Humanoid Whole-body Control), p. 4 (B. Humanoid Whole-body Control), p. 2 (Abstract) |
| Output/action | The actions ay of the policy correspond one-to-one with the joints of the robot's lower body. | joint/whole-body action, motion target 또는 task trajectory | p. 4 (B. Humanoid Whole-body Control), p. 2 (Abstract), p. 5 (C. Hardware System Design) |
| Objective/outcome | Given that the symmetry loss can reach values on the order of 20 without constraints, no significant difference is observed across the three methods in terms of symmetry loss. | tracking, balance, skill/task success와 recovery | p. 7 (A. Humanoid Whole-body Control), p. 2 (Abstract), p. 5 (1 2001p) |

## Main Claims and Actual Contribution

- **p. 4 / B. Humanoid Whole-body Control - extractive body cue:** We introduce the training settings and three key techniques of our framework in this section
- **p. 2 / Abstract - extractive body cue:** Unlike previous whole-body contro! methods that depend on motion priors derived from MoCap data [12], our framework eliminates this dependency, resulting in a more cfficient ...
- **p. 2 / Abstract - extractive body cue:** In responce, we introduce HOMIE, a semi-autonomous humanoid teleoperation system that integrates a RL policy for body control mapped to a pedal, an isomorphic exoskeleton ...
- **p. 4 / A. System Overview - extractive body cue:** 2, HOMIE consists of low-level policy Toco and an exoskeleton-based hardware system.
- **p. 3 / A. Teleoperation Systems - extractive body cue:** HOMIE is designed to combine all the advantages mentioned above, integrating isomorphic exoskeleton arms with a pair of novel motionsensing gloves.
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** In summary, symmetry data augmentation significantly improves training efficiency, while the use of symmetry loss effectively prevents the policy from sacrificing symmetry to complete tasks ...
- **p. 10 / C. Teleoperation System - extractive body cue:** The results, shown in Fig. /, indicate that our system achieves task completion times nearly half of those of the VRbased method.
- **p. 7 / C. Hardware System Design - extractive body cue:** To achieve this, we use three small pedals to control these commands.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (A. Humanoid Whole-body Control), p. 10 (C. Teleoperation System) |
| Embodiment/environment | This migration enables the use of HOMIE to control robots within a variety of simulated environments By leveraging these simulated scenes, the robots can perform diverse loco-manipulation tasks more cost-effectively and in ... | hardware/simulator version and reset protocol | p. 10 (20 Bet), p. 10 (20 Bet) |
| Dataset/benchmark | Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other changes in reward scales or training pipeline. | role, split, size and leakage | p. 10 (20 Bet), p. 10 (20 Bet), p. 8 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control) |
| Metric | These results indicate that just scaling up the height tracking reward in hei may initially lead to faster reduction in height tracking error, but it negatively affects the feedback from ‘other rewards, ... | definition, denominator, direction and uncertainty | p. 8 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control), p. 7 (A. Humanoid Whole-body Control) |
| Baseline/ablation | Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other changes in reward scales or training pipeline. | fair input/data/compute/action matching | p. 8 (A. Humanoid Whole-body Control), p. 7 (A. Humanoid Whole-body Control), p. 7 (A. Humanoid Whole-body Control) |

## Explicit Limitations and Failure Boundary

- **p. 7 / A. Humanoid Whole-body Control - extractive body cue:** Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample from
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** We design two additional algorithms w/o knee, which does not USE rinee described in Eq.
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Infact, het ultimately does not achieve faster ‘convergence in height tracking compared to ours.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: HOMIE empowers the humanoid robot to execute various loco-manipulation tasks in the real world. (2): Squatting to grasp a tape and placing it ...
- **p. 9 / C. Teleoperation System - extractive body cue:** These tasks showcase the robustness of our loco-manipulation policy and HOMIE 's ability 10 teleopeate humanoids perform a wide range of complex tasks in various ...
- **p. 9 / C. Teleoperation System - extractive body cue:** I (<), the robot is controlled to push a 60 kg person sitting in a chair, who weighs roughly twice as much as the robot, ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose acquisition.를 문제로 두고, We introduce the training settings and three key techniques of our framework in this section를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (A. Teleoperation Systems), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (B. Whole-body Loco-Manipulation), p. 8 (A. Humanoid Whole-body Control) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
