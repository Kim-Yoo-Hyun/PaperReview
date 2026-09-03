# Problem - RayI2P: Learning Rays for Image-to-Point Cloud Registration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=arfeGsDWoq; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247078. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): This modality gap makes it inherently difficult to design shared feature representations and establish reliable 2D-3D correspondences.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Image-to-point cloud registration aims to estimate the 6-DoF camera pose of a query image relative to a 3D point cloud map.
- **p. 1 / ABSTRACT - extractive body cue:** Existing methods fall into two categories: matching-free methods regress pose directly using geometric priors, but lack fine-grained supervision and struggle with precise alignment; matching-based methods ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these issues, we propose a novel ray-based registration framework that first predicts patch-wise 3D ray bundles connecting image patches to the 3D scene ...
- **p. 1 / ABSTRACT - extractive body cue:** This formulation naturally resolves projection ambiguity, provides scaleconsistent geometry encoding, and enables fine-grained supervision for accurate pose estimation.
- **p. 1 / ABSTRACT - extractive body cue:** Experiments on KITTI and nuScenes show that our approach achieves state-of-the-art registration accuracy, outperforming existing methods.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This modality gap makes it inherently difficult to design shared feature representations and establish reliable 2D-3D correspondences.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, as illustrated in Figure 1(a), this frustum-based optimization only provides coarse supervision, and the resulting poses are often inaccurate due to the lack of ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This modality gap makes it inherently difficult to design shared feature representations and establish reliable 2D-3D correspondences. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The output feature map is downsampled by a factor of 8 relative to the input image, yielding a resolution of 20 × ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | output, feature, downsampled, factor, relative, input, image, yielding, resolution, KITTI | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | OVERVIEW, Given, image, point, cloud, same, scene, goal | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: output, feature, downsampled, factor, relative, input, image, yielding, resolution, KITTI | p. 16 (A.6 MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, summarized, follows, novel, ray-based, paradigm, image-to-point | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: overall, loss, consists, three, terms, regression, Lray, camera | p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4 EXPERIMENTS), p. 14 (A.1 EVALUATION METRICS), p. 7 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, as illustrated in Figure 1(a), this frustum-based optimization only provides coarse supervision, and the resulting poses are often inaccurate due to the lack of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (b) Two key challenges of existing matching-based approaches: (1) projectioninduced correspondence ambiguity: multiple geometrically distinct 3D points project to the same image region; (2) depth-induced ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The main contributions are summarized as follows: (1) We propose a novel ray-based paradigm for image-to-point cloud registration, which effectively addresses the core limitations of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This formulation naturally mitigates the limitations of previous methods.

## What the Paper Changes

PDF body contribution framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 METHOD), p. 4 (3 METHOD)): The main contributions are summarized as follows: (1) We propose a novel ray-based paradigm for image-to-point cloud registration, which effectively addresses the core limitations of prior approaches by modeling image ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To realize this idea, we propose a novel ray-based framework for image-to-point cloud registration as shown in Figure 1(c).
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (2) Extensive experiments on KITTI and nuScenes demonstrate that our method achieves state-of-the-art performance in cross-modal registration accuracy, validating the effectiveness of our ray-based representation.
- **p. 4 / 3 METHOD - extractive body cue:** 3.1 OVERVIEW Given an image I ∈RH×W ×3 and a point cloud P ∈RN×3 from the same scene, our goal is to determine the camera ...
- **p. 4 / 3 METHOD - extractive body cue:** In this paper, we propose a ray-based imageto-point cloud registration method composed of two main stages: a ray prediction module to infer consistent 3D rays ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | This failure mode, although observed only in rare extreme cases, reveals a fundamental limitation of the current framework: ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | Figure 5: Visual comparison between classical pose solver and our proposed ray-guided pose re- gression module. Classical pose ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | In this paper, we present a novel ray-based framework for image-to-point cloud registration that overcomes key limitations of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | While our method achieves competitive performance on challenging outdoor datasets, it still exhibits certain limitation primarily associated with ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 16 (A.6 MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 1 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 16 (A.6 MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 1 (1 INTRODUCTION), objective p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
