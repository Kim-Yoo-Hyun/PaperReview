# Problem - Unifying 3D Vision-Language Understanding via Promptable Queries

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6043_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06043.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): Recent advancements in embodied artificial intelligence have emphasized the importance of connecting 3D scene understanding with natural language [16,27, 29, 44, 71].

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** Recent advancements in embodied artificial intelligence have emphasized the importance of connecting 3D scene understanding with natural language [16,27, 29, 44, 71].
- **p. 1 / 1 Introduction - extractive PDF cue:** This step is crucial for embodied agents to understand and execute human instructions in real-world scenarios [4,51].
- **p. 1 / 1 Introduction - extractive PDF cue:** In recent years, numerous tasks and datasets for benchmarking 3D scene understanding with languages have been proposed, including 3D semantic segmentation [52], 3D vision-language ⋆Work ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Prompt: [Navigate to the door] Prompt: [Chair] Prompt: [Cabinet to the left of the TV] Prompt: [I want to watch Super Bowl] Prompt: [Describe this ...
- **p. 5 / 3 Method - extractive PDF cue:** In this section, we present PQ3D, which consists of three main modules: Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning, as depicted in ...
- **p. 7 / 3 Method - extractive PDF cue:** 3.3 Prompt-guided Query Learning We propose a novel Transformer-like decoder to instruct the instance queries to assimilate scene and prompt information.
- **p. 6 / 3 Method - extractive PDF cue:** With such unification, we do not distinguish different prompt formats anymore and this design enables the model to transfer knowledge between different prompts.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Recent advancements in embodied artificial intelligence have emphasized the importance of connecting 3D scene understanding with natural language [16,27, 29, 44, 71]. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Finally, each updated instance query is fed into three output heads to predict an instance mask, a task-relevance score, and a sentence. ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Finally, updated, instance, query, three, output, heads, predict, mask, task-relevance | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Output, Heads, Losses, adopt, following, three, support, variety | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Finally, updated, instance, query, three, output, heads, predict, mask, task-relevance | p. 6 (3 Method), p. 8 (3 Method), p. 8 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: section, present, PQ3D, consists, three, main, modules, Task | p. 5 (3 Method), p. 7 (3 Method), p. 6 (3 Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: During, training, text, responses, provided, supervision, dense, caption | p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (3 Method), p. 6 (3 Method), p. 6 (3 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 11 (4 Experiments), p. 11 (Figure/Table caption), p. 12 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** This step is crucial for embodied agents to understand and execute human instructions in real-world scenarios [4,51].

## What the Paper Changes

PDF contribution framing (p. 5 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 6 (3 Method)): In this section, we present PQ3D, which consists of three main modules: Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning, as depicted in Fig.

- **p. 7 / 3 Method - extractive PDF cue:** 3.3 Prompt-guided Query Learning We propose a novel Transformer-like decoder to instruct the instance queries to assimilate scene and prompt information.
- **p. 6 / 3 Method - extractive PDF cue:** With such unification, we do not distinguish different prompt formats anymore and this design enables the model to transfer knowledge between different prompts.
- **p. 6 / 3 Method - extractive PDF cue:** Finally, each updated instance query is fed into three output heads to predict an instance mask, a task-relevance score, and a sentence. model [49], which ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | However, our model trained only on the Multi3DRefer dataset "PQ3D (sg.)" exhibits better performance in the ZT and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | As our model utilizes the CLIP text encoder, it may face limitations in understanding long sentences. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Different from 3D-VisTA, our model does not use a classification head for QA, which causes a performance drop ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | 5 Conclusions and Future Works In conclusion, our proposed PQ3D addresses the challenges in 3D vision-language learning (3D-VL) ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 6 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method), objective p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
