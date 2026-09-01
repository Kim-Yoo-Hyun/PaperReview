# Method - VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://vla-arena.github.io/; PDF retrieval source: https://arxiv.org/pdf/2512.22539. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (1. Introduction), p. 6 (3. Task Suites in VLA-Arena), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Structured Task Design), p. 4 (2. Structured Task Design)): Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key findings: (I) a reliance on ...

## Method Body Digest

- **p. 3 / 1. Introduction - extractive body cue:** Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key ...
- **p. 6 / 3. Task Suites in VLA-Arena - extractive body cue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models 0.0 0.25 0.5 0.75 1.0 Success Rate StatePreservation L0 OpenVLA OpenVLA-OFT Pi0 UniVLA L1 L2 L0 L1 ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this challenge, we propose VLA-Arena, a comprehensive and accessible benchmark for evaluating VLA models.
- **p. 2 / 1. Introduction - extractive body cue:** By stressing models with these structured perturbations, we expose latent fragilities and determine whether models rely on robust grounding or fragile memorization of training patterns.
- **p. 3 / 2. Structured Task Design - extractive body cue:** To quantitatively measure the capability frontiers of VLA models, we propose a structured task design, as compared in Table 1.
- **p. 4 / 2. Structured Task Design - extractive body cue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models object configurations, and minimal environmental or planning challenges, representing well-practiced scenarios. • Level 1 (L1) Near-Distribution Generali ...
- **p. 6 / 3. Task Suites in VLA-Arena - extractive body cue:** Models are first trained on a vocabulary of foundational skills (L0).
- **p. 5 / 3. Task Suites in VLA-Arena - extractive body cue:** This dimension evaluates the model's ability to not only complete its primary objective but to do so while adhering to safety constraints, a critical requirement ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We introduce VLA-Arena, the first benchmark to structurally evaluate the performance and safety of VLAs.
- **p. 2 / 1. Introduction - extractive body cue:** To address this challenge, we propose VLA-Arena, a comprehensive and accessible benchmark for evaluating VLA models.
- **p. 3 / 2. Structured Task Design - extractive body cue:** To quantitatively measure the capability frontiers of VLA models, we propose a structured task design, as compared in Table 1.

## Source Evidence Cues

- **p. 3 / 1. Introduction - extractive body cue:** Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key ...
- **p. 6 / 3. Task Suites in VLA-Arena - extractive body cue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models 0.0 0.25 0.5 0.75 1.0 Success Rate StatePreservation L0 OpenVLA OpenVLA-OFT Pi0 UniVLA L1 L2 L0 L1 ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this challenge, we propose VLA-Arena, a comprehensive and accessible benchmark for evaluating VLA models.
- **p. 2 / 1. Introduction - extractive body cue:** By stressing models with these structured perturbations, we expose latent fragilities and determine whether models rely on robust grounding or fragile memorization of training patterns.
- **p. 3 / 2. Structured Task Design - extractive body cue:** To quantitatively measure the capability frontiers of VLA models, we propose a structured task design, as compared in Table 1.
- **p. 4 / 2. Structured Task Design - extractive body cue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models object configurations, and minimal environmental or planning challenges, representing well-practiced scenarios. • Level 1 (L1) Near-Distribution Generali ...
- **p. 6 / 3. Task Suites in VLA-Arena - extractive body cue:** Models are first trained on a vocabulary of foundational skills (L0).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis ... | p. 3 (1. Introduction), p. 6 (3. Task Suites in VLA-Arena) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models 0.0 0.25 0.5 0.75 1.0 Success Rate StatePreservation L0 OpenVLA OpenVLA-OFT Pi0 UniVLA L1 ... | p. 6 (3. Task Suites in VLA-Arena), p. 2 (1. Introduction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | To address this challenge, we propose VLA-Arena, a comprehensive and accessible benchmark for evaluating VLA models. | p. 2 (1. Introduction), p. 2 (1. Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3. Task Suites in VLA-Arena - extractive body cue:** This dimension evaluates the model's ability to not only complete its primary objective but to do so while adhering to safety constraints, a critical requirement ...
- **p. 1 / 170 Tasks - extractive body cue:** HDF5 RLDS Lerobot Specify Safety Constraints: Mug Fall; The Gripper in Contact with the Mug Original Observation Perturbed Observation Noise Light Camera Color C-BDDL Specify ...
- **p. 2 / Abstract - extractive body cue:** Our extensive evaluation of state-ofthe-art VLAs reveals critical limitations: memorization over generalization, superficial visual perception, and a neglect of safety constraints.
- **p. 2 / 1. Introduction - extractive body cue:** Overlooked safety: Situated in idealized environments, previous works do not address the safety constraints that are non-negotiable prior to real-world deployment (Tan et al., 2025b; ...
- **p. 3 / 1. Introduction - extractive body cue:** Metric: SR (Success Rate), CC (Cumulative Cost).
- **p. 3 / 1. Introduction - extractive body cue:** Evaluation Dims: Safety constraints, Long-Horizon, Extrapolation, Distractors.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 5 (3. Task Suites in VLA-Arena), p. 1 (170 Tasks), p. 2 (Abstract), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (2. Structured Task Design).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | VLA-Arena, Open-Source, Framework, Benchmarking, Vision-Language-Action, Models, Success, Rate, StatePreservation, OpenVLA, OpenVLA-OFT, Pi0, UniVLA, UnseenObjects | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | VLA-Arena, Open-Source, Framework, Benchmarking, Vision-Language-Action, Models, Success, Rate, StatePreservation, OpenVLA | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | introduce, VLA-Arena, first, benchmark, structurally, evaluate, performance, safety, VLAs, address | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | dimension, evaluates, model, ability, only, complete, primary, objective, while, adhering | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3. Task Suites in VLA-Arena - extractive body cue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models 0.0 0.25 0.5 0.75 1.0 Success Rate StatePreservation L0 OpenVLA OpenVLA-OFT Pi0 UniVLA L1 L2 L0 L1 ...
- **p. 1 / 2 Supported Trajectory - extractive body cue:** Collection Methods Smooth Conversion among Data Formats Specify Goal: Lemon on the Bowl (c) Open-source Framework for VLA-Arena Language Command Perturbation Visual Observation Perturbation edible ...
- **p. 1 / Abstract - extractive body cue:** It features a novel structured task design framework to quantify difficulty across three orthogonal axes: (1) Task Structure, (2) Language Command, and (3) Visual Observation.
- **p. 3 / 1. Introduction - extractive body cue:** Perturbation Dims: Lighting, Camera pose, Object Color, Language instructions, and Visual Noise.
- **p. 3 / 1. Introduction - extractive body cue:** Orthogonal to this, the task-independent language command (W0-W4) and visual observation (V0-V4) axes introduce graded perturbations to tasks for diagnostic probing.
- **p. 4 / 2. Structured Task Design - extractive body cue:** V3 = V2 + camera position perturbations. • Level 4 (V4) Visual Noise: The final level tests the model's resilience to imperfect sensor data by ...
- **p. 2 / 1. Introduction - extractive body cue:** Vision-Language-Action models (VLAs) aim to build generalist robot control policies (Brohan et al., 2022; Ma et al., 2024; Zhong et al., 2025a; Reed et al., ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Autoregressive VLAs: OpenVLA (Kim et al., 2024) tokenizes continuous actions into discrete bins per timestep. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Despite mastering atomic skills on L0 tasks, models struggle when language requires adapting these skills to novel contexts (i.e., Extrapolation) or sequences ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | The results are calculated as the average over 30 evaluation episodes, with 10 episodes per seed. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1. Introduction - extractive body cue:** Conducting an extensive study on VLA-Arena with leading models from the two dominant architectural paradigms: autoregressive and continuous action generation, our analysis surfaces three key ...
- **p. 2 / 1. Introduction - extractive body cue:** By stressing models with these structured perturbations, we expose latent fragilities and determine whether models rely on robust grounding or fragile memorization of training patterns.
- **p. 6 / 3. Task Suites in VLA-Arena - extractive body cue:** Models are first trained on a vocabulary of foundational skills (L0).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Conducting, extensive, study, VLA-Arena, leading, models, dominant, architectural, paradigms, autoregressive, continuous, action, generation, analysis, surfaces, three, findings, reliance, memorization, over.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | To facilitate reproducible fine-tuning, we introduce curated datasets derived from human demonstrations. | p. 7 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup) |
| Baseline harness | In Table 2, a crossmodel comparison indicates that π0 generally outperforms the other models. | p. 7 (4.2. Analysis of Performance and Failure Modes), p. 6 (4.1. Experimental Setup) |
| Metric / failure reporting | Second, without explicit safety constraints, models prioritize task completion, often incurring high CC to achieve success. | p. 7 (4.2. Analysis of Performance and Failure Modes), p. 7 (4.1. Experimental Setup) |

## Failure and Ablation Link

- **p. 43 / Figure/Table caption - extractive body cue:** Table 30. OpenVLA-OFT Fine-tuning Hyperparameters. H.3.5. OPENVLA-OFT TRAINING PARAMETERS The OpenVLA-OFT model was fine-tuned using LoRA. The training utilized 7 devices, resulting in a total ...
- **p. 42 / Figure/Table caption - extractive body cue:** Table 29. π0 Fine-tuning Hyperparameters. The π0 model was fine-tuned for 60k steps, which utilizes LoRA for memory efficiency. The backbone variants were specified as ...
- **p. 7 / 4.2. Analysis of Performance and Failure Modes - extractive body cue:** Unexpectedly, they show less sensitivity to Table 4.
- **p. 7 / 4.3. Diagnosing Semantic and Visual Grounding - extractive body cue:** Notably, π0 and OpenVLA-OFT maintain partial functionality on V4, suggesting dual-input views aid invariant grounding.
- **p. 41 / Figure/Table caption - extractive body cue:** Table 27. UniVLA Fine-tuning Hyperparameters. The training of UniVLA utilized a batch size of 8 per device and employed 2 gradient accumulation steps, resulting in ...
- **p. 41 / Figure/Table caption - extractive body cue:** Table 26. OpenVLA Fine-tuning Hyperparameters. The OpenVLA model was fine-tuned using Low-Rank Adaptation (LoRA). The training was distributed across 8 GPUs, resulting in a total ...
- **p. 8 / 4.3. Diagnosing Semantic and Visual Grounding - extractive body cue:** Impact of Language on VLA-Arena and LIBERO. ting: fine-tuning causes the model to abandon generalizable concepts, overfitting specific pixel distributions rather than retaining robust representations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (1. Introduction), p. 6 (3. Task Suites in VLA-Arena), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Structured Task Design), p. 4 (2. Structured Task Design), objective p. 5 (3. Task Suites in VLA-Arena), p. 1 (170 Tasks), p. 2 (Abstract), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction), temporal p. 6 (4.1. Experimental Setup), p. 7 (4.2. Analysis of Performance and Failure Modes), p. 2 (1. Introduction), p. 6 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup), p. 9 (5. Real-Robot Validation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
