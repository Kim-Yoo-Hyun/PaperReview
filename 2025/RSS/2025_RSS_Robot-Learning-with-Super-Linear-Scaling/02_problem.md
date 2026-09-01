# Problem - Robot Learning with Super-Linear Scaling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p025.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p025.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 1 (1. Iyrropucrion)): Continual learning also faces challenges, such as catastrophic forgetting, as discussed in prior work [18].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Scaling robot learning requires data collection pipelines that sale favorably with human effort.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we propose Crowdsourcing and Amorizing Human Effort for Realto~ ‘Sim-to-Real(CASHER), a pipeline for scaling up data collection ‘and learning in simulation where ...
- **p. 1 / Abstract - extractive PDF cue:** The key idea is to crowdsource digital twins of real-world scenes using 3D reconstruction and collect large-scale data in simulation, rather than the real-world.
- **p. 1 / Abstract - extractive PDF cue:** Data ion is intially driven by RL, bootstrapped ms.
- **p. 1 / Abstract - extractive PDF cue:** As the training of a generalist policy progresses across environments, its generalization capabilities ‘can be used to replace human effort with model-generated tions.
- **p. 2 / 1. Iyrropucrion - extractive PDF cue:** Continual learning also faces challenges, such as catastrophic forgetting, as discussed in prior work [18].
- **p. 2 / 1. Iyrropucrion - extractive PDF cue:** Generating procedurally accurate training environ- ‘ments remains an open challenge.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Continual learning also faces challenges, such as catastrophic forgetting, as discussed in prior work [18]. | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | train, MLP, network, size, takes, embedding, point, cloud, observation, dimensions | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | deploying, visuomotor, policy, perceptual, observations, RGB, point, clouds | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: train, MLP, network, size, takes, embedding, point, cloud, observation, dimensions | p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS), p. 4 (4 Sample set of A' digital twins from crowdsourced) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: CASHER, enables, fine-tuning, prestrained, target, scenario, video, sean | p. 1 (Abstract), p. 1 (1. Iyrropucrion), p. 2 (1. Iyrropucrion) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: implement, PPO, loss, algorithm, built, upon, Stable, Baselines | p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Success / guarantee | closed-loop task success and robustness | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Iyrropucrion - extractive PDF cue:** Generating procedurally accurate training environ- ‘ments remains an open challenge.
- **p. 3 / 1. Iyrropucrion - extractive PDF cue:** are available, generating valid robot trajectories that solve the task is another challenge.
- **p. 3 / 1. Iyrropucrion - extractive PDF cue:** However, these policies often fail to generalize to different scenarios, requiring significant human effort for each new environment.
- **p. 1 / 1. Iyrropucrion - extractive PDF cue:** CASHER (1) creates a data flywheel, where data begets more data through model generalization.

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 1 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 12 (IX. IMPLEMENTATION DETAILS)): We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort.

- **p. 1 / 1. Iyrropucrion - extractive PDF cue:** Our contributions include 1) a novel continual data collection system based on real-to-sim-to-real for training generalist policies, 2) a novel scanned deployment fine-tuning technique for ...
- **p. 2 / 1. Iyrropucrion - extractive PDF cue:** Overview of CASHER, we propose « system for taining generalist policies leveraging real-o-sim simulation on crowdsouced scans.
- **p. 3 / 1. Iyrropucrion - extractive PDF cue:** CASHER consists of three elements - 1) fast, accessible digital twin generation with 3-D reconstruction methods, 2) multi-environment model learning that amortizes the data collection ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive PDF cue:** To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local point ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | This reduces the amount of human effort required for data collection as training progresses, Importantly, the generalization across ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | T can be used to obtain a single robust, statecovering optimal multi-environment policy xs3(as/s¢) for all Ex :1,-++»€2x ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | This model-generated data can then be used to train a robust, high-coverage statebased policy 4(a/s+) using demonstration-bootstrapped re | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS), p. 4 (4 Sample set of A' digital twins from crowdsourced), p. 4 (4 Sample set of A' digital twins from crowdsourced). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 1 (1. Iyrropucrion), interface p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS), p. 4 (4 Sample set of A' digital twins from crowdsourced), p. 4 (4 Sample set of A' digital twins from crowdsourced), objective p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
