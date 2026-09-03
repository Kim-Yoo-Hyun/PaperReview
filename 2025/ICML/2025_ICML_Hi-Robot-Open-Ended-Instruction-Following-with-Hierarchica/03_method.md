# Method - Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lNVHg9npif; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/165445. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (5.1. Tasks and Baseline Methods), p. 7 (5.1. Tasks and Baseline Methods), p. 5 (4.3. Data Collection and Training Hi Robot), p. 6 (5.1. Tasks and Baseline Methods), p. 7 (5.1. Tasks and Baseline Methods), p. 4 (4.2. Incorporating User Interaction)): The training data consists of full table cleaning episodes.

## Method Body Digest

- **p. 5 / 5.1. Tasks and Baseline Methods - extractive body cue:** The training data consists of full table cleaning episodes.
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** Flat VLA with synthetic data: This ablation uses the π0 low-level policy by itself, without a high-level model, but includes the synthetic data in the ...
- **p. 5 / 4.3. Data Collection and Training Hi Robot - extractive body cue:** To train the low-level policy plo(At/I1 t, ..., In t , ˆℓt, qt), we use Dlabeled ∪Ddemo using a flow-matching objective, following Black et al.
- **p. 6 / 5.1. Tasks and Baseline Methods - extractive body cue:** This requires the high-level model to reason about the task and each object (e.g., recognizing that reusable plastic cups are dishes, while paper cups are ...
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** GPT-4o high-level model: This method uses the same high-level/low-level decomposition as Hi Robot, but queries the GPT-4o API-based model for the high level, while using ...
- **p. 4 / 4.2. Incorporating User Interaction - extractive body cue:** When ut is included, we use a text to speech system to play the utterance to the user, and remove it from ˆℓt before passing ...
- **p. 6 / 5.1. Tasks and Baseline Methods - extractive body cue:** All images are from policy rollouts. tively alter the goal of the task, such as "can you clean up only the trash, but not dishes?", ...
- **p. 5 / 4.3. Data Collection and Training Hi Robot - extractive body cue:** We train the high-level policy phi(ˆℓt/I1 t, ..., In t , ℓt) on Dsyn ∪Dlabeled using the cross-entropy loss for nexttoken prediction.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during task ...
- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of our paper is a hierarchical interactive robot learning system (Hi Robot), a novel framework that uses VLMs for both high-level reasoning ...
- **p. 5 / 5.1. Tasks and Baseline Methods - extractive body cue:** The training data consists of full table cleaning episodes.

## Source Evidence Cues

- **p. 5 / 5.1. Tasks and Baseline Methods - extractive body cue:** The training data consists of full table cleaning episodes.
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** Flat VLA with synthetic data: This ablation uses the π0 low-level policy by itself, without a high-level model, but includes the synthetic data in the ...
- **p. 5 / 4.3. Data Collection and Training Hi Robot - extractive body cue:** To train the low-level policy plo(At/I1 t, ..., In t , ˆℓt, qt), we use Dlabeled ∪Ddemo using a flow-matching objective, following Black et al.
- **p. 6 / 5.1. Tasks and Baseline Methods - extractive body cue:** This requires the high-level model to reason about the task and each object (e.g., recognizing that reusable plastic cups are dishes, while paper cups are ...
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** GPT-4o high-level model: This method uses the same high-level/low-level decomposition as Hi Robot, but queries the GPT-4o API-based model for the high level, while using ...
- **p. 4 / 4.2. Incorporating User Interaction - extractive body cue:** When ut is included, we use a text to speech system to play the utterance to the user, and remove it from ˆℓt before passing ...
- **p. 6 / 5.1. Tasks and Baseline Methods - extractive body cue:** All images are from policy rollouts. tively alter the goal of the task, such as "can you clean up only the trash, but not dishes?", ...
- **Detected method headings:** 4.4. Model Architecture and Implementation (p. 5); 5.1. Tasks and Baseline Methods (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The training data consists of full table cleaning episodes. | p. 5 (5.1. Tasks and Baseline Methods), p. 7 (5.1. Tasks and Baseline Methods) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Flat VLA with synthetic data: This ablation uses the π0 low-level policy by itself, without a high-level model, but includes the synthetic ... | p. 7 (5.1. Tasks and Baseline Methods), p. 5 (4.3. Data Collection and Training Hi Robot) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To train the low-level policy plo(At/I1 t, ..., In t , ˆℓt, qt), we use Dlabeled ∪Ddemo using a flow-matching objective, following ... | p. 5 (4.3. Data Collection and Training Hi Robot), p. 6 (5.1. Tasks and Baseline Methods) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.3. Data Collection and Training Hi Robot - extractive body cue:** We train the high-level policy phi(ˆℓt/I1 t, ..., In t , ℓt) on Dsyn ∪Dlabeled using the cross-entropy loss for nexttoken prediction.
- **p. 5 / 4.3. Data Collection and Training Hi Robot - extractive body cue:** To train the low-level policy plo(At/I1 t, ..., In t , ˆℓt, qt), we use Dlabeled ∪Ddemo using a flow-matching objective, following Black et al.
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models Average Grocery Shopping Sandwich Making 100 80 60 40 20 0 Table Bussing TASK PROGRESS Instruction ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (4.3. Data Collection and Training Hi Robot), p. 5 (4.3. Data Collection and Training Hi Robot).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | provide, state-of-the-art, vision-language, model, robot, observation, target, atomic, command, come, prompt, human, interaction, have | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | provide, state-of-the-art, vision-language, model, robot, observation, target, atomic, command, come | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | framework, enables, robot, process, much, more, complex, prompts, prior, end-to-end | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | train, high-level, policy, t/I1, Dsyn, Dlabeled, cross-entropy, loss, nexttoken, prediction | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we provide a state-of-the-art vision-language model with a robot observation and target atomic command, and ask it to come up with a ...
- **p. 4 / 3. Preliminaries and Problem Statement - extractive body cue:** We build on the π0 VLA (Black et al., 2024), which additionally handles multiple images and continuous state observations qt, and modifies the VLM to ...
- **p. 3 / 3. Preliminaries and Problem Statement - extractive body cue:** A learned policy controls a robot by processing observation inputs, which we denote ot, and producing one or more actions At = [at, at+1, ..., ...
- **p. 4 / 3. Preliminaries and Problem Statement - extractive body cue:** The low-level policy uses these commands, images, and robot states to produce actions and optionally verbal responses. cretization.
- **p. 5 / 4.2. Incorporating User Interaction - extractive body cue:** The resulting dataset is used to train the high-level policy, which maps image observations and user commands to verbal responses and skill labels. ground feedback ...
- **p. 2 / 1. Introduction - extractive body cue:** In our system, the robot incorporates complex prompts and language feedback using a VLM, which is tasked with interpreting the current observations and user utterances, ...
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** Flat VLA: This comparison directly uses the same π0 lowlevel policy as in Hi Robot, but without any high level or synthetic data, representing a ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The most commonly used VLMs represent p(ℓ′/I, ℓ) via an autoregressive decoder-only Transformer model, factorizing the distribution into a product of autoregressive ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Hi Robot enables robots to follow multi-stage instructions, adapt to real-time corrections and constraints, complete unseen long-horizon tasks, and respond verbally when ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Each evaluation consists of 20 trials per task per method. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 5.1. Tasks and Baseline Methods - extractive body cue:** The training data consists of full table cleaning episodes.
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** Flat VLA with synthetic data: This ablation uses the π0 low-level policy by itself, without a high-level model, but includes the synthetic data in the ...
- **p. 5 / 4.3. Data Collection and Training Hi Robot - extractive body cue:** To train the low-level policy plo(At/I1 t, ..., In t , ˆℓt, qt), we use Dlabeled ∪Ddemo using a flow-matching objective, following Black et al.
- **p. 6 / 5.1. Tasks and Baseline Methods - extractive body cue:** All images are from policy rollouts. tively alter the goal of the task, such as "can you clean up only the trash, but not dishes?", ...
- **p. 4 / 4.2. Incorporating User Interaction - extractive body cue:** When the system receives a user intervention, the high-level inference is triggered immediately to recompute ˆℓt.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, data, consists, full, table, cleaning, episodes, Flat, VLA, synthetic, ablation, uses, low-level, policy, itself, without, high-level, model, includes, still.
- **Relevant PDF headings:** 4.4. Model Architecture and Implementation (p. 5); 5.1. Tasks and Baseline Methods (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Task progress quantifies how closely the robot matches the intended goal and is computed by the proportion of objects that are successfully ... | p. 8 (5.2. Metrics and Evaluation Protocol), p. 8 (5.2. Metrics and Evaluation Protocol) |
| Action / skill decoding | Across all tasks, Hi Robot exhibits substantially higher Instruction Accuracy and Task Progress, compared to GPT4o and the flat baseline. | p. 8 (5.3. Core Results), p. 8 (Figure/Table caption) |
| Receding execution / feedback | Figure 5: Comparisons to Prior Methods. Hi Robot outperforms GPT-4o and flat VLA on Table Bussing, Sandwich Making, and Grocery Shopping. Hi ... | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8: Hierarchical policy vs. flat policy. The hierarchical approach outperforms the flat variant trained on the same data, as it effectively integrates user feedback ...
- **p. 8 / 5.2. Metrics and Evaluation Protocol - extractive body cue:** Without synthetic data, the highlevel policy aligns well with image observations but ignores user constraints. as a correct prediction; otherwise, it is labeled as incorrect.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Ablation on synthetic data. Synthetic data is essential for handling open-ended instructions, as the model trained with- out it struggle with user-driven deviations, ...
- **p. 5 / 4.4. Model Architecture and Implementation - extractive body cue:** The lowlevel policy is the π0 VLA (Black et al., 2024), which is trained by finetuning PaliGemma-3B with an additional flow matching "action expert" to ...
- **p. 9 / 6. Discussion and Future Work - extractive body cue:** Our system also has a number of limitations that could be studied in future work.
- **p. 8 / 5.3. Core Results - extractive body cue:** With human high-level instructions, the lowlevel policy executes nearly flawlessly, showing that failures stem more from reasoning than actuation.
- **p. 9 / 6. Discussion and Future Work - extractive body cue:** Coupling these two layers more directly, e.g. by allowing the high-level policy to be more aware of how successfully the low-level policy completes each command, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (5.1. Tasks and Baseline Methods), p. 7 (5.1. Tasks and Baseline Methods), p. 5 (4.3. Data Collection and Training Hi Robot), p. 6 (5.1. Tasks and Baseline Methods), p. 7 (5.1. Tasks and Baseline Methods), p. 4 (4.2. Incorporating User Interaction), objective p. 5 (4.3. Data Collection and Training Hi Robot), p. 5 (4.3. Data Collection and Training Hi Robot), p. 7 (5.1. Tasks and Baseline Methods), temporal p. 3 (3. Preliminaries and Problem Statement), p. 2 (1. Introduction), p. 5 (5.1. Tasks and Baseline Methods), p. 5 (4.4. Model Architecture and Implementation), p. 6 (5.1. Tasks and Baseline Methods), p. 7 (5.1. Tasks and Baseline Methods).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
