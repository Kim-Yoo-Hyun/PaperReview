# DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This limitation is further amplified in egocentric videos, a rapidly growing data source that introduces unique challenges for 3D scene reconstruction[7, 16, 29, 32, 41].를 문제로 두고, In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • Our proposed method achieves ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Reconstructing clean, distractor-free 3D scenes from realworld captures remains a significant challenge, particularly in highly dynamic and cluttered settings such as egocentric videos.
- **p. 1 / Abstract - extractive body cue:** To tackle this problem, we introduce DeGauss, a simple and robust self-supervised framework for dynamic scene reconstruction based on a decoupled dynamic-static Gaussian Splatting design.
- **p. 1 / Abstract - extractive body cue:** DeGauss models dynamic elements with foreground Gaussians and static content with background Gaussians, using a probabilistic mask to coordinate their composition and enable independent yet ...
- **p. 1 / Abstract - extractive body cue:** DeGauss generalizes robustly across a wide range of real-world scenarios, from casual image collections to long, dynamic egocentric videos, without relying on complex heuristics or ...
- **p. 1 / Abstract - extractive body cue:** Experiments on benchmarks including NeRF-on-the-go, ADT, AEA, Hot3D, and EPIC-Fields demonstrate that DeGauss consistently outperforms existing methods, establishing a strong baseline for generalizable, distractor-free 3D ...
- **p. 1 / 1. Introduction - extractive body cue:** This limitation is further amplified in egocentric videos, a rapidly growing data source that introduces unique challenges for 3D scene reconstruction[7, 16, 29, 32, 41].
- **p. 1 / 1. Introduction - extractive body cue:** These factors introduce significant challenges for This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • ...
- **p. 2 / 1. Introduction - extractive body cue:** We show that our method achieves superior results compared to baseline dynamic scene modeling approaches, with notable advantages across diverse datasets [13, 21].
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** To address this, we introduce a brightness control mask that enhances the background branch's capacity to model non-Lambertian effects.
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** Our method simultaneously reconstructs the 3D scene and learns an unsupervised decomposition into decoupled static background and dynamic foreground branches, where the update is loosely ...
- **p. 5 / 3.6. Unsupervised scene decomposition - extractive body cue:** Our method offers significantly greater robustness in handling local minimas.
- **p. 3 / 3.2. Foreground deformable gaussian - extractive body cue:** The spatial-temporal module comprises an encoder H and a decoder D.
- **p. 3 / 3.2. Foreground deformable gaussian - extractive body cue:** The encoder, based on Hexplane [3], extracts spatio-temporal features based on reference time t with fd = H(Gf, t), and the multi-head decoder D predicts ...
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** This decoupled formulation guarantee flexible yet accurate scene decomposition result. appearance modeling.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • Our proposed method achieves ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control) |
| State/latent | summary, contributions, DeGauss, decoupled, foregroundbackground, design, leverages, dynamic-static, Gaussian, splatting, robust, generalizable | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control), p. 2 (1. Introduction) |
| Output/action | SH Attributes Foreground Render Probabilistic Mask Brightness Control Background Render Controlled Background Composed Render Input Image Activation Rasterize Mask Rasterize Rasterize Foreground Gaussians Background Gaussians Mask Attri ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.4. Background Brightness Control), p. 2 (1. Introduction), p. 5 (3.6. Unsupervised scene decomposition) |
| Objective/outcome | (11) While both main loss Lmain and utility loss Luti are used for optimizable parameters' update, only the gradient magnitude of Lmain are used to densify foreground and background gaussians. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.7. Loss function), p. 5 (3.7. Loss function), p. 4 (3.4. Background Brightness Control) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • ...
- **p. 2 / 1. Introduction - extractive body cue:** We show that our method achieves superior results compared to baseline dynamic scene modeling approaches, with notable advantages across diverse datasets [13, 21].
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** To address this, we introduce a brightness control mask that enhances the background branch's capacity to model non-Lambertian effects.
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** Our method simultaneously reconstructs the 3D scene and learns an unsupervised decomposition into decoupled static background and dynamic foreground branches, where the update is loosely ...
- **p. 5 / 3.6. Unsupervised scene decomposition - extractive body cue:** Our method offers significantly greater robustness in handling local minimas.
- **p. 7 / 4.3. Results - extractive body cue:** Notably, our method consistently achieves significantly better LPIPS scores over the previous SOTA method SpotlessSplats [24].
- **p. 7 / 4.3. Results - extractive body cue:** 2, where our methods achieve consistently better LPIPS scores.
- **p. 5 / 4.3. Results - extractive body cue:** To assess the performance of our method for the distractorfree scene reconstruction task in the presence of noisy inputs, we conduct evaluations on both egocentric ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Results), p. 7 (4.3. Results) |
| Embodiment/environment | HyperNeRF Dataset [21] features real-world activities captured with smooth trajectories. | hardware/simulator version and reset protocol | p. 5 (4.2. Datasets), p. 7 (4.3. Results) |
| Dataset/benchmark | Distractor free scene reconstruction on NeRF On-the-go Dataset[22].The best , second best , and third best are highlighted. ‡: ±0.005 SSIM and LPIPS due to rounding uncertainty of originally reported result. | role, split, size and leakage | p. 5 (4.2. Datasets), p. 7 (4.3. Results), p. 6 (4.3. Results), p. 5 (4.2. Datasets) |
| Metric | 2, where our methods achieve consistently better LPIPS scores. | definition, denominator, direction and uncertainty | p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (4.2. Datasets) |
| Baseline/ablation | Compared to baseline methods [10, 24, 31], our method models high-quality distractor-free static background with accurate foreground separation. | fair input/data/compute/action matching | p. 6 (4.3. Results), p. 7 (4.3. Results), p. 6 (4.3. Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting.
- **p. 7 / 4.3. Results - extractive body cue:** We show our method robustly handles occlusion and reconstructs fine static details compared to SpotlessSplats [24]in Fig.
- **p. 7 / 4.3. Results - extractive body cue:** Our method robustly handles various challenges, preserving clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference test views, we report detailed per-scene metrics ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Compared to SpotlessSplats [24], which is constrained by initialization and overfit to floaters. Our method offers signifi- cantly greater robustness in handling local ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This limitation is further amplified in egocentric videos, a rapidly growing data source that introduces unique challenges for 3D scene reconstruction[7, 16, 29, 32, 41].를 문제로 두고, In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • Our proposed method achieves ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control), p. 3 (3.2. Foreground deformable gaussian) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
