# Method - OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=UHF0km7R5M; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167304. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Model Architecture), p. 5 (3.2. Model Architecture), p. 4 (3.2. Model Architecture), p. 5 (3.2. Model Architecture)): We first describe how OTTER utilizes the vision-language alignment of pre-trained vision and language encoders to extract text-aware vision features, then provide a more detailed explanation of the model architecture.

## Method Body Digest

- **p. 3 / 3. Method - extractive body cue:** We first describe how OTTER utilizes the vision-language alignment of pre-trained vision and language encoders to extract text-aware vision features, then provide a more detailed ...
- **p. 3 / 3. Method - extractive body cue:** We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM.
- **p. 4 / 3.2. Model Architecture - extractive body cue:** Policy Network and Action Head OTTER uses a transformer as the policy network, consisting of 4 layers and 8 heads, with a hidden dimension of ...
- **p. 5 / 3.2. Model Architecture - extractive body cue:** OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction Figure 4: Example scenes in the simulation (left) and in the physical environments (right) using a ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** For each output token at a given timestep, we use a FFN to predict the next 12 actions.
- **p. 5 / 3.2. Model Architecture - extractive body cue:** Through experimentation, we determined that an action horizon of 8 steps yields optimal performance.
- **p. 3 / 3.1. Text-Aware Visual Feature Extraction - extractive body cue:** Specifically, we use the similarity scores to select and combine visual features that best align with the task instruction, creating compact representations for downstream action ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** This token serves as input to a policy network for action prediction.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by language ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose OTTER, a VLA model that leverages the semantic alignment capabilities of pre-trained VLMs for better generalization.
- **p. 3 / 3. Method - extractive body cue:** We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM.

## Source Evidence Cues

- **p. 3 / 3. Method - extractive body cue:** We first describe how OTTER utilizes the vision-language alignment of pre-trained vision and language encoders to extract text-aware vision features, then provide a more detailed ...
- **p. 3 / 3. Method - extractive body cue:** We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM.
- **p. 4 / 3.2. Model Architecture - extractive body cue:** Policy Network and Action Head OTTER uses a transformer as the policy network, consisting of 4 layers and 8 heads, with a hidden dimension of ...
- **p. 5 / 3.2. Model Architecture - extractive body cue:** OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction Figure 4: Example scenes in the simulation (left) and in the physical environments (right) using a ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** For each output token at a given timestep, we use a FFN to predict the next 12 actions.
- **p. 5 / 3.2. Model Architecture - extractive body cue:** Through experimentation, we determined that an action horizon of 8 steps yields optimal performance.
- **Detected method headings:** 2.2. Vision Language Action Models (p. 3); 3. Method (p. 3); 3.2. Model Architecture (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We first describe how OTTER utilizes the vision-language alignment of pre-trained vision and language encoders to extract text-aware vision features, then provide ... | p. 3 (3. Method), p. 3 (3. Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM. | p. 3 (3. Method), p. 4 (3.2. Model Architecture) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Policy Network and Action Head OTTER uses a transformer as the policy network, consisting of 4 layers and 8 heads, with a ... | p. 4 (3.2. Model Architecture), p. 5 (3.2. Model Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Text-Aware Visual Feature Extraction - extractive body cue:** Specifically, we use the similarity scores to select and combine visual features that best align with the task instruction, creating compact representations for downstream action ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** This token serves as input to a policy network for action prediction.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Different, input, modalities, usually, encoded, separate, tokens, multi-view, images, visual, feature, extractors, along, tokenized | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Different, input, modalities, usually, encoded, separate, tokens, multi-view, images, visual | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | OTTER, novel, VLA, architecture, freezes, pre-trained, vision, language, encoders, extracts | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Specifically, similarity, scores, select, combine, visual, features, best, align, task | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive body cue:** Different input modalities are usually encoded into separate tokens: multi-view images encoded via visual feature extractors, along with tokenized language instructions, optionally with the robot's ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** This token serves as input to a policy network for action prediction.
- **p. 3 / 3. Method - extractive body cue:** We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM.
- **p. 1 / 1. Introduction - extractive body cue:** (b) Text-Aware Feature Extraction: the proposed approach, OTTER, extracts visual tokens that correspond to the text tokens, and then feeds them into the policy.
- **p. 3 / 3.1. Text-Aware Visual Feature Extraction - extractive body cue:** Specifically, we use the similarity scores to select and combine visual features that best align with the task instruction, creating compact representations for downstream action ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** For each output token at a given timestep, we use a FFN to predict the next 12 actions.
- **p. 5 / 3.2. Model Architecture - extractive body cue:** OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction Figure 4: Example scenes in the simulation (left) and in the physical environments (right) using a ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | When executing the predicted actions, we employ temporal ensembling (Zhao et al., 2023) in conjunction with receding horizon control (Chi et al., ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | At time step t, we concatenate the embodiment feature fe with the perception feature f ′ l and f ′ vl along ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | For a fair comparison, we extended the context history length of Octo to 10 (Octo cannot exceed a context length of 10 ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Through experimentation, we determined that an action horizon of 8 steps yields optimal performance. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Method - extractive body cue:** We first describe how OTTER utilizes the vision-language alignment of pre-trained vision and language encoders to extract text-aware vision features, then provide a more detailed ...
- **p. 3 / 3. Method - extractive body cue:** We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM.
- **p. 6 / 5.1. Real-world Experiments - extractive body cue:** For fair comparisons, we fine-tune Octo and OpenVLA on DS-PnP using the same amount of learning steps.
- **p. 6 / 4.2. Baselines - extractive body cue:** For each model, we conduct physical robot pick and place experiments, with 100 trials on in-distribution training tasks and 70 trials on unseen tasks.
- **p. 7 / 5.1. Real-world Experiments - extractive body cue:** The results further suggest that OTTER's generalization capabilities can be enhanced through increased model capacity (OTTER-L) and pre-training on large robotic datasets (OTTER-OXE). on unseen ...
- **p. 7 / 5.1. Real-world Experiments - extractive body cue:** Err. π0-Fast-Droid 0% 0% 0% 61% 29% ± 3.5% Finetuned π0-Fast-Droid 0% 45% 27% 51% 35% ± 3.8% Finetuned Octo 0% 0% 0% 5% 4% ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, describe, OTTER, utilizes, vision-language, alignment, pre-trained, vision, language, encoders, extract, text-aware, features, then, provide, more, detailed, explanation, model, architecture.
- **Relevant PDF headings:** 2.2. Vision Language Action Models (p. 3); 3. Method (p. 3); 3.2. Model Architecture (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We collect robotic datasets on multi-task scenes using a Franka robot, where there are multiple tasks that can be completed in the ... | p. 5 (4.1. Environment Setup), p. 6 (5.1. Real-world Experiments) |
| Action / skill decoding | Table 3: Simulation results on LIBERO. We evaluate OTTER and other baselines on 30 in-distribution tasks in LIBERO- Spatial/Object/Goal and on 10 ... | p. 8 (Figure/Table caption), p. 5 (4.2. Baselines) |
| Receding execution / feedback | OTTER achieves a similar success rate on the in-distribution training tasks and unseen tasks, significantly outperforming the baselines, highlighting the benefits of ... | p. 6 (4.2. Baselines), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Simulation results on LIBERO. We evaluate OTTER and other baselines on 30 in-distribution tasks in LIBERO- Spatial/Object/Goal and on 10 unseen tasks we ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 7: Examples of attention maps of frozen CLIP's attention features (Xattn) on Open-X dataset. The bottom texts are the corresponding text tokens. D. More ...
- **p. 5 / 4.2. Baselines - extractive body cue:** To evaluate if the text-aware visual features extracted in OTTER can better leverage the semantic understanding capabilities of the pre-trained VLMs, we consider four baselines ...
- **p. 6 / 4.2. Baselines - extractive body cue:** Direct Feature Passing OTTER (DFP-OTTER): a variant of OTTER where the text tokens, vision tokens are passed to an attention pooling layer separately to obtain ...
- **p. 7 / 5.3. Ablations - extractive body cue:** Addition ablation studies can be found in Appendix D.
- **p. 7 / 5.3. Ablations - extractive body cue:** We consider the following ablations on the design choices of OTTER.
- **p. 6 / 5.1. Real-world Experiments - extractive body cue:** We compare the performance of Octo and OpenVLA finetuned on DS-ALL and OTTER pretrained on OXE and fine-tuned on DS-ALL, denoted as OTTER-OXE.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Model Architecture), p. 5 (3.2. Model Architecture), p. 4 (3.2. Model Architecture), p. 5 (3.2. Model Architecture), objective p. 3 (3.1. Text-Aware Visual Feature Extraction), p. 4 (3.2. Model Architecture), temporal p. 5 (3.2. Model Architecture), p. 4 (3.2. Model Architecture), p. 4 (3.2. Model Architecture), p. 5 (3.2. Model Architecture), p. 6 (5.1. Real-world Experiments), p. 6 (5.1. Real-world Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
