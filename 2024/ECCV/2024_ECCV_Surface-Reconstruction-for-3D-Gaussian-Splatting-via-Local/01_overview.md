# Surface Reconstruction for 3D Gaussian Splatting via Local Structural Hints

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/274_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/274_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Prior efforts to address this intricate challenge of extracting surface meshes from 3D Gaussian Splatting have been sparse.를 문제로 두고, To address this, we propose a novel regularizer that leverages a neural implicit network to approximate the signed distance values of the MLS function at sampling points and the normals at Gaussian ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 3D Gaussian Splatting (3DGS) [20] has garnered significant attention in the realm of 3D computer vision for its exceptional efficiency in modeling 3D radiance fields.
- **p. 1 / 1 Introduction - extractive body cue:** Given multi-view images with corresponding camera poses, 3DGS initializes Gaussian primitives from a sparse point cloud that comes from COLMAP [41] and renders a novel ...
- **p. 1 / 1 Introduction - extractive body cue:** With the dynamic densification operation on Gaussians including splitting and cloning, the final scene will be represented by millions of tiny Gaussians with unparalleled rendering ...
- **p. 1 / 1 Introduction - extractive body cue:** Despite the superior rendering efficiency and quality achieved by 3DGS over its implicit counterparts, Neural Radiance Field (NeRF) [3,31,32], its surface reconstruction ability is largely ...
- **p. 2 / 1 Introduction - extractive body cue:** Wu, J.Zheng, J.Cai. main reason is that a large number of discrete tiny Gaussians are noisy, unorganized, and do not align well with the underlying ...
- **p. 2 / 1 Introduction - extractive body cue:** Prior efforts to address this intricate challenge of extracting surface meshes from 3D Gaussian Splatting have been sparse.
- **p. 2 / 1 Introduction - extractive body cue:** These artifacts not only compromise the mesh's visual fidelity but also underscore the limitations of the regularization strategies in fully capturing complex surface geometry in ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** To address this, we propose a novel regularizer that leverages a neural implicit network to approximate the signed distance values of the MLS function at ...
- **p. 8 / 3 Method - extractive body cue:** We propose a novel strategy to further align the Gaussians with the surface.
- **p. 3 / 1 Introduction - extractive body cue:** Moreover, to ensure geometry consistency, we propose regularizing the MLS-based function prediction with a jointly learned neural implicit field.
- **p. 7 / 3 Method - extractive body cue:** Inspired by the depth rendering from [15,19,26,28], we also incorporate such a design in our framework by rendering the depth with the z-coordinate zi of ...
- **p. 2 / 1 Introduction - extractive body cue:** The key insight of our approach is to leverage the local structure hints to guide the optimization of Gaussians.
- **p. 9 / 3 Method - extractive body cue:** At first, we train the model with the color reconstruction loss as in original 3DGS [20] together with the monocular cue related losses in Sec.
- **p. 10 / 3 Method - extractive body cue:** After the optimization, we use 3D Gaussian means and normals for Poisson surface reconstruction [18] to extract the reconstructed meshes.
- **p. 5 / 3 Method - extractive body cue:** 3.1 and then elaborate on the technical details of each core module.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In addition to the vanilla IMLS definition, we further introduce a Robust IMLS (RIMLS) by applying a 1-D Gaussian kernel inputted with the norm of the difference between the normalized gradient ∇FMLP ... | RGB-D, image set, point cloud, depth와 camera pose | p. 9 (3 Method), p. 1 (1 Introduction) |
| State/latent | addition, vanilla, IMLS, definition, further, introduce, Robust, RIMLS, applying, Gaussian, kernel, inputted | geometry, map, object/relationship state | p. 9 (3 Method), p. 1 (1 Introduction), p. 5 (3 Method) |
| Output/action | Given multi-view images with corresponding camera poses, 3DGS initializes Gaussian primitives from a sparse point cloud that comes from COLMAP [41] and renders a novel view with a dedicated tile-based rasterization technique. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method) |
| Objective/outcome | The loss function will backpropagate the gradients to both the Gaussian Splatting field and the neural SDF. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 9 (3 Method), p. 9 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** To address this, we propose a novel regularizer that leverages a neural implicit network to approximate the signed distance values of the MLS function at ...
- **p. 8 / 3 Method - extractive body cue:** We propose a novel strategy to further align the Gaussians with the surface.
- **p. 3 / 1 Introduction - extractive body cue:** Moreover, to ensure geometry consistency, we propose regularizing the MLS-based function prediction with a jointly learned neural implicit field.
- **p. 7 / 3 Method - extractive body cue:** Inspired by the depth rendering from [15,19,26,28], we also incorporate such a design in our framework by rendering the depth with the z-coordinate zi of ...
- **p. 2 / 1 Introduction - extractive body cue:** The key insight of our approach is to leverage the local structure hints to guide the optimization of Gaussians.
- **p. 13 / 4 Experiments - extractive body cue:** While keeping the MLS term with the gradient term in the joint loss (w/o eikonal term), the F-score can be significantly improved thanks to the ...
- **p. 13 / 4 Experiments - extractive body cue:** 3 (b), although L = 1 has achieved good results, the F-score keeps improving as L gets increased.
- **p. 12 / 4 Experiments - extractive body cue:** It provides very important hints about the Gaussian orientation, which also significantly improves the quality of Poisson reconstruction.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 13 (4 Experiments), p. 13 (4 Experiments) |
| Embodiment/environment | 2) ScanNet [10] is a real-world dataset captured with challenging image quality. | hardware/simulator version and reset protocol | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Dataset/benchmark | Chamfer-L1↓F-score ↑ COLMAP [41] 0.141 0.537 UNISURF [33] 0.359 0.267 NeuS [51] 0.194 0.291 VolSDF [58] 0.267 0.346 Manhattan-SDF [16] 0.070 0.602 MonoSDF (Grid) [62] 0.064 0.626 MonoSDF (MLP) [62] 0.042 0.733 ... | role, split, size and leakage | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 14 (4 Experiments), p. 11 (4 Experiments) |
| Metric | For quantitative evaluation of surface quality, we measure Chamfer Distance, Normal Consistency Score and Fscore with a threshold of 5cm on Replica. | definition, denominator, direction and uncertainty | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Baseline/ablation | We compare with previous strong baselines of neural implicit surface [16,33,51,58,62] and the 3DGS-based approach SuGaR [15]. | fair input/data/compute/action matching | p. 14 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 2: Joint optimization of 3DGS and neural implicit representation. We propose a novel strategy to further align the Gaussians with the surface. We jointly ...
- **p. 14 / 4 Experiments - extractive body cue:** Although the MonoSDF (MLP) adopts pure MLP structure which shows robustness to the camera noise, the training time of such a variant gets much longer ...
- **p. 12 / 4 Experiments - extractive body cue:** 2, the inaccurate normal estimated by the density gradient will lead to a degraded iso-surface estimation compared with Scaffold-GS+D and ScaffoldGS+N.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Prior efforts to address this intricate challenge of extracting surface meshes from 3D Gaussian Splatting have been sparse.를 문제로 두고, To address this, we propose a novel regularizer that leverages a neural implicit network to approximate the signed distance values of the MLS function at sampling points and the normals at Gaussian ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 9 (3 Method), p. 10 (3 Method), p. 5 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
