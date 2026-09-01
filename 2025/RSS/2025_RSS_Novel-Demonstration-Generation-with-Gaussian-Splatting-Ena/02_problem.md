# Problem - Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p146.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p146.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. INrRopucTION), p. 3 (C. Gaussian planting in Roboties), p. 2 (B. Data Augmentation for Policy Learning), p. 1 (Abstract), p. 2 (1. INrRopucTION)): However, the Sim-to-Real gap presents

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Visuomotor policies learned from teleoperated, demonstrations face challenges such as lengthy data collection, high costs, and ting approaches address these issues by augmenting image observations ...
- **p. 1 / Abstract - extractive body cue:** However, the former is constrained to 2D data augmentation, while the latler suffers from imprecise physical
- **p. 1 / Abstract - extractive body cue:** Scene, and augment data across six types of generalization with, five techniques: 3D Gaussian replacement for varying object types, scene appearance, and robot embodiments; equivariant ...
- **p. 1 / Abstract - extractive body cue:** fe real-world experiments demonstrate that ces the generalization of visuomo
- **p. 1 / Abstract - extractive body cue:** tor policies under diverse disturbances.
- **p. 1 / 1. INrRopucTION - extractive body cue:** However, the Sim-to-Real gap presents
- **p. 3 / C. Gaussian planting in Roboties - extractive body cue:** However, importing reconstructed real-world objects to simulation is a strenuous process, and physical interactions tend to suffer from large sim-to-real gaps due to the flawed ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, the Sim-to-Real gap presents | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | The images. camera poses, and depth prior serve as inputs to 3DGS [25], which returns 3D. ‘Gaussians representing the entire scene Gucene, ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | images, camera, poses, depth, prior, serve, inputs, DGS, returns, Gaussians | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | policy, trained, Behavioural, Cloning, end-to-end, manner, aiming, maximize | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: images, camera, poses, depth, prior, serve, inputs, DGS, returns, Gaussians | p. 4 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training), p. 6 (C. Policy Training) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: enables, autonomous, editing, reconstructed, scene, generate, diverse, demonstrations | p. 3 (C. Gaussian planting in Roboties), p. 3 (IV. METHODOLOGY), p. 2 (1. INrRopucTION) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: camera, extrinsies, optimized, through, gradient, descent, optimization, objective | p. 5 (A. Reconstruction and Preprocessing), p. 2 (A. Generalizable Policy in Robot Manipulation), p. 4 (A. Reconstruction and Preprocessing), p. 4 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (A. Reconstruction and Preprocessing), p. 2 (A. Generalizable Policy in Robot Manipulation), p. 4 (A. Reconstruction and Preprocessing) |
| Success / guarantee | closed-loop task success and robustness | p. 7 (A. Experimental Setup), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / C. Gaussian planting in Roboties - extractive body cue:** However, importing reconstructed real-world objects to simulation is a strenuous process, and physical interactions tend to suffer from large sim-to-real gaps due to the flawed ...
- **p. 2 / B. Data Augmentation for Policy Learning - extractive body cue:** Nonetheless, these studies mainly augment task demonstrations on 2D images, which lack spatial information, Hence, only limited augmentation can be achieved, and the ‘augmented demonstrations ...
- **p. 1 / Abstract - extractive body cue:** Visuomotor policies learned from teleoperated, demonstrations face challenges such as lengthy data collection, high costs, and ting approaches address these issues by augmenting image observations ...
- **p. 2 / 1. INrRopucTION - extractive body cue:** significant challenges that hinder policy performance in realworld scenarios.

## What the Paper Changes

PDF contribution framing (p. 3 (C. Gaussian planting in Roboties), p. 3 (IV. METHODOLOGY), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION), p. 1 (Front matter)): Our method enables autonomous editing of the reconstructed scene to generate diverse demonstrations with various configurations.

- **p. 3 / IV. METHODOLOGY - extractive body cue:** To generate high-fidelity and diverse data from a single expert trajectory, we present RoboSplat, a novel demonstration generation approach based on 3DGS.
- **p. 2 / 1. INrRopucTION - extractive body cue:** Thanks t0 its explicit representation of the scene, 3DGS enables interpretable editing ofthe reconstructed scene, which paves the way for generating novel manipulation configurations, Furthermore, ...
- **p. 2 / 1. INrRopucTION - extractive body cue:** Based on that, we propose RoboSplat, a novel and efficacious approach to demonstration generation with Gaussian ‘Splatting.
- **p. 1 / Front matter - extractive body cue:** Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | The drawer is placed in a Sem%Sem workspace, with a fixed orientation, The target object is located in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Fig. 1: Starting from a single expert demonstration and multi-view images, our method generates diverse and visu realistic ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Robustness when Facing Various Deployment Settings | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In particular, our policy achieves 100% success rate on the Pick Object task, showcasing strong robustness against various ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training), p. 6 (C. Policy Training), p. 2 (B. Data Augmentation for Policy Learning). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. INrRopucTION), p. 3 (C. Gaussian planting in Roboties), p. 2 (B. Data Augmentation for Policy Learning), p. 1 (Abstract), p. 2 (1. INrRopucTION), interface p. 4 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training), p. 6 (C. Policy Training), p. 2 (B. Data Augmentation for Policy Learning), objective p. 5 (A. Reconstruction and Preprocessing), p. 2 (A. Generalizable Policy in Robot Manipulation), p. 4 (A. Reconstruction and Preprocessing), p. 4 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
