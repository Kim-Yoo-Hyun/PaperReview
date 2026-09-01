# Problem - Asynchronous Methods for Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v48/mniha16.html; PDF retrieval source: https://proceedings.mlr.press/v48/mniha16.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract)): We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.
- **p. 1 / Abstract - extractive PDF cue:** We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four methods ...
- **p. 1 / Abstract - extractive PDF cue:** The best performing method, an asynchronous variant of actor-critic, surpasses the current state-of-the-art on the Atari domain while training for half the time on a ...
- **p. 1 / Abstract - extractive PDF cue:** Furthermore, we show that asynchronous actor-critic succeeds on a wide variety of continuous motor control problems as well as on a new task of navigating ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Deep neural networks provide rich representations that can enable reinforcement learning (RL) algorithms to perform effectively.
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** Keeping the learners on a single machine removes the communication costs of sending gradients and parameters and enables us to use Hogwild!

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural ... | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | The action value Qπ(s, a) = E [Rt/st = s, a] is the expected return for selecting action a in state s ... | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF |
| State / latent | action, value, Rt/st, expected, return, selecting, state, following, policy, optimal | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | When, approximate, value, function, baseline, quantity, scale, policy | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: action, value, Rt/st, expected, return, selecting, state, following, policy, optimal | p. 2 (3. Reinforcement Learning Background), p. 2 (3. Reinforcement Learning Background), p. 3 (3. Reinforcement Learning Background) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: present, asynchronous, variants, four, standard, reinforcement, learning, algorithms | p. 1 (Abstract), p. 1 (Abstract), p. 3 (4. Asynchronous RL Framework) |
| Objective / loss / cost | expected return / constrained return; cue terms: Initialize, thread, step, counter, target, network, weights, gradients | p. 3 (4. Asynchronous RL Framework), p. 4 (4. Asynchronous RL Framework), p. 2 (3. Reinforcement Learning Background), p. 3 (3. Reinforcement Learning Background), p. 4 (4. Asynchronous RL Framework), p. 1 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (4. Asynchronous RL Framework), p. 1 (Abstract), p. 2 (3. Reinforcement Learning Background) |
| Success / guarantee | task return, success and safe execution | p. 5 (5. Experiments), p. 6 (5.4. Labyrinth), p. 6 (5.4. Labyrinth) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive PDF cue:** We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four methods ...

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 1 (Abstract), p. 3 (4. Asynchronous RL Framework)): We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four methods to successfully train neural network ...

- **p. 1 / Abstract - extractive PDF cue:** We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** Keeping the learners on a single machine removes the communication costs of sending gradients and parameters and enables us to use Hogwild!

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | While this shows that stable online Q-learning is possible without experience replay, which was used for this purpose ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Somewhat surprisingly, asynchronous one-step Q-learning and Sarsa algorithms exhibit superlinear speedups that cannot be explained by purely computational ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Finally, we analyzed the stability and robustness of the four proposed asynchronous algorithms. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (3. Reinforcement Learning Background), p. 2 (3. Reinforcement Learning Background), p. 3 (3. Reinforcement Learning Background), p. 3 (4. Asynchronous RL Framework). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), interface p. 2 (3. Reinforcement Learning Background), p. 2 (3. Reinforcement Learning Background), p. 3 (3. Reinforcement Learning Background), p. 3 (4. Asynchronous RL Framework), objective p. 3 (4. Asynchronous RL Framework), p. 4 (4. Asynchronous RL Framework), p. 2 (3. Reinforcement Learning Background), p. 3 (3. Reinforcement Learning Background), p. 4 (4. Asynchronous RL Framework), p. 1 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
