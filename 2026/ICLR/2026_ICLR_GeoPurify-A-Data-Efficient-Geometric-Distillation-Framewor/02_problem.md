# Problem - GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=mN49LupE8l; PDF retrieval source: https://openreview.net/pdf/57fa2e7334b7e5972b3c62c83d3aecf630a1f0e3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): However, this often results in severe geometric inconsistencies, since 2D models lack awareness of 3D spatial structure.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Recent attempts to transfer features from 2D Vision-Language Models (VLMs) to 3D semantic segmentation expose a persistent trade-off.
- **p. 1 / ABSTRACT - extractive PDF cue:** Directly projecting 2D features into 3D yields noisy and fragmented predictions, whereas enforcing geometric coherence necessitates costly training pipelines and large-scale, annotated 3D data.
- **p. 1 / ABSTRACT - extractive PDF cue:** We argue that this limitation stems from the dominant segmentationand-matching paradigm, which fails to reconcile 2D semantics with 3D geometric structure.
- **p. 1 / ABSTRACT - extractive PDF cue:** The geometric cues are not eliminated during the 2D-to-3D transfer but remain latent within the noisy and view-aggregated features.
- **p. 1 / ABSTRACT - extractive PDF cue:** To exploit this property, we propose GeoPurify that applies a small Student Affinity Network to purify 2D VLM-generated 3D point features using geometric priors distilled ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, this often results in severe geometric inconsistencies, since 2D models lack awareness of 3D spatial structure.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** This approach fails to scale to the diverse and complex real-world objects and is further constrained by the prohibitive cost of manual 3D annotation, a ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, this often results in severe geometric inconsistencies, since 2D models lack awareness of 3D spatial structure. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 3.1 OVERALL ARCHITECTURE As illustrated in Figure 2, our proposed GeoPurify first leverages a frozen Vision-Language Model (Ψ2D) to transfer and merge ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | OVERALL, ARCHITECTURE, illustrated, Figure, GeoPurify, first, leverages, frozen, Vision-Language, Model | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Training-free, methods, directly, exploit, VLMs, segmentation, projecting, multi-view | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: OVERALL, ARCHITECTURE, illustrated, Figure, GeoPurify, first, leverages, frozen, Vision-Language, Model | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 1 (1 INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, introduce, GeoPurify, data-efficient, framework, built, hypothesis | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: student, network, maps, point, cloud, geometric, embeddings, Ggeo | p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4 EXPERIMENTS), p. 21 (Figure/Table caption), p. 6 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** This approach fails to scale to the diverse and complex real-world objects and is further constrained by the prohibitive cost of manual 3D annotation, a ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our proposed method aims to bridge this critical gap by purifying the semantically rich 2D features with robust 3D geometric priors. disconnects geometry and semantics.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** As shown in Figure 1-(b), 2D VLM features (Fsem) are semantically rich but geometrically inconsistent, resulting fragments and shape distortion, whereas priors from 3D self-supervised ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 1 (1 INTRODUCTION)): In summary, our contributions are: • We introduce GeoPurify, a data-efficient framework built on the hypothesis that beyond their semantic richness, VLM-projected features also embed a latent 3D geometric structure.

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Motivated by this hypothesis, we present GeoPurify, a data-efficient framework designed to recover latent geometric structure from noisy semantic features and produce robust 3D representations.
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** To address this, we introduce a 3D student affinity network ϕS that learns geometric affinities from the point cloud using a self-supervised 3D geometric model ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** 3.3 GEOMETRIC CONTRASTIVE DISTILLATION To rectify the geometric inconsistencies within the initial semantic features Fsem, we introduce a contrastive purification module trained via knowledge distillation.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** To move beyond these limitations, the field is shifting toward open-vocabulary 3D understanding, which enables models to identify objects using arbitrary descriptions rather than predefined ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 21 | Figure 6: Illustration of typical failure modes. From left to right: challenges with the presence of over-smoothing artifacts ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | First, we filter for quality, culling any scene that falls below the median value for both richness (Nc) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Without them, the model learns the global scene layout but fails to disentangle co-located surfaces. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 1: The Fundamental Disconnect: Semantic Richness vs. Geometric Coherence. Left: Original RGB 3D scene. Middle: Features distilled ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), objective p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
