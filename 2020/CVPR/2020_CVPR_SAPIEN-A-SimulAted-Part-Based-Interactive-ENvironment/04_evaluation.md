# Evaluation - SAPIEN: A SimulAted Part-Based Interactive ENvironment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 7 (Figure/Table caption), p. 7 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception)): This method (PBVS) achieves an 81.8% success rate for door opening.

## Evaluation Body Digest

- **p. 5 / 4.1. Robotic Perception - extractive body cue:** SAPIEN simulator, equipped with the PartNet-Mobility dataset, provides a platform for several robotic perception tasks.
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** With the large-scale PartNet-Mobility dataset, SAPIEN also supports various robotic interaction tasks, including solving low-level control tasks, such as button pushing, handle grasping, and drawer ...
- **p. 5 / 4. Tasks and Benchmarks - extractive body cue:** We demonstrate the versatile abilities of our simulator by demonstrating robotic perception and interaction tasks.
- **p. 6 / 4.1. Robotic Perception - extractive body cue:** We use all 2,346 objects over 46 categories from the PartNetMobility dataset for this task.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** After 1M interaction steps, we evaluate the performance on the unseen objects, each for 20 episodes.
- **p. 6 / 4.1. Robotic Perception - extractive body cue:** Movable Part Detection Before interacting with objects by parts, robotic agents need to first detect the parts of interest.
- **p. 7 / 4.1. Robotic Perception - extractive body cue:** We study two robotic interaction tasks: door-opening and drawer-pulling. architectures, loss designs, and training protocols.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** To demonstrate our simulator in manipulation tasks, we first use manually designed heuristic pipelines to solve the tasks.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 4. Tasks and Benchmarks (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Robotic Interaction | BENCHMARK / DATASET | This method (PBVS) achieves an 81.8% success rate for door opening. | p. 8 (4.2. Robotic Interaction) |
| 4.2. Robotic Interaction | BENCHMARK / DATASET | Using ground-truth visual information, we can achieve a 95.3% success rate. | p. 8 (4.2. Robotic Interaction) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 5: Robotic Interaction tasks. We study two robotic interaction tasks: door-opening and drawer-pulling. architectures, loss designs, and training protocols. We summarize the experimental ... | p. 7 (Figure/Table caption) |
| 4.1. Robotic Perception | BENCHMARK / DATASET | In our experiments, ResNet50 achieves better performance than PointNet++. | p. 7 (4.1. Robotic Perception) |
| 4.1. Robotic Perception | BENCHMARK / DATASET | Mask R-CNN PartNet InsSeg Ground Truth Figure 4: Movable Part Detection Results. | p. 6 (4.1. Robotic Perception) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Robotic Perception - extractive body cue:** SAPIEN simulator, equipped with the PartNet-Mobility dataset, provides a platform for several robotic perception tasks.
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** With the large-scale PartNet-Mobility dataset, SAPIEN also supports various robotic interaction tasks, including solving low-level control tasks, such as button pushing, handle grasping, and drawer ...
- **p. 5 / 4. Tasks and Benchmarks - extractive body cue:** We demonstrate the versatile abilities of our simulator by demonstrating robotic perception and interaction tasks.
- **p. 6 / 4.1. Robotic Perception - extractive body cue:** We use all 2,346 objects over 46 categories from the PartNetMobility dataset for this task.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** After 1M interaction steps, we evaluate the performance on the unseen objects, each for 20 episodes.
- **p. 6 / 4.1. Robotic Perception - extractive body cue:** Movable Part Detection Before interacting with objects by parts, robotic agents need to first detect the parts of interest.
- **p. 7 / 4.1. Robotic Perception - extractive body cue:** We study two robotic interaction tasks: door-opening and drawer-pulling. architectures, loss designs, and training protocols.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** To demonstrate our simulator in manipulation tasks, we first use manually designed heuristic pipelines to solve the tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Robot-object Interaction in SAPIEN. We show the ray-traced scene (top) and robot camera views (bottom): RGB image, surface normals, depth and semantic segmen- ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1: Comparison to other Simulation Environments. Habitat [44] is a representative for navigation environments, which include Gibson [58, 57], Minos [43] and others; they ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 2: Comparison of Articulated Part Datasets. *RBO is collected in real-world with long video sequences. Finally, there are environments that integrate full- featured physics ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: SAPIEN Simulator Overview. The left box shows SAPIEN Renderer, which takes custom shaders and scene information to produce images such as RGB-D and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: SAPIEN Enables Many Robotic Interaction Tasks. From left to right, we show five examples: faucet manipulation, object fetching, object lifting, chair folding, and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 3: Statistics of PartNet-Mobility Dataset. #M and #P shows the number of models and movable parts respectively. 3D Warehouse* and organized as in ShapeNet ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Movable Part Detection Results. The left column shows the results of Mask R-CNN [16], where each bounding box indicates a detected movable part. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4: Movable Part Detection Results. (AP% with IoU threshold 0.5) 2D and PC denote 2D images and point clouds as different input modalities for ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | SAPIEN simulator, equipped with the PartNet-Mobility dataset, provides a platform for several robotic perception tasks. | embodiment, simulator version and control stack | p. 5 (4.1. Robotic Perception), p. 7 (4.2. Robotic Interaction) |
| Task/environment | With the large-scale PartNet-Mobility dataset, SAPIEN also supports various robotic interaction tasks, including solving low-level control tasks, such as button pushing, handle grasping, and ... | reset, timeout, object/scene variation | p. 7 (4.2. Robotic Interaction), p. 5 (4. Tasks and Benchmarks) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 8 (4.2. Robotic Interaction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For door-opening, the RL agent tends to overfit the training objects, as when the number of training objects Tasks Door (Final Angle Degree) Drawer ... | definition/direction/unit from same section | p. 8 (4.2. Robotic Interaction) |
| This method (PBVS) achieves an 81.8% success rate for door opening. | definition/direction/unit from same section | p. 8 (4.2. Robotic Interaction) |
| The classification of different motion types achieves quite high accuracy, and the axis prediction for sliders (translational joints) achieves lower error than for hinges ... | definition/direction/unit from same section | p. 7 (4.1. Robotic Perception) |
| For quantitative evaluation, we report per-part-category Average Precision (AP) scores as commonly used for object detection tasks and average across all part categories to ... | definition/direction/unit from same section | p. 6 (4.1. Robotic Perception) |
| H acc. and S acc. denotes classification accuracy for hinge and slider respectively. | definition/direction/unit from same section | p. 7 (4.1. Robotic Perception) |
| We demonstrate the versatile abilities of our simulator by demonstrating robotic perception and interaction tasks. | definition/direction/unit from same section | p. 5 (4. Tasks and Benchmarks) |
| Figure 1: Robot-object Interaction in SAPIEN. We show the ray-traced scene (top) and robot camera views (bottom): RGB image, surface normals, depth and semantic ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Table 1: Comparison to other Simulation Environments. Habitat [44] is a representative for navigation environments, which include Gibson [58, 57], Minos [43] and others; ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We evaluate two baseline algorithms, ResNet-50 [17] and PointNet++ [39], that deals with the input RGB-D partial scans using either 2D or 3D formats. | comparison identity and matched condition | p. 6 (4.1. Robotic Perception) |
| Leveraging the rich assets from the PartNet-Mobility dataset and the SAPIEN rendering pipeline, we evaluate two state-of-the-art perception algorithms for object or part detection. | comparison identity and matched condition | p. 6 (4.1. Robotic Perception) |
| Table 1: Comparison to other Simulation Environments. Habitat [44] is a representative for navigation environments, which include Gibson [58, 57], Minos [43] and others; ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Table 2: Comparison of Articulated Part Datasets. *RBO is collected in real-world with long video sequences. Finally, there are environments that integrate full- featured ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| We adopt Soft ActorCritic(SAC) [15], which is one of the SOTA reinforcement learning algorithms, trained on 2, 4, 8, 16 doors or drawers, and ... | comparison identity and matched condition | p. 8 (4.2. Robotic Interaction) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Simple ambient and directional lighting without shadows are provided for RGB rendering. | component/input/data sensitivity | p. 6 (4.1. Robotic Perception) |
| With the large-scale PartNet-Mobility dataset, SAPIEN also supports various robotic interaction tasks, including solving low-level control tasks, such as button pushing, handle grasping, and ... | component/input/data sensitivity | p. 7 (4.2. Robotic Interaction) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The input of the agent consists of point clouds, normal maps and segmentation masks captured by three fixed cameras mounted on the left, right ... | This method (PBVS) achieves an 81.8% success rate for door opening. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 7 (Figure/Table caption), p. 7 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception) |
| Primary metric/result | Using ground-truth visual information, we can achieve a 95.3% success rate. | numeric claim only at cited anchor | p. 8 (4.2. Robotic Interaction) |

- Numeric sentences retained from the body:
- **p. 5 / 3.4. Profiling Analysis - extractive body cue:** The SAPIEN engine can run at about 5000Hz on the manipulation task we will describe in Sec.
- **p. 5 / 3.4. Profiling Analysis - extractive body cue:** 4.2 and can render at about 700Hz with OpenGL mode.
- **p. 5 / 3.4. Profiling Analysis - extractive body cue:** Tests were performed on a laptop with Ubuntu 18.04, on 2.2 GHz Intel i7-8750 CPU and an Nvidia GeForce RTX 2070 GPU.
- **p. 6 / 4.1. Robotic Perception - extractive body cue:** We use all 2,346 objects over 46 categories from the PartNetMobility dataset for this task.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** After 1M interaction steps, we evaluate the performance on the unseen objects, each for 20 episodes.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** After 1M interaction steps, we evaluate the performance on the unseen objects, each for 20 episodes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | If the agent cannot move the joint to the given threshold or move 11103 | p. 7 (4.2. Robotic Interaction) |
| body limitation/failure cue | in the opposite direction, then it fails. | p. 8 (4.2. Robotic Interaction) |
| body limitation/failure cue | During training, agents receive positive rewards when the target part approaches the joint limit with the opening door/drawer, while obtaining negative rewards when the ... | p. 8 (4.2. Robotic Interaction) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Tests were performed on a laptop with Ubuntu 18.04, on 2.2 GHz Intel i7-8750 CPU and an Nvidia GeForce RTX 2070 GPU. | p. 5 (3.4. Profiling Analysis) |
| The SAPIEN engine can run at about 5000Hz on the manipulation task we will describe in Sec. | p. 5 (3.4. Profiling Analysis) |
| For quantitative evaluation, we report per-part-category Average Precision (AP) scores as commonly used for object detection tasks and average across all part categories to ... | p. 6 (4.1. Robotic Perception) |
| After 1M interaction steps, we evaluate the performance on the unseen objects, each for 20 episodes. | p. 8 (4.2. Robotic Interaction) |
| First, we need proper vision methods to encode the geometric information of the scene, which may change during interaction procedures. | p. 8 (4.2. Robotic Interaction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** If the agent cannot move the joint to the given threshold or move 11103
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** in the opposite direction, then it fails.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** During training, agents receive positive rewards when the target part approaches the joint limit with the opening door/drawer, while obtaining negative rewards when the gripper ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Robotic Perception), p. 7 (4.2. Robotic Interaction), p. 5 (4. Tasks and Benchmarks), p. 6 (4.1. Robotic Perception), p. 8 (4.2. Robotic Interaction), p. 6 (4.1. Robotic Perception), metrics p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 7 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception), p. 7 (4.1. Robotic Perception), p. 5 (4. Tasks and Benchmarks), baselines p. 6 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption), p. 8 (4.2. Robotic Interaction), results p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 7 (Figure/Table caption), p. 7 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
