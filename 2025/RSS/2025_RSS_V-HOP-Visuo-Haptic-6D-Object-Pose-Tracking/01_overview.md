# V-HOP: Visuo-Haptic 6D Object Pose Tracking

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p037.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p037.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, visuo-haptic perception, 6D pose, tactile sensing, state estimation, manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p037.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p037.pdf
- Code/Project: https://ivl.cs.brown.edu/research/v-hop
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 (i) Domain generalization: Compared to visual-only baselines, visuo-tactile approaches struggle to generalize, hindered by insufficient data diversity and model scalability.를 문제로 두고, First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans naturally int ision and haptic robus sreption during manipulation. ‘The loss of either ‘modality significantly degrades performance.
- **p. 1 / Abstract - extractive body cue:** Inspired by this multisensory integration, prior object pose estimation research has attempted to combine visual and hapticiactile feedback.
- **p. 1 / Abstract - extractive body cue:** Although these works demonstrate improvements in controlled environments or synthetic datasets, they often underperform mn-only approaches in real-world setlings due to poor generalization across diverse ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce a novel unified haptic representation that effectively handles multiple gripper embodiments.
- **p. 1 / Abstract - extractive body cue:** Building on this representation, we introduce a new visuo-haptic transformer-based object pose tracker that seamlessly integrates visual and haptic input.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** (i) Domain generalization: Compared to visual-only baselines, visuo-tactile approaches struggle to generalize, hindered by insufficient data diversity and model scalability.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** To address these challenges, we propose V-HOP (Fig.

## Core Idea

- **p. 1 / 1. INTRODUCTION - extractive body cue:** First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** To address these challenges, we propose V-HOP (Fig.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Second, we propose 4 transformer-based object pose tracker to fuse visual and haptic features.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Our method demonstrates remarkable robustness and significantly outperforms FoundationPose, which could lose object tracks entirely (Fig.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** Later, we introduce our visuo-haptic model and how it is trained.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** We first outline the core representations used in our haptic modality: gripper and object representations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A, Problem Definition We tackle the model-based visu tracking problem, assuming access to: + Visual observations: An RGB-D sensor observes the object in the environment. + Haptic feedback: The object is manipulated ... | tactile image/force, vision과 proprioceptive history | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| State/latent | Problem, Definition, tackle, model-based, visu, tracking, assuming, access, Visual, observations, RGB-D, sensor | contact geometry, force state 또는 latent dynamics | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| Output/action | 2) A sequence of RGB-D images O ~ {O,}{_. where each observation O, = 1;,.Dj] includes an RGB image I, and a depth map D, | grasp/contact action, force command 또는 object motion | p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (III. MeTHODOLOGY) |
| Objective/outcome | slip/contact success, force/pose error와 robustness | slip/contact success, force/pose error와 robustness | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / 1. INTRODUCTION - extractive body cue:** First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** To address these challenges, we propose V-HOP (Fig.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Second, we propose 4 transformer-based object pose tracker to fuse visual and haptic features.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Our method demonstrates remarkable robustness and significantly outperforms FoundationPose, which could lose object tracks entirely (Fig.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** Later, we introduce our visuo-haptic model and how it is trained.
- **p. 7 / experiment - extractive body cue:** Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance of ...
- **p. 7 / experiment - extractive body cue:** V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score.
- **p. 8 / B. Bimanual Handover Experiment - extractive body cue:** ‘TABLE VI: Success rate on bimanual handover task:

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (experiment), p. 7 (experiment) |
| Embodiment/environment | Our synthesized dataset exemplifies this principle and supports our robust real-world performance. | hardware/simulator version and reset protocol | p. 5 (A. Multi-embodied Dataset), p. 5 (A. Multi-embodied Dataset) |
| Dataset/benchmark | To validate the real-world effectiveness of our approach, wwe perform sim-to-real experiments using our robot platform, (Fig. | role, split, size and leakage | p. 5 (A. Multi-embodied Dataset), p. 5 (A. Multi-embodied Dataset), p. 7 (experiment), p. 7 (experiment) |
| Metric | ‘TABLE VI: Success rate on bimanual handover task: | definition, denominator, direction and uncertainty | p. 8 (B. Bimanual Handover Experiment), p. 8 (B. Bimanual Handover Experiment), p. 9 (C. Can-in-Mug Experiment) |
| Baseline/ablation | V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. | fair input/data/compute/action matching | p. 7 (experiment), p. 7 (experiment), p. 8 (B. Bimanual Handover Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 7 / B. Bimanual Handover Experiment - extractive body cue:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp.
- **p. 8 / C. Can-in-Mug Experiment - extractive body cue:** Successful execution hinges on precise pose estimation for both objects, as any noise in their poses can lead to failure.
- **p. 7 / B. Bimanual Handover Experiment - extractive body cue:** Inaccurate tracking results could lead to collision during the handover.
- **p. 9 / VI. RELATED Works - extractive body cue:** More recent works aim to overcome some of these limitations.
- **p. 9 / VI. RELATED Works - extractive body cue:** While model-free approaches [65, 69, 54] exist, they fall outside the scope of this work.
- **p. 5 / A. Multi-embodied Dataset - extractive body cue:** V) demonstrate robust performance and eliminate the need for costly real-world data collection,
- **p. 5 / A. Multi-embodied Dataset - extractive body cue:** Our synthesized dataset exemplifies this principle and supports our robust real-world performance.

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 (i) Domain generalization: Compared to visual-only baselines, visuo-tactile approaches struggle to generalize, hindered by insufficient data diversity and model scalability.를 문제로 두고, First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (III. MeTHODOLOGY), p. 3 (III. MeTHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** To address these challenges, we propose V-HOP (Fig. (p. 1, 1. INTRODUCTION).
- **Actual contribution:** First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning. (p. 1, 1. INTRODUCTION).
- **Evaluation boundary:** Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance of integrating visual and haptic information ... (p. 7, experiment).
- **Explicit failure boundary:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp. (p. 7, B. Bimanual Handover Experiment).
