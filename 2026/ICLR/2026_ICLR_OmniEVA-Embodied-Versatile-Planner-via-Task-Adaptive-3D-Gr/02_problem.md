# Problem - OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (52 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=tkEmIJv1tB; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247599. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): In particular, neglecting object affordances, workspace limitations, and kinematic feasibility leads to action sequences that cannot be executed on physical platforms.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Recent advances in multimodal large language models (MLLMs) have opened new opportunities for embodied intelligence, enabling multimodal understanding, reasoning, and interaction, as well as continuous ...
- **p. 1 / ABSTRACT - extractive body cue:** Nevertheless, current MLLM-based embodied systems face two critical limitations.
- **p. 1 / ABSTRACT - extractive body cue:** First, Geometric Adaptability Gap: models trained solely on 2D inputs or with hard-coded 3D geometry injection suffer from either insufficient spatial information or restricted 2D ...
- **p. 1 / ABSTRACT - extractive body cue:** Second, Embodiment Constraint Gap: prior work often neglects the physical constraints of real robots, resulting in task plans that are theoretically valid but practically infeasible.To ...
- **p. 1 / ABSTRACT - extractive body cue:** (2) an Embodiment-Aware Reasoning framework that incorporates task goals and physical constraints into the reasoning loop, ensuring executable plans.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In particular, neglecting object affordances, workspace limitations, and kinematic feasibility leads to action sequences that cannot be executed on physical platforms.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, the absence of embodied long-horizon planning benchmarks that explicitly incorporate embodiment constraints makes it difficult to systematically evaluate the unique challenges they pose.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In particular, neglecting object affordances, workspace limitations, and kinematic feasibility leads to action sequences that cannot be executed on physical platforms. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | OVERVIEW, OmniEVA, builds, pretrained, MLLMs, typically, comprises, three, principal, components | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | OmniEVA, designed, accommodate, wide, range, input, modalities, output | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: OVERVIEW, OmniEVA, builds, pretrained, MLLMs, typically, comprises, three, principal, components | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 17 (A.2 INPUT MODALITIES AND OUTPUT REPRESENTATIONS) |
| Decision / output variable | geometry/map/query r; body terms: address, limitations, introduce, OmniEVA, Embodied, Versatile, Planner, novel | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Given, reward, i-th, response, rformat, racc, ViT, encoder | p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 18 (A.3 IMPLEMENTATION DETAIL OF EMBODIMENT-AWARE REASONING), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (Figure/Table caption), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, the absence of embodied long-horizon planning benchmarks that explicitly incorporate embodiment constraints makes it difficult to systematically evaluate the unique challenges they pose.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY), p. 18 (A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS), p. 4 (3 METHODOLOGY)): To address these limitations, we introduce OmniEVA (Embodied Versatile Planner), a novel architecture that pioneers Task-Adaptive 3D Grounding and Embodiment-aware Reasoning.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** OmniEVA is the first framework to dynamically integrate 2D and 3D inputs via taskconditioned feature selection, enabling versatile and executable embodied reasoning through two key ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** Dynamic 3D Injection via Gated Routing Rather than applying 3D positional encoding uniformly for all tasks, we propose a Task-Adaptive Gated Router (TAGR) that selectively ...
- **p. 18 / A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS - extractive body cue:** This format enables precise object localization and descriptive annotation within a single image frame.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Left: The overall architecture of OmniEVA, featuring a novel task-adaptive gated router that dynamically incorporates 3D positional embeddings.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 1: Performance Comparison across 2D and 3D Embodied Reasoning Benchmarks. Despite recent progress, two core challenges remain. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 26 | Designed to overcome the limitations of traditional multimodal models-which primarily operate at the image-level or bounding box-level-it incorporates ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 29 | To overcome these limitations, we introduce a 3D-aware planning framework that ingests sequential RGB-D observations and directly generates ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 29 | Physical constraints, including object location, size, collision potential, must be considered, making this task highly relevant to the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 17 (A.2 INPUT MODALITIES AND OUTPUT REPRESENTATIONS), p. 18 (A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 17 (A.2 INPUT MODALITIES AND OUTPUT REPRESENTATIONS), p. 18 (A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS), objective p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
