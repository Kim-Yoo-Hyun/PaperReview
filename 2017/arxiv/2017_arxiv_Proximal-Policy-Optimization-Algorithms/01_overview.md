# Proximal Policy Optimization Algorithms

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1707.06347.
> PDF retrieval source: https://arxiv.org/pdf/1707.06347. Reading tracker status/evidence was not changed.

- Year/Venue: 2017 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Reinforcement Learning, policy learning, Robotics
- Official paper: https://arxiv.org/abs/1707.06347
- Full-text retrieval: https://arxiv.org/pdf/1707.06347
- Code/Project: https://github.com/openai/baselines
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Q-learning (with function approximation) fails on many simple problems1 and is poorly understood, vanilla policy gradient methods have poor data effiency and robustness; and trust region policy optimization (TRPO) is relatively complica ...를 문제로 두고, Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose a new family of policy gradient methods for reinforcement learning, which alternate between sampling data through interaction with the environment, and optimizing a ...
- **p. 1 / Abstract - extractive body cue:** Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates.
- **p. 1 / Abstract - extractive body cue:** The new methods, which we call proximal policy optimization (PPO), have some of the benefits of trust region policy optimization (TRPO), but they are much ...
- **p. 1 / Abstract - extractive body cue:** Our experiments test PPO on a collection of benchmark tasks, including simulated robotic locomotion and Atari game playing, and we show that PPO outperforms other ...
- **p. 1 / 1 Introduction - extractive body cue:** In recent years, several different approaches have been proposed for reinforcement learning with neural network function approximators.
- **p. 1 / 1 Introduction - extractive body cue:** Q-learning (with function approximation) fails on many simple problems1 and is poorly understood, vanilla policy gradient methods have poor data effiency and robustness; and trust ...
- **p. 1 / 1 Introduction - extractive body cue:** However, there is room for improvement in developing a method that is scalable (to large models and parallel implementations), data efficient, and robust (i.e., successful ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates.
- **p. 1 / 1 Introduction - extractive body cue:** We propose a novel objective with clipped probability ratios, which forms a pessimistic estimate (i.e., lower bound) of the performance of the policy.
- **p. 3 / 1 Introduction - extractive body cue:** The main objective we propose is the following: LCLIP (θ) = ˆEt h min(rt(θ) ˆAt, clip(rt(θ), 1 -ϵ, 1 + ϵ) ˆAt) i (7) where ...
- **p. 1 / Abstract - extractive body cue:** We propose a new family of policy gradient methods for reinforcement learning, which alternate between sampling data through interaction with the environment, and optimizing a ...
- **p. 1 / 1 Introduction - extractive body cue:** This paper seeks to improve the current state of affairs by introducing an algorithm that attains the data efficiency and reliable performance of TRPO, while ...
- **p. 2 / 1 Introduction - extractive body cue:** (2) While it is appealing to perform multiple steps of optimization on this loss LPG using the same trajectory, doing so is not well-justified, and ...
- **p. 3 / 1 1 + ϵ - extractive body cue:** It shows how several objectives vary as we interpolate along the policy update direction, obtained by proximal policy optimization (the algorithm we will introduce shortly) ...
- **p. 5 / 1 1 + ϵ - extractive body cue:** If using a neural network architecture that shares parameters between the policy and value function, we must use a loss function that combines the policy ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We propose a new family of policy gradient methods for reinforcement learning, which alternate between sampling data through interaction with the environment, and optimizing a "surrogate" objective function using stochastic gradient ascent. | state 또는 observation, action, reward와 transition history | p. 1 (Abstract), p. 2 (1 Introduction) |
| State/latent | family, policy, gradient, methods, reinforcement, learning, alternate, between, sampling, data, through, interaction | policy/value state와 action-selection variable | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | This follows from the fact that a certain surrogate objective (which computes the max KL over states instead of the mean) forms a lower bound (i.e., a pessimistic bound) on the performance ... | action policy와 induced trajectory | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | 2.2 Trust Region Methods In TRPO [Sch+15b], an objective function (the "surrogate" objective) is maximized subject to a constraint on the size of the policy update. | expected return, task success, stability와 sample efficiency | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates.
- **p. 1 / 1 Introduction - extractive body cue:** We propose a novel objective with clipped probability ratios, which forms a pessimistic estimate (i.e., lower bound) of the performance of the policy.
- **p. 3 / 1 Introduction - extractive body cue:** The main objective we propose is the following: LCLIP (θ) = ˆEt h min(rt(θ) ˆAt, clip(rt(θ), 1 -ϵ, 1 + ϵ) ˆAt) i (7) where ...
- **p. 7 / 6 Experiments - extractive body cue:** We see that PPO outperforms the previous methods on almost all the continuous control environments.
- **p. 6 / 6 Experiments - extractive body cue:** 0.69 Table 1: Results from continuous control benchmark.
- **p. 6 / 6 Experiments - extractive body cue:** Note that we also tried clipping in log space, but found the performance to be no better.
- **p. 7 / 6 Experiments - extractive body cue:** A2C stands for advantage actor critic, and is a synchronous version of A3C, which we found to have the same or better performance than the ...
- **p. 8 / 6 Experiments - extractive body cue:** A table of results and learning curves for all 49 games is provided in Appendix B.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (6 Experiments), p. 6 (6 Experiments) |
| Embodiment/environment | Namely, we used 7 simulated robotics tasks2 implemented in OpenAI Gym [Bro+16], which use the MuJoCo [TET12] physics engine. | hardware/simulator version and reset protocol | p. 6 (6 Experiments), p. 7 (6 Experiments) |
| Dataset/benchmark | 6.4 Comparison to Other Algorithms on the Atari Domain We also ran PPO on the Arcade Learning Environment [Bel+15] benchmark and compared against well-tuned implementations of A2C [Mni+16] and ACER [Wan+16]. | role, split, size and leakage | p. 6 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 6 (6 Experiments) |
| Metric | Table 3. To represent the policy, we used a fully-connected MLP with two hidden layers of 64 units, and tanh nonlinearities, outputting the mean of a Gaussian distribution, with variable standard deviations, ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 8 (6 Experiments), p. 6 (6 Experiments) |
| Baseline/ablation | 6.4 Comparison to Other Algorithms on the Atari Domain We also ran PPO on the Arcade Learning Environment [Bel+15] benchmark and compared against well-tuned implementations of A2C [Mni+16] and ACER [Wan+16]. | fair input/data/compute/action matching | p. 8 (6 Experiments), p. 6 (6 Experiments), p. 7 (6 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7 Conclusion - extractive body cue:** We have introduced proximal policy optimization, a family of policy optimization methods that use multiple epochs of stochastic gradient ascent to perform each policy update.
- **p. 8 / 7 Conclusion - extractive body cue:** These methods have the stability and reliability of trust-region methods but are much simpler to implement, requiring only few lines of code change to a ...

## Why Read It

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Q-learning (with function approximation) fails on many simple problems1 and is poorly understood, vanilla policy gradient methods have poor data effiency and robustness; and trust region policy optimization (TRPO) is relatively complica ...를 문제로 두고, Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
