# Evaluation - D3D-VLP: Dynamic 3D Vision-Language-Planning Model for Embodied Grounding and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_D3D-VLP_Dynamic_3D_Vision-Language-Planning_Model_for_Embodied_Grounding_and_Navigation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_D3D-VLP_Dynamic_3D_Vision-Language-Planning_Model_for_Embodied_Grounding_and_Navigation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (Evaluation/Results): evaluation statement was not recovered.

## Evaluation Body Digest

- **p. 8 / 4.5. Real-World Mobile Manipulation Experiments - extractive PDF cue:** Grounding & Grasp Place Task OK-Robot [38] 11/32 4/16 3/16 0/10 DynaMem [37] 13/32 6/16 4/16 0/10 Dynam3D+OWLv2 [42, 57] 21/32 9/16 7/16 1/10 D3D-VLP ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate D3D-VLP on a diverse suite of five challenging benchmarks: 1-3) Vision-and-Language Navigation (VLN).
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** These tasks evaluate the ability of the agent to follow natural language instructions that ranges from stepby-step directions (R2R-CE) to coarse-grained destination descriptions (REVERIE-CE) and ...
- **p. 8 / 4.5. Real-World Mobile Manipulation Experiments - extractive PDF cue:** This task consists of sub-tasks including navigation, grounding and grasping the target, and
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation study on components and training data. Settings Training data R2R-CE Nav. SG3D Grounding OSR SR SPL
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Model Architecture Comparison. The end-to-end models directly map instructions to navigation actions, and modu- lar systems assemble multiple specialized components. Our D3D- VLP ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Framework of our D3D-VLP model. Given an instruction and streaming posed RGB-D images, a Dynam3D Encoder [57] builds and updates a Multi-level 3D ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The Unified Autoregressive Formulation of our D3D-VLP model. The core 3D Vision-Language-Planning model takes a comprehensive set of inputs: the natural language instruction, ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.5. Real-World Mobile Manipulation Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.5. Real-World Mobile Manipulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Grounding & Grasp Place Task OK-Robot [38] 11/32 4/16 3/16 0/10 DynaMem [37] 13/32 6/16 4/16 0/10 Dynam3D+OWLv2 [42, 57] 21/32 9/16 7/16 1/10 ... | p. 8 (4.5. Real-World Mobile Manipulation Experiments) |
| 4.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate D3D-VLP on a diverse suite of five challenging benchmarks: 1-3) Vision-and-Language Navigation (VLN). | p. 6 (4.1. Experimental Setup) |
| 4.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | These tasks evaluate the ability of the agent to follow natural language instructions that ranges from stepby-step directions (R2R-CE) to coarse-grained destination descriptions (REVERIE-CE) ... | p. 6 (4.1. Experimental Setup) |

## Dataset / Benchmark Role

- **p. 8 / 4.5. Real-World Mobile Manipulation Experiments - extractive PDF cue:** Grounding & Grasp Place Task OK-Robot [38] 11/32 4/16 3/16 0/10 DynaMem [37] 13/32 6/16 4/16 0/10 Dynam3D+OWLv2 [42, 57] 21/32 9/16 7/16 1/10 D3D-VLP ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate D3D-VLP on a diverse suite of five challenging benchmarks: 1-3) Vision-and-Language Navigation (VLN).
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** These tasks evaluate the ability of the agent to follow natural language instructions that ranges from stepby-step directions (R2R-CE) to coarse-grained destination descriptions (REVERIE-CE) and ...
- **p. 8 / 4.5. Real-World Mobile Manipulation Experiments - extractive PDF cue:** This task consists of sub-tasks including navigation, grounding and grasping the target, and

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Model Architecture Comparison. The end-to-end models directly map instructions to navigation actions, and modu- lar systems assemble multiple specialized components. Our D3D- VLP ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Framework of our D3D-VLP model. Given an instruction and streaming posed RGB-D images, a Dynam3D Encoder [57] builds and updates a Multi-level 3D ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The Unified Autoregressive Formulation of our D3D-VLP model. The core 3D Vision-Language-Planning model takes a comprehensive set of inputs: the natural language instruction, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Composition of sample annotations in our constructed 3D CoT dataset. The fully annotated gold data is about 175K, and the partially annotated data ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Evaluation of embodied navigation benchmarks with monocular camera, ∗denotes zero-shot method. Methods System Type R2R-CE REVERIE-CE NavRAG-CE HM3D-OVON NE↓
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Evaluation of task-oriented sequential grounding and nav- igation task on SG3D-Nav [75] benchmark. Methods System Type Navigation Grounding s-SR t-SR
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation study on components and training data. Settings Training data R2R-CE Nav. SG3D Grounding OSR SR SPL
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Evaluation of real-world mobile manipulation task. Methods Nav. Grounding & Grasp Place Task OK-Robot [38] 11/32

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Grounding & Grasp Place Task OK-Robot [38] 11/32 4/16 3/16 0/10 DynaMem [37] 13/32 6/16 4/16 0/10 Dynam3D+OWLv2 [42, 57] 21/32 9/16 7/16 1/10 ... | embodiment, simulator version and control stack | p. 8 (4.5. Real-World Mobile Manipulation Experiments), p. 6 (4.1. Experimental Setup) |
| Task/environment | We evaluate D3D-VLP on a diverse suite of five challenging benchmarks: 1-3) Vision-and-Language Navigation (VLN). | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3. Our Method), p. 1 (1. Introduction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 4. Ablation study on components and training data. Settings Training data R2R-CE Nav. SG3D Grounding OSR SR SPL | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1. Model Architecture Comparison. The end-to-end models directly map instructions to navigation actions, and modu- lar systems assemble multiple specialized components. Our D3D- ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Framework of our D3D-VLP model. Given an instruction and streaming posed RGB-D images, a Dynam3D Encoder [57] builds and updates a Multi-level ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. The Unified Autoregressive Formulation of our D3D-VLP model. The core 3D Vision-Language-Planning model takes a comprehensive set of inputs: the natural language ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 1. Model Architecture Comparison. The end-to-end models directly map instructions to navigation actions, and modu- lar systems assemble multiple specialized components. Our D3D- ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Table 4. Ablation study on components and training data. Settings Training data R2R-CE Nav. SG3D Grounding OSR SR SPL | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4. Ablation study on components and training data. Settings Training data R2R-CE Nav. SG3D Grounding OSR SR SPL | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 1. Model Architecture Comparison. The end-to-end models directly map instructions to navigation actions, and modu- lar systems assemble multiple specialized components. Our D3D- ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are: • We propose D3D-VLP, a 3D vision-language-planning model that unifies multi-step planning, grounding, and navigation in unseen and ... | no result cue | PDF body cue; verify exact table/figure and matched conditions | 본문 anchor 없음 |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work could incorporate Reinforcement Learning to further enhance this framework. | p. 8 (5. Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D 32464 | p. 2 (3. Our Method) |
| RGB images Depth images Dynam3D Encoder Waypoint Predictor D3D-VLP Model "Set up a nightlight in the bathroom." Instruction Historical plans, grounded targets, action, answer ... | p. 3 (3. Our Method) |
| It means that although ∼21% individual steps are correctly executed, only ∼4% full tasks are completed. | p. 7 (4.3. Long-Horizon Grounding and Planning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Future work could incorporate Reinforcement Learning to further enhance this framework.

- **PDF anchors reviewed:** datasets p. 8 (4.5. Real-World Mobile Manipulation Experiments), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.5. Real-World Mobile Manipulation Experiments), metrics p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), results 본문 anchor 없음.
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
