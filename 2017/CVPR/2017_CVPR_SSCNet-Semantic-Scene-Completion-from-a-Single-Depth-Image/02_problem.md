# Problem - SSCNet: Semantic Scene Completion from a Single Depth Image

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1611.08974; PDF retrieval source: https://arxiv.org/pdf/1611.08974. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): However, if we consider the context due to surrounding objects, such as the table and floor, the problem is much easier.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This paper focuses on semantic scene completion, a task for producing a complete 3D voxel representation of volumetric occupancy and semantic labels for a scene ...
- **p. 1 / Abstract - extractive body cue:** Previous work has considered scene completion and semantic labeling of depth maps separately.
- **p. 1 / Abstract - extractive body cue:** However, we observe that these two problems are tightly intertwined.
- **p. 1 / Abstract - extractive body cue:** To leverage the coupled nature of these two tasks, we introduce the semantic scene completion network (SSCNet), an end-to-end 3D convolutional network that takes a ...
- **p. 1 / Abstract - extractive body cue:** Our network uses a dilation-based 3D context module to efficiently expand the receptive field and enable 3D context learning.
- **p. 2 / 1. Introduction - extractive body cue:** However, if we consider the context due to surrounding objects, such as the table and floor, the problem is much easier.
- **p. 2 / 1. Introduction - extractive body cue:** First, how do we effectively capture contextual information from 3D volumetric data, where the signal is sparse and lacks high frequency detail?

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, if we consider the context due to surrounding objects, such as the table and floor, the problem is much easier. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | (a) Input single-view depth map (b) Visible surface from the depth map; color is for visualization only. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Input, single-view, depth, Visible, surface, color, visualization, only, motivation, goal | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | then, choose, camera, poses, distribution, NYU-Depth, dataset, render | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Input, single-view, depth, Visible, surface, color, visualization, only, motivation, goal | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (4.2. Synthetic depth map generation) |
| Decision / output variable | geometry/map/query r; body terms: provide, training, data, network, introduce, SUNCG, manually, created | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: loss, function, network, voxel-wise, softmax, wijkLsm, pijk, yijk | p. 5 (3.2. Network architecture), p. 4 (3.2. Network architecture), p. 4 (3.2. Network architecture) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Network architecture), p. 5 (3.2. Network architecture), p. 4 (3.2. Network architecture) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (5.1. Experimental results), p. 6 (5. Evaluation), p. 6 (5. Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** First, how do we effectively capture contextual information from 3D volumetric data, where the signal is sparse and lacks high frequency detail?
- **p. 1 / 1. Introduction - extractive body cue:** Prior work is limited to address only part of this problem as shown in FigFigure 1.
- **p. 1 / 1. Introduction - extractive body cue:** Therefore, the two problems of predicting voxel occupancy and identifying object semantics are strongly coupled.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (4. Synthesizing training data), p. 5 (4. Synthesizing training data)): To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and semantic annotations.

- **p. 1 / 1. Introduction - extractive body cue:** Similarly, for a robot, the ability to infer complete 3D shape from partial observations is necessary for low-level tasks such as grasping and obstacle avoidance ...
- **p. 2 / 1. Introduction - extractive body cue:** In support of that goal, we design a dilation-based 3D context module that enables efficient context learning with large receptive fields.
- **p. 5 / 4. Synthesizing training data - extractive body cue:** In this paper, we present a new large-scale synthetic 3D scene dataset, from which we obtain a large amount of training data with synthetically rendered ...
- **p. 5 / 4. Synthesizing training data - extractive body cue:** During the task, we show a set of top view renderings of each floor and ask turkers to vote whether this is a valid apartment ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | While Firman et al. produces good results for many cases, their approach fails when the scene becomes complex. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For instance, their algorithm fails to complete half of the bed in the first row of Figure 7, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In contrast, our algorithm is based on only depth and does not use additional mesh model at test ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Moreover, since our method does not require the model fitting step it is much faster at 7s compared ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (4.2. Synthetic depth map generation), p. 4 (3.2. Network architecture). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (4.2. Synthetic depth map generation), p. 4 (3.2. Network architecture), objective p. 5 (3.2. Network architecture), p. 4 (3.2. Network architecture), p. 4 (3.2. Network architecture).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
