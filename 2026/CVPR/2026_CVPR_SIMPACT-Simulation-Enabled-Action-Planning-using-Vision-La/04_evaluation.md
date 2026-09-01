# Evaluation - SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Front matter), p. 5 (Front matter), p. 5 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 4 (Front matter)): We evaluate this variant and find that it consistently achieves a zero success rate across all of our real-world tasks.

## Evaluation Body Digest

- **p. 4 / Front matter - extractive body cue:** Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task.
- **p. 3 / Front matter - extractive body cue:** Across tasks, we observe a high degree of consistency between simulation and real-world outcomes, with 89% of all cases exhibiting aligned success or failure.
- **p. 4 / Front matter - extractive body cue:** Input Specification • Task Instruction: Main task goal. • Real-World Context: Workspace limits, safe ranges • Simulation Rollouts: Specify the format of input context describing ...
- **p. 5 / Front matter - extractive body cue:** Standardized Benchmark Results We also provide evaluation of our method on the CALVIN benchmark [41] containing long-horizon tasks in simulation, as shown in Table 8.
- **p. 2 / Front matter - extractive body cue:** We evaluate this variant and find that it consistently achieves a zero success rate across all of our real-world tasks.
- **p. 2 / Front matter - extractive body cue:** Task Specification You are a versatile, general-purpose AI assistant functioning as an embodied planner for a robot arm.
- **p. 5 / Front matter - extractive body cue:** Evaluation results on the CALVIN Long-Horizon MultiTask Language Control (LH-MTLC) benchmark. #.
- **p. 3 / Front matter - extractive body cue:** With more efficient VLMs tailored for robotics applications, the

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate this variant and find that it consistently achieves a zero success rate across all of our real-world tasks. | p. 2 (Front matter) |
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our framework can also incorporate real-world feedback to improve the success rate after execution failures. | p. 5 (Front matter) |
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | Increasing the number of sampled proposals may improve performance in such cases. | p. 5 (Front matter) |
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | Avoid aggressive or risky proposals and focus on plans with high success rates. | p. 2 (Front matter) |
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | Despite the overall high alignment ratio, there remains room to improve simulation and real consistency. | p. 3 (Front matter) |

## Dataset / Benchmark Role

- **p. 4 / Front matter - extractive body cue:** Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task.
- **p. 3 / Front matter - extractive body cue:** Across tasks, we observe a high degree of consistency between simulation and real-world outcomes, with 89% of all cases exhibiting aligned success or failure.
- **p. 4 / Front matter - extractive body cue:** Input Specification • Task Instruction: Main task goal. • Real-World Context: Workspace limits, safe ranges • Simulation Rollouts: Specify the format of input context describing ...
- **p. 5 / Front matter - extractive body cue:** Standardized Benchmark Results We also provide evaluation of our method on the CALVIN benchmark [41] containing long-horizon tasks in simulation, as shown in Table 8.
- **p. 2 / Front matter - extractive body cue:** We evaluate this variant and find that it consistently achieves a zero success rate across all of our real-world tasks.
- **p. 2 / Front matter - extractive body cue:** Task Specification You are a versatile, general-purpose AI assistant functioning as an embodied planner for a robot arm.
- **p. 5 / Front matter - extractive body cue:** Evaluation results on the CALVIN Long-Horizon MultiTask Language Control (LH-MTLC) benchmark. #.
- **p. 3 / Front matter - extractive body cue:** With more efficient VLMs tailored for robotics applications, the

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 8. Action sampling prompt `sample outline. This prompt includes task specifications, input requirements, action primitive defini- tions, planning guidelines, and output format. It is ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 9. Example rollout context for action optimization in pivoting task. The context contains the action waypoints and the simulated state snapshots at each waypoint, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 10. Additional qualitative results. Following Fig. 5, this figure shows the initial state, execution progress, and final state for the sweeping tasks. better understand ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 11. Action optimization prompt `opt outline. This prompt includes task, input, and output specifications. It is combined with simulation rollout context as input to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 12. Correlation Between Simulation and Real-world Success/Failure. Results from 20 samples per task (100 total). Each rollout is categorized as one of: sim-success/real-success (green), ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 5. Computation time. We compute the average computa- tion time over 10 cases from each task. Component Time (mins) simulation construction 1.9 action sampling ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 13. Example scene setup variations. Throughout our ex- periments, we vary the object types, poses, colors and materials to demonstrate the robustness and generalizability ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 6. Robustness analysis of VLM-estimated physics parame- ters (N = 10 samples). The low variance and stable ranges indi- cate consistent estimation capabilities. Task ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task. | embodiment, simulator version and control stack | p. 4 (Front matter), p. 3 (Front matter) |
| Task/environment | Across tasks, we observe a high degree of consistency between simulation and real-world outcomes, with 89% of all cases exhibiting aligned success or failure. | reset, timeout, object/scene variation | p. 3 (Front matter), p. 4 (Front matter) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (Front matter), p. 2 (Front matter) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (Front matter), p. 3 (Front matter) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Avoid aggressive or risky proposals and focus on plans with high success rates. | definition/direction/unit from same section | p. 2 (Front matter) |
| We evaluate this variant and find that it consistently achieves a zero success rate across all of our real-world tasks. | definition/direction/unit from same section | p. 2 (Front matter) |
| Success rate vs friction coefficient µ. | definition/direction/unit from same section | p. 5 (Front matter) |
| Planning failures in simulation also transfer to the real world, further reducing success rates. | definition/direction/unit from same section | p. 5 (Front matter) |
| Robustness Validation We validate the robustness of our method by randomizing the scene layout and introducing different distractors for each rollout, as illustrated in ... | definition/direction/unit from same section | p. 4 (Front matter) |
| Figure 11. Action optimization prompt `opt outline. This prompt includes task, input, and output specifications. It is combined with simulation rollout context as input ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| After initial failed execution, we perform re-planning after simulation update leading to successful completion. planning successfully recovers 50% of them, with an average of ... | definition/direction/unit from same section | p. 6 (Front matter) |
| These tasks appear more sensitive to accurate physical modeling and contact dynamics. | definition/direction/unit from same section | p. 3 (Front matter) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our zero-shot method outperforms imitation learning baseline HULC [40] and VLA baseline Figure 14. | comparison identity and matched condition | p. 5 (Front matter) |
| We also include results from the current best performing baseline FLOWER [56] as a reference. | comparison identity and matched condition | p. 5 (Front matter) |
| Further Ablation Analysis We additionally consider a variant of our method in which we simultaneously replace the VLM sampler with a random sampler and ... | comparison identity and matched condition | p. 2 (Front matter) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Further Ablation Analysis We additionally consider a variant of our method in which we simultaneously replace the VLM sampler with a random sampler and ... | component/input/data sensitivity | p. 2 (Front matter) |
| Notably, this simplified variant is algorithmically identical to Prompting-with-the-Future (PWTF) [45]. | component/input/data sensitivity | p. 2 (Front matter) |
| These execution failures highlight the sensitivity and difficulty of our tasks: even minor errors in the planned actions can lead to failure. | component/input/data sensitivity | p. 5 (Front matter) |
| The VLM planning stage is the most time-consuming component. | component/input/data sensitivity | p. 3 (Front matter) |
| Computation Time Table 5 reports the runtime of each component in our method. | component/input/data sensitivity | p. 3 (Front matter) |
| Component Time (mins) simulation construction 1.9 action sampling 2.8 simulation rollout 0.8 action optimization 0.9 on the task. | component/input/data sensitivity | p. 4 (Front matter) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| For rigid objects, the numerical state consists of their full 6-DoF rigid transformation. | We evaluate this variant and find that it consistently achieves a zero success rate across all of our real-world tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Front matter), p. 5 (Front matter), p. 5 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 4 (Front matter) |
| Primary metric/result | Our framework can also incorporate real-world feedback to improve the success rate after execution failures. | numeric claim only at cited anchor | p. 5 (Front matter) |

- Numeric sentences retained from the body:
- **p. 3 / Front matter - extractive body cue:** Example Rollout Context { "timestamp": "20260112_224423", "object_names": ["brown_box", "pocky_box"], % total 2 objects ,! "waypoints": [ { "position": [0.4199, -0.2452, 0.3555], ,! "orientation": [0.00, 0.71, ...
- **p. 3 / Front matter - extractive body cue:** Each task therefore has 20 samples: 10 from the main experiments using our full pipeline, and 10 using direct VLM sampled action sequences.
- **p. 4 / Front matter - extractive body cue:** Results from 20 samples per task (100 total).
- **p. 5 / Front matter - extractive body cue:** Robustness analysis of VLM-estimated physics parameters (N = 10 samples).
- **p. 5 / Front matter - extractive body cue:** Task Parameter Mean ± Std Range [Min, Max] Non-toppling Push Mass (kg) 1.033 ± 0.0015 [1.0, 1.05] Friction Coeff. µ 0.36 ± 0.11 [0.3, 0.5] ...
- **p. 3 / Front matter - extractive body cue:** Example Rollout Context { "timestamp": "20260112_224423", "object_names": ["brown_box", "pocky_box"], % total 2 objects ,! "waypoints": [ { "position": [0.4199, -0.2452, 0.3555], ,! "orientation": [0.00, 0.71, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Correlation Between Simulation and RealWorld Performance This section examines the correlation between simulation and real-world results, specifically whether success or failure in simulation predicts ... | p. 2 (Front matter) |
| body limitation/failure cue | Across tasks, we observe a high degree of consistency between simulation and real-world outcomes, with 89% of all cases exhibiting aligned success or failure. | p. 3 (Front matter) |
| body limitation/failure cue | Simulated failures enable the VLM to avoid similar real-world failures, while simulated successes offer informative guidance for selecting effective action sequences. | p. 3 (Front matter) |
| body limitation/failure cue | 2) Infer Logic & Physics: Identify the causes of failures and the characteristics of successful attempts. | p. 4 (Front matter) |
| body limitation/failure cue | Simulation and real outcomes match in 89% of cases (both success or both failure), with 11% showing sim-success/real-fail. | p. 4 (Front matter) |
| body limitation/failure cue | The pivoting and shape rope failures are both planning failures. | p. 5 (Front matter) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We follow the open-sourced CEM implementation from PWTF and adopt the same set of hyperparameters. | p. 2 (Front matter) |
| SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models Supplementary Material This supplementary material provides additional implementation details, experiment analyses, and qualitative results supporting our main ... | p. 1 (Front matter) |
| Computation Time Table 5 reports the runtime of each component in our method. | p. 3 (Front matter) |
| The image segmentation and pose estimation steps require significantly less time. | p. 3 (Front matter) |
| We compute the average computation time over 10 cases from each task. | p. 4 (Front matter) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Front matter - extractive body cue:** Correlation Between Simulation and RealWorld Performance This section examines the correlation between simulation and real-world results, specifically whether success or failure in simulation predicts the ...
- **p. 3 / Front matter - extractive body cue:** Across tasks, we observe a high degree of consistency between simulation and real-world outcomes, with 89% of all cases exhibiting aligned success or failure.
- **p. 3 / Front matter - extractive body cue:** Simulated failures enable the VLM to avoid similar real-world failures, while simulated successes offer informative guidance for selecting effective action sequences.
- **p. 4 / Front matter - extractive body cue:** 2) Infer Logic & Physics: Identify the causes of failures and the characteristics of successful attempts.
- **p. 4 / Front matter - extractive body cue:** Simulation and real outcomes match in 89% of cases (both success or both failure), with 11% showing sim-success/real-fail.
- **p. 5 / Front matter - extractive body cue:** The pivoting and shape rope failures are both planning failures.

- **PDF anchors reviewed:** datasets p. 4 (Front matter), p. 3 (Front matter), p. 4 (Front matter), p. 5 (Front matter), p. 2 (Front matter), p. 2 (Front matter), metrics p. 2 (Front matter), p. 2 (Front matter), p. 5 (Front matter), p. 5 (Front matter), p. 4 (Front matter), p. 4 (Figure/Table caption), baselines p. 5 (Front matter), p. 5 (Front matter), p. 2 (Front matter), results p. 2 (Front matter), p. 5 (Front matter), p. 5 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 4 (Front matter).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
