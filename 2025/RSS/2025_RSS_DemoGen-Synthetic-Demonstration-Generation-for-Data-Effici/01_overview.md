# DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p157.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p157.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, synthetic data, demonstration generation, 3D perception, Imitation Learning, manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p157.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p157.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} reflect the current state of the end-effector, ...를 문제로 두고, The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) end-effector pose inthe world frame, and a®™ ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Visuomotor policies have shown great promise in robotic manipulation but often require substantial hur collected data for effective per factor driving the high data demands ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present Demo a low-cost, fully synthetic approach for automatic demonstration generation.
- **p. 1 / Abstract - extractive body cue:** Using only one human-collected demonstration per ly augmented demonstrations trajectory to novel object configurations.
- **p. 1 / Abstract - extractive body cue:** Visual observations are synthesized by leveraging, 3D point clouds as the modality and rearranging the subjects in the scene via 3D editing, Empirically, DemoGen significantly ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, DemoGen can be extended to enable additional out-of-distibution capabilities, including disturbance resistance and obstacle avoidance.
- **p. 5 / A. Problem Formulation - extractive body cue:** The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} ...

## Core Idea

- **p. 4 / A. Problem Formulation - extractive body cue:** The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) ...
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** In real-world experiments, we use the DBSCAN [15] elustering algorithm to discard the outlier points and downsample the number of points in the point cloud ...
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated settings, ...
- **p. 4 / A. Problem Formulation - extractive body cue:** A visuomotor policy + : O +> A directly maps the visual observations 0 < © to the predicted actions « cA.
- **p. 5 / A. Problem Formulation - extractive body cue:** The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} ...
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** It is noteworthy that we found directly replacing the current state with the next target pose action (ie., 07°" < aj) ‘may impair performance, asthe ...
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** The observations consist of point cloud data and proprioceptive states.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} reflect the current state of the end-effector, ... | observation history와 expert trajectory/action | p. 5 (A. Problem Formulation), p. 4 (A. Problem Formulation) |
| State/latent | observation, includes, point, cloud, data, proprioceptive, feedback, robot, where, reflect, current, state | behavior policy와 temporal action context | p. 5 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 17 (A. Policy Training and Implementation Details) |
| Output/action | A visuomotor policy + : O +> A directly maps the visual observations 0 < © to the predicted actions « cA. | predicted action 또는 action chunk | p. 4 (A. Problem Formulation), p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details) |
| Objective/outcome | 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated settings, resulting in an equal training cost regardless ... | imitation error, task success, robustness와 compounding error | p. 17 (A. Policy Training and Implementation Details), p. 6 (C. TAMP-based Action Generation), p. 17 (A. Policy Training and Implementation Details) |

## Main Claims and Actual Contribution

- **p. 4 / A. Problem Formulation - extractive body cue:** The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) ...
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor policies and object ...
- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 20: Visualization of the policy performance trained on human-collected datasets. (Upper row) The demonstrated configurations. (Bottom row) The spatial heatmaps with success rates averaged ...
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** On the other hand, both 3D representations and pre-trained 2D visual encoders contribute to improved spatial generalization capabilities.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Qualitative visualization of the spatial effective range. The grid maps display discretized tabletop workspaces from a bird's-eye view under different demonstration configurations. Dark ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 9: Performance Saturation. We report the policy performance boost wart. the increase of synthetic demonstrations over 3 seeds.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** These encoders are widely used in previous works [9, 31] to enhance policy performance.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** We compare its performance against 2D Diffusion Policy (DP) [8] in the empirical study in Sec.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 18 (Figure/Table caption) |
| Embodiment/environment | In the following benchmarking, we explore the relationship between the number of demonstrations and policy performance to determine how many demonstrations are sufficient for effective training. | hardware/simulator version and reset protocol | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 4 (B. Benchmarking Spatial Generalization Capability) |
| Dataset/benchmark | R3M utilizes a ResNet [21] architecture and is pre-trained on roboties-specific tasks. | role, split, size and leakage | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 4 (B. Benchmarking Spatial Generalization Capability), p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details) |
| Metric | We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor policies and object randomization ranges are adopted, The resuls are ... | definition, denominator, direction and uncertainty | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 18 (Figure/Table caption), p. 4 (B. Benchmarking Spatial Generalization Capability) |
| Baseline/ablation | Fig. 22: Raw evaluation results in the Sauce-Spreading task. (Top) Examples of the processing results for metric calculation. (Bottom) Compared with the regular DemoGen, the policy trained with the ADR strategy better ... | fair input/data/compute/action matching | p. 18 (Figure/Table caption), p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details) |

## Explicit Limitations and Failure Boundary

- **p. 12 / B. Obstacle Avoidance - extractive body cue:** Trained on the source demonstrations without obstacles, the visuomotor policy fails to account for potential collisions, e.g., it might knock over the coffee cup placed ...
- **p. 12 / B. Obstacle Avoidance - extractive body cue:** Obstacle-avoiding trajectories are generated by a motion planning tool [28], ensuring collision-free actions.
- **p. 11 / B. Cluttered Scene - extractive body cue:** When the scene becomes even more complex, e.g. clutter, DemoGen does not necessarily work well.
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** We vary the number of demonstrations from 25 to 400, The object configurations are randomly sampled from a slightly larger range than the evaluation workspace ...
- **p. 11 / B. Cluttered Scene - extractive body cue:** 16: DemoGen for disturbance resistance.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** Since Ts indicates the steps of actions executed on the robot without re-planning, our horizon settings result in a closed-loop re-planning latency of 0.5 seconds. ...
- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 22: Raw evaluation results in the Sauce-Spreading task. (Top) Examples of the processing results for metric calculation. (Bottom) Compared with the regular DemoGen, the ...

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} reflect the current state of the end-effector, ...를 문제로 두고, The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) end-effector pose inthe world frame, and a®™ ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 5 (A. Problem Formulation), p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details), p. 4 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 6 (C. TAMP-based Action Generation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
