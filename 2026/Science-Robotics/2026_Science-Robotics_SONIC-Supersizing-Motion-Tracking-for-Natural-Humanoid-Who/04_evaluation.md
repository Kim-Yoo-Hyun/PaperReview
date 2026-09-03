# Evaluation - SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/dair/publication/sonic2026/; PDF retrieval source: https://research.nvidia.com/labs/dair/publication/sonic2026/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 19 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking), p. 9 (2.5. Foundation-Model-Driven Loco-manipulation), p. 11 (2.5. Foundation-Model-Driven Loco-manipulation)): Table 3: Ablation studies. SR denotes success rate. Each entry reports a single evaluation per configuration on the full test split (descriptive; no statistical test applied). (A) FSQ outperforms VQ-VAE ...

## Evaluation Body Digest

- **p. 13 / 3.1. Humanoid Motion Dataset - extractive body cue:** 14,513 701 253 Dance 9,689 504 485 Injured 9,386 1,167 528 Action / Tool use 9,920 228 322 Others (10+ main cat.) 63,583 429 890 ...
- **p. 3 / 2.1. Motion Tracking - extractive body cue:** From our motion-capture dataset, we constructed two held-out splits.
- **p. 5 / 2.1. Motion Tracking - extractive body cue:** This comparison primarily reflects cross-dataset generalization and scaling effects rather than a fully data-matched benchmark, as the baselines were trained on different source data and ...
- **p. 3 / 2.1. Motion Tracking - extractive body cue:** In this section, we evaluated the generalization capabilities of our tracker on large-scale, unseen motion datasets in simulation and the real world.
- **p. 12 / 2.6. Discussion - extractive body cue:** We observe consistent improvements as data, model capacity, and compute increase, with generalization to unseen motions in simulation and real-world deployments.
- **p. 13 / 3.1. Humanoid Motion Dataset - extractive body cue:** The dataset spans 33 motion categories (Tab.
- **p. 5 / 2.1. Motion Tracking - extractive body cue:** The real-world policy achieved 99.2% success rate compared to 100% in simulation, with an overall MPJPE-L of 25.7 mm (vs.
- **p. 6 / 2.2. Interactive Motion Control - extractive body cue:** SONIC enabled much more fluid, responsive, and natural motion generation, retaining the robot's full freedom of movement throughout the task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 2. Results (p. 3); 3.1. Humanoid Motion Dataset (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Ablation studies. SR denotes success rate. Each entry reports a single evaluation per configuration on the full test split (descriptive; no statistical ... | p. 19 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2: Scaling and benchmarking of SONIC for universal motion tracking. (A to C) Effect of scaling data size, model size, and compute on ... | p. 4 (Figure/Table caption) |
| 2.1. Motion Tracking | EMPIRICAL / REAL-ROBOT OR HARDWARE | Scaling yielded consistent improvements on both test-content (out-of-distribution, OOD) and test-repetition: the largest model achieved 99.6% success with 23.8 mm MPJPE-L on test-content, compared ... | p. 5 (2.1. Motion Tracking) |
| 2.1. Motion Tracking | EMPIRICAL / REAL-ROBOT OR HARDWARE | The real-world policy achieved 99.2% success rate compared to 100% in simulation, with an overall MPJPE-L of 25.7 mm (vs. | p. 5 (2.1. Motion Tracking) |
| 2.5. Foundation-Model-Driven Loco-manipulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Trained on 200 trajectories, the policy achieved 70% success. | p. 9 (2.5. Foundation-Model-Driven Loco-manipulation) |

## Dataset / Benchmark Role

- **p. 13 / 3.1. Humanoid Motion Dataset - extractive body cue:** 14,513 701 253 Dance 9,689 504 485 Injured 9,386 1,167 528 Action / Tool use 9,920 228 322 Others (10+ main cat.) 63,583 429 890 ...
- **p. 3 / 2.1. Motion Tracking - extractive body cue:** From our motion-capture dataset, we constructed two held-out splits.
- **p. 5 / 2.1. Motion Tracking - extractive body cue:** This comparison primarily reflects cross-dataset generalization and scaling effects rather than a fully data-matched benchmark, as the baselines were trained on different source data and ...
- **p. 3 / 2.1. Motion Tracking - extractive body cue:** In this section, we evaluated the generalization capabilities of our tracker on large-scale, unseen motion datasets in simulation and the real world.
- **p. 12 / 2.6. Discussion - extractive body cue:** We observe consistent improvements as data, model capacity, and compute increase, with generalization to unseen motions in simulation and real-world deployments.
- **p. 13 / 3.1. Humanoid Motion Dataset - extractive body cue:** The dataset spans 33 motion categories (Tab.
- **p. 5 / 2.1. Motion Tracking - extractive body cue:** The real-world policy achieved 99.2% success rate compared to 100% in simulation, with an overall MPJPE-L of 25.7 mm (vs.
- **p. 6 / 2.2. Interactive Motion Control - extractive body cue:** SONIC enabled much more fluid, responsive, and natural motion generation, retaining the robot's full freedom of movement throughout the task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: SONIC enables diverse humanoid tasks through a universal control policy that handles diverse input modalities and control interfaces. [17], and CALM [18] provide ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Scaling and benchmarking of SONIC for universal motion tracking. (A to C) Effect of scaling data size, model size, and compute on test-content ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Interactive whole-body control with SONIC. A single universal control policy, driven by the real-time kinematic planner, executes diverse user-commanded behaviors on the Unitree ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Multi-modal, real-time control with SONIC. A single universal control policy is driven by heteroge- neous input modalities. (A) Video teleoperation: full-body motion is ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: VLA-driven loco-manipulation tasks. Each row shows a temporally ordered sequence of frames (time proceeds left to right). (A) Apple-to-plate pick-and-place via the 3-point ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: Vision-language-action (VLA) control through the universal token interface. (A) Task success rates. A GR00T N1.5 model, fine-tuned on teleoperated data, is evaluated across ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 2: Dataset split statistics and main/sub-category distribution. Each main category (such as Locomotion and Dance) contains many sub-categories describing specific motion types (such as ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 6: SONIC enables universal humanoid motion tracking through a universal control policy that handles diverse motion commands and modalities. Specialized encoders process robot, human, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 14,513 701 253 Dance 9,689 504 485 Injured 9,386 1,167 528 Action / Tool use 9,920 228 322 Others (10+ main cat.) 63,583 429 ... | embodiment, simulator version and control stack | p. 13 (3.1. Humanoid Motion Dataset), p. 3 (2.1. Motion Tracking) |
| Task/environment | From our motion-capture dataset, we constructed two held-out splits. | reset, timeout, object/scene variation | p. 3 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 15 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 16 (3.3. Generative Kinematic Motion Planner), p. 16 (3.2. Universal Humanoid Motion Tracking) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (m/s) (H) Commanded vs Achieved Ideal OpenHomie SONIC 0 1 2 3 4 5 Commanded Velocity (m/s) 0 20 40 60 80 100 Survival ... | definition/direction/unit from same section | p. 4 (2.1. Motion Tracking) |
| (D to G) Comparison with baselines on test-content, test-repetition, and PHUMA [43] (𝑁=7,016, 9,395, and 68,326 motions): (D) success rate (SONIC vs. each baseline, ... | definition/direction/unit from same section | p. 4 (2.1. Motion Tracking) |
| (B) Action-space ablation: task completion success rate using universal motion tokens vs. explicit SMPL poses. | definition/direction/unit from same section | p. 11 (2.5. Foundation-Model-Driven Loco-manipulation) |
| The primary measure was the success rate (Succ), where a motion imitation was deemed unsuccessful if the humanoid deviated too far from the reference ... | definition/direction/unit from same section | p. 3 (2.1. Motion Tracking) |
| The real-world policy achieved 99.2% success rate compared to 100% in simulation, with an overall MPJPE-L of 25.7 mm (vs. | definition/direction/unit from same section | p. 5 (2.1. Motion Tracking) |
| The 97.2% success rate on PHUMA is particularly notable because PHUMA aggregates motions from video-based pose estimation with a different retargeting pipeline [43], making ... | definition/direction/unit from same section | p. 5 (2.1. Motion Tracking) |
| All success rates are strict binary outcomes over 10-20 trials per task (Tab. | definition/direction/unit from same section | p. 9 (2.5. Foundation-Model-Driven Loco-manipulation) |
| (A) VLA task success rates (universal motion token action space) Task Interface Training Data Trials Success Apple to plate 3-point 300 trajs (single-obj) 20 ... | definition/direction/unit from same section | p. 11 (2.5. Foundation-Model-Driven Loco-manipulation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared against state-of-the-art trackers: GMT [33], Any2Track [30], and BeyondMimic [29]. | comparison identity and matched condition | p. 5 (2.1. Motion Tracking) |
| To show that a universal tracker can match or exceed specialist controllers, we compared SONIC against OpenHomie [13], a state-of-the-art single-task locomotion controller optimized ... | comparison identity and matched condition | p. 5 (2.1. Motion Tracking) |
| For baseline comparisons, we additionally evaluated on PHUMA [43], a publicly available dataset of 3 | comparison identity and matched condition | p. 3 (2.1. Motion Tracking) |
| (D to G) Comparison with baselines on test-content, test-repetition, and PHUMA [43] (𝑁=7,016, 9,395, and 68,326 motions): (D) success rate (SONIC vs. each baseline, ... | comparison identity and matched condition | p. 4 (2.1. Motion Tracking) |
| (m/s) (H) Commanded vs Achieved Ideal OpenHomie SONIC 0 1 2 3 4 5 Commanded Velocity (m/s) 0 20 40 60 80 100 Survival ... | comparison identity and matched condition | p. 4 (2.1. Motion Tracking) |
| Unpaired comparisons used Welch's two-sided 𝑡-test (unequal variances): scaling effects were assessed between the smallest and largest configuration on each axis, and success and ... | comparison identity and matched condition | p. 19 (3.7. Statistical Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 1: Vision-language-action (VLA) control through the universal token interface. (A) Task success rates. A GR00T N1.5 model, fine-tuned on teleoperated data, is evaluated ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |
| Ablation tables report a single evaluation per configuration and are therefore descriptive. | component/input/data sensitivity | p. 19 (3.7. Statistical Analysis) |
| (A to C) Effect of scaling data size, model size, and compute on test-content (unseen motion content, OOD) and test-repetition (held-out takes of seen ... | component/input/data sensitivity | p. 4 (2.1. Motion Tracking) |
| Utilizing the scalable nature of SONIC, we noted that all the applications above were specified after training, without retraining the planner or the tracking ... | component/input/data sensitivity | p. 6 (2.2. Interactive Motion Control) |
| Human motion was estimated at ≥60 frames per second (fps), enabling interactive teleoperation without specialized motion-capture hardware. | component/input/data sensitivity | p. 9 (2.3. Video Teleoperation and Multi-Modal Control) |
| We observed that predicting universal tokens produced smoother and safer behavior than predicting explicit SMPL poses, which resulted in jerky motions and poor directional ... | component/input/data sensitivity | p. 9 (2.5. Foundation-Model-Driven Loco-manipulation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose Supersizing mOtion tracking for Natural humanoId Control (SONIC), a framework that enables natural humanoid control across a wide range of applications (Movie ... | Table 3: Ablation studies. SR denotes success rate. Each entry reports a single evaluation per configuration on the full test split (descriptive; no statistical ... | PDF body cue; verify exact table/figure and matched conditions | p. 19 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking), p. 9 (2.5. Foundation-Model-Driven Loco-manipulation), p. 11 (2.5. Foundation-Model-Driven Loco-manipulation) |
| Primary metric/result | Figure 2: Scaling and benchmarking of SONIC for universal motion tracking. (A to C) Effect of scaling data size, model size, and compute on ... | numeric claim only at cited anchor | p. 4 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 3 / 2.1. Motion Tracking - extractive body cue:** SONIC, trained on 100 million frames of motion over 21k GPU hours (128 GPUs over 7 days), exhibited strong generalization to unseen motions.
- **p. 3 / 2.1. Motion Tracking - extractive body cue:** The first, test-content (7,016 clips, 15 hours), evaluated generalization to unseen motion content and contained 182 sub-categories entirely absent from training.
- **p. 3 / 2.1. Motion Tracking - extractive body cue:** The second, testrepetition (9,395 clips, 12 hours), evaluated robustness to new performances and repetitions of known motion types.
- **p. 4 / 2.1. Motion Tracking - extractive body cue:** Lines and shaded bands: mean ±1 s.d. over 𝑛=6 evaluations per configuration.
- **p. 4 / 2.1. Motion Tracking - extractive body cue:** 86/200 runs, Welch's 𝑡-test, 𝑃< 0.001), and (J) tracking error (paired 𝑡-test across commanded velocities, 𝑃< 0.001 in both velocity regimes); mean ±1 s.d. over ...
- **p. 5 / 2.1. Motion Tracking - extractive body cue:** For compute, we trained on 2, 4, and 16 nodes (16, 32, and 128 GPUs), all to 50k iterations, yielding approximately 2k, 9k, and 21k ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our metric, similar to [29], captured the physically meaningful failure modes such as falling. | p. 5 (2.1. Motion Tracking) |
| body limitation/failure cue | Limitations include the lack of formal treatment of safety and energy efficiency for extended deployments. | p. 12 (2.6. Discussion) |
| body limitation/failure cue | It also contrasts with task-specific reward engineering (for example, locomotion controllers such as OpenHomie [13]), where each behavior requires a tailored objective that does ... | p. 12 (2.6. Discussion) |
| body limitation/failure cue | After retargeting to the Unitree G1 using General Motion Retargeting (GMR) [54] and PyRoki [55], we filtered out physically implausible motions (such as stair ... | p. 13 (3.1. Humanoid Motion Dataset) |
| body limitation/failure cue | Visualizations of out-of-distribution test motions, including successful and failed tracking cases, are provided in the Supplementary Materials (Fig. | p. 5 (2.1. Motion Tracking) |
| body limitation/failure cue | The second, testrepetition (9,395 clips, 12 hours), evaluated robustness to new performances and repetitions of known motion types. | p. 3 (2.1. Motion Tracking) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For compute, more GPUs yielded better asymptotic performance at the same iteration count, as larger batch sizes improved optimization stability. | p. 5 (2.1. Motion Tracking) |
| The planner achieved inference times under 5 ms on a standard laptop and ∼12 ms on a Jetson Orin GPU. | p. 6 (2.2. Interactive Motion Control) |
| For compute, we trained on 2, 4, and 16 nodes (16, 32, and 128 GPUs), all to 50k iterations, yielding approximately 2k, 9k, and ... | p. 5 (2.1. Motion Tracking) |
| We chose FSQ over the vector-quantized variational autoencoder (VQ-VAE) [62] for training stability under joint PPO optimization (the Implementation Details section), and validated this ... | p. 15 (3.2. Universal Humanoid Motion Tracking) |
| Due to compute constraints, this sweep was run on 32 GPUs rather than 128. | p. 18 (3.6. Validation of Key Design Choices) |
| SONIC, trained on 100 million frames of motion over 21k GPU hours (128 GPUs over 7 days), exhibited strong generalization to unseen motions. | p. 3 (2.1. Motion Tracking) |
| We further reported the local (root-relative) mean per-joint position error (MPJPE-L) 𝐸mpjpe (in millimeters, mm), computed over 14 body links (pelvis, knees, ankles, torso, ... | p. 3 (2.1. Motion Tracking) |
| (A to C) Effect of scaling data size, model size, and compute on test-content (unseen motion content, OOD) and test-repetition (held-out takes of seen ... | p. 4 (2.1. Motion Tracking) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 2.1. Motion Tracking - extractive body cue:** Our metric, similar to [29], captured the physically meaningful failure modes such as falling.
- **p. 12 / 2.6. Discussion - extractive body cue:** Limitations include the lack of formal treatment of safety and energy efficiency for extended deployments.
- **p. 12 / 2.6. Discussion - extractive body cue:** It also contrasts with task-specific reward engineering (for example, locomotion controllers such as OpenHomie [13]), where each behavior requires a tailored objective that does not ...
- **p. 13 / 3.1. Humanoid Motion Dataset - extractive body cue:** After retargeting to the Unitree G1 using General Motion Retargeting (GMR) [54] and PyRoki [55], we filtered out physically implausible motions (such as stair climbing ...
- **p. 5 / 2.1. Motion Tracking - extractive body cue:** Visualizations of out-of-distribution test motions, including successful and failed tracking cases, are provided in the Supplementary Materials (Fig.
- **p. 3 / 2.1. Motion Tracking - extractive body cue:** The second, testrepetition (9,395 clips, 12 hours), evaluated robustness to new performances and repetitions of known motion types.

- **Evidence anchors reviewed:** datasets p. 13 (3.1. Humanoid Motion Dataset), p. 3 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking), p. 3 (2.1. Motion Tracking), p. 12 (2.6. Discussion), p. 13 (3.1. Humanoid Motion Dataset), metrics p. 4 (2.1. Motion Tracking), p. 4 (2.1. Motion Tracking), p. 11 (2.5. Foundation-Model-Driven Loco-manipulation), p. 3 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking), baselines p. 5 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking), p. 3 (2.1. Motion Tracking), p. 4 (2.1. Motion Tracking), p. 4 (2.1. Motion Tracking), p. 19 (3.7. Statistical Analysis), results p. 19 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking), p. 9 (2.5. Foundation-Model-Driven Loco-manipulation), p. 11 (2.5. Foundation-Model-Driven Loco-manipulation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (39 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 3: Ablation studies. SR denotes success rate. Each entry reports a single evaluation per configuration on the full test split (descriptive; no statistical test applied). (A) FSQ outperforms VQ-VAE ... (p. 19, Figure/Table caption).
- **Metric evidence:** SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control 4m 10m 22m 100m Frames (millions) 98.6% 98.8% 99.0% 99.2% 99.4% 99.6% 99.8% Success Rate 24.4mm 24.2mm 23.9mm 23.8mm 22.7mm 22.6mm ... (p. 4, 2.1. Motion Tracking).
- **Baseline/ablation evidence:** For baseline comparisons, we additionally evaluated on PHUMA [43], a publicly available dataset of 3 (p. 3, 2.1. Motion Tracking).
- **Failure/negative evidence:** Our metric, similar to [29], captured the physically meaningful failure modes such as falling. (p. 5, 2.1. Motion Tracking).
