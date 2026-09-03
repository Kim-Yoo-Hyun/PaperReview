# ElasticFusion: Dense SLAM Without A Pose Graph

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss11/p01.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss11/p01.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2015 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, SLAM, RGB-D, 3D reconstruction
- Official paper: https://www.roboticsproceedings.org/rss11/p01.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss11/p01.pdf
- Code/Project: https://github.com/mp3guy/ElasticFusion
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing dense SLAM methods suitable for incremental, real-time operation struggle when the sensor makes movements which are both of extended duration and often criss-cross loop back on themselves.를 문제로 두고, In the following, we summarise the key elements of our method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a novel approach to real-time dense visual SLAM.
- **p. 1 / Abstract - extractive body cue:** Our system is capable of capturing comprehensive dense globally consistent surfel-based maps of room scale environments explored using an RGB-D camera in an incremental online ...
- **p. 1 / Abstract - extractive body cue:** This is accomplished by using dense frame-tomodel camera tracking and windowed surfel-based fusion coupled with frequent model refinement through non-rigid surface deformations.
- **p. 1 / Abstract - extractive body cue:** Our approach applies local model-to-model surface loop closure optimisations as often as possible to stay close to the mode of the map distribution, while utilising ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In dense 3D SLAM, a space is mapped by fusing the data from a moving sensor into a representation of the continuous surfaces it contains, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, existing dense SLAM methods suitable for incremental, real-time operation struggle when the sensor makes movements which are both of extended duration and often criss-cross ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** As we show in our evaluation of the system in Section VII, this approach to dense SLAM achieves state-of-the-art performance with trajectory estimation results on ...

## Core Idea

- **p. 2 / II. APPROACH OVERVIEW - extractive body cue:** In the following, we summarise the key elements of our method.
- **p. 2 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** This component of our method is inspired by the surfelbased fusion system of Keller et al.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Pose graph SLAM systems primarily focus on optimising the camera trajectory, whereas our approach (utilising a deformation graph) instead focuses on optimising the map.
- **p. 2 / II. APPROACH OVERVIEW - extractive body cue:** We adopt an architecture which is typically found in realtime dense visual SLAM systems that alternates between tracking and mapping [15, 25, 9, 8, 2, ...
- **p. 2 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** If registration is successful, a loop has been closed to the older inactive model and the entire model is non-rigidly deformed into place to reflect ...
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** In the following section we describe our fused map representation and method for predictive tracking.
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** If a match is detected, register the views together and check if the registration is globally consistent with the model's geometry.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As we show in our evaluation of the system in Section VII, this approach to dense SLAM achieves state-of-the-art performance with trajectory estimation results on par with or better than existing dense ... | camera/depth stream, pose, map와 language goal | p. 2 (I. INTRODUCTION), p. 2 (II. APPROACH OVERVIEW) |
| State/latent | evaluation, system, Section, VII, dense, SLAM, achieves, state-of-the-art, performance, trajectory, estimation, better | robot pose, free-space/semantic map와 local goal | p. 2 (I. INTRODUCTION), p. 2 (II. APPROACH OVERVIEW), p. 1 (I. INTRODUCTION) |
| Output/action | We mainly use CUDA to implement our tracking reduction process and the OpenGL Shading Language for view prediction and map management. | collision-free trajectory 또는 velocity command | p. 2 (II. APPROACH OVERVIEW), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | goal reach, safety, localization error와 replanning latency | goal reach, safety, localization error와 replanning latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / II. APPROACH OVERVIEW - extractive body cue:** In the following, we summarise the key elements of our method.
- **p. 2 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** This component of our method is inspired by the surfelbased fusion system of Keller et al.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Pose graph SLAM systems primarily focus on optimising the camera trajectory, whereas our approach (utilising a deformation graph) instead focuses on optimising the map.
- **p. 7 / VII. EVALUATION - extractive body cue:** Interestingly our frame-to-model only results are also comparable in performance, whereas a uniform increase in accuracy is achieved when active to inactive model deformations are ...
- **p. 7 / VII. EVALUATION - extractive body cue:** These results show that our trajectory estimation performance is on par with or better than existing state-of-the-art systems that Fig.
- **p. 8 / VII. EVALUATION - extractive body cue:** It is also shown that our surface reconstruction results are superior to all other systems.
- **p. 8 / VII. EVALUATION - extractive body cue:** On surface reconstruction, local loops only scores 0.099m and global loops only scores 0.103m.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION) |
| Embodiment/environment | The Lab dataset contains a very loopy trajectory around a large office environment with many global and local loop closures. | hardware/simulator version and reset protocol | p. 8 (VII. EVALUATION), p. 7 (VII. EVALUATION) |
| Dataset/benchmark | Trajectory Estimation To evaluate the trajectory estimation performance of our approach we test our system on the RGB-D benchmark of Sturm et al. | role, split, size and leakage | p. 8 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 8 (VII. EVALUATION) |
| Metric | We evaluate the performance of our system both quantitatively and qualitatively in terms of trajectory estimation, surface reconstruction accuracy and computational performance. | definition, denominator, direction and uncertainty | p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 8 (VII. EVALUATION) |
| Baseline/ablation | These results show that our trajectory estimation performance is on par with or better than existing state-of-the-art systems that Fig. | fair input/data/compute/action matching | p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VIII. CONCLUSION - extractive body cue:** In future work we wish to address the problem of map scalability beyond whole rooms and also investigate the problem of dense globally consistent SLAM ...
- **p. 7 / VII. EVALUATION - extractive body cue:** We evaluate our approach on all four trajectories in the living room scene (including synthetic noise) providing surface reconstruction accuracy results in comparison to the ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing dense SLAM methods suitable for incremental, real-time operation struggle when the sensor makes movements which are both of extended duration and often criss-cross loop back on themselves.를 문제로 두고, In the following, we summarise the key elements of our method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
