# Evaluation - Habitat 3.0: A Co-Habitat for Humans, Avatars, and Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/430894999584d0bd358611e2ecf00b15-Abstract-Conference.html; PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/430894999584d0bd358611e2ecf00b15-Abstract-Conference.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 25 (Figure/Table caption), p. 19 (A.2 SOCIAL REARRANGEMENT), p. 17 (A.1 SOCIAL NAVIGATION), p. 9 (Figure/Table caption), p. 18 (Figure/Table caption)): Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of removing sensors. Scenes and Robot. We ...

## Evaluation Body Digest

- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** In all episodes, to make sure that the robot learns to find the humanoid, the robot location is initialized at least 3m away from the ...
- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** To compute this measure, we split the humanoid trajectory into equally spaced waypoints, we then use a path planner to measure the number of steps ...
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects or placing an ...
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** During training, the episode terminates if there is a collision between the humanoid and the robot.
- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** This ensures that the robot arm camera does not penetrate walls or obstacles while allowing the robot to navigate in a cluttered scene.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We work with a known, fixed library of low-level skills that can accomplish instructions like "navigate to the fridge" or "pick an apple." For the ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** These skills do not use privileged information, and hence are more prone to failures in the diverse set of scenes considered in our tasks.
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** This results in reactive behaviors, like the high-level policy commanding the robot to move backwards to give way to the humanoid in narrow corridors, or ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** A IMPLEMENTATION DETAILS (p. 16); C DETAILED COMPARISON RESULTS (p. 21); C.2.2 ADDITIONAL ABLATION RESULTS AND ANALYSIS (p. 23).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 9: Robot Embodiment. Spot robot in the simulation environment is designed to minimize the embodiment gaps to the robot in the physical world. ... | p. 25 (Figure/Table caption) |
| A.2 SOCIAL REARRANGEMENT | BENCHMARK / DATASET | This performance can potentially be improved by training the high-level policy with learned low-level skills in-the-loop, or by fine-tuning in this setting. | p. 19 (A.2 SOCIAL REARRANGEMENT) |
| A.1 SOCIAL NAVIGATION | BENCHMARK / DATASET | We see that the agent is able to improve the reward while minimizing the distance to the humanoid for finding and following the humanoid ... | p. 17 (A.1 SOCIAL NAVIGATION) |
| Figure/Table caption | BENCHMARK / DATASET | Table 1: Human-in-the-Loop Coordination Results. We report estimated mean and 95% confidence intervals (CI) across 30 participants. drop in performance. Removing the humanoid-GPS results ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** In all episodes, to make sure that the robot learns to find the humanoid, the robot location is initialized at least 3m away from the ...
- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** To compute this measure, we split the humanoid trajectory into equally spaced waypoints, we then use a path planner to measure the number of steps ...
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects or placing an ...
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** During training, the episode terminates if there is a collision between the humanoid and the robot.
- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** This ensures that the robot arm camera does not penetrate walls or obstacles while allowing the robot to navigate in a cluttered scene.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We work with a known, fixed library of low-level skills that can accomplish instructions like "navigate to the fridge" or "pick an apple." For the ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** These skills do not use privileged information, and hence are more prone to failures in the diverse set of scenes considered in our tasks.
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** This results in reactive behaviors, like the high-level policy commanding the robot to move backwards to give way to the humanoid in narrow corridors, or ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Habitat 3.0: An Embodied AI framework designed to facilitate simulation of human avatars and robotic agents within a wide array of indoor environments. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Humanoid Avatars. Visualization of the skeleton rig and skinned mesh (a). A subset of the sampled avatars featuring distinct genders, body shapes, and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of removing ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Overview of social rearrangement (left). Baseline results, averaged over 3 seeds (right).
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Human-in-the-Loop Coordination Results. We report estimated mean and 95% confidence intervals (CI) across 30 participants. drop in performance. Removing the humanoid-GPS results in ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 5: Social Navigation training curves. We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations. We ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 6: Social Rearrangement training curves. We plot the training success and reward for the social rearrangement baselines (top) and ablations (bottom). We use 3 ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 2: Social Navigation baseline results. We report three additional metrics: (1) Backup-Yield Rate (BYR), (2) The Total Distance between the robot and the humanoid ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In all episodes, to make sure that the robot learns to find the humanoid, the robot location is initialized at least 3m away from ... | embodiment, simulator version and control stack | p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION) |
| Task/environment | To compute this measure, we split the humanoid trajectory into equally spaced waypoints, we then use a path planner to measure the number of ... | reset, timeout, object/scene variation | p. 17 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 17 (A.2 SOCIAL REARRANGEMENT), p. 2 (1 INTRODUCTION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 17 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 9: Robot Embodiment. Spot robot in the simulation environment is designed to minimize the embodiment gaps to the robot in the physical world. ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |
| The final social navigation reward is as follows: rsocial-nav t = 10⊮success + rdistance t + 3rorientation t -0.1. | definition/direction/unit from same section | p. 16 (A.1 SOCIAL NAVIGATION) |
| The robot receives a bonus reward of +10 if the robot successfully maintains a safety distance between 1m and 2m to the humanoid and ... | definition/direction/unit from same section | p. 16 (A.1 SOCIAL NAVIGATION) |
| The final social rearrangement reward is as follows: rsocial-rearrange t = 10 · ⊮success + 5 · ⊮subgoal -5 · ⊮collision -0.005. | definition/direction/unit from same section | p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations. | definition/direction/unit from same section | p. 17 (A.1 SOCIAL NAVIGATION) |
| We see that the agent is able to improve the reward while minimizing the distance to the humanoid for finding and following the humanoid ... | definition/direction/unit from same section | p. 17 (A.1 SOCIAL NAVIGATION) |
| We plot the training success and reward for the social rearrangement baselines (top) and ablations (bottom). | definition/direction/unit from same section | p. 18 (A.2 SOCIAL REARRANGEMENT) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5: Social Navigation training curves. We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations. ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| 6 shows learning curves for all baselines and ablations on the social rearrangement task. | comparison identity and matched condition | p. 18 (A.2 SOCIAL REARRANGEMENT) |
| We plot the training success and reward for the social rearrangement baselines (top) and ablations (bottom). | comparison identity and matched condition | p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 4: Overview of social rearrangement (left). Baseline results, averaged over 3 seeds (right). | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| All baselines are trained with 3 different random seeds, and results are reported averaged across those seeds. | comparison identity and matched condition | p. 16 (A.1 SOCIAL NAVIGATION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Among the ablations, removing the sensors used in original training make learning slower, with primitive actions having the most effect. | component/input/data sensitivity | p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Figure 12: Benchmark results in Habitat 3.0. We study the effect of varying scene size, number of objects, type of agents and single or ... | component/input/data sensitivity | p. 28 (Figure/Table caption) |
| We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations. | component/input/data sensitivity | p. 17 (A.1 SOCIAL NAVIGATION) |
| 5 shows the average distance between the humanoid and the robot and reward learning curve over the number of simulation steps for the end-to-end ... | component/input/data sensitivity | p. 17 (A.1 SOCIAL NAVIGATION) |
| 6 shows learning curves for all baselines and ablations on the social rearrangement task. | component/input/data sensitivity | p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each. | Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 25 (Figure/Table caption), p. 19 (A.2 SOCIAL REARRANGEMENT), p. 17 (A.1 SOCIAL NAVIGATION), p. 9 (Figure/Table caption), p. 18 (Figure/Table caption) |
| Primary metric/result | Figure 9: Robot Embodiment. Spot robot in the simulation environment is designed to minimize the embodiment gaps to the robot in the physical world. ... | numeric claim only at cited anchor | p. 25 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** Each GPU runs 24 parallel environments, and collects 128 steps for each update.
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** During evaluation, the total episode length is 1500 steps and the episode terminates if there is a collision between the humanoid and the robot.
- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** We use 3 seeds for each model. path are fixed across the baselines.
- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** Each GPU runs 24 parallel environments, and collects 128 steps for each update.
- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We use 2 PPO minibatches and 1 epoch per update, an entropy loss of 1e-4, and clip the gradient norm to 0.2.
- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The policy uses a ResNet-18 (He et al., 2016) visual encoder to embed the 256 × 256 depth input image into a 512 dimension embedding.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Since the Spot robot has a long body shape and cannot be represented by a single cylinder, we use a 2-cylinder representation, placed in ... | p. 17 (A.1 SOCIAL NAVIGATION) |
| body limitation/failure cue | Hence the high-level policy is not robust to low-level execution failures. | p. 19 (A.2 SOCIAL REARRANGEMENT) |
| body limitation/failure cue | These skills do not use privileged information, and hence are more prone to failures in the diverse set of scenes considered in our tasks. | p. 19 (A.2 SOCIAL REARRANGEMENT) |
| body limitation/failure cue | During training, the episode terminates if there is a collision between the humanoid and the robot. | p. 16 (A.1 SOCIAL NAVIGATION) |
| body limitation/failure cue | Figure 5: Social Navigation training curves. We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations. ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | The final social rearrangement reward is as follows: rsocial-rearrange t = 10 · ⊮success + 5 · ⊮subgoal -5 · ⊮collision -0.005. | p. 18 (A.2 SOCIAL REARRANGEMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each GPU runs 24 parallel environments, and collects 128 steps for each update. | p. 16 (A.1 SOCIAL NAVIGATION) |
| To compute the Finding Success Weighted by Path Steps and Following rate, we need to measure the optimal finding time l. | p. 17 (A.1 SOCIAL NAVIGATION) |
| To compute this measure, we split the humanoid trajectory into equally spaced waypoints, we then use a path planner to measure the number of ... | p. 17 (A.1 SOCIAL NAVIGATION) |
| We use a learning rate of 1 × 10-4 and the maximum gradient norm of 0.2. | p. 16 (A.1 SOCIAL NAVIGATION) |
| We present the overall task success as well as the training reward for all approaches, averaged over 3 seeds. | p. 18 (A.2 SOCIAL REARRANGEMENT) |
| All baselines are trained with three different random seeds, and results are reported averaged across those seeds. | p. 18 (A.2 SOCIAL REARRANGEMENT) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** Since the Spot robot has a long body shape and cannot be represented by a single cylinder, we use a 2-cylinder representation, placed in the ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** Hence the high-level policy is not robust to low-level execution failures.
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** These skills do not use privileged information, and hence are more prone to failures in the diverse set of scenes considered in our tasks.
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** During training, the episode terminates if there is a collision between the humanoid and the robot.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 5: Social Navigation training curves. We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations. We ...
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The final social rearrangement reward is as follows: rsocial-rearrange t = 10 · ⊮success + 5 · ⊮subgoal -5 · ⊮collision -0.005.

- **Evidence anchors reviewed:** datasets p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT), metrics p. 25 (Figure/Table caption), p. 16 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 7 (Figure/Table caption), p. 17 (A.1 SOCIAL NAVIGATION), baselines p. 17 (Figure/Table caption), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 16 (A.1 SOCIAL NAVIGATION), results p. 7 (Figure/Table caption), p. 25 (Figure/Table caption), p. 19 (A.2 SOCIAL REARRANGEMENT), p. 17 (A.1 SOCIAL NAVIGATION), p. 9 (Figure/Table caption), p. 18 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
