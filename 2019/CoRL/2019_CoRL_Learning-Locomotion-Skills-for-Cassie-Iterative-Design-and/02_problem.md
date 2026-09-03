# Problem - Learning Locomotion Skills for Cassie: Iterative Design and Sim-to-Real

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.ubc.ca/~van/papers/2019-CORL-cassie/index.html; PDF retrieval source: https://arxiv.org/pdf/1903.09537. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES)): However, these systems are relatively stable in comparison to human-scale bipeds, for which convincing demonstrations of DRL methods to dynamic locomotion on real hardware are still lacking, to the best ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Deep reinforcement learning (DRL) is a promising approach for developing legged locomotion skills.
- **p. 1 / Abstract - extractive body cue:** However, the iterative design process that is inevitable in practice is poorly supported by the default methodology.
- **p. 1 / Abstract - extractive body cue:** It is difficult to predict the outcomes of changes made to the reward functions, policy architectures, and the set of tasks being trained on.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a practical method that allows the reward function to be fully redefined on each successive design iteration while limiting the ...
- **p. 1 / Abstract - extractive body cue:** We characterize policies via sets of Deterministic Action Stochastic State (DASS) tuples, which represent the deterministic policy state-action pairs as sampled from the states visited ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these systems are relatively stable in comparison to human-scale bipeds, for which convincing demonstrations of DRL methods to dynamic locomotion on real hardware are ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This offers a strong alternative to "fine-tuning" approaches, where an existing policy may be adapted via small changes and additions to an existing reward function, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these systems are relatively stable in comparison to human-scale bipeds, for which convincing demonstrations of DRL methods to dynamic locomotion on ... | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | 2, where the blue curves represent the limit cycle produced by a deterministic policy, and the green arrows represent the deterministic feedback ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | where, blue, curves, represent, limit, cycle, produced, deterministic, policy, green | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | MDP, defined, tuple, where, state, space, action, problem | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: where, blue, curves, represent, limit, cycle, produced, deterministic, policy, green | p. 3 (IV. METHODS), p. 3 (IV. METHODS), p. 2 (III. PRELIMINARIES) |
| Decision / output variable | joint action/torque/footstep; body terms: section, present, collecting, stateaction, pairs, dataset, imitation, learning | p. 3 (IV. METHODS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: Data, Collection, assume, Gaussian, distributions, same, covariance, minimizing | p. 4 (IV. METHODS), p. 5 (VI. POLICY COMPRESSION AND DISTILLATION), p. 4 (IV. METHODS), p. 3 (IV. METHODS), p. 3 (IV. METHODS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. METHODS), p. 5 (VI. POLICY COMPRESSION AND DISTILLATION), p. 3 (IV. METHODS) |
| Success / guarantee | progress, balance and terrain robustness | p. 4 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** This offers a strong alternative to "fine-tuning" approaches, where an existing policy may be adapted via small changes and additions to an existing reward function, ...
- **p. 2 / III. PRELIMINARIES - extractive body cue:** The goal of reinforcement learning is to find a policy π, parameterized by θ, where πθ : S × A →[0, ∞) is the probability ...
- **p. 2 / III. PRELIMINARIES - extractive body cue:** More formally, we aim to solve the following optimization problem:
- **p. 3 / III. PRELIMINARIES - extractive body cue:** This causes the well-known covariate shift problem, where the student policy will accumulate errors overtime and eventually drift to states that were not seen by ...

## What the Paper Changes

PDF body contribution framing (p. 3 (IV. METHODS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (VI. POLICY COMPRESSION AND DISTILLATION)): In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used to combine imitation learning and reinforcement ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** To summarize, this paper makes the following contributions: • We present a simple-yet-effective technique to reconstruct policies from only a small number of samples, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a DRL design process that reflects and supports the iterative nature of control policy design.
- **p. 5 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** In this section, we present results for using DASS to compress and distill multiple policies.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We hypothesize the robustness stems from learning stochastic policies that operate at a low control rate, allowing the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | [25], where each rollout is started from some states sampled from the reference motions and is terminated when ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | A benefit of the fixed covariance is that because of the noise constantly injected into the system during ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (IV. METHODS), p. 3 (IV. METHODS), p. 2 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), interface p. 3 (IV. METHODS), p. 3 (IV. METHODS), p. 2 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES), objective p. 4 (IV. METHODS), p. 5 (VI. POLICY COMPRESSION AND DISTILLATION), p. 4 (IV. METHODS), p. 3 (IV. METHODS), p. 3 (IV. METHODS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
