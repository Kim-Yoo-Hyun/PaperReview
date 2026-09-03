# ORB-SLAM: A Versatile and Accurate Monocular SLAM System

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1502.00956.
> PDF retrieval source: https://arxiv.org/pdf/1502.00956. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2015 / T-RO
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: SLAM, calibration, geometry
- Official paper: https://arxiv.org/abs/1502.00956
- Full-text retrieval: https://arxiv.org/pdf/1502.00956
- Code/Project: https://github.com/raulmur/ORB_SLAM2
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Unfortunately several factors severely limit its application: lack of loop closing and adequate handling of occlusions, low invariance to viewpoint of the relocalization and the need of human intervention for map bootstrapping.를 문제로 두고, In this work we build on the main ideas of PTAM, the place recognition work of G´alvez-L´opez and Tard´os [5], the scale-aware loop closing of Strasdat et. al [6] and the use ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / Abstract - extractive body cue:** This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments.
- **p. 2 / Abstract - extractive body cue:** The system is robust to severe motion clutter, allows wide baseline loop closing and relocalization, and includes full automatic initialization.
- **p. 2 / Abstract - extractive body cue:** Building on excellent algorithms of recent years, we designed from scratch a novel system that uses the same features for all SLAM tasks: tracking, mapping, ...
- **p. 2 / Abstract - extractive body cue:** A survival of the fittest strategy that selects the points and keyframes of the reconstruction leads to excellent robustness and generates a compact and trackable ...
- **p. 2 / Abstract - extractive body cue:** We present an exhaustive evaluation in 27 sequences from the most popular datasets.
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** Unfortunately several factors severely limit its application: lack of loop closing and adequate handling of occlusions, low invariance to viewpoint of the relocalization and the ...
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** This algorithm, while limited to small scale operation, provides simple but effective methods for keyframe selection, feature matching, point triangulation, camera localization for every frame, ...

## Core Idea

- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** In this work we build on the main ideas of PTAM, the place recognition work of G´alvez-L´opez and Tard´os [5], the scale-aware loop closing of ...
- **p. 2 / Abstract - extractive body cue:** We present an exhaustive evaluation in 27 sequences from the most popular datasets.
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** This allows to match them from wide baselines, boosting the accuracy of BA.
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** The novel procedure to create an initial map is presented in Section IV.
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** The main novelty is that we perform the optimization over the Essential Graph, a sparser subgraph of the covisibility graph which is explained in Section ...
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** Nowadays we know that to achieve accurate results at non-prohibitive computational cost, a real time SLAM algorithm has to provide BA with: • Corresponding observations ...
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** We use the Levenberg-Marquardt algorithm implemented in g2o [37] to carry out all optimizations.
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** We use ORB features [9] which allow real-time performance without GPUs, providing good invariance to changes in viewpoint and illumination. • Real time operation in ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | When a new keyframe is inserted, it is included in the tree linked to the keyframe which shares most point observations, and when a keyframe is erased by the culling policy, the ... | camera/depth stream, pose, map와 language goal | p. 6 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac) |
| State/latent | When, keyframe, inserted, included, tree, linked, shares, most, point, observations, erased, culling | robot pose, free-space/semantic map와 local goal | p. 6 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 4 (III. SYSTEM OVERVIEW) |
| Output/action | Nowadays we know that to achieve accurate results at non-prohibitive computational cost, a real time SLAM algorithm has to provide BA with: • Corresponding observations of scene features (map points) among a ... | collision-free trajectory 또는 velocity command | p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 4 (III. SYSTEM OVERVIEW), p. 5 (III. SYSTEM OVERVIEW) |
| Objective/outcome | In the Appendix we describe the error terms, cost functions, and variables involved in each optimization. | goal reach, safety, localization error와 replanning latency | p. 5 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 5 (III. SYSTEM OVERVIEW) |

## Main Claims and Actual Contribution

- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** In this work we build on the main ideas of PTAM, the place recognition work of G´alvez-L´opez and Tard´os [5], the scale-aware loop closing of ...
- **p. 2 / Abstract - extractive body cue:** We present an exhaustive evaluation in 27 sequences from the most popular datasets.
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** This allows to match them from wide baselines, boosting the accuracy of BA.
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** The novel procedure to create an initial map is presented in Section IV.
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** The main novelty is that we perform the optimization over the Essential Graph, a sparser subgraph of the covisibility graph which is explained in Section ...
- **p. 11 / VIII. EXPERIMENTS - extractive body cue:** In terms of accuracy ORB-SLAM and PTAM are similar in open trajectories, while ORB-SLAM achieves higher accuracy when detecting large loops as in the sequence ...
- **p. 15 / VIII. EXPERIMENTS - extractive body cue:** Performing an additional BA after the pose graph optimization slightly improves the accuracy while increasing substantially the time.
- **p. 15 / VIII. EXPERIMENTS - extractive body cue:** We have noticed that some iterations of full BA slightly improves the accuracy in the trajectories with loops but it has negligible effect in open ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 11 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS) |
| Embodiment/environment | We have performed an extensive experimental validation of our system in the large robot sequence of NewCollege [39], evaluating the general performance of the system, in 16 handheld indoor sequences of the ... | hardware/simulator version and reset protocol | p. 9 (VIII. EXPERIMENTS), p. 12 (VIII. EXPERIMENTS) |
| Dataset/benchmark | System Performance in the NewCollege Dataset The NewCollege dataset [39] contains a 2.2km sequence from a robot traversing a campus and adjacent parks. | role, split, size and leakage | p. 9 (VIII. EXPERIMENTS), p. 12 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS) |
| Metric | In the first experiment we build a map with the first 30 seconds of the sequence fr2 xyz and perform global relocalization with every successive frame and evaluate the accuracy of the ... | definition, denominator, direction and uncertainty | p. 11 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS) |
| Baseline/ablation | We perform the same experiment with PTAM for comparison. | fair input/data/compute/action matching | p. 11 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS), p. 12 (VIII. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 16 / IX. CONCLUSIONS AND DISCUSSION - extractive body cue:** However, direct methods have their own limitations.
- **p. 16 / IX. CONCLUSIONS AND DISCUSSION - extractive body cue:** Future Work The accuracy of our system can still be improved incorporating points at infinity in the tracking.
- **p. 15 / VIII. EXPERIMENTS - extractive body cue:** In sequence 08 there are no loops and drift cannot be corrected, which makes clear the need of loop closures to achieve accurate reconstructions.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** The big loop on the right does not perfectly align because it was traversed in opposite directions and the place recognizer was not able to ...
- **p. 11 / VIII. EXPERIMENTS - extractive body cue:** However, the paper does not give enough details on how those results were obtained, and we have been unable to reproduce them.
- **p. 12 / VIII. EXPERIMENTS - extractive body cue:** During the sequences sitting rpy and walking xyz the map does not grow, because the map created so far explains well the scene.
- **p. 14 / VIII. EXPERIMENTS - extractive body cue:** Sequence 08 does not contains loops and drift (especially scale) is not corrected.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Unfortunately several factors severely limit its application: lack of loop closing and adequate handling of occlusions, low invariance to viewpoint of the relocalization and the need of human intervention for map bootstrapping.를 문제로 두고, In this work we build on the main ideas of PTAM, the place recognition work of G´alvez-L´opez and Tard´os [5], the scale-aware loop closing of Strasdat et. al [6] and the use ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 4 (III. SYSTEM OVERVIEW), p. 1 (Body text (section not recovered)), p. 3 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
