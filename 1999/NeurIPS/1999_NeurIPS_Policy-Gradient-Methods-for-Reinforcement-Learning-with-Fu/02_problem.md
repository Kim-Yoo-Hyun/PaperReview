# Problem - Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html; PDF retrieval source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract)): The value-function approach has worked well in many applications, but has several limitations.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Function approximation is essential to reinforcement learning, but the standard approach of approximating a value function and determining a policy from it has so far ...
- **p. 1 / Abstract - extractive body cue:** In this paper we explore an alternative approach in which the policy is explicitly represented by its own function approximator, independent of the value function, ...
- **p. 1 / Abstract - extractive body cue:** Williams's REINFORCE method and actor-critic methods are examples of this approach.
- **p. 1 / Abstract - extractive body cue:** Our main new result is to show that the gradient can be written in a form suitable for estimation from experience aided by an approximate ...
- **p. 1 / Abstract - extractive body cue:** Using this result, we prove for the first time that a version of policy iteration with arbitrary differentiable function approximation is convergent to a locally ...
- **p. 1 / Abstract - extractive body cue:** The value-function approach has worked well in many applications, but has several limitations.
- **p. 2 / Abstract - extractive body cue:** Our result strengthens theirs and generalizes it to arbitrary differentiable function approximators.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The value-function approach has worked well in many applications, but has several limitations. | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is ... | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF |
| State / latent | example, policy, might, represented, neural, network, whose, input, representation, state | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | average, reward, formulation, value, state-action, pair, given, policy | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: example, policy, might, represented, neural, network, whose, input, representation, state | p. 2 (Abstract), p. 1 (Abstract), p. 3 (Abstract) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: Konda, Tsitsiklis, prep, independently, developed, very, simialr, result | p. 2 (Abstract) |
| Objective / loss / cost | expected return / constrained return; cue terms: explore, alternative, policy, explicitly, represented, function, approximator, independent | p. 3 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 3 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (Abstract), p. 3 (Abstract), p. 1 (Abstract) |
| Success / guarantee | task return, success and safe execution | p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** Function approximation is essential to reinforcement learning, but the standard approach of approximating a value function and determining a policy from it has so far ...
- **p. 2 / Abstract - extractive body cue:** Our result strengthens theirs and generalizes it to arbitrary differentiable function approximators.

## What the Paper Changes

PDF contribution framing (p. 2 (Abstract)): Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours.

- additional contribution cue 없음

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | As a result, VAPS does not converge to a locally optimal policy, except in the case that no ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | In any event, the key aspect of both expressions for the gradient is that their are no terms ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | (This follows immediately because l:a 87r~~a) = 0, Vs E S.) The choice of v does not affect ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), interface p. 2 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 1 (Abstract), objective p. 3 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 3 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
