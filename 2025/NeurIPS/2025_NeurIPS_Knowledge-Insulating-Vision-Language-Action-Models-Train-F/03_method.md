# Method - Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=cb0xbZ3APM; PDF retrieval source: https://openreview.net/pdf/a125f5bc144a834ceef1946ec665a202b39c5b8c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract)): While a number of different designs have been successful, a common theme is that models adapted for effective dexterous control typically augment a transformer or VLM backbone with some sort ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive PDF cue:** While a number of different designs have been successful, a common theme is that models adapted for effective dexterous control typically augment a transformer or ...
- **p. 1 / 1 Introduction - extractive PDF cue:** The success of large language models (LLMs) can be attributed to the availability of large-scale datasets combined with powerful model architectures such as transformers that ...
- **p. 2 / 1 Introduction - extractive PDF cue:** As experiments show, having both action representations at training time is crucial. autoregressive decoding with large models, a challenge only exacerbated by ever larger models.
- **p. 1 / Abstract - extractive PDF cue:** While these modules improve real-time and control capabilities, it remains an open question whether they preserve or degrade the semantic knowledge contained in the pretrained ...
- **p. 2 / 1 Introduction - extractive PDF cue:** 1.7 1.25 3.14 1.42 NOISE ACTION EXPERT (300M) continuous actions -17 12 34 142 autoregressive loss flow matching loss bidirectional w/o loss stop gradient pick ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This approach has additional advantages: first, using next-token prediction makes the model learn much faster and more stably.
- **p. 1 / 1 Introduction - extractive PDF cue:** Autoregressive decoding of discrete tokens is poorly suited to this kind of high-frequency continuous control, both because of the limited resolution of discretized actions and ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Furthermore, physical systems typically produce more complex observations than VLMs are trained for, such as multi-view images and proprioceptive states.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.
- **p. 2 / 1 Introduction - extractive PDF cue:** Second, using an action expert still enables fast inference.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive PDF cue:** While a number of different designs have been successful, a common theme is that models adapted for effective dexterous control typically augment a transformer or ...
- **p. 1 / 1 Introduction - extractive PDF cue:** The success of large language models (LLMs) can be attributed to the availability of large-scale datasets combined with powerful model architectures such as transformers that ...
- **p. 2 / 1 Introduction - extractive PDF cue:** As experiments show, having both action representations at training time is crucial. autoregressive decoding with large models, a challenge only exacerbated by ever larger models.
- **p. 1 / Abstract - extractive PDF cue:** While these modules improve real-time and control capabilities, it remains an open question whether they preserve or degrade the semantic knowledge contained in the pretrained ...
- **Detected method headings:** A.3 Datasets for training the generalist model (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | While a number of different designs have been successful, a common theme is that models adapted for effective dexterous control typically augment ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The success of large language models (LLMs) can be attributed to the availability of large-scale datasets combined with powerful model architectures such ... | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | As experiments show, having both action representations at training time is crucial. autoregressive decoding with large models, a challenge only exacerbated by ... | p. 2 (1 Introduction), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive PDF cue:** 1.7 1.25 3.14 1.42 NOISE ACTION EXPERT (300M) continuous actions -17 12 34 142 autoregressive loss flow matching loss bidirectional w/o loss stop gradient pick ...
- **p. 1 / 1 Introduction - extractive PDF cue:** The success of large language models (LLMs) can be attributed to the availability of large-scale datasets combined with powerful model architectures such as transformers that ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This approach has additional advantages: first, using next-token prediction makes the model learn much faster and more stably.
- **p. 1 / 1 Introduction - extractive PDF cue:** Autoregressive decoding of discrete tokens is poorly suited to this kind of high-frequency continuous control, both because of the limited resolution of discretized actions and ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | While, number, different, designs, have, been, successful, common, theme, models, adapted, effective, dexterous, control | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | While, number, different, designs, have, been, successful, common, theme, models | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | address, challenge, training, recipe, addresses, issues, refer, knowledge, insulation, Second | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | NOISE, ACTION, EXPERT, continuous, actions, autoregressive, loss, flow, matching, bidirectional | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** While a number of different designs have been successful, a common theme is that models adapted for effective dexterous control typically augment a transformer or ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Furthermore, physical systems typically produce more complex observations than VLMs are trained for, such as multi-view images and proprioceptive states.
- **p. 1 / Abstract - extractive PDF cue:** To address this challenge, recent VLA models have used specialized modules for efficient continuous control, such as action experts or continuous output heads, which typically ...
- **p. 1 / 1 Introduction - extractive PDF cue:** A natural next step to bring the power of LLMs to the physical world is to further extend them to take physical actions, resulting in ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | While a number of different designs have been successful, a common theme is that models adapted for effective dexterous control typically augment ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | How fast does our model train in terms of training steps? | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For example, the action expert in the π0 architecture has fewer parameters than the VLM backbone, and hence π0 can achieve a ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / 1 Introduction - extractive PDF cue:** The success of large language models (LLMs) can be attributed to the availability of large-scale datasets combined with powerful model architectures such as transformers that ...
- **p. 2 / 1 Introduction - extractive PDF cue:** As experiments show, having both action representations at training time is crucial. autoregressive decoding with large models, a challenge only exacerbated by ever larger models.
- **p. 1 / Abstract - extractive PDF cue:** While these modules improve real-time and control capabilities, it remains an open question whether they preserve or degrade the semantic knowledge contained in the pretrained ...
- **p. 8 / 6 Experiments - extractive PDF cue:** OpenVLA-OFT follows language well and has low inference time, but has the lowest overall performance. detailed ablation of modeling choices made for our method as ...
- **p. 8 / 6 Experiments - extractive PDF cue:** Our model has the highest performance, low inference time, and follows language instructions well. π0-FAST also follows language well and has good performance, but requires ...
- **p. 10 / 6 Experiments - extractive PDF cue:** Since here we use the discrete action tokens only during training time, one may wonder whether simpler, naive tokenization is sufficient for learning good representations.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** While, number, different, designs, have, been, successful, common, theme, models, adapted, effective, dexterous, control, typically, augment, transformer, VLM, backbone, some.
- **Relevant PDF headings:** A.3 Datasets for training the generalist model (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The robot is tasked with moving objects from a kitchen counter into an (already open) drawer. | p. 9 (6 Experiments), p. 9 (6 Experiments) |
| Action / skill decoding | Our method outperforms all other baselines both in terms of performance and the ability of the model to follow language instructions. | p. 8 (6 Experiments), p. 7 (6 Experiments) |
| Receding execution / feedback | 6a shows that for the "table bussing" task our recipe achieves comparable performance to the embodiment specific results from above. | p. 8 (6 Experiments), p. 10 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 6 Experiments - extractive PDF cue:** This ablation removes both the stop-gradient and cotraining on VLM data from our proposed method, which can also be considered a variant of HybridVLA [33] ...
- **p. 9 / 6 Experiments - extractive PDF cue:** 4b, stopping the gradient flow from the action expert is an effective way of improving language following compared to π0 and joint-training without stop-gradient and ...
- **p. 10 / 6 Experiments - extractive PDF cue:** The core idea in our approach is to use discretized actions to provide a learning signal to fine-tune VLM representations, while simultaneously training a continuous ...
- **p. 7 / 6 Experiments - extractive PDF cue:** What is the effect of stopping the gradient flow?
- **p. 8 / 6 Experiments - extractive PDF cue:** OpenVLA-OFT follows language well and has low inference time, but has the lowest overall performance. detailed ablation of modeling choices made for our method as ...
- **p. 9 / 6 Experiments - extractive PDF cue:** 7, then joint-training without stop-gradient can also achieve good language following.
- **p. 10 / 6 Experiments - extractive PDF cue:** 7 Discussion & Limitations We analyze the performance, generalization, and language following capabilities of continuousaction VLAs that fine-tune VLMs to output continuous actions, show that ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), objective p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), temporal p. 2 (1 Introduction), p. 7 (6 Experiments), p. 7 (6 Experiments), p. 9 (6 Experiments), p. 9 (6 Experiments), p. 5 (2 Related work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
