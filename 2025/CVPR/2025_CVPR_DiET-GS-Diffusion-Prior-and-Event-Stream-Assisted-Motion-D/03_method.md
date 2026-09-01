# Method - DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method), p. 5 (4. Our Method)): To this end, we propose a novel optimization problem that leverages EDI prior to further constrain the 3DGS in terms of 1) fine-grained details, 2) precise color and 3) regularizing ...

## Method Body Digest

- **p. 4 / 4. Our Method - extractive PDF cue:** To this end, we propose a novel optimization problem that leverages EDI prior to further constrain the 3DGS in terms of 1) fine-grained details, 2) ...
- **p. 5 / 4. Our Method - extractive PDF cue:** Since the input of the diffusion model ˆCB is obtained by averaging a set of rendered sharp images { ˆC}n-1 i=0 along the camera trajectory, ...
- **p. 4 / 4. Our Method - extractive PDF cue:** Since EDI is defined in the monochrome brightness domain, we first model the EDI based on pixel intensity values.
- **p. 5 / 4. Our Method - extractive PDF cue:** Given the predicted noise and zt, we then obtain the predicted denoised latent ˆzt-1 via the DDPM reverse process.
- **p. 5 / 4. Our Method - extractive PDF cue:** Jointly optimizing these two constraints reaches an equilibrium between scene-specific details guided by the event-based loss and the prior knowledge of the pretrained diffusion model.
- **p. 4 / 4. Our Method - extractive PDF cue:** Following the original 3DGS, we thus formulate a blur reconstruction loss to minimize the photometric error LP as Lblur = Lp(CB, ˆCB) = (1 -λ1)L1 ...
- **p. 5 / 4. Our Method - extractive PDF cue:** Finally, the EDI loss is given by combining all of the EDI-based objectives as: Ledi = Ledi gray + Ledi color + Ledi simul.
- **p. 4 / 4. Our Method - extractive PDF cue:** Event Double Integration (EDI) Loss.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Given a set of blurry images and corresponding event streams, we propose a novel framework to construct deblurring 3DGS by jointly leveraging the EDI [33] ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To restore both accurate color and well-defined details, we introduce a novel framework that uses the EDI prior to achieve 1) fine-grained details, 2) accurate ...

## Source Evidence Cues

- **p. 4 / 4. Our Method - extractive PDF cue:** To this end, we propose a novel optimization problem that leverages EDI prior to further constrain the 3DGS in terms of 1) fine-grained details, 2) ...
- **p. 5 / 4. Our Method - extractive PDF cue:** Since the input of the diffusion model ˆCB is obtained by averaging a set of rendered sharp images { ˆC}n-1 i=0 along the camera trajectory, ...
- **p. 4 / 4. Our Method - extractive PDF cue:** Since EDI is defined in the monochrome brightness domain, we first model the EDI based on pixel intensity values.
- **p. 5 / 4. Our Method - extractive PDF cue:** Given the predicted noise and zt, we then obtain the predicted denoised latent ˆzt-1 via the DDPM reverse process.
- **Detected method headings:** 4. Our Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | To this end, we propose a novel optimization problem that leverages EDI prior to further constrain the 3DGS in terms of 1) ... | p. 4 (4. Our Method), p. 5 (4. Our Method) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Since the input of the diffusion model ˆCB is obtained by averaging a set of rendered sharp images { ˆC}n-1 i=0 along ... | p. 5 (4. Our Method), p. 4 (4. Our Method) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | Since EDI is defined in the monochrome brightness domain, we first model the EDI based on pixel intensity values. | p. 4 (4. Our Method), p. 5 (4. Our Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4. Our Method - extractive PDF cue:** Jointly optimizing these two constraints reaches an equilibrium between scene-specific details guided by the event-based loss and the prior knowledge of the pretrained diffusion model.
- **p. 4 / 4. Our Method - extractive PDF cue:** Following the original 3DGS, we thus formulate a blur reconstruction loss to minimize the photometric error LP as Lblur = Lp(CB, ˆCB) = (1 -λ1)L1 ...
- **p. 5 / 4. Our Method - extractive PDF cue:** Finally, the EDI loss is given by combining all of the EDI-based objectives as: Ledi = Ledi gray + Ledi color + Ledi simul.
- **p. 4 / 4. Our Method - extractive PDF cue:** Event Double Integration (EDI) Loss.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method), p. 4 (4. Our Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | latent, image, sharp, randomly, sampled, timestep, recovered, warping, stated, initialization, step, However, unlike, setting | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | latent, image, sharp, randomly, sampled, timestep, recovered, warping, stated, initialization | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | Once, optimized, capable, recovering, well-defined, details, accurate, color, input, blurry | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | Jointly, optimizing, constraints, reaches, equilibrium, between, scene-specific, details, guided, event-based | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4. Our Method - extractive PDF cue:** Based on the latent image I, a sharp latent image Ii at a randomly sampled timestep ti can be recovered by warping I to timestep ...
- **p. 5 / 4. Our Method - extractive PDF cue:** However, unlike [20], our setting lacks the clean images which are necessary to guide noise prediction of diffusion model as conditional input.
- **p. 5 / 4. Our Method - extractive PDF cue:** The UNet backbone [41] of the pretrained diffusion model takes zt as input and the ground truth blurry image CB as a condition to predict ...
- **p. 4 / 4. Our Method - extractive PDF cue:** The recovered sharp latent images are subsequently fed into SfM for the estimation of the camera poses and point cloud.
- **p. 2 / 1. Introduction - extractive PDF cue:** Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that ...
- **p. 3 / 3. Preliminaries - extractive PDF cue:** In the DDPM reverse process, a diffusion U-net is trained to predict the noise ϵ(z, y, t) to denoise zt into zt-1 as follows: zt-1 ...
- **p. 3 / 3. Preliminaries - extractive PDF cue:** We propose a novel framework to leverage the EDI prior to constrain 3D Gaussian Splatting in recovering sharp rendered images with better fine-grained details and ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Given Ii as image-level supervision, we synthesize the brightness of color image ˆCi rendered at the same timestep. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | This sharp image I can then be warped to any timestep within the exposure period [t -τ/2, t + τ/2] following I(t ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | All experiments are conducted using a single NVIDIA RTX 6000 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4. Our Method - extractive PDF cue:** To this end, we propose a novel optimization problem that leverages EDI prior to further constrain the 3DGS in terms of 1) fine-grained details, 2) ...
- **p. 4 / 4. Our Method - extractive PDF cue:** We obtain a set of latent images for each training view by warping the recovered latent image I to each of the n timesteps uniformly ...
- **p. 5 / 4. Our Method - extractive PDF cue:** 3, and encode it to a latent z0 = E( ˆCB) via a pretrained VAE encoder E.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** novel, optimization, problem, leverages, EDI, prior, further, constrain, DGS, terms, fine-grained, details, precise, color, regularizing, Since, input, diffusion, model, obtained.
- **Relevant PDF headings:** 4. Our Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | The EvDeblur-CDAVIS Dataset contains five real-world scenes, each with 11 to 18 blurry training images paired with corresponding event streams. | p. 6 (5.2. Datasets), p. 6 (5.2. Datasets) |
| Denoiser / vector field | Our DiETGS largely outperforms all baselines in PSNR, SSIM, and LPIPS on both synthetic and real-world datasets, showing the effectiveness of our ... | p. 7 (5.4. Quantitative Comparisons), p. 7 (5.3. Experiment Settings) |
| Sampling / downstream interface | Furthermore, our DiET-GS++ shows significant improvement in MUSIQ and CLIP-IQA metrics, achieving the best results but showing a slight drop in PSNR ... | p. 7 (5.4. Quantitative Comparisons), p. 7 (5.4. Quantitative Comparisons) |

## Failure and Ablation Link

- **p. 7 / 5.4. Quantitative Comparisons - extractive PDF cue:** Ablation study on Ledi gray and Ledi color samples compared to DiET-GS which is supervised by realcaptured data.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overall framework of our DiET-GS. Stage 1 (DiET-GS) optimizes the deblurring 3DGS with the event streams and diffusion prior. To preserve accurate color ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study on DiET-GS and DiET-GS++ 3DGS. 2) We find that our DiET-GS is capable of restor- ing cleaner textures and clearer edges ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Ablation on Ledi simul (1st row) and Lrsd (S1) (2nd row). adding EDI simulation Ledi simul further aids fine-grained deblurring as shown in ...
- **p. 7 / 5.4. Quantitative Comparisons - extractive PDF cue:** As already discussed in [20, 62], since DiET-GS++ is solely guided by a pretrained generative model, the resulting images may contain more variation with respect ...
- **p. 6 / Dataset - extractive PDF cue:** Specifically, ˜C = D(z′ 0) = D(f2D +E( ˆC)), where D is pretrained VAE decoder (cf.
- **p. 6 / Dataset - extractive PDF cue:** After optimization, our model can render latent residual f2D which contains rich edge details directly guided by the pretrained diffusion model.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method), p. 5 (4. Our Method), objective p. 5 (4. Our Method), p. 4 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method), temporal p. 4 (4. Our Method), p. 4 (4. Our Method), p. 5 (4. Our Method), p. 5 (4. Our Method), p. 3 (3. Preliminaries), p. 6 (5.1. Implementation Details).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
