# Sim-to-Real: Learning Agile Locomotion For Quadruped Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://roboticsproceedings.org/rss14/p10.html.
> PDF retrieval source: https://arxiv.org/pdf/1804.10332. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, sim-to-real
- Official paper: https://roboticsproceedings.org/rss14/p10.html
- Full-text retrieval: https://arxiv.org/pdf/1804.10332
- Code/Project: https://sites.google.com/view/learning-agile-locomotion
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 Overcoming the reality gap is challenging.를 문제로 두고, The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Designing agile locomotion for quadruped robots often requires extensive expertise and tedious manual tuning.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present a system to automate this process by leveraging deep reinforcement learning techniques.
- **p. 1 / Abstract - extractive body cue:** Our system can learn quadruped locomotion from scratch using simple reward signals.
- **p. 1 / Abstract - extractive body cue:** In addition, users can provide an open loop reference to guide the learning process when more control over the learned gait is needed.
- **p. 1 / Abstract - extractive body cue:** The control policies are learned in a physics simulator and then deployed on real robots.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Overcoming the reality gap is challenging.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Even worse, this gap is greatly amplified in locomotion tasks.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a complete learning system for agile locomotion, in which control policies are learned in simulation and deployed on real robots.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that with deep RL, highly agile locomotion gaits can emerge automatically.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference trajectories and a ...
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** Our problem is partially observable because certain states such as the position of the Minitaur's base and the foot contact forces are not accessible due ...
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** We represent the feedback component π with a neural network and solve the above POMDP using Proximal Policy Optimization [5].
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** More importantly, a compact observation space helps to transfer the policy to the real robot.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** Policy Representation Although learning from scratch can eliminate the need of human expertise, and sometimes achieve better performance, having control of the learned policies is ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | If we want a policy that is learned from scratch, we can set ¯a(t) = 0 and give the feedback component π(o) a wide output range. | proprioception, terrain/perception observation과 velocity command | p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS) |
| State/latent | want, policy, learned, scratch, give, feedback, component, wide, output, range, reason, decouple | body/contact state, foothold 또는 behavior mode | p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS) |
| Output/action | For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference trajectories and a feedback component that adjusts the leg poses ... | joint target, torque, footstep 또는 locomotion action | p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS) |
| Objective/outcome | Reinforcement learning optimizes a policy π : O 7→A that maximizes the expected return (accumulated rewards) R. π∗= arg maxπEs0∼D[Rπ(s0)] (1) B. | velocity/progress, stability, energy와 terrain generalization | p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a complete learning system for agile locomotion, in which control policies are learned in simulation and deployed on real robots.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that with deep RL, highly agile locomotion gaits can emerge automatically.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference trajectories and a ...
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** After we improved the simulation (Section V-A), an agile galloping gait emerged automatically.
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** After training with the improved simulator and random perturbations, the Minitaur is able to trot stably in simulation.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Controller performance in simulation (blue) and on the robot (red). From left to right, the controllers are trained using baseline simulation, using baseline ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 9: Comparison of controllers trained with different obser- vation spaces and randomization. The blue and red bars are the performance in simulation and in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION) |
| Embodiment/environment | This time, we observed stable, comparable movements in both simulation and on the real robot. | hardware/simulator version and reset protocol | p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION) |
| Dataset/benchmark | This time, we observed stable, comparable movements in both simulation and on the real robot. | role, split, size and leakage | p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION) |
| Metric | Fig. 8: Performance of controllers when they are tested in different simulation environments. Error bars indicate one standard deviation. 0 2 4 6 small | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption) |
| Baseline/ablation | We compared the learned gaits with the handcrafted ones from Ghost Robotics [3]. | fair input/data/compute/action matching | p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption), p. 6 (VI. EVALUATION AND DISCUSSION) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot.
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** Note that while this open loop controller expresses the user's preference of the locomotion style, by itself, it cannot produce any forward movement in the ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The simulated and the real Minitaurs learned to gallop using deep reinforcement learning. to locomotion tasks due to the difficulties of automatically resetting ...
- **p. 8 / VII. CONCLUSION - extractive body cue:** This points us to two interesting avenues for future work.
- **p. 8 / VII. CONCLUSION - extractive body cue:** With an accurate physical model and robust controllers, we have successfully deployed the controllers learned in simulation on the real robots.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found that ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 Overcoming the reality gap is challenging.를 문제로 두고, The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot. (p. 6, VI. EVALUATION AND DISCUSSION).
- **Actual contribution:** The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 6: Controller performance in simulation (blue) and on the robot (red). From left to right, the controllers are trained using baseline simulation, using baseline simulation with random perturbations, and ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** However, the binary outcome of success or failure does not capture the key characteristics of locomotion, such as running speed and energy consumption. (p. 7, B. Narrowing the Reality Gap).
