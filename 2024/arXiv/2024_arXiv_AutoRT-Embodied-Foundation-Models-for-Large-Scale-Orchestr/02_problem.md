# Problem - AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://deepmind.google/research/publications/48151/; PDF retrieval source: https://deepmind.google/research/publications/48151/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): The bottleneck for achieving these goals, however, is the need for large amounts of robotic experience in the real world - much larger than robot datasets collected in lab settings ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Foundation models that incorporate language, vision, and more recently actions have revolutionized the ability to harness internet scale data to reason about useful tasks.
- **p. 1 / ABSTRACT - extractive body cue:** However, one of the key challenges of training embodied foundation models is the lack of data grounded in the physical world.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios ...
- **p. 1 / ABSTRACT - extractive body cue:** AutoRT leverages vision-language models (VLMs) for scene understanding and grounding, and further uses large language models (LLMs) for proposing diverse and novel instructions to be ...
- **p. 1 / ABSTRACT - extractive body cue:** Guiding data collection by tapping into the knowledge of foundation models enables AutoRT to effectively reason about autonomy tradeoffs and safety while significantly scaling up ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The bottleneck for achieving these goals, however, is the need for large amounts of robotic experience in the real world - much larger than robot ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While current robotic learning methods offer appealing solutions for acquiring individual robotic skills, and large language models (LLMs), vision-language models (VLMs) and large multimodal models ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The bottleneck for achieving these goals, however, is the need for large amounts of robotic experience in the real world - much ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | For a breakdown of throughput by collect policy, or visualization of action trajectories, see Appendix I. | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | breakdown, throughput, collect, policy, visualization, action, trajectories, Appendix, generated, task | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | AutoRT, best, knowledge, first, system, where, LLM-controlled, robots | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: breakdown, throughput, collect, policy, visualization, action, trajectories, Appendix, generated, task | p. 5 (3. Place the napkin onto), p. 5 (3. Place the napkin onto), p. 2 (1 INTRODUCTION) |
| Decision / output variable | normalized sample or downstream action; body terms: AutoRT, system, leverages, existing, foundation, models, scale, deployment | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: process, takes, account, constraints, specified, constitutional, prompting, where | p. 2 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3. Place the napkin onto), p. 7 (3. Place the napkin onto), p. 7 (3. Place the napkin onto) |
| Success / guarantee | cross-domain transfer and task performance | p. 7 (Figure/Table caption), p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** While current robotic learning methods offer appealing solutions for acquiring individual robotic skills, and large language models (LLMs), vision-language models (VLMs) and large multimodal models ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our system for large-scale orchestration of robotic agents, which we call AutoRT, tackles this problem.

## What the Paper Changes

PDF contribution framing (p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 4 (3. Place the napkin onto), p. 4 (3. Place the napkin onto)): In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios with minimal human supervision.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show that AutoRT scales robot deployment by allowing 1 human to supervise 3-5 mobile manipulators.
- **p. 1 / ABSTRACT - extractive body cue:** Guiding data collection by tapping into the knowledge of foundation models enables AutoRT to effectively reason about autonomy tradeoffs and safety while significantly scaling up ...
- **p. 4 / 3. Place the napkin onto - extractive body cue:** Green sections are contributions of this work.
- **p. 4 / 3. Place the napkin onto - extractive body cue:** No part of this requires advance knowledge of the layout of the environment or objects it contains, making it easy to run on a fleet ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Failures of perception such as hallucination of objects, lack of generalization to novel environments, and motion blur can ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Despite the promise of AutoRT, the current approach comes with a number of limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | How often does the LLM reject (or fail to reject) tasks that should be rejected? | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Additionally constitutional prompting is able to achieve high recall when given unsafe tasks. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3. Place the napkin onto), p. 5 (3. Place the napkin onto), p. 2 (1 INTRODUCTION), p. 7 (3. Place the napkin onto). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 5 (3. Place the napkin onto), p. 5 (3. Place the napkin onto), p. 2 (1 INTRODUCTION), p. 7 (3. Place the napkin onto), objective p. 2 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
