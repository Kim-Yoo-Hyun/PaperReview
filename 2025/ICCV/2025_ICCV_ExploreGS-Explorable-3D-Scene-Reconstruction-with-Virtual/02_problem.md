# Problem - ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera Samplings and Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): This limitation stems from missing information, since optimization-based approaches cannot synthesize contents beyond the observed data.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Recent advances in novel view synthesis (NVS) have enabled real-time rendering with 3D Gaussian Splatting (3DGS).
- **p. 1 / Abstract - extractive PDF cue:** However, existing methods struggle with artifacts and missing regions when rendering from viewpoints that deviate from the training trajectory, limiting seamless scene exploration.
- **p. 1 / Abstract - extractive PDF cue:** To address this, we propose a 3DGS-based pipeline that generates additional training views to enhance reconstruction.
- **p. 1 / Abstract - extractive PDF cue:** We introduce an information-gain-driven virtual camera placement strategy to maximize scene coverage, followed by video diffusion priors to refine rendered results.
- **p. 1 / Abstract - extractive PDF cue:** Fine-tuning 3D Gaussians with these enhanced views significantly improves reconstruction quality.
- **p. 2 / 1. Introduction - extractive PDF cue:** This limitation stems from missing information, since optimization-based approaches cannot synthesize contents beyond the observed data.
- **p. 2 / 1. Introduction - extractive PDF cue:** The key challenges of explorable scene reconstruction lie in determining the optimal placement of virtual viewpoints.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This limitation stems from missing information, since optimization-based approaches cannot synthesize contents beyond the observed data. | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | Then, we determine the boundary of reconstructable scene based on the input observations and identify occupied regions for virtual viewpoints samplings. | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF |
| State / latent | Then, determine, boundary, reconstructable, scene, input, observations, identify, occupied, regions | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | Unfortunately, experience, fully, realized, existing, methods, suffer, severe | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: Then, determine, boundary, reconstructable, scene, input, observations, identify, occupied, regions | p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization), p. 2 (1. Introduction) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: summary, contributions, organized, follows, pipeline, explorable, scene, reconstruction | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Scene initialization) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: camera, trajectories, maximizes, information, gain, sampled, trajectory, Trn | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.2. Scene initialization), p. 4 (3.3. Virtual view sampling), p. 4 (3.3. Virtual view sampling) |
| Success / guarantee | sample quality, diversity and latency | p. 8 (5.3. Ablation study), p. 8 (5.3. Ablation study), p. 6 (4.2. Curated Nerfbusters) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** The key challenges of explorable scene reconstruction lie in determining the optimal placement of virtual viewpoints.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Scene initialization), p. 3 (3.3. Virtual view sampling), p. 1 (1. Introduction)): In summary, our contributions can be organized as follows: • We propose a pipeline for explorable 3D scene reconstruction, which incorporates the real-time rendering of 3DGS, video diffusion priors to ...

- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we introduce ExploreGS, a pipeline that enables explorable scene reconstruction using diffusion priors and 3DGS.
- **p. 3 / 3.2. Scene initialization - extractive PDF cue:** To this end, we introduce a simple rasterization-based algorithm to construct the occupancy grid O ∈RS×S×S.
- **p. 3 / 3.3. Virtual view sampling - extractive PDF cue:** After initializing the target scene, our method utilizes video diffusion priors to supplement the missing information from 27044
- **p. 1 / 1. Introduction - extractive PDF cue:** This advancement has been further accelerated by recent 3D Gaussian Splatting (3DGS) [11], which enables highquality rendering in real-time.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | In addition, extending the scene bounding box to cover a large scale scene would be an interesting avenue ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Gridbased approach often fails to maximize information gain, as it includes the gain from free space, resulting in ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization), p. 2 (1. Introduction), p. 2 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
