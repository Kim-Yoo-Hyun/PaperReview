# Evaluation - ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.11575; PDF retrieval source: https://arxiv.org/pdf/2602.11575. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS)): As in simulation, ReaDy-Go and Vid2Sim achieve comparable success rates in Static, but their performance diverges in Dynamic.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For each task and environment, we evaluate 100 episodes in simulation and 10 episodes in real-world experiments.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For this experiment, the policy is trained on the combined datasets from three environments, i.e., a total of 1,200 episodes from Outside, Lobby, and Library.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The validation scenarios consist of 50 episodes for each environment, and we selected the checkpoint with the best validation performance, which is used for testing ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** These results highlight the importance of incorporating photorealistic dynamic obstacles into the simulation pipeline to achieve robust navigation performance in dynamic real-world environments.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** ReaDy-Go generates photorealistic, geometrically consistent dynamic scenarios with natural human motion from novel viewpoints, enabling navigation dataset generation for target deployment environments.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Visual Navigation Performance in Simulation The impact of photorealistic dynamic GS simulation datasets on visual navigation policies is examined through simulation tests comparing ReaDy-Go against ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** 2) Evaluation metrics: We evaluate navigation performance using Success Rate (SR) and Average Reaching Time (ART).
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** ReaDy-Go maintains high success rates and low average reaching times relatively well, whereas Vid2Sim exhibits a substantial performance drop.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As in simulation, ReaDy-Go and Vid2Sim achieve comparable success rates in Static, but their performance diverges in Dynamic. | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | ReaDy-Go achieves comparable success rates in both Static and Dynamic in the real world, consistent with its simulation results across all environments, even though ... | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | ReaDy-Go and Vid2Sim, both trained in real-to-sim target environments, achieve higher success rates and lower average reaching times than general navigation models (GNM, NoMaD, ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Since the two methods differ only in the training data, i.e., photorealistic human GS dynamic obstacles for ReaDy-Go versus human assets in a physics ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2) Evaluation metrics: We evaluate navigation performance using Success Rate (SR) and Average Reaching Time (ART). | p. 5 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For each task and environment, we evaluate 100 episodes in simulation and 10 episodes in real-world experiments.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For this experiment, the policy is trained on the combined datasets from three environments, i.e., a total of 1,200 episodes from Outside, Lobby, and Library.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The validation scenarios consist of 50 episodes for each environment, and we selected the checkpoint with the best validation performance, which is used for testing ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** These results highlight the importance of incorporating photorealistic dynamic obstacles into the simulation pipeline to achieve robust navigation performance in dynamic real-world environments.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** ReaDy-Go generates photorealistic, geometrically consistent dynamic scenarios with natural human motion from novel viewpoints, enabling navigation dataset generation for target deployment environments.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Visual Navigation Performance in Simulation The impact of photorealistic dynamic GS simulation datasets on visual navigation policies is examined through simulation tests comparing ReaDy-Go against ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The proposed real-to-sim dynamic environment sim- ulation pipeline for visual navigation. ReaDy-Go generates photorealistic navigation datasets for dynamic scenarios and trains environment-specific visual ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: ReaDy-Go overview. The proposed photorealistic simulation pipeline for visual navigation in dynamic environments consists of three main components: (1) a real-to-sim dynamic 3D ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Visualization of the robot expert planner. (a) The robot follows a collision-free path (red) from start (green) to goal (blue). (b) When a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Qualitative novel-view synthesis results from the proposed dynamic GS simulation pipeline across diverse viewpoints and environments. ReaDy-Go generates photorealistic, geometrically consistent dynamic scenarios ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. First, the proposed human animation module generates plausible body motions for human GS avatars within static GS scenes along given 2D trajectories, without ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Failure case analysis in real-world experiments. ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Qualitative real-world navigation results. ReaDy-Go avoids a dynamic obstacle, while the baselines collide with it. target environments with six previously unseen humans. For ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 1. The policy achieves over a 50% success rate in both Static and Dynamic, with a higher average reaching time than in the training ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For each task and environment, we evaluate 100 episodes in simulation and 10 episodes in real-world experiments. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Task/environment | For this experiment, the policy is trained on the combined datasets from three environments, i.e., a total of 1,200 episodes from Outside, Lobby, and ... | reset, timeout, object/scene variation | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 2) Evaluation metrics: We evaluate navigation performance using Success Rate (SR) and Average Reaching Time (ART). | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| ReaDy-Go maintains high success rates and low average reaching times relatively well, whereas Vid2Sim exhibits a substantial performance drop. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| As in simulation, ReaDy-Go and Vid2Sim achieve comparable success rates in Static, but their performance diverges in Dynamic. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| ReaDy-Go shows the highest success rate and the lowest average reaching time in Dynamic, with only a slight performance degradation compared to Static. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| ReaDy-Go and Vid2Sim, both trained in real-to-sim target environments, achieve higher success rates and lower average reaching times than general navigation models (GNM, NoMaD, ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| In this section, we evaluate the visual navigation performance in dynamic environments and the robustness to sim-to-real transfer of ReaDy-Go visual navigation policies trained ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 1: The proposed real-to-sim dynamic environment sim- ulation pipeline for visual navigation. ReaDy-Go generates photorealistic navigation datasets for dynamic scenarios and trains environment-specific ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 3: Visualization of the robot expert planner. (a) The robot follows a collision-free path (red) from start (green) to goal (blue). (b) When ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For a fair comparison with image-goal navigation baselines (GNM, ViNT, and NoMaD), we provide them goal images captured at goal positions within 10 m ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Then, simulation and realworld experiments are conducted in static and dynamic tasks to compare its effective and robust navigation performance for target deployment environments ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Real-World Visual Navigation Performance To investigate the effectiveness of the proposed pipeline in mitigating the sim-to-real gap, we compare the real-world navigation performance of ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Visual Navigation Performance in Simulation The impact of photorealistic dynamic GS simulation datasets on visual navigation policies is examined through simulation tests comparing ReaDy-Go ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| ReaDy-Go avoids a dynamic obstacle, while the baselines collide with it. target environments with six previously unseen humans. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| ReaDy-Go shows the highest success rate and the lowest average reaching time in Dynamic, with only a slight performance degradation compared to Static. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3) Baselines: We compare the following baselines against ReaDy-Go visual navigation policies to evaluate the effect of photorealistic dynamic GS simulation data for target ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| To isolate the effect of photorealistic dynamic obstacles on navigation policies, we employ the same policy architecture, human trajectories, and expert planner for both ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| First, the proposed human animation module generates plausible body motions for human GS avatars within static GS scenes along given 2D trajectories, without relying ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Fig. 2: ReaDy-Go overview. The proposed photorealistic simulation pipeline for visual navigation in dynamic environments consists of three main components: (1) a real-to-sim dynamic ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The framework consists of three key components: (1) a dynamic GS simulator that integrates a static scene GS, an animatable human GS obstacle, and ... | As in simulation, ReaDy-Go and Vid2Sim achieve comparable success rates in Static, but their performance diverges in Dynamic. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Primary metric/result | ReaDy-Go achieves comparable success rates in both Static and Dynamic in the real world, consistent with its simulation results across all environments, even though ... | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For each task and environment, we evaluate 100 episodes in simulation and 10 episodes in real-world experiments.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The validation scenarios consist of 50 episodes for each environment, and we selected the checkpoint with the best validation performance, which is used for testing ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The image resolution is 144×256, and the three consecutive images used by the policy are sampled at 0.5 s intervals.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In real-world experiments, the policy requires only 18 ms per inference (55 Hz) on the onboard computer, while the camera operates at 20 Hz.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For this experiment, the policy is trained on the combined datasets from three environments, i.e., a total of 1,200 episodes from Outside, Lobby, and Library.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic obstacle collision and Static collision during ... | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | Second, while ReaDy-Go and Vid2Sim showed similar numbers of failures in cases unrelated to dynamic obstacle interactions, ReaDy-Go was more robust in situations involving ... | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 3: Visualization of the robot expert planner. (a) The robot follows a collision-free path (red) from start (green) to goal (blue). (b) When ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | The robot should reach the goal without collisions within the scenario time limit. | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | These indicate that real-to-sim simulation with GS is a costeffective and scalable approach to achieve fewer collisions and faster task completion with only a ... | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 1: The proposed real-to-sim dynamic environment sim- ulation pipeline for visual navigation. ReaDy-Go generates photorealistic navigation datasets for dynamic scenarios and trains environment-specific ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The policy predicts the action (v, w) and is trained with the Adam optimizer with a learning rate of 10-4. | p. 5 (IV. EXPERIMENTS) |
| Implementation Details 1) Dataset: We selected three target environments, Outside, Lobby, and Library, as shown in Fig. | p. 5 (IV. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic obstacle collision and Static collision during detour.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Second, while ReaDy-Go and Vid2Sim showed similar numbers of failures in cases unrelated to dynamic obstacle interactions, ReaDy-Go was more robust in situations involving dynamic ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Visualization of the robot expert planner. (a) The robot follows a collision-free path (red) from start (green) to goal (blue). (b) When a ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The robot should reach the goal without collisions within the scenario time limit.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** These indicate that real-to-sim simulation with GS is a costeffective and scalable approach to achieve fewer collisions and faster task completion with only a video.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The proposed real-to-sim dynamic environment sim- ulation pipeline for visual navigation. ReaDy-Go generates photorealistic navigation datasets for dynamic scenarios and trains environment-specific visual ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), baselines p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), results p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
