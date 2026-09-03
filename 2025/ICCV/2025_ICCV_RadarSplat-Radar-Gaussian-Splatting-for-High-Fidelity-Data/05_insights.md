# Insights — RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 3. Methods - extractive body cue:** To account for radar noise, we propose a noise detection method (Sec.
- **p. 3 / 3. Methods - extractive body cue:** For scene reconstruction, we present a radar model that renders radar images from 3D Gaussians based on radar physics (Sec.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** Our method produces a clear denoised image, whereas Radar Fields struggles with multipath effects.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** We propose a denoising algorithm that removes noise across detected noisy azimuth angles, θnoise ∈Θsat ∪Θmulti, identified in Sec.
- **p. 2 / 1. Introduction - extractive body cue:** This enables more realistic radar image synthesis and improved 3D geometry estimation compared to [5], as shown in Figure 1.
- **p. 6 / 3.6. Training Losses - extractive body cue:** To refine the model, we introduce two regularization losses.
- **p. 5 / 3.5. Radar Gaussian Splatting - extractive body cue:** Next, we introduce our rendering pipeline, which incorporates elevation and azimuth projection along with spectral leakage modeling.
- **Contribution anchor:** p. 3 (3. Methods), p. 3 (3. Methods), p. 5 (3.4. Denoising and Occupancy Map Pre-processing), p. 5 (3.4. Denoising and Occupancy Map Pre-processing), p. 2 (1. Introduction), p. 6 (3.6. Training Losses)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.
- **p. 2 / 1. Introduction - extractive body cue:** While Radar Fields demonstrates encouraging results, due to the lack of noise modeling, it can only synthesize preprocessed, noise-excluded radar images, making realistic radar data ...
- **p. 1 / 1. Introduction - extractive body cue:** Real-world data collection to train models is time-consuming and prohibitively expensive, while developing realistic sensor simulations during real-world driving scenarios is hindered by the persistent ...
- **p. 6 / 4.2. Novel Radar View Rendering - extractive body cue:** In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** RadarSplat also fails to model other noises when disabling the proposed noise probability. reconstruction.
- **p. 8 / 5. Conclusion - extractive body cue:** This enables radar inverse rendering for radar signal decomposition, high-fidelity radar data synthesis, and robust noise-free occupancy prediction.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Our proposed radar image denoising method preserves rich information while remaining robust to multipath effects. In contrast, the dynamic threshold approach used in ...
- **Boundary to test:** In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To account for radar noise, we propose a noise detection method (Sec. | p. 3 (3. Methods), p. 3 (3. Methods) |
| Reported outcome | With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× better in SSIM score. | p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation) |
| Failure/limitation | In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation. | p. 6 (4.2. Novel Radar View Rendering), p. 8 (4.4. Ablation Studies) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Additionally, Locc corresponds to the L1 error between the rendered occupancy state Iα output by RadarSplat and the initial occupancy map Iocc estimated in the preprocessing step to aid in training. λi ...를 Azimuth projection is then applied via a 1D convolution along the azimuth axis with kernel size 2Q and stride size Q, and a kernel weighted by the azimuth antenna profile, Gθ(θ), producing ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To account for radar noise, we propose a noise detection method (Sec.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, sensor fusion, LiDAR, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Image synthesis and geometry reconstruction evaluation on Boreas dataset [7]..
3. Compare against the body-reported baseline or a matched simpler baseline: With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× better in SSIM score..
4. Report the body metric and its denominator/aggregation: To assess the quality of occupancy estimation, we report the RMSE, Relative Chamfer Distance (R-CD), and Accuracy..
5. Re-run the body-reported ablation/failure condition: Figure 12. Ablation studies on image synthesis. RadarSplat fails to model multipath effects when disabling the proposed multipath modeling. Radar- Splat also fails to model other noises when disabling the proposed noise ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (3.6. Training Losses), p. 5 (3.4. Denoising and Occupancy Map Pre-processing), p. 5 (3.5. Radar Gaussian Splatting); the primary result is directionally consistent at p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation), p. 7 (4.3. Occupancy State Estimation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 account, radar, noise mechanism이 With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 ... 대비 To assess the quality of occupancy estimation, we report the RMSE, Relative Chamfer Distance (R-CD), and Accuracy.을 개선하고, In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
