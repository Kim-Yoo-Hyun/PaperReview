# RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.를 문제로 두고, To account for radar noise, we propose a noise detection method (Sec.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** High-fidelity 3D scene reconstruction plays a crucial role in autonomous driving by enabling novel data generation from existing datasets.
- **p. 1 / Abstract - extractive body cue:** This allows simulating safety-critical scenarios and augmenting training datasets without incurring further data collection costs.
- **p. 1 / Abstract - extractive body cue:** While recent advances in radiance fields have demonstrated promising results in 3D reconstruction and sensor data synthesis using cameras and LiDAR, their potential for radar ...
- **p. 1 / Abstract - extractive body cue:** Radar is crucial for autonomous driving due to its robustness in adverse weather conditions like rain, fog, and snow, where optical sensors often struggle.
- **p. 1 / Abstract - extractive body cue:** Although the state-of-the-art radar-based neural representation shows promise for 3D driving scene reconstruction, it performs poorly in scenarios with significant radar noise, including receiver saturation ...
- **p. 1 / 1. Introduction - extractive body cue:** Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.
- **p. 2 / 1. Introduction - extractive body cue:** While Radar Fields demonstrates encouraging results, due to the lack of noise modeling, it can only synthesize preprocessed, noise-excluded radar images, making realistic radar data ...

## Core Idea

- **p. 3 / 3. Methods - extractive body cue:** To account for radar noise, we propose a noise detection method (Sec.
- **p. 3 / 3. Methods - extractive body cue:** For scene reconstruction, we present a radar model that renders radar images from 3D Gaussians based on radar physics (Sec.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** Our method produces a clear denoised image, whereas Radar Fields struggles with multipath effects.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** We propose a denoising algorithm that removes noise across detected noisy azimuth angles, θnoise ∈Θsat ∪Θmulti, identified in Sec.
- **p. 2 / 1. Introduction - extractive body cue:** This enables more realistic radar image synthesis and improved 3D geometry estimation compared to [5], as shown in Figure 1.
- **p. 6 / 3.6. Training Losses - extractive body cue:** To refine the model, we introduce two regularization losses.
- **p. 5 / 3.5. Radar Gaussian Splatting - extractive body cue:** Next, we introduce our rendering pipeline, which incorporates elevation and azimuth projection along with spectral leakage modeling.
- **p. 6 / 3.6. Training Losses - extractive body cue:** Additionally, Locc corresponds to the L1 error between the rendered occupancy state Iα output by RadarSplat and the initial occupancy map Iocc estimated in the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Additionally, Locc corresponds to the L1 error between the rendered occupancy state Iα output by RadarSplat and the initial occupancy map Iocc estimated in the preprocessing step to aid in training. λi ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3.6. Training Losses), p. 6 (3.5.2. Rendering with Azimuth Projection) |
| State/latent | Additionally, Locc, corresponds, error, between, rendered, occupancy, state, output, RadarSplat, initial, Iocc | geometry, map, object/relationship state | p. 6 (3.6. Training Losses), p. 6 (3.5.2. Rendering with Azimuth Projection), p. 4 (3.2. Multipath and Saturation Noise Detection) |
| Output/action | Azimuth projection is then applied via a 1D convolution along the azimuth axis with kernel size 2Q and stride size Q, and a kernel weighted by the azimuth antenna profile, Gθ(θ), producing ... | point map, pose, scene graph, affordance 또는 query result | p. 6 (3.5.2. Rendering with Azimuth Projection), p. 4 (3.2. Multipath and Saturation Noise Detection), p. 4 (3.2. Multipath and Saturation Noise Detection) |
| Objective/outcome | The rendering equation is defined as: Pr(θ, n) = i X ϕi Pt · G(ϕi)2 · σi (4π)3R4n (11) Note that the wavelength, λ, and the general loss factor, L, in Eq. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.5.1. Rendering with Elevation Projection), p. 5 (3.5. Radar Gaussian Splatting), p. 6 (3.6. Training Losses) |

## Main Claims and Actual Contribution

- **p. 3 / 3. Methods - extractive body cue:** To account for radar noise, we propose a noise detection method (Sec.
- **p. 3 / 3. Methods - extractive body cue:** For scene reconstruction, we present a radar model that renders radar images from 3D Gaussians based on radar physics (Sec.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** Our method produces a clear denoised image, whereas Radar Fields struggles with multipath effects.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** We propose a denoising algorithm that removes noise across detected noisy azimuth angles, θnoise ∈Θsat ∪Θmulti, identified in Sec.
- **p. 2 / 1. Introduction - extractive body cue:** This enables more realistic radar image synthesis and improved 3D geometry estimation compared to [5], as shown in Figure 1.
- **p. 6 / 4.2. Novel Radar View Rendering - extractive body cue:** With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× better in SSIM ...
- **p. 7 / 4.3. Occupancy State Estimation - extractive body cue:** The results indicate that RadarSplat achieves accurate 3D reconstruction similar to LiDAR, by taking only 2D noisy radar images as input.
- **p. 7 / 4.3. Occupancy State Estimation - extractive body cue:** The proposed method outperforms Radar Fields across all metrics, achieving better reconstruction by reducing RMSE by 1.22 m and improving accuracy more than 1.5× compared ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation) |
| Embodiment/environment | Image synthesis and geometry reconstruction evaluation on Boreas dataset [7]. | hardware/simulator version and reset protocol | p. 6 (4.3. Occupancy State Estimation), p. 6 (4.3. Occupancy State Estimation) |
| Dataset/benchmark | In the rain and night scenes, the camera is either blurred due to raindrops or has limited visibility due to low illumination. | role, split, size and leakage | p. 6 (4.3. Occupancy State Estimation), p. 6 (4.3. Occupancy State Estimation), p. 8 (4.5. Adverse Weather and Lighting Conditions), p. 7 (4.4. Ablation Studies) |
| Metric | To assess the quality of occupancy estimation, we report the RMSE, Relative Chamfer Distance (R-CD), and Accuracy. | definition, denominator, direction and uncertainty | p. 6 (4.3. Occupancy State Estimation), p. 8 (4.4. Ablation Studies), p. 6 (4.3. Occupancy State Estimation) |
| Baseline/ablation | With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× better in SSIM score. | fair input/data/compute/action matching | p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation), p. 7 (4.3. Occupancy State Estimation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Novel Radar View Rendering - extractive body cue:** In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** RadarSplat also fails to model other noises when disabling the proposed noise probability. reconstruction.
- **p. 8 / 5. Conclusion - extractive body cue:** This enables radar inverse rendering for radar signal decomposition, high-fidelity radar data synthesis, and robust noise-free occupancy prediction.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Our proposed radar image denoising method preserves rich information while remaining robust to multipath effects. In contrast, the dynamic threshold approach used in ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Three types of radar noise of scanning radar highlighted in a raw radar image in polar space (bottom) and Cartesian space (top). The ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. System Overview. RadarSplat takes radar images and poses as input. The preprocessing step includes noise detection and initial occupancy mapping. The multipath source ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Range-power signal and its FFT of a radar azimuth beam with multipath effects. The constant and peak magnitude in the FFT results are ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.를 문제로 두고, To account for radar noise, we propose a noise detection method (Sec.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 6 (3.6. Training Losses), p. 5 (3.4. Denoising and Occupancy Map Pre-processing), p. 5 (3.5. Radar Gaussian Splatting) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
