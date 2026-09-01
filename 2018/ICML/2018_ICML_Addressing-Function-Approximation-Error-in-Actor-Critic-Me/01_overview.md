# Addressing Function Approximation Error in Actor-Critic Methods

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1802.09477.
> PDF retrieval source: https://arxiv.org/pdf/1802.09477. Reading tracker status/evidence was not changed.

- Year/Venue: 2018 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, continuous control, actor-critic
- Official paper: https://arxiv.org/abs/1802.09477
- Full-text retrieval: https://arxiv.org/pdf/1802.09477
- Code/Project: https://github.com/sfujim/TD3
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Our proposed method addresses these issues, and greatly outperforms the current state of the art.를 문제로 두고, Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In value-based reinforcement learning methods such as deep Q-learning, function approximation errors are known to lead to overestimated value estimates and suboptimal policies.
- **p. 1 / Abstract - extractive body cue:** We show that this problem persists in an actor-critic setting and propose novel mechanisms to minimize its effects on both the actor and the critic.
- **p. 1 / Abstract - extractive body cue:** Our algorithm builds on Double Q-learning, by taking the minimum value between a pair of critics to limit overestimation.
- **p. 1 / Abstract - extractive body cue:** We draw the connection between target networks and overestimation bias, and suggest delaying policy updates to reduce per-update error and further improve performance.
- **p. 1 / Abstract - extractive body cue:** We evaluate our method on the suite of OpenAI gym tasks, outperforming the state of the art in every environment tested.
- **p. 1 / 1. Introduction - extractive body cue:** Our proposed method addresses these issues, and greatly outperforms the current state of the art.
- **p. 1 / 1. Introduction - extractive body cue:** In reinforcement learning problems with discrete action spaces, the issue of value overestimation as a result of function approximation errors is well-studied.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance.
- **p. 1 / 1. Introduction - extractive body cue:** Second, to address the coupling of value and policy, we propose delaying policy updates until the value estimate has converged.
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** We propose delaying policy updates until the value error is as small as possible.
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** We introduce a regularization strategy for deep value learning, target policy smoothing, which mimics the learning update from SARSA (Sutton & Barto, 1998).
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ϵ)] , (13) ...
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ 1 ←θ1, θ′ ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** If target networks can be used to reduce the error over multiple updates, and policy updates on high-error states cause divergent behavior, then the policy ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slowupdating target networks, (τ = 0.1, 0.01), ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At each discrete time step t, with a given state s ∈S, the agent selects actions a ∈A with respect to its policy π : S →A, receiving a reward r and ... | state 또는 observation, action, reward와 transition history | p. 2 (3. Background), p. 6 (5.3. Target Policy Smoothing Regularization) |
| State/latent | discrete, time, step, given, state, agent, selects, actions, respect, policy, receiving, reward | policy/value state와 action-selection variable | p. 2 (3. Background), p. 6 (5.3. Target Policy Smoothing Regularization), p. 6 (5.3. Target Policy Smoothing Regularization) |
| Output/action | Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ 1 ←θ1, θ′ 2 ←θ2, φ′ ←φ Initialize replay buffer ... | action policy와 induced trajectory | p. 6 (5.3. Target Policy Smoothing Regularization), p. 6 (5.3. Target Policy Smoothing Regularization), p. 1 (1. Introduction) |
| Objective/outcome | As deep function approximators require multiple gradient updates to converge, target networks provide a stable objective in the learning 0.0 0.2 0.4 0.6 0.8 1.0 Time steps (1e5) 150 200 250 300 ... | expected return, task success, stability와 sample efficiency | p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance.
- **p. 1 / 1. Introduction - extractive body cue:** Second, to address the coupling of value and policy, we propose delaying policy updates until the value estimate has converged.
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** We propose delaying policy updates until the value error is as small as possible.
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** We introduce a regularization strategy for deep value learning, target policy smoothing, which mimics the learning update from SARSA (Sutton & Barto, 1998).
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ϵ)] , (13) ...
- **p. 8 / 6.2. Ablation Studies - extractive body cue:** Method HCheetah Hopper Walker2d Ant TD3 9532.99 3304.75 4565.24 4185.06 DDPG 3162.50 1731.94 1520.90 816.35 AHE 8401.02 1061.77 2362.13 564.07 AHE + DP 7588.64 1465.11 ...
- **p. 8 / 6.1. Evaluation - extractive body cue:** TD3 matches or outperforms all other algorithms in both final performance and learning speed across all tasks.
- **p. 6 / 6. Experiments - extractive body cue:** We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy Gradient algorithm (DDPG) (Lillicrap et al., 2015) ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (6.2. Ablation Studies), p. 8 (6.1. Evaluation) |
| Embodiment/environment | Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise. | hardware/simulator version and reset protocol | p. 8 (6.1. Evaluation), p. 7 (6.1. Evaluation) |
| Dataset/benchmark | Learning curves for the OpenAI gym continuous control tasks. | role, split, size and leakage | p. 8 (6.1. Evaluation), p. 7 (6.1. Evaluation), p. 7 (6. Experiments), p. 8 (6.2. Ablation Studies) |
| Metric | Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise. | definition, denominator, direction and uncertainty | p. 8 (6.1. Evaluation), p. 6 (6. Experiments), p. 7 (6. Experiments) |
| Baseline/ablation | A full comparison between our re-tuned version and the baselines DDPG is provided in the supplementary material. | fair input/data/compute/action matching | p. 8 (6.1. Evaluation), p. 8 (6.2. Ablation Studies), p. 13 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7. Conclusion - extractive body cue:** Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning.
- **p. 7 / 6.1. Evaluation - extractive body cue:** Afterwards, we use an off-policy exploration strategy, adding Gaussian noise N(0, 0.1) to each action.
- **p. 7 / 6.1. Evaluation - extractive body cue:** Unlike the original implementation of DDPG, we used uncorrelated noise for exploration as we found noise drawn from the Ornstein-Uhlenbeck (Uhlenbeck & Ornstein, 1930) process ...
- **p. 8 / 6.1. Evaluation - extractive body cue:** Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise.

## Why Read It

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Our proposed method addresses these issues, and greatly outperforms the current state of the art.를 문제로 두고, Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3. Background), p. 3 (3. Background), p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
