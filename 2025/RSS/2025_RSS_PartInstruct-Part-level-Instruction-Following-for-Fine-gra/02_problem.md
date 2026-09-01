# Problem - PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p148.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p148.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract)): Kine-grained robot manipulation, such as lifting and rotating a bottle to display the label on the cap, requires robust reasoning about object parts and their relationships with intended tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Kine-grained robot manipulation, such as lifting and rotating a bottle to display the label on the cap, requires robust reasoning about object parts and their ...
- **p. 1 / Abstract - extractive body cue:** Despite recent advances in training general-purpose robot manipulation policies guided by language instructions, there is a notable lack of large-scale datasets for fine-grained ‘manipulation tasks ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Partinstruct, the first large-scale benchmark for both
- **p. 1 / Abstract - extractive body cue:** robot manipulation models using part-level instructions.
- **p. 1 / Abstract - extractive body cue:** ‘expert demonstrations synthesized in a 3D simulator, where each demonstration is paired with a high-level task instruction, a in of base part-based skill instructions, and ...
- **p. 7 / B. Bi-level Planning - extractive body cue:** Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.
- **p. 4 / A. Problem Setup - extractive body cue:** ‘To develop an embodied agent capable of executing tasks defined by g, we hypothesize that it would be beneficial to star, With a set of ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Kine-grained robot manipulation, such as lifting and rotating a bottle to display the label on the cap, requires robust reasoning about object ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | for the low-level action policy based on the task instruction and the current observation. | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | low-level, action, policy, task, instruction, current, observation, Diffuser, Actor, D-DA | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | skill, instruction, low-level, action, policy, then, generates, actions | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: low-level, action, policy, task, instruction, current, observation, Diffuser, Actor, D-DA | p. 7 (1 Actions .ow-Level Action), p. 6 (A. End-to-End Policy Learning), p. 7 (1 Actions .ow-Level Action) |
| Decision / output variable | method trajectory/action; body terms: Specifically, bi-level, planner, consists, modules, high-level, task, low-level | p. 7 (B. Bi-level Planning), p. 4 (A. Problem Setup), p. 6 (A. End-to-End Policy Learning) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: updates, skill, instruction, once, every, steps, while, low-level | p. 7 (1 Actions .ow-Level Action), p. 7 (B. Bi-level Planning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (1 Actions .ow-Level Action), p. 7 (B. Bi-level Planning) |
| Success / guarantee | comparable score and protocol validity | p. 7 (Figure/Table caption), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** Despite recent advances in training general-purpose robot manipulation policies guided by language instructions, there is a notable lack of large-scale datasets for fine-grained ‘manipulation tasks ...

## What the Paper Changes

PDF contribution framing (p. 7 (B. Bi-level Planning), p. 4 (A. Problem Setup), p. 6 (A. End-to-End Policy Learning)): Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.

- **p. 4 / A. Problem Setup - extractive body cue:** ‘To develop an embodied agent capable of executing tasks defined by g, we hypothesize that it would be beneficial to star, With a set of ...
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** Diffusion Policy (DP) [5] represents a visuomotor policy as a conditional denoising diffusion process in the action space, which allows it to effectively handle multimodal ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | While they can follow simple part-based instructions such as "grasp" or "touch? instructions Tike "touch the left part" ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | However, VLM-based planners can still fail during task planning, particularly in tasks that require a long chain of, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 7 (1 Actions .ow-Level Action), p. 6 (A. End-to-End Policy Learning), p. 7 (1 Actions .ow-Level Action), p. 8 (B. Bi-level Planning). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), interface p. 7 (1 Actions .ow-Level Action), p. 6 (A. End-to-End Policy Learning), p. 7 (1 Actions .ow-Level Action), p. 8 (B. Bi-level Planning), objective p. 7 (1 Actions .ow-Level Action), p. 7 (B. Bi-level Planning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
