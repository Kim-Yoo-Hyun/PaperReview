# Problem - IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement), p. 1 (1. Introduction), p. 2 (1. Introduction)): To address these limitations, RNRMap [14] introduces a renderable neural radiance map representation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Visual navigation with an image as goal is a fundamental and challenging problem.
- **p. 1 / Abstract - extractive body cue:** Conventional methods either rely on end-to-end RL learning or modular-based policy with topological graph or BEV map as memory, which cannot fully model the geometric ...
- **p. 1 / Abstract - extractive body cue:** In order to efficiently and accurately localize the goal image in 3D space, we build our navigation system upon the renderable 3D gaussian (3DGS) representation.
- **p. 1 / Abstract - extractive body cue:** However, due to the computational intensity of 3DGS optimization and the large search space of 6-DoF camera pose, directly leveraging 3DGS for image localization during ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework for efficient and 3D-aware image-goal navigation.
- **p. 1 / 1. Introduction - extractive body cue:** To address these limitations, RNRMap [14] introduces a renderable neural radiance map representation.
- **p. 2 / 1. Introduction - extractive body cue:** Despite these compelling properties, adapting 3DGS representations for image-goal navigation presents significant challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To address these limitations, RNRMap [14] introduces a renderable neural radiance map representation. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Incremental Scene Representation Scene Embedding 𝑬௧ Coarse-to-fine Navigation Reaching Target Local Policy Action Renderingbased Stopper Exploration Current RGB-D Input Target Image Activation ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Incremental, Scene, Representation, Embedding, Coarse-to-fine, Navigation, Reaching, Target, Local, Policy | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | receives, posed, RGB-D, video, stream, required, execute, action | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Incremental, Scene, Representation, Embedding, Coarse-to-fine, Navigation, Reaching, Target, Local, Policy | p. 5 (3.3.1. Coarse Target Localization), p. 3 (3.2. Incremental Scene Representation), p. 3 (3.1. Problem Statement) |
| Decision / output variable | path/waypoint/velocity; body terms: IGL-Nav, Incremental, Gaussian, Localization, framework, progressively, constructs, DGS | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Additionally, apply, cross-entropy, loss, supervise, outputs, nearby, target | p. 3 (3.2. Incremental Scene Representation), p. 3 (3.2. Incremental Scene Representation), p. 5 (3.3.1. Coarse Target Localization), p. 5 (3.3.1. Coarse Target Localization), p. 4 (3.3. Coarse-to-fine Localization) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.2. Incremental Scene Representation), p. 4 (3.3.1. Coarse Target Localization), p. 4 (3.3. Coarse-to-fine Localization) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4.2. Comparison with State-of-the-art), p. 7 (4.3. Analysis of IGL-Nav), p. 6 (4.2. Comparison with State-of-the-art) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Despite these compelling properties, adapting 3DGS representations for image-goal navigation presents significant challenges.
- **p. 3 / 3.1. Problem Statement - extractive body cue:** These limitations fundamentally constrain the system's operational flexibility and real-world deployment potential.
- **p. 1 / 1. Introduction - extractive body cue:** Image-goal navigation, which requires an agent initialized in unknown environment to navigate to the location and orientation specified by an image [39], is a fundamental ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, goal image localization within scene-level 3DGS maps becomes intractable due to the exponential search space complexity inherent in 6-DoF camera pose estimation.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement), p. 3 (3.2. Incremental Scene Representation), p. 4 (3.3.1. Coarse Target Localization)): To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework that (1) progressively constructs 3DGS through feed-forward prediction, eliminating offline optimization; and (2) enables efficient hierarchical goal sea ...

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose to leverage 3D Gaussian Splatting (3DGS) [10] as the scene representation for imagegoal navigation.
- **p. 3 / 3.1. Problem Statement - extractive body cue:** A is the set of actions, which consists of move forward, turn left, turn right and stop.
- **p. 3 / 3.2. Incremental Scene Representation - extractive body cue:** To accommodate streaming video input while effectively leveraging camera pose and depth priors, we present the first feedforward 3DGS reconstruction model for monocular RGB-D sequences, ...
- **p. 4 / 3.3.1. Coarse Target Localization - extractive body cue:** To solve this problem, we propose to further discretize the 3D embeddings Et and Eg.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | A limitation of IGL-Nav is that it requires depth and camera intrinsics of goal image. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | As shown in Table 3, with predicted depth and camera intrinsics, the performance of IGLNav is still robust. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.3.1. Coarse Target Localization), p. 3 (3.2. Incremental Scene Representation), p. 3 (3.1. Problem Statement), p. 5 (3.3.1. Coarse Target Localization). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (3.3.1. Coarse Target Localization), p. 3 (3.2. Incremental Scene Representation), p. 3 (3.1. Problem Statement), p. 5 (3.3.1. Coarse Target Localization), objective p. 3 (3.2. Incremental Scene Representation), p. 3 (3.2. Incremental Scene Representation), p. 5 (3.3.1. Coarse Target Localization), p. 5 (3.3.1. Coarse Target Localization), p. 4 (3.3. Coarse-to-fine Localization).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** To address these limitations, RNRMap [14] introduces a renderable neural radiance map representation. (p. 1, 1. Introduction).
- **Formulation-changing contribution:** To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework that (1) progressively constructs 3DGS through feed-forward prediction, eliminating offline optimization; and (2) enables efficient hierarchical goal sea ... (p. 2, 1. Introduction).
- **Assumption/failure evidence:** A limitation of IGL-Nav is that it requires depth and camera intrinsics of goal image. (p. 8, 5. Conclusion).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
