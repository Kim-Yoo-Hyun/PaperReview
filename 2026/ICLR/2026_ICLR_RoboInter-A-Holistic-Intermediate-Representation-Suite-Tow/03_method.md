# Method - RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (68 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PGUC3mmMoi; PDF retrieval source: https://openreview.net/pdf/c5f8c1cd83b4c3e70c6b81498b10fcef9000dc8b.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR), p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR)): Planner Training Data RoboInter-Spatial RoboInter-Temporal General Grounding General Understanding Simulation Data Embodied Grounding Embodied Understanding Figure 11: Training data distribution for the Planner.

## Method Body Digest

- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** Planner Training Data RoboInter-Spatial RoboInter-Temporal General Grounding General Understanding Simulation Data Embodied Grounding Embodied Understanding Figure 11: Training data distribution for the Planner.
- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** We partially follow the basic VLM training recipe of InternVL (Chen et al., 2024b), and as shown in Figure 11, to ensure that the Planner ...
- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** Training uses BF16 mixed precision, a maximum gradient norm of 1.0, zero weight decay, and a warmup ratio of 0.03.
- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** The RoboInterVLM(QwenVL2.5 7B) Planner is trained for one epoch with a global batch size of 128 and a per-device batch size of 4, without gradient ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** All annotations are temporally synchronized with executed actions and robot states, together with two-view observations (one third-person and one wrist-view camera), enabling end-to-end action learning.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Existing datasets (et al., 2023; Khazatsky et al., 2024) typically pair visual inputs with overall instructions and robot actions, but they rarely provide the fine-grained ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** The remarkable generalization of large language models (LLMs) and vision-language models (VLMs) through large-scale pretraining has inspired efforts to extend this paradigm to robotics, giving ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Prior work leverages 2D trace (Gu et al., 2023), optical flow (Xu et al., 2024), subtasks (Zhang et al., 2024; Belkhale et al., 2024), key ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To address this gap, we propose the RoboInter Manipulation Suite, illustrated in Figure.1.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Built upon the high-level VLM planner trained on these curated VQA data, we introduce RoboInter-VLA, an integrated plan-then-execute framework that supports both modular and end2
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Although web-scale multimodal data enables broad semantic reasoning, existing large-scale robot datasets (et al., 2023; Khazatsky et al., 2024; Wu et al., 2024; Bu et ...

## Source Evidence Cues

- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** Planner Training Data RoboInter-Spatial RoboInter-Temporal General Grounding General Understanding Simulation Data Embodied Grounding Embodied Understanding Figure 11: Training data distribution for the Planner.
- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** We partially follow the basic VLM training recipe of InternVL (Chen et al., 2024b), and as shown in Figure 11, to ensure that the Planner ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Planner Training Data RoboInter-Spatial RoboInter-Temporal General Grounding General Understanding Simulation Data Embodied Grounding Embodied Understanding Figure 11: Training data distribution for the ... | p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR), p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We partially follow the basic VLM training recipe of InternVL (Chen et al., 2024b), and as shown in Figure 11, to ensure ... | p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Planner Training Data RoboInter-Spatial RoboInter-Temporal General Grounding General Understanding Simulation Data Embodied Grounding Embodied Understanding Figure 11: Training data distribution for the ... | p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** Training uses BF16 mixed precision, a maximum gradient norm of 1.0, zero weight decay, and a warmup ratio of 0.03.
- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** The RoboInterVLM(QwenVL2.5 7B) Planner is trained for one epoch with a global batch size of 128 and a per-device batch size of 4, without gradient ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR), p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | annotations, temporally, synchronized, executed, actions, robot, states, together, two-view, observations, third-person, wrist-view, camera, enabling | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | annotations, temporally, synchronized, executed, actions, robot, states, together, two-view, observations | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | address, RoboInter, Manipulation, Suite, illustrated, Figure, Built, upon, high-level, VLM | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Training, uses, BF16, mixed, precision, maximum, gradient, norm, zero, weight | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** All annotations are temporally synchronized with executed actions and robot states, together with two-view observations (one third-person and one wrist-view camera), enabling end-to-end action learning.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Existing datasets (et al., 2023; Khazatsky et al., 2024) typically pair visual inputs with overall instructions and robot actions, but they rarely provide the fine-grained ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** The remarkable generalization of large language models (LLMs) and vision-language models (VLMs) through large-scale pretraining has inspired efforts to extend this paradigm to robotics, giving ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Prior work leverages 2D trace (Gu et al., 2023), optical flow (Xu et al., 2024), subtasks (Zhang et al., 2024; Belkhale et al., 2024), key ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Modular approaches (Huang et al., 2023; Belkhale et al., 2024; Huang et al., 2024a; Liu et al., 2024a; Nasiriany et al., 2024) infer high-level structures ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** RoboInter introduces per-frame dense annotations data across varied intermediate representations to advance both embodied understanding and end-to-end action learning.
- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** Action head, the LLM backbone, and the vision backbone all remain trainable.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Published as a conference paper at ICLR 2026 𝙍𝙤𝙗𝙤𝙄𝙣𝙩𝙚𝙧 𝙍𝙤𝙗𝙤𝙄𝙣𝙩𝙚𝙧-𝘿𝙖𝙩𝙖 𝙍𝙤𝙗𝙤𝙄𝙣𝙩𝙚𝙧-𝙑𝙌𝘼 Transfer General to Robotics 𝙍𝙤𝙗𝙤𝙄𝙣𝙩𝙚𝙧-𝙏𝙤𝙤𝙡 Obj/Gripper Annotation Subtasks Annotation Key Frame ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | A: place the plate on top of the plate on the countertop Past Description Future Primitive Video check Record Video Subset Annotation ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | To accommodate network latency, the control loop is limited to lower than 10 Hz, and demonstrations are collected using a SpaceMouse. | hardware, batch and throughput |

## Training vs Inference

- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** Planner Training Data RoboInter-Spatial RoboInter-Temporal General Grounding General Understanding Simulation Data Embodied Grounding Embodied Understanding Figure 11: Training data distribution for the Planner.
- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** We partially follow the basic VLM training recipe of InternVL (Chen et al., 2024b), and as shown in Figure 11, to ensure that the Planner ...
- **p. 18 / A.1.1 EXPERIMENTAL SETTING - extractive PDF cue:** At inference time, we utilize a shorter CoT (only subtask, affordance box, and gripper box), as well as a caching mechanism that stores slowly varying ...
- **p. 27 / A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR - extractive PDF cue:** The RoboInter-IC-E2E Executor is trained with a global batch size of 128 and a per-device batch size of 8.
- **p. 18 / A.1.1 EXPERIMENTAL SETTING - extractive PDF cue:** (2) π0 (Black et al., 2024): Fine-tuned from the official JAX checkpoints of the Droid dataset.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Planner, Training, Data, RoboInter-Spatial, RoboInter-Temporal, General, Grounding, Understanding, Simulation, Embodied, Figure, distribution, partially, follow, basic, VLM, recipe, InternVL, Chen, ensure.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Our evaluation focuses on a kitchen environment, where we design four manipulation tasks, each executed 15 times: • Pick the Spoon: The ... | p. 26 (A.3.3 CLOSE-LOOP EVALUATION ON REAL-WORLD WIDOWX ROBOT), p. 5 (3 DATASET) |
| Baseline harness | On SimplerEnv, our minimal Vanilla design outperforms common baselines (π0, π0-FAST), though it is slightly below CogACT (61.8 vs. | p. 25 (A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV), p. 25 (A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION) |
| Metric / failure reporting | 60.0%) and achieves a higher average success rate (60.0% vs. | p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 9 (3 DATASET) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 5: Ablation of intermediate representation. We re- port OLS under multiple thresholds. Six representations are evaluated, where finer-grained categories yield larger gains. Variant OLS ...
- **p. 18 / A.1.1 EXPERIMENTAL SETTING - extractive PDF cue:** (3) Vanilla: A from-scratch baseline without a pretrained Planner and without annotated intermediate representations.
- **p. 26 / A.3.3 CLOSE-LOOP EVALUATION ON REAL-WORLD WIDOWX ROBOT - extractive PDF cue:** All models are pretrained on the BridgeV2 without further post-training or finetuning prior to deployment, and all experiments are executed using the same real-world setup.
- **p. 17 / A.2.2 Experiment Results for Data Scaling Law - extractive PDF cue:** 22 A.2.3 Ablation for Designs and Intermediate Representations Types of F-CoT . .
- **p. 18 / A.1.1 EXPERIMENTAL SETTING - extractive PDF cue:** The Modular variant achieves strong real-world performance and competitive out-of-distribution (OOD) generalization.
- **p. 22 / A.2.1 INFERENCE TIME ANALYSIS - extractive PDF cue:** For real-world deployment, we apply practical acceleration strategies, including textual caching and chunked execution for EC-E2E, and asynchronous dual-frequency execution for the Modular variant.
- **p. 25 / A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV - extractive PDF cue:** The GR environment includes two settings, Visual Matching (VM) and Variant Aggregation (VA).

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR), p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR), objective p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR), p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR), temporal p. 2 (1 INTRODUCTION), p. 4 (16 Primitive Skills), p. 2 (1 INTRODUCTION), p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 4 (6 Embodiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
