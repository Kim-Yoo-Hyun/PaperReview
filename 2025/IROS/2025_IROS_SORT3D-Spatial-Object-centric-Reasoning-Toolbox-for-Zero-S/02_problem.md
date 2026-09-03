# Problem - SORT3D: Spatial Object-centric Reasoning Toolbox for Zero-Shot 3D Grounding Using Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2504.18684; PDF retrieval source: https://arxiv.org/pdf/2504.18684. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Resolving natural language expressions referring to specific objects using semantic object attributes and inter-object spatial relations-the core challenge of 3D referential grounding-remains difficult despite being an intuitive task fo ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Interpreting object-referential language and grounding objects in 3D with spatial relations and attributes is essential for robots operating alongside humans.
- **p. 1 / Abstract - extractive body cue:** However, this task is often challenging due to the diversity of scenes, large number of fine-grained objects, and complex free-form nature of language references.
- **p. 1 / Abstract - extractive body cue:** Furthermore, in the 3D domain, obtaining large amounts of natural language training data is difficult.
- **p. 1 / Abstract - extractive body cue:** Thus, it is important for methods to learn from little data and zero-shot generalize to new environments.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we propose SORT3D, an approach that utilizes rich object attributes from 2D data and merges a heuristics-based spatial reasoning toolbox with ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Resolving natural language expressions referring to specific objects using semantic object attributes and inter-object spatial relations-the core challenge of 3D referential grounding-remains difficult despite being ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, training end-to-end learning-based methods on 3D referential grounding requires a large amount of annotated data aligning language references to a 3D scene, which the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Resolving natural language expressions referring to specific objects using semantic object attributes and inter-object spatial relations-the core challenge of 3D referential grounding-remains ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 3D referential grounding additionally acts as a precursor to downstream tasks such as object-goal navigation, multi-action instruction-following, and scene visual question answering ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | referential, grounding, additionally, acts, precursor, downstream, tasks, object-goal, navigation, multi-action | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | LLM, prompted, in-context, example, decompose, referential, statement, series | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: referential, grounding, additionally, acts, precursor, downstream, tasks, object-goal, navigation, multi-action | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Decision / output variable | geometry/map/query r; body terms: SORT3D, Spatial, Object-centric, Reasoning, Toolbox, Grounding, LLMs, arXiv | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Qwen2-VL-7B, VLM, found, perform, best, generating, accurate, concise | p. 3 (III. METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, training end-to-end learning-based methods on 3D referential grounding requires a large amount of annotated data aligning language references to a 3D scene, which the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate our method on standard 3D object referential grounding benchmarks, ReferIt3D [1] and IRef-VLA [17], and demonstrate performance competitive with SOTA on complex view-dependent ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also deploy our full pipeline on two robotic ground vehicles for real-time indoor navigation, demonstrating our method's ability to further generalize to previously unseen ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY)): To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown.

- **p. 2 / I. INTRODUCTION - extractive body cue:** As a result, our method only requires a single in-context example of the toolbox usage and no other training data.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate our method on standard 3D object referential grounding benchmarks, ReferIt3D [1] and IRef-VLA [17], and demonstrate performance competitive with SOTA on complex view-dependent ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** This component is the only pipeine change required for our method to be deployed in the real-world.
- **p. 3 / III. METHODOLOGY - extractive body cue:** The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In the bottom right, the model fails at pragmatics, picking out the rightmost pillow, instead of recognizing that ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), objective p. 3 (III. METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
