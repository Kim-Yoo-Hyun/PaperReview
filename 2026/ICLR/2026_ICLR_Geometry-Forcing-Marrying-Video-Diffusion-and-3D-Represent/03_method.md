# Method - Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ULXYZCms41; PDF retrieval source: https://openreview.net/pdf/dea370a01f4626162b2a827d9926302e6c125e13.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 20 (C.4 METRICS), p. 18 (C.4 METRICS), p. 18 (C.2 TRAINING), p. 21 (C.4 METRICS), p. 21 (C.4 METRICS), p. 19 (C.4 METRICS)): Method Frames FVD↓ LPIPS↓ SSIM↑ PSNR↑ RPE↓ RVE↓ DFoT (Song et al., 2025) 256 364 0.55 0.36 11.40 0.3575 297 Geometry Forcing-4 256 261 0.51 0.38 12.21 0.3451 297 Geometry ...

## Method Body Digest

- **p. 20 / C.4 METRICS - extractive PDF cue:** Method Frames FVD↓ LPIPS↓ SSIM↑ PSNR↑ RPE↓ RVE↓ DFoT (Song et al., 2025) 256 364 0.55 0.36 11.40 0.3575 297 Geometry Forcing-4 256 261 0.51 ...
- **p. 18 / C.4 METRICS - extractive PDF cue:** Specifically, DROID-SLAM first extracts corresponding features across frames and then refines camera poses (Gt) and per-pixel depth estimates (dt) through its differentiable Dense Bundle Adjustment ...
- **p. 18 / C.2 TRAINING - extractive PDF cue:** The geometric alignment loss is combined with the standard diffusion training objective.
- **p. 21 / C.4 METRICS - extractive PDF cue:** The feature extraction time of the VGGT model increases with the number of input views.
- **p. 21 / C.4 METRICS - extractive PDF cue:** Method Aesthetic Quality↑ Imaging Quality↑ Motion Smoothness↑ Wan2.1 0.58 0.56 0.98 Wan2.1 + GF 0.59 0.59 0.99 We also provide a feature extraction time of ...
- **p. 19 / C.4 METRICS - extractive PDF cue:** A camera trajectory of 256 frames is then constructed by rotating the initial camera pose around the Y-axis.
- **p. 19 / C.4 METRICS - extractive PDF cue:** For each of 100 randomly sampled RealEstate10K video clips, we extract the first frame and initial camera pose.
- **p. 20 / C.4 METRICS - extractive PDF cue:** Additionally, during inference, our method incurs no additional computational cost compared to other methods that use explicit or implicit memory.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To align these two representations, our method introduces two complementary alignment objectives: Angular Alignment and Scale Alignment.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Experimental results demonstrate that our method delivers substantial gains in geometric consistency and visual quality over the baseline methods.
- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** 4.2, we introduce two regularization objectives designed to facilitate representation alignment between the diffusion model and geometric foundation model.

## Source Evidence Cues

- **p. 20 / C.4 METRICS - extractive PDF cue:** Method Frames FVD↓ LPIPS↓ SSIM↑ PSNR↑ RPE↓ RVE↓ DFoT (Song et al., 2025) 256 364 0.55 0.36 11.40 0.3575 297 Geometry Forcing-4 256 261 0.51 ...
- **p. 18 / C.4 METRICS - extractive PDF cue:** Specifically, DROID-SLAM first extracts corresponding features across frames and then refines camera poses (Gt) and per-pixel depth estimates (dt) through its differentiable Dense Bundle Adjustment ...
- **p. 18 / C.2 TRAINING - extractive PDF cue:** The geometric alignment loss is combined with the standard diffusion training objective.
- **p. 21 / C.4 METRICS - extractive PDF cue:** The feature extraction time of the VGGT model increases with the number of input views.
- **p. 21 / C.4 METRICS - extractive PDF cue:** Method Aesthetic Quality↑ Imaging Quality↑ Motion Smoothness↑ Wan2.1 0.58 0.56 0.98 Wan2.1 + GF 0.59 0.59 0.99 We also provide a feature extraction time of ...
- **p. 19 / C.4 METRICS - extractive PDF cue:** A camera trajectory of 256 frames is then constructed by rotating the initial camera pose around the Y-axis.
- **p. 19 / C.4 METRICS - extractive PDF cue:** For each of 100 randomly sampled RealEstate10K video clips, we extract the first frame and initial camera pose.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Method Frames FVD↓ LPIPS↓ SSIM↑ PSNR↑ RPE↓ RVE↓ DFoT (Song et al., 2025) 256 364 0.55 0.36 11.40 0.3575 297 Geometry Forcing-4 ... | p. 20 (C.4 METRICS), p. 18 (C.4 METRICS) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Specifically, DROID-SLAM first extracts corresponding features across frames and then refines camera poses (Gt) and per-pixel depth estimates (dt) through its differentiable ... | p. 18 (C.4 METRICS), p. 18 (C.2 TRAINING) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | The geometric alignment loss is combined with the standard diffusion training objective. | p. 18 (C.2 TRAINING), p. 21 (C.4 METRICS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 18 / C.2 TRAINING - extractive PDF cue:** The geometric alignment loss is combined with the standard diffusion training objective.
- **p. 18 / C.4 METRICS - extractive PDF cue:** Specifically, DROID-SLAM first extracts corresponding features across frames and then refines camera poses (Gt) and per-pixel depth estimates (dt) through its differentiable Dense Bundle Adjustment ...
- **p. 20 / C.4 METRICS - extractive PDF cue:** Additionally, during inference, our method incurs no additional computational cost compared to other methods that use explicit or implicit memory.
- **p. 24 / C.4 METRICS - extractive PDF cue:** Qualitative Ablation on Alignment loss.
- **p. 19 / C.4 METRICS - extractive PDF cue:** We optimize the DPT head for 2500 steps using a learning rate of 1×10-4 and a batch size of 4.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 18 (C.2 TRAINING), p. 18 (C.4 METRICS), p. 24 (C.4 METRICS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | evaluate, effectiveness, widely, adopted, benchmarks, camera-view-conditioned, video, generation, RealEstate10K, Zhou, action-conditioned, Minecraft, environment, Baker | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | evaluate, effectiveness, widely, adopted, benchmarks, camera-view-conditioned, video, generation, RealEstate10K, Zhou | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | align, representations, introduces, complementary, alignment, objectives, Angular, Scale, Experimental, demonstrate | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | geometric, alignment, loss, combined, standard, diffusion, training, objective, Specifically, DROID-SLAM | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We evaluate the effectiveness of GF on two widely adopted benchmarks: camera-view-conditioned video generation on RealEstate10K (Zhou et al., 2018) and action-conditioned video generation in ...
- **p. 21 / C.4 METRICS - extractive PDF cue:** The feature extraction time of the VGGT model increases with the number of input views.
- **p. 21 / C.4 METRICS - extractive PDF cue:** The result shows that the extraction time increases from 0.1s to 0.8s when the input increases from 1 to 12.
- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** The target velocity field is defined as the difference between the noise and the clean input.
- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** 3.2 VISUAL GEOMETRY GROUNDED TRANSFORMER Visual Geometry Grounded Transformer (VGGT) (Wang et al., 2025b) is a feed-forward model that directly outputs 3D attributes of a ...
- **p. 5 / 3 PRELIMINARIES - extractive PDF cue:** Angular Alignment enforces directional correspondence between the hidden states of the diffusion model, denoted by h, and specified target features, denoted by y.
- **p. 5 / 3 PRELIMINARIES - extractive PDF cue:** In practice, the target features y ∈RL×N×P ×D, where L denotes the number of layers, N denotes the number of input images, P denotes the ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Revisit Error (RVE) assesses long-range temporal consistency by examining discrepancies between initial and revisited frames under complete camera rotation. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | For action-conditioned video generation, we apply GF to Next-Frame Diffusion (Cheng et al., 2025), training on 32-frame 384×224 videos for 2,000 steps ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | For action-conditioned video generation, we apply GF to Next-Frame Diffusion (Cheng et al., 2025), training on 32-frame 384×224 videos for 2,000 steps ... | hardware, batch and throughput |

## Training vs Inference

- **p. 20 / C.4 METRICS - extractive PDF cue:** Method Frames FVD↓ LPIPS↓ SSIM↑ PSNR↑ RPE↓ RVE↓ DFoT (Song et al., 2025) 256 364 0.55 0.36 11.40 0.3575 297 Geometry Forcing-4 256 261 0.51 ...
- **p. 18 / C.4 METRICS - extractive PDF cue:** Specifically, DROID-SLAM first extracts corresponding features across frames and then refines camera poses (Gt) and per-pixel depth estimates (dt) through its differentiable Dense Bundle Adjustment ...
- **p. 18 / C.2 TRAINING - extractive PDF cue:** The geometric alignment loss is combined with the standard diffusion training objective.
- **p. 6 / 5 EXPERIMENTS - extractive PDF cue:** For action-conditioned video generation, we apply GF to Next-Frame Diffusion (Cheng et al., 2025), training on 32-frame 384×224 videos for 2,000 steps with a learning ...
- **p. 18 / C.2 TRAINING - extractive PDF cue:** Training proceeds for 2 epochs using a learning rate of 8 × 10-6 and a global batch size of 40.
- **p. 20 / C.4 METRICS - extractive PDF cue:** For fine-tuning, our method requires only a few thousand steps and completes within hours, yielding substantial efficiency gains over full pre-training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Frames, FVD, LPIPS, SSIM, PSNR, RPE, RVE, DFoT, Song, Geometry, Forcing-4, Forcing-8, Forcing-16, default, ALIGNMENT, CONTEXT, LENGTH, Forcing, feeds, VGGT.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | In this section, we evaluate Geometry Forcing (GF) on camera-view-conditioned video generation on the RealEstate10K (Zhou et al., 2018) dataset and action-conditioned ... | p. 6 (5 EXPERIMENTS), p. 18 (C.1 DATASET) |
| Denoiser / vector field | Figure 2: Qualitative comparison of camera view-conditioned video generation under full- circle rotation. Videos are generated from a single frame, and per-frame ... | p. 7 (Figure/Table caption), p. 7 (5 EXPERIMENTS) |
| Sampling / downstream interface | Experimental results demonstrate that our approach achieves improvements across multiple evaluation dimensions, including visual aesthetics, motion smoothness, and motion quality, as detailed ... | p. 20 (C.4 METRICS), p. 19 (C.4 METRICS) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation study on target represen- tation. We compare the effect of aligning the diffusion model with different target representa- tions: DINOv2 (semantic), VGGT ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 3: Ablation study on alignment depth. We present FVD-256 and FVD-16 re- sults for different alignment layers of the dif- fusion model, which suggest ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5.3 ABLATION STUDIES We provide a series of ablation studies to validate the design of GF.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 2: Ablation study on target representation.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Figure 3: Ablation study on alignment depth.
- **p. 24 / C.4 METRICS - extractive PDF cue:** To further assess the impact of the proposed scale alignment loss, we conduct qualitative comparisons between models trained with and without this component (Fig.
- **p. 19 / C.4 METRICS - extractive PDF cue:** D SUPPLEMENTARY EXPERIMENTS D.1 ABLATION ON TEACHER MODEL Geometry Forcing does not depend on a specific 3D foundation model but still requires the 3D foundation ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 20 (C.4 METRICS), p. 18 (C.4 METRICS), p. 18 (C.2 TRAINING), p. 21 (C.4 METRICS), p. 21 (C.4 METRICS), p. 19 (C.4 METRICS), objective p. 18 (C.2 TRAINING), p. 18 (C.4 METRICS), p. 20 (C.4 METRICS), p. 24 (C.4 METRICS), p. 19 (C.4 METRICS), temporal p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 22 (C.4 METRICS), p. 4 (3 PRELIMINARIES), p. 7 (5 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
