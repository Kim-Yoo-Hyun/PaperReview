# Evaluation - GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.05152; PDF retrieval source: https://arxiv.org/pdf/2503.05152. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (V. EXPERIMENTS), p. 3 (Figure/Table caption), p. 4 (V. EXPERIMENTS), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption)): In our experiments, we compare the proposed method with conventional methods in terms of success rate, path efficiency, and robustness with respect to the number of pre-collected images in the ...

## Evaluation Body Digest

- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** Simulation Setup 1) Robot Setup: We simulate a circular wheeled robot (radius: 0.5 m) that navigates the environment using the Habitat simulator API, with state ...
- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** Experiment Setup 1) Image-Goal Navigation Task: The task is image-goal navigation, where the robot must move from a start pose to a goal position at ...
- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** In our experiments, we compare the proposed method with conventional methods in terms of success rate, path efficiency, and robustness with respect to the number ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3. Comparison of the SPL on each environment. where Ntrials is the number of trials, Li is the path length of the i-th trial, ...
- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** Consequently, the simulator restricts the robot from leaving the traversable area, and collision avoidance performance is not evaluated2.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. GSplatVNM employs 3DGS as a compact and renderable envi- ronment representation for the VNM, which imagines future point-of-view images to efficiently navigate the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. Trajectories of the image collection and selected navigation results for each environment. GSplatVNM can generate point-of-view images that are not included in the ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Overview of the proposed GSplatVNM. In a conventional ITG-based approach, the environment is represented by ITG, and the target point-of-views given to the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / SIMULATION | In our experiments, we compare the proposed method with conventional methods in terms of success rate, path efficiency, and robustness with respect to the ... | p. 4 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 2. Overview of the proposed GSplatVNM. In a conventional ITG-based approach, the environment is represented by ITG, and the target point-of-views given to ... | p. 3 (Figure/Table caption) |
| V. EXPERIMENTS | EMPIRICAL / SIMULATION | Consequently, the simulator restricts the robot from leaving the traversable area, and collision avoidance performance is not evaluated2. | p. 4 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 3. Comparison of the SPL on each environment. where Ntrials is the number of trials, Li is the path length of the i-th ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 4. Trajectories of the image collection and selected navigation results for each environment. GSplatVNM can generate point-of-view images that are not included in ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** Simulation Setup 1) Robot Setup: We simulate a circular wheeled robot (radius: 0.5 m) that navigates the environment using the Habitat simulator API, with state ...
- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** Experiment Setup 1) Image-Goal Navigation Task: The task is image-goal navigation, where the robot must move from a start pose to a goal position at ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. GSplatVNM employs 3DGS as a compact and renderable envi- ronment representation for the VNM, which imagines future point-of-view images to efficiently navigate the ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Overview of the proposed GSplatVNM. In a conventional ITG-based approach, the environment is represented by ITG, and the target point-of-views given to the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3. Comparison of the SPL on each environment. where Ntrials is the number of trials, Li is the path length of the i-th trial, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. Trajectories of the image collection and selected navigation results for each environment. GSplatVNM can generate point-of-view images that are not included in the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Simulation Setup 1) Robot Setup: We simulate a circular wheeled robot (radius: 0.5 m) that navigates the environment using the Habitat simulator API, with ... | embodiment, simulator version and control stack | p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Task/environment | Experiment Setup 1) Image-Goal Navigation Task: The task is image-goal navigation, where the robot must move from a start pose to a goal position ... | reset, timeout, object/scene variation | p. 4 (V. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (2) Pre-Collection), p. 2 (A. ITG-based Visual Navigation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In our experiments, we compare the proposed method with conventional methods in terms of success rate, path efficiency, and robustness with respect to the ... | definition/direction/unit from same section | p. 4 (V. EXPERIMENTS) |
| Fig. 3. Comparison of the SPL on each environment. where Ntrials is the number of trials, Li is the path length of the i-th ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Consequently, the simulator restricts the robot from leaving the traversable area, and collision avoidance performance is not evaluated2. | definition/direction/unit from same section | p. 4 (V. EXPERIMENTS) |
| Fig. 1. GSplatVNM employs 3DGS as a compact and renderable envi- ronment representation for the VNM, which imagines future point-of-view images to efficiently navigate ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 4. Trajectories of the image collection and selected navigation results for each environment. GSplatVNM can generate point-of-view images that are not included in ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 4. Trajectories of the image collection and selected navigation results for each environment. GSplatVNM can generate point-of-view images that are not included in ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Fig. 3. Comparison of the SPL on each environment. where Ntrials is the number of trials, Li is the path length of the i-th ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

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
| 3DGS is a neural model that enables high-quality 3D reconstruction of the environment from a pre-collected image database (DB) and can further synthesize novel ... | In our experiments, we compare the proposed method with conventional methods in terms of success rate, path efficiency, and robustness with respect to the ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (V. EXPERIMENTS), p. 3 (Figure/Table caption), p. 4 (V. EXPERIMENTS), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | Fig. 2. Overview of the proposed GSplatVNM. In a conventional ITG-based approach, the environment is represented by ITG, and the target point-of-views given to ... | numeric claim only at cited anchor | p. 3 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** The camera has a resolution of 1280×720 pixels and a field of view of 120 degrees.
- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** A trial is considered successful if the robot reaches the goal within a specified distance (0.5 m for Greigsville and Ribera, and 1.0 m for ...
- **p. 2 / III. 3DGS AS ENVIRONMENT REPRESENTATION - extractive PDF cue:** Thus, the ellipsoid-to-sphere distance between the i-th ellipsoid and the robot centroid ˆp = FR⊤(p-µi) can be formulated as the following quadratic program: di(p) = ...
- **p. 4 / IV. VISUAL NAVIGATION WITH 3DGS - extractive PDF cue:** These networks are trained in a supervised manner on large, heterogeneous datasets collected across a diverse set of environments and robotic platforms over 100 hours, ...
- **p. 4 / 2) Pre-Collection - extractive PDF cue:** Before the navigation task, the robot explores the environment using an exploration policy based on NoMaD [3] and collects images at regular intervals of 0.5 ...
- **p. 5 / 2) Pre-Collection - extractive PDF cue:** Experimental Results 1) Comparisons of the Navigation Efficiency: Figure 3 presents the SPL distribution over Ntrials = 20 trials for each environment and image DB ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The second term is a collision penalty to avoid the infeasibility of global planning. | p. 3 (IV. VISUAL NAVIGATION WITH 3DGS) |
| body limitation/failure cue | A* search considers collisions between the robot and the 3DGS as well as the loss function (2). | p. 3 (IV. VISUAL NAVIGATION WITH 3DGS) |
| body limitation/failure cue | In our experiments, we assume that the robot is equipped with a collision avoidance system independent of NoMaD. | p. 4 (V. EXPERIMENTS) |
| body limitation/failure cue | Consequently, the simulator restricts the robot from leaving the traversable area, and collision avoidance performance is not evaluated2. | p. 4 (V. EXPERIMENTS) |
| body limitation/failure cue | In contrast, GSplatVNM demonstrates robustness with respect to the image DB size in terms of SPL. | p. 5 (2) Pre-Collection) |
| body limitation/failure cue | In contrast, NoMaD w/ ITG shows significant degradation in SPL as the image DB size decreases-especially in the Ribera and skokloster-castle environments-due to a ... | p. 5 (2) Pre-Collection) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| A trial is considered successful if the robot reaches the goal within a specified distance (0.5 m for Greigsville and Ribera, and 1.0 m ... | p. 4 (V. EXPERIMENTS) |
| Typically, the robot localizes itself within the ITG and navigates by following a path computed using graph search algorithms [11]. | p. 2 (A. ITG-based Visual Navigation) |
| 2, ITG is a graph representation of the environment, where each node represents a point-of-view image and edges encode traversability [6]. | p. 2 (A. ITG-based Visual Navigation) |
| Specifically, we use the Learned Perceptual Image Patch Similarity (LPIPS) metric [27], which is computed from the feature maps of AlexNet [28] and ranges ... | p. 3 (IV. VISUAL NAVIGATION WITH 3DGS) |
| That is, we compute the traversable trajectory T as follows: T = {qstart,(x0,y0,θ 0 yaw),...,(xM-1,yM-1,θ M-1 yaw ),qgoal}, (3) {(x0,y0),...,(xM-1,yM-1)} = A*(qstart,qgoal), θ i ... | p. 3 (IV. VISUAL NAVIGATION WITH 3DGS) |
| NoMaD consists of three networks: • A subgoal image-conditioned vision encoder, ct = fenc(Oobs,Itarget), that extracts context features from the observation Oobs and target ... | p. 4 (IV. VISUAL NAVIGATION WITH 3DGS) |
| The shortest path length is computed using the Dijkstra algorithm on the traversable area map provided by the simulator. | p. 5 (2) Pre-Collection) |
| Experimental Results 1) Comparisons of the Navigation Efficiency: Figure 3 presents the SPL distribution over Ntrials = 20 trials for each environment and image ... | p. 5 (2) Pre-Collection) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive PDF cue:** The second term is a collision penalty to avoid the infeasibility of global planning.
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive PDF cue:** A* search considers collisions between the robot and the 3DGS as well as the loss function (2).
- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** In our experiments, we assume that the robot is equipped with a collision avoidance system independent of NoMaD.
- **p. 4 / V. EXPERIMENTS - extractive PDF cue:** Consequently, the simulator restricts the robot from leaving the traversable area, and collision avoidance performance is not evaluated2.
- **p. 5 / 2) Pre-Collection - extractive PDF cue:** In contrast, GSplatVNM demonstrates robustness with respect to the image DB size in terms of SPL.
- **p. 5 / 2) Pre-Collection - extractive PDF cue:** In contrast, NoMaD w/ ITG shows significant degradation in SPL as the image DB size decreases-especially in the Ribera and skokloster-castle environments-due to a reduced ...

- **PDF anchors reviewed:** datasets p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), metrics p. 4 (V. EXPERIMENTS), p. 5 (Figure/Table caption), p. 4 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), results p. 4 (V. EXPERIMENTS), p. 3 (Figure/Table caption), p. 4 (V. EXPERIMENTS), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
