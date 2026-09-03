# Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Schwarz_Generative_Gaussian_Splatting_Generating_3D_Scenes_with_Video_Diffusion_Priors_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Schwarz_Generative_Gaussian_Splatting_Generating_3D_Scenes_with_Video_Diffusion_Priors_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Schwarz_Generative_Gaussian_Splatting_Generating_3D_Scenes_with_Video_Diffusion_Priors_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Schwarz_Generative_Gaussian_Splatting_Generating_3D_Scenes_with_Video_Diffusion_Priors_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, these works cannot leverage pre-trained video diffusion models, because of their custom network architectures for incorporating the 3D representation.를 문제로 두고, We summarize our main contributions as follows: • We propose an approach that directly integrates an explicit 3D representation with a pre-trained latent video diffusion backbone, thereby improving 3D consistency of the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Synthesizing consistent and photorealistic 3D scenes is an open problem in computer vision.
- **p. 1 / Abstract - extractive body cue:** Video diffusion models generate impressive videos but cannot directly synthesize 3D representations, i.e., lack 3D consistency in the generated sequences.
- **p. 1 / Abstract - extractive body cue:** In addition, directly training generative 3D models is challenging due to a lack of 3D training data at scale.
- **p. 1 / Abstract - extractive body cue:** In this work, we present Generative Gaussian Splatting (GGS) - a novel approach that integrates a 3D representation with a pre-trained latent video diffusion model.
- **p. 1 / Abstract - extractive body cue:** Specifically, our model synthesizes a feature field parameterized via 3D Gaussian primitives.
- **p. 1 / 1. Introduction - extractive body cue:** However, these works cannot leverage pre-trained video diffusion models, because of their custom network architectures for incorporating the 3D representation.
- **p. 1 / 1. Introduction - extractive body cue:** However, the generated multi-view images often lack 3D consistency, requiring carefully tailored 3D reconstruction algorithms [13, 70] or time consuming iterative procedures [76].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our main contributions as follows: • We propose an approach that directly integrates an explicit 3D representation with a pre-trained latent video diffusion ...
- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** To address this limitation, we introduce a stronger bias in the model to learn correct spatial relationships between frames.
- **p. 3 / 3. Method - extractive body cue:** We introduce Generative Gaussian Splatting (GGS) which directly synthesizes 3D-consistent scenes from one or more posed reference images.
- **p. 4 / 3.2. Integrating 3D Constraints - extractive body cue:** We introduce noise only to the latents of the target images {zl tgt,0}L l=1, while leaving the reference images noise-free.
- **p. 2 / 1. Introduction - extractive body cue:** Another interesting property of our approach is that using an explicit 3D representation like Gaussian splats supports training with additional depth supervision where available, resulting ...
- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** Similarly to PixelSplat [5], we use the epipolar transformer to correlate features along epipolar lines via attention.
- **p. 3 / 3.1. Pose-Conditional Image-To-Video Architecture - extractive body cue:** The camera encoder processes the Pl¨ucker embeddings {Pm} of the poses {pm} and outputs multi-scale camera embeddings, which are then used to condition the diffusion ...
- **p. 4 / 3.2. Integrating 3D Constraints - extractive body cue:** The images are first encoded into a latent representation {zm 0 }, which is then partitioned into K reference images and L target images.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We summarize our main contributions as follows: • We propose an approach that directly integrates an explicit 3D representation with a pre-trained latent video diffusion backbone, thereby improving 3D consistency of the ... | conditioning observation와 noisy/intermediate sample | p. 2 (1. Introduction), p. 3 (3. Method) |
| State/latent | summarize, main, contributions, follows, directly, integrates, explicit, representation, pre-trained, latent, video, diffusion | latent/noise variable와 conditional distribution | p. 2 (1. Introduction), p. 3 (3. Method), p. 2 (1. Introduction) |
| Output/action | The video model was trained with v-prediction, and conditioned on a single input image by concatenation of the reference latent to the input sequence, as proposed in [3]. | generated sample, action chunk 또는 trajectory | p. 3 (3. Method), p. 2 (1. Introduction), p. 3 (3.2. Integrating 3D Constraints) |
| Objective/outcome | This loss function minimizes the Euclidean distance between the predicted mean, µk, of each per-pixel splat and its corresponding ground truth 3D coordinate. | distribution fit, multimodality, sample quality와 latency | p. 4 (3.2. Integrating 3D Constraints), p. 3 (3.2. Integrating 3D Constraints), p. 3 (3.2. Integrating 3D Constraints) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our main contributions as follows: • We propose an approach that directly integrates an explicit 3D representation with a pre-trained latent video diffusion ...
- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** To address this limitation, we introduce a stronger bias in the model to learn correct spatial relationships between frames.
- **p. 3 / 3. Method - extractive body cue:** We introduce Generative Gaussian Splatting (GGS) which directly synthesizes 3D-consistent scenes from one or more posed reference images.
- **p. 4 / 3.2. Integrating 3D Constraints - extractive body cue:** We introduce noise only to the latents of the target images {zl tgt,0}L l=1, while leaving the reference images noise-free.
- **p. 2 / 1. Introduction - extractive body cue:** Another interesting property of our approach is that using an explicit 3D representation like Gaussian splats supports training with additional depth supervision where available, resulting ...
- **p. 6 / 4.1. Scene Synthesis From a Single Image - extractive body cue:** On RealEstate10K, our approach significantly improves image quality and 3D consistency over the baselines.
- **p. 8 / 4.3. Autoregressive Scene Synthesis - extractive body cue:** With improved consistency, floating artifacts in the reconstructions are significantly reduced (see also Fig.
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive body cue:** Our approach achieves similar results on RealEstate10K but does not reach the same reconstruction quality on ScanNet++.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.1. Scene Synthesis From a Single Image), p. 8 (4.3. Autoregressive Scene Synthesis) |
| Embodiment/environment | Despite the similar name, ScanNet++ features different cameras and scenes from ScanNet, allowing us to assess the generalization of our method in real-world scenarios. | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Dataset/benchmark | But ultimately, our goal is to generate high-quality 3D scenes. | role, split, size and leakage | p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.2. Scene Synthesis From Two Images), p. 6 (4.2. Scene Synthesis From Two Images) |
| Metric | Single Image to 3D: FID and FVD scores for rendered views between the generated images at 576×320 pixels. sequence lead to clearly visible artifacts in the 3D reconstruction. | definition, denominator, direction and uncertainty | p. 7 (4.2. Scene Synthesis From Two Images), p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Baseline/ablation | Baseline Comparison Given One Reference Image: We show results for the strongest baselines CameraCtrl [15] and ViewCrafter[76] together with our approach without (Ours-No3D) and with 3D representation (GGS). | fair input/data/compute/action matching | p. 7 (4.2. Scene Synthesis From Two Images), p. 6 (4.2. Scene Synthesis From Two Images), p. 5 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Table 3. To address this limitation, we introduce a stronger bias in the model to learn correct spatial relationships be- tween frames. Specifically, we integrate ...
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive body cue:** However, PixelSplat does not support view extrapolation, which is our primary objective.
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive body cue:** Our approach achieves similar results on RealEstate10K but does not reach the same reconstruction quality on ScanNet++.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Model Architecture: Our approach, GGS, directly synthesizes a 3D representation, which is parameterized by a set of Gaussian splats {gm}, from a set ...
- **p. 5 / 4. Experiments - extractive body cue:** Peak Signal-to-Noise Ratio and LPIPS [80] quantify reconstruction quality.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** Compared to the 2D decoder (GGS), the 3D decoder improves 3D consistency but moderately degrades visual fidelity.

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, these works cannot leverage pre-trained video diffusion models, because of their custom network architectures for incorporating the 3D representation.를 문제로 두고, We summarize our main contributions as follows: • We propose an approach that directly integrates an explicit 3D representation with a pre-trained latent video diffusion backbone, thereby improving 3D consistency of the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Integrating 3D Constraints), p. 3 (3.1. Pose-Conditional Image-To-Video Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
