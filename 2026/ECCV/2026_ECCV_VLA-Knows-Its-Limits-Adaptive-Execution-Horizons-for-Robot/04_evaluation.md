# Evaluation - VLA Knows Its Limits: Adaptive Execution Horizons for Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.21445; PDF retrieval source: https://arxiv.org/pdf/2602.21445. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.2. Simulation Results), p. 1 (Figure/Table caption)): 8, and find that AutoHorizon consistently achieves higher success rates.

## Evaluation Body Digest

- **p. 7 / 4.2. Simulation Results - extractive PDF cue:** Our experiments leverage two benchmark datasets: the LIBERO dataset [20], which offers a diverse suite of single-arm manipulation tasks, and the RoboTwin dataset [7, 23], ...
- **p. 7 / 4.2. Simulation Results - extractive PDF cue:** 3 presents the results on the RoboTwin benchmark across tasks with varying difficulty.
- **p. 8 / 4.3. Real-World Results - extractive PDF cue:** We further evaluate AutoHorizon in real-world robotic manipulation scenarios.
- **p. 8 / 4.3. Real-World Results - extractive PDF cue:** Performance comparison on real-world tasks.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** It serves as a strong yet costly baseline, as it requires p rollouts per task.
- **p. 8 / 4.2. Simulation Results - extractive PDF cue:** 8, and find that AutoHorizon consistently achieves higher success rates.
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 7. Average success rates on the LIBERO benchmark with a prediction horizon of 10 using π0.5. Fig. 7 reports results under a shorter prediction ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Illustration of the average success rates on the LIBERO benchmark using π0.5. Varying the execution horizon leads to substantial success rate fluctuations, and ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Settings (p. 6); 4.2. Simulation Results (p. 7); 4.3. Real-World Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 8, and find that AutoHorizon consistently achieves higher success rates. | p. 8 (4.2. Simulation Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7. Average success rates on the LIBERO benchmark with a prediction horizon of 10 using π0.5. Fig. 7 reports results under a shorter ... | p. 13 (Figure/Table caption) |
| 4.2. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The enhanced Static Oracle+ consistently achieves strong results, and the specific horizon values used for this baseline are listed in Sec. | p. 7 (4.2. Simulation Results) |
| 4.2. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method consistently achieves superior results, demonstrating robustness and generalization across different architectures and training regimes. | p. 7 (4.2. Simulation Results) |
| 4.2. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating robustness to hyperparameter choices. | p. 8 (4.2. Simulation Results) |

## Dataset / Benchmark Role

- **p. 7 / 4.2. Simulation Results - extractive PDF cue:** Our experiments leverage two benchmark datasets: the LIBERO dataset [20], which offers a diverse suite of single-arm manipulation tasks, and the RoboTwin dataset [7, 23], ...
- **p. 7 / 4.2. Simulation Results - extractive PDF cue:** 3 presents the results on the RoboTwin benchmark across tasks with varying difficulty.
- **p. 8 / 4.3. Real-World Results - extractive PDF cue:** We further evaluate AutoHorizon in real-world robotic manipulation scenarios.
- **p. 8 / 4.3. Real-World Results - extractive PDF cue:** Performance comparison on real-world tasks.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** It serves as a strong yet costly baseline, as it requires p rollouts per task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Illustration of the average success rates on the LIBERO benchmark using π0.5. Varying the execution horizon leads to substantial success rate fluctuations, and ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Left: (a) In conventional action chunking, the execution horizon e is heuristically chosen by humans and remains fixed across chunks. (b) In contrast, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Visualization of average attention weights in π0.5 across different stages of task execution. Intra-chunk actions consistently attend to the same vision and language ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of normalized action self-attention weights. Across different prediction horizons, the predicted ac- tions exhibit strong attention to the initial and terminal action ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Performance comparison of π0.5 on LIBERO benchmark under different prediction horizons. Best results are in bold. Setting p = 10 p = 50 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Performance comparison using GR00T N1.5 on the LIBERO benchmark. Best results are highlighted in bold. Task Suite LIB-Spatial LIB-Object LIB-Goal LIB-10 Static
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Estimated execution horizon distributions by Auto- Horizon. The legend displays the mean values of the distributions. as the execution horizon extends, while the ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Performance comparison using π0.5 on the RoboTwin tasks. Best results are highlighted in bold. Task Suite Adjust Bottle Pick Bottles Place Container Stack ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our experiments leverage two benchmark datasets: the LIBERO dataset [20], which offers a diverse suite of single-arm manipulation tasks, and the RoboTwin dataset [7, ... | embodiment, simulator version and control stack | p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results) |
| Task/environment | 3 presents the results on the RoboTwin benchmark across tasks with varying difficulty. | reset, timeout, object/scene variation | p. 7 (4.2. Simulation Results), p. 8 (4.3. Real-World Results) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1. Introduction), p. 5 (3.3. VLA Knows Its Limits) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 8, and find that AutoHorizon consistently achieves higher success rates. | definition/direction/unit from same section | p. 8 (4.2. Simulation Results) |
| Figure 7. Average success rates on the LIBERO benchmark with a prediction horizon of 10 using π0.5. Fig. 7 reports results under a shorter ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Figure 1. Illustration of the average success rates on the LIBERO benchmark using π0.5. Varying the execution horizon leads to substantial success rate fluctuations, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| When the execution horizon becomes excessively long (e > 40), the robot struggles to maintain accurate object localization, leading to frequent object drops and ... | definition/direction/unit from same section | p. 8 (4.3. Real-World Results) |
| For all experiments, we report both the mean and standard deviation to ensure fair comparison and robust evaluation. | definition/direction/unit from same section | p. 7 (4.1. Experimental Settings) |
| AutoHorizon operates on the first or third sampling step and typically uses fixed hyperparameters of q = 0.9 and τ = 0.3, requiring no ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| An enhanced version of Static Oracle that performs brute-force search over the prediction horizon, thereby achieving optimal performance under fixed horizon settings. | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| Performance comparison using GR00T N1.5 on the LIBERO benchmark. | definition/direction/unit from same section | p. 7 (4.1. Experimental Settings) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating robustness to hyperparameter choices. | comparison identity and matched condition | p. 8 (4.2. Simulation Results) |
| We compare against the following baselines: • Static Oracle. | comparison identity and matched condition | p. 6 (4.1. Experimental Settings) |
| Across both horizon configurations, AutoHorizon consistently outperforms all baselines. | comparison identity and matched condition | p. 7 (4.2. Simulation Results) |
| The enhanced Static Oracle+ consistently achieves strong results, and the specific horizon values used for this baseline are listed in Sec. | comparison identity and matched condition | p. 7 (4.2. Simulation Results) |
| It serves as a strong yet costly baseline, as it requires p rollouts per task. | comparison identity and matched condition | p. 6 (4.1. Experimental Settings) |
| We further compare with a variation of Static Oracle using fixed horizons closest to AutoHorizon's mean estimated values (e.g., e = 14 and e ... | comparison identity and matched condition | p. 8 (4.2. Simulation Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Task Suite LIB-Spatial LIB-Object LIB-Goal LIB-10 Static Oracle e = 1 92.7 ± 0.9 94.7 ± 3.4 82.7 ± 0.9 74.7 ± 3.4 e ... | component/input/data sensitivity | p. 7 (4.1. Experimental Settings) |
| We also examine the effect of hyperparameters in Sec. | component/input/data sensitivity | p. 8 (4.2. Simulation Results) |
| For π0.5, we conduct experiments with two variants using prediction horizons of p = 10 and p = 50 to examine horizon-dependent behavior. | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |
| Table 8. Effect of language tokens on LIBERO benchmark. Task Suite LIB-Spatial LIB-Object LIB-Goal LIB-10 p = 10 e = 10 | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 9. Hyper-parameter sensitivity analysis. L = 2 L = 3 L = 4 L = 5 L = 6 89.9±1.2 92.1±1.0 | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| For GR00T N1.5, we adopt the publicly released pretrained checkpoints with the default prediction horizon of p = 16. | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the ... | 8, and find that AutoHorizon consistently achieves higher success rates. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.2. Simulation Results), p. 1 (Figure/Table caption) |
| Primary metric/result | Figure 7. Average success rates on the LIBERO benchmark with a prediction horizon of 10 using π0.5. Fig. 7 reports results under a shorter ... | numeric claim only at cited anchor | p. 13 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 4.1. Experimental Settings - extractive PDF cue:** Task Suite LIB-Spatial LIB-Object LIB-Goal LIB-10 Static Oracle e = 1 92.7 ± 0.9 94.7 ± 3.4 82.7 ± 0.9 74.7 ± 3.4 e = ...
- **p. 7 / 4.2. Simulation Results - extractive PDF cue:** Each task is executed for 100 trials.
- **p. 7 / 4.2. Simulation Results - extractive PDF cue:** The performance of Static Oracle first rises and then declines LIB-Spatial LIB-Object LIB-Goal LIB-10 10 15 20 25 30 35 Horizon Value Spatial: 13.48 Object: ...
- **p. 8 / 4.2. Simulation Results - extractive PDF cue:** Task Suite Adjust Bottle Pick Bottles Place Container Stack Bowls Place Cup Open Laptop Press Stapler Static Oracle e = 0.2p 79.0 ± 1.4 40.7 ...
- **p. 8 / 4.3. Real-World Results - extractive PDF cue:** Experiments are conducted on a Franka Research 3 robot (7-DoF arm) [10] following the DROID experimental setup [15].
- **p. 8 / 4.3. Real-World Results - extractive PDF cue:** A total of 150 trajectories are collected for model finetuning.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7 | p. 7 (4.2. Simulation Results) |
| body limitation/failure cue | For all experiments, we report both the mean and standard deviation to ensure fair comparison and robust evaluation. | p. 7 (4.1. Experimental Settings) |
| body limitation/failure cue | Object positions and orientations are randomized across trials to ensure robustness and generalization. | p. 8 (4.3. Real-World Results) |
| body limitation/failure cue | Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating robustness to hyperparameter choices. | p. 8 (4.2. Simulation Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each task is evaluated over ten trials per setting, with each trial capped at 300 control steps, amounting to approximately three hours of total ... | p. 8 (4.3. Real-World Results) |
| For GR00T N1.5, we adopt the publicly released pretrained checkpoints with the default prediction horizon of p = 16. | p. 6 (4.1. Experimental Settings) |
| AutoHorizon operates on the first or third sampling step and typically uses fixed hyperparameters of q = 0.9 and τ = 0.3, requiring no ... | p. 6 (4.1. Experimental Settings) |
| We also examine the effect of hyperparameters in Sec. | p. 8 (4.2. Simulation Results) |
| Let Tv, Tl, and Ta denote the number of encoded vision, language, and action tokens within the VLA respectively. | p. 3 (3.1. Preliminary) |
| This invariance is consistently observed across different sampling steps, task rollouts, and pretrained models. | p. 4 (3.1. Preliminary) |
| We also observe an unusually high concentration of attention on the first language token, a phenomenon that persists across all transformer blocks and sampling ... | p. 5 (3.3. VLA Knows Its Limits) |
| However, unlike in LLMs, where sink tokens often encode structural or positional information, the language attention sink in VLAs appears largely redundant and carries ... | p. 5 (3.3. VLA Knows Its Limits) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Simulation Results - extractive PDF cue:** Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7
- **p. 7 / 4.1. Experimental Settings - extractive PDF cue:** For all experiments, we report both the mean and standard deviation to ensure fair comparison and robust evaluation.
- **p. 8 / 4.3. Real-World Results - extractive PDF cue:** Object positions and orientations are randomized across trials to ensure robustness and generalization.
- **p. 8 / 4.2. Simulation Results - extractive PDF cue:** Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating robustness to hyperparameter choices.

- **PDF anchors reviewed:** datasets p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.3. Real-World Results), p. 8 (4.3. Real-World Results), p. 6 (4.1. Experimental Settings), metrics p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption), p. 1 (Figure/Table caption), p. 8 (4.3. Real-World Results), p. 7 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), baselines p. 8 (4.2. Simulation Results), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 6 (4.1. Experimental Settings), p. 8 (4.2. Simulation Results), results p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.2. Simulation Results), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
