# Problem - Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): In this work, we propose Urban-GS, a novel framework that resolves the above challenges to deliver compact, high-fidelity unified aerial-to-street reconstruction.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Recently, 3D Gaussian Splatting (3DGS) has revolutionized radiance field reconstruction, enabling efficient and highfidelity novel view synthesis.
- **p. 1 / Abstract - extractive PDF cue:** However, seamless integration of both aerial and street view images to model urban scenes remains a significant challenge for 3DGS.
- **p. 1 / Abstract - extractive PDF cue:** This joint setting suffers from extreme view coverage disparity, complex multi-scale details, and imbalanced viewpoint distributions.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we present Urban-GS, a novel framework built upon Gaussian Splatting for the compact unified reconstruction and high-fidelity rendering of urban scenes from ...
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we first develop an Aerial-Street Joint Adaptive Densification method to resolve the densification conflicts arising from large view coverage disparity.
- **p. 2 / 1. Introduction - extractive PDF cue:** In this work, we propose Urban-GS, a novel framework that resolves the above challenges to deliver compact, high-fidelity unified aerial-to-street reconstruction.
- **p. 2 / 1. Introduction - extractive PDF cue:** This limitation highlights the necessity of jointly reconstructing scenes using aerial and street view imagery, as the complementary perspectives offered by these two modalities are ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In this work, we propose Urban-GS, a novel framework that resolves the above challenges to deliver compact, high-fidelity unified aerial-to-street reconstruction. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Concurrently, the drastic variation in projection areas across different views arises precisely from the large variation in observation distances inherent to the ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Concurrently, drastic, variation, projection, areas, across, different, views, arises, precisely | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | state, persists, certain, period, anchor, considered, have, contribution | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Concurrently, drastic, variation, projection, areas, across, different, views, arises, precisely | p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 5 (4.2. Contribution-based Anchor Pruning) |
| Decision / output variable | geometry/map/query r; body terms: resolves, densification, conflicts, enabling, joint, contributions, enhancing, overall | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Methods) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Quantitative, comparison, across, accumulating, gradients, densification, aerial, views | p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.3. Global-to-Local Optimization), p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 5 (4.2. Contribution-based Anchor Pruning), p. 5 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.4. Loss Function) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.2. Contribution-based Anchor Pruning), p. 5 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.4. Loss Function) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (5.1. Experimental Setup), p. 8 (5.3. Ablations Study and Analysis), p. 8 (5.3. Ablations Study and Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** This limitation highlights the necessity of jointly reconstructing scenes using aerial and street view imagery, as the complementary perspectives offered by these two modalities are ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Building on this foundation, recent advances have substantially improved the scalability and rendering fidelity of Gaussian Splatting for urban scenes using either aerial [14-16, 24] ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Methods), p. 5 (4.2. Contribution-based Anchor Pruning), p. 6 (4.3. Global-to-Local Optimization)): This method resolves densification conflicts, enabling joint contributions and enhancing overall reconstruction fidelity. • A Contribution-based Anchor Pruning method that enables reliable and efficient removal of redundant anchors in m ...

- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, the main contributions of our method are: • An in-depth analysis of the densification conflicts in aerial-street scene reconstruction, and a corresponding Aerial-Street ...
- **p. 4 / 4. Methods - extractive PDF cue:** 4.2, we present a contribution-based anchor pruning strategy adopted in Urban-GS to mitigate the excessive memory consumption caused by capturing multi-scale scene details.
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive PDF cue:** To address this issue, we propose a contributionweighted mask regularization term.
- **p. 6 / 4.3. Global-to-Local Optimization - extractive PDF cue:** Efficiency comparison between our method and Horizon-GS [10] on the Horizon-GS dataset. stage.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Figure 2. The overview pipeline of Urban-GS. Top (Gloabal Training): We start by initializing LOD-structured anchors from SfM- ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Table 3. Efficiency comparison between our method and Horizon-GS [10] on the Horizon-GS dataset. stage. For each selected ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This limitation is evident in its struggles in the unified aerial-street setting. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | However, this approach fundamentally fails to account for the contribution variations caused by drastic changes in projection areas. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 5 (4.2. Contribution-based Anchor Pruning), p. 5 (4.2. Contribution-based Anchor Pruning). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 5 (4.2. Contribution-based Anchor Pruning), p. 5 (4.2. Contribution-based Anchor Pruning), objective p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.3. Global-to-Local Optimization), p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 5 (4.2. Contribution-based Anchor Pruning), p. 5 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.4. Loss Function).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
