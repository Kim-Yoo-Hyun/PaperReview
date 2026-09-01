# Problem - Flow Equivariant World Models: Structured Memory for Dynamic Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=jgqFnXEDGG; PDF retrieval source: https://openreview.net/pdf/25b19208166528c9c48b16cdd741d730218a8089.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (2. Background), p. 2 (2. Background), p. 1 (1. Introduction)): While these models achieve impressive perceptual quality and scale well with growing data and compute, their current form inherently lacks the ability to predict long-horizon dynamics, especially in partially observable ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Embodied systems experience the world as ‘a symphony of flows': a combination of many continuous streams of sensory input coupled to selfmotion, interwoven with the ...
- **p. 1 / Abstract - extractive PDF cue:** These sensory streams and the underlying dynamics of the world obey smooth, timeparameterized symmetries which existing world models ignore.
- **p. 1 / Abstract - extractive PDF cue:** Without a memory that respects this structure, partial observability presents a major obstacle to existing methods: each observation reveals only a fraction of the world, ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we introduce Flow Equivariant World Modeling, a framework that leverages time-parameterized symmetries within a latent memory for stable and accurate dynamics prediction ...
- **p. 1 / Abstract - extractive PDF cue:** The latent memory shifts and transforms equivariantly with self-motion and inferred external object motion, keeping information about out-of-view regions aligned as time progresses.
- **p. 2 / 2. Background - extractive PDF cue:** While these models achieve impressive perceptual quality and scale well with growing data and compute, their current form inherently lacks the ability to predict long-horizon ...
- **p. 2 / 2. Background - extractive PDF cue:** This limitation necessitates a form of memory in order to represent and integrate partial information through time.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While these models achieve impressive perceptual quality and scale well with growing data and compute, their current form inherently lacks the ability ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | A sequence-to-sequence model Φ defines a map f 7→h for outputs h = {ht}T t=0, ht : X′ →RK′, such as mapping ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | sequence-to-sequence, model, defines, outputs, mapping, input, video, sequence, hidden, states | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Because, elements, Lie, algebra, combine, structured, manner, then | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: sequence-to-sequence, model, defines, outputs, mapping, input, video, sequence, hidden, states | p. 2 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance) |
| Decision / output variable | geometry/map/query r; body terms: embodied, agents, dynamic, world, survival, critically, depends, ability | p. 1 (1. Introduction), p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: simple, addition, indeed, equivariant, respect, linear, transformations, inputs | p. 5 (3.1. Generalized Flow Equivariance), p. 5 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 7 (4.2. 2D MNIST World Benchmark) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 2. Background - extractive PDF cue:** This limitation necessitates a form of memory in order to represent and integrate partial information through time.
- **p. 1 / 1. Introduction - extractive PDF cue:** When an agent observes dynamics, turns away, then turns back to the original viewpoint, flow equivariance asserts dynamics continue even when unobserved; existing work loses ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 5 (3.1. Generalized Flow Equivariance)): As embodied agents in a dynamic world, our survival critically depends on our ability to accurately model our surrounding environment, our own self-motion through it, *Equal contribution 1Kempner Institute, Harvard ...

- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which supports ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** Finally, to complete our framework, we note that motion is relative (i.e. self-motion of an agent is equivalent to global motion of the input).
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** For the first set of experiments, to validate our framework in a 2D environment, we construct a recurrent model with self-motion and flow equivariance following ...
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** To extend our framework to more complex datasets, we construct a second FloWM instantiation with a Vision Transformer (ViT) (Dosovitskiy et al., 2021) encoder and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Similarly, future work may extend FloWM beyond the current discrete velocity sets V to continuous families; however prior ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 2. Existing world model memory is inherently limited in partially observed dynamic environments. a) Standard autoregressive video ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Predictions from FloWM remain consistent with ground truth for 150 timesteps past the observation window, well beyond its ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | During inference, DFoT maintains a sliding window composed of context and prediction frames at different noise levels; after ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (2. Background), p. 2 (2. Background), p. 1 (1. Introduction), interface p. 2 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), objective p. 5 (3.1. Generalized Flow Equivariance), p. 5 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
