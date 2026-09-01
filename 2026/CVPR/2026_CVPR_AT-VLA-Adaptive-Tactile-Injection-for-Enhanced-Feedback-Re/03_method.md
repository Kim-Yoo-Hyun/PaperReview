# Method - AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Adaptive Tactile Injection), p. 3 (3.1. Framework of AT-VLA), p. 4 (3.1. Framework of AT-VLA), p. 5 (3.3. Effective Tactile Reaction Dual-Stream), p. 5 (3.3. Effective Tactile Reaction Dual-Stream), p. 3 (3.1. Framework of AT-VLA)): Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected and enables the action expert to flexibly handle ...

## Method Body Digest

- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected and enables the ...
- **p. 3 / 3.1. Framework of AT-VLA - extractive body cue:** 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, and left wrist ...
- **p. 4 / 3.1. Framework of AT-VLA - extractive body cue:** To enable the model to handle contact-rich tasks, we introduce an additional tactile encoder.
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** These designs encourage the model to develop a more comprehensive representation of physical dynamics and tactile semantics, bridging instantaneous contact perception and predictive interaction reasoning.
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** We extract the tactile token after the Action Expert module and employ a lightweight decoder network to generate the next-step tactile signal, supervised by an ...
- **p. 3 / 3.1. Framework of AT-VLA - extractive body cue:** The policy then generates an action chunk A, representing the 14-DoF endeffector pose for both arms: A = \ pi _ {\theta }(I, L, T, ...
- **p. 5 / 3.4. Training Objectives and Inference Pipeline - extractive body cue:** All objectives are trained simultaneously, under the overall supervision L = La + λ1 ∗Lg + λ2 ∗Lr, λ1 and λ2 are all both to ...
- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** For supervision, we manually annotate the training episodes by assigning a label of 0 to non-contact frames and 1 to contact frames, and adopt binary ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly ...
- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected and enables the ...
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** Concretely, we propose a Tactile Generation strategy, which enables the model to forecast both the 3D normal and tangential forces for the next time step.

## Source Evidence Cues

- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected and enables the ...
- **p. 3 / 3.1. Framework of AT-VLA - extractive body cue:** 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, and left wrist ...
- **p. 4 / 3.1. Framework of AT-VLA - extractive body cue:** To enable the model to handle contact-rich tasks, we introduce an additional tactile encoder.
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** These designs encourage the model to develop a more comprehensive representation of physical dynamics and tactile semantics, bridging instantaneous contact perception and predictive interaction reasoning.
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** We extract the tactile token after the Action Expert module and employ a lightweight decoder network to generate the next-step tactile signal, supervised by an ...
- **p. 3 / 3.1. Framework of AT-VLA - extractive body cue:** The policy then generates an action chunk A, representing the 14-DoF endeffector pose for both arms: A = \ pi _ {\theta }(I, L, T, ...
- **Detected method headings:** 2.1. Vision Language Action Model (p. 2); 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected ... | p. 4 (3.2. Adaptive Tactile Injection), p. 3 (3.1. Framework of AT-VLA) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, ... | p. 3 (3.1. Framework of AT-VLA), p. 4 (3.1. Framework of AT-VLA) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | To enable the model to handle contact-rich tasks, we introduce an additional tactile encoder. | p. 4 (3.1. Framework of AT-VLA), p. 5 (3.3. Effective Tactile Reaction Dual-Stream) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Training Objectives and Inference Pipeline - extractive body cue:** All objectives are trained simultaneously, under the overall supervision L = La + λ1 ∗Lg + λ2 ∗Lr, λ1 and λ2 are all both to ...
- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** For supervision, we manually annotate the training episodes by assigning a label of 0 to non-contact frames and 1 to contact frames, and adopt binary ...
- **p. 4 / 3.1. Framework of AT-VLA - extractive body cue:** We inherit both its model architecture and its action generation pipeline, where the actions are supervised by the action loss La.
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** We extract the tactile token after the Action Expert module and employ a lightweight decoder network to generate the next-step tactile signal, supervised by an ...
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 5 (3.4. Training Objectives and Inference Pipeline), p. 4 (3.1. Framework of AT-VLA), p. 4 (3.2. Adaptive Tactile Injection), p. 5 (3.3. Effective Tactile Reaction Dual-Stream).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, takes, input, image, observations, head, camera, right, wrist, left, respectively, language, instruction, tactile | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | policy, takes, input, image, observations, head, camera, right, wrist, left | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | main, contributions, follows, Adaptive, Tactile, Injection, making, first, attempt, balance | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | objectives, trained, simultaneously, under, overall, supervision, balance, different, losses, scale | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Framework of AT-VLA - extractive body cue:** 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, and left wrist ...
- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** With the tactile gate to determine when to incorporate tactile feedback, the action expert's architecture must be able to handle inputs under both states of ...
- **p. 2 / 1. Introduction - extractive body cue:** 1, we propose Adaptive Tactile Vision-Language-Action (AT-VLA), which, for the first time, achieves a balance between preserving pretrained capabilities and integrating tactile inputs, while ensuring ...
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we decouple sensory processing into two streams of different frequency: a slow stream, where visual and language inputs are processed through a large Vision-Language ...
- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected and enables the ...
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** For a rapid reaction, we define the input modalities process into two streams: a slow stream operates at a lower inference speed to interpret visual ...
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** Furthermore, to advance the fast stream with an accurate reaction to tactile input, we aim to enhance the model towards a deeper understanding of tactile ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | Building on previous action chunking strategies, the visual and language observation at time step tn can provide guidance for a future horizon ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | Consequently, slow stream's output serves as a latent condition that temporally guides action generation across the following H time steps. | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | Furthermore, to enable rapid and accurate tactile responses, we propose a Tactile Reaction Dual-Stream mechanism, which decouples sensory processing into a slow ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Framework of AT-VLA - extractive body cue:** The tactile encoder is a lightweight module composed of several MLP layers, designed to ensure fast inference while efficiently processing tactile signals.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Therefore, address, issues, Adaptive, Tactile, Injection, module, dynamically, controls, when, where, feedback, injected, enables, action, expert, flexibly, handle, different, gate.
- **Relevant PDF headings:** 2.1. Vision Language Action Model (p. 2); 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | 2) In contrast, VTLA and RDP, which do not have pretrained models on large-scale datasets, are trained only on the subset of ... | p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation) |
| Contact / dynamics inference | Compared with state-of-the-art VLA models GO-1 and π0.5, which are trained without tactile feedback, our model demonstrates comparable performance during the pre-contact ... | p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation) |
| Force-aware action correction | It can reflect how much improvement our method achieves. | p. 5 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study. Each variant selectively removes or changes components to assess their contributions. Components Tactile Format Tasks Tactile Gate Adaptive Cross Attention
- **p. 6 / 4.3. Modality-agnostic Evaluation - extractive body cue:** Modality-agnostic evaluation.The AT-VLA variants with (w/.) and without (w/o.) tactile input share identical model weights, differing only in whether tactile information is provided during inference.
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** Compared with state-of-the-art VLA models GO-1 and π0.5, which are trained without tactile feedback, our model demonstrates comparable performance during the pre-contact manipulation phase, indicating ...
- **p. 5 / 4.1. Setup - extractive body cue:** This task demands precise force and motion coordination to ensure smooth rotation without slipping.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Intuition. We visualize the attention maps in the Action Expert module to examine how the model's attention distribution and action reasoning vary across ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Visualization. We visualize the execution progress of four typical contact-rich tasks. is crucial for real-world robotic applications where sensor failures or missing modalities ...
- **p. 5 / 4.2. Contact-rich Task Evaluation - extractive body cue:** 2. π0.5 [6] is a state-of-the-art VLA model consisting of both pretraining and post-training stages.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Adaptive Tactile Injection), p. 3 (3.1. Framework of AT-VLA), p. 4 (3.1. Framework of AT-VLA), p. 5 (3.3. Effective Tactile Reaction Dual-Stream), p. 5 (3.3. Effective Tactile Reaction Dual-Stream), p. 3 (3.1. Framework of AT-VLA), objective p. 5 (3.4. Training Objectives and Inference Pipeline), p. 4 (3.2. Adaptive Tactile Injection), p. 4 (3.1. Framework of AT-VLA), p. 5 (3.3. Effective Tactile Reaction Dual-Stream), temporal p. 5 (3.3. Effective Tactile Reaction Dual-Stream), p. 5 (3.3. Effective Tactile Reaction Dual-Stream), p. 4 (3.2. Adaptive Tactile Injection), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
