# Demonstrating A Walk in the Park: Learning to Walk in 20 Minutes With Model-Free Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=0.875); canonical paper source: https://roboticsproceedings.org/rss19/p056.html.
> PDF retrieval source: https://arxiv.org/pdf/2208.07860. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, quadruped locomotion, real-world reinforcement learning, sample efficiency
- Official paper: https://roboticsproceedings.org/rss19/p056.html
- Full-text retrieval: https://arxiv.org/pdf/2208.07860
- Code/Project: https://sites.google.com/berkeley.edu/walk-in-the-park
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=0.875)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 This result runs counter to the principles articulated in several prior works, which suggest either than simulated training is critical for robotic locomotion because the training times are too long [22], [32]-[35], ...를 문제로 두고, Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under 20 minutes. 를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Deep reinforcement learning is a promising approach to learning policies in uncontrolled environments that do not require domain knowledge.
- **p. 1 / Abstract - extractive body cue:** Unfortunately, due to sample inefficiency, deep RL applications have primarily focused on simulated environments.
- **p. 1 / Abstract - extractive body cue:** In this work, we demonstrate that the recent advancements in machine learning algorithms and libraries combined with a carefully tuned robot controller lead to learning ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our approach on several indoor and outdoor terrains which are known to be challenging for classical modelbased controllers.
- **p. 1 / Abstract - extractive body cue:** We observe the robot to be able to learn walking gait consistently on all of these terrains.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This result runs counter to the principles articulated in several prior works, which suggest either than simulated training is critical for robotic locomotion because the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** While our results largely build on existing methods, we demonstrate for the first time that a careful combination of existing components can enable direct real-world ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under 20 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Crucially, this does not require novel algorithmic components or any other unexpected innovation, but rather careful implementation of one of several existing algorithmic frameworks (and ...
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** DroQ [60] similarly allows for a higher update to data ratio by regularizing the critic networks with dropout [61] and layer normalization [65].
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Our choice of algorithm and implementation is aimed at enabling real-time synchronous training, which we expand on in Section V.
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Actor-critic methods have recently become significantly more sample-efficient by improving the training of the critic, thereby allowing more updates to the critic network for the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Reinforcement learning offers a promising alternative, acquiring effective control strategies directly through interaction with the real system, potentially right in the environment in which the robot will be situated. | proprioception, terrain/perception observation과 velocity command | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| State/latent | Reinforcement, learning, offers, promising, alternative, acquiring, effective, control, strategies, directly, through, interaction | body/contact state, foothold 또는 behavior mode | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | Experimental Design Training Statistics Simulation Real World Hardware Actions Resets Terrains Samples Hours Samples Hours Ours A1 PD targets Learned In/Outdoor 0 0 20 · 103 0.3 Wu et al. | joint target, torque, footstep 또는 locomotion action | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (B. Efficient Model-Free RL) |
| Objective/outcome | These algorithms use up to 20 times the number of critic updates to speed up learning with respect to the number of samples collected, but this increases their computational cost such that ... | velocity/progress, stability, energy와 terrain generalization | p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under 20 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Crucially, this does not require novel algorithmic components or any other unexpected innovation, but rather careful implementation of one of several existing algorithmic frameworks (and ...
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** DroQ [60] similarly allows for a higher update to data ratio by regularizing the critic networks with dropout [61] and layer normalization [65].
- **p. 6 / V. SIMULATION ANALYSIS - extractive body cue:** From these results, we can conclude that a variety of regularization or normalization methods, if implemented and applied carefully, can all achieve a similar level ...
- **p. 5 / V. SIMULATION ANALYSIS - extractive body cue:** Since our goal is to run training on a real robot, we aim for design decisions and algorithms that lead to improved stability and sample ...
- **p. 5 / V. SIMULATION ANALYSIS - extractive body cue:** We see that na¨ıvely increasing the number of critic updates made per time-step improves sample efficiency, but still requires roughly 30k samples, which would amount ...
- **p. 6 / V. SIMULATION ANALYSIS - extractive body cue:** Left to right: flat, solid ground covered in dense foam mats; a 5cm memory foam mattress; loose ground comprised of eucalyptus bark; a grassy lawn; ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS) |
| Embodiment/environment | 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task setup choices; (d) regularization and normalization methods for efficient ... | hardware/simulator version and reset protocol | p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS) |
| Dataset/benchmark | Since our goal is to run training on a real robot, we aim for design decisions and algorithms that lead to improved stability and sample efficiency. | role, split, size and leakage | p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS) |
| Metric | To match the real-world setup, we simulate the official A1 model in MuJoCo, and used the same position controller and rewards as discussed in Section III-B. | definition, denominator, direction and uncertainty | p. 5 (V. SIMULATION ANALYSIS), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Baseline/ablation | Therefore, for the remaining ablations, we used the value of damping set to 10. | fair input/data/compute/action matching | p. 5 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS) |

## Explicit Limitations and Failure Boundary

- **p. 4 / IV. SYSTEM DESIGN - extractive body cue:** In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in the real world, we found that p = [0.05, ...
- **p. 4 / IV. SYSTEM DESIGN - extractive body cue:** As such, such policies cannot trivially be further trained in the real world.
- **p. 5 / IV. SYSTEM DESIGN - extractive body cue:** During early experiments with the real robot, we found that using the forward velocity in the robot's local frame caused it to dive forward as ...
- **p. 5 / V. SIMULATION ANALYSIS - extractive body cue:** In particular, we confirm the efficacy of constraining the action space: we observe that the simulated agent cannot make any progress in the unconstrained action ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 This result runs counter to the principles articulated in several prior works, which suggest either than simulated training is critical for robotic locomotion because the training times are too long [22], [32]-[35], ...를 문제로 두고, Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under 20 minutes. 를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL), p. 6 (V. SIMULATION ANALYSIS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
