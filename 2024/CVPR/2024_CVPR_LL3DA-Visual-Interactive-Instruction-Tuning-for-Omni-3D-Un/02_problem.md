# Problem - LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.18651; PDF retrieval source: https://arxiv.org/pdf/2311.18651. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formatting)): Though these methods have achieved remarkable success addressing different challenges in understanding 3D worlds with natural language, there are certain limitations.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Recent advances in Large Multimodal Models (LMM) have made it possible for various applications in humanmachine interactions.
- **p. 1 / Abstract - extractive PDF cue:** However, developing LMMs that can comprehend, reason, and plan in complex and diverse 3D environments remains a challenging topic, especially considering the demand for understanding ...
- **p. 1 / Abstract - extractive PDF cue:** Existing works seek help from multi-view images, and project 2D features to 3D space as 3D scene representations.
- **p. 1 / Abstract - extractive PDF cue:** This, however, leads to huge computational overhead and performance degradation.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we present LL3DA, a Large Language 3D Assistant that takes point cloud as direct input and respond to both textualinstructions and visual-prompts.
- **p. 2 / 1. Introduction - extractive PDF cue:** Though these methods have achieved remarkable success addressing different challenges in understanding 3D worlds with natural language, there are certain limitations.
- **p. 1 / 1. Introduction - extractive PDF cue:** During this LLM carnival, researchers are also seeking generalized LLM solutions to various vision language tasks [16, 54, 59].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Though these methods have achieved remarkable success addressing different challenges in understanding 3D worlds with natural language, there are certain limitations. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | summarize, contributions, present, LLM-based, solution, understanding, reasoning, planning, complex, environments | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Next, aggregated, scene, embeddings, projected, prefix, textual, instructions | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: summarize, contributions, present, LLM-based, solution, understanding, reasoning, planning, complex, environments | p. 2 (1. Introduction), p. 3 (3.1. Problem Formatting), p. 3 (3.2. Model Design) |
| Decision / output variable | geometry/map/query r; body terms: summarize, contributions, present, LLM-based, solution, understanding, reasoning, planning | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: parameters, embedding, layers, LLM, kept, frozen, save, memory | p. 4 (3.2. Model Design) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Model Design), p. 4 (3.2. Model Design) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (5.2. Comparison with SoTA Specialists), p. 17 (Figure/Table caption), p. 5 (5.2. Comparison with SoTA Specialists) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** During this LLM carnival, researchers are also seeking generalized LLM solutions to various vision language tasks [16, 54, 59].
- **p. 1 / 1. Introduction - extractive PDF cue:** The recent surge in Large Language Model (LLM) families [13, 27, 41, 49, 58] opens up great opportunities for solving various machine learning tasks in ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Prior works have made initial success addressing various 3D vision and language tasks.
- **p. 3 / 3.1. Problem Formatting - extractive PDF cue:** This design could naturally fit in the vocabulary of existing pre-trained LLMs [49, 58].

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3.1. Problem Formatting), p. 4 (3.2. Model Design)): To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model takes both the textual instructions ...

- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, by introducing additional visual interactions, our method could further remove the ambiguities within the vague textual instructions.
- **p. 3 / 3. Methodology - extractive PDF cue:** Next, we introduce our model design in details (Sec.
- **p. 3 / 3.1. Problem Formatting - extractive PDF cue:** 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction It, and potential ...
- **p. 4 / 3.2. Model Design - extractive PDF cue:** (1) Here, fenc consists of d-dimensioned features for M points uniformly down-sampled from the input 3D scene through the Farthest Point Sampling (FPS) algorithm.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 3 (3.1. Problem Formatting), p. 3 (3.2. Model Design), p. 4 (3.2. Model Design). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formatting), interface p. 2 (1. Introduction), p. 3 (3.1. Problem Formatting), p. 3 (3.2. Model Design), p. 4 (3.2. Model Design), objective p. 4 (3.2. Model Design).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
