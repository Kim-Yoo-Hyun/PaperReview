# Evaluation - AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=NuR4lG4gKB; PDF retrieval source: https://openreview.net/pdf/fa8a077d4c454280e6633258b55a9ff0b4d204e5.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 8 (4.2.2. RESULTS AND ANALYSIS), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 4 (3.2. Evaluation Framework)): Compared to low-DoF ground-based platforms, the performance of existing VLA models on high-DoF aerial platforms remains suboptimal. π0 achieves its peak success rate in Base Manipulation tasks characterized by minimal ...

## Evaluation Body Digest

- **p. 4 / 3.2. Evaluation Framework - extractive body cue:** Compared to traditional ground robot tasks, aerial mobile manipulation introduces unique challenges such as dynamic coupling of the floating base, volumetric workspaces, and temporal complexity ...
- **p. 5 / 4.1. VLA Experiments - extractive body cue:** Q5: Safety constraints are critical in robotic tasks.
- **p. 5 / 4.1.1. EXPERIMENTAL SETUP - extractive body cue:** The training dataset is derived from our human-teleoperated simulation data, fully reflecting the 5
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Our evaluation revealed destructive interactions with the environment in certain episodes, indicating that addressing safety constraints in Aerial Manipulation Systems remains a pivotal direction for ...
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Furthermore, they demonstrate that pre-training on massive crossembodiment data (including mobile robotics) enables models to acquire generalizable mechanical manipulation priors.
- **p. 7 / 4.2.1. EXPERIMENTAL SETUP - extractive body cue:** To establish a representative benchmark, we analyze six diverse open-source VLMs.
- **p. 7 / 4.2.1. EXPERIMENTAL SETUP - extractive body cue:** Molmo7B-D-0924 (Deitke et al., 2024) employs a data-centric strategy via the PixMo dataset for efficient alignment.
- **p. 4 / 3.2. Evaluation Framework - extractive body cue:** For VLA models, we conduct closed-loop evaluations based on an online simulation environment, focusing on UAV-Arm Coordination capabilities under real-time inference.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 2.4. Benchmarks for Robot Manipulation (p. 3); 3.2. Evaluation Framework (p. 4); 3.4. Dataset Construction (p. 5); 4. Experiments (p. 5); 4.1. VLA Experiments (p. 5); 4.1.1. EXPERIMENTAL SETUP (p. 5); 4.1.2. MAIN RESULTS AND ANALYSIS (p. 6); 4.2. VLM Experiments (p. 6); 4.2.1. EXPERIMENTAL SETUP (p. 7); 4.2.2. RESULTS AND ANALYSIS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1.2. MAIN RESULTS AND ANALYSIS | BENCHMARK / DATASET | Compared to low-DoF ground-based platforms, the performance of existing VLA models on high-DoF aerial platforms remains suboptimal. π0 achieves its peak success rate in ... | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| 4.2.2. RESULTS AND ANALYSIS | BENCHMARK / DATASET | The table displays normalized sub-metric scores and planning success rates (Succ, %) for each model across different task scenarios and instruction types. | p. 8 (4.2.2. RESULTS AND ANALYSIS) |
| 4.1.2. MAIN RESULTS AND ANALYSIS | BENCHMARK / DATASET | Experimental results indicate that large-scale pre-trained models, represented by π0.5 and π0, demonstrate significant advantages in the AIR-VLA evaluation, outperforming traditional imitation learning baselines ... | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| 4.2.2. RESULTS AND ANALYSIS | BENCHMARK / DATASET | Notably, Qwen3-VL achieves state-ofthe-art (SOTA) performance across all baseline models in four core dimensions: Process Planning, Spatial Navigation, Object Grounding, and Skill Selection, highlighting ... | p. 7 (4.2.2. RESULTS AND ANALYSIS) |
| 4.2.2. RESULTS AND ANALYSIS | BENCHMARK / DATASET | In-depth analysis indicates that this lack of 3D spatial awareness is the primary bottleneck limiting the end-to-end planning Success Rate. | p. 7 (4.2.2. RESULTS AND ANALYSIS) |

## Dataset / Benchmark Role

- **p. 4 / 3.2. Evaluation Framework - extractive body cue:** Compared to traditional ground robot tasks, aerial mobile manipulation introduces unique challenges such as dynamic coupling of the floating base, volumetric workspaces, and temporal complexity ...
- **p. 5 / 4.1. VLA Experiments - extractive body cue:** Q5: Safety constraints are critical in robotic tasks.
- **p. 5 / 4.1.1. EXPERIMENTAL SETUP - extractive body cue:** The training dataset is derived from our human-teleoperated simulation data, fully reflecting the 5
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Our evaluation revealed destructive interactions with the environment in certain episodes, indicating that addressing safety constraints in Aerial Manipulation Systems remains a pivotal direction for ...
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Furthermore, they demonstrate that pre-training on massive crossembodiment data (including mobile robotics) enables models to acquire generalizable mechanical manipulation priors.
- **p. 7 / 4.2.1. EXPERIMENTAL SETUP - extractive body cue:** To establish a representative benchmark, we analyze six diverse open-source VLMs.
- **p. 7 / 4.2.1. EXPERIMENTAL SETUP - extractive body cue:** Molmo7B-D-0924 (Deitke et al., 2024) employs a data-centric strategy via the PixMo dataset for efficient alignment.
- **p. 4 / 3.2. Evaluation Framework - extractive body cue:** For VLA models, we conduct closed-loop evaluations based on an online simulation environment, focusing on UAV-Arm Coordination capabilities under real-time inference.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview of AIR-VLA model framework and dataset of aerial manipulation tasks.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the AIR-VLA benchmark. AIR-VLA serves as a full-stack Vision-Language-Action platform tailored for aerial manipulation systems. It integrates a simulation-based teleoperation data ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Detailed performance evaluation of models across four task suites and overall average. The table displays normalized scores for sub-metrics and weighted total scores ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Robustness evaluation of π0.5 under disturbance and perception-deprived conditions. The table shows absolute scores for each metric, with values in parentheses indicating the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Evaluation pipeline for VLM high-level planning capabilities in aerial manipulation tasks.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Detailed evaluation of VLM task planning capabilities. The table displays normalized sub-metric scores and planning success rates (Succ, %) for each model across ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 4. Task examples in AIR-VLA dataset. Coupled Dynamics and Long-Horizon Reasoning. Unlike traditional benchmarks that often treat navigation and manipulation as decoupled phases or ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5. Observation Space. This figure illustrates instances of observations from various camera perspectives.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Compared to traditional ground robot tasks, aerial mobile manipulation introduces unique challenges such as dynamic coupling of the floating base, volumetric workspaces, and temporal ... | embodiment, simulator version and control stack | p. 4 (3.2. Evaluation Framework), p. 5 (4.1. VLA Experiments) |
| Task/environment | Q5: Safety constraints are critical in robotic tasks. | reset, timeout, object/scene variation | p. 5 (4.1. VLA Experiments), p. 5 (4.1.1. EXPERIMENTAL SETUP) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 3 (1. Introduction), p. 5 (3.4. Dataset Construction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The table displays normalized sub-metric scores and planning success rates (Succ, %) for each model across different task scenarios and instruction types. | definition/direction/unit from same section | p. 8 (4.2.2. RESULTS AND ANALYSIS) |
| Compared to low-DoF ground-based platforms, the performance of existing VLA models on high-DoF aerial platforms remains suboptimal. π0 achieves its peak success rate in ... | definition/direction/unit from same section | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| In-depth analysis indicates that this lack of 3D spatial awareness is the primary bottleneck limiting the end-to-end planning Success Rate. | definition/direction/unit from same section | p. 7 (4.2.2. RESULTS AND ANALYSIS) |
| Abbreviations: Pos: Base Positioning Accuracy (Spos); Arm: Manipulator Efficacy (Sarm); Safe: Environmental Safety (Ssafe); Task: Task Progression (Stask); Tot: Weighted Total Score (Stotal). | definition/direction/unit from same section | p. 7 (4.2. VLM Experiments) |
| Models are sorted in ascending order by their Overall Average Total score. | definition/direction/unit from same section | p. 8 (4.2.2. RESULTS AND ANALYSIS) |
| Our experiments are structured around the following research questions: Q1: Can VLA models maintain superior task completion performance in high-DoF (12-DoF in experiments) robotic ... | definition/direction/unit from same section | p. 5 (4.1. VLA Experiments) |
| Nevertheless, there remains substantial room for improvement in overall task completion rates. | definition/direction/unit from same section | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| Specifically, we quantify the feasibility of UAV spatial navigation, the manipulation precision of the end-effector, and dynamic safety during longhorizon task execution. | definition/direction/unit from same section | p. 4 (3.2. Evaluation Framework) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Experimental results indicate that large-scale pre-trained models, represented by π0.5 and π0, demonstrate significant advantages in the AIR-VLA evaluation, outperforming traditional imitation learning baselines ... | comparison identity and matched condition | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| Notably, Qwen3-VL achieves state-ofthe-art (SOTA) performance across all baseline models in four core dimensions: Process Planning, Spatial Navigation, Object Grounding, and Skill Selection, highlighting ... | comparison identity and matched condition | p. 7 (4.2.2. RESULTS AND ANALYSIS) |
| Compared to traditional ground robot tasks, aerial mobile manipulation introduces unique challenges such as dynamic coupling of the floating base, volumetric workspaces, and temporal ... | comparison identity and matched condition | p. 4 (3.2. Evaluation Framework) |
| In this section, we report the quantitative performance of baseline models on the four task suites of AIR-VLA. | comparison identity and matched condition | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| The table shows absolute scores for each metric, with values in parentheses indicating the performance drop (↓∆) compared to the Standard condition. | comparison identity and matched condition | p. 7 (4.2. VLM Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To establish a representative benchmark, we evaluate six diverse models: π0 (Black et al., 2026) and π0.5 (Black et al., 2025), Flow Matching-based foundation ... | component/input/data sensitivity | p. 5 (4.1.1. EXPERIMENTAL SETUP) |
| Notably, even under few-shot fine-tuning settings with only 30-50 demonstrations, foundation models like π0.5 rapidly adapt to aerial manipulation paradigms unseen during pretraining, achieving ... | component/input/data sensitivity | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| We adopted a differentiated fine-tuning strategy based on task difficulty: 30 trajectories were used for fine-tuning simple single-step tasks with less physical interaction, while ... | component/input/data sensitivity | p. 6 (4.1.1. EXPERIMENTAL SETUP) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of this paper are summarized as follows: • Pioneering Aerial Manipulation VLA Benchmark: We propose the first VLA benchmark testbed specifically ... | Compared to low-DoF ground-based platforms, the performance of existing VLA models on high-DoF aerial platforms remains suboptimal. π0 achieves its peak success rate in ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 8 (4.2.2. RESULTS AND ANALYSIS), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 4 (3.2. Evaluation Framework) |
| Primary metric/result | The table displays normalized sub-metric scores and planning success rates (Succ, %) for each model across different task scenarios and instruction types. | numeric claim only at cited anchor | p. 8 (4.2.2. RESULTS AND ANALYSIS) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1.1. EXPERIMENTAL SETUP - extractive body cue:** We adopted a differentiated fine-tuning strategy based on task difficulty: 30 trajectories were used for fine-tuning simple single-step tasks with less physical interaction, while 50 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly more severe disturbances to the system than in ... | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| body limitation/failure cue | Notably, in spatial understanding tasks, the models exhibit Spatial Grounding Failure: although the correct object category is identified, the agent manipulates an identical object ... | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| body limitation/failure cue | In summary, VLMs hold immense potential for high-level planning in aerial manipulation, particularly in mitigating the long-horizon reasoning limitations of VLA models. | p. 7 (4.2.2. RESULTS AND ANALYSIS) |
| body limitation/failure cue | Our findings reveal that while transferring pre-trained VLA models to aerial platforms is feasible, existing models still face severe challenges in handling floating-base dynamic ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Robustness evaluation of π0.5 under disturbance and perception-deprived conditions. | p. 7 (4.2. VLM Experiments) |
| body limitation/failure cue | Q2: Can VLA models cope with external disturbances in AMS and complete tasks under random base jitter? | p. 5 (4.1. VLA Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| InternVL3 5-8B (Wang et al., 2025b) adopts a "strong vision encoder + strong language decoder" design, targeting geometric perception. | p. 7 (4.2.1. EXPERIMENTAL SETUP) |
| To enhance generalization, we constructed diverse environments (residential, industrial, outdoor) with varying lighting conditions. | p. 5 (3.4. Dataset Construction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly more severe disturbances to the system than in ground-based ...
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Notably, in spatial understanding tasks, the models exhibit Spatial Grounding Failure: although the correct object category is identified, the agent manipulates an identical object at ...
- **p. 7 / 4.2.2. RESULTS AND ANALYSIS - extractive body cue:** In summary, VLMs hold immense potential for high-level planning in aerial manipulation, particularly in mitigating the long-horizon reasoning limitations of VLA models.
- **p. 8 / 5. Conclusion - extractive body cue:** Our findings reveal that while transferring pre-trained VLA models to aerial platforms is feasible, existing models still face severe challenges in handling floating-base dynamic coupling, ...
- **p. 7 / 4.2. VLM Experiments - extractive body cue:** Robustness evaluation of π0.5 under disturbance and perception-deprived conditions.
- **p. 5 / 4.1. VLA Experiments - extractive body cue:** Q2: Can VLA models cope with external disturbances in AMS and complete tasks under random base jitter?

- **Evidence anchors reviewed:** datasets p. 4 (3.2. Evaluation Framework), p. 5 (4.1. VLA Experiments), p. 5 (4.1.1. EXPERIMENTAL SETUP), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2.1. EXPERIMENTAL SETUP), metrics p. 8 (4.2.2. RESULTS AND ANALYSIS), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 7 (4.2. VLM Experiments), p. 8 (4.2.2. RESULTS AND ANALYSIS), p. 5 (4.1. VLA Experiments), baselines p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 4 (3.2. Evaluation Framework), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2. VLM Experiments), results p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 8 (4.2.2. RESULTS AND ANALYSIS), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 4 (3.2. Evaluation Framework).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
