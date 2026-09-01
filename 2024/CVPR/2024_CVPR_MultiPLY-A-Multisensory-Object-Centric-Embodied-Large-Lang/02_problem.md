# Problem - MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Looking ahead, challenges inevitably exist for building embodied multisensory large language models.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Human beings possess the capability to multiply a m´elange of multisensory cues while actively exploring and interacting with the 3D world.
- **p. 1 / Abstract - extractive PDF cue:** Current multi-modal large language models, however, passively absorb sensory data as inputs, lacking the capacity to actively interact with the objects in the 3D environment ...
- **p. 1 / Abstract - extractive PDF cue:** To usher in the study of this area, we propose MultiPLY, a multisensory embodied large language model that could incorporate multisensory interactive data, including visual, ...
- **p. 1 / Abstract - extractive PDF cue:** To this end, we first collect Multisensory Universe, a large-scale multisensory interaction dataset comprising 500k data by deploying an LLM-powered embodied agent to engage with ...
- **p. 1 / Abstract - extractive PDF cue:** To perform instruction tuning with pretrained LLM on such generated data, we first encode the 3D scene as abstracted object-centric representations, and then introduce action ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Looking ahead, challenges inevitably exist for building embodied multisensory large language models.
- **p. 2 / 1. Introduction - extractive PDF cue:** The first challenge resides in the paucity of multisensory interaction data for training such an LLM.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Looking ahead, challenges inevitably exist for building embodied multisensory large language models. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | contributions, Multisensory, Universe, large-scale, dataset, comprising, data, collected, agent, engaging | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | observation, outcome, agent, sent, back, LLM, inputs, state | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: contributions, Multisensory, Universe, large-scale, dataset, comprising, data, collected, agent, engaging | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.4. Training & Inference) |
| Decision / output variable | geometry/map/query r; body terms: contributions, Multisensory, Universe, large-scale, dataset, comprising, data, collected | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.4. Training & Inference) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: feature, goes, through, Sigmoid, layer, optimized, binary, cross | p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference), p. 6 (4.4. Training & Inference) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (5.4. Task Decomposition), p. 8 (5.4. Task Decomposition), p. 6 (5.1. Object Retrieval) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** The first challenge resides in the paucity of multisensory interaction data for training such an LLM.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.4. Training & Inference), p. 5 (4.2. Action Tokens)): To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected by an agent engaging with the 3D embodied ...

- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we propose MultiPLY, a multisensory embodied LLM that could encode multisensory object-centric representations, including visual, audio, tactile, and thermal information, by deploying ...
- **p. 5 / 4.4. Training & Inference - extractive PDF cue:** Our training loss consists of two parts.
- **p. 5 / 4.2. Action Tokens - extractive PDF cue:** Note that the navigation action could be executed by any pre-defined pathfinder module and is not the research focus of this paper. • <OBSERVE> token ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | One limitation of our model is that currently MultiPLY does not involve detailed navigation and control policy, but ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | As these models cannot interact with the environment to get the tactile, impact sound, and temperature data, we ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Second, 3Dbased models surpass 2D models, mainly because singleview images sometimes fail to provide enough information to reason ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | LLaVA and 3D-LLM take the holistic representation as inputs, and thus fail to compete with models that could ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.4. Training & Inference), p. 5 (4.2. Action Tokens). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.4. Training & Inference), p. 5 (4.2. Action Tokens), objective p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference), p. 6 (4.4. Training & Inference).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
