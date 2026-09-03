# Insights — Structure-from-Motion Revisited

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_cvpr_2016/papers/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose a new SfM algorithm to approach this ultimate goal.
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** We propose a novel robust next best image selection method for accurate pose estimation and reliable triangulation in Sec.
- **p. 3 / 2.2. Incremental Reconstruction - extractive body cue:** 4.5, we propose a method to identify and parameterize highly overlapping images for efficient BA of dense collections.
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** Triangulation is a crucial step in SfM, as it increases the stability of the existing model through redundancy [58] and it enables registration of new ...
- **p. 1 / 1. Introduction - extractive body cue:** Inspired by these works, increasingly largescale reconstruction systems have been developed for hundreds of thousands [1] and millions [20, 62, 51, 50] to recently a ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** Starting from a metric reconstruction, new images can be registered to the current model by solving the Perspective-n-Point (PnP) problem [18] using feature correspondences to ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** Without further refinement, SfM usually drifts quickly to a non-recoverable state.
- **Contribution anchor:** p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** While the existing systems have advanced the state of the art tremendously, robustness, accuracy, completeness, and scalability remain the key problems in incremental SfM that ...
- **p. 8 / 6. Conclusion - extractive body cue:** The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, and efficiency.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. late ...
- **p. 7 / 5. Experiments - extractive body cue:** Robust and Efficient Triangulation.
- **p. 8 / 7.82 M - extractive body cue:** The reconstruction quality is comparable for all choices of V > 0.3 and increasingly degrades for a smaller V .
- **Boundary to test:** The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, and efficiency.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we propose a new SfM algorithm to approach this ultimate goal. | p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction) |
| Reported outcome | For all datasets, we significantly outperform any other method in terms of completeness, especially for the larger models. | p. 8 (7.82 M), p. 8 (7.82 M) |
| Failure/limitation | The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, and efficiency. | p. 8 (6. Conclusion), p. 4 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 The outputs are pose estimates P = {Pc ∈SE(3) / c = 1...NP } for registered images and the reconstructed scene structure as a set of points X = {Xk ∈R3 / ...를 While the existing systems have advanced the state of the art tremendously, robustness, accuracy, completeness, and scalability remain the key problems in incremental SfM that prevent its use as a general-purpose method.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, and efficiency.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we propose a new SfM algorithm to approach this ultimate goal.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, 3D reconstruction, SLAM, geometry`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, and efficiency.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: An experiment on the Dubrovnik dataset (Fig..
3. Compare against the body-reported baseline or a matched simpler baseline: We run experiments on a large variety of datasets to evaluate both the proposed components and the overall system compared to state-of-the-art incremental (Bundler [53], VisualSFM [62]) and global SfM systems (DISCO ....
4. Report the body metric and its denominator/aggregation: After each image registration, we measure the number of registered images shared between the strategies (intersection over union) and the reconstruction error as the median distance to the ground-truth camera locations..
5. Re-run the body-reported ablation/failure condition: Figure 4. Next best view scores for Gaussian distributed points xj ∈[0, 1]×[0, 1] with mean µ and std. dev. σ. Score S w.r.t. uni- formity (left) and number of points for ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (2.2. Incremental Reconstruction), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction); the primary result is directionally consistent at p. 8 (7.82 M), p. 8 (7.82 M), p. 4 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 SfM, algorithm, ultimate mechanism이 We run experiments on a large variety of datasets to evaluate both the proposed components and ... 대비 After each image registration, we measure the number of registered images shared between the strategies (intersection over union) ...을 개선하고, The proposed components of the algorithm improve the state of the art in terms of completeness, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
