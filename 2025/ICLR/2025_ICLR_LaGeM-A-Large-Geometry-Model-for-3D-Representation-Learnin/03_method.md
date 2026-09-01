# Method - LaGeM: A Large Geometry Model for 3D Representation Learning and Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=72OSO38a2z; PDF retrieval source: https://openreview.net/pdf/fadb73da860f028d2b7db1267acefa4519a291e3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY)): Motivated by this, we propose a cascaded latent diffusion model.

## Method Body Digest

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Motivated by this, we propose a cascaded latent diffusion model.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** We use cross attention to compress the feature set CA(Pi, Pi-1) = Xi.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Each latent vector in Z is first converted back to feature space RC (Latent to Feature, or LtoF in short), LtoF(Z) = X ′ = ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Then PInput is converted to an unordered set with cross-attention CA(Q = PE(P), K = PE(PInput), V = PE(PInput)) = X = {x ∈RC}i=1,2,...,M, (1) ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** As shown in the previous section, we use cross-attention for resampling (both down-sampling and upsampling).
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** When using a small number (512) of latent vectors, our model uses 0.87x time and 0.66x memory during training.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** We do not need an explicit loss to regularize the latent space.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Features to Latents (FtoL) Latent Loss Latents to Features (LtoF) VAE µ = FCµ(x) z = µ + σ ⊙ϵ KL Divergence x′ = FCup(z) ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We summarize our contributions as follows: • We propose a hierarchical autoencoder architecture with faster training time and low memory consumption.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The latent space is composed of several levels. • The model is capable of training on large-scale datasets like objaverse. • We propose a cascaded ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We proposed a U-Net-style transformer for the autoencoding.

## Source Evidence Cues

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Motivated by this, we propose a cascaded latent diffusion model.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** We use cross attention to compress the feature set CA(Pi, Pi-1) = Xi.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Each latent vector in Z is first converted back to feature space RC (Latent to Feature, or LtoF in short), LtoF(Z) = X ′ = ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Then PInput is converted to an unordered set with cross-attention CA(Q = PE(P), K = PE(PInput), V = PE(PInput)) = X = {x ∈RC}i=1,2,...,M, (1) ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** As shown in the previous section, we use cross-attention for resampling (both down-sampling and upsampling).
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** When using a small number (512) of latent vectors, our model uses 0.87x time and 0.66x memory during training.
- **Detected method headings:** 3 METHODOLOGY (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Motivated by this, we propose a cascaded latent diffusion model. | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | We use cross attention to compress the feature set CA(Pi, Pi-1) = Xi. | p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | Each latent vector in Z is first converted back to feature space RC (Latent to Feature, or LtoF in short), LtoF(Z) = ... | p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** We do not need an explicit loss to regularize the latent space.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Features to Latents (FtoL) Latent Loss Latents to Features (LtoF) VAE µ = FCµ(x) z = µ + σ ⊙ϵ KL Divergence x′ = FCup(z) ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** (2) This compression step is also regularized by KL divergence.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** Formally, the optimization goal (for our three-level implementation) is as follows, min D3
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** For larger models (2k latent vectors), the advantage is even more significant (0.7x time and 0.58x memory).
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | process, first, downsamples, input, point, cloud, PInput, furthest, sampling, FPS, where, down-sampling, ratio, low-resolution | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | process, first, downsamples, input, point, cloud, PInput, furthest, sampling, FPS | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | summarize, contributions, follows, hierarchical, autoencoder, architecture, faster, training, time, memory | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | need, explicit, loss, regularize, latent, space, Features, Latents, FtoL, LtoF | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** The process first downsamples the 3D input point cloud PInput = {pi}i=1,...,N with furthest point sampling (FPS), P = FPS(PInput, r), where r is the ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** For notational convenience, we denote the input point cloud as level 0.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** In the i-th level, we first obtain a lower resolution of the point clouds in the (i -1)-th level, FPS(Pi-1, ri-1) = Pi where P0 ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** For diffusion-based image super-resolution methods, this is often done by bilinearly interpolating small images and concatenating them with denoising networks' inputs.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Point Cloud Output Init Diffusion Level 2 Diffusion Level 1 Diffusion Level 3 C Figure 2: Pipeline.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** We also write CA(P, PInput) for short.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** Specifically, assuming we are training a denoising network for Z2, the input of the network is ˜Z2(t), CA( ˜Z2(t), Z3).
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | , (10) where Di is a denoising network, t represents timestep or noise level, ˜Zi(t) is the noised version (at timestep t) ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | (2) This compression step is also regularized by KL divergence. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | For larger models (2k latent vectors), the advantage is even more significant (0.7x time and 0.58x memory). | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | For larger models (2k latent vectors), the advantage is even more significant (0.7x time and 0.58x memory). | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** When using a small number (512) of latent vectors, our model uses 0.87x time and 0.66x memory during training.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We can see that, LaGeM-ShapeNet has almost the same number of parameters as VecSet, but with much shorter training time and less training memory.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** For Objaverse-10k, due to limited training GPU resources, we select a subset of 10k models from Objaverse and train the unconditional generative model.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** This severely affects the training time when M is large.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** VecSet LaGeM VecSet LaGeM VecSet LaGeM Batch Size 64 8 4 Self Attn Layers 24 8/8/8 24 8/8/8 24 8/8/8 Attn Channels 512 512/512/512 1k ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Motivated, cascaded, latent, diffusion, model, cross, attention, compress, feature, Pi-1, vector, first, converted, back, space, LtoF, short, Then, PInput, unordered.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | The objects from these datasets vary from daily objects, CAD models, human models, and synthetic objects. | p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Denoiser / vector field | Both models are compared against VecSet (Zhang et al., 2023). | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Sampling / downstream interface | While for LaGeM-Objaverse, there is a large improvement in both training cost and quantitative results. | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 13: Latent with red color Z means it is replaced by Gaussian noise. Latent with blue color Z means it is generated with the ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Due to failures of modeling loading and conversion, we obtained around 600k watertight models for training.
- **p. 10 / 5 CONCLUSION - extractive PDF cue:** Our method does not solve the high training cost problem of diffusion itself.
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 13: Latent with red color Z means it is replaced by Gaussian noise. Latent with blue color Z means it is generated with the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), objective p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), temporal p. 6 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 7 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
