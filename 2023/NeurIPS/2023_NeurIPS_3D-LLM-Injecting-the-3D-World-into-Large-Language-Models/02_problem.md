# Problem - 3D-LLM: Injecting the 3D World into Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.12981; PDF retrieval source: https://arxiv.org/pdf/2307.12981. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract)): Large language models (LLMs) and Vision-Language Models (VLMs) have been proven to excel at multiple tasks, such as commonsense reasoning.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Large language models (LLMs) and Vision-Language Models (VLMs) have been proven to excel at multiple tasks, such as commonsense reasoning.
- **p. 1 / Abstract - extractive body cue:** Powerful as these models can be, they are not grounded in the 3D physical world, which involves richer concepts such as spatial relationships, affordances, physics, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose to inject the 3D world into large language models and introduce a whole new family of 3D-LLMs.
- **p. 1 / Abstract - extractive body cue:** Specifically, 3D-LLMs can take 3D point clouds and their features as input and perform a diverse set of 3D-related tasks, including captioning, dense captioning, 3D ...
- **p. 1 / Abstract - extractive body cue:** Using three types of prompting mechanisms that we design, we are able to collect over 300k 3D-language data covering these tasks.
- **p. 3 / 5. Facing the mirror and dress - extractive body cue:** To sum up, our paper has the following contributions: • We introduce a new family of 3D-based Large Language models (3D-LLMs) that can take 3D ...
- **p. 2 / 5. Facing the mirror and dress - extractive body cue:** To address this, we propose a set of unique data generation pipelines that could generate large-scale 3D data paired with language.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Large language models (LLMs) and Vision-Language Models (VLMs) have been proven to excel at multiple tasks, such as commonsense reasoning. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | To this end, we propose to inject the 3D world into large language models, and introduce a whole new family of 3D-LLMs ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | inject, world, large, language, models, introduce, whole, family, D-LLMs, could | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | After, adding, additional, location, tokens, unfreeze, weights, input | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: inject, world, large, language, models, introduce, whole, family, D-LLMs, could | p. 2 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress) |
| Decision / output variable | geometry/map/query r; body terms: following, contributions, introduce, family, D-based, Large, Language, models | p. 3 (5. Facing the mirror and dress), p. 1 (Abstract), p. 2 (5. Facing the mirror and dress) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Then, align, features, rays, pixels, MSE, loss, taking | p. 6 (5. Facing the mirror and dress) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (5. Facing the mirror and dress), p. 2 (5. Facing the mirror and dress) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** Powerful as these models can be, they are not grounded in the 3D physical world, which involves richer concepts such as spatial relationships, affordances, physics, ...

## What the Paper Changes

PDF body contribution framing (p. 3 (5. Facing the mirror and dress), p. 1 (Abstract), p. 2 (5. Facing the mirror and dress), p. 3 (5. Facing the mirror and dress), p. 2 (5. Facing the mirror and dress)): To sum up, our paper has the following contributions: • We introduce a new family of 3D-based Large Language models (3D-LLMs) that can take 3D points with features and language ...

- **p. 1 / Abstract - extractive body cue:** In this work, we propose to inject the 3D world into large language models and introduce a whole new family of 3D-LLMs.
- **p. 2 / 5. Facing the mirror and dress - extractive body cue:** To address this, we propose a set of unique data generation pipelines that could generate large-scale 3D data paired with language.
- **p. 3 / 5. Facing the mirror and dress - extractive body cue:** We introduce a 3D localization mechanism for training the 3D-LLMs to better capture 3D spatial information. • Experiments on held-out evaluation dataset, ScanQA, outperform state-of-the-art ...
- **p. 2 / 5. Facing the mirror and dress - extractive body cue:** Unlike the vast amount of paired 2D-images-and-text data on the Internet, the scarcity of 3D data hinders the development of 3D-based foundation models.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | A limitation is that the 3D feature extractor relies on 2D multi-view images, and thus all 3D scenes ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We report BLEU, ROUGE-L, METEOR, CIDEr for robust answer matching. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress), p. 2 (5. Facing the mirror and dress). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), interface p. 2 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress), p. 2 (5. Facing the mirror and dress), objective p. 6 (5. Facing the mirror and dress).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
