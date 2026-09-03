# FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, existing methods typically select a fixed number of experts, lacking adaptability to tasks of varying complexity.를 문제로 두고, Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce the Dual Gating Mixture-of-Experts, where ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-language-action (VLA) models have significantly advanced robotic manipulation by enabling robots to interpret language instructions for task execution.
- **p. 1 / Abstract - extractive body cue:** However, training these models often relies on large-scale user-specific data, raising concerns about privacy and security, which in turn limits their broader adoption.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose FedVLA, the first federated VLA learning framework, enabling distributed model training that preserves data privacy without compromising performance.
- **p. 1 / Abstract - extractive body cue:** Our framework integrates task-aware representation learning, adaptive expert selection, and expert-driven federated aggregation, enabling efficient and privacy-preserving training of VLA models.
- **p. 1 / Abstract - extractive body cue:** Specifically, we introduce an InstructionOriented Scene-Parsing mechanism, which decomposes and enhances object-level features based on task instructions, improving contextual understanding.
- **p. 2 / 1. Introduction - extractive body cue:** However, existing methods typically select a fixed number of experts, lacking adaptability to tasks of varying complexity.
- **p. 2 / 1. Introduction - extractive body cue:** These limitations highlight the need for a task-adaptive and flexible FL framework, specifically designed for multi-modal robotic learning.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce the ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions in this work can be summarized as follows: • We propose FedVLA, the first privacy-preserving federated learning framework for VLA training, ensuring ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike traditional centralized training, which requires aggregating all user data on a central server, FL enables distributed model training across multiple clients without transferring raw ...
- **p. 1 / 1. Introduction - extractive body cue:** Our federated VLA framework enables decentralized training on user devices, preserving privacy while utilizing expertdriven aggregation to enhance model generalization across diverse tasks. enabling robots ...
- **p. 5 / 3.4. Algorithms - extractive body cue:** The aggregated global trunk module is then redistributed to clients for the next training round.
- **p. 5 / 3.4. Algorithms - extractive body cue:** At the start of each training round t, each client processes task-specific data using Instruction-Oriented Scene-Parsing to extract structured features, followed by Dual Gating MoE ...
- **p. 6 / 3.4. Algorithms - extractive body cue:** Algorithm 2 FedVLA: Server Input: T is the number of training rounds. θ represents the global trunk parameters.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In contrast, VLA models operate in multi-modal environments, requiring the joint processing of visual observations, language instructions, and robotic actions, which significantly increases the complexity of federated training. | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | contrast, VLA, models, operate, multi-modal, environments, requiring, joint, processing, visual, observations, language | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/action | IOSP decomposes observation images into object-level representations guided by task instructions and leverages vision-language alignment techniques to improve contextual understanding. | continuous action, pose 또는 action chunk | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | On the server side, the server receives expert selection statistics and trunk updates from all participating clients and performs Expert-Driven Aggregation, which dynamically assigns aggregation weights based on expert selection similar ... | instruction following, task success, generalization과 latency | p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce the ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions in this work can be summarized as follows: • We propose FedVLA, the first privacy-preserving federated learning framework for VLA training, ensuring ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike traditional centralized training, which requires aggregating all user data on a central server, FL enables distributed model training across multiple clients without transferring raw ...
- **p. 1 / 1. Introduction - extractive body cue:** Our federated VLA framework enables decentralized training on user devices, preserving privacy while utilizing expertdriven aggregation to enhance model generalization across diverse tasks. enabling robots ...
- **p. 6 / 4.1. Simulation - extractive body cue:** Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Simulation evaluation across four tasks. Performance Comparison. The evaluation results in the simulation environment are presented in Table 1. Fed- VLA achieves an ...
- **p. 7 / 4.2. Real-World - extractive body cue:** In contrast, FedAvg exhibits a significant performance drop across all tasks, with an average success rate of 53.3%, which is 10.0% lower than our method.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** We compare the task success rate and record the validation loss during the training process.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.1. Simulation), p. 6 (Figure/Table caption) |
| Embodiment/environment | We collect real-world robotic demonstrations for household-related tasks, including Clean Up, Trash Collection, Open Drawer, and Sorting Pills, as shown in Figure 4. | hardware/simulator version and reset protocol | p. 6 (4.2. Real-World), p. 6 (4.1. Simulation) |
| Dataset/benchmark | These findings strongly support that IOSP helps decompose complex visual scenes into task-relevant object representations, DGMoE module routes the adaptive knowledge, EDA ensures the integrity and effectiveness of the aggregation. | role, split, size and leakage | p. 6 (4.2. Real-World), p. 6 (4.1. Simulation), p. 7 (4.3. Ablation Studies), p. 7 (4.2. Real-World) |
| Metric | We compare the task success rate and record the validation loss during the training process. | definition, denominator, direction and uncertainty | p. 7 (4.3. Ablation Studies), p. 7 (4.2. Real-World), p. 6 (4.1. Simulation) |
| Baseline/ablation | Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%. | fair input/data/compute/action matching | p. 6 (4.1. Simulation), p. 6 (4. Experiments), p. 8 (4.4. Analysis on DGMoE) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4. Experiments - extractive body cue:** For evaluation, the success and failure of a trial are recoreded as 1 and 0.
- **p. 6 / 4.1. Simulation - extractive body cue:** For collision detection and dynamics simulation, we employ official physics engines to ensure accurate robotic interactions within the simulation environment.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** The integration of these modules together results in a architecture that supports FedVLA's robustness and adaptability across diverse tasks.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, existing methods typically select a fixed number of experts, lacking adaptability to tasks of varying complexity.를 문제로 두고, Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce the Dual Gating Mixture-of-Experts, where ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
