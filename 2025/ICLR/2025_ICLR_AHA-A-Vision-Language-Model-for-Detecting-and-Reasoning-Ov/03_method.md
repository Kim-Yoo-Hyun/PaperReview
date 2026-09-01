# Method - AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=JVkdSi7Ekg; PDF retrieval source: https://openreview.net/pdf/baa69f167306f963174767be4974c69528aa6379.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (4 Method), p. 10 (4 Method), p. 7 (4 Method), p. 9 (4 Method), p. 6 (4 Method), p. 10 (4 Method)): 2, our model architecture includes an image encoder, a linear projector, a language tokenizer, and a transformerbased language model.

## Method Body Digest

- **p. 7 / 4 Method - extractive body cue:** 2, our model architecture includes an image encoder, a linear projector, a language tokenizer, and a transformerbased language model.
- **p. 10 / 4 Method - extractive body cue:** The PRoC3S system solves tasks specified in natural language by prompting an LLM for a Language-Model Program (LMP) that generates plans, and then testing a ...
- **p. 7 / 4 Method - extractive body cue:** These multimodal tokens are then concatenated and passed through the language transformer.
- **p. 9 / 4 Method - extractive body cue:** The model was then assessed on the ManiSkill-Fail dataset across four evaluation metrics.
- **p. 6 / 4 Method - extractive body cue:** Finally, we detail the instruction fine-tuning pipeline and the model architecture selection for AHA (Sec.4.3).
- **p. 10 / 4 Method - extractive body cue:** Each policy was trained using PPO over task-specific training steps and evaluated across 1,000 test steps.
- **p. 6 / 4 Method - extractive body cue:** For example, in a task like "stacking cubes", a sub-task could represent a primitive action, such as 'picking up the cube'.
- **p. 10 / 4 Method - extractive body cue:** To systematically assess the reasoning capabilities of different VLMs under budget constraints, we sampled one reward function initially and allowed for iterations over two sessions ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce FailGen, a data generation pipeline for the procedural generation of failure demonstration data for robotic manipulation tasks across simulators.
- **p. 7 / 4 Method - extractive body cue:** This structured input enables consistent handling of data across different tasks and viewpoints.

## Source Evidence Cues

- **p. 7 / 4 Method - extractive body cue:** 2, our model architecture includes an image encoder, a linear projector, a language tokenizer, and a transformerbased language model.
- **p. 10 / 4 Method - extractive body cue:** The PRoC3S system solves tasks specified in natural language by prompting an LLM for a Language-Model Program (LMP) that generates plans, and then testing a ...
- **p. 7 / 4 Method - extractive body cue:** These multimodal tokens are then concatenated and passed through the language transformer.
- **p. 9 / 4 Method - extractive body cue:** The model was then assessed on the ManiSkill-Fail dataset across four evaluation metrics.
- **p. 6 / 4 Method - extractive body cue:** Finally, we detail the instruction fine-tuning pipeline and the model architecture selection for AHA (Sec.4.3).
- **p. 10 / 4 Method - extractive body cue:** Each policy was trained using PPO over task-specific training steps and evaluated across 1,000 test steps.
- **p. 6 / 4 Method - extractive body cue:** For example, in a task like "stacking cubes", a sub-task could represent a primitive action, such as 'picking up the cube'.
- **Detected method headings:** 4 Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 2, our model architecture includes an image encoder, a linear projector, a language tokenizer, and a transformerbased language model. | p. 7 (4 Method), p. 10 (4 Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The PRoC3S system solves tasks specified in natural language by prompting an LLM for a Language-Model Program (LMP) that generates plans, and ... | p. 10 (4 Method), p. 7 (4 Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | These multimodal tokens are then concatenated and passed through the language transformer. | p. 7 (4 Method), p. 9 (4 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 10 / 4 Method - extractive body cue:** To systematically assess the reasoning capabilities of different VLMs under budget constraints, we sampled one reward function initially and allowed for iterations over two sessions ...
- **p. 9 / 4 Method - extractive body cue:** This includes automatic reward generation for reinforcement learning applications [17], automatic task plan generation for task and motion planning 9
- **p. 9 / 4 Method - extractive body cue:** An average quadratic fit gradient of 0.0022 across all four metrics demonstrates a scaling effect with fine-tuning on our procedurally generated data pipeline.
- **p. 10 / 4 Method - extractive body cue:** AHA enables efficient reward synthesis for reinforcement learning.
- **p. 7 / 4 Method - extractive body cue:** During fine-tuning, only the projector and transformer weights are updated, while the vision encoder and tokenizer remain frozen.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 9 (4 Method), p. 10 (4 Method), p. 10 (4 Method), p. 7 (4 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | capture, temporal, relationships, within, action, sequence, input, image, constructed, selecting, single, frame, represents, robot | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | capture, temporal, relationships, within, action, sequence, input, image, constructed, selecting | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | introduce, AHA, open-source, vision-language, model, VLM, uses, natural, language, detect | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | systematically, assess, reasoning, capabilities, different, VLMs, under, budget, constraints, sampled | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 4 Method - extractive body cue:** To capture the temporal relationships within the action sequence, the input image was constructed by selecting a single frame that represents the robot's trajectory up ...
- **p. 6 / 4 Method - extractive body cue:** For the input formulation in VLMs for instruction fine-tuning and evaluation, we required a query prompt 6
- **p. 10 / 4 Method - extractive body cue:** Comparing the evaluated policy success rates using different failure feedback VLMs, we observed that AHA-13B provided intuitive, human-level failure reasoning that aided in modifying and ...
- **p. 6 / 4 Method - extractive body cue:** 4.1 Failure Reasoning Formulation Unlike previous works [48, 28, 22] that primarily focus on detecting task success as binary classification problem, we approach failure reasoning ...
- **p. 10 / 4 Method - extractive body cue:** We incorporated a VLM into this pipeline in two ways: (1) we prompt the VLM with visualizations of failed plan executions within the simulator, ask ...
- **p. 7 / 4 Method - extractive body cue:** with an input image for prompting the VLMs.
- **p. 1 / 1 Introduction - extractive body cue:** These models, including large language models (LLMs) and vision-language models (VLMs), have shown proficiency in interpreting and executing human language instructions[5], producing accurate predictions and ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | To capture the temporal relationships within the action sequence, the input image was constructed by selecting a single frame that represents the ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The image data is structured as a matrix I, where each row corresponds to a different camera viewpoint {V0, V1, . . ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Each task was evaluated over 10 trials, with a 10 | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4 Method - extractive body cue:** Finally, we detail the instruction fine-tuning pipeline and the model architecture selection for AHA (Sec.4.3).
- **p. 10 / 4 Method - extractive body cue:** Each policy was trained using PPO over task-specific training steps and evaluated across 1,000 test steps.
- **p. 7 / 4 Method - extractive body cue:** During fine-tuning, only the projector and transformer weights are updated, while the vision encoder and tokenizer remain frozen.
- **p. 9 / 4 Method - extractive body cue:** We evaluated Aha's performance using a range of AHA data for instruction fine-tuning, spanning [3k, 6k, 12k, 34k, 48k, 60k], and co-trained individual checkpoints corresponding ...
- **p. 10 / 4 Method - extractive body cue:** Each policy was trained using PPO over task-specific training steps and evaluated across 1,000 test steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, architecture, includes, image, encoder, linear, projector, language, tokenizer, transformerbased, PRoC3S, system, solves, tasks, specified, natural, prompting, LLM, Language-Model, Program.
- **Relevant PDF headings:** 4 Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Lastly, we adapted a failure benchmark from the RoboFail dataset [48], which features real-world robot failures in seven UR5 robot tasks. | p. 8 (4 Method), p. 8 (4 Method) |
| Action / skill decoding | Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and ... | p. 8 (Figure/Table caption), p. 7 (4 Method) |
| Receding execution / feedback | Figure 3: (Left) Scaling law with the AHA dataset. Scaling of effect of model performance with varying domain specific fine-tuning data. (Right) ... | p. 9 (Figure/Table caption), p. 3 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / 4 Method - extractive body cue:** Scaling of effect of model performance with varying domain specific fine-tuning data.
- **p. 8 / 4 Method - extractive body cue:** The first dataset, AHA dataset (Test), includes 11k image-question pairs from 10 RLBench tasks, generated similarly to the fine-tuning data via FailGen (Section 3.2) but ...
- **p. 9 / 4 Method - extractive body cue:** An average quadratic fit gradient of 0.0022 across all four metrics demonstrates a scaling effect with fine-tuning on our procedurally generated data pipeline.
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: AHA datasets for instruction-tuning. We combined the AHA dataset, our large-scale robotic manipulation failure dataset, with VQA and object detection data. By incorporating ...
- **p. 6 / 4 Method - extractive body cue:** For the input formulation in VLMs for instruction fine-tuning and evaluation, we required a query prompt 6
- **p. 6 / 4 Method - extractive body cue:** This section outlines the failure reasoning problem formulation (Sec.4.1) used to fine-tune and evaluate AHA.
- **p. 7 / 4 Method - extractive body cue:** All components are initialized with pre-trained weights.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (4 Method), p. 10 (4 Method), p. 7 (4 Method), p. 9 (4 Method), p. 6 (4 Method), p. 10 (4 Method), objective p. 10 (4 Method), p. 9 (4 Method), p. 9 (4 Method), p. 10 (4 Method), p. 7 (4 Method), temporal p. 7 (4 Method), p. 7 (4 Method), p. 6 (4 Method), p. 8 (4 Method), p. 10 (4 Method), p. 10 (4 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
