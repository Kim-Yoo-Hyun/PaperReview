# Problem - KinectFusion: Real-Time Dense Surface Mapping and Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.microsoft.com/en-us/research/publication/kinectfusion-real-time-dense-surface-mapping-and-tracking/; PDF retrieval source: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ismar2011.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 6 (3.1 Preliminaries), p. 6 (3.1 Preliminaries)): While this work is very promising for AR, dense scene reconstruction in real-time remains a challenge for passive monocular systems which assume the availability of the right type of camera ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** We present a system for accurate real-time mapping of complex and arbitrary indoor scenes in variable lighting conditions, using only a moving low-cost depth camera ...
- **p. 1 / ABSTRACT - extractive body cue:** We fuse all of the depth data streamed from a Kinect sensor into a single global implicit surface model of the observed scene in real-time.
- **p. 1 / ABSTRACT - extractive body cue:** The current sensor pose is simultaneously obtained by tracking the live depth frame relative to the global model using a coarse-to-fine iterative closest point (ICP) ...
- **p. 1 / ABSTRACT - extractive body cue:** We demonstrate the advantages of tracking against the growing full surface model compared with frame-to-frame tracking, obtaining tracking and mapping results in constant time within ...
- **p. 1 / ABSTRACT - extractive body cue:** We also show both qualitative and quantitative results relating to various aspects of our tracking and mapping system.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While this work is very promising for AR, dense scene reconstruction in real-time remains a challenge for passive monocular systems which assume the availability of ...
- **p. 2 / 2 BACKGROUND - extractive body cue:** While the quality of this depth map is generally remarkable given the cost of the device, a number of challenges remain.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While this work is very promising for AR, dense scene reconstruction in real-time remains a challenge for passive monocular systems which assume ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Later, it was discovered to be practically advantageous to abandon the propagation of a full probabilistic state and instead to run two ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Later, discovered, practically, advantageous, abandon, propagation, full, probabilistic, state, instead | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Sensor, Pose, Estimation, Live, camera, localisation, involves, estimating | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Later, discovered, practically, advantageous, abandon, propagation, full, probabilistic, state, instead | p. 2 (2 BACKGROUND), p. 4 (3.1 Preliminaries), p. 6 (3.1 Preliminaries) |
| Decision / output variable | path/waypoint/velocity; body terms: present, detailed, analysis, what, believe, first, system, permits | p. 2 (1 INTRODUCTION), p. 6 (3.1 Preliminaries), p. 7 (3.1 Preliminaries) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Storing, weight, value, allows, important, aspect, global, minimum | p. 5 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), p. 4 (3.1 Preliminaries), p. 5 (3.1 Preliminaries) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), p. 7 (3.1 Preliminaries) |
| Success / guarantee | goal reach with collision-free execution | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 2 BACKGROUND - extractive body cue:** While the quality of this depth map is generally remarkable given the cost of the device, a number of challenges remain.
- **p. 3 / 2 BACKGROUND - extractive body cue:** The restrictive non mobile range sensor prototype and lack of global pose optimisation to reduce drift prevented them from using the system for reconstructing larger ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** (Left) pixel iteration count are shown where for each pixel the ray is traversed in steps of at most one voxel (white equals 480 increments ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** (middle) ray marching steps are drastically reduced by skipping empty space according to the minimum truncation µ (white equals 70 iterations and black 10 ≈6× ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 6 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), p. 2 (1 INTRODUCTION), p. 4 (3.1 Preliminaries)): In this paper we present a detailed method with analysis of what we believe is the first system which permits real-time, dense volumetric reconstruction of complex room-sized scenes using a ...

- **p. 6 / 3.1 Preliminaries - extractive body cue:** Second, modern GPU hardware enables a fully parrallelised processing pipeline, so that the data association and point-plane optimisation can use all of the available surface ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** The symmetry of the system enables operations and memory to be saved and the final sum is obtained using a parallel tree-based reduction [13], to ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A key novelty is that tracking, performed at 30Hz frame-rate, is always relative to the fully up-to-date fused dense model, and we demonstrate the advantages ...
- **p. 4 / 3.1 Preliminaries - extractive body cue:** An example given in Figure 4 demonstrates how the TSDF allows us to represent arbitrary genus surfaces as zero crossings within the volume.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | 4.3 Observations and Failure Modes Our system is robust to a wide range of practical conditions in terms ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Both outcomes will lead to a reduced quality reconstruction and tracking failure. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The main failure case in standard indoor scenes is when the sensor is faced by a large planar ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | If either test fails, the system is placed into re-localisation mode. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (2 BACKGROUND), p. 4 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), p. 4 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 6 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), interface p. 2 (2 BACKGROUND), p. 4 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), p. 4 (3 METHOD), objective p. 5 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), p. 4 (3.1 Preliminaries), p. 5 (3.1 Preliminaries).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
