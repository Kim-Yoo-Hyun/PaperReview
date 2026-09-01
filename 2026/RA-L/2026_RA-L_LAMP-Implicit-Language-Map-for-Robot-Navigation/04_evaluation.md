# Evaluation - LAMP: Implicit Language Map for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.11862; PDF retrieval source: https://arxiv.org/pdf/2602.11862. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption)): First, success rate is computed considering only the top 1% of the predictions; a trial is deemed successful if the robot ends up within 20 m of the center of ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** In the following subsections, Section IV-A describes the dataset configuration and implementation details, Section IV-B presents the experimental results obtained in the Nvidia Isaac simulation ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** In our real-world experiments, we deployed a robot equipped with six cameras to navigate each floor of the building.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** First, success rate is computed considering only the top 1% of the predictions; a trial is deemed successful if the robot ends up within 20 ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Next, the Success weighted by Path Length (SPL) metric evaluates navigation efficiency by penalizing unnecessarily long paths.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. System Overview. (a) Implicit Language Map Construction: The robot traverses the environment and collects pairs of camera poses x and corresponding images I. ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive memory ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5. Visualization of real-world experiments. : Start pose, representing the initial position from which navigation is initiated. : Coarse goal pose, selected based on ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. Visualization of each language map representation in the near-goal region of NVIDIA's City Tower Demo 3D Models Pack scene using the viridis colormap. ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, success rate is computed considering only the top 1% of the predictions; a trial is deemed successful if the robot ends up within ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The purpose of our experiments is to demonstrate that LAMP, our method which implicitly incorporates language information within large-scale scenes, achieves memory efficiency and ... | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 2. System Overview. (a) Implicit Language Map Construction: The robot traverses the environment and collects pairs of camera poses x and corresponding images ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** In the following subsections, Section IV-A describes the dataset configuration and implementation details, Section IV-B presents the experimental results obtained in the Nvidia Isaac simulation ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** In our real-world experiments, we deployed a robot equipped with six cameras to navigate each floor of the building.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive memory ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. System Overview. (a) Implicit Language Map Construction: The robot traverses the environment and collects pairs of camera poses x and corresponding images I. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3. Examples of objects used in our simulation navigation experiments. The top row displays large objects (volume ≥1 m3) such as statues and a ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. Visualization of each language map representation in the near-goal region of NVIDIA's City Tower Demo 3D Models Pack scene using the viridis colormap. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5. Visualization of real-world experiments. : Start pose, representing the initial position from which navigation is initiated. : Coarse goal pose, selected based on ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In the following subsections, Section IV-A describes the dataset configuration and implementation details, Section IV-B presents the experimental results obtained in the Nvidia Isaac ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | In our real-world experiments, we deployed a robot equipped with six cameras to navigate each floor of the building. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (III. METHOD), p. 4 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| First, success rate is computed considering only the top 1% of the predictions; a trial is deemed successful if the robot ends up within ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Next, the Success weighted by Path Length (SPL) metric evaluates navigation efficiency by penalizing unnecessarily long paths. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 2. System Overview. (a) Implicit Language Map Construction: The robot traverses the environment and collects pairs of camera poses x and corresponding images ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 5. Visualization of real-world experiments. : Start pose, representing the initial position from which navigation is initiated. : Coarse goal pose, selected based ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 4. Visualization of each language map representation in the near-goal region of NVIDIA's City Tower Demo 3D Models Pack scene using the viridis ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Fig. 3. Examples of objects used in our simulation navigation experiments. The top row displays large objects (volume ≥1 m3) such as statues and ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Fig. 5. Visualization of real-world experiments. : Start pose, representing the initial position from which navigation is initiated. : Coarse goal pose, selected based ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 3. Examples of objects used in our simulation navigation experiments. The top row displays large objects (volume ≥1 m3) such as statues and ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our main contributions of LAMP (Language Map) as follows: • We introduce LAMP, the first implicit language map leveraging a language-driven continuous ... | First, success rate is computed considering only the top 1% of the predictions; a trial is deemed successful if the robot ends up within ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Primary metric/result | The purpose of our experiments is to demonstrate that LAMP, our method which implicitly incorporates language information within large-scale scenes, achieves memory efficiency and ... | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | In the Extinguisher scene, the node-based method fails because it does not directly observe the goal, whereas our method correctly identifies the target by ... | p. 6 (1) Comparison of Language Map Representation Methods) |
| body limitation/failure cue | Even with this increased memory usage, the grid-based approach captures large objects but fails to detect smaller ones. | p. 5 (1) Comparison of Language Map Representation Methods) |
| body limitation/failure cue | In contrast, the node-based method needs about 70 times more memory than our method to reach a similar success rate, yet its performance in ... | p. 5 (1) Comparison of Language Map Representation Methods) |
| body limitation/failure cue | Finally, in the Boxes scene, the grid-based method is hindered by z-axis projection artifacts, while the node-based method detects the boxes but fails to ... | p. 6 (1) Comparison of Language Map Representation Methods) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| First, success rate is computed considering only the top 1% of the predictions; a trial is deemed successful if the robot ends up within ... | p. 5 (IV. EXPERIMENTS) |
| 6), the distance penalty hyperparameter λdist is set to 5. | p. 5 (IV. EXPERIMENTS) |
| Formally, for each node v ∈V, we define: score(v) = w1 svc(v) + w2 su(v) + w3 sss(v), (5) where svc(v) is a View ... | p. 4 (III. METHOD) |
| We solve (6) via a gradient-based method, updating δx at each step t by δxt+1 = δxt -α ˆmt √ˆvt + ϵ, (7) where ... | p. 4 (III. METHOD) |
| We introduce a map representation that continuously encodes language features within a large-scale space, ensuring memory efficiency and enabling fine-grained path planning. | p. 2 (III. METHOD) |
| This approach contrasts with previous methods that explicitly store precomputed embeddings at every node, leading to large memory usage. | p. 3 (III. METHOD) |
| Inspired by NeRF frameworks [34], we implicitly encode the language embeddings of the scene as viewed from each position, rather than encoding the color ... | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive memory ...
- **p. 6 / 1) Comparison of Language Map Representation Methods - extractive PDF cue:** In the Extinguisher scene, the node-based method fails because it does not directly observe the goal, whereas our method correctly identifies the target by leveraging ...
- **p. 5 / 1) Comparison of Language Map Representation Methods - extractive PDF cue:** Even with this increased memory usage, the grid-based approach captures large objects but fails to detect smaller ones.
- **p. 5 / 1) Comparison of Language Map Representation Methods - extractive PDF cue:** In contrast, the node-based method needs about 70 times more memory than our method to reach a similar success rate, yet its performance in the ...
- **p. 6 / 1) Comparison of Language Map Representation Methods - extractive PDF cue:** Finally, in the Boxes scene, the grid-based method is hindered by z-axis projection artifacts, while the node-based method detects the boxes but fails to plan ...

- **PDF anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), metrics p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 2 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
