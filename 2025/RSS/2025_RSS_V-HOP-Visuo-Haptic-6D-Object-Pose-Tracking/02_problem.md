# Problem - V-HOP: Visuo-Haptic 6D Object Pose Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p037.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p037.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION)): (i) Domain generalization: Compared to visual-only baselines, visuo-tactile approaches struggle to generalize, hindered by insufficient data diversity and model scalability.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humans naturally int ision and haptic robus sreption during manipulation. ‘The loss of either ‘modality significantly degrades performance.
- **p. 1 / Abstract - extractive body cue:** Inspired by this multisensory integration, prior object pose estimation research has attempted to combine visual and hapticiactile feedback.
- **p. 1 / Abstract - extractive body cue:** Although these works demonstrate improvements in controlled environments or synthetic datasets, they often underperform mn-only approaches in real-world setlings due to poor generalization across diverse ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce a novel unified haptic representation that effectively handles multiple gripper embodiments.
- **p. 1 / Abstract - extractive body cue:** Building on this representation, we introduce a new visuo-haptic transformer-based object pose tracker that seamlessly integrates visual and haptic input.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** (i) Domain generalization: Compared to visual-only baselines, visuo-tactile approaches struggle to generalize, hindered by insufficient data diversity and model scalability.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** To address these challenges, we propose V-HOP (Fig.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (i) Domain generalization: Compared to visual-only baselines, visuo-tactile approaches struggle to generalize, hindered by insufficient data diversity and model scalability. | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | A, Problem Definition We tackle the model-based visu tracking problem, assuming access to: + Visual observations: An RGB-D sensor observes the object ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF |
| State / latent | Problem, Definition, tackle, model-based, visu, tracking, assuming, access, Visual, observations | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | Recent, state-of-the-art, object, pose, estimation, methods, FoundationPose, have | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: Problem, Definition, tackle, model-based, visu, tracking, assuming, access, Visual, observations | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| Decision / output variable | contact-aware action/force; body terms: First, introduce, novel, unified, haptic, representation, facilitates, cross-embodiment | p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Objective / loss / cost | contact prediction/control error; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | slip/contact success and safe interaction | p. 8 (B. Bimanual Handover Experiment), p. 8 (B. Bimanual Handover Experiment), p. 9 (C. Can-in-Mug Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. INTRODUCTION - extractive body cue:** To address these challenges, we propose V-HOP (Fig.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this section, we first define the problem formally and then review existing haptic representations and our proposed unified representation,
- **p. 2 / 1. INTRODUCTION - extractive body cue:** based visual pose tracking problem [66, 7]. while the inputs

## What the Paper Changes

PDF contribution framing (p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (III. MeTHODOLOGY)): First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning.

- **p. 1 / 1. INTRODUCTION - extractive body cue:** To address these challenges, we propose V-HOP (Fig.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Second, we propose 4 transformer-based object pose tracker to fuse visual and haptic features.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Our method demonstrates remarkable robustness and significantly outperforms FoundationPose, which could lose object tracks entirely (Fig.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** Later, we introduce our visuo-haptic model and how it is trained.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Successful execution hinges on precise pose estimation for both objects, as any noise in their poses can lead ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Inaccurate tracking results could lead to collision during the handover. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | More recent works aim to overcome some of these limitations. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (III. MeTHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), interface p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (III. MeTHODOLOGY), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
