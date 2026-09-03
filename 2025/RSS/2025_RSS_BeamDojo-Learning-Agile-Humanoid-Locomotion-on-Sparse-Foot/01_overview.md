# BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p068.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p068.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, perceptive locomotion, sparse footholds, Reinforcement Learning
- Official paper: https://www.roboticsproceedings.org/rss21/p068.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p068.pdf
- Code/Project: https://why618188.github.io/beamdojo/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, these methods encounter great challenges when applied to humanoid robots, primarily due to a key difference를 문제로 두고, To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Traversing risky terrains with sparse footholds poses f significant challenge for humanoid robot iri foot placements and stable locomotion.
- **p. 1 / Abstract - extractive body cue:** E approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.
- **p. 1 / Abstract - extractive body cue:** BEAMDOJO begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion ...
- **p. 1 / Abstract - extractive body cue:** To encourage sufficient trial-and-error exploration, BEAMDOJO incorporates a two-stage RL approach: the first stage relaxes
- **p. 1 / 1. INrRopucTION - extractive body cue:** However, these methods encounter great challenges when applied to humanoid robots, primarily due to a key difference
- **p. 2 / 1. INrRopucTION - extractive body cue:** Enabling agile movement on risky terrains for humanoid robots presents several challenges.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.
- **p. 2 / 1. INrRopucTION - extractive body cue:** In this work, we introduce BEAMDOJO, a novel reinforcement learning-based framework for controlling humanoid robots traversing risky terrains with sparse footholds.
- **p. 2 / 1. INrRopucTION - extractive body cue:** + We propose BEAMDOIO, a two-stage RL framework that combines a newly designed foothold reward for the polygonal foot model and a double critic, enabling ...
- **p. 3 / A. Foothold Reward - extractive body cue:** To accommodate the polygonal foot model of the humanoid robot, we introduce a sampling-based foothold reward that evaluates foot placement on sparse footholds.This evaluation
- **p. 1 / Body text (section not recovered) - extractive body cue:** 1: Our proposed framework, BEAMDOJO, enables agile and robust humanoid locomotion across challenging sparse foothold.
- **p. 2 / A. Locomotion on Sparse Footholds - extractive body cue:** Recent studies have explored combining RL. with modelbased controllers, such as using RL to generate trajectories that are then tracked by model-based controllers [15, 61, ...
- **p. 2 / 1. INrRopucTION - extractive body cue:** We begin by defining a samplingbased foothold reward, designed to evaluate the foot placement ‘of a polygonal foot model. ‘To address the challenge of sparse ...
- **p. 1 / Abstract - extractive body cue:** dynamics by training the humanoid on flat terr providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 1) Observation Space and Action Space: ‘The policy observations, denoted a8 o,, consist of four components: 0 = [61 0f°"*, of", a ® ‘The commands ¢; € R° specify the desired velocity, ... | proprioception, reference pose/motion, visual or language command | p. 5 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL) |
| State/latent | Observation, Space, Action, policy, observations, denoted, consist, four, components, commands, specify, desired | whole-body pose, balance/contact state와 skill/mode | p. 5 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 1 (Abstract) |
| Output/action | We let the humanoid robot traverse the terrain F, receiving proprioceptive observations, while providing perceptual feedback in the form of the elevation map of terrain T at the corresponding humanoids base position, ... | joint/whole-body action, motion target 또는 task trajectory | p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 1 (Abstract), p. 2 (1. INrRopucTION) |
| Objective/outcome | The primary objective is to optimize the policy x(as / s+) to maximize the discounted cumulative rewards: | tracking, balance, skill/task success와 recovery | p. 3 (B. Reinforcement Learning in Locomotion Control), p. 3 (B. Double Critic for Sparse Reward Learning), p. 4 (B. Double Critic for Sparse Reward Learning) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.
- **p. 2 / 1. INrRopucTION - extractive body cue:** In this work, we introduce BEAMDOJO, a novel reinforcement learning-based framework for controlling humanoid robots traversing risky terrains with sparse footholds.
- **p. 2 / 1. INrRopucTION - extractive body cue:** + We propose BEAMDOIO, a two-stage RL framework that combines a newly designed foothold reward for the polygonal foot model and a double critic, enabling ...
- **p. 3 / A. Foothold Reward - extractive body cue:** To accommodate the polygonal foot model of the humanoid robot, we introduce a sampling-based foothold reward that evaluates foot placement on sparse footholds.This evaluation
- **p. 1 / Body text (section not recovered) - extractive body cue:** 1: Our proposed framework, BEAMDOJO, enables agile and robust humanoid locomotion across challenging sparse foothold.
- **p. 7 / B. Simulation Experiments - extractive body cue:** 1) Quantitative results: We report the success rate (Race) and traverse rate (R,9y) for four terrains at medium and hard difficulty levels (terrain level 6 ...
- **p. 7 / A. Experimental Setup - extractive body cue:** 4 Success Rate Raocc: The percentage of successful at
- **p. 8 / B. Simulation Experiments - extractive body cue:** In contrast, ‘our method and the ablation with double critic demonstrates superior motion smoothness and improved feet clearance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup) |
| Embodiment/environment | 1) Hardware Setup: We use Unitree G1 humanoid robot for our experiments in this work. | hardware/simulator version and reset protocol | p. 6 (evaluation), p. 7 (A. Experimental Setup) |
| Dataset/benchmark | This terrain requires the robot to make large steps to cross, the gaps. | role, split, size and leakage | p. 6 (evaluation), p. 7 (A. Experimental Setup), p. 5 (evaluation), p. 5 (evaluation) |
| Metric | single-stage approaches and ablation designs, achieving, high success rates and low foothold errors across all ‘challenging terrains. | definition, denominator, direction and uncertainty | p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup), p. 10 (Figure/Table caption) |
| Baseline/ablation | This requires a distinct gait compared to regular Jocomotion tasks. | fair input/data/compute/action matching | p. 5 (evaluation), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 7 Single Leg Support ) Stand Still - extractive body cue:** 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. stone sizes and step distances, as shown in Fig.
- **p. 8 / B. Simulation Experiments - extractive body cue:** Meanwhile, the double-critic setup separates the foothold reward from the locomotion rewards, ensuring that its updates remain unaffected by the noise of unstable locomotion signals, ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 11: Failure Case Analysis. We evaluate the success rate on varying (a) stove sizes, and (b) step distances.
- **p. 7 / A. Experimental Setup - extractive body cue:** before falling to the total terrain length (8 m).
- **p. 8 / 10 3 oss Liss - extractive body cue:** This advantage is achieved by leveraging LiDAR to its full potential, whereas a single depth camera, cannot handle such scenarios.
- **p. 9 / 7 Single Leg Support ) Stand Still - extractive body cue:** ‘We compare this approach with other binary and coarse reward designs: when p% of the sampled points fall outside the safe area, a full penalty ...
- **p. 6 / evaluation - extractive body cue:** 2) Elevation Map and System Design: ‘The raw point cloud data obtained directly from the LiDAR suffers from significant occlusion and noise, making it challenging ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, these methods encounter great challenges when applied to humanoid robots, primarily due to a key difference를 문제로 두고, To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. INrRopucTION), p. 1 (Abstract), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION), p. 3 (B. Reinforcement Learning in Locomotion Control), p. 2 (A. Locomotion on Sparse Footholds) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
