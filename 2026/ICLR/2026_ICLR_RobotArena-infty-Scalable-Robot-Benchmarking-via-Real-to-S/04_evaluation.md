# Evaluation - RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OutljIofvS; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245501. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 6 (Figure/Table caption), p. 24 (Figure/Table caption), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Figure 9: Policy evaluation results in RobotArena ∞ versus SIMPLER of Li et al. (2024c). 5.3 ROBOTARENA ∞VERSUS SIMPLER OF LI ET AL. (2024C) In Figure 9, we compare the ...

## Evaluation Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** The result is a continuously evolving, reproducible, and scalable benchmark for real-world-trained robot manipulation policies, addressing a critical missing capability in today's robotics landscape.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human feedback.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** BEHAVIOR boasts an impressive manual effort of asset and environment creation, while SIMPLER reconstructs four real-world Bridge scenes and includes hand-designed reward functions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing them ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We present a scalable and extensible benchmarking protocol for robotics, by coupling physics engines, real-to-sim translation and human preference feedback.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Both our benchmark environments and evaluation code will be publicly released and centrally maintained for continual support.
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and correctly ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 17: Example VLM-generated task evaluation curves on base environment. Left panels: Representative frames sampled at low- and high-progress points. Right panels: VLM-assigned completion score ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Figure 9: Policy evaluation results in RobotArena ∞ versus SIMPLER of Li et al. (2024c). 5.3 ROBOTARENA ∞VERSUS SIMPLER OF LI ET AL. (2024C) ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 4: Left: Task progress scores computed by prompting Gemini 2.5 Pro with image frames and synchronized object and robot state sequences. Right: Example ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and ... | p. 24 (Figure/Table caption) |
| ABSTRACT | BENCHMARK / DATASET | As policies expand in scope and complexity, these barriers only intensify, since defining "success" in robotics often hinges on nuanced human judgments of execution ... | p. 1 (ABSTRACT) |
| 1 INTRODUCTION | BENCHMARK / DATASET | In contrast, fields such as computer vision and natural language processing have advanced rapidly thanks to standardized benchmarks that provide consistent metrics, clear performance ... | p. 1 (1 INTRODUCTION) |

## Dataset / Benchmark Role

- **p. 1 / ABSTRACT - extractive body cue:** The result is a continuously evolving, reproducible, and scalable benchmark for real-world-trained robot manipulation policies, addressing a critical missing capability in today's robotics landscape.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human feedback.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** BEHAVIOR boasts an impressive manual effort of asset and environment creation, while SIMPLER reconstructs four real-world Bridge scenes and includes hand-designed reward functions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing them ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We present a scalable and extensible benchmarking protocol for robotics, by coupling physics engines, real-to-sim translation and human preference feedback.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Both our benchmark environments and evaluation code will be publicly released and centrally maintained for continual support.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: RobotArena ∞provides a scalable and extensible robot benchmarking framework by automating environment construction and evaluation. It automatically generates simulated environment seeded from real ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Automated video-to-simulation translation in RobotArena ∞. Given a frame from a video demonstration, we automatically create a corresponding simulated environment. and task evaluation ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Automated robot-camera calibra- tion through differentiable rendering of pose- conditioned 3D robot Gaussians. RobotArena ∞automatically creates simula- tion environments in physics engines from ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Left: Task progress scores computed by prompting Gemini 2.5 Pro with image frames and synchronized object and robot state sequences. Right: Example task ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Simulation environments in RobotArena ∞seeded from videos demonstrations in the datasets of Bridge, RH20T and DROID. in the estimated rankings, we compute confidence ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Policy evaluation results obtained from VLMs (a) in all RobotArena ∞environments and (b) in perturbations of BridgeSim environments. 5. X-VLA Zheng et al. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Human preference ranking of VLAs in BridgeSim environments from 8,749 pairwise comparisons. We show the VLA rankings derived from human pairwise preferences in ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8: Comparison of Simulation- Based Against Real-World-based Robot Evaluations using Ma et al. (2024)

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The result is a continuously evolving, reproducible, and scalable benchmark for real-world-trained robot manipulation policies, addressing a critical missing capability in today's robotics landscape. | embodiment, simulator version and control stack | p. 1 (ABSTRACT), p. 1 (ABSTRACT) |
| Task/environment | We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human ... | reset, timeout, object/scene variation | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (ABSTRACT), p. 1 (ABSTRACT) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 17: Example VLM-generated task evaluation curves on base environment. Left panels: Representative frames sampled at low- and high-progress points. Right panels: VLM-assigned completion ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Figure 18: Example VLM-generated task evaluation curves on perturbed environments. Top: A high-progress moment immediately after the object lift, for which the VLM predicts ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| We then deploy VLAs in these environments and evaluate their execution trajectories using two complementary strategies: (1) absolute evaluation, in which prompted VLMs or ... | definition/direction/unit from same section | p. 2 (1 INTRODUCTION) |
| Figure 4: Left: Task progress scores computed by prompting Gemini 2.5 Pro with image frames and synchronized object and robot state sequences. Right: Example ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 9: Policy evaluation results in RobotArena ∞ versus SIMPLER of Li et al. (2024c). 5.3 ROBOTARENA ∞VERSUS SIMPLER OF LI ET AL. (2024C) ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 5: Simulation environments in RobotArena ∞seeded from videos demonstrations in the datasets of Bridge, RH20T and DROID. in the estimated rankings, we compute ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| BEHAVIOR boasts an impressive manual effort of asset and environment creation, while SIMPLER reconstructs four real-world Bridge scenes and includes hand-designed reward functions. | definition/direction/unit from same section | p. 2 (1 INTRODUCTION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Such manual oversight also raises concerns about consistency and fairness, particularly when baselines and new models are compared under slightly different conditions. | comparison identity and matched condition | p. 1 (1 INTRODUCTION) |
| In contrast, fields such as computer vision and natural language processing have advanced rapidly thanks to standardized benchmarks that provide consistent metrics, clear performance ... | comparison identity and matched condition | p. 1 (1 INTRODUCTION) |
| The simulated environments are derived from both in-distribution and out-of-distribution videos, enabling rigorous tests of generalization in contemporary robot policies. comparisons of responses to ... | comparison identity and matched condition | p. 2 (1 INTRODUCTION) |
| Our benchmark is not without limitations. | comparison identity and matched condition | p. 3 (1 INTRODUCTION) |
| Figure 6: Human preference ranking of VLAs in BridgeSim environments from 8,749 pairwise comparisons. We show the VLA rankings derived from human pairwise preferences ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 8: Comparison of Simulation- Based Against Real-World-based Robot Evaluations using Ma et al. (2024) | comparison identity and matched condition | p. 9 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our benchmark is not without limitations. | component/input/data sensitivity | p. 3 (1 INTRODUCTION) |
| Figure 14: Background Change Example. The top-left image shows the original image without background perturbations. | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| Figure 15: Color Shift Example. The leftmost image shows the original image without color perturbations. color vector [R, G , B ], we compute: ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| Figure 16: Object Position Perturbation Example. The top-left image shows the original setup without perturbation. | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Figure 7: Policy evaluation results obtained from VLMs (a) in all RobotArena ∞environments and (b) in perturbations of BridgeSim environments. 5. X-VLA Zheng et ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing ... | Figure 9: Policy evaluation results in RobotArena ∞ versus SIMPLER of Li et al. (2024c). 5.3 ROBOTARENA ∞VERSUS SIMPLER OF LI ET AL. (2024C) ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 6 (Figure/Table caption), p. 24 (Figure/Table caption), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Primary metric/result | Figure 4: Left: Task progress scores computed by prompting Gemini 2.5 Pro with image frames and synchronized object and robot state sequences. Right: Example ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Intuitively, this focuses evaluation on the terminal phase of execution, where task completion (or failure) is most evident. | p. 6 (2 RELATED WORK) |
| body limitation/failure cue | Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and ... | p. 24 (Figure/Table caption) |
| body limitation/failure cue | Our benchmark is not without limitations. | p. 3 (1 INTRODUCTION) |
| body limitation/failure cue | For example, in RH20TSim, RoboVLM (19.05%) achieves a substantially higher score than all other models, while X-VLA fails (0.00%). | p. 8 (2 RELATED WORK) |
| body limitation/failure cue | 6 LIMITATIONS AND FUTURE DIRECTIONS By leveraging recent advances in reality-to-simulation translation and crowdsourced evaluation, RobotArena ∞provides a scalable and extensible robot benchmark. | p. 9 (2 RELATED WORK) |
| body limitation/failure cue | Second, even within the same environment, performance degrades under perturbations, showing that robustness to distribution shifts remains an open challenge. | p. 2 (1 INTRODUCTION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Human operators must supervise trials and manually reset scenes, which restricts the scale and frequency of evaluations (Vincent et al., 2024; Abou-Chakra et al., ... | p. 1 (1 INTRODUCTION) |
| In contrast, fields such as computer vision and natural language processing have advanced rapidly thanks to standardized benchmarks that provide consistent metrics, clear performance ... | p. 1 (1 INTRODUCTION) |
| We measure both in-distribution performance by testing on simulation environments seeded from training videos in established datasets such as Bridge Walke et al. | p. 2 (1 INTRODUCTION) |
| It automatically generates simulated environment seeded from real videos, deploys robot policies, and evaluates them using VLMs and crowdsourced workers that cast preferences between ... | p. 2 (1 INTRODUCTION) |
| Both our benchmark environments and evaluation code will be publicly released and centrally maintained for continual support. | p. 3 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 2 RELATED WORK - extractive body cue:** Intuitively, this focuses evaluation on the terminal phase of execution, where task completion (or failure) is most evident.
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and correctly ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our benchmark is not without limitations.
- **p. 8 / 2 RELATED WORK - extractive body cue:** For example, in RH20TSim, RoboVLM (19.05%) achieves a substantially higher score than all other models, while X-VLA fails (0.00%).
- **p. 9 / 2 RELATED WORK - extractive body cue:** 6 LIMITATIONS AND FUTURE DIRECTIONS By leveraging recent advances in reality-to-simulation translation and crowdsourced evaluation, RobotArena ∞provides a scalable and extensible robot benchmark.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Second, even within the same environment, performance degrades under perturbations, showing that robustness to distribution shifts remains an open challenge.

- **Evidence anchors reviewed:** datasets p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), metrics p. 24 (Figure/Table caption), p. 22 (Figure/Table caption), p. 24 (Figure/Table caption), p. 2 (1 INTRODUCTION), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), baselines p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), results p. 9 (Figure/Table caption), p. 6 (Figure/Table caption), p. 24 (Figure/Table caption), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
