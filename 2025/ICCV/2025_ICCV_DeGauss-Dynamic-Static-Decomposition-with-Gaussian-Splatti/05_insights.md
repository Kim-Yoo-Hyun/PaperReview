# Insights — DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • ...
- **p. 2 / 1. Introduction - extractive body cue:** We show that our method achieves superior results compared to baseline dynamic scene modeling approaches, with notable advantages across diverse datasets [13, 21].
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** To address this, we introduce a brightness control mask that enhances the background branch's capacity to model non-Lambertian effects.
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** Our method simultaneously reconstructs the 3D scene and learns an unsupervised decomposition into decoupled static background and dynamic foreground branches, where the update is loosely ...
- **p. 5 / 3.6. Unsupervised scene decomposition - extractive body cue:** Our method offers significantly greater robustness in handling local minimas.
- **p. 3 / 3.2. Foreground deformable gaussian - extractive body cue:** The spatial-temporal module comprises an encoder H and a decoder D.
- **p. 3 / 3.2. Foreground deformable gaussian - extractive body cue:** The encoder, based on Hexplane [3], extracts spatio-temporal features based on reference time t with fd = H(Gf, t), and the multi-head decoder D predicts ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control), p. 4 (3.4. Background Brightness Control), p. 5 (3.6. Unsupervised scene decomposition), p. 3 (3.2. Foreground deformable gaussian)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** This limitation is further amplified in egocentric videos, a rapidly growing data source that introduces unique challenges for 3D scene reconstruction[7, 16, 29, 32, 41].
- **p. 1 / 1. Introduction - extractive body cue:** These factors introduce significant challenges for This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 2 / 1. Introduction - extractive body cue:** While these methods improve generalization across diverse inputs, they suffer from long training times and struggle to balance dynamic and static representations.
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, dynamic Gaussian methods [36, 39] learn deformation fields for temporal modeling but tend to overfit to training views and generalize poorly to novel viewpoints ...
- **p. 8 / 6. Conclusion - extractive body cue:** This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting.
- **p. 7 / 4.3. Results - extractive body cue:** We show our method robustly handles occlusion and reconstructs fine static details compared to SpotlessSplats [24]in Fig.
- **p. 7 / 4.3. Results - extractive body cue:** Our method robustly handles various challenges, preserving clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference test views, we report detailed per-scene metrics ...
- **Boundary to test:** This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • Our proposed method achieves ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Notably, our method consistently achieves significantly better LPIPS scores over the previous SOTA method SpotlessSplats [24]. | p. 7 (4.3. Results), p. 7 (4.3. Results) |
| Failure/limitation | This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting. | p. 8 (6. Conclusion), p. 7 (4.3. Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • Our proposed method achieves ...를 SH Attributes Foreground Render Probabilistic Mask Brightness Control Background Render Controlled Background Composed Render Input Image Activation Rasterize Mask Rasterize Rasterize Foreground Gaussians Background Gaussians Mask Attri ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • Our proposed method achieves ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: HyperNeRF Dataset [21] features real-world activities captured with smooth trajectories..
3. Compare against the body-reported baseline or a matched simpler baseline: Compared to baseline methods [10, 24, 31], our method models high-quality distractor-free static background with accurate foreground separation..
4. Report the body metric and its denominator/aggregation: 2, where our methods achieve consistently better LPIPS scores..
5. Re-run the body-reported ablation/failure condition: Left of the dashed line: composed render comparisons; right: static reconstruction comparison(without camera masks)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.4. Background Brightness Control), p. 3 (3.2. Foreground deformable gaussian), p. 3 (3.2. Foreground deformable gaussian); the primary result is directionally consistent at p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (4.3. Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, DeGauss mechanism이 Compared to baseline methods [10, 24, 31], our method models high-quality distractor-free static background with accurate ... 대비 2, where our methods achieve consistently better LPIPS scores.을 개선하고, This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
