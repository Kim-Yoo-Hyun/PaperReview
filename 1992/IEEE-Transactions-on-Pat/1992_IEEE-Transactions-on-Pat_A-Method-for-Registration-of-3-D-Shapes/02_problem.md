# Problem - A Method for Registration of 3-D Shapes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://doi.org/10.1109/34.121791; PDF retrieval source: https://doi.org/10.1109/34.121791. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1) Point sets), p. 2 (1) Point sets), p. 4 (B. Point to Implicit Entity Distance), p. 4 (B. Point to Implicit Entity Distance), p. 1 (1. Istmopuction)): reasonable quality curve data but has difficulty with very noisy curves because the method uses arclenath sampling of the curves to obtain corresponding point sets.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This paper describes general-purpose, representation-independent method for the accurate and. computationally ‘eMicient registration of 3-D shapes Including freeform curves ‘and surfaces.
- **p. 1 / Abstract - extractive body cue:** The method handles the fll ix degrees of freedom ind is based on the iterative closest point (ICP) algorithm, Which requires only a procedure to ...
- **p. 1 / Abstract - extractive body cue:** The ICP algorithm always ‘Converges monotonically to the nearest local minimum of « mear Square distance metric, and experience shows that the rate of/ convergence ...
- **p. 1 / Abstract - extractive body cue:** Therefore, given an adequate set of intial rotations and translations for 2 particular class of objects with a certain level of "shape complexity," one can ...
- **p. 1 / Abstract - extractive body cue:** For example, a given "model" shape and a sensed "data" shape that represents 2 major portion of the model shape can be registered in minutes ...
- **p. 2 / 1) Point sets - extractive body cue:** reasonable quality curve data but has difficulty with very noisy curves because the method uses arclenath sampling of the curves to obtain corresponding point sets.
- **p. 2 / 1) Point sets - extractive body cue:** The primary limitation of this work was that it relied ‘on the probable existence of reasonably large planar regions Within a free-form shape.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | reasonable quality curve data but has difficulty with very noisy curves because the method uses arclenath sampling of the curves to obtain ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | [36] also describe a method for the registration of multiple overlapping range images without distinctive feature extraction. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | describe, registration, multiple, overlapping, range, images, without, distinctive, feature, extraction | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | issue, initial, registration, states, addressed, next, Finally, experimental | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: describe, registration, multiple, overlapping, range, images, without, distinctive, feature, extraction | p. 2 (1) Point sets), p. 1 (1) Point sets), p. 1 (1) Point sets) |
| Decision / output variable | geometry/map/query r; body terms: SVD, eross-, covariance, matrix, point, distributions, does, however | p. 4 (B. Point to Implicit Entity Distance), p. 2 (1) Point sets), p. 2 (1) Point sets) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Horn, Harris, addressed, problem, estimating, exact, rigid-body, motion | p. 2 (1) Point sets), p. 4 (B. Point to Implicit Entity Distance), p. 3 (A. Point to Parametric Entity Distance), p. 3 (A. Point to Parametric Entity Distance), p. 4 (A. Point to Parametric Entity Distance), p. 6 (B. Convergence Theorem) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (B. Point to Implicit Entity Distance), p. 7 (B. Convergence Theorem), p. 8 (B. Convergence Theorem) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (B. Point to Implicit Entity Distance), p. 7 (B. Convergence Theorem), p. 16 (A BN) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1) Point sets - extractive body cue:** The primary limitation of this work was that it relied ‘on the probable existence of reasonably large planar regions Within a free-form shape.
- **p. 4 / B. Point to Implicit Entity Distance - extractive body cue:** Therefore, this result cannot be used if precise distance results are required.
- **p. 4 / B. Point to Implicit Entity Distance - extractive body cue:** The SVD approach, based on the eross- ‘covariance matrix of two point distributions, does, however, ‘generalize easily ton dimensions and would be our method of ...
- **p. 1 / 1. Istmopuction - extractive body cue:** general, unified approach, which generalizes 10 n dimensions land provides solutions to 1) the point-set matching problem without correspondence and 2) the free-form curve matching ...

## What the Paper Changes

PDF contribution framing (p. 4 (B. Point to Implicit Entity Distance), p. 2 (1) Point sets), p. 2 (1) Point sets)): The SVD approach, based on the eross- ‘covariance matrix of two point distributions, does, however, ‘generalize easily ton dimensions and would be our method of choice for n > 3 ...

- **p. 2 / 1) Point sets - extractive body cue:** A recent conference proceedings [47] contains new contributions on this subject.
- **p. 2 / 1) Point sets - extractive body cue:** ‘Schwartz and Sharir [50] developed a solution to the freeform space curve matching problem without feature extraction in late 1985.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | This is a problem with almost all of the shape ‘matching algorithms in the literature For any given ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | ‘would yield a smaller mean square error than the least squares registration, which cannot possibly be the case. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | 4d, Terminate the iteration when the change in meansquare error falls below a preset threshold > > 0 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Note the smooth character ofall the curves. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1) Point sets), p. 1 (1) Point sets), p. 1 (1) Point sets), p. 2 (1) Point sets). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1) Point sets), p. 2 (1) Point sets), p. 4 (B. Point to Implicit Entity Distance), p. 4 (B. Point to Implicit Entity Distance), p. 1 (1. Istmopuction), interface p. 2 (1) Point sets), p. 1 (1) Point sets), p. 1 (1) Point sets), p. 2 (1) Point sets), objective p. 2 (1) Point sets), p. 4 (B. Point to Implicit Entity Distance), p. 3 (A. Point to Parametric Entity Distance), p. 3 (A. Point to Parametric Entity Distance), p. 4 (A. Point to Parametric Entity Distance), p. 6 (B. Convergence Theorem).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
