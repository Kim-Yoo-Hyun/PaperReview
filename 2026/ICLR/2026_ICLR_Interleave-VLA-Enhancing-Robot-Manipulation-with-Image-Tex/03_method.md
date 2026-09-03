# Method - Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ULTWUuGhC3; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245105. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling existing VLAs to process interleaved ...

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this limitation, we first build a high-quality interleaved image-text datasets, crucial for training multimodal models.
- **p. 1 / ABSTRACT - extractive body cue:** Building on this insight, we introduce Interleave-VLA, a robot learning paradigm extending interleaved image-text instructions from digital world to directly generating continuous action sequences in ...
- **p. 1 / ABSTRACT - extractive body cue:** It offers a natural, flexible, and model-agnostic paradigm that extends state-of-the-art vision-language-action (VLA) models with minimal modifications while achieving strong zero-shot generalization.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (1) We introduce Interleave-VLA: a lightweight, transferable paradigm that enhances the generalization capability of current text input VLA models with interleaved image-text instructions.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We summarize our key takeaways below: • Generalization failures in VLAs often stem from attentional hallucinations, which we summarized as attentional bias, diffused attention, and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by this progress, the robotic community is actively developing robotic foundation models (Brohan et al., 2023; Kim et al., 2024; O'Neill et al., 2024; ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To develop a general and practical robot policy capable of acting on interleaved image-text instructions in the real world, a straightforward solution is to build ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The interleaved format enables robust zeroshot generalization to novel objects and user-provided sketches unseen during training.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (1) We introduce Interleave-VLA: a lightweight, transferable paradigm that enhances the generalization capability of current text input VLA models with interleaved image-text instructions.

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive body cue:** As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this limitation, we first build a high-quality interleaved image-text datasets, crucial for training multimodal models.
- **p. 1 / ABSTRACT - extractive body cue:** Building on this insight, we introduce Interleave-VLA, a robot learning paradigm extending interleaved image-text instructions from digital world to directly generating continuous action sequences in ...
- **p. 1 / ABSTRACT - extractive body cue:** It offers a natural, flexible, and model-agnostic paradigm that extends state-of-the-art vision-language-action (VLA) models with minimal modifications while achieving strong zero-shot generalization.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (1) We introduce Interleave-VLA: a lightweight, transferable paradigm that enhances the generalization capability of current text input VLA models with interleaved image-text instructions.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We summarize our key takeaways below: • Generalization failures in VLAs often stem from attentional hallucinations, which we summarized as attentional bias, diffused attention, and ...
- **Detected method headings:** A THE USE OF LARGE LANGUAGE MODELS (LLMS) (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To address this limitation, we first build a high-quality interleaved image-text datasets, crucial for training multimodal models. | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Building on this insight, we introduce Interleave-VLA, a robot learning paradigm extending interleaved image-text instructions from digital world to directly generating continuous ... | p. 1 (ABSTRACT), p. 1 (ABSTRACT) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 INTRODUCTION - extractive body cue:** As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by this progress, the robotic community is actively developing robotic foundation models (Brohan et al., 2023; Kim et al., 2024; O'Neill et al., 2024; ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 2 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | develop, general, practical, robot, policy, capable, acting, interleaved, image-text, instructions, real, world, straightforward, solution | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | develop, general, practical, robot, policy, capable, acting, interleaved, image-text, instructions | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | illustrated, Figure, Interleave-VLA, consists, three, components, lightweight, adaptation, module, introduces | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | illustrated, Figure, Interleave-VLA, consists, three, components, lightweight, adaptation, module, introduces | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To develop a general and practical robot policy capable of acting on interleaved image-text instructions in the real world, a straightforward solution is to build ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** (c) It enables flexible, zero-shot instruction following with cropped images, web photos, and hand-drawn sketches for practical and intuitive human-robot interaction.
- **p. 1 / ABSTRACT - extractive body cue:** It offers a natural, flexible, and model-agnostic paradigm that extends state-of-the-art vision-language-action (VLA) models with minimal modifications while achieving strong zero-shot generalization.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We then propose a new paradigm called Interleave-VLA, designed for generating continuous actions from interleaved inputs.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (1) We introduce Interleave-VLA: a lightweight, transferable paradigm that enhances the generalization capability of current text input VLA models with interleaved image-text instructions.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We summarize our key takeaways below: • Generalization failures in VLAs often stem from attentional hallucinations, which we summarized as attentional bias, diffused attention, and ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The resulting interleaved dataset contains over 210k episodes and 13 million frames, making it a large-scale, real-world interleaved embodied dataset. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Formally, a policy πθ under the Interleave-VLA paradigm generates an action at at each timestep t by sampling from a distribution conditioned ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 INTRODUCTION - extractive body cue:** As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this limitation, we first build a high-quality interleaved image-text datasets, crucial for training multimodal models.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We summarize our key takeaways below: • Generalization failures in VLAs often stem from attentional hallucinations, which we summarized as attentional bias, diffused attention, and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** illustrated, Figure, Interleave-VLA, consists, three, components, lightweight, adaptation, module, introduces, special, separator, tokens, tokenizer, enabling, existing, VLAs, process, interleaved, inputs.
- **Relevant PDF headings:** A THE USE OF LARGE LANGUAGE MODELS (LLMS) (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Notably, although the pretraining dataset does not include FANUC robot arm data, it still enables strong cross-embodiment transfer to FANUC. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Action / skill decoding | In contrast, Interleave-VLA outperforms Text-VLA baselines by leveraging in-context visual grounding and cross-modality training to reduce attentional hallucinations. | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Receding execution / feedback | Table 13: Detailed evaluation results on 9 Out-of-Domain generalization tasks based on SimplerEnv. Success rates (%) are reported for π0, Interleave-VLA (adapted ... | p. 27 (Figure/Table caption), p. 10 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Pretraining on the Interleaved X-Embodiment dataset significantly boosts performance through effective crossembodiment transfer, reducing the need for laborious data collection.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Across all four generalization levels, our general Interleave-VLA paradigm, when directly extended to OpenVLA, achieves the best performance without relying on any task-specific designs.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Building on its versatile inference interface, Interleave-VLA further showcases an emergent capability to interpret instructions in a completely zero-shot manner, directly handling unseen input modalities ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** To isolate the contribution of the visual goal signal, we perform an ablation in the SimplerEnvBridge setting (Table 2).
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparing Interleave-VLA with representative VLA methods. Unlike prior systems that depend on fixed backbones, source external Internet or simulation data, and accept only ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Interleave-VLA unlocks powerful zero-shot generalization to diverse instruction modali- ties, including hand-drawn sketches, user-cropped images, and Internet photos, without ever seeing them in ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** It also outperforms π0.5 which enjoys additional pretraining with additonal object grounding and detection VQA data.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), objective p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), temporal p. 2 (1 INTRODUCTION), p. 4 (2 RELATED WORK), p. 6 (2 RELATED WORK), p. 10 (5 CONCLUSION), p. 1 (ABSTRACT), p. 3 (2 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
