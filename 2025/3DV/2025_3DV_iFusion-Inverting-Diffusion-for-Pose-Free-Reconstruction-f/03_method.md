# Method - iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=W7vOFBCGPm&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Diffusion as a Pose Estimator), p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 4 (3.1. Diffusion as a Pose Estimator), p. 3 (3.1. Diffusion as a Pose Estimator), p. 3 (3. Method), p. 5 (3.3. From Sparse Views to 3D Reconstruction)): (a) Pose Optimization + noise Pre-trained Diffusion Reconstruction Loss (b) Sparse-view Fine-tuning + noise Pre-trained Diffusion LoRA Reconstruction Loss (c) 3D Reconstruction Reconstruction Module Pre-trained Diffusion LoRA back propa ...

## Method Body Digest

- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (a) Pose Optimization + noise Pre-trained Diffusion Reconstruction Loss (b) Sparse-view Fine-tuning + noise Pre-trained Diffusion LoRA Reconstruction Loss (c) 3D Reconstruction Reconstruction Module Pre-trained ...
- **p. 5 / 3.3. From Sparse Views to 3D Reconstruction - extractive body cue:** 3.2, and then feed them as the training data to the differentiable renderer, e.g., NeRF [38] and NeuS [69].
- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (c) Conditioned on ˆTr→q and the refined diffusion model, we optimize a reconstruction module to perform sparse view 3D reconstruction.
- **p. 3 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (4), we query a view in its latent space zt ∼E(xq) using Eq.
- **p. 3 / 3. Method - extractive body cue:** By inverting the diffusion model, accurate poses can be estimated.
- **p. 5 / 3.3. From Sparse Views to 3D Reconstruction - extractive body cue:** The final objective is the weighted sum of Lrec and LSDS.
- **p. 2 / 2. A self-training and test-time training inspired fine-tuning - extractive body cue:** This stage results in a much stronger novel view synthesis diffusion model, which plays a crucial role in guiding the reconstruction process.
- **p. 3 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** To ensure that the estimated pose ˆTr→q continue to lie on the SE(3) manifold during the gradientbased optimization, we parameterize the pose Tr→q = exp(ξ), ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce iFusion, a novel framework that reconstructs diverse 3D objects with sparse, pose-free views.
- **p. 2 / 1. Introduction - extractive body cue:** We propose a novel camera pose estimator that significantly outperforms existing methods in terms of both accuracy and required number of input views, while being ...
- **p. 4 / 3.2. From Single-View to Multi-View - extractive body cue:** We propose to close the gap by further fine-tuning the DM with the given views and estimated poses.

## Source Evidence Cues

- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (a) Pose Optimization + noise Pre-trained Diffusion Reconstruction Loss (b) Sparse-view Fine-tuning + noise Pre-trained Diffusion LoRA Reconstruction Loss (c) 3D Reconstruction Reconstruction Module Pre-trained ...
- **p. 5 / 3.3. From Sparse Views to 3D Reconstruction - extractive body cue:** 3.2, and then feed them as the training data to the differentiable renderer, e.g., NeRF [38] and NeuS [69].
- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (c) Conditioned on ˆTr→q and the refined diffusion model, we optimize a reconstruction module to perform sparse view 3D reconstruction.
- **p. 3 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (4), we query a view in its latent space zt ∼E(xq) using Eq.
- **p. 3 / 3. Method - extractive body cue:** By inverting the diffusion model, accurate poses can be estimated.
- **p. 5 / 3.3. From Sparse Views to 3D Reconstruction - extractive body cue:** The final objective is the weighted sum of Lrec and LSDS.
- **p. 2 / 2. A self-training and test-time training inspired fine-tuning - extractive body cue:** This stage results in a much stronger novel view synthesis diffusion model, which plays a crucial role in guiding the reconstruction process.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | (a) Pose Optimization + noise Pre-trained Diffusion Reconstruction Loss (b) Sparse-view Fine-tuning + noise Pre-trained Diffusion LoRA Reconstruction Loss (c) 3D Reconstruction ... | p. 4 (3.1. Diffusion as a Pose Estimator), p. 5 (3.3. From Sparse Views to 3D Reconstruction) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | 3.2, and then feed them as the training data to the differentiable renderer, e.g., NeRF [38] and NeuS [69]. | p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 4 (3.1. Diffusion as a Pose Estimator) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | (c) Conditioned on ˆTr→q and the refined diffusion model, we optimize a reconstruction module to perform sparse view 3D reconstruction. | p. 4 (3.1. Diffusion as a Pose Estimator), p. 3 (3.1. Diffusion as a Pose Estimator) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** To ensure that the estimated pose ˆTr→q continue to lie on the SE(3) manifold during the gradientbased optimization, we parameterize the pose Tr→q = exp(ξ), ...
- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (a) Pose Optimization + noise Pre-trained Diffusion Reconstruction Loss (b) Sparse-view Fine-tuning + noise Pre-trained Diffusion LoRA Reconstruction Loss (c) 3D Reconstruction Reconstruction Module Pre-trained ...
- **p. 3 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** Finally, we compute the residuals for backpropagation of the transformation's gradient ∇ˆTr→q.
- **p. 5 / 3.3. From Sparse Views to 3D Reconstruction - extractive body cue:** The final objective is the weighted sum of Lrec and LSDS.
- **p. 5 / 3.3. From Sparse Views to 3D Reconstruction - extractive body cue:** (3), we further incorporate the reconstruction loss on the registered input views: Lrec =
- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** This adjustment aligns with diffusion models' coarse-to-fine progressive optimization and has been empirically observed to lead to more stable optimization.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (3.1. Diffusion as a Pose Estimator), p. 3 (3.1. Diffusion as a Pose Estimator), p. 4 (3.1. Diffusion as a Pose Estimator), p. 4 (3.1. Diffusion as a Pose Estimator), p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 5 (3.3. From Sparse Views to 3D Reconstruction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, pose-free, images, estimate, pose, optimally, reconstruct, input, view, through, frozen, diffusion, model, More | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Given, pose-free, images, estimate, pose, optimally, reconstruct, input, view, through | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | introduce, iFusion, novel, framework, reconstructs, diverse, objects, sparse, pose-free, views | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | ensure, estimated, pose, continue, manifold, during, gradientbased, optimization, parameterize, where | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (a) Given as few as two pose-free images (xr, xq), we estimate the pose ˆTr→q from T0 to optimally reconstruct the input view through the ...
- **p. 2 / 1. Introduction - extractive body cue:** More specifically, we adopt an analysisby-synthesis paradigm [7, 45, 78] that optimizes the transformation by minimizing the difference between the denoised latent visual features, i.e., ...
- **p. 3 / 2. Preliminary - extractive body cue:** Moreover, DM may optionally take conditional inputs c, e.g., texts, bounding box layouts, and depth maps.
- **p. 3 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** Intuitively, a model trained for a task involving camera poses could potentially be used in reverse: to retrieve or estimate the camera pose from given ...
- **p. 5 / 3.3. From Sparse Views to 3D Reconstruction - extractive body cue:** 2 2 , (9) where x is the input image and Rψ( ˆT) is the rendered view from viewpoint ˆT acquired from Eq.
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, multiple potential 3D structures could correspond to the same input image.
- **p. 2 / 1. Introduction - extractive body cue:** We propose a novel camera pose estimator that significantly outperforms existing methods in terms of both accuracy and required number of input views, while being ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | More specifically, we randomly sample a registered view as the input condition at each denoising timestep. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | [16], instead of sampling the timestep t from a uniform distribution as in training, we linearly decrease t. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | The reported computation time was measured on a single Nvidia 3090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (a) Pose Optimization + noise Pre-trained Diffusion Reconstruction Loss (b) Sparse-view Fine-tuning + noise Pre-trained Diffusion LoRA Reconstruction Loss (c) 3D Reconstruction Reconstruction Module Pre-trained ...
- **p. 5 / 3.3. From Sparse Views to 3D Reconstruction - extractive body cue:** 3.2, and then feed them as the training data to the differentiable renderer, e.g., NeRF [38] and NeuS [69].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Pose, Optimization, noise, Pre-trained, Diffusion, Reconstruction, Loss, Sparse-view, Fine-tuning, LoRA, Module, back, propagation, Figure, iFusion, framework, then, feed, them, training.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Datasets We conduct experiments using two publicly available object datasets: Google Scanned Object (GSO) [9] and OmniObject3D (OO3D) [73]. | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Denoiser / vector field | Ablation of t annealing for pose estimation on GSO [9]. n poses t annealing Recall ↑ 5◦ 10◦ 20◦ (a) 4 - ... | p. 8 (4.3. Ablation Study), p. 5 (4.2. Experimental Result) |
| Sampling / downstream interface | Evaluation results on pose estimation. iFusion achieves significant improvements for all metrics under 2 input views. | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Experimental Result) |

## Failure and Ablation Link

- **p. 6 / 4.2. Experimental Result - extractive body cue:** We observe that iFusion effectively leverages the additional images without camera poses and generates more faithful images.
- **p. 6 / 4.2. Experimental Result - extractive body cue:** To conclude, when faithful reconstruction is desired, iFusion is extremely beneficial, requiring very few additional view that can be casually captured without knowing the camera ...
- **p. 7 / 4.2. Experimental Result - extractive body cue:** It is clear that iFusion significantly enhances existing reconstruction methods including Zero123-SDS [31], DreamGaussian [64], and Magic123 [48], by adding an additional view without the ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Ablation of t annealing for pose estimation on GSO [9]. n poses t annealing Recall ↑ 5◦ 10◦ 20◦ (a) 4 - 48.61 56.67 61.39 ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Ablation of the number of initial poses for pose estimation on GSO [9]. n poses Recall ↑ Time (s) ↓ 5◦ 10◦ 20◦ (a) 1 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Demonstration on real-world 3D reconstruction. With only two casually taken photos without camera poses, iFusion can reconstruct plausible 3D assets. The top row ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative results on pose estimation. We visualize the predicted poses (thin) alongside the ground truth (bold), using the same color, while the reference ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Diffusion as a Pose Estimator), p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 4 (3.1. Diffusion as a Pose Estimator), p. 3 (3.1. Diffusion as a Pose Estimator), p. 3 (3. Method), p. 5 (3.3. From Sparse Views to 3D Reconstruction), objective p. 3 (3.1. Diffusion as a Pose Estimator), p. 4 (3.1. Diffusion as a Pose Estimator), p. 3 (3.1. Diffusion as a Pose Estimator), p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 4 (3.1. Diffusion as a Pose Estimator), temporal p. 4 (3.2. From Single-View to Multi-View), p. 4 (3.1. Diffusion as a Pose Estimator), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 3 (3. Method), p. 5 (3.3. From Sparse Views to 3D Reconstruction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
