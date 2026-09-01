# Evaluation - OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/iyer25a.html; PDF retrieval source: https://arxiv.org/pdf/2403.07870. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 13 (Figure/Table caption), p. 5 (Figure/Table caption)): Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies.

## Evaluation Body Digest

- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in this case, Quest ...
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** Our experiments and tasks are designed to answer the following questions: 1) How versatile is OPEN TEACH across a range of robotics setups?
- **p. 8 / 4) How intuitive is the system for new users? - extractive body cue:** Robot Setup Task Number of Demos Success Rate Franka-Allegro Open Box 3 9/10 Grasp Sponge 6 7/10 Pick Up Tea Sachet 4 7/10 Grasp Object ...
- **p. 8 / 4) How intuitive is the system for new users? - extractive body cue:** Task Success Rate Median completion time for successful demonstrations (in s) New User Expert New User Expert Holo-Dex AnyTeleop Open Teach Open Teach Holo-Dex AnyTeleop ...
- **p. 7 / 4) How intuitive is the system for new users? - extractive body cue:** 4: Real world task rollouts demonstrating the ability of OPEN TEACH to perform intricate, long-horizon tasks.
- **p. 8 / 4) How intuitive is the system for new users? - extractive body cue:** In Table IV, we present a comparative analysis of success rates and median completion times for new users across Holo-Dex, AnyTeleop, and OPEN TEACH for ...
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies.
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** We employ behavior cloning to train policies on LIBERO Sim, achieving an average success rate of 93%, thus confirming the high quality of the collected ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 2) We experimentally show that the demonstrations col (p. 2); V. EXPERIMENTAL EVALUATION (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4) How intuitive is the system for new users? | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies. | p. 6 (4) How intuitive is the system for new users?) |
| 4) How intuitive is the system for new users? | EMPIRICAL / REAL-ROBOT OR HARDWARE | Similar to prior work [20, 22], these policies were learned within 20 minutes and achieved an average success rate of 82%, validating the high ... | p. 6 (4) How intuitive is the system for new users?) |
| 4) How intuitive is the system for new users? | EMPIRICAL / REAL-ROBOT OR HARDWARE | On these tasks, OPEN TEACH demonstrates a higher success rate along with significantly reduced median time to complete tasks compared to the other baselines. | p. 8 (4) How intuitive is the system for new users?) |
| 4) How intuitive is the system for new users? | EMPIRICAL / REAL-ROBOT OR HARDWARE | Intriguingly, some new users, despite their unfamiliarity with the framework, achieve comparable or superior performance to the experts in certain tasks. | p. 8 (4) How intuitive is the system for new users?) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Thumb retargeting difference TABLE VI: Success rates for the user study conducted across 15 individuals. Each user roughly performs 3 tasks on ... | p. 13 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in this case, Quest ...
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** Our experiments and tasks are designed to answer the following questions: 1) How versatile is OPEN TEACH across a range of robotics setups?
- **p. 8 / 4) How intuitive is the system for new users? - extractive body cue:** Robot Setup Task Number of Demos Success Rate Franka-Allegro Open Box 3 9/10 Grasp Sponge 6 7/10 Pick Up Tea Sachet 4 7/10 Grasp Object ...
- **p. 8 / 4) How intuitive is the system for new users? - extractive body cue:** Task Success Rate Median completion time for successful demonstrations (in s) New User Expert New User Expert Holo-Dex AnyTeleop Open Teach Open Teach Holo-Dex AnyTeleop ...
- **p. 7 / 4) How intuitive is the system for new users? - extractive body cue:** 4: Real world task rollouts demonstrating the ability of OPEN TEACH to perform intricate, long-horizon tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We present OPEN TEACH, a unified robot teleoperation framework that supports multiple arms and hands, allows mobile manipulation, is calibration-free, and works across ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of the teleoperation module in OPEN TEACH. Provided a hand and wrist pose within the VR interface, the controller transmits keypoint data ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: The demonstration collection process as viewed from within the VR application. Shown here is one task being performed for each real-world setup. High ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Real world task rollouts demonstrating the ability of OPEN TEACH to perform intricate, long-horizon tasks.
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 5: Thumb retargeting difference TABLE VI: Success rates for the user study conducted across 15 individuals. Each user roughly performs 3 tasks on average. ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 6: Real world task rollouts demonstrating the ability of OPEN TEACH to perform intricate, long-horizon tasks.
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 7: Real world task rollouts demonstrating the ability of OPEN TEACH to perform intricate, long-horizon tasks.
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 8: Real world task rollouts demonstrating the ability of OPEN TEACH to perform intricate, long-horizon tasks.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in this case, ... | embodiment, simulator version and control stack | p. 6 (4) How intuitive is the system for new users?), p. 6 (V. EXPERIMENTAL EVALUATION) |
| Task/environment | Our experiments and tasks are designed to answer the following questions: 1) How versatile is OPEN TEACH across a range of robotics setups? | reset, timeout, object/scene variation | p. 6 (V. EXPERIMENTAL EVALUATION), p. 8 (4) How intuitive is the system for new users?) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Table IV, we present a comparative analysis of success rates and median completion times for new users across Holo-Dex, AnyTeleop, and OPEN TEACH ... | definition/direction/unit from same section | p. 8 (4) How intuitive is the system for new users?) |
| Task Success Rate Median completion time for successful demonstrations (in s) New User Expert New User Expert Holo-Dex AnyTeleop Open Teach Open Teach Holo-Dex ... | definition/direction/unit from same section | p. 8 (4) How intuitive is the system for new users?) |
| Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies. | definition/direction/unit from same section | p. 6 (4) How intuitive is the system for new users?) |
| We employ behavior cloning to train policies on LIBERO Sim, achieving an average success rate of 93%, thus confirming the high quality of the ... | definition/direction/unit from same section | p. 6 (4) How intuitive is the system for new users?) |
| Fig. 5: Thumb retargeting difference TABLE VI: Success rates for the user study conducted across 15 individuals. Each user roughly performs 3 tasks on ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Fig. 1: We present OPEN TEACH, a unified robot teleoperation framework that supports multiple arms and hands, allows mobile manipulation, is calibration-free, and works ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: Overview of the teleoperation module in OPEN TEACH. Provided a hand and wrist pose within the VR interface, the controller transmits keypoint ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 3: The demonstration collection process as viewed from within the VR application. Shown here is one task being performed for each real-world setup. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On these tasks, OPEN TEACH demonstrates a higher success rate along with significantly reduced median time to complete tasks compared to the other baselines. | comparison identity and matched condition | p. 8 (4) How intuitive is the system for new users?) |
| Fig. 3: The demonstration collection process as viewed from within the VR application. Shown here is one task being performed for each real-world setup. ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Since the Holo-Dex and AnyTeleop baselines lack open-source code for arm retargeting, we were unable to evaluate them on tasks involving arm movements. | comparison identity and matched condition | p. 8 (4) How intuitive is the system for new users?) |
| Similar to prior work [20, 22], these policies were learned within 20 minutes and achieved an average success rate of 82%, validating the high ... | comparison identity and matched condition | p. 6 (4) How intuitive is the system for new users?) |
| The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in this case, ... | comparison identity and matched condition | p. 6 (4) How intuitive is the system for new users?) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Each setup is a combination of a variant of a robot arm with either an Allegro Hand or a 2-fingered gripper. | component/input/data sensitivity | p. 6 (4) How intuitive is the system for new users?) |
| The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in this case, ... | component/input/data sensitivity | p. 6 (4) How intuitive is the system for new users?) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting ... | Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 13 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Primary metric/result | Similar to prior work [20, 22], these policies were learned within 20 minutes and achieved an average success rate of 82%, validating the high ... | numeric claim only at cited anchor | p. 6 (4) How intuitive is the system for new users?) |

- Numeric sentences retained from the body:
- **p. 6 / IV. OPEN TEACH - extractive body cue:** The Allegro hand's streaming frequency is configured at 60 Hz, while the xArm, Franka Emika Panka, and Kinova Jaco arms are set to 90 Hz, ...
- **p. 6 / IV. OPEN TEACH - extractive body cue:** The Hello Stretch is controlled at 5Hz using the controller released by Shafiullah et al.
- **p. 2 / Abstract - extractive body cue:** Using natural hand gestures and movements, users can manipulate robots at up to 90Hz with smooth visual feedback and interface widgets offering closeup environment views.
- **p. 2 / Abstract - extractive body cue:** We demonstrate the versatility of OPEN TEACH across 38 tasks on different robots.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To control the robot, users can simply use hand gestures, which are detected using onboard hand-pose estimators at 90Hz.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We experimentally evaluate OPEN TEACH on 38 tasks across single arm, bimanual, multi-fingered, and mobile manipulation robot setups in both simulation and the real world.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the ... | p. 8 (VI. LIMITATIONS AND DISCUSSION) |
| body limitation/failure cue | Fig. 3: The demonstration collection process as viewed from within the VR application. Shown here is one task being performed for each real-world setup. ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For both of these methods, the first phase involves obtaining a non-parametric base-policy πb : Z →A with encoded representations z ∈Z and actions ... | p. 3 (III. BACKGROUND ON IMITATION LEARNING) |
| Robot Hand: We use the teacher's hand pose obtained from the VR to compute the individual joint angles in the teacher's hand. | p. 4 (IV. OPEN TEACH) |
| Human-to-Robot Retargeting Hardware Network Server Hand Pose Detection Pose Detection Wrist Pose Detection Camera Stream Visual Feedback Oculus Passthrough Fig. | p. 4 (III. BACKGROUND ON IMITATION LEARNING) |
| The simplicity of the proposed framework has been summarized in Code Snippet 1. | p. 5 (IV. OPEN TEACH) |
| To mitigate steady-state error, we include a gravity compensation module to compute offset torques. | p. 5 (IV. OPEN TEACH) |
| Details about these implementations have been included in Appendix A. | p. 6 (IV. OPEN TEACH) |
| The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in this case, ... | p. 6 (4) How intuitive is the system for new users?) |
| Following this, they are tasked with performing five trials for each of three distinct tasks using Holo-Dex [4], AnyTeleop [47], and OPEN TEACH. | p. 8 (4) How intuitive is the system for new users?) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VI. LIMITATIONS AND DISCUSSION - extractive body cue:** However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: The demonstration collection process as viewed from within the VR application. Shown here is one task being performed for each real-world setup. High ...

- **PDF anchors reviewed:** datasets p. 6 (4) How intuitive is the system for new users?), p. 6 (V. EXPERIMENTAL EVALUATION), p. 8 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 7 (4) How intuitive is the system for new users?), metrics p. 8 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?), p. 13 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 8 (4) How intuitive is the system for new users?), p. 5 (Figure/Table caption), p. 8 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?), results p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 13 (Figure/Table caption), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
