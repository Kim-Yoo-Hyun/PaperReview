# Insights — Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ycPVp0577R; PDF retrieval source: https://arxiv.org/pdf/2503.22204.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** This enables unified static/dynamic open-vocabulary segmentation, eliminates auxiliary language fields, and significantly reduces training complexity. • Our framework features a robust object tracking module that ...
- **p. 4 / 3 Method - extractive body cue:** We introduce Segment then Splat, a unified approach for 3D open-vocabulary segmentation based on Gaussian Splatting, as illustrated in Fig.
- **p. 5 / 3 Method - extractive body cue:** Specifically, we introduce an additional object-level loss term, 5
- **p. 5 / 3 Method - extractive body cue:** To capture newly appearing objects, we introduce a detection mechanism at fixed intervals of ∆t.
- **p. 6 / 3 Method - extractive body cue:** To robustly address this, we propose a partial mask filtering strategy applied at the end of training.
- **p. 4 / 3 Method - extractive body cue:** Following Deformable 3D Gaussian Splatting [17], we incorporate a deformation field to capture scene dynamics: (δx, δr, δs) = Fθ(γ(x), γ(t)), (3) where Fθ represents ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** However, these approaches require a predefined number of objects for clustering [13] or are limited to foreground segmentation [14], and also cannot be directly applied ...
- **p. 1 / 1 Introduction - extractive body cue:** 2) Failure to capture true 3D object information, complicating 39th Conference on Neural Information Processing Systems (NeurIPS 2025).
- **p. 1 / 1 Introduction - extractive body cue:** While 3DGS has demonstrated remarkable performance in scene reconstruction and novel view synthesis, it lacks inherent semantic understandings, limiting its applicability in tasks that require ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike existing methods that adopt a "splat then segment" approach, our method reverses the process by first initializing each object with a specific set of ...
- **p. 10 / 5 Conclusion - extractive body cue:** Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such as "a sheep sitting on the chair ...
- **p. 10 / 4 Experiments - extractive body cue:** However, this minor failure does not affect the final reconstruction, as sufficient information is retained from other views.
- **p. 9 / 4 Experiments - extractive body cue:** Moreover, because DGD does not directly supervise the language embeddings of each Gaussian, Gaussians located far apart may share similar embeddings, further deteriorating segmentation quality.
- **Boundary to test:** Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such as "a sheep sitting on the chair in front of the table." Similar to ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Similar to the 3DOVS dataset, 2D pixel-based methods produce less precise object boundaries, while our method demonstrates significantly improved results. | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Failure/limitation | Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such as "a sheep sitting on the chair in front of the table." Similar to ... | p. 10 (5 Conclusion), p. 10 (4 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 "Chopsticks" Initialized Objectspecific Gaussians Reconstruction Rasterize Object Query Result Trained Objectspecific Gaussians "Chopsticks" Gaussians CLIP Rasterize Rendered Image & 2D Feature Map Queried 2D Mask Object Query Result Sf ...를 Following Deformable 3D Gaussian Splatting [17], we incorporate a deformation field to capture scene dynamics: (δx, δr, δs) = Fθ(γ(x), γ(t)), (3) where Fθ represents deformation field, which takes Gaussian mean x ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such as "a sheep sitting on the chair in front of the table." Similar to ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Gaussian Splatting, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such as "a sheep sitting on the chair in front of the table." Similar to ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: (a) Static scenes LERF_OVS 3DOVS Method mIoU↑ Time↓ mIoU↑ Time↓ 2D LangSplat [10] 46.37 62.00 82.49 68.90 LEGaussians [11] 18.79 72.00 52.12 55.90 G-Grouping [36] 29.59 77.00 76.24 56.10 3D LangSplat [10] ....
3. Compare against the body-reported baseline or a matched simpler baseline: Our method outperforms all baseline approaches..
4. Report the body metric and its denominator/aggregation: Leveraging ground-truth labels, we adopt two metrics: Object Recall Rate (ORR), defined as ORR = 1 k k X i=1 number of tracked objects number of GT objects , (12) where k ....
5. Re-run the body-reported ablation/failure condition: We conduct an ablation study on each component of our robust object tracking module, as shown in Tab..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3 Method), p. 6 (3 Method), p. 4 (3 Method); the primary result is directionally consistent at p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, include mechanism이 Our method outperforms all baseline approaches. 대비 Leveraging ground-truth labels, we adopt two metrics: Object Recall Rate (ORR), defined as ORR = 1 k k ...을 개선하고, Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
