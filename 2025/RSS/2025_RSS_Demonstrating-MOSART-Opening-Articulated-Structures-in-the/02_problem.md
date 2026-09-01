# Problem - Demonstrating MOSART: Opening Articulated Structures in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p033.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p033.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 1 (Abstract)): Finally, we also consluct experiments to understand a) how MOSART compares to an end-to-end leaming approach, ) how sensitive MOSART is to the performance of each individual submodule, c) whether ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** What does it take to build mobile manipalation systems that can competently operate on previously unseen ‘objects in previously unseen environments?
- **p. 1 / Abstract - extractive body cue:** This work answers this question using opening of articulated structures as a mobile ‘manipulation testbed.
- **p. 1 / Abstract - extractive body cue:** Specifically, our focus is on the end-to-end performance on this task without any privileged information, i.e. the robot starts at a location with the novel ...
- **p. 1 / Abstract - extractive body cue:** ‘open it, We first develop a system for this task, and then conduct 100+ end-to-end system tests across 13 real world test sites.
- **p. 1 / Abstract - extractive body cue:** Our large-scale study reveals a number of surprising findings: a) modular systems outperform end-to-end learned systems for this task, even when the end-to-end learned systems ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Finally, we also consluct experiments to understand a) how MOSART compares to an end-to-end leaming approach, ) how sensitive MOSART is to the performance of ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** It is not as much a failure in estimating articulation parameters, but the detection of target objects and estimation of the handle location in 3D ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Finally, we also consluct experiments to understand a) how MOSART compares to an end-to-end leaming approach, ) how sensitive MOSART is to ... | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | We also add additional heads to Mask RCNN; however, rather than directly predicting 3D outputs from the RGB-D input, we adopt a ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF |
| State / latent | additional, heads, Mask, RCNN, however, rather, directly, predicting, outputs, RGB-D | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | surprise, find, modular, system, outperforms, latest, endto-end, learning | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: additional, heads, Mask, RCNN, however, rather, directly, predicting, outputs, RGB-D | p. 4 (A. Predicting Articulation Parameters), p. 3 (A. Predicting Articulation Parameters), p. 2 (1. Iyrropucrion) |
| Decision / output variable | base plus arm/gripper action; body terms: considered, broad, ways, putting, together, system, modular, end-to-end | p. 2 (1. Iyrropucrion), p. 4 (B. Generating Motion Plans), p. 1 (Front matter) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | task completion and recovery | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1. Iyrropucrion - extractive body cue:** It is not as much a failure in estimating articulation parameters, but the detection of target objects and estimation of the handle location in 3D ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** In comparison, an imitation learning system will need to recollect a large amount of training data for tackling a new articulation type. * The failure ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** A major obstacle to realizing this vision lies in the lack of strong generalization capabilities: current systems struggle to adapt to novel objects and unfamiliar ...
- **p. 1 / Abstract - extractive body cue:** Our large-scale study reveals a number of surprising findings: a) modular systems outperform end-to-end learned systems for this task, even when the end-to-end learned systems ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Iyrropucrion), p. 4 (B. Generating Motion Plans), p. 1 (Front matter), p. 1 (Front matter), p. 2 (Abstract)): We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, Our approach, called MOSART for ...

- **p. 4 / B. Generating Motion Plans - extractive body cue:** In contrast to these approaches, we develop a system that operates on novel object instances in novel environments in a zero-shot manner without requiring any ...
- **p. 1 / Front matter - extractive body cue:** g novel cabinets, drawers, and ovens
- **p. 1 / Front matter - extractive body cue:** Specifically, we develop MOSART, a MOdular System for opening ARTiculated structures, and conduct extensive testing
- **p. 2 / Abstract - extractive body cue:** ‘models developed in isolation struggle when faced with robot ‘centric viewpoints.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Finally, there are limitations of the embodiment we use (e.g. it cannot reach cabinets high up, or exert ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Figure 8. 59% of failures (ie. 7 failures) are due to perception, including various kinds of failures, such ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Grasping failures accounted for approximately 25% of all observed failures, underscoring the inherent difficulty of achieving precise, last-centimeter ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (A. Predicting Articulation Parameters), p. 3 (A. Predicting Articulation Parameters), p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 1 (Abstract), interface p. 4 (A. Predicting Articulation Parameters), p. 3 (A. Predicting Articulation Parameters), p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
