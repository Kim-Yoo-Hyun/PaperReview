# Insights — DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that ...
- **p. 1 / 1. Introduction - extractive body cue:** Given a set of blurry images and corresponding event streams, we propose a novel framework to construct deblurring 3DGS by jointly leveraging the EDI [33] ...
- **p. 2 / 1. Introduction - extractive body cue:** To restore both accurate color and well-defined details, we introduce a novel framework that uses the EDI prior to achieve 1) fine-grained details, 2) accurate ...
- **p. 4 / 4. Our Method - extractive body cue:** To this end, we propose a novel optimization problem that leverages EDI prior to further constrain the 3DGS in terms of 1) fine-grained details, 2) ...
- **p. 1 / 1. Introduction - extractive body cue:** Our DiET-GS++ enables highquality novel-view synthesis by recovering precise color and welldefined details from the blurry multi-view images. tured and free from any artifact.
- **p. 5 / 4. Our Method - extractive body cue:** Since the input of the diffusion model ˆCB is obtained by averaging a set of rendered sharp images { ˆC}n-1 i=0 along the camera trajectory, ...
- **p. 4 / 4. Our Method - extractive body cue:** Since EDI is defined in the monochrome brightness domain, we first model the EDI based on pixel intensity values.
- **Contribution anchor:** p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Our Method), p. 1 (1. Introduction), p. 5 (4. Our Method)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Earlier works [1, 11, 42] focus on utilizing solely event-based data, lacking the capacity to preserve color information.
- **p. 2 / 1. Introduction - extractive body cue:** However, most of these existing works still rely on blurry images alone to recover accurate color, often resulting in unwanted color artifacts.
- **p. 1 / 1. Introduction - extractive body cue:** Given a set of blurry images and corresponding event streams, we propose a novel framework to construct deblurring 3DGS by jointly leveraging the EDI [33] ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose DiET-GS, a Diffusion prior and EvenT stream-assisted motion deblurring 3DGS.
- **p. 3 / 3. Preliminaries - extractive body cue:** Given the predicted denoised latent ˆzt-1 from zt and the current noised latent zt-1 at timestep t -1, the ob21741
- **p. 6 / Dataset - extractive body cue:** Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get noised latents z′t and z′t-1.
- **p. 6 / Dataset - extractive body cue:** Finally, given ˆC as conditional input, the UNet backbone of pretrained diffusion model predicts the noise residual of z′t to derive the denoised latent ˆz′ ...
- **Boundary to test:** Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get noised latents z′t and z′t-1.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that our framework significantly surpasses the existing baselines, ... | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | Furthermore, our DiET-GS++ shows significant improvement in MUSIQ and CLIP-IQA metrics, achieving the best results but showing a slight drop in PSNR and SSIM metrics. | p. 7 (5.4. Quantitative Comparisons), p. 7 (5.4. Quantitative Comparisons) |
| Failure/limitation | Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get noised latents z′t and z′t-1. | p. 6 (Dataset), p. 6 (Dataset) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `conditioning observation와 noisy/intermediate sample → latent/noise variable와 conditional distribution → generated sample, action chunk 또는 trajectory`.
- 이 논문의 재사용 가능한 지점은 Based on the latent image I, a sharp latent image Ii at a randomly sampled timestep ti can be recovered by warping I to timestep ti as stated in the initialization step.를 However, unlike [20], our setting lacks the clean images which are necessary to guide noise prediction of diffusion model as conditional input.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 latent/noise variable와 conditional distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get noised latents z′t and z′t-1.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that our framework significantly surpasses the existing baselines, ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, Diffusion, Generation, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get noised latents z′t and z′t-1.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The EvDeblur-CDAVIS Dataset contains five real-world scenes, each with 11 to 18 blurry training images paired with corresponding event streams..
3. Compare against the body-reported baseline or a matched simpler baseline: Our DiETGS largely outperforms all baselines in PSNR, SSIM, and LPIPS on both synthetic and real-world datasets, showing the effectiveness of our framework to leverage EDI prior..
4. Report the body metric and its denominator/aggregation: Table 1. Quantitative comparisons on both synthetic and real-world dataset. The results are the average of every scenes within the dataset. The best results are in bold while the second best results ....
5. Re-run the body-reported ablation/failure condition: Ablation study on Ledi gray and Ledi color samples compared to DiET-GS which is supervised by realcaptured data..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method); the primary result is directionally consistent at p. 7 (5.4. Quantitative Comparisons), p. 7 (5.4. Quantitative Comparisons), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Once, optimized, capable mechanism이 Our DiETGS largely outperforms all baselines in PSNR, SSIM, and LPIPS on both synthetic and real-world ... 대비 Table 1. Quantitative comparisons on both synthetic and real-world dataset. The results are the average of every scenes ...을 개선하고, Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
