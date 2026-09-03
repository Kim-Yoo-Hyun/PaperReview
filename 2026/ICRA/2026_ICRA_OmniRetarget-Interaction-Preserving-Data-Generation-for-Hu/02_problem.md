# Problem - OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2509.26633; PDF retrieval source: https://arxiv.org/pdf/2509.26633. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies.
- **p. 1 / Abstract - extractive body cue:** However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration.
- **p. 1 / Abstract - extractive body cue:** More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation.
- **p. 1 / Abstract - extractive body cue:** To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and ...
- **p. 1 / Abstract - extractive body cue:** By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OMNIRETARGET generates kinematically feasible trajectories.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This embodiment gap means that simply adapting human motions is in ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Thanks to the high-quality interaction-preserving motion retargeting, these policies are trained and deployed in a minimal and unified way: it involves only ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Thanks, high-quality, interaction-preserving, motion, retargeting, policies, trained, deployed, minimal, unified | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | address, introduce, OMNIRETARGET, interactionpreserving, data, generation, engine, interaction | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Thanks, high-quality, interaction-preserving, motion, retargeting, policies, trained, deployed, minimal, unified | p. 1 (Body text (section not recovered)), p. 1 (I. INTRODUCTION) |
| Decision / output variable | joint/whole-body action; body terms: address, introduce, OMNIRETARGET, interactionpreserving, data, generation, engine, interaction | p. 1 (Abstract), p. 1 (Abstract) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: minimizing, Laplacian, deformation, between, human, robot, meshes, while | p. 1 (Abstract), p. 1 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Success / guarantee | motion/task success and recovery | p. 12 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (I. INTRODUCTION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** This embodiment gap means that simply adapting human motions is in ...

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 1 (Abstract)): To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, ...

- **p. 1 / Abstract - extractive body cue:** Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Fig. 3: Cross-embodiment robot-object-terrain interaction. Drake [52], which correctly handles the differential geometry of rotations on the S3 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Fig. 5: Additional hardware results showing diverse, agile and human-like behaviors. • Observation noise: ±0.05 for orientation in ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Body text (section not recovered)), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (Body text (section not recovered)), p. 1 (I. INTRODUCTION), objective p. 1 (Abstract), p. 1 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
