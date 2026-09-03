# Method - Can VLMs Diagnose and Recover from VLA Manipulation Faults?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://kakigo.github.io/VLA-FixBench/; PDF retrieval source: https://kakigo.github.io/VLA-FixBench/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (Approach), p. 3 (Approach)): Reinforcement learning has been explored for failure recovery by learning corrective behaviors through interaction, including recent efforts that guide agents back to in-distribution states after Out-Of-Distribution (OOD) failures (Kim ...

## Method Body Digest

- **p. 3 / Approach - extractive body cue:** Reinforcement learning has been explored for failure recovery by learning corrective behaviors through interaction, including recent efforts that guide agents back to in-distribution states after ...
- **p. 3 / Approach - extractive body cue:** The bottom axis indicates the trade-off between evaluation convenience and physical accuracy. proaches employ supervised classifiers or temporal models to predict failure states from sensory ...
- **p. 3 / Approach - extractive body cue:** While effective in specific domains (Li et al., 2026), such methods typically rely on task rewards or policy-level supervision, embedding recovery implicitly in learned behaviors.
- **p. 1 / 1. Introduction - extractive body cue:** Moreover, current VLM-VLA interactions are largely instruction-based and lack a unified closed-loop framework for diagnosis and recovery (Yang et al., 2025a; Thoduka et al., 2024).
- **p. 1 / 1. Introduction - extractive body cue:** With the rapid advancement of embodied intelligence, Vision-Language-Action (VLA) models have demonstrated increasing advantages in scenarios such as industrial assembly, logistics sorting, and household services.
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • VLA-FixBench, a robotic manipulation fault evaluation dataset comprising 6k failure cases covering perception, control, and cognition errors, ...
- **p. 2 / 1. Introduction - extractive body cue:** We further construct a VLM-VLA collaboration mechanism that enables fault detection, rollback, and action repair during VLA execution.
- **p. 4 / 3. Construction of VLA-FixBench - extractive body cue:** Multi-dimensional Annotation We develop a fine-grained annotation framework to construct a high-resolution failure map across three integrated dimensions: temporal, spatial, and semantic.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce VLA-FixBench, a benchmark for VLM-assisted VLA fault diagnosis and recovery, with over 6,000 annotated failure cases across perception, planning, ...
- **p. 1 / 1. Introduction - extractive body cue:** Based on VLA-FixBench, we propose FaultEval, a unified static-to-dynamic-to-real evaluation framework that assesses VLM performance in fault identification, severity estimation, temporal localization, spatial correction, and ...
- **p. 2 / 1. Introduction - extractive body cue:** We further construct a VLM-VLA collaboration mechanism that enables fault detection, rollback, and action repair during VLA execution.

## Source Evidence Cues

- **p. 3 / Approach - extractive body cue:** Reinforcement learning has been explored for failure recovery by learning corrective behaviors through interaction, including recent efforts that guide agents back to in-distribution states after ...
- **p. 3 / Approach - extractive body cue:** The bottom axis indicates the trade-off between evaluation convenience and physical accuracy. proaches employ supervised classifiers or temporal models to predict failure states from sensory ...
- **Detected method headings:** Approach (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Reinforcement learning has been explored for failure recovery by learning corrective behaviors through interaction, including recent efforts that guide agents back to ... | p. 3 (Approach), p. 3 (Approach) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | The bottom axis indicates the trade-off between evaluation convenience and physical accuracy. proaches employ supervised classifiers or temporal models to predict failure ... | p. 3 (Approach) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Reinforcement learning has been explored for failure recovery by learning corrective behaviors through interaction, including recent efforts that guide agents back to ... | p. 3 (Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / Approach - extractive body cue:** While effective in specific domains (Li et al., 2026), such methods typically rely on task rewards or policy-level supervision, embedding recovery implicitly in learned behaviors.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | bottom, axis, indicates, trade-off, between, evaluation, convenience, physical, accuracy, proaches, employ, supervised, classifiers, temporal | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | bottom, axis, indicates, trade-off, between, evaluation, convenience, physical, accuracy, proaches | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | address, challenges, introduce, VLA-FixBench, benchmark, VLM-assisted, VLA, fault, diagnosis, recovery | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | While, effective, specific, domains, methods, typically, rely, task, rewards, policy-level | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / Approach - extractive body cue:** The bottom axis indicates the trade-off between evaluation convenience and physical accuracy. proaches employ supervised classifiers or temporal models to predict failure states from sensory ...
- **p. 3 / Approach - extractive body cue:** Reinforcement learning has been explored for failure recovery by learning corrective behaviors through interaction, including recent efforts that guide agents back to in-distribution states after ...
- **p. 1 / 1. Introduction - extractive body cue:** Moreover, current VLM-VLA interactions are largely instruction-based and lack a unified closed-loop framework for diagnosis and recovery (Yang et al., 2025a; Thoduka et al., 2024).
- **p. 1 / 1. Introduction - extractive body cue:** With the rapid advancement of embodied intelligence, Vision-Language-Action (VLA) models have demonstrated increasing advantages in scenarios such as industrial assembly, logistics sorting, and household services.
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • VLA-FixBench, a robotic manipulation fault evaluation dataset comprising 6k failure cases covering perception, control, and cognition errors, ...
- **p. 2 / 1. Introduction - extractive body cue:** We further construct a VLM-VLA collaboration mechanism that enables fault detection, rollback, and action repair during VLA execution.
- **p. 4 / 3. Construction of VLA-FixBench - extractive body cue:** Multi-dimensional Annotation We develop a fine-grained annotation framework to construct a high-resolution failure map across three integrated dimensions: temporal, spatial, and semantic.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Real-Time Latency and Inspection Protocol Our realrobot evaluation uses a sparse pause-and-inspect protocol instead of querying the VLM at every control step. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | These models represent actions as a structured sequence within a generative framework. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Video streams are transmitted to the VLM at 1 Hz for real-time fault diagnosis, rollback decisions, and corrective action recommendations. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Reinforcement, learning, been, explored, failure, recovery, corrective, behaviors, through, interaction, including, recent, efforts, guide, agents, back, in-distribution, states, after, Out-Of-Distribution.
- **Relevant PDF headings:** Approach (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | To evaluate the practical performance of multimodal models in real-world robotic manipulation, we conduct on-robot experiments. | p. 6 (4.3. Real-Time Evaluation), p. 9 (5.4. Real-Time Evaluation Results) |
| Baseline harness | Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, ... | p. 5 (4.2. Dynamic Evaluation), p. 8 (5.4. Real-Time Evaluation Results) |
| Metric / failure reporting | Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, ... | p. 5 (4.2. Dynamic Evaluation), p. 9 (5.6. Ablation Study) |

## Failure and Ablation Link

- **p. 5 / 4.2. Dynamic Evaluation - extractive body cue:** This design follows three principles: (1) clarity and simplicity, allowing general black-box VLMs to integrate without model-specific output heads or adapters; (2) direct mapping from ...
- **p. 8 / 5.4. Real-Time Evaluation Results - extractive body cue:** Real-robot evaluations (Table 3) validate the sensitivitystability paradox.
- **p. 8 / 5.4. Real-Time Evaluation Results - extractive body cue:** Current VLMs may misclassify trajectories that would have succeeded without intervention, triggering unnecessary rollback or correction and turning successes into failures.
- **p. 3 / 2.2. Benchmark and Failure Evaluation of VLM - extractive body cue:** Architectures like OpenVLA (Kim et al., 2024) and GR00T N1 (NVIDIA et al., 2025) utilize frozen vision-language backbones augmented with lightweight action heads to maintain ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Data Acquisition.For simulation, we fine-tuned OpenVLA7B (Kim et al., 2024) using data from the LIBERO bencha b c d e f g h i i ...
- **p. 9 / 5.4. Real-Time Evaluation Results - extractive body cue:** The real-robot setup is therefore a sparse diagnostic-and-recovery loop that trades limited inspection latency for recovery from failures that the VLA alone cannot escape.
- **p. 3 / 2.2. Benchmark and Failure Evaluation of VLM - extractive body cue:** We introduce a unified benchmark and evaluation framework that systematically characterizes failure types, severity, and spatiotemporal repair behaviors, and explicitly measures how VLMs contribute to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (Approach), p. 3 (Approach), objective p. 3 (Approach), temporal p. 9 (5.4. Real-Time Evaluation Results), p. 3 (2.2. Benchmark and Failure Evaluation of VLM), p. 3 (2.2. Benchmark and Failure Evaluation of VLM), p. 4 (4. FaultEval Evaluation Framework), p. 4 (4.2. Dynamic Evaluation), p. 6 (4.3. Real-Time Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Reinforcement learning has been explored for failure recovery by learning corrective behaviors through interaction, including recent efforts that guide agents back to in-distribution states after Out-Of-Distribution (OOD) failures (Kim ... (p. 3, Approach).
- **Objective/update evidence:** While effective in specific domains (Li et al., 2026), such methods typically rely on task rewards or policy-level supervision, embedding recovery implicitly in learned behaviors. (p. 3, Approach).
- **Temporal/runtime evidence:** Real-Time Latency and Inspection Protocol Our realrobot evaluation uses a sparse pause-and-inspect protocol instead of querying the VLM at every control step. (p. 9, 5.4. Real-Time Evaluation Results).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
