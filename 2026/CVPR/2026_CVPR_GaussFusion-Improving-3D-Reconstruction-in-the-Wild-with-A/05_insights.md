# Insights — GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse reconstruction ...
- **p. 2 / 1. Introduction - extractive body cue:** We present GaussFusion, a video-to-video generative model for robust 3D reconstruction that features as key component the GP-Buffer, a pixel-aligned video representation that encodes multi-modal ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** The contribution γi is the product of the learned opacity αi and the 2D Gaussian function evaluated at the pixel center u with projected mean ...
- **p. 1 / 1. Introduction - extractive body cue:** Photorealistic 3D reconstruction and novel-view synthesis are fundamental problems in computer vision, with applications in virtual reality, autonomous driving, and robotics.
- **p. 1 / 1. Introduction - extractive body cue:** However, despite these advances, current methods still suffer from artifacts in sparseview and under-captured scenarios, and degrade significantly at novel views far from training views ...
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** 3.3) along this trajectory to obtain novel renderings, which are then refined by our geometry-aware video generator to produce artifactfree frames.
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** Finally, we merge the generated novel views with the original inputs and optimize the 3D Gaussian splats using the standard photometric loss (Eq.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminaries), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. 3D Reconstruction Updating)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** To address these limitations, several methods [3, 32, 34, 41, 46, 49, 56, 66, 70] have explored leveraging generative priors to enhance 3D reconstruction by ...
- **p. 2 / 1. Introduction - extractive body cue:** Similarly, MVSplat360 [7] refines feed-forward reconstructions but fails to generalize to optimization-based pipelines, as it is tightly coupled to a specific feed-forward model [6].
- **p. 1 / 1. Introduction - extractive body cue:** However, despite these advances, current methods still suffer from artifacts in sparseview and under-captured scenarios, and degrade significantly at novel views far from training views ...
- **p. 2 / 1. Introduction - extractive body cue:** This raises a key question: How can we train a single high-quality reconstruction refinement model that generalizes across different 3DGS paradigms?
- **p. 8 / 6. Conclusion - extractive body cue:** We discuss our limitations and future work in Supp.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) [23] reconstruction using either per-scene optimization or ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. GaussFusion Video Generator Architecture. Our model refines video latents using geometry-aware conditioning derived from 3D Gaussian splatting (3DGS). A Gaussian primitive buffer-comprising color, ...
- **Boundary to test:** We discuss our limitations and future work in Supp.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse reconstruction pipelines. • A comprehensive ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable performance with significantly improved runtime efficiency, reachin ... | p. 6 (15.11 FPS), p. 1 (Figure/Table caption) |
| Failure/limitation | We discuss our limitations and future work in Supp. | p. 8 (6. Conclusion), p. 1 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 (2) Feed-Forward 3DGS Reconstruction Models learn to directly predict a complete set of 3D Gaussian parameters from a small set of posed/unposed input images [4, 58, 60, 68].를 Given a target sample x1 (e.g., image or video), random noise x0 ∼N(0, I), and a timestep t ∈[0, 1], the intermediate latent xt is defined by: xt = tx1 + (1 ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We discuss our limitations and future work in Supp.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse reconstruction pipelines. • A comprehensive ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We discuss our limitations and future work in Supp.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Testing scenes are drawn from the official test splits of each dataset, which remain unseen during training..
3. Compare against the body-reported baseline or a matched simpler baseline: The model trained exclusively on DL3DV outperforms all baselines trained on the same dataset by a substantial margin in terms of image quality..
4. Report the body metric and its denominator/aggregation: A slightly higher FID score is observed, which we attribute to the reduced number of denoising steps and minor loss of high-frequency details..
5. Re-run the body-reported ablation/failure condition: GaussFusion effectively removes rendering artifacts such as blur, floaters, ghosting, and texture distortions, producing sharper geometry, cleaner reconstruction than Splatfacto [61], GenFusion [57], DiFiX3D+ [55], and ExploreGS [25], a ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.4. 3D Reconstruction Updating), p. 5 (3.4. 3D Reconstruction Updating); the primary result is directionally consistent at p. 6 (15.11 FPS), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, follows mechanism이 The model trained exclusively on DL3DV outperforms all baselines trained on the same dataset by a ... 대비 A slightly higher FID score is observed, which we attribute to the reduced number of denoising steps and ...을 개선하고, We discuss our limitations and future work in Supp. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
