# VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://vla-arena.github.io/.
> PDF retrieval source: https://arxiv.org/pdf/2512.22539. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, Benchmark, safety, distractor, extrapolation, long-horizon
- Official paper: https://vla-arena.github.io/
- Full-text retrieval: https://arxiv.org/pdf/2512.22539
- Code/Project: https://vla-arena.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 This lack of integration prevents understanding how models handle concurrent challenges across visual, linguistic, and structural dimensions of task.를 문제로 두고, We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While Vision-Language-Action models (VLAs) are rapidly advancing toward generalist robot poli1Institute for Artificial Intelligence.
- **p. 1 / Abstract - extractive body cue:** 3Beijing Academy of Artificial Intelligence.
- **p. 1 / Abstract - extractive body cue:** 5State Key Laboratory of General Artificial Intelligence.
- **p. 1 / Abstract - extractive body cue:** To address this, we introduce VLA-Arena, a comprehensive benchmark.
- **p. 1 / Abstract - extractive body cue:** It features a novel structured task design framework to quantify difficulty across three orthogonal axes: (1) Task Structure, (2) Language Command, and (3) Visual Observation.
- **p. 2 / 1. Introduction - extractive body cue:** This lack of integration prevents understanding how models handle concurrent challenges across visual, linguistic, and structural dimensions of task.
- **p. 3 / 1. Introduction - extractive body cue:** Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs.
- **p. 2 / 1. Introduction - extractive body cue:** To address this challenge, we propose VLA-Arena, a comprehensive and accessible benchmark for evaluating VLA models.
- **p. 3 / 2. Structured Task Design - extractive body cue:** To quantitatively measure the capability frontiers of VLA models, we propose a structured task design, as compared in Table 1.
- **p. 3 / 2. Structured Task Design - extractive body cue:** Based on this classification, we propose the cumulative cost (CC) metric for a trajectory τ of length L: CC(τ) = L-1 X t=0 cinst(st, at) ...
- **p. 1 / Abstract - extractive body cue:** This allows us to systematically design tasks with fine-grained difficulty levels, enabling a precise measurement of model capability frontiers.
- **p. 3 / 1. Introduction - extractive body cue:** Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key ...
- **p. 6 / 3. Task Suites in VLA-Arena - extractive body cue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models 0.0 0.25 0.5 0.75 1.0 Success Rate StatePreservation L0 OpenVLA OpenVLA-OFT Pi0 UniVLA L1 L2 L0 L1 ...
- **p. 2 / 1. Introduction - extractive body cue:** By stressing models with these structured perturbations, we expose latent fragilities and determine whether models rely on robust grounding or fragile memorization of training patterns.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models 0.0 0.25 0.5 0.75 1.0 Success Rate StatePreservation L0 OpenVLA OpenVLA-OFT Pi0 UniVLA L1 L2 L0 L1 L2 W0 W1 W2 W3 W4 0.0 ... | standardized observation, action, task state와 evaluation split | p. 6 (3. Task Suites in VLA-Arena), p. 1 (2 Supported Trajectory) |
| State/latent | VLA-Arena, Open-Source, Framework, Benchmarking, Vision-Language-Action, Models, Success, Rate, StatePreservation, OpenVLA, OpenVLA-OFT, Pi0 | benchmark state/goal와 method decision | p. 6 (3. Task Suites in VLA-Arena), p. 1 (2 Supported Trajectory), p. 1 (Abstract) |
| Output/action | Collection Methods Smooth Conversion among Data Formats Specify Goal: Lemon on the Bowl (c) Open-source Framework for VLA-Arena Language Command Perturbation Visual Observation Perturbation edible fruit apple eating apple Pick up the ... | policy/controller trajectory 또는 measured result | p. 1 (2 Supported Trajectory), p. 1 (Abstract), p. 3 (1. Introduction) |
| Objective/outcome | This dimension evaluates the model's ability to not only complete its primary objective but to do so while adhering to safety constraints, a critical requirement for real-world deployment. | success metric, robustness, generalization과 reproducibility | p. 5 (3. Task Suites in VLA-Arena), p. 1 (170 Tasks), p. 2 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs.
- **p. 2 / 1. Introduction - extractive body cue:** To address this challenge, we propose VLA-Arena, a comprehensive and accessible benchmark for evaluating VLA models.
- **p. 3 / 2. Structured Task Design - extractive body cue:** To quantitatively measure the capability frontiers of VLA models, we propose a structured task design, as compared in Table 1.
- **p. 3 / 2. Structured Task Design - extractive body cue:** Based on this classification, we propose the cumulative cost (CC) metric for a trajectory τ of length L: CC(τ) = L-1 X t=0 cinst(st, at) ...
- **p. 1 / Abstract - extractive body cue:** This allows us to systematically design tasks with fine-grained difficulty levels, enabling a precise measurement of model capability frontiers.
- **p. 7 / 4.2. Analysis of Performance and Failure Modes - extractive body cue:** Second, without explicit safety constraints, models prioritize task completion, often incurring high CC to achieve success.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** To provide a comprehensive assessment, we employ success rate (SR) and cumulative cost (CC) as metrics.
- **p. 8 / 4.3. Diagnosing Semantic and Visual Grounding - extractive body cue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models VLA-Arena (Ours) LIBERO Benchmark 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate -52% -28% -64% -28% w/ ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (4.2. Analysis of Performance and Failure Modes), p. 7 (4.1. Experimental Setup) |
| Embodiment/environment | To facilitate reproducible fine-tuning, we introduce curated datasets derived from human demonstrations. | hardware/simulator version and reset protocol | p. 7 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup) |
| Dataset/benchmark | VLA-Arena inherits the simulation backbone of robosuite (Zhu et al., 2020) and LIBERO (Liu et al., 2023) but addresses their limitations (Zhou et al., 2025b; Fei et al., 2025; Guo et al., ... | role, split, size and leakage | p. 7 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study) |
| Metric | To provide a comprehensive assessment, we employ success rate (SR) and cumulative cost (CC) as metrics. | definition, denominator, direction and uncertainty | p. 7 (4.1. Experimental Setup), p. 8 (4.3. Diagnosing Semantic and Visual Grounding), p. 5 (Figure/Table caption) |
| Baseline/ablation | In Table 2, a crossmodel comparison indicates that π0 generally outperforms the other models. | fair input/data/compute/action matching | p. 7 (4.2. Analysis of Performance and Failure Modes), p. 6 (4.1. Experimental Setup), p. 6 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 22 / Figure/Table caption - extractive body cue:** Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): General ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 6. Attention Visualization for the Token "plate" Comparing OpenVLA and OpenVLA-OFT. The instruction is "pick up the bowl and place it on the plate". ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4. Consistent Failure Modes Observed in Real-World Deployment. When deployed on a physical Franka Research 3 robot, the model exhibits the same vulnerabilities diagnosed ...
- **p. 9 / 6. Conclusion - extractive body cue:** By exposing critical failure modes, our research aims to steer the community toward developing robotic agents that are generalizable and safe for real-world deployment.
- **p. 8 / 4.3. Diagnosing Semantic and Visual Grounding - extractive body cue:** While models appear robust to language command perturbations, their failure in semantic extrapolation tasks exposes a fundamental deficit in language-driven skill generalization.
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 7. Cross-layer Attention Visualization on the "plate" Token and Generalization Analysis across Models. This figure illustrates the 18-layer attention distributions of π0.5, π0, and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Performance Evaluation of Models on the VLA-Arena Benchmark. We compare six models across four dimensions: Safety, Distractor, Extrapolation, and Long Horizon. Performance is ...

## Why Read It

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 This lack of integration prevents understanding how models handle concurrent challenges across visual, linguistic, and structural dimensions of task.를 문제로 두고, We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 6 (3. Task Suites in VLA-Arena), p. 2 (1. Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (48 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, existing benchmarks suffer from several limitations. (p. 2, 1. Introduction).
- **Actual contribution:** We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs. (p. 2, 1. Introduction).
- **Evaluation boundary:** Table 1. Comprehensive Comparison with Existing Robotics Benchmarks. Benchmarks are grouped by their underlying Physics Engine. Resources: Data (Fine-grained, filtered datasets), Frmwk (Open framework supporting custom uploads). Structu ... (p. 3, Figure/Table caption).
- **Explicit failure boundary:** While VLAs have progressed rapidly, their capability boundaries, limitations, and failure modes remain poorly understood. (p. 2, 1. Introduction).
