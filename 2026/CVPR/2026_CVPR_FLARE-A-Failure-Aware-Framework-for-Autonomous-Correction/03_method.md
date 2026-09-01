# Method - FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 5 (3.4. Unified Training and Closed-Loop Inference), p. 5 (3.4. Unified Training and Closed-Loop Inference)): Following modern VLA architectures [4, 15, 18], the policy is Markovian-lacking history-and predicts an action chunk at based on the current visual observation ot ∈O and language instruction I.

## Method Body Digest

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Following modern VLA architectures [4, 15, 18], the policy is Markovian-lacking history-and predicts an action chunk at based on the current visual observation ot ∈O ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This policy, which outputs a distribution over action sequences at ∈AK (where K is the chunk length and A is the action space), is written ...
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** Instead of training a single, monolithic model prone to task interference, we adopt a modular and scalable expert policy library approach.
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** Training an Expert Policy Library Our unified training dataset, comprising Dtask aug (original and "retryaugmented" task data) and Dreset aug (all augmented "reset" skill data), ...
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** For example, the "reset cup" adapter is trained exclusively on its corresponding reset demonstrations, using the prompt Ireset = "reset the cup." This modular approach ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** An ID Error is a state st = (se t, sr t) where the environment state is valid (se t ∈Se task), but the robot ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Instead of correctly inferring task progress primarily from the environment state se t (e.g., "the cup is now grasped"), the policy incorrectly learns to associate ...
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** It identifies the required reset skill (e.g., "reset the cup") and directs the control system to swap the active LoRA adapter to the corresponding πreset,j ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose FLARE, a Failure-Aware Retry/Reset framework designed to transform brittle VLAs into resilient embodied agents (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce a perturbation-bridging augmentation strategy that injects random pose perturbations between task segments, followed by a bridging segments that reconnects them.
- **p. 3 / 3. Methodology - extractive body cue:** Our method provides a distinct solution for each case, training a unified VLA system to handle both (Fig.

## Source Evidence Cues

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Following modern VLA architectures [4, 15, 18], the policy is Markovian-lacking history-and predicts an action chunk at based on the current visual observation ot ∈O ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This policy, which outputs a distribution over action sequences at ∈AK (where K is the chunk length and A is the action space), is written ...
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** Instead of training a single, monolithic model prone to task interference, we adopt a modular and scalable expert policy library approach.
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** Training an Expert Policy Library Our unified training dataset, comprising Dtask aug (original and "retryaugmented" task data) and Dreset aug (all augmented "reset" skill data), ...
- **Detected method headings:** 2.2. Vision-Language-Action Models (p. 2); 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Following modern VLA architectures [4, 15, 18], the policy is Markovian-lacking history-and predicts an action chunk at based on the current visual ... | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | This policy, which outputs a distribution over action sequences at ∈AK (where K is the chunk length and A is the action ... | p. 3 (3.1. Problem Formulation), p. 5 (3.4. Unified Training and Closed-Loop Inference) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | Instead of training a single, monolithic model prone to task interference, we adopt a modular and scalable expert policy library approach. | p. 5 (3.4. Unified Training and Closed-Loop Inference), p. 5 (3.4. Unified Training and Closed-Loop Inference) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** For example, the "reset cup" adapter is trained exclusively on its corresponding reset demonstrations, using the prompt Ireset = "reset the cup." This modular approach ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** An ID Error is a state st = (se t, sr t) where the environment state is valid (se t ∈Se task), but the robot ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Instead of correctly inferring task progress primarily from the environment state se t (e.g., "the cup is now grasped"), the policy incorrectly learns to associate ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 5 (3.4. Unified Training and Closed-Loop Inference).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Following, modern, VLA, architectures, policy, Markovian-lacking, history-and, predicts, action, chunk, current, visual, observation, language | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Following, modern, VLA, architectures, policy, Markovian-lacking, history-and, predicts, action, chunk | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | FLARE, Failure-Aware, Retry/Reset, framework, designed, transform, brittle, VLAs, resilient, embodied | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | example, reset, adapter, trained, exclusively, corresponding, demonstrations, prompt, Ireset, modular | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Following modern VLA architectures [4, 15, 18], the policy is Markovian-lacking history-and predicts an action chunk at based on the current visual observation ot ∈O ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This policy, which outputs a distribution over action sequences at ∈AK (where K is the chunk length and A is the action space), is written ...
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** It identifies the required reset skill (e.g., "reset the cup") and directs the control system to swap the active LoRA adapter to the corresponding πreset,j ...
- **p. 1 / 1. Introduction - extractive body cue:** Another line of research employs reinforcement [13, 27, 33, 43] or instruction-based This CVPR paper is the Open Access version, provided by the Computer Vision ...
- **p. 1 / 1. Introduction - extractive body cue:** One direction leverages Multimodal Large Language Models (MLLMs) to provide semantic feedback [25, 37, 38, 41]; these systems can recognize highlevel failures but typically depend ...
- **p. 2 / 1. Introduction - extractive body cue:** Retry addresses ID errors by systematically decoupling robot pose from environment state.
- **p. 2 / 1. Introduction - extractive body cue:** (2) A perturbation-bridging augmentation strategy that decouples robot pose from environment state, equipping VLAs with built-in retry robustness.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | This policy, which outputs a distribution over action sequences at ∈AK (where K is the chunk length and A is the action ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Following modern VLA architectures [4, 15, 18], the policy is Markovian-lacking history-and predicts an action chunk at based on the current visual ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | Following modern VLA architectures [4, 15, 18], the policy is Markovian-lacking history-and predicts an action chunk at based on the current visual ... | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Real-World Task (40 trials) π0.5 (Baseline) Ours (FLARE) Stack Three Blocks 62.5% 75.0% Insert U-shaped Block 45.0% 55.0% Figure 3. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** Instead of training a single, monolithic model prone to task interference, we adopt a modular and scalable expert policy library approach.
- **p. 5 / 3.4. Unified Training and Closed-Loop Inference - extractive body cue:** Training an Expert Policy Library Our unified training dataset, comprising Dtask aug (original and "retryaugmented" task data) and Dreset aug (all augmented "reset" skill data), ...
- **p. 6 / 4. Experiment - extractive body cue:** We fine-tuned the language model and action expert of π0.5 [15] using LoRA [14], training with the Adam optimizer at a constant learning rate of ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Following, modern, VLA, architectures, policy, Markovian-lacking, history-and, predicts, action, chunk, current, visual, observation, language, instruction, outputs, distribution, over, sequences, where.
- **Relevant PDF headings:** 2.2. Vision-Language-Action Models (p. 2); 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | Real-world Validation To verify FLARE's effectiveness and address concerns about privileged simulation states, we conducted real-world experiments on a Piper arm with ... | p. 7 (4. Experiment), p. 6 (4. Experiment) |
| Filtering / recovery | More notably, our method even outperforms Phoenix-Human, demonstrating the comprehensive advantage of our framework over prior selfreflection approaches-even when compared to a ... | p. 6 (4. Experiment), p. 7 (4. Experiment) |
| Monitoring / re-entry | Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do ... | p. 6 (Figure/Table caption), p. 6 (4. Experiment) |

## Failure and Ablation Link

- **p. 7 / 5.2. Ablations and Analysis for Reset skills learning - extractive body cue:** To assess the necessity of this component, we ablate the reset skill entirely and also evaluate a variant of our framework that replaces the multimodal ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. The performance comparison for our method and two variants, Ours w/o Reset and Ours-Oracle. Ours w/o Reset only applies the perturbation & bridging ...
- **p. 6 / 4. Experiment - extractive body cue:** We fine-tuned the language model and action expert of π0.5 [15] using LoRA [14], training with the Adam optimizer at a constant learning rate of ...
- **p. 6 / 4. Experiment - extractive body cue:** We attribute this to the decoupling effect of our perturbation-and-bridging strategy, which enhances the VLA model's robustness to environmental variations.
- **p. 7 / 5.1. Analysis of Perturbation & Bridging - extractive body cue:** The best performance is achieved when r = 30◦and t = 0.7 in 0 10 20 30 40 50 60 70 80 Rotation Angle (degrees) ...
- **p. 8 / 5.2. Ablations and Analysis for Reset skills learning - extractive body cue:** Task Reset/Retry Reset Object Timestamp Coffee 88% 88% 78% ThreePiece Assembly 96% 78% 66% components: retry/reset classification, reset-object identification, and timestamp identification.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The overall framework of our method. We first collect the failure data with the VLA model trained with regular demonstrations. Then we perform ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 5 (3.4. Unified Training and Closed-Loop Inference), p. 5 (3.4. Unified Training and Closed-Loop Inference), objective p. 5 (3.4. Unified Training and Closed-Loop Inference), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), temporal p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 6 (4. Experiment), p. 6 (4. Experiment), p. 7 (4. Experiment), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
