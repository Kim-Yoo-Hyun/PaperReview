# Problem - LSD-SLAM: Large-Scale Direct Monocular SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://cvg.cit.tum.de/research/vslam/lsdslam; PDF retrieval source: https://jakobengel.github.io/pdf/engel14eccv.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 4 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), p. 6 (2 Preliminaries)): One of the major benefits of monocular SLAM - and simultaneously one of the biggest challenges - comes with the inherent scale-ambiguity: The scale of the world cannot be observed ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** Real-time monocular Simultaneous Localization and Mapping (SLAM) and 3D reconstruction have become increasingly popular research topics.
- **p. 1 / 1 Introduction - extractive PDF cue:** Two major reasons are (1) their use in robotics, in particular to navigate unmanned aerial vehicles (UAVs) [10, 8, 1], and (2) augmented and virtual ...
- **p. 1 / 1 Introduction - extractive PDF cue:** One of the major benefits of monocular SLAM - and simultaneously one of the biggest challenges - comes with the inherent scale-ambiguity: The scale of ...
- **p. 1 / 1 Introduction - extractive PDF cue:** The advantage is that this allows to seamlessly switch between differently scaled environments, such as a desk environment indoors and large-scale outdoor environments.
- **p. 1 / 1 Introduction - extractive PDF cue:** Scaled sensors on the other hand, such as depth or stereo cameras, have a limited range at which they can provide reliable measurements and hence ...
- **p. 4 / 2 Preliminaries - extractive PDF cue:** 2.2), and briefly introduce propagation of uncertainty (Sec.
- **p. 5 / 2 Preliminaries - extractive PDF cue:** (7) In order to be robust to outliers arising e.g. from occlusions or reflections, different weighting-schemes [14] have been proposed, resulting in an iteratively reweighted ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | One of the major benefits of monocular SLAM - and simultaneously one of the biggest challenges - comes with the inherent scale-ambiguity: ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | 2.3 Propagation of Uncertainty Propagation of uncertainty is a statistical tool to derive the uncertainty of the output of a function f(X), ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Propagation, Uncertainty, statistical, tool, derive, output, function, caused, input, Map | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Images, per-pixel, inverse, depth, variance, written, functions, where | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Propagation, Uncertainty, statistical, tool, derive, output, function, caused, input, Map | p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 4 (2 Preliminaries) |
| Decision / output variable | path/waypoint/velocity; body terms: Complete, algorithm, consists, three, major, components, tracking, depth | p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 1 (1 Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Weighted, Gauss-Newton, Optimization, Lie-Manifolds, Two, images, aligned, minimization | p. 7 (2 Preliminaries), p. 8 (2 Preliminaries), p. 5 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (2 Preliminaries), p. 8 (I. Mini), p. 8 (2 Preliminaries) |
| Success / guarantee | goal reach with collision-free execution | p. 14 (Figure/Table caption), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 4 / 2 Preliminaries - extractive PDF cue:** 2.2), and briefly introduce propagation of uncertainty (Sec.
- **p. 5 / 2 Preliminaries - extractive PDF cue:** (7) In order to be robust to outliers arising e.g. from occlusions or reflections, different weighting-schemes [14] have been proposed, resulting in an iteratively reweighted ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** 3.4) replace KF refine KF yes no tracking reference add to map Current Map Take KF? min ξ∈se(3) P p
- **p. 6 / 2 Preliminaries - extractive PDF cue:** 2.3 Propagation of Uncertainty Propagation of uncertainty is a statistical tool to derive the uncertainty of the output of a function f(X), caused by uncertainty ...

## What the Paper Changes

PDF contribution framing (p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 1 (1 Introduction)): 3.1 The Complete Method The algorithm consists of three major components: tracking, depth map estimation and map optimization as visualized in Fig.

- **p. 7 / 2 Preliminaries - extractive PDF cue:** 3.2 Map Representation The map is represented as a pose graph of keyframes: Each keyframe Ki consists of a camera image Ii : Ωi →R, ...
- **p. 1 / 1 Introduction - extractive PDF cue:** The advantage is that this allows to seamlessly switch between differently scaled environments, such as a desk environment indoors and large-scale outdoor environments.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | For LSD-SLAM, we also show the number of keyframes created. 'x' denotes tracking failure, '-' no available data. | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Major components of the proposed method are two key novelties: (1) a direct method to align two keyframes ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | We experimentally showed that the approach reliably tracks and maps even challenging hand-held trajectories with a length of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 4 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), p. 6 (2 Preliminaries), interface p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries), objective p. 7 (2 Preliminaries), p. 8 (2 Preliminaries), p. 5 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
