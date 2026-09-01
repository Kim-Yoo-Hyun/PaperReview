# Problem - Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2503.05189v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 4 (3) Persistent Object Tracking phase for online tracking)): Recently introduced Gaussian Splats [1] efficiently model object geometry, but lack persistent state estimation for taskoriented manipulation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Tracking and manipulating irregularly-shaped, previously unseen objects in dynamic environments is important for robotic applications in manufacturing, assembly, and logistics.
- **p. 1 / Abstract - extractive body cue:** Recently introduced Gaussian Splats [1] efficiently model object geometry, but lack persistent state estimation for taskoriented manipulation.
- **p. 1 / Abstract - extractive body cue:** POGS updates object states without requiring expensive rescanning or prior CAD models of objects.
- **p. 1 / Abstract - extractive body cue:** After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features ...
- **p. 1 / Abstract - extractive body cue:** POGS supports grasping, reorientation, and natural language-driven manipulation by refining object pose estimates, facilitating sequential object reset operations with human-induced object perturbations and tool servoing, ...
- **p. 1 / Abstract - extractive body cue:** The challenge is greater when dealing with irregularly shaped objects for which obtaining an accurate Computer-Aided Design (CAD) model is impractical.
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** After each object reset, a human will randomly reconfigure both objects to different poses and the process is repeated until failure.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Recently introduced Gaussian Splats [1] efficiently model object geometry, but lack persistent state estimation for taskoriented manipulation. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | objects, moved, humans, robots, POGS, update, state, online, allowing, flexible | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Unlike, object, grouping, features, language, where, learn, embedding | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: objects, moved, humans, robots, POGS, update, state, online, allowing, flexible | p. 2 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking) |
| Decision / output variable | geometry/map/query r; body terms: makes, following, contributions, Persistent, Object, Gaussian, Splat, POGS | p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: operates, through, complementary, mechanisms, attracting, features, belong, same | p. 3 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract), p. 1 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract), p. 1 (Abstract) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (3) Persistent Object Tracking phase for online tracking), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 6 (3) Persistent Object Tracking phase for online tracking) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** The challenge is greater when dealing with irregularly shaped objects for which obtaining an accurate Computer-Aided Design (CAD) model is impractical.
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** After each object reset, a human will randomly reconfigure both objects to different poses and the process is repeated until failure.
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** We evaluate this experiment by recording the maximum number of sequential object resets before failure, the object grasp rate, the object place rate, and the ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** This feature loss measures how well the current pose estimates visually align the rendered model with the actual objects.

## What the Paper Changes

PDF contribution framing (p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract)): This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped objects. • A robot system ...

- **p. 1 / Abstract - extractive body cue:** To enable online state estimation, tracking, and manipulation of unseen objects in dynamic environments, we present Persistent Object Gaussian Splat (POGS), an editable objectcentric feature ...
- **p. 1 / Abstract - extractive body cue:** (Bottom) A POGS unified representation enables language querying, grasp sampling, and continuous tracking of irregular objects as they move.
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** The drill handle is fully occluded by the motor body, yet our POGS unified representation enables handle grasping based on previously observed geometry.
- **p. 2 / Abstract - extractive body cue:** Our approach aims to achieve robust online object tracking and scene updating with

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | After each object reset, a human will randomly reconfigure both objects to different poses and the process is ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | We evaluate this experiment by recording the maximum number of sequential object resets before failure, the object grasp ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 4 (3) Persistent Object Tracking phase for online tracking), interface p. 2 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract), objective p. 3 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract), p. 1 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
