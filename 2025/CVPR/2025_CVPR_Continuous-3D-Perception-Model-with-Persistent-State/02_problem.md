# Problem - Continuous 3D Perception Model with Persistent State

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.12387; PDF retrieval source: https://arxiv.org/pdf/2501.12387. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to continuously update allows it to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We present a unified framework capable of solving a broad range of 3D tasks.
- **p. 1 / Abstract - extractive PDF cue:** Our approach features a stateful recurrent model that continuously updates its state representation with each new observation.
- **p. 1 / Abstract - extractive PDF cue:** Given a stream of images, this evolving state can be used to generate metric-scale pointmaps (per-pixel 3D points) for each new input in an online ...
- **p. 1 / Abstract - extractive PDF cue:** These pointmaps reside within a common coordinate system, and can be accumulated into a coherent, dense scene reconstruction that updates as new images arrive.
- **p. 1 / Abstract - extractive PDF cue:** Our model, called CUT3R (Continuous Updating Transformer for 3D Reconstruction), captures rich priors of real-world scenes: not only can it predict accurate pointmaps from image ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to ...
- **p. 1 / 1. Introduction - extractive PDF cue:** We achieve these capabilities by integrating data-driven priors with a recurrent update mechanism.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Following the state-image interaction, explicit 3D pointmaps and camera poses are extracted for each view. | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Following, state-image, interaction, explicit, pointmaps, camera, poses, extracted, view, denotes | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | State, Image, Pointmaps, Cameras, Scene, reconstruction, time, Input | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Following, state-image, interaction, explicit, pointmaps, camera, poses, extracted, view, denotes | p. 3 (3. Method), p. 3 (3.1. State-Input Interaction Mechanism), p. 4 (3.1. State-Input Interaction Mechanism) |
| Decision / output variable | path/waypoint/velocity; body terms: learned, prior, enables, address, challenges, encountered, traditional, methods | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: stages, trained, images, reduce, computational, costs, following, DUSt3R | p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective), p. 3 (3.1. State-Input Interaction Mechanism), p. 3 (3. Method), p. 4 (3.2. Querying the State with Unseen Views), p. 4 (3.1. State-Input Interaction Mechanism) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Method), p. 4 (3.3. Training Objective), p. 4 (3.2. Querying the State with Unseen Views) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (4.3. 3D Reconstruction), p. 8 (4.4. Analysis), p. 5 (4.1. Monocular and Video Depth Estimation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** We achieve these capabilities by integrating data-driven priors with a recurrent update mechanism.
- **p. 2 / 1. Introduction - extractive PDF cue:** These datasets span a broad spectrum of scene types and contexts-static and dynamic, indoor and outdoor, real and synthetic-enabling the model to acquire robust and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** During inference, our recurrent framework naturally accepts varying numbers of images, and supports a wide range of input data settings: from streaming video to unstructured ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. State-Input Interaction Mechanism)): The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to continuously update allows it to ...

- **p. 2 / 1. Introduction - extractive PDF cue:** Our framework is designed to be general and flexible, making it well-suited for training on an extensive collection of datasets and adaptable to diverse inference ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Building on these insights, we introduce an online 3D perception framework that unifies three key capabilities: 1) reconstructing 3D scenes from few observations, 2) continuously ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We also show that our method can infer previously unseen structures and continuously refine the reconstruction as new observations arrive.
- **p. 3 / 3.1. State-Input Interaction Mechanism - extractive PDF cue:** Our method takes a stream of images as input.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Most prior approaches do so through test-time optimization, as seen in RobustCVD [47] and CasualSAM [128], which jointly ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Table 6. Training Datasets. We provide more details of our training datasets. We classify a dataset as dynamic ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3. Method), p. 3 (3.1. State-Input Interaction Mechanism), p. 4 (3.1. State-Input Interaction Mechanism), p. 4 (3.2. Querying the State with Unseen Views). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3. Method), p. 3 (3.1. State-Input Interaction Mechanism), p. 4 (3.1. State-Input Interaction Mechanism), p. 4 (3.2. Querying the State with Unseen Views), objective p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective), p. 3 (3.1. State-Input Interaction Mechanism), p. 3 (3. Method), p. 4 (3.2. Querying the State with Unseen Views), p. 4 (3.1. State-Input Interaction Mechanism).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
