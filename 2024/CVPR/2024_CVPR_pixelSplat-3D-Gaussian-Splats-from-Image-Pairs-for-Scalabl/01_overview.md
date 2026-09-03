# pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In contrast, in the generalizable case, we need to back-propagate gradients through the representation and thus cannot rely on non-differentiable operations.를 문제로 두고, Our method consists of a two-view image encoder and a pixel-aligned Gaussian prediction module.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce pixelSplat, a feed-forward model that learns to reconstruct 3D radiance fields parameterized by 3D Gaussian primitives from pairs of images.
- **p. 1 / Abstract - extractive body cue:** Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time.
- **p. 1 / Abstract - extractive body cue:** To overcome local minima inherent to sparse and locally supported representations, we predict a dense probability distribution over 3D and sample Gaussian means from that ...
- **p. 1 / Abstract - extractive body cue:** We make this sampling operation differentiable via a reparameterization trick, allowing us to back-propagate gradients through the Gaussian splatting representation.
- **p. 1 / Abstract - extractive body cue:** We benchmark our method on wide-baseline novel view synthesis on the real-world RealEstate10k and ACID datasets, where we outperform state-of-the-art light field transformers and accelerate ...
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, in the generalizable case, we need to back-propagate gradients through the representation and thus cannot rely on non-differentiable operations.
- **p. 2 / 1. Introduction - extractive body cue:** We significantly outperform previous black-box based light field transformers on the real-world ACID and RealEstate10k datasets while drastically reducing both training and rendering cost and ...

## Core Idea

- **p. 3 / 4. Image-conditioned 3D Gaussian Inference - extractive body cue:** Our method consists of a two-view image encoder and a pixel-aligned Gaussian prediction module.
- **p. 1 / 1. Introduction - extractive body cue:** We present pixelSplat, which brings the benefits of a primitive-based 3D representation-fast and memoryefficient rendering as well as interpretable 3D structureto generalizable view synthesis.
- **p. 2 / 1. Introduction - extractive body cue:** We demonstrate the efficacy of our method by showcasing, for the first time, how a 3D Gaussian splatting representation can be predicted in a single ...
- **p. 1 / Abstract - extractive body cue:** We benchmark our method on wide-baseline novel view synthesis on the real-world RealEstate10k and ACID datasets, where we outperform state-of-the-art light field transformers and accelerate ...
- **p. 3 / 4. Image-conditioned 3D Gaussian Inference - extractive body cue:** We present pixelSplat, a Gaussian-based generalizable novel view synthesis model.
- **p. 1 / Abstract - extractive body cue:** Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time.
- **p. 4 / 4.1. Resolving Scale Ambiguity - extractive body cue:** Note that for brevity, we use h to represent the function that computes depths from bucket indices (see equations 6 and 7). date per-pixel features ...
- **p. 3 / 4.1. Resolving Scale Ambiguity - extractive body cue:** We first encode each view separately into feature volumes F and ˜F via a per-image feature encoder.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We investigate the problem of generalizable novel view synthesis from sparse image observations. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | investigate, problem, generalizable, novel, view, synthesis, sparse, image, observations, Given, pair, input | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (4.1. Resolving Scale Ambiguity) |
| Output/action | Given a pair of input images, pixelSplat reconstructs a 3D radiance field parameterized via 3D Gaussian primitives. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 4 (4.1. Resolving Scale Ambiguity), p. 3 (4.1. Resolving Scale Ambiguity) |
| Objective/outcome | This means that in each backward pass, we assign the gradients of the loss L with respect to the opacities α to the gradients of the depth probability buckets ϕ, i.e., ∇ϕL ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.2. Gaussian Parameter Prediction), p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / 4. Image-conditioned 3D Gaussian Inference - extractive body cue:** Our method consists of a two-view image encoder and a pixel-aligned Gaussian prediction module.
- **p. 1 / 1. Introduction - extractive body cue:** We present pixelSplat, which brings the benefits of a primitive-based 3D representation-fast and memoryefficient rendering as well as interpretable 3D structureto generalizable view synthesis.
- **p. 2 / 1. Introduction - extractive body cue:** We demonstrate the efficacy of our method by showcasing, for the first time, how a 3D Gaussian splatting representation can be predicted in a single ...
- **p. 1 / Abstract - extractive body cue:** We benchmark our method on wide-baseline novel view synthesis on the real-world RealEstate10k and ACID datasets, where we outperform state-of-the-art light field transformers and accelerate ...
- **p. 3 / 4. Image-conditioned 3D Gaussian Inference - extractive body cue:** We present pixelSplat, a Gaussian-based generalizable novel view synthesis model.
- **p. 6 / 5.2. Results - extractive body cue:** Our method outperforms the baselines on all metrics, with especially significant improvements in perceptual distance (LPIPS).
- **p. 8 / 5.3. Ablations and Analysis - extractive body cue:** Qualitatively, this produces ghosting and motion blur artifacts that are evidence of incorrect depth predictions; quantitatively, performance drops significantly.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons. We outperform all baseline methods in terms PSNR, LPIPS, and SSIM for novel view synthesis on the real-world RealEstate10k and ACID ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5.2. Results), p. 8 (5.3. Ablations and Analysis) |
| Embodiment/environment | Both datasets include camera poses computed by SfM software, necessitating the scale-aware design discussed in Section 4.1. | hardware/simulator version and reset protocol | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup) |
| Dataset/benchmark | Qualitative comparison of novel views on the RealEstate10k (top) and ACID (bottom) test sets. | role, split, size and leakage | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 7 (5.2. Results), p. 8 (5.3. Ablations and Analysis) |
| Metric | In Figure 6, we visualize epipolar attention scores, demonstrating that our epipolar transformer successfully discovers cross-view correspondences. | definition, denominator, direction and uncertainty | p. 8 (5.3. Ablations and Analysis), p. 6 (5.1. Experimental Setup), p. 6 (5.2. Results) |
| Baseline/ablation | Because the prior state-of-the-art wide-baseline novel view synthesis model by Du et al. | fair input/data/compute/action matching | p. 6 (5.1. Experimental Setup), p. 6 (5.2. Results), p. 7 (5.2. Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** Without our sampling approach, our model falls into local minima that manifest themselves as speckling artifacts.
- **p. 7 / 5.2. Results - extractive body cue:** Note that while the resulting Gaussians facilitate high-fidelity novel-view synthesis for in-distribution camera poses, they suffer from the same failure modes as 3D Gaussians optimized ...
- **p. 8 / 6. Conclusion - extractive body cue:** An exciting avenue for future work is to leverage our model for generative modeling by combining it with diffusion models [48, 51] or to remove ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Scale ambiguity. SfM does not reconstruct camera poses in real-world, metric scale-poses are scaled by an arbitrary scale factor that is different for ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** To evaluate visual fidelity, we compare each method's rendered images to the corresponding ground-truth frames by computing a peak signal-to-noise ratio (PSNR), structural similarity index ...
- **p. 7 / 5.2. Results - extractive body cue:** Specifically, reflective surfaces are often transparent, and Gaussians appear billboard-like when viewed from out-of-distribution views.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In contrast, in the generalizable case, we need to back-propagate gradients through the representation and thus cannot rely on non-differentiable operations.를 문제로 두고, Our method consists of a two-view image encoder and a pixel-aligned Gaussian prediction module.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (Abstract), p. 3 (4. Image-conditioned 3D Gaussian Inference), p. 4 (4.1. Resolving Scale Ambiguity) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
