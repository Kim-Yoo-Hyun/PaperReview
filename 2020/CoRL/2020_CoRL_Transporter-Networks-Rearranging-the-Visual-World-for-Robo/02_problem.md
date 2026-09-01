# Problem - Transporter Networks: Rearranging the Visual World for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.14406; PDF retrieval source: https://arxiv.org/pdf/2010.14406. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): This naturally leads us to ask: is there structure that we can incorporate into our end-to-end models to improve their learning efficiency, without imposing any of the limitations or burdens ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** End-to-end models that map directly from pixels to actions hold the capacity to learn complex manipulation skills, but are known to require copious amounts of ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Integrating object-centric assumptions - e.g., object keypoints [3, 4, 5, 6], embeddings [7, 8], or dense descriptors [9, 10, 11] - has been shown to ...
- **p. 1 / 1 Introduction - extractive PDF cue:** However, these representations often impose data collection burdens (i.e., configuring scenes with specific singulated objects) and still struggle to address challenging scenarios with unseen classes ...
- **p. 1 / 1 Introduction - extractive PDF cue:** This naturally leads us to ask: is there structure that we can incorporate into our end-to-end models to improve their learning efficiency, without imposing any ...
- **p. 1 / 1 Introduction - extractive PDF cue:** In this work, we propose the Transporter Network, a simple end-to-end model architecture that preserves spatial structure for vision-based manipulation, without object-centric assumptions: • Manipulation ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Prior end-to-end models [1, 2] often use convolutional architectures with raw images, in which valuable spatial information can be lost to perspective distortions.
- **p. 2 / 1 Introduction - extractive PDF cue:** They do not require any prior knowledge of the objects to be manipulated - they rely only on information contained within partial RGB-D data from ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This naturally leads us to ask: is there structure that we can incorporate into our end-to-end models to improve their learning efficiency, ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | Picking: Our picking model is a single feed-forward FCN that takes as input the visual observation ot∈RH×W×4 and outputs dense pixel-wise values ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | Picking, model, single, feed-forward, FCN, takes, input, visual, observation, outputs | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | Consider, problem, learning, pick-and-place, actions, robot, visual, observations | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: Picking, model, single, feed-forward, FCN, takes, input, visual, observation, outputs | p. 5 (3 Method), p. 5 (3 Method), p. 2 (3 Method) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: Transporter, Networks, decompose, problem, picking, pick-conditioned, placing, fpick | p. 3 (3 Method), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective / loss / cost | task/contact/pose objective; cue terms: stride, chosen, balance, between, maximizing, receptive, field, coverage | p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |
| Success / guarantee | completion, contact success and robustness | p. 7 (4 Results), p. 6 (4 Results), p. 6 (4 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** Prior end-to-end models [1, 2] often use convolutional architectures with raw images, in which valuable spatial information can be lost to perspective distortions.
- **p. 2 / 1 Introduction - extractive PDF cue:** They do not require any prior knowledge of the objects to be manipulated - they rely only on information contained within partial RGB-D data from ...
- **p. 2 / 1 Introduction - extractive PDF cue:** On 10 unique tabletop manipulation tasks, Transporter Networks trained from scratch are capable of achieving greater than 90% success on most tasks with objects in ...

## What the Paper Changes

PDF contribution framing (p. 3 (3 Method), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method)): Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - but in this work, our primary ...

- **p. 1 / 1 Introduction - extractive PDF cue:** Our method uses 3D reconstruction to project visual data onto a spatiallyconsistent representation as input, with which it is able to better exploit equivariance [13, ...
- **p. 1 / 1 Introduction - extractive PDF cue:** In this work, we propose the Transporter Network, a simple end-to-end model architecture that preserves spatial structure for vision-based manipulation, without object-centric assumptions: • Manipulation ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We propose a simple model architecture that learns to attend to a local region and predict its spatial displacement, while retaining the spatial structure of ...
- **p. 4 / 3 Method - extractive PDF cue:** Our method preserves rotation and translation equivariance for efficient learning.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Performance is evaluated with a metric from 0 (failure) to 100 (success). | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Figure 9. Depictions of the generalization ability of different models on the simplified translation-only block-insertion task. Each episode ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For example, when a stack of blocks falls over, they can re-build the stack of blocks as if ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3 Method), p. 5 (3 Method), p. 2 (3 Method), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 5 (3 Method), p. 5 (3 Method), p. 2 (3 Method), p. 1 (1 Introduction), objective p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
