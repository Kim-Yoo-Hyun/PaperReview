# OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2509.26633.
> PDF retrieval source: https://arxiv.org/pdf/2509.26633. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, loco-manipulation, motion retargeting
- Official paper: https://arxiv.org/abs/2509.26633
- Full-text retrieval: https://arxiv.org/pdf/2509.26633
- Code/Project: https://omniretarget.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.를 문제로 두고, To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies.
- **p. 1 / Abstract - extractive body cue:** However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration.
- **p. 1 / Abstract - extractive body cue:** More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation.
- **p. 1 / Abstract - extractive body cue:** To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and ...
- **p. 1 / Abstract - extractive body cue:** By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OMNIRETARGET generates kinematically feasible trajectories.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This embodiment gap means that simply adapting human motions is in ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and ...
- **p. 1 / Abstract - extractive body cue:** Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Thanks to the high-quality interaction-preserving motion retargeting, these policies are trained and deployed in a minimal and unified way: it involves only 5 rewards, 4 robot domain randomization terms, and a purely ... | proprioception, reference pose/motion, visual or language command | p. 1 (Body text (section not recovered)), p. 1 (I. INTRODUCTION) |
| State/latent | Thanks, high-quality, interaction-preserving, motion, retargeting, policies, trained, deployed, minimal, unified, involves, only | whole-body pose, balance/contact state와 skill/mode | p. 1 (Body text (section not recovered)), p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Output/action | To address these challenges, imitating human motions offers a powerful alternative for learning whole-body control, especially for complex scene interactions. | joint/whole-body action, motion target 또는 task trajectory | p. 1 (I. INTRODUCTION) |
| Objective/outcome | By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OMNIRETARGET generates kinematically feasible trajectories. | tracking, balance, skill/task success와 recovery | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and ...
- **p. 1 / Abstract - extractive body cue:** Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward engineering ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: OMNIRETARGET overview. Human demonstrations are retargeted to the robot via interaction-mesh-based constrained optimization. Each spatial and shape augmentation is solved as a new ...
- **p. 1 / Abstract - extractive body cue:** We comprehensively evaluate OMNIRETARGET by retargeting motions from OMOMO [1], LAFAN1 [2], and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While deep reinforcement learning (RL) has shown remarkable success in robot control, efficient exploration is highly sensitive to reward engineering [3].
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Additional hardware results showing diverse, agile and human-like behaviors. • Observation noise: ±0.05 for orientation in Rot6D, ±0.5 m/s and ±0.2 rad/s for ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 12 (Figure/Table caption) |
| Embodiment/environment | The quest to enable humanoid robots to perform complex whole-body scene- and object-interaction tasks has long been constrained by a fundamental data bottleneck. | hardware/simulator version and reset protocol | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Dataset/benchmark | The quest to enable humanoid robots to perform complex whole-body scene- and object-interaction tasks has long been constrained by a fundamental data bottleneck. | role, split, size and leakage | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Metric | Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor inter- action preservation. This task therefore measures ... | definition, denominator, direction and uncertainty | p. 12 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (I. INTRODUCTION) |
| Baseline/ablation | Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward engineering could help, but it contradicts our minimal ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 1 (Abstract), p. 12 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Cross-embodiment robot-object-terrain interaction. Drake [52], which correctly handles the differential geometry of rotations on the S3 manifold [53]. Our interaction-mesh-based kinematic pipeline is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Additional hardware results showing diverse, agile and human-like behaviors. • Observation noise: ±0.05 for orientation in Rot6D, ±0.5 m/s and ±0.2 rad/s for ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.를 문제로 두고, To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 7 (Figure/Table caption), p. 12 (Figure/Table caption), p. 3 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
