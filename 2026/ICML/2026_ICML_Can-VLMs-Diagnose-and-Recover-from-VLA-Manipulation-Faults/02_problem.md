# Problem - Can VLMs Diagnose and Recover from VLA Manipulation Faults?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`.
> Analysis basis: official ICML proceedings page (abstract only; public PDF unavailable) checked on 2026-09-02 (1 source page(s); official ICML proceedings page (abstract only; public PDF unavailable); extraction quality: medium); canonical paper source: https://kakigo.github.io/VLA-FixBench/; body source: https://icml.cc/virtual/2026/poster/64203. The note is an evidence-anchored abstract/source-page analysis; exact tables/equations or section details remain at the cited source anchors. Evidence boundary: abstract/source-page only; method details, exact metrics, limitations and failure cases require full-text review. Reading tracker status/evidence was not changed.

## Problem in One Sentence

abstract/source-page framing (p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?)): We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.

## PDF Body Digest

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** While VLMs offer strong explanatory capabilities, their effectiveness in assisting VLAs is limited by their unclear role in diagnostics and inadequate collaboration mechanisms.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** To address this, we introduce VLA-FixBench, a fault evaluation dataset that spans perception, planning, and control failures, and provides annotations for task stages, fault types, ...
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We further propose FaultEval, a static-to-dynamic-to-real evaluation framework that benchmarks 20 VLMs across multiple fault-related dimensions.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Building on these insights, we design a VLM-VLA collaboration mechanism that localizes spatiotemporal deviations and rolls back task execution to enable targeted recovery.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** This suggests that better failure diagnosis and recovery could make future robotic systems safer and more reliable.

## System and Scope

| Dimension | abstract/source-page evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Based on these findings, we design a robot recovery mechanism that can stop execution, roll back to an earlier safe step, and ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from abstract/source-page |
| State / latent | findings, design, robot, recovery, mechanism, stop, execution, roll, back, earlier | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | introduce, VLA-FixBench, dataset, robot, manipulation, failures, covering, problems | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | abstract/source-page-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: findings, design, robot, recovery, mechanism, stop, execution, roll, back, earlier | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Decision / output variable | method trajectory/action; body terms: introduce, VLA-FixBench, dataset, robot, manipulation, failures, covering, problems | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | comparable score and protocol validity | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited abstract/source-page anchors.

## Bottleneck in Prior Work

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** This suggests that better failure diagnosis and recovery could make future robotic systems safer and more reliable.

## What the Paper Changes

abstract/source-page contribution framing (p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?)): We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** To address this, we introduce VLA-FixBench, a fault evaluation dataset that spans perception, planning, and control failures, and provides annotations for task stages, fault types, ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | This suggests that better failure diagnosis and recovery could make future robotic systems safer and more reliable. | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | We also build an evaluation framework to test how well different vision-language models can detect failures, locate when ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), interface p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
