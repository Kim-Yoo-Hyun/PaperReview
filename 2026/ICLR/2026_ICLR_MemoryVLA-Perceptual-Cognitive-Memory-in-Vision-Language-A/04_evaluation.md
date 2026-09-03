# Evaluation - MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=54U3XHf7qq; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248101. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 9 (4 EXPERIMENTS)): Touch Medium Color3 Color5 Color9 Success CronusVLA (Li et al., 2025a) 32 5 31 13 9 18.0 SpatialVLA (Qu et al., 2025) 23 27 27 17 11 21.0 OpenVLA-OFT (Kim ...

## Evaluation Body Digest

- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4 overviews our evaluation across simulation and real-world, covering 3 robots, 6 benchmarks, 150+ tasks with 500+ variations.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** (Appendix B) 4.1 EXPERIMENTAL SETUPS Simulation and Real-world Benchmarks.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In total, we evaluate 3 robots across 6 benchmarks, spanning over 150 tasks and 500 variations.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.3 SIMULATED EVALUATION ON LIBERO Training and Evaluation Setup We evaluate on the LIBERO (Liu et al., 2023a) benchmark with a Franka robot across five ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.5 REAL-WORLD EVALUATION Training and Evaluation Setup We evaluate two real-robot suites, General and Long-horizon Temporal, on Franka and WidowX robots.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Following the standard Mikasa-Robo protocol using 250 demonstrations per task at 128×128 resolution, 100 evaluation episodes per task and endeffector control.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 4.4 SIMULATED EVALUATION ON MIKASA-ROBO Training and Evaluation Setup We evaluate on the Mikasa-Robo (Cherepanov et al., 2025) benchmark.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Evaluation Results on Real-world As shown in Tab.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); B Robustness and Generalization Evaluation (p. 17); B.1 Real-world Evaluation (p. 17); B.2 Simulation Evaluation (p. 17); B ROBUSTNESS AND GENERALIZATION EVALUATION (p. 18); B.1 REAL-WORLD EVALUATION (p. 18); B.2 SIMULATION EVALUATION (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Touch Medium Color3 Color5 Color9 Success CronusVLA (Li et al., 2025a) 32 5 31 13 9 18.0 SpatialVLA (Qu et al., 2025) 23 27 ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | MemoryVLA achieves an overall success rate of 72.7%, improving CogACT by +4.6 points and surpassing π0. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, MemoryVLA achieves an average success rate of 71.9%, a +14.6 point gain over the CogACT-Large baseline, and surpasses recent state-of-the-art VLAs including π0 ... | p. 7 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: Performance comparison on SimplerEnv-Fractal (Li et al., 2024b) with Google robot. Success rates (%) are reported for Visual Matching (VM) and Visual ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick Coke Can and (b) Move Near ... | p. 19 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4 overviews our evaluation across simulation and real-world, covering 3 robots, 6 benchmarks, 150+ tasks with 500+ variations.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** (Appendix B) 4.1 EXPERIMENTAL SETUPS Simulation and Real-world Benchmarks.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In total, we evaluate 3 robots across 6 benchmarks, spanning over 150 tasks and 500 variations.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.3 SIMULATED EVALUATION ON LIBERO Training and Evaluation Setup We evaluate on the LIBERO (Liu et al., 2023a) benchmark with a Franka robot across five ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.5 REAL-WORLD EVALUATION Training and Evaluation Setup We evaluate two real-robot suites, General and Long-horizon Temporal, on Franka and WidowX robots.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Following the standard Mikasa-Robo protocol using 250 demonstrations per task at 128×128 resolution, 100 evaluation episodes per task and endeffector control.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 4.4 SIMULATED EVALUATION ON MIKASA-ROBO Training and Evaluation Setup We evaluate on the Mikasa-Robo (Cherepanov et al., 2025) benchmark.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Evaluation Results on Real-world As shown in Tab.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) In Push Buttons tasks, pre- and post-push states look nearly identical, calling for temporal modeling. (b) Humans handle manipulation tasks via a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overall architecture of MemoryVLA. RGB observation and language instruction are encoded by a 7B VLM into perceptual and cognitive tokens, forming short-term working ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Details of memory module. (a) Retrieval: current perceptual and cognitive tokens query the PCMB via cross-attention with timestep positional encoding to fetch relevant ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Experimental setup overview. Top: Four simulation benchmarks, SimpleEnv-Bridge, SimpleEnv-Fractal, LIBERO, and Mikasa-Robo. Bottom: real-world evaluation (General and Long- horizon Temporal), real-world robustness and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison on SimplerEnv-Bridge (Li et al., 2024b) with WidowX robot. CogACT-Large is our re-evaluated baseline using official weight, and MemoryVLA achieves a ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Performance comparison on SimplerEnv-Fractal (Li et al., 2024b) with Google robot. Success rates (%) are reported for Visual Matching (VM) and Visual Aggregation ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Performance comparison on LIBERO (Liu et al., 2023a) with Franka robot. Success rates (%) are reported across five suites. * indicates methods using ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Performance comparison on Mikasa-Robo (Cherepanov et al., 2025) with Franka robot. Success rates (%) are reported. CronusVLA results are reproduced by us.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4 overviews our evaluation across simulation and real-world, covering 3 robots, 6 benchmarks, 150+ tasks with 500+ variations. | embodiment, simulator version and control stack | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | (Appendix B) 4.1 EXPERIMENTAL SETUPS Simulation and Real-world Benchmarks. | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3 METHOD), p. 4 (3 METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick Coke Can and (b) Move Near ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| MemoryVLA achieves an overall success rate of 72.7%, improving CogACT by +4.6 points and surpassing π0. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Results are reported at the best validation step, and each task is evaluated with 24 trials to compute success rates. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Success rates (%) are reported for Visual Matching (VM) and Visual Aggregation (VA) suites. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Per-suite success rates are 98.4% on Spatial, 98.4% on Object, 96.4% on Goal, 93.4% on Long-10, and 95.6% on Long-90. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Success rates (%) are reported across five suites. * indicates methods using additional proprioceptive and wrist-camera inputs. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| We report average success rates (%) on SimplerEnv-Bridge tasks. | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| Table 4: Performance comparison on Mikasa-Robo (Cherepanov et al., 2025) with Franka robot. Success rates (%) are reported. CronusVLA results are reproduced by us. | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 1: (a) In Push Buttons tasks, pre- and post-push states look nearly identical, calling for temporal modeling. (b) Humans handle manipulation tasks via ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| 1, MemoryVLA achieves an average success rate of 71.9%, a +14.6 point gain over the CogACT-Large baseline, and surpasses recent state-of-the-art VLAs including π0 ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Table 15: Inference efficiency comparison. Latency, throughput, and GPU memory are measured over 300 runs in bfloat16 with action chunk length set to 16 ... | comparison identity and matched condition | p. 27 (Figure/Table caption) |
| Table 17: Comparison with temporal-context VLA methods across diverse benchmarks. Mem- oryVLA outperforms temporal-context VLA baselines across both memory-focused benchmarks and general manipulation benchmarks, ... | comparison identity and matched condition | p. 28 (Figure/Table caption) |
| To comprehensively evaluate MemoryVLA, we organize experiments around six core questions: (1) How does MemoryVLA compare with state-of-the-art methods on SimplerEnv benchmark? | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| CogACT-Large is our re-evaluated baseline using official weight, and MemoryVLA achieves a +14.6 gain in average success. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 6: Ablation on memory type and length. We report average success rates (%) on SimplerEnv-Bridge tasks. Variant Avg. Success Memory Type | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Table 9: Action Length Statistics across all simulation (SimplerEnv Bridge/Fractal, LIBERO Spa- tial/Object/Goal, LIBERO-10/90) and real-world (General, Temporal) task suites. For real-world tasks, the ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |
| The Fractal testbed includes 336 variants, yielding 2,856 trials in total. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| Note that MemoryVLA uses only third-person RGB, without wrist views or proprioceptive states. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| For methods without LIBERO-90 results, we report the average over the first four suites. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Pick Diverse Fruits comprises five variants with 5 trials per variant (25 total); all other General tasks use 15 trials. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM ... | Touch Medium Color3 Color5 Color9 Success CronusVLA (Li et al., 2025a) 32 5 31 13 9 18.0 SpatialVLA (Qu et al., 2025) 23 27 ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 9 (4 EXPERIMENTS) |
| Primary metric/result | MemoryVLA achieves an overall success rate of 72.7%, improving CogACT by +4.6 points and surpassing π0. | numeric claim only at cited anchor | p. 7 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4 overviews our evaluation across simulation and real-world, covering 3 robots, 6 benchmarks, 150+ tasks with 500+ variations.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Implementation Details We train on 8 NVIDIA A100 GPUs with PyTorch FSDP, using 32 samples per GPU for a global batch of 256 and a ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In total, we evaluate 3 robots across 6 benchmarks, spanning over 150 tasks and 500 variations.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Results are reported at the best validation step, and each task is evaluated with 24 trials to compute success rates.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The Fractal testbed includes 336 variants, yielding 2,856 trials in total.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 1, MemoryVLA achieves an average success rate of 71.9%, a +14.6 point gain over the CogACT-Large baseline, and surpasses recent state-of-the-art VLAs including π0 (Black ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD variants for two representative tasks (Pick Place Order ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick Coke Can and (b) Move Near ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | Figure 7: Robustness and generalization under out-of-distribution (OOD) variants in simu- lation: Hinge-like object manipulation. (a) OOD variants of Open/Close Drawer and (b) Place ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Table 11: Ablation on the Number of Cognitive Tokens. Increasing the number of cognitive tokens from 1 to 4 does not improve performance. A ... | p. 25 (Figure/Table caption) |
| body limitation/failure cue | 4.6) (6) How robust and generalizable is it under diverse environmental conditions? | p. 6 (4 EXPERIMENTS) |
| body limitation/failure cue | Bottom: real-world evaluation (General and Longhorizon Temporal), real-world robustness and generalization evaluation. | p. 7 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details We train on 8 NVIDIA A100 GPUs with PyTorch FSDP, using 32 samples per GPU for a global batch of 256 and ... | p. 6 (4 EXPERIMENTS) |
| Results are reported at the best validation step, and each task is evaluated with 24 trials to compute success rates. | p. 7 (4 EXPERIMENTS) |
| At inference we use DDIM (Song et al., 2020) with 10 sampling steps and a classifier-free guidance(CFG) (Ho & Salimans, 2022) guidance scale of ... | p. 6 (4 EXPERIMENTS) |
| The Fractal testbed includes 336 variants, yielding 2,856 trials in total. | p. 7 (4 EXPERIMENTS) |
| Standard 5 tasks are trained jointly for 20k steps, and validation is performed every 1k steps and results are reported at the best validation ... | p. 8 (4 EXPERIMENTS) |
| Training runs for approximately 5k-20k steps depending on the task and data size. | p. 9 (4 EXPERIMENTS) |
| Pick Diverse Fruits comprises five variants with 5 trials per variant (25 total); all other General tasks use 15 trials. | p. 9 (4 EXPERIMENTS) |
| The current RGB observation and language instruction are first encoded by a VLM into perceptual and cognitive tokens, forming a working memory, analogous to ... | p. 4 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 18 / Figure/Table caption - extractive body cue:** Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD variants for two representative tasks (Pick Place Order and ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick Coke Can and (b) Move Near tasks ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 7: Robustness and generalization under out-of-distribution (OOD) variants in simu- lation: Hinge-like object manipulation. (a) OOD variants of Open/Close Drawer and (b) Place Apple ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 11: Ablation on the Number of Cognitive Tokens. Increasing the number of cognitive tokens from 1 to 4 does not improve performance. A single ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4.6) (6) How robust and generalizable is it under diverse environmental conditions?
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Bottom: real-world evaluation (General and Longhorizon Temporal), real-world robustness and generalization evaluation.

- **Evidence anchors reviewed:** datasets p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), metrics p. 19 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), baselines p. 2 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 27 (Figure/Table caption), p. 28 (Figure/Table caption), p. 6 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), results p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 9 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
