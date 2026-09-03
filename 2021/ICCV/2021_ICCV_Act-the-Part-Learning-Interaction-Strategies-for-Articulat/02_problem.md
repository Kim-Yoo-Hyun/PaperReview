# Problem - Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2105.01047; PDF retrieval source: https://arxiv.org/pdf/2105.01047. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 2 (1. Introduction), p. 2 (1. Introduction)): Passive part segmentation algorithms require detailed annotation and cannot generalize to new categories.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** People often use physical intuition when manipulating articulated objects, irrespective of object semantics.
- **p. 1 / Abstract - extractive body cue:** Motivated by this observation, we identify an important embodied task where an agent must play with objects to recover their parts.
- **p. 1 / Abstract - extractive body cue:** To this end, we introduce Act the Part (AtP) to learn how to interact with articulated objects to discover and segment their pieces.
- **p. 1 / Abstract - extractive body cue:** By coupling action selection and motion segmentation, AtP is able to isolate structures to make perceptual part recovery possible without semantic labels.
- **p. 1 / Abstract - extractive body cue:** Our experiments show AtP learns efficient strategies for part discovery, can generalize to unseen categories, and is capable of conditional reasoning for the task.
- **p. 1 / 1. Introduction - extractive body cue:** Passive part segmentation algorithms require detailed annotation and cannot generalize to new categories.
- **p. 1 / 1. Introduction - extractive body cue:** While motion can help discover new objects, prior work cannot infer actions for understanding individual parts.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Passive part segmentation algorithms require detailed annotation and cannot generalize to new categories. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Given the sequence of T observations, sensor readings, and actions, the goal is to infer part mask MT ∈{1, 2, ..., N ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, sequence, observations, sensor, readings, actions, goal, infer, part, mask | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Mask, Part, Network, Decoder, ResNet18, Image, Observation, Action | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Given, sequence, observations, sensor, readings, actions, goal, infer, part, mask | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Learning to Act to Discover Parts) |
| Decision / output variable | geometry/map/query r; body terms: address, challenges, introduce, Act, Part, arXiv, generalizes, unseen | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. History Aggregation) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: pixel-wise, binary, cross, entropy, loss, supervise, hold, push | p. 3 (3.1. Problem Formulation), p. 4 (3.3. Learning to Discover Parts from Action), p. 4 (3.2. Learning to Act to Discover Parts), p. 3 (3.1. Problem Formulation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.3. Learning to Discover Parts from Action), p. 2 (3. Approach), p. 3 (3.2. Learning to Act to Discover Parts) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4.1. Metrics and Points of Comparison), p. 7 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** While motion can help discover new objects, prior work cannot infer actions for understanding individual parts.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** However, we also show our model generalizes to real-world images without finetuning.
- **p. 2 / 1. Introduction - extractive body cue:** (2) Our method generalizes to unseen object instances and categories with different numbers of parts and joints.
- **p. 2 / 1. Introduction - extractive body cue:** By reasoning about changes in visual observations, our perception algorithm is able to discover new parts, keep track of existing ones, and update the part ...

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. History Aggregation), p. 2 (3. Approach), p. 1 (1. Introduction)): To address these challenges, we introduce Act the Part.

- **p. 2 / 1. Introduction - extractive body cue:** (2) Our method generalizes to unseen object instances and categories with different numbers of parts and joints.
- **p. 4 / 3.4. History Aggregation - extractive body cue:** We introduce a history aggregation algorithm to updated part memory V , based on predicted Mt and Mt+1.
- **p. 2 / 3. Approach - extractive body cue:** We then explain the three components of our approach: an interaction network (Sec.
- **p. 1 / 1. Introduction - extractive body cue:** Our task and approach novelty are highlighted in Fig.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | G for more real world experiment results and failure case analysis. | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Figure 13. Failure Modes. (a) On three link objects our model sometimes struggles to split parts that have ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. Interaction for Part Discovery. Passive part segmenta- tion algorithms require detailed annotation and cannot generalize to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Learning to Act to Discover Parts), p. 2 (3.1. Problem Formulation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Learning to Act to Discover Parts), p. 2 (3.1. Problem Formulation), objective p. 3 (3.1. Problem Formulation), p. 4 (3.3. Learning to Discover Parts from Action), p. 4 (3.2. Learning to Act to Discover Parts), p. 3 (3.1. Problem Formulation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Passive part segmentation algorithms require detailed annotation and cannot generalize to new categories. (p. 1, 1. Introduction).
- **Formulation-changing contribution:** Our task and approach novelty are highlighted in Fig. (p. 1, 1. Introduction).
- **Assumption/failure evidence:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). (p. 5, 4.1. Metrics and Points of Comparison).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
