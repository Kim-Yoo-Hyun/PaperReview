# Problem - Code as Policies: Language Model Programs for Embodied Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.07753; PDF retrieval source: https://arxiv.org/pdf/2209.07753. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): While promising, this abstraction prevents the LLMs from directly influencing the perception-action feedback loop, making it difficult to ground language in ways that (i) generalize modes of feedback that share ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Large language models (LLMs) trained on codecompletion have been shown to be capable of synthesizing simple Python programs from docstrings [1].
- **p. 1 / Abstract - extractive PDF cue:** We find that these code-writing LLMs can be re-purposed to write robot policy code, given natural language commands.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, policy code can express functions or feedback loops that process perception outputs (e.g., from object detectors [2], [3]) and parameterize control primitive APIs.
- **p. 1 / Abstract - extractive PDF cue:** When provided as input several example language commands (formatted as comments) followed by corresponding policy code (via few-shot prompting), LLMs can take in new commands ...
- **p. 1 / Abstract - extractive PDF cue:** By chaining classic logic structures and referencing third-party libraries (e.g., NumPy, Shapely) to perform arithmetic, LLMs used in this way can write robot policies that ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** While promising, this abstraction prevents the LLMs from directly influencing the perception-action feedback loop, making it difficult to ground language in ways that (i) generalize ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Code as policies presents a new approach to linking words, percepts, and actions; enabling applications in human-robot interaction, but is not without limitations.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While promising, this abstraction prevents the LLMs from directly influencing the perception-action feedback loop, making it difficult to ground language in ways ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | When provided with several example language commands followed by corresponding policy code (via few-shot prompting, in gray), LLMs can take in new ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | When, provided, several, example, language, commands, followed, corresponding, policy, code | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Policy, code, express, functions, feedback, loops, process, perception | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: When, provided, several, example, language, commands, followed, corresponding, policy, code | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: enables, robots, perform, spatial-geometric, reasoning, parse, object, relationships | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: LMP, expected, return, value, obtain, locals, after, exec | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Code as policies presents a new approach to linking words, percepts, and actions; enabling applications in human-robot interaction, but is not without limitations.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** 1: Given examples (via few-shot prompting), robots can use code-writing large language models (LLMs) to translate natural language commands into robot policy code which process ...

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Our approach enables robots to perform spatial-geometric reasoning, parse object relationships, and form multi-step behaviors using off-the-shelf models and few-shot prompting with no additional training.

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** See full videos and more tasks at code-as-policies.github.io We present Code as Policies (CaP): a robot-centric formulation of language model generated programs (LMPs) executed on ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Our approach also assumes all given instructions are feasible, and we cannot tell if a response will be ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | It also illustrates the ability to follow long-horizon reactive commands with control structures as well as precise spatial ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
