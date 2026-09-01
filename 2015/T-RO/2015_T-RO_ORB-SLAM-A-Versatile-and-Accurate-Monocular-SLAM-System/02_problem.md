# Problem - ORB-SLAM: A Versatile and Accurate Monocular SLAM System

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1502.00956; PDF retrieval source: https://arxiv.org/pdf/1502.00956. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 4 (III. SYSTEM OVERVIEW), p. 1 (Front matter), p. 3 (B UNDLE ADJUSTMENT (BA) is known to provide ac)): Unfortunately several factors severely limit its application: lack of loop closing and adequate handling of occlusions, low invariance to viewpoint of the relocalization and the need of human intervention for ...

## PDF Body Digest

- **p. 2 / Abstract - extractive PDF cue:** This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments.
- **p. 2 / Abstract - extractive PDF cue:** The system is robust to severe motion clutter, allows wide baseline loop closing and relocalization, and includes full automatic initialization.
- **p. 2 / Abstract - extractive PDF cue:** Building on excellent algorithms of recent years, we designed from scratch a novel system that uses the same features for all SLAM tasks: tracking, mapping, ...
- **p. 2 / Abstract - extractive PDF cue:** A survival of the fittest strategy that selects the points and keyframes of the reconstruction leads to excellent robustness and generates a compact and trackable ...
- **p. 2 / Abstract - extractive PDF cue:** We present an exhaustive evaluation in 27 sequences from the most popular datasets.
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive PDF cue:** Unfortunately several factors severely limit its application: lack of loop closing and adequate handling of occlusions, low invariance to viewpoint of the relocalization and the ...
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive PDF cue:** This algorithm, while limited to small scale operation, provides simple but effective methods for keyframe selection, feature matching, point triangulation, camera localization for every frame, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Unfortunately several factors severely limit its application: lack of loop closing and adequate handling of occlusions, low invariance to viewpoint of the ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | When a new keyframe is inserted, it is included in the tree linked to the keyframe which shares most point observations, and ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | When, keyframe, inserted, included, tree, linked, shares, most, point, observations | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | requiere, features, need, extraction, much, less, image, excludes | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: When, keyframe, inserted, included, tree, linked, shares, most, point, observations | p. 6 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 4 (III. SYSTEM OVERVIEW) |
| Decision / output variable | path/waypoint/velocity; body terms: build, main, ideas, PTAM, place, recognition, alvez-L, opez | p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 2 (Abstract), p. 5 (III. SYSTEM OVERVIEW) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Appendix, describe, error, terms, cost, functions, variables, involved | p. 5 (III. SYSTEM OVERVIEW), p. 6 (III. SYSTEM OVERVIEW), p. 8 (VI. LOCAL MAPPING), p. 6 (III. SYSTEM OVERVIEW), p. 8 (VI. LOCAL MAPPING) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (III. SYSTEM OVERVIEW), p. 8 (VI. LOCAL MAPPING), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac) |
| Success / guarantee | goal reach with collision-free execution | p. 11 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive PDF cue:** This algorithm, while limited to small scale operation, provides simple but effective methods for keyframe selection, feature matching, point triangulation, camera localization for every frame, ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive PDF cue:** While our current implementation make use of ORB, the techniques proposed are not restricted to these features.
- **p. 1 / Front matter - extractive PDF cue:** Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting /republishing this material for advertising or promotional ...
- **p. 3 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive PDF cue:** In the current paper we add the initialization method, the Essential Graph, and perfect all methods involved.

## What the Paper Changes

PDF contribution framing (p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 2 (Abstract), p. 5 (III. SYSTEM OVERVIEW), p. 4 (III. SYSTEM OVERVIEW), p. 5 (III. SYSTEM OVERVIEW)): In this work we build on the main ideas of PTAM, the place recognition work of G´alvez-L´opez and Tard´os [5], the scale-aware loop closing of Strasdat et. al [6] and ...

- **p. 2 / Abstract - extractive PDF cue:** We present an exhaustive evaluation in 27 sequences from the most popular datasets.
- **p. 5 / III. SYSTEM OVERVIEW - extractive PDF cue:** In order not to include all the edges provided by the covisibility graph, which can be very dense, we propose to build an Essential Graph ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive PDF cue:** This allows to match them from wide baselines, boosting the accuracy of BA.
- **p. 5 / III. SYSTEM OVERVIEW - extractive PDF cue:** The novel procedure to create an initial map is presented in Section IV.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | However, direct methods have their own limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Future Work The accuracy of our system can still be improved incorporating points at infinity in the tracking. | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | In sequence 08 there are no loops and drift cannot be corrected, which makes clear the need of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | The big loop on the right does not perfectly align because it was traversed in opposite directions and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 4 (III. SYSTEM OVERVIEW), p. 5 (III. SYSTEM OVERVIEW). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 4 (III. SYSTEM OVERVIEW), p. 1 (Front matter), p. 3 (B UNDLE ADJUSTMENT (BA) is known to provide ac), interface p. 6 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 4 (III. SYSTEM OVERVIEW), p. 5 (III. SYSTEM OVERVIEW), objective p. 5 (III. SYSTEM OVERVIEW), p. 6 (III. SYSTEM OVERVIEW), p. 8 (VI. LOCAL MAPPING), p. 6 (III. SYSTEM OVERVIEW), p. 8 (VI. LOCAL MAPPING).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
