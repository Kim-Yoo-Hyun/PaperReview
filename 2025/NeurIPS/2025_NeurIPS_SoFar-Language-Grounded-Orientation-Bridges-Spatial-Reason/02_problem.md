# Problem - SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (46 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kmv7yg6QXv; PDF retrieval source: https://openreview.net/pdf/44ce67ddf7a771b623a5a1cba738c147c2617eb1.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): However, translating a specific language description into a desired orientation is challenging for existing VLMs.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** While spatial reasoning has made progress in object localization relationships, it often overlooks object orientation-a key factor in 6-DoF fine-grained manipulation.
- **p. 1 / Abstract - extractive PDF cue:** Traditional pose representations rely on pre-defined frames or templates, limiting generalization and semantic grounding.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we introduce the concept of semantic orientation, which defines object orientations using natural language in a reference-frame-free manner (e.g., the "plug-in" direction ...
- **p. 1 / Abstract - extractive PDF cue:** To support this, we construct OrienText300K, a large-scale dataset of 3D objects annotated with semantic orientations, and develop PointSO, a general model for zero-shot semantic ...
- **p. 1 / Abstract - extractive PDF cue:** By integrating semantic orientation into VLM agents, our SOFAR framework enables 6-DoF spatial reasoning and generates robotic actions.
- **p. 2 / 1 Introduction - extractive PDF cue:** However, translating a specific language description into a desired orientation is challenging for existing VLMs.
- **p. 4 / 1 Introduction - extractive PDF cue:** Data Annotation As mentioned in the introduction, VLMs struggle to produce accurate object orientation values, which presents a significant challenge for data generation.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, translating a specific language description into a desired orientation is challenging for existing VLMs. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | X Y Z Pose Estimation Category / Instance Template Needed Only axis, the relationship with instruction is unclear "Blow Wind" "Top" "Back" ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Pose, Estimation, Category, Instance, Template, Needed, Only, axis, relationship, instruction | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | PointSO, takes, object, point, clouds, language, description, inputs | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Pose, Estimation, Category, Instance, Template, Needed, Only, axis, relationship, instruction | p. 2 (Abstract), p. 4 (1 Introduction), p. 4 (1 Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: PointSO, generalizable, cross-modal, Transformer, semantic, orientation, prediction, addition | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: optimization, minimize, negative, cosine, similarity, Lcos, between, predicted | p. 4 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (1 Introduction), p. 1 (Abstract), p. 4 (1 Introduction) |
| Success / guarantee | instruction-conditioned task success | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 4 / 1 Introduction - extractive PDF cue:** Data Annotation As mentioned in the introduction, VLMs struggle to produce accurate object orientation values, which presents a significant challenge for data generation.
- **p. 5 / 1 Introduction - extractive PDF cue:** To bridge this gap, we build an integrated reasoning system where a powerful VLM acts as an agent and reasons about the scene while communicating ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We observe that current VLMs struggle with understanding object orientation, making them insufficient for 6-DoF robot manipulation planning.
- **p. 3 / 1 Introduction - extractive PDF cue:** We develop the SOFAR system, which enhances spatial reasoning with 6-DoF scene graph and achieves SOTA performance on Open6DOR, SimplerEnv, and generalizes across embodiments (e.g., ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction)): We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction.

- **p. 2 / 1 Introduction - extractive PDF cue:** In addition, we introduce Open6DOR V2, a large-scale benchmark for 6-DoF object rearrangement in simulation, which supports both open-loop and closed-loop control.
- **p. 3 / 1 Introduction - extractive PDF cue:** Finally, we present two new benchmarks, Open6DOR V2 and 6-DoF SpatialBench, to evaluate 6-DoF rearrangement and spatial reasoning.
- **p. 3 / 1 Introduction - extractive PDF cue:** To support this, we introduce OrienText300K, a curated dataset of 3D models annotated with diverse language-guided orientation labels.
- **p. 5 / 1 Introduction - extractive PDF cue:** This enriched spatial representation enables the VLM to perform accurate spatial reasoning by leveraging its visual and linguistic understanding.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Furthermore, leveraging the error detection and re-planning capabilities of VLMs [48, 1], we can make multiple attempts following ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 31 | Figure 16: Failure case distribution analysis of our SOFAR. C | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We employ OMPL [103] to generate a collision-free trajectory, initializing joint positions at the midpoint to ensure smooth ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (Abstract), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 2 (Abstract), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), objective p. 4 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
