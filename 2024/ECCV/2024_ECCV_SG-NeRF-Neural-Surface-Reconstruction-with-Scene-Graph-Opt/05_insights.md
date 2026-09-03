# Insights — SG-NeRF: Neural Surface Reconstruction with Scene Graph Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8870_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08870.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of outliers.
- **p. 3 / 1 Introduction - extractive body cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...
- **p. 2 / 1 Introduction - extractive body cue:** Our method works effectively and can produce high-quality 3D reconstructions. produce a sparse scene representation.
- **p. 5 / 3 Method - extractive body cue:** 3.1 Scene Graph A scene graph G = (V, E) in SfM consists of a set of nodes V and edges E.
- **p. 5 / 3 Method - extractive body cue:** Lastly, we introduce a coarse-to-fine training strategy to ensure an efficient and stable training process (Sec.
- **p. 7 / 3 Method - extractive body cue:** Below, we first briefly review the radiance field representation and then introduce our joint optimization scheme.
- **p. 5 / 3 Method - extractive body cue:** Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec.
- **Contribution anchor:** p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** Outlier images can happen when repetitive patterns or textureless regions are present, resulting in SfM failures.
- **p. 3 / 1 Introduction - extractive body cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead to ...
- **p. 14 / 5 Conclusion - extractive body cue:** Even though our method can greatly refine the inlier poses, the improvement on outlier poses is moderate (whose effect is still largely alleviated with the ...
- **p. 13 / 4 Experiments - extractive body cue:** Please also note that there are several failure cases from the competitors indicating completely incorrect reconstruction.
- **p. 10 / 4 Experiments - extractive body cue:** Most of these poses tend to come with a large angular deviation and cannot be rectified through local optimization.
- **p. 12 / 4 Experiments - extractive body cue:** The subpar performance of the competitors is due to their pose optimization processes, namely, local optimizations, which cannot rectify the poses with significant errors.
- **Boundary to test:** Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead to incor- rect structures (NeuS [49] and Neuralangelo ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of outliers. | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Reported outcome | While BARF* achieves the best results in scene 37, it is more likely to impose negative impact on camera poses, thereby has worse performance in most scenes. | p. 13 (7.71 3.77†), p. 11 (4 Experiments) |
| Failure/limitation | Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead to incor- rect structures (NeuS [49] and Neuralangelo ... | p. 2 (Figure/Table caption), p. 14 (5 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Specifically, for each scene, the input is a set of RGB images I = {I1, I2, ..., In}, and the output is a 3D surface reconstruction S of the scene.를 The network takes a 3D location and viewing direction as input and generates the corresponding density and RGB color (i.e., radiance) as output.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead to incor- rect structures (NeuS [49] and Neuralangelo ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of outliers.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `NeRF, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead to incor- rect structures (NeuS [49] and Neuralangelo ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec..
3. Compare against the body-reported baseline or a matched simpler baseline: We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec..
4. Report the body metric and its denominator/aggregation: Table 3: Quantitative results of our ablation studies. We individually remove the use of sparsification by thresholding (w/o τ), confidence estimation (w/o CS), Intersection- over-Union loss (w/o IoU), and coarse-to-fine optimization st ....
5. Re-run the body-reported ablation/failure condition: Furthermore, we perform a series of ablation studies and analyses to verify the effectiveness of each proposed component (Sec..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method); the primary result is directionally consistent at p. 13 (7.71 3.77†), p. 11 (4 Experiments), p. 12 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 novel, framework, jointly mechanism이 We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely ... 대비 Table 3: Quantitative results of our ablation studies. We individually remove the use of sparsification by thresholding (w/o ...을 개선하고, Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
