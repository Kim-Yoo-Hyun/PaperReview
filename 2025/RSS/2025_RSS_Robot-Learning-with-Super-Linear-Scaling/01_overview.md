# Robot Learning with Super-Linear Scaling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p025.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p025.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning, scaling laws, robot data
- Official paper: https://www.roboticsproceedings.org/rss21/p025.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p025.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p025.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 Continual learning also faces challenges, such as catastrophic forgetting, as discussed in prior work [18].를 문제로 두고, We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Scaling robot learning requires data collection pipelines that sale favorably with human effort.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Crowdsourcing and Amorizing Human Effort for Realto~ ‘Sim-to-Real(CASHER), a pipeline for scaling up data collection ‘and learning in simulation where ...
- **p. 1 / Abstract - extractive body cue:** The key idea is to crowdsource digital twins of real-world scenes using 3D reconstruction and collect large-scale data in simulation, rather than the real-world.
- **p. 1 / Abstract - extractive body cue:** Data ion is intially driven by RL, bootstrapped ms.
- **p. 1 / Abstract - extractive body cue:** As the training of a generalist policy progresses across environments, its generalization capabilities ‘can be used to replace human effort with model-generated tions.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Continual learning also faces challenges, such as catastrophic forgetting, as discussed in prior work [18].
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Generating procedurally accurate training environ- ‘ments remains an open challenge.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort.
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Our contributions include 1) a novel continual data collection system based on real-to-sim-to-real for training generalist policies, 2) a novel scanned deployment fine-tuning technique for ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Overview of CASHER, we propose « system for taining generalist policies leveraging real-o-sim simulation on crowdsouced scans.
- **p. 3 / 1. Iyrropucrion - extractive body cue:** CASHER consists of three elements - 1) fast, accessible digital twin generation with 3-D reconstruction methods, 2) multi-environment model learning that amortizes the data collection ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local point ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** The poticy model is a simple Multi-Layer Perceptron (MLP) network, with input as the privileged state in simulation as specified in VII and outputs a ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together With the state of the robot (end-effector scaled pose, postion, ... | observation history와 expert trajectory/action | p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS) |
| State/latent | train, MLP, network, size, takes, embedding, point, cloud, observation, dimensions, together, state | behavior policy와 temporal action context | p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS), p. 4 (B. Amortized Data Collection) |
| Output/action | The poticy model is a simple Multi-Layer Perceptron (MLP) network, with input as the privileged state in simulation as specified in VII and outputs a probability <istribution of 14 classes, corresponding t0 ... | predicted action 또는 action chunk | p. 12 (IX. IMPLEMENTATION DETAILS), p. 4 (B. Amortized Data Collection), p. 4 (B. Amortized Data Collection) |
| Objective/outcome | To implement PPO with the BC loss algorithm, we built upon the Stable Baselines 3 repository [33]. | imitation error, task success, robustness와 compounding error | p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort.
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Our contributions include 1) a novel continual data collection system based on real-to-sim-to-real for training generalist policies, 2) a novel scanned deployment fine-tuning technique for ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Overview of CASHER, we propose « system for taining generalist policies leveraging real-o-sim simulation on crowdsouced scans.
- **p. 3 / 1. Iyrropucrion - extractive body cue:** CASHER consists of three elements - 1) fast, accessible digital twin generation with 3-D reconstruction methods, 2) multi-environment model learning that amortizes the data collection ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local point ...
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive body cue:** To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% rate ...
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive body cue:** Furthermore, Figure 3b shows a linear correlation between simulation and real world performance, indicating that our real-to-sim-to-real scaling approach in simulation proportionally corresponds to improved ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| Embodiment/environment | The first experiment involves a thorough real-world evaluation of these policies across two institutions, using three different kitchens and six different objects, with six rollouts ‘each (a total of 108 rollouts per ... | hardware/simulator version and reset protocol | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Dataset/benchmark | For fair comparison, we train these policies using human demonstrations in each environment. | role, split, size and leakage | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS), p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Metric | As shown in Figure 3 a, we confirm the real-to-sim-to-real pipeline scaling law: as the number of trained environments increases, the zeroshot success rate also increases, reaching a 62% when trained ‘on ... | definition, denominator, direction and uncertainty | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Baseline/ablation | In Section IV-B, ‘we compare this baseline to the autonomous data collection system presented in Section III-B. | fair input/data/compute/action matching | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS), p. 6 (A. Zero-Shot Scaling Laws Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 4 / B. Amortized Data Collection - extractive body cue:** For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a second state-based policy *+a(a,/s) using demonstration-bootstrapped reinforcement ...
- **p. 5 / B. Amortized Data Collection - extractive body cue:** This reduces the amount of human effort required for data collection as training progresses, Importantly, the generalization across environments does not need to achieve perfect ...
- **p. 4 / B. Amortized Data Collection - extractive body cue:** T can be used to obtain a single robust, statecovering optimal multi-environment policy xs3(as/s¢) for all Ex :1,-++»€2x Via demonstration-bootstrapped reinforcement learning.
- **p. 5 / C. Fine-uning of Generalist Policies on Deployment - extractive body cue:** This model-generated data can then be used to train a robust, high-coverage statebased policy 4(a/s+) using demonstration-bootstrapped re
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive body cue:** To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% rate ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 10. Overview of the experiment setup for evaluating the robustness

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 Continual learning also faces challenges, such as catastrophic forgetting, as discussed in prior work [18].를 문제로 두고, We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 1 (1. Iyrropucrion), p. 12 (IX. IMPLEMENTATION DETAILS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
