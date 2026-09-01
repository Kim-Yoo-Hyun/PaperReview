# Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2010.15920.
> PDF retrieval source: https://arxiv.org/pdf/2010.15920. Reading tracker status/evidence was not changed.

- Year/Venue: 2020 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: CORE
- Tags: Robotics, safe reinforcement learning, recovery policy, real robot
- Official paper: https://arxiv.org/abs/2010.15920
- Full-text retrieval: https://arxiv.org/pdf/2010.15920
- Code/Project: https://sites.google.com/berkeley.edu/recovery-rl/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, when deploying RL agents in the real world, unconstrained exploration can result in highly suboptimal behaviors which can damage the robot, break surroundings objects, or bottleneck the learning process.를 문제로 두고, Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more efficiently learn in the real world.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Safety remains a central obstacle preventing widespread use of RL in the real world: learning new tasks in uncertain environments requires extensive exploration, but safety ...
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **p. 1 / Abstract - extractive body cue:** We evaluate Recovery RL on 6 simulation domains, including two contact-rich manipulation tasks and an imagebased navigation task, and an image-based obstacle avoidance task on ...
- **p. 1 / Abstract - extractive body cue:** We compare Recovery RL to 5 prior safe RL methods which jointly optimize for task performance and safety via constrained optimization or reward shaping and ...
- **p. 1 / Abstract - extractive body cue:** Results suggest that Recovery RL trades off constraint violations and task successes 2 - 20 times more efficiently in simulation domains and 3 times more ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, when deploying RL agents in the real world, unconstrained exploration can result in highly suboptimal behaviors which can damage the robot, break surroundings objects, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** While these approaches are appealing for their generality and simplicity, there are two key aspects which make them difficult to use in practice.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present Recovery RL, a new algorithm for safe robotic RL.
- **p. 1 / I. INTRODUCTION - extractive body cue:** If it tips over the carton, then not only can this possibly break the carton and create a mess, but it also requires laborious human ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Separating the task and recovery policies makes it easier to balance task performance and safety, and allows using off-the-shelf RL algorithms for both.
- **p. 5 / IV. RECOVERY RL - extractive body cue:** [8] to plan over a learned stochastic dynamics model, while for tasks with visual observations, we use a VAE based latent dynamics model.
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** First, the inherent objective conflict between exploring to learn new tasks and limiting exploration to avoid constraint violations can lead to suboptimalities in policy optimization.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over πtask ∈Π and a recovery policy πrec, ... | observation, uncertainty/risk estimate와 task command | p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL) |
| State/latent | present, algorithm, optimize, equation, III, utilizing, pair, policies, task, policy, trained, maximize | safe set, recovery state 또는 constraint margin | p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL), p. 1 (I. INTRODUCTION) |
| Output/action | If the task policy πtask proposes an action aπtask at state s such that (s,aπtask)̸ ∈T π safe, then a recovery action sampled from πrec is executed instead of aπtask. | shielded, recovery 또는 safe action | p. 4 (IV. RECOVERY RL), p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective/outcome | We train ˆQπ φ,risk by minimizing the following MSE loss with respect to the target (RHS of equation IV.1). | task return과 violation/failure probability | p. 4 (IV. RECOVERY RL), p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present Recovery RL, a new algorithm for safe robotic RL.
- **p. 1 / I. INTRODUCTION - extractive body cue:** If it tips over the carton, then not only can this possibly break the carton and create a mess, but it also requires laborious human ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Separating the task and recovery policies makes it easier to balance task performance and safety, and allows using off-the-shelf RL algorithms for both.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation environments
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Simulation Experiments: Left: ratio of successes to constraint violations over the course of online training. In all navigation tasks, we find that Recovery ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We find that without this relabeling, Recovery RL achieves very poor performance as it rarely achieves task successes.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTS), p. 6 (Figure/Table caption) |
| Embodiment/environment | Domains: We evaluate Recovery RL on a set of 6 simulation domains (Figure 3) and an image-based obstacle avoidance task on a physical robot (Figure 6). | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Dataset/benchmark | ACCEPTED FEBRUARY, 2021 Figure 3: Simulation Experiments Domains: We evaluate Recovery RL on a set of 2D navigation tasks, two contact rich manipulation environments, and a visual navigation task. | role, split, size and leakage | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Metric | We find that Recovery RL violates constraints less often than comparisons while maintaining a similar task success rate and more efficiently optimizing the task reward. | definition, denominator, direction and uncertainty | p. 5 (V. EXPERIMENTS), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption) |
| Baseline/ablation | Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation environments | fair input/data/compute/action matching | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. EXPERIMENTS - extractive body cue:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We hypothesize that the model-based recovery mechanism is better able to compensate for approximation errors in ˆQπ φ,risk, resulting in a more robust recovery policy.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Results suggest that Recovery RL performs much more poorly when πrec and ˆQπ φ,risk are not pretrained with data from Doffline, indicating the ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 12: Physical Experiment Reward Learning Curve: We show the total reward attained in each episode smoothed over a 10 episode length window with results ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Recovery RL can safely learn policies for contact-rich tasks from high-dimensional image observations in simulation experiments and on a physical robotic system. We ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Recovery RL: For intuition, we illustrate Recovery RL on a 2D maze navigation task where a constraint violation corresponds to hitting a wall. ...
- **p. 5 / IV. RECOVERY RL - extractive body cue:** Practical Implementation Recovery Policy: Any off-policy RL algorithm can be used to learn πrec.

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, when deploying RL agents in the real world, unconstrained exploration can result in highly suboptimal behaviors which can damage the robot, break surroundings objects, or bottleneck the learning process.를 문제로 두고, Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more efficiently learn in the real world.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 5 (IV. RECOVERY RL) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
