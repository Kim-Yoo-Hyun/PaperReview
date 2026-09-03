# MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3187_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03187.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3187_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03187.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, reconstructing a 3D scene from a single image is inherently ill-posed and ambiguous, posing a significant challenge when applied to a more general and larger scene, which is the key focus ...를 문제로 두고, In this paper, we present MVSplat, a Gaussian-based feed-forward model for novel view synthesis.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** We consider the problem of 3D scene reconstruction and novel view synthesis from very sparse (i.e., as few as two) images in just one forward ...
- **p. 2 / 1 Introduction - extractive body cue:** While remarkable progress has been made using neural scene representations, e.g., Scene Representation Networks (SRN) [32], Neural Radiance Fields (NeRF) [23] and Light Filed Networks ...
- **p. 2 / 1 Introduction - extractive body cue:** Recently, 3D Gaussian Splatting (3DGS) [18] has emerged as an efficient and expressive 3D representation thanks to its fast rendering speed and high quality.
- **p. 2 / 1 Introduction - extractive body cue:** Using rasterization-based rendering, 3DGS inherently avoids the expensive volumetric sampling process of NeRF, leading to highly efficient and high-quality 3D reconstruction and novel view synthesis.
- **p. 2 / 1 Introduction - extractive body cue:** Very recently, several feed-forward Gaussian Splatting methods have been proposed to explore 3D reconstruction from sparse view images, notably Splatter Image [35] and pixelSplat [1].
- **p. 2 / 1 Introduction - extractive body cue:** However, reconstructing a 3D scene from a single image is inherently ill-posed and ambiguous, posing a significant challenge when applied to a more general and ...
- **p. 2 / 1 Introduction - extractive body cue:** Such a formulation reduces the task's learning difficulty, enabling our method to achieve state-of-the-art performance with lightweight model size and fast speed.

## Core Idea

- **p. 5 / 3 Method - extractive body cue:** In this paper, we present MVSplat, a Gaussian-based feed-forward model for novel view synthesis.
- **p. 2 / 1 Introduction - extractive body cue:** This enables the rendering of novel view images using the predicted 3D Gaussians with the differentiable splatting operation [18].
- **p. 2 / 1 Introduction - extractive body cue:** Such a formulation reduces the task's learning difficulty, enabling our method to achieve state-of-the-art performance with lightweight model size and fast speed.
- **p. 5 / 3 Method - extractive body cue:** Unlike pixelSplat [1] that predicts probabilistic depth, we develop an efficient and high-performance multi-view depth estimation model that enables unprojecting predicted depth maps as the ...
- **p. 6 / 3 Method - extractive body cue:** (4) can be ambiguous for texture-less regions, we propose to further refine it with an additional lightweight 2D U-Net [27, 28].
- **p. 5 / 3 Method - extractive body cue:** Then, we use a multi-view Transformer with selfand cross-attention layers to exchange information between different views.
- **p. 5 / 3 Method - extractive body cue:** For better efficiency, we use Swin Transformer's local window attention [22] in our Transformer architecture.
- **p. 7 / 3 Method - extractive body cue:** 3.3 Training Loss Our model predicts a set of 3D Gaussian parameters {(µj, αj, Σj, cj)}H×W ×K j=1 , which are then used for rendering ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | MVSplat 7 refinement is performed with a very lightweight 2D U-Net, which takes multiview images, features, and current depth predictions as input, and outputs perview residual depths. | RGB-D, image set, point cloud, depth와 camera pose | p. 7 (3 Method), p. 6 (3 Method) |
| State/latent | MVSplat, refinement, performed, very, lightweight, U-Net, takes, multiview, images, features, current, depth | geometry, map, object/relationship state | p. 7 (3 Method), p. 6 (3 Method), p. 5 (3 Method) |
| Output/action | The U-Net takes the concatenation of Transformer features F i and cost volume Ci as inputs, and outputs a residual ∆Ci ∈R H 4 × W 4 ×D that is added to ... | point map, pose, scene graph, affordance 또는 query result | p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |
| Objective/outcome | 2, is trained end-to-end using only a simple rendering loss for supervision. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- **p. 5 / 3 Method - extractive body cue:** In this paper, we present MVSplat, a Gaussian-based feed-forward model for novel view synthesis.
- **p. 2 / 1 Introduction - extractive body cue:** This enables the rendering of novel view images using the predicted 3D Gaussians with the differentiable splatting operation [18].
- **p. 2 / 1 Introduction - extractive body cue:** Such a formulation reduces the task's learning difficulty, enabling our method to achieve state-of-the-art performance with lightweight model size and fast speed.
- **p. 5 / 3 Method - extractive body cue:** Unlike pixelSplat [1] that predicts probabilistic depth, we develop an efficient and high-performance multi-view depth estimation model that enables unprojecting predicted depth maps as the ...
- **p. 6 / 3 Method - extractive body cue:** (4) can be ambiguous for texture-less regions, we propose to further refine it with an additional lightweight 2D U-Net [27, 28].
- **p. 12 / 4 Experiments - extractive body cue:** Note that the MVSplat significantly outperforms pixelSplat in terms of LPIPS, and the gain is larger when the domain gap between source and target datasets ...
- **p. 9 / 4 Experiments - extractive body cue:** MVSplat achieves the highest quality on novel view results even under challenging conditions, such as these regions with repeated patterns ("window frames" in 1st row), ...
- **p. 10 / 4 Experiments - extractive body cue:** 4. pixelSplat requires an extra 50,000 steps to fine-tune the Gaussians with an additional depth regularization to achieve reasonable geometry reconstruction results.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 12 (4 Experiments), p. 9 (4 Experiments) |
| Embodiment/environment | On the DTU dataset, we report results on 16 validation scenes, with 4 novel views for each scene. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | Models trained on the source dataset RealEstate10K (indoor scenes) are used to conduct zero-shot test on scenes from target datasets ACID (outdoor scenes) and DTU (object-centric scenes), without any finetuning. pixelSplat tends ... | role, split, size and leakage | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 11 (4 Experiments), p. 9 (4 Experiments) |
| Metric | The inference time and model parameters are also reported to enable thorough comparisons of speed and accuracy trade-offs. | definition, denominator, direction and uncertainty | p. 8 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments) |
| Baseline/ablation | MVSplat also produces significantly higher-quality 3D Gaussian primitives compared to the latest state-of-the-art pixelSplat [1], as demonstrated in Fig. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 13 (Figure/Table caption), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 12 / 4 Experiments - extractive body cue:** This limitation is analogous to the reason why pixelSplat performs inferior in cross-dataset generalization tests discussed earlier.
- **p. 14 / 4 Experiments - extractive body cue:** This is because our cost volume cannot find any matches in these regions, leading to poorer geometry cues.
- **p. 14 / 5 Conclusion - extractive body cue:** Besides, our model is currently trained on the RealEstate10K dataset, where its diversity is not sufficient enough to generalize robustly to in-the-wild real-world scenarios despite ...
- **p. 11 / 4 Experiments - extractive body cue:** MVSplat is inherently superior in generalizing to out-of-distribution novel scenes, primarily due to the fact that the cost volume captures the relative similarity between features, ...
- **p. 12 / 4 Experiments - extractive body cue:** This discrepancy is attributed to the reliance of pixelSplat on pure feature aggregation, which lacks robustness to changes in feature distribution.
- **p. 13 / 4 Experiments - extractive body cue:** When removing it from the "base" model, the quantitative results drop significantly: it decreases the PSNR by more than 3dB, and increases LPIPS by 0.064 ...
- **p. 13 / 4 Experiments - extractive body cue:** The variant "w/o cost volume" exhibits a direct overlay of the two input views, indicating that the 3D Gaussian parameters extracted from the two input ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, reconstructing a 3D scene from a single image is inherently ill-posed and ambiguous, posing a significant challenge when applied to a more general and larger scene, which is the key focus ...를 문제로 두고, In this paper, we present MVSplat, a Gaussian-based feed-forward model for novel view synthesis.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
