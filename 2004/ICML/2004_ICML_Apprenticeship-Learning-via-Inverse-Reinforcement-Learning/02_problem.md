# Problem - Apprenticeship Learning via Inverse Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ai.stanford.edu/~pabbeel/irl/; PDF retrieval source: https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Preliminaries)): From conversations with engineers in industry and our own experience in applying reinforcement learning algorithms to several robots, we believe that, for many problems, the difficulty of manually specifying a ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We consider learning in a Markov decision process where we are not explicitly given a reward function, but where instead we can observe an expert ...
- **p. 1 / Abstract - extractive PDF cue:** This setting is useful in applications (such as the task of driving) where it may be difficult to write down an explicit reward function specifying ...
- **p. 1 / Abstract - extractive PDF cue:** We think of the expert as trying to maximize a reward function that is expressible as a linear combination of known features, and give an ...
- **p. 1 / Abstract - extractive PDF cue:** Our algorithm is based on using "inverse reinforcement learning" to try to recover the unknown reward function.
- **p. 1 / Abstract - extractive PDF cue:** We show that our algorithm terminates in a small number of iterations, and that even though we may never recover the expert's reward function, the ...
- **p. 1 / 1. Introduction - extractive PDF cue:** From conversations with engineers in industry and our own experience in applying reinforcement learning algorithms to several robots, we believe that, for many problems, the ...
- **p. 1 / 1. Introduction - extractive PDF cue:** However, we believe that even the reward function is frequently difficult to specify manually.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | From conversations with engineers in industry and our own experience in applying reinforcement learning algorithms to several robots, we believe that, for ... | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | A policy π is a mapping from states to probability distributions over actions. | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | policy, mapping, states, probability, distributions, over, actions, value, Es0, Here | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | Given, reward, function, MDPs, state, transition, probabilities, value | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: policy, mapping, states, probability, distributions, over, actions, value, Es0, Here | p. 2 (2. Preliminaries), p. 2 (2. Preliminaries), p. 1 (1. Introduction) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: assume, expert, trying, without, necessarily, succeeding, optimize, unknown | p. 2 (1. Introduction), p. 3 (3. Algorithm) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: Three, iterations, max-margin, algorithm, reward, function, being, optimized | p. 3 (3. Algorithm), p. 3 (3. Algorithm), p. 4 (3. Algorithm), p. 4 (3.1. A simpler algorithm) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Algorithm), p. 4 (3. Algorithm), p. 4 (3. Algorithm) |
| Success / guarantee | closed-loop task success and robustness | p. 4 (4. Theoretical results), p. 5 (4. Theoretical results), p. 5 (5.1. Gridworld) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** However, we believe that even the reward function is frequently difficult to specify manually.
- **p. 2 / 1. Introduction - extractive PDF cue:** Note however, that this method is applicable only to problems where the task is to mimic the expert's trajectory.
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we assume that the expert is trying (without necessarily succeeding) to optimize an unknown reward function that can be expressed as a ...
- **p. 3 / 2. Preliminaries - extractive PDF cue:** The generalization to approximate RL algorithms offers no special difficulties; see the full paper.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 3 (3. Algorithm)): In this paper, we assume that the expert is trying (without necessarily succeeding) to optimize an unknown reward function that can be expressed as a linear combination of known "features." ...

- **p. 3 / 3. Algorithm - extractive PDF cue:** (The SVM problem is a quadratic programming problem (QP), so we can also use any generic QP solver.) In Figure 1 we show an example ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | The agent has four actions to try to move in each of the four compass directions, but with ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Nice: The highest priority is to avoid collisions than the "mimic the expert" algorithm initially. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Since no "true" reward was ever specified or used in the experiments, we cannot report on the results ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Table 1. Feature expectations of teacher ˆµE and of selected/learned policy µ(˜π) (as estimated by Monte Carlo). and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (2. Preliminaries), p. 2 (2. Preliminaries), p. 1 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Preliminaries), interface p. 2 (2. Preliminaries), p. 2 (2. Preliminaries), p. 1 (1. Introduction), p. 1 (1. Introduction), objective p. 3 (3. Algorithm), p. 3 (3. Algorithm), p. 4 (3. Algorithm), p. 4 (3.1. A simpler algorithm).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
