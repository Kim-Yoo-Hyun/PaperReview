# Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p034.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p034.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, 3D perception, object reconstruction, contact-rich manipulation, dynamics, occlusion
- Official paper: https://www.roboticsproceedings.org/rss21/p034.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p034.pdf
- Code/Project: https://vysics-vision-and-physics.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Estimating geometry through contact-rich interactions is not a trivial problem.를 문제로 두고, Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in yellow shows the robot-object interaction,를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce Vysies, a vision-and-physies frame- ‘work for a robot to build an expressive geometry and dynamics model of a single rigid body, using a ...
- **p. 1 / Abstract - extractive body cue:** While the computer vision comhas built powerful visual 3D perception algorithms, cat tered environments with heavy occlusions can limit the visibility of objects of interest.
- **p. 1 / Abstract - extractive body cue:** However, observed motion of partially occluded objects can imply physical interactions took place, sueh as contact with a robot or the environment.
- **p. 1 / Abstract - extractive body cue:** These inferred contacts can supplement the visible geometry with "physible geomet which best explains the observed object motion through physics. ‘Vysies uses a vision-based tracking ...
- **p. 1 / Abstract - extractive body cue:** into optimizing a signed distance object shape.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Estimating geometry through contact-rich interactions is not a trivial problem.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** While some might be recognized from an existing database, others will require physical interaction to be newly understood on the spot.

## Core Idea

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in ...
- **p. 4 / IV. APPROACH - extractive body cue:** Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together such that they ...
- **p. 4 / IV. APPROACH - extractive body cue:** ‘The basis of our contribution is in how we unify the visible and "physible" geometry measurements together. §IV-A di cusses how vision helps in the ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** We first compare the geometry reconstruction of our method with that of shape completion models and single-view 3D generation models.
- **p. 8 / 200.0 BundlesDF - extractive body cue:** Our method recovers the occluded geometry through physics-based reasoning over the observed trajectories, substantially and consistently improving the geometric accuracy in both metrics.
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** Trajectory-Based Dynamics Model Learning
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** ‘System identification is an important robotics subfield that aims to build accurate system models, which can then be leveraged via model-based control techniques.
- **p. 3 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** While [56] avoids the problematic gradients in contactrch scenarios by using a gradient-free search over a discrete set of hypothesized geometries, Vysics leverages smooth, implicit-based ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | portions of its geometry, and observations of the object's state evolution can inject more geometric information when contact, | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. INTRODUCTION), p. 2 (A. Vision-Based Geometry Reconstruction and Completion) |
| State/latent | portions, geometry, observations, object, state, evolution, inject, more, geometric, information, when, contact | geometry, map, object/relationship state | p. 1 (1. INTRODUCTION), p. 2 (A. Vision-Based Geometry Reconstruction and Completion), p. 4 (IV. APPROACH) |
| Output/action | Moreover, advances in image generation models [54], 3D scene representations [44, 32], and large-scale 3D object datasets [22, 21] have spurred 3D generative pipelines [39, 42, 27, 38, 71, 76), though these ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (A. Vision-Based Geometry Reconstruction and Completion), p. 4 (IV. APPROACH), p. 2 (A. Vision-Based Geometry Reconstruction and Completion) |
| Objective/outcome | While [56] avoids the problematic gradients in contactrch scenarios by using a gradient-free search over a discrete set of hypothesized geometries, Vysics leverages smooth, implicit-based losses and thus can directly regress the ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (C. Simultaneous Tracking and Shape Reconstruction) |

## Main Claims and Actual Contribution

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in ...
- **p. 4 / IV. APPROACH - extractive body cue:** Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together such that they ...
- **p. 4 / IV. APPROACH - extractive body cue:** ‘The basis of our contribution is in how we unify the visible and "physible" geometry measurements together. §IV-A di cusses how vision helps in the ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** We first compare the geometry reconstruction of our method with that of shape completion models and single-view 3D generation models.
- **p. 8 / 200.0 BundlesDF - extractive body cue:** Our method recovers the occluded geometry through physics-based reasoning over the observed trajectories, substantially and consistently improving the geometric accuracy in both metrics.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 9: The quantitative comparison of the dynamics prediction accuracy in pose error. Trajectories are predicted by replaying the robot interaction with the estimated geometry ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 10: ‘The dynamics prediction accuracy evaluated by the duration of the simulated trajectory under small pose error.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in interactions with object ‘mask annotations, as well as ... | hardware/simulator version and reset protocol | p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Dataset/benchmark | These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in interactions with object ‘mask annotations, as well as ... | role, split, size and leakage | p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Metric | Fig. 9: The quantitative comparison of the dynamics prediction accuracy in pose error. Trajectories are predicted by replaying the robot interaction with the estimated geometry in simula- tion | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Baseline/ablation | Fig. 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline. In the image view, the mesh projection is shown in green, and ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / B. Dynamics Predictions - extractive body cue:** A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** Under severe occlusion, while the shape completion ‘models can achieve similar or slightly lower chamfer distance than pure vision-based reconstruction, BundleSDF, they fall behind Vysics ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Vision-based shape reconstruction (projection shown in green) can be limited by occlusion. Fusing vision and contact rich physics, our method recovers the occluded ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** There are substantial visual ‘occlusions preventing the camera from directly seeing much of the object geometry.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory.
- **p. 7 / B. Metrics - extractive body cue:** 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Estimating geometry through contact-rich interactions is not a trivial problem.를 문제로 두고, Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in yellow shows the robot-object interaction,를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 4 (IV. APPROACH), p. 2 (C. Simultaneous Tracking and Shape Reconstruction), p. 4 (IV. APPROACH), p. 2 (C. Simultaneous Tracking and Shape Reconstruction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
