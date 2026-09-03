# Evaluation - Habitat: A Platform for Embodied AI Research

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.01201; PDF retrieval source: https://arxiv.org/pdf/1904.01201. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5. Results and Findings), p. 8 (5. Results and Findings), p. 7 (5. Results and Findings), p. 8 (5. Results and Findings), p. 4 (Figure/Table caption), p. 12 (Figure/Table caption)): Interestingly, RGB agents do not significantly outperform Blind agents; we hypothesize because both are equipped with GPS sensors.

## Evaluation Body Digest

- **p. 7 / 5. Results and Findings - extractive body cue:** In contrast, RGB sensors provide a high-dimensional complex signal that may be prone to overfitting to train environments due to the variety across scenes (even ...
- **p. 7 / 5. Results and Findings - extractive body cue:** This is consistent with our previous analysis that Gibson contains smaller scenes and shorter episodes.
- **p. 8 / 5. Results and Findings - extractive body cue:** We believe the reason is the previously noted observation that Gibson scenes are smaller and episodes are shorter (lower GDSP) than Matterport3D.
- **p. 8 / 5. Results and Findings - extractive body cue:** We report average SPL for a model trained on the source dataset in each row, as evaluated on test episodes for the target dataset in ...
- **p. 2 / 2. We conduct the first cross-dataset generalization exper - extractive body cue:** iments {train, test} × {Matterport3D, Gibson} for multiple sensors {Blind1, RGB, RGBD, D} × {GPS+Compass} and find that only agents with depth (D) sensors generalize ...
- **p. 7 / 5. Results and Findings - extractive body cue:** The differences are about an order of magnitude larger than the standard deviation of average SPL for all cases (e.g. on the Gibson dataset errors ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Average SPL of agents on the val set over the course of training. Previous work [20, 16] has analyzed performance at 5-10 million ...
- **p. 8 / 5. Results and Findings - extractive body cue:** Gibson agents are trained on ‘easier' episodes and encounter positive reward more easily during random exploration, thus bootstrapping learning.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 2. We conduct the first cross-dataset generalization exper (p. 2); 5. Results and Findings (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5. Results and Findings | BENCHMARK / DATASET | Interestingly, RGB agents do not significantly outperform Blind agents; we hypothesize because both are equipped with GPS sensors. | p. 7 (5. Results and Findings) |
| 5. Results and Findings | BENCHMARK / DATASET | Our findings so far are that RL (PPO) agents significantly outperform SLAM [20]. | p. 8 (5. Results and Findings) |
| 5. Results and Findings | BENCHMARK / DATASET | All RL (PPO) agents start out with far worse SPL, but RL (PPO) Depth, in particular, improves dramatically and matches the classic baseline at ... | p. 7 (5. Results and Findings) |
| 5. Results and Findings | BENCHMARK / DATASET | Second, we find a potentially counter-intuitive trend - agents trained on Gibson consistently outperform their counterparts trained on Matterport3D, even when evaluated on Matterport3D. | p. 8 (5. Results and Findings) |
| Figure/Table caption | BENCHMARK / DATASET | Table 1: Performance of Habitat-Sim in frames per second for an example Matterport3D scene (id 17DRP5sb8fy) on an Intel Xeon E5-2690 v4 CPU and ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5. Results and Findings - extractive body cue:** In contrast, RGB sensors provide a high-dimensional complex signal that may be prone to overfitting to train environments due to the variety across scenes (even ...
- **p. 7 / 5. Results and Findings - extractive body cue:** This is consistent with our previous analysis that Gibson contains smaller scenes and shorter episodes.
- **p. 8 / 5. Results and Findings - extractive body cue:** We believe the reason is the previously noted observation that Gibson scenes are smaller and episodes are shorter (lower GDSP) than Matterport3D.
- **p. 8 / 5. Results and Findings - extractive body cue:** We report average SPL for a model trained on the source dataset in each row, as evaluated on test episodes for the target dataset in ...
- **p. 2 / 2. We conduct the first cross-dataset generalization exper - extractive body cue:** iments {train, test} × {Matterport3D, Gibson} for multiple sensors {Blind1, RGB, RGBD, D} × {GPS+Compass} and find that only agents with depth (D) sensors generalize ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The ‘software stack' for training embodied agents involves (1) datasets providing 3D assets with semantic annotations, (2) simulators that render these assets and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Example rendered sensor observations for three sensors (color camera, depth sensor, semantic instance mask) in two differ- ent environment datasets. A Matterport3D [8] ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Performance of Habitat-Sim in frames per second for an example Matterport3D scene (id 17DRP5sb8fy) on an Intel Xeon E5-2690 v4 CPU and Nvidia ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Average SPL of agents on the val set over the course of training. Previous work [20, 16] has analyzed performance at 5-10 million ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Performance of baseline methods on the PointGoal task [2] tested on the Gibson [30] and MP3D [8] test sets under multiple sensor configurations. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Navigation examples for different sensory configurations of the RL (PPO) agent, visualizing trials from the Gibson and MP3D val sets. A blue dot ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Generalization of agents between datasets. We report average SPL for a model trained on the source dataset in each row, as evaluated on ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 6: Architecture of Habitat-Sim main classes. The Simulator delegates management of all resources related to 3D environments to a ResourceManager that is responsible for ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In contrast, RGB sensors provide a high-dimensional complex signal that may be prone to overfitting to train environments due to the variety across scenes ... | embodiment, simulator version and control stack | p. 7 (5. Results and Findings), p. 7 (5. Results and Findings) |
| Task/environment | This is consistent with our previous analysis that Gibson contains smaller scenes and shorter episodes. | reset, timeout, object/scene variation | p. 7 (5. Results and Findings), p. 8 (5. Results and Findings) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (1. Introduction), p. 4 (3. Habitat Platform) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The differences are about an order of magnitude larger than the standard deviation of average SPL for all cases (e.g. on the Gibson dataset ... | definition/direction/unit from same section | p. 7 (5. Results and Findings) |
| Figure 3: Average SPL of agents on the val set over the course of training. Previous work [20, 16] has analyzed performance at 5-10 ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| We report average SPL for a model trained on the source dataset in each row, as evaluated on test episodes for the target dataset ... | definition/direction/unit from same section | p. 8 (5. Results and Findings) |
| Gibson agents are trained on ‘easier' episodes and encounter positive reward more easily during random exploration, thus bootstrapping learning. | definition/direction/unit from same section | p. 8 (5. Results and Findings) |
| Figure 7: Performance of Habitat-Sim under different sensor frame memory transfer strategies for increasing image resolution. We see that ‘GPU->GPU' is unaffected by image ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Table 3: Performance of Habitat-Sim in frames per second for an example Matterport3D scene (id 17DRP5sb8fy) on a Xeon E5-2690 v4 CPU and Nvidia ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Figure 10: Average number of collisions during successful navi- gation episodes for the different sensory configurations of the RL (PPO) baseline agent on test ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Figure 2: Example rendered sensor observations for three sensors (color camera, depth sensor, semantic instance mask) in two differ- ent environment datasets. A Matterport3D ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 3: Average SPL of agents on the val set over the course of training. Previous work [20, 16] has analyzed performance at 5-10 ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Interestingly, RGB agents do not significantly outperform Blind agents; we hypothesize because both are equipped with GPS sensors. | comparison identity and matched condition | p. 7 (5. Results and Findings) |
| Our findings so far are that RL (PPO) agents significantly outperform SLAM [20]. | comparison identity and matched condition | p. 8 (5. Results and Findings) |
| Second, we find a potentially counter-intuitive trend - agents trained on Gibson consistently outperform their counterparts trained on Matterport3D, even when evaluated on Matterport3D. | comparison identity and matched condition | p. 8 (5. Results and Findings) |
| Table 5: Statistics of path length (in actions) for an oracle which greedily fits actions to follow the negative of geodesic distance gradient on ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Figure 8: Architecture of Habitat-API. The core functionality defines fundamental building blocks such as the API for interacting with the simulator backend and receiving ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Specifically, Habitat consists of the following: 1. | Interestingly, RGB agents do not significantly outperform Blind agents; we hypothesize because both are equipped with GPS sensors. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5. Results and Findings), p. 8 (5. Results and Findings), p. 7 (5. Results and Findings), p. 8 (5. Results and Findings), p. 4 (Figure/Table caption), p. 12 (Figure/Table caption) |
| Primary metric/result | Our findings so far are that RL (PPO) agents significantly outperform SLAM [20]. | numeric claim only at cited anchor | p. 8 (5. Results and Findings) |

- Numeric sentences retained from the body:
- **p. 1 / Abstract - extractive body cue:** Habitat-Sim is fast - when rendering a scene from Matterport3D, it achieves several thousand frames per second (fps) running single-threaded, and can reach over 10,000 ...
- **p. 2 / 1. Introduction - extractive body cue:** When rendering a scene from the Matterport3D dataset, Habitat-Sim achieves several thousand frames per second (fps) running singlethreaded, and can reach over 10,000 fps multi-process ...
- **p. 4 / 3. Habitat Platform - extractive body cue:** By comparison, AI2-THOR [17] and CHALET [31] run at tens of fps, MINOS [24] and Gibson [30] run at about a hundred, and House3D [29] ...
- **p. 4 / 3. Habitat Platform - extractive body cue:** By operating at 10,000 frames per second we shift the bottleneck from simulation to optimization for network training.
- **p. 4 / 3. Habitat Platform - extractive body cue:** Based on TensorFlow benchmarks, many popular network architectures run at frame rates that are 10-100x lower on a single GPU3.
- **p. 5 / 4. PointGoal Navigation at Scale - extractive body cue:** These actions are mapped to idealized actuations that result in 10 degree turns for the turning actions and linear displacement of 0.25m for the move_forward ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Another planned avenue of future work involves procedural generation of 3D environments by leveraging a combination of 3D reconstruction and virtual object datasets. | p. 9 (7. Future Work) |
| body limitation/failure cue | Figure 10: Average number of collisions during successful navi- gation episodes for the different sensory configurations of the RL (PPO) baseline agent on test ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | SLAM [20] does not require training and thus has a constant performance (0.59 on Gibson, 0.42 on Matterport3D). | p. 7 (5. Results and Findings) |
| body limitation/failure cue | RGB and RGBD agents suffer a significant performance degradation, while the Blind agent is least affected (as we would expect). | p. 8 (5. Results and Findings) |
| body limitation/failure cue | Figure 7: Performance of Habitat-Sim under different sensor frame memory transfer strategies for increasing image resolution. We see that ‘GPU->GPU' is unaffected by image ... | p. 12 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. ... | p. 4 (3. Habitat Platform) |
| Training agents to 75 million steps took (in sum over all three datasets): 320 GPU-hours for Blind, 566 GPU-hours for RGB, 475 GPU-hours for ... | p. 6 (4. PointGoal Navigation at Scale) |
| We ran our experiments with 5 random seeds per run, to confirm that these differences are statistically significant. | p. 7 (5. Results and Findings) |
| Habitat-Sim is fast - when rendering a scene from Matterport3D, it achieves several thousand frames per second (fps) running single-threaded, and can reach over ... | p. 1 (Abstract) |
| The Habitat architecture and implementation combine modularity and high performance. | p. 2 (1. Introduction) |
| Datasets have been a key driver of progress in computer vision, NLP, and other areas of AI [10, 18, 4, 1]. | p. 2 (1. Introduction) |
| Based on TensorFlow benchmarks, many popular network architectures run at frame rates that are 10-100x lower on a single GPU3. | p. 4 (3. Habitat Platform) |
| This threshold significantly exceeds the number of steps an optimal agent requires to reach all goals (see the supplement). | p. 5 (4. PointGoal Navigation at Scale) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 7. Future Work - extractive body cue:** Another planned avenue of future work involves procedural generation of 3D environments by leveraging a combination of 3D reconstruction and virtual object datasets.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 10: Average number of collisions during successful navi- gation episodes for the different sensory configurations of the RL (PPO) baseline agent on test set ...
- **p. 7 / 5. Results and Findings - extractive body cue:** SLAM [20] does not require training and thus has a constant performance (0.59 on Gibson, 0.42 on Matterport3D).
- **p. 8 / 5. Results and Findings - extractive body cue:** RGB and RGBD agents suffer a significant performance degradation, while the Blind agent is least affected (as we would expect).
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7: Performance of Habitat-Sim under different sensor frame memory transfer strategies for increasing image resolution. We see that ‘GPU->GPU' is unaffected by image resolution ...

- **Evidence anchors reviewed:** datasets p. 7 (5. Results and Findings), p. 7 (5. Results and Findings), p. 8 (5. Results and Findings), p. 8 (5. Results and Findings), p. 2 (2. We conduct the first cross-dataset generalization exper), metrics p. 7 (5. Results and Findings), p. 7 (Figure/Table caption), p. 8 (5. Results and Findings), p. 8 (5. Results and Findings), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 7 (5. Results and Findings), p. 8 (5. Results and Findings), p. 8 (5. Results and Findings), p. 13 (Figure/Table caption), p. 13 (Figure/Table caption), results p. 7 (5. Results and Findings), p. 8 (5. Results and Findings), p. 7 (5. Results and Findings), p. 8 (5. Results and Findings), p. 4 (Figure/Table caption), p. 12 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
