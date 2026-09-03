# Method - Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p109.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p109.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (A. Co-Training on Real-World and Simulation Data), p. 3 (A. Co-Training on Real-World and Simulation Data), p. 2 (B. Sim-to-Real and Sim-Real Co-Training), p. 8 (C. Effectiveness of Co-Training in Data-Rich Settings), p. 8 (C. Effectiveness of Co-Training in Data-Rich Settings), p. 2 (2) We demonstrate empirically how co-training on syn)): In practice, we use an ‘equivalent formulation of a, which represents the probability ‘of sampling from simulation data in each training batch.

## Method Body Digest

- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** In practice, we use an ‘equivalent formulation of a, which represents the probability ‘of sampling from simulation data in each training batch.
- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** We adopt the co-training formulation following prior work [7], where ‘we minimize the behavioral cloning action loss
- **p. 2 / B. Sim-to-Real and Sim-Real Co-Training - extractive body cue:** However, domain randomization approaches can require careful tuning and a significant human burden to determine proper randomization ranges for the parameters that enable the policy ...
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** Our findings highlight practical strategies for optimizing co-training and improving real-world policy performance.
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** Even with 400 real demonstrations, the co-trained policy consistently outperforms the realonly policy, demonstrating that sim-and-real co-training remains beneficial even in data-rich settings.
- **p. 2 / 2) We demonstrate empirically how co-training on syn - extractive body cue:** improving policy performance across two domains by an average of 38%;
- **p. 9 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** A Simple Recipe for Sim-and-Real Co-Training
- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** Our end objective is to produce vision-based manipulation policies that maximize task performance on one or multiple downstream tasks in real-world environments.

## Design Rationale

- **p. 3 / B. Data Composition Factors - extractive body cue:** We define these parameters in more detail and quantify them in Section IV, when we introduce the domains and tasks, and we study how important ...
- **p. 4 / C. Automated Synthetic Data Generation - extractive body cue:** Our workflow consists of three components: (1) We start with a real-world target task in mind and some prior simulation data: (2) Given real-world tasks ...
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** In this section, we present systematic studies that help identify key elements for successful co-training.

## Source Evidence Cues

- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** In practice, we use an ‘equivalent formulation of a, which represents the probability ‘of sampling from simulation data in each training batch.
- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** We adopt the co-training formulation following prior work [7], where ‘we minimize the behavioral cloning action loss
- **p. 2 / B. Sim-to-Real and Sim-Real Co-Training - extractive body cue:** However, domain randomization approaches can require careful tuning and a significant human burden to determine proper randomization ranges for the parameters that enable the policy ...
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** Our findings highlight practical strategies for optimizing co-training and improving real-world policy performance.
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** Even with 400 real demonstrations, the co-trained policy consistently outperforms the realonly policy, demonstrating that sim-and-real co-training remains beneficial even in data-rich settings.
- **p. 2 / 2) We demonstrate empirically how co-training on syn - extractive body cue:** improving policy performance across two domains by an average of 38%;
- **p. 9 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** A Simple Recipe for Sim-and-Real Co-Training
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | In practice, we use an ‘equivalent formulation of a, which represents the probability ‘of sampling from simulation data in each training batch. | p. 3 (A. Co-Training on Real-World and Simulation Data), p. 3 (A. Co-Training on Real-World and Simulation Data) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | We adopt the co-training formulation following prior work [7], where ‘we minimize the behavioral cloning action loss | p. 3 (A. Co-Training on Real-World and Simulation Data), p. 2 (B. Sim-to-Real and Sim-Real Co-Training) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | However, domain randomization approaches can require careful tuning and a significant human burden to determine proper randomization ranges for the parameters that ... | p. 2 (B. Sim-to-Real and Sim-Real Co-Training), p. 8 (C. Effectiveness of Co-Training in Data-Rich Settings) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** We adopt the co-training formulation following prior work [7], where ‘we minimize the behavioral cloning action loss
- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** Our end objective is to produce vision-based manipulation policies that maximize task performance on one or multiple downstream tasks in real-world environments.
- **p. 2 / B. Sim-to-Real and Sim-Real Co-Training - extractive body cue:** However, domain randomization approaches can require careful tuning and a significant human burden to determine proper randomization ranges for the parameters that enable the policy ...
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** The co-training ratio, cis the probability of sampling from simulation data in each rminibatch.
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** Our findings highlight practical strategies for optimizing co-training and improving real-world policy performance.
- **p. 9 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** We recommend utilizing a sufficiently large amount of simulation data (ideally, orders of magnitude more than real-world data) and carefully tuning the co-training ratio to ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 3 (A. Co-Training on Real-World and Simulation Data), p. 3 (A. Co-Training on Real-World and Simulation Data).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | framework, policies, trained, predict, actions, ground, truth, state-action, pairs, provided, demonstration, dataset, study, aims | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | framework, policies, trained, predict, actions, ground, truth, state-action, pairs, provided | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | define, parameters, more, detail, quantify, them, Section, when, introduce, domains | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | adopt, co-training, formulation, following, prior, where, minimize, behavioral, cloning, action | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / A. Learning Manipulation from Demonstration Data - extractive body cue:** In this framework, policies are trained to predict actions based fon ground truth state-action pairs provided in a demonstration dataset.
- **p. 3 / B. Sim-to-Real and Sim-Real Co-Training - extractive body cue:** Our study aims to provide actionable guidelines ‘on how to strategically combine these data sources to achieve superior policy learning outcomes in the real word.
- **p. 6 / 1) The same robot and action spa - extractive body cue:** 2) The same task goal-specifically, the same success check and, if applicable, the same language instructions; 3) The same object categories, though individual instances may ...
- **p. 4 / IV. Srupy Serur - extractive body cue:** Our goal is to develop a simple recipe for co-training ‘on real-robot and simulation data to significantly improve real-world policy performance compared to training on ...
- **p. 1 / Abstract - extractive body cue:** A compelling alternative is to co-train the policy on a mixture of simulation and real-world datasets, Preliminary studies have recently shown this strategy to substantially ...
- **p. 2 / 2) We demonstrate empirically how co-training on syn - extractive body cue:** improving policy performance across two domains by an average of 38%;
- **p. 3 / B. Sim-to-Real and Sim-Real Co-Training - extractive body cue:** IIL PROBLEM STATEMENT AND PRELIMINARIES
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Te ability to generalize across diverse environments and tasks is a critical step toward realizing generalist robotic systems. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | In this framework, policies are trained to predict actions based fon ground truth state-action pairs provided in a demonstration dataset. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | None of these 10 tasks is semantically equivalent to the real-world tasks-they involve different source and/or target receptacles, We use DexMimicGen [10], ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** In practice, we use an ‘equivalent formulation of a, which represents the probability ‘of sampling from simulation data in each training batch.
- **p. 3 / A. Co-Training on Real-World and Simulation Data - extractive body cue:** We adopt the co-training formulation following prior work [7], where ‘we minimize the behavioral cloning action loss
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** Our findings highlight practical strategies for optimizing co-training and improving real-world policy performance.
- **p. 8 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** Even with 400 real demonstrations, the co-trained policy consistently outperforms the realonly policy, demonstrating that sim-and-real co-training remains beneficial even in data-rich settings.
- **p. 9 / C. Effectiveness of Co-Training in Data-Rich Settings - extractive body cue:** A Simple Recipe for Sim-and-Real Co-Training

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** practice, equivalent, formulation, represents, probability, sampling, simulation, data, training, batch, adopt, co-training, following, prior, where, minimize, behavioral, cloning, action, loss.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | The term "digital cousin" was recently introduced by Dai et al, [26] to describe simulation environments that are close to, but not ... | p. 6 (C. Building Task-Aware Simulation Datasets), p. 7 (V. EXPERIMENTS) |
| Balance-aware whole-body execution | This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates ... | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Recovery / adaptation | This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates ... | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / V. EXPERIMENTS - extractive body cue:** ‘TABLE I: Effect of different simulation data in the co-training mix.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** 4: Effect of the quantity of real demonstrations.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** As shown in Table Il, the policy trained without manual alignment of the simulation environment, co- solely on Rea achieves a success rate of only ...
- **p. 9 / VI. Limtrarions - extractive body cue:** Extending our approach to a broader set of manipulation tasks, such as high-precision insertion, and longer-horizon tasks, is left for future work.
- **p. 9 / VI. Limtrarions - extractive body cue:** Applying this cotraining strategy to such tasks presents a challenge, Future work could explore the use of co-training data produced by video generation models and ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Next, we delve into the systematic experiments that guided further investigate the robustness of this gap by training the the development of our recipe (Section ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The diversimulation data to enhance real-world policy performance. sity in simulation data contributes to improved generalizability Finally, in the last row of Table 1, policies ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (A. Co-Training on Real-World and Simulation Data), p. 3 (A. Co-Training on Real-World and Simulation Data), p. 2 (B. Sim-to-Real and Sim-Real Co-Training), p. 8 (C. Effectiveness of Co-Training in Data-Rich Settings), p. 8 (C. Effectiveness of Co-Training in Data-Rich Settings), p. 2 (2) We demonstrate empirically how co-training on syn), objective p. 3 (A. Co-Training on Real-World and Simulation Data), p. 3 (A. Co-Training on Real-World and Simulation Data), p. 2 (B. Sim-to-Real and Sim-Real Co-Training), p. 8 (C. Effectiveness of Co-Training in Data-Rich Settings), p. 8 (C. Effectiveness of Co-Training in Data-Rich Settings), p. 9 (C. Effectiveness of Co-Training in Data-Rich Settings), temporal p. 1 (1. IyrRopucTION), p. 2 (A. Learning Manipulation from Demonstration Data), p. 3 (C. Automated Synthetic Data Generation), p. 6 (4) The same environmental fixture categories (e.g. kitchen), p. 6 (B. Prior Task-Agnostic Simulation Data), p. 9 (VI. Limtrarions).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** We adopt the co-training formulation following prior work [7], where ‘we minimize the behavioral cloning action loss (p. 3, A. Co-Training on Real-World and Simulation Data).
- **Objective/update evidence:** We adopt the co-training formulation following prior work [7], where ‘we minimize the behavioral cloning action loss (p. 3, A. Co-Training on Real-World and Simulation Data).
- **Temporal/runtime evidence:** Te ability to generalize across diverse environments and tasks is a critical step toward realizing generalist robotic systems. (p. 1, 1. IyrRopucTION).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
