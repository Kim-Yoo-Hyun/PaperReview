# Problem - RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** High-fidelity 3D scene reconstruction plays a crucial role in autonomous driving by enabling novel data generation from existing datasets.
- **p. 1 / Abstract - extractive body cue:** This allows simulating safety-critical scenarios and augmenting training datasets without incurring further data collection costs.
- **p. 1 / Abstract - extractive body cue:** While recent advances in radiance fields have demonstrated promising results in 3D reconstruction and sensor data synthesis using cameras and LiDAR, their potential for radar ...
- **p. 1 / Abstract - extractive body cue:** Radar is crucial for autonomous driving due to its robustness in adverse weather conditions like rain, fog, and snow, where optical sensors often struggle.
- **p. 1 / Abstract - extractive body cue:** Although the state-of-the-art radar-based neural representation shows promise for 3D driving scene reconstruction, it performs poorly in scenarios with significant radar noise, including receiver saturation ...
- **p. 1 / 1. Introduction - extractive body cue:** Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.
- **p. 2 / 1. Introduction - extractive body cue:** While Radar Fields demonstrates encouraging results, due to the lack of noise modeling, it can only synthesize preprocessed, noise-excluded radar images, making realistic radar data ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Additionally, Locc corresponds to the L1 error between the rendered occupancy state Iα output by RadarSplat and the initial occupancy map Iocc ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Additionally, Locc, corresponds, error, between, rendered, occupancy, state, output, RadarSplat | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | frequency, domain, output, discrete, Fourier, transform, index, observation | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Additionally, Locc, corresponds, error, between, rendered, occupancy, state, output, RadarSplat | p. 6 (3.6. Training Losses), p. 6 (3.5.2. Rendering with Azimuth Projection), p. 4 (3.2. Multipath and Saturation Noise Detection) |
| Decision / output variable | geometry/map/query r; body terms: account, radar, noise, detection, Sec, scene, reconstruction, present | p. 3 (3. Methods), p. 3 (3. Methods), p. 5 (3.4. Denoising and Occupancy Map Pre-processing) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: rendering, equation, defined, R4n, Note, wavelength, general, loss | p. 5 (3.5.1. Rendering with Elevation Projection), p. 3 (3. Methods), p. 3 (3. Methods), p. 4 (3.2. Multipath and Saturation Noise Detection), p. 5 (3.5. Radar Gaussian Splatting), p. 6 (3.6. Training Losses) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Methods), p. 3 (3. Methods), p. 4 (3.2. Multipath and Saturation Noise Detection) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.3. Occupancy State Estimation), p. 8 (4.4. Ablation Studies), p. 6 (4.3. Occupancy State Estimation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** While Radar Fields demonstrates encouraging results, due to the lack of noise modeling, it can only synthesize preprocessed, noise-excluded radar images, making realistic radar data ...
- **p. 1 / 1. Introduction - extractive body cue:** Real-world data collection to train models is time-consuming and prohibitively expensive, while developing realistic sensor simulations during real-world driving scenarios is hindered by the persistent ...

## What the Paper Changes

PDF body contribution framing (p. 3 (3. Methods), p. 3 (3. Methods), p. 5 (3.4. Denoising and Occupancy Map Pre-processing), p. 5 (3.4. Denoising and Occupancy Map Pre-processing), p. 2 (1. Introduction)): To account for radar noise, we propose a noise detection method (Sec.

- **p. 3 / 3. Methods - extractive body cue:** For scene reconstruction, we present a radar model that renders radar images from 3D Gaussians based on radar physics (Sec.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** Our method produces a clear denoised image, whereas Radar Fields struggles with multipath effects.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** We propose a denoising algorithm that removes noise across detected noisy azimuth angles, θnoise ∈Θsat ∪Θmulti, identified in Sec.
- **p. 2 / 1. Introduction - extractive body cue:** This enables more realistic radar image synthesis and improved 3D geometry estimation compared to [5], as shown in Figure 1.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | RadarSplat also fails to model other noises when disabling the proposed noise probability. reconstruction. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This enables radar inverse rendering for radar signal decomposition, high-fidelity radar data synthesis, and robust noise-free occupancy prediction. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 6. Our proposed radar image denoising method preserves rich information while remaining robust to multipath effects. In ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (3.6. Training Losses), p. 6 (3.5.2. Rendering with Azimuth Projection), p. 4 (3.2. Multipath and Saturation Noise Detection), p. 4 (3.2. Multipath and Saturation Noise Detection). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 6 (3.6. Training Losses), p. 6 (3.5.2. Rendering with Azimuth Projection), p. 4 (3.2. Multipath and Saturation Noise Detection), p. 4 (3.2. Multipath and Saturation Noise Detection), objective p. 5 (3.5.1. Rendering with Elevation Projection), p. 3 (3. Methods), p. 3 (3. Methods), p. 4 (3.2. Multipath and Saturation Noise Detection), p. 5 (3.5. Radar Gaussian Splatting), p. 6 (3.6. Training Losses).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
