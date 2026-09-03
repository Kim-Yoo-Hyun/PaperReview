# Insights — SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms for ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these challenges, we introduce SplatAD, a novel view synthesis method that unifies camera and lidar rendering and is designed for real-time rendering of ...
- **p. 3 / 3. Method - extractive body cue:** Our method projects 3D Gaussians with associated feature vectors onto the corresponding sensor modalities (camera and lidar) and employs sensor-specific tiling to match their distinct ...
- **p. 3 / 3.2. Camera rendering - extractive body cue:** While we retain 3DGS's high-level steps-projection and view frustum culling, tile-assignment, depth sorting, and tilebased rasterization-we introduce key adaptations to better model the unique characteristics ...
- **p. 5 / 3.3. Lidar rendering - extractive body cue:** done in our method by modifying the projection accordingly.
- **p. 5 / 3.3. Lidar rendering - extractive body cue:** While we use the expected range for training, the median range is used during inference as it, in contrast to the expected range, does not ...
- **p. 3 / 3.1. Scene representation - extractive body cue:** Last, our representation contains a learnable embedding per sensor to model their specific appearance characteristics.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3.2. Camera rendering), p. 5 (3.3. Lidar rendering), p. 5 (3.3. Lidar rendering)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Nevertheless, 3DGS-based methods for the AD setting [7, 43, 51] inherit the limitation of only being able to render camera data, overlooking the lidar modality.
- **p. 2 / 1. Introduction - extractive body cue:** Applying 3DGS to lidar sensors presents unique challenges due to their distinct characteristics.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these challenges, we introduce SplatAD, a novel view synthesis method that unifies camera and lidar rendering and is designed for real-time rendering of ...
- **p. 8 / 5. Conclusion - extractive body cue:** Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid.
- **p. 8 / 5. Conclusion - extractive body cue:** Drawing inspiration from recent advances in human reconstruction [18, 20, 26] can provide inspiration how to overcome this limitation in future research.
- **p. 7 / 4.1. Image rendering - extractive body cue:** However, we note that using Inception-v3 features instead does not change the model ranking or our conclusions.
- **p. 6 / 4. Experiments - extractive body cue:** To validate the robustness of our method, we evaluate it across multiple popular AD datasets, using the same set of hyperparameters.
- **Boundary to test:** Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms for rasterizing sparse point clouds in spherical coordinates. ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Figure 4. Removing our rolling shutter modeling compensation leads to inaccurate geometries and inconsistencies in the learning. We measure speed using resolution-agnostic megapixels per second. SplatAD consistently outperforms existing ... | p. 7 (Figure/Table caption), p. 7 (4.1. Image rendering) |
| Failure/limitation | Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid. | p. 8 (5. Conclusion), p. 8 (5. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms for rasterizing sparse point clouds in spherical coordinates. ...를 Our proposed lidar rendering matches the image rendering on a high level, but modifies each component to accurately model sensor characteristics.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms for rasterizing sparse point clouds in spherical coordinates. ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, sensor fusion, LiDAR, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Datasets: We perform experiments on PandaSet [41], Argoverse2 [38] and nuScenes [5]..
3. Compare against the body-reported baseline or a matched simpler baseline: Compared to the baselines, SplatAD produces sharp images with a high level of detail..
4. Report the body metric and its denominator/aggregation: We measure the quality of our lidar point clouds using the same metrics as in [35], i.e., median squared depth error, RMSE intensity error, ray drop accuracy, and chamfer distance, see Tab..
5. Re-run the body-reported ablation/failure condition: Further, some cameras are cropped slightly to remove views of the ego-vehicle, such as the hood and the trunk..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.3. Lidar rendering), p. 3 (3.2. Camera rendering), p. 3 (3.1. Scene representation); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 7 (4.1. Image rendering), p. 8 (4.3. Ablations); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, contributions, follows mechanism이 Compared to the baselines, SplatAD produces sharp images with a high level of detail. 대비 We measure the quality of our lidar point clouds using the same metrics as in [35], i.e., median ...을 개선하고, Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
