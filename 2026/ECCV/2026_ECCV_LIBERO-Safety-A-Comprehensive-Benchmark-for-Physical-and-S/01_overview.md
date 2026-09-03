# LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (42 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2606.23686.
> PDF retrieval source: https://arxiv.org/pdf/2606.23686. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Vision-Language Model, Benchmark, semantic
- Official paper: https://arxiv.org/abs/2606.23686
- Full-text retrieval: https://arxiv.org/pdf/2606.23686
- Code/Project: https://libero-safety.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (42 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, these benchmarks suffer from two critical limitations.를 문제로 두고, In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior Domain Definition Language (UBDDL) to enable the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Vision-Language-Action models (VLAs) have become a key direction for building general-purpose robotic intelligence [30].
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Recent progress in data scaling, model architectures, and policy optimization has significantly advanced their capabilities, yielding improved task success, stronger generalization, and broader transfer across ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As these systems progress toward realworld deployment, the operational context shifts from controlled laboratory settings to environments involving close human-robot interaction, dynamic obstacles, and unstructured ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** These settings introduce safety-critical requirements that current VLA policies fall short of satisfying in a robust and consistent way.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Reliable deployment demands motion-level reliability and constraint satisfaction during close human-robot interaction.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these benchmarks suffer from two critical limitations.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** First, their exclusive reliance on human teleoperation is prohibitively time-consuming, severely bottlenecking the scalability required to train robust foundation models.

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast, our framework holistically assesses semantic reasoning to refuse malicious instructions, general human-robot interaction (HRI) safety for collaborative co-habitation, and uniquely introduces proximal avoidance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** To systematically evaluate these challenges, we introduce a comprehensive VLA safety benchmark and develop an efficient (b) Data Generation Pipeline to synthesize 19.7K strictly collision-free ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike existing benchmarks, our framework systematically evaluates the physical and semantic safety boundaries of VLA models through parameterized task specifications and multi-dimensional hazard scenarios.
- **p. 5 / 462 Hand-Object Pairs - extractive body cue:** Our benchmark consists of four core components: a parametric environment definition framework (Sec.
- **p. 8 / 462 Hand-Object Pairs - extractive body cue:** Metric Human Teleoperation Ours Human Effort (min/task) 7.4 1.8 Data Scalability 1:1 1:M Collision Guarantee Human-dependent Planner-enforced Spatial Representation World-centric Object-centric Trajectory Consistency High variance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys.
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** 1 Fast, Low-Level Control High-Frequency Data Planner/ Policy Affordance-Aware Grasping Tabletop Spatial Avoidance Human-Robot Interaction Free-Space Hand-Object Avoidance OpenVLA OpenVLA-OFT VLA-JEPA UniVLA GR00T N1.5 GR00T ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys. | standardized observation, action, task state와 evaluation split | p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs) |
| State/latent | Image, Input, Text, Instruction, Multi-modal, VLM, Action, Decoder, Proprioception, Tokens, World, Model | benchmark state/goal와 method decision | p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 6 (462 Hand-Object Pairs) |
| Output/action | 1 Fast, Low-Level Control High-Frequency Data Planner/ Policy Affordance-Aware Grasping Tabletop Spatial Avoidance Human-Robot Interaction Free-Space Hand-Object Avoidance OpenVLA OpenVLA-OFT VLA-JEPA UniVLA GR00T N1.5 GR00T N1.6 Explic ... | policy/controller trajectory 또는 measured result | p. 1 (462 Hand-Object Pairs), p. 6 (462 Hand-Object Pairs), p. 7 (462 Hand-Object Pairs) |
| Objective/outcome | To guarantee kinematic feasibility and strict adherence to safety constraints, all generated motions are subjected to a rigorous human-in-the-loop screening process, ultimately yielding a final dataset of 19,664 high-quality safe demons ... | success metric, robustness, generalization과 reproducibility | p. 8 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast, our framework holistically assesses semantic reasoning to refuse malicious instructions, general human-robot interaction (HRI) safety for collaborative co-habitation, and uniquely introduces proximal avoidance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** To systematically evaluate these challenges, we introduce a comprehensive VLA safety benchmark and develop an efficient (b) Data Generation Pipeline to synthesize 19.7K strictly collision-free ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike existing benchmarks, our framework systematically evaluates the physical and semantic safety boundaries of VLA models through parameterized task specifications and multi-dimensional hazard scenarios.
- **p. 5 / 462 Hand-Object Pairs - extractive body cue:** Our benchmark consists of four core components: a parametric environment definition framework (Sec.
- **p. 11 / 4 Experiment - extractive body cue:** Among the evaluated standard VLAs, π0.5 achieves the highest overall success rate across all suites and difficulty levels.
- **p. 10 / 4 Experiment - extractive body cue:** Notably, the foundational OpenVLA model fails to achieve meaningful success
- **p. 12 / 4 Experiment - extractive body cue:** While RoboBrain2.0 achieves a high RR (80%) at L0, its performance drops precipitously on more complex and deceptive prompts (L1 and L2).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 11 (4 Experiment), p. 10 (4 Experiment) |
| Embodiment/environment | In our benchmark, the barrier function is defined by a distance-based safety margin: \la b el {e q:d i stance_barrier} h(z_t)= d(z_t,\mathcal {O}_t)-d_{\mathrm {safe}}, (A.4) where d(zt, Ot) denotes the minimum distance ... | hardware/simulator version and reset protocol | p. 40 (C.3 Additional Experimental Results), p. 14 (4 Experiment) |
| Dataset/benchmark | To ensure unbiased representation learning across tasks, dataset and trajectory weight balancing are explicitly enabled. | role, split, size and leakage | p. 40 (C.3 Additional Experimental Results), p. 14 (4 Experiment), p. 37 (C.2 Training Configurations), p. 41 (C.3 Additional Experimental Results) |
| Metric | Metrics are reported as mean Success Rate (SR, %), with standard deviations computed across three training seeds shown in parentheses. | definition, denominator, direction and uncertainty | p. 11 (4 Experiment), p. 10 (4 Experiment), p. 38 (C.3 Additional Experimental Results) |
| Baseline/ablation | Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the SR remains relatively stable, fluctuating between 56.3% ... | fair input/data/compute/action matching | p. 13 (4 Experiment), p. 10 (4 Experiment), p. 9 (4 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 39 / C.3 Additional Experimental Results - extractive body cue:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures.
- **p. 10 / 4 Experiment - extractive body cue:** To further assess execution quality, we employ 3 supplementary metrics: Collision Rate (CR) isolates collision-induced terminations from standard task failures, Execution Time evaluates operational efficiency ...
- **p. 42 / C.3 Additional Experimental Results - extractive body cue:** These dynamic guardrails will allow the control policy to trigger verified safe fallback maneuvers prior to any catastrophic physical failure.
- **p. 41 / C.3 Additional Experimental Results - extractive body cue:** E Limitations and Future Work While the proposed evaluation framework establishes a rigorous safety benchmark for visual language action models, several limitations regarding simulation fidelity ...
- **p. 14 / 5 Conclusion - extractive body cue:** Meanwhile, LIBEROSafety remains a simulation-based benchmark; it cannot fully capture realworld contact dynamics, hardware latency, or unpredictable human behavior.
- **p. 14 / 5 Conclusion - extractive body cue:** We introduce a UBDDL-powered parametric framework that procedurally generates diverse safety-critical scenes, together with a keypose-driven data generation pipeline that alleviates the scalability constraints of ...
- **p. 10 / 4 Experiment - extractive body cue:** Any safety constraint violation (detailed in Appendix A) immediately terminates the episode and is recorded as a failure.

## Why Read It

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, these benchmarks suffer from two critical limitations.를 문제로 두고, In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior Domain Definition Language (UBDDL) to enable the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 8 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (42 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, these benchmarks suffer from two critical limitations. (p. 2, 1 INTRODUCTION).
- **Actual contribution:** In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior Domain Definition Language (UBDDL) to ... (p. 3, 1 INTRODUCTION).
- **Evaluation boundary:** Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the SR remains relatively stable, fluctuating ... (p. 13, 4 Experiment).
- **Explicit failure boundary:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures. (p. 39, C.3 Additional Experimental Results).
