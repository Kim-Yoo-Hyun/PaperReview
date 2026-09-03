# Problem - TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, these approaches typically entangle scene content and viewpoint cues in the same feature embeddings, making it difficult to disentangle camera parameters from scene content and causing pose errors to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present TokenSplat, a feed-forward framework for joint 3D Gaussian reconstruction and camera pose estimation from unposed multi-view images.
- **p. 1 / Abstract - extractive body cue:** At its core, TokenSplat introduces a Token-aligned Gaussian Prediction module that aligns semantically corresponding information across views directly in the feature space.
- **p. 1 / Abstract - extractive body cue:** Guided by coarse token positions and fusion confidence, it aggregates multiscale contextual features to enable long-range cross-view reasoning and reduce redundancy from overlapping Gaussians.
- **p. 1 / Abstract - extractive body cue:** To further enhance pose robustness and disentangle viewpoint cues from scene semantics, TokenSplat employs learnable camera tokens and an Asymmetric Dual-Flow Decoder (ADF-Decoder) that enforces ...
- **p. 1 / Abstract - extractive body cue:** This maintains clean factorization within a feed-forward architecture, enabling coherent reconstruction and stable pose estimation without iterative refinement.
- **p. 1 / 1. Introduction - extractive body cue:** However, these approaches typically entangle scene content and viewpoint cues in the same feature embeddings, making it difficult to disentangle camera parameters from scene content ...
- **p. 1 / 1. Introduction - extractive body cue:** Despite this progress, most existing 3DGS-based reconstruction pipelines [3, 6, 21, 22, 25, 26, 45] rely on per-scene optimization, which restricts their *Corresponding author scalability ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these approaches typically entangle scene content and viewpoint cues in the same feature embeddings, making it difficult to disentangle camera parameters ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | For camera pose estimation, the network predicts per-view poses Pi that transform each input image Ii into the canonical reference view I1. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | camera, pose, estimation, network, predicts, per-view, poses, transform, input, image | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | input, view, first, encoded, image, tokens, shared, ViT | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: camera, pose, estimation, network, predicts, per-view, poses, transform, input, image | p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction), p. 3 (3.2. Architecture) |
| Decision / output variable | geometry/map/query r; body terms: summary, main, contributions, follows, TokenSplat, feed-forward, pose-free, reconstruction | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: overall, camera, pose, loss, Lpose, LMSE, Lalign, model | p. 5 (3.6. Loss Functions), p. 5 (3.6. Loss Functions), p. 3 (3.3. Asymmetric Dual-Flow Decoder), p. 4 (3.3. Asymmetric Dual-Flow Decoder) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.3. Asymmetric Dual-Flow Decoder), p. 4 (3.3. Asymmetric Dual-Flow Decoder), p. 4 (3.4. Token Fusion for Scene Reconstruction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4.1. Experimental Settings), p. 6 (4.2. Experimental Results), p. 5 (4.1. Experimental Settings) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Despite this progress, most existing 3DGS-based reconstruction pipelines [3, 6, 21, 22, 25, 26, 45] rely on per-scene optimization, which restricts their *Corresponding author scalability ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • We propose TokenSplat, a feed-forward pose-free reconstruction framework that jointly estimates camera poses and 3D Gaussian ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Architecture), p. 4 (3.3. Asymmetric Dual-Flow Decoder)): In summary, our main contributions are as follows: • We propose TokenSplat, a feed-forward pose-free reconstruction framework that jointly estimates camera poses and 3D Gaussian scenes from unposed multi-view images, ...

- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose TokenSplat, a feed-forward 3D Gaussian splatting framework that reconstructs 3D scenes from an arbitrary number of unposed images while ...
- **p. 2 / 1. Introduction - extractive body cue:** To jointly optimize 3D reconstruction and camera pose estimation within a feed-forward architecture, we introduce learnable camera tokens and an Asymmetric DualFlow Decoder (ADF-Decoder) that ...
- **p. 3 / 3.2. Architecture - extractive body cue:** 1, our method is a Transformer-based architecture for feed-forward 3D reconstruction from unposed images.
- **p. 4 / 3.3. Asymmetric Dual-Flow Decoder - extractive body cue:** The ADF-Decoder consists of 12 decoder blocks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | It yields consistent accuracy improvements and robust zero-shot generalization across diverse datasets. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Despite the difference in view counts, TokenSplat maintains stable reconstruction quality, while competing methods, including AnySplat, which fuses ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | FreeSplat generates numerous scattered Gaussians, while NoPoSplat and SPFSplat show poor scalability and fail to generalize to unseen ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | On ScanNet, the model maintains accurate pose estimation under the 28-view setting, reducing ATE by 0.018 over AnySplat, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction), p. 3 (3.2. Architecture), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction), p. 3 (3.2. Architecture), p. 2 (1. Introduction), objective p. 5 (3.6. Loss Functions), p. 5 (3.6. Loss Functions), p. 3 (3.3. Asymmetric Dual-Flow Decoder), p. 4 (3.3. Asymmetric Dual-Flow Decoder).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
