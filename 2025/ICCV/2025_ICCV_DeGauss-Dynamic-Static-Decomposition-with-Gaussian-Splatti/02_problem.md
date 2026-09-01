# Problem - DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): This limitation is further amplified in egocentric videos, a rapidly growing data source that introduces unique challenges for 3D scene reconstruction[7, 16, 29, 32, 41].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Reconstructing clean, distractor-free 3D scenes from realworld captures remains a significant challenge, particularly in highly dynamic and cluttered settings such as egocentric videos.
- **p. 1 / Abstract - extractive PDF cue:** To tackle this problem, we introduce DeGauss, a simple and robust self-supervised framework for dynamic scene reconstruction based on a decoupled dynamic-static Gaussian Splatting design.
- **p. 1 / Abstract - extractive PDF cue:** DeGauss models dynamic elements with foreground Gaussians and static content with background Gaussians, using a probabilistic mask to coordinate their composition and enable independent yet ...
- **p. 1 / Abstract - extractive PDF cue:** DeGauss generalizes robustly across a wide range of real-world scenarios, from casual image collections to long, dynamic egocentric videos, without relying on complex heuristics or ...
- **p. 1 / Abstract - extractive PDF cue:** Experiments on benchmarks including NeRF-on-the-go, ADT, AEA, Hot3D, and EPIC-Fields demonstrate that DeGauss consistently outperforms existing methods, establishing a strong baseline for generalizable, distractor-free 3D ...
- **p. 1 / 1. Introduction - extractive PDF cue:** This limitation is further amplified in egocentric videos, a rapidly growing data source that introduces unique challenges for 3D scene reconstruction[7, 16, 29, 32, 41].
- **p. 1 / 1. Introduction - extractive PDF cue:** These factors introduce significant challenges for This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This limitation is further amplified in egocentric videos, a rapidly growing data source that introduces unique challenges for 3D scene reconstruction[7, 16, ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | summary, contributions, DeGauss, decoupled, foregroundbackground, design, leverages, dynamic-static, Gaussian, splatting | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | model, dynamics, reconstruction, recent, methods, NeRF-on-the-go, WildGaussians, SpotlessSplats | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: summary, contributions, DeGauss, decoupled, foregroundbackground, design, leverages, dynamic-static, Gaussian, splatting | p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, DeGauss, decoupled, foregroundbackground, design, leverages, dynamic-static | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: While, main, loss, Lmain, utility, Luti, optimizable, parameters | p. 5 (3.7. Loss function), p. 5 (3.7. Loss function), p. 4 (3.4. Background Brightness Control), p. 4 (3.6. Unsupervised scene decomposition) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.4. Background Brightness Control), p. 4 (3.6. Unsupervised scene decomposition), p. 3 (3.3. Probabilistic Composition Mask Rasterization) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (4.2. Datasets) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** These factors introduce significant challenges for This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 2 / 1. Introduction - extractive PDF cue:** While these methods improve generalization across diverse inputs, they suffer from long training times and struggle to balance dynamic and static representations.
- **p. 2 / 1. Introduction - extractive PDF cue:** Specifically, dynamic Gaussian methods [36, 39] learn deformation fields for temporal modeling but tend to overfit to training views and generalize poorly to novel viewpoints ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control), p. 4 (3.4. Background Brightness Control), p. 5 (3.6. Unsupervised scene decomposition)): In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • Our proposed method achieves ...

- **p. 2 / 1. Introduction - extractive PDF cue:** We show that our method achieves superior results compared to baseline dynamic scene modeling approaches, with notable advantages across diverse datasets [13, 21].
- **p. 4 / 3.4. Background Brightness Control - extractive PDF cue:** To address this, we introduce a brightness control mask that enhances the background branch's capacity to model non-Lambertian effects.
- **p. 4 / 3.4. Background Brightness Control - extractive PDF cue:** Our method simultaneously reconstructs the 3D scene and learns an unsupervised decomposition into decoupled static background and dynamic foreground branches, where the update is loosely ...
- **p. 5 / 3.6. Unsupervised scene decomposition - extractive PDF cue:** Our method offers significantly greater robustness in handling local minimas.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We show our method robustly handles occlusion and reconstructs fine static details compared to SpotlessSplats [24]in Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Our method robustly handles various challenges, preserving clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 3. Compared to SpotlessSplats [24], which is constrained by initialization and overfit to floaters. Our method offers ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control), p. 2 (1. Introduction), p. 5 (3.6. Unsupervised scene decomposition). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control), p. 2 (1. Introduction), p. 5 (3.6. Unsupervised scene decomposition), objective p. 5 (3.7. Loss function), p. 5 (3.7. Loss function), p. 4 (3.4. Background Brightness Control), p. 4 (3.6. Unsupervised scene decomposition).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
