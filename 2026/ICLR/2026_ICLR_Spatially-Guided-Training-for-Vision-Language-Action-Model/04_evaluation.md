# Evaluation - Spatially Guided Training for Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eKhOrQWAVJ; PDF retrieval source: https://openreview.net/pdf/5b6d4b55e3d738aceaa3495460aa12907b69dcee.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 6 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), p. 20 (Figure/Table caption), p. 5 (3 EXPERIMENTS)): Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et al. (2024) and GR00T N1.5 Bjorck ...

## Evaluation Body Digest

- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** 3.4 EVALUATION IN REAL-WORLD CLUTTERED-SCENE PICK-AND-PLACE We use the Franka Research 3 robot to evaluate the generalization performance of our model and baselines on the ...
- **p. 6 / 3 EXPERIMENTS - extractive PDF cue:** We further evaluate ST4VLA on the LIBERO simulation suite, detailed in Appendix Section B.2 Table 2: Result comparisons of robotic manipulation on SimplerEnv (Google-Robot) benchmark.
- **p. 6 / 3 EXPERIMENTS - extractive PDF cue:** Compared with prior state-of-the-art models, it attains a 5.9% gain in Google Robot Visual Matching, a 5.3% gain in Visual Aggregation, and a 9.8% gain ...
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 3: Result comparisons of robotic manipulation on SimplerEnv (WidowX) benchmark.
- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** Details of the real-world robot setup and additional experimental configurations are provided in Appendix Section D.3.
- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 200 simulated tasks, the post-training leverages both large-scale simulation data and real-world trajectories.
- **p. 4 / 3 EXPERIMENTS - extractive PDF cue:** Finally, we examine real-robot performance on both short-horizon and long-horizon tasks to validate practical deployment capabilities (Section 3.5).
- **p. 4 / 3 EXPERIMENTS - extractive PDF cue:** We then evaluate large-scale instruction-following pick-and-place in simulation and real-world to test generalization (Section 3.3 and Section 3.4 ).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 3 EXPERIMENTS (p. 4); B.2 LIBERO Benchmark (p. 18); B ADDITIONAL EXPERIMENTS (p. 19); B.2 LIBERO BENCHMARK (p. 19).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5. Compared to previous strong baselines, such as GR00T N1 and π0, the ST4VLA framework achieves notable improvements, particularly on the spatial and ... | p. 20 (Figure/Table caption) |
| 3 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to the Vanilla VLA based on QwenVL-2.5-3B-Instruct, ST4VLA achieves substantial improvements: a 14.6% increase in Google Robot Visual Matching and a 12.4% increase ... | p. 6 (3 EXPERIMENTS) |
| 3 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our Spatially Guided approach achieves the best balance: it maintains 70% of original RefCOGO-g performance while reaching 60% WidowX success in just 20k steps. | p. 5 (3 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Extended training curves up to 100k steps on WidowX and Google Robot tasks. Even with prolonged training, baselines saturate at a significantly ... | p. 20 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** 3.4 EVALUATION IN REAL-WORLD CLUTTERED-SCENE PICK-AND-PLACE We use the Franka Research 3 robot to evaluate the generalization performance of our model and baselines on the ...
- **p. 6 / 3 EXPERIMENTS - extractive PDF cue:** We further evaluate ST4VLA on the LIBERO simulation suite, detailed in Appendix Section B.2 Table 2: Result comparisons of robotic manipulation on SimplerEnv (Google-Robot) benchmark.
- **p. 6 / 3 EXPERIMENTS - extractive PDF cue:** Compared with prior state-of-the-art models, it attains a 5.9% gain in Google Robot Visual Matching, a 5.3% gain in Visual Aggregation, and a 9.8% gain ...
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 3: Result comparisons of robotic manipulation on SimplerEnv (WidowX) benchmark.
- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** Details of the real-world robot setup and additional experimental configurations are provided in Appendix Section D.3.
- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 200 simulated tasks, the post-training leverages both large-scale simulation data and real-world trajectories.
- **p. 4 / 3 EXPERIMENTS - extractive PDF cue:** Finally, we examine real-robot performance on both short-horizon and long-horizon tasks to validate practical deployment capabilities (Section 3.5).
- **p. 4 / 3 EXPERIMENTS - extractive PDF cue:** We then evaluate large-scale instruction-following pick-and-place in simulation and real-world to test generalization (Section 3.3 and Section 3.4 ).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: ST4VLA integrates spatial priors into the vision-language-action training pipeline. Given a task instruction, the VLM planner produces latent plans through explicit spatial prompting, ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of ST4VLA. ST4VLA adopts a spatially guided two-stage training pipeline. Stage 1 (spatial grounding pre-training): the VLM is trained on large-scale multisource ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Ablation study on the effect of auxiliary spatial prompting during co-training. From left to right: (a) perception performance (IoU@0.5 on RefCOCO-g); (b) manipulation ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1: Study of VLA training strategies and their effects on multi-modal understanding, spatial grounding, and robot manipulation performance. Multi-modal Understanding Spatial Grounding Robotic Manipulation ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Result comparisons of robotic manipulation on SimplerEnv (Google-Robot) benchmark. The underlined scores indicate the best results excluding ST4VLA. Numbers are officially reported; otherwise, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3: Result comparisons of robotic manipulation on SimplerEnv (WidowX) benchmark. The underlined scores indicate the best results, excluding our results. WidowX Robot Models Co-Train ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et al. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Comparison of results on real-world generalization of pick-and-place tasks. Success rates (%) are reported. Abbreviations: In dist.: in-distribution; New inst.: new instance; Similar ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3.4 EVALUATION IN REAL-WORLD CLUTTERED-SCENE PICK-AND-PLACE We use the Franka Research 3 robot to evaluate the generalization performance of our model and baselines on ... | embodiment, simulator version and control stack | p. 7 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Task/environment | We further evaluate ST4VLA on the LIBERO simulation suite, detailed in Appendix Section B.2 Table 2: Result comparisons of robotic manipulation on SimplerEnv (Google-Robot) ... | reset, timeout, object/scene variation | p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 3: Ablation study on the effect of auxiliary spatial prompting during co-training. From left to right: (a) perception performance (IoU@0.5 on RefCOCO-g); (b) ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Success Rate (%) 𝝅𝟎 GR00T N1.5 51 75 80 In distribution 42 65 68 Unseen object 47 75 78 Unseen instruction 33 59 72 ... | definition/direction/unit from same section | p. 7 (3 EXPERIMENTS) |
| 3.5 EVALUATION IN LONG-HORIZON MANIPULATION 𝝅𝟎 GR00t N1.5 ST4VLA 29 42 59 In distribution 16 41 54 Physical interference 26 45 57 Task replanning ... | definition/direction/unit from same section | p. 8 (3 EXPERIMENTS) |
| Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 4: Comparison of results on real-world generalization of pick-and-place tasks. Success rates (%) are reported. Abbreviations: In dist.: in-distribution; New inst.: new instance; ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 5. Compared to previous strong baselines, such as GR00T N1 and π0, the ST4VLA framework achieves notable improvements, particularly on the spatial and ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Figure 8: Overview of objects and containers used in instruction-following pick-and-place. For each model, we conduct a total of 300 rollout evaluations. Each trial ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |
| The underlined scores indicate the best results excluding ST4VLA. | definition/direction/unit from same section | p. 6 (3 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 5. Compared to previous strong baselines, such as GR00T N1 and π0, the ST4VLA framework achieves notable improvements, particularly on the spatial and ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Compared to the vanilla co-training baseline, our ST4VLA achieves superior robotic manipulation performance (84.6% VM / 75.9% VA on Google Robot and 73.2% on ... | comparison identity and matched condition | p. 5 (3 EXPERIMENTS) |
| Compared with prior state-of-the-art models, it attains a 5.9% gain in Google Robot Visual Matching, a 5.3% gain in Visual Aggregation, and a 9.8% ... | comparison identity and matched condition | p. 6 (3 EXPERIMENTS) |
| ST4VLA outperforms all baselines across real-world test settings. | comparison identity and matched condition | p. 8 (3 EXPERIMENTS) |
| Figure 6: Extended training curves up to 100k steps on WidowX and Google Robot tasks. Even with prolonged training, baselines saturate at a significantly ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 3: Ablation study on the effect of auxiliary spatial prompting during co-training. From left to right: (a) perception performance (IoU@0.5 on RefCOCO-g); (b) ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| (2025a) ✓ 83.7 65.4 56.0 6.4 52.9 Vanilla VLA ✗ 90.0 69.8 52.5 52.2 66.1 Vanilla Co-training VLA ✓ 91.3 75.1 55.0 59.4 70.2 ... | component/input/data sensitivity | p. 6 (3 EXPERIMENTS) |
| We compare three distinct training strategies using the OXE dataset for action data and a curated set of spatial grounding datasets for multimodal co-training: ... | component/input/data sensitivity | p. 5 (3 EXPERIMENTS) |
| Table 9: Ablation on the scaling of Spatial Grounding Pre-training data volume. Pre-training Scale Google Robot VM Google Robot VA WidowX VM Average | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Table 10: Ablation analysis of different spatial prompt formulations on SimplerEnv, comparing the default Unified Prompt against non-semantic and explicit formatting constraints. Prompt Type ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |
| Figure 17: Showcases for real-world large scale pick-and-place manipulation w/wo co-training. We further evaluate our framework in real-world cluttered tabletop environments. As shown in ... | component/input/data sensitivity | p. 32 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action ... | Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 6 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), p. 20 (Figure/Table caption), p. 5 (3 EXPERIMENTS) |
| Primary metric/result | Table 5. Compared to previous strong baselines, such as GR00T N1 and π0, the ST4VLA framework achieves notable improvements, particularly on the spatial and ... | numeric claim only at cited anchor | p. 20 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** With the inclusion of background elements, the benchmark encompasses more than 3,000 objects and containers.
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** Furthermore, for each of the 200 tasks, we additionally collected 5 trajectories with identical object sets but randomized layouts, which were used for post-training.
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** 3.4 EVALUATION IN REAL-WORLD CLUTTERED-SCENE PICK-AND-PLACE We use the Franka Research 3 robot to evaluate the generalization performance of our model and baselines on the ...
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** We collect 1K pick-and-place trajectories involving 23 objects and 5 containers, which are used for post-training.
- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** 3.5 EVALUATION IN LONG-HORIZON MANIPULATION 𝝅𝟎 GR00t N1.5 ST4VLA 29 42 59 In distribution 16 41 54 Physical interference 26 45 57 Task replanning Success ...
- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** We collect 22 hours of teleoperated demonstrations, segment trajectories into subtasks, and train ST4VLA jointly on task decomposition, subtask identification and action prediction.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure cases during real-world instruction-following pick-and-place tasks. As shown ... | p. 36 (Figure/Table caption) |
| body limitation/failure cue | Figure 25: Simulation data synthesis pipeline. The pipeline generates diverse robotic manipulation data from a large asset library, converts intermediate representations into VQA data, ... | p. 38 (Figure/Table caption) |
| body limitation/failure cue | Vanilla co-training partially preserves perception but exhibits unstable oscillations in both metrics. | p. 5 (3 EXPERIMENTS) |
| body limitation/failure cue | To address these limitations, we construct a large-scale simulation benchmark in Isaac-Sim by GenManip Gao et al. | p. 7 (3 EXPERIMENTS) |
| body limitation/failure cue | Results in Figure 5 show that ST4VLA consistently surpasses GR00T N1.5 and π0, reliably grounding high-level goals into executable steps, adapting to disturbances, and ... | p. 8 (3 EXPERIMENTS) |
| body limitation/failure cue | (2025a) also adopts spatial pre-training, though it does not explicitly leverage spatial prompting to guide action generation. | p. 9 (4 RELATED WORK) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our Spatially Guided approach achieves the best balance: it maintains 70% of original RefCOGO-g performance while reaching 60% WidowX success in just 20k steps. | p. 5 (3 EXPERIMENTS) |
| Vanilla VLA shows rapid spatial perception degradation, with RefCOCO-g performance dropping to near-random levels by 20k steps, indicating that action-only optimization disrupts spatial representations. | p. 5 (3 EXPERIMENTS) |
| Results in Figure 5 show that ST4VLA consistently surpasses GR00T N1.5 and π0, reliably grounding high-level goals into executable steps, adapting to disturbances, and ... | p. 8 (3 EXPERIMENTS) |
| Source code, data and models are released at https: //internrobotics.github.io/internvla-m1.github.io. | p. 1 (ABSTRACT) |
| Given a task instruction, the VLM planner produces latent plans through explicit spatial prompting, which then effectively guides the action expert to generate control ... | p. 2 (1 INTRODUCTION) |
| The framework builds on a dual-system architecture: System 2 (the VLM planner) employs as a multimodal encoder to capture spatial and semantic priors, while ... | p. 3 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 36 / Figure/Table caption - extractive PDF cue:** Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure cases during real-world instruction-following pick-and-place tasks. As shown in ...
- **p. 38 / Figure/Table caption - extractive PDF cue:** Figure 25: Simulation data synthesis pipeline. The pipeline generates diverse robotic manipulation data from a large asset library, converts intermediate representations into VQA data, and ...
- **p. 5 / 3 EXPERIMENTS - extractive PDF cue:** Vanilla co-training partially preserves perception but exhibits unstable oscillations in both metrics.
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** To address these limitations, we construct a large-scale simulation benchmark in Isaac-Sim by GenManip Gao et al.
- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** Results in Figure 5 show that ST4VLA consistently surpasses GR00T N1.5 and π0, reliably grounding high-level goals into executable steps, adapting to disturbances, and dynamically ...
- **p. 9 / 4 RELATED WORK - extractive PDF cue:** (2025a) also adopts spatial pre-training, though it does not explicitly leverage spatial prompting to guide action generation.

- **PDF anchors reviewed:** datasets p. 7 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), metrics p. 5 (Figure/Table caption), p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 20 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 20 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 6 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), p. 20 (Figure/Table caption), p. 5 (3 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
