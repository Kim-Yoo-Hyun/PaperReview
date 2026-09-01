# Constrained Policy Optimization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v70/achiam17a.html.
> PDF retrieval source: https://arxiv.org/pdf/1705.10528. Reading tracker status/evidence was not changed.

- Year/Venue: 2017 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, safe reinforcement learning, constraints, policy optimization
- Official paper: https://proceedings.mlr.press/v70/achiam17a.html
- Full-text retrieval: https://arxiv.org/pdf/1705.10528
- Code/Project: https://github.com/jachiam/cpo
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 safety 문제를 이해하기 위해 읽는다. 본문은 Although optimal policies for finite CMDPs with known models can be obtained by linear programming, methods for high-dimensional control are lacking.를 문제로 두고, In this work, we propose the first such algorithm, allowing applications to constrained deep RL.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** For many applications of reinforcement learning it can be more convenient to specify both a reward function and constraints, rather than trying to design behavior ...
- **p. 1 / Abstract - extractive body cue:** For example, systems that physically interact with or around humans should satisfy safety constraints.
- **p. 1 / Abstract - extractive body cue:** Recent advances in policy search algorithms (Mnih et al., 2016; Schulman et al., 2015; Lillicrap et al., 2016; Levine et al., 2016) have enabled new ...
- **p. 1 / Abstract - extractive body cue:** We propose Constrained Policy Optimization (CPO), the first general-purpose policy search algorithm for constrained reinforcement learning with guarantees for near-constraint satisfaction at each iteration.
- **p. 1 / Abstract - extractive body cue:** Our method allows us to train neural network policies for high-dimensional control while making guarantees about policy behavior all throughout training.
- **p. 1 / 1. Introduction - extractive body cue:** Although optimal policies for finite CMDPs with known models can be obtained by linear programming, methods for high-dimensional control are lacking.
- **p. 1 / 1. Introduction - extractive body cue:** Currently, policy search algorithms enjoy state-of-theart performance on high-dimensional control tasks (Mnih et al., 2016; Duan et al., 2016).

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this work, we propose the first such algorithm, allowing applications to constrained deep RL.
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Then, because the theoretically guaranteed update will take toosmall steps in practice, we propose CPO as a practical approximation based on trust region methods.
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Inspired by trust region methods, we propose CPO, which uses a trust region instead of penalties on policy divergence to enable larger step sizes: πk+1 ...
- **p. 1 / 1. Introduction - extractive body cue:** Driving our approach is a new theoretical result that bounds the difference between the rewards or costs of two different policies.
- **p. 2 / 1. Introduction - extractive body cue:** In our experiments, we show that CPO can train neural network policies with thousands of parameters on highdimensional simulated robot locomotion tasks to maximize rewards ...
- **p. 6 / 6.1. Approximately Solving the CPO Update - extractive body cue:** Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... do Sample a ...
- **p. 4 / 5.2. Trust Region Methods - extractive body cue:** Trust region algorithms for reinforcement learning (Schulman et al., 2015; 2016) have policy updates of the form πk+1 = arg max π∈Πθ E s∼dπk a∼π ...
- **p. 3 / 5. Constrained Policy Optimization - extractive body cue:** Policy search algorithms approach this problem by searching for the optimal policy within a set Πθ ⊆Π of parametrized policies with parameters θ (for example, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... do Sample a set of trajectories D = {τ} ∼πk ... | observation, uncertainty/risk estimate와 task command | p. 6 (6.1. Approximately Solving the CPO Update), p. 1 (1. Introduction) |
| State/latent | Constrained, Policy, Optimization, Algorithm, Input, Initial, tolerance, Sample, trajectories, Form, estimates, approximate | safe set, recovery state 또는 constraint margin | p. 6 (6.1. Approximately Solving the CPO Update), p. 1 (1. Introduction), p. 4 (5.2. Trust Region Methods) |
| Output/action | Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using pixels as inputs) (Mnih et al., 2015; 2016), robot lo ... | shielded, recovery 또는 safe action | p. 1 (1. Introduction), p. 4 (5.2. Trust Region Methods), p. 1 (1. Introduction) |
| Objective/outcome | However, for small step sizes δ, the objective and cost constraints are well-approximated by linearizing around πk, and the KLdivergence constraint is well-approximated by second order expansion (at πk = π, the ... | task return과 violation/failure probability | p. 5 (6.1. Approximately Solving the CPO Update), p. 5 (6.1. Approximately Solving the CPO Update), p. 3 (5. Constrained Policy Optimization) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** In this work, we propose the first such algorithm, allowing applications to constrained deep RL.
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Then, because the theoretically guaranteed update will take toosmall steps in practice, we propose CPO as a practical approximation based on trust region methods.
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Inspired by trust region methods, we propose CPO, which uses a trust region instead of penalties on policy divergence to enable larger step sizes: πk+1 ...
- **p. 1 / 1. Introduction - extractive body cue:** Driving our approach is a new theoretical result that bounds the difference between the rewards or costs of two different policies.
- **p. 2 / 1. Introduction - extractive body cue:** In our experiments, we show that CPO can train neural network policies with thousands of parameters on highdimensional simulated robot locomotion tasks to maximize rewards ...
- **p. 8 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return.
- **p. 8 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** Using cost shaping (CS) in the constraint while optimizing generally improves the agent's adherence to the true constraint on C-return. environment and makes sense when ...
- **p. 7 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** We find that CPO is successful at approximately enforcing constraints in all environments.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 8 (8.1. Evaluating CPO and Comparison Analysis) |
| Embodiment/environment | We consider two tasks, and train multiple different agents (robots) for each task: • Circle: The agent is rewarded for running in a wide circle, but is constrained to stay within a ... | hardware/simulator version and reset protocol | p. 6 (8. Experiments), p. 7 (8.1. Evaluating CPO and Comparison Analysis) |
| Dataset/benchmark | We experiment with three different agents: a point-mass (S ⊆R9, A ⊆R2), a quadruped robot (called an ‘ant') (S ⊆R32, A ⊆R8), and a simple humanoid (S ⊆ R102, A ⊆R10). | role, split, size and leakage | p. 6 (8. Experiments), p. 7 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8. Experiments), p. 8 (8.1. Evaluating CPO and Comparison Analysis) |
| Metric | Figure 1. Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 in all others); the x-axis is training iteration. CPO drives the constraint function almost ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 6 (8. Experiments), p. 7 (8. Experiments) |
| Baseline/ablation | We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. | fair input/data/compute/action matching | p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 6 (8. Experiments), p. 7 (8.1. Evaluating CPO and Comparison Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 6.2. Feasibility - extractive body cue:** Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary.
- **p. 6 / 6.3. Tightening Constraints via Cost Shaping - extractive body cue:** We choose ∆to be the probability of entering an unsafe state within a fixed time horizon, according to a learned model that is updated at ...

## Why Read It

RL, IL, offline learning, and robot data의 safety 문제를 이해하기 위해 읽는다. 본문은 Although optimal policies for finite CMDPs with known models can be obtained by linear programming, methods for high-dimensional control are lacking.를 문제로 두고, In this work, we propose the first such algorithm, allowing applications to constrained deep RL.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 6 (6.1. Approximately Solving the CPO Update), p. 4 (5.2. Trust Region Methods), p. 3 (5. Constrained Policy Optimization), p. 5 (5.3. Trust Region Optimization for Constrained MDPs) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
