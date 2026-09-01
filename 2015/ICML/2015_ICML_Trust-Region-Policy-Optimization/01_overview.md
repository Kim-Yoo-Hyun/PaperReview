# Trust Region Policy Optimization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v37/schulman15.html.
> PDF retrieval source: https://arxiv.org/pdf/1502.05477. Reading tracker status/evidence was not changed.

- Year/Venue: 2015 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Reinforcement Learning, policy optimization, on-policy RL
- Official paper: https://proceedings.mlr.press/v37/schulman15.html
- Full-text retrieval: https://arxiv.org/pdf/1502.05477
- Code/Project: https://proceedings.mlr.press/v37/schulman15.html
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task (Gabillon et al., 2013).를 문제로 두고, Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We describe an iterative procedure for optimizing policies, with guaranteed monotonic improvement.
- **p. 1 / Abstract - extractive body cue:** By making several approximations to the theoretically-justified procedure, we develop a practical algorithm, called Trust Region Policy Optimization (TRPO).
- **p. 1 / Abstract - extractive body cue:** This algorithm is similar to natural policy gradient methods and is effective for optimizing large nonlinear policies such as neural networks.
- **p. 1 / Abstract - extractive body cue:** Our experiments demonstrate its robust performance on a wide variety of tasks: learning simulated robotic swimming, hopping, and walking gaits; and playing Atari games using ...
- **p. 1 / Abstract - extractive body cue:** Despite its approximations that deviate from the theory, TRPO tends to give monotonic improvement, with little tuning of hyperparameters.
- **p. 1 / 1 Introduction - extractive body cue:** Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task (Gabillon et al., ...
- **p. 1 / 1 Introduction - extractive body cue:** Most algorithms for policy optimization can be classified into three broad categories: (1) policy iteration methods, which alternate between estimating the value function under the ...

## Core Idea

- **p. 2 / 2 Preliminaries - extractive body cue:** Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a).
- **p. 3 / 2 Preliminaries - extractive body cue:** Trust region policy optimization, which we propose in the following section, is an approximation to Algorithm 1, which uses a constraint on the KL divergence ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 6 Practical Algorithm Here we present two practical policy optimization algorithm based on the ideas above, which use either the single path or vine sampling ...
- **p. 1 / 1 Introduction - extractive body cue:** In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as playing Atari games ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Using q to denote the sampling distribution, the contribution of a single sn to the loss function is X a πθ(a/sn)Aθold(sn, a) = Ea∼q πθ(a/sn) ...
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** We use the conjugate gradient algorithm followed by a line search, which is altogether only slightly more expensive than computing the gradient itself.
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter δ (the bound ...
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Relative entropy policy search (REPS) (Peters et al., 2010) constrains the state-action marginals p(s, a), while TRPO constrains the conditionals p(a/s).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This implies the classic result that the update performed by exact policy iteration, which uses the deterministic policy ˜π(s) = arg maxa Aπ(s, a), improves the policy if there is at least ... | state 또는 observation, action, reward와 transition history | p. 2 (2 Preliminaries), p. 4 (2 Preliminaries) |
| State/latent | implies, classic, result, update, performed, exact, policy, iteration, uses, deterministic, maxa, improves | policy/value state와 action-selection variable | p. 2 (2 Preliminaries), p. 4 (2 Preliminaries), p. 5 (2 Preliminaries) |
| Output/action | Here, we generate a set of trajectories via simulation of the policy and incorporate all state-action pairs (sn, an) into the objective. | action policy와 induced trajectory | p. 4 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (3. Approximately solve this constrained optimization) |
| Objective/outcome | The natural policy gradient (Kakade, 2002) can be obtained as a special case of the update in Equation (12) by using a linear approximation to L and a quadratic approximation to the ... | expected return, task success, stability와 sample efficiency | p. 6 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |

## Main Claims and Actual Contribution

- **p. 2 / 2 Preliminaries - extractive body cue:** Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a).
- **p. 3 / 2 Preliminaries - extractive body cue:** Trust region policy optimization, which we propose in the following section, is an approximation to Algorithm 1, which uses a constraint on the KL divergence ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 6 Practical Algorithm Here we present two practical policy optimization algorithm based on the ideas above, which use either the single path or vine sampling ...
- **p. 1 / 1 Introduction - extractive body cue:** In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as playing Atari games ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Using q to denote the sampling distribution, the contribution of a single sn to the loss function is X a πθ(a/sn)Aθold(sn, a) = Ea∼q πθ(a/sn) ...
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Though this difference might seem subtle, our experiments demonstrate that it significantly improves the algorithm's performance on larger problems.
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** The rate of improvement in the policy is similar to the empirical FIM, as shown in the experiments.
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** 7 Connections with Prior Work As mentioned in Section 4, our derivation results in a policy update that is related to several prior methods, providing ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |
| Embodiment/environment | 8.1 Simulated Robotic Locomotion We conducted the robotic locomotion experiments using the MuJoCo simulator (Todorov et al., 2012). | hardware/simulator version and reset protocol | p. 6 (3. Can TRPO be used to solve challenging large-scale), p. 6 (1. What are the performance characteristics of the single) |
| Dataset/benchmark | We ended the episodes when the hopper fell over, which was defined by thresholds on the torso height and angle. | role, split, size and leakage | p. 6 (3. Can TRPO be used to solve challenging large-scale), p. 6 (1. What are the performance characteristics of the single), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 5 (2 Preliminaries) |
| Metric | Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies substantially from ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |
| Baseline/ablation | This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to the Q-values). | fair input/data/compute/action matching | p. 5 (2 Preliminaries), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 7 (3. Can TRPO be used to solve challenging large-scale) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled.
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Unlike REPS, our approach does not require a costly nonlinear optimization in the inner loop.
- **p. 5 / 2 Preliminaries - extractive body cue:** We can greatly reduce the variance of the Q-value differences between rollouts by using the same random number sequence for the noise in each of ...
- **p. 7 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** These results provide empirical evidence that constraining the KL divergence is a more robust way to choose step sizes and make fast, consistent progress, compared ...

## Why Read It

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task (Gabillon et al., 2013).를 문제로 두고, Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (3. Approximately solve this constrained optimization) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
