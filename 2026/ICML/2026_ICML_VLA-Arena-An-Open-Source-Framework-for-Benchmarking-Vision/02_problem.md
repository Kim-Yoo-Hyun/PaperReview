# Problem - VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://vla-arena.github.io/; PDF retrieval source: https://arxiv.org/pdf/2512.22539. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction)): This lack of integration prevents understanding how models handle concurrent challenges across visual, linguistic, and structural dimensions of task.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** While Vision-Language-Action models (VLAs) are rapidly advancing toward generalist robot poli1Institute for Artificial Intelligence.
- **p. 1 / Abstract - extractive body cue:** 3Beijing Academy of Artificial Intelligence.
- **p. 1 / Abstract - extractive body cue:** 5State Key Laboratory of General Artificial Intelligence.
- **p. 1 / Abstract - extractive body cue:** To address this, we introduce VLA-Arena, a comprehensive benchmark.
- **p. 1 / Abstract - extractive body cue:** It features a novel structured task design framework to quantify difficulty across three orthogonal axes: (1) Task Structure, (2) Language Command, and (3) Visual Observation.
- **p. 2 / 1. Introduction - extractive body cue:** This lack of integration prevents understanding how models handle concurrent challenges across visual, linguistic, and structural dimensions of task.
- **p. 3 / 1. Introduction - extractive body cue:** Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This lack of integration prevents understanding how models handle concurrent challenges across visual, linguistic, and structural dimensions of task. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models 0.0 0.25 0.5 0.75 1.0 Success Rate StatePreservation L0 OpenVLA OpenVLA-OFT Pi0 UniVLA L1 ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | VLA-Arena, Open-Source, Framework, Benchmarking, Vision-Language-Action, Models, Success, Rate, StatePreservation, OpenVLA | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | features, novel, structured, task, design, framework, quantify, difficulty | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: VLA-Arena, Open-Source, Framework, Benchmarking, Vision-Language-Action, Models, Success, Rate, StatePreservation, OpenVLA | p. 6 (3. Task Suites in VLA-Arena), p. 1 (2 Supported Trajectory), p. 1 (Abstract) |
| Decision / output variable | method trajectory/action; body terms: introduce, VLA-Arena, first, benchmark, structurally, evaluate, performance, safety | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Structured Task Design) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: dimension, evaluates, model, ability, only, complete, primary, objective | p. 5 (3. Task Suites in VLA-Arena), p. 1 (170 Tasks), p. 2 (Abstract), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (2. Structured Task Design) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction) |
| Success / guarantee | comparable score and protocol validity | p. 7 (4.1. Experimental Setup), p. 8 (4.3. Diagnosing Semantic and Visual Grounding), p. 5 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1. Introduction - extractive body cue:** Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key ...
- **p. 2 / 1. Introduction - extractive body cue:** However, existing benchmarks suffer from several limitations.
- **p. 3 / 1. Introduction - extractive body cue:** (Graded difficulty levels, e.g., L0-L2).

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Structured Task Design), p. 3 (2. Structured Task Design), p. 1 (Abstract)): We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs.

- **p. 2 / 1. Introduction - extractive body cue:** To address this challenge, we propose VLA-Arena, a comprehensive and accessible benchmark for evaluating VLA models.
- **p. 3 / 2. Structured Task Design - extractive body cue:** To quantitatively measure the capability frontiers of VLA models, we propose a structured task design, as compared in Table 1.
- **p. 3 / 2. Structured Task Design - extractive body cue:** Based on this classification, we propose the cumulative cost (CC) metric for a trajectory τ of length L: CC(τ) = L-1 X t=0 cinst(st, at) ...
- **p. 1 / Abstract - extractive body cue:** This allows us to systematically design tasks with fine-grained difficulty levels, enabling a precise measurement of model capability frontiers.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 22 | Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | Figure 6. Attention Visualization for the Token "plate" Comparing OpenVLA and OpenVLA-OFT. The instruction is "pick up the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Figure 4. Consistent Failure Modes Observed in Real-World Deployment. When deployed on a physical Franka Research 3 robot, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | By exposing critical failure modes, our research aims to steer the community toward developing robotic agents that are ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (3. Task Suites in VLA-Arena), p. 1 (2 Supported Trajectory), p. 1 (Abstract), p. 3 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), interface p. 6 (3. Task Suites in VLA-Arena), p. 1 (2 Supported Trajectory), p. 1 (Abstract), p. 3 (1. Introduction), objective p. 5 (3. Task Suites in VLA-Arena), p. 1 (170 Tasks), p. 2 (Abstract), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (2. Structured Task Design).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (48 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, existing benchmarks suffer from several limitations. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs. (p. 2, 1. Introduction).
- **Assumption/failure evidence:** While VLAs have progressed rapidly, their capability boundaries, limitations, and failure modes remain poorly understood. (p. 2, 1. Introduction).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
