# Problem - What Matters for Batch Online Reinforcement Learning in Robotics?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10006859; PDF retrieval source: https://arxiv.org/pdf/2505.08078. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 4 (3 Preliminaries)): Learning from autonomously collected data for policy improvement, however, remains a significant challenge in robot learning as current algorithms struggle to fully leverage this autonomous data [3].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The ability to learn from large batches of autonomously collected data for policy improvement-a paradigm we refer to as batch online reinforcement learning-holds the promise ...
- **p. 1 / Abstract - extractive PDF cue:** Yet, despite the promise of this paradigm, it remains challenging to achieve due to algorithms not being able to learn effectively from the autonomous data.
- **p. 1 / Abstract - extractive PDF cue:** For example, prior works have applied imitation learning and filtered imitation learning methods to the batch online RL problem, but these algorithms often fail to ...
- **p. 1 / Abstract - extractive PDF cue:** This raises the question of what matters for effective batch online reinforcement learning in robotics.
- **p. 1 / Abstract - extractive PDF cue:** Motivated by this question, we perform a systematic empirical study of three axes-(i) algorithm class, (ii) policy extraction methods, and (iii) policy expressivity-and analyze how ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Learning from autonomously collected data for policy improvement, however, remains a significant challenge in robot learning as current algorithms struggle to fully leverage this autonomous ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Although recent works have focused on mitigating this gap by proposing large robotic datasets [1, 2], robot learning continues to operate under a substantially smaller ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Learning from autonomously collected data for policy improvement, however, remains a significant challenge in robot learning as current algorithms struggle to fully ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | observations, general, recipe, effective, batch, online, train, expressive, policy, actor | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | RGB, images, robot, proprioceptive, state, joint, end-effector, positions | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: observations, general, recipe, effective, batch, online, train, expressive, policy, actor | p. 2 (1 Introduction), p. 6 (3 Preliminaries), p. 8 (3 Preliminaries) |
| Decision / output variable | normalized sample or downstream action; body terms: recipe, simple, practical, addition, induce, even, more, diversity | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Preliminaries) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: traditional, objective, find, policy, maximizes, expected, discounted, rewards | p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries), p. 8 (3 Preliminaries) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3 Preliminaries), p. 4 (3 Preliminaries), p. 6 (3 Preliminaries) |
| Success / guarantee | cross-domain transfer and task performance | p. 9 (6 Discussion), p. 15 (Figure/Table caption), p. 5 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** Although recent works have focused on mitigating this gap by proposing large robotic datasets [1, 2], robot learning continues to operate under a substantially smaller ...
- **p. 2 / 1 Introduction - extractive PDF cue:** IL methods have inherent limitations in their ability to leverage suboptimal demonstrations within autonomously collected datasets, while methods based on weighted or filtered IL often ...
- **p. 3 / 3 Preliminaries - extractive PDF cue:** Robotics operates under a smaller data regime than other fields due to the difficulty in obtaining data.
- **p. 4 / 3 Preliminaries - extractive PDF cue:** The size of D0 varies from 5 to 100 demonstrations depending on the task difficulty; we choose this size such that the base policy π0 ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries)): On top of the recipe, we propose a simple practical addition to induce even more diversity and achieve better sample efficiency: applying a small amount of temporally correlated noise modeled ...

- **p. 2 / 1 Introduction - extractive PDF cue:** Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function ...
- **p. 5 / 3 Preliminaries - extractive PDF cue:** In Figure 3, we present the average normalized returns over iterations of batch online RL for each algorithm class on our six tasks.
- **p. 5 / 3 Preliminaries - extractive PDF cue:** Based on our results, in Section 5 we present a recipe for batch online RL, and demonstrate the practicality of the recipe on a challenging ...
- **p. 6 / 3 Preliminaries - extractive PDF cue:** We present the results of data scaling in Figure 5.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Our work presents a general recipe on batch online RL, though it does have a number of limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 7 Limitations In this work, we empirically analyze the key axes that affect performance in batch online RL, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Vanilla IL performs the worst on all tasks, which is perhaps not surprising as vanilla IL will fit ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Intuitively, this makes sense because value-based RL methods can use the Q-function to determine which states and actions ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 6 (3 Preliminaries), p. 8 (3 Preliminaries), p. 3 (3 Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), interface p. 2 (1 Introduction), p. 6 (3 Preliminaries), p. 8 (3 Preliminaries), p. 3 (3 Preliminaries), objective p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries), p. 8 (3 Preliminaries).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
