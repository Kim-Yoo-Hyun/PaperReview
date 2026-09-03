# Problem - Search3D: Hierarchical Open-Vocabulary 3D Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.18431; PDF retrieval source: https://arxiv.org/pdf/2409.18431. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Finally, the least obvious limitation is derived from the way these models compute the point-level features: Although the projected open-vocabulary features are fine-grained at the level of the geometrical scene ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D segmentation enables exploration of 3D spaces using free-form text descriptions.
- **p. 1 / Abstract - extractive body cue:** Existing methods for open-vocabulary 3D instance segmentation primarily focus on identifying object-level instances but struggle with finer-grained scene entities such as object parts, or regions ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Search3D, an approach to construct hierarchical open-vocabulary 3D scene representations, enabling 3D search at multiple levels of granularity: fine-grained object ...
- **p. 1 / Abstract - extractive body cue:** Unlike prior methods, Search3D shifts towards a more flexible open-vocabulary 3D search paradigm, moving beyond explicit object-centric queries.
- **p. 1 / Abstract - extractive body cue:** For systematic evaluation, we further contribute a scene-scale open-vocabulary 3D part segmentation benchmark based on MultiScan, along with a set of open-vocabulary fine-grained part annotations ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, the least obvious limitation is derived from the way these models compute the point-level features: Although the projected open-vocabulary features are fine-grained at the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, storing these per-point features is memoryintensive, they are inherently noisy, and they lack instance-level information - a critical requirement for real-world applications in which ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Finally, the least obvious limitation is derived from the way these models compute the point-level features: Although the projected open-vocabulary features are ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | This representation is built upon 3D scenes reconstructed using posed RGB-D image sequences, as shown in Fig. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | representation, built, upon, scenes, reconstructed, posed, RGB-D, image, sequences, Fig | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Ultimately, systems, designed, real-world, interactions, must, able, identify | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: representation, built, upon, scenes, reconstructed, posed, RGB-D, image, sequences, Fig | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: summarize, contributions, hierarchical, open-vocabulary, segmentation, capable, segmenting, entire | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: segment, neighboring, segments, within, same, object, exhibit, similar | p. 4 (2) Computing open-vocabulary features for the scene repre), p. 1 (I. INTRODUCTION), p. 4 (2) Computing open-vocabulary features for the scene repre) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (2) Computing open-vocabulary features for the scene repre), p. 4 (2) Computing open-vocabulary features for the scene repre) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, storing these per-point features is memoryintensive, they are inherently noisy, and they lack instance-level information - a critical requirement for real-world applications in which ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A purely object-centric understanding fails to provide this level of detail.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While effective for these predefined classes, such approaches struggle to generalize to novel classes.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary textual queries, by aggregating features ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** To evaluate our method, we introduce a novel evaluation suite for open-vocabulary scene-scale 3D part segmentation based on MultiScan [16].
- **p. 3 / III. METHOD - extractive body cue:** We introduce a novel hierarchical 3D scene representation enabling open-vocabulary segmentation for scene entities at multiple granularities, including objects and their parts.
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: We propose Search3D, a method for open-vocabulary 3D search at multiple levels of granularity.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables searching across objects, parts, and attributes matching any given user query (right). critical to scene interaction.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Discussion and Limitations One limitation of our work is the reliance on a simple geometrical over-segmentation method for ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (2) Computing open-vocabulary features for the scene repre). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (2) Computing open-vocabulary features for the scene repre), objective p. 4 (2) Computing open-vocabulary features for the scene repre), p. 1 (I. INTRODUCTION), p. 4 (2) Computing open-vocabulary features for the scene repre).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
