# Problem - FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2402.04555; PDF retrieval source: https://arxiv.org/pdf/2402.04555. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, the supervised object detectors are trained in specific data distribution and lack generalization ability.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Semantic mapping based on the supervised object detectors is sensitive to image distribution.
- **p. 1 / Abstract - extractive PDF cue:** In real-world environments, the object detection and segmentation performance can lead to a major drop, preventing the use of semantic mapping in a wider domain.
- **p. 1 / Abstract - extractive PDF cue:** On the other hand, the development of vision-language foundation models demonstrates a strong zero-shot transferability across data distribution.
- **p. 1 / Abstract - extractive PDF cue:** It provides an opportunity to construct generalizable instance-aware semantic maps.
- **p. 1 / Abstract - extractive PDF cue:** Hence, this work explores how to boost instance-aware semantic mapping from object detection generated from foundation models.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, the supervised object detectors are trained in specific data distribution and lack generalization ability.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** However, these challenges have not been considered in traditional semantic mapping works.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, the supervised object detectors are trained in specific data distribution and lack generalization ability. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | GroundingDINO [6], the latest State-of-the-Arts (SOTA) openset object detection network, reads a text prompt and performs Manuscript received: October 24, 2023; Accepted: ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | GroundingDINO, latest, State-of-the-Arts, SOTA, openset, object, detection, network, reads, text | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | main, contributions, fuse, object, detections, visionlanguage, foundation, models | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: GroundingDINO, latest, State-of-the-Arts, SOTA, openset, object, detection, network, reads, text | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: incrementally, fuses, object, detections, foundation, models, instance-aware, semantic | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (6 Method) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Since, Kimera, updates, label, measurements, manually, assigned, likelihood | p. 6 (6 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (6 Method), p. 7 (6 Method), p. 7 (6 Method) |
| Success / guarantee | goal reach with collision-free execution | p. 5 (V. EXPERIMENT), p. 5 (Figure/Table caption), p. 1 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** However, these challenges have not been considered in traditional semantic mapping works.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** IEEE ROBOTICS AND AUTOMATION LETTERS, VOL.9, NO.3, MARCH 2024 2 challenges should be addressed.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** All of these foundation models are trained using large-scale data and demonstrate strong zero-shot generalization ability in various image distributions.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (6 Method), p. 6 (6 Method), p. 7 (6 Method)): Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map.

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To address such challenges, we propose a probabilistic label fusion method following the Bayes filter algorithm.
- **p. 6 / 6 Method - extractive PDF cue:** Compared with Kimera using RAM-GroundedSAM, our method achieved +15.6 mAP50.
- **p. 6 / 6 Method - extractive PDF cue:** The rest of the ScanNet experiment focus on evaluating each module of our method through an ablation study.
- **p. 7 / 6 Method - extractive PDF cue:** As shown in Figure 10(b), our method detects the table correctly.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, and GroundingDINO ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Fig. 6: The visualization shows instance voxel grid map (a) before and (b) after the merge. The inconsistent ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We consider those limitations of foundation models. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Compared with the original Fusion++ method, the main difference is that our implemented version does not maintain a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (6 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (6 Method), objective p. 6 (6 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
