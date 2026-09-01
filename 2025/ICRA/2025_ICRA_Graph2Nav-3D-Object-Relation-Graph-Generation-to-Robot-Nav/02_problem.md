# Problem - Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2504.16782v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, there are two major limitations in current 3D scene graph generation methods which hinder the growth of this field.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We propose Graph2Nav, a real-time 3D objectrelation graph generation framework, for autonomous navigation in the real world.
- **p. 1 / Abstract - extractive PDF cue:** Our framework fully generates and exploits both 3D objects and a rich set of semantic relationships among objects in a 3D layered scene graph, which ...
- **p. 1 / Abstract - extractive PDF cue:** It learns to generate 3D semantic relations among objects, by leveraging and advancing state-of-the-art 2D panoptic scene graph works into the 3D world via 3D ...
- **p. 1 / Abstract - extractive PDF cue:** This approach avoids previous training data constraints in learning 3D scene graphs directly from 3D data.
- **p. 1 / Abstract - extractive PDF cue:** We conduct experiments to validate the accuracy in locating 3D objects and labeling objectrelations in our 3D scene graphs.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, there are two major limitations in current 3D scene graph generation methods which hinder the growth of this field.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this paper, we present Graph2Nav (Figure 1), a novel real-time 3D object-relation graph generation framework that addresses these limitations to robot navigation.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, there are two major limitations in current 3D scene graph generation methods which hinder the growth of this field. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | 3D Semantic Object Extraction We assume that a sensor system, which is composed of an RGBD camera or a LiDAR-camera suite, is ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Semantic, Object, Extraction, assume, sensor, system, composed, RGBD, camera, LiDAR-camera | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | figure, examples, input, images, point, clouds, generated, Graph2Nav | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Semantic, Object, Extraction, assume, sensor, system, composed, RGBD, camera, LiDAR-camera | p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV), p. 1 (I. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: framework, fully, generates, exploits, objects, first, authors, have | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. GRAPH2NAV) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: avoids, previous, training, data, constraints, learning, scene, graphs | p. 1 (Abstract), p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV), p. 4 (III. GRAPH2NAV) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV), p. 4 (III. GRAPH2NAV) |
| Success / guarantee | goal reach with collision-free execution | p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this paper, we present Graph2Nav (Figure 1), a novel real-time 3D object-relation graph generation framework that addresses these limitations to robot navigation.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. GRAPH2NAV)): Our framework fully generates and exploits both 3D objects and ∗The first two authors have equal contribution.

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D object-relation ...
- **p. 3 / III. GRAPH2NAV - extractive PDF cue:** Note Graph2Nav is designed to support various types of pose graph-based SLAM systems, whether it is vision-based, LiDAR-based, or a tightly-coupled LiDAR-vision system.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | To fulfull this goal, we propose Graph2Nav, a novel real-time 3D object-relation graph generation framework that addresses current ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The plan can also be dynamically changed, updated, or replanned during execution, if any failure happens or any ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV), p. 1 (I. INTRODUCTION), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV), p. 1 (I. INTRODUCTION), p. 1 (Abstract), objective p. 1 (Abstract), p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV), p. 4 (III. GRAPH2NAV).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
