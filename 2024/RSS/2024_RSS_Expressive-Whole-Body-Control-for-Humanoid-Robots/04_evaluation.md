# Evaluation - Expressive Whole-Body Control for Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p107.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p107.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 9 (Figure/Table caption), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 7 (IV. RESULTS)): V, our method achieves the best linear velocity tracking performance (MELV).

## Evaluation Body Digest

- **p. 5 / IV. RESULTS - extractive PDF cue:** In this section we aim to answer the following questions through extensive experiments both in sim and the real world: • How well does ExBody ...
- **p. 6 / IV. RESULTS - extractive PDF cue:** In our work, we show the advantage of learning robust Whole-Body control for humanoid robots from large motion datasets.
- **p. 5 / IV. RESULTS - extractive PDF cue:** II. • No RSI: Initialize the environment with default DoF positions and root states instead of sampling from the motion dataset. • Full body tracking: ...
- **p. 7 / IV. RESULTS - extractive PDF cue:** However we can still see that it works better on a small O.O.D dataset than a large training set.
- **p. 6 / IV. RESULTS - extractive PDF cue:** Due to the limited torque, DoFs of the real robot, we design ExBody to only mimic the arm motions ge ∼Ge while the wholebody's objective ...
- **p. 7 / IV. RESULTS - extractive PDF cue:** 7: We sample 20-second simulation rollouts with 4096 environments and take the mean episode length as our metric.
- **p. 8 / IV. RESULTS - extractive PDF cue:** We choose the uptown funk motion from O.O.D. dataset form II From Fig.
- **p. 8 / IV. RESULTS - extractive PDF cue:** The top row shows the robot motions and original dance video snapshots.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** IV. RESULTS (p. 5); C. Dataset Visualization (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | V, our method achieves the best linear velocity tracking performance (MELV). | p. 6 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, even with a reduced sampling range, the performance is significantly worse than ours, indicating ExBody's advantage in overcoming conflicts of objectives problems. | p. 6 (IV. RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 11: Text2Motion trajectories replay. A motion sequence is prompted offline with the input "a man mimics boxing punches" through MDM [64]. Our robot ... | p. 9 (Figure/Table caption) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5, we study whether velocity goal vx will affect the performance of other goals. | p. 5 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The average performance is not directly implied from the heatmap and is further discussed in Tab. | p. 5 (IV. RESULTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. RESULTS - extractive PDF cue:** In this section we aim to answer the following questions through extensive experiments both in sim and the real world: • How well does ExBody ...
- **p. 6 / IV. RESULTS - extractive PDF cue:** In our work, we show the advantage of learning robust Whole-Body control for humanoid robots from large motion datasets.
- **p. 5 / IV. RESULTS - extractive PDF cue:** II. • No RSI: Initialize the environment with default DoF positions and root states instead of sampling from the motion dataset. • Full body tracking: ...
- **p. 7 / IV. RESULTS - extractive PDF cue:** However we can still see that it works better on a small O.O.D dataset than a large training set.
- **p. 6 / IV. RESULTS - extractive PDF cue:** Due to the limited torque, DoFs of the real robot, we design ExBody to only mimic the arm motions ge ∼Ge while the wholebody's objective ...
- **p. 7 / IV. RESULTS - extractive PDF cue:** 7: We sample 20-second simulation rollouts with 4096 environments and take the mean episode length as our metric.
- **p. 8 / IV. RESULTS - extractive PDF cue:** We choose the uptown funk motion from O.O.D. dataset form II From Fig.
- **p. 8 / IV. RESULTS - extractive PDF cue:** The top row shows the robot motions and original dance video snapshots.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Our Robot demonstrates diverse and expressive whole-body movements in different scenarios. Top Row: The robot is dancing, hugging and doing high-five with a ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overview of our framework. Our framework is able to train on data from various sources such as static human motion datasets, generative models, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Left: During training, we extract a large repertoire of retargeted motion clips and train our ExBody policy. Right: During deployment, we can replay ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: We sample 10,000 points of hand positions relative to the robot. Left: retargeted motion dataset. Right: learned ExBody policy rollouts. The upper body ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5: Tracking error heatmaps for root movement goal Gm. Top row: goals sampled from MoCap motion dataset. Middle row: op row with the sampled ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: Random Sampling gm results in a behavior that the policy immediately kneels after initialization, trying to be as stable as possible while ignoring ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: We sample 20-second simulation rollouts with 4096 environments and take the mean episode length as our metric. The termination condition for an episode ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 8: H1 robot doing a High Five in the real world. Top Row: ExBody only (Ours) walks with more bent knees and has more ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In this section we aim to answer the following questions through extensive experiments both in sim and the real world: • How well does ... | embodiment, simulator version and control stack | p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Task/environment | In our work, we show the advantage of learning robust Whole-Body control for humanoid robots from large motion datasets. | reset, timeout, object/scene variation | p. 6 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, it has even worse performance, demonstrating a high-frequency jittery movement that is not feasible for sim-to-real transfer, indicating for such a complex system, ... | definition/direction/unit from same section | p. 7 (IV. RESULTS) |
| In areas where the sample density is sparse, the tracking error is slightly higher. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| 5 we can see that for the motion sample, the tracking error is very low where the sample density is dense. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| 5: Tracking error heatmaps for root movement goal Gm. | definition/direction/unit from same section | p. 6 (IV. RESULTS) |
| For the first two columns, the tracking error considers both x and y axes. | definition/direction/unit from same section | p. 6 (IV. RESULTS) |
| Unified policy is more robust than separate ones. | definition/direction/unit from same section | p. 7 (IV. RESULTS) |
| This phenomenon can be further evidenced by Full Body Tracking baseline having a poor performance compared to our method and is not able to ... | definition/direction/unit from same section | p. 8 (IV. RESULTS) |
| Fig. 15: Video-to-Motion evaluation. (a,b) The videos were self-recorded and subsequently processed offline using Move One [3] to create custom motions. (c,d) To assess ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare with baselines to show that our approach ExBody is superior compared with other design choices. | comparison identity and matched condition | p. 6 (IV. RESULTS) |
| This phenomenon can be further evidenced by Full Body Tracking baseline having a poor performance compared to our method and is not able to ... | comparison identity and matched condition | p. 8 (IV. RESULTS) |
| 19.26 330.33 828.99 683.97 15.39 179.26 583.04 498.05 TABLE V: Comparisons with baselines. | comparison identity and matched condition | p. 7 (IV. RESULTS) |
| IV Baseline vx vy roll pitch base height Random Sample ±2.0 ±1.0 ±0.5 ±0.5 [0.9, 1.1] Random Sample Small ±1.5 ±1.0 ±0.2 ±0.2 [0.9, ... | comparison identity and matched condition | p. 5 (IV. RESULTS) |
| In this section we aim to answer the following questions through extensive experiments both in sim and the real world: • How well does ... | comparison identity and matched condition | p. 5 (IV. RESULTS) |
| The Random Sample baseline's behavior is a kneel-down motion for all the goals as shown in Fig. | comparison identity and matched condition | p. 6 (IV. RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We can see that our policy can track roll, pitch and root height well without being affected by walking velocity. | component/input/data sensitivity | p. 5 (IV. RESULTS) |
| Our baselines are as follows: • ExBody + AMP: This baseline uses an AMP reward to encourage the policy's transitions to be similar to ... | component/input/data sensitivity | p. 5 (IV. RESULTS) |
| ExBody + AMP NoReg tries to replace the regularization terms in Tab. | component/input/data sensitivity | p. 7 (IV. RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach ... | V, our method achieves the best linear velocity tracking performance (MELV). | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 9 (Figure/Table caption), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 7 (IV. RESULTS) |
| Primary metric/result | However, even with a reduced sampling range, the performance is significantly worse than ours, indicating ExBody's advantage in overcoming conflicts of objectives problems. | numeric claim only at cited anchor | p. 6 (IV. RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. RESULTS - extractive PDF cue:** IV Baseline vx vy roll pitch base height Random Sample ±2.0 ±1.0 ±0.5 ±0.5 [0.9, 1.1] Random Sample Small ±1.5 ±1.0 ±0.2 ±0.2 [0.9, 1.1] ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** 4: We sample 10,000 points of hand positions relative to the robot.
- **p. 8 / IV. RESULTS - extractive PDF cue:** 10: We uniformly sample 4096 different vx ∈[0, 2] in root movement goal Gm with 15s for each vx.
- **p. 8 / IV. RESULTS - extractive PDF cue:** 9 with a moving window of length 4s.
- **p. 8 / IV. RESULTS - extractive PDF cue:** The linearly fitted stepping frequency when vx = 0 is slightly above 2.0Hz, while in Fig.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Auto recovery and initialization could be explored to reduce the cost of doing experiments. | p. 9 (VII. LIMITATIONS) |
| body limitation/failure cue | We introduce a method designed to enable a humanoid robot to track expressive upper body motions while ensuring the maintenance of robust locomotion capabilities ... | p. 9 (VI. DISCUSSIONS) |
| body limitation/failure cue | Note that although Random Sample looks better than Motion Sample, the heatmap does not consider the sample density. | p. 5 (IV. RESULTS) |
| body limitation/failure cue | Why does not ExBody do full DoF tracking? | p. 6 (IV. RESULTS) |
| body limitation/failure cue | Again our method does not require such manual tuning of curriculum to work. | p. 6 (IV. RESULTS) |
| body limitation/failure cue | Fig. 13: Policy's state distribution under different sampling strategies. The green dots are the policy rollout's states. For dataset sampling, we record 20 data ... | p. 15 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The bottom row is the computed step frequency f = n/∆t for each segment, where n and ∆t are the total steps and time ... | p. 8 (IV. RESULTS) |
| The PD controllers compute the torque for each motor with the specified PD gains ki p and damping coefficient ki d. b) Expressive Whole-Body ... | p. 3 (II. PROBLEM FORMULATION) |
| However, our proposed approach should generalize to similar body forms that differ in the exact number of actuated degrees of freedom. a) Command-conditioned Locomotion ... | p. 3 (II. PROBLEM FORMULATION) |
| In this section we aim to answer the following questions through extensive experiments both in sim and the real world: • How well does ... | p. 5 (IV. RESULTS) |
| The robot's lower body movements exhibit numerous artifacts, notably that while the reference motion is designed for a single step, the robot executes multiple ... | p. 6 (IV. RESULTS) |
| We first bin all sampled points into a grid of size 0.2x0.2 (regardless of the unit, except the grid size along y axis of ... | p. 6 (IV. RESULTS) |
| We compute the step frequency using the same method in Fig. | p. 8 (IV. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / VII. LIMITATIONS - extractive PDF cue:** Auto recovery and initialization could be explored to reduce the cost of doing experiments.
- **p. 9 / VI. DISCUSSIONS - extractive PDF cue:** We introduce a method designed to enable a humanoid robot to track expressive upper body motions while ensuring the maintenance of robust locomotion capabilities in ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** Note that although Random Sample looks better than Motion Sample, the heatmap does not consider the sample density.
- **p. 6 / IV. RESULTS - extractive PDF cue:** Why does not ExBody do full DoF tracking?
- **p. 6 / IV. RESULTS - extractive PDF cue:** Again our method does not require such manual tuning of curriculum to work.
- **p. 15 / Figure/Table caption - extractive PDF cue:** Fig. 13: Policy's state distribution under different sampling strategies. The green dots are the policy rollout's states. For dataset sampling, we record 20 data points ...

- **PDF anchors reviewed:** datasets p. 5 (IV. RESULTS), p. 6 (IV. RESULTS), p. 5 (IV. RESULTS), p. 7 (IV. RESULTS), p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), metrics p. 7 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), baselines p. 6 (IV. RESULTS), p. 8 (IV. RESULTS), p. 7 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS), results p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 9 (Figure/Table caption), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 7 (IV. RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
