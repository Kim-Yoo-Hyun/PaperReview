# Problem - One-Shot Visual Imitation Learning via Meta-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.07326; PDF retrieval source: https://arxiv.org/pdf/1703.07326. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): Demonstrations are an extremely convenient form of information we can use to teach robots to overcome these two challenges.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Imitation learning has been commonly applied to solve different tasks in isolation.
- **p. 1 / Abstract - extractive PDF cue:** This usually requires either careful feature engineering, or a significant number of samples.
- **p. 1 / Abstract - extractive PDF cue:** This is far from what we desire: ideally, robots should be able to learn from very few demonstrations of any given task, and instantly generalize ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we consider the setting where there is a very large (maybe infinite) set of tasks, and each task has many instantiations.
- **p. 1 / 1 Introduction - extractive PDF cue:** Demonstrations are an extremely convenient form of information we can use to teach robots to overcome these two challenges.
- **p. 2 / 1 Introduction - extractive PDF cue:** And second, there are many tasks that are extremely difficult to explain in words, even if we assume perfect linguistic abilities: for example, explaining how ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Demonstrations are an extremely convenient form of information we can use to teach robots to overcome these two challenges. | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | When conditioned on both the first demonstration and this observation, the network is trained to output the corresponding action. systems are not ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | When, conditioned, first, demonstration, observation, network, trained, output, corresponding, action | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | note, pair, demonstrations, same, task, provides, supervised, training | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: When, conditioned, first, demonstration, observation, network, trained, output, corresponding, action | p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: meta-learning, framework, achieving, capability, call, one-shot, imitation, learning | p. 1 (Abstract), p. 5 (B C), p. 3 (1 Introduction) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: where, objective, maximize, expected, performance, learned, policy, when | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Success / guarantee | closed-loop task success and robustness | p. 7 (5 Experiments), p. 7 (5 Experiments), p. 14 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** And second, there are many tasks that are extremely difficult to explain in words, even if we assume perfect linguistic abilities: for example, explaining how ...
- **p. 2 / 1 Introduction - extractive PDF cue:** (c) We can phrase this as a supervised learning problem, where we train this network on a set of training tasks, and with enough examples ...
- **p. 1 / 1 Introduction - extractive PDF cue:** To accomplish this, we must solve two broad problems.
- **p. 3 / 1 Introduction - extractive PDF cue:** The use of soft attention over both types of inputs made strong generalization possible.

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 5 (B C), p. 3 (1 Introduction), p. 1 (Abstract), p. 5 (B C)): In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.

- **p. 5 / B C - extractive PDF cue:** The memory content to be extracted consists of the coordinates of each block, concatenated with the input embedding.
- **p. 3 / 1 Introduction - extractive PDF cue:** In particular, on a family of block stacking tasks, our neural network policy was able to perform well on novel block configurations which were not ...
- **p. 1 / Abstract - extractive PDF cue:** Our experiments show that the use of soft attention allows the model to generalize to conditions and tasks unseen in the training data.
- **p. 5 / B C - extractive PDF cue:** Intuitively, this operation allows each block to query other blocks in relation to itself (e.g. find the closest block), and extract the queried information.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 19 | Figure 6: Breakdown of the success and failure scenarios. The area that each color occupies represent the ratio ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 22 | Table 8: Breakdown of success and failure scenarios for DAGGER policy. 10 | reported limitation/failure wording; scope must be verified |
| body cue at p. 22 | Table 6: Success rates of a set of tasks that are equivalent up to permutations, using the DAGGER ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In fact, even our scripted policy frequently fails on the hardest tasks. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (B C). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), interface p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (B C), objective p. 2 (1 Introduction), p. 2 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
