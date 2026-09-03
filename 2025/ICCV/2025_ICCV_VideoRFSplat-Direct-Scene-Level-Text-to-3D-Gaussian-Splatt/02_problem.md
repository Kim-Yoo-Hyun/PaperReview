# Problem - VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): These pose fundamental challenges to developing generative models for direct 3DGS generation, introducing difficulties distinct from object-level generation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We propose VideoRFSplat, a direct text-to-3D model leveraging a video generation model to generate realistic 3D Gaussian Splatting (3DGS) for unbounded real-world scenes.
- **p. 1 / Abstract - extractive body cue:** To generate diverse camera poses and unbounded spatial extent of real-world scenes, while ensuring generalization to arbitrary text prompts, previous methods fine-tune 2D generative models ...
- **p. 1 / Abstract - extractive body cue:** However, these methods suffer from instability when extending 2D generative models to joint modeling due to the modality gap, which necessitates additional models to stabilize ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose an architecture and a sampling strategy to jointly model multi-view images and camera poses when fine-tuning a video genera
- **p. 1 / Abstract - extractive body cue:** Our core idea is a dual-stream architecture that attaches a dedicated pose generation model alongside a pretrained video generation model via communication blocks, generating multi-view ...
- **p. 2 / 1. Introduction - extractive body cue:** These pose fundamental challenges to developing generative models for direct 3DGS generation, introducing difficulties distinct from object-level generation.
- **p. 2 / 1. Introduction - extractive body cue:** However, prior works [20, 34, 35] have suffered from instability in extending 2D generative models to joint modeling due to the modality gap, hindering high-quality ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These pose fundamental challenges to developing generative models for direct 3DGS generation, introducing difficulties distinct from object-level generation. | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | We hypothesize that uncertainty in early sampling leads to unstable pose-image interactions, destabilizing camera pose generation and ultimately degrading multi-view image quality. | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF body |
| State / latent | hypothesize, uncertainty, early, sampling, leads, unstable, pose-image, interactions, destabilizing, camera | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | evaluation, sequences, RealEstate10K, extracted, camera, trajectories, captions, generate | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: hypothesize, uncertainty, early, sampling, leads, unstable, pose-image, interactions, destabilizing, camera | p. 8 (Method), p. 2 (1. Introduction), p. 8 (Method) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: Furthermore, asynchronous, adaptation, Classifier-Free, Guidance, CFG, enables, clearer | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Dual-Stream Pose-Video Joint Model) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: loss, enables, vector, field, prediction, even, different, timesteps | p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model) |
| Success / guarantee | sample quality, diversity and latency | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** However, prior works [20, 34, 35] have suffered from instability in extending 2D generative models to joint modeling due to the modality gap, hindering high-quality ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model)): Furthermore, we propose an asynchronous adaptation of Classifier-Free Guidance (CFG) that enables the clearer pose to better guide multi-view image generation.

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, to eliminate external dependency, we present VideoRFSplat, a direct 3DGS generation model that introduces an architecture and sampling strategy for jointly generating ...
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To reduce interference, we propose a dual-stream architecture with dedicated submodules for pose and image generation, communicating via cross-attention at intermediate layers (see Fig.
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To address this, we propose an asynchronous timestep strategy, decoupling the timesteps of pose and multi-view generation modules and enabling one modality to denoise faster, ...
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** This exchange enables controlled interaction between the two models while preserving their specialized forward paths and reducing interference between pose and multi-view modalities.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Figure 3. Failure analysis of synchronized sampling and the effectiveness of asynchronous sampling. (Left) Early in sampling (t ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 7. Architecture Comparison. For each example, Left: chan- nel concat architecture (SplatFlow). Right: our architecture. framed key ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 4. Asynchrnous schedule (δ = 0.2). During sampling, we denoise the pose modality faster than im- ages, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 8 (Method), p. 2 (1. Introduction), p. 8 (Method), p. 4 (4.1. Dual-Stream Pose-Video Joint Model). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 8 (Method), p. 2 (1. Introduction), p. 8 (Method), p. 4 (4.1. Dual-Stream Pose-Video Joint Model), objective p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
