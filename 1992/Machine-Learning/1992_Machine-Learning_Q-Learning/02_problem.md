# Problem - Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00992698; PDF retrieval source: https://doi.org/10.1007/BF00992698. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction)): Section 2 describes the problem, the method, and the notation, section 3 gives an overview of the proof, and section 4 discusses two extensions.

## PDF Body Digest

- **p. 1 / 1. Introduction - extractive body cue:** O~-learning (Watkins, 1989) is a form of model-free reinforcement learning.
- **p. 1 / 1. Introduction - extractive body cue:** It can also be viewed as a method of asynchronous dynamic programming (DP).
- **p. 1 / 1. Introduction - extractive body cue:** It provides agents with the capability of learning to act optimally in Markovian domains by experiencing the consequences of actions, without requiring them to build ...
- **p. 1 / 1. Introduction - extractive body cue:** Learning proceeds similarly to Sutton's (1984; 1988) method of temporal differences (TD): an agent tries an action at a particular state, and evaluates its consequences ...
- **p. 1 / 1. Introduction - extractive body cue:** By trying all actions in all states repeatedly, it learns which are best overall, judged by long-term discounted reward.
- **p. 1 / 1. Introduction - extractive body cue:** Section 2 describes the problem, the method, and the notation, section 3 gives an overview of the proof, and section 4 discusses two extensions.
- **p. 3 / 2. The task for ~-learning - extractive body cue:** In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Section 2 describes the problem, the method, and the notation, section 3 gives an overview of the proof, and section 4 discusses ... | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | Y In other words, the ~ value is the expected discounted reward for executing action a at state x and following policy ... | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF |
| State / latent | other, words, value, expected, discounted, reward, executing, action, state, following | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | considered, strong, condition, states, actions, selected--however, under, stochastic | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: other, words, value, expected, discounted, reward, executing, action, state, following | p. 2 (2. The task for ~-learning), p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: learning, agent, experience, consists, sequence, distinct, stages, episodes | p. 3 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 4 (3. The convergence proof) |
| Objective / loss / cost | expected return / constrained return; cue terms: task, facing, agent, determining, optimal, policy, maximizes, total | p. 3 (2. The task for ~-learning), p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3.2. The theorem), p. 4 (3. The convergence proof), p. 6 (3.1. Lemmas) |
| Success / guarantee | task return, success and safe execution | p. 4 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 5 (3.1. Lemmas) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Section 2 describes the problem, the method, and the notation, section 3 gives an overview of the proof, and section 4 discusses two extensions.

## What the Paper Changes

PDF contribution framing (p. 3 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 4 (3. The convergence proof), p. 1 (1. Introduction)): In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes.

- **p. 4 / 3. The convergence proof - extractive body cue:** A state of the AFI~, (x, n), consists of a card number (or level) n, together with a state x from the real process.
- **p. 4 / 3. The convergence proof - extractive body cue:** Replaying the episode on card t consists of emitting the reward, rt, written on the card, and then moving to the next state (Yt, t ...
- **p. 1 / 1. Introduction - extractive body cue:** Examples of its use include Barto and Singh (1990), Sutton (1990), Chapman and Kaelbling (1991), Mahadevan and Connell (1991), and Lin (1992), who developed it ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The theorem above only proves the convergence of a restricted version of Watkins' (1989) comprehensive Q-learning algorithm, since ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (2. The task for ~-learning), p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), interface p. 2 (2. The task for ~-learning), p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning), p. 1 (1. Introduction), objective p. 3 (2. The task for ~-learning), p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
