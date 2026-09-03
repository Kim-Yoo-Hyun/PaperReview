# Problem - Hindsight Experience Replay

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1707.01495; PDF retrieval source: https://arxiv.org/pdf/1707.01495. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 5 (2 Background), p. 1 (1 Introduction), p. 3 (2 Background), p. 3 (2 Background), p. 1 (1 Introduction)): These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly care about (such as binary ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Dealing with sparse rewards is one of the biggest challenges in Reinforcement Learning (RL).
- **p. 1 / Abstract - extractive body cue:** We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need ...
- **p. 1 / Abstract - extractive body cue:** It can be combined with an arbitrary off-policy RL algorithm and may be seen as a form of implicit curriculum.
- **p. 1 / Abstract - extractive body cue:** We demonstrate our approach on the task of manipulating objects with a robotic arm.
- **p. 1 / Abstract - extractive body cue:** In particular, we run experiments on three different tasks: pushing, sliding, and pick-and-place, in each case using only binary rewards indicating whether or not the ...
- **p. 5 / 2 Background - extractive body cue:** These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly ...
- **p. 1 / 1 Introduction - extractive body cue:** However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the ... | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | A deterministic policy is a mapping from states to actions: π : S →A. | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF body |
| State / latent | deterministic, policy, mapping, states, actions, setup, possible, train, approximator, Q-function | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | training, universal, policies, Schaul, take, input, only, current | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: deterministic, policy, mapping, states, actions, setup, possible, train, approximator, Q-function | p. 2 (2 Background), p. 3 (2 Background), p. 2 (1 Introduction) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: introduce, technique, called, Hindsight, Experience, Replay, HER, allows | p. 2 (1 Introduction), p. 1 (Abstract), p. 4 (2 Background) |
| Objective / loss / cost | expected return / constrained return; cue terms: network, trained, mini-batch, gradient, descent, loss, encourages, approximated | p. 2 (2 Background), p. 2 (2 Background), p. 3 (2 Background), p. 3 (2 Background) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (2 Background), p. 3 (2 Background), p. 3 (2 Background) |
| Success / guarantee | task return, success and safe execution | p. 9 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is ...
- **p. 3 / 2 Background - extractive body cue:** While using a shaped reward solves the problem in our toy environment, it may be difficult to apply to more complicated problems.
- **p. 3 / 2 Background - extractive body cue:** VIME (Houthooft et al., 2016), count-based exploration (Ostrovski et al., 2017) or bootstrapped DQN (Osband et al., 2016)) does not help here because the real ...
- **p. 1 / 1 Introduction - extractive body cue:** Reinforcement learning (RL) combined with neural networks has recently led to a wide range of successes in learning policies for sequential decision-making problems.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 1 (Abstract), p. 4 (2 Background), p. 2 (2 Background), p. 3 (2 Background)): In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can be combined with any off-policy ...

- **p. 1 / Abstract - extractive body cue:** We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need ...
- **p. 4 / 2 Background - extractive body cue:** In order to solve this problem we introduce the technique of Hindsight Experience Replay which is the crux of our approach.
- **p. 2 / 2 Background - extractive body cue:** In this section we introduce reinforcement learning formalism used in the paper as well as RL algorithms we use in our experiments.
- **p. 3 / 2 Background - extractive body cue:** Instead of shaping the reward we propose a different solution which does not require any domain knowledge.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | In this task a puck is placed on a long slippery table and the target position is outside ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | It does not have to be robust to noisy observations because it is not used during the deployment ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our results suggest that domain-agnostic reward shaping does not work well (at least in the simple forms we ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Surprisingly neither DDPG, nor DDPG+HER was able to successfully solve any of the tasks with any of these ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (2 Background), p. 3 (2 Background), p. 2 (1 Introduction), p. 3 (2 Background). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 5 (2 Background), p. 1 (1 Introduction), p. 3 (2 Background), p. 3 (2 Background), p. 1 (1 Introduction), interface p. 2 (2 Background), p. 3 (2 Background), p. 2 (1 Introduction), p. 3 (2 Background), objective p. 2 (2 Background), p. 2 (2 Background), p. 3 (2 Background), p. 3 (2 Background).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is also carefully shaped (Ng et ... (p. 1, 1 Introduction).
- **Formulation-changing contribution:** In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can be combined with any off-policy ... (p. 2, 1 Introduction).
- **Assumption/failure evidence:** These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly care about (such as binary ... (p. 5, 2 Background).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
