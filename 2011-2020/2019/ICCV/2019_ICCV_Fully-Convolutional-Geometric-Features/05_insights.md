# Insights — Fully Convolutional Geometric Features

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_ICCV_2019/html/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_ICCV_2019/papers/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive body cue:** In this section, we propose metric learning losses for fully-convolutional feature learning.
- **p. 1 / 1. Introduction - extractive body cue:** Our approach is the most accurate and the fastest.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach does not require low-level preprocessing or 3D patches as input, and can rapidly generate high-resolution features with state-ofthe-art discriminative power.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach achieves state-of-the-art performance on the 3DMatch benchmark [36], while being nine times faster than the fastest learning-based method and 290 times faster than ...
- **p. 8 / 6.7. Runtime - extractive body cue:** On average, our approach takes about 0.36 seconds to extract features for a single fragment on 3DMatch with 2.5cm voxel size.
- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive body cue:** We used L2 normalization to project features to the surface of a hypersphere and pass the gradient from the loss through the normalization layer to ...
- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive body cue:** For the contrastive loss, we use both normalized (denoted norm.) and unnormalized features.
- **Contribution anchor:** p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 8 (6.7. Runtime), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, current pipelines limit spatial context by focusing on patches with restricted spatial extent.
- **p. 1 / 1. Introduction - extractive body cue:** The gray region shows the Pareto frontier of the prior methods. patches for feature learning is akin to extracting small 2D patches around each pixel ...
- **p. 2 / 1. Introduction - extractive body cue:** Our approach achieves state-of-the-art performance on the 3DMatch benchmark [36], while being nine times faster than the fastest learning-based method and 290 times faster than ...
- **p. 8 / 7. Conclusion - extractive body cue:** An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration.
- **p. 4 / 5. Implementation - extractive body cue:** Next, we find the hardest negatives for all positive pairs and filter out the hardest negatives that fall within the vicinity of positive pairs by ...
- **p. 4 / 5. Implementation - extractive body cue:** First, we create a matrix P that contains the indices of positive pairs (i, j) as well as an additional matrix Pdt that contains all ...
- **p. 5 / 6.1. Datasets and Training - extractive body cue:** If ICP fails or the number of overlapping voxels is less than 1k, we removed the pair from the dataset.
- **Boundary to test:** An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this section, we propose metric learning losses for fully-convolutional feature learning. | p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 1 (1. Introduction) |
| Reported outcome | We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses. | p. 4 (6. Experiments), p. 8 (Figure/Table caption) |
| Failure/limitation | An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration. | p. 8 (7. Conclusion), p. 4 (5. Implementation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Our approach does not require low-level preprocessing or 3D patches as input, and can rapidly generate high-resolution features with state-ofthe-art discriminative power.를 As the input to the network requires unique coordinates C and corresponding features F, we first downsample the input point cloud using a fast GPU-based voxel downsampling function.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this section, we propose metric learning losses for fully-convolutional feature learning.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, registration, 3D geometry, representation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This training set contains 11 sequences, which we split into train/val/test sets as follows: sequence 0 to 5 for training, sequence 7 to 8 for 8961.
3. Compare against the body-reported baseline or a matched simpler baseline: We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses..
4. Report the body metric and its denominator/aggregation: Table 6: Results on the KITTI dataset. Relative Trans- lation Error (RTE) and Relative Rotation Error (RRE) af- ter RANSAC on FCGF trained with the hardest-contrastive loss with various downsampling voxel sizes. ....
5. Re-run the body-reported ablation/failure condition: We found rotation augmentation to be a simple (SO(3) multiplication) and effective way to make FCGF invariant to relative camera pose change..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses); the primary result is directionally consistent at p. 4 (6. Experiments), p. 8 (Figure/Table caption), p. 5 (6.2. Evaluation Metrics); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 section, metric, learning mechanism이 We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the ... 대비 Table 6: Results on the KITTI dataset. Relative Trans- lation Error (RTE) and Relative Rotation Error (RRE) af- ...을 개선하고, An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
