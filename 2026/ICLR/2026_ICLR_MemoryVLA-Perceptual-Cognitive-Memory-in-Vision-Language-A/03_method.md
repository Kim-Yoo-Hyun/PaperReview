# Method - MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=54U3XHf7qq; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248101. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD)): Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = (a1, . . . , ...

## Method Body Digest

- **p. 4 / 3 METHOD - extractive body cue:** Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = ...
- **p. 6 / 3 METHOD - extractive body cue:** The combined representation is then refined through a feed-forward network to obtain the denoised action at that step.
- **p. 6 / 3 METHOD - extractive body cue:** Since real-world robotic actions lie in a continuous multimodal control space, we adopt a diffusion-based Transformer (DiT) (Peebles & Xie, 2023) implemented with Denoising Diffusion ...
- **p. 4 / 3 METHOD - extractive body cue:** The resulting representations are then fed into a memory-conditioned diffusion action expert to generate a sequence of N future 7-DoF actions.
- **p. 5 / 3 METHOD - extractive body cue:** (6) This attention operation is followed by a feed-forward network to complete one Transformer layer, and applying two such layers yields the final retrieved embeddings ...
- **p. 5 / 3 METHOD - extractive body cue:** The resulting memory-augmented features ˜p and ˜c are then forwarded to the memory consolidation stage.
- **p. 6 / 3 METHOD - extractive body cue:** The model is trained with mean squared error (MSE) loss between the predicted and target actions, and the final denoised vectors are passed through an ...
- **p. 6 / 3 METHOD - extractive body cue:** The pair with the highest similarity in each stream is selected and merged by averaging their vectors, thereby reducing redundancy. i∗ x = arg maxi=1,...,L-1 ...

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Drawing on cognitive science insights, we propose MemoryVLA (Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** For real-world evaluations, we introduce 12 tasks across Franka and WidowX robots, spanning 6 general tasks and 6 long-horizon temporal tasks.

## Source Evidence Cues

- **p. 4 / 3 METHOD - extractive body cue:** Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = ...
- **p. 6 / 3 METHOD - extractive body cue:** The combined representation is then refined through a feed-forward network to obtain the denoised action at that step.
- **p. 6 / 3 METHOD - extractive body cue:** Since real-world robotic actions lie in a continuous multimodal control space, we adopt a diffusion-based Transformer (DiT) (Peebles & Xie, 2023) implemented with Denoising Diffusion ...
- **p. 4 / 3 METHOD - extractive body cue:** The resulting representations are then fed into a memory-conditioned diffusion action expert to generate a sequence of N future 7-DoF actions.
- **p. 5 / 3 METHOD - extractive body cue:** (6) This attention operation is followed by a feed-forward network to complete one Transformer layer, and applying two such layers yields the final retrieved embeddings ...
- **p. 5 / 3 METHOD - extractive body cue:** The resulting memory-augmented features ˜p and ˜c are then forwarded to the memory consolidation stage.
- **Detected method headings:** 3 METHOD (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future ... | p. 4 (3 METHOD), p. 6 (3 METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The combined representation is then refined through a feed-forward network to obtain the denoised action at that step. | p. 6 (3 METHOD), p. 6 (3 METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Since real-world robotic actions lie in a continuous multimodal control space, we adopt a diffusion-based Transformer (DiT) (Peebles & Xie, 2023) implemented ... | p. 6 (3 METHOD), p. 4 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 METHOD - extractive body cue:** The model is trained with mean squared error (MSE) loss between the predicted and target actions, and the final denoised vectors are passed through an ...
- **p. 6 / 3 METHOD - extractive body cue:** The pair with the highest similarity in each stream is selected and merged by averaging their vectors, thereby reducing redundancy. i∗ x = arg maxi=1,...,L-1 ...
- **p. 5 / 3 METHOD - extractive body cue:** (c) Consolidation: the fused tokens are updated into PCMB.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 6 (3 METHOD), p. 5 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, current, RGB, image, language, instruction, parameterized, policy, outputs, sequence, future, actions, where, action | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Given, current, RGB, image, language, instruction, parameterized, policy, outputs, sequence | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, summarized, follows, Inspired, human, memory, systems, cognitive, science, MemoryVLA | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | model, trained, mean, squared, error, MSE, loss, between, predicted, target | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 METHOD - extractive body cue:** Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = ...
- **p. 4 / 3 METHOD - extractive body cue:** 3.1 OVERVIEW OF MEMORYVLA Problem Formulation We formulate robotic manipulation in VLA models as a sequential decision-making process, where visual observations and language instructions are ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** First, a vision encoder extracts perceptual tokens from observation, while a large language model (LLM) processes them together with the language instruction, leveraging commonsense priors ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** UniVLA (Bu et al., 2025b) incorporates past actions into input prompts, making an initial attempt at temporal modeling.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Vision-Language-Action (VLA) models (Brohan et al., 2023; Kim et al., 2024; Black et al., 2024; Li et al., 2024a; Sun et al., 2025; Xie et ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The brain encodes multi-modal sensory inputs into both perceptual and cognitive representations.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | However, this working memory only reflects the present timestep and lacks temporal dependencies. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Each memory entry is associated with its episode timestep via a sinusoidal embedding TE(·), which is added as positional encoding. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | However, this working memory only reflects the present timestep and lacks temporal dependencies. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For Long-horizon Temporal, each task uses 200-300 demonstrations and is evaluated with 10-15 trials using step-wise scoring to reflect progress over sub-goals. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Implementation Details We train on 8 NVIDIA A100 GPUs with PyTorch FSDP, using 32 samples per GPU for a global batch of 256 and a ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** At inference we use DDIM (Song et al., 2020) with 10 sampling steps and a classifier-free guidance(CFG) (Ho & Salimans, 2022) guidance scale of 1.5.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Standard 5 tasks are trained jointly for 20k steps, and validation is performed every 1k steps and results are reported at the best validation step.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Training runs for approximately 5k-20k steps depending on the task and data size.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Given, current, RGB, image, language, instruction, parameterized, policy, outputs, sequence, future, actions, where, action, consists, relative, translation, rotation, Euler, angles.
- **Relevant PDF headings:** 3 METHOD (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 4 overviews our evaluation across simulation and real-world, covering 3 robots, 6 benchmarks, 150+ tasks with 500+ variations. | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Action / skill decoding | Figure 1: (a) In Push Buttons tasks, pre- and post-push states look nearly identical, calling for temporal modeling. (b) Humans handle manipulation ... | p. 2 (Figure/Table caption), p. 7 (4 EXPERIMENTS) |
| Receding execution / feedback | Touch Medium Color3 Color5 Color9 Success CronusVLA (Li et al., 2025a) 32 5 31 13 9 18.0 SpatialVLA (Qu et al., 2025) ... | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 10 / Figure/Table caption - extractive body cue:** Table 6: Ablation on memory type and length. We report average success rates (%) on SimplerEnv-Bridge tasks. Variant Avg. Success Memory Type
- **p. 25 / Figure/Table caption - extractive body cue:** Table 9: Action Length Statistics across all simulation (SimplerEnv Bridge/Fractal, LIBERO Spa- tial/Object/Goal, LIBERO-10/90) and real-world (General, Temporal) task suites. For real-world tasks, the "Filtered" ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The Fractal testbed includes 336 variants, yielding 2,856 trials in total.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Note that MemoryVLA uses only third-person RGB, without wrist views or proprioceptive states.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** For methods without LIBERO-90 results, we report the average over the first four suites.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Pick Diverse Fruits comprises five variants with 5 trials per variant (25 total); all other General tasks use 15 trials.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 64.6 Both 71.9 Memory Length 4 67.7 16 71.9 64 67.7 Table 7: Ablation on memory retrieval, fusion, consolidation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), objective p. 6 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD), temporal p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
