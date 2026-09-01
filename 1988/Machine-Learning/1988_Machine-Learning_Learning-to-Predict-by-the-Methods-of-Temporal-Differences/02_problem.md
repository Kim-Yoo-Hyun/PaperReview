# Problem - Learning to Predict by the Methods of Temporal Differences

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00115009; PDF retrieval source: https://doi.org/10.1007/BF00115009. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): Most pattern recognition problems, for examt)le, can be treated as prediction problems in which the classifier nmst predict the correct classifications.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This article introduces a class of incremental learning procedures specialized for prediction that is, for using past experience with an incompletely known system to predict ...
- **p. 1 / Abstract - extractive body cue:** Whereas conventional prediction-learning methods assign credit by means of the difference between predicted and actual outcomes, tile new methods assign credit by means of the ...
- **p. 1 / Abstract - extractive body cue:** Although such temporal-difference method~ have been used in Samuel's checker player, Holland's bucket brigade, and the author's Adaptive Heuristic Critic, they have remained poorly understood.
- **p. 1 / Abstract - extractive body cue:** Here we prove their convergence and optimality for special cases and relate them to supervised-learning methods.
- **p. 1 / Abstract - extractive body cue:** For most real-world prediction problems, telnporal-differenee methods require less memory and less peak computation than conventional methods and they produce more accurate predictions.
- **p. 1 / 1. Introduction - extractive body cue:** Most pattern recognition problems, for examt)le, can be treated as prediction problems in which the classifier nmst predict the correct classifications.
- **p. 1 / 1. Introduction - extractive body cue:** Learning-to-predict problems also arise in heuristic search, e.g., in learning an evahmtion function that predicts tile utility of searching particular parts of tile search space, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Most pattern recognition problems, for examt)le, can be treated as prediction problems in which the classifier nmst predict the correct classifications. | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | For each nonterminal state i, there was a corresponding observation vector xi; if the walk was in state i at time t ... | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF |
| State / latent | nonterminal, state, there, corresponding, observation, vector, walk, time, then, Thus | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | multi-layer, networks, focuses, learning, input-output, pings, more, comt | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: nonterminal, state, there, corresponding, observation, vector, walk, time, then, Thus | p. 11 (3.2 A random-walk example), p. 11 (3.2 A random-walk example), p. 3 (1. Introduction) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: TTON, article, introduce, provide, tilt, first, formal, theory | p. 2 (1. Introduction), p. 11 (3.2 A random-walk example), p. 2 (1. Introduction) |
| Objective / loss / cost | expected return / constrained return; cue terms: position, known, long, experience, lead, time, loss, only | p. 9 (3.1 A game-playing example), p. 9 (3.1 A game-playing example), p. 10 (3.1 A game-playing example), p. 24 (4.3 Temporal-difference methods as gradient descent), p. 24 (4.3 Temporal-difference methods as gradient descent), p. 12 (3.2 A random-walk example) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 10 (3.1 A game-playing example), p. 13 (3.2 A random-walk example), p. 13 (3.2 A random-walk example) |
| Success / guarantee | task return, success and safe execution | p. 13 (3.2 A random-walk example), p. 28 (6.1 Samuel's checker-playing program), p. 12 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Learning-to-predict problems also arise in heuristic search, e.g., in learning an evahmtion function that predicts tile utility of searching particular parts of tile search space, ...
- **p. 2 / 1. Introduction - extractive body cue:** S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 11 (3.2 A random-walk example), p. 2 (1. Introduction), p. 8 (3. Examples of faster learning with TD methods), p. 9 (3.1 A game-playing example)): S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures specialized for prediction problems.

- **p. 11 / 3.2 A random-walk example - extractive body cue:** In this paper, we propose that the only required characteristic is that the system predicted be a dynamical one, that it have a state which ...
- **p. 2 / 1. Introduction - extractive body cue:** This simplification allows us to evaluate them in isolation and has enabled us to obtain formal results.
- **p. 8 / 3. Examples of faster learning with TD methods - extractive body cue:** In this section, we develop two illustrative examples: a game-playing example to help develop intuitions, and a random-walk example as a simple demonstration with experimental ...
- **p. 9 / 3.1 A game-playing example - extractive body cue:** What evaluation should the novel position receive as a result of this experience?

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 32 | In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 25 | In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | We cannot apply this lemma directly to D(I - Q) because it is not symmetric. | reported limitation/failure wording; scope must be verified |
| body cue at p. 22 | SUTTON and biased coins, and thus cannot be uniquely determined. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 11 (3.2 A random-walk example), p. 11 (3.2 A random-walk example), p. 3 (1. Introduction), p. 9 (3.1 A game-playing example). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 11 (3.2 A random-walk example), p. 11 (3.2 A random-walk example), p. 3 (1. Introduction), p. 9 (3.1 A game-playing example), objective p. 9 (3.1 A game-playing example), p. 9 (3.1 A game-playing example), p. 10 (3.1 A game-playing example), p. 24 (4.3 Temporal-difference methods as gradient descent), p. 24 (4.3 Temporal-difference methods as gradient descent), p. 12 (3.2 A random-walk example).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
