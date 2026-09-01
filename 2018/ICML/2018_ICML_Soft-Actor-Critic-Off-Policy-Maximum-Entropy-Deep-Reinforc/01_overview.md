# Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v80/haarnoja18b.html.
> PDF retrieval source: https://arxiv.org/pdf/1801.01290. Reading tracker status/evidence was not changed.

- Year/Venue: 2018 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Reinforcement Learning, continuous control, maximum entropy
- Official paper: https://proceedings.mlr.press/v80/haarnoja18b.html
- Full-text retrieval: https://arxiv.org/pdf/1801.01290
- Code/Project: https://github.com/haarnoja/sac
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Both of these challenges severely limit the applicability of model-free deep RL to real-world tasks.를 문제로 두고, We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy prior methods.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Model-free deep reinforcement learning (RL) algorithms have been demonstrated on a range of challenging decision making and control tasks.
- **p. 1 / Abstract - extractive body cue:** However, these methods typically suffer from two major challenges: very high sample complexity and brittle convergence properties, which necessitate meticulous hyperparameter tuning.
- **p. 1 / Abstract - extractive body cue:** Both of these challenges severely limit the applicability of such methods to complex, real-world domains.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose soft actor-critic, an offpolicy actor-critic deep RL algorithm based on the maximum entropy reinforcement learning framework.
- **p. 1 / Abstract - extractive body cue:** In this framework, the actor aims to maximize expected reward while also maximizing entropy.
- **p. 1 / 1. Introduction - extractive body cue:** Both of these challenges severely limit the applicability of model-free deep RL to real-world tasks.
- **p. 1 / 1. Introduction - extractive body cue:** This challenge is further exacerbated in continuous state and action spaces, where a separate actor network is often used to perform the maximization in Q-learning.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy prior ...
- **p. 2 / 1. Introduction - extractive body cue:** We present a convergence proof for policy iteration in the maximum entropy framework, and then introduce a new algorithm based on an approximation to this ...
- **p. 3 / 3.2. Maximum Entropy Reinforcement Learning - extractive body cue:** Though such algorithms have previously been proposed for conventional reinforcement learning, our method is, to our knowledge, the first off-policy actor-critic method in the maximum ...
- **p. 3 / 4. From Soft Policy Iteration to Soft - extractive body cue:** We will first present this derivation, verify that the corresponding algorithm converges to the optimal policy from its density class, and then present a practical ...
- **p. 5 / 4.2. Soft Actor-Critic - extractive body cue:** Soft Actor-Critic estimated from a single action sample from the current policy without introducing a bias, but in practice, including a separate function approximator for ...
- **p. 6 / 4.2. Soft Actor-Critic - extractive body cue:** The algorithm is agnostic to the parameterization of the policy, as long as it can be evaluated for any arbitrary state-action tuple.
- **p. 4 / 4.2. Soft Actor-Critic - extractive body cue:** For example, the value functions can be modeled as expressive neural networks, and the policy as a Gaussian with mean and covariance given by neural ...
- **p. 5 / 4.2. Soft Actor-Critic - extractive body cue:** To that end, we reparameterize the policy using a neural network transformation at = fφ(ϵt; st), (11) Algorithm 1 Soft Actor-Critic Initialize parameter vectors ψ, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We will use ρπ(st) and ρπ(st, at) to denote the state and state-action marginals of the trajectory distribution induced by a policy π(at/st). | state 또는 observation, action, reward와 transition history | p. 3 (3.1. Notation), p. 6 (4.2. Soft Actor-Critic) |
| State/latent | will, denote, state, state-action, marginals, trajectory, distribution, induced, policy, at/st, algorithm, agnostic | policy/value state와 action-selection variable | p. 3 (3.1. Notation), p. 6 (4.2. Soft Actor-Critic), p. 3 (3.1. Notation) |
| Output/action | The algorithm is agnostic to the parameterization of the policy, as long as it can be evaluated for any arbitrary state-action tuple. | action policy와 induced trajectory | p. 6 (4.2. Soft Actor-Critic), p. 3 (3.1. Notation), p. 1 (1. Introduction) |
| Objective/outcome | Let πold ∈Π and let πnew be the optimizer of the minimization problem defined in Equation 4. | expected return, task success, stability와 sample efficiency | p. 4 (4.1. Derivation of Soft Policy Iteration), p. 5 (4.2. Soft Actor-Critic), p. 4 (4.1. Derivation of Soft Policy Iteration) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy prior ...
- **p. 2 / 1. Introduction - extractive body cue:** We present a convergence proof for policy iteration in the maximum entropy framework, and then introduce a new algorithm based on an approximation to this ...
- **p. 3 / 3.2. Maximum Entropy Reinforcement Learning - extractive body cue:** Though such algorithms have previously been proposed for conventional reinforcement learning, our method is, to our knowledge, the first off-policy actor-critic method in the maximum ...
- **p. 6 / 5. Experiments - extractive body cue:** The stability of the algorithm also plays a large role in performance: easier tasks make it more practical to tune hyperparameters to achieve good results, ...
- **p. 7 / 5.1. Comparative Evaluation - extractive body cue:** The results show that, overall, SAC performs comparably to the baseline methods on the easier tasks and outperforms them on the harder tasks with a ...
- **p. 6 / 5. Experiments - extractive body cue:** Our SQL implementation also includes two Q-functions, which we found to improve its performance in most environments.
- **p. 7 / 5.2. Ablation Study - extractive body cue:** The results in the previous section suggest that algorithms based on the maximum entropy principle can outperform conventional RL methods on challenging tasks such as ...
- **p. 8 / 5.2. Ablation Study - extractive body cue:** We found this variant to benefit from taking more than one gradient step between the environment steps, which can improve performance but also increases the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (5. Experiments), p. 7 (5.1. Comparative Evaluation) |
| Embodiment/environment | We compare our method to prior techniques on a range of challenging continuous control tasks from the OpenAI gym benchmark suite (Brockman et al., 2016) and also on the rllab implementation of ... | hardware/simulator version and reset protocol | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Dataset/benchmark | In this comparison, we updated the target value network weights with hard updates, by periodically overwriting the target network parameters to match the current value network (see Appendix E for a comparison ... | role, split, size and leakage | p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.2. Ablation Study), p. 7 (5.1. Comparative Evaluation) |
| Metric | The optimal reward scale varies between environments, and should be tuned for each task separately. | definition, denominator, direction and uncertainty | p. 8 (5.2. Ablation Study), p. 8 (5.2. Ablation Study), p. 7 (5.2. Ablation Study) |
| Baseline/ablation | The results show that, overall, SAC performs comparably to the baseline methods on the easier tasks and outperforms them on the harder tasks with a large margin, both in terms of learning ... | fair input/data/compute/action matching | p. 7 (5.1. Comparative Evaluation), p. 7 (5.2. Ablation Study), p. 14 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** Our results suggest that stochastic, entropy maximizing reinforcement learning algorithms can provide a promising avenue for improved robustness and stability, and further exploration of maximum ...
- **p. 7 / 5.1. Comparative Evaluation - extractive body cue:** For example, DDPG fails to make any progress on Ant-v1, Humanoidv1, and Humanoid (rllab), a result that is corroborated by prior work (Gu et al., ...
- **p. 7 / 5.2. Ablation Study - extractive body cue:** To compare how the stochasticity of the policy and entropy maximization affects the performance, we compare to a deterministic variant of SAC that does not ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 4. Training curves for additional baseline (Trust-PCL) and for two SAC variants. Soft actor-critic with hard target update (blue) differs from standard SAC in ...
- **p. 8 / 5.2. Ablation Study - extractive body cue:** Note that the policy is trained to maximize also the entropy, and the mean action does not, in general, correspond the optimal action for the ...
- **p. 6 / 5. Experiments - extractive body cue:** We turned off the exploration noise for evaluation for DDPG and PPO.
- **p. 6 / 5. Experiments - extractive body cue:** For maximum entropy algorithms, which do not explicitly inject exploration noise, we either evaluated with the exploration noise (SQL) or use the mean action (SAC).

## Why Read It

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Both of these challenges severely limit the applicability of model-free deep RL to real-world tasks.를 문제로 두고, We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy prior methods.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Maximum Entropy Reinforcement Learning), p. 3 (4. From Soft Policy Iteration to Soft) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
