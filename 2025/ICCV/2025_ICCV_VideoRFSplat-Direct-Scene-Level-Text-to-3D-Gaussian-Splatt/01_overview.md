# VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, geometry, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 These pose fundamental challenges to developing generative models for direct 3DGS generation, introducing difficulties distinct from object-level generation.를 문제로 두고, Furthermore, we propose an asynchronous adaptation of Classifier-Free Guidance (CFG) that enables the clearer pose to better guide multi-view image generation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose VideoRFSplat, a direct text-to-3D model leveraging a video generation model to generate realistic 3D Gaussian Splatting (3DGS) for unbounded real-world scenes.
- **p. 1 / Abstract - extractive body cue:** To generate diverse camera poses and unbounded spatial extent of real-world scenes, while ensuring generalization to arbitrary text prompts, previous methods fine-tune 2D generative models ...
- **p. 1 / Abstract - extractive body cue:** However, these methods suffer from instability when extending 2D generative models to joint modeling due to the modality gap, which necessitates additional models to stabilize ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose an architecture and a sampling strategy to jointly model multi-view images and camera poses when fine-tuning a video genera
- **p. 1 / Abstract - extractive body cue:** Our core idea is a dual-stream architecture that attaches a dedicated pose generation model alongside a pretrained video generation model via communication blocks, generating multi-view ...
- **p. 2 / 1. Introduction - extractive body cue:** These pose fundamental challenges to developing generative models for direct 3DGS generation, introducing difficulties distinct from object-level generation.
- **p. 2 / 1. Introduction - extractive body cue:** However, prior works [20, 34, 35] have suffered from instability in extending 2D generative models to joint modeling due to the modality gap, hindering high-quality ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose an asynchronous adaptation of Classifier-Free Guidance (CFG) that enables the clearer pose to better guide multi-view image generation.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, to eliminate external dependency, we present VideoRFSplat, a direct 3DGS generation model that introduces an architecture and sampling strategy for jointly generating ...
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To reduce interference, we propose a dual-stream architecture with dedicated submodules for pose and image generation, communicating via cross-attention at intermediate layers (see Fig.
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To address this, we propose an asynchronous timestep strategy, decoupling the timesteps of pose and multi-view generation modules and enabling one modality to denoise faster, ...
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** This exchange enables controlled interaction between the two models while preserving their specialized forward paths and reducing interference between pose and multi-view modalities.
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** The pose generation model adopts a transformer-based architecture [69, 71], explicitly conditioned on textual prompts and pose-specific timestep to generate camera rays [87], forming a ...
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To enable this, we use the following loss: ~\l ab el {eq : time ste p_ los s } \math cal {L }_{ ours} := ...
- **p. 8 / Method - extractive body cue:** For evaluation, we use 1000 sequences from RealEstate10K [93] with extracted camera trajectories and captions to generate images.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We hypothesize that uncertainty in early sampling leads to unstable pose-image interactions, destabilizing camera pose generation and ultimately degrading multi-view image quality. | conditioning observation와 noisy/intermediate sample | p. 8 (Method), p. 2 (1. Introduction) |
| State/latent | hypothesize, uncertainty, early, sampling, leads, unstable, pose-image, interactions, destabilizing, camera, pose, generation | latent/noise variable와 conditional distribution | p. 8 (Method), p. 2 (1. Introduction), p. 8 (Method) |
| Output/action | This approach is motivated by our observation that synchronized denoising of multi-view images and camera poses, particularly at early timesteps, leads to mutual ambiguity, increasing uncertainty and causing unstable generation. | generated sample, action chunk 또는 trajectory | p. 2 (1. Introduction), p. 8 (Method), p. 4 (4.1. Dual-Stream Pose-Video Joint Model) |
| Objective/outcome | This loss enables vector field prediction even with different timesteps for pose and image modalities. | distribution fit, multimodality, sample quality와 latency | p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose an asynchronous adaptation of Classifier-Free Guidance (CFG) that enables the clearer pose to better guide multi-view image generation.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, to eliminate external dependency, we present VideoRFSplat, a direct 3DGS generation model that introduces an architecture and sampling strategy for jointly generating ...
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To reduce interference, we propose a dual-stream architecture with dedicated submodules for pose and image generation, communicating via cross-attention at intermediate layers (see Fig.
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To address this, we propose an asynchronous timestep strategy, decoupling the timesteps of pose and multi-view generation modules and enabling one modality to denoise faster, ...
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** This exchange enables controlled interaction between the two models while preserving their specialized forward paths and reducing interference between pose and multi-view modalities.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative results on MVImgNet [84] and DL3DV [41] validation sets. VideoRFSplat achieves the higher performance across all metrics without SDS++ refinement. sess image ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. VideoRFSplat outperforms other methods in FID-8K (43.07), translation error (0.063), rotation error (0.4223), and CLIPScore (31.1). These results confirm that VideoRFSplat generates images ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Results on camera conditioned generation. VideoRFS- plat can perform camera-conditioned generation. models under identical conditions for 60K iterations with Mochi [69] and then ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | Following previous works [20, 35], we evaluate our model on the MVImgNet and DL3DV validation datasets, as well as the T3Bench benchmark [23]. | hardware/simulator version and reset protocol | p. 6 (5.1. Experimental Setups), p. 6 (5.1. Experimental Setups) |
| Dataset/benchmark | Following previous works [20, 35], we evaluate our model on the MVImgNet and DL3DV validation datasets, as well as the T3Bench benchmark [23]. | role, split, size and leakage | p. 6 (5.1. Experimental Setups), p. 6 (5.1. Experimental Setups) |
| Metric | Table 5. VideoRFSplat outperforms other methods in FID-8K (43.07), translation error (0.063), rotation error (0.4223), and CLIPScore (31.1). These results confirm that VideoRFSplat generates images following camera trajectories. Qualita ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Baseline/ablation | Table 1. Quantitative results on T3Bench [23]. VideoRFSplat outperforms all baselines without SDS++ refinement. | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 5 (5. Experimental Results), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Failure analysis of synchronized sampling and the effectiveness of asynchronous sampling. (Left) Early in sampling (t > 0.85), synchronous sampling induces excessive oscillations ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Architecture Comparison. For each example, Left: chan- nel concat architecture (SplatFlow). Right: our architecture. framed key objects. We hypothesize that uncertainty in early ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Asynchrnous schedule (δ = 0.2). During sampling, we denoise the pose modality faster than im- ages, as it is robust to fast denoising. ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 These pose fundamental challenges to developing generative models for direct 3DGS generation, introducing difficulties distinct from object-level generation.를 문제로 두고, Furthermore, we propose an asynchronous adaptation of Classifier-Free Guidance (CFG) that enables the clearer pose to better guide multi-view image generation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
