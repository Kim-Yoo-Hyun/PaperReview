# Evaluation - VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.08792; PDF retrieval source: https://arxiv.org/pdf/2410.08792. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), p. 4 (IV. EXPERIMENTS)): To achieve success (TSR=1), each step in the plan must match the demo's action sequence in both content and temporal order. • FSR is equivalent to the conventional SR in ...

## Evaluation Body Digest

- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with still images or ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We are particularly interested in how well the robot can follow the demonstration videos step by step.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Real-world Experiment Setup Real-world experiments have demonstrated that SeeDo can manipulate objects in the physical world using an appropriate LMP.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** The experiment is conducted on a Universal Robots' UR10e cobot attached with a Robotiq 2F-85 gripper.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Garment Organization Task contains demonstrations of a human organizing their garments into separate boxes.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of the ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Conventional evaluation metric reports success rate (SR) of each task which could only reflect the completion at the final state of operation.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | To achieve success (TSR=1), each step in the plan must match the demo's action sequence in both content and temporal order. • FSR is ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Conventional evaluation metric reports success rate (SR) of each task which could only reflect the completion at the final state of operation. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Model Success Rate Failure Reason TSR↑ FSR↑ SSR↑ Vision↓ Spatial↓ Temporal↓ SeeDo w/o V.P. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This indicates room for future improvement. | p. 6 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with still images or ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We are particularly interested in how well the robot can follow the demonstration videos step by step.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Real-world Experiment Setup Real-world experiments have demonstrated that SeeDo can manipulate objects in the physical world using an appropriate LMP.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** The experiment is conducted on a Universal Robots' UR10e cobot attached with a Robotiq 2F-85 gripper.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Garment Organization Task contains demonstrations of a human organizing their garments into separate boxes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: VLM See, Robot Do. We designed an agent framework centered around a large Vision Language Model to interpret long- horizon human demonstration videos ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: The SeeDo agent consists of three modules. From left to right, a) The Keyframe Selection module detects the operating hand in the video ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: We collect long-horizon human demonstration videos across three diverse categories as our benchmark and carry out both simulation and real-world experiments. Tasks from ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: Results visualization on all three tasks.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of the ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 6: KDE plots of pointwise differences between the automated evaluation script and manually verified ground truth across three tasks and the overall. The vertical ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with still images ... | embodiment, simulator version and control stack | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | We are particularly interested in how well the robot can follow the demonstration videos step by step. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (III. METHOD), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Conventional evaluation metric reports success rate (SR) of each task which could only reflect the completion at the final state of operation. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Based on this, we propose three metrics: Task Success Rate (TSR), Final-state Success Rate (FSR), and Step Success Rate (SSR), to evaluate the completeness ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Model Success Rate Failure Reason TSR↑ FSR↑ SSR↑ Vision↓ Spatial↓ Temporal↓ SeeDo w/o V.P. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| To better understand the performance, we categorized failure cases based on the three error types discussed in Sec. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Finally, we analyzed and discussed the types of errors that occurred with SeeDo and the baselines. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| We also present ablation studies to assess the impact of separate modules. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Fig. 2: The SeeDo agent consists of three modules. From left to right, a) The Keyframe Selection module detects the operating hand in the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| SeeDo outperforms all closed-source and open-source video VLM baselines across TSR, FSR, and SSR. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| These two ablation baselines are reported respectively in Table II and Table III. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| In addition to comparing SeeDo to baselines across all three tasks. | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| Finally, we analyzed and discussed the types of errors that occurred with SeeDo and the baselines. | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| Baselines Video understanding VLMs. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| For consistency, we use the same core prompts as SeeDo across all baselines. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Since SeeDo utilizes GPT-4o as its VLM, we further test three variants of GPT-4o using different frame sampling strategies while keeping the same prompts: ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| We also present ablation studies to assess the impact of separate modules. | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |
| Our method operates purely on relative spatial relationships (e.g., left, right, above, below) extracted from the demonstration, without relying on fixed camera viewpoints; thus, ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Ablation on the visual prompting for Spatial Understanding. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Fig. 3: We collect long-horizon human demonstration videos across three diverse categories as our benchmark and carry out both simulation and real-world experiments. Tasks ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and ... | To achieve success (TSR=1), each step in the plan must match the demo's action sequence in both content and temporal order. • FSR is ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), p. 4 (IV. EXPERIMENTS) |
| Primary metric/result | Conventional evaluation metric reports success rate (SR) of each task which could only reflect the completion at the final state of operation. | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Gemini 1.5 Pro natively supports video input, while for the open-source models, we follow their official implementations, uniformly sampling 16 frames per video as input.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Since SeeDo utilizes GPT-4o as its VLM, we further test three variants of GPT-4o using different frame sampling strategies while keeping the same prompts: • ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models ... | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | However, spatial errors remain the main source of SeeDo 's failures. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Model Success Rate Failure Reason TSR↑ FSR↑ SSR↑ Vision↓ Spatial↓ Temporal↓ SeeDo w/o V.P. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with still images ... | p. 4 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| It aligns the pick-drop steps from the generated plan to the demo video in temporal order and computes the ratio of the number of ... | p. 5 (IV. EXPERIMENTS) |
| Meanwhile, we observed that even in cases where TSR and FSR fail, SeeDo is often able to successfully interpret most of the task steps ... | p. 6 (IV. EXPERIMENTS) |
| In addition to comparing SeeDo to baselines across all three tasks. | p. 4 (IV. EXPERIMENTS) |
| Finally, we analyzed and discussed the types of errors that occurred with SeeDo and the baselines. | p. 4 (IV. EXPERIMENTS) |
| We compare SeeDo with VLMs that are capable of direct video understanding. | p. 5 (IV. EXPERIMENTS) |
| This imposes high accuracy demands on all three modules of SeeDo. | p. 6 (IV. EXPERIMENTS) |
| 2: The SeeDo agent consists of three modules. | p. 3 (III. METHOD) |
| The VLM Interpreter module leverages chain-of-thought (CoT) [17] to generate task planning steps for robot execution. | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** However, spatial errors remain the main source of SeeDo 's failures.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Model Success Rate Failure Reason TSR↑ FSR↑ SSR↑ Vision↓ Spatial↓ Temporal↓ SeeDo w/o V.P.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of the ...
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with still images or ...

- **PDF anchors reviewed:** datasets p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), metrics p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), baselines p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), results p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), p. 4 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
