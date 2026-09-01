# Problem - MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2104.08212; PDF retrieval source: https://arxiv.org/abs/2104.08212. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, to realize these benefits for a real-world robotic learning system, we need to overcome a number of major challenges [64, 32, 11, 86], which have so far made it ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** General-purpose robotic systems must master a large repertoire of diverse skills to be useful in a range of daily tasks.
- **p. 1 / Abstract - extractive body cue:** While reinforcement learning provides a powerful framework for acquiring individual behaviors, the time needed to acquire each skill makes the prospect of a generalist robot ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we study how a largescale collective robotic learning system can acquire a repertoire of behaviors simultaneously, sharing exploration, experience, and representations across ...
- **p. 1 / Abstract - extractive body cue:** In this framework new tasks can be continuously instantiated from previously learned tasks improving overall performance and capabilities of the system.
- **p. 1 / Abstract - extractive body cue:** To instantiate this system, we develop a scalable and intuitive framework for specifying new tasks through user-provided examples of desired outcomes, devise a multi-robot collective ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, to realize these benefits for a real-world robotic learning system, we need to overcome a number of major challenges [64, 32, 11, 86], which ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In addition, by collecting experience simultaneously using controllers for a variety of tasks with different difficulty, arXiv:2104.08212v2 [cs.RO] 27 Apr 2021

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, to realize these benefits for a real-world robotic learning system, we need to overcome a number of major challenges [64, 32, ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | At each time step, the policy selects an action a given the current state s and the current task Ti that is ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | time, step, policy, selects, action, given, current, state, task, beginning | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | fact, supervised, learning, train, similar, neural, network, architecture | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: time, step, policy, selects, action, given, current, state, task, beginning | p. 3 (III. SYSTEM OVERVIEW), p. 3 (III. SYSTEM OVERVIEW), p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS) |
| Decision / output variable | normalized sample or downstream action; body terms: further, make, following, contributions, address, challenge, providing, rewards | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: goal, multi-task, policy, maximize, expected, rewards, tasks, drawn | p. 4 (III. SYSTEM OVERVIEW), p. 4 (III. SYSTEM OVERVIEW) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 4 (III. SYSTEM OVERVIEW), p. 1 (I. INTRODUCTION) |
| Success / guarantee | cross-domain transfer and task performance | p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 17 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** In addition, by collecting experience simultaneously using controllers for a variety of tasks with different difficulty, arXiv:2104.08212v2 [cs.RO] 27 Apr 2021
- **p. 2 / I. INTRODUCTION - extractive body cue:** We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While existing methods are effective and able to generalize, they require considerable on-robot training time, as well as extensive engineering effort for setting up each ...

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. SYSTEM OVERVIEW)): We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to quickly define new tasks and ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** D) Sample of behaviorally and visually distinct tasks such as covering, chasing, alignment, which we show our method can adapt to.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present our multi-task system as well as examples of some of the tasks that it is capable of performing in Fig.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Can we instead amortize the cost of learning this repertoire over multiple skills, where the effort needed to learn whole repertoire is reduced, easier skills ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** First, we discuss two base choices for the impersonation function fI, then we introduce a more principled solution.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Fig. 4: Video frames for the place-anywhere task. Success and failure videos are iteratively captured in pairs to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Fig. 3: Path of episodes through task impersonation, where episodes are routed to train relevant tasks, and data ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | MT-Opt, which uses impersonated successes and failures, achieves 39% success for the same task, a ≈10× improvement. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. SYSTEM OVERVIEW), p. 3 (III. SYSTEM OVERVIEW), p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 4 (III. SYSTEM OVERVIEW). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. SYSTEM OVERVIEW), p. 3 (III. SYSTEM OVERVIEW), p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 4 (III. SYSTEM OVERVIEW), objective p. 4 (III. SYSTEM OVERVIEW), p. 4 (III. SYSTEM OVERVIEW).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
