# Problem - VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/xu25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/xu25c/xu25c.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): However, existing visual grounding datasets[1, 2] are scarce and limited to a pre-defined vocabulary, challenging the development of general models for open-world applications.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D visual grounding is crucial for robots, requiring integration of natural language and 3D scene understanding.
- **p. 1 / Abstract - extractive body cue:** Traditional methods depending on supervised learning with 3D point clouds are limited by scarce datasets.
- **p. 1 / Abstract - extractive body cue:** Recently zero-shot methods leveraging LLMs have been proposed to address the data issue.
- **p. 1 / Abstract - extractive body cue:** While effective, these methods only use object-centric information, limiting their ability to handle complex queries.
- **p. 1 / Abstract - extractive body cue:** In this work, we present VLM-Grounder, a novel framework using vision-language models (VLMs) for zero-shot 3D visual grounding based solely on 2D images.
- **p. 1 / 1 Introduction - extractive body cue:** However, existing visual grounding datasets[1, 2] are scarce and limited to a pre-defined vocabulary, challenging the development of general models for open-world applications.
- **p. 1 / 1 Introduction - extractive body cue:** Since LLMs cannot directly process 3D environments, these methods employ a point cloud-based 3D localization module [10, 11] to detect objects and convert their attributes ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, existing visual grounding datasets[1, 2] are scarce and limited to a pre-defined vocabulary, challenging the development of general models for open-world ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 2) Inputting many images quickly consumes the VLM's context length, limiting output content and potentially affecting performance. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Inputting, many, images, quickly, consumes, VLM, context, length, limiting, output | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Additionally, measure, retrieval, time, different, numbers, input, images | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Inputting, many, images, quickly, consumes, VLM, context, length, limiting, output | p. 4 (3 Methodology), p. 4 (3 Methodology), p. 7 (3 Methodology) |
| Decision / output variable | geometry/map/query r; body terms: While, methods, achieve, strong, performance, they, only, objectcentric | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Methodology) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: More, images, increase, inference, costs, including, token, usage | p. 4 (3 Methodology), p. 4 (3 Methodology), p. 7 (3 Methodology) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3 Methodology), p. 8 (3 Methodology), p. 6 (3 Methodology) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 19 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Since LLMs cannot directly process 3D environments, these methods employ a point cloud-based 3D localization module [10, 11] to detect objects and convert their attributes ...
- **p. 2 / 1 Introduction - extractive body cue:** Object 1 is a black cabinet at (x1, y1, z1).
- **p. 2 / 1 Introduction - extractive body cue:** However, estimating a 3D bounding box from a single image can be problematic due to limited field-of-view and inaccurate depth information.

## What the Paper Changes

PDF body contribution framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 1 (1 Introduction)): While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like "find the room with the most ...

- **p. 2 / 1 Introduction - extractive body cue:** Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts identified by the benchmark to stitch images, enhancing VLM's performance.
- **p. 3 / 3 Methodology - extractive body cue:** In this section, we present the overall framework of VLM-Grounder (Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To study the effects of stitching, we designed a novel benchmark called the VisualRetrieval Benchmark, detailed in Sec.
- **p. 1 / 1 Introduction - extractive body cue:** Our approach involves a VLM that analyzes user queries and sequences of images capturing the scene to locate the target object, whose 2D mask is ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 20 | Figure 5: Failure cases of the VLM grounding module. 20 | reported limitation/failure wording; scope must be verified |
| body cue at p. 21 | Figure 8: A failure case of the projection module. 21 | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Although our multi-view ensemble projection module helps mitigate this issue, it cannot entirely eliminate it. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 5 Conclusion and Limitations In this paper, we presented VLM-Grounder, a VLM agent that excels in zero-shot 3D ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3 Methodology), p. 4 (3 Methodology), p. 7 (3 Methodology), p. 7 (3 Methodology). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 4 (3 Methodology), p. 4 (3 Methodology), p. 7 (3 Methodology), p. 7 (3 Methodology), objective p. 4 (3 Methodology), p. 4 (3 Methodology), p. 7 (3 Methodology).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
