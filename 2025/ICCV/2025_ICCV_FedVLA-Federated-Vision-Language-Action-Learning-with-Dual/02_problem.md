# Problem - FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): However, existing methods typically select a fixed number of experts, lacking adaptability to tasks of varying complexity.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-language-action (VLA) models have significantly advanced robotic manipulation by enabling robots to interpret language instructions for task execution.
- **p. 1 / Abstract - extractive PDF cue:** However, training these models often relies on large-scale user-specific data, raising concerns about privacy and security, which in turn limits their broader adoption.
- **p. 1 / Abstract - extractive PDF cue:** To address this, we propose FedVLA, the first federated VLA learning framework, enabling distributed model training that preserves data privacy without compromising performance.
- **p. 1 / Abstract - extractive PDF cue:** Our framework integrates task-aware representation learning, adaptive expert selection, and expert-driven federated aggregation, enabling efficient and privacy-preserving training of VLA models.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we introduce an InstructionOriented Scene-Parsing mechanism, which decomposes and enhances object-level features based on task instructions, improving contextual understanding.
- **p. 2 / 1. Introduction - extractive PDF cue:** However, existing methods typically select a fixed number of experts, lacking adaptability to tasks of varying complexity.
- **p. 2 / 1. Introduction - extractive PDF cue:** These limitations highlight the need for a task-adaptive and flexible FL framework, specifically designed for multi-modal robotic learning.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, existing methods typically select a fixed number of experts, lacking adaptability to tasks of varying complexity. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | In contrast, VLA models operate in multi-modal environments, requiring the joint processing of visual observations, language instructions, and robotic actions, which significantly ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | contrast, VLA, models, operate, multi-modal, environments, requiring, joint, processing, visual | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | federated, VLA, framework, enables, decentralized, training, user, devices | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: contrast, VLA, models, operate, multi-modal, environments, requiring, joint, processing, visual | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: Extensive, experiments, simulation, real-world, environments, demonstrate, FedVLA, achieves | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: server, side, receives, expert, selection, statistics, trunk, updates | p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4.3. Ablation Studies), p. 7 (4.2. Real-World), p. 6 (4.1. Simulation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** These limitations highlight the need for a task-adaptive and flexible FL framework, specifically designed for multi-modal robotic learning.
- **p. 1 / 1. Introduction - extractive PDF cue:** Our federated VLA framework enables decentralized training on user devices, preserving privacy while utilizing expertdriven aggregation to enhance model generalization across diverse tasks. enabling robots ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce the Dual Gating Mixture-of-Experts, where ...

- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions in this work can be summarized as follows: • We propose FedVLA, the first privacy-preserving federated learning framework for VLA training, ensuring ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Unlike traditional centralized training, which requires aggregating all user data on a central server, FL enables distributed model training across multiple clients without transferring raw ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Our federated VLA framework enables decentralized training on user devices, preserving privacy while utilizing expertdriven aggregation to enhance model generalization across diverse tasks. enabling robots ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | For evaluation, the success and failure of a trial are recoreded as 1 and 0. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | For collision detection and dynamics simulation, we employ official physics engines to ensure accurate robotic interactions within the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The integration of these modules together results in a architecture that supports FedVLA's robustness and adaptability across diverse ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), objective p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
