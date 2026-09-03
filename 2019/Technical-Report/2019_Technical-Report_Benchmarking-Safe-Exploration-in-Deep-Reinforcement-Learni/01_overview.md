# Benchmarking Safe Exploration in Deep Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/.
> PDF retrieval source: https://cdn.openai.com/safexp-short.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / Technical Report
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, safe reinforcement learning, Safety Gym, Benchmark, constraints
- Official paper: https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/
- Full-text retrieval: https://cdn.openai.com/safexp-short.pdf
- Code/Project: https://github.com/openai/safety-gym
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 benchmark 문제를 이해하기 위해 읽는다. 본문은 While RL is not yet fully mature or ready to serve as an "off-the-shelf" solution, it appears to offer a viable path to solving hard sequential decision-making problems that cannot currently be ...를 문제로 두고, To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL) agents need to explore their environments in order to learn optimal policies by trial and error.
- **p. 1 / Abstract - extractive body cue:** In many environments, safety is a critical concern and certain errors are unacceptable: for example, robotics systems that interact with humans should never cause injury ...
- **p. 1 / Abstract - extractive body cue:** While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating ...
- **p. 1 / Abstract - extractive body cue:** Consequently we take the position that safe exploration should be viewed as a critical focus area for RL research, and in this work we make ...
- **p. 1 / Abstract - extractive body cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 1 / 1 Introduction - extractive body cue:** While RL is not yet fully mature or ready to serve as an "off-the-shelf" solution, it appears to offer a viable path to solving hard ...
- **p. 2 / 1 Introduction - extractive body cue:** However, there is not yet a standard set of environments for making progress on safe exploration specifically.2 Different papers use different environments and evaluation procedures, ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.
- **p. 2 / 1 Introduction - extractive body cue:** Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating ...
- **p. 1 / Abstract - extractive body cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 1 / Abstract - extractive body cue:** Second, we present the Safety Gym benchmark suite, a new slate of high-dimensional continuous control environments for measuring research progress on constrained RL.
- **p. 2 / 1 Introduction - extractive body cue:** While "sim-to-real" transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building ...
- **p. 2 / 1 Introduction - extractive body cue:** We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction ...
- **p. 3 / 1 Introduction - extractive body cue:** Our baseline algorithms include Trust Region Policy Optimization (TRPO) [Schulman et al., 2015] and Proximal Policy Optimization (PPO) [Schulman et al., 2017] in their original ...
- **p. 1 / Abstract - extractive body cue:** While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction of the final policy, and average regret ... | standardized observation, action, task state와 evaluation split | p. 2 (1 Introduction), p. 1 (Abstract) |
| State/latent | recommend, protocol, evaluating, constrained, algorithms, Safety, Gym, environments, three, metrics, task, performance | benchmark state/goal와 method decision | p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/action | While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating the complexities of the real world (such ... | policy/controller trajectory 또는 measured result | p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | These are expressed via a reward function and a set of auxiliary cost functions respectively. | success metric, robustness, generalization과 reproducibility | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.
- **p. 2 / 1 Introduction - extractive body cue:** Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating ...
- **p. 1 / Abstract - extractive body cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 1 / Abstract - extractive body cue:** Second, we present the Safety Gym benchmark suite, a new slate of high-dimensional continuous control environments for measuring research progress on constrained RL.
- **p. 21 / 5.3 Results - extractive body cue:** By success, we mean attaining improvements simultaneously along both the episodic return axis and the constraint regret axis, while still producing a constraint-satisfying policy at ...
- **p. 14 / 5 Experiments - extractive body cue:** However, we highlight a few common rules that guide our discussion: • All agents that fail to satisfy constraints are strictly worse than all agents ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 3: Constraint elements used in our environments. currently-highlighted button, which is the goal button. After the agent presses the correct button, the environment will ...
- **p. 14 / 5 Experiments - extractive body cue:** Metrics: To characterize the task and safety performance of an agent and its training run, we measure the following throughout training: • The average episodic ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 21 (5.3 Results), p. 14 (5 Experiments) |
| Embodiment/environment | SG6 has at least one environment for each task, robot, and level. | hardware/simulator version and reset protocol | p. 15 (5 Experiments), p. 21 (5.3 Results) |
| Dataset/benchmark | SGCar: All six Car robot environments with constraints in Safety Gym. | role, split, size and leakage | p. 15 (5 Experiments), p. 21 (5.3 Results), p. 15 (5 Experiments), p. 16 (5 Experiments) |
| Metric | We compare normalized scores like we would compare individual training runs: the average constraint violation should be zero (or within noise of zero), and among approximately constraint-satisfying algorithms, one algorithm dominates an ... | definition, denominator, direction and uncertainty | p. 15 (5 Experiments), p. 16 (5.3 Results), p. 16 (5.3 Results) |
| Baseline/ablation | Advancing SOTA on Safety Gym: Our baseline results for constrained RL indicate a need for stronger and/or better-tuned algorithms to succeed on Safety Gym environments. | fair input/data/compute/action matching | p. 21 (5.3 Results), p. 14 (5 Experiments), p. 21 (5.3 Results) |

## Explicit Limitations and Failure Boundary

- **p. 16 / 5 Experiments - extractive body cue:** [2017], we omit the learned failure predictor they used for cost shaping.
- **p. 21 / 5.3 Results - extractive body cue:** There are a number of avenues we consider promising for future work.
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 6: Diversity of generated layouts for the Safexp-PointPush2-v0 env. 4.2 Safety Gym Benchmark Suite Safety Gym ships with a suite of pre-configured benchmark environments, ...
- **p. 14 / 5 Experiments - extractive body cue:** First and foremost, it corresponds directly to safety outcomes: a lower cost rate means that fewer unsafe things happened.
- **p. 14 / 5 Experiments - extractive body cue:** E τ∼πθ XT t=0 ct  ≤d, where ct is the aggregate indicator cost function for the environment (ct = 1 for an unsafe interaction, ...
- **p. 15 / 5 Experiments - extractive body cue:** 3Characteristic return and cumulative cost were obtained by averaging over the last five epochs of training to reduce noise.
- **p. 15 / 5 Experiments - extractive body cue:** We compare normalized scores like we would compare individual training runs: the average constraint violation should be zero (or within noise of zero), and among ...

## Why Read It

World models, safety, uncertainty, and recovery의 benchmark 문제를 이해하기 위해 읽는다. 본문은 While RL is not yet fully mature or ready to serve as an "off-the-shelf" solution, it appears to offer a viable path to solving hard sequential decision-making problems that cannot currently be ...를 문제로 두고, To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
