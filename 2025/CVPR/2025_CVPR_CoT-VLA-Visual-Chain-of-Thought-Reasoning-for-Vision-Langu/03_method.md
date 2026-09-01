# Method - CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. The Base Vision-Language Model), p. 4 (3.2. The Base Vision-Language Model), p. 5 (10. For complete dataset specifications and training hyper), p. 5 (10. For complete dataset specifications and training hyper)): We use the VILA-U model trained on 256 × 256 resolution images, where each image is encoded into 16 × 16 × 4 tokens with a residual depth of 4 ...

## Method Body Digest

- **p. 4 / 3.2. The Base Vision-Language Model - extractive PDF cue:** We use the VILA-U model trained on 256 × 256 resolution images, where each image is encoded into 16 × 16 × 4 tokens with ...
- **p. 4 / 3.2. The Base Vision-Language Model - extractive PDF cue:** VILA-U utilizes residual quantization [32] to improve the representational capacity of discrete visual features - incorporating a depth transformer, as introduced in RQ-VAE [32], to ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive PDF cue:** Algorithm 1 CoT-VLA test-time closed-loop control Require: CoT-VLA Model Pθ, initial state sobs 0 , language instruction l 0: t ←0 0: while True do ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive PDF cue:** During this phase, we optimize the LLM backbone, projector, and depth transformer while keeping the vision tower frozen, maintaining the same training setup as the ...
- **p. 4 / 3.3. Training Procedures - extractive PDF cue:** During training, we minimize the cross-entropy loss for action predictions: \math c a l
- **p. 4 / 3.3. Training Procedures - extractive PDF cue:** {L} _{\ text {action}} = - \sum _{i=1}^{m}\log P_\theta (\mathbf {a}_{t}...\mathbf {a}_{t+m}/l,s_t,s_{t+n} ) (5) Given a batch of input sequences, The overall training objective combines ...
- **p. 1 / 1. Introduction - extractive PDF cue:** One promising direction is vision-language-action (VLA) models, which leverage the rich understanding capabilities of pretrained vision-language models (VLMs) to map natural language instructions and visual ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our key contributions include: • We introduce a method of visual chain-of-thought reasoning through subgoal image generation as an intermediate reasoning step for robotic control. ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its ...
- **p. 4 / 3.2. The Base Vision-Language Model - extractive PDF cue:** This enables autoregressive image and video generation while significantly enhancing the understanding capabilities of VLMs that leverage discrete visual features.

## Source Evidence Cues

- **p. 4 / 3.2. The Base Vision-Language Model - extractive PDF cue:** We use the VILA-U model trained on 256 × 256 resolution images, where each image is encoded into 16 × 16 × 4 tokens with ...
- **p. 4 / 3.2. The Base Vision-Language Model - extractive PDF cue:** VILA-U utilizes residual quantization [32] to improve the representational capacity of discrete visual features - incorporating a depth transformer, as introduced in RQ-VAE [32], to ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive PDF cue:** Algorithm 1 CoT-VLA test-time closed-loop control Require: CoT-VLA Model Pθ, initial state sobs 0 , language instruction l 0: t ←0 0: while True do ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive PDF cue:** During this phase, we optimize the LLM backbone, projector, and depth transformer while keeping the vision tower frozen, maintaining the same training setup as the ...
- **Detected method headings:** 3.2. The Base Vision-Language Model (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We use the VILA-U model trained on 256 × 256 resolution images, where each image is encoded into 16 × 16 × ... | p. 4 (3.2. The Base Vision-Language Model), p. 4 (3.2. The Base Vision-Language Model) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | VILA-U utilizes residual quantization [32] to improve the representational capacity of discrete visual features - incorporating a depth transformer, as introduced in ... | p. 4 (3.2. The Base Vision-Language Model), p. 5 (10. For complete dataset specifications and training hyper) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Algorithm 1 CoT-VLA test-time closed-loop control Require: CoT-VLA Model Pθ, initial state sobs 0 , language instruction l 0: t ←0 0: ... | p. 5 (10. For complete dataset specifications and training hyper), p. 5 (10. For complete dataset specifications and training hyper) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3. Training Procedures - extractive PDF cue:** During training, we minimize the cross-entropy loss for action predictions: \math c a l
- **p. 4 / 3.3. Training Procedures - extractive PDF cue:** {L} _{\ text {action}} = - \sum _{i=1}^{m}\log P_\theta (\mathbf {a}_{t}...\mathbf {a}_{t+m}/l,s_t,s_{t+n} ) (5) Given a batch of input sequences, The overall training objective combines ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive PDF cue:** During this phase, we optimize the LLM backbone, projector, and depth transformer while keeping the vision tower frozen, maintaining the same training setup as the ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.3. Training Procedures), p. 4 (3.3. Training Procedures).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | One, promising, direction, vision-language-action, VLA, models, leverage, rich, understanding, capabilities, pretrained, vision-language, VLMs, natural | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | One, promising, direction, vision-language-action, VLA, models, leverage, rich, understanding, capabilities | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, include, introduce, visual, chain-of-thought, reasoning, through, subgoal, image, generation | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | During, training, minimize, cross-entropy, loss, action, predictions, math, text, theta | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** One promising direction is vision-language-action (VLA) models, which leverage the rich understanding capabilities of pretrained vision-language models (VLMs) to map natural language instructions and visual ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive PDF cue:** Algorithm 1 CoT-VLA test-time closed-loop control Require: CoT-VLA Model Pθ, initial state sobs 0 , language instruction l 0: t ←0 0: while True do ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our key contributions include: • We introduce a method of visual chain-of-thought reasoning through subgoal image generation as an intermediate reasoning step for robotic control. ...
- **p. 4 / 3.3. Training Procedures - extractive PDF cue:** {L} _{\ text {action}} = - \sum _{i=1}^{m}\log P_\theta (\mathbf {a}_{t}...\mathbf {a}_{t+m}/l,s_t,s_{t+n} ) (5) Given a batch of input sequences, The overall training objective combines ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Unlike vanilla VLAs, CoT-VLA (bottom) can also leverage action-less datasets like EPIC-KITCHEN-100 [27] to enhance subgoal image generation ability, unlocking the potential of using abundant ...
- **p. 4 / 3.3. Training Procedures - extractive PDF cue:** Our training objective has two key components: subgoal image generation with causal attention (2) and action generation with full attention (3).
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Additionally, inspired by recent advances in robot learning [10, 17, 77], we predict sequences of actions (action chunking) rather than a single ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We evaluate four model variants: VLA - a baseline implementation following the standard VLA framework [29], with the same VILA-U backbone but ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | LIBERO We present quantitative results in Table 1, where each method is evaluated over 500 trials per task suite, with 3 random ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. The Base Vision-Language Model - extractive PDF cue:** We use the VILA-U model trained on 256 × 256 resolution images, where each image is encoded into 16 × 16 × 4 tokens with ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive PDF cue:** During this phase, we optimize the LLM backbone, projector, and depth transformer while keeping the vision tower frozen, maintaining the same training setup as the ...
- **p. 8 / 4.4. Better Visual Reasoning Helps - extractive PDF cue:** Recent advancement in fast image generation or fast LLM inference techniques could potentially improve the throughput of the model [7, 31, 33, 57, 73] and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** VILA-U, model, trained, resolution, images, where, image, encoded, tokens, residual, depth, utilizes, quantization, improve, representational, capacity, discrete, visual, features, incorporating.
- **Relevant PDF headings:** 3.2. The Base Vision-Language Model (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We conduct evaluations across three complementary settings: the LIBERO benchmark [37] for evaluation in simulation environments, the Bridge-V2 platform [60] with its ... | p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments) |
| Action / skill decoding | Our experiments aim to addresses following questions: • How does our system perform compared to state-of-the-art baselines across multiple benchmarks and embodiments? | p. 5 (4. Experiments), p. 6 (4.2. Evaluations Results) |
| Receding execution / feedback | Table 1. LIBERO benchmark experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard ... | p. 5 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** Ablation studies of CoT-VLA components. a) Results on LIBERO-Spatial and LIBERO-Goal benchmarks demonstrate the effectiveness of three components: action chunking, hybrid attention, and visual chain-of-thought ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We evaluate four model variants: VLA - a baseline implementation following the standard VLA framework [29], with the same VILA-U backbone but without chain-of-thought reasoning ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** OpenVLA [29] is an open-source VLA model that fine-tunes pretrained vision-language models on the OpenX dataset; and Octo [59] is a generalist model pretrained on ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** To assess the importance of our pretraining stage, we conduct ablation studies on the Franka-Tabletop setup.
- **p. 8 / 4.4. Better Visual Reasoning Helps - extractive PDF cue:** To investigate how visual reasoning capabilities transfer to robot performance, we conduct an ablation study on the Franka-Tabletop setup using novel, long-horizon tasks that combine ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** While the dataset was incorporated into the pretraining phase alongside OpenX, we performed additional task-specific fine-tuning exclusively on Bridge-V2 until achieving a training action prediction ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Comparison between vanilla VLA and CoT-VLA frameworks. Prior VLA models (top) directly predict robot ac- tions from task inputs without explicit reasoning steps ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. The Base Vision-Language Model), p. 4 (3.2. The Base Vision-Language Model), p. 5 (10. For complete dataset specifications and training hyper), p. 5 (10. For complete dataset specifications and training hyper), objective p. 4 (3.3. Training Procedures), p. 4 (3.3. Training Procedures), p. 5 (10. For complete dataset specifications and training hyper), temporal p. 2 (1. Introduction), p. 7 (4.3. Ablation Study), p. 8 (4.4. Better Visual Reasoning Helps), p. 8 (4.4. Better Visual Reasoning Helps), p. 4 (3.3. Training Procedures), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
