# Method - Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Architecture), p. 3 (3. Method), p. 4 (3.1. Architecture), p. 4 (3.1. Architecture)): This design preserves the scalability of Transformer networks and enables denoising to be conditioned directly on image patches, thereby allowing the model to capture nuanced changes in action over historical ...

## Method Body Digest

- **p. 3 / 3.1. Architecture - extractive body cue:** This design preserves the scalability of Transformer networks and enables denoising to be conditioned directly on image patches, thereby allowing the model to capture nuanced ...
- **p. 3 / 3. Method - extractive body cue:** We then define the training objective for generating multi-modal actions.
- **p. 4 / 3.1. Architecture - extractive body cue:** The instruction tokens, image features, timestep embeddings, and noised action are concatenated to construct a token sequence, which is then fed into the network to ...
- **p. 4 / 3.1. Architecture - extractive body cue:** Our model employs a Transformer-based diffusion architecture, integrating a pretrained CLIP network to extract language instruction tokens.
- **p. 4 / 3.2. Training Objective - extractive body cue:** The optimization objective of Dita is to minimize the mean squared error (MSE) loss between xt and ˆxt.
- **p. 3 / 3.1. Architecture - extractive body cue:** In other words, we directly apply the diffusion objective in the action chunk space with a large Transformer model, in contrast to the diffusion action ...
- **p. 4 / 3.4. Pretraining Details - extractive body cue:** We employ the DDPM diffusion objective [25] with Ttrain = 1000 timesteps for pretraining, while adopting DDIM [69] with Teval = 20 timesteps during zero-shot ...
- **p. 2 / 1. Introduction - extractive body cue:** In pursuit of a unified robotic policy, recent studies have directly mapped visual observations and language instructions to actions using expansive VLA models for navigation ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce Dita, a Diffusion Transformer (DiT) Policy that capitalizes on the Transformer architecture, as demonstrated in prior work [8, 9, 32, ...
- **p. 3 / 3. Method - extractive body cue:** Finally, we present the data and implementation specifics for the pretraining of our model.
- **p. 3 / 3.1. Architecture - extractive body cue:** This design preserves the scalability of Transformer networks and enables denoising to be conditioned directly on image patches, thereby allowing the model to capture nuanced ...

## Source Evidence Cues

- **p. 3 / 3.1. Architecture - extractive body cue:** This design preserves the scalability of Transformer networks and enables denoising to be conditioned directly on image patches, thereby allowing the model to capture nuanced ...
- **p. 3 / 3. Method - extractive body cue:** We then define the training objective for generating multi-modal actions.
- **p. 4 / 3.1. Architecture - extractive body cue:** The instruction tokens, image features, timestep embeddings, and noised action are concatenated to construct a token sequence, which is then fed into the network to ...
- **p. 4 / 3.1. Architecture - extractive body cue:** Our model employs a Transformer-based diffusion architecture, integrating a pretrained CLIP network to extract language instruction tokens.
- **Detected method headings:** 3. Method (p. 3); 3.1. Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | This design preserves the scalability of Transformer networks and enables denoising to be conditioned directly on image patches, thereby allowing the model ... | p. 3 (3.1. Architecture), p. 3 (3. Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We then define the training objective for generating multi-modal actions. | p. 3 (3. Method), p. 4 (3.1. Architecture) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The instruction tokens, image features, timestep embeddings, and noised action are concatenated to construct a token sequence, which is then fed into ... | p. 4 (3.1. Architecture), p. 4 (3.1. Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Training Objective - extractive body cue:** The optimization objective of Dita is to minimize the mean squared error (MSE) loss between xt and ˆxt.
- **p. 3 / 3. Method - extractive body cue:** We then define the training objective for generating multi-modal actions.
- **p. 3 / 3.1. Architecture - extractive body cue:** In other words, we directly apply the diffusion objective in the action chunk space with a large Transformer model, in contrast to the diffusion action ...
- **p. 4 / 3.4. Pretraining Details - extractive body cue:** We employ the DDPM diffusion objective [25] with Ttrain = 1000 timesteps for pretraining, while adopting DDIM [69] with Teval = 20 timesteps during zero-shot ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.2. Training Objective), p. 3 (3. Method), p. 3 (3.1. Architecture), p. 4 (3.4. Pretraining Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | pursuit, unified, robotic, policy, recent, studies, have, directly, mapped, visual, observations, language, instructions, actions | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | pursuit, unified, robotic, policy, recent, studies, have, directly, mapped, visual | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | introduce, Dita, Diffusion, Transformer, DiT, Policy, capitalizes, architecture, demonstrated, prior | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | optimization, objective, Dita, minimize, mean, squared, error, MSE, loss, between | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** In pursuit of a unified robotic policy, recent studies have directly mapped visual observations and language instructions to actions using expansive VLA models for navigation ...
- **p. 3 / 1. Introduction - extractive body cue:** Remarkably, this promising performance is achieved exclusively with a single third-person camera input, while the model's inherent flexibility affords researchers the freedom to integrate additional ...
- **p. 3 / 3.1. Architecture - extractive body cue:** Dita only takes language instructions and third-person camera images as input.
- **p. 4 / 3.2. Training Objective - extractive body cue:** The denoising network Eω(clang, cobs, t, xt) is constructed upon a causal Transformer, where cobs represents the image observation, clang denotes the language instruction, and ...
- **p. 4 / 3.4. Pretraining Details - extractive body cue:** Based on preliminary experiments reported in ManiSkill2 [22], we utilize 2-frame image observations to predict 16 action chunks.
- **p. 2 / 1. Introduction - extractive body cue:** Other diffusion policies [30, 61, 72] attempt to integrate historical image observations and instructions into embeddings prior to the denoising process, which might limit the ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Specifically, we concatenate language tokens, image features, and timestep embeddings at the beginning of the sequence, treating the noisy action in conjunction ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The instruction tokens, image features, timestep embeddings, and noised action are concatenated to construct a token sequence, which is then fed into ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Training is conducted with a batch size of 8192 across 32 NVIDIA A100 GPUs, allocating 256 samples per GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Method - extractive body cue:** We then define the training objective for generating multi-modal actions.
- **p. 4 / 3.1. Architecture - extractive body cue:** Our model employs a Transformer-based diffusion architecture, integrating a pretrained CLIP network to extract language instruction tokens.
- **p. 4 / 3.4. Pretraining Details - extractive body cue:** Training is conducted with a batch size of 8192 across 32 NVIDIA A100 GPUs, allocating 256 samples per GPU.
- **p. 3 / 3. Method - extractive body cue:** Finally, we present the data and implementation specifics for the pretraining of our model.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** design, preserves, scalability, Transformer, networks, enables, denoising, conditioned, directly, image, patches, thereby, allowing, model, capture, nuanced, changes, action, over, historical.
- **Relevant PDF headings:** 3. Method (p. 3); 3.1. Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The results illustrate that Dita excels at discerning subtle visual nuances in long-horizon tasks and generalizes proficiently across diverse environments, effectively transferring ... | p. 6 (4.4. CALVIN), p. 4 (4. Simulation Experiments) |
| Action / skill decoding | We also implement RT-1 [8] style baseline model EDisc ω↑s with an architecture similar to ours for comparison. | p. 6 (4.4. CALVIN), p. 6 (4.4. CALVIN) |
| Receding execution / feedback | Overall, Dita achieves a 63.8% success rate on two-step 7692 | p. 7 (5.1. Real-Robot Task Finetuning), p. 5 (4.1. Baselines) |

## Failure and Ablation Link

- **p. 5 / 4.4. CALVIN - extractive body cue:** Furthermore, Dita surpasses its non-pretrained variant by a margin of 1.23, underscoring its superior transferability.
- **p. 5 / 4.1. Baselines - extractive body cue:** Success rate comparison with RT-1-X [8], Octo-Base [72] and OpenVLA-7B [32] on SimplerEnv (both match and variant results of Google Robot [8]).
- **p. 6 / 4.6. Ablation Study - extractive body cue:** In this section, we conduct an ablation study on key factors in the model architecture design, including observation length, trajectory length, and denoising steps.
- **p. 6 / 4.4. CALVIN - extractive body cue:** The results illustrate that Dita excels at discerning subtle visual nuances in long-horizon tasks and generalizes proficiently across diverse environments, effectively transferring knowledge from extensive, ...
- **p. 7 / 4.6. Ablation Study - extractive body cue:** Ablation on ManiSkill2 about the observation length (# obs) and the trajectory length (# traj). # obs # traj All PickC StackC S-YCB C-YCB EGAD ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We introduce Dita, an open-source, simple yet effective policy for generalist robotic learning. Pretrained on large-scale cross- embodiment datasets, Dita enables 10-shot adaptation ...
- **p. 4 / 4. Simulation Experiments - extractive body cue:** Across all four benchmarks, Dita pretrained on OXE datasets Eω↑OXE is evaluated in a zero-shot manner on SimplerEnv, while it is finetuned on the remaining ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Architecture), p. 3 (3. Method), p. 4 (3.1. Architecture), p. 4 (3.1. Architecture), objective p. 4 (3.2. Training Objective), p. 3 (3. Method), p. 3 (3.1. Architecture), p. 4 (3.4. Pretraining Details), temporal p. 3 (3.1. Architecture), p. 4 (3.1. Architecture), p. 4 (3.1. Architecture), p. 6 (4.6. Ablation Study), p. 7 (5.1. Real-Robot Task Finetuning), p. 7 (5.1. Real-Robot Task Finetuning).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
