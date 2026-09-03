# Problem - Maximum a Posteriori Policy Optimisation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=S1ANxQW0b; PDF retrieval source: https://openreview.net/forum?id=S1ANxQW0b. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.
- **p. 1 / ABSTRACT - extractive body cue:** We show that several existing methods can directly be related to our derivation.
- **p. 1 / ABSTRACT - extractive body cue:** We develop two off-policy algorithms and demonstrate that they are competitive with the state-of-the-art in deep reinforcement learning.
- **p. 1 / ABSTRACT - extractive body cue:** In particular, for continuous control, our method outperforms existing methods with respect to sample efficiency, premature convergence and robustness to hyperparameter settings.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Model free reinforcement learning algorithms can acquire sophisticated behaviours by interacting with the environment while receiving simple rewards.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Two types of algorithms currently dominate scalable learning for continuous control problems: First, Trust-Region Policy Optimisation (TRPO; Schulman et al.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks. | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen. | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF body |
| State / latent | subsequently, updates, policy, better, actions, state, will, have, probabilities, chosen | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | Instead, uses, samples, Q-function, compare, different, actions, given | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: subsequently, updates, policy, better, actions, state, will, have, probabilities, chosen | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: novel, off-policy, algorithm, benefits, best, properties, classes, introduce | p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | expected return / constrained return; cue terms: contrast, typical, off-policy, value-gradient, algorithms, algorithm, does, require | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Success / guarantee | task return, success and safe execution | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Two types of algorithms currently dominate scalable learning for continuous control problems: First, Trust-Region Policy Optimisation (TRPO; Schulman et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We evaluate our algorithm on a broad spectrum of continuous control problems including a 56 DoF humanoid body.

## What the Paper Changes

PDF body contribution framing (p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION)): In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.

- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show below that several algorithms, including TRPO, can be directly related to this perspective.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), objective p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks. (p. 1, 1 INTRODUCTION).
- **Formulation-changing contribution:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. (p. 1, 1 INTRODUCTION).
- **Assumption/failure evidence:** The case for the Walker-2D parkour domain (where we compare against a PPO baseline) is even more striking: where standard PPO requires approximately 1M trajectories to find a good policy ... (p. 9, 5 EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
