# Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p109.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p109.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, simulation, robot data, sim-to-real, vision-based manipulation, humanoid
- Official paper: https://www.roboticsproceedings.org/rss21/p109.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p109.pdf
- Code/Project: https://co-training.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, they involve considerable cost, time, and scalability challenges, and it remains unclear whether simply scaling real-world data collection alone is sufficient to train generalist robot models.를 문제로 두고, We define these parameters in more detail and quantify them in Section IV, when we introduce the domains and tasks, and we study how important it is to align each factor between ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large real-world robot datasets hold great potential to train generalist robot models, but scaling real-world human data collection is time-consuming and resource-intensive.
- **p. 1 / Abstract - extractive body cue:** Sim= tlation has great potent ing large-scale data, especially with recent advances in generative AI and automated data generation tools that enabl °
- **p. 1 / Abstract - extractive body cue:** However, and transferring it to the real world often demands hhuman effort to bridge the reality gap.
- **p. 1 / Abstract - extractive body cue:** A compelling alternative is to co-train the policy on a mixture of simulation and real-world datasets, Preliminary studies have recently shown this strategy to substantially ...
- **p. 1 / Abstract - extractive body cue:** We derive this recipe from comprehensive experiments that validate the co-training strategy on various simulation and real-world datasets.
- **p. 1 / 1. IyrRopucTION - extractive body cue:** However, they involve considerable cost, time, and scalability challenges, and it remains unclear whether simply scaling real-world data collection alone is sufficient to train generalist ...
- **p. 2 / 1. IyrRopucTION - extractive body cue:** However, approaches that use simulation data must deal with the reality gap since the Visuals and physies in simulation do not align perfectly with the ...

## Core Idea

- **p. 3 / B. Data Composition Factors - extractive body cue:** We define these parameters in more detail and quantify them in Section IV, when we introduce the domains and tasks, and we study how important ...
- **p. 4 / C. Automated Synthetic Data Generation - extractive body cue:** Our workflow consists of three components: (1) We start with a real-world target task in mind and some prior simulation data: (2) Given real-world tasks ...
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** In this section, we present systematic studies that help identify key elements for successful co-training.
- **p. 2 / 1. IyrRopucTION - extractive body cue:** We summarize our contributions as follows:
- **p. 1 / 1. IyrRopucTION - extractive body cue:** 1: Sim-and-Real Co-Training We show how co-training policies on real-world and simulation data can attain superior per formance in the real-robot deployment, compared to training ...
- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** In practice, we use an ‘equivalent formulation of a, which represents the probability ‘of sampling from simulation data in each training batch.
- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** We adopt the co-training formulation following prior work [7], where ‘we minimize the behavioral cloning action loss
- **p. 2 / B. Sim-to-Real and Sim-Real Co-Training - extractive body cue:** However, domain randomization approaches can require careful tuning and a significant human burden to determine proper randomization ranges for the parameters that enable the policy ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this framework, policies are trained to predict actions based fon ground truth state-action pairs provided in a demonstration dataset. | proprioception, reference pose/motion, visual or language command | p. 2 (A. Learning Manipulation from Demonstration Data), p. 3 (B. Sim-to-Real and Sim-Real Co-Training) |
| State/latent | framework, policies, trained, predict, actions, ground, truth, state-action, pairs, provided, demonstration, dataset | whole-body pose, balance/contact state와 skill/mode | p. 2 (A. Learning Manipulation from Demonstration Data), p. 3 (B. Sim-to-Real and Sim-Real Co-Training), p. 6 (1) The same robot and action spa) |
| Output/action | Our study aims to provide actionable guidelines ‘on how to strategically combine these data sources to achieve superior policy learning outcomes in the real word. | joint/whole-body action, motion target 또는 task trajectory | p. 3 (B. Sim-to-Real and Sim-Real Co-Training), p. 6 (1) The same robot and action spa), p. 4 (IV. Srupy Serur) |
| Objective/outcome | We adopt the co-training formulation following prior work [7], where ‘we minimize the behavioral cloning action loss | tracking, balance, skill/task success와 recovery | p. 3 (A. Co-Training on Real-World and Simulation Data), p. 3 (A. Co-Training on Real-World and Simulation Data), p. 2 (B. Sim-to-Real and Sim-Real Co-Training) |

## Main Claims and Actual Contribution

- **p. 3 / B. Data Composition Factors - extractive body cue:** We define these parameters in more detail and quantify them in Section IV, when we introduce the domains and tasks, and we study how important ...
- **p. 4 / C. Automated Synthetic Data Generation - extractive body cue:** Our workflow consists of three components: (1) We start with a real-world target task in mind and some prior simulation data: (2) Given real-world tasks ...
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** In this section, we present systematic studies that help identify key elements for successful co-training.
- **p. 2 / 1. IyrRopucTION - extractive body cue:** We summarize our contributions as follows:
- **p. 1 / 1. IyrRopucTION - extractive body cue:** 1: Sim-and-Real Co-Training We show how co-training policies on real-world and simulation data can attain superior per formance in the real-robot deployment, compared to training ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates of 50% and ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** As shown in the task, we evaluate on eight new object categories (carrot, ladle, third row of Table I policies trained on Rea? and Prior ...
- **p. 8 / datasets - extractive body cue:** As shown in Tuble Il policies co-trained with DC achieve a twice higher success rate ‘compared with the policies trained solely on Real for both ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Embodiment/environment | The term "digital cousin" was recently introduced by Dai et al, [26] to describe simulation environments that are close to, but not perfectly aligned with, their real-world counterpart, We extend this notion ... | hardware/simulator version and reset protocol | p. 6 (C. Building Task-Aware Simulation Datasets), p. 7 (V. EXPERIMENTS) |
| Dataset/benchmark | ‘To understand how simulation data enhances real-world Policy performance, we investigate whether exposure to diA, Effectiveness of Sim-and-Real Co-Training verse situations in simulation-ones not explicitly covered Coctraining with tas ... | role, split, size and leakage | p. 6 (C. Building Task-Aware Simulation Datasets), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (C. Building Task-Aware Simulation Datasets) |
| Metric | This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates of 50% and 80%. | definition, denominator, direction and uncertainty | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (datasets) |
| Baseline/ablation | This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates of 50% and 80%. | fair input/data/compute/action matching | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / VI. Limtrarions - extractive body cue:** Extending our approach to a broader set of manipulation tasks, such as high-precision insertion, and longer-horizon tasks, is left for future work.
- **p. 9 / VI. Limtrarions - extractive body cue:** Applying this cotraining strategy to such tasks presents a challenge, Future work could explore the use of co-training data produced by video generation models and ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Next, we delve into the systematic experiments that guided further investigate the robustness of this gap by training the the development of our recipe (Section ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The diversimulation data to enhance real-world policy performance. sity in simulation data contributes to improved generalizability Finally, in the last row of Table 1, policies ...
- **p. 8 / datasets - extractive body cue:** This result indicates that diverse simulation data substantially improve policy robustness to spatial variations.
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 12: Examples of the Video2Video model outputs with different noise strength, Left: An example video frame from the simulation

## Why Read It

RL, IL, offline learning, and robot data의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, they involve considerable cost, time, and scalability challenges, and it remains unclear whether simply scaling real-world data collection alone is sufficient to train generalist robot models.를 문제로 두고, We define these parameters in more detail and quantify them in Section IV, when we introduce the domains and tasks, and we study how important it is to align each factor between ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. IyrRopucTION), p. 1 (Abstract), p. 2 (1. IyrRopucTION), p. 2 (B. Sim-to-Real and Sim-Real Co-Training), p. 4 (IV. Srupy Serur), p. 3 (A. Co-Training on Real-World and Simulation Data) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, they involve considerable cost, time, and scalability challenges, and it remains unclear whether simply scaling real-world data collection alone is sufficient to train generalist robot models. (p. 1, 1. IyrRopucTION).
- **Actual contribution:** 1: Sim-and-Real Co-Training We show how co-training policies on real-world and simulation data can attain superior per formance in the real-robot deployment, compared to training solely ‘on real-world data, We ... (p. 1, 1. IyrRopucTION).
- **Evaluation boundary:** Specifically, we demonstrate how co-training with simulation data enhances the real-world policy's in-domain performance (Section V-A) and improves its generalization to novel scenarios (Section V-B). (p. 6, V. EXPERIMENTS).
- **Explicit failure boundary:** Finally, for the CLoseDoo= task, we recon 4 success if the door's joint angle is less than 5° and record a failure otherwise (p. 15, 256. We also add language conditioning to facilitate training).
