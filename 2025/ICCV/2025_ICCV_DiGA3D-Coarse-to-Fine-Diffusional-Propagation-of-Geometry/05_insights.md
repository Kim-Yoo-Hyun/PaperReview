# Insights — DiGA3D: Coarse-to-Fine Diffusional Propagation of Geometry and Appearance for Versatile 3D Inpainting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to consistently ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline with a coarseThis ICCV paper is the Open Access version, provided ...
- **p. 5 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** For each scene, we present two novel views to compare the rendering quality and multi-view consistency with the existing state-of-the-art methods. ter is conducted independently.
- **p. 2 / 1. Introduction - extractive body cue:** Thus, our method offers a coarse-to-fine pipeline that can effectively bridge consistent 2D appearance and 3D geometry, enabling versatile 3D inpainting.
- **p. 4 / 3.3. Multi-view Consistent Image Inpainting - extractive body cue:** Prior to employing AFP, we introduce a robust strategy for selecting the reference views.
- **p. 4 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** Therefore, we propose a texture-geometry guided SDS (TG-SDS) loss within the latent space of ControlNet [42].
- **p. 3 / 3.1. Preliminary - extractive body cue:** In the coarse stage, we employ DDIM Inversion [33] to generate deterministic latents, which are then used to produce coarsely consistent inpainting results with a ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 2 (1. Introduction), p. 4 (3.3. Multi-view Consistent Image Inpainting), p. 4 (3.4. Texture-Geometry Guided SDS Loss)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** This limitation becomes particularly evident when inpainting regions require significant geometric changes.
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline with a coarseThis ICCV paper is the Open Access version, provided ...
- **p. 2 / 1. Introduction - extractive body cue:** to-fine manner that utilizes 3D Gaussian Splatting (3DGS) to leverage diffusion priors for propagating appearance and geometry across multiple views.
- **p. 3 / 3.2. Problem formulation and overview - extractive body cue:** We define the problem of versatile 3D inpainting using 3DGS as follows: Given a pretrained 3D Gaussians G, a positive prompt Tp, a negative prompt ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Text-to-3D has seen significant advancements by optimizing a 3D representation using a 2D pre-trained image diffusion prior ϵϕ, based on Score Distillation Sampling (SDS) [27].
- **p. 7 / 4.3.1. Object Removal - extractive body cue:** While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show significant ...
- **Boundary to test:** While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show significant advantages in PSNR, masked PSNR, and masked ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to consistently propagate appearance and geometry in a coarse-to-fine ... | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | Our method achieves clear improvements in PSNR and obtains better scores in most metrics. | p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study) |
| Failure/limitation | While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show significant advantages in PSNR, masked PSNR, and masked ... | p. 7 (4.3.1. Object Removal) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `conditioning observation와 noisy/intermediate sample → latent/noise variable와 conditional distribution → generated sample, action chunk 또는 trajectory`.
- 이 논문의 재사용 가능한 지점은 The outputs of AFP are the inpainted image Ii and the depth map Di estimated by the monocular depth estimator [30] ˜D.를 The outputs of texture-geometry warping are the texture map C′ i and the depth map D′ i. jective is to inpaint the 3D Gaussians based on these text prompts.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 latent/noise variable와 conditional distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show significant advantages in PSNR, masked PSNR, and masked ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to consistently propagate appearance and geometry in a coarse-to-fine ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Diffusion, Generation, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show significant advantages in PSNR, masked PSNR, and masked ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We evaluate our versatile 3D inpainting methods in three different datasets with multi-view images from feed-forward and 360 degrees: 1) SPIn-NeRF dataset [25] provide 10 scenes that each scene includes 60 images ....
3. Compare against the body-reported baseline or a matched simpler baseline: We compared our method with four baselines, i.e., SPIn-NeRF [25], NeRFiller [38], MVIP-NeRF [7], and GScream [37]..
4. Report the body metric and its denominator/aggregation: We find that our methods achieve relatively high scores compared to other approaches, demonstrating that they can generate more realistic and relevant objects with text prompts..
5. Re-run the body-reported ablation/failure condition: The visualization of ablation study for key components on the object replacement task using LLFF dataset [22]..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.4. Texture-Geometry Guided SDS Loss), p. 3 (3.1. Preliminary), p. 4 (3.3. Multi-view Consistent Image Inpainting); the primary result is directionally consistent at p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study), p. 7 (4.3.1. Object Removal); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, outlined mechanism이 We compared our method with four baselines, i.e., SPIn-NeRF [25], NeRFiller [38], MVIP-NeRF [7], and GScream ... 대비 We find that our methods achieve relatively high scores compared to other approaches, demonstrating that they can generate ...을 개선하고, While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
