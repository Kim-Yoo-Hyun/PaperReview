# Problem - Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction)): Open-vocabulary 3D scene understanding methods propose a solution towards these challenges by training a model not on a fixed label set but rather aligning the 3D model with 2D foundation ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Current approaches for 3D scene graph prediction rely on labeled datasets to train models for a fixed set of known object classes and relationship categories.
- **p. 1 / Abstract - extractive body cue:** We present Open3DSG, an alternative approach to learn 3D scene graph prediction in an open world without requiring labeled scene graph data.
- **p. 1 / Abstract - extractive body cue:** We co-embed the features from a 3D scene graph prediction backbone with the feature space of powerful open world 2D vision language foundation models.
- **p. 1 / Abstract - extractive body cue:** This enables us to predict 3D scene graphs from 3D point clouds in a zero-shot manner by querying object classes from an open vocabulary and ...
- **p. 1 / Abstract - extractive body cue:** Open3DSG is the first 3D point cloud method to predict not only explicit open-vocabulary object classes, but also open-set relationships that are not limited to ...
- **p. 1 / 1. Introduction - extractive body cue:** Open-vocabulary 3D scene understanding methods propose a solution towards these challenges by training a model not on a fixed label set but rather aligning the ...
- **p. 2 / 1. Introduction - extractive body cue:** This limitation makes it challenging to adopt 2D VLMs for scene graph predictions where compositional relationships are the core part.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Open-vocabulary 3D scene understanding methods propose a solution towards these challenges by training a model not on a fixed label set but ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | 3.1), and in parallel, we extract vision-language features from aligned 2D images (Sec. | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | parallel, extract, vision-language, features, aligned, images, Sec, overall, goal, distill | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Given, complexity, high-level, abstraction, How, Wall, related, state-of-the-art | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: parallel, extract, vision-language, features, aligned, images, Sec, overall, goal, distill | p. 3 (3. Method), p. 3 (3. Method), p. 1 (1. Introduction) |
| Decision / output variable | path/waypoint/velocity; body terms: highlight, following, three, contributions, first, present, create, interactive | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4.2. Closed-set 3D scene graph prediction), p. 8 (4.3. Ablation studies), p. 6 (4.1. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** This limitation makes it challenging to adopt 2D VLMs for scene graph predictions where compositional relationships are the core part.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method)): We highlight the following three contributions: • We are the first to present a method to create an interactive graph representation of a scene from a 3D point cloud, which ...

- **p. 1 / 1. Introduction - extractive body cue:** We present Open3DSG the first approach for learning to predict open-vocabulary 3D scene graphs from 3D point clouds.
- **p. 1 / 1. Introduction - extractive body cue:** The advantage of our method is that it can be queried and prompted for any instance in the scene, such as the TV and Wall, ...
- **p. 3 / 3. Method - extractive body cue:** An overview of our method is shown in Fig.
- **p. 3 / 3. Method - extractive body cue:** The overall goal of our approach is to distill the knowledge of 2D vision-language models into a 3D graph neural network (GNN) to predict open-vocabulary ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | While closed-vocabulary evaluations are valuable, they cannot highlight the huge potential of open-vocabulary methods such as ours. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In future work, we see potential in improving relationship prediction even further to achieve even better and more ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | However, since we predict relationships in a generative manner, we cannot provide fixed queries for our relationship prediction. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We demonstrate that a naive CLIP-based approach is ill-suited for relationship prediction, but also a two-step approach similar ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3. Method), p. 3 (3. Method), p. 1 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3. Method), p. 3 (3. Method), p. 1 (1. Introduction), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
