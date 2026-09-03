# Problem - Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=i5wlozMFsQ; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245153. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): This disparity is widely recognized as the "seeing-to-doing gap" (Yuan et al., 2025): a failure to reliably translate rich perceptual understanding into effective robotic actions.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Generalization in embodied AI is hindered by the "seeing-to-doing gap", stemming from data scarcity and embodiment heterogeneity.
- **p. 1 / ABSTRACT - extractive body cue:** To address this, we pioneer "pointing" as a unified, embodiment-agnostic intermediate representation, defining four core embodied pointing abilities that bridge high-level vision-language comprehension with low-level ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce Embodied-R1, a 3B Vision-Language Model (VLM) specifically designed for embodied reasoning and pointing.
- **p. 1 / ABSTRACT - extractive body cue:** We use a wide range of embodied and general visual reasoning datasets as sources to construct a large-scale dataset, Embodied-Points-200K, which supports key embodied pointing ...
- **p. 1 / ABSTRACT - extractive body cue:** Then we train Embodied-R1 using a two-stage Reinforced Fine-tuning (RFT) curriculum with specialized multi-task reward design.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This disparity is widely recognized as the "seeing-to-doing gap" (Yuan et al., 2025): a failure to reliably translate rich perceptual understanding into effective robotic actions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This gap is largely attributed to two key challenges: (a) data scarcity, where limited embodied data prevents from sufficiently grounding language and vision with physical ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This disparity is widely recognized as the "seeing-to-doing gap" (Yuan et al., 2025): a failure to reliably translate rich perceptual understanding into ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | This gap is largely attributed to two key challenges: (a) data scarcity, where limited embodied data prevents from sufficiently grounding language and ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | largely, attributed, challenges, data, scarcity, where, limited, embodied, prevents, sufficiently | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | would, tend, output, only, points, form, straight, line | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: largely, attributed, challenges, data, scarcity, where, limited, embodied, prevents, sufficiently | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| Decision / output variable | action, pose, option or chunk a; body terms: bridge, pointing, intuitive, effective, paradigm, connect, high-level, understanding | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| Objective / loss / cost | policy/action modeling objective; cue terms: practice, found, without, constraint, model, VTG, task, prone | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| Success / guarantee | instruction-conditioned task success | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 24 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** This gap is largely attributed to two key challenges: (a) data scarcity, where limited embodied data prevents from sufficiently grounding language and vision with physical ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** I need to avoid obstacles and carefully move the moka pot from current position to the right side of the drawer. </think> <answer><point>[[450,496],[453,47 8], … ...

## What the Paper Changes

PDF body contribution framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1)): To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Simultaneously, its embodiment-agnostic nature enables knowledge transfer across diverse robot platforms, resolving the heterogeneity challenge.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Second, for the VTG task, we introduced an additional constraint on the format: the generated visual trace must consist of exactly 8 points.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 18 | We would like to add two clarifying points: First, if the task output fails to meet the required ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | A detailed discussion of limitations is provided in App. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | D, we conducted an in-depth analysis of failure cases and execution time. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The score is the accuracy of points falling within the target region. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), objective p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
