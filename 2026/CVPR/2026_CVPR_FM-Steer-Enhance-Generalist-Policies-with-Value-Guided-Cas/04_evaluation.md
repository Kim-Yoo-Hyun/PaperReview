# Evaluation - FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption)): Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer (π0) achieves the highest average success rate and ...

## Evaluation Body Digest

- **p. 5 / 5. Experiments - extractive PDF cue:** We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including prior test-time computing ...
- **p. 5 / 5. Experiments - extractive PDF cue:** Our experiments evaluate whether FM-Steer can effectively enhance existing flow-based VLAs at test time while preserving the efficiency required for real-time robotic control.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer (π0) achieves the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Real-world evaluation on WidowX, Franka, and AgiBot G-1 tasks. We evaluate FM-Steer across 3 real-robot platforms with varying backgrounds, poses, and motion distractors. ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present FM-Steer, a test-time computing framework exploring human-like thinking capabilities for dexterous robot control. Equipped with value-guided test-time sampling and cascaded action ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of FM-Steer. FM-Steer augments a flow-based VLA with two modules: the intermediate flow verifier and the Lite- Flow denoiser. Given an observation, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. SimplerEnv Results. We compare FM-Steer with two prior test-time computing methods, V-GPS [50] and RoboMonkey [33], on four WidowX tasks and Google Robot ...
- **p. 8 / 6. Conclusion - extractive PDF cue:** The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Implementation Details (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer (π0) achieves ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. We present FM-Steer, a test-time computing framework exploring human-like thinking capabilities for dexterous robot control. Equipped with value-guided test-time sampling and cascaded ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. Real-world evaluation on WidowX, Franka, and AgiBot G-1 tasks. We evaluate FM-Steer across 3 real-robot platforms with varying backgrounds, poses, and motion ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. SimplerEnv Results. We compare FM-Steer with two prior test-time computing methods, V-GPS [50] and RoboMonkey [33], on four WidowX tasks and Google ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 5. Experiments - extractive PDF cue:** We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including prior test-time computing ...
- **p. 5 / 5. Experiments - extractive PDF cue:** Our experiments evaluate whether FM-Steer can effectively enhance existing flow-based VLAs at test time while preserving the efficiency required for real-time robotic control.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present FM-Steer, a test-time computing framework exploring human-like thinking capabilities for dexterous robot control. Equipped with value-guided test-time sampling and cascaded action ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of FM-Steer. FM-Steer augments a flow-based VLA with two modules: the intermediate flow verifier and the Lite- Flow denoiser. Given an observation, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Experimental setups on WidowX, AgiBot G-1, and Franka. We evaluate FM-Steer across 3 simulation environments and 3 different real-world robotic platforms, covering 15 ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer (π0) achieves the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. SimplerEnv Results. We compare FM-Steer with two prior test-time computing methods, V-GPS [50] and RoboMonkey [33], on four WidowX tasks and Google Robot ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Real-world evaluation on WidowX, Franka, and AgiBot G-1 tasks. We evaluate FM-Steer across 3 real-robot platforms with varying backgrounds, poses, and motion distractors. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Visualization of value-guided test-time sampling and cascaded action denoising. Panel (a) shows value maps of can- didate actions, where the ground-truth actions lie ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Real-world ablations on WidowX, Franka, and Agi- Bot G-1. We conduct ablation studies of FM-Steer across 3 differ- ent real-world robotic platforms, covering ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including prior test-time ... | embodiment, simulator version and control stack | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Task/environment | Our experiments evaluate whether FM-Steer can effectively enhance existing flow-based VLAs at test time while preserving the efficiency required for real-time robotic control. | reset, timeout, object/scene variation | p. 5 (5. Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (3. Preliminaries), p. 4 (4.2. Cascaded Action Denoising) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 4 (4.1. Value-Guided Test-Time Sampling), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer (π0) achieves ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 4. Real-world evaluation on WidowX, Franka, and AgiBot G-1 tasks. We evaluate FM-Steer across 3 real-robot platforms with varying backgrounds, poses, and motion ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1. We present FM-Steer, a test-time computing framework exploring human-like thinking capabilities for dexterous robot control. Equipped with value-guided test-time sampling and cascaded ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Overview of FM-Steer. FM-Steer augments a flow-based VLA with two modules: the intermediate flow verifier and the Lite- Flow denoiser. Given an ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 2. SimplerEnv Results. We compare FM-Steer with two prior test-time computing methods, V-GPS [50] and RoboMonkey [33], on four WidowX tasks and Google ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including prior test-time ... | comparison identity and matched condition | p. 5 (5. Experiments) |
| Figure 1. We present FM-Steer, a test-time computing framework exploring human-like thinking capabilities for dexterous robot control. Equipped with value-guided test-time sampling and cascaded ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 4. Real-world evaluation on WidowX, Franka, and AgiBot G-1 tasks. We evaluate FM-Steer across 3 real-robot platforms with varying backgrounds, poses, and motion ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 3. Ablations on LIBERO and SimplerEnv. We conduct ablation studies across LIBERO [44] and SimplerEnv [39] on Wid- owX and Google Robot tasks. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 6. Real-world ablations on WidowX, Franka, and Agi- Bot G-1. We conduct ablation studies of FM-Steer across 3 differ- ent real-world robotic platforms, ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Ablations on LIBERO and SimplerEnv. We conduct ablation studies across LIBERO [44] and SimplerEnv [39] on Wid- owX and Google Robot tasks. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 6. Real-world ablations on WidowX, Franka, and Agi- Bot G-1. We conduct ablation studies of FM-Steer across 3 differ- ent real-world robotic platforms, ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the main contributions of this work are: • We propose FM-Steer, a test-time computing framework that enhances flow-based Vision-Language-Action models while improving ... | Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer (π0) achieves ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | Figure 1. We present FM-Steer, a test-time computing framework exploring human-like thinking capabilities for dexterous robot control. Equipped with value-guided test-time sampling and cascaded ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Implementation Details - extractive PDF cue:** During deployment, we use a single RTX 4090 GPU for inference.
- **p. 5 / 5.1. Implementation Details - extractive PDF cue:** FMSteer sets the noise-level bound T in the range of 0.7 to 0.9 and selects N = 5 candidates from the original VLA at each ...
- **p. 4 / 4.1. Value-Guided Test-Time Sampling - extractive PDF cue:** Lite-Flow Denoiser Flow-Based VLA Flow Matching Head Intermediate Flow Verifier visual token text token action token special query token state token 90Hz 4Hz Stochasticity Sampling ...
- **p. 5 / 4.2. Cascaded Action Denoising - extractive PDF cue:** 3rd person camera WidowX 250 Robot Arm Gripper AgiBot G-1 Humanoid Robot Head camera Left hand camera right hand camera effector Franka Panda Emika Robot ...
- **p. 5 / 4.3. Training and Deployment Strategy - extractive PDF cue:** For example, at the initial timestep t, the original VLA generates N = 5 candidate action chunks {Aτ1 t , Aτ2 t , . . ...
- **p. 5 / 5.1. Implementation Details - extractive PDF cue:** During deployment, we use a single RTX 4090 GPU for inference.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies. | p. 8 (6. Conclusion) |
| body limitation/failure cue | FM-Steer combines valueguided test-time sampling with effective best-of-N selection and cascaded action denoising, integrating the original VLA with a lightweight denoiser to achieve rapid ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 2. Overview of FM-Steer. FM-Steer augments a flow-based VLA with two modules: the intermediate flow verifier and the Lite- Flow denoiser. Given an ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | FMSteer sets the noise-level bound T in the range of 0.7 to 0.9 and selects N = 5 candidates from the original VLA at ... | p. 5 (5.1. Implementation Details) |
| body limitation/failure cue | Figure 3. Experimental setups on WidowX, AgiBot G-1, and Franka. We evaluate FM-Steer across 3 simulation environments and 3 different real-world robotic platforms, covering ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Figure 5. Visualization of value-guided test-time sampling and cascaded action denoising. Panel (a) shows value maps of can- didate actions, where the ground-truth actions ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| FM-Steer is trained on 8 A100 GPUs with a batch size ranging from 8 to 32 across different datasets. | p. 5 (5.1. Implementation Details) |
| During deployment, we use a single RTX 4090 GPU for inference. | p. 5 (5.1. Implementation Details) |
| 4.2) to complete the remaining Euler forward steps. | p. 3 (4.1. Value-Guided Test-Time Sampling) |
| During the forward Euler process used to compute the integral in Eq. | p. 3 (4.1. Value-Guided Test-Time Sampling) |
| To ensure a fair comparison, we first adjust the hyperparameters of each method (e.g., chunk size and number of candidates) to achieve its best ... | p. 7 (5.3. Efficiency Improvement) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive PDF cue:** The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies.
- **p. 8 / 6. Conclusion - extractive PDF cue:** FM-Steer combines valueguided test-time sampling with effective best-of-N selection and cascaded action denoising, integrating the original VLA with a lightweight denoiser to achieve rapid and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of FM-Steer. FM-Steer augments a flow-based VLA with two modules: the intermediate flow verifier and the Lite- Flow denoiser. Given an observation, ...
- **p. 5 / 5.1. Implementation Details - extractive PDF cue:** FMSteer sets the noise-level bound T in the range of 0.7 to 0.9 and selects N = 5 candidates from the original VLA at each ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Experimental setups on WidowX, AgiBot G-1, and Franka. We evaluate FM-Steer across 3 simulation environments and 3 different real-world robotic platforms, covering 15 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Visualization of value-guided test-time sampling and cascaded action denoising. Panel (a) shows value maps of can- didate actions, where the ground-truth actions lie ...

- **PDF anchors reviewed:** datasets p. 5 (5. Experiments), p. 5 (5. Experiments), metrics p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 5 (5. Experiments), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
