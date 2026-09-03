# Problem - FastSLAM: A Factored Solution to the Simultaneous Localization and Mapping Problem

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.cmu.edu/~thrun/papers/montemerlo.fastslam-tr.html; PDF retrieval source: https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 4 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract)): Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** The ability to simultaneously localize a robot and accurately map its surroundings is considered by many to be a key prerequisite of truly autonomous robots.
- **p. 1 / Abstract - extractive body cue:** However, few approaches to this problem scale up to handle the very large number of landmarks present in real environments.
- **p. 1 / Abstract - extractive body cue:** Kalman filter-based algorithms, for example, require time quadratic in the number of landmarks to incorporate each sensor observation.
- **p. 1 / Abstract - extractive body cue:** This paper presents FastSLAM, an algorithm that recursively estimates the full posterior distribution over robot pose and landmark locations, yet scales logarithmically with the number ...
- **p. 1 / Abstract - extractive body cue:** This algorithm is based on an exact factorization of the posterior into a product of conditional landmark distributions and a distribution over robot paths.
- **p. 4 / Abstract - extractive body cue:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.
- **p. 1 / Abstract - extractive body cue:** A key limitation of EKF-based approaches is their computational complexity.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Kalman filter-based algorithms, for example, require time quadratic in the number of landmarks to incorporate each sensor observation. | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Kalman, filter-based, algorithms, example, require, time, quadratic, number, landmarks, incorporate | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | note, linear, Gaussian, observation, model, resulting, distribution, exactly | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Kalman, filter-based, algorithms, example, require, time, quadratic, number, landmarks, incorporate | p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract) |
| Decision / output variable | path/waypoint/velocity; body terms: extend, FastSLAM, algorithm, situations, unknown, data, association, number | p. 2 (Abstract), p. 4 (Abstract), p. 1 (Abstract) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: obtain, Bayes, zt-1, Markov, st-1, ut-1, nt-1, simply | p. 3 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 4 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (Figure/Table caption), p. 5 (Abstract), p. 5 (Abstract) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** A key limitation of EKF-based approaches is their computational complexity.
- **p. 1 / Abstract - extractive body cue:** The resulting algorithm is an instance of the Rao-Blackwellized particle filter [5, 14].
- **p. 2 / Abstract - extractive body cue:** We are now ready to formulate the SLAM problem.
- **p. 2 / Abstract - extractive body cue:** In mobile robotics, the motion model is usually a time-invariant probabilistic generalization of robot kinematics [1].

## What the Paper Changes

PDF body contribution framing (p. 2 (Abstract), p. 4 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract)): We also extend the FastSLAM algorithm to situations with unknown data association and unknown number of landmarks, showing that our approach can be extended to the full range of SLAM ...

- **p. 4 / Abstract - extractive body cue:** Our approach makes it possible to execute a FastSLAM iteration in O(M log K) time.
- **p. 1 / Abstract - extractive body cue:** This observation was made previously by Murphy [13], who developed an efficient particle filtering algorithm for learning grid maps.
- **p. 2 / Abstract - extractive body cue:** We develop a tree-based data structure that reduces the running time of FastSLAM to O(M log K), making it significantly faster than existing EKF-based SLAM ...
- **p. 3 / Abstract - extractive body cue:** This will allows us to silently "forget" all other pose estimates, rendering the size of each particle independent of the time index t.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Unfortunately, the physical testbed does not allow for systematic experiments regarding the scaling properties of the approach. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Many measurement models in the literature assume that the robot can measure range and bearing to landmarks, confounded ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | It has been observed frequently that false data association will make the conventional EKF approach fail catastrophically [2]. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 4 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 4 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), interface p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 4 (Abstract), objective p. 3 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 4 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
