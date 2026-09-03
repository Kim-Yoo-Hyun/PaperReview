# Method - Dream-to-Recon: Monocular 3D Reconstruction with Diffusion-Depth Distillation from Single Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wulff_Dream-to-Recon_Monocular_3D_Reconstruction_with_Diffusion-Depth_Distillation_from_Single_Images_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wulff_Dream-to-Recon_Monocular_3D_Reconstruction_with_Diffusion-Depth_Distillation_from_Single_Images_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Training the View Completion Model), p. 5 (3.4. Distilling into a Scene Reconstruction Model), p. 4 (3.2. Training the View Completion Model), p. 3 (3.2. Training the View Completion Model), p. 3 (3. Method), p. 5 (3.4. Distilling into a Scene Reconstruction Model)): Training uses only a single view per scene and leverages forward-backward warping for data generation. b) The VCM is applied iteratively alongside a depth prediction network to synthesize virtual novel ...

## Method Body Digest

- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** Training uses only a single view per scene and leverages forward-backward warping for data generation. b) The VCM is applied iteratively alongside a depth prediction ...
- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** The loss term provides training signals to the surface areas of the predicted density field, which are particularly hard to learn. \mat h c al ...
- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** 1 ControlNet Denoising U-Net VCM Noise CLIP(Iin) a) View Completion Model Training b) Multi-view and 3D Data Synthesis Predict Depth VCM c) Synthetic Data Distillation ...
- **p. 3 / 3.2. Training the View Completion Model - extractive body cue:** Then, a generative model fills in the empty or occluded regions conditioned on the known context and ideally removes artifacts.
- **p. 3 / 3. Method - extractive body cue:** In the following, we first introduce our view completion model (VCM), which completes occlusions and removes artifacts in warped images.
- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** We then directly supervise them via the depth predictions Di from V using a Gaussian Negative Log-Likelihood (GNLL) loss, as proposed in [46].
- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** The training involves two loss terms.
- **p. 4 / 3.3. Synthesizing Scene Geometry - extractive body cue:** Within the render-refine-repeat framework, we generate several synthetic novel views, complete them using the VCM, predict corresponding depth maps, and update the scene geometry.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we show that our method has unique advantages when it comes to dynamic scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • A specialized view completion model that inpaints and refines synthetic novel views and which can be trained using only a single ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** For a given scene, our method receives as input a single image Iin ∈([0, 1]3)Ω, where Ω= {1, . . . , H} × {1, ...

## Source Evidence Cues

- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** Training uses only a single view per scene and leverages forward-backward warping for data generation. b) The VCM is applied iteratively alongside a depth prediction ...
- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** The loss term provides training signals to the surface areas of the predicted density field, which are particularly hard to learn. \mat h c al ...
- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** 1 ControlNet Denoising U-Net VCM Noise CLIP(Iin) a) View Completion Model Training b) Multi-view and 3D Data Synthesis Predict Depth VCM c) Synthetic Data Distillation ...
- **p. 3 / 3.2. Training the View Completion Model - extractive body cue:** Then, a generative model fills in the empty or occluded regions conditioned on the known context and ideally removes artifacts.
- **p. 3 / 3. Method - extractive body cue:** In the following, we first introduce our view completion model (VCM), which completes occlusions and removes artifacts in warped images.
- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** We then directly supervise them via the depth predictions Di from V using a Gaussian Negative Log-Likelihood (GNLL) loss, as proposed in [46].
- **Detected method headings:** 3. Method (p. 3); 3.2. Training the View Completion Model (p. 3); 3.4. Distilling into a Scene Reconstruction Model (p. 5); 4.4. Distillation into a Feed-Forward Model (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Training uses only a single view per scene and leverages forward-backward warping for data generation. b) The VCM is applied iteratively alongside ... | p. 4 (3.2. Training the View Completion Model), p. 5 (3.4. Distilling into a Scene Reconstruction Model) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | The loss term provides training signals to the surface areas of the predicted density field, which are particularly hard to learn. \mat ... | p. 5 (3.4. Distilling into a Scene Reconstruction Model), p. 4 (3.2. Training the View Completion Model) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | 1 ControlNet Denoising U-Net VCM Noise CLIP(Iin) a) View Completion Model Training b) Multi-view and 3D Data Synthesis Predict Depth VCM c) ... | p. 4 (3.2. Training the View Completion Model), p. 3 (3.2. Training the View Completion Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** We then directly supervise them via the depth predictions Di from V using a Gaussian Negative Log-Likelihood (GNLL) loss, as proposed in [46].
- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** The training involves two loss terms.
- **p. 4 / 3.3. Synthesizing Scene Geometry - extractive body cue:** Within the render-refine-repeat framework, we generate several synthetic novel views, complete them using the VCM, predict corresponding depth maps, and update the scene geometry.
- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** Training uses only a single view per scene and leverages forward-backward warping for data generation. b) The VCM is applied iteratively alongside a depth prediction ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (3.4. Distilling into a Scene Reconstruction Model), p. 5 (3.4. Distilling into a Scene Reconstruction Model), p. 4 (3.3. Synthesizing Scene Geometry).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, input, image, Iin, predicted, depth, DIin, first, warp, pixels, virtual, novel, view, random | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Given, input, image, Iin, predicted, depth, DIin, first, warp, pixels | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | Furthermore, unique, advantages, when, comes, dynamic, scenes, contributions, specialized, view | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | then, directly, supervise, them, depth, predictions, Gaussian, Negative, Log-Likelihood, GNLL | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. Training the View Completion Model - extractive body cue:** Given an input image Iin and predicted depth DIin, we first warp the pixels into a virtual novel view with a random camera pose.
- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** Training uses only a single view per scene and leverages forward-backward warping for data generation. b) The VCM is applied iteratively alongside a depth prediction ...
- **p. 2 / 1. Introduction - extractive body cue:** Starting from an input image, they first warp the pixels into a virtual novel view using the depth predictor.
- **p. 3 / 3.2. Training the View Completion Model - extractive body cue:** From this input, the VCM produces an inpainted and refined image.
- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** For areas of the input image, which would be occluded in the novel view, the backward warped image will be corrupted.
- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** Given a single image as input, it predicts a discretized occupancy field ΘSRM ∈[0, 1]Z×H×W .
- **p. 1 / 1. Introduction - extractive body cue:** Consequently, it is not possible to infer information about areas that are beyond the parts visible in the input image.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Both use multi-view supervision from all cameras and multiple time steps. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | This failure stems from their use of multi-view data across multiple timesteps, which introduces inconsistency when the object is in motion. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | 1 ControlNet Denoising U-Net VCM Noise CLIP(Iin) a) View Completion Model Training b) Multi-view and 3D Data Synthesis Predict Depth VCM c) ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** Training uses only a single view per scene and leverages forward-backward warping for data generation. b) The VCM is applied iteratively alongside a depth prediction ...
- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** The loss term provides training signals to the surface areas of the predicted density field, which are particularly hard to learn. \mat h c al ...
- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** 1 ControlNet Denoising U-Net VCM Noise CLIP(Iin) a) View Completion Model Training b) Multi-view and 3D Data Synthesis Predict Depth VCM c) Synthetic Data Distillation ...
- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** 1 ControlNet Denoising U-Net VCM Noise CLIP(Iin) a) View Completion Model Training b) Multi-view and 3D Data Synthesis Predict Depth VCM c) Synthetic Data Distillation ...
- **p. 5 / 4.1. Setup - extractive body cue:** We add batch-normalization layers to the backbone's decoder to stabilize mixed-precision training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Training, uses, only, single, view, scene, leverages, forward-backward, warping, data, generation, VCM, applied, iteratively, alongside, depth, prediction, network, synthesize, virtual.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. Training the View Completion Model (p. 3); 3.4. Distilling into a Scene Reconstruction Model (p. 5); 4.4. Distillation into a Feed-Forward Model (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Both datasets contain scenes with complex layouts and possibly dynamic objects. | p. 5 (4.1. Setup), p. 6 (4.2. Scene Reconstruction) |
| Denoiser / vector field | Here, the state-of-the-art volumetric reconstruction methods Behind the Scenes (BTS) [60] and Know Your Neighbor (KYN) [27] serve as baselines. | p. 6 (4.2. Scene Reconstruction), p. 7 (4.3.1. Conditioning of the VCM) |
| Sampling / downstream interface | We contend that, despite being slightly outperformed in quantitative metrics by the directly synthesized geometry, the distilled model is more reliable and ... | p. 6 (4.2. Scene Reconstruction), p. 8 (4.3.2. Occlusion detection in novel views) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Qualitative effect of different loss terms. See Tab. 4. lated variants, our full loss setup achieves competitive Oacc and the highest IEacc. While ...
- **p. 6 / 4.3.1. Conditioning of the VCM - extractive body cue:** We evaluate both configurations on the KITTI-360 dataset (VCMK), and further examine the effect of finetuning on Waymo (VCMK→W).
- **p. 8 / 4.3.2. Occlusion detection in novel views - extractive body cue:** Effect of occlusion detection strategies.
- **p. 6 / 4.3. Scene Synthesis using the VCM - extractive body cue:** To this end, we rigorously validate our design choices through a series of ablation studies.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Effect of VCM conditioning. See Tab. 2.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Dream-to-Recon. We leverage fine-tuned diffusion models for inpainting and a pre-trained depth predictor to generate high- quality scene geometry from a single image, ...
- **p. 6 / 4.2. Scene Reconstruction - extractive body cue:** This failure stems from their use of multi-view data across multiple timesteps, which introduces inconsistency when the object is in motion.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Training the View Completion Model), p. 5 (3.4. Distilling into a Scene Reconstruction Model), p. 4 (3.2. Training the View Completion Model), p. 3 (3.2. Training the View Completion Model), p. 3 (3. Method), p. 5 (3.4. Distilling into a Scene Reconstruction Model), objective p. 5 (3.4. Distilling into a Scene Reconstruction Model), p. 5 (3.4. Distilling into a Scene Reconstruction Model), p. 4 (3.3. Synthesizing Scene Geometry), p. 4 (3.2. Training the View Completion Model), temporal p. 6 (4.2. Scene Reconstruction), p. 6 (4.2. Scene Reconstruction), p. 3 (3.2. Training the View Completion Model), p. 4 (3.3. Synthesizing Scene Geometry), p. 4 (3.3. Synthesizing Scene Geometry), p. 5 (3.3. Synthesizing Scene Geometry).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
