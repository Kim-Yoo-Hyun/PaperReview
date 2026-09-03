# Insights — Robust and Efficient 3D Gaussian Splatting for Urban Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/supplemental/Yuan_Robust_and_Efficient_ICCV_2025_supplemental.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / Body text (section not recovered) - extractive body cue:** Appearance Transformation After reconstruction, our method enables scene appearance transformation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** In contrast, our method can complete all steps, except for the non-LOD mode, with memory usage not exceeding 24GB.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Implementation Details of Our Method We implemented our method based on gsplat [50], which offers higher computational and memory efficiency compared to the [8].
- **p. 2 / Body text (section not recovered) - extractive body cue:** Overall, our method demonstrates a clear advantage in nearly all quality-related metrics.
- **p. 3 / Body text (section not recovered) - extractive body cue:** Additional ablations Table 10 presents the results of ablation studies on the antialiasing, AbsGS, and tile-based culling components in our method.
- **p. 1 / Body text (section not recovered) - extractive body cue:** After finishing reconstruction, we use COLMAP's geo-registration to align the reconstructed model with GPS coordinates.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Therefore, the training process was extended to 50 epochs, with densification enabled during the first 25 epochs.
- **Contribution anchor:** p. 2 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 2 (Body text (section not recovered)), p. 3 (Body text (section not recovered)), p. 1 (Body text (section not recovered))

### Strongest assumption and failure boundary

- **p. 4 / Body text (section not recovered) - extractive body cue:** The LOD mode of CityGaussian encountered a bug in the Campus, resulting in a completely black rendered image.
- **p. 1 / Body text (section not recovered) - extractive body cue:** In the in-partition prioritized densification, The value of ˆdmax is identical to the partition size.
- **p. 3 / Body text (section not recovered) - extractive body cue:** Evaluation of Similarity Regularization Similarity regularization enhances the generalization ability of the appearance transformation module.
- **p. 3 / Body text (section not recovered) - extractive body cue:** In the BigCity scene, since the number of Gaussians has already reached the upper limit without anti-aliasing, enabling anti-aliasing does not allow for additional Gaussians, ...
- **p. 3 / Body text (section not recovered) - extractive body cue:** It can be observed that while smaller partition sizes effectively reduce the number of Gaussians and lower resource consumption, they also lead to a certain ...
- **Boundary to test:** In the BigCity scene, since the number of Gaussians has already reached the upper limit without anti-aliasing, enabling anti-aliasing does not allow for additional Gaussians, leading to a slight degradation in metrics.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Appearance Transformation After reconstruction, our method enables scene appearance transformation. | p. 2 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) |
| Reported outcome | Figure 8. Synthesis the two corresponding states from a new viewpoint based on the embedding vector provided by the reference image (bottom right). presents the visualization results for both scenes, demon- strating ... | p. 3 (Figure/Table caption), p. 3 (Body text (section not recovered)) |
| Failure/limitation | In the BigCity scene, since the number of Gaussians has already reached the upper limit without anti-aliasing, enabling anti-aliasing does not allow for additional Gaussians, leading to a slight degradation in metrics. | p. 3 (Body text (section not recovered)), p. 3 (Body text (section not recovered)) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 When the number of input images is 600, these adjustments yield consistent hyperparameter with the original settings.를 When conducting experiments on our own scenes, we proportionally increased the number of training iterations based on the number of input images.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In the BigCity scene, since the number of Gaussians has already reached the upper limit without anti-aliasing, enabling anti-aliasing does not allow for additional Gaussians, leading to a slight degradation in metrics.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Appearance Transformation After reconstruction, our method enables scene appearance transformation.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In the BigCity scene, since the number of Gaussians has already reached the upper limit without anti-aliasing, enabling anti-aliasing does not allow for additional Gaussians, leading to a slight degradation in metrics.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Metric Calculation Given that we have the appearance transform model, which optimizes only the embeddings of training set images, we followed a strategy similar to NeRF-W [21] to evaluate the test set ....
3. Compare against the body-reported baseline or a matched simpler baseline: Table 10. Additional qualitative ablations. Anti-Aliasing AbsGS Without With (a) (b).
4. Report the body metric and its denominator/aggregation: Overall, our method demonstrates a clear advantage in nearly all quality-related metrics..
5. Re-run the body-reported ablation/failure condition: Table 10. Additional qualitative ablations. Anti-Aliasing AbsGS Without With (a) (b).
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 3 (Body text (section not recovered)); the primary result is directionally consistent at p. 3 (Figure/Table caption), p. 3 (Body text (section not recovered)), p. 2 (Body text (section not recovered)); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Appearance, Transformation, After mechanism이 Table 10. Additional qualitative ablations. Anti-Aliasing AbsGS Without With (a) (b) 대비 Overall, our method demonstrates a clear advantage in nearly all quality-related metrics.을 개선하고, In the BigCity scene, since the number of Gaussians has already reached the upper limit without ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
