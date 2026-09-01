# Method - ComPC: Completing a 3D Point Cloud with 2D Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SoUwcVplq4; PDF retrieval source: https://openreview.net/pdf/07e0e163b5ab2a3918ebbccd045080a0decea42e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY)): Specifically, we use Iin to guide the optimization of 3D Gaussians Gm by borrowing priors from the 2D diffusion model in Zero 1-to-3 (Liu et al., 2023).

## Method Body Digest

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Specifically, we use Iin to guide the optimization of 3D Gaussians Gm by borrowing priors from the 2D diffusion model in Zero 1-to-3 (Liu et ...
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** 2, the whole completion process is composed of Partial Gaussian Initialization (PGI), Zero-shot Fractal Completion (ZFC), and Point Cloud Extraction (PCE).
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** To introduce priors from pretrained 2D diffusion models, we use 3D Gaussian Splatting (GS) to achieve differentiable rendering from 3D point clouds to 2D images.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Given that the centers of Gin are anchored to Pin, we can estimate Vp by minimizing: Vp = arg min Vn CD(Pin[h(Gin, Vn)], Pin) + ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** For any point cloud to be completed, we first determine an reference camera pose Vp, that captures its most completed observation.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Upon estimating the reference camera pose Vp, we render a reference image Iin from 3D Gaussians Gin initialized from partial point cloud Pin.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Inspired by the amodal perception (Lehar, 1999; Breckon & Fisher, 2005), we aim to complete a point cloud by utilizing the observation from a reference ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** 2.2 POINT CLOUD COMPLETION Point cloud completion aims to recover completed point clouds from partial input point clouds.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial points, which is ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** In view of the above-mentioned issues, we propose a novel test-time point cloud completion framework that eliminates the need for any extra manually provided information ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Inspired by the capability of novel view synthetic diffusion model, e.g., Zero 1-to-3 (Liu et al., 2023), we propose to use the reference image as ...

## Source Evidence Cues

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Specifically, we use Iin to guide the optimization of 3D Gaussians Gm by borrowing priors from the 2D diffusion model in Zero 1-to-3 (Liu et ...
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** 2, the whole completion process is composed of Partial Gaussian Initialization (PGI), Zero-shot Fractal Completion (ZFC), and Point Cloud Extraction (PCE).
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** To introduce priors from pretrained 2D diffusion models, we use 3D Gaussian Splatting (GS) to achieve differentiable rendering from 3D point clouds to 2D images.
- **Detected method headings:** 3 METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Specifically, we use Iin to guide the optimization of 3D Gaussians Gm by borrowing priors from the 2D diffusion model in Zero ... | p. 4 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | 2, the whole completion process is composed of Partial Gaussian Initialization (PGI), Zero-shot Fractal Completion (ZFC), and Point Cloud Extraction (PCE). | p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | To introduce priors from pretrained 2D diffusion models, we use 3D Gaussian Splatting (GS) to achieve differentiable rendering from 3D point clouds ... | p. 4 (3 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Given that the centers of Gin are anchored to Pin, we can estimate Vp by minimizing: Vp = arg min Vn CD(Pin[h(Gin, Vn)], Pin) + ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Published as a conference paper at ICLR 2025 𝑓𝑍 SDS 𝑉𝑖 𝐼𝑖 𝑃𝑖𝑛 𝑃𝑝𝑟𝑒 𝐺𝑖𝑛 𝐺𝑚 Virtual Camera Froze parameters Optimize parameters Initialize 3D Gaussians ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | main, contributions, summarized, below, Partial, Gaussian, Initialization, generate, reference, image, points, observed, estimated, viewpoint | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | main, contributions, summarized, below, Partial, Gaussian, Initialization, generate, reference, image | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | main, contributions, summarized, below, Partial, Gaussian, Initialization, generate, reference, image | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | Given, centers, Gin, anchored, Pin, estimate, minimizing, Depth, where, Chamfer | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial points, which is ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** For any point cloud to be completed, we first determine an reference camera pose Vp, that captures its most completed observation.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Published as a conference paper at ICLR 2025 𝑓𝑍 SDS 𝑉𝑖 𝐼𝑖 𝑃𝑖𝑛 𝑃𝑝𝑟𝑒 𝐺𝑖𝑛 𝐺𝑚 Virtual Camera Froze parameters Optimize parameters Initialize 3D Gaussians ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Upon estimating the reference camera pose Vp, we render a reference image Iin from 3D Gaussians Gin initialized from partial point cloud Pin.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Inspired by the amodal perception (Lehar, 1999; Breckon & Fisher, 2005), we aim to complete a point cloud by utilizing the observation from a reference ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** 2.2 POINT CLOUD COMPLETION Point cloud completion aims to recover completed point clouds from partial input point clouds.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** The Fractal approach focuses on predicting only the missing regions of point clouds, preserving existing details by retaining the shapes from the partial input.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Defining ϵfZ as the noise anticipated by the 2D diffusion model fZ with t and ϵ indicating the time step and standard ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | Published as a conference paper at ICLR 2025 𝑓𝑍 SDS 𝑉𝑖 𝐼𝑖 𝑃𝑖𝑛 𝑃𝑝𝑟𝑒 𝐺𝑖𝑛 𝐺𝑚 Virtual Camera Froze parameters Optimize parameters ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** To introduce priors from pretrained 2D diffusion models, we use 3D Gaussian Splatting (GS) to achieve differentiable rendering from 3D point clouds to 2D images.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Additionally, it incorporates a Preservation Constraint computed with respect to Vp.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, Iin, guide, optimization, Gaussians, borrowing, priors, diffusion, model, Zero, to-3, Liu, whole, completion, process, composed, Partial, Gaussian, Initialization, PGI.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Published as a conference paper at ICLR 2025 Table 12: Quantitative comparison on ShapeNet dataset. "Known category" and "Unknown category" denote categories ... | p. 19 (A.10 EVALUATION ON LIDAR POINTS), p. 9 (4 EXPERIMENTS) |
| Denoiser / vector field | We compare our approach with state-of-the-art supervised methods including PointAttN(Wang et al., 2024), PoinTr (Yu et al., 2021), SVDFormer (Zhu et al., ... | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Sampling / downstream interface | The results demonstrate that the Preservation Constraint improves performance compared to standard view-dependent diffusion guidance. | p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** We also provide quantitative ablation study for our proposed components in Table 4.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** 5 without any prompts and related geometries.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Depth Coordinates Normal(Ours) CD 2.25 2.01 1.96 EMD 2.88 2.64 2.60 Table 4: Ablation for ZFC and PCE.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** More detailed ablation study can be found in the appendix A.
- **p. 14 / Figure/Table caption - extractive PDF cue:** Figure 9: Ablation study for Grid Pulling module. Far, Near, and Merge denote the Lfar, Lnear, and merge layer gm(·), respectively. Vanilla Gaussian + Opacity ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 5: The setting of mentioned hyper-parameters in Sec. 3. Hyper-parameters w0 ∼w3 1e-3, 1e3, 1e2, 0.1 δ, σ0, σn 0.01, 0.005, 0.05 Iterations 1000 ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 11: Ablation Study for the Fractal completion strategy. W/ Fractal and W/O Fractal denote using and not using Fractal completion strategy, respectively.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), objective p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), temporal p. 5 (2) The color Gc), p. 4 (3 METHODOLOGY), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (1) The opacity Go).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
