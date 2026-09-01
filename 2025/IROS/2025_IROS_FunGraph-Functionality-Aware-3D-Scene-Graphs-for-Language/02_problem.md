# Problem - FunGraph: Functionality Aware 3D Scene Graphs for Language-Prompted Scene Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.07909; PDF retrieval source: https://arxiv.org/pdf/2503.07909. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): One of the key challenges in modeling intra-object relationships is accurately perceiving functional object parts.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The concept of 3D scene graphs is increasingly recognized as a powerful semantic and hierarchical representation of the environment.
- **p. 1 / Abstract - extractive PDF cue:** Current approaches often address this at a coarse, object-level resolution.
- **p. 1 / Abstract - extractive PDF cue:** In contrast, our goal is to develop a representation that enables robots to directly interact with their environment by identifying both the location of functional ...
- **p. 1 / Abstract - extractive PDF cue:** To achieve this, we focus on detecting and storing objects at a finer resolution, focusing on affordance-relevant parts.
- **p. 1 / Abstract - extractive PDF cue:** The primary challenge lies in the scarcity of data that extends beyond instance-level detection and the inherent difficulty of capturing detailed object features using robotic ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** One of the key challenges in modeling intra-object relationships is accurately perceiving functional object parts.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To address this challenge, we utilize SceneFun3D [5], a large-scale dataset that provides sensory data and 3D annotations for functional interactive elements in household environments.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | One of the key challenges in modeling intra-object relationships is accurately perceiving functional object parts. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | input, consists, series, RGB-D, observations, corresponding, camera, poses, Because, cm-resolution | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | One, representation, affordance, grounding, unconstrained, language, queries, produce | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: input, consists, series, RGB-D, observations, corresponding, camera, poses, Because, cm-resolution | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: provides, overview, input, consists, series, RGB-D, observations, corresponding | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Because, cm-resolution, LiDARs, detailed, enough, mm-resolution, scanners, cost-prohibitive | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To address this challenge, we utilize SceneFun3D [5], a large-scale dataset that provides sensory data and 3D annotations for functional interactive elements in household environments.

## What the Paper Changes

PDF contribution framing (p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): 3 provides an overview of our method.

- **p. 3 / III. METHOD - extractive PDF cue:** The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, and corresponding camera ...
- **p. 4 / III. METHOD - extractive PDF cue:** Overview of our functionality-aware 3D scene graph generation pipeline, which consists of three stages: (1) Detection, where instance segmentation and feature extraction are performed to ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Specifically, our contributions are: • A method to detect functional interactive elements from images, predict their affordances, and assign contextualized descriptions. • A framework, FunGraph, ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Therefore, our approach involves generating 2D data for detector fine-tuning and analyzing its impact in 3D.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | It does not rely on segmenting a pre-existing highquality point cloud, which makes it also suitable for robotics ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Fig. 4. Illustration of our context-based label refinement. The VLM is queried to contextualize functional elements with their ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | As is evident from the numbers, ConceptGraphs does not account for the | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We note that the exact numerical results are difficult to compare, as [5] does not release either the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), objective p. 4 (III. METHOD), p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
