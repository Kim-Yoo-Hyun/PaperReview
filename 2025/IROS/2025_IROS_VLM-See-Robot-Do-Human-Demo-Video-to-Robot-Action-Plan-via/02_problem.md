# Problem - VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.08792; PDF retrieval source: https://arxiv.org/pdf/2410.08792. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, significant challenges remain in teaching robots to learn from human videos due to the substantial domain gap between robots and humans.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability.
- **p. 1 / Abstract - extractive PDF cue:** Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning.
- **p. 1 / Abstract - extractive PDF cue:** Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline.
- **p. 1 / Abstract - extractive PDF cue:** We named it SeeDo because it enables the VLM to "see" human demonstrations and explain the corresponding plans to the robot for it to "do".
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, significant challenges remain in teaching robots to learn from human videos due to the substantial domain gap between robots and humans.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To mitigate these limitations, SeeDo integrates not only with a VLM interpreter module but also with a arXiv:2410.08792v2 [cs.RO] 24 Sep 2025

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, significant challenges remain in teaching robots to learn from human videos due to the substantial domain gap between robots and humans. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Some employ pretrained VLMs for further fine-tuning to learn the mapping from visual inputs and language instructions to actions [5, 6], or ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Some, employ, pretrained, VLMs, further, fine-tuning, learn, mapping, visual, inputs | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | SeeDo-generated, task, plans, seamlessly, processed, step, robot, action | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Some, employ, pretrained, VLMs, further, fine-tuning, learn, mapping, visual, inputs | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, follows, introduce, SeeDo, VLM-based, agent, integrates | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Context, length, becomes, major, constraint, when, VLMs, process | p. 3 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To mitigate these limitations, SeeDo integrates not only with a VLM interpreter module but also with a arXiv:2410.08792v2 [cs.RO] 24 Sep 2025

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION)): In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM interpreter modules to interpret long-horizon ...

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Inspired by this capability, we propose SeeDo, a modularized agent centered around a VLM.
- **p. 3 / III. METHOD - extractive PDF cue:** To alleviate these issues, we introduce a visual prompting module in SeeDo that enhances the visual capabilities of the VLM.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** First, VLMs' rich commonsense knowledge enables them to understand objects and their relationships, helping robots understand the task goals despite the embodiment gap.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | However, spatial errors remain the main source of SeeDo 's failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Model Success Rate Failure Reason TSR↑ FSR↑ SSR↑ Vision↓ Spatial↓ Temporal↓ SeeDo w/o V.P. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), objective p. 3 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
