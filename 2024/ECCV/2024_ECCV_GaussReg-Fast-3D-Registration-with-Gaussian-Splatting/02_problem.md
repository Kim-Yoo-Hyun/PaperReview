# Problem - GaussReg: Fast 3D Registration with Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2380_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): But this method faces two issues: a) it is difficult to turn NeRF of unbounded scene to bounded voxel; b) the resolution limitation of the voxel grid makes this method ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** In traditional 3D scene scanning and reconstruction, a large-scale scene is usually divided into different blocks, resulting in many independent sub-scenes that may † Corresponding ...
- **p. 2 / 1 Introduction - extractive body cue:** Scene A Scene B Render Render Render Register Scene A+B Fig.
- **p. 2 / 1 Introduction - extractive body cue:** 1: The purpose of our method is to register scenes A and B with Gaussian Splatting [17] models, and then combine A with B to ...
- **p. 2 / 1 Introduction - extractive body cue:** The first row is the visualization of the 3D Gaussians. not in the same coordinate system.
- **p. 2 / 1 Introduction - extractive body cue:** Therefore, the registration between them plays a crucial role.
- **p. 2 / 1 Introduction - extractive body cue:** But this method faces two issues: a) it is difficult to turn NeRF of unbounded scene to bounded voxel; b) the resolution limitation of the ...
- **p. 3 / 1 Introduction - extractive body cue:** However, it still lacks evaluation benchmarks of scene-level registration with GS.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | But this method faces two issues: a) it is difficult to turn NeRF of unbounded scene to bounded voxel; b) the resolution ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The coarse registration accepts PointsA and PointsB as input, and output a coarse transformation {sc, Rc, Tc}. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | coarse, registration, accepts, PointsA, PointsB, input, output, transformation, Training, Strategy | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Image-Guided, Feature, Extraction, Figure, adopt, principle, multi-view, stereo | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: coarse, registration, accepts, PointsA, PointsB, input, output, transformation, Training, Strategy | p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, summarized, best, knowledge, first, explore, registration | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Followed, DCNN, regularization, probability, volume, feature, obtained, cost | p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 7 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 10 (4 Experiment), p. 10 (4 Experiment), p. 11 (4 Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive body cue:** However, it still lacks evaluation benchmarks of scene-level registration with GS.
- **p. 2 / 1 Introduction - extractive body cue:** When considering large-scale scene reconstruction based on NeRF, there are two main challenges: 1) Due to the complex occlusions present in real-world scenes, lots of ...
- **p. 3 / 1 Introduction - extractive body cue:** In addition, we collect a dataset named GSReg, comprising 6 indoor and 4 outdoor scenarios, to assess the generalization capability of our method.

## What the Paper Changes

PDF body contribution framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method)): The main contributions can be summarized as: • To the best of our knowledge, we are the first to explore the registration of 3D scenes considering Gaussian Splatting representations. • ...

- **p. 3 / 1 Introduction - extractive body cue:** Ultimately, we propose a novel coarse-to-fine GS registration framework: GaussReg.
- **p. 2 / 1 Introduction - extractive body cue:** 1: The purpose of our method is to register scenes A and B with Gaussian Splatting [17] models, and then combine A with B to ...
- **p. 5 / 3 Method - extractive body cue:** In this section, we present our proposed GaussReg for 3D Registration with Gaussian Splatting (GS).
- **p. 5 / 3 Method - extractive body cue:** 3.1 Overview As shown in Figure 2, the proposed GaussReg mainly consists of two stages, including the Coarse Registration, and the Image-Guided Fine Registration.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | Limitations and Future Work We only adopt a simple strategy to fuse and filter two GS models. | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | For indoor scenes in ScanNetGSReg, SuperPoint [10] sometimes fails to extract effective keypoints, leading to registration failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Future work can further explore to address this issue. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Eventually, after excluding cases of failed initial point cloud generation or unsuccessful GS reconstruction, we obtain 1297 training ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 6 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 6 (3 Method), objective p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 7 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
