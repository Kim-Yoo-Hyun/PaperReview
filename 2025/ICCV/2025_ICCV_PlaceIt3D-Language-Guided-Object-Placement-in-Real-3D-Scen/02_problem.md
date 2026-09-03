# Problem - PlaceIt3D: Language-Guided Object Placement in Real 3D Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): We study language-guided 3D asset placement in reconstructed scenes, a problem closest to grounding and to synthetic scene generation, yet distinct in that it requires addressing all of the following ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce the task of Language-Guided Object Placement in Real 3D Scenes.
- **p. 1 / Abstract - extractive body cue:** Given a 3D reconstructed point-cloud scene, a 3D asset, and a natural-language instruction, the goal is to place the asset so that the instruction is ...
- **p. 1 / Abstract - extractive body cue:** The task demands tackling four intertwined challenges: (a) one-to-many ambiguity in valid placements; (b) precise geometric and physical reasoning; (c) joint understanding across the scene, ...
- **p. 1 / Abstract - extractive body cue:** The first three challenges mirror the complexities of synthetic scene generation, while the metadata-free, noisy-scan scenario is inherited from language-guided 3D visual grounding.
- **p. 1 / Abstract - extractive body cue:** We inaugurate this task by introducing a benchmark and evaluation protocol, releasing a dataset for training multi-modal large language models (MLLMs), and establishing a first ...
- **p. 2 / 1. Introduction - extractive body cue:** We study language-guided 3D asset placement in reconstructed scenes, a problem closest to grounding and to synthetic scene generation, yet distinct in that it requires ...
- **p. 2 / 1. Introduction - extractive body cue:** Many constraints are geometric and cannot be resolved from 2D projections alone.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We study language-guided 3D asset placement in reconstructed scenes, a problem closest to grounding and to synthetic scene generation, yet distinct in ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | As in the shoe example, the goal is to find a valid placement of the object among multiple configurations that satisfy the ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | shoe, example, goal, find, valid, placement, object, among, multiple, configurations | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Among, valid, options, model, must, follow, user, stated | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: shoe, example, goal, find, valid, placement, object, among, multiple, configurations | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: advance, research, area, make, three, contributions, summarized, here | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: combination, Binary, Cross, Entropy, BCE, Dice, losses, when | p. 6 (4.4. Losses), p. 6 (4.4. Losses) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4.4. Losses), p. 6 (4.4. Losses) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 4 (3.2.2. Benchmark metrics), p. 7 (5.1. Quantitative results), p. 7 (5.1. Quantitative results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Many constraints are geometric and cannot be resolved from 2D projections alone.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): To advance research in this area, we make three key contributions, summarized here: • We introduce PLACEIT3D-benchmark for languageguided placement with 3,500 evaluation examples, each consisting of a real ScanNet ...

- **p. 2 / 1. Introduction - extractive body cue:** Like the benchmark, it uses ScanNet scenes and PartObjaverse-Tiny assets. • We propose PLACEWIZARD, a proto-method for this task built on recent 3D LLMs [25].
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we focus on the novel task of languageguided 3D object placement in a reconstructed real 3D scene.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Our novel task formulation currently has several limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Despite these limitations, we believe our work lays the groundwork for further research in this area. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Due to its frequent failure to accurately detect floor regions, we substitute in ground truth floor masks, while ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In contrast, the rule-based system, which leverages both asset and scene meshes, can produce more plausible placements, albeit ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), objective p. 6 (4.4. Losses), p. 6 (4.4. Losses).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
