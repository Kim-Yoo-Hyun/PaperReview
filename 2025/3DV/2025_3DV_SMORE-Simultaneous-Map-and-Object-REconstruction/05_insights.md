# Insights — SMORE: Simultaneous Map and Object REconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://arxiv.org/pdf/2406.13896.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** An example of the depth maps produced by our method is shown in Fig.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce a global optimization that refines both ego and object poses so as to minimize a scan-to-surface reconstruction error, dramatically improving results (right).
- **p. 4 / 4.1. Decomposition - extractive body cue:** Our approach consists of applying coordinate descent to Equation (2): alternating between fixing the poses to optimize surfaces and then fixing the surfaces to optimize ...
- **p. 4 / 4. Objective - extractive body cue:** Our method aims to find the surfaces and object motions that best explain the LiDAR measurements.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, recent novel view synthesis methods have modeled AV scenes with a composition of rigid models [24, 33, 34, 43].
- **p. 4 / 4.1. Decomposition - extractive body cue:** The first step of both derivations decomposes the objective across objects.
- **p. 4 / 4.1. Decomposition - extractive body cue:** In the following sections we derive the appropriate surface and pose optimization steps from the global objective.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Decomposition), p. 4 (4. Objective), p. 1 (1. Introduction), p. 4 (4.1. Decomposition)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, investment in autonomous driving has created a new mode of depth capture - spinning LiDAR sensors atop moving vehicles - which is largely unaddressed ...
- **p. 1 / 1. Introduction - extractive body cue:** This problem has been widely studied in the context of handheld RGB-D sensors capturing humanscale scenes [23, 29, 44, 48].
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are (1) posing the classic dynamic surface reconstruction problem in the context of
- **p. 2 / 1. Introduction - extractive body cue:** Labeling in-the-wild data is extremely costly, and as a result, many autonomous driving tasks rely on reprocessing existing data of varying quality.
- **p. 3 / 1. Introduction - extractive body cue:** LiDAR-based urban scenes, (2) combining insights from actor decomposition of radiance fields and continuous-time SLAM to produce high-quality reconstructions that reduce error by 10X over ...
- **p. 6 / 5.1. Lidar Novel View Synthesis - extractive body cue:** Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. NuScenes surface reconstruction produced by aggregating LiDAR scans using human-annotated ego-pose and dynamic object bounding boxes (left). We introduce a global optimization that ...
- **Boundary to test:** Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | An example of the depth maps produced by our method is shown in Fig. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Figure 2. Dynamic object reconstructions using human-annotated bounding-box annotations (top left) tend to be noisy. Optimizing over object pose (top right) improves accuracy, while de-skewing scans to account for dynamic object motion ... | p. 2 (Figure/Table caption), p. 8 (6. Qualitative Results) |
| Failure/limitation | Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations. | p. 6 (5.1. Lidar Novel View Synthesis), p. 2 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 We assume as input a sequence of LiDAR sweeps measured at timestamps t ∈T , and coarse tracks of K objects.를 Since we are using a compositional model of the scene, we will need a coordinate frame for each component. • Ego coordinates: This is the moving ego-vehicle coordinate frame used to measure ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: An example of the depth maps produced by our method is shown in Fig.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Datasets: All of our experiments are conducted on nuScenes[3] and Argoverse 2.0[42]..
3. Compare against the body-reported baseline or a matched simpler baseline: However, the comparison is with a state-of-the-art LiDAR odometry method instead of the ground truth since we find odometry is generally superior..
4. Report the body metric and its denominator/aggregation: We report the average distance and two accuracy metrics to characterize the distribution of errors..
5. Re-run the body-reported ablation/failure condition: Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4.1. Decomposition), p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?); the primary result is directionally consistent at p. 2 (Figure/Table caption), p. 8 (6. Qualitative Results), p. 6 (5.1. Lidar Novel View Synthesis); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 example, depth, maps mechanism이 However, the comparison is with a state-of-the-art LiDAR odometry method instead of the ground truth since ... 대비 We report the average distance and two accuracy metrics to characterize the distribution of errors.을 개선하고, Iterations are stopped if the mean registration error for an object falls below 1 centimeter for ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
