# Problem - C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 3 (3.1. Problem Definition), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, these methods primarily rely on single-view generation and lack mechanisms for handling multiple geometrically related views.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We introduce C-GenReg, a training-free framework for 3D point cloud registration that leverages the complementary strengths of world-scale generative priors and registration-oriented Vision Foundation Models ...
- **p. 1 / Abstract - extractive PDF cue:** Current learning-based 3D point cloud registration methods struggle to generalize across sensing modalities, sampling differences, and environments.
- **p. 1 / Abstract - extractive PDF cue:** Hence, CGenReg augments the geometric point cloud registration branch by transferring the matching problem into an auxiliary image domain, where VFMs excel, using a World ...
- **p. 1 / Abstract - extractive PDF cue:** This generative transfer preserves spatial coherence across source and target views without any fine-tuning.
- **p. 1 / Abstract - extractive PDF cue:** From these generated views, a VFM pretrained for finding dense correspondences extracts matches.
- **p. 2 / 1. Introduction - extractive PDF cue:** However, these methods primarily rely on single-view generation and lack mechanisms for handling multiple geometrically related views.
- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** However, C∗is unknown in practice, and the core challenge is to establish reliable correspondences between P and Q.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these methods primarily rely on single-view generation and lack mechanisms for handling multiple geometrically related views. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | From each input point cloud, we render a depth map and use the Cosmos-Transfer WFM [18] to generate multi-view-consistent RGB images that ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | input, point, cloud, render, depth, Cosmos-Transfer, WFM, generate, multi-view-consistent, RGB | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | When, data, provided, LiDAR, point, clouds, simulate, same | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: input, point, cloud, render, depth, Cosmos-Transfer, WFM, generate, multi-view-consistent, RGB | p. 3 (3.2. C-GenReg - Overview), p. 4 (3.2. C-GenReg - Overview), p. 4 (3.3. Generated-RGB Branch) |
| Decision / output variable | geometry/map/query r; body terms: Standard, point, cloud, registration, consists, feature, extraction, matching | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: fusion, module, designed, main, objectives, preserve, inductive, biases | p. 3 (3.1. Problem Definition), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.3. Generated-RGB Branch) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.1. Experimental Settings), p. 7 (4.2. Method Evaluation), p. 8 (4.3. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** However, C∗is unknown in practice, and the core challenge is to establish reliable correspondences between P and Q.
- **p. 1 / 1. Introduction - extractive PDF cue:** Methods that perform well in indoor RGB-D scenes often degrade on different sensors or outdoor LiDAR data, revealing limited cross-domain generalization.
- **p. 1 / 1. Introduction - extractive PDF cue:** In contrast, the image domain has largely overcome such generalization limits through Vision Foundation Models (VFMs), which achieve remarkable robustness by training on massive, heterogeneous ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Existing generative approaches for point cloud registration [12, 13, 27] have recently demonstrated the potential of diffusion models for this task.

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion)): Standard point cloud registration consists of feature extraction, feature matching, and robust pose estimation (e.g.

- **p. 2 / 1. Introduction - extractive PDF cue:** In contrast, our method, C-GenReg (stands for Consistent Generative Registration), leverages WFMs to generate multiview-consistent RGB views directly from geometry, eliminating the need for any ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Instead, we introduce a "Matchthen-Fuse" scheme that combines two independent correspondence posteriors, one from the WFM + VFM branch and one from the geometric branch, ...
- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive PDF cue:** To address this, we introduce the Disjunctive Posterior Fusion (Noisy-OR), which aggregates evidence 3008
- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive PDF cue:** To meet these goals, we propose a "match-then-fuse" probabilistic strategy, where putative correspondences are first established independently for each modality by computing feature similarity matrices ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Figure 4. Prompt robustness on 3DMatch. Relative rotation (RRE,◦) and translation (RTE, cm) errors under different prompt types. ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.2. C-GenReg - Overview), p. 4 (3.2. C-GenReg - Overview), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.3. Generated-RGB Branch). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 3 (3.1. Problem Definition), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.2. C-GenReg - Overview), p. 4 (3.2. C-GenReg - Overview), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.3. Generated-RGB Branch), objective p. 3 (3.1. Problem Definition), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
