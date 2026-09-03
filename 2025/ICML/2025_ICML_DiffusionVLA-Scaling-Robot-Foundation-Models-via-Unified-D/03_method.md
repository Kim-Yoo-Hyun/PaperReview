# Method - DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=VdwdU81Uzy; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/166841. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Methodology), p. 5 (3.2. Model Design Choices), p. 3 (3. Methodology), p. 4 (3.1. Architecture), p. 5 (3.1. Architecture), p. 4 (3.1. Architecture)): In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in Section 3.2.

## Method Body Digest

- **p. 3 / 3. Methodology - extractive body cue:** In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** Because larger models typically needs more data for training, we use OXE and Droid together for pre-training DiVLA-72B.
- **p. 3 / 3. Methodology - extractive body cue:** Developing such an integrated model presents substantial challenges, with key issues centered on: (i) designing an architecture that seamlessly and efficiently integrates both autoregressive and ...
- **p. 4 / 3.1. Architecture - extractive body cue:** If multiple embodiments are evolved, instead of making a copy of a separate action decoder (Octo Model Team et al., 2024), we simply initialized a ...
- **p. 5 / 3.1. Architecture - extractive body cue:** Our reasoning injection module operates by taking the final embedding from the tokenized output of the reasoning component and directly injecting it into the policy ...
- **p. 4 / 3.1. Architecture - extractive body cue:** It is also possible to use any other pre-trained VLM as backbone, since we decouple the vision-language understanding with action generation, making the overall architecture ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** Given a batch of input sequences, the overall training loss is formulated as a combination of the diffusion loss and the next-token prediction (ntp) loss: ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** To balance the contribution of each component to the overall loss, we typically set α = 10 in all experiments.

## Design Rationale

- **p. 3 / 3. Methodology - extractive body cue:** In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose a unified model, named DiffusionVLA (DiVLA in short), that integrates autoregression with a diffusion model.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, we propose a reasoning injection module, which reuses reasoning outputs and embeds them directly into the policy head, thus enriching the ...

## Source Evidence Cues

- **p. 3 / 3. Methodology - extractive body cue:** In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** Because larger models typically needs more data for training, we use OXE and Droid together for pre-training DiVLA-72B.
- **p. 3 / 3. Methodology - extractive body cue:** Developing such an integrated model presents substantial challenges, with key issues centered on: (i) designing an architecture that seamlessly and efficiently integrates both autoregressive and ...
- **p. 4 / 3.1. Architecture - extractive body cue:** If multiple embodiments are evolved, instead of making a copy of a separate action decoder (Octo Model Team et al., 2024), we simply initialized a ...
- **p. 5 / 3.1. Architecture - extractive body cue:** Our reasoning injection module operates by taking the final embedding from the tokenized output of the reasoning component and directly injecting it into the policy ...
- **p. 4 / 3.1. Architecture - extractive body cue:** It is also possible to use any other pre-trained VLM as backbone, since we decouple the vision-language understanding with action generation, making the overall architecture ...
- **Detected method headings:** 3. Methodology (p. 3); 3.1. Architecture (p. 3); 3.2. Model Design Choices (p. 5); 4.4. Behavior Analysis of Robot Foundation Model (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our ... | p. 3 (3. Methodology), p. 5 (3.2. Model Design Choices) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Because larger models typically needs more data for training, we use OXE and Droid together for pre-training DiVLA-72B. | p. 5 (3.2. Model Design Choices), p. 3 (3. Methodology) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Developing such an integrated model presents substantial challenges, with key issues centered on: (i) designing an architecture that seamlessly and efficiently integrates ... | p. 3 (3. Methodology), p. 4 (3.1. Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Model Design Choices - extractive body cue:** Given a batch of input sequences, the overall training loss is formulated as a combination of the diffusion loss and the next-token prediction (ntp) loss: ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** To balance the contribution of each component to the overall loss, we typically set α = 10 in all experiments.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.2. Model Design Choices), p. 5 (3.2. Model Design Choices).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | data, contain, only, robotic, actions, paired, partially, observations, language, instructions, embedding, reasoning, directly, within | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | data, contain, only, robotic, actions, paired, partially, observations, language, instructions | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | section, introduce, overall, framework, explore, design, choices, inform, model, architecture | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Given, batch, input, sequences, overall, training, loss, formulated, combination, diffusion | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.2. Model Design Choices - extractive body cue:** These data contain only robotic actions, paired partially with observations and language instructions.
- **p. 5 / 3.1. Architecture - extractive body cue:** By embedding reasoning directly within the policy model, we avoid the computational and operational complexities of iterative input-output cycles, enabling faster and more seamless reasoning ...
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, we propose a reasoning injection module, which reuses reasoning outputs and embeds them directly into the policy head, thus enriching the ...
- **p. 3 / 3. Methodology - extractive body cue:** Our ultimate goal is to create a unified framework that combines autoregressive models, which excel at predicting language sequences for reasoning, with diffusion models, which ...
- **p. 2 / 1. Introduction - extractive body cue:** 2) Strong action interpretability: Our reasoning injection module provides insights into the end-to-end policy's decision-making, explaining robot actions and facilitating failure analysis.
- **p. 4 / 3.1. Architecture - extractive body cue:** For vision-language processing, we leveraged Qwen2VL (Wang et al., 2024b), a state-of-the-art vision-language model available in three sizes: 2B, 8B, and 72B parameters.
- **p. 4 / 3.1. Architecture - extractive body cue:** It is also possible to use any other pre-trained VLM as backbone, since we decouple the vision-language understanding with action generation, making the overall architecture ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Our ultimate goal is to create a unified framework that combines autoregressive models, which excel at predicting language sequences for reasoning, with ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Among these VLAs, a prominent approach frames action prediction as a next-token prediction (NTP) task, mirroring the dominant autoregressive paradigm in Large ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.2. Model Design Choices - extractive body cue:** Because larger models typically needs more data for training, we use OXE and Droid together for pre-training DiVLA-72B.
- **p. 3 / 3. Methodology - extractive body cue:** Developing such an integrated model presents substantial challenges, with key issues centered on: (i) designing an architecture that seamlessly and efficiently integrates both autoregressive and ...
- **p. 4 / 3.1. Architecture - extractive body cue:** If multiple embodiments are evolved, instead of making a copy of a separate action decoder (Octo Model Team et al., 2024), we simply initialized a ...
- **p. 4 / 3.1. Architecture - extractive body cue:** It is also possible to use any other pre-trained VLM as backbone, since we decouple the vision-language understanding with action generation, making the overall architecture ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We use 2e-5 as a fixed learning rate to train the model, similar to OpenVLA.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** section, introduce, overall, framework, explore, design, choices, inform, model, architecture, Because, larger, models, typically, needs, more, data, training, OXE, Droid.
- **Relevant PDF headings:** 3. Methodology (p. 3); 3.1. Architecture (p. 3); 3.2. Model Design Choices (p. 5); 4.4. Behavior Analysis of Robot Foundation Model (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | (c) Seen Tableware (d) Unseen Tableware (a) Bimanual Robot Setup (b) Setup for Table Bussing (e) Seen Trash (f) Unseen Trash Figure ... | p. 8 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 7 (4.5. Zero-Shot Bin Picking of Unseen Objects) |
| Action / skill decoding | Our method outperforms the state-of-the-art robot foundation models by a large margin. | p. 6 (4. Experiments), p. 5 (Figure/Table caption) |
| Receding execution / feedback | Figure 3: Experimental Results for Factory Sorting. We compared our DiVLA with Diffusion Policy, Octo, TinyVLA, and OpenVLA. DiVLA achieves the highest ... | p. 5 (Figure/Table caption), p. 8 (4.6. Adapt to Real-World Bimanual Robot) |

## Failure and Ablation Link

- **p. 16 / Figure/Table caption - extractive body cue:** Table 8: Ablation study on reasoning injection module. In-Distribution Model \ Tasks Task 1 Task 2 Task 3 Task 4 Task 5
- **p. 16 / Figure/Table caption - extractive body cue:** Table 7: Ablation study on OpenVLA using one camera view and three camera views. For a fair comparison, our main experi- ments evaluate OpenVLA using ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We apply LoRA on VLM for fine-tuning.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We use LoRA (Hu et al., 2021) to fine-tune the VLM models.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 10: Multi-task Learning and Visual Generalization. We evaluate each method on multi-task learning and visual generalizations, including adding additional distractors, changing the background, and ...
- **p. 7 / 4.4. Behavior Analysis of Robot Foundation Model - extractive body cue:** Failure case analysis via self-generated reasoning.
- **p. 8 / 5. Conclusion - extractive body cue:** Additionally, we show that DiVLA has robust generalization capabilities, adapting effectively to new instructions, tasks, and environments.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Methodology), p. 5 (3.2. Model Design Choices), p. 3 (3. Methodology), p. 4 (3.1. Architecture), p. 5 (3.1. Architecture), p. 4 (3.1. Architecture), objective p. 5 (3.2. Model Design Choices), p. 5 (3.2. Model Design Choices), temporal p. 3 (3. Methodology), p. 2 (1. Introduction), p. 3 (3.1. Architecture), p. 4 (3.1. Architecture), p. 5 (3.2. Model Design Choices), p. 7 (4.4. Behavior Analysis of Robot Foundation Model).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
