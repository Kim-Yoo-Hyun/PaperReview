# Evaluation - VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://vla-arena.github.io/; PDF retrieval source: https://arxiv.org/pdf/2512.22539. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Analysis of Performance and Failure Modes), p. 7 (4.1. Experimental Setup), p. 8 (4.3. Diagnosing Semantic and Visual Grounding), p. 5 (Figure/Table caption), p. 47 (Figure/Table caption), p. 8 (4.4. Disentangling Memorization from Generalization)): Second, without explicit safety constraints, models prioritize task completion, often incurring high CC to achieve success.

## Evaluation Body Digest

- **p. 7 / 4.1. Experimental Setup - extractive body cue:** To facilitate reproducible fine-tuning, we introduce curated datasets derived from human demonstrations.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Datasets are organized by level (i.e., L0 or L1) and size (i.e., Small, Medium, and Large, containing 10, 30, and 50 trajectories per task, respectively).
- **p. 8 / 4.5. Ablation Study - extractive body cue:** VLA-Arena inherits the simulation backbone of robosuite (Zhu et al., 2020) and LIBERO (Liu et al., 2023) but addresses their limitations (Zhou et al., 2025b; ...
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Evaluated on a physical Franka Research 3 robot.
- **p. 6 / 4. Experiments - extractive body cue:** (§ 4.3); (III) Does the structured task design (i.e., L0-L2) provide a richer perspective on model performance?
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** UniVLA (Bu et al., 2025) predicts task-centric latent tokens, moving away from low-level control signals. π0-FAST (Pertsch et al., 2025) advances action tokenization with the ...
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** To provide a comprehensive assessment, we employ success rate (SR) and cumulative cost (CC) as metrics.
- **p. 8 / 4.3. Diagnosing Semantic and Visual Grounding - extractive body cue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models VLA-Arena (Ours) LIBERO Benchmark 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate -52% -28% -64% -28% w/ ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Analysis of Performance and Failure Modes | BENCHMARK / DATASET | Second, without explicit safety constraints, models prioritize task completion, often incurring high CC to achieve success. | p. 7 (4.2. Analysis of Performance and Failure Modes) |
| 4.1. Experimental Setup | BENCHMARK / DATASET | To provide a comprehensive assessment, we employ success rate (SR) and cumulative cost (CC) as metrics. | p. 7 (4.1. Experimental Setup) |
| 4.3. Diagnosing Semantic and Visual Grounding | BENCHMARK / DATASET | VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models VLA-Arena (Ours) LIBERO Benchmark 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate -52% -28% -64% -28% ... | p. 8 (4.3. Diagnosing Semantic and Visual Grounding) |
| Figure/Table caption | BENCHMARK / DATASET | Table 2. Performance Evaluation of Models on the VLA-Arena Benchmark. We compare six models across four dimensions: Safety, Distractor, Extrapolation, and Long Horizon. Performance ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 32. Detailed Variance Results. We report the variance of Success Rate (SR) and Cumulative Cost (CC) across 3 evaluation seeds for all tasks. ... | p. 47 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4.1. Experimental Setup - extractive body cue:** To facilitate reproducible fine-tuning, we introduce curated datasets derived from human demonstrations.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Datasets are organized by level (i.e., L0 or L1) and size (i.e., Small, Medium, and Large, containing 10, 30, and 50 trajectories per task, respectively).
- **p. 8 / 4.5. Ablation Study - extractive body cue:** VLA-Arena inherits the simulation backbone of robosuite (Zhu et al., 2020) and LIBERO (Liu et al., 2023) but addresses their limitations (Zhou et al., 2025b; ...
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Evaluated on a physical Franka Research 3 robot.
- **p. 6 / 4. Experiments - extractive body cue:** (§ 4.3); (III) Does the structured task design (i.e., L0-L2) provide a richer perspective on model performance?
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** UniVLA (Bu et al., 2025) predicts task-centric latent tokens, moving away from low-level control signals. π0-FAST (Pertsch et al., 2025) advances action tokenization with the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview of VLA-Arena Benchmark and Framework. (a) Structured Task Design: Span four key dimensions: Safety, Distractor, Extrapolation, and Long Horizon, covering 11 task ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Comprehensive Comparison with Existing Robotics Benchmarks. Benchmarks are grouped by their underlying Physics Engine. Resources: Data (Fine-grained, filtered datasets), Frmwk (Open framework supporting ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. Each dimension contains suites of tasks designed to isolate a specific challenge, such as Safety or Long Hori- 4
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Performance Evaluation of Models on the VLA-Arena Benchmark. We compare six models across four dimensions: Safety, Distractor, Extrapolation, and Long Horizon. Performance is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2. Performance under Language and Visual Perturbations across Contrasting Task Types. Upper: StatePreservation involves visually unique targets, requiring no joint reasoning. Lower: UnseenObjects necessitates ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Visual Grounding Gap between VLM and VLAs. Level Qwen3-VL-8B VLAs (Avg.) Grounding Accuracy Perf. Drop Perf. Drop V0
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Disentangled Performance Leaderboard. ①, ②, and ③denote 1st, 2nd, and 3rd place, respectively.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Impact of Language on VLA-Arena and LIBERO. ting: fine-tuning causes the model to abandon generalizable concepts, overfitting specific pixel distributions rather than retaining ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To facilitate reproducible fine-tuning, we introduce curated datasets derived from human demonstrations. | embodiment, simulator version and control stack | p. 7 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup) |
| Task/environment | Datasets are organized by level (i.e., L0 or L1) and size (i.e., Small, Medium, and Large, containing 10, 30, and 50 trajectories per task, ... | reset, timeout, object/scene variation | p. 7 (4.1. Experimental Setup), p. 8 (4.5. Ablation Study) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 6 (3. Task Suites in VLA-Arena), p. 1 (2 Supported Trajectory) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (Abstract), p. 3 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To provide a comprehensive assessment, we employ success rate (SR) and cumulative cost (CC) as metrics. | definition/direction/unit from same section | p. 7 (4.1. Experimental Setup) |
| VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models VLA-Arena (Ours) LIBERO Benchmark 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate -52% -28% -64% -28% ... | definition/direction/unit from same section | p. 8 (4.3. Diagnosing Semantic and Visual Grounding) |
| Table 2. Performance Evaluation of Models on the VLA-Arena Benchmark. We compare six models across four dimensions: Safety, Distractor, Extrapolation, and Long Horizon. Performance ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 32. Detailed Variance Results. We report the variance of Success Rate (SR) and Cumulative Cost (CC) across 3 evaluation seeds for all tasks. ... | definition/direction/unit from same section | p. 47 (Figure/Table caption) |
| Table 1. Comprehensive Comparison with Existing Robotics Benchmarks. Benchmarks are grouped by their underlying Physics Engine. Resources: Data (Fine-grained, filtered datasets), Frmwk (Open framework ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Moreover, the trade-off between SmolVLA's conservative safety and OpenVLA's high-cost success underscores safety as an independent axis that poses unique challenges to VLAs. | definition/direction/unit from same section | p. 8 (4.4. Disentangling Memorization from Generalization) |
| Level Qwen3-VL-8B VLAs (Avg.) Grounding Accuracy Perf. | definition/direction/unit from same section | p. 7 (4.1. Experimental Setup) |
| Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In Table 2, a crossmodel comparison indicates that π0 generally outperforms the other models. | comparison identity and matched condition | p. 7 (4.2. Analysis of Performance and Failure Modes) |
| We evaluate our method against a diverse set of baseline VLAs. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| In this section, we aim to answer the following questions: (I) Can we effectively expose failure modes in state-of-the-art VLAs? | comparison identity and matched condition | p. 6 (4. Experiments) |
| In contrast, VLA-Arena suffers a 52-64% collapse from a 79% baseline. | comparison identity and matched condition | p. 8 (4.5. Ablation Study) |
| Figure 6. Attention Visualization for the Token "plate" Comparing OpenVLA and OpenVLA-OFT. The instruction is "pick up the bowl and place it on the ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Second, without explicit safety constraints, models prioritize task completion, often incurring high CC to achieve success. | comparison identity and matched condition | p. 7 (4.2. Analysis of Performance and Failure Modes) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 30. OpenVLA-OFT Fine-tuning Hyperparameters. H.3.5. OPENVLA-OFT TRAINING PARAMETERS The OpenVLA-OFT model was fine-tuned using LoRA. The training utilized 7 devices, resulting in a ... | component/input/data sensitivity | p. 43 (Figure/Table caption) |
| Table 29. π0 Fine-tuning Hyperparameters. The π0 model was fine-tuned for 60k steps, which utilizes LoRA for memory efficiency. The backbone variants were specified ... | component/input/data sensitivity | p. 42 (Figure/Table caption) |
| Unexpectedly, they show less sensitivity to Table 4. | component/input/data sensitivity | p. 7 (4.2. Analysis of Performance and Failure Modes) |
| Notably, π0 and OpenVLA-OFT maintain partial functionality on V4, suggesting dual-input views aid invariant grounding. | component/input/data sensitivity | p. 7 (4.3. Diagnosing Semantic and Visual Grounding) |
| Table 27. UniVLA Fine-tuning Hyperparameters. The training of UniVLA utilized a batch size of 8 per device and employed 2 gradient accumulation steps, resulting ... | component/input/data sensitivity | p. 41 (Figure/Table caption) |
| Table 26. OpenVLA Fine-tuning Hyperparameters. The OpenVLA model was fine-tuned using Low-Rank Adaptation (LoRA). The training was distributed across 8 GPUs, resulting in a ... | component/input/data sensitivity | p. 41 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs. | Second, without explicit safety constraints, models prioritize task completion, often incurring high CC to achieve success. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Analysis of Performance and Failure Modes), p. 7 (4.1. Experimental Setup), p. 8 (4.3. Diagnosing Semantic and Visual Grounding), p. 5 (Figure/Table caption), p. 47 (Figure/Table caption), p. 8 (4.4. Disentangling Memorization from Generalization) |
| Primary metric/result | To provide a comprehensive assessment, we employ success rate (SR) and cumulative cost (CC) as metrics. | numeric claim only at cited anchor | p. 7 (4.1. Experimental Setup) |

- Numeric sentences retained from the body:
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** The results are calculated as the average over 30 evaluation episodes, with 10 episodes per seed.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Datasets are organized by level (i.e., L0 or L1) and size (i.e., Small, Medium, and Large, containing 10, 30, and 50 trajectories per task, respectively).
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Evaluated on a physical Franka Research 3 robot.
- **p. 1 / 170 Tasks - extractive body cue:** (a) Structured Task Design: Span four key dimensions: Safety, Distractor, Extrapolation, and Long Horizon, covering 11 task suites with three difficulty levels (L0-L2), totaling 170 ...
- **p. 1 / Abstract - extractive body cue:** For task structure, VLAArena comprises 11 task suites organized into four dimensions: Safety, Distractor, Extrapolation, and Long Horizon, totaling 170 tasks.
- **p. 2 / 1. Introduction - extractive body cue:** The task structure axis comprises 170 tasks organized into 11 suites, which are grouped by their core challenge into four dimensions (i.e., Safety, Extrapolation, Distractor, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): ... | p. 22 (Figure/Table caption) |
| body limitation/failure cue | Figure 6. Attention Visualization for the Token "plate" Comparing OpenVLA and OpenVLA-OFT. The instruction is "pick up the bowl and place it on the ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Figure 4. Consistent Failure Modes Observed in Real-World Deployment. When deployed on a physical Franka Research 3 robot, the model exhibits the same vulnerabilities ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | By exposing critical failure modes, our research aims to steer the community toward developing robotic agents that are generalizable and safe for real-world deployment. | p. 9 (6. Conclusion) |
| body limitation/failure cue | While models appear robust to language command perturbations, their failure in semantic extrapolation tasks exposes a fundamental deficit in language-driven skill generalization. | p. 8 (4.3. Diagnosing Semantic and Visual Grounding) |
| body limitation/failure cue | Figure 7. Cross-layer Attention Visualization on the "plate" Token and Generalization Analysis across Models. This figure illustrates the 18-layer attention distributions of π0.5, π0, ... | p. 21 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The results are calculated as the average over 30 evaluation episodes, with 10 episodes per seed. | p. 7 (4.1. Experimental Setup) |
| SmolVLA (Shukor et al., 2025) is a lightweight, efficient version deployable on consumer-grade hardware (more model details can be found in Appendix H). | p. 7 (4.1. Experimental Setup) |
| Due to limitations in scale and reproducibility caused by hardware variability and operational overhead, simulation has become an effective tool for architecture and algorithm ... | p. 2 (1. Introduction) |
| This simulates sensor degradation (e.g., electronic noise in lowlight) to assess the integrity of visual concepts against hardware imperfections (Hendrycks & Dietterich, 2019). | p. 4 (2. Structured Task Design) |
| To facilitate cross-model comparison at the same difficulty, the highest SR and CC values are bolded and color-coded by level: blue for L0, orange ... | p. 5 (3. Task Suites in VLA-Arena) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 22 / Figure/Table caption - extractive body cue:** Figure 8. Visualization of Typical Failure Modes in Dynamic Distractors Tasks. The failure cases are categorized into three types: 1) Misplaced grasp (Top row): General ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 6. Attention Visualization for the Token "plate" Comparing OpenVLA and OpenVLA-OFT. The instruction is "pick up the bowl and place it on the plate". ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4. Consistent Failure Modes Observed in Real-World Deployment. When deployed on a physical Franka Research 3 robot, the model exhibits the same vulnerabilities diagnosed ...
- **p. 9 / 6. Conclusion - extractive body cue:** By exposing critical failure modes, our research aims to steer the community toward developing robotic agents that are generalizable and safe for real-world deployment.
- **p. 8 / 4.3. Diagnosing Semantic and Visual Grounding - extractive body cue:** While models appear robust to language command perturbations, their failure in semantic extrapolation tasks exposes a fundamental deficit in language-driven skill generalization.
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 7. Cross-layer Attention Visualization on the "plate" Token and Generalization Analysis across Models. This figure illustrates the 18-layer attention distributions of π0.5, π0, and ...

- **Evidence anchors reviewed:** datasets p. 7 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 6 (4. Experiments), p. 6 (4.1. Experimental Setup), metrics p. 7 (4.1. Experimental Setup), p. 8 (4.3. Diagnosing Semantic and Visual Grounding), p. 5 (Figure/Table caption), p. 47 (Figure/Table caption), p. 3 (Figure/Table caption), p. 8 (4.4. Disentangling Memorization from Generalization), baselines p. 7 (4.2. Analysis of Performance and Failure Modes), p. 6 (4.1. Experimental Setup), p. 6 (4. Experiments), p. 8 (4.5. Ablation Study), p. 20 (Figure/Table caption), p. 7 (4.2. Analysis of Performance and Failure Modes), results p. 7 (4.2. Analysis of Performance and Failure Modes), p. 7 (4.1. Experimental Setup), p. 8 (4.3. Diagnosing Semantic and Visual Grounding), p. 5 (Figure/Table caption), p. 47 (Figure/Table caption), p. 8 (4.4. Disentangling Memorization from Generalization).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (48 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1. Comprehensive Comparison with Existing Robotics Benchmarks. Benchmarks are grouped by their underlying Physics Engine. Resources: Data (Fine-grained, filtered datasets), Frmwk (Open framework supporting custom uploads). Structu ... (p. 3, Figure/Table caption).
- **Metric evidence:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models VLA-Arena (Ours) LIBERO Benchmark 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate -52% -28% -64% -28% w/ Correct Language Instruction w/ Wrong ... (p. 8, 4.3. Diagnosing Semantic and Visual Grounding).
- **Baseline/ablation evidence:** In Table 2, a crossmodel comparison indicates that π0 generally outperforms the other models. (p. 7, 4.2. Analysis of Performance and Failure Modes).
- **Failure/negative evidence:** While VLAs have progressed rapidly, their capability boundaries, limitations, and failure modes remain poorly understood. (p. 2, 1. Introduction).
