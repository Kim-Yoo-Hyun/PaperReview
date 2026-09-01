# Problem - LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.23686; PDF retrieval source: https://arxiv.org/pdf/2606.23686. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): However, these benchmarks suffer from two critical limitations.

## PDF Body Digest

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Vision-Language-Action models (VLAs) have become a key direction for building general-purpose robotic intelligence [30].
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Recent progress in data scaling, model architectures, and policy optimization has significantly advanced their capabilities, yielding improved task success, stronger generalization, and broader transfer across ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** As these systems progress toward realworld deployment, the operational context shifts from controlled laboratory settings to environments involving close human-robot interaction, dynamic obstacles, and unstructured ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** These settings introduce safety-critical requirements that current VLA policies fall short of satisfying in a robust and consistent way.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Reliable deployment demands motion-level reliability and constraint satisfaction during close human-robot interaction.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, these benchmarks suffer from two critical limitations.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** First, their exclusive reliance on human teleoperation is prohibitively time-consuming, severely bottlenecking the scalability required to train robust foundation models.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these benchmarks suffer from two critical limitations. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | Image, Input, Text, Instruction, Multi-modal, VLM, Action, Decoder, Proprioception, Tokens | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | While, standard, BDDL, focuses, primarily, deterministic, symbolic, states | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Image, Input, Text, Instruction, Multi-modal, VLM, Action, Decoder, Proprioception, Tokens | p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 6 (462 Hand-Object Pairs) |
| Decision / output variable | method trajectory/action; body terms: summary, establish, evaluation, framework, through, four, core, technical | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (462 Hand-Object Pairs) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: guarantee, kinematic, feasibility, strict, adherence, safety, constraints, generated | p. 1 (462 Hand-Object Pairs), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (462 Hand-Object Pairs) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Success / guarantee | comparable score and protocol validity | p. 11 (4 Experiment), p. 10 (4 Experiment), p. 38 (C.3 Additional Experimental Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** First, their exclusive reliance on human teleoperation is prohibitively time-consuming, severely bottlenecking the scalability required to train robust foundation models.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** This infrastructure drives a fivedimensional curriculum that decouples safety into semantic reasoning and physical constraints. - Keypose-Driven Data Generation Pipeline: To overcome the inefficiency and ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Our results reveal that while high-diversity training fosters safer trajectories, task success remains bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.

## What the Paper Changes

PDF contribution framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (462 Hand-Object Pairs), p. 3 (1 INTRODUCTION), p. 5 (462 Hand-Object Pairs)): In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior Domain Definition Language (UBDDL) to ...

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In contrast, our framework holistically assesses semantic reasoning to refuse malicious instructions, general human-robot interaction (HRI) safety for collaborative co-habitation, and uniquely introduces proximal avoidance ...
- **p. 1 / 462 Hand-Object Pairs - extractive PDF cue:** To systematically evaluate these challenges, we introduce a comprehensive VLA safety benchmark and develop an efficient (b) Data Generation Pipeline to synthesize 19.7K strictly collision-free ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Unlike existing benchmarks, our framework systematically evaluates the physical and semantic safety boundaries of VLA models through parameterized task specifications and multi-dimensional hazard scenarios.
- **p. 5 / 462 Hand-Object Pairs - extractive PDF cue:** Our benchmark consists of four core components: a parametric environment definition framework (Sec.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 39 | This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | To further assess execution quality, we employ 3 supplementary metrics: Collision Rate (CR) isolates collision-induced terminations from standard ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 42 | These dynamic guardrails will allow the control policy to trigger verified safe fallback maneuvers prior to any catastrophic ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 41 | E Limitations and Future Work While the proposed evaluation framework establishes a rigorous safety benchmark for visual language ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 6 (462 Hand-Object Pairs), p. 7 (462 Hand-Object Pairs). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 6 (462 Hand-Object Pairs), p. 7 (462 Hand-Object Pairs), objective p. 1 (462 Hand-Object Pairs), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (462 Hand-Object Pairs).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
