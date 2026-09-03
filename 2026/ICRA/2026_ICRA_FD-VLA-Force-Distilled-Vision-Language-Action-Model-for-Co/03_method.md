# Method - FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2602.02142. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY)): Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual force signals during training only; (ii) maximize feature-level ...

## Method Body Digest

- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual force signals during ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Rather than directly incorporating the raw force measurements into the VLM, we introduce the Force Distillation Module (FDM) that can predict a latent force representation ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Force Distillation Module (FDM) Our FDM generates a compact, state-aware force representation that can be seamlessly integrated into the VLA pipeline without requiring specialized tactile ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Overall Training Objective The overall objective of our FD-VLA framework combines two complementary components, i.e., a standard policy learning loss and a force-distillation loss, which ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivation The objective of this work is to explore an effective and data-efficient approach to incorporate additional force modality into VLA model for contact-rich manipulation.
- **p. 5 / III. METHODOLOGY - extractive body cue:** Action Expert The action expert πθ is instantiated as a transformer that predicts an action chunk At = [at, ..., at+H-1] conditioned on VLM features ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** We seek a design that integrates force without modifying the pretrained VLM, thereby preserving its semantic alignment while avoiding costly retraining.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Finally, the force distillation is achieved by the alignment between the feature representations from these two branches, where an auxiliary distillation loss is used as ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the main contributions of this work are summarized as follows: • We propose the FD-VLA framework that injects a distilled force token into ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a novel FD-VLA framework that incorporates a distilled force token, rather than raw sensor signals, into the VLA model to ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual force signals during ...

## Source Evidence Cues

- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual force signals during ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Rather than directly incorporating the raw force measurements into the VLM, we introduce the Force Distillation Module (FDM) that can predict a latent force representation ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Force Distillation Module (FDM) Our FDM generates a compact, state-aware force representation that can be seamlessly integrated into the VLA pipeline without requiring specialized tactile ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Overall Training Objective The overall objective of our FD-VLA framework combines two complementary components, i.e., a standard policy learning loss and a force-distillation loss, which ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivation The objective of this work is to explore an effective and data-efficient approach to incorporate additional force modality into VLA model for contact-rich manipulation.
- **p. 5 / III. METHODOLOGY - extractive body cue:** Action Expert The action expert πθ is instantiated as a transformer that predicts an action chunk At = [at, ..., at+H-1] conditioned on VLM features ...
- **Detected method headings:** III. METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual ... | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Rather than directly incorporating the raw force measurements into the VLM, we introduce the Force Distillation Module (FDM) that can predict a ... | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Force Distillation Module (FDM) Our FDM generates a compact, state-aware force representation that can be seamlessly integrated into the VLA pipeline without ... | p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / III. METHODOLOGY - extractive body cue:** Overall Training Objective The overall objective of our FD-VLA framework combines two complementary components, i.e., a standard policy learning loss and a force-distillation loss, which ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** We seek a design that integrates force without modifying the pretrained VLM, thereby preserving its semantic alignment while avoiding costly retraining.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivation The objective of this work is to explore an effective and data-efficient approach to incorporate additional force modality into VLA model for contact-rich manipulation.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Finally, the force distillation is achieved by the alignment between the feature representations from these two branches, where an auxiliary distillation loss is used as ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** We train the action expert with a conditional flow-matching objective, Lτ(θ) = E p(At/Xt), q(Aτ t /At) h
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | multimodal, inputs, VLA, include, language, instruction, visual, observation, robot, state, force, where, denotes, timestamp | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | multimodal, inputs, VLA, include, language, instruction, visual, observation, robot, state | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, main, contributions, summarized, follows, FD-VLA, framework, injects, distilled, force | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Overall, Training, Objective, FD-VLA, framework, combines, complementary, components, standard, policy | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHODOLOGY - extractive body cue:** The multimodal inputs of VLA include language instruction L, visual observation Vt, robot state St, and force Ft, where t denotes the timestamp.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This allows them to map RGB inputs and natural-language instructions directly to low-level robot commands, while benefiting from strong This research is supported by National ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the main contributions of this work are summarized as follows: • We propose the FD-VLA framework that injects a distilled force token into ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** language instruction, and robot proprioceptive state are encoded into their corresponding feature representations f V t ∈ RNv×D, f L ∈RNl×D, and f S t ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Rather than directly incorporating the raw force measurements into the VLM, we introduce the Force Distillation Module (FDM) that can predict a latent force representation ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** The policy learns a velocity field rather than stepwise residuals, which is well suited to chunked action prediction.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual force signals during ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The policy learns a velocity field rather than stepwise residuals, which is well suited to chunked action prediction. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | 2 illustrates the overall framework of the proposed FD-VLA. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual force signals during ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Force Distillation Module (FDM) Our FDM generates a compact, state-aware force representation that can be seamlessly integrated into the VLA pipeline without requiring specialized tactile ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Overall Training Objective The overall objective of our FD-VLA framework combines two complementary components, i.e., a standard policy learning loss and a force-distillation loss, which ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Note that the FDM is trained to align with real force signals f aF ∈R1×D encoded by a projection layer only during the training stage, ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For evaluation, each task was trained using a set of 50 demonstrations and subsequently evaluated over 30 independent test trials to ensure statistical robustness.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Force Distillation Module (FDM) Our FDM generates a compact, state-aware force representation that can be seamlessly integrated into the VLA pipeline without requiring specialized tactile ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Motivated, challenges, FD-VLA, guided, three, design, principles, leverage, predicted, force, tokens, obtained, through, distillation, actual, signals, during, training, only, maximize.
- **Relevant PDF headings:** III. METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Results are averaged over 30 evaluation episodes per task. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Action / skill decoding | DP3 is selected as a strong diffusion-based control framework with a parameter scale comparable to ours, which provides a capacity-matched baseline that ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Receding execution / feedback | Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, substantially outperforming both SmolVLA ... | p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We compare FD-VLA (ours) with SmolVLA, π0 and DP3, SmolVLA and π0 are evaluated with and without force inputs.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In the Press Emergency Button task, success required the button to be fully depressed and remain engaged without rebound.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of our framework. During training, measured force signals are encoded into an actual force token via a lightweight projection. A learnable query ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Visualization of real-world experimental tasks: 1) Clean the whiteboard, 2) Press the emergency button, 3) Insert the plug into the socket. the control ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Visualization of the real robotic platform. We use a UR5e robot arm as the main manipulation platform, the Kinect Azure camera as the ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** This architecture allows our system to leverage the semantic richness of pretrained VLM while introducing stable, taskrelevant physical reasoning through force distillation, achieving both robustness ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), objective p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), temporal p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
