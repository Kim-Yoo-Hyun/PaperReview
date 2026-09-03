# Method - Octo: An Open-Source Generalist Robot Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.12213; PDF retrieval source: https://arxiv.org/pdf/2405.12213. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL)): We use the t5-base (111M) model [74]. • Image observations and goals are passed through a shallow convolution stack, then split into a sequence of flattened patches [22].

## Method Body Digest

- **p. 4 / III. THE OCTO MODEL - extractive body cue:** We use the t5-base (111M) model [74]. • Image observations and goals are passed through a shallow convolution stack, then split into a sequence of ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Training objective We use a conditional diffusion decoding head to predict continuous, multi-modal action distributions [34, 17].
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** We use the same diffusion training objective during finetuning and update the full model, a recipe which outperformed those that freeze subsets of the pretrained ...
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** When adding new tasks, observations, or loss functions downstream, we can wholly retain the pretrained weights for the transformer, only adding new positional embeddings, a ...
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** Architecture At its core, Octo is a transformer-based policy π.
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** In this section, we describe the Octo model, our open-source generalist robot policy that can be adapted to new robots and tasks - including new ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** We use the AdamW optimizer [51] with an inverse square root decay learning rate schedule [97], with weight decay of 0.1 and gradient clipping of ...
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** We discuss the key design decisions, training objectives, training dataset, and infrastructure.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In principle, collected ∗Lead authors, ordered alphabetically, see Section A for list of contributions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our primary contribution is Octo, a transformer-based policy pretrained on the largest robot manipulation dataset to date: 800k robot demonstrations from the Open X-Embodiment dataset ...
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** It consists of three key parts: input tokenizers that transform

## Source Evidence Cues

- **p. 4 / III. THE OCTO MODEL - extractive body cue:** We use the t5-base (111M) model [74]. • Image observations and goals are passed through a shallow convolution stack, then split into a sequence of ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Training objective We use a conditional diffusion decoding head to predict continuous, multi-modal action distributions [34, 17].
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** We use the same diffusion training objective during finetuning and update the full model, a recipe which outperformed those that freeze subsets of the pretrained ...
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** When adding new tasks, observations, or loss functions downstream, we can wholly retain the pretrained weights for the transformer, only adding new positional embeddings, a ...
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** Architecture At its core, Octo is a transformer-based policy π.
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** In this section, we describe the Octo model, our open-source generalist robot policy that can be adapted to new robots and tasks - including new ...
- **Detected method headings:** III. THE OCTO MODEL (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We use the t5-base (111M) model [74]. • Image observations and goals are passed through a shallow convolution stack, then split into ... | p. 4 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Training objective We use a conditional diffusion decoding head to predict continuous, multi-modal action distributions [34, 17]. | p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We use the same diffusion training objective during finetuning and update the full model, a recipe which outperformed those that freeze subsets ... | p. 5 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / III. THE OCTO MODEL - extractive body cue:** We use the AdamW optimizer [51] with an inverse square root decay learning rate schedule [97], with weight decay of 0.1 and gradient clipping of ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** We use the same diffusion training objective during finetuning and update the full model, a recipe which outperformed those that freeze subsets of the pretrained ...
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** We discuss the key design decisions, training objectives, training dataset, and infrastructure.
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** When adding new tasks, observations, or loss functions downstream, we can wholly retain the pretrained weights for the transformer, only adding new positional embeddings, a ...
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** It also supports natural language instructions, goal images, observation histories, and multi-modal, chunked action prediction via diffusion decoding [17].
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** The attention pattern of the Octo transformer is block-wise masked: observation tokens can only attend causally to tokens from the same or earlier time steps ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | supports, natural, language, instructions, goal, images, observation, histories, multi-modal, chunked, action, prediction, diffusion, decoding | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | supports, natural, language, instructions, goal, images, observation, histories, multi-modal, chunked | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | principle, collected, Lead, authors, ordered, alphabetically, Section, list, contributions, primary | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | AdamW, optimizer, inverse, square, root, decay, learning, rate, schedule, weight | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. THE OCTO MODEL - extractive body cue:** It also supports natural language instructions, goal images, observation histories, and multi-modal, chunked action prediction via diffusion decoding [17].
- **p. 2 / I. INTRODUCTION - extractive body cue:** The core of our model is a transformer architecture that maps arbitrary input tokens (created from observations and tasks) to output tokens (then decoded into ...
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** Our design allows us to flexibly add new task and observation inputs or action output heads to the model during downstream finetuning.
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** In this section, we describe the Octo model, our open-source generalist robot policy that can be adapted to new robots and tasks - including new ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, while the individual components that comprise Octo - a transformer backbone, support for both language and goal image specification, and a diffusion head to ...
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** Task and observation tokenizers: We convert task definitions (e.g., language instructions ℓand goal images g) and observations o (e.g., wrist and third-person camera streams) into ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** We apply common image data augmentations during training, and randomly zero out the language instruction or goal image per training example to enable Octo to ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The attention pattern of the Octo transformer is block-wise masked: observation tokens can only attend causally to tokens from the same or ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Octo's design is inspired by several recent advances in robot imitation learning and scalable transformer training, including the use of denoising diffusion ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | We train using 2 frames of observation history; in our preliminary experiments, we found significantly diminishing gains beyond the first additional frame. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We train using 2 frames of observation history; in our preliminary experiments, we found significantly diminishing gains beyond the first additional frame. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Training objective We use a conditional diffusion decoding head to predict continuous, multi-modal action distributions [34, 17].
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** We use the same diffusion training objective during finetuning and update the full model, a recipe which outperformed those that freeze subsets of the pretrained ...
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** When adding new tasks, observations, or loss functions downstream, we can wholly retain the pretrained weights for the transformer, only adding new positional embeddings, a ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** The ViT-B was trained for 300k steps with a batch size of 2048 using a TPU v4-128 pod, which took 14 hours.
- **p. 6 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** A ViT-B visual encoder is initialized to the VC-1 weights [57], a state-of-the-art visual representation pretrained on 4,000 hours of ego-centric videos and ImageNet, and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** t5-base, model, Image, observations, goals, passed, through, shallow, convolution, stack, then, split, sequence, flattened, patches, Training, objective, conditional, diffusion, decoding.
- **Relevant PDF headings:** III. THE OCTO MODEL (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We evaluate Octo's capabilities to control robots in environments from the pretraining data out-of-the-box and to efficiently finetune to new tasks and ... | p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Action / skill decoding | On average across the six evaluation setups (detailed in Appendix F), Octo outperforms the next best baseline by 52%. | p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL) |
| Receding execution / feedback | Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are ... | p. 8 (Figure/Table caption), p. 7 (1) Can Octo control multiple robot embodiments and solve) |

## Failure and Ablation Link

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Model architecture. Left: Octo tokenizes task descriptions (green) and input observations (blue) using a pretrained language model and a lightweight CNN, respectively. Top: ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** For datasets without language annotations, we always use goal image conditioning.
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Training Details We trained two variants of our model: Octo-Small with a transformer backbone that mirrors the size of a ViT-S, and Octo-Base with a ...
- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** Unless noted otherwise, we perform all ablations on the OctoSmall model due to our compute budget.
- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** Aggregate Performance Octo-Small (Ours) 83% DATA RT-X dataset mix [67] 60% Single robot dataset (Bridge Data) 43% POLICY Discretized Action Prediction [67] 18% Continuous Action ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce Octo, an open-source, generalist policy for robotic manipulation. Octo is a transformer-based policy pretrained on 800k diverse robot episodes from the ...
- **p. 6 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** Out-of-the-box, Octo can control multiple robots in environments from the pretraining data.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), objective p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL), temporal p. 4 (III. THE OCTO MODEL), p. 3 (II. RELATED WORK), p. 5 (III. THE OCTO MODEL), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (I. INTRODUCTION), p. 3 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** When adding new tasks, observations, or loss functions downstream, we can wholly retain the pretrained weights for the transformer, only adding new positional embeddings, a new lightweight encoder, or the ... (p. 4, III. THE OCTO MODEL).
- **Objective/update evidence:** We use the AdamW optimizer [51] with an inverse square root decay learning rate schedule [97], with weight decay of 0.1 and gradient clipping of 1.0. (p. 5, III. THE OCTO MODEL).
- **Temporal/runtime evidence:** We train using 2 frames of observation history; in our preliminary experiments, we found significantly diminishing gains beyond the first additional frame. (p. 5, III. THE OCTO MODEL).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
