# Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with the Gaussian splatting pipeline.를 문제로 두고, The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into a lightweight student network. • Our method ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Unsigned distance function (UDF) is well suited for representing open surfaces, but learning them from multi-view images is challenging because ground-truth surfaces are unavailable for ...
- **p. 1 / Abstract - extractive body cue:** Prior methods optimize UDFs with global objectives and apply gradient-based priors ignoring the non-differentiability for queries on the target surface, which leads to unstable training ...
- **p. 1 / Abstract - extractive body cue:** We address these issues by distilling a patch-based UDF prior, trained on synthetic ground truth algebraic surfaces with closed form expressions, into a lightweight student ...
- **p. 1 / Abstract - extractive body cue:** We design a band-limited knowledge distillation strategy that leverages a pretrained patch-based UDF predictor to provide reliable near-surface UDF supervision, enabling stable student training and ...
- **p. 1 / Abstract - extractive body cue:** In addition, we introduce a visibility- and geometry-aware confidence weighting that modulates teacher influence, further steering the student toward accurate surfaces in ambiguous or weakly ...
- **p. 1 / 1. Introduction - extractive body cue:** To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with ...
- **p. 1 / 1. Introduction - extractive body cue:** Surface reconstruction from multi-view images is a fundamental problem in computer vision and graphics.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into ...
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we introduce a visibility- and geometry-aware confidence weighting, together with a joint optimization scheme, to further steer the student toward accurate surfaces from ...
- **p. 3 / 3. Method - extractive body cue:** Our framework integrates Gaussian Splatting with UDF learning via a band-limited distillation scheme: a frozen local-shape UDF teacher ut provides supervision in a narrow nearsurface ...
- **p. 3 / 3. Method - extractive body cue:** Rendering proceeds by projecting each Gaussian onto the image plane and compositing its contribution in frontto-back order.
- **p. 5 / 3.3. Band-limited Knowledge Distillation - extractive body cue:** Furthermore, the overall distillation formulation offers several advantages: it simplifies the learning task by limiting the geometric complexity within each patch, enables effective reuse of ...
- **p. 3 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** Considering the strengths of LoSF-UDF [19] including robustness to noise and local feature representation, we use it as the teacher UDF model for distillation, denoted ...
- **p. 4 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** To integrate this patch-based UDF prior into the 3DGS optimization, we use it to regularize the student UDF model fs.
- **p. 5 / 3.3. Band-limited Knowledge Distillation - extractive body cue:** representation to fit the scene geometry and appearance, and then optimize the student network within this band.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into a lightweight student network. • Our method ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 3 (3. Method) |
| State/latent | main, contributions, follows, novel, framework, learns, UDF, over, Gaussian, primitives, distilling, patch-based | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method) |
| Output/action | Our goal is to reconstruct accurate, geometrically consistent open surfaces from calibrated multi-view images. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Method), p. 3 (3. Method), p. 5 (3.5. Joint Optimization) |
| Objective/outcome | The Gaussian parameters are optimized by minimizing the L1 photometric loss between the rendered image C′(u, v) and the ground-truth image C(u, v): Lr = /C′(u, v) -C(u, v)/1 , (2) | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3. Method), p. 4 (3.3. Band-limited Knowledge Distillation), p. 5 (3.5. Joint Optimization) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into ...
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we introduce a visibility- and geometry-aware confidence weighting, together with a joint optimization scheme, to further steer the student toward accurate surfaces from ...
- **p. 3 / 3. Method - extractive body cue:** Our framework integrates Gaussian Splatting with UDF learning via a band-limited distillation scheme: a frozen local-shape UDF teacher ut provides supervision in a narrow nearsurface ...
- **p. 3 / 3. Method - extractive body cue:** Rendering proceeds by projecting each Gaussian onto the image plane and compositing its contribution in frontto-back order.
- **p. 5 / 3.3. Band-limited Knowledge Distillation - extractive body cue:** Furthermore, the overall distillation formulation offers several advantages: it simplifies the learning task by limiting the geometric complexity within each patch, enables effective reuse of ...
- **p. 7 / 4.2. DF3D Dataset - extractive body cue:** Among UDF-based approaches, our model further achieves competitive runtime 4897
- **p. 8 / 4.2. DF3D Dataset - extractive body cue:** GaussianUDF [29], which couples a global UDF with 3D Gaussian Splatting, improves surface completeness over appearance-only methods but tends to oversmooth the geometry and loses ...
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared methods, including classical NeRF-style SDF baselines (NeuS [48]), Gaussian-based ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.2. DF3D Dataset), p. 8 (4.2. DF3D Dataset) |
| Embodiment/environment | We further evaluate our method on the DTU dataset [22], which contains 15 widely used multi-view scenes for surface reconstruction. | hardware/simulator version and reset protocol | p. 8 (4.3. DTU Dataset), p. 5 (4.1. Experiment Settings) |
| Dataset/benchmark | Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3). | role, split, size and leakage | p. 8 (4.3. DTU Dataset), p. 5 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings), p. 7 (4.2. DF3D Dataset) |
| Metric | Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3). | definition, denominator, direction and uncertainty | p. 6 (4.1. Experiment Settings), p. 8 (4.3. DTU Dataset), p. 4 (Figure/Table caption) |
| Baseline/ablation | As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared methods, including classical NeRF-style SDF baselines (NeuS [48]), Gaussian-based methods without explicit distance fields (3DGS [24], ... | fair input/data/compute/action matching | p. 8 (4.3. DTU Dataset), p. 7 (4.2. DF3D Dataset), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to further ...
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** It is well known that learning unsigned distance functions (UDFs) is intrinsically more challenging than learning signed distance fields (SDFs), due to sign ambiguity and ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with the Gaussian splatting pipeline.를 문제로 두고, The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into a lightweight student network. • Our method ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Learning Patch-based UDF Priors), p. 4 (3.2. Learning Patch-based UDF Priors), p. 5 (3.3. Band-limited Knowledge Distillation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
