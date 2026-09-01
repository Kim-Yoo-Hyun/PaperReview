# Problem - PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (63 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=T5QLRRHyL1; PDF retrieval source: https://openreview.net/pdf/4bb6ff694eaca45e88773722cf73178602665bfd.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** Imagine a domestic robot that collaborates with humans in daily activities using natural language, akin to human-to-human interactions.
- **p. 1 / 1 Introduction - extractive PDF cue:** This scenario requires two key features: the dynamic collaboration between the robot and the human, and the use of natural language for interaction.
- **p. 1 / 1 Introduction - extractive PDF cue:** Current benchmarks in embodied AI typically satisfy one or the other condition; either robots operate in isolation (Shridhar et al., 2020; Zhu et al., 2023; ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Despite significant progress in the field of embodied AI, there remains a gap in realistic benchmarks that evaluate robots in collaborative settings.
- **p. 1 / 1 Introduction - extractive PDF cue:** To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions.
- **p. 1 / 1 Introduction - extractive PDF cue:** Curating such a benchmark of large-scale, natural language tasks with tailored evaluation functions presents significant challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | PARTNR consists of 100,000 natural language instructions paired with tailored evaluation functions, focusing on four task types: (1) constraint-free, where sub-tasks can ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | PARTNR, consists, natural, language, instructions, paired, tailored, evaluation, functions, focusing | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | capture, extraneous, agent, effort, measure, portion, actions, increase | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: PARTNR, consists, natural, language, instructions, paired, tailored, evaluation, functions, focusing | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 10 (Method) |
| Decision / output variable | method trajectory/action; body terms: bridge, introduce, Planning, Reasoning, Tasks, humaN-Robot, collaboration, PARTNR | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: highlights, limitations, LLMs, reasoning, about, agent, capabilities, following | p. 10 (Method), p. 10 (Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 10 (Method), p. 10 (Method) |
| Success / guarantee | comparable score and protocol validity | p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** Curating such a benchmark of large-scale, natural language tasks with tailored evaluation functions presents significant challenges.
- **p. 1 / 1 Introduction - extractive PDF cue:** Despite significant progress in the field of embodied AI, there remains a gap in realistic benchmarks that evaluate robots in collaborative settings.
- **p. 2 / 1 Introduction - extractive PDF cue:** LLMs also struggle to recover from skill failures and perception grounding errors, resulting in lower performance when privileged skills and privileged perception are removed.

## What the Paper Changes

PDF contribution framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 10 (Method)): To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents to collaborate with humans across ...

- **p. 1 / 1 Introduction - extractive PDF cue:** PARTNR consists of 100,000 natural language instructions paired with tailored evaluation functions, focusing on four task types: (1) constraint-free, where sub-tasks can be completed in ...
- **p. 2 / 1 Introduction - extractive PDF cue:** LLM-based helper agents LLM Planner We propose modular LLM-based agent baselines to collaborate in our benchmark.
- **p. 2 / 1 Introduction - extractive PDF cue:** To overcome this, we propose a semi-automated generation method using Large Language Models (LLMs) with simulation-in-the-loop grounding.
- **p. 10 / Method - extractive PDF cue:** This allows us to run at-scale evaluation of our tasks with 129 non-expert human participants.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 11 | PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1 Introduction), p. 1 (1 Introduction), p. 10 (Method), p. 11 (Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), interface p. 1 (1 Introduction), p. 1 (1 Introduction), p. 10 (Method), p. 11 (Method), objective p. 10 (Method), p. 10 (Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
