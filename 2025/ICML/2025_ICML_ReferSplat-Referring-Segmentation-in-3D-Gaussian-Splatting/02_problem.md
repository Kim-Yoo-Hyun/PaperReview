# Problem - ReferSplat: Referring Segmentation in 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=reuShgiHdg; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/165044. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Problem Statement and Method Overview)): However, these methods face significant limitations when applied to R3DGS.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce Referring 3D Gaussian Splatting Segmentation (R3DGS), a new task that aims to segment target objects in a 3D Gaussian scene based on natural ...
- **p. 1 / Abstract - extractive body cue:** This task requires the model to identify newly described objects that may be occluded or not directly visible in a novel view, posing a significant ...
- **p. 1 / Abstract - extractive body cue:** Developing this capability is crucial for advancing embodied AI.
- **p. 1 / Abstract - extractive body cue:** To support research in this area, we construct the first R3DGS dataset, Ref-LERF.
- **p. 1 / Abstract - extractive body cue:** Our analysis reveals that 3D multimodal understanding and spatial relationship modeling are key challenges for R3DGS.
- **p. 2 / 1. Introduction - extractive body cue:** However, these methods face significant limitations when applied to R3DGS.
- **p. 1 / 1. Introduction - extractive body cue:** To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these methods face significant limitations when applied to R3DGS. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | While the proposed Position-aware Cross-Modal Interaction module effectively captures the relationship between Gaussian representations and text descriptions, distinguishing between languages with similar ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | While, Position-aware, Cross-Modal, Interaction, module, effectively, captures, relationship, between, Gaussian | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | generate, high-quality, pseudo, masks, input, image, referring, expression | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: While, Position-aware, Cross-Modal, Interaction, module, effectively, captures, relationship, between, Gaussian | p. 5 (3.5. Gaussian-Text Contrastive Learning), p. 2 (1. Introduction), p. 4 (3.3. 3D Gaussian Referring Fields) |
| Decision / output variable | geometry/map/query r; body terms: bridge, introduce, task, Referring, Gaussian, Splatting, Segmentation, R3DGS | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: total, training, objective, Lloss, Lbce, Lcon, where, balancing | p. 6 (3.5. Gaussian-Text Contrastive Learning), p. 4 (3.3. 3D Gaussian Referring Fields), p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 5 (3.4. Position-aware Cross-Modal Interaction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 6 (3.5. Gaussian-Text Contrastive Learning), p. 5 (3.4. Position-aware Cross-Modal Interaction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.3. Ablation Study), p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 7 (4.3. Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** 1, R3DGS requires the model to identify newly described objects, even when occluded or not directly visible in the novel view, posing a significant challenge ...
- **p. 1 / 1. Introduction - extractive body cue:** To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene ...
- **p. 2 / 1. Introduction - extractive body cue:** One major drawback is the lack of interaction between the text query and Gaussian representations during training.
- **p. 3 / 3.2. Problem Statement and Method Overview - extractive body cue:** The key challenge lies in segmenting the target object in this unseen view, where it may be partially occluded or even entirely invisible.

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Problem Statement and Method Overview), p. 4 (3.3. 3D Gaussian Referring Fields)): To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene based on natural language expressions ...

- **p. 2 / 1. Introduction - extractive body cue:** To enhance spatial reasoning, we introduce a Position-aware Cross-Modal Interaction module that extracts position features for both Gaussians and language descriptions.
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose ReferSplat, an end-to-end framework that models 3D Gaussian points with natural language expressions in a spatially aware paradigm for Referring ...
- **p. 3 / 3.2. Problem Statement and Method Overview - extractive body cue:** To infuse languageawareness into the 3D Gaussians, we introduce a new property called referring features.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive body cue:** 2, our method surpasses existing approaches, establishing a superior referring segmentation framework in 3D Gaussian scenes.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 1) Our current method does not account for dynamic factors, which are crucial for real-world applications. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 2) While we focus on 3D referring segmentation in Gaussian Splatting, our method does not incorporate 3D visual ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our 3D Gaussian Referring Fields enable the model to recognize occluded or non-visible objects by leveraging multi-view 3D ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.5. Gaussian-Text Contrastive Learning), p. 2 (1. Introduction), p. 4 (3.3. 3D Gaussian Referring Fields), p. 4 (3.3. 3D Gaussian Referring Fields). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Problem Statement and Method Overview), interface p. 5 (3.5. Gaussian-Text Contrastive Learning), p. 2 (1. Introduction), p. 4 (3.3. 3D Gaussian Referring Fields), p. 4 (3.3. 3D Gaussian Referring Fields), objective p. 6 (3.5. Gaussian-Text Contrastive Learning), p. 4 (3.3. 3D Gaussian Referring Fields), p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 5 (3.4. Position-aware Cross-Modal Interaction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
