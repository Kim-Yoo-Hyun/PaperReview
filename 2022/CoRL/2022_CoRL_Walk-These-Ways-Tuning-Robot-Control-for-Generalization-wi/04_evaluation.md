# Evaluation - Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/margolis23a.html; PDF retrieval source: https://arxiv.org/pdf/2212.03238. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (Figure/Table caption), p. 7 (3 Method), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 4 (3 Method), p. 5 (3 Method)): Table 5: Removing gait constraints results in improved velocity tracking task performance on flat ground. Heat maps (right) break down the mean task reward for each velocity command, revealing that ...

## Evaluation Body Digest

- **p. 8 / 3 Method - extractive body cue:** In a real-world example, the robot was able to crawl under a 22 cm bar; the robot body thickness is 13 cm, leaving 9 cm ...
- **p. 5 / 3 Method - extractive body cue:** During training, one concern is that the robot might abandon its task or choose an early termination when the task reward is overwhelmed by penalties ...
- **p. 5 / 3 Method - extractive body cue:** However, this penalizes the robot during fast turning tasks requiring relative lateral motion of the feet.
- **p. 7 / 3 Method - extractive body cue:** Payload manipulation: We experiment with another task where the robot is required to transport a ball from one place to another, then bend its body ...
- **p. 8 / 3 Method - extractive body cue:** 5 Discussion and Limitations Our experiments show that the benefits of adding MoB can come at a cost to in-distribution task performance, specifically limiting the ...
- **p. 6 / 3 Method - extractive body cue:** We deploy our controller in the real world on the Unitree Go1 Edu robot [27].
- **p. 6 / 3 Method - extractive body cue:** We perform system identification to reduce the sim-to-real gap in the robot dynamics.
- **p. 7 / 3 Method - extractive body cue:** Navigating confined spaces: Consider the scenario where the robot needs to go under a bar.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Removing gait constraints results in improved velocity tracking task performance on flat ground. Heat maps (right) break down the mean task reward ... | p. 11 (Figure/Table caption) |
| 3 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | Therefore, it is possible to improve performance in an out-of-distribution terrain by modulating the parameters of the MoB policy. | p. 7 (3 Method) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Zero-shot generalization to platform terrain (visualized right). Pacing and trotting yield the best survival time in out-of-distribution deployment, outperforming the gait-free baseline. ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 11: Flat Ground Velocity Tracking Heatmaps: We provide heatmaps as in Table 5 for the other major gaits: pronking, pacing, and bounding. In ... | p. 14 (Figure/Table caption) |
| 3 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | To obtain MoB, we train a conditional policy π(·/ct, bt) that achieves tasks specified by the command (ct) in multiple ways that result from ... | p. 4 (3 Method) |

## Dataset / Benchmark Role

- **p. 8 / 3 Method - extractive body cue:** In a real-world example, the robot was able to crawl under a 22 cm bar; the robot body thickness is 13 cm, leaving 9 cm ...
- **p. 5 / 3 Method - extractive body cue:** During training, one concern is that the robot might abandon its task or choose an early termination when the task reward is overwhelmed by penalties ...
- **p. 5 / 3 Method - extractive body cue:** However, this penalizes the robot during fast turning tasks requiring relative lateral motion of the feet.
- **p. 7 / 3 Method - extractive body cue:** Payload manipulation: We experiment with another task where the robot is required to transport a ball from one place to another, then bend its body ...
- **p. 8 / 3 Method - extractive body cue:** 5 Discussion and Limitations Our experiments show that the benefits of adding MoB can come at a cost to in-distribution task performance, specifically limiting the ...
- **p. 6 / 3 Method - extractive body cue:** We deploy our controller in the real world on the Unitree Go1 Edu robot [27].
- **p. 6 / 3 Method - extractive body cue:** We perform system identification to reduce the sim-to-real gap in the robot dynamics.
- **p. 7 / 3 Method - extractive body cue:** Navigating confined spaces: Consider the scenario where the robot needs to go under a bar.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Multiplicity of Behavior (MoB) enables a human to tune a single quadruped policy trained on flat ground to diverse unseen environments. Top row: ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: A learned controller transitions between classical structured gaits: trotting, pronking, pac- ing, and bounding in place at alternating frequencies 2Hz and 4Hz. Images ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Reward structure: task rewards, augmented auxiliary rewards, and fixed auxiliary rewards. Task Augmented Auxiliary Fixed Auxiliary 3
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: Behavior tuning enables interventional studies on the relationship between gait proper- ties and performance criteria within a single policy. Here, we illustrate how ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4: Zero-shot generalization to platform terrain (visualized right). Pacing and trotting yield the best survival time in out-of-distribution deployment, outperforming the gait-free baseline. Pronk- ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: We demonstrate that behavior transitions can be performed even in quick sequence at high speed for synthesis of agile maneuvers. Emulating gap crossing ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 5: Removing gait constraints results in improved velocity tracking task performance on flat ground. Heat maps (right) break down the mean task reward for ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 6: Randomization ranges for dynam- ics parameters (top) and commands (bottom) during training. vcmd x , ωcmd z are adapted ac- cording to a ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In a real-world example, the robot was able to crawl under a 22 cm bar; the robot body thickness is 13 cm, leaving 9 ... | embodiment, simulator version and control stack | p. 8 (3 Method), p. 5 (3 Method) |
| Task/environment | During training, one concern is that the robot might abandon its task or choose an early termination when the task reward is overwhelmed by ... | reset, timeout, object/scene variation | p. 5 (3 Method), p. 5 (3 Method) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 5 (3 Method) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (1 Introduction), p. 4 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 4: Zero-shot generalization to platform terrain (visualized right). Pacing and trotting yield the best survival time in out-of-distribution deployment, outperforming the gait-free baseline. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 3: Behavior tuning enables interventional studies on the relationship between gait proper- ties and performance criteria within a single policy. Here, we illustrate ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| For example, when implementing stance width as a behavior parameter, a naive approach would be to simply reward a constant desired distance between left ... | definition/direction/unit from same section | p. 5 (3 Method) |
| To quantify and control the tradeoff between task performance and reward shaping is an interesting future direction, for which some prior methods have been ... | definition/direction/unit from same section | p. 8 (3 Method) |
| Table 5: Removing gait constraints results in improved velocity tracking task performance on flat ground. Heat maps (right) break down the mean task reward ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Figure 10: Frequency vs Speed: Impact of trot- ting frequency on flat-ground velocity tracking reward across speeds (Section 4.2). Enforcing low frequency (2Hz) makes ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| All reward terms are listed in Table 1. | definition/direction/unit from same section | p. 4 (3 Method) |
| Auxiliary rewards are used constrain the 4 | definition/direction/unit from same section | p. 4 (3 Method) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Pacing and trotting yield the best survival time in out-of-distribution deployment, outperforming the gait-free baseline. | comparison identity and matched condition | p. 7 (3 Method) |
| Here, we illustrate how power consumption varies across speeds for common quadrupedal gaits and for a baseline policy without gait constraint. | comparison identity and matched condition | p. 6 (3 Method) |
| The Raibert Heuristic computes the desired foot position in the ground plane, pf,cmd x,y,foot(scmd y ), as an adjustment to the baseline stance width ... | comparison identity and matched condition | p. 5 (3 Method) |
| The gait-free baseline is trained by the method above, but excludes all augmented auxiliary rewards (Table 1). | comparison identity and matched condition | p. 6 (3 Method) |
| Pronking attains the best velocity tracking performance, with similar survival time to the baseline. | comparison identity and matched condition | p. 7 (3 Method) |
| Figure 9: Footswing Height vs Robustness: Impact of footswing height on time to failure on the platform terrain (Section 4.2). Increased footswing height yields ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3: Behavior tuning enables interventional studies on the relationship between gait proper- ties and performance criteria within a single policy. Here, we illustrate ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| As we are interested in studying out-of-distribution generalization, we only train on flat ground without any randomization of terrain geometry. | component/input/data sensitivity | p. 5 (3 Method) |
| In contrast, with the help of a human pilot, our gait-conditioned policy with high footswing command enables fast and smooth obstacle traversal without tripping, ... | component/input/data sensitivity | p. 7 (3 Method) |
| This interferes with performance in other tasks like running efficiently, so learned locomotion controllers without MoB often provide incentive to keep the feet nominally ... | component/input/data sensitivity | p. 8 (3 Method) |
| Table 5: Removing gait constraints results in improved velocity tracking task performance on flat ground. Heat maps (right) break down the mean task reward ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present a framework for policy learning that enables improved performance in out-of-distribution scenarios under some assumptions detailed below. | Table 5: Removing gait constraints results in improved velocity tracking task performance on flat ground. Heat maps (right) break down the mean task reward ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (Figure/Table caption), p. 7 (3 Method), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 4 (3 Method), p. 5 (3 Method) |
| Primary metric/result | Therefore, it is possible to improve performance in an out-of-distribution terrain by modulating the parameters of the MoB policy. | numeric claim only at cited anchor | p. 7 (3 Method) |

- Numeric sentences retained from the body:
- **p. 4 / 3 Method - extractive body cue:** 3.1 Task Structure for MoB Task Specification.
- **p. 4 / 3 Method - extractive body cue:** As an example, commanding f cmd = 3 Hz will result in each foot making contact three times per second. hcmd z is the body ...
- **p. 6 / 3 Method - extractive body cue:** Gait 0.0 m/s 1.0 m/s 2.0 m/s 3.0 m/s Trotting 9±1 24±1 53±5 98±9 Pronking 32±1 43±2 68±5 112±5 Pacing 13±3 25±2 55±3 99±6 Bounding ...
- **p. 6 / 3 Method - extractive body cue:** Separately, we identify a latency of around 20 ms in our system and model this as a constant action delay during simulation.
- **p. 6 / 3 Method - extractive body cue:** For both training and deployment, the control frequency is 50Hz.
- **p. 7 / 3 Method - extractive body cue:** We report two metrics: mean reward and mean survival time as a fraction of the maximum episode length (10 s).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: Multiplicity of Behavior (MoB) enables a human to tune a single quadruped policy trained on flat ground to diverse unseen environments. Top ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Table 5. Forward and Backward Locomotion. During evaluation in the random platforms environment, we found that walking backward leads to fewer failures than walking ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | Figure 8: Forward vs Backward Walking on Platforms. Time to failure for different gaits and velocities in the random platforms environment (zero-shot test). The ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | Figure 9: Footswing Height vs Robustness: Impact of footswing height on time to failure on the platform terrain (Section 4.2). Increased footswing height yields ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Therefore, prior works would either attempt to climb over bushes as obstacles or fall back on a robust proprioceptive controller that is unaware of ... | p. 7 (3 Method) |
| body limitation/failure cue | The gait-free baseline cannot accomplish this; in the absence of such constraints during training, it will 7 | p. 7 (3 Method) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To enable the robot to both run and spin fast, we sample task ct = (vcmd x , vcmd y , ωcmd z ) ... | p. 5 (3 Method) |
| The observation space ot consists of joint positions and velocities qt, ˙qt (measured by joint encoders) and the gravity vector in the body frame ... | p. 5 (3 Method) |
| An onboard Jetson TX2 NX computer runs our trained policy. | p. 6 (3 Method) |
| We implement an interface based on Lightweight Communications and Marshalling (LCM) [28] to pass sensor data, motor commands, and joystick state between our code ... | p. 6 (3 Method) |
| Subscript reports standard deviation across three random seeds. | p. 7 (3 Method) |
| At this tempo, combinations of phases 0, 0.25, and 0.5 with frequencies of 1.5 Hz and 3 Hz yield eighth, quarter, half, and full ... | p. 8 (3 Method) |
| Agile forward leap: As a demonstration of gait transitions at high speed, we modulate contact schedule, velocity, and gait frequency at to encode an ... | p. 8 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Multiplicity of Behavior (MoB) enables a human to tune a single quadruped policy trained on flat ground to diverse unseen environments. Top row: ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 5. Forward and Backward Locomotion. During evaluation in the random platforms environment, we found that walking backward leads to fewer failures than walking forward. ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 8: Forward vs Backward Walking on Platforms. Time to failure for different gaits and velocities in the random platforms environment (zero-shot test). The temperature ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 9: Footswing Height vs Robustness: Impact of footswing height on time to failure on the platform terrain (Section 4.2). Increased footswing height yields better ...
- **p. 7 / 3 Method - extractive body cue:** Therefore, prior works would either attempt to climb over bushes as obstacles or fall back on a robust proprioceptive controller that is unaware of the ...
- **p. 7 / 3 Method - extractive body cue:** The gait-free baseline cannot accomplish this; in the absence of such constraints during training, it will 7

- **PDF anchors reviewed:** datasets p. 8 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method), metrics p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (3 Method), p. 8 (3 Method), p. 11 (Figure/Table caption), p. 14 (Figure/Table caption), baselines p. 7 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 14 (Figure/Table caption), results p. 11 (Figure/Table caption), p. 7 (3 Method), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 4 (3 Method), p. 5 (3 Method).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
