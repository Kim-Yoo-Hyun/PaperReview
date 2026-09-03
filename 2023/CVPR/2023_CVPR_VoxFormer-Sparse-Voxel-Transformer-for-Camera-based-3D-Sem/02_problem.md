# Problem - VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2302.12251; PDF retrieval source: https://arxiv.org/pdf/2302.12251. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Preliminary)): However, obtaining accurate and complete 3D information of the real world is difficult, since the task is challenged by the lack of sensing resolution and the incomplete observation due to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humans can easily imagine the complete 3D geometry of occluded objects and scenes.
- **p. 1 / Abstract - extractive body cue:** This appealing ability is vital for recognition and understanding.
- **p. 1 / Abstract - extractive body cue:** To enable such capability in AI systems, we propose VoxFormer, a Transformerbased semantic scene completion framework that can output complete 3D volumetric semantics from only ...
- **p. 1 / Abstract - extractive body cue:** Our framework adopts a two-stage design where we start from a sparse set of visible and occupied voxel queries from depth estimation, followed by a ...
- **p. 1 / Abstract - extractive body cue:** A key idea of this design is that the visual features on 2D images correspond only to the visible scene structures rather than the occluded ...
- **p. 1 / 1. Introduction - extractive body cue:** However, obtaining accurate and complete 3D information of the real world is difficult, since the task is challenged by the lack of sensing resolution and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, there is still a significant performance gap between state-of-the-art SSC methods [2] and human perception in driving scenes.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, obtaining accurate and complete 3D information of the real world is difficult, since the task is challenged by the lack of ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | More specifically, we use as input current and previous images denoted by It = {It, It-1, ...}, and use as output a ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | More, specifically, input, current, previous, images, denoted, It-1, output, voxel | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Depthbased, Query, Proposal, Feature, Extractor, Depth, Prediction, Voxel | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: More, specifically, input, current, previous, images, denoted, It-1, output, voxel | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.3. Predefined Parameters) |
| Decision / output variable | geometry/map/query r; body terms: contributions, summarized, follows, novel, two-stage, framework, lifts, images | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Overall Architecture) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: train, stage-2, weighted, cross-entropy, loss, stage-1, employ, binary | p. 5 (3.3. Predefined Parameters), p. 3 (3.1. Preliminary), p. 5 (3.6. Training Loss), p. 3 (3.2. Overall Architecture), p. 4 (3.3. Predefined Parameters), p. 4 (3.3. Predefined Parameters) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Preliminary), p. 3 (3.2. Overall Architecture), p. 4 (3.3. Predefined Parameters) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.2. Performance), p. 7 (4.2. Performance), p. 6 (4.2. Performance) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** However, there is still a significant performance gap between state-of-the-art SSC methods [2] and human perception in driving scenes.
- **p. 3 / 3.1. Preliminary - extractive body cue:** More specifically, we use as input current and previous images denoted by It = {It, It-1, ...}, and use as output a voxel grid Yt ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Overall Architecture), p. 4 (3.3. Predefined Parameters), p. 4 (3.3. Predefined Parameters)): Our contributions in this work can be summarized as follows: • A novel two-stage framework that lifts images into a complete 3D voxelized semantic scene. • A novel query proposal ...

- **p. 2 / 1. Introduction - extractive body cue:** VoxFormer consists of class-agnostic query proposal (stage-1) and class-specific semantic segmentation (stage2), where stage-1 proposes a sparse set of occupied voxels, and stage-2 completes the ...
- **p. 3 / 3.2. Overall Architecture - extractive body cue:** Our framework is a two-stage cascade composed of class-agnostic proposals and class-specific segmentation similar to [68]: stage-1 generates class-agnostic query proposals, and stage-2 uses an ...
- **p. 4 / 3.3. Predefined Parameters - extractive body cue:** Note that our framework supports the input of single or multiple images. computations.
- **p. 4 / 3.3. Predefined Parameters - extractive body cue:** The estimated depth after correction enables the class-agnostic query proposal stage: the query located at an occupied position will be selected to carry out deformable ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.3. Predefined Parameters), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Preliminary), interface p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.3. Predefined Parameters), p. 2 (1. Introduction), objective p. 5 (3.3. Predefined Parameters), p. 3 (3.1. Preliminary), p. 5 (3.6. Training Loss), p. 3 (3.2. Overall Architecture), p. 4 (3.3. Predefined Parameters), p. 4 (3.3. Predefined Parameters).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
