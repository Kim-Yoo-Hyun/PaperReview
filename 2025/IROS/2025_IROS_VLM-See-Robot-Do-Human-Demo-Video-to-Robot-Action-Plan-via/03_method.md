# Method - VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.08792; PDF retrieval source: https://arxiv.org/pdf/2410.08792. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD)): The module first instructs the VLM to identify objects in the frames and then use an open-vocabulary object detector [53] to extract object bounding boxes in the first frame.

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** The module first instructs the VLM to identify objects in the frames and then use an open-vocabulary object detector [53] to extract object bounding boxes ...
- **p. 4 / III. METHOD - extractive body cue:** In real-world experiment, we follow [1, 20] and first use a segmentation model to segment all objects of interest in the RGB images, then query ...
- **p. 3 / III. METHOD - extractive body cue:** The speed valleys are identified as keyframes. b) The Visual Prompting module detects and tracks objects and then applies the tracking results as visual prompts ...
- **p. 4 / III. METHOD - extractive body cue:** Specifically, following the approaches in [1] and [20], we use Language Model Programs (LMPs) to implement the task plans on a UR10e robot arm in ...
- **p. 3 / III. METHOD - extractive body cue:** Context length becomes a major constraint when VLMs process long-horizon videos.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Some employ pretrained VLMs for further fine-tuning to learn the mapping from visual inputs and language instructions to actions [5, 6], or leverage the general ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM ...
- **p. 4 / III. METHOD - extractive body cue:** The SeeDo-generated task plans can be seamlessly processed step by step by any robot action model that can take text input.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Inspired by this capability, we propose SeeDo, a modularized agent centered around a VLM.
- **p. 3 / III. METHOD - extractive body cue:** To alleviate these issues, we introduce a visual prompting module in SeeDo that enhances the visual capabilities of the VLM.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** The module first instructs the VLM to identify objects in the frames and then use an open-vocabulary object detector [53] to extract object bounding boxes ...
- **p. 4 / III. METHOD - extractive body cue:** In real-world experiment, we follow [1, 20] and first use a segmentation model to segment all objects of interest in the RGB images, then query ...
- **p. 3 / III. METHOD - extractive body cue:** The speed valleys are identified as keyframes. b) The Visual Prompting module detects and tracks objects and then applies the tracking results as visual prompts ...
- **p. 4 / III. METHOD - extractive body cue:** Specifically, following the approaches in [1] and [20], we use Language Model Programs (LMPs) to implement the task plans on a UR10e robot arm in ...
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The module first instructs the VLM to identify objects in the frames and then use an open-vocabulary object detector [53] to extract ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In real-world experiment, we follow [1, 20] and first use a segmentation model to segment all objects of interest in the RGB ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The speed valleys are identified as keyframes. b) The Visual Prompting module detects and tracks objects and then applies the tracking results ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** Context length becomes a major constraint when VLMs process long-horizon videos.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Some, employ, pretrained, VLMs, further, fine-tuning, learn, mapping, visual, inputs, language, instructions, actions, leverage | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Some, employ, pretrained, VLMs, further, fine-tuning, learn, mapping, visual, inputs | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, follows, introduce, SeeDo, VLM-based, agent, integrates, keyframe, selection | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Context, length, becomes, major, constraint, when, VLMs, process, long-horizon, videos | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** Some employ pretrained VLMs for further fine-tuning to learn the mapping from visual inputs and language instructions to actions [5, 6], or leverage the general ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM ...
- **p. 4 / III. METHOD - extractive body cue:** The SeeDo-generated task plans can be seamlessly processed step by step by any robot action model that can take text input.
- **p. 1 / I. INTRODUCTION - extractive body cue:** SeeDo is designed to interpret long-horizon human demonstration videos into sub-task steps in natural language, which can then be executed by language model programs (LMPs) ...
- **p. 3 / III. METHOD - extractive body cue:** Opensource VLMs often simply sample frames uniformly [10, 46], but this approach is less effective for long-horizon demonstration videos, as frames showing important actions may ...
- **p. 3 / III. METHOD - extractive body cue:** Hand-object interactions are critical in demonstration videos [35, 36] and we observe that hands typically move slower when picking or placing objects, providing a clue ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We compare SeeDo against baselines such as the state-of-the-art video VLMs [10, 11], and find that SeeDo achieve the best performance.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | To achieve success (TSR=1), each step in the plan must match the demo's action sequence in both content and temporal order. • ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | In contrast, videos offer a more straightforward medium, making them particularly wellsuited for long-horizon tasks that involve multiple steps or require understanding ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** module, first, instructs, VLM, identify, objects, frames, then, open-vocabulary, object, detector, extract, bounding, boxes, frame, real-world, experiment, follow, segmentation, model.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with ... | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Action / skill decoding | SeeDo outperforms all closed-source and open-source video VLM baselines across TSR, FSR, and SSR. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Receding execution / feedback | To achieve success (TSR=1), each step in the plan must match the demo's action sequence in both content and temporal order. • ... | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Since SeeDo utilizes GPT-4o as its VLM, we further test three variants of GPT-4o using different frame sampling strategies while keeping the same prompts: • ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We also present ablation studies to assess the impact of separate modules.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our method operates purely on relative spatial relationships (e.g., left, right, above, below) extracted from the demonstration, without relying on fixed camera viewpoints; thus, the ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Ablation on the visual prompting for Spatial Understanding.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: We collect long-horizon human demonstration videos across three diverse categories as our benchmark and carry out both simulation and real-world experiments. Tasks from ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** However, spatial errors remain the main source of SeeDo 's failures.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), objective p. 3 (III. METHOD), temporal p. 5 (IV. EXPERIMENTS), p. 1 (I. INTRODUCTION), p. 2 (II. RELATED WORKS), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
