# Evaluation - VLMaps: Visual-Language Maps for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.05714; PDF retrieval source: https://arxiv.org/pdf/2210.05714. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 11 (Figure/Table caption)): Subgoals in a Row 1 2 3 4 LM-Nav [13] 5 5 0 0 CoW [12] 33 5 0 0 CLIP Map 19 0 0 0 VLMaps (ours) 62 33 ...

## Evaluation Body Digest

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We use the Habitat simulator [45] with the Matterport3D dataset [46] for the evaluation of multi-object and spatial goal navigation tasks.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The dataset contains a large set of realistic indoor scenes that help evaluate the generalization capabilities of navigating agents.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our benchmark consists of 21 trajectories in seven scenes, with manually specified corresponding language instructions for evaluation.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Real Robot Experiments We also perform real-world experiments using the HSR mobile robot for indoor navigation given natural language commands.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In each sequence, we randomly specify a starting position of the robot in one scene and then pick four among 30 object categories as subgoal ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Different from object navigation tasks where agents only need to approach a certain object type within a range disregarding the relative spatial shift to the ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In contrast, while achieving similar success rate compared to the drone with a ground map, the drone with a drone map manages to navigate with ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We evaluate the Success Rate (SR) and the Success rate weighted by the (normalized inverse) Path Length (SPL) [48] defined as: SPL = 1 N ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Subgoals in a Row 1 2 3 4 LM-Nav [13] 5 5 0 0 CoW [12] 33 5 0 0 CLIP Map 19 0 ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This improves object navigation efficiency (Success [%] weighted by Path Length, SPL). | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, these results demonstrate the ability of VLMaps to index landmarks with natural language in the real world and, more importantly, its applicability to ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We compute the in-a-row success rate in the same way as in Sec. | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6: Qualitative semantic segmentation results | p. 11 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We use the Habitat simulator [45] with the Matterport3D dataset [46] for the evaluation of multi-object and spatial goal navigation tasks.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The dataset contains a large set of realistic indoor scenes that help evaluate the generalization capabilities of navigating agents.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our benchmark consists of 21 trajectories in seven scenes, with manually specified corresponding language instructions for evaluation.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Real Robot Experiments We also perform real-world experiments using the HSR mobile robot for indoor navigation given natural language commands.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In each sequence, we randomly specify a starting position of the robot in one scene and then pick four among 30 object categories as subgoal ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Different from object navigation tasks where agents only need to approach a certain object type within a range disregarding the relative spatial shift to the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: VLMaps is a spatial map representation in which pretrained visual- language model features are fused into a 3D reconstruction of the physical world. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model finetuning. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: System overview. A VLMap is created by fusing pretrained visual-language features into the reconstruction of the environment to enable visual-spatial-language-based reasoning. By providing ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Object mask for object type "chair". 4a shows the top-down map of the scene and the red circles specify the locations of type ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: VLMaps enable different embodiments to define their own obstacle maps for navigation. The left image shows the top-down view of an environment. The ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: Qualitative semantic segmentation results

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use the Habitat simulator [45] with the Matterport3D dataset [46] for the evaluation of multi-object and spatial goal navigation tasks. | embodiment, simulator version and control stack | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Task/environment | The dataset contains a large set of realistic indoor scenes that help evaluate the generalization capabilities of navigating agents. | reset, timeout, object/scene variation | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (III. METHOD), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In contrast, while achieving similar success rate compared to the drone with a ground map, the drone with a drone map manages to navigate ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| We evaluate the Success Rate (SR) and the Success rate weighted by the (normalized inverse) Path Length (SPL) [48] defined as: SPL = 1 ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Subgoals in a Row 1 2 3 4 LM-Nav [13] 5 5 0 0 CoW [12] 33 5 0 0 CLIP Map 19 0 ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Subgoals in a Row Independent 1 2 3 4 Subgoals LM-Nav [13] 26 4 1 1 26 CoW [12] 42 15 7 3 36 ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| For map creation in Habitat, we collect 12,096 RGB-D frames across ten different scenes and record the camera | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| IV-D), and (iv) to demonstrate on real robots that VLMaps can enable zero-shot spatial goal navigation given unseen language instructions (Sec. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Fig. 1: VLMaps is a spatial map representation in which pretrained visual- language model features are fused into a 3D reconstruction of the physical ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 3: System overview. A VLMap is created by fusing pretrained visual-language features into the reconstruction of the environment to enable visual-spatial-language-based reasoning. By ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms other baselines in this task. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| We observe that VLMaps performs consistently better compared to all baselines. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| The goals of our experiments are four-fold: (i) to quantitatively evaluate our VLMaps approach against recent open-vocabulary navigation baselines on the standard task of ... | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| This metric indicates how efficient the actual path is compared to the ground truth shortest path when the navigation task is achieved. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| In contrast, while achieving similar success rate compared to the drone with a ground map, the drone with a drone map manages to navigate ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Fig. 1: VLMaps is a spatial map representation in which pretrained visual- language model features are fused into a 3D reconstruction of the physical ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 1: VLMaps is a spatial map representation in which pretrained visual- language model features are fused into a 3D reconstruction of the physical ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Fig. 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Fig. 3: System overview. A VLMap is created by fusing pretrained visual-language features into the reconstruction of the environment to enable visual-spatial-language-based reasoning. By ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries. | Subgoals in a Row 1 2 3 4 LM-Nav [13] 5 5 0 0 CoW [12] 33 5 0 0 CLIP Map 19 0 ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 11 (Figure/Table caption) |
| Primary metric/result | This improves object navigation efficiency (Success [%] weighted by Path Length, SPL). | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In these two environments, the robot is required to navigate in a continuous environment with actions: move forward 0.05 meters, turn left 1 degree, turn ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In each sequence, we randomly specify a starting position of the robot in one scene and then pick four among 30 object categories as subgoal ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our benchmark consists of 21 trajectories in seven scenes, with manually specified corresponding language instructions for evaluation.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Examples of subgoals are "east of the table", "in between the chair and the sofa", or "move forward 3 meters".
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In our three setups, the ground truth trajectories for the LoCoBot and the drone are planned on floor-level and on height level of 1.7 meters ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For map creation, we record 374 frames for the evaluated scene and use an off-the-shelf RGB-D SLAM solution, RTAB-Map [49] to estimate the camera poses.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We observe that failure cases are caused by: 1) inaccurate depth, which introduces noise during the map creation and decreases the landmark indexing accuracy ... | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | This is because when the drone does not have access to a customized obstacle map, it fails to benefit from flying over ground objects ... | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We compute the in-a-row success rate in the same way as in Sec. | p. 5 (IV. EXPERIMENTS) |
| For all map-based methods, including CoW, CLIP Map, ground truth semantic map and our method, we apply the code generation techniques introduced in Sec. | p. 5 (IV. EXPERIMENTS) |
| We evaluate VLMaps on both a LoCoBot and a drone to test its capability of generating obstacle maps at runtime for multi-embodiment navigation. | p. 6 (IV. EXPERIMENTS) |
| Among the successful trials, six of them are spatial goals like "move between the chair and the wooden box" or "move to the south ... | p. 6 (IV. EXPERIMENTS) |
| The LSeg visual encoder maps an image such that the embedding of each pixel lies in the CLIP feature space. | p. 2 (III. METHOD) |
| LSeg Text Encoder (Frozen) "chair", "table", "floor", "wall", ... | p. 3 (III. METHOD) |
| We then compute the pixel-to-category similarity matrix S=Q·ET, where S∈R ¯H ¯ W×M. | p. 3 (III. METHOD) |
| The generated code can directly be executed on the robot with the built-in Python exec function. | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We observe that failure cases are caused by: 1) inaccurate depth, which introduces noise during the map creation and decreases the landmark indexing accuracy and ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model finetuning. ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This is because when the drone does not have access to a customized obstacle map, it fails to benefit from flying over ground objects to ...

- **Evidence anchors reviewed:** datasets p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), baselines p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), results p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 11 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Subgoals in a Row 1 2 3 4 LM-Nav [13] 5 5 0 0 CoW [12] 33 5 0 0 CLIP Map 19 0 0 0 VLMaps (ours) 62 33 ... (p. 5, IV. EXPERIMENTS).
- **Metric evidence:** Subgoals in a Row 1 2 3 4 LM-Nav [13] 5 5 0 0 CoW [12] 33 5 0 0 CLIP Map 19 0 0 0 VLMaps (ours) 62 33 ... (p. 5, IV. EXPERIMENTS).
- **Baseline/ablation evidence:** Our method outperforms other baselines in this task. (p. 5, IV. EXPERIMENTS).
- **Failure/negative evidence:** We observe that failure cases are caused by: 1) inaccurate depth, which introduces noise during the map creation and decreases the landmark indexing accuracy and 2) action noise, which can ... (p. 6, IV. EXPERIMENTS).
