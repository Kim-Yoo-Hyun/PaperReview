# Evaluation - Can VLMs Diagnose and Recover from VLA Manipulation Faults?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://kakigo.github.io/VLA-FixBench/; PDF retrieval source: https://kakigo.github.io/VLA-FixBench/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.2. Dynamic Evaluation), p. 9 (5.6. Ablation Study), p. 6 (4.2. Dynamic Evaluation), p. 8 (5.2. Static Evaluation Results), p. 8 (5.2. Static Evaluation Results), p. 9 (5.5. Alignment Between Static and Dynamic Evaluation)): Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, and precise rollback outperforms coarse task restarts, demonstrating ...

## Evaluation Body Digest

- **p. 6 / 4.3. Real-Time Evaluation - extractive body cue:** To evaluate the practical performance of multimodal models in real-world robotic manipulation, we conduct on-robot experiments.
- **p. 9 / 5.4. Real-Time Evaluation Results - extractive body cue:** Thus, our realrobot experiments do not claim that off-the-shelf VLMs solve robotic recovery; rather, they expose the mismatch between current VLM benchmarks and the capabilities ...
- **p. 3 / 2.2. Benchmark and Failure Evaluation of VLM - extractive body cue:** While existing benchmarks like LIBERO (Liu et al., 2023)provide rigorous environments to assess task success rates , they largely overlook the underlying failure behaviors.
- **p. 4 / 4.2. Dynamic Evaluation - extractive body cue:** To assess corrective capabilities of multimodal models in robotic manipulation, we design a dynamic evaluation framework in simulation, focusing on corrective behavior during task execution, ...
- **p. 5 / 4.2. Dynamic Evaluation - extractive body cue:** Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, and precise rollback ...
- **p. 9 / 5.6. Ablation Study - extractive body cue:** Effectiveness of Self-Correction Across all evaluated tasks, human-in-the-loop correction consistently yields substantial performance gains over open-loop execution, improving average success rates by 13% points in ...
- **p. 3 / 2.2. Benchmark and Failure Evaluation of VLM - extractive body cue:** In contrast to prior work, we focus on task-level, interpretable, and recoverable failures in robotic manipulation.
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** The resulting dataset is curated with fine-grained annotations (failure type, subtask, and severity).

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 2.2. Benchmark and Failure Evaluation of VLM (p. 3); 4. FaultEval Evaluation Framework (p. 4); 4.1. Static Evaluation (p. 4); 4.2. Dynamic Evaluation (p. 4); 4.3. Real-Time Evaluation (p. 6); 5. Results (p. 7); 5.1. Experimental Setup (p. 7); 5.2. Static Evaluation Results (p. 7); 5.3. Dynamic Evaluation Results (p. 8); 5.4. Real-Time Evaluation Results (p. 8); 5.5. Alignment Between Static and Dynamic Evaluation (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Dynamic Evaluation | BENCHMARK / DATASET | Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, and precise ... | p. 5 (4.2. Dynamic Evaluation) |
| 5.6. Ablation Study | BENCHMARK / DATASET | Effectiveness of Self-Correction Across all evaluated tasks, human-in-the-loop correction consistently yields substantial performance gains over open-loop execution, improving average success rates by 13% points ... | p. 9 (5.6. Ablation Study) |
| 4.2. Dynamic Evaluation | BENCHMARK / DATASET | Simulation Results on Dynamic Evaluation Metrics: Geometric Correction Accuracy (GCA), Temporal Localization Accuracy (TLA), and Simulation Success Rate (SSR). | p. 6 (4.2. Dynamic Evaluation) |
| 5.2. Static Evaluation Results | BENCHMARK / DATASET | The performance is measured across diagnostic metrics (Recall, Precision, F2-Score, and FPR) and the manipulation Success Rate (SR). | p. 8 (5.2. Static Evaluation Results) |
| 5.2. Static Evaluation Results | BENCHMARK / DATASET | Conversely, open-source models like Qwen2.5/3-VL and InternVL achieve parity in high-level semantic understanding, with Qwen2.5-VL78B outperforming all closed-source models in spatial object errors (SOE: ... | p. 8 (5.2. Static Evaluation Results) |

## Dataset / Benchmark Role

- **p. 6 / 4.3. Real-Time Evaluation - extractive body cue:** To evaluate the practical performance of multimodal models in real-world robotic manipulation, we conduct on-robot experiments.
- **p. 9 / 5.4. Real-Time Evaluation Results - extractive body cue:** Thus, our realrobot experiments do not claim that off-the-shelf VLMs solve robotic recovery; rather, they expose the mismatch between current VLM benchmarks and the capabilities ...
- **p. 3 / 2.2. Benchmark and Failure Evaluation of VLM - extractive body cue:** While existing benchmarks like LIBERO (Liu et al., 2023)provide rigorous environments to assess task success rates , they largely overlook the underlying failure behaviors.
- **p. 4 / 4.2. Dynamic Evaluation - extractive body cue:** To assess corrective capabilities of multimodal models in robotic manipulation, we design a dynamic evaluation framework in simulation, focusing on corrective behavior during task execution, ...
- **p. 5 / 4.2. Dynamic Evaluation - extractive body cue:** Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, and precise rollback ...
- **p. 9 / 5.6. Ablation Study - extractive body cue:** Effectiveness of Self-Correction Across all evaluated tasks, human-in-the-loop correction consistently yields substantial performance gains over open-loop execution, improving average success rates by 13% points in ...
- **p. 3 / 2.2. Benchmark and Failure Evaluation of VLM - extractive body cue:** In contrast to prior work, we focus on task-level, interpretable, and recoverable failures in robotic manipulation.
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** The resulting dataset is curated with fine-grained annotations (failure type, subtask, and severity).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview of VLA-FixBench, Center: Hierarchical failure types in Perception, Planning, and Control. Left: Severity definitions ranging from redundant motions (Level-1) to catastrophic failures ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the VLA-FixBench framework. The pipeline includes: (Left) Dataset Construction with hierarchical task decomposition and spatio-temporal failure annotations; (Middle) Static Benchmark for ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Left: Static diagnostic accuracy across different task domains and severity levels. Right: Dynamic diagnostic performance, including Geometric Correction Accuracy (GCA) and Temporal Localization ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Static Evaluation Results of Fault Type Classification (FTC), Sub-task Success Evaluation (SSE), and Fault Severity Rating (FSR) across VLA Models.[Keys: Best/Second best in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Simulation Results on Dynamic Evaluation Metrics: Geometric Correction Accuracy (GCA), Temporal Localization Accuracy (TLA), and Simulation Success Rate (SSR). [Keys: Best/Second best in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Faults correlation analysis. Conditional failure depen- dency heatmap over fine-grained fault types. Each entry denotes P(b / a), the probability that failure type ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. The left figure shows the relationship between different fault types occurrence probability and task length, while the right figure shows the relationship between ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Failure recovery in the real-robot make-tea task.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To evaluate the practical performance of multimodal models in real-world robotic manipulation, we conduct on-robot experiments. | embodiment, simulator version and control stack | p. 6 (4.3. Real-Time Evaluation), p. 9 (5.4. Real-Time Evaluation Results) |
| Task/environment | Thus, our realrobot experiments do not claim that off-the-shelf VLMs solve robotic recovery; rather, they expose the mismatch between current VLM benchmarks and the ... | reset, timeout, object/scene variation | p. 9 (5.4. Real-Time Evaluation Results), p. 3 (2.2. Benchmark and Failure Evaluation of VLM) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 3 (Approach), p. 3 (Approach) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The performance is measured across diagnostic metrics (Recall, Precision, F2-Score, and FPR) and the manipulation Success Rate (SR). | definition/direction/unit from same section | p. 8 (5.2. Static Evaluation Results) |
| Figure 10. Annotation interface and operating procedure used for VLA-FixBench data annotation. Prediction Accuracy and Robustness. Precision and FPR evaluate the correctness of fault ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| To assess corrective capabilities of multimodal models in robotic manipulation, we design a dynamic evaluation framework in simulation, focusing on corrective behavior during task ... | definition/direction/unit from same section | p. 4 (4.2. Dynamic Evaluation) |
| Effectiveness of Self-Correction Across all evaluated tasks, human-in-the-loop correction consistently yields substantial performance gains over open-loop execution, improving average success rates by 13% points ... | definition/direction/unit from same section | p. 9 (5.6. Ablation Study) |
| While top-tier models like GPT-5 and GPT-5.2 demonstrate superior diagnostic precision, achieving the highest AA scores (up to 68.60%).Their Magnitude Accuracy (MA) remains a ... | definition/direction/unit from same section | p. 8 (5.3. Dynamic Evaluation Results) |
| Table 2. Simulation Results on Dynamic Evaluation Metrics: Geometric Correction Accuracy (GCA), Temporal Localization Accuracy (TLA), and Simulation Success Rate (SSR). [Keys: Best/Second best ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 3. Left: Static diagnostic accuracy across different task domains and severity levels. Right: Dynamic diagnostic performance, including Geometric Correction Accuracy (GCA) and Temporal ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| While existing benchmarks like LIBERO (Liu et al., 2023)provide rigorous environments to assess task success rates , they largely overlook the underlying failure behaviors. | definition/direction/unit from same section | p. 3 (2.2. Benchmark and Failure Evaluation of VLM) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, and precise ... | comparison identity and matched condition | p. 5 (4.2. Dynamic Evaluation) |
| By contrast, Qwen3-VL-235B is more conservative, with the highest Precision (0.7273) and lowest FPR (0.0588), though its SR (15%) remains below the Groot-N1.5-only baseline. | comparison identity and matched condition | p. 8 (5.4. Real-Time Evaluation Results) |
| SSR results expose a correction paradox: aggressive models (e.g., GPT series) often suffer from lower success rates than the baseline due to secondary failures ... | comparison identity and matched condition | p. 8 (5.3. Dynamic Evaluation Results) |
| In contrast to prior work, we focus on task-level, interpretable, and recoverable failures in robotic manipulation. | comparison identity and matched condition | p. 3 (2.2. Benchmark and Failure Evaluation of VLM) |
| Together, these complementary tracks balance efficiency and accuracy, enabling systematic model comparison and diagnosis for VLA systems. | comparison identity and matched condition | p. 4 (4. FaultEval Evaluation Framework) |
| This design follows three principles: (1) clarity and simplicity, allowing general black-box VLMs to integrate without model-specific output heads or adapters; (2) direct mapping ... | comparison identity and matched condition | p. 5 (4.2. Dynamic Evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This design follows three principles: (1) clarity and simplicity, allowing general black-box VLMs to integrate without model-specific output heads or adapters; (2) direct mapping ... | component/input/data sensitivity | p. 5 (4.2. Dynamic Evaluation) |
| Real-robot evaluations (Table 3) validate the sensitivitystability paradox. | component/input/data sensitivity | p. 8 (5.4. Real-Time Evaluation Results) |
| Current VLMs may misclassify trajectories that would have succeeded without intervention, triggering unnecessary rollback or correction and turning successes into failures. | component/input/data sensitivity | p. 8 (5.4. Real-Time Evaluation Results) |
| Architectures like OpenVLA (Kim et al., 2024) and GR00T N1 (NVIDIA et al., 2025) utilize frozen vision-language backbones augmented with lightweight action heads to ... | component/input/data sensitivity | p. 3 (2.2. Benchmark and Failure Evaluation of VLM) |
| Data Acquisition.For simulation, we fine-tuned OpenVLA7B (Kim et al., 2024) using data from the LIBERO bencha b c d e f g h i ... | component/input/data sensitivity | p. 7 (5.1. Experimental Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these challenges, we introduce VLA-FixBench, a benchmark for VLM-assisted VLA fault diagnosis and recovery, with over 6,000 annotated failure cases across perception, ... | Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, and precise ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.2. Dynamic Evaluation), p. 9 (5.6. Ablation Study), p. 6 (4.2. Dynamic Evaluation), p. 8 (5.2. Static Evaluation Results), p. 8 (5.2. Static Evaluation Results), p. 9 (5.5. Alignment Between Static and Dynamic Evaluation) |
| Primary metric/result | Effectiveness of Self-Correction Across all evaluated tasks, human-in-the-loop correction consistently yields substantial performance gains over open-loop execution, improving average success rates by 13% points ... | numeric claim only at cited anchor | p. 9 (5.6. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 6 / 4.3. Real-Time Evaluation - extractive body cue:** Video streams are transmitted to the VLM at 1 Hz for real-time fault diagnosis, rollback decisions, and corrective action recommendations.
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** 2 3 4 6 7 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 P(Fault / Task Length) Fault Type a b c d e ...
- **p. 9 / 5.4. Real-Time Evaluation Results - extractive body cue:** Thus, VLM latency is explicitly included in the closed-loop cycle: Tloop = Texec + Tvlm + Trollback, (8) where Texec = 1s, Tvlm is the ...
- **p. 4 / 3. Construction of VLA-FixBench - extractive body cue:** VLA-FixBench comprises 6,034 task execution episodes collected from 40 simulated and two real-robot environments.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The real-robot setup is therefore a sparse diagnostic-and-recovery loop that trades limited inspection latency for recovery from failures that the VLA alone cannot escape. | p. 9 (5.4. Real-Time Evaluation Results) |
| body limitation/failure cue | We introduce a unified benchmark and evaluation framework that systematically characterizes failure types, severity, and spatiotemporal repair behaviors, and explicitly measures how VLMs contribute ... | p. 3 (2.2. Benchmark and Failure Evaluation of VLM) |
| body limitation/failure cue | To bridge low-level signals and task execution, some works analyze failures in specific manipulation tasks. | p. 2 (2.1. Robotic Failure Diagnosis and Recovery) |
| body limitation/failure cue | As a result, existing failure analyses remain fragmented and lack a unified framework for systematic evaluation across tasks and models (Lin et al., 2025).Classical ... | p. 2 (2.1. Robotic Failure Diagnosis and Recovery) |
| body limitation/failure cue | Error severity level 7s Roll back time Accuracy Failure onset timestamp Convenience | p. 3 (2.1. Robotic Failure Diagnosis and Recovery) |
| body limitation/failure cue | For each failure scenario i, the model generates a dynamic recovery tuple ˆdi = ⟨ˆtstop, ˆtrb, vi⟩, consisting of the Stop Time ˆtstop ∈R≥0 ... | p. 4 (4.2. Dynamic Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The rectified initial action a′ trb is computed as: a′ ˆtrb = π(strb) + ∆p, where ∆p = δ · v (2) Here, ∆p ... | p. 5 (4.2. Dynamic Evaluation) |
| SSR is computed over all four LIBERO task suites, providing a unified assessment of performance consistency across diverse manipulation settings. | p. 6 (4.2. Dynamic Evaluation) |
| However, in several cases, they correctly detect that the VLA policy has entered a local optimum or erroneous trajectory, trigger rollback, and enable successful ... | p. 8 (5.4. Real-Time Evaluation Results) |
| [Keys: Best/Second best] Model Recall Precision F2-Score FPR SR Gemini-2.5-Pro (DeepMind, 2025b) 0.1795 0.4667 0.2047 0.1333 20 Gemini-2.5-Flash (DeepMind, 2025b) 0.1429 0.4167 0.1645 0.0933 ... | p. 8 (5.2. Static Evaluation Results) |
| We compute rank correlations between static and simulation evaluations, obtaining Spearman's ρ = 0.43 and Kendall's τ = 0.33. | p. 9 (5.5. Alignment Between Static and Dynamic Evaluation) |
| Level-1 Level-2 Level-3 FIH SG AOCI P&P MLT 0 50.3 57.1 26.8 28.4 26.5 22.6 27.4 0 12.1 37.8 71.7 60.9 57.0 54.0 61.4 ... | p. 4 (3. Construction of VLA-FixBench) |
| Impact of Rollback Step Selection We further analyze recovery strategies by comparing naive task-level rollback with rollback to intermediate execution steps. | p. 9 (5.6. Ablation Study) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5.4. Real-Time Evaluation Results - extractive body cue:** The real-robot setup is therefore a sparse diagnostic-and-recovery loop that trades limited inspection latency for recovery from failures that the VLA alone cannot escape.
- **p. 3 / 2.2. Benchmark and Failure Evaluation of VLM - extractive body cue:** We introduce a unified benchmark and evaluation framework that systematically characterizes failure types, severity, and spatiotemporal repair behaviors, and explicitly measures how VLMs contribute to ...
- **p. 2 / 2.1. Robotic Failure Diagnosis and Recovery - extractive body cue:** To bridge low-level signals and task execution, some works analyze failures in specific manipulation tasks.
- **p. 2 / 2.1. Robotic Failure Diagnosis and Recovery - extractive body cue:** As a result, existing failure analyses remain fragmented and lack a unified framework for systematic evaluation across tasks and models (Lin et al., 2025).Classical learning-based ...
- **p. 3 / 2.1. Robotic Failure Diagnosis and Recovery - extractive body cue:** Error severity level 7s Roll back time Accuracy Failure onset timestamp Convenience
- **p. 4 / 4.2. Dynamic Evaluation - extractive body cue:** For each failure scenario i, the model generates a dynamic recovery tuple ˆdi = ⟨ˆtstop, ˆtrb, vi⟩, consisting of the Stop Time ˆtstop ∈R≥0 representing ...

- **Evidence anchors reviewed:** datasets p. 6 (4.3. Real-Time Evaluation), p. 9 (5.4. Real-Time Evaluation Results), p. 3 (2.2. Benchmark and Failure Evaluation of VLM), p. 4 (4.2. Dynamic Evaluation), p. 5 (4.2. Dynamic Evaluation), p. 9 (5.6. Ablation Study), metrics p. 8 (5.2. Static Evaluation Results), p. 16 (Figure/Table caption), p. 4 (4.2. Dynamic Evaluation), p. 9 (5.6. Ablation Study), p. 8 (5.3. Dynamic Evaluation Results), p. 6 (Figure/Table caption), baselines p. 5 (4.2. Dynamic Evaluation), p. 8 (5.4. Real-Time Evaluation Results), p. 8 (5.3. Dynamic Evaluation Results), p. 3 (2.2. Benchmark and Failure Evaluation of VLM), p. 4 (4. FaultEval Evaluation Framework), p. 5 (4.2. Dynamic Evaluation), results p. 5 (4.2. Dynamic Evaluation), p. 9 (5.6. Ablation Study), p. 6 (4.2. Dynamic Evaluation), p. 8 (5.2. Static Evaluation Results), p. 8 (5.2. Static Evaluation Results), p. 9 (5.5. Alignment Between Static and Dynamic Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, and precise rollback outperforms coarse task restarts, demonstrating ... (p. 5, 4.2. Dynamic Evaluation).
- **Metric evidence:** Effectiveness of Self-Correction Across all evaluated tasks, human-in-the-loop correction consistently yields substantial performance gains over open-loop execution, improving average success rates by 13% points in simulation and by 35% ... (p. 9, 5.6. Ablation Study).
- **Baseline/ablation evidence:** In contrast to prior work, we focus on task-level, interpretable, and recoverable failures in robotic manipulation. (p. 3, 2.2. Benchmark and Failure Evaluation of VLM).
- **Failure/negative evidence:** GPT-5-2 achieves the highest sensitivity (Recall: 0.8571, F2-Score: 0.7143), but its high FPR (0.7568) causes task failure (SR: 0), indicating that oversensitive diagnosis can disrupt nominal executions. (p. 8, 5.4. Real-Time Evaluation Results).
