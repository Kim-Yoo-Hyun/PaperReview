# Method - FP3: A 3D Foundation Policy for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://2026.ieee-icra.org/awards/; PDF retrieval source: https://arxiv.org/pdf/2503.08950. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 8 (8 Training Scenes), p. 8 (8 Training Scenes)): FP3 is a 1.3B encoder-decoder transformer network following a two-stage pre-training and post-training recipe.

## Method Body Digest

- **p. 3 / III. METHOD - extractive PDF cue:** FP3 is a 1.3B encoder-decoder transformer network following a two-stage pre-training and post-training recipe.
- **p. 3 / III. METHOD - extractive PDF cue:** Now we describe the detailed structure of FP3 model, including the encoding of multi-modal inputs and the transformer-based encoder-decoder architecture.
- **p. 4 / III. METHOD - extractive PDF cue:** The Transformer encoder fuses multi-modal input embeddings to latent tokens, while the Transformer decoder takes in the noise actions and leverages adaLN [47, 5, 32] ...
- **p. 4 / III. METHOD - extractive PDF cue:** Pour the water in the bottle into the cup Language Instruction (𝑥, 𝑦, 𝑧, α, 𝛽, 𝛾, 𝑔) Proprioception States Uni3D ViT Uni3D ViT CLIP ...
- **p. 8 / 8 Training Scenes - extractive PDF cue:** FP3 can perfectly follow the instructions to execute the correct tasks rather than simply memorize the training distribution. • FP3-Base-Image converts the point cloud observations ...
- **p. 8 / 8 Training Scenes - extractive PDF cue:** We achieve the best performance when using 3D point cloud input, a larger model, and largerscale pre-training data.
- **p. 7 / 8 Training Scenes - extractive PDF cue:** 4: Visualizations of post-training environments and in-the-wild evaluations.
- **p. 4 / III. METHOD - extractive PDF cue:** The weight decay is set to 0.1, and gradient clipping is set to 1.0.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong generalizability ...
- **p. 4 / III. METHOD - extractive PDF cue:** Thanks to the effective initialization from pre-training, this small amount of fine-tuning data enables zero-shot deployment to novel environments and objects.
- **p. 3 / III. METHOD - extractive PDF cue:** We introduce the 3D Foundation Policy (FP3) model for generalist robotic manipulation, achieving high data efficiency and generalization capability.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive PDF cue:** FP3 is a 1.3B encoder-decoder transformer network following a two-stage pre-training and post-training recipe.
- **p. 3 / III. METHOD - extractive PDF cue:** Now we describe the detailed structure of FP3 model, including the encoding of multi-modal inputs and the transformer-based encoder-decoder architecture.
- **p. 4 / III. METHOD - extractive PDF cue:** The Transformer encoder fuses multi-modal input embeddings to latent tokens, while the Transformer decoder takes in the noise actions and leverages adaLN [47, 5, 32] ...
- **p. 4 / III. METHOD - extractive PDF cue:** Pour the water in the bottle into the cup Language Instruction (𝑥, 𝑦, 𝑧, α, 𝛽, 𝛾, 𝑔) Proprioception States Uni3D ViT Uni3D ViT CLIP ...
- **p. 8 / 8 Training Scenes - extractive PDF cue:** FP3 can perfectly follow the instructions to execute the correct tasks rather than simply memorize the training distribution. • FP3-Base-Image converts the point cloud observations ...
- **p. 8 / 8 Training Scenes - extractive PDF cue:** We achieve the best performance when using 3D point cloud input, a larger model, and largerscale pre-training data.
- **p. 7 / 8 Training Scenes - extractive PDF cue:** 4: Visualizations of post-training environments and in-the-wild evaluations.
- **Detected method headings:** 1) We propose a novel diffusion-based 3D robot policy (p. 2); III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | FP3 is a 1.3B encoder-decoder transformer network following a two-stage pre-training and post-training recipe. | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Now we describe the detailed structure of FP3 model, including the encoding of multi-modal inputs and the transformer-based encoder-decoder architecture. | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The Transformer encoder fuses multi-modal input embeddings to latent tokens, while the Transformer decoder takes in the noise actions and leverages adaLN ... | p. 4 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHOD - extractive PDF cue:** The weight decay is set to 0.1, and gradient clipping is set to 1.0.
- **p. 3 / III. METHOD - extractive PDF cue:** However, pre-trained large-scale foundation vision encoders have demonstrated a performance advantage over small encoders in image-based policies [13, 37].
- **p. 4 / III. METHOD - extractive PDF cue:** We use the AdamW optimizer [40] with a cosine learning rate schedule.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, point, cloud, observation, language, robot, proprioceptive, state, input, predicts, action, chunks, future, actions | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | takes, point, cloud, observation, language, robot, proprioceptive, state, input, predicts | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | introduce, Foundation, Policy, FP3, first, point, cloud-based, language-visuomotor, model, robotic | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | weight, decay, gradient, clipping, However, pre-trained, large-scale, foundation, vision, encoders | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive PDF cue:** It takes the 3D point cloud observation, language, and robot proprioceptive state as input and predicts action chunks of future actions.
- **p. 4 / III. METHOD - extractive PDF cue:** Pour the water in the bottle into the cup Language Instruction (𝑥, 𝑦, 𝑧, α, 𝛽, 𝛾, 𝑔) Proprioception States Uni3D ViT Uni3D ViT CLIP ...
- **p. 3 / III. METHOD - extractive PDF cue:** Formally, we formalize the problem of language-conditioned visuomotor control as modeling the distribution p(At/ot), where ot = [P1 t, ..., Pn t , ℓt, qt] ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** One potential limitation of current policy foundation models is their exclusive reliance on 2D image observations, lacking 3D observation inputs.
- **p. 8 / 8 Training Scenes - extractive PDF cue:** FP3 can perfectly follow the instructions to execute the correct tasks rather than simply memorize the training distribution. • FP3-Base-Image converts the point cloud observations ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Towards this goal of policy foundation models, there have been some initial attempts at vision-language-action (VLA) models [80, 36, 3], which build upon the vision-language ...
- **p. 4 / III. METHOD - extractive PDF cue:** To handle the partial observation, we stack 2 frames as input, including 1 step observation history, to compensate for the missing dynamic information of the ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | To handle the partial observation, we stack 2 frames as input, including 1 step observation history, to compensate for the missing dynamic ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The diffusion denoiser of FP3 is a Transformer decoder that denoises the action chunks from noise with temporal causal masking following [79]. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | To handle the partial observation, we stack 2 frames as input, including 1 step observation history, to compensate for the missing dynamic ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | To handle the partial observation, we stack 2 frames as input, including 1 step observation history, to compensate for the missing dynamic ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHOD - extractive PDF cue:** FP3 is a 1.3B encoder-decoder transformer network following a two-stage pre-training and post-training recipe.
- **p. 8 / 8 Training Scenes - extractive PDF cue:** FP3 can perfectly follow the instructions to execute the correct tasks rather than simply memorize the training distribution. • FP3-Base-Image converts the point cloud observations ...
- **p. 8 / 8 Training Scenes - extractive PDF cue:** We achieve the best performance when using 3D point cloud input, a larger model, and largerscale pre-training data.
- **p. 7 / 8 Training Scenes - extractive PDF cue:** 4: Visualizations of post-training environments and in-the-wild evaluations.
- **p. 4 / III. METHOD - extractive PDF cue:** The FP3 base model is pre-trained for 3M steps with a batch size of 128 using 8 NVIDIA A800 GPUs, which takes about 48 hours.
- **p. 8 / 8 Training Scenes - extractive PDF cue:** FP3 can perfectly follow the instructions to execute the correct tasks rather than simply memorize the training distribution. • FP3-Base-Image converts the point cloud observations ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** FP3, encoder-decoder, transformer, network, following, two-stage, pre-training, post-training, recipe, Now, describe, detailed, structure, model, including, encoding, multi-modal, inputs, transformer-based, architecture.
- **Relevant PDF headings:** 1) We propose a novel diffusion-based 3D robot policy (p. 2); III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | As we pre-train our FP3 model on the DROID dataset, we also build a real robot setup similar to DROID for evaluating ... | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 4 (III. METHOD) |
| Action / skill decoding | The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to ... | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| Receding execution / feedback | The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to ... | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |

## Failure and Ablation Link

- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first failure, ...
- **p. 4 / III. METHOD - extractive PDF cue:** As we only care about the operated object, we cropped the points outside a 1-meter box to remove redundant points.
- **p. 4 / III. METHOD - extractive PDF cue:** Thanks to the effective initialization from pre-training, this small amount of fine-tuning data enables zero-shot deployment to novel environments and objects.
- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** In this challenging setting, we observe that all baseline policies without pre-training, including FP3-Scratch, often fail to recognize the target objects, resulting in near-zero performance ...
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** Ablations We finally do ablation studies on the observation choice, model size, and pre-training data size.
- **p. 8 / 8 Training Scenes - extractive PDF cue:** FP3 can perfectly follow the instructions to execute the correct tasks rather than simply memorize the training distribution. • FP3-Base-Image converts the point cloud observations ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of 3D Foundation Policy (FP3), a 1.3B 3D point cloud-based language-visuomotor policy pre-trained on 60k episodes from the DROID dataset [35]. FP3 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 8 (8 Training Scenes), p. 8 (8 Training Scenes), objective p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), temporal p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol), p. 1 (Front matter).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
