# Evaluation - ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html; PDF retrieval source: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Abstract), p. 9 (Abstract), p. 8 (Figure/Table caption), p. 9 (Abstract), p. 21 (Figure/Table caption), p. 17 (Figure/Table caption)): We adopted pointcloud observation mode and designed point cloud-based vision architectures as our feature extractor since previous work [46] has achieved significant performance improvements by using point clouds instead of ...

## Evaluation Body Digest

- **p. 9 / Abstract - extractive body cue:** We plan to process more objects from the PartNet-Mobility dataset [62] and add them to our ManiSkill assets; 2) While the four tasks currently provided ...
- **p. 9 / Abstract - extractive body cue:** Models are trained with our demonstrations dataset, with 300 demonstration trajectories per training environment.
- **p. 8 / Abstract - extractive body cue:** We designed and benchmarked this architecture since it allows the model to capture the relation between different objects and possibly provides better performance.
- **p. 8 / Abstract - extractive body cue:** For learning-from-demonstrations algorithms on top of point cloud architectures, we benchmark two approaches - Imitation Learning (IL) and Offline/Batch Reinforcement Learning (Offline/Batch RL).
- **p. 21 / Figure/Table caption - extractive body cue:** Table 5: The success rates of SAC [60] agents on OpenCabinetDrawer trained from scratch with 106 time-steps on different numbers of cabinets. The SAC agents ...
- **p. 9 / Abstract - extractive body cue:** 3.2 Object-Level Generalization Results Algorithm BC BCQ TD3+BC Architecture PointNet PointNet + Transformer PointNet + Transformer PointNet + Transformer Split Training Test Training Test Training ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: The average success rates of different agents on one single environment (fixed object instance) of OpenCabinetDrawer with different numbers of demonstration trajectories. The ...
- **p. 8 / Abstract - extractive body cue:** 3.1 Single Environment Results #Demo Trajectories 10 30 100 300 1000 #Gradient Steps 2000 4000 10000 20000 40000 PointNet, BC 0.13 0.23 0.37 0.68 0.76 ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** B.5 Evaluation Kit (p. 16); B.5 Evaluation Kit (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Abstract | BENCHMARK / DATASET | We adopted pointcloud observation mode and designed point cloud-based vision architectures as our feature extractor since previous work [46] has achieved significant performance improvements ... | p. 8 (Abstract) |
| Abstract | BENCHMARK / DATASET | The results suggest that existing works on 3D deep learning and learning-from-demonstrations algorithms might have been insufficient yet to achieve good performance when trained ... | p. 9 (Abstract) |
| Figure/Table caption | BENCHMARK / DATASET | Table 2: The average success rates of different agents on one single environment (fixed object instance) of OpenCabinetDrawer with different numbers of demonstration trajectories. ... | p. 8 (Figure/Table caption) |
| Abstract | BENCHMARK / DATASET | 3.2 Object-Level Generalization Results Algorithm BC BCQ TD3+BC Architecture PointNet PointNet + Transformer PointNet + Transformer PointNet + Transformer Split Training Test Training Test ... | p. 9 (Abstract) |
| Figure/Table caption | BENCHMARK / DATASET | Table 5: The success rates of SAC [60] agents on OpenCabinetDrawer trained from scratch with 106 time-steps on different numbers of cabinets. The SAC ... | p. 21 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / Abstract - extractive body cue:** We plan to process more objects from the PartNet-Mobility dataset [62] and add them to our ManiSkill assets; 2) While the four tasks currently provided ...
- **p. 9 / Abstract - extractive body cue:** Models are trained with our demonstrations dataset, with 300 demonstration trajectories per training environment.
- **p. 8 / Abstract - extractive body cue:** We designed and benchmarked this architecture since it allows the model to capture the relation between different objects and possibly provides better performance.
- **p. 8 / Abstract - extractive body cue:** For learning-from-demonstrations algorithms on top of point cloud architectures, we benchmark two approaches - Imitation Learning (IL) and Offline/Batch Reinforcement Learning (Offline/Batch RL).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: A subset of environments in ManiSkill. We currently support 4 different manipulation tasks: OpenCabinetDoor, OpenCabinetDrawer, PushChair, and MoveBucket; each features a large variety ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: ManiSkill features diverse articulated objects with complex topological and geometric variations, such as different numbers and shapes of doors and/or drawers on different ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Rendered point clouds from our tasks. ManiSkill supports 3D visual inputs which are widely accessible in real environments, allowing various computer vision models ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Dataset statistics for ManiSkill. For OpenCabinetDoor and OpenCabinetDrawer, numbers outside of the parenthesis indicate the number of unique cabinets, where each cabinet may ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: RGB-D (RGB/Depth) and point cloud observations in ManiSkill. Left two images: RGB-D image from one of the three cameras mounted on the robot. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: The average success rates of different agents on one single environment (fixed object instance) of OpenCabinetDrawer with different numbers of demonstration trajectories. The ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Mean and standard deviation of average success rates on training and test environments of each task over 5 different runs, under the point ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 5: Overall illustration of ManiSkill. We manually re-model and postprocess objects from the PartNet-Mobility dataset, split them into training and test sets, and then ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We plan to process more objects from the PartNet-Mobility dataset [62] and add them to our ManiSkill assets; 2) While the four tasks currently ... | embodiment, simulator version and control stack | p. 9 (Abstract), p. 9 (Abstract) |
| Task/environment | Models are trained with our demonstrations dataset, with 300 demonstration trajectories per training environment. | reset, timeout, object/scene variation | p. 9 (Abstract), p. 8 (Abstract) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 5 (Abstract), p. 4 (Abstract) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 5 (Abstract), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 5: The success rates of SAC [60] agents on OpenCabinetDrawer trained from scratch with 106 time-steps on different numbers of cabinets. The SAC ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| 3.2 Object-Level Generalization Results Algorithm BC BCQ TD3+BC Architecture PointNet PointNet + Transformer PointNet + Transformer PointNet + Transformer Split Training Test Training Test ... | definition/direction/unit from same section | p. 9 (Abstract) |
| Table 2: The average success rates of different agents on one single environment (fixed object instance) of OpenCabinetDrawer with different numbers of demonstration trajectories. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| 3.1 Single Environment Results #Demo Trajectories 10 30 100 300 1000 #Gradient Steps 2000 4000 10000 20000 40000 PointNet, BC 0.13 0.23 0.37 0.68 ... | definition/direction/unit from same section | p. 8 (Abstract) |
| For each task, the average test success rates are calculated over the 10 test environments and 50 evaluation trajectories per environment. | definition/direction/unit from same section | p. 9 (Abstract) |
| Figure 5: Overall illustration of ManiSkill. We manually re-model and postprocess objects from the PartNet-Mobility dataset, split them into training and test sets, and ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Table 9: The success rates of TD3+BC trained with different values of α on one environment of OpenCabinetDrawer and 300 demonstration trajectories. The algorithm ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 6: When decomposing a bucket (a), standard VHACD [74] algorithm (b, 2340 faces) misses details, and tends to produce artifacts, such as bumps ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Therefore, we designed several baselines and open-sourced their implementations here to encourage future explorations in the field. | comparison identity and matched condition | p. 8 (Abstract) |
| 3 Baseline Architectures, Algorithms, and Experiments Learning object-level generalizable manipulation skills through 3D visual inputs and learning-fromdemonstrations algorithms has been underexplored. | comparison identity and matched condition | p. 8 (Abstract) |
| Interestingly, we did not find offline RL algorithms to outperform BC. | comparison identity and matched condition | p. 9 (Abstract) |
| Table 4: Mean and standard deviation of FPS (frame per second) of the environments in ManiSkill. In state mode, most computations are used on ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| Figure 5: Overall illustration of ManiSkill. We manually re-model and postprocess objects from the PartNet-Mobility dataset, split them into training and test sets, and ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| Table 6: The hyperparameters of SAC for demonstration generation. D Implementation Details of Baseline Architectures, Algorithms, and | comparison identity and matched condition | p. 22 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| While network architectures and algorithms play an important role in the performance, learning manipulation skills from demonstrations is challenging without a large number of ... | component/input/data sensitivity | p. 8 (Abstract) |
| Intuitively, this allows the extracted feature to not only contain geometric information of objects, but also contain the relation between the robot and each ... | component/input/data sensitivity | p. 8 (Abstract) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Here we propose SAPIEN Manipulation Skill Benchmark (ManiSkill) to benchmark manipulation skills over diverse objects in a full-physics simulator. | We adopted pointcloud observation mode and designed point cloud-based vision architectures as our feature extractor since previous work [46] has achieved significant performance improvements ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Abstract), p. 9 (Abstract), p. 8 (Figure/Table caption), p. 9 (Abstract), p. 21 (Figure/Table caption), p. 17 (Figure/Table caption) |
| Primary metric/result | The results suggest that existing works on 3D deep learning and learning-from-demonstrations algorithms might have been insufficient yet to achieve good performance when trained ... | numeric claim only at cited anchor | p. 9 (Abstract) |

- Numeric sentences retained from the body:
- **p. 9 / Abstract - extractive body cue:** 3.2 Object-Level Generalization Results Algorithm BC BCQ TD3+BC Architecture PointNet PointNet + Transformer PointNet + Transformer PointNet + Transformer Split Training Test Training Test Training ...
- **p. 9 / Abstract - extractive body cue:** This takes about 5 hours for BC, 35 hours for BCQ, and 9 hours for TD3+BC using the PointNet + Transformer architecture on one NVIDIA ...
- **p. 3 / Abstract - extractive body cue:** It currently includes a total of 162 objects from 3 object categories (more objects are being added) selected and manually processed from a widely used ...
- **p. 3 / Abstract - extractive body cue:** Second, ManiSkill focuses on 4 object-centric manipulation tasks that exemplify household manipulation skills with different types of object motions, thereby posing challenges to distinct aspects ...
- **p. 3 / Abstract - extractive body cue:** Third, to facilitate learning-from-demonstration methods, we have collected a large number of successful trajectories (~36,000 trajectories, ~1.5M 3D point cloud / RGB-D frames in total).
- **p. 4 / Abstract - extractive body cue:** Our data is high-quality, that every object is verified to support RL. • The manipulation tasks we design target at distinct challenges of manipulation skills ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It is worth noting that our experiment results should not discourage benchmark users to include failure trajectories and find better usage of offline RL ... | p. 9 (Abstract) |
| body limitation/failure cue | Figure 4: RGB-D (RGB/Depth) and point cloud observations in ManiSkill. Left two images: RGB-D image from one of the three cameras mounted on the ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | We fix issues if we cannot learn a policy to achieve the task. | p. 8 (Abstract) |
| body limitation/failure cue | For example, certain cabinet drawers may be stuck due to inaccurate overlapping between collision shapes. | p. 8 (Abstract) |
| body limitation/failure cue | 4 Conclusion and Limitations In this work, we propose ManiSkill, an articulated benchmark for generalizable physical object manipulation from 3D visual inputs with diverse ... | p. 9 (Abstract) |
| body limitation/failure cue | Table 4: Mean and standard deviation of FPS (frame per second) of the environments in ManiSkill. In state mode, most computations are used on ... | p. 17 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We follow their original implementations and tune the hyperparameters. | p. 8 (Abstract) |
| All code of our benchmark (simulator, environment, SDK, and baselines) is open-sourced, and a challenge facing interdisciplinary researchers will be held based on the ... | p. 1 (Abstract) |
| ManiSkill supports 3D visual inputs which are widely accessible in real environments, allowing various computer vision models to be applied. | p. 3 (Abstract) |
| While oftentimes other benchmarks are limited to a single domain of research and a single modality, our benchmark supports three different tracks for researchers ... | p. 3 (Abstract) |
| Therefore, this track encourages researchers to explore 3D computer vision network architectures for generalizable shape understanding over complex topologies and geometries. | p. 7 (Abstract) |
| Moreover, ManiSkill benchmark aims to encourage interdisciplinary insights from computer vision, reinforcement learning, and robotics to advance generalizable physical object manipulation. | p. 7 (Abstract) |
| Details of the algorithm implementations are presented in Sec D of the supplementary material. | p. 8 (Abstract) |
| We train each model for 150k gradient steps. | p. 9 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Abstract - extractive body cue:** It is worth noting that our experiment results should not discourage benchmark users to include failure trajectories and find better usage of offline RL methods, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: RGB-D (RGB/Depth) and point cloud observations in ManiSkill. Left two images: RGB-D image from one of the three cameras mounted on the robot. ...
- **p. 8 / Abstract - extractive body cue:** We fix issues if we cannot learn a policy to achieve the task.
- **p. 8 / Abstract - extractive body cue:** For example, certain cabinet drawers may be stuck due to inaccurate overlapping between collision shapes.
- **p. 9 / Abstract - extractive body cue:** 4 Conclusion and Limitations In this work, we propose ManiSkill, an articulated benchmark for generalizable physical object manipulation from 3D visual inputs with diverse object ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 4: Mean and standard deviation of FPS (frame per second) of the environments in ManiSkill. In state mode, most computations are used on physical ...

- **Evidence anchors reviewed:** datasets p. 9 (Abstract), p. 9 (Abstract), p. 8 (Abstract), p. 8 (Abstract), metrics p. 21 (Figure/Table caption), p. 9 (Abstract), p. 8 (Figure/Table caption), p. 8 (Abstract), p. 9 (Abstract), p. 17 (Figure/Table caption), baselines p. 8 (Abstract), p. 8 (Abstract), p. 9 (Abstract), p. 17 (Figure/Table caption), p. 17 (Figure/Table caption), p. 22 (Figure/Table caption), results p. 8 (Abstract), p. 9 (Abstract), p. 8 (Figure/Table caption), p. 9 (Abstract), p. 21 (Figure/Table caption), p. 17 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
