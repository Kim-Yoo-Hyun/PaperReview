# Evaluation - MapDream: Task-Driven Map Learning for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IkXFH6alZN; PDF retrieval source: https://openreview.net/pdf/6e898fbe18f2ef7449852473b4a8ab53fd0fda57.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.1.2. METRICS), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET), p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET), p. 7 (4.5.2. REINFORCEMENT FINE-TUNING UNDER)): Across all settings, MapDream improves both success rate and path efficiency, which we attribute to its task-driven generative maps that are refined through two-stage optimization and reinforcement fine-tuning.

## Evaluation Body Digest

- **p. 8 / 4.6. Real-world Generalization - extractive body cue:** Notably, the model is trained only on the R2R-CE and RxR-CE simulators, yet transfers in a zeroshot manner to real-world, previously unseen indoor scenes.
- **p. 6 / 4.2.2. TRAINING DETAILS - extractive body cue:** Unseen-Dataset generalization performance on the RxRCE Val-Unseen split.
- **p. 5 / 4.1.1. EXPERIMENTAL ENVIRONMENTS - extractive body cue:** Results are reported on the validation-unseen splits to assess generalization to novel environments.
- **p. 8 / 4.6. Real-world Generalization - extractive body cue:** 4, MapDream generates task-driven maps that evolve with the robot's motion and encode navigationrelevant spatial affordances, allowing the robot to follow long-horizon language instructions successfully ...
- **p. 5 / 4.1.1. EXPERIMENTAL ENVIRONMENTS - extractive body cue:** We evaluate our method on the widely adopted continuousenvironment VLN benchmarks R2R-CE (Krantz et al., 2020) and RxR-CE (Ku et al., 2020).
- **p. 6 / 4.2.2. TRAINING DETAILS - extractive body cue:** Comparison of different methods on the R2R-CE Val-Unseen and RxR-CE Val-Unseen splits.
- **p. 7 / 4.4. Qualitative Analysis - extractive body cue:** These results indicate that the learned maps serve as effective abstractions of the environment, supporting accurate navigation without requiring full scene reconstruction.
- **p. 7 / 4.5.1. TWO-STAGE TRAINING - extractive body cue:** Effect of staged learning on R2R-CE val-unseen.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experiment Setup (p. 5); 4.1.1. EXPERIMENTAL ENVIRONMENTS (p. 5); 4.2. Implementation Details (p. 5); 4.2.1. DATASET COLLECTION (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Comparison with State-of-the-Art Methods | EMPIRICAL / REAL-ROBOT OR HARDWARE | Across all settings, MapDream improves both success rate and path efficiency, which we attribute to its task-driven generative maps that are refined through two-stage ... | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| 4.1.2. METRICS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We adopt the standard VLN evaluation protocol (Krantz et al., 2020; Ku et al., 2020) to assess navigation performance using success rate (SR), oracle ... | p. 5 (4.1.2. METRICS) |
| 4.3. Comparison with State-of-the-Art Methods | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, MapDream achieves the best overall performance among monocular approaches on both datasets, with the highest SR and SPL while ... | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| 4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 5, increasing map size improves reconstruction fidelity but brings only marginal gains in navigation performance. | p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET) |
| 4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, the most compact configuration attains a comparable success rate to the largest model (42.2 vs. | p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET) |

## Dataset / Benchmark Role

- **p. 8 / 4.6. Real-world Generalization - extractive body cue:** Notably, the model is trained only on the R2R-CE and RxR-CE simulators, yet transfers in a zeroshot manner to real-world, previously unseen indoor scenes.
- **p. 6 / 4.2.2. TRAINING DETAILS - extractive body cue:** Unseen-Dataset generalization performance on the RxRCE Val-Unseen split.
- **p. 5 / 4.1.1. EXPERIMENTAL ENVIRONMENTS - extractive body cue:** Results are reported on the validation-unseen splits to assess generalization to novel environments.
- **p. 8 / 4.6. Real-world Generalization - extractive body cue:** 4, MapDream generates task-driven maps that evolve with the robot's motion and encode navigationrelevant spatial affordances, allowing the robot to follow long-horizon language instructions successfully ...
- **p. 5 / 4.1.1. EXPERIMENTAL ENVIRONMENTS - extractive body cue:** We evaluate our method on the widely adopted continuousenvironment VLN benchmarks R2R-CE (Krantz et al., 2020) and RxR-CE (Ku et al., 2020).
- **p. 6 / 4.2.2. TRAINING DETAILS - extractive body cue:** Comparison of different methods on the R2R-CE Val-Unseen and RxR-CE Val-Unseen splits.
- **p. 7 / 4.4. Qualitative Analysis - extractive body cue:** These results indicate that the learned maps serve as effective abstractions of the environment, supporting accurate navigation without requiring full scene reconstruction.
- **p. 7 / 4.5.1. TWO-STAGE TRAINING - extractive body cue:** Effect of staged learning on R2R-CE val-unseen.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Map-in-the-Loop Architecture. Unlike previous ap- proaches that either omit maps or rely on expert-designed represen- tations, MapDream adopts a map-in-the-loop design that learns ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the MapDream Framework. The diagram shows the two-stage optimization of MapDream. Stage 1 learns structured task-driven maps from visual observations and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison of different methods on the R2R-CE Val-Unseen and RxR-CE Val-Unseen splits. Observations used include single RGB camera (S.RGB), depth sensor (Depth), panoramic ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Unseen-Dataset generalization performance on the RxR- CE Val-Unseen split. All results are obtained only training on the R2R-CE training set.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative navigation example illustrating the effect of task-driven maps in MapDream. (Left) Trajectory comparison shows that MapDream (green) closely follows the ground-truth path ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Effect of staged learning on R2R-CE val-unseen. Map SPT RFT NE↓ OSR↑ SR↑ SPL↑
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Effect of Reinforcement Fine-tuning under Different Channel Initializations. Channel SPT RFT NE↓ OSR↑ SR↑
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Effect of BEV token capacity on R2R-CE val-unseen. Resolution Tokens NE ↓ OSR ↑ SR ↑ SPL ↑ Time(s)

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Notably, the model is trained only on the R2R-CE and RxR-CE simulators, yet transfers in a zeroshot manner to real-world, previously unseen indoor scenes. | embodiment, simulator version and control stack | p. 8 (4.6. Real-world Generalization), p. 6 (4.2.2. TRAINING DETAILS) |
| Task/environment | Unseen-Dataset generalization performance on the RxRCE Val-Unseen split. | reset, timeout, object/scene variation | p. 6 (4.2.2. TRAINING DETAILS), p. 5 (4.1.1. EXPERIMENTAL ENVIRONMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3.1. Overview) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (1. Introduction), p. 4 (3.3.2. PRE-TRAINING THE MAP MODULE) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We adopt the standard VLN evaluation protocol (Krantz et al., 2020; Ku et al., 2020) to assess navigation performance using success rate (SR), oracle ... | definition/direction/unit from same section | p. 5 (4.1.2. METRICS) |
| As shown in Table 1, MapDream achieves the best overall performance among monocular approaches on both datasets, with the highest SR and SPL while ... | definition/direction/unit from same section | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| Across all settings, MapDream improves both success rate and path efficiency, which we attribute to its task-driven generative maps that are refined through two-stage ... | definition/direction/unit from same section | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| Notably, the most compact configuration attains a comparable success rate to the largest model (42.2 vs. | definition/direction/unit from same section | p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET) |
| This highlights a favorable accuracy-efficiency tradeoff and suggests that MapDream naturally operates in a low-resolution, low-token regime without sacrificing navigation performance. | definition/direction/unit from same section | p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET) |
| We primarily report SR and SPL, which capture task completion and path efficiency, respectively. | definition/direction/unit from same section | p. 5 (4.1.2. METRICS) |
| Reinforcement learning consistently improves all variants, with SR gains of +3.4 (All), +5.5 (Distance), +4.1 (Landmark), and +4.2 (Occupancy), accompanied by increases in SPL ... | definition/direction/unit from same section | p. 7 (4.5.2. REINFORCEMENT FINE-TUNING UNDER) |
| We conduct three ablation studies on R2R-CE that jointly probe MapDream along complementary design dimensions: optimization strategy, robustness to map initialization, and representation capacity. | definition/direction/unit from same section | p. 7 (4.5. Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We evaluate the effect of two-stage training in MapDream by comparing three configurations: a baseline VLN policy without maps, the map-conditioned model after Stage ... | comparison identity and matched condition | p. 7 (4.5.1. TWO-STAGE TRAINING) |
| Additionally, we generate 500K non-oracle samples through exploratory rollouts in the training environments, improving robustness to outof-distribution states and enhancing generalization across diverse scenarios. | comparison identity and matched condition | p. 5 (4.2.1. DATASET COLLECTION) |
| We adopt the standard VLN evaluation protocol (Krantz et al., 2020; Ku et al., 2020) to assess navigation performance using success rate (SR), oracle ... | comparison identity and matched condition | p. 5 (4.1.2. METRICS) |
| The policy is initialized from pretrained NVILA-2B weights and trained with a mixture of oracle expert trajectories and DAgger-collected data. | comparison identity and matched condition | p. 6 (4.2.2. TRAINING DETAILS) |
| We compare MapDream with state-of-the-art methods on the R2R-CE and RxR-CE benchmarks under a single RGB camera (monocular) observation setting. | comparison identity and matched condition | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| Introducing Stage 1 yields consistent improvements across all metrics over the baseline, demonstrating that generative task-driven maps provide useful spatial abstractions for instruction-following navigation. | comparison identity and matched condition | p. 7 (4.5.1. TWO-STAGE TRAINING) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We evaluate the effect of two-stage training in MapDream by comparing three configurations: a baseline VLN policy without maps, the map-conditioned model after Stage ... | component/input/data sensitivity | p. 7 (4.5.1. TWO-STAGE TRAINING) |
| Concretely, we analyze the effect of two-stage training, the sensitivity of reinforcement finetuning to different channel initializations, and the trade-off between BEV map compactness ... | component/input/data sensitivity | p. 7 (4.5. Ablation Study) |
| MapDream: Task-Driven Map Learning for Vision-Language Navigation performance after supervised pretraining, reinforcement fine-tuning narrows these gaps, bringing all variants to similar final SR (43.6-45.6) ... | component/input/data sensitivity | p. 8 (4.5.2. REINFORCEMENT FINE-TUNING UNDER) |
| Effect of Reinforcement Fine-tuning under Different Channel Initializations. | component/input/data sensitivity | p. 8 (4.5.2. REINFORCEMENT FINE-TUNING UNDER) |
| Observations used include single RGB camera (S.RGB), depth sensor (Depth), panoramic view (Pano.) and map representation (Map). † indicates methods without using LLMs. | component/input/data sensitivity | p. 6 (4.2.2. TRAINING DETAILS) |
| Stage 1 performs supervised pre-training of both the map module and the VLN policy, while Stage 2 jointly fine-tunes them with reinforcement learning. | component/input/data sensitivity | p. 5 (4.2.2. TRAINING DETAILS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are: • We first introduce a task-driven perspective on map representations for VLN, reframing maps as representations shaped by downstream navigation ... | Across all settings, MapDream improves both success rate and path efficiency, which we attribute to its task-driven generative maps that are refined through two-stage ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.1.2. METRICS), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET), p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET), p. 7 (4.5.2. REINFORCEMENT FINE-TUNING UNDER) |
| Primary metric/result | We adopt the standard VLN evaluation protocol (Krantz et al., 2020; Ku et al., 2020) to assess navigation performance using success rate (SR), oracle ... | numeric claim only at cited anchor | p. 5 (4.1.2. METRICS) |

- Numeric sentences retained from the body:
- **p. 5 / 4.2.2. TRAINING DETAILS - extractive body cue:** Stage 1 runs for two epochs and takes approximately 60 hours, and Stage 2 performs 2000 RL steps and takes approximately 10 hours.
- **p. 6 / 4.2.2. TRAINING DETAILS - extractive body cue:** The model is trained for 2000 steps with a learning rate of 1 × 10-6, jointly fine-tuning both the map module and the VLN policy.
- **p. 8 / 4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET - extractive body cue:** In particular, inference latency per decision step drops from 12.7 s to 1.3 s, making compact maps far more suitable for real-time continuous control.
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** It is defined as: ract = N-1 X i=0 iY j=0 1[at+j = a∗ t+j].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We focus on the continuous-environment (CE) protocol because continuous control introduces fine motion granularity and realistic noise, making navigation sensitive to small geometric deviations. | p. 5 (4.1.1. EXPERIMENTAL ENVIRONMENTS) |
| body limitation/failure cue | Additionally, we generate 500K non-oracle samples through exploratory rollouts in the training environments, improving robustness to outof-distribution states and enhancing generalization across diverse scenarios. | p. 5 (4.2.1. DATASET COLLECTION) |
| body limitation/failure cue | These results empirically validate that learning spatial abstractions under navigation objectives leads to more robust decision making in continuous environments. | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| body limitation/failure cue | We conduct three ablation studies on R2R-CE that jointly probe MapDream along complementary design dimensions: optimization strategy, robustness to map initialization, and representation capacity. | p. 7 (4.5. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Janus-Pro is trained for one epoch with a batch size of 40 and a learning rate of 1 × 10-4 in a supervised pre-training ... | p. 5 (4.2.2. TRAINING DETAILS) |
| The model is trained for 2000 steps with a learning rate of 1 × 10-6, jointly fine-tuning both the map module and the VLN ... | p. 6 (4.2.2. TRAINING DETAILS) |
| We optimize the policy with cross-entropy loss over the next three predicted action steps at each time step using a learning rate of 1 ... | p. 6 (4.2.2. TRAINING DETAILS) |
| Stage 1 runs for two epochs and takes approximately 60 hours, and Stage 2 performs 2000 RL steps and takes approximately 10 hours. | p. 5 (4.2.2. TRAINING DETAILS) |
| MapDream: Task-Driven Map Learning for Vision-Language Navigation Instruction: Go through the dining room and up the steps. | p. 7 (4.3. Comparison with State-of-the-Art Methods) |
| 4, MapDream generates task-driven maps that evolve with the robot's motion and encode navigationrelevant spatial affordances, allowing the robot to follow long-horizon language instructions ... | p. 8 (4.6. Real-world Generalization) |
| We adopt lightweight ground-truth map signals during supervised pre-training to encode navigation-critical cues; this design is not exclusive, and alternative compact variants are possible. | p. 4 (3.3.1. MAP SUPERVISION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.1.1. EXPERIMENTAL ENVIRONMENTS - extractive body cue:** We focus on the continuous-environment (CE) protocol because continuous control introduces fine motion granularity and realistic noise, making navigation sensitive to small geometric deviations.
- **p. 5 / 4.2.1. DATASET COLLECTION - extractive body cue:** Additionally, we generate 500K non-oracle samples through exploratory rollouts in the training environments, improving robustness to outof-distribution states and enhancing generalization across diverse scenarios.
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive body cue:** These results empirically validate that learning spatial abstractions under navigation objectives leads to more robust decision making in continuous environments.
- **p. 7 / 4.5. Ablation Study - extractive body cue:** We conduct three ablation studies on R2R-CE that jointly probe MapDream along complementary design dimensions: optimization strategy, robustness to map initialization, and representation capacity.

- **Evidence anchors reviewed:** datasets p. 8 (4.6. Real-world Generalization), p. 6 (4.2.2. TRAINING DETAILS), p. 5 (4.1.1. EXPERIMENTAL ENVIRONMENTS), p. 8 (4.6. Real-world Generalization), p. 5 (4.1.1. EXPERIMENTAL ENVIRONMENTS), p. 6 (4.2.2. TRAINING DETAILS), metrics p. 5 (4.1.2. METRICS), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET), p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET), p. 5 (4.1.2. METRICS), baselines p. 7 (4.5.1. TWO-STAGE TRAINING), p. 5 (4.2.1. DATASET COLLECTION), p. 5 (4.1.2. METRICS), p. 6 (4.2.2. TRAINING DETAILS), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 7 (4.5.1. TWO-STAGE TRAINING), results p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.1.2. METRICS), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET), p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET), p. 7 (4.5.2. REINFORCEMENT FINE-TUNING UNDER).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
