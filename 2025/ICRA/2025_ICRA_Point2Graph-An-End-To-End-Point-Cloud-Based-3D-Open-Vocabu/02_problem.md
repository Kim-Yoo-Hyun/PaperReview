# Problem - Point2Graph: An End-To-End Point Cloud-Based 3D Open-Vocabulary Scene Graph for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2409.10350v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Lacking 3D-text pair data leads to poor performance in 3D object and room segmentation and classication.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Current open-vocabulary scene graph generation algorithms highly rely on both 3D scene point cloud data and posed RGB-D images and thus have limited applications in ...
- **p. 1 / Abstract - extractive body cue:** To solve this problem, we propose Point2Graph, a novel end-to-end point cloud-based 3D open-vocabulary scene graph generation framework in which the requirement of posed RGB-D ...
- **p. 1 / Abstract - extractive body cue:** This hierarchical framework contains room and object detection/segmentation and openvocabulary classication.
- **p. 1 / Abstract - extractive body cue:** For the room layer, we leverage the advantage of merging the geometry-based border detection algorithm with the learning-based region detection to segment rooms and create ...
- **p. 1 / Abstract - extractive body cue:** In addition, we create an end-toend pipeline for the object layer to detect and classify 3D objects based solely on 3D point cloud data.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Lacking 3D-text pair data leads to poor performance in 3D object and room segmentation and classication.
- **p. 1 / I. INTRODUCTION - extractive body cue:** For example, the point clouds created from a Building Information Model (BIM) or LiDAR sensors often lack the RGB-D images and their pose data [13], ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Lacking 3D-text pair data leads to poor performance in 3D object and room segmentation and classication. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | First, the input point cloud is segmented into N slices along the z-axis, with each slice projected onto an occupancy grid map ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | First, input, point, cloud, segmented, slices, along, z-axis, slice, projected | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Speci, cally, model, takes, input, ltered, point, cloud | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: First, input, point, cloud, segmented, slices, along, z-axis, slice, projected | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY) |
| Decision / output variable | path/waypoint/velocity; body terms: Generally, speaking, framework, consists, room, segmentation, classi, cation | p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Then, argmax, majority, voting, applied, type, room, Next | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | goal reach with collision-free execution | p. 6 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** For example, the point clouds created from a Building Information Model (BIM) or LiDAR sensors often lack the RGB-D images and their pose data [13], ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY)): Generally speaking, our framework consists of a room segmentation and classication module and an object detection and classication module.

- **p. 4 / III. METHODOLOGY - extractive body cue:** Object-Level Detection and Classication After getting the segmentation result for each room, our approach mainly consists of two steps, where the rst step deals with ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** In this section, we present our design of Point2Graph, which builds a compact and enriched open-vocabulary 3D scene graph with solely 3D scene model input.
- **p. 4 / III. METHODOLOGY - extractive body cue:** 5: Overview of the 3D open-vocabulary detection pipeline: It consists of two stages: (1) detection and localization using class-agnostic bounding boxes and DBSCAN ltering for ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Voronoi Navigation Graph In order to let a robot navigate in the area where our scene graph is built, we propose a navigation graph based ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Nevertheless, Point2Graph has its limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In conclusion, this work presents the Point2Graph framework, which addresses the limitations of current openvocabulary 3D scene graph ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Our proposed "Snap-Lookup" pipeline, which incorporates room visual features into type inference, can differentiate between various types of ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), objective p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
