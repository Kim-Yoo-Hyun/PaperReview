# Problem - Towards Physically Executable 3D Gaussian for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=HB6KvsqcAn; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/246616. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): (2) Lack of a physically executable structure.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** 3D Gaussian Splatting (3DGS), a 3D representation method with photorealistic real-time rendering capabilities, is regarded as an effective tool for narrowing the sim-to-real gap.
- **p. 1 / ABSTRACT - extractive body cue:** However, it lacks fine-grained semantics and physical executability for Visual-Language Navigation (VLN).
- **p. 1 / ABSTRACT - extractive body cue:** To address this, we propose SAGE-3D (Semantically and Physically Aligned Gaussian Environments for 3D Navigation), a new paradigm that upgrades 3DGS into an executable, semantically ...
- **p. 1 / ABSTRACT - extractive body cue:** It comprises two components: (1) ObjectCentric Semantic Grounding, which adds object-level fine-grained annotations to 3DGS; and (2) Physics-Aware Execution Jointing, which embeds collision objects into ...
- **p. 1 / ABSTRACT - extractive body cue:** We release InteriorGS, containing 1K object-annotated 3DGS indoor scene data, and introduce SAGE-Bench, the first 3DGS-based VLN benchmark with 2M VLN data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (2) Lack of a physically executable structure.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Consequently, deriving reliable collision geometries from 3DGS is difficult, and aligning semantics with appearance is non-trivial.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (2) Lack of a physically executable structure. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Vision-and-Language Navigation (VLN) is a core capability for Vision-Language Action (VLA) models, enabling them to follow natural language instructions and navigate complex ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Vision-and-Language, Navigation, VLN, core, capability, Vision-Language, Action, VLA, models, enabling | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Additionally, design, semantic, top-down, derived, DGS, support, instruction | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Vision-and-Language, Navigation, VLN, core, capability, Vision-Language, Action, VLA, models, enabling | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: introduce, DGS-Mesh, Hybrid, Representation, starting, mesh, scene, data | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: shortest-path, search, generate, trajectories, cost, function, integrates, free-space | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 15 (A IMPLEMENTATION DETAILS) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Consequently, deriving reliable collision geometries from 3DGS is difficult, and aligning semantics with appearance is non-trivial.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using 3DGS to provide photorealistic appearance.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we present SAGE-3D (Semantically and Physically Aligned Gaussian Environments for 3D Navigation), a paradigm that upgrades 3DGS from a purely perceptual scene ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 4 corroborate this finding: the NaVILA model (blue trajectory) exhibits unsmooth movement and persistent collisions that conventional metrics ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1: Traditional 3DGS vs. Our work. Compared with traditional 3DGS, our InteriorGS pro- vides object-level 3DGS annotations ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 15 (A IMPLEMENTATION DETAILS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 15 (A IMPLEMENTATION DETAILS), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
