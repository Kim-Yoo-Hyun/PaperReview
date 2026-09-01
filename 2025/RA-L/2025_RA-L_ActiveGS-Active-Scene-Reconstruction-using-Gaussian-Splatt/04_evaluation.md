# Evaluation - ActiveGS: Active Scene Reconstruction using Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2412.17769; PDF retrieval source: https://arxiv.org/pdf/2412.17769. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION)): Our approach achieves the best performance in both rendering and mesh quality across all test scenes, supporting our first claim that it outperforms state-of-the-art NeRF and GSbased methods.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction methods; (ii) we ...
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Our real-world experiments indicate that our approach is effective for actively reconstructing unknown scenes by Fig 6: Our real-world experiments using a UAV equipped with ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** We conduct our simulation experiments using the Habitat simulator [29] and the Replica dataset [33].
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Real-World Experiments We demonstrate the applicability our framework in a realworld experiment using a UAV equipped with an Intel RealSense 455 RGB-D camera to reconstruct ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** 6 IEEE ROBOTICS AND AUTOMATION LETTERS.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** We run 5 trials for all methods across 8 test scenes.
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** The ablation study comparing Ours and Ours (w/o ROI) demonstrates the benefits of ROI-based sampling for targeted inspection, reflected by higher means and smaller standard ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** III-E. • Ours (w/o ROI): A variant of our ActiveGS that leverages only local random sampling, with NROI = 0. • Ours†: A variant of ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EXPERIMENTAL EVALUATION (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach achieves the best performance in both rendering and mesh quality across all test scenes, supporting our first claim that it outperforms state-of-the-art ... | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction methods; (ii) ... | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | We consider ROI-based sampling to achieve targeted candidate viewpoint generation as described in Sec. | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our ActiveGS outperforms baselines in all test scenes. | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our confidence formulation also outperforms the variant in Ours† by considering viewpoint distribution. | p. 7 (IV. EXPERIMENTAL EVALUATION) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction methods; (ii) we ...
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Our real-world experiments indicate that our approach is effective for actively reconstructing unknown scenes by Fig 6: Our real-world experiments using a UAV equipped with ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** We conduct our simulation experiments using the Habitat simulator [29] and the Replica dataset [33].
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Real-World Experiments We demonstrate the applicability our framework in a realworld experiment using a UAV equipped with an Intel RealSense 455 RGB-D camera to reconstruct ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** 6 IEEE ROBOTICS AND AUTOMATION LETTERS.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** We run 5 trials for all methods across 8 test scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction methods; (ii) ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION) |
| Task/environment | Our real-world experiments indicate that our approach is effective for actively reconstructing unknown scenes by Fig 6: Our real-world experiments using a UAV equipped ... | reset, timeout, object/scene variation | p. 7 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. OUR APPROACH), p. 3 (III. OUR APPROACH) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (III. OUR APPROACH), p. 4 (III. OUR APPROACH) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The ablation study comparing Ours and Ours (w/o ROI) demonstrates the benefits of ROI-based sampling for targeted inspection, reflected by higher means and smaller ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTAL EVALUATION) |
| III-E. • Ours (w/o ROI): A variant of our ActiveGS that leverages only local random sampling, with NROI = 0. • Ours†: A variant ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction methods; (ii) ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Our approaches demonstrate a large performance gain to the state-of-the-art NeRF-based approach, NARUTO, motivating the use of GS in active scene reconstruction. • FisherRF ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Given the limited on-board resources, we run ActiveGS on our desktop PC, where it receives RGB-D and pose data from the UAV for map ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTAL EVALUATION) |
| We report the mean and standard deviation for PSNR and completeness ratio. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL EVALUATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our ActiveGS outperforms baselines in all test scenes. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Our approach achieves the best performance in both rendering and mesh quality across all test scenes, supporting our first claim that it outperforms state-of-the-art ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction methods; (ii) ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Our confidence formulation also outperforms the variant in Ours† by considering viewpoint distribution. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTAL EVALUATION) |
| We show RGB rendering and surface meshes for two scenes, with red circles highlighting areas of low-quality reconstruction from baseline approaches. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTAL EVALUATION) |
| III-E. • Ours (w/o ROI): A variant of our ActiveGS that leverages only local random sampling, with NROI = 0. • Ours†: A variant ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL EVALUATION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| III-E. • Ours (w/o ROI): A variant of our ActiveGS that leverages only local random sampling, with NROI = 0. • Ours†: A variant ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Our confidence formulation also outperforms the variant in Ours† by considering viewpoint distribution. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTAL EVALUATION) |
| The ablation study comparing Ours and Ours (w/o ROI) demonstrates the benefits of ROI-based sampling for targeted inspection, reflected by higher means and smaller ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENTAL EVALUATION) |
| We replace its 3D GS map with our 2D GS. • NARUTO [5]: A state-of-the-art NeRF-based active scene reconstruction pipeline. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTAL EVALUATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce ActiveGS, a novel framework for active scene reconstruction using GS for autonomous robotic tasks. | Our approach achieves the best performance in both rendering and mesh quality across all test scenes, supporting our first claim that it outperforms state-of-the-art ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION) |
| Primary metric/result | Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction methods; (ii) ... | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTAL EVALUATION) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** We test our implementation on a desktop PC with an Intel Core i9-10940X CPU and an NVIDIA RTX A5000 GPU.
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** In this setup, one mapping and planning steps take approximately 1 s and 0.5 s, respectively.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** We run 5 trials for all methods across 8 test scenes.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** We set the maximum mission time to 300 s and evaluate reconstruction performance every 60 s.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Unlike simulation experiments, we do not account for the pitch angle of viewpoints in this experiment due to control limitations. | p. 7 (IV. EXPERIMENTAL EVALUATION) |
| body limitation/failure cue | Given the limited on-board resources, we run ActiveGS on our desktop PC, where it receives RGB-D and pose data from the UAV for map ... | p. 7 (IV. EXPERIMENTAL EVALUATION) |
| body limitation/failure cue | The camera has a depth sensing range of [0.1, 5.0] m and Gaussian noise in the depth measurements with linearly increased standard deviation σ ... | p. 5 (IV. EXPERIMENTAL EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We test our implementation on a desktop PC with an Intel Core i9-10940X CPU and an NVIDIA RTX A5000 GPU. | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| We run 5 trials for all methods across 8 test scenes. | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| In this setup, one mapping and planning steps take approximately 1 s and 0.5 s, respectively. | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Given the limited on-board resources, we run ActiveGS on our desktop PC, where it receives RGB-D and pose data from the UAV for map ... | p. 7 (IV. EXPERIMENTAL EVALUATION) |
| For scenarios, including search and rescue, agricultural robotics, and industrial inspection, online active reconstruction using mobile robots demands both mission efficiency and reconstruction quality. | p. 1 (A CTIVE exploration and reconstruction of unknown) |
| The framework alternates between mapping and planning steps until a predefined mission time is reached. | p. 3 (III. OUR APPROACH) |
| After every 5 mapping steps, we perform a visibility check on all Gaussian primitives and delete those invisible to all history views to compact ... | p. 4 (III. OUR APPROACH) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Unlike simulation experiments, we do not account for the pitch angle of viewpoints in this experiment due to control limitations.
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Given the limited on-board resources, we run ActiveGS on our desktop PC, where it receives RGB-D and pose data from the UAV for map updates ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** The camera has a depth sensing range of [0.1, 5.0] m and Gaussian noise in the depth measurements with linearly increased standard deviation σ = ...

- **PDF anchors reviewed:** datasets p. 5 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), metrics p. 7 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), baselines p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), results p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
