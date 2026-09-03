# Method - DiGA3D: Coarse-to-Fine Diffusional Propagation of Geometry and Appearance for Versatile 3D Inpainting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.4. Texture-Geometry Guided SDS Loss), p. 3 (3.1. Preliminary), p. 4 (3.3. Multi-view Consistent Image Inpainting), p. 3 (3.2. Problem formulation and overview), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 2 (3.1. Preliminary)): Therefore, we propose a texture-geometry guided SDS (TG-SDS) loss within the latent space of ControlNet [42].

## Method Body Digest

- **p. 4 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** Therefore, we propose a texture-geometry guided SDS (TG-SDS) loss within the latent space of ControlNet [42].
- **p. 3 / 3.1. Preliminary - extractive body cue:** In the coarse stage, we employ DDIM Inversion [33] to generate deterministic latents, which are then used to produce coarsely consistent inpainting results with a ...
- **p. 4 / 3.3. Multi-view Consistent Image Inpainting - extractive body cue:** To propagate the inpainted appearance from reference views, we first integrate a self-attention mechanism [40] to extract attention features from each view, as shown in ...
- **p. 3 / 3.2. Problem formulation and overview - extractive body cue:** In the coarse stage, we employ DDIM inversion and the Attention Feature Propagate (AFP) module, allowing attention features to propagate from reference views to other ...
- **p. 5 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** In this process, the rendered images Ii, along with the projected warped texture maps C′, warped depth maps D′, and mask m are input into ...
- **p. 2 / 3.1. Preliminary - extractive body cue:** Gaussian Splatting [13] is a pointbased 3D representation method.
- **p. 2 / 3.1. Preliminary - extractive body cue:** The covariance matrix Σ can be decomposed into a rotation matrix R and a scaling matrix S for differentiable optimization: Σ = RSST RT .
- **p. 5 / 3.5. Optimization - extractive body cue:** The 3D Gaussians G are optimized with all properties by minimizing the photometric loss and depth loss: \b e gi n {split} \m at h ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to consistently ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline with a coarseThis ICCV paper is the Open Access version, provided ...
- **p. 5 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** For each scene, we present two novel views to compare the rendering quality and multi-view consistency with the existing state-of-the-art methods. ter is conducted independently.

## Source Evidence Cues

- **p. 4 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** Therefore, we propose a texture-geometry guided SDS (TG-SDS) loss within the latent space of ControlNet [42].
- **p. 3 / 3.1. Preliminary - extractive body cue:** In the coarse stage, we employ DDIM Inversion [33] to generate deterministic latents, which are then used to produce coarsely consistent inpainting results with a ...
- **p. 4 / 3.3. Multi-view Consistent Image Inpainting - extractive body cue:** To propagate the inpainted appearance from reference views, we first integrate a self-attention mechanism [40] to extract attention features from each view, as shown in ...
- **p. 3 / 3.2. Problem formulation and overview - extractive body cue:** In the coarse stage, we employ DDIM inversion and the Attention Feature Propagate (AFP) module, allowing attention features to propagate from reference views to other ...
- **p. 5 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** In this process, the rendered images Ii, along with the projected warped texture maps C′, warped depth maps D′, and mask m are input into ...
- **p. 2 / 3.1. Preliminary - extractive body cue:** Gaussian Splatting [13] is a pointbased 3D representation method.
- **p. 2 / 3.1. Preliminary - extractive body cue:** The covariance matrix Σ can be decomposed into a rotation matrix R and a scaling matrix S for differentiable optimization: Σ = RSST RT .
- **Detected method headings:** 3. Method (p. 2); 4.2. Methods for Comparison (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Therefore, we propose a texture-geometry guided SDS (TG-SDS) loss within the latent space of ControlNet [42]. | p. 4 (3.4. Texture-Geometry Guided SDS Loss), p. 3 (3.1. Preliminary) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | In the coarse stage, we employ DDIM Inversion [33] to generate deterministic latents, which are then used to produce coarsely consistent inpainting ... | p. 3 (3.1. Preliminary), p. 4 (3.3. Multi-view Consistent Image Inpainting) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | To propagate the inpainted appearance from reference views, we first integrate a self-attention mechanism [40] to extract attention features from each view, ... | p. 4 (3.3. Multi-view Consistent Image Inpainting), p. 3 (3.2. Problem formulation and overview) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.5. Optimization - extractive body cue:** The 3D Gaussians G are optimized with all properties by minimizing the photometric loss and depth loss: \b e gi n {split} \m at h ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** By rendering a random view through a differentiable renderer g(·), SDS updates the parameter θ by randomly selecting timesteps t ∼U(tmin, tmax) and forwarding x ...
- **p. 4 / 3.2. Problem formulation and overview - extractive body cue:** In the fine stage, we leverage the TG-SDS loss as geometry regularization to improve both geometry and texture of the inpainted 3D scenes (see Sec.
- **p. 3 / 3.1. Preliminary - extractive body cue:** In the fine stage, we utilize ControlNet [42], leveraging texture and depth images as conditions, to further refine the inpainted 3D scene by TG-SDS loss.
- **p. 4 / 3.2. Problem formulation and overview - extractive body cue:** The overall loss functions are shown in Sec.
- **p. 5 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** It is important to note that we only backpropagate the gradient for the masked pixels.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.2. Problem formulation and overview), p. 4 (3.4. Texture-Geometry Guided SDS Loss), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 5 (3.4. Texture-Geometry Guided SDS Loss).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | outputs, AFP, inpainted, image, depth, estimated, monocular, estimator, texture-geometry, warping, texture, jective, inpaint, Gaussians | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | outputs, AFP, inpainted, image, depth, estimated, monocular, estimator, texture-geometry, warping | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | summary, contributions, outlined, follows, introduce, DiGA3D, versatile, inpainting, pipeline, leverages | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | Gaussians, optimized, properties, minimizing, photometric, loss, depth, split, lambda, mathcal | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. Problem formulation and overview - extractive body cue:** The outputs of AFP are the inpainted image Ii and the depth map Di estimated by the monocular depth estimator [30] ˜D.
- **p. 3 / 3.2. Problem formulation and overview - extractive body cue:** The outputs of texture-geometry warping are the texture map C′ i and the depth map D′ i. jective is to inpaint the 3D Gaussians based ...
- **p. 5 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** In this process, the rendered images Ii, along with the projected warped texture maps C′, warped depth maps D′, and mask m are input into ...
- **p. 2 / 1. Introduction - extractive body cue:** This involves using warped texture images and depth maps from reference views as conditional inputs for multi-control diffusion models [42].
- **p. 5 / 3.5. Optimization - extractive body cue:** In the coarse stage, we employ a pre-trained monocular depth estimator [30] ˜D to produce the depth map Di from the inpainted image Ii.
- **p. 4 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** We first employ the depth image-based rendering (DIBR) method [10] to warp images from the reference views to other views.
- **p. 2 / 3.1. Preliminary - extractive body cue:** The covariance matrix Σ can be decomposed into a rotation matrix R and a scaling matrix S for differentiable optimization: Σ = RSST RT .
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | The diffusion model ϕ is pre-trained to predict sampled noise ϵϕ(xt; t, y) that adds noise to the image x at timestep ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | By rendering a random view through a differentiable renderer g(·), SDS updates the parameter θ by randomly selecting timesteps t ∼U(tmin, tmax) ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | When using K-means for selecting reference views, it is important to balance memory cost and performance during the coarse stage. | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Our method is trained on a single NVIDIA 48GB A6000 GPU.
- **p. 4 / 3.3. Multi-view Consistent Image Inpainting - extractive body cue:** Next, we decode inpainted latents to produce coarsely consistent inpainted results for training the 3D Gaussians.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Therefore, texture-geometry, guided, SDS, TG-SDS, loss, within, latent, space, ControlNet, coarse, stage, employ, DDIM, Inversion, generate, deterministic, latents, then, produce.
- **Relevant PDF headings:** 3. Method (p. 2); 4.2. Methods for Comparison (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | We evaluate our versatile 3D inpainting methods in three different datasets with multi-view images from feed-forward and 360 degrees: 1) SPIn-NeRF dataset ... | p. 5 (4.1. Experimental Setup), p. 7 (4.3.1. Object Removal) |
| Denoiser / vector field | We compared our method with four baselines, i.e., SPIn-NeRF [25], NeRFiller [38], MVIP-NeRF [7], and GScream [37]. | p. 6 (4.1. Experimental Setup), p. 7 (4.3.1. Object Removal) |
| Sampling / downstream interface | Our method achieves clear improvements in PSNR and obtains better scores in most metrics. | p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study) |

## Failure and Ablation Link

- **p. 8 / 4.3.3. Object Replacement - extractive body cue:** The visualization of ablation study for key components on the object replacement task using LLFF dataset [22].
- **p. 8 / 4.4. Ablation Study - extractive body cue:** 8, we depict the visualizations of the ablation study on key components.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We evaluate our versatile 3D inpainting methods in three different datasets with multi-view images from feed-forward and 360 degrees: 1) SPIn-NeRF dataset [25] provide 10 ...
- **p. 7 / 4.3. Results - extractive body cue:** For each scene, we present two novel views to compare the rendering quality and multi-view consistency with the existing state-of-the-art methods. re-texturing, and object replacement, ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** 2) For object re-texturing and replacement tasks, we follow established practices by calculating the CLIP score and 16349
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Quantitative results of object re-texturing and replacement.
- **p. 6 / 4.2. Methods for Comparison - extractive body cue:** For object re-texturing and replacement, we evaluate our method against InstructNeRF2NeRF (IN2N) [12], GaussianEditor [8], and GaussCtrl [39].

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.4. Texture-Geometry Guided SDS Loss), p. 3 (3.1. Preliminary), p. 4 (3.3. Multi-view Consistent Image Inpainting), p. 3 (3.2. Problem formulation and overview), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 2 (3.1. Preliminary), objective p. 5 (3.5. Optimization), p. 3 (3.1. Preliminary), p. 4 (3.2. Problem formulation and overview), p. 3 (3.1. Preliminary), p. 4 (3.2. Problem formulation and overview), p. 5 (3.4. Texture-Geometry Guided SDS Loss), temporal p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.3. Multi-view Consistent Image Inpainting), p. 7 (4.3. Results), p. 8 (4.4. Ablation Study), p. 8 (4.3.3. Object Replacement).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
