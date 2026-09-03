# Method - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2506.01844; PDF retrieval source: https://arxiv.org/pdf/2506.01844. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract)): In this work, we introduce SmolVLA, an open-source initiative featuring a compact yet capable VLA model, released alongside reproducible and efficient training and inference recipes.

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce SmolVLA, an open-source initiative featuring a compact yet capable VLA model, released alongside reproducible and efficient training and inference recipes.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce an optimized asynchronous inference stack that decouples action execution from observation processing and action prediction, reducing latency and enabling fast, resource-efficient inference.
- **p. 1 / Abstract - extractive body cue:** To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action ...
- **p. 1 / Abstract - extractive body cue:** Self-Attention Self-Attention Self-Attention Cross-Attention Cross-Attention Self-Attention Task: Grasp the object and put it in the bin State Noisy Actions [at ,at+1 … ,at+H] KV KV ...
- **p. 2 / 1 Introduction - extractive body cue:** While encouraging efforts like OpenVLA (Kim et al., 2024) and RT-2-X (O'Neill et al., 2024) demonstrate the feasibility of open VLA systems, they remain large, ...
- **p. 1 / Abstract - extractive body cue:** SmolVLA is pretrained on public community datasets and evaluated on low-cost robots.
- **p. 1 / Abstract - extractive body cue:** However, existing VLAs are typically massive-often with billions of parameters-leading to high training costs and limited real-world deployability.
- **p. 2 / 1 Introduction - extractive body cue:** These models take multimodal inputs-such as visual observations and natural language instructions-and predict the corresponding robotic actions.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We present SmolVLA, a compact and efficient vision-language agent optimized for training on consumer-grade GPUs and deployment on CPUs.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce SmolVLA, an open-source initiative featuring a compact yet capable VLA model, released alongside reproducible and efficient training and inference recipes.
- **p. 1 / Abstract - extractive body cue:** SmolVLA consists of a compact pretrained vision-language model, discarding the last L -N layers (scissors icon).

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce SmolVLA, an open-source initiative featuring a compact yet capable VLA model, released alongside reproducible and efficient training and inference recipes.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce an optimized asynchronous inference stack that decouples action execution from observation processing and action prediction, reducing latency and enabling fast, resource-efficient inference.
- **p. 1 / Abstract - extractive body cue:** To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action ...
- **p. 1 / Abstract - extractive body cue:** Self-Attention Self-Attention Self-Attention Cross-Attention Cross-Attention Self-Attention Task: Grasp the object and put it in the bin State Noisy Actions [at ,at+1 … ,at+H] KV KV ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | In this work, we introduce SmolVLA, an open-source initiative featuring a compact yet capable VLA model, released alongside reproducible and efficient training ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We introduce an optimized asynchronous inference stack that decouples action execution from observation processing and action prediction, reducing latency and enabling fast, ... | p. 2 (1 Introduction), p. 1 (Abstract) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates ... | p. 1 (Abstract), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** While encouraging efforts like OpenVLA (Kim et al., 2024) and RT-2-X (O'Neill et al., 2024) demonstrate the feasibility of open VLA systems, they remain large, ...
- **p. 1 / Abstract - extractive body cue:** SmolVLA is pretrained on public community datasets and evaluated on low-cost robots.
- **p. 1 / Abstract - extractive body cue:** However, existing VLAs are typically massive-often with billions of parameters-leading to high training costs and limited real-world deployability.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce an optimized asynchronous inference stack that decouples action execution from observation processing and action prediction, reducing latency and enabling fast, resource-efficient inference.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | models, take, multimodal, inputs-such, visual, observations, natural, language, instructions-and, predict, corresponding, robotic, actions, remaining | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | models, take, multimodal, inputs-such, visual, observations, natural, language, instructions-and, predict | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | present, SmolVLA, compact, efficient, vision-language, agent, optimized, training, consumer-grade, GPUs | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | While, encouraging, efforts, like, OpenVLA, Kim, RT-2-X, Neill, demonstrate, feasibility | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** These models take multimodal inputs-such as visual observations and natural language instructions-and predict the corresponding robotic actions.
- **p. 1 / Abstract - extractive body cue:** The remaining layers embed three inputs: (i) language instruction, (ii) RGB image(s), and (iii) robot sensorimotor state.
- **p. 1 / Abstract - extractive body cue:** Self-Attention Self-Attention Self-Attention Cross-Attention Cross-Attention Self-Attention Task: Grasp the object and put it in the bin State Noisy Actions [at ,at+1 … ,at+H] KV KV ...
- **p. 2 / 1 Introduction - extractive body cue:** We introduce an optimized asynchronous inference stack that decouples action execution from observation processing and action prediction, reducing latency and enabling fast, resource-efficient inference.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Our model predicts chunks of actions, where each chunk consists of n time steps. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | To ensure compatibility with these optimizations, we maintain a fixed sequence length and batch size, discarding any excess frames in an episode ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | During pretraining, we train for 200,000 steps with a global batch size of 256 on all our community datasets. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce SmolVLA, an open-source initiative featuring a compact yet capable VLA model, released alongside reproducible and efficient training and inference recipes.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce an optimized asynchronous inference stack that decouples action execution from observation processing and action prediction, reducing latency and enabling fast, resource-efficient inference.
- **p. 1 / Abstract - extractive body cue:** To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action ...
- **p. 10 / 4 Experiments - extractive body cue:** During pretraining, we train for 200,000 steps with a global batch size of 256 on all our community datasets.
- **p. 10 / 4 Experiments - extractive body cue:** Pretraining was conducted using 4 GPUs to accomodate for large batch size, but the model can easily be trained on a single GPU due to ...
- **p. 12 / 4 Experiments - extractive body cue:** Inference Time (s) - Real World Total Avg Std Sync 137.5 13.75 2.42 Async 97.0 9.70 2.95 (b) ∣Task completion time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, SmolVLA, open-source, initiative, featuring, compact, capable, VLA, model, released, alongside, reproducible, efficient, training, inference, recipes, optimized, asynchronous, stack, decouples.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | For real-world evaluation, we collected three datasets using the SO-100 robot arm (Knight et al.) and 1 with SO-101 arm (Knight et ... | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Action / skill decoding | SmolVLA outperforms other VLA-based approaches such as Octo (Team et al., 2024) and OpenVLA (Kim et al., 2024), as well as the ... | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Receding execution / feedback | Asynchronous inference achieves similar success rates (left) but is significantly faster (middle) and complete more tasks (right) in fixed-time settings. | p. 12 (4 Experiments), p. 12 (4 Experiments) |

## Failure and Ablation Link

- **p. 11 / 4 Experiments - extractive body cue:** Effect of pretraining and multitask learning.
- **p. 10 / 4 Experiments - extractive body cue:** We also compare against two variants of π0: one initialized from a vision-language model (Paligemma-3B), and another further pretrained on robotics datasets (intitialized from the ...
- **p. 12 / 4 Experiments - extractive body cue:** Unless otherwise noted, models are trained from scratch without any pretraining on robotics data.
- **p. 14 / 4 Experiments - extractive body cue:** We study the effect of varying n on the overall performance.
- **p. 10 / 4 Experiments - extractive body cue:** However, we observe in practice that the model can be trained for a much smaller number of steps without sacrificing significant performance levels.
- **p. 12 / 4 Experiments - extractive body cue:** All ablations are conducted on the LIBERO benchmark.
- **p. 13 / 4 Experiments - extractive body cue:** Further, we also test a variant sampling every second VLM layer (Skip % 2, (Shukor and Cord, 2024))-reducing depth by half while retaining full model ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), objective p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), temporal p. 14 (4 Experiments), p. 10 (4 Experiments), p. 14 (4 Experiments), p. 5 (2 Related work), p. 6 (2 Related work), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Self-Attention Self-Attention Self-Attention Cross-Attention Cross-Attention Self-Attention Task: Grasp the object and put it in the bin State Noisy Actions [at ,at+1 … ,at+H] KV KV QKV Vision-Language Model Action Expert ... (p. 1, Abstract).
- **Objective/update evidence:** SmolVLA is pretrained on public community datasets and evaluated on low-cost robots. (p. 1, Abstract).
- **Temporal/runtime evidence:** To ensure compatibility with these optimizations, we maintain a fixed sequence length and batch size, discarding any excess frames in an episode that do not fit a complete batch. (p. 10, 4 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
