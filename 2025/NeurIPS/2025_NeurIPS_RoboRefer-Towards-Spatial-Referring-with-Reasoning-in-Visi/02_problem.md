# Problem - RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (71 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OGxalNUHbJ; PDF retrieval source: https://openreview.net/pdf/81387e1e7f5169279b63c293ca88b1e4a8bc7e35.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction)): Thus, this work attempts to address this gap by integrating both levels for comprehensive spatial referring.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Spatial referring is a fundamental capability of embodied robots to interact with the 3D physical world.
- **p. 1 / Abstract - extractive body cue:** However, even with the powerful pretrained vision language models (VLMs), recent approaches are still not qualified to accurately understand the complex 3D scenes and dynamically ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose RoboRefer, a 3D-aware VLM that can first achieve precise spatial understanding by integrating a disentangled but dedicated depth encoder via ...
- **p. 1 / Abstract - extractive body cue:** Moreover, RoboRefer advances generalized multi-step spatial reasoning via reinforcement fine-tuning (RFT), with metric-sensitive process reward functions tailored for spatial referring tasks.
- **p. 1 / Abstract - extractive body cue:** To support SFT and RFT training, we introduce RefSpatial, a large-scale dataset of 20M QA pairs (2× prior), covering 31 spatial relations (vs.
- **p. 2 / 1 Introduction - extractive body cue:** Thus, this work attempts to address this gap by integrating both levels for comprehensive spatial referring.
- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Thus, this work attempts to address this gap by integrating both levels for comprehensive spatial referring. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | D.4.1 Sampling Action Groups Given an input state s = (O, Q), where O denotes the visual encoding of the RGB or ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Sampling, Action, Groups, Given, input, state, where, denotes, visual, encoding | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | RoboRefer, perform, single-step, precise, spatial, understanding, RGB, inputs | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Sampling, Action, Groups, Given, input, state, where, denotes, visual, encoding | p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 4 (3 Method), p. 4 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: contributions, summarized, follows, RoboRefer, D-aware, reasoning, VLM, trained | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Unlike, PPO, relies, costly, value, network, GRPO, estimates | p. 4 (3 Method), p. 5 (3 Method), p. 48 (C Implementation Details and Samples of RefSpatial-Bench), p. 54 (C Implementation Details and Samples of RefSpatial-Bench), p. 57 (C Implementation Details and Samples of RefSpatial-Bench), p. 57 (C Implementation Details and Samples of RefSpatial-Bench) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 Method), p. 5 (3 Method), p. 20 (B.3.5 Question-Answer Pair Generation) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 23 (B.1.1 Multi-Stage Image Filtering), p. 8 (4 Experiments), p. 9 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.
- **p. 3 / 1 Introduction - extractive body cue:** (2) We construct RefSpatial, a well-annotated dataset tailored for spatial referring, facilitating both SFT and RFT training, and introduce RefSpatial-Bench, a benchmark that fills the ...
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, current VLMs depend heavily on supervised fine-tuning (SFT) for implicit reasoning, risking memorizing answers over explicit reasoning and thereby hindering generalization and accuracy in ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Method)): Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions to achieve spatial referring.

- **p. 2 / 1 Introduction - extractive body cue:** To advance spatial referring, we introduce RefSpatial, a large-scale dataset of 2.5M high-quality examples with 20M QA pairs (2× prior [3]).
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose RoboRefer, a 3D-aware VLM that not only acquires precise spatial understanding via SFT but also exhibits generalized strong reasoning capabilities ...
- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.
- **p. 4 / 3 Method - extractive body cue:** To address this, we propose a simple yet effective approach: a dedicated depth encoder and projector, initialized from their RGB counterparts.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 52 | Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 21 | 53 F More Demonstrations 54 G More Discussion on Limitations and Future Work 54 H Broader Impacts 54 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 54 | G More Discussion on Limitations and Future Work Despite achieving promising results, our model still has limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | 33 B.2.3 Addressing Limitations: Object Annotation and Bounding Box Filtering . . | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 4 (3 Method), p. 4 (3 Method), p. 7 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), interface p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 4 (3 Method), p. 4 (3 Method), p. 7 (3 Method), objective p. 4 (3 Method), p. 5 (3 Method), p. 48 (C Implementation Details and Samples of RefSpatial-Bench), p. 54 (C Implementation Details and Samples of RefSpatial-Bench), p. 57 (C Implementation Details and Samples of RefSpatial-Bench), p. 57 (C Implementation Details and Samples of RefSpatial-Bench).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
