# Problem - Lift, Splat, Shoot: Encoding Images from Arbitrary Camera Rigs by Implicitly Unprojecting to 3D

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2008.05711; PDF retrieval source: https://arxiv.org/pdf/2008.05711. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): As a result, the model cannot learn in a data-driven way what the best way is to fuse information across cameras.

## PDF Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Computer vision algorithms generally take as input an image and output either a prediction that is coordinate-frame agnostic - such as in classification [19,30,16,17] - ...
- **p. 2 / 1 Introduction - extractive body cue:** This paradigm does not match the setting for perception in self-driving outof-the-box.
- **p. 2 / 1 Introduction - extractive body cue:** In self-driving, multiple sensors are given as input, each with a different coordinate frame, and perception models are ultimately tasked with producing predictions in a ...
- **p. 2 / 1 Introduction - extractive body cue:** There are many simple, practical strategies for extending the single-image paradigm to the multi-view setting.
- **p. 2 / 1 Introduction - extractive body cue:** For instance, for the problem of 3D object detection from n cameras, one can apply a single-image detector to all input images individually, then rotate ...
- **p. 2 / 1 Introduction - extractive body cue:** As a result, the model cannot learn in a data-driven way what the best way is to fuse information across cameras.
- **p. 2 / 1 Introduction - extractive body cue:** It also means backpropagation cannot be used to automatically improve the perception system using feedback from the downstream planner.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | As a result, the model cannot learn in a data-driven way what the best way is to fuse information across cameras. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Computer vision algorithms generally take as input an image and output either a prediction that is coordinate-frame agnostic - such as in ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Computer, vision, algorithms, generally, take, input, image, output, either, prediction | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Splat, Pillar, Pooling, follow, pointpillars, architecture, convert, large | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Computer, vision, algorithms, generally, take, input, image, output, either, prediction | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: section, present, learning, bird, s-eye-view, representations, scenes, image | p. 4 (3 Method), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: definition, enables, learn, interpretable, spatial, cost, function, without | p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 Method), p. 8 (3 Method), p. 5 (3 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 10 (Figure/Table caption), p. 10 (6 DOF localization and rasterize), p. 6 (3 Method) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** It also means backpropagation cannot be used to automatically improve the perception system using feedback from the downstream planner.

## What the Paper Changes

PDF body contribution framing (p. 4 (3 Method), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 6 (3 Method)): In this section, we present our approach for learning bird's-eye-view representations of scenes from image data captured by an arbitrary camera rig.

- **p. 2 / 1 Introduction - extractive body cue:** We propose a model named "Lift-Splat" that preserves the 3 symmetries identified above by design while also being end-to-end differentiable.
- **p. 2 / 1 Introduction - extractive body cue:** In Section 3.3, we propose a method for "shooting" proposal trajectories into this reference plane for interpretable end-to-end motion planning.
- **p. 3 / 1 Introduction - extractive body cue:** We present empirical evidence in Sec 5 that our model learns an effective mechanism for fusing information from a distribution of possible inputs.
- **p. 6 / 3 Method - extractive body cue:** 3.3 Shoot: Motion Planning Key aspect of our Lift-Splat model is that it enables end-to-end cost map learning for motion planning from camera-only input.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | We present methods for training our model that make the network robust to simple models of calibration noise. | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Our model does not have access to the speed of the car so it is compelling that the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | 5.3 Robustness Because the bird's-eye-view CNN learns from data how to fuse information across cameras, we can train ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | On the left, we show that by training with a large amount of noise in the extrinsics (blue), ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method), objective p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
