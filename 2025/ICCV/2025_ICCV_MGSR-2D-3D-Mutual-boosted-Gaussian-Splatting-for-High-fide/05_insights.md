# Insights — MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy (Figure ...
- **p. 2 / 1. Introduction - extractive body cue:** The input consists of multi-view images captured from various camera positions and angles, under significantly varying light conditions.
- **p. 3 / 3.1. Overview - extractive body cue:** MGSR is a 2D/3D mutual-boosted framework that consists of two branches: improved 3DGS branch (Section 3.2) and 2DGS branch (Section 3.3).
- **p. 3 / 3.1. Overview - extractive body cue:** To address this limitation, we introduce a geometry-guided illumination decomposition module, which leverages depth information from the 2DGS branch to enhance rendering performance under diverse ...
- **p. 5 / 3.3. Surface reconstruction with 2DGS - extractive body cue:** The overall loss of the 2DGS branch consists of a weighted combination: L2D = Lrender + λ3(γLn + λ4Ln-TV) + λ5Ld-TV, (11) where λ3, λ4, ...
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** The total loss Ltotal of the alternating optimization is: Ltotal = w2DL2D + w3DL3D + wdepth-mutualLZ, (15) where the losses of the 3D module L3D ...
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** Specifically, as one branch reaches convergence, it will initiate our alternating optimization process first.
- **Contribution anchor:** p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 5 (3.3. Surface reconstruction with 2DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, 2DGS still cannot effectively model surfaces when ambient lighting changes.
- **p. 1 / 1. Introduction - extractive body cue:** However, despite the effectiveness of illumination decomposition in rendering, these methods are time-consuming and still struggle to achieve meaningful mesh extraction due to inherent limitations ...
- **p. 2 / 1. Introduction - extractive body cue:** Prior to alternating optimization, the two modules undergo an independent warm-up stage, and an autostop strategy is introduced to reduce unnecessary computational burdens.
- **p. 7 / 4.2. Results - extractive body cue:** To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, which fail to capture surface holes or ...
- **p. 8 / 6. Conclusion - extractive body cue:** A possible way for addressing this issue is to incorporate exposure compensation for input images, which we will investigate as a future work.
- **p. 6 / 4.1. Datasets and evaluation metrics - extractive body cue:** Due to the limitation of CD, we mainly focus on NC metric, which aligns better 27300
- **p. 7 / 4.2. Results - extractive body cue:** Previous GS-based methods fail to effectively reconstruct glass or mirror surfaces, resulting in damaged and inaccurate surfaces.
- **Boundary to test:** To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, which fail to capture surface holes or bumps.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy (Figure 1c). | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Figure 1. MGSR achieves strong NVS and SR results compared with methods based on 2DGS [6] and 3DGS [24]. The input consists of multi-view images captured from various camera positions and angles, ... | p. 2 (Figure/Table caption), p. 8 (4.2. Results) |
| Failure/limitation | To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, which fail to capture surface holes or bumps. | p. 7 (4.2. Results), p. 8 (6. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 2D Gaussians Normals Images Depths 2D-GS Branch Ref-images Ref-map × + Trans-images 3D Gaussians 3D-GS Branch Depths Mutual-boosted Supervision NVS SR Inputs under Various Light Conditions MGSR Pipeline Output Warm-up Warm-up Figure ...를 Input images NeuS2 2D-GS GOF MGSR (Ours) Coffee MuscleCar Figure 5.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, which fail to capture surface holes or bumps.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy (Figure 1c).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, which fail to capture surface holes or bumps.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: DTU [7] is a large MVS dataset, where some scenes feature unfavorable light conditions for surface reconstruction, such as overexposure, underexposure, and metallic reflections..
3. Compare against the body-reported baseline or a matched simpler baseline: MGSR visually outperforms all baselines, resulting in the best NC, with smooth surfaces and accurate color modeling..
4. Report the body metric and its denominator/aggregation: We utilize SSIM and PSNR to evaluate the rendering quality, while reconstruction accuracy is validated by 10K sampled points with Normal Consistency (NC) and Chamfer Distance (CD) measurements..
5. Re-run the body-reported ablation/failure condition: Figure 2. MGSR is a 2D/3D mutual-boosted framework with two branches: 2DGS branch (upper) for SR and 3DGS branch (bottom) for NVS. Each branch is enhanced by our specific designs. Upon receiving ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.1. Overview), p. 5 (3.3. Surface reconstruction with 2DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians); the primary result is directionally consistent at p. 2 (Figure/Table caption), p. 8 (4.2. Results), p. 7 (4.2. Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 solve, contradictions, MGSR mechanism이 MGSR visually outperforms all baselines, resulting in the best NC, with smooth surfaces and accurate color ... 대비 We utilize SSIM and PSNR to evaluate the rendering quality, while reconstruction accuracy is validated by 10K sampled ...을 개선하고, To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
