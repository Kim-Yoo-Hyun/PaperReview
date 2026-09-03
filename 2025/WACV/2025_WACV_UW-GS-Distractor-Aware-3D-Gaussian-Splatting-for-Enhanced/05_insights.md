# Insights — UW-GS: Distractor-Aware 3D Gaussian Splatting for Enhanced Underwater Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** To address this issue, we propose a novel approach for color appearance formation.
- **p. 1 / 1. Introduction - extractive body cue:** To address the aforementioned issues, we propose a new Gaussian Splatting (GS)-based method, UW-GS, specifically for underwater scenes.
- **p. 2 / 1. Introduction - extractive body cue:** We also incorporated pseudo-depth maps generated from DepthAnything [47], trained with more general scenes, to enhance the robustness of our method.
- **p. 3 / 3.1. Problem formulation - extractive body cue:** Therefore, we propose a new color appearance model and a physical-based density control module in UW-GS.
- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** The left panel of Figure 2 illustrates the workflow of our method.
- **p. 4 / 3.1. Problem formulation - extractive body cue:** In the splatting process, the physical-based density control module addresses densification failures and the binary motion mask handle distractors. we propose a pixel-level mask, named ...
- **p. 5 / 3.5. Binary Motion Mask - extractive body cue:** Inspired by RobustNeRF [35], we introduce a Binary Motion Mask (BMM) ω into our reconstruction loss function to eliminate the distractors as the follows: LRec ...
- **Contribution anchor:** p. 4 (3.3. Color Appearance Model), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem formulation), p. 4 (3.3. Color Appearance Model), p. 4 (3.1. Problem formulation)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, underwater activities are often constrained by the limitations of current technologies, the scarcity of diving experts, and high operational costs.
- **p. 2 / 1. Introduction - extractive body cue:** Finally, given the scarcity of underwater datasets, we collected a new dataset featuring four expansive areas of shallow underwater scenes, each presenting unique challenges compared ...
- **p. 3 / 3.1. Problem formulation - extractive body cue:** Moreover, moving objects such as fish and floating particles pose challenges to underwater 3D reconstruction.
- **p. 4 / 3.1. Problem formulation - extractive body cue:** In the splatting process, the physical-based density control module addresses densification failures and the binary motion mask handle distractors. we propose a pixel-level mask, named ...
- **p. 1 / 1. Introduction - extractive body cue:** Unfortunately, the existing methods [26, 39] do not address this issue.
- **p. 8 / 5. Results and Discussion - extractive body cue:** The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be neglected.
- **p. 7 / 5. Results and Discussion - extractive body cue:** The limited improvement compared to 3DGS can be attributed to the unstable lighting from above the water surface.
- **Boundary to test:** The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be neglected.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address this issue, we propose a novel approach for color appearance formation. | p. 4 (3.3. Color Appearance Model), p. 1 (1. Introduction) |
| Reported outcome | For the SeaThru-NeRF dataset, our method shows the best overall performance and achieves average 2.09dB and 2.70dB PSNR improvement compared to 3DGS and Seathru-NeRF respectively, although it has the second-best SSIM in ... | p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion) |
| Failure/limitation | The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be neglected. | p. 8 (5. Results and Discussion), p. 7 (5. Results and Discussion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 The 3D Gaussians with modified color will be sent to do 2D projection and then generate pixel color in rasterization module to output the final underwater image.를 Similar to [25], we use an additional MLP f with positon encoded depth and viewing direction input to estimate medium properties: (T D i , T B i , βd i , ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be neglected.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address this issue, we propose a novel approach for color appearance formation.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be neglected.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: On the other hand, we will also use these three metrics in dynamic scenes after using motion mask provided from dataset to exclude moving objects..
3. Compare against the body-reported baseline or a matched simpler baseline: We tested our method and compared with three state of the arts: Instant-NGP [33], SeaThru-NeRF [26], and original 3DGS [22]..
4. Report the body metric and its denominator/aggregation: Figure 1. Visual comparison between 3DGS [22] and our proposed UW-GS method. Left to right: Raw videos and the results of 3DGS and UW-GS, respectively. The top row, enhanced for visualization purposes, ....
5. Re-run the body-reported ablation/failure condition: Figure 7. Examples of rendering results from Composite and Sar- dine scenes. From left to right: raw videos, results without and with BMM, respectively. restored results based on the estimated water medium ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.1. Problem formulation), p. 4 (3.1. Problem formulation), p. 5 (3.5. Binary Motion Mask); the primary result is directionally consistent at p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion), p. 7 (5. Results and Discussion); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, issue, novel mechanism이 We tested our method and compared with three state of the arts: Instant-NGP [33], SeaThru-NeRF [26], ... 대비 Figure 1. Visual comparison between 3DGS [22] and our proposed UW-GS method. Left to right: Raw videos and ...을 개선하고, The improvement of our method is not obvious in the shallow underwater scene because the disturbance ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
