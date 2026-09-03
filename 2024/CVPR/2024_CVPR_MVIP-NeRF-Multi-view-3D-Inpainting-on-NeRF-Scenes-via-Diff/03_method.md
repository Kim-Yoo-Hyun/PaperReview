# Method - MVIP-NeRF: Multi-view 3D Inpainting on NeRF Scenes via Diffusion Prior

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_MVIP-NeRF_Multi-view_3D_Inpainting_on_NeRF_Scenes_via_Diffusion_Prior_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_MVIP-NeRF_Multi-view_3D_Inpainting_on_NeRF_Scenes_via_Diffusion_Prior_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Problem formulation and overview), p. 4 (3.3. Appearance Diffusion Prior), p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 5 (3.4. Geometry Diffusion Prior), p. 5 (3.5. Multi-view Score Distillation)): Then, a latent diffusion model is employed as the appearance and geometry prior.

## Method Body Digest

- **p. 4 / 3.2. Problem formulation and overview - extractive body cue:** Then, a latent diffusion model is employed as the appearance and geometry prior.
- **p. 4 / 3.3. Appearance Diffusion Prior - extractive body cue:** In this work, we use the stablediffusion-inpainting model [21] as our guidance model.
- **p. 3 / 3.1. Preliminary - extractive body cue:** Formally, let x = g(θ) represent an image rendered by a differentiable generator g with parameter θ, then SDS minimizes density distillation loss [18] which ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Therefore, the NeRF reconstruction loss can be formulated as La =  r∈R // ˆC(r) -C(r)//2, (1) where ˆC(r) represents the rendered color blended from ...
- **p. 5 / 3.4. Geometry Diffusion Prior - extractive body cue:** To update θ, we again employ the SDS loss that computes the gradient w.r.t. θ as: ∇θLg masked = w(t)  ϵω φ(zt; m, y, ...
- **p. 5 / 3.5. Multi-view Score Distillation - extractive body cue:** Intuitively, this function implies that when updating θ, we take into account the interactions with other sampled views, thereby promoting view consistency.
- **p. 6 / 3.5. Multi-view Score Distillation - extractive body cue:** its multi-view version, and jointly train the loss as: L = La unmasked + λ1Lg unmasked + λ2Lma masked + λ3Lg masked.
- **p. 4 / 3.2. Problem formulation and overview - extractive body cue:** Rather than directly utilizing inconsistent 2D inpainting results as supervisions and resolving these inconsistencies post hoc, we employ two SDS losses to compute a gradient ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we present MVIP-NeRF, a novel approach that performs multiview-consistent inpainting in NeRF scenes via diffusion priors.
- **p. 2 / 1. Introduction - extractive body cue:** (iv) Extensive experiments to show the effectiveness of our method over existing NeRF inpainting techniques.
- **p. 4 / 3.2. Problem formulation and overview - extractive body cue:** To further enhance consistency for large-view motion, we introduce a multi-view score function.

## Source Evidence Cues

- **p. 4 / 3.2. Problem formulation and overview - extractive body cue:** Then, a latent diffusion model is employed as the appearance and geometry prior.
- **p. 4 / 3.3. Appearance Diffusion Prior - extractive body cue:** In this work, we use the stablediffusion-inpainting model [21] as our guidance model.
- **p. 3 / 3.1. Preliminary - extractive body cue:** Formally, let x = g(θ) represent an image rendered by a differentiable generator g with parameter θ, then SDS minimizes density distillation loss [18] which ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Therefore, the NeRF reconstruction loss can be formulated as La =  r∈R // ˆC(r) -C(r)//2, (1) where ˆC(r) represents the rendered color blended from ...
- **p. 5 / 3.4. Geometry Diffusion Prior - extractive body cue:** To update θ, we again employ the SDS loss that computes the gradient w.r.t. θ as: ∇θLg masked = w(t)  ϵω φ(zt; m, y, ...
- **p. 5 / 3.5. Multi-view Score Distillation - extractive body cue:** Intuitively, this function implies that when updating θ, we take into account the interactions with other sampled views, thereby promoting view consistency.
- **p. 6 / 3.5. Multi-view Score Distillation - extractive body cue:** its multi-view version, and jointly train the loss as: L = La unmasked + λ1Lg unmasked + λ2Lma masked + λ3Lg masked.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Then, a latent diffusion model is employed as the appearance and geometry prior. | p. 4 (3.2. Problem formulation and overview), p. 4 (3.3. Appearance Diffusion Prior) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | In this work, we use the stablediffusion-inpainting model [21] as our guidance model. | p. 4 (3.3. Appearance Diffusion Prior), p. 3 (3.1. Preliminary) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | Formally, let x = g(θ) represent an image rendered by a differentiable generator g with parameter θ, then SDS minimizes density distillation ... | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Geometry Diffusion Prior - extractive body cue:** To update θ, we again employ the SDS loss that computes the gradient w.r.t. θ as: ∇θLg masked = w(t)  ϵω φ(zt; m, y, ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Formally, let x = g(θ) represent an image rendered by a differentiable generator g with parameter θ, then SDS minimizes density distillation loss [18] which ...
- **p. 4 / 3.2. Problem formulation and overview - extractive body cue:** Rather than directly utilizing inconsistent 2D inpainting results as supervisions and resolving these inconsistencies post hoc, we employ two SDS losses to compute a gradient ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** For an efficient implementation, SDS updates the parameter θ by randomly choosing timesteps t ∼U(tmin, tmax) and forward x = g(θ) with noise ϵ ∼N(0, ...
- **p. 4 / 3.2. Problem formulation and overview - extractive body cue:** In the optimization process, for unmasked regions, we employ direct pixel-wise RGB and depth reconstruction losses.
- **p. 5 / 3.4. Geometry Diffusion Prior - extractive body cue:** The second column displays the normal map derived from the density field gradient and the corresponding optimized depth map.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (3.4. Geometry Diffusion Prior), p. 4 (3.2. Problem formulation and overview), p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.3. Appearance Diffusion Prior), p. 5 (3.4. Geometry Diffusion Prior).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Input, views, masks, camera, poses, Shared, diffusion, prior, Multi-view, appearance, SDS, Geometry, Text, prompt | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Input, views, masks, camera, poses, Shared, diffusion, prior, Multi-view, appearance | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | present, MVIP-NeRF, novel, performs, multiview-consistent, inpainting, NeRF, scenes, diffusion, priors | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | update, again, employ, SDS, loss, computes, gradient, masked, Formally, represent | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Problem formulation and overview - extractive body cue:** Input views, masks, and camera poses Shared diffusion priorࣦ ௨௡௠௔௦௞௘ௗ ௔ Multi-view appearance SDS ࣦ ௠௔௦௞௘ௗ ௔ Geometry SDS ࣦ ௠௔௦௞௘ௗ ௚ࣦ ௨௡௠௔௦௞௘ௗ ௚ ࠁ ...
- **p. 5 / 3.4. Geometry Diffusion Prior - extractive body cue:** In the first column, we present the input image with a mask (black region) and the depth map generated by NeRF, optimized with unmasked pixels.
- **p. 4 / 3.4. Geometry Diffusion Prior - extractive body cue:** In our work, we have two observations: (i) text-to-image diffusion models have a strong shape prior due to their training on diverse objects, and (ii) ...
- **p. 3 / 3.2. Problem formulation and overview - extractive body cue:** Given a set of RGB images, I = {Ii}n i=1, with corresponding 3D poses G = {Gi}n i=1, 2D masks M = {mi}n i=1, and ...
- **p. 5 / 3.4. Geometry Diffusion Prior - extractive body cue:** In particular, we search the K view 38 view 18 Inputs view 48 w/o multi-view w/ multi-view Figure 4.
- **p. 2 / 1. Introduction - extractive body cue:** Besides, they share the common limitation of neglecting the correlation between inpainted RGB images and inpainted depth maps, resulting in less pleasing geometry completion.
- **p. 2 / 1. Introduction - extractive body cue:** We summarize our contributions as follows: (i) A diffusion prior guided approach for high-quality NeRF inpainting, achieved without the need for explicit supervision of inpainted ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | For an efficient implementation, SDS updates the parameter θ by randomly choosing timesteps t ∼U(tmin, tmax) and forward x = g(θ) with ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | The range of timesteps tmin and tmax are chosen to sample from not too small or large noise levels and the text ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Preliminary - extractive body cue:** Therefore, the NeRF reconstruction loss can be formulated as La =  r∈R // ˆC(r) -C(r)//2, (1) where ˆC(r) represents the rendered color blended from ...
- **p. 6 / 3.5. Multi-view Score Distillation - extractive body cue:** its multi-view version, and jointly train the loss as: L = La unmasked + λ1Lg unmasked + λ2Lma masked + λ3Lg masked.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We implemented our NeRF inpainting model built upon SPIn-NeRF [17] and trained it on 4 NVIDIA V100 GPUs for 10, 000 iterations using the Adam ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** In addition, we implement an annealing timestep scheduling strategy [39], which allocates more training steps to lower values of t.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, latent, diffusion, model, employed, appearance, geometry, prior, stablediffusion-inpainting, guidance, Formally, represent, image, rendered, differentiable, generator, parameter, SDS, minimizes, density.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | This dataset comprises all 10 real-world scenes with slight viewpoint variations from [17]. | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Denoiser / vector field | Table 1. Comparison with state-of-the-art methods on two real-world datasets. Our method is best compared to other novel-view synthesis baselines in inpainting ... | p. 7 (Figure/Table caption), p. 6 (4.2. Results) |
| Sampling / downstream interface | Figure 3. Effect of different normal map generation methods. In the first column, we present the input image with a mask (black ... | p. 5 (Figure/Table caption), p. 7 (4.2. Results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation analysis. Our method is best compared to different variants of our method in inpainting the missing regions of the scene. Columns show ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method overview. Given posed RGB images with corresponding masks, depth maps (optional), and a text description, MVIP- NeRF can faithfully recover plausible textures ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Effect of multi-view score distillation. The first row shows inpainting results without the multi-view score, while the second row shows the results with ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Additionally, 40 test images without the object are provided for quantitative evaluations.
- **p. 6 / 4.2. Results - extractive body cue:** In total, we compare two NeRF inpainting approaches: SPIn-NeRF [17] with LaMa [27], and Remove-NeRF [35] with LaMa [27].
- **p. 7 / 4.2. Results - extractive body cue:** Remove-NeRF SPIn-NeRF Input views GT (two novel views) Ours Masks Remove-NeRF SPIn-NeRF Input views GT (two novel views) Ours Masks Figure 5.
- **p. 7 / 4.2. Results - extractive body cue:** Columns show the deviation from known ground-truth RGB images or depth maps of the scene (without the target object), based on the peak signal-to-noise ratio ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Problem formulation and overview), p. 4 (3.3. Appearance Diffusion Prior), p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 5 (3.4. Geometry Diffusion Prior), p. 5 (3.5. Multi-view Score Distillation), objective p. 5 (3.4. Geometry Diffusion Prior), p. 3 (3.1. Preliminary), p. 4 (3.2. Problem formulation and overview), p. 3 (3.1. Preliminary), p. 4 (3.2. Problem formulation and overview), p. 5 (3.4. Geometry Diffusion Prior), temporal p. 3 (3.1. Preliminary), p. 4 (3.3. Appearance Diffusion Prior), p. 6 (4.1. Experimental Setup), p. 2 (1. Introduction), p. 6 (4.1. Experimental Setup), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
