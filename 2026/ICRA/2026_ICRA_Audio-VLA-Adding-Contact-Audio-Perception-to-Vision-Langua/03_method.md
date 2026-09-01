# Method - Audio-VLA: Adding Contact Audio Perception to Vision-Language-Action Model for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2511.09958v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD)): The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a unified representation space, a 7B-parameter Llama2 language model as backbone, ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive PDF cue:** The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a unified representation space, a 7B-parameter ...
- **p. 2 / III. METHOD - extractive PDF cue:** This section first details the Audio-VLA architecture, then presents our training objective and audio-enhanced simulation environments for LIBERO [8] and RLBench [9].
- **p. 3 / III. METHOD - extractive PDF cue:** It consists of two powerful vision transformers, DINOv2 [23] and SigLIP [24], pre-trained on Internet-scale image data to capture rich visual features and comprehensive spatial ...
- **p. 4 / III. METHOD - extractive PDF cue:** This enables Faud to capture high-frequency acoustic features and temporal dynamics of contact events, providing physical interaction information unavailable through visual perception alone.
- **p. 4 / III. METHOD - extractive PDF cue:** The input of the proprio encoder is proprioceptive robot state pt, which includes information such as joint angles, encoded via an MLP layer ϕstate(·) to ...
- **p. 2 / III. METHOD - extractive PDF cue:** 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi
- **p. 5 / III. METHOD - extractive PDF cue:** These recordings are organized into a structured library indexed by material pairs, interaction types, and force magnitudes.
- **p. 4 / III. METHOD - extractive PDF cue:** This is achieved through the minimization of the mean L1 loss function: L = 1 K · D K-1 X k=0 D X i=1

## Design Rationale

- **p. 2 / III. METHOD - extractive PDF cue:** 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In this paper, we propose Audio-VLA, a multimodal manipulation policy that combines acoustic and visual perception.
- **p. 3 / III. METHOD - extractive PDF cue:** It consists of two powerful vision transformers, DINOv2 [23] and SigLIP [24], pre-trained on Internet-scale image data to capture rich visual features and comprehensive spatial ...

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive PDF cue:** The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a unified representation space, a 7B-parameter ...
- **p. 2 / III. METHOD - extractive PDF cue:** This section first details the Audio-VLA architecture, then presents our training objective and audio-enhanced simulation environments for LIBERO [8] and RLBench [9].
- **p. 3 / III. METHOD - extractive PDF cue:** It consists of two powerful vision transformers, DINOv2 [23] and SigLIP [24], pre-trained on Internet-scale image data to capture rich visual features and comprehensive spatial ...
- **p. 4 / III. METHOD - extractive PDF cue:** This enables Faud to capture high-frequency acoustic features and temporal dynamics of contact events, providing physical interaction information unavailable through visual perception alone.
- **p. 4 / III. METHOD - extractive PDF cue:** The input of the proprio encoder is proprioceptive robot state pt, which includes information such as joint angles, encoded via an MLP layer ϕstate(·) to ...
- **p. 2 / III. METHOD - extractive PDF cue:** 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi
- **p. 5 / III. METHOD - extractive PDF cue:** These recordings are organized into a structured library indexed by material pairs, interaction types, and force magnitudes.
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a unified representation ... | p. 3 (III. METHOD), p. 2 (III. METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | This section first details the Audio-VLA architecture, then presents our training objective and audio-enhanced simulation environments for LIBERO [8] and RLBench [9]. | p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | It consists of two powerful vision transformers, DINOv2 [23] and SigLIP [24], pre-trained on Internet-scale image data to capture rich visual features ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHOD - extractive PDF cue:** This is achieved through the minimization of the mean L1 loss function: L = 1 K · D K-1 X k=0 D X i=1
- **p. 4 / III. METHOD - extractive PDF cue:** Training objective Our proposed Audio-VLA aims to minimize the discrepancy between the predicted action block ˆAt and the expertdemonstrated ground truth action block A∗ t ...
- **p. 2 / III. METHOD - extractive PDF cue:** This section first details the Audio-VLA architecture, then presents our training objective and audio-enhanced simulation environments for LIBERO [8] and RLBench [9].
- **p. 3 / III. METHOD - extractive PDF cue:** To fully leverage these signals, we optimize for high-frequency feature extraction and fine-grained temporal modeling.
- **p. 3 / III. METHOD - extractive PDF cue:** To enhance AudioCLIP's capability in perceiving robotic contact events, additional training is conducted on the ManiWAV [13] robotic manipulation dataset based on the original pretrained ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Furthermore, recognizing, limitations, existing, evaluation, metrics, focus, primarily, final, task, outcomes, Completion, Rate, TCR | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Furthermore, recognizing, limitations, existing, evaluation, metrics, focus, primarily, final, task | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Audio-VLA, consists, four, components, including, multi-modal, encoder, multi, multimodal, manipulation | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | achieved, through, minimization, mean, loss, function, K-1, Training, objective, Audio-VLA | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Furthermore, recognizing the limitations of existing evaluation metrics that focus primarily on final task outcomes, the Task Completion Rate (TCR) evaluation metric is proposed to ...
- **p. 4 / III. METHOD - extractive PDF cue:** Subsequently, we extract the action hidden states Hact from Hdec, where each vector h(m) ∈Rdllm for m = 1, . . . , K · ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** 1: Unlike VLA models, Audio-VLA incorporates audio perception, enabling better assessment of contact states and understanding of manipulation dynamics. events [13] and interaction feedback [14], ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Contact audio has emerged as a promising alternative tactile sensing approach leveraging contact microphones to capture vibration signals from object interactions, providing real-time feedback about ...
- **p. 3 / III. METHOD - extractive PDF cue:** SigLIP+ DINOv2 SigLIP+ DINOv2 vision encoder Audio encoder Multi-modal encoder tI tS MLP vis F Concatenation aud F prop F Sequence Concatenation Llama2 7B parallel ...
- **p. 4 / III. METHOD - extractive PDF cue:** The tokens from all modalities are concatenated with K·D learnable empty action embeddings Eempty ∈R(K·D)×dllm to form the complete input sequence: Xin = [Elang; X; ...
- **p. 3 / III. METHOD - extractive PDF cue:** The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a unified representation space, a 7B-parameter ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The raw audio stream is segmented into fixed-length chunks corresponding to each timestep for temporal alignment with visual observations. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | At each timestep t, the audio input is St ∈RB×C×T , where C denotes the number of audio channels and T represents ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Evaluation Protocols: Evaluations are conducted with inference on an NVIDIA H20 GPU communicating with the robot platform through ROS [38], where inference ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / III. METHOD - extractive PDF cue:** This section first details the Audio-VLA architecture, then presents our training objective and audio-enhanced simulation environments for LIBERO [8] and RLBench [9].
- **p. 3 / III. METHOD - extractive PDF cue:** It consists of two powerful vision transformers, DINOv2 [23] and SigLIP [24], pre-trained on Internet-scale image data to capture rich visual features and comprehensive spatial ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** The LoRA [26] rank is set to 32, training runs for 50k to 100k steps depending on the task, the batch size is 8, and ...
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** Evaluation Protocols: Evaluations are conducted with inference on an NVIDIA H20 GPU communicating with the robot platform through ROS [38], where inference and execution run ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Formally, TCR is defined as: TCR = Achieved Progress Task Target ∈[0, 1] (13) where the achieved progress is task-specific, in this paper: • EAWM: ...
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** Audio Encoder LoRA Fine-tuning Necessity.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, consists, multi-modal, encoders, including, audio, vision, proprioceptive, modules, Projector, heterogeneous, features, unified, representation, space, B-parameter, Llama2, language, backbone, four-layer.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The performance gap reveals that in tasks requiring precise force control and continuous state monitoring, visual modality nearly loses its ability to ... | p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Action / skill decoding | The inferior performance of the vision-only configuration compared to the full configuration demonstrates that audio provides critical information for TABLE IV: Ablation ... | p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Receding execution / feedback | I, AudioVLA achieves 97.6% average success rate on LIBERO and 55.1% on RLBench, outperforming all comparative methods. | p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Additionally, we conduct ablation studies in both simulation and real-world settings to investigate the effectiveness of incorporating contact audio signals into VLA. a) Simulation Experiments ...
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** The pre-trained audio encoder cannot effectively process manipulation-specific sounds without LoRA [26].
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** Ablation Studies Ablation studies on RLBench in Table III and real robot experiments in Table IV reveal the importance of both audio modality integration and ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** The robustness differential validates that contact audio provides environment-invariant physical signals.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Architecture of Audio-VLA. The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable information particularly when visual perception fails to ...
- **p. 7 / V. CONCLUSION - extractive PDF cue:** This paper presents Audio-VLA, a multimodal manipulation policy that integrates acoustic perception into VLA models to overcome vision-only limitations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD), objective p. 4 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), temporal p. 5 (IV. EXPERIMENT), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 6 (IV. EXPERIMENT).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
