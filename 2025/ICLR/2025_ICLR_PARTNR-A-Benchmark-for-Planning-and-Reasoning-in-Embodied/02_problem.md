# Problem - PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=T5QLRRHyL1; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114714. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** We present a benchmark for Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR) designed to study human-robot coordination in household activities.
- **p. 1 / ABSTRACT - extractive body cue:** PARTNR tasks exhibit characteristics of everyday tasks, such as spatial, temporal, and heterogeneous agent capability constraints.
- **p. 1 / ABSTRACT - extractive body cue:** We employ a semi-automated task generation pipeline using Large Language Models (LLMs), incorporating simulation-in-the-loop for the grounding and verification.
- **p. 1 / ABSTRACT - extractive body cue:** PARTNR stands as the largest benchmark of its kind, comprising 100,000 natural language tasks, spanning 60 houses and 5,819 unique objects.
- **p. 1 / ABSTRACT - extractive body cue:** We analyze state-of-the-art LLMs on PARTNR tasks, across the axes of planning, perception and skill execution.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Curating such a benchmark of large-scale, natural language tasks with tailored evaluation functions presents significant challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | PARTNR consists of 100,000 natural language instructions paired with tailored evaluation functions, focusing on four task types: (1) constraint-free, where sub-tasks can ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | PARTNR, consists, natural, language, instructions, paired, tailored, evaluation, functions, focusing | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Subsequently, verified, instructions, evaluation, functions, utilized, guide, LLM | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: PARTNR, consists, natural, language, instructions, paired, tailored, evaluation, functions, focusing | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Decision / output variable | method trajectory/action; body terms: bridge, introduce, Planning, Reasoning, Tasks, humaN-Robot, collaboration, PARTNR | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | comparable score and protocol validity | p. 35 (Figure/Table caption), p. 9 (Figure/Table caption), p. 37 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Curating such a benchmark of large-scale, natural language tasks with tailored evaluation functions presents significant challenges.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Despite significant progress in the field of embodied AI, there remains a gap in realistic benchmarks that evaluate robots in collaborative settings.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** LLMs also struggle to recover from skill failures and perception grounding errors, resulting in lower performance when privileged skills and privileged perception are removed.

## What the Paper Changes

PDF body contribution framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents to collaborate with humans across ...

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a semi-automated approach using 1
- **p. 2 / 1 INTRODUCTION - extractive body cue:** LLM-based helper agents LLM Planner We propose modular LLM-based agent baselines to collaborate in our benchmark.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As PARTNR consists of natural language tasks and LLMs have shown strong results in planning (Yao et al., 2023; Ahn et al., 2022; Huang et ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 24 | Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models. | reported limitation/failure wording; scope must be verified |
| body cue at p. 38 | Figure 14: HITL Interface. Participants control human and robot agents using keyboard/mouse controls to complete the PARTNR tasks. ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
