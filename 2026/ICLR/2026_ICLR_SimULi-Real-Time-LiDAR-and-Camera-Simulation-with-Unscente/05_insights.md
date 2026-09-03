# Insights — SimULi: Real-Time LiDAR and Camera Simulation with Unscented Transforms

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=osxP6FafPZ; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247739. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We make the following contributions: (1) we extend 3DGUT with LiDAR support and introduce an automated tiling scheme from which we derive optimal tiling parameters ...
- **p. 5 / 3 METHOD - extractive body cue:** Particle Contributions and Response.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** With the rise of end-to-end policy models, accurate sensor simulation has become a critical component in the development and evaluation of autonomous vehicle (AV) systems.
- **p. 4 / 3 METHOD - extractive body cue:** Our goal is to learn a controllable scene representation that simulates camera and LiDAR renderings from novel viewpoints in real-time (Fig.
- **p. 7 / 3 METHOD - extractive body cue:** As crosssensor data contains inconsistencies that are impossible to eliminate, this forces the representation to prioritize the reconstruction quality of one modality over the other ...
- **p. 6 / 3 METHOD - extractive body cue:** Prior work encodes camera and LiDAR into the same representation constrained with a LiDAR-supervised depth loss.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3 METHOD), p. 2 (1 INTRODUCTION), p. 4 (3 METHOD), p. 7 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, this comes at the cost of limitations inherent to the rasterization paradigm.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As they are optimized to match real-world observations, they also exhibit a smaller domain gap compared to traditional artist-generated simulators.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We make the following contributions: (1) we extend 3DGUT with LiDAR support and introduce an automated tiling scheme from which we derive optimal tiling parameters ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Dynamic Scenes. FPS numbers are averaged across Waymo Dynamic and PandaSet. Approaches that use CNNs for upsampling (Yang et al., 2023b; Tonderski et ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The choice M = 32, Nε = 16 gives the best LiDAR rendering speed (note that does not affect quality).
- **Boundary to test:** Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by rendering LiDAR directly. Our bilateral grids also ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios. | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Reported outcome | Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across all metrics for all values of ⇀d, and renders LiDAR 2→ faster. | p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Failure/limitation | Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by rendering LiDAR directly. Our bilateral grids also ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 3.4 OPTIMIZATION We jointly optimize the camera particles Gc, LiDAR particles Gl, bilateral grids A, and the environment map by sampling a random input image and LiDAR scan at each training step.를 With the rise of end-to-end policy models, accurate sensor simulation has become a critical component in the development and evaluation of autonomous vehicle (AV) systems.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by rendering LiDAR directly. Our bilateral grids also ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `sensor fusion, LiDAR, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by rendering LiDAR directly. Our bilateral grids also ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We perform experiments on all four scenes of the Waymo Interp. benchmark (Huang et al., 2023) and follow the suggested protocol of holding out every 5th frame for validation..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 5. Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across all metrics for all values of ⇀d, and renders LiDAR ....
4. Report the body metric and its denominator/aggregation: We list the median absolute depth error, mean relative depth accuracy, and chamfer distance of LiDAR predictions in meters, and intensity and ray drop accuracy for methods that support it..
5. Re-run the body-reported ablation/failure condition: We evaluate image quality through PSNR, SSIM (Wang et al., 2004), and the AlexNet variant of LPIPS (Zhang et al., 2018)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD); the primary result is directionally consistent at p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 high-fidelity, efficient, reconstruction mechanism이 Table 5. Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but ... 대비 We list the median absolute depth error, mean relative depth accuracy, and chamfer distance of LiDAR predictions in ...을 개선하고, Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
