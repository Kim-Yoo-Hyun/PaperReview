# Problem - HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=h7aQxzKbq6; PDF retrieval source: https://openreview.net/pdf/eafdc79dd4a2aa8bac8cced6ed84a72b790f2bcd.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 5 (3 BACKGROUND), p. 8 (3 BACKGROUND), p. 10 (3 BACKGROUND), p. 1 (1 INTRODUCTION)): A line of prior work (Brohan et al., 2023a; Kim et al., 2024; Black et al., 2024) builds open-world vision-language-action models (VLAs) by finetuning off-the-shelf pretrained VLMs to directly produce ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved ...
- **p. 1 / ABSTRACT - extractive PDF cue:** One fundamental challenge is the lack of robotic data, which are typically obtained through expensive on-robot operation.
- **p. 1 / ABSTRACT - extractive PDF cue:** A promising remedy is to leverage cheaper, "off-domain" data such as action-free videos, handdrawn sketches or simulation data.
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we posit that hierarchical visionlanguage-action (VLA) models can be more effective in utilizing off-domain data than standard monolithic VLA models that directly ...
- **p. 1 / ABSTRACT - extractive PDF cue:** In particular, we study a class of hierarchical VLA models, where the high-level VLM is finetuned to produce a coarse 2D path indicating the desired ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** A line of prior work (Brohan et al., 2023a; Kim et al., 2024; Black et al., 2024) builds open-world vision-language-action models (VLAs) by finetuning off-the-shelf ...
- **p. 5 / 3 BACKGROUND - extractive PDF cue:** The primary advantages of finetuning such a hierarchical VLM that produces intermediate representations as opposed to directly producing actions a with a monolithic model (Kim ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | A line of prior work (Brohan et al., 2023a; Kim et al., 2024; Black et al., 2024) builds open-world vision-language-action models (VLAs) ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | (a) VLM Path Prediction Policy Input Instruction: "Put the object in the bowl." z = Depth/3D Observation VLM response: [(0.25, 0.1, 0), ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | VLM, Path, Prediction, Policy, Input, Instruction, Put, object, bowl, Depth/3D | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | VLA, models, refer, monolithic, rely, crucially, large, robotics | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: VLM, Path, Prediction, Policy, Input, Instruction, Put, object, bowl, Depth/3D | p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND), p. 1 (1 INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: important, note, while, certainly, first, hierarchical, VLA, models | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 BACKGROUND) |
| Objective / loss / cost | policy/action modeling objective; cue terms: simulated, experiments, Colosseum, changes, needed, fact, performance, drop | p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B.1 VLM IMPLEMENTATION DETAILS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B.1 VLM IMPLEMENTATION DETAILS) |
| Success / guarantee | instruction-conditioned task success | p. 9 (Figure/Table caption), p. 29 (Figure/Table caption), p. 9 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 5 / 3 BACKGROUND - extractive PDF cue:** The primary advantages of finetuning such a hierarchical VLM that produces intermediate representations as opposed to directly producing actions a with a monolithic model (Kim ...
- **p. 8 / 3 BACKGROUND - extractive PDF cue:** pick up the green pepper and put it in the red bowl pick up the banana and put it in the black bowl push down ...
- **p. 10 / 3 BACKGROUND - extractive PDF cue:** 5.3.1 MULTIMODAL VQA BENCHMARK PERFORMANCE 6 CONCLUSION AND LIMITATIONS In summary, we study hierarchical VLA models that achieve robust generalization in robotic manipulation.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Developing general robot manipulation policies has been notoriously difficult.

## What the Paper Changes

PDF contribution framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 BACKGROUND), p. 6 (3 BACKGROUND), p. 6 (3 BACKGROUND)): It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et al., 2024a), we propose the novel ...

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To this end, we propose a hierarchical architecture for VLAs, HAMSTER (Hierarchical Action Models with SeparaTEd Path Representations), where large fine-tuned VLMs are connected to ...
- **p. 5 / 3 BACKGROUND - extractive PDF cue:** It consists of two interconnected models: first, a higher-level VLM that is finetuned on large-scale, off-domain data to produce intermediate 2D path guidance (detailed in ...
- **p. 6 / 3 BACKGROUND - extractive PDF cue:** A sample consists of a prompt z like Locate object between the marked items, an input image img and answer ans like [(0.25, 0.11), (0.22, ...
- **p. 6 / 3 BACKGROUND - extractive PDF cue:** This dataset consists of data automatically generated in simulation and collected from existing real-world datasets; its diverse tasks enable the HAMSTER VLM to reason about ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E for failure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | 5.3.1 MULTIMODAL VQA BENCHMARK PERFORMANCE 6 CONCLUSION AND LIMITATIONS In summary, we study hierarchical VLA models that achieve ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 28 | Figure 15: Performance Distribution of RVT2+Sketch and 3DDA+Sketch This section outlines the failure modes observed during our experiments ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 1: Overview of HAMSTER, VLAs and "smaller" imitation learning methods. HAMSTER's hierarchi- cal design results in better ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 7 (3 BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 5 (3 BACKGROUND), p. 8 (3 BACKGROUND), p. 10 (3 BACKGROUND), p. 1 (1 INTRODUCTION), interface p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 7 (3 BACKGROUND), objective p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B.1 VLM IMPLEMENTATION DETAILS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
