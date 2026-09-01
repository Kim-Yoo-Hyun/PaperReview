# Method - TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=b1CVu9l5GO; PDF retrieval source: https://openreview.net/pdf/cc4b18989f84e02c6b06df8b480b7156ad8ee1ee.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (2 PRELIMINARIES), p. 1 (ABSTRACT), p. 4 (2 PRELIMINARIES), p. 2 (1 INTRODUCTION), p. 3 (2 PRELIMINARIES), p. 4 (2 PRELIMINARIES)): The learning architecture comprises a visual encoder Fϕ, mapping image observations oi to features zi = Fϕ(oi), and a policy network πθ outputting action distributions ˆa ∼πθ(·/z, s).

## Method Body Digest

- **p. 3 / 2 PRELIMINARIES - extractive PDF cue:** The learning architecture comprises a visual encoder Fϕ, mapping image observations oi to features zi = Fϕ(oi), and a policy network πθ outputting action distributions ...
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatialtemporal awareness for action prediction by encoding state-action ...
- **p. 4 / 2 PRELIMINARIES - extractive PDF cue:** These visual traces are then visually overlaid on the robot's original observations, serving as visual prompts that provide the model with a spatial memory of ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** A separator token is then inserted between the visual tokens of these two images, then concatenating with text tokens and feeding into the underlying vision ...
- **p. 3 / 2 PRELIMINARIES - extractive PDF cue:** These discrete actions are then incorporated into the language model's vocabulary, often replacing the least frequently used tokens.
- **p. 4 / 2 PRELIMINARIES - extractive PDF cue:** At any given timestep t and a time window budget N, we first extract a set of dense point trajectories, P, from a sequence of ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** To address this, we propose explicitly computing multi-point temporal trajectories and overlaying them directly onto the image inputs for VLA models.
- **p. 3 / 2 PRELIMINARIES - extractive PDF cue:** During VLM training, the model is trained end-to-end with a next text token prediction objective on paired or interleaved vision and language data curated from ...

## Design Rationale

- **p. 1 / ABSTRACT - extractive PDF cue:** To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-XEmbodiment and ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We introduce visual trace prompting, a novel technique that significantly enhances VLA models' spatial-temporal reasoning in manipulation tasks. • Dataset & models.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We introduce TraceVLA, a 7B-parameter VLA model fine-tuned from OpenVLA using our novel visual trace prompting dataset, which includes 150K robot manipulation trajectories as shown ...

## Source Evidence Cues

- **p. 3 / 2 PRELIMINARIES - extractive PDF cue:** The learning architecture comprises a visual encoder Fϕ, mapping image observations oi to features zi = Fϕ(oi), and a policy network πθ outputting action distributions ...
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatialtemporal awareness for action prediction by encoding state-action ...
- **p. 4 / 2 PRELIMINARIES - extractive PDF cue:** These visual traces are then visually overlaid on the robot's original observations, serving as visual prompts that provide the model with a spatial memory of ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** A separator token is then inserted between the visual tokens of these two images, then concatenating with text tokens and feeding into the underlying vision ...
- **p. 3 / 2 PRELIMINARIES - extractive PDF cue:** These discrete actions are then incorporated into the language model's vocabulary, often replacing the least frequently used tokens.
- **p. 4 / 2 PRELIMINARIES - extractive PDF cue:** At any given timestep t and a time window budget N, we first extract a set of dense point trajectories, P, from a sequence of ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** To address this, we propose explicitly computing multi-point temporal trajectories and overlaying them directly onto the image inputs for VLA models.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The learning architecture comprises a visual encoder Fϕ, mapping image observations oi to features zi = Fϕ(oi), and a policy network πθ ... | p. 3 (2 PRELIMINARIES), p. 1 (ABSTRACT) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatialtemporal awareness for action prediction ... | p. 1 (ABSTRACT), p. 4 (2 PRELIMINARIES) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | These visual traces are then visually overlaid on the robot's original observations, serving as visual prompts that provide the model with a ... | p. 4 (2 PRELIMINARIES), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2 PRELIMINARIES - extractive PDF cue:** During VLM training, the model is trained end-to-end with a next text token prediction objective on paired or interleaved vision and language data curated from ...
- **p. 3 / 2 PRELIMINARIES - extractive PDF cue:** The cross-entropy loss focuses specifically on the predicted action tokens.
- **p. 5 / 1. We then identify - extractive PDF cue:** This approach ensures that for each timestep t > N, at least N steps of historical context are available, while significantly reducing computational costs.
- **p. 5 / 1. We then identify - extractive PDF cue:** Additionally, the 4B Phi3V-based VLA model will also provide the community with a more compact VLA model for finetuning compared to the larger 7B Prismatic ...
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatialtemporal awareness for action prediction by encoding state-action ...
- **p. 4 / 1. We then identify - extractive PDF cue:** For each training example, with probability α, we replace the visual trace prompt image with the original image and remove the corresponding hint from the ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (2 PRELIMINARIES), p. 3 (2 PRELIMINARIES), p. 5 (1. We then identify).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | VISUAL, TRACE, PROMPTING, Multi-Point, Tracking, Initial, State, Final, Generation, Original, Image, User, inputs, Language | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | VISUAL, TRACE, PROMPTING, Multi-Point, Tracking, Initial, State, Final, Generation, Original | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | further, validate, effectiveness, generality, present, compact, VLA, model, Phi-3-Vision, pretrained | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | During, VLM, training, model, trained, end-to-end, next, text, token, prediction | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2 PRELIMINARIES - extractive PDF cue:** 3.1 VISUAL TRACE PROMPTING Multi-Point Tracking Initial State Final State Visual Trace Prompting Visual Trace Generation Original Image 🧑💻 User: [Prompting for visual inputs] - ...
- **p. 3 / 2 PRELIMINARIES - extractive PDF cue:** The learning architecture comprises a visual encoder Fϕ, mapping image observations oi to features zi = Fϕ(oi), and a policy network πθ outputting action distributions ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Text Tokenizer Image Tokenizer Action Tokens Prompting with Task Language Instructions You are given two images: one with the original robot observation, and another one ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** We posit that this limitation arises because simply mapping image inputs as current states to control actions is insufficient.
- **p. 4 / 1. We then identify - extractive PDF cue:** As shown in Figure 1, we adjust the text prompt to inform the VLA model of this additional visual input before requesting the appropriate action ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** A separator token is then inserted between the visual tokens of these two images, then concatenating with text tokens and feeding into the underlying vision ...
- **p. 4 / 2 PRELIMINARIES - extractive PDF cue:** These visual traces are then visually overlaid on the robot's original observations, serving as visual prompts that provide the model with a spatial memory of ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | This performance drop is likely due to redundant information between visual tokens at different timesteps, which may distract the model from focusing ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | For the 40 × 40 dense point tracking, as it requires recalculation only every 20 steps, the average time cost per timestep ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For the 40 × 40 dense point tracking, as it requires recalculation only every 20 steps, the average time cost per timestep ... | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** For evaluating memory cost, we launch a single-node multi-gpu training job with 8 H100 graphics cards under varying batch sizes, and we measure the maximum ...
- **p. 10 / 4 EXPERIMENT - extractive PDF cue:** (Right): Comparison of inference time across different models.
- **p. 5 / 1. We then identify - extractive PDF cue:** Additionally, we pretrained a 4B VLA model with Phi3-Vision as its backbone VLM (Abdin et al., 2024a), on the Open X-Embodiment dataset using a batch ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** learning, architecture, comprises, visual, encoder, mapping, image, observations, features, policy, network, outputting, action, distributions, introduce, trace, prompting, simple, effective, facilitate.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We design 8 real-world robot tasks with different manipulation skills and objects including 4 unseen tasks for generalization evaluation. | p. 7 (4 EXPERIMENT), p. 5 (4 EXPERIMENT) |
| Action / skill decoding | Table 1: Performance results on three SimplerEnv Google robot tasks under two evaluation metrics: visual matching and variant aggregation. Overall performance is ... | p. 6 (Figure/Table caption), p. 7 (4 EXPERIMENT) |
| Receding execution / feedback | Table 1: Performance results on three SimplerEnv Google robot tasks under two evaluation metrics: visual matching and variant aggregation. Overall performance is ... | p. 6 (Figure/Table caption), p. 6 (4 EXPERIMENT) |

## Failure and Ablation Link

- **p. 5 / 4 EXPERIMENT - extractive PDF cue:** Our simulation evaluation utilizes SimplerEnv, which incorporates two distinct settings: visual matching and variant aggregation.
- **p. 5 / 4 EXPERIMENT - extractive PDF cue:** Complementing this, the variant aggregation setting covers a wide range of environmental variations as shown in Figure 4, including backgrounds from different rooms, lighter and ...
- **p. 6 / 4 EXPERIMENT - extractive PDF cue:** Numbers are averaged across the visual matching and variant aggregation metrics.
- **p. 6 / 4 EXPERIMENT - extractive PDF cue:** These results suggest that the visual trace prompting technique employed in TraceVLA enhances the model's ability to generalize across different robotic manipulation tasks and environmental ...
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** 4.3 ABLATION STUDIES To analyze the performance gain from visual trace prompting, we further study the following questions.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** To answer this, we also tested the performance of the 7B OpenVLA and 4B OpenVLA-Phi3 models finetuned on the exact same dataset as ours, but ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** As shown in Figure 10 (left), when the batch size is 32, the memory difference between TraceVLA and models without visual trace prompting (for both ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (2 PRELIMINARIES), p. 1 (ABSTRACT), p. 4 (2 PRELIMINARIES), p. 2 (1 INTRODUCTION), p. 3 (2 PRELIMINARIES), p. 4 (2 PRELIMINARIES), objective p. 3 (2 PRELIMINARIES), p. 3 (2 PRELIMINARIES), p. 5 (1. We then identify), p. 5 (1. We then identify), p. 1 (ABSTRACT), p. 4 (1. We then identify), temporal p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 4 (1. We then identify), p. 4 (2 PRELIMINARIES).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
