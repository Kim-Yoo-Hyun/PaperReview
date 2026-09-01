# Problem - CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 3 (1) Visual con), p. 1 (1. Introduction), p. 2 (1) Visual con), p. 2 (1) Visual contextual)): However, current 3DSGG methods struggle with two main challenges.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** 3D Scene Graph Generation (3DSGG) aims to classify objects and their predicates within 3D point cloud scenes.
- **p. 1 / Abstract - extractive PDF cue:** However, current 3DSGG methods struggle with two main challenges.
- **p. 1 / Abstract - extractive PDF cue:** 1) The dependency on labor-intensive groundtruth annotations.
- **p. 1 / Abstract - extractive PDF cue:** 2) Closed-set classes training hampers the recognition of novel objects and predicates.
- **p. 1 / Abstract - extractive PDF cue:** Addressing these issues, our idea is to extract cross-modality features by CLIP from text and image data naturally related to 3D point clouds.
- **p. 3 / 1) Visual con - extractive PDF cue:** they are constrained by large language models (LLM) and lack the capacity for scene understanding.
- **p. 1 / 1. Introduction - extractive PDF cue:** Existing 3DSGG models are mainly working in two directions to improve the accuracy.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, current 3DSGG methods struggle with two main challenges. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Our approach begins with the extraction of cross-modality features from text T , image I, and 3D point clouds P (Section 3.1). | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | begins, extraction, cross-modality, features, text, image, point, clouds, Section, CCL-3DSGG | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | During, inference, input, prompt, point, cloud, object, class | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: begins, extraction, cross-modality, features, text, image, point, clouds, Section, CCL-3DSGG | p. 3 (3. Methods), p. 4 (3.1. Cross-modality Features Extraction), p. 5 (3.2. Cross-Modality Contrastive Losses) |
| Decision / output variable | path/waypoint/velocity; body terms: primary, contributions, summarized, practical, tasks, DSGG, Specifically, novel | p. 2 (1) Visual contextual), p. 1 (Abstract), p. 3 (3. Methods) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Contrastive, loss, optimization, methods, refine, representations, augmenting, similarity | p. 3 (3. Methods), p. 3 (1) Prompt learning based methods adjust to downstream), p. 4 (3.1. Cross-modality Features Extraction), p. 4 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4.4. Predicting Novel Classes), p. 6 (Figure/Table caption), p. 7 (4.4. Predicting Novel Classes) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1) Visual con - extractive PDF cue:** they are constrained by large language models (LLM) and lack the capacity for scene understanding.
- **p. 1 / 1. Introduction - extractive PDF cue:** Existing 3DSGG models are mainly working in two directions to improve the accuracy.
- **p. 2 / 1) Visual con - extractive PDF cue:** Concurrent works [4, 16, 25, 26] have harnessed 3DSG for robotics, yet 27864
- **p. 2 / 1) Visual contextual - extractive PDF cue:** To enhance the ability of model to understand spatial features, the current camera view is considered as positives and those from other views as negatives.

## What the Paper Changes

PDF contribution framing (p. 2 (1) Visual contextual), p. 1 (Abstract), p. 3 (3. Methods), p. 3 (3.1. Cross-modality Features Extraction), p. 4 (3.2. Cross-Modality Contrastive Losses)): The primary contributions are summarized as: • We propose the new and practical tasks of OV 3DSGG.

- **p. 1 / Abstract - extractive PDF cue:** Specifically, we propose a novel Cross-Modality Contrastive Learning 3DSGG (CCL-3DSGG) method.
- **p. 3 / 3. Methods - extractive PDF cue:** Our framework is depicted in Figure 2.
- **p. 3 / 3.1. Cross-modality Features Extraction - extractive PDF cue:** To enhance the discriminative power of text features and ensure precise cross-modality feature alignment, we propose segmenting text based on grammatical analysis [43, 50].
- **p. 4 / 3.2. Cross-Modality Contrastive Losses - extractive PDF cue:** The purpose of cross-modality contrastive losses is to align image and text to 3DSG, which consists of Multi-view Image-3DSG Contrastive (I3D) Loss and Text3DSG Contrastive ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Limitations: There are several limitations of our work and still much to do to realize the full potential ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For better viewing, we only show failure cases. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In future work, it will be interesting to design experiments to quantify the success of open vocabulary queries ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 1. (a) Difference in training: Previous 3DSGG models trained on closed-set classes by fully supervised [12, 48, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3. Methods), p. 4 (3.1. Cross-modality Features Extraction), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 3 (3.1. Cross-modality Features Extraction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Abstract), p. 3 (1) Visual con), p. 1 (1. Introduction), p. 2 (1) Visual con), p. 2 (1) Visual contextual), interface p. 3 (3. Methods), p. 4 (3.1. Cross-modality Features Extraction), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 3 (3.1. Cross-modality Features Extraction), objective p. 3 (3. Methods), p. 3 (1) Prompt learning based methods adjust to downstream), p. 4 (3.1. Cross-modality Features Extraction), p. 4 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
