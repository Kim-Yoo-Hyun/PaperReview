# Problem - PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p056.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p056.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (IV. PROBLEM STATEMENT), p. 4 (IV. PROBLEM STATEMENT), p. 5 (IV. PROBLEM STATEMENT), p. 5 (IV. PROBLEM STATEMENT)): Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Robots are inereasingly envisioned as human com- 1.
- **p. 1 / Abstract - extractive body cue:** Ivrropucrion anions, assisting with everyday tasks that offen involve manip
- **p. 1 / Abstract - extractive body cue:** Despite recent advances in robotic Robots are increasingly popular as assistive agents in evhardware and embodied Al, existing systems continue to struggle eryday life, particularly ...
- **p. 1 / Abstract - extractive body cue:** and fabric. ‘These' limitations stem from the lack of robust perception techniques for reliable state estimation under diverse often involving the grasp of thin, deformable ...
- **p. 1 / Abstract - extractive body cue:** fal conditions and the absence of planning methods capa- paper and fabric [51].
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces.
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** Although creases or irregularities in the ‘material can sometimes provide grasping points, a particularly challenging scenario arises when the object is extremely flat and lacks ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces. | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | 2) Diffusion Policy Training: Train a policy fon this dataset t0 infer motions from tactile feedback and proprioceptive states, ensuring generalization to ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF |
| State / latent | Diffusion, Policy, Training, Train, dataset, infer, motions, tactile, feedback, proprioceptive | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | Motion, Noise, ATR, Port, Puvit, dioe, PP-Tac, Policy | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: Diffusion, Policy, Training, Train, dataset, infer, motions, tactile, feedback, proprioceptive | p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 9 (B. Depth Reconstruction of VBTS), p. 7 (A. Implementation Details) |
| Decision / output variable | contact-aware action/force; body terms: address, visionindependent, tactile-based, core, idea, leverages, tactile, feedback | p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 6 (A. Implementation Details), p. 5 (IV. PROBLEM STATEMENT) |
| Objective / loss / cost | contact prediction/control error; cue terms: reconstruction, loss, median, losses, below, implement, through, PPTac | p. 7 (B. Depth Reconstruction of VBTS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 8 (B. Depth Reconstruction of VBTS), p. 8 (B. Depth Reconstruction of VBTS) |
| Success / guarantee | slip/contact success and safe interaction | p. 9 (Figure/Table caption), p. 5 (A. Grasp Motion Dataset Synthesis), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** Although creases or irregularities in the ‘material can sometimes provide grasping points, a particularly challenging scenario arises when the object is extremely flat and lacks ...
- **p. 5 / IV. PROBLEM STATEMENT - extractive body cue:** One challenge is determining the control inputs for all finger joints and the hand pose (i.e. the end-effector pose of the manipulator).
- **p. 5 / IV. PROBLEM STATEMENT - extractive body cue:** In practice, our approach solved this problem by adopting a Iearing-based policy rather than a model-based optimization paradigm.

## What the Paper Changes

PDF contribution framing (p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 6 (A. Implementation Details), p. 5 (IV. PROBLEM STATEMENT), p. 8 (B. Depth Reconstruction of VBTS), p. 4 (IV. PROBLEM STATEMENT)): To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), facilitating the creation of a buckling ...

- **p. 6 / A. Implementation Details - extractive body cue:** Thus, the entire inference process consists of 10 steps.
- **p. 5 / IV. PROBLEM STATEMENT - extractive body cue:** In practice, our approach solved this problem by adopting a Iearing-based policy rather than a model-based optimization paradigm.
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** These evaluations showcase the robustness and adaptability of our approach,
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** This research introduces a novel approach to tackle the paper picking problem that was previously unexplored.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We also compare our system with various manipulators to highlight its advantages and limitations (Section VI-D). | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Fig. 6: Inference pipeline of the proposed PP-Tae policy. Conditioned on robot proprioception and the target force that ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 9 (B. Depth Reconstruction of VBTS), p. 7 (A. Implementation Details), p. 6 (B. PP-Tac Policy). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (IV. PROBLEM STATEMENT), p. 4 (IV. PROBLEM STATEMENT), p. 5 (IV. PROBLEM STATEMENT), p. 5 (IV. PROBLEM STATEMENT), interface p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 9 (B. Depth Reconstruction of VBTS), p. 7 (A. Implementation Details), p. 6 (B. PP-Tac Policy), objective p. 7 (B. Depth Reconstruction of VBTS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
