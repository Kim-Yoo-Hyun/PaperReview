# Method - RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2509.15212v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 4 (3 Methodology), p. 6 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY)): Stage1: language Encoder Decoder Action chunks decoded Action chunks Action Representation Learning via ActionVAE Transformer Stage2: language Transformer Human-Centric Trajectory-Aware Video Modeling Ego-Centric Video Generative Pretra ...

## Method Body Digest

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Stage1: language Encoder Decoder Action chunks decoded Action chunks Action Representation Learning via ActionVAE Transformer Stage2: language Transformer Human-Centric Trajectory-Aware Video Modeling Ego-Centric Video Generative ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** 2, the ActionVAE consists of an encoder that compresses an "action chunk" into a compact and continuous latent embedding, and a decoder that reconstructs the ...
- **p. 4 / 3 Methodology - extractive PDF cue:** In this work, we propose RynnVLA-001, a Vision-Language-Action (VLA) model built upon large-scale video generation pretraining.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** During training, the model is optimized with two concurrent objectives: 1) Robot Action Prediction: The hidden state corresponding to the output of the <ACTION_PLACEHOLDER> token ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The training of the action head is supervised by L1 loss, which is computed exclusively for the outputs at token positions of <ACTION_PLACEHOLDER>.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** To provide the model with proprioceptive information, we introduce state embeddings (blue blocks in Fig.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The training is supervised by the cross-entropy loss over discrete visual tokens and language tokens.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** 2) Future Visual Prediction: The model continues the autoregressive prediction of visual tokens for the next frame, supervised by cross-entropy loss.

## Design Rationale

- **p. 1 / 1 Introduction - extractive PDF cue:** In this work, we propose RynnVLA-001, a VLA model enhanced by video generation pretraining.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To ensure the smoothness and temporal coherence of predicted actions, we propose ActionVAE, a variational autoencoder that encodes action chunks into compact embeddings.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our framework leverages three types of training data: (1) Ego-Centric Video Generative Pretraining uses millions of ego-centric human manipulation videos for future frame prediction.

## Source Evidence Cues

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Stage1: language Encoder Decoder Action chunks decoded Action chunks Action Representation Learning via ActionVAE Transformer Stage2: language Transformer Human-Centric Trajectory-Aware Video Modeling Ego-Centric Video Generative ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** 2, the ActionVAE consists of an encoder that compresses an "action chunk" into a compact and continuous latent embedding, and a decoder that reconstructs the ...
- **p. 4 / 3 Methodology - extractive PDF cue:** In this work, we propose RynnVLA-001, a Vision-Language-Action (VLA) model built upon large-scale video generation pretraining.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** During training, the model is optimized with two concurrent objectives: 1) Robot Action Prediction: The hidden state corresponding to the output of the <ACTION_PLACEHOLDER> token ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The training of the action head is supervised by L1 loss, which is computed exclusively for the outputs at token positions of <ACTION_PLACEHOLDER>.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** To provide the model with proprioceptive information, we introduce state embeddings (blue blocks in Fig.
- **Detected method headings:** 3 METHODOLOGY (p. 4); 3 Methodology (p. 4); 3 METHODOLOGY (p. 5); 3 METHODOLOGY (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Stage1: language Encoder Decoder Action chunks decoded Action chunks Action Representation Learning via ActionVAE Transformer Stage2: language Transformer Human-Centric Trajectory-Aware Video Modeling ... | p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | 2, the ActionVAE consists of an encoder that compresses an "action chunk" into a compact and continuous latent embedding, and a decoder ... | p. 6 (3 METHODOLOGY), p. 4 (3 Methodology) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | In this work, we propose RynnVLA-001, a Vision-Language-Action (VLA) model built upon large-scale video generation pretraining. | p. 4 (3 Methodology), p. 6 (3 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** During training, the model is optimized with two concurrent objectives: 1) Robot Action Prediction: The hidden state corresponding to the output of the <ACTION_PLACEHOLDER> token ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The training is supervised by the cross-entropy loss over discrete visual tokens and language tokens.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** 2) Future Visual Prediction: The model continues the autoregressive prediction of visual tokens for the next frame, supervised by cross-entropy loss.
- **p. 4 / 3 Methodology - extractive PDF cue:** The objective of this stage is to train an I2V model that closely mimics the inference process of a VLA model.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The training of the action head is supervised by L1 loss, which is computed exclusively for the outputs at token positions of <ACTION_PLACEHOLDER>.
- **p. 4 / 3 Methodology - extractive PDF cue:** The model is progressively trained through three stages, as illustrated in Fig.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3 Methodology), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | typical, VLA, setting, actions, predicted, conditioned, current, observations, visual, inputs, robot, states, language, instruction | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | typical, VLA, setting, actions, predicted, conditioned, current, observations, visual, inputs | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | RynnVLA-001, VLA, model, enhanced, video, generation, pretraining, ensure, smoothness, temporal | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | During, training, model, optimized, concurrent, objectives, Robot, Action, Prediction, hidden | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Methodology - extractive PDF cue:** In a typical VLA setting, actions are predicted conditioned on current observations (e.g., visual inputs and robot states) and a language instruction.
- **p. 4 / 3 Methodology - extractive PDF cue:** 3) Robot-Centric Vision-Language-Action Modeling: The VLA model inherits the weights from the previous stages and is trained on robot data using language instructions and current ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** (3) Robot-Centric Vision-Language-Action Modeling employs robot datasets paired with language instructions to learn mappings from visual observations and language to robotic actions. image and a ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** At each step of the cycle, the model receives the language instruction, the current RGB observation from the robot's cameras and current robot states as ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** During inference, given an observation and a language instruction, the model outputs a single action embedding, which is subsequently decoded by ActionVAE into a sequence ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** This sequence explicitly provides four components: (1) the high-level goal (language), (2) robot-centric visual observations (front and wrist views), (3) the current robot state, and ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The input sequence is now structured as: [language, visual tokenst, state embeddingt, <ACTION_PLACEHOLDER>, ...], where <ACTION_PLACEHOLDER> is the signal to generate continuous action embeddings.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | 3.3 ActionVAE: Action Representaton via VAE In VLA models, predicting action chunks (i.e., short sequences of actions) is more effective than predicting ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | These embeddings represent the current keypoint positions of the human wrists and are fed into the model at each timestep. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | In contrast, all other models are evaluated with 60 trials per task. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Stage1: language Encoder Decoder Action chunks decoded Action chunks Action Representation Learning via ActionVAE Transformer Stage2: language Transformer Human-Centric Trajectory-Aware Video Modeling Ego-Centric Video Generative ...
- **p. 4 / 3 Methodology - extractive PDF cue:** In this work, we propose RynnVLA-001, a Vision-Language-Action (VLA) model built upon large-scale video generation pretraining.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** During training, the model is optimized with two concurrent objectives: 1) Robot Action Prediction: The hidden state corresponding to the output of the <ACTION_PLACEHOLDER> token ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The training of the action head is supervised by L1 loss, which is computed exclusively for the outputs at token positions of <ACTION_PLACEHOLDER>.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Benefiting from the pretrained T2I checkpoint, the RynnVLA-001-Chameleon model achieves reasonable results on simple grasping.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** All models are trained with reduced epochs for efficiency; scores are for relative comparison.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Stage1, language, Encoder, Decoder, Action, chunks, decoded, Representation, Learning, ActionVAE, Transformer, Stage2, Human-Centric, Trajectory-Aware, Video, Modeling, Ego-Centric, Generative, Pretraining, Head.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 4); 3 Methodology (p. 4); 3 METHODOLOGY (p. 5); 3 METHODOLOGY (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | To train and evaluate our proposed RynnVLA-001 model, we collect a new real-world manipulation dataset using a LeRobot SO100 robotic arm (Cadene ... | p. 7 (5 Experiments), p. 8 (5 EXPERIMENTS) |
| Action / skill decoding | We compare our model with two strong open-source baselines, namely GR00T N1.5 (Bjorck et al., 2025a) and Pi0 (Black et al., 2024). | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Receding execution / feedback | In contrast, RynnVLA-001-Video achieves a significant performance improvement, indicating that priors learned from ego-centric videos are effective for VLA adaptation. | p. 9 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** To investigate the effectiveness of our proposed two-stage pretraining pipeline, we conduct a comprehensive ablation study, with results presented in Table 3 and Table 4.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** To evaluate the effectiveness of the component, we conduct an ablation study on the Calvin ABC->D benchmark, comparing the performance of predicting VAE embeddings against ...
- **p. 12 / 5 EXPERIMENTS - extractive PDF cue:** A variant of RynnVLA-001 is trained solely on data without distractor objects.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** By incorporating this second pretraining stage where the model learns to predict human trajectories, our full model, RynnVLA-001, achieves the best performance among all variants.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** For experimental efficiency, our full model and the ablated variants are trained from the pretraining weights of RynnVLA-001-Video but for a reduced number of epochs.
- **p. 11 / 5 EXPERIMENTS - extractive PDF cue:** 5.4 Ablation Study on Model Designs
- **p. 12 / 5 EXPERIMENTS - extractive PDF cue:** To validate this hypothesis, we perform an ablation study.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 4 (3 Methodology), p. 6 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), objective p. 6 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 4 (3 Methodology), p. 5 (3 METHODOLOGY), p. 4 (3 Methodology), temporal p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 7 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
