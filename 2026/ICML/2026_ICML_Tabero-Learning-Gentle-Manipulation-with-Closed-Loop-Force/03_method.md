# Method - Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2605.27886; PDF retrieval source: https://arxiv.org/pdf/2605.27886. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.4. Tabero-VTLA), p. 4 (3.4. Tabero-VTLA), p. 6 (3.6. Metrics Beyond Success Rate), p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 6 (3.6. Metrics Beyond Success Rate)): Although these fingertip forces can be decomposed to recover the full 6D interaction wrench on the object, we find it more effective to directly feed the concatenated 6D vector into ...

## Method Body Digest

- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Although these fingertip forces can be decomposed to recover the full 6D interaction wrench on the object, we find it more effective to directly feed ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Its features then interact with visual features via cross-attention in the transformer, enabling joint reasoning over contact history and scene geometry.
- **p. 6 / 3.6. Metrics Beyond Success Rate - extractive body cue:** To address this limitation, we introduce a set of processaware metrics that quantify the quality of physical interaction during task execution: Maximum Transient Grip Force ...
- **p. 5 / 3.5. Decoupled Force-Position Hybrid Controller - extractive body cue:** Real-time force feedback system: the policy predicts force-position commands, which a decoupled low-level controller tracks to achieve compliant interaction.
- **p. 5 / 3.5. Decoupled Force-Position Hybrid Controller - extractive body cue:** The policy outputs a desired end-effector pose Ppred ∈SE(3) and a target applied force Ftarget applied (expressed in ΣC ).
- **p. 6 / 3.6. Metrics Beyond Success Rate - extractive body cue:** The mean applied force magnitude during contact, measuring overall interaction intensity.
- **p. 3 / 3.2. Cross-Modal Data Acquisition - extractive body cue:** Force Modality Language Modality "Pick up firmly" Action Modality Vision Modality Tactile Modality OpenSource Manipulation Traj. & Task Config Tabero Different Physical Parameters Different Modalities ...
- **p. 3 / 3.1. Cross-Platform Data Reutilization - extractive body cue:** To address this issue, we align the tool center point (TCP) of the end-effector by adjusting the base pose of the robot arm and use ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our work makes the following contributions: The Tabero benchmark, which enables scalable visiontactile-language data generation by replaying open-source trajectories in a high-fidelity tactile ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Building on the Pi0 infrastructure and leveraging flow matching, our approach enables continuous prediction of both pose and force.
- **p. 1 / 1. Introduction - extractive body cue:** To enable language-conditioned gentle manipulation, we introduce Tabero (Fig.

## Source Evidence Cues

- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Although these fingertip forces can be decomposed to recover the full 6D interaction wrench on the object, we find it more effective to directly feed ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Its features then interact with visual features via cross-attention in the transformer, enabling joint reasoning over contact history and scene geometry.
- **p. 6 / 3.6. Metrics Beyond Success Rate - extractive body cue:** To address this limitation, we introduce a set of processaware metrics that quantify the quality of physical interaction during task execution: Maximum Transient Grip Force ...
- **p. 5 / 3.5. Decoupled Force-Position Hybrid Controller - extractive body cue:** Real-time force feedback system: the policy predicts force-position commands, which a decoupled low-level controller tracks to achieve compliant interaction.
- **p. 5 / 3.5. Decoupled Force-Position Hybrid Controller - extractive body cue:** The policy outputs a desired end-effector pose Ppred ∈SE(3) and a target applied force Ftarget applied (expressed in ΣC ).
- **p. 6 / 3.6. Metrics Beyond Success Rate - extractive body cue:** The mean applied force magnitude during contact, measuring overall interaction intensity.
- **p. 3 / 3.2. Cross-Modal Data Acquisition - extractive body cue:** Force Modality Language Modality "Pick up firmly" Action Modality Vision Modality Tactile Modality OpenSource Manipulation Traj. & Task Config Tabero Different Physical Parameters Different Modalities ...
- **Detected method headings:** 3. Method (p. 3); 3.5. Decoupled Force-Position Hybrid Controller (p. 5); 4.3. Effectiveness of Hybrid Controller (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Although these fingertip forces can be decomposed to recover the full 6D interaction wrench on the object, we find it more effective ... | p. 4 (3.4. Tabero-VTLA), p. 4 (3.4. Tabero-VTLA) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Its features then interact with visual features via cross-attention in the transformer, enabling joint reasoning over contact history and scene geometry. | p. 4 (3.4. Tabero-VTLA), p. 6 (3.6. Metrics Beyond Success Rate) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | To address this limitation, we introduce a set of processaware metrics that quantify the quality of physical interaction during task execution: Maximum ... | p. 6 (3.6. Metrics Beyond Success Rate), p. 5 (3.5. Decoupled Force-Position Hybrid Controller) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Cross-Platform Data Reutilization - extractive body cue:** To address this issue, we align the tool center point (TCP) of the end-effector by adjusting the base pose of the robot arm and use ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Below, we detail the tactile tokenizer and loss function, and also compare alternative tactile injection strategies inspired by prior work.
- **p. 5 / 3.4. Tabero-VTLA - extractive body cue:** Force Supervision Flow matching naturally supports continuous force prediction, motivating our weighted loss design.
- **p. 5 / 3.4. Tabero-VTLA - extractive body cue:** The final loss is: L = 1 Dact Dact X d=1 wd(ed)2, (2) where wd = λforce for dimensions corresponding to predicted forces, and wd ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 4 (3.4. Tabero-VTLA), p. 5 (3.4. Tabero-VTLA), p. 5 (3.4. Tabero-VTLA).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Real-Time, Force, Feedback, System, VTLA, VIT, Paligemma, Action, Expert, Robot, States, Force-aware, Instruction, Marker | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Real-Time, Force, Feedback, System, VTLA, VIT, Paligemma, Action, Expert, Robot | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | summary, makes, following, contributions, Tabero, benchmark, enables, scalable, visiontactile-language, data | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | address, issue, align, tool, center, point, TCP, end-effector, adjusting, base | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.5. Decoupled Force-Position Hybrid Controller - extractive body cue:** Real-Time Force Feedback System VTLA System VIT Paligemma Action Expert Robot States Force-aware Instruction Marker Motion Field?
- **p. 4 / 3.2. Cross-Modal Data Acquisition - extractive body cue:** All cameras are rendered in parallel using tiled rendering, and all modalities, including visual, tactile, force, language instructions, and executed actions, are sampled synchronously at ...
- **p. 5 / 3.5. Decoupled Force-Position Hybrid Controller - extractive body cue:** Real-time force feedback system: the policy predicts force-position commands, which a decoupled low-level controller tracks to achieve compliant interaction.
- **p. 2 / 1. Introduction - extractive body cue:** Tabero-VTLA: Leveraging the Tabero dataset, we propose a VTLA system featuring a decoupled force-position controller and introduce a multidimensional evaluation protocol to comprehensively assess the ...
- **p. 4 / 3.3. Enriching Tactile Force Diversity - extractive body cue:** Language instructions are augmented with adverbs such as "gently" or "softly" for low-force interactions and "firmly" or "tightly" for high-force ones, aligning semantics with the ...
- **p. 2 / 1. Introduction - extractive body cue:** Motivation: Current vision-language-action (VLA) systems and robotic arm-gripper setups based on synthetic data lack force feedback mechanisms, causing learned policies to frequently damage objects during ...
- **p. 1 / 1. Introduction - extractive body cue:** While recent advances in vision-language-action (VLA) foundation models have shown remarkable progress (Kim et al., 2025a; Black et al., 2025b;a; NVIDIA et al., 2025; Liu ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | All cameras are rendered in parallel using tiled rendering, and all modalities, including visual, tactile, force, language instructions, and executed actions, are ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | A lightweight Temporal Convolutional Network (TCN) encodes this spatiotemporal sequence into tokens for integration into the transformer backbone. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | All cameras are rendered in parallel using tiled rendering, and all modalities, including visual, tactile, force, language instructions, and executed actions, are ... | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4.4. Ablation and Comparison of VTLA - extractive body cue:** All models, excluding the ablation architectures, were fine-tuned via LoRA with an identical set of hyperparameters, detailed parameters reported in the Appendix A.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Although, fingertip, forces, decomposed, recover, full, interaction, wrench, object, find, more, effective, directly, feed, concatenated, vector, multilayer, perceptron, MLP, obtain.
- **Relevant PDF headings:** 3. Method (p. 3); 3.5. Decoupled Force-Position Hybrid Controller (p. 5); 4.3. Effectiveness of Hybrid Controller (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Specifically, we select four subtasks from the LIBERO benchmark suite and compare the success rates of the original MuJoCo-based dataset with those ... | p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation) |
| Baseline harness | We compare a baseline using binary gripper control against our approach, which explicitly sets different force parameters during execution, the results are ... | p. 6 (4.2. Tactile Data Diversity Analysis), p. 6 (4.1. Cross-Platform Data Validation) |
| Metric / failure reporting | Adding explicit force supervision enables precise force prediction and substantially improves performance under gentle conditions. | p. 8 (4.4. Ablation and Comparison of VTLA), p. 8 (4.4. Ablation and Comparison of VTLA) |

## Failure and Ablation Link

- **p. 7 / 4.3. Effectiveness of Hybrid Controller - extractive body cue:** We conduct four ablation studies on the gripper controller: (a) full force with hybrid control, (b) reduced force with hybrid control, (c) reduced force without ...
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** We adapt a base VLA model using LoRA to incorporate tactile marker fields (Dataset A and B), while a vision-language-only variant is trained on Dataset ...
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** 1 highlight the sensitivity of contact-rich tasks to end-effector design and force regulation.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Ablation study on gripper force control. GF stands for gripper force. In Tabero Object task 1, the predicted force is shown in blue ...
- **p. 8 / 4.4. Ablation and Comparison of VTLA - extractive body cue:** All models, excluding the ablation architectures, were fine-tuned via LoRA with an identical set of hyperparameters, detailed parameters reported in the Appendix A.
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** 2, removing tactile feedback leads to complete failure in force modulation, highlighting its critical role in gentle manipulation.
- **p. 8 / 5. Conclusions - extractive body cue:** Future work could explore reinforcement learning to balance these objectives.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.4. Tabero-VTLA), p. 4 (3.4. Tabero-VTLA), p. 6 (3.6. Metrics Beyond Success Rate), p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 6 (3.6. Metrics Beyond Success Rate), objective p. 3 (3.1. Cross-Platform Data Reutilization), p. 4 (3.4. Tabero-VTLA), p. 5 (3.4. Tabero-VTLA), p. 5 (3.4. Tabero-VTLA), temporal p. 4 (3.2. Cross-Modal Data Acquisition), p. 4 (3.4. Tabero-VTLA), p. 3 (3.2. Cross-Modal Data Acquisition), p. 3 (3.2. Cross-Modal Data Acquisition), p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 5 (3.5. Decoupled Force-Position Hybrid Controller).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
