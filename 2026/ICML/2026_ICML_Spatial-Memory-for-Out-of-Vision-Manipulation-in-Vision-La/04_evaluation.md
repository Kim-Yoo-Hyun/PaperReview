# Evaluation - Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=5i888dLp8N; PDF retrieval source: https://openreview.net/pdf/95685162fa940bca32702d659b96eebf84138a75.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Real World Results), p. 7 (4.3. Real World Results), p. 8 (4.4. Simulation Results), p. 8 (4.4. Simulation Results), p. 6 (4.1. Benchmarks), p. 5 (Figure/Table caption)): In Figure 4, SOMA achieves the highest success rates across all five real-world out-of-vision (OOV) manipulation tasks.

## Evaluation Body Digest

- **p. 6 / 4.1. Benchmarks - extractive body cue:** SimplerEnv offers a standardized real-to-sim benchmark for evaluating policy success rates across simulated environments reflecting real-world robotic systems (Zitkovich et al., 2023).
- **p. 6 / 4.1. Benchmarks - extractive body cue:** As shown in Figure 3 and 5, we construct a real-world benchmark of five out-of-vision pickand-place (PnP) tasks with increasing difficulty to evaluate SOMA under ...
- **p. 8 / 4.3. Real World Results - extractive body cue:** Performance comparison via SR (%) across task categories on the Robocasa Tabletop GR1 benchmarks with varying numbers of demonstrations per task.
- **p. 7 / 4.2. Implementation - extractive body cue:** In simulation, the overview memory is constructed from the initial robot observation.
- **p. 7 / 4.3. Real World Results - extractive body cue:** In Figure 4, SOMA achieves the highest success rates across all five real-world out-of-vision (OOV) manipulation tasks.
- **p. 8 / 4.3. Real World Results - extractive body cue:** SimplerEnv evaluation across different SOTAs on Google Robot tasks.
- **p. 18 / Figure/Table caption - extractive body cue:** Table 10. Detailed Ablation studies on Robocasa Tabletop GR-1 benchmark. We compare different Update Strategies, Retrieval Modules, and Memory Representations. Reported values are success rates ...
- **p. 7 / 4.3. Real World Results - extractive body cue:** In contrast, SOMA maintains consistently higher success rates across both Pick and Place stages, with the performance gap widening as task complexity increases.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Benchmarks (p. 6); 4.2. Implementation (p. 6); 4.3. Real World Results (p. 7); 4.4. Simulation Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Real World Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | In Figure 4, SOMA achieves the highest success rates across all five real-world out-of-vision (OOV) manipulation tasks. | p. 7 (4.3. Real World Results) |
| 4.3. Real World Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | It demonstrates that SOMA's advantages go beyond improved success rates and manifest as qualitatively different execution behavior. | p. 7 (4.3. Real World Results) |
| 4.4. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, SOMA achieves the highest average performance of 52.0% with 300 demos and maintains competitive results across all data regimes, surpassing strong baselines such ... | p. 8 (4.4. Simulation Results) |
| 4.4. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to strong baselines like RoboVLM (Liu et al., 2025) (60.6%), SOMA improves performance particularly on challenging partialobservation tasks like Pick Coke Can (+7.7%), ... | p. 8 (4.4. Simulation Results) |
| 4.1. Benchmarks | EMPIRICAL / REAL-ROBOT OR HARDWARE | SimplerEnv offers a standardized real-to-sim benchmark for evaluating policy success rates across simulated environments reflecting real-world robotic systems (Zitkovich et al., 2023). | p. 6 (4.1. Benchmarks) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Benchmarks - extractive body cue:** SimplerEnv offers a standardized real-to-sim benchmark for evaluating policy success rates across simulated environments reflecting real-world robotic systems (Zitkovich et al., 2023).
- **p. 6 / 4.1. Benchmarks - extractive body cue:** As shown in Figure 3 and 5, we construct a real-world benchmark of five out-of-vision pickand-place (PnP) tasks with increasing difficulty to evaluate SOMA under ...
- **p. 8 / 4.3. Real World Results - extractive body cue:** Performance comparison via SR (%) across task categories on the Robocasa Tabletop GR1 benchmarks with varying numbers of demonstrations per task.
- **p. 7 / 4.2. Implementation - extractive body cue:** In simulation, the overview memory is constructed from the initial robot observation.
- **p. 7 / 4.3. Real World Results - extractive body cue:** In Figure 4, SOMA achieves the highest success rates across all five real-world out-of-vision (OOV) manipulation tasks.
- **p. 8 / 4.3. Real World Results - extractive body cue:** SimplerEnv evaluation across different SOTAs on Google Robot tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of the Out-of-Vision (OOV) limitation in existing VLA models. Most VLAs rely on purely reactive percep- tion-actions are driven only by what ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Illustration of the proposed SOMA framework. SOMA enhances OOV manipulation via spatial memory. (A) Spatial Memory Construction: Before manipulation, if the specified objects ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Illustration of our real world benchmark settings. We design five challenging out-of-vision pick-and-place (PnP) tasks to evaluate the robot's OOV manipulation capabilities. Tasks ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Performance comparison across five real world out-of-vision tasks. "Fixed Head Camera" denotes we train SOMA under fixed head camera setting. StarVLA (Ye et ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Behavioral comparison between GR00T-N1.5 and SOMA on five real-world OOV manipulation tasks. To maintain an up-to-date and globally coherent scene representation, Dynamic Memory ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Ablation study on scan-based exploration and spatial mem- ory for real-world OOV manipulation. Scan+GR00T performs head scanning and uses the detected target frame ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Illustration of task execution examples for our five challenging out-of-vision tasks in real world using our proposed SOMA. experiments, the Spatial Memory Construction ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Performance comparison via SR (%) across task categories on the Robocasa Tabletop GR1 benchmarks with varying numbers of demonstrations per task. Each group ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | SimplerEnv offers a standardized real-to-sim benchmark for evaluating policy success rates across simulated environments reflecting real-world robotic systems (Zitkovich et al., 2023). | embodiment, simulator version and control stack | p. 6 (4.1. Benchmarks), p. 6 (4.1. Benchmarks) |
| Task/environment | As shown in Figure 3 and 5, we construct a real-world benchmark of five out-of-vision pickand-place (PnP) tasks with increasing difficulty to evaluate SOMA ... | reset, timeout, object/scene variation | p. 6 (4.1. Benchmarks), p. 8 (4.3. Real World Results) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 3 (3. Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.1. Spatial Memory Construction), p. 6 (3.3. Contextual Memory Retrieval) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 10. Detailed Ablation studies on Robocasa Tabletop GR-1 benchmark. We compare different Update Strategies, Retrieval Modules, and Memory Representations. Reported values are success ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| In contrast, SOMA maintains consistently higher success rates across both Pick and Place stages, with the performance gap widening as task complexity increases. | definition/direction/unit from same section | p. 7 (4.3. Real World Results) |
| SimplerEnv offers a standardized real-to-sim benchmark for evaluating policy success rates across simulated environments reflecting real-world robotic systems (Zitkovich et al., 2023). | definition/direction/unit from same section | p. 6 (4.1. Benchmarks) |
| In Figure 4, SOMA achieves the highest success rates across all five real-world out-of-vision (OOV) manipulation tasks. | definition/direction/unit from same section | p. 7 (4.3. Real World Results) |
| Notably, even with only 30-100 demonstrations per task, SOMA maintains high success rates, revealing strong sample efficiency and robust generalization to unseen spatial configurations. | definition/direction/unit from same section | p. 8 (4.4. Simulation Results) |
| Figure 4. Performance comparison across five real world out-of-vision tasks. "Fixed Head Camera" denotes we train SOMA under fixed head camera setting. StarVLA (Ye ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 9. Performance comparison via success rate (%) across task categories on the Robocasa Tabletop GR-1 benchmark with varying numbers of demonstrations per task. ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| All experiments evaluated over 50 episodes for accuracy. | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 5. Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote Geometric cues and object semantics, respectively. SimplerEnv Results. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Compared to strong baselines like RoboVLM (Liu et al., 2025) (60.6%), SOMA improves performance particularly on challenging partialobservation tasks like Pick Coke Can (+7.7%), ... | comparison identity and matched condition | p. 8 (4.4. Simulation Results) |
| No-Scan SOMA slightly outperforms Scan+GR00T despite using only a single-view initialization, highlighting the benefit of an explicit memory structure even without multi-view coverage. | comparison identity and matched condition | p. 7 (4.3. Real World Results) |
| We adopt GR00T N1.5 (Bjorck et al., 2025) as the real-world baseline. | comparison identity and matched condition | p. 6 (4.2. Implementation) |
| Ablation study on scan-based exploration and spatial memory for real-world OOV manipulation. | comparison identity and matched condition | p. 6 (4.1. Benchmarks) |
| Scan+GR00T, which performs head scanning without maintaining a persistent spatial memory, yields the lowest performance, indicating that scan-based exploration alone is insufficient for reliable ... | comparison identity and matched condition | p. 7 (4.3. Real World Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2. Ablation study on scan-based exploration and spatial mem- ory for real-world OOV manipulation. Scan+GR00T performs head scanning and uses the detected target ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 10. Detailed Ablation studies on Robocasa Tabletop GR-1 benchmark. We compare different Update Strategies, Retrieval Modules, and Memory Representations. Reported values are success ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| As shown in Table 5, we conduct the ablation study on different components of the overview scene memory. | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |
| Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote Geometric cues and object semantics, respectively. | component/input/data sensitivity | p. 8 (4.4. Simulation Results) |
| The fixed-head variant fails once either the target or the goal leaves the field of view, confirming the brittleness of view-bound policies under partial ... | component/input/data sensitivity | p. 7 (4.3. Real World Results) |
| No-Scan SOMA slightly outperforms Scan+GR00T despite using only a single-view initialization, highlighting the benefit of an explicit memory structure even without multi-view coverage. | component/input/data sensitivity | p. 7 (4.3. Real World Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and ... | In Figure 4, SOMA achieves the highest success rates across all five real-world out-of-vision (OOV) manipulation tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Real World Results), p. 7 (4.3. Real World Results), p. 8 (4.4. Simulation Results), p. 8 (4.4. Simulation Results), p. 6 (4.1. Benchmarks), p. 5 (Figure/Table caption) |
| Primary metric/result | It demonstrates that SOMA's advantages go beyond improved success rates and manifest as qualitatively different execution behavior. | numeric claim only at cited anchor | p. 7 (4.3. Real World Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Benchmarks - extractive body cue:** These tasks OOV Task Scan+GR00T No-Scan SOMA Scan-only SOMA Full SOMA Task 1 19.0 20.0 25.0 30.0 Task 2 22.0 24.0 29.0 35.0 Task 3 ...
- **p. 6 / 4.2. Implementation - extractive body cue:** During training, all components are optimized except the VLM language decoder, using multi-task learning with a batch size of 60 for 30,000 steps on 32 ...
- **p. 6 / 4.2. Implementation - extractive body cue:** All inference are executed on a server equipped with an NVIDIA RTX 4090 GPU.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** All experiments evaluated over 50 episodes for accuracy.
- **p. 5 / 3.2. Dynamic Memory Refinement - extractive body cue:** We adopt 20 episodes and average SR (Success Rate) to evaluate the models by multi-stages.
- **p. 5 / 3.2. Dynamic Memory Refinement - extractive body cue:** Behavioral Analysis on Real-World Out-of-Vision Tasks Model Task 1 Task 2 Task 3 Task 4 Task 5 First-Fixation Time (s) ↓ GR00T-N1.5 7.6 21.0 14.8 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per category). Under full observability, failures reflect ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. Illustration of the Out-of-Vision (OOV) limitation in existing VLA models. Most VLAs rely on purely reactive percep- tion-actions are driven only by ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | We propose SOMA, a spatial memory framework for VisionLanguage-Action models that addresses the fundamental limitation of view-bound perception in out-of-vision manip8 | p. 8 (5. Conclusion) |
| body limitation/failure cue | Table 14. Failure mode analysis on real-world OOV tasks (25 sampled failed episodes, 5 per task). Failures predominantly arise when translating reliable spatial localization ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | If the target cannot be localized, SOMA initiates an active head-scanning procedure along a predefined trajectory to construct the spatial memory. | p. 7 (4.2. Implementation) |
| body limitation/failure cue | Scan-only SOMA further improves success rates by leveraging multi-view scanning to construct a more complete initial memory, but still falls short of the full ... | p. 7 (4.3. Real World Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During training, all components are optimized except the VLM language decoder, using multi-task learning with a batch size of 60 for 30,000 steps on ... | p. 6 (4.2. Implementation) |
| All inference are executed on a server equipped with an NVIDIA RTX 4090 GPU. | p. 6 (4.2. Implementation) |
| These representations are aggregated into an overview scene memory M0, which encodes a unified spatial-semantic representation of all observed objects. | p. 3 (3. Method) |
| The resulting memory-enhanced vision-language tokens, together with robot states and noised action embeddings, are processed by DiT blocks and an action decoder to predict ... | p. 3 (3. Method) |
| Spatial Memory Construction Current Observation: {"! ", "#", "$ "} Vision Encoder B. | p. 4 (3.1. Spatial Memory Construction) |
| Dynamic Memory Refinement ··· ··· ··· Instruction: "Pick the pink cup and place it in the basket." Text Tokenizer VLM Robot State: {%% ", ... | p. 4 (3.1. Spatial Memory Construction) |
| Given the previous memory vector mt-1 k and the new observation mt j, we compute the semantic similarity st kj and a dynamic fusion ... | p. 5 (3.2. Dynamic Memory Refinement) |
| The current observation ot h is processed by the same embedding pipeline described in Section 3.1 at time t, producing the current memory tokens ... | p. 5 (3.2. Dynamic Memory Refinement) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 20 / Figure/Table caption - extractive body cue:** Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per category). Under full observability, failures reflect limitations ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of the Out-of-Vision (OOV) limitation in existing VLA models. Most VLAs rely on purely reactive percep- tion-actions are driven only by what ...
- **p. 8 / 5. Conclusion - extractive body cue:** We propose SOMA, a spatial memory framework for VisionLanguage-Action models that addresses the fundamental limitation of view-bound perception in out-of-vision manip8
- **p. 20 / Figure/Table caption - extractive body cue:** Table 14. Failure mode analysis on real-world OOV tasks (25 sampled failed episodes, 5 per task). Failures predominantly arise when translating reliable spatial localization into ...
- **p. 7 / 4.2. Implementation - extractive body cue:** If the target cannot be localized, SOMA initiates an active head-scanning procedure along a predefined trajectory to construct the spatial memory.
- **p. 7 / 4.3. Real World Results - extractive body cue:** Scan-only SOMA further improves success rates by leveraging multi-view scanning to construct a more complete initial memory, but still falls short of the full model.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Benchmarks), p. 6 (4.1. Benchmarks), p. 8 (4.3. Real World Results), p. 7 (4.2. Implementation), p. 7 (4.3. Real World Results), p. 8 (4.3. Real World Results), metrics p. 18 (Figure/Table caption), p. 7 (4.3. Real World Results), p. 6 (4.1. Benchmarks), p. 7 (4.3. Real World Results), p. 8 (4.4. Simulation Results), p. 5 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 8 (4.4. Simulation Results), p. 7 (4.3. Real World Results), p. 6 (4.2. Implementation), p. 6 (4.1. Benchmarks), p. 7 (4.3. Real World Results), results p. 7 (4.3. Real World Results), p. 7 (4.3. Real World Results), p. 8 (4.4. Simulation Results), p. 8 (4.4. Simulation Results), p. 6 (4.1. Benchmarks), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
