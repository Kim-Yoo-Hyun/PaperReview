# Problem - Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v80/haarnoja18b.html; PDF retrieval source: https://arxiv.org/pdf/1801.01290. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Maximum Entropy Reinforcement Learning)): Both of these challenges severely limit the applicability of model-free deep RL to real-world tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Model-free deep reinforcement learning (RL) algorithms have been demonstrated on a range of challenging decision making and control tasks.
- **p. 1 / Abstract - extractive body cue:** However, these methods typically suffer from two major challenges: very high sample complexity and brittle convergence properties, which necessitate meticulous hyperparameter tuning.
- **p. 1 / Abstract - extractive body cue:** Both of these challenges severely limit the applicability of such methods to complex, real-world domains.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose soft actor-critic, an offpolicy actor-critic deep RL algorithm based on the maximum entropy reinforcement learning framework.
- **p. 1 / Abstract - extractive body cue:** In this framework, the actor aims to maximize expected reward while also maximizing entropy.
- **p. 1 / 1. Introduction - extractive body cue:** Both of these challenges severely limit the applicability of model-free deep RL to real-world tasks.
- **p. 1 / 1. Introduction - extractive body cue:** This challenge is further exacerbated in continuous state and action spaces, where a separate actor network is often used to perform the maximization in Q-learning.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Both of these challenges severely limit the applicability of model-free deep RL to real-world tasks. | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | We will use ρπ(st) and ρπ(st, at) to denote the state and state-action marginals of the trajectory distribution induced by a policy ... | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF body |
| State / latent | will, denote, state, state-action, marginals, trajectory, distribution, induced, policy, at/st | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | address, policy, learning, continuous, action, spaces, explore, design | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: will, denote, state, state-action, marginals, trajectory, distribution, induced, policy, at/st | p. 3 (3.1. Notation), p. 6 (4.2. Soft Actor-Critic), p. 3 (3.1. Notation) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: present, empirical, soft, actor-critic, attains, substantial, improvement, performance | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Maximum Entropy Reinforcement Learning) |
| Objective / loss / cost | expected return / constrained return; cue terms: Let, optimizer, minimization, problem, defined, Equation, soft, Q-function | p. 4 (4.1. Derivation of Soft Policy Iteration), p. 4 (4.1. Derivation of Soft Policy Iteration), p. 5 (4.2. Soft Actor-Critic), p. 5 (4.2. Soft Actor-Critic) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (4.1. Derivation of Soft Policy Iteration), p. 5 (4.2. Soft Actor-Critic), p. 6 (4.2. Soft Actor-Critic) |
| Success / guarantee | task return, success and safe execution | p. 8 (5.2. Ablation Study), p. 8 (5.2. Ablation Study), p. 7 (5.2. Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** This challenge is further exacerbated in continuous state and action spaces, where a separate actor network is often used to perform the maximization in Q-learning.
- **p. 2 / 1. Introduction - extractive body cue:** We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy prior ...
- **p. 2 / 1. Introduction - extractive body cue:** SAC also avoids the complexity and potential instability associated with approximate inference in prior off-policy maximum entropy algorithms based on soft Q-learning (Haarnoja et al., ...
- **p. 3 / 3.2. Maximum Entropy Reinforcement Learning - extractive body cue:** In problem settings where multiple actions seem equally attractive, the policy will commit equal probability mass to those actions.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Maximum Entropy Reinforcement Learning)): We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy prior methods.

- **p. 2 / 1. Introduction - extractive body cue:** We present a convergence proof for policy iteration in the maximum entropy framework, and then introduce a new algorithm based on an approximation to this ...
- **p. 3 / 3.2. Maximum Entropy Reinforcement Learning - extractive body cue:** Though such algorithms have previously been proposed for conventional reinforcement learning, our method is, to our knowledge, the first off-policy actor-critic method in the maximum ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Our results suggest that stochastic, entropy maximizing reinforcement learning algorithms can provide a promising avenue for improved robustness ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For example, DDPG fails to make any progress on Ant-v1, Humanoidv1, and Humanoid (rllab), a result that is ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | To compare how the stochasticity of the policy and entropy maximization affects the performance, we compare to a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Figure 4. Training curves for additional baseline (Trust-PCL) and for two SAC variants. Soft actor-critic with hard target ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Notation), p. 6 (4.2. Soft Actor-Critic), p. 3 (3.1. Notation), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Maximum Entropy Reinforcement Learning), interface p. 3 (3.1. Notation), p. 6 (4.2. Soft Actor-Critic), p. 3 (3.1. Notation), p. 1 (1. Introduction), objective p. 4 (4.1. Derivation of Soft Policy Iteration), p. 4 (4.1. Derivation of Soft Policy Iteration), p. 5 (4.2. Soft Actor-Critic), p. 5 (4.2. Soft Actor-Critic).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Both of these challenges severely limit the applicability of model-free deep RL to real-world tasks. (p. 1, 1. Introduction).
- **Formulation-changing contribution:** We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy prior methods. (p. 2, 1. Introduction).
- **Assumption/failure evidence:** For maximum entropy algorithms, which do not explicitly inject exploration noise, we either evaluated with the exploration noise (SQL) or use the mean action (SAC). (p. 6, 5. Experiments).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
