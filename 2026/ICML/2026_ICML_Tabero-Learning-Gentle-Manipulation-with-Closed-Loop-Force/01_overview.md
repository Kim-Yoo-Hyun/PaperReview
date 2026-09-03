# Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2605.27886.
> PDF retrieval source: https://arxiv.org/pdf/2605.27886. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, VLA, tactile, force feedback, contact-rich manipulation, Benchmark, dexterity
- Official paper: https://arxiv.org/abs/2605.27886
- Full-text retrieval: https://arxiv.org/pdf/2605.27886
- Code/Project: https://github.com/NathanWu7/Tabero
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Training such models, however, faces two major challenges.를 문제로 두고, In summary, our work makes the following contributions: The Tabero benchmark, which enables scalable visiontactile-language data generation by replaying open-source trajectories in a high-fidelity tactile simulator and establishes the f ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Tactile sensing is essential for robots to achieve human-like gentle manipulation.
- **p. 1 / Abstract - extractive body cue:** However, existing Vision-Language-Action (VLA) models struggle to exploit tactile feedback for gentle manipulation due to scarce aligned vision-tactile-language data and the lack of effective closed-loop ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce Tabero, a benchmark and model suite for gentle, language-conditioned robotic manipulation that demands fine-grained contact force perception.
- **p. 1 / Abstract - extractive body cue:** First, the Tabero benchmark addresses the scarcity of tactile data by presenting a data-efficient pipeline that repurposes open-source robot manipulation trajectories to generate diverse vision-tactile-language ...
- **p. 1 / Abstract - extractive body cue:** Second, we propose Tabero-VTLA, an architecture with a decoupled force-position command interface; the resulting force-position commands are executed by a fixed hybrid controller to enable ...
- **p. 1 / 1. Introduction - extractive body cue:** Training such models, however, faces two major challenges.
- **p. 1 / 1. Introduction - extractive body cue:** Simulation offers a scalable alternative, yet existing pipelines focus on visual diversity and lack efficient mechanisms to generate and integrate high-fidelity tactile signals.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our work makes the following contributions: The Tabero benchmark, which enables scalable visiontactile-language data generation by replaying open-source trajectories in a high-fidelity tactile ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Building on the Pi0 infrastructure and leveraging flow matching, our approach enables continuous prediction of both pose and force.
- **p. 1 / 1. Introduction - extractive body cue:** To enable language-conditioned gentle manipulation, we introduce Tabero (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** Tabero: We present a high-fidelity multimodal simulation platform integrating Isaac Lab with advanced tactile simulation.
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** To integrate this tactile signal into the VLA foundation model, we introduce a tactile tokenizer that maps tactile inputs into conditional tokens.
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Although these fingertip forces can be decomposed to recover the full 6D interaction wrench on the object, we find it more effective to directly feed ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Its features then interact with visual features via cross-attention in the transformer, enabling joint reasoning over contact history and scene geometry.
- **p. 6 / 3.6. Metrics Beyond Success Rate - extractive body cue:** To address this limitation, we introduce a set of processaware metrics that quantify the quality of physical interaction during task execution: Maximum Transient Grip Force ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Real-Time Force Feedback System VTLA System VIT Paligemma Action Expert Robot States Force-aware Instruction Marker Motion Field? | standardized observation, action, task state와 evaluation split | p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 4 (3.2. Cross-Modal Data Acquisition) |
| State/latent | Real-Time, Force, Feedback, System, VTLA, VIT, Paligemma, Action, Expert, Robot, States, Force-aware | benchmark state/goal와 method decision | p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 4 (3.2. Cross-Modal Data Acquisition), p. 5 (3.5. Decoupled Force-Position Hybrid Controller) |
| Output/action | All cameras are rendered in parallel using tiled rendering, and all modalities, including visual, tactile, force, language instructions, and executed actions, are sampled synchronously at 20 Hz to produce temporally aligned multimodal ... | policy/controller trajectory 또는 measured result | p. 4 (3.2. Cross-Modal Data Acquisition), p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 2 (1. Introduction) |
| Objective/outcome | To address this issue, we align the tool center point (TCP) of the end-effector by adjusting the base pose of the robot arm and use a high-gain PD joint controller during trajectory ... | success metric, robustness, generalization과 reproducibility | p. 3 (3.1. Cross-Platform Data Reutilization), p. 4 (3.4. Tabero-VTLA), p. 5 (3.4. Tabero-VTLA) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our work makes the following contributions: The Tabero benchmark, which enables scalable visiontactile-language data generation by replaying open-source trajectories in a high-fidelity tactile ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Building on the Pi0 infrastructure and leveraging flow matching, our approach enables continuous prediction of both pose and force.
- **p. 1 / 1. Introduction - extractive body cue:** To enable language-conditioned gentle manipulation, we introduce Tabero (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** Tabero: We present a high-fidelity multimodal simulation platform integrating Isaac Lab with advanced tactile simulation.
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** To integrate this tactile signal into the VLA foundation model, we introduce a tactile tokenizer that maps tactile inputs into conditional tokens.
- **p. 8 / 4.4. Ablation and Comparison of VTLA - extractive body cue:** Adding explicit force supervision enables precise force prediction and substantially improves performance under gentle conditions.
- **p. 8 / 4.4. Ablation and Comparison of VTLA - extractive body cue:** When tactile tokens such as images or force fields are provided, the policy gains basic force modulation ability and achieves nontrivial success.
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** Cross-platform data validation: Task success rates across four LIBERO subtasks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (4.4. Ablation and Comparison of VTLA), p. 8 (4.4. Ablation and Comparison of VTLA) |
| Embodiment/environment | Specifically, we select four subtasks from the LIBERO benchmark suite and compare the success rates of the original MuJoCo-based dataset with those of our replayed version in Isaac Lab. | hardware/simulator version and reset protocol | p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation) |
| Dataset/benchmark | This subset includes 9 tasks from the Object dataset, each executed under two force conditions specified by linguistic adverbs. | role, split, size and leakage | p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis), p. 7 (4.2. Tactile Data Diversity Analysis) |
| Metric | Cross-platform data validation: Task success rates across four LIBERO subtasks. | definition, denominator, direction and uncertainty | p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis) |
| Baseline/ablation | We compare a baseline using binary gripper control against our approach, which explicitly sets different force parameters during execution, the results are shown in fig. | fair input/data/compute/action matching | p. 6 (4.2. Tactile Data Diversity Analysis), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.3. Effectiveness of Hybrid Controller) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** 2, removing tactile feedback leads to complete failure in force modulation, highlighting its critical role in gentle manipulation.
- **p. 8 / 5. Conclusions - extractive body cue:** Future work could explore reinforcement learning to balance these objectives.
- **p. 8 / 5. Conclusions - extractive body cue:** Nevertheless, Our current framework does not jointly optimize for both task success and minimal interaction force.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Tabero Simulation Platform. Tabero replicates the LIBERO task environments, enables data reuse, enhances the visual fidelity of simulated data, and makes it possible ...
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** Dataset B also employs continuous control but reduces the force to 10%, representing an extreme low-force regime where slippage is likely.
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** This degradation is especially pronounced in tasks requiring delicate manipulation, where lower grip forces strongly correlate with reduced success.

## Why Read It

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Training such models, however, faces two major challenges.를 문제로 두고, In summary, our work makes the following contributions: The Tabero benchmark, which enables scalable visiontactile-language data generation by replaying open-source trajectories in a high-fidelity tactile simulator and establishes the f ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. Tabero-VTLA), p. 4 (3.4. Tabero-VTLA), p. 6 (3.6. Metrics Beyond Success Rate) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Training such models, however, faces two major challenges. (p. 1, 1. Introduction).
- **Actual contribution:** In summary, our work makes the following contributions: The Tabero benchmark, which enables scalable visiontactile-language data generation by replaying open-source trajectories in a high-fidelity tactile simulator and establishes the f ... (p. 2, 1. Introduction).
- **Evaluation boundary:** When using the same robot kinematics and control policy as in the original dataset, our baseline configuration yields a success rate distribution that closely matches that reported in OpenVLA (Kim ... (p. 6, 4.1. Cross-Platform Data Validation).
- **Explicit failure boundary:** 2, removing tactile feedback leads to complete failure in force modulation, highlighting its critical role in gentle manipulation. (p. 7, 4.2. Tactile Data Diversity Analysis).
