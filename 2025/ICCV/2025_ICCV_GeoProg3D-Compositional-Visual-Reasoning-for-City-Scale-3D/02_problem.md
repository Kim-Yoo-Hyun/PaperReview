# Problem - GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): However, when extending conventional 3D language fields for large-scale urban 3D scenes, two fundamental difficulties emerge: (1) Scalability for city-scale 3D data: Since existing methods primarily focus on indoor scenes, ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** The advancement of 3D language fields has enabled intuitive interactions with 3D scenes via natural language.
- **p. 1 / Abstract - extractive body cue:** However, existing approaches are typically limited to smallscale environments, lacking the scalability and compositional reasoning capabilities necessary for large, complex urban settings.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we propose GeoProg3D, a visual programming framework that enables natural language-driven interactions with city-scale highfidelity 3D scenes.
- **p. 1 / Abstract - extractive body cue:** GeoProg3D consists of two key components: (i) a Geography-aware City-scale 3D Language Field (GCLF) that leverages a memory-efficient hierarchical 3D model to handle large-scale data, ...
- **p. 1 / Abstract - extractive body cue:** Our framework employs large language models (LLMs) as reasoning engines to dynamically combine GV-APIs and operate GCLF, effectively supporting diverse geographic vision tasks.
- **p. 2 / 1. Introduction - extractive body cue:** However, when extending conventional 3D language fields for large-scale urban 3D scenes, two fundamental difficulties emerge: (1) Scalability for city-scale 3D data: Since existing methods ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, when extending conventional 3D language fields for large-scale urban 3D scenes, two fundamental difficulties emerge: (1) Scalability for city-scale 3D data: ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | summary, contributions, threefold, GeoProg3D, framework, compositional, reasoning, over, city-scale, language | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | GeoEval3D, composed, unique, queries, summary, contributions, threefold, GeoProg3D | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: summary, contributions, threefold, GeoProg3D, framework, compositional, reasoning, over, city-scale, language | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.3. Dataset construction and statistics) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, threefold, GeoProg3D, framework, compositional, reasoning, over | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.1. Task Definition) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5.1. Evaluation metrics), p. 7 (5.1. Evaluation metrics), p. 8 (5.2. Experimental results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.1. Task Definition)): In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform various 3D geographic vision tasks ...

- **p. 2 / 1. Introduction - extractive body cue:** To validate the effectiveness, we introduce novel tasks designed to assess urban-scale geographic visual reasoning capabilities and present GeoEval3D, a benchmark dataset specifically developed for ...
- **p. 6 / 4.1. Task Definition - extractive body cue:** The task set Qi = {(qk, ak)}Ki k=1 consists of pairs of queries qk and the corresponding ground truth answers ak.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Ablation study of different Geographical Vision APIs. itative examples and failure cases. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Note that MES-H and CMP are not evaluated in UrbanScene3D because Ground Truth for height cannot be obtained. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These results demonstrate the limitations of localization using 3D language fields alone in 3D urban scenes and the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.3. Dataset construction and statistics). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.3. Dataset construction and statistics), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
