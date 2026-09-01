# Evaluation - MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2.2. HM3D-ObjNav Benchmark), p. 6 (4.1. Experimental Setting), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption)): As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the previous best-performing method WMNav [31], and significantly outperforms ...

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setting - extractive PDF cue:** We evaluate our proposed approach on two established goal-oriented navigation benchmarks: 1) GOAT-Bench [19] (Multi-modal lifelong open-vocabulary dataset, 360 episodes, 36 scenes, 2669 total subtasks, ...
- **p. 6 / 4.1. Experimental Setting - extractive PDF cue:** 2) HM3DObjNav (HM3D-Semantics-v0.2 [41] from 2023 Habitat Challenge, 1000 episodes, 36 scenes, 6 goal categories).
- **p. 7 / 4.2.1. Goat-Bench Benchmark - extractive PDF cue:** These results highlight the effectiveness of our multi-modal scene graph in tackling multi-modal lifelong navigation tasks.
- **p. 7 / 4.2.1. Goat-Bench Benchmark - extractive PDF cue:** The results in Table 1 also show the outstanding performance of our MSGNav in tackling multimodal goals, lifelong navigation task settings.
- **p. 6 / 4.1. Experimental Setting - extractive PDF cue:** Following standard practice, we assess navigation performance using Success Rate (SR = Nsuccess Ntotal ) and Success weighted by Path Length (SPL = 1 Ntotal ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Component ablation experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. The first row without any module, ...
- **p. 7 / 4.2.2. HM3D-ObjNav Benchmark - extractive PDF cue:** As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the previous best-performing method ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Scene graph experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. "Node-only" indicates Concept-graph [9] without object ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Experimental Setting (p. 6); 4.2. Main Experimental Results (p. 6); 4.2.1. Goat-Bench Benchmark (p. 7); 4.2.2. HM3D-ObjNav Benchmark (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2.2. HM3D-ObjNav Benchmark | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the previous best-performing ... | p. 7 (4.2.2. HM3D-ObjNav Benchmark) |
| 4.1. Experimental Setting | EMPIRICAL / SOURCE-REPORTED EVALUATION | Following standard practice, we assess navigation performance using Success Rate (SR = Nsuccess Ntotal ) and Success weighted by Path Length (SPL = 1 ... | p. 6 (4.1. Experimental Setting) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Experiments on the HM3D-ObjNav benchmark. gains 12.5% in SR and 6.7% in SPL (row 3). Notably, in- troducing either AVU (row 4) ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3. Component ablation experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. The first row without any ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. Performance comparisons between our MSGNav and other existing methods for embodied navigation on Goat-Bench [19]: the multi-modal open-vocabulary navigation benchmark. (a) The ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setting - extractive PDF cue:** We evaluate our proposed approach on two established goal-oriented navigation benchmarks: 1) GOAT-Bench [19] (Multi-modal lifelong open-vocabulary dataset, 360 episodes, 36 scenes, 2669 total subtasks, ...
- **p. 6 / 4.1. Experimental Setting - extractive PDF cue:** 2) HM3DObjNav (HM3D-Semantics-v0.2 [41] from 2023 Habitat Challenge, 1000 episodes, 36 scenes, 6 goal categories).
- **p. 7 / 4.2.1. Goat-Bench Benchmark - extractive PDF cue:** These results highlight the effectiveness of our multi-modal scene graph in tackling multi-modal lifelong navigation tasks.
- **p. 7 / 4.2.1. Goat-Bench Benchmark - extractive PDF cue:** The results in Table 1 also show the outstanding performance of our MSGNav in tackling multimodal goals, lifelong navigation task settings.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. One example illustrating the key insights of our work. We introduce the Multi-modal 3D Scene Graph (M3DSG) as an alternative to traditional 3D ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Performance comparisons between our MSGNav and other existing methods for embodied navigation on Goat-Bench [19]: the multi-modal open-vocabulary navigation benchmark. (a) The superiority ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The overall framework of our MSGNav. At time step t, the agent incrementally constructs the scene graph St based on received observation It ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Demonstration of the "last-mile" problem. (a) Previ- ous methods select the nearest traversable position after target lo- calization, and often fail due to ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Experiments on the "Val Unseen" split of GOAT-Bench. "†" denotes the results we reproduced due to different settings. ObjNav [41] benchmark.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Experiments on the HM3D-ObjNav benchmark. gains 12.5% in SR and 6.7% in SPL (row 3). Notably, in- troducing either AVU (row 4) or ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Component ablation experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. The first row without any module, ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Scene graph experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. "Node-only" indicates Concept-graph [9] without object ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our proposed approach on two established goal-oriented navigation benchmarks: 1) GOAT-Bench [19] (Multi-modal lifelong open-vocabulary dataset, 360 episodes, 36 scenes, 2669 total ... | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setting), p. 6 (4.1. Experimental Setting) |
| Task/environment | 2) HM3DObjNav (HM3D-Semantics-v0.2 [41] from 2023 Habitat Challenge, 1000 episodes, 36 scenes, 6 goal categories). | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setting), p. 7 (4.2.1. Goat-Bench Benchmark) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3.1.1. Problem definition), p. 4 (3.1.2. Overview) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3.1.2. Overview), p. 7 (4.3.2. Advantage of M3DSG) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Following standard practice, we assess navigation performance using Success Rate (SR = Nsuccess Ntotal ) and Success weighted by Path Length (SPL = 1 ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Setting) |
| Table 3. Component ablation experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. The first row without any ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the previous best-performing ... | definition/direction/unit from same section | p. 7 (4.2.2. HM3D-ObjNav Benchmark) |
| Table 4. Scene graph experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. "Node-only" indicates Concept-graph [9] without ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| MSGNav achieves the best performance with 52.0% SPL and 29.6% SPL compared to both previously training-based and train-free methods. | definition/direction/unit from same section | p. 7 (4.2.1. Goat-Bench Benchmark) |
| We used the official success distance threshold from the benchmark: 0.25 for GoatBench and 1.0 for HM3D-ObjNav. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setting) |
| Figure 2. Performance comparisons between our MSGNav and other existing methods for embodied navigation on Goat-Bench [19]: the multi-modal open-vocabulary navigation benchmark. (a) The ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the previous best-performing ... | comparison identity and matched condition | p. 7 (4.2.2. HM3D-ObjNav Benchmark) |
| Table 3. Component ablation experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. The first row without any ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| MSGNav achieves the best performance with 52.0% SPL and 29.6% SPL compared to both previously training-based and train-free methods. | comparison identity and matched condition | p. 7 (4.2.1. Goat-Bench Benchmark) |
| We will show the main comparison results with other stateof-the-art methods on the Goat-Bench [19] and HM3D37159 | comparison identity and matched condition | p. 6 (4.2. Main Experimental Results) |
| Figure 2. Performance comparisons between our MSGNav and other existing methods for embodied navigation on Goat-Bench [19]: the multi-modal open-vocabulary navigation benchmark. (a) The ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Table 4. Scene graph experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. "Node-only" indicates Concept-graph [9] without ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Component ablation experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. The first row without any ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Specifically, this includes component ablation, the advantages of multimodal edges, and demonstrating how the VVD module aids in "last-mile" decision-making. | component/input/data sensitivity | p. 7 (4.3. Ablation Analysis) |
| Although our Success Path Length (SPL) is nearly the same as WMNav without any significant advantage, this may be because the VVD module prioritizes ... | component/input/data sensitivity | p. 7 (4.2.2. HM3D-ObjNav Benchmark) |
| Table 4. Scene graph experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. "Node-only" indicates Concept-graph [9] without ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: • M3DSG: We propose a multi-modal 3D scene graph that incorporates visual information, overcoming pure-text limitations and ... | As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the previous best-performing ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2.2. HM3D-ObjNav Benchmark), p. 6 (4.1. Experimental Setting), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Following standard practice, we assess navigation performance using Success Rate (SR = Nsuccess Ntotal ) and Success weighted by Path Length (SPL = 1 ... | numeric claim only at cited anchor | p. 6 (4.1. Experimental Setting) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setting - extractive PDF cue:** We evaluate our proposed approach on two established goal-oriented navigation benchmarks: 1) GOAT-Bench [19] (Multi-modal lifelong open-vocabulary dataset, 360 episodes, 36 scenes, 2669 total subtasks, ...
- **p. 6 / 4.1. Experimental Setting - extractive PDF cue:** 2) HM3DObjNav (HM3D-Semantics-v0.2 [41] from 2023 Habitat Challenge, 1000 episodes, 36 scenes, 6 goal categories).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5. Statistical box plot of candidate viewpoint scores com- puted by the VVD module and distances from GT viewpoints. representations in embodied navigation. ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | In this paper, we propose the MSGNav, a zero-shot embodied navigation framework built upon a Multi-modal 3D Scene Graph (M3DSG) that preserves visual information ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 4. Demonstration of the "last-mile" problem. (a) Previ- ous methods select the nearest traversable position after target lo- calization, and often fail due ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The task is successful if the agent reaches any target viewpoint within d meters in at most T steps; otherwise, it fails. | p. 3 (3.1.1. Problem definition) |
| To address this gap, we propose the M3DSG, an explicit and multimodal 3D scene graph that is incrementally built to encode scene contexts while ... | p. 3 (3.1.2. Overview) |
| For each candidate vi, VVD computes a visibility score by evaluating occlusion between vi and target point cloud PC¯o. | p. 6 (3.3.4. Visibility-based Viewpoint Decision (VVD)) |
| (b) Our VVD samples candidate viewpoints and computes visibility, which can select a suitable viewpoint close to GT for successful navigation. can also influence ... | p. 6 (3.3.3. Closed-Loop Reasoning (CLR)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Statistical box plot of candidate viewpoint scores com- puted by the VVD module and distances from GT viewpoints. representations in embodied navigation. Limitations ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** In this paper, we propose the MSGNav, a zero-shot embodied navigation framework built upon a Multi-modal 3D Scene Graph (M3DSG) that preserves visual information for ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Demonstration of the "last-mile" problem. (a) Previ- ous methods select the nearest traversable position after target lo- calization, and often fail due to ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Setting), p. 6 (4.1. Experimental Setting), p. 7 (4.2.1. Goat-Bench Benchmark), p. 7 (4.2.1. Goat-Bench Benchmark), metrics p. 6 (4.1. Experimental Setting), p. 8 (Figure/Table caption), p. 7 (4.2.2. HM3D-ObjNav Benchmark), p. 8 (Figure/Table caption), p. 7 (4.2.1. Goat-Bench Benchmark), p. 6 (4.1. Experimental Setting), baselines p. 7 (4.2.2. HM3D-ObjNav Benchmark), p. 8 (Figure/Table caption), p. 7 (4.2.1. Goat-Bench Benchmark), p. 6 (4.2. Main Experimental Results), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 7 (4.2.2. HM3D-ObjNav Benchmark), p. 6 (4.1. Experimental Setting), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
