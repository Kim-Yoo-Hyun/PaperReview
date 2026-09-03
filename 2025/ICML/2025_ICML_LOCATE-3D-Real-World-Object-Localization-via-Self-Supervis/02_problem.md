# Problem - LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=FKi6yjXwCN; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/165205. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 3 (1. Introduction), p. 4 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): They often require human annotation at inference time in the form of detailed 3D meshes or object instance segmentation, making them difficult to deploy on real-world devices.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present LOCATE 3D, a model for localizing objects in 3D scenes from referring expressions like "the small coffee table between the sofa and the ...
- **p. 1 / Abstract - extractive body cue:** Notably, LOCATE 3D operates directly on sensor observation streams (posed RGB-D frames), enabling real-world deployment on robots and AR devices.
- **p. 1 / Abstract - extractive body cue:** Key to our approach is 3D-JEPA, a novel self-supervised learning (SSL) algorithm applicable to sensor point clouds.
- **p. 1 / Abstract - extractive body cue:** It takes as input a 3D pointcloud featurized using 2D foundation models (CLIP, DINO).
- **p. 1 / Abstract - extractive body cue:** Subsequently, masked prediction in latent space is employed as a pretext task to aid the self-supervised learning of contextualized pointcloud features.
- **p. 1 / 1. Introduction - extractive body cue:** They often require human annotation at inference time in the form of detailed 3D meshes or object instance segmentation, making them difficult to deploy on ...
- **p. 3 / 1. Introduction - extractive body cue:** We found directly reconstructing such fine-grained and high-dimensional features to be difficult.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | They often require human annotation at inference time in the form of detailed 3D meshes or object instance segmentation, making them difficult ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Preprocessing: Lifting 2D Foundation Model Features into 3D Point Clouds We begin by preprocessing the inputs (posed RGB-D images) by constructing a ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Preprocessing, Lifting, Foundation, Model, Features, Point, Clouds, begin, inputs, posed | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | takes, inputs, point, clouds, features, lifted, foundation, models | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Preprocessing, Lifting, Foundation, Model, Features, Point, Clouds, begin, inputs, posed | p. 3 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: Specifically, decoder, module, consists, three, attention, blocks, self-attention | p. 4 (2.3.1. LANGUAGE-CONDITIONED 3D DECODER), p. 5 (2.3.1. LANGUAGE-CONDITIONED 3D DECODER), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Specifically, LOCATE, optimizes, composite, loss, function, includes, mask | p. 5 (2.3.2. TRAINING LOCATE 3D), p. 5 (2.3.2. TRAINING LOCATE 3D) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (2.3.2. TRAINING LOCATE 3D), p. 5 (2.3.2. TRAINING LOCATE 3D) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 20 (Figure/Table caption), p. 7 (Figure/Table caption), p. 20 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1. Introduction - extractive body cue:** We found directly reconstructing such fine-grained and high-dimensional features to be difficult.
- **p. 4 / 1. Introduction - extractive body cue:** This allows for faster mixing of information from the start, due to lack of an explicit grouping.
- **p. 2 / 1. Introduction - extractive body cue:** Crucially, LOCATE 3D achieves these impressive results with fewer assumptions compared to prior models.
- **p. 2 / 1. Introduction - extractive body cue:** It further exhibits strong generalization capabilities on held-out scenes and annotations in ScanNet++.

## What the Paper Changes

PDF body contribution framing (p. 4 (2.3.1. LANGUAGE-CONDITIONED 3D DECODER), p. 5 (2.3.1. LANGUAGE-CONDITIONED 3D DECODER), p. 1 (1. Introduction), p. 5 (2.3.1. LANGUAGE-CONDITIONED 3D DECODER), p. 2 (1. Introduction)): Specifically, each decoder module consists of three attention blocks: (1) a self-attention block that enables queries to refine their representations through mutual interaction, (2) a cross-attention block where queries extract ...

- **p. 5 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive body cue:** Our decoder consists of three parallel prediction heads (Figure 7) that process the refined learned queries Q independently as object proposals.
- **p. 1 / 1. Introduction - extractive body cue:** We outline our contributions in this work below.
- **p. 5 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive body cue:** For bounding boxes, we developed a novel architecture (Figure 7).
- **p. 2 / 1. Introduction - extractive body cue:** We show that the resulting 3D-JEPA features are contextualized for the scene, while the features lifted from 2D foundation models only provide local understanding.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Limitations We can utilize such caching because our benchmarks operate under static (ScanNet) or quasi-static (robot) environments. | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Figure 8: Learning rate schedule for encoder and decoder. Fine-tuning a pre-trained encoder alongside a randomly initialized decoder ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This choice better represents realworld deployment scenarios though it typically results in performance degradation due to sensor noise, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | As outlined earlier, our model is capable of working with sensor streams and does not require human intervention ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 3 (1. Introduction), p. 4 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), objective p. 5 (2.3.2. TRAINING LOCATE 3D), p. 5 (2.3.2. TRAINING LOCATE 3D).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
