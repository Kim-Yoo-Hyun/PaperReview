# GOAT: GO to Any Thing

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p073.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p073.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, Navigation, semantic memory, lifelong learning, mobile manipulation, open-world
- Official paper: https://www.roboticsproceedings.org/rss20/p073.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p073.html
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 In deployment scenarios such as homes and warehouses, mobile robots are expected to autonomously navigate for extended periods, seamlessly executing tasks articulated in terms that are intuitively understandable by human operators.를 문제로 두고, This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and fine-grained language descriptions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In deployment scenarios such as homes and warehouses, mobile robots are expected to autonomously navigate for extended periods, seamlessly executing tasks articulated in terms that ...
- **p. 1 / Abstract - extractive body cue:** We present GO To Any Thing (GOAT), a universal navigation system capable of tackling these requirements with three key features: a) Multimodal: it can tackle ...
- **p. 1 / Abstract - extractive body cue:** GOAT is made possible through a modular system design and a continually augmented instanceaware semantic memory that keeps track of the appearance of objects from ...
- **p. 1 / Abstract - extractive body cue:** This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and language descriptions.
- **p. 1 / Abstract - extractive body cue:** In experimental comparisons spanning over 90 hours in 9 different homes consisting of 675 goals selected across 200+ different object instances, we find GOAT achieves ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and fine-grained language descriptions.
- **p. 4 / IV. GOAT METHOD - extractive body cue:** For language goals, we first extract an object category from the language description (by prompting with Mistral 7B [30] in our experiments), then match CLIP ...
- **p. 4 / IV. GOAT METHOD - extractive body cue:** Similarly, for image goals, we first extract an object category from the image with MaskRCNN, then match keypoints of the goal image with keypoints of ...
- **p. 3 / IV. GOAT METHOD - extractive body cue:** If no instance is localized, the global policy outputs an exploration goal.
- **p. 3 / IV. GOAT METHOD - extractive body cue:** In this semantic map representation, the first C channels store the unique instance ids of the projected objects.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes as input the current depth image Dt, RGB image It, and pose reading xt from onboard sensors. | egocentric RGB-D, language/task goal, base-arm proprioception | p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD) |
| State/latent | takes, input, current, depth, image, RGB, pose, reading, onboard, sensors, instance, localized | map/object/contact state와 base-arm coordination decision | p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD) |
| Output/action | If no instance is localized, the global policy outputs an exploration goal. | base motion plus arm/gripper action | p. 3 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD) |
| Objective/outcome | We take a simple approach: when new observations are received from the sensors, we overwrite the relevant cells in the semantic map based on the updated occupancy information. | long-horizon task success, reachability, collision과 recovery | p. 4 (IV. GOAT METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and fine-grained language descriptions.
- **p. 5 / V. RESULTS - extractive body cue:** GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT.
- **p. 5 / V. RESULTS - extractive body cue:** GOAT achieves 83% average success rate (94% for object categories, 86% for image goals, and 68% for language goals).
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. Navigation performance based on sequential goal count. GOAT performance improves with experience in the environment: from a 60% success rate (0.2 SPL) at ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Perception and memory update. The perception system processes RGB-D input to infill depth, segment object instances, project them into a top-down semantic map, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Embodiment/environment | We evaluate the ability of the GOAT agent to tackle the GOAT task, i.e., reach a sequence of unseen multimodal object instances in unseen environments. | hardware/simulator version and reset protocol | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Dataset/benchmark | We evaluate the ability of the GOAT agent to tackle the GOAT task, i.e., reach a sequence of unseen multimodal object instances in unseen environments. | role, split, size and leakage | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Metric | GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. | definition, denominator, direction and uncertainty | p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 8 (Figure/Table caption) |
| Baseline/ablation | GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. | fair input/data/compute/action matching | p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / VII. DISCUSSION - extractive body cue:** environment is fully explored, failures are almost exclusively due to failures in matching the correct goal.
- **p. 10 / VII. DISCUSSION - extractive body cue:** The most common failure is a language goal being matched against the an object of the correct class, but the wrong instance (i.e.
- **p. 8 / VII. DISCUSSION - extractive body cue:** a) Modularity allows GOAT to Achieve Robust GeneralPurpose Navigation in the Real World: The GOAT system as a whole is a robust navigation platform, achieving ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 In deployment scenarios such as homes and warehouses, mobile robots are expected to autonomously navigate for extended periods, seamlessly executing tasks articulated in terms that are intuitively understandable by human operators.를 문제로 두고, This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and fine-grained language descriptions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD), p. 5 (V. RESULTS), p. 5 (V. RESULTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, for extremely long trajectories a mechanism to increase parallelism or cull duplicate images would be necessary to increase matching speeds. g) Additional Limitations: To achieve robust imagematching results GOAT's ... (p. 10, VII. DISCUSSION).
- **Actual contribution:** This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and fine-grained language descriptions. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. (p. 5, V. RESULTS).
- **Explicit failure boundary:** 68.2). d) Real-World Open-Vocabulary Detection: Limitations and Opportunities: An interesting and noteworthy observation is that despite the rapid advances in open (or large) vocabulary vision-and-language models (VLMs) [37, 43], we ... (p. 10, VII. DISCUSSION).
