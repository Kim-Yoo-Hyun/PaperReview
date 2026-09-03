# LSD-SLAM: Large-Scale Direct Monocular SLAM

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://cvg.cit.tum.de/research/vslam/lsdslam.
> PDF retrieval source: https://jakobengel.github.io/pdf/engel14eccv.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2014 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, SLAM, monocular geometry, 3D reconstruction
- Official paper: https://cvg.cit.tum.de/research/vslam/lsdslam
- Full-text retrieval: https://jakobengel.github.io/pdf/engel14eccv.pdf
- Code/Project: https://github.com/tum-vision/lsd_slam
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 One of the major benefits of monocular SLAM - and simultaneously one of the biggest challenges - comes with the inherent scale-ambiguity: The scale of the world cannot be observed and drifts ...를 문제로 두고, We propose a direct (feature-less) monocular SLAM algorithm which, in contrast to current state-of-the-art regarding direct methods, allows to build large-scale, consistent maps of the environment.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Real-time monocular Simultaneous Localization and Mapping (SLAM) and 3D reconstruction have become increasingly popular research topics.
- **p. 1 / 1 Introduction - extractive body cue:** Two major reasons are (1) their use in robotics, in particular to navigate unmanned aerial vehicles (UAVs) [10, 8, 1], and (2) augmented and virtual ...
- **p. 1 / 1 Introduction - extractive body cue:** One of the major benefits of monocular SLAM - and simultaneously one of the biggest challenges - comes with the inherent scale-ambiguity: The scale of ...
- **p. 1 / 1 Introduction - extractive body cue:** The advantage is that this allows to seamlessly switch between differently scaled environments, such as a desk environment indoors and large-scale outdoor environments.
- **p. 1 / 1 Introduction - extractive body cue:** Scaled sensors on the other hand, such as depth or stereo cameras, have a limited range at which they can provide reliable measurements and hence ...
- **p. 4 / 2 Preliminaries - extractive body cue:** 2.2), and briefly introduce propagation of uncertainty (Sec.
- **p. 5 / 2 Preliminaries - extractive body cue:** (7) In order to be robust to outliers arising e.g. from occlusions or reflections, different weighting-schemes [14] have been proposed, resulting in an iteratively reweighted ...

## Core Idea

- **p. 1 / Body text (section not recovered) - extractive body cue:** We propose a direct (feature-less) monocular SLAM algorithm which, in contrast to current state-of-the-art regarding direct methods, allows to build large-scale, consistent maps of the ...
- **p. 6 / 2 Preliminaries - extractive body cue:** 3.1 The Complete Method The algorithm consists of three major components: tracking, depth map estimation and map optimization as visualized in Fig.
- **p. 7 / 2 Preliminaries - extractive body cue:** 3.2 Map Representation The map is represented as a pose graph of keyframes: Each keyframe Ki consists of a camera image Ii : Ωi →R, ...
- **p. 1 / 1 Introduction - extractive body cue:** The advantage is that this allows to seamlessly switch between differently scaled environments, such as a desk environment indoors and large-scale outdoor environments.
- **p. 6 / 2 Preliminaries - extractive body cue:** The three main components of the algorithm are then described in Sec.
- **p. 7 / 2 Preliminaries - extractive body cue:** Given sufficient translational camera movement in the first seconds, the algorithm "locks" to a certain configuration, and after a couple of keyframe propagations converges to ...
- **p. 4 / 2 Preliminaries - extractive body cue:** (1) During optimization, a minimal representation for the camera pose is required, which is given by the corresponding element ξ ∈se(3) of the associated Lie-algebra.
- **p. 4 / 2 Preliminaries - extractive body cue:** In particular, we summarize the representation of 3D poses as elements of Lie-Algebras (Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2.3 Propagation of Uncertainty Propagation of uncertainty is a statistical tool to derive the uncertainty of the output of a function f(X), caused by uncertainty on its input X. | camera/depth stream, pose, map와 language goal | p. 6 (2 Preliminaries), p. 7 (2 Preliminaries) |
| State/latent | Propagation, Uncertainty, statistical, tool, derive, output, function, caused, input, Map, Representation, represented | robot pose, free-space/semantic map와 local goal | p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 4 (2 Preliminaries) |
| Output/action | 3.2 Map Representation The map is represented as a pose graph of keyframes: Each keyframe Ki consists of a camera image Ii : Ωi →R, an inverse depth map Di : ΩDi ... | collision-free trajectory 또는 velocity command | p. 7 (2 Preliminaries), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries) |
| Objective/outcome | 2.2 Weighted Gauss-Newton Optimization on Lie-Manifolds Two images are aligned by Gauss-Newton minimization of the photometric error E(ξ) = X i (Iref(pi) -I(ω(pi, Dref(pi), ξ)))2 / {z } =:r2 i (ξ) , ... | goal reach, safety, localization error와 replanning latency | p. 5 (2 Preliminaries), p. 4 (2 Preliminaries), p. 7 (2 Preliminaries) |

## Main Claims and Actual Contribution

- **p. 1 / Body text (section not recovered) - extractive body cue:** We propose a direct (feature-less) monocular SLAM algorithm which, in contrast to current state-of-the-art regarding direct methods, allows to build large-scale, consistent maps of the ...
- **p. 6 / 2 Preliminaries - extractive body cue:** 3.1 The Complete Method The algorithm consists of three major components: tracking, depth map estimation and map optimization as visualized in Fig.
- **p. 7 / 2 Preliminaries - extractive body cue:** 3.2 Map Representation The map is represented as a pose graph of keyframes: Each keyframe Ki consists of a camera image Ii : Ωi →R, ...
- **p. 1 / 1 Introduction - extractive body cue:** The advantage is that this allows to seamlessly switch between differently scaled environments, such as a desk environment indoors and large-scale outdoor environments.
- **p. 12 / 4 Results - extractive body cue:** 4.1 Qualitative Results on Large Trajectories We tested the algorithm on several long and challenging trajectories, which include many camera rotations, large scale changes and ...
- **p. 13 / 4 Results - extractive body cue:** 9: Results on the TUM RGB-D benchmark [25], and two simulated sequences from [12], measured as absolute trajectory RMSE (cm).
- **p. 13 / 4 Results - extractive body cue:** For comparison we show respective results from semi-dense mono-VO [9], keypoint-based mono-SLAM [15], direct RGB-D SLAM [14] and keypointbased RGB-D SLAM [7].
- **p. 14 / 4 Results - extractive body cue:** 10: Convergence radius and accuracy of sim(3) direct image alignment with and without ESM minimization (indicated by light / dark) for a different number of ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 12 (4 Results), p. 13 (4 Results) |
| Embodiment/environment | 9: Results on the TUM RGB-D benchmark [25], and two simulated sequences from [12], measured as absolute trajectory RMSE (cm). | hardware/simulator version and reset protocol | p. 13 (4 Results), p. 12 (4 Results) |
| Dataset/benchmark | Note that for monocular SLAM this is a very challenging benchmark, as it contains fast rotational movement, strong motion blur and rolling shutter artifacts. | role, split, size and leakage | p. 13 (4 Results), p. 12 (4 Results), p. 12 (4 Results), p. 13 (4 Results) |
| Metric | Fig. 10: Convergence radius and accuracy of sim(3) direct image alignment with and without ESM minimization (indicated by light / dark) for a different num- ber of pyramid levels (color). All frames ... | definition, denominator, direction and uncertainty | p. 14 (Figure/Table caption), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Baseline/ablation | Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to right: Accumulated pointcloud thesholded with different maximum variance. Note how the reconstruction be- c ... | fair input/data/compute/action matching | p. 3 (Figure/Table caption), p. 13 (4 Results), p. 14 (4 Results) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 4 Results - extractive body cue:** For LSD-SLAM, we also show the number of keyframes created. 'x' denotes tracking failure, '-' no available data.
- **p. 14 / 5 Conclusion - extractive body cue:** Major components of the proposed method are two key novelties: (1) a direct method to align two keyframes on sim(3), explicitly incorporating and detecting scale-drift ...
- **p. 14 / 5 Conclusion - extractive body cue:** We experimentally showed that the approach reliably tracks and maps even challenging hand-held trajectories with a length of over 500 m, in particular including large ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to right: Accumulated pointcloud thesholded with different maximum ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Overview over the complete LSD-SLAM algorithm. In practice, the residuals are highly correlated, such that Σξ is only a lower bound - yet ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Statistic normalization: (a) reference image. (b-d): tracked images and inverse variance σ-2 rp of the residual. For pure rotation, depth noise has no ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 One of the major benefits of monocular SLAM - and simultaneously one of the biggest challenges - comes with the inherent scale-ambiguity: The scale of the world cannot be observed and drifts ...를 문제로 두고, We propose a direct (feature-less) monocular SLAM algorithm which, in contrast to current state-of-the-art regarding direct methods, allows to build large-scale, consistent maps of the environment.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 4 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), p. 6 (2 Preliminaries), p. 1 (Body text (section not recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
