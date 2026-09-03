# Method - ReconFusion: 3D Reconstruction with Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Diffusion Model for Novel View Synthesis), p. 4 (3.1. Diffusion Model for Novel View Synthesis), p. 5 (3.3. Implementation Details), p. 3 (3.1. Diffusion Model for Novel View Synthesis), p. 4 (3.1. Diffusion Model for Novel View Synthesis), p. 5 (3.3. Implementation Details)): For relative camera pose and geometric information, we use a PixelNeRF [67] model Rϕ to render a feature map f with the same spatial resolution as the latents from the ...

## Method Body Digest

- **p. 3 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** For relative camera pose and geometric information, we use a PixelNeRF [67] model Rϕ to render a feature map f with the same spatial resolution ...
- **p. 4 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** Training We freeze the weights of the pretrained encoder and decoder, initialize the U-Net parameters θ from pretrained weights, and optimize the modified architecture for ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** The encoder of our PixelNeRF is a small U-Net that takes as input an image of resolution 512×512 and outputs a feature map of resolution ...
- **p. 3 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** For high-level semantic information about the inputs, we use the CLIP [38] embedding of each input image (denoted eobs) and feed this sequence of feature ...
- **p. 4 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** 2, we optimize the PixelNeRF parameters ϕ with a photometric loss: LPixelNeRF(ϕ) = Exobs,πobs,x,π∥c -x↓∥2 , (3) where c is an output of the PixelNeRF ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Our base diffusion model is a re-implementation of the Latent Diffusion Model [43] that has been trained on an internal dataset of image-text pairs with ...
- **p. 4 / 3.2. 3D Reconstruction with Diffusion Priors - extractive body cue:** The NeRF parameters ψ are optimized by minimizing the reconstruction error between a rendered image x = x(ψ, πobs) and an observed image xobs at ...
- **p. 4 / 3.2. 3D Reconstruction with Diffusion Priors - extractive body cue:** Reconstruction loss NeRF-based methods optimize a randomly initialized 3D model to match a set of posed images.

## Design Rationale

- **p. 5 / 3.3. Implementation Details - extractive body cue:** This enables our models to scale to large numbers of input images while selecting inputs that are most useful for the sampled novel view.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach outperforms existing baselines on several datasets of both forward-facing and unbounded 360◦ scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we show that our diffusion prior is an effective drop-in regularizer for NeRFs across a range of capture settings.

## Source Evidence Cues

- **p. 3 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** For relative camera pose and geometric information, we use a PixelNeRF [67] model Rϕ to render a feature map f with the same spatial resolution ...
- **p. 4 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** Training We freeze the weights of the pretrained encoder and decoder, initialize the U-Net parameters θ from pretrained weights, and optimize the modified architecture for ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** The encoder of our PixelNeRF is a small U-Net that takes as input an image of resolution 512×512 and outputs a feature map of resolution ...
- **p. 3 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** For high-level semantic information about the inputs, we use the CLIP [38] embedding of each input image (denoted eobs) and feed this sequence of feature ...
- **p. 4 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** 2, we optimize the PixelNeRF parameters ϕ with a photometric loss: LPixelNeRF(ϕ) = Exobs,πobs,x,π∥c -x↓∥2 , (3) where c is an output of the PixelNeRF ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Our base diffusion model is a re-implementation of the Latent Diffusion Model [43] that has been trained on an internal dataset of image-text pairs with ...
- **Detected method headings:** 3.1. Diffusion Model for Novel View Synthesis (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | For relative camera pose and geometric information, we use a PixelNeRF [67] model Rϕ to render a feature map f with the ... | p. 3 (3.1. Diffusion Model for Novel View Synthesis), p. 4 (3.1. Diffusion Model for Novel View Synthesis) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Training We freeze the weights of the pretrained encoder and decoder, initialize the U-Net parameters θ from pretrained weights, and optimize the ... | p. 4 (3.1. Diffusion Model for Novel View Synthesis), p. 5 (3.3. Implementation Details) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | The encoder of our PixelNeRF is a small U-Net that takes as input an image of resolution 512×512 and outputs a feature ... | p. 5 (3.3. Implementation Details), p. 3 (3.1. Diffusion Model for Novel View Synthesis) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. 3D Reconstruction with Diffusion Priors - extractive body cue:** The NeRF parameters ψ are optimized by minimizing the reconstruction error between a rendered image x = x(ψ, πobs) and an observed image xobs at ...
- **p. 4 / 3.2. 3D Reconstruction with Diffusion Priors - extractive body cue:** Reconstruction loss NeRF-based methods optimize a randomly initialized 3D model to match a set of posed images.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** The reconstruction term Lrecon uses the Charbonnier loss [7] as in Zip-NeRF.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** To enable classifier-free guidance (CFG), we set the input images to all zeros randomly with probability 10%.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 4 (3.2. 3D Reconstruction with Diffusion Priors), p. 4 (3.2. 3D Reconstruction with Diffusion Priors), p. 5 (3.3. Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | encoder, PixelNeRF, small, U-Net, takes, input, image, resolution, outputs, feature, channels, supplement, more, details | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | encoder, PixelNeRF, small, U-Net, takes, input, image, resolution, outputs, feature | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | enables, models, scale, large, numbers, input, images, while, selecting, inputs | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | NeRF, parameters, optimized, minimizing, reconstruction, error, between, rendered, image, observed | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.3. Implementation Details - extractive body cue:** The encoder of our PixelNeRF is a small U-Net that takes as input an image of resolution 512×512 and outputs a feature map of resolution ...
- **p. 4 / 3.2. 3D Reconstruction with Diffusion Priors - extractive body cue:** To enable 3D reconstruction from a smaller number of posed inputs, we augment the state-of-the-art 3D reconstruction pipeline from Zip-NeRF [2] with a prior from ...
- **p. 1 / 1. Introduction - extractive body cue:** Methods like NeRF [32] optimize a 3D representation whose renderings match observed input images at given camera poses.
- **p. 2 / 1. Introduction - extractive body cue:** As posed multiview data is limited (compared to massive single image datasets), we finetune our diffusion model from a pretrained latent diffusion model [43] on ...
- **p. 3 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** Conditioning Similar to Zero-1-to-3 [29], we start from an LDM trained for text-to-image generation, and additionally condition on input images and poses.
- **p. 4 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** 2 , (2) where t ∈{1, . . . , T} is the diffusion timestep, ϵ ∼ N(0, I), zt = αtE(x) + σtϵ is ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** In practice, diffusion models for view synthesis can be conditioned on a small number of observed input images and poses.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Regardless of t, we always sample the denoised image with k = 10 steps. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | We fix tmax = 1.0 for all training steps, and linearly anneal tmin from 1.0 to 0.0. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | Regardless of t, we always sample the denoised image with k = 10 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** Training We freeze the weights of the pretrained encoder and decoder, initialize the U-Net parameters θ from pretrained weights, and optimize the modified architecture for ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Our base diffusion model is a re-implementation of the Latent Diffusion Model [43] that has been trained on an internal dataset of image-text pairs with ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** We jointly train the PixelNeRF and finetune the denoising U-Net with batch size 256 and learning rate 10-4 for a total of 250k iterations.
- **p. 3 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** LDMs encode input images to a latent representation using a pretrained variational auto-encoder (VAE) E.
- **p. 4 / 3.2. 3D Reconstruction with Diffusion Priors - extractive body cue:** The trained diffusion model produces plausible single images for novel camera poses, but generated images are often inconsistent for different poses or random seeds.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** relative, camera, pose, geometric, information, PixelNeRF, model, render, feature, same, spatial, resolution, latents, target, viewpoint, xobs, Training, freeze, weights, pretrained.
- **Relevant PDF headings:** 3.1. Diffusion Model for Novel View Synthesis (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | For the mip-NeRF 360 dataset, we retain its original test set and select the input views from the training set using a ... | p. 5 (4.1. Experiment Setup), p. 5 (4.1. Experiment Setup) |
| Denoiser / vector field | Our method outperforms all baselines on both in-distribution and out-of-distribution datasets, achieving state-of-the-art performance for few-view NeRF reconstructions. | p. 7 (4.2. Comparison Results), p. 5 (4.1. Experiment Setup) |
| Sampling / downstream interface | Table 1. Quantitative evaluation of few-view 3D reconstruction methods. Datasets are ordered in terms of sparsity from easier (novel views are close ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Ablation of diffusion model on 3-view reconstruc- tion. We show two samples from the diffusion model, and ren- derings from the reconstructed NeRFs ...
- **p. 5 / 4. Experiments - extractive body cue:** We also perform several ablations on the components of the diffusion model and the 3D reconstruction procedure (Sec.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** Both variants produce sampled images of lower quality, which subsequently degrades the NeRF reconstruction.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** 4, we ablate two aspects of our diffusion model: the use of pretrained diffusion model weights (PT) and conditioning signal.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** For PT, we initialize the diffusion model weights from a pretrained text-to-image model. pose uses a pose conditioning similar to ZeroNVS [45] while pixelnerf uses ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Methods for reconstructing a 3D scene from images, such as Neural Radiance Fields (NeRF), often exhibit artifacts when trained with few input views. ...
- **p. 8 / 5. Discussion - extractive body cue:** Many current limitations are evident: the heavyweight diffusion model is costly and slows down reconstruction significantly; our current results demonstrate only limited 3D outpainting abilities ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Diffusion Model for Novel View Synthesis), p. 4 (3.1. Diffusion Model for Novel View Synthesis), p. 5 (3.3. Implementation Details), p. 3 (3.1. Diffusion Model for Novel View Synthesis), p. 4 (3.1. Diffusion Model for Novel View Synthesis), p. 5 (3.3. Implementation Details), objective p. 4 (3.2. 3D Reconstruction with Diffusion Priors), p. 4 (3.2. 3D Reconstruction with Diffusion Priors), p. 5 (3.3. Implementation Details), p. 5 (3.3. Implementation Details), temporal p. 5 (3.3. Implementation Details), p. 5 (3.3. Implementation Details), p. 7 (4.3. Ablation Studies), p. 8 (4.4. Scaling to More Views), p. 4 (3.1. Diffusion Model for Novel View Synthesis), p. 2 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
