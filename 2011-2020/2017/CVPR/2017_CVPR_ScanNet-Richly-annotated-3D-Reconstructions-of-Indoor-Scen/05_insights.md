# Insights — ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1702.04405; PDF retrieval source: https://arxiv.org/pdf/1702.04405. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 ...
- **p. 1 / 1. Introduction - extractive body cue:** In the collection of this dataset, we have considered two main research questions: 1) how can we design a framework that allows many people to ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** This allows us to select the floor plane based on the scan bounding box and the normal most similar to the IMU up vector direction.
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** BundleFusion produces accurate pose alignments which we then use to perform volumetric integration through VoxelHashing [62] and extract a high resolution surface mesh using the ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** There is a large variety of algorithms targeting this scenario [59, 88, 7, 62, 37, 89, 42, 9, 90, 38, 12].
- **Contribution anchor:** p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Typically, 3D deep learning methods use synthetic data to mitigate this lack of real-world data [91, 6].
- **p. 1 / 1. Introduction - extractive body cue:** Thus, many of the current RGB-D datasets [74, 92, 77, 32] are orders of magnitude smaller than their 2D counterparts.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is ...
- **p. 8 / 6. Conclusion - extractive body cue:** We demonstrated that the richlyannotated scan data collected so far in ScanNet is useful in achieving state-of-the-art performance on several 3D scene understanding tasks; we ...
- **p. 3 / 3.1. RGB-D Scanning - extractive body cue:** This feature was critical for providing intuition to users who are not familiar with the constraints and limitations of 3D reconstruction algorithms.
- **p. 5 / 3.3. Semantic Annotation - extractive body cue:** The main limitation of this interface is due to the mismatch between the corpus of available CAD models and the objects observed in the ScanNet ...
- **p. 5 / 3.3. Semantic Annotation - extractive body cue:** A promising way to alleviate this limitation is to algorithmically suggest candidate retrieved and aligned CAD models such that workers can perform an easier verification ...
- **Boundary to test:** Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is non-trivial. Thus, existing work on 3D ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 distinct spaces. | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | On the other hand, training on ScanNet translates well to testing on SceneNN; as a result, the test results on SceneNN are significantly improved by using the training data from ScanNet. | p. 7 (5.1. 3D Object Classification), p. 20 (Figure/Table caption) |
| Failure/limitation | Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is non-trivial. Thus, existing work on 3D ... | p. 1 (Figure/Table caption), p. 8 (6. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 For each input scan, we first run BundleFusion [12] at a voxel resolution of 1 cm3.를 We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably robust given handheld RGBD video data.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is non-trivial. Thus, existing work on 3D ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 distinct spaces.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Dataset, semantic, 3D reconstruction`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is non-trivial. Thus, existing work on 3D ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Our main goal driving the design of our framework was to allow untrained users to capture semantically labeled surfaces of indoor scenes with commodity hardware..
3. Compare against the body-reported baseline or a matched simpler baseline: Summary statistics for ScanNet compared to the most similar existing dataset (SceneNN [32])..
4. Report the body metric and its denominator/aggregation: Percentages indicate average instance accuracy of retrieved model to query region..
5. Re-run the body-reported ablation/failure condition: Without the turntable rotation animation, many workers only annotated from the initial view and never used camera controls despite the provided instructions..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction); the primary result is directionally consistent at p. 7 (5.1. 3D Object Classification), p. 20 (Figure/Table caption), p. 2 (Dataset); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, ScanNet, dataset mechanism이 Summary statistics for ScanNet compared to the most similar existing dataset (SceneNN [32]). 대비 Percentages indicate average instance accuracy of retrieved model to query region.을 개선하고, Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
