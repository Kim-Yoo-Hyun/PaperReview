# Evaluation - Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (62 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2510.03342; PDF retrieval source: https://arxiv.org/pdf/2510.03342. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation)): To improve research iteration speed, we have developed methods for evaluation without real robots in the loop.

## Evaluation Body Digest

- **p. 4 / 2.3. Evaluation - extractive body cue:** Over 90% of the evaluation episodes during the development of Gemini Robotics 1.5 were conducted in simulation.
- **p. 4 / 2.3. Evaluation - extractive body cue:** We use the open-source MuJoCo simulator (Todorov et al., 2012) to generate evaluation scenes for the robot embodiments in this report.
- **p. 4 / 2.3. Evaluation - extractive body cue:** This has allowed us to massively scale up the breadth of our evaluations to new objects, scenes, and environments, and to rapidly iterate on architectural ...
- **p. 4 / 2.3. Evaluation - extractive body cue:** To improve research iteration speed, we have developed methods for evaluation without real robots in the loop.
- **p. 22 / 7. Discussion - extractive body cue:** Its performance on tasks like visual and spatial thinking, task planning, progress estimation, and success detection is critical for robust, real-world robotic applications.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 2.3. Evaluation (p. 4); B.2.3.2 Qualitative Results (p. 43).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 2.3. Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | To improve research iteration speed, we have developed methods for evaluation without real robots in the loop. | p. 4 (2.3. Evaluation) |
| 2.3. Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | This has allowed us to massively scale up the breadth of our evaluations to new objects, scenes, and environments, and to rapidly iterate on ... | p. 4 (2.3. Evaluation) |

## Dataset / Benchmark Role

- **p. 4 / 2.3. Evaluation - extractive body cue:** Over 90% of the evaluation episodes during the development of Gemini Robotics 1.5 were conducted in simulation.
- **p. 4 / 2.3. Evaluation - extractive body cue:** We use the open-source MuJoCo simulator (Todorov et al., 2012) to generate evaluation scenes for the robot embodiments in this report.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Over 90% of the evaluation episodes during the development of Gemini Robotics 1.5 were conducted in simulation. | embodiment, simulator version and control stack | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |
| Task/environment | We use the open-source MuJoCo simulator (Todorov et al., 2012) to generate evaluation scenes for the robot embodiments in this report. | reset, timeout, object/scene variation | p. 4 (2.3. Evaluation) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (2.1. Model & Architecture), p. 3 (2.1. Model & Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use the open-source MuJoCo simulator (Todorov et al., 2012) to generate evaluation scenes for the robot embodiments in this report. | definition/direction/unit from same section | p. 4 (2.3. Evaluation) |
| This has allowed us to massively scale up the breadth of our evaluations to new objects, scenes, and environments, and to rapidly iterate on ... | definition/direction/unit from same section | p. 4 (2.3. Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For all comparisons reported in this report, we perform A/B/n testing on real robots. | comparison identity and matched condition | p. 4 (2.3. Evaluation) |
| To improve research iteration speed, we have developed methods for evaluation without real robots in the loop. | comparison identity and matched condition | p. 4 (2.3. Evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To improve research iteration speed, we have developed methods for evaluation without real robots in the loop. | component/input/data sensitivity | p. 4 (2.3. Evaluation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This multi-embodiment pre-training allows GR 1.5 to control multiple robots, including the ALOHA, Bi-arm Franka, and Apollo humanoid robots, without any robot-specific post-training, and ... | To improve research iteration speed, we have developed methods for evaluation without real robots in the loop. | PDF body cue; verify exact table/figure and matched conditions | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |
| Primary metric/result | This has allowed us to massively scale up the breadth of our evaluations to new objects, scenes, and environments, and to rapidly iterate on ... | numeric claim only at cited anchor | p. 4 (2.3. Evaluation) |

- Numeric sentences retained from the body:
- **p. 5 / 3. Gemini Robotics 1.5 is a general multi-embodiment Vision-Language-Action - extractive body cue:** The full benchmark includes 230 tasks in total.
- **p. 15 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** For the real-time evaluations, we sample recorded real-world robot rollouts from Section 5, and run the model at 5Hz and simulate inference latency.
- **p. 16 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** This is indicated by "°F" written on the lower part of the dial. * Numbers: The major markings on the scale are 30, 50, 80, ...
- **p. 16 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** The second tick mark would represent 70. * The pointer is pointing to the unnumbered tick mark that is immediately after the 50 mark. * ...
- **p. 16 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** This divides the 30-degree interval into three sections, with each section representing 10 degrees (50 + 10 = 60; 60 + 10 = 70; 70 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Its performance on tasks like visual and spatial thinking, task planning, progress estimation, and success detection is critical for robust, real-world robotic applications. | p. 22 (7. Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Able to scale embodied reasoning performance via inference time compute. | p. 11 (4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model) |
| Although real-world evaluation is still required to determine model quality, evaluation in simulation dramatically reduces the volume of tests on real hardware. | p. 4 (2.3. Evaluation) |
| The development of GR 1.5 requires comparisons of a large number of architecture variations, algorithm hyperparameters and other settings across multiple embodiments and tasks. | p. 4 (2.3. Evaluation) |
| Real-time SD considers model inference latency when computing prediction accuracy, while offline success detection assumes unlimited inference time for each prediction. | p. 14 (4.2. Frontier capabilities for Embodied Reasoning) |
| In the offline setting, we allow models unlimited inference time for success detection. | p. 15 (4.2. Frontier capabilities for Embodied Reasoning) |
| We find that models often require long inference time making real-time usage challenging, since stale success predictions quickly become irrelevant during dynamic robot interactions. | p. 15 (4.2. Frontier capabilities for Embodied Reasoning) |
| To accomplish a user-specified task, it can leverage digital tools to access external information or perform additional reasoning steps. | p. 3 (2.1. Model & Architecture) |
| It breaks complex tasks into simpler steps that can be executed by the VLA, and it performs success detection to decide when to switch ... | p. 3 (2.1. Model & Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 22 / 7. Discussion - extractive body cue:** Its performance on tasks like visual and spatial thinking, task planning, progress estimation, and success detection is critical for robust, real-world robotic applications.

- **PDF anchors reviewed:** datasets p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation), metrics p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation), baselines p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation), results p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
