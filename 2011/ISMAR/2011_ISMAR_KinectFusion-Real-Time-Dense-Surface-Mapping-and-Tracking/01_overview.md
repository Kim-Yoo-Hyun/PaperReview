# KinectFusion: Real-Time Dense Surface Mapping and Tracking

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.microsoft.com/en-us/research/publication/kinectfusion-real-time-dense-surface-mapping-and-tracking/.
> PDF retrieval source: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ismar2011.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2011 / ISMAR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, SLAM, RGB-D, 3D reconstruction
- Official paper: https://www.microsoft.com/en-us/research/publication/kinectfusion-real-time-dense-surface-mapping-and-tracking/
- Full-text retrieval: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ismar2011.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 While this work is very promising for AR, dense scene reconstruction in real-time remains a challenge for passive monocular systems which assume the availability of the right type of camera motion and ...를 문제로 두고, In this paper we present a detailed method with analysis of what we believe is the first system which permits real-time, dense volumetric reconstruction of complex room-sized scenes using a handheld Kinect ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We present a system for accurate real-time mapping of complex and arbitrary indoor scenes in variable lighting conditions, using only a moving low-cost depth camera ...
- **p. 1 / ABSTRACT - extractive body cue:** We fuse all of the depth data streamed from a Kinect sensor into a single global implicit surface model of the observed scene in real-time.
- **p. 1 / ABSTRACT - extractive body cue:** The current sensor pose is simultaneously obtained by tracking the live depth frame relative to the global model using a coarse-to-fine iterative closest point (ICP) ...
- **p. 1 / ABSTRACT - extractive body cue:** We demonstrate the advantages of tracking against the growing full surface model compared with frame-to-frame tracking, obtaining tracking and mapping results in constant time within ...
- **p. 1 / ABSTRACT - extractive body cue:** We also show both qualitative and quantitative results relating to various aspects of our tracking and mapping system.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While this work is very promising for AR, dense scene reconstruction in real-time remains a challenge for passive monocular systems which assume the availability of ...
- **p. 2 / 2 BACKGROUND - extractive body cue:** While the quality of this depth map is generally remarkable given the cost of the device, a number of challenges remain.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper we present a detailed method with analysis of what we believe is the first system which permits real-time, dense volumetric reconstruction of ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** Second, modern GPU hardware enables a fully parrallelised processing pipeline, so that the data association and point-plane optimisation can use all of the available surface ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** The symmetry of the system enables operations and memory to be saved and the final sum is obtained using a parallel tree-based reduction [13], to ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A key novelty is that tracking, performed at 30Hz frame-rate, is always relative to the fully up-to-date fused dense model, and we demonstrate the advantages ...
- **p. 4 / 3.1 Preliminaries - extractive body cue:** An example given in Figure 4 demonstrates how the TSDF allows us to represent arbitrary genus surfaces as zero crossings within the volume.
- **p. 6 / 3.1 Preliminaries - extractive body cue:** The point-plane error metric in combination with correspondences obtained using projective data association was first demonstrated in a real time modelling system by [23] where ...
- **p. 4 / 3 METHOD - extractive body cue:** Surface reconstruction update: The global scene fusion process, where given the pose determined by tracking the depth data from a new sensor frame, the surface ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** Many tracking algorithms use feature selection to improve speed by reducing the number of points for which data association need be performed.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Later, it was discovered to be practically advantageous to abandon the propagation of a full probabilistic state and instead to run two procedures in alternation or in parallel: tracking, estimating the pose ... | camera/depth stream, pose, map와 language goal | p. 2 (2 BACKGROUND), p. 4 (3.1 Preliminaries) |
| State/latent | Later, discovered, practically, advantageous, abandon, propagation, full, probabilistic, state, instead, procedures, alternation | robot pose, free-space/semantic map와 local goal | p. 2 (2 BACKGROUND), p. 4 (3.1 Preliminaries), p. 6 (3.1 Preliminaries) |
| Output/action | We will also use a dot notation to denote homogeneous vectors ˙u := (u⊤/1)⊤ 3.2 Surface Measurement At time k a measurement comprises a raw depth map Rk which provides calibrated depth ... | collision-free trajectory 또는 velocity command | p. 4 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), p. 4 (3 METHOD) |
| Objective/outcome | Storing a weight Wk(p) with each value allows an important aspect of the global minimum of the convex L2 de-noising metric to be exploited for real-time fusion; that the solution can be ... | goal reach, safety, localization error와 replanning latency | p. 5 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), p. 4 (3.1 Preliminaries) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper we present a detailed method with analysis of what we believe is the first system which permits real-time, dense volumetric reconstruction of ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** Second, modern GPU hardware enables a fully parrallelised processing pipeline, so that the data association and point-plane optimisation can use all of the available surface ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** The symmetry of the system enables operations and memory to be saved and the final sum is obtained using a parallel tree-based reduction [13], to ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A key novelty is that tracking, performed at 30Hz frame-rate, is always relative to the fully up-to-date fused dense model, and we demonstrate the advantages ...
- **p. 4 / 3.1 Preliminaries - extractive body cue:** An example given in Figure 4 demonstrates how the TSDF allows us to represent arbitrary genus surfaces as zero crossings within the volume.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Rapid accumulation of errors results in the non-circular trajectory and poor reconstruction is apparent (though see later Figure 11 where frame-skipping is shown to improve ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We have conducted a number of experiments to investigate the performance of our system.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** But the frame-model tracking results in drift-free operation without explicit global optimisation.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | Finally, for comparison, a new longer dataset of MN frames was processed, where a user moved the sensor over the scene without precise repetition. | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Dataset/benchmark | 6 CONCLUSIONS The availability of commodity depth sensors such as Kinect has the potential to revolutionise the fields of robotics and human-computer interaction. | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Metric | Rapid accumulation of errors results in the non-circular trajectory and poor reconstruction is apparent (though see later Figure 11 where frame-skipping is shown to improve this). | definition, denominator, direction and uncertainty | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Baseline/ablation | Note that this can be compared with the reconstruction from the same number of MN different frames of the same scene obtained from hand-held sensor motion in Figure 9. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.3 Observations and Failure Modes Our system is robust to a wide range of practical conditions in terms of scene structure and camera motion.
- **p. 7 / 3.1 Preliminaries - extractive body cue:** Both outcomes will lead to a reduced quality reconstruction and tracking failure.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The main failure case in standard indoor scenes is when the sensor is faced by a large planar scene which fills most of its field ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** If either test fails, the system is placed into re-localisation mode.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 While this work is very promising for AR, dense scene reconstruction in real-time remains a challenge for passive monocular systems which assume the availability of the right type of camera motion and ...를 문제로 두고, In this paper we present a detailed method with analysis of what we believe is the first system which permits real-time, dense volumetric reconstruction of complex room-sized scenes using a handheld Kinect ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 6 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), p. 6 (3.1 Preliminaries) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
