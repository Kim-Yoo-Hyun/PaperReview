# SPIN: Simultaneous Perception, Interaction and Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, mobile manipulation, active perception, whole-body control
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.pdf
- Code/Project: https://spin-robot.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 We evaluate across 6 benchmarks in simulation ranging from easy, medium, and hard difficulty, and two real-world environments with a similar level of clutter as the hard environments in simulation and also ...를 문제로 두고, We find that our method outperforms classical methods and baselines which do not use active vision.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While there has been remarkable progress recently in the fields of manipulation and locomotion, mobile manipulation remains a long-standing challenge.
- **p. 1 / Abstract - extractive body cue:** Compared to locomotion or static manipulation, a mobile system must make a diverse range of long-horizon tasks feasible in unstructured and dynamic environments.
- **p. 1 / Abstract - extractive body cue:** While the applications are broad and interesting, there are a plethora of challenges in developing these systems such as coordination between the base and arm, ...
- **p. 1 / Abstract - extractive body cue:** Prior works approach the problem using disentangled modular skills for mobility and manipulation that are trivially tied together.
- **p. 1 / Abstract - extractive body cue:** This causes several limitations such as compounding errors, delays in decision-making, and no whole-body coordination.
- **p. 2 / 1. Introduction - extractive body cue:** We evaluate across 6 benchmarks in simulation ranging from easy, medium, and hard difficulty, and two real-world environments with a similar level of clutter as ...
- **p. 2 / 1. Introduction - extractive body cue:** We train our approach via reinforcement learning (RL), and to get around the computational bottleneck of rendering depth images, we use a teacher-student training framework ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We find that our method outperforms classical methods and baselines which do not use active vision.
- **p. 3 / 2. Method - extractive body cue:** We propose two methods: (1) Coupled Visuomotor Optimization (CVO) learns robot and camera actions at the same time.
- **p. 4 / 2. Method - extractive body cue:** We present two approaches to tackle this problem.
- **p. 2 / 1. Introduction - extractive body cue:** We now discuss our approach in detail.
- **p. 4 / 2. Method - extractive body cue:** The agent learns to develop whole-body coordination such as the robot's arm movement in the last two frames, in order to reactively adapt and navigate ...
- **p. 3 / 2. Method - extractive body cue:** This is followed by a phase-2 supervised training where this behavior is distilled into a student network that operates with ego-centric depth images (2) Decoupled ...
- **p. 4 / 2. Method - extractive body cue:** Since the scandots are permutation invariant, we pass them through a trainable point-net architecture P to obtain compressed latent zt = P(˜st) that we pass ...
- **p. 4 / 2. Method - extractive body cue:** In particular, the policy gets proprioception xt and only visible scandots ˜st = F(st, xt) as observation and has to predict both the camera and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In particular, the policy gets proprioception xt and only visible scandots ˜st = F(st, xt) as observation and has to predict both the camera and the robot actions. | egocentric RGB-D, language/task goal, base-arm proprioception | p. 4 (2. Method), p. 4 (2. Method) |
| State/latent | particular, policy, gets, proprioception, only, visible, scandots, observation, predict, camera, robot, actions | map/object/contact state와 base-arm coordination decision | p. 4 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth) |
| Output/action | This policy is trained via RL to predict the robot actions from phase 1 policy arobot. | base motion plus arm/gripper action | p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 2 (1. Introduction) |
| Objective/outcome | Rewards: For the navigation task, we use distance to goal reward ∥gt∥along with a forward progress reward / (vt)g / where (vt)g is velocity along the direction of the goal. r_ \ ... | long-horizon task success, reachability, collision과 recovery | p. 4 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We find that our method outperforms classical methods and baselines which do not use active vision.
- **p. 3 / 2. Method - extractive body cue:** We propose two methods: (1) Coupled Visuomotor Optimization (CVO) learns robot and camera actions at the same time.
- **p. 4 / 2. Method - extractive body cue:** We present two approaches to tackle this problem.
- **p. 2 / 1. Introduction - extractive body cue:** We now discuss our approach in detail.
- **p. 4 / 2. Method - extractive body cue:** The agent learns to develop whole-body coordination such as the robot's arm movement in the last two frames, in order to reactively adapt and navigate ...
- **p. 7 / 4.3. Simulation results - extractive body cue:** Ours achieves ≈ 68% higher success rate than the FixCam baseline with the 18139
- **p. 7 / 4.3. Simulation results - extractive body cue:** Our method achieves ≈33% higher success rate than the NoPointNet baseline since permutation invariant scandots latent makes the optimization problem easier and also generalizes better ...
- **p. 8 / 4.3. Simulation results - extractive body cue:** Finally, we compare between the decoupled (DVO) and coupled (CVO) variants of our method and find that they achieve similar performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Simulation results), p. 7 (4.3. Simulation results) |
| Embodiment/environment | While simulation benchmarks are useful for fair comparison with baselines as well as reproducibility, real-world experimenting is essential for determining the efficacy of our system in truly unstructured and dynamic environments. | hardware/simulator version and reset protocol | p. 5 (4. Results and Analysis), p. 7 (4.3. Simulation results) |
| Dataset/benchmark | For this, we test our system on various real-world environments as shown in Figure 1 and benchmark its performance on 2 real-world setups as described in Section 4.2. | role, split, size and leakage | p. 5 (4. Results and Analysis), p. 7 (4.3. Simulation results), p. 5 (4. Results and Analysis), p. 7 (4.2. Real-world results) |
| Metric | 2 we compare success rate and average number of collisions. | definition, denominator, direction and uncertainty | p. 7 (4.2. Real-world results), p. 7 (4.3. Simulation results), p. 8 (4.3. Simulation results) |
| Baseline/ablation | We report the success rate of our method compared with the baseline. | fair input/data/compute/action matching | p. 8 (4.3. Simulation results), p. 5 (4. Results and Analysis), p. 5 (4. Results and Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. We illustrate one scenario of the simulation benchmark here with many obstacles in a narrow passage. The agent learns to develop whole-body coordination ...
- **p. 5 / 4. Results and Analysis - extractive body cue:** What are the limitations of the latter?
- **p. 6 / 4.1. Emergent Behavior - extractive body cue:** We observe that in cases when there is no feasible path for the robot to navigate through, it also learns to stop and look around ...
- **p. 7 / 4.2. Real-world results - extractive body cue:** 2 we compare success rate and average number of collisions.
- **p. 7 / 4.2. Real-world results - extractive body cue:** It has the emergent ability to avoid a new obstacle in space, whereas the classical baseline relies on the pre-built map and fails entirely.
- **p. 8 / 4.3. Simulation results - extractive body cue:** Static Obstacles Dynamic Obstacles Scenario 1 Ours Classical Ours Classical Average Success 0.8 0.6 0.6 0.0 Average # Collisions 1.0 0.4 1.6 1.2 Scenario 2 ...
- **p. 5 / 3. Experimental Setup - extractive body cue:** Note that this baseline gets an easier version of the problem since it assumes that the map is known in advance and does not consider ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 We evaluate across 6 benchmarks in simulation ranging from easy, medium, and hard difficulty, and two real-world environments with a similar level of clutter as the hard environments in simulation and also ...를 문제로 두고, We find that our method outperforms classical methods and baselines which do not use active vision.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Method), p. 4 (2. Method), p. 3 (2. Method), p. 4 (2. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
