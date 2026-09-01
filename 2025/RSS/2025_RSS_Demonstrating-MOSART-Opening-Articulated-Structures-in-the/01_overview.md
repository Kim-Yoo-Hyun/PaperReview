# Demonstrating MOSART: Opening Articulated Structures in the Real World

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p033.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p033.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, mobile manipulation, articulated objects, real-world evaluation
- Official paper: https://www.roboticsproceedings.org/rss21/p033.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p033.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p033.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (25 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 Finally, we also consluct experiments to understand a) how MOSART compares to an end-to-end leaming approach, ) how sensitive MOSART is to the performance of each individual submodule, c) whether MOSART can ...를 문제로 두고, We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, Our approach, called MOSART for a MOdular ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** What does it take to build mobile manipalation systems that can competently operate on previously unseen ‘objects in previously unseen environments?
- **p. 1 / Abstract - extractive body cue:** This work answers this question using opening of articulated structures as a mobile ‘manipulation testbed.
- **p. 1 / Abstract - extractive body cue:** Specifically, our focus is on the end-to-end performance on this task without any privileged information, i.e. the robot starts at a location with the novel ...
- **p. 1 / Abstract - extractive body cue:** ‘open it, We first develop a system for this task, and then conduct 100+ end-to-end system tests across 13 real world test sites.
- **p. 1 / Abstract - extractive body cue:** Our large-scale study reveals a number of surprising findings: a) modular systems outperform end-to-end learned systems for this task, even when the end-to-end learned systems ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Finally, we also consluct experiments to understand a) how MOSART compares to an end-to-end leaming approach, ) how sensitive MOSART is to the performance of ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** It is not as much a failure in estimating articulation parameters, but the detection of target objects and estimation of the handle location in 3D ...

## Core Idea

- **p. 2 / 1. Iyrropucrion - extractive body cue:** We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, ...
- **p. 4 / B. Generating Motion Plans - extractive body cue:** In contrast to these approaches, we develop a system that operates on novel object instances in novel environments in a zero-shot manner without requiring any ...
- **p. 1 / Front matter - extractive body cue:** g novel cabinets, drawers, and ovens
- **p. 1 / Front matter - extractive body cue:** Specifically, we develop MOSART, a MOdular System for opening ARTiculated structures, and conduct extensive testing
- **p. 2 / Abstract - extractive body cue:** ‘models developed in isolation struggle when faced with robot ‘centric viewpoints.
- **p. 20 / A. Robot Utility Models - extractive body cue:** We provide additional details about Robot Utility Models (RUM) [16].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We also add additional heads to Mask RCNN; however, rather than directly predicting 3D outputs from the RGB-D input, we adopt a two-stage approach involving 2D prediction from RGB images followed by ... | egocentric RGB-D, language/task goal, base-arm proprioception | p. 4 (A. Predicting Articulation Parameters), p. 3 (A. Predicting Articulation Parameters) |
| State/latent | additional, heads, Mask, RCNN, however, rather, directly, predicting, outputs, RGB-D, input, adopt | map/object/contact state와 base-arm coordination decision | p. 4 (A. Predicting Articulation Parameters), p. 3 (A. Predicting Articulation Parameters), p. 2 (1. Iyrropucrion) |
| Output/action | Researchers have extensively looked at different aspects: a) construction of various datasets (from simulation (40, 14, 20], real world images [76, 36, 1], and real world 3D scans [2¢ 77), b) use ... | base motion plus arm/gripper action | p. 3 (A. Predicting Articulation Parameters), p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion) |
| Objective/outcome | long-horizon task success, reachability, collision과 recovery | long-horizon task success, reachability, collision과 recovery | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1. Iyrropucrion - extractive body cue:** We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, ...
- **p. 4 / B. Generating Motion Plans - extractive body cue:** In contrast to these approaches, we develop a system that operates on novel object instances in novel environments in a zero-shot manner without requiring any ...
- **p. 1 / Front matter - extractive body cue:** g novel cabinets, drawers, and ovens
- **p. 1 / Front matter - extractive body cue:** Specifically, we develop MOSART, a MOdular System for opening ARTiculated structures, and conduct extensive testing
- **p. 2 / Abstract - extractive body cue:** ‘models developed in isolation struggle when faced with robot ‘centric viewpoints.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: MOSART Design. The perception module outputs 3D articulation parameters in the robot frame using RGB-D images. The robot then navigates to the target ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We first present ‘our end-to-end system test results, evaluating MOSART on 31 novel drawers and cupboards across 10 buildings (Section IV-A), To see how a ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (IV. EXPERIMENTS), p. 3 (Figure/Table caption) |
| Embodiment/environment | In each test, the robot is placed approximately 1.5m from the target object with the camera oriented so as to have the target ‘object in view. | hardware/simulator version and reset protocol | p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | For most successful trials, the robot opens the drawer / cupboard completely (ie. drawers by 35cm and cupboards by 90°) in a graceful manner (see videos in supplementary materials). | role, split, size and leakage | p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Metric | Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments. | definition, denominator, direction and uncertainty | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (Figure/Table caption) |
| Baseline/ablation | This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to two recent articulation parameter prediction systems [53, 76], ... | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 8 (Figure/Table caption), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / Discussion - extractive body cue:** Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles.
- **p. 9 / V. Limitations - extractive body cue:** Finally, there are limitations of the embodiment we use (e.g. it cannot reach cabinets high up, or exert enough force to pull open fridge doors).
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8. 59% of failures (ie. 7 failures) are due to perception, including various kinds of failures, such as failure to detect meshed cabinets (2/7), ...
- **p. 10 / Discussion - extractive body cue:** Grasping failures accounted for approximately 25% of all observed failures, underscoring the inherent difficulty of achieving precise, last-centimeter adjustments required for successful grasping.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We then study the generalization of our pipeline to other articulation types and diverse handles (Section IV-E), before wwe analyze the failure modes of our ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Section IV-F° provides a extensive discussion of the failure modes
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Contact Correction. (a) shows a grasping attempt with No contact correction, whereas (b) shows the grasping attempt with contact correction. Due to compounding ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 Finally, we also consluct experiments to understand a) how MOSART compares to an end-to-end leaming approach, ) how sensitive MOSART is to the performance of each individual submodule, c) whether MOSART can ...를 문제로 두고, We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, Our approach, called MOSART for a MOdular ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 1 (Abstract), p. 20 (A. Robot Utility Models) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
