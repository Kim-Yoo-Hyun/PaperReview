# Problem - Trust Region Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v37/schulman15.html; PDF retrieval source: https://arxiv.org/pdf/1502.05477. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 3 (2 Preliminaries)): Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task (Gabillon et al., 2013).

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We describe an iterative procedure for optimizing policies, with guaranteed monotonic improvement.
- **p. 1 / Abstract - extractive body cue:** By making several approximations to the theoretically-justified procedure, we develop a practical algorithm, called Trust Region Policy Optimization (TRPO).
- **p. 1 / Abstract - extractive body cue:** This algorithm is similar to natural policy gradient methods and is effective for optimizing large nonlinear policies such as neural networks.
- **p. 1 / Abstract - extractive body cue:** Our experiments demonstrate its robust performance on a wide variety of tasks: learning simulated robotic swimming, hopping, and walking gaits; and playing Atari games using ...
- **p. 1 / Abstract - extractive body cue:** Despite its approximations that deviate from the theory, TRPO tends to give monotonic improvement, with little tuning of hyperparameters.
- **p. 1 / 1 Introduction - extractive body cue:** Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task (Gabillon et al., ...
- **p. 1 / 1 Introduction - extractive body cue:** Most algorithms for policy optimization can be classified into three broad categories: (1) policy iteration methods, which alternate between estimating the value function under the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task ... | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | This implies the classic result that the update performed by exact policy iteration, which uses the deterministic policy ˜π(s) = arg maxa ... | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF |
| State / latent | implies, classic, result, update, performed, exact, policy, iteration, uses, deterministic | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | Trust, Region, Policy, Optimization, mate, performing, rollout, short | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: implies, classic, result, update, performed, exact, policy, iteration, uses, deterministic | p. 2 (2 Preliminaries), p. 4 (2 Preliminaries), p. 5 (2 Preliminaries) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: Instead, introduce, following, local, approximation, Trust, region, policy | p. 2 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries) |
| Objective / loss / cost | expected return / constrained return; cue terms: natural, policy, gradient, Kakade, obtained, special, case, update | p. 6 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |
| Success / guarantee | task return, success and safe execution | p. 8 (Figure/Table caption), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Most algorithms for policy optimization can be classified into three broad categories: (1) policy iteration methods, which alternate between estimating the value function under the ...
- **p. 2 / 2 Preliminaries - extractive body cue:** The complex dependency of ρ˜π(s) on ˜π makes Equation (2) difficult to optimize directly.
- **p. 2 / 2 Preliminaries - extractive body cue:** To define the conservative policy iteration update, let πold denote the current policy, and let π′ = arg maxπ′ Lπold(π′).
- **p. 3 / 2 Preliminaries - extractive body cue:** Since mixture policies are rarely used in practice, this result is crucial for extending the improvement guarantee to practical problems.

## What the Paper Changes

PDF contribution framing (p. 2 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries), p. 1 (1 Introduction), p. 4 (2 Preliminaries)): Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a).

- **p. 3 / 2 Preliminaries - extractive body cue:** Trust region policy optimization, which we propose in the following section, is an approximation to Algorithm 1, which uses a constraint on the KL divergence ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 6 Practical Algorithm Here we present two practical policy optimization algorithm based on the ideas above, which use either the single path or vine sampling ...
- **p. 1 / 1 Introduction - extractive body cue:** In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as playing Atari games ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Using q to denote the sampling distribution, the contribution of a single sn to the loss function is X a πθ(a/sn)Aθold(sn, a) = Ea∼q πθ(a/sn) ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | The analytic estimator integrates over the action at each state sn, and does not depend on the action ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Unlike REPS, our approach does not require a costly nonlinear optimization in the inner loop. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We can greatly reduce the variance of the Q-value differences between rollouts by using the same random number ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These results provide empirical evidence that constraining the KL divergence is a more robust way to choose step ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (2 Preliminaries), p. 4 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (3. Approximately solve this constrained optimization). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 3 (2 Preliminaries), interface p. 2 (2 Preliminaries), p. 4 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (3. Approximately solve this constrained optimization), objective p. 6 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
