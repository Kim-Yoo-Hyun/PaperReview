# Problem - Can VLMs Diagnose and Recover from VLA Manipulation Faults?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://kakigo.github.io/VLA-FixBench/; PDF retrieval source: https://kakigo.github.io/VLA-FixBench/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, due to current technical limitations, existing VLA models fre

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis.
- **p. 1 / Abstract - extractive body cue:** While VLMs offer strong explanatory capabilities, their effectiveness in assisting VLAs is limited by their unclear role in diagnostics and inadequate collaboration mechanisms.
- **p. 1 / Abstract - extractive body cue:** To address this, we introduce VLA-FixBench, a fault evaluation dataset that spans perception, planning, and control failures, and provides annotations for task stages, fault types, ...
- **p. 1 / Abstract - extractive body cue:** We further propose FaultEval, a static-to-dynamicto-real evaluation framework that benchmarks
- **p. 1 / 1. Introduction - extractive body cue:** With the rapid advancement of embodied intelligence, Vision-Language-Action (VLA) models have demonstrated increasing advantages in scenarios such as industrial assembly, logistics sorting, and household services.
- **p. 1 / 1. Introduction - extractive body cue:** However, due to current technical limitations, existing VLA models fre
- **p. 1 / 1. Introduction - extractive body cue:** As a result, existing methods face key limitations: insufficient focus on VLM-VLA collaboration with no standardized interfaces (Yang et al., 2025b; Chen et al., 2024), ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, due to current technical limitations, existing VLA models fre | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | The bottom axis indicates the trade-off between evaluation convenience and physical accuracy. proaches employ supervised classifiers or temporal models to predict failure ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | bottom, axis, indicates, trade-off, between, evaluation, convenience, physical, accuracy, proaches | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Moreover, current, VLM-VLA, interactions, largely, instruction-based, lack, unified | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: bottom, axis, indicates, trade-off, between, evaluation, convenience, physical, accuracy, proaches | p. 3 (Approach), p. 3 (Approach), p. 1 (1. Introduction) |
| Decision / output variable | method trajectory/action; body terms: address, challenges, introduce, VLA-FixBench, benchmark, VLM-assisted, VLA, fault | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: While, effective, specific, domains, methods, typically, rely, task | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (Approach) |
| Success / guarantee | comparable score and protocol validity | p. 8 (5.2. Static Evaluation Results), p. 16 (Figure/Table caption), p. 4 (4.2. Dynamic Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** As a result, existing methods face key limitations: insufficient focus on VLM-VLA collaboration with no standardized interfaces (Yang et al., 2025b; Chen et al., 2024), ...
- **p. 2 / 1. Introduction - extractive body cue:** Spatial Deviation Understanding Task: Unplug the connector and insert it into the black socket.
- **p. 2 / 1. Introduction - extractive body cue:** Overview of VLA-FixBench, Center: Hierarchical failure types in Perception, Planning, and Control.

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Construction of VLA-FixBench)): To address these challenges, we introduce VLA-FixBench, a benchmark for VLM-assisted VLA fault diagnosis and recovery, with over 6,000 annotated failure cases across perception, planning, and control.

- **p. 1 / 1. Introduction - extractive body cue:** Based on VLA-FixBench, we propose FaultEval, a unified static-to-dynamic-to-real evaluation framework that assesses VLM performance in fault identification, severity estimation, temporal localization, spatial correction, and ...
- **p. 2 / 1. Introduction - extractive body cue:** We further construct a VLM-VLA collaboration mechanism that enables fault detection, rollback, and action repair during VLA execution.
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • VLA-FixBench, a robotic manipulation fault evaluation dataset comprising 6k failure cases covering perception, control, and cognition errors, ...
- **p. 4 / 3. Construction of VLA-FixBench - extractive body cue:** Multi-dimensional Annotation We develop a fine-grained annotation framework to construct a high-resolution failure map across three integrated dimensions: temporal, spatial, and semantic.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | The real-robot setup is therefore a sparse diagnostic-and-recovery loop that trades limited inspection latency for recovery from failures ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | We introduce a unified benchmark and evaluation framework that systematically characterizes failure types, severity, and spatiotemporal repair behaviors, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | To bridge low-level signals and task execution, some works analyze failures in specific manipulation tasks. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | As a result, existing failure analyses remain fragmented and lack a unified framework for systematic evaluation across tasks ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (Approach), p. 3 (Approach), p. 1 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (Approach), p. 3 (Approach), p. 1 (1. Introduction), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, due to current technical limitations, existing VLA models fre (p. 1, 1. Introduction).
- **Formulation-changing contribution:** Our main contributions are summarized as follows: • VLA-FixBench, a robotic manipulation fault evaluation dataset comprising 6k failure cases covering perception, control, and cognition errors, with fine-grained annotations of sub-task ... (p. 2, 1. Introduction).
- **Assumption/failure evidence:** GPT-5-2 achieves the highest sensitivity (Recall: 0.8571, F2-Score: 0.7143), but its high FPR (0.7568) causes task failure (SR: 0), indicating that oversensitive diagnosis can disrupt nominal executions. (p. 8, 5.4. Real-Time Evaluation Results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
