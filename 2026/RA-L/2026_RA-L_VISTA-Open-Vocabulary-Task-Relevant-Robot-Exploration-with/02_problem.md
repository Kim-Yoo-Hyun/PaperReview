# Problem - VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2507.01125. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION)): Prior work in robot exploration broadly uses traditional 3D scene representations, such as occupancy grids and voxel grids.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present VISTA (Viewpoint-based Image selection with Semantic Task Awareness), an active exploration method for robots to plan informative trajectories that improve 3D map quality ...
- **p. 1 / Abstract - extractive body cue:** Given an open-vocabulary search instruction (e.g., "find a person"), VISTA enables a robot to explore its environment to search for the object of interest, while ...
- **p. 1 / Abstract - extractive body cue:** The robot navigates its environment by planning receding-horizon trajectories that prioritize semantic similarity to the query and exploration of unseen regions of the environment.
- **p. 1 / Abstract - extractive body cue:** To evaluate trajectories, VISTA introduces a novel, efficient viewpoint-semantic coverage metric that quantifies both the geometric view diversity and task relevance in the 3D scene.
- **p. 1 / Abstract - extractive body cue:** On static datasets, our coverage metric outperforms state-of-the-art baselines, FisherRF and Bayes' Rays, in computation speed and reconstruction quality.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Prior work in robot exploration broadly uses traditional 3D scene representations, such as occupancy grids and voxel grids.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In each voxel, the geometric uncertainty is the minimum angular separation between the test viewpoint and all view angles from which that voxel has appeared ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Prior work in robot exploration broadly uses traditional 3D scene representations, such as occupancy grids and voxel grids. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | As the robot moves, it collects full pose odometry information along with RGB and depth images in order to train a 3DGS ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | robot, moves, collects, full, pose, odometry, information, along, RGB, depth | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Once, robot, receives, input, query, must, then, construct | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: robot, moves, collects, full, pose, odometry, information, along, RGB, depth | p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION) |
| Decision / output variable | geometry/map/query r; body terms: present, VISTA, algorithm, Viewpoint-based, Image, Selection, Semantic, Task | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: updates, assume, motion, robot, restricted, axes | p. 3 (III. PROBLEM FORMULATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. PROBLEM FORMULATION) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** In each voxel, the geometric uncertainty is the minimum angular separation between the test viewpoint and all view angles from which that voxel has appeared ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, VISTA samples trajectories, and selects those with viewpoints that maximize a weighted combination of geometric uncertainty and semantic relevance, ultimately guiding the robot toward ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We consider a robotic exploration problem in which a robot has an onboard, forward-facing RGB-D camera with reliable state estimation.

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION)): We present VISTA, an algorithm for Viewpoint-based Image Selection with Semantic Task Awareness.

- **p. 2 / I. INTRODUCTION - extractive body cue:** We introduce: 1) an efficient information metric that combines view angle diversity and semantic task relevance stored on a voxel grid that can be recursively ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through an experimental campaign with a total of 36 hardware executions, we show that VISTA outperforms state-of-the-art baselines, achieving 6x better success rates in environments ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** This explicit representation not only enables Gaussian Splatting to avoid unnecessary computation involving empty space, but it also enables the utilization of fast tile-based rasterization.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | We evaluate each method using the standard metrics: Peak-Signal-Noise-Ratio (PSNR), Learned Perceptuation Image Patch Similarity (LPIPS), and Structural ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Through these experiments, we find that all methods have some successes on the easy low-occlusion map domain. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Fig. 4. The top row shows our three environments and two robots, with the search object in a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), interface p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), objective p. 3 (III. PROBLEM FORMULATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** We consider a robotic exploration problem in which a robot has an onboard, forward-facing RGB-D camera with reliable state estimation. (p. 3, III. PROBLEM FORMULATION).
- **Formulation-changing contribution:** We present VISTA, an algorithm for Viewpoint-based Image Selection with Semantic Task Awareness. (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** In the second map, we expect methods that do not account for geometric information gain to struggle to find the query object. (p. 6, V. RESULTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
