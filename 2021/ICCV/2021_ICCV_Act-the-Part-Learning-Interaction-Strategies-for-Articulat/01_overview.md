# Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2105.01047.
> PDF retrieval source: https://arxiv.org/pdf/2105.01047. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, 3D Vision, active perception, articulated objects, part discovery
- Official paper: https://arxiv.org/abs/2105.01047
- Full-text retrieval: https://arxiv.org/pdf/2105.01047
- Code/Project: https://act-the-part.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Passive part segmentation algorithms require detailed annotation and cannot generalize to new categories.를 문제로 두고, To address these challenges, we introduce Act the Part 를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** People often use physical intuition when manipulating articulated objects, irrespective of object semantics.
- **p. 1 / Abstract - extractive body cue:** Motivated by this observation, we identify an important embodied task where an agent must play with objects to recover their parts.
- **p. 1 / Abstract - extractive body cue:** To this end, we introduce Act the Part (AtP) to learn how to interact with articulated objects to discover and segment their pieces.
- **p. 1 / Abstract - extractive body cue:** By coupling action selection and motion segmentation, AtP is able to isolate structures to make perceptual part recovery possible without semantic labels.
- **p. 1 / Abstract - extractive body cue:** Our experiments show AtP learns efficient strategies for part discovery, can generalize to unseen categories, and is capable of conditional reasoning for the task.
- **p. 1 / 1. Introduction - extractive body cue:** Passive part segmentation algorithms require detailed annotation and cannot generalize to new categories.
- **p. 1 / 1. Introduction - extractive body cue:** While motion can help discover new objects, prior work cannot infer actions for understanding individual parts.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce Act the Part.
- **p. 2 / 1. Introduction - extractive body cue:** (2) Our method generalizes to unseen object instances and categories with different numbers of parts and joints.
- **p. 4 / 3.4. History Aggregation - extractive body cue:** We introduce a history aggregation algorithm to updated part memory V , based on predicted Mt and Mt+1.
- **p. 2 / 3. Approach - extractive body cue:** We then explain the three components of our approach: an interaction network (Sec.
- **p. 1 / 1. Introduction - extractive body cue:** Our task and approach novelty are highlighted in Fig.
- **p. 4 / 3.2. Learning to Act to Discover Parts - extractive body cue:** Mask 𝑀!"# Part Network Mask Decoder Mask Decoder ResNet18 Image Observation Action Applied Figure 4.
- **p. 4 / 3.5. Reward - extractive body cue:** At inference, we first predict and execute an action.
- **p. 3 / 3.2. Learning to Act to Discover Parts - extractive body cue:** 3, we use a shared ResNet18 [16] with two residual decoder heads wired with U-Net [39] skip connections.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given the sequence of T observations, sensor readings, and actions, the goal is to infer part mask MT ∈{1, 2, ..., N +1}H×W , where each pixel is assigned a value corresponding ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |
| State/latent | Given, sequence, observations, sensor, readings, actions, goal, infer, part, mask, where, pixel | geometry, map, object/relationship state | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Learning to Act to Discover Parts) |
| Output/action | (a) The interaction network computes hold and push from an image observation and current part memory. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Problem Formulation), p. 4 (3.2. Learning to Act to Discover Parts), p. 2 (3.1. Problem Formulation) |
| Objective/outcome | We use pixel-wise binary cross entropy loss to supervise the hold and push reward maps. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Learning to Act to Discover Parts), p. 3 (3.1. Problem Formulation), p. 4 (3.3. Learning to Discover Parts from Action) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce Act the Part.
- **p. 2 / 1. Introduction - extractive body cue:** (2) Our method generalizes to unseen object instances and categories with different numbers of parts and joints.
- **p. 4 / 3.4. History Aggregation - extractive body cue:** We introduce a history aggregation algorithm to updated part memory V , based on predicted Mt and Mt+1.
- **p. 2 / 3. Approach - extractive body cue:** We then explain the three components of our approach: an interaction network (Sec.
- **p. 1 / 1. Introduction - extractive body cue:** Our task and approach novelty are highlighted in Fig.
- **p. 5 / 4.2. Benchmark Results - extractive body cue:** While other algorithms' performance saturate quickly with one or two interactions, [Ours-Touch] and [Ours-NoTouch] are able to improve with more interactions.
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** Furthermore, this result suggests more complex perceptual modules are necessary to get push-only policies to achieve competitive performance at this task.
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** 2, we see that [Ours-Touch] outperforms [Ours-NoTouch] in most categories.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results) |
| Embodiment/environment | Dataset, test initialization, and pre-trained models will be released for reproducibility and benchmarking. | hardware/simulator version and reset protocol | p. 5 (4. Evaluation), p. 8 (4.3. Real World Results) |
| Dataset/benchmark | Our network learns a policy to interact with unseen objects and categories. | role, split, size and leakage | p. 5 (4. Evaluation), p. 8 (4.3. Real World Results), p. 6 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results) |
| Metric | The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). | definition, denominator, direction and uncertainty | p. 5 (4.1. Metrics and Points of Comparison), p. 7 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results) |
| Baseline/ablation | Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time. | fair input/data/compute/action matching | p. 7 (4.2. Benchmark Results), p. 5 (4.1. Metrics and Points of Comparison), p. 6 (4.2. Benchmark Results) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.1. Metrics and Points of Comparison - extractive body cue:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%).
- **p. 8 / 4.3. Real World Results - extractive body cue:** G for more real world experiment results and failure case analysis.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 13. Failure Modes. (a) On three link objects our model sometimes struggles to split parts that have been grouped together in the part memory. ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Interaction for Part Discovery. Passive part segmenta- tion algorithms require detailed annotation and cannot generalize to new categories. While motion can help discover ...
- **p. 8 / 5. Conclusion and Future Work - extractive body cue:** We see broad scope for future work including extensions to 3D part segmentation and singular frameworks for rigid, articulated, and deformable object understanding.
- **p. 6 / 4.2. Benchmark Results - extractive body cue:** Due to space limitation, only three interaction steps are shown in this figure.
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** Furthermore, for eyeglasses, MAPE value falls under 0.33, suggesting the model finds the three parts in most cases.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Passive part segmentation algorithms require detailed annotation and cannot generalize to new categories.를 문제로 두고, To address these challenges, we introduce Act the Part 를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Learning to Act to Discover Parts) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Passive part segmentation algorithms require detailed annotation and cannot generalize to new categories. (p. 1, 1. Introduction).
- **Actual contribution:** Our task and approach novelty are highlighted in Fig. (p. 1, 1. Introduction).
- **Evaluation boundary:** Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time. (p. 7, 4.2. Benchmark Results).
- **Explicit failure boundary:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). (p. 5, 4.1. Metrics and Points of Comparison).
