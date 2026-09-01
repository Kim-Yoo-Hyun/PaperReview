# Problem - Ditto: Building Digital Twins of Articulated Objects from Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2202.08227; PDF retrieval source: https://arxiv.org/pdf/2202.08227. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Problem Formulation)): However, they infer part-level geometry on the point cloud which cannot be used for physical simulation, because physical simulation requires compact geometry of the object such as the mesh for ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Digitizing physical objects into the virtual world has the potential to unlock new research and applications in embodied AI and mixed reality.
- **p. 1 / Abstract - extractive body cue:** This work focuses on recreating interactive digital twins of real-world articulated objects, which can be directly imported into virtual environments.
- **p. 1 / Abstract - extractive body cue:** We introduce Ditto to learn articulation model estimation and 3D geometry reconstruction of an articulated object through interactive perception.
- **p. 1 / Abstract - extractive body cue:** Given a pair of visual observations of an articulated object before and after interaction, Ditto reconstructs part-level geometry and estimates the articulation model of the ...
- **p. 1 / Abstract - extractive body cue:** We employ implicit neural representations for joint geometry and articulation modeling.
- **p. 2 / 1. Introduction - extractive body cue:** However, they infer part-level geometry on the point cloud which cannot be used for physical simulation, because physical simulation requires compact geometry of the object ...
- **p. 1 / 1. Introduction - extractive body cue:** A promising path towards closing the reality gap is digitizing physical objects and recreating them in virtual environments.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, they infer part-level geometry on the point cloud which cannot be used for physical simulation, because physical simulation requires compact geometry ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The input to our method is a pair of point cloud observations P1, P2 ∈RN×3 of the articulated object before and after ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | input, pair, point, cloud, observations, articulated, object, before, after, interaction | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | joint, state, translation, distance, resulting, interaction, Since, assume | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: input, pair, point, cloud, observations, articulated, object, before, after, interaction | p. 3 (3. Problem Formulation), p. 3 (3. Problem Formulation), p. 4 (4.2. Implicit Decoders) |
| Decision / output variable | geometry/map/query r; body terms: Given, visual, observations, before, after, interaction, jointly, reconstructs | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: joint, type, prediction, apply, standard, binary, cross, entropy | p. 3 (3. Problem Formulation), p. 3 (4. Method), p. 5 (4.3. Training), p. 5 (4.3. Training), p. 4 (4.1. Two-Stream Encoder), p. 4 (4.1. Two-Stream Encoder) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Problem Formulation), p. 4 (4.1. Two-Stream Encoder), p. 4 (4.2. Implicit Decoders) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5.3. Evaluation Metrics), p. 8 (5.5. Ablation Studies), p. 7 (5.3. Evaluation Metrics) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** A promising path towards closing the reality gap is digitizing physical objects and recreating them in virtual environments.
- **p. 2 / 1. Introduction - extractive body cue:** The key technical challenge is to establish correspondences between these two partial observations.
- **p. 1 / 1. Introduction - extractive body cue:** The majority of prior work focuses on solving individual components of the problem rather than constructing a full-fledged model.
- **p. 3 / 3. Problem Formulation - extractive body cue:** We study the problem of recreating interactive digital twins of articulated objects from a pair of sensory observations before and after an interaction.

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Method), p. 5 (4.3. Training)): Given visual observations before and after interaction, our method jointly reconstructs the part-level geometry and articulation model of the object.

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we apply our method to real-world articulated objects for recreating digital twins.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce Ditto (Digital twin of articulated objects), an implicit neural representation-based model that jointly predicts part-level geometry and kinematic articulation between the parts.
- **p. 3 / 4. Method - extractive body cue:** Ditto consists of a two-stream encoder that fuses two input point clouds and multiple implicit decoders for geometry and articulation.
- **p. 5 / 4.3. Training - extractive body cue:** Our method does not assume known joint types during inference.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Failure of joint estimation also harms segmentation prediction because the joint parameter decoders and the segmentation decoder share ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 3, A-SDF fails to reconstruct the shape details of unseen objects, especially the objects with prismatic joints. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We observe that using the same 3D and 2D features for geometry and articulation makes training unstable, and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In comparison, Ditto does not suffer from such a bottleneck as an end-to-end method. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3. Problem Formulation), p. 3 (3. Problem Formulation), p. 4 (4.2. Implicit Decoders), p. 4 (4.2. Implicit Decoders). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Problem Formulation), interface p. 3 (3. Problem Formulation), p. 3 (3. Problem Formulation), p. 4 (4.2. Implicit Decoders), p. 4 (4.2. Implicit Decoders), objective p. 3 (3. Problem Formulation), p. 3 (4. Method), p. 5 (4.3. Training), p. 5 (4.3. Training), p. 4 (4.1. Two-Stream Encoder), p. 4 (4.1. Two-Stream Encoder).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
