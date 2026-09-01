# Method - VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 3 (3.3. Training Residual VQ-VAE), p. 3 (3. Methods), p. 2 (3. Methods), p. 2 (3. Methods)): Instead of discretizing action sequences into uniform bins, the action sequence at:t+n is first processed through a pre-trained and frozen Residual VQVAE encoder ϕ(·), generating latent representations.

## Method Body Digest

- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive PDF cue:** Instead of discretizing action sequences into uniform bins, the action sequence at:t+n is first processed through a pre-trained and frozen Residual VQVAE encoder ϕ(·), generating ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive PDF cue:** By leveraging hierarchical quantization with non-overlapping token ID ranges, the model achieves better action representation, avoids semantic confusion between layers, and ensures stable loss convergence ...
- **p. 3 / 3.3. Training Residual VQ-VAE - extractive PDF cue:** To improve the encoder's ability to process temporal and spatial information, we introduced two types of embeddings before the action sequences are passed into the ...
- **p. 3 / 3. Methods - extractive PDF cue:** Conv Residual VQ Encoder � Action sequence Conv Residual VQ Decoder � � q(�) Action Reconstruction Quantizer ⊕ - + Quantizer ⊕ - + VQVAE ...
- **p. 2 / 3. Methods - extractive PDF cue:** We use OpenVLA[26] as our backbone model.
- **p. 2 / 3. Methods - extractive PDF cue:** The method frames action prediction as a vision-language task, mapping input observation images and natural language instructions to discrete robot action sequences.
- **p. 3 / 3.2. Action Tokenizer via Residual VQ-VAE - extractive PDF cue:** To train the framework, we minimize the total loss L, a weighted combination of reconstruction loss Lrec, vector quantization (VQ) loss Lcodebook, and commitment loss ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive PDF cue:** The loss function is the standard next-token prediction loss, computed as the cross-entropy between the predicted token distribution ˆzi q and the ground truth token ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Specifically, we propose a convolutional residual VQVAE [5, 28, 52] framework for training action tokenizers.
- **p. 1 / 1. Introduction - extractive PDF cue:** To effectively train the model, we propose a progressive training strategy: Initially, we train the tokenizer on realworld robotic datasets, such as OpenX-Embodiment [34], which ...

## Source Evidence Cues

- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive PDF cue:** Instead of discretizing action sequences into uniform bins, the action sequence at:t+n is first processed through a pre-trained and frozen Residual VQVAE encoder ϕ(·), generating ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive PDF cue:** By leveraging hierarchical quantization with non-overlapping token ID ranges, the model achieves better action representation, avoids semantic confusion between layers, and ensures stable loss convergence ...
- **p. 3 / 3.3. Training Residual VQ-VAE - extractive PDF cue:** To improve the encoder's ability to process temporal and spatial information, we introduced two types of embeddings before the action sequences are passed into the ...
- **p. 3 / 3. Methods - extractive PDF cue:** Conv Residual VQ Encoder � Action sequence Conv Residual VQ Decoder � � q(�) Action Reconstruction Quantizer ⊕ - + Quantizer ⊕ - + VQVAE ...
- **p. 2 / 3. Methods - extractive PDF cue:** We use OpenVLA[26] as our backbone model.
- **p. 2 / 3. Methods - extractive PDF cue:** The method frames action prediction as a vision-language task, mapping input observation images and natural language instructions to discrete robot action sequences.
- **Detected method headings:** 3. Methods (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Instead of discretizing action sequences into uniform bins, the action sequence at:t+n is first processed through a pre-trained and frozen Residual VQVAE ... | p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | By leveraging hierarchical quantization with non-overlapping token ID ranges, the model achieves better action representation, avoids semantic confusion between layers, and ensures ... | p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 3 (3.3. Training Residual VQ-VAE) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To improve the encoder's ability to process temporal and spatial information, we introduced two types of embeddings before the action sequences are ... | p. 3 (3.3. Training Residual VQ-VAE), p. 3 (3. Methods) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.2. Action Tokenizer via Residual VQ-VAE - extractive PDF cue:** To train the framework, we minimize the total loss L, a weighted combination of reconstruction loss Lrec, vector quantization (VQ) loss Lcodebook, and commitment loss ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive PDF cue:** The loss function is the standard next-token prediction loss, computed as the cross-entropy between the predicted token distribution ˆzi q and the ground truth token ...
- **p. 3 / 3. Methods - extractive PDF cue:** Conv Residual VQ Encoder � Action sequence Conv Residual VQ Decoder � � q(�) Action Reconstruction Quantizer ⊕ - + Quantizer ⊕ - + VQVAE ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive PDF cue:** By leveraging hierarchical quantization with non-overlapping token ID ranges, the model achieves better action representation, avoids semantic confusion between layers, and ensures stable loss convergence ...
- **p. 2 / 3. Methods - extractive PDF cue:** OpenVLA's origin formulation is to adopt a discrete tokenization strategy for robot action prediction through fine-tuning the Prismatic7B VLM backbone.
- **p. 2 / 3. Methods - extractive PDF cue:** The method frames action prediction as a vision-language task, mapping input observation images and natural language instructions to discrete robot action sequences.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (3.2. Action Tokenizer via Residual VQ-VAE), p. 3 (3. Methods), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 2 (3. Methods).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | frames, action, prediction, vision-language, task, mapping, input, observation, images, natural, language, instructions, discrete, robot | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | frames, action, prediction, vision-language, task, mapping, input, observation, images, natural | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, follows, general, convolutional, residual, VQ-VAEbased, framework, action, tokenizers | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | train, framework, minimize, total, loss, weighted, combination, reconstruction, Lrec, vector | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3. Methods - extractive PDF cue:** The method frames action prediction as a vision-language task, mapping input observation images and natural language instructions to discrete robot action sequences.
- **p. 3 / 3. Methods - extractive PDF cue:** A: Input image Language Instruction VQ Decoder � language tokenizer task: Put all cups into the basket predicted robot actions XYZ positions, Euler angles, gripper ...
- **p. 4 / 3.3. Training Residual VQ-VAE - extractive PDF cue:** low-frequency and high-frequency temporal patterns in the input actions, improving its ability to represent finegrained temporal details. • Action-Type Embedding: Learnable embeddings were added for ...
- **p. 3 / 3.2. Action Tokenizer via Residual VQ-VAE - extractive PDF cue:** Given an input action sequence at:t+n ∈Rn×d, where n is the sequence length and d the action dimensionality, the encoder ϕenc, composed of 2D temporal ...
- **p. 4 / 3.3. Training Residual VQ-VAE - extractive PDF cue:** To train a more universal robot action tokenizer and reduce computational overhead, the model is trained using only action sequences as input, without additional conditional ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Tokenization plays a critical role in recent generative models, including large language models (LLMs) [1, 31], image and video generation models [17, 23, 39], and ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Compared to image patches and language tokens, action sequences are inherently easier to compress because of their spatio-temporal continuity.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | low-frequency and high-frequency temporal patterns in the input actions, improving its ability to represent finegrained temporal details. • Action-Type Embedding: Learnable embeddings ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The method frames action prediction as a vision-language task, mapping input observation images and natural language instructions to discrete robot action sequences. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Additionally, we fine-tune the original OpenVLA model on the LIBERO-90 dataset using LoRA as a baseline for comparison.For a fair comparison, all ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive PDF cue:** Instead of discretizing action sequences into uniform bins, the action sequence at:t+n is first processed through a pre-trained and frozen Residual VQVAE encoder ϕ(·), generating ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive PDF cue:** By leveraging hierarchical quantization with non-overlapping token ID ranges, the model achieves better action representation, avoids semantic confusion between layers, and ensures stable loss convergence ...
- **p. 5 / 4.1.1. Experiment Setup - extractive PDF cue:** Both models are trained on a single A100 GPU with a batch size of 1024, which takes about only 1 week.
- **p. 5 / 4.1.1. Experiment Setup - extractive PDF cue:** Additionally, we fine-tune the original OpenVLA model on the LIBERO-90 dataset using LoRA as a baseline for comparison.For a fair comparison, all fine-tuning on the ...
- **p. 4 / 3.3. Training Residual VQ-VAE - extractive PDF cue:** For example, training on the Open X-Embodiment dataset requires just one A100 GPU and is completed in one week.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Instead, discretizing, action, sequences, uniform, bins, sequence, first, processed, through, pre-trained, frozen, Residual, VQVAE, encoder, generating, latent, representations, leveraging, hierarchical.
- **Relevant PDF headings:** 3. Methods (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | In simulation, evaluations are performed on the LIBERO90 benchmark within the LIBERO dataset. | p. 6 (4.2.1. Experiment Setup), p. 4 (4.1.1. Experiment Setup) |
| Action / skill decoding | Additionally, the results show that VQO+L+M outperforms VQO+L, which in turn outperforms VQO, indicating the effectiveness of incorporating synthetic data during training ... | p. 7 (4.2.3. Performance on Long-Horizon Tasks), p. 5 (4.1.3. Scaling Data Improves VQ-VAE Action Tokenizer) |
| Receding execution / feedback | The evaluation results of residual VQ-VAE architectures.The results demonstrate that the Conv Residual VQ-VAE outperforms the MLP-based version, particularly when trained on ... | p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 4.3.2. Embedding Integration Effectiveness - extractive PDF cue:** To evaluate the impact of embeddings, we conducted an ablation study comparing the model's performance with and without embeddings.
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** In this section, we report some ablation studies to show the effectiveness of the design choices of our method.
- **p. 7 / 4.2.3. Performance on Long-Horizon Tasks - extractive PDF cue:** Additionally, the results show that VQO+L+M outperforms VQO+L, which in turn outperforms VQO, indicating the effectiveness of incorporating synthetic data during training without compromising real-world ...
- **p. 8 / 4.3.1. Action Chunking via VQ-VAE and Autoregressive - extractive PDF cue:** To evaluate the effectiveness of different action chunking strategies, we design ablation experiments comparing the autoregressive output of OpenVLA to the VQ-based action chunking method ...
- **p. 4 / 4. Experiments - extractive PDF cue:** We also investigate the impact of action tokenizers on the performance, inference speed, and long-horizon capabilities of VLA models, alongside ablation studies to evaluate key ...
- **p. 5 / 4.1.2. Effectiveness of Conv Residual VQ-VAE - extractive PDF cue:** Specifically, we used two variants of Residual VQ-VAE models: one with a simple MLP as the encoder and decoder, and the other with a larger ...
- **p. 5 / 4.1.3. Scaling Data Improves VQ-VAE Action Tokenizer - extractive PDF cue:** Furthermore, an ablation study using only ManiSkill data for training VQM resulted in substantially lower performance, underscoring the critical role of sufficient synthetic data scale. ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 3 (3.3. Training Residual VQ-VAE), p. 3 (3. Methods), p. 2 (3. Methods), p. 2 (3. Methods), objective p. 3 (3.2. Action Tokenizer via Residual VQ-VAE), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 3 (3. Methods), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 2 (3. Methods), p. 2 (3. Methods), temporal p. 4 (3.3. Training Residual VQ-VAE), p. 2 (3. Methods), p. 2 (2. Related Works), p. 3 (3.2. Action Tokenizer via Residual VQ-VAE), p. 3 (3.2. Action Tokenizer via Residual VQ-VAE), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
