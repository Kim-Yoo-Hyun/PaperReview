# Insights — OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914-supp.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / body section not recovered - extractive body cue:** Here, we provide a detailed explanation of the Occlusion Report module that we proposed to effectively evaluate the occlusion
- **p. 1 / body section not recovered - extractive body cue:** In the development process, we tested a wide range of rendering methods and documented their different performances, which demonstrates how scene-level rendering stands out from ...
- **p. 2 / body section not recovered - extractive body cue:** This array will be denoted as PC, i.e. point count, as it is designed to store the number of points of the 3D mask projected ...
- **p. 4 / body section not recovered - extractive body cue:** The novel (unseen) classes in PLA are highlighted in blue.
- **p. 4 / body section not recovered - extractive body cue:** In S3DIS, OpenIns3D consistently achieves high results in these novel classes.
- **p. 3 / body section not recovered - extractive body cue:** The remaining masks from phase one first go through the Occlusion Report module to select the best K views.
- **p. 3 / body section not recovered - extractive body cue:** The Mask Proposal Module is built upon a lightweight version of Mask3D [14] with three decoder layers.
- **Contribution anchor:** p. 1 (body section not recovered), p. 1 (body section not recovered), p. 2 (body section not recovered), p. 4 (body section not recovered), p. 4 (body section not recovered), p. 3 (body section not recovered)

### Strongest assumption and failure boundary

- **p. 1 / body section not recovered - extractive body cue:** The section structure is listed as follows: - Section 1: More Details on Methodologies - Section 2: Implementation Details - Section 3: Per-Categories Results - ...
- **p. 4 / body section not recovered - extractive body cue:** This table comparison is conducted to demonstrate the generalization capability of the mask module.
- **p. 7 / body section not recovered - extractive body cue:** Methods BBox Prop cabinet bed chair sofa table door window bookshelf picture counter desk curtain fridge shower c. toilet sink bathtub OpenIns3D MPM-SC 17.1 57.5 ...
- **p. 6 / body section not recovered - extractive body cue:** Although these methods brought some improvement, they still proved to have strong limitations when the mask proposed was not perfect.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 1: Illustration of Local Enforced Lookup. The remaining masks from phase one first go through the Occlusion Report module to select the best K ...
- **p. 6 / body section not recovered - extractive body cue:** We used Occlusion Reports methods to select the top K views from all frames and crop out mask pixels with an enlarged bounding box.
- **Boundary to test:** Methods BBox Prop cabinet bed chair sofa table door window bookshelf picture counter desk curtain fridge shower c. toilet sink bathtub OpenIns3D MPM-SC 17.1 57.5 74.5 59.2 36.9 29.3 47.5 26.4 0.0 ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Here, we provide a detailed explanation of the Occlusion Report module that we proposed to effectively evaluate the occlusion | p. 1 (body section not recovered), p. 1 (body section not recovered) |
| Reported outcome | This approach achieved notable performance, primarily due to the high quality of 2D images. | p. 6 (body section not recovered), p. 7 (body section not recovered) |
| Failure/limitation | Methods BBox Prop cabinet bed chair sofa table door window bookshelf picture counter desk curtain fridge shower c. toilet sink bathtub OpenIns3D MPM-SC 17.1 57.5 74.5 59.2 36.9 29.3 47.5 26.4 0.0 ... | p. 7 (body section not recovered), p. 6 (body section not recovered) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Most other methods in this comparison use an object-centred rendering approach where a depth map or point cloud is projected into images for classification.를 OpenIns3D: 3D Open-vocabulary Instance Segmentation 3 Unmatched masks after MGL View angle 10.8 0.0 90.2 80.3 … 32.9 Occlusion Rate (%) Occlusion Report Cropped images Mask2Pixel map Top K best views 2D ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Methods BBox Prop cabinet bed chair sofa table door window bookshelf picture counter desk curtain fridge shower c. toilet sink bathtub OpenIns3D MPM-SC 17.1 57.5 74.5 59.2 36.9 29.3 47.5 26.4 0.0 ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Here, we provide a detailed explanation of the Occlusion Report module that we proposed to effectively evaluate the occlusion
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Methods BBox Prop cabinet bed chair sofa table door window bookshelf picture counter desk curtain fridge shower c. toilet sink bathtub OpenIns3D MPM-SC 17.1 57.5 74.5 59.2 36.9 29.3 47.5 26.4 0.0 ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To demonstrate this, we provide some demos deploying OpenIns3D on Lidarbased datasets like ArkitScene Lidar, whose 2D images are not available, and.
3. Compare against the body-reported baseline or a matched simpler baseline: Compared with other SOTA models on OVOD, cross-domain OpenIns3D still has competitive performance..
4. Report the body metric and its denominator/aggregation: Fig. 1: Illustration of Local Enforced Lookup. The remaining masks from phase one first go through the Occlusion Report module to select the best K views. The selected images are cropped before ....
5. Re-run the body-reported ablation/failure condition: Raw point clouds GT instance masks Predicted masks without filtering Predicted masks with filtering Raw point clouds GT instance masks Predicted masks without filtering Predicted masks with filtering Fig..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (body section not recovered), p. 3 (body section not recovered), p. 3 (body section not recovered); the primary result is directionally consistent at p. 6 (body section not recovered), p. 7 (body section not recovered), p. 8 (body section not recovered); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Here, provide, detailed mechanism이 Compared with other SOTA models on OVOD, cross-domain OpenIns3D still has competitive performance. 대비 Fig. 1: Illustration of Local Enforced Lookup. The remaining masks from phase one first go through the Occlusion ...을 개선하고, Methods BBox Prop cabinet bed chair sofa table door window bookshelf picture counter desk curtain fridge ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
