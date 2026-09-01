# Problem - RT-H: Action Hierarchies Using Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p049.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p049.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Language is the engine of human reasoning, empowering us to break complex concepts into simpler ones, to correct our misunderstandings, and to generalize concepts in new settings.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Language provides a way to break down complex concepts into digestible pieces.
- **p. 1 / Abstract - extractive body cue:** Recent works in robot imitation learning have proposed learning language-conditioned policies that predict actions given visual observations and the high-level task specified in language.
- **p. 1 / Abstract - extractive body cue:** These methods leverage the structure of natural language to share data between semantically similar tasks (e.g., "pick coke can" and "pick an apple") in multi-task ...
- **p. 1 / Abstract - extractive body cue:** However, as tasks become more semantically diverse (e.g., "pick coke can" and "pour cup"), sharing data between tasks becomes harder and thus learning to map ...
- **p. 1 / Abstract - extractive body cue:** To bridge this divide between tasks and actions, our insight is to teach the robot the language of actions, describing lowlevel motions with more fine-grained ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Language is the engine of human reasoning, empowering us to break complex concepts into simpler ones, to correct our misunderstandings, and to generalize concepts in ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** concepts [1], providing language corrections [2, 3], or enabling generalization to new settings [4].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Language is the engine of human reasoning, empowering us to break complex concepts into simpler ones, to correct our misunderstandings, and to ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Recent works in robot imitation learning have proposed learning language-conditioned policies that predict actions given visual observations and the high-level task specified ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Recent, works, robot, imitation, learning, have, language-conditioned, policies, predict, actions | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | works, often, share, common, paradigm, given, high-level, task | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Recent, works, robot, imitation, learning, have, language-conditioned, policies, predict, actions | p. 1 (Abstract), p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: Motivated, benefits, language, motions, end-to-end, framework, RT-H, Robot | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective / loss / cost | policy/action modeling objective; cue terms: advantage, language, settings, encode, shared, structure, between, similar | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (I. INTRODUCTION) |
| Success / guarantee | instruction-conditioned task success | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** concepts [1], providing language corrections [2, 3], or enabling generalization to new settings [4].
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, we show that language motions in RT-H generalize to variations in scene and objects better than RT-2.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (Abstract)): Motivated by the benefits of language motions, we propose an end-to-end framework, RT-H (Robot Transformer with Action Hierarchies), for learning these action hierarchies: at each step, RT-H conditions on the ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** Creating such an action hierarchy leads to several benefits: (1) It enables much better data sharing between different tasks at the level of language motions, ...
- **p. 1 / Abstract - extractive body cue:** Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this along with the high-level ...
- **p. 1 / Abstract - extractive body cue:** This enables a new paradigm for flexible policies that can learn from human intervention in language.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Fig. 1: Given a task in language like "close the pistachio jar" and an image of the scene, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The oatmeal example also highlights how language motion corrections can make the policy's behavior interpretable and thus more ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Since we only care about learning to correct the failure modes of RT-2, we must use RT-2 trained ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | This failure mode rarely happens for in-distribution tasks, but as tasks diverge from the data distribution, it becomes ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (Abstract), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 1 (Abstract), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
