# Problem - DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries)): Earlier works [1, 11, 42] focus on utilizing solely event-based data, lacking the capacity to preserve color information.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Reconstructing sharp 3D representations from blurry multi-view images is a long-standing problem in computer vision.
- **p. 1 / Abstract - extractive body cue:** Recent works attempt to enhance high-quality novel view synthesis from the motion blur by leveraging eventbased cameras, benefiting from high dynamic range and microsecond temporal ...
- **p. 1 / Abstract - extractive body cue:** However, they often reach sub-optimal visual quality in either restoring inaccurate color or losing fine-grained details.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present DiET-GS, a diffusion prior and event streamassisted motion deblurring 3DGS.
- **p. 1 / Abstract - extractive body cue:** Our framework effectively leverages blur-free event streams and diffusion prior in a two-stage training strategy.
- **p. 1 / 1. Introduction - extractive body cue:** Earlier works [1, 11, 42] focus on utilizing solely event-based data, lacking the capacity to preserve color information.
- **p. 2 / 1. Introduction - extractive body cue:** However, most of these existing works still rely on blurry images alone to recover accurate color, often resulting in unwanted color artifacts.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Earlier works [1, 11, 42] focus on utilizing solely event-based data, lacking the capacity to preserve color information. | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | Based on the latent image I, a sharp latent image Ii at a randomly sampled timestep ti can be recovered by warping ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF body |
| State / latent | latent, image, sharp, randomly, sampled, timestep, recovered, warping, stated, initialization | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | UNet, backbone, pretrained, diffusion, model, takes, input, ground | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: latent, image, sharp, randomly, sampled, timestep, recovered, warping, stated, initialization | p. 4 (4. Our Method), p. 5 (4. Our Method), p. 5 (4. Our Method) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: Once, optimized, capable, recovering, well-defined, details, accurate, color | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: Jointly, optimizing, constraints, reaches, equilibrium, between, scene-specific, details | p. 5 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method), p. 4 (4. Our Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method) |
| Success / guarantee | sample quality, diversity and latency | p. 6 (Figure/Table caption), p. 6 (5.1. Implementation Details), p. 7 (5.3. Experiment Settings) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** However, most of these existing works still rely on blurry images alone to recover accurate color, often resulting in unwanted color artifacts.
- **p. 1 / 1. Introduction - extractive body cue:** Given a set of blurry images and corresponding event streams, we propose a novel framework to construct deblurring 3DGS by jointly leveraging the EDI [33] ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose DiET-GS, a Diffusion prior and EvenT stream-assisted motion deblurring 3DGS.
- **p. 3 / 3. Preliminaries - extractive body cue:** Given the predicted denoised latent ˆzt-1 from zt and the current noised latent zt-1 at timestep t -1, the ob21741

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Our Method), p. 1 (1. Introduction)): Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that our framework significantly surpasses the ...

- **p. 1 / 1. Introduction - extractive body cue:** Given a set of blurry images and corresponding event streams, we propose a novel framework to construct deblurring 3DGS by jointly leveraging the EDI [33] ...
- **p. 2 / 1. Introduction - extractive body cue:** To restore both accurate color and well-defined details, we introduce a novel framework that uses the EDI prior to achieve 1) fine-grained details, 2) accurate ...
- **p. 4 / 4. Our Method - extractive body cue:** To this end, we propose a novel optimization problem that leverages EDI prior to further constrain the 3DGS in terms of 1) fine-grained details, 2) ...
- **p. 1 / 1. Introduction - extractive body cue:** Our DiET-GS++ enables highquality novel-view synthesis by recovering precise color and welldefined details from the blurry multi-view images. tured and free from any artifact.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get noised latents ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Finally, given ˆC as conditional input, the UNet backbone of pretrained diffusion model predicts the noise residual of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We employ three standard metrics: Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM), and VGG-based Learned Perceptual ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4. Our Method), p. 5 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), interface p. 4 (4. Our Method), p. 5 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method), objective p. 5 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method), p. 4 (4. Our Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
