# Method - 3D-VLA: A 3D Vision-Language-Action Generative World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://icml.cc/virtual/2024/poster/34575; PDF retrieval source: https://icml.cc/virtual/2024/poster/34575. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (4.3. Injecting Goal Generation Ability into 3D-VLA), p. 5 (4.2.2. INTERACTION TOKENS), p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION), p. 4 (4.1. Overview), p. 4 (4.1. Overview), p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION)): We first pretrain the embodied diffusion models in terms of different modalities such as images, depths and point clouds, and then align the decoders of these diffusion models to the ...

## Method Body Digest

- **p. 5 / 4.3. Injecting Goal Generation Ability into 3D-VLA - extractive body cue:** We first pretrain the embodied diffusion models in terms of different modalities such as images, depths and point clouds, and then align the decoders of ...
- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** To enhance the model's comprehension of 3D scenes and facilitate interaction within these environments, we introduce a novel set of interaction tokens.
- **p. 6 / 4.3.2. BRIDGING LLM AND GOAL GENERATION - extractive body cue:** Based on this, we can apply a transformer-based projector, which is capable of mapping the decoder features and embeddings from the Large Language Model (LLM) ...
- **p. 4 / 4.1. Overview - extractive body cue:** Next, we inject goal generation ability into 3D-VLA by first pretraining the embodied diffusion models and employing a projector for aligning the LLM and the ...
- **p. 4 / 4.1. Overview - extractive body cue:** As shown in Figure 2, we first build our backbone on top of 3D-LLM (Hong et al., 2023), and further enhance the model's capabilities to ...
- **p. 6 / 4.3.2. BRIDGING LLM AND GOAL GENERATION - extractive body cue:** To make training 3D-VLA more efficient and to avoid catastrophic forgetting, we utilize LoRA (Hu et al., 2021) to fine-tune different diffusion models.
- **p. 8 / 5.3. Embodied Action Planning - extractive body cue:** The results in the first row are sampled from the test set of held-in training data while the second row is the unseen environments gathered ...
- **p. 6 / 4.3.2. BRIDGING LLM AND GOAL GENERATION - extractive body cue:** We minimize both the LLM and DM denoising loss.

## Design Rationale

- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene.
- **p. 2 / 1. Introduction - extractive body cue:** To sum up, we have the following contributions: • We propose 3D-VLA, a new family of 3D vision-languageaction embodied foundation models that unify 3D perception, ...
- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** To enhance the model's comprehension of 3D scenes and facilitate interaction within these environments, we introduce a novel set of interaction tokens.

## Source Evidence Cues

- **p. 5 / 4.3. Injecting Goal Generation Ability into 3D-VLA - extractive body cue:** We first pretrain the embodied diffusion models in terms of different modalities such as images, depths and point clouds, and then align the decoders of ...
- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** To enhance the model's comprehension of 3D scenes and facilitate interaction within these environments, we introduce a novel set of interaction tokens.
- **p. 6 / 4.3.2. BRIDGING LLM AND GOAL GENERATION - extractive body cue:** Based on this, we can apply a transformer-based projector, which is capable of mapping the decoder features and embeddings from the Large Language Model (LLM) ...
- **p. 4 / 4.1. Overview - extractive body cue:** Next, we inject goal generation ability into 3D-VLA by first pretraining the embodied diffusion models and employing a projector for aligning the LLM and the ...
- **p. 4 / 4.1. Overview - extractive body cue:** As shown in Figure 2, we first build our backbone on top of 3D-LLM (Hong et al., 2023), and further enhance the model's capabilities to ...
- **p. 6 / 4.3.2. BRIDGING LLM AND GOAL GENERATION - extractive body cue:** To make training 3D-VLA more efficient and to avoid catastrophic forgetting, we utilize LoRA (Hu et al., 2021) to fine-tune different diffusion models.
- **p. 8 / 5.3. Embodied Action Planning - extractive body cue:** The results in the first row are sampled from the test set of held-in training data while the second row is the unseen environments gathered ...
- **Detected method headings:** 4. Methods (p. 4); 4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We first pretrain the embodied diffusion models in terms of different modalities such as images, depths and point clouds, and then align ... | p. 5 (4.3. Injecting Goal Generation Ability into 3D-VLA), p. 5 (4.2.2. INTERACTION TOKENS) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To enhance the model's comprehension of 3D scenes and facilitate interaction within these environments, we introduce a novel set of interaction tokens. | p. 5 (4.2.2. INTERACTION TOKENS), p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Based on this, we can apply a transformer-based projector, which is capable of mapping the decoder features and embeddings from the Large ... | p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION), p. 4 (4.1. Overview) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4.3.2. BRIDGING LLM AND GOAL GENERATION - extractive body cue:** We minimize both the LLM and DM denoising loss.
- **p. 5 / 4.3. Injecting Goal Generation Ability into 3D-VLA - extractive body cue:** Human beings pre-visualize the final states of the scenes to facilitate action prediction or decision making, which is a key aspect in building world models.
- **p. 7 / 5.3. Embodied Action Planning - extractive body cue:** Tasks We evaluate the ability of 3D-VLA for robot arm action prediction on two benchmarks, namely RLBench (James et al., 2020) and CALVIN (Mees et ...
- **p. 8 / 5.3. Embodied Action Planning - extractive body cue:** Evaluation of action planning on CALVIN dataset. matches the baseline performance in most tasks within the RLBench action prediction, showing its planning capability.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | D-VLA, Vision-Language-Action, Generative, World, Model, Robot, Actions, action, tokens, Control, Projector, Image, Point, Cloud | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | D-VLA, Vision-Language-Action, Generative, World, Model, Robot, Actions, action, tokens, Control | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Thirdly, better, encode, dynamics, framework, introduce, scene, tokens, enclose, embeddings | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | minimize, LLM, denoising, loss, Human, beings, pre-visualize, final, states, scenes | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1. Introduction - extractive body cue:** 3D-VLA: A 3D Vision-Language-Action Generative World Model Robot: Actions are: [action tokens] Robot Control Projector Image / Point Cloud Diffusion Model Initial State Goal State ...
- **p. 3 / 1. Introduction - extractive body cue:** This generated goal state can then be fed back to our model to guide the robot control. • Our 3D-VLA can conduct a series of ...
- **p. 5 / 4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS - extractive body cue:** We utilize our curated 3D-language video data to train a conditional diffusion model that edits the initial state modality based on instructions to generate the ...
- **p. 8 / 5.3. Embodied Action Planning - extractive body cue:** For RLBench, we compare our model 3DVLA with LanCon-Learn (Silva et al., 2021), which is a multi-task approach that can predict actions based on instruction-conditioned ...
- **p. 2 / 1. Introduction - extractive body cue:** To sum up, we have the following contributions: • We propose 3D-VLA, a new family of 3D vision-languageaction embodied foundation models that unify 3D perception, ...
- **p. 5 / 4.3.2. BRIDGING LLM AND GOAL GENERATION - extractive body cue:** Challenges remain as to how to seamlessly incorporate the pretrained decoders into the LLMs so that 3D-VLA could generate goals with regard to any pretrained ...
- **p. 8 / 5.3. Embodied Action Planning - extractive body cue:** 3D-VLA: A 3D Vision-Language-Action Generative World Model Move green chip bag near water bottle (RT-1) RT-1 Jaco Play Place the long bread on the table ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | For instance, when asking Runway (Esser et al., 2023) to generate future frames given the instruction "open the drawer", the entire scene ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training process. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.3. Injecting Goal Generation Ability into 3D-VLA - extractive body cue:** We first pretrain the embodied diffusion models in terms of different modalities such as images, depths and point clouds, and then align the decoders of ...
- **p. 4 / 4.1. Overview - extractive body cue:** Next, we inject goal generation ability into 3D-VLA by first pretraining the embodied diffusion models and employing a projector for aligning the LLM and the ...
- **p. 6 / 4.3.2. BRIDGING LLM AND GOAL GENERATION - extractive body cue:** To make training 3D-VLA more efficient and to avoid catastrophic forgetting, we utilize LoRA (Hu et al., 2021) to fine-tune different diffusion models.
- **p. 8 / 5.3. Embodied Action Planning - extractive body cue:** The results in the first row are sampled from the test set of held-in training data while the second row is the unseen environments gathered ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, pretrain, embodied, diffusion, models, terms, different, modalities, images, depths, point, clouds, then, align, decoders, embedding, space, D-VLA, through, alignment.
- **Relevant PDF headings:** 4. Methods (p. 4); 4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The tasks include 1) embodied QA on RoboVQA dataset (Sermanet et al., 2023); 2) task captioning on 11 Open-X datasets (Padalkar et ... | p. 6 (5.1. 3D Reasoning and Localization), p. 4 (3.1. Dataset Collection) |
| Action / skill decoding | Figure 2. Overview of our 3D-VLA pipeline. The left part shows our goal-generation capability. Our model can imagine the final state image ... | p. 3 (Figure/Table caption), p. 6 (5.1. 3D Reasoning and Localization) |
| Receding execution / feedback | Table 6. Evaluation of action planning on CALVIN dataset. matches the baseline performance in most tasks within the RLBench action prediction, showing ... | p. 8 (Figure/Table caption), p. 7 (5.1. 3D Reasoning and Localization) |

## Failure and Ablation Link

- **p. 3 / 3. 3D Embodied Instruction Tuning Dataset - extractive body cue:** Without 3D information, it is challenging for a robot to comprehend and execute the commands that require 3D spatial reasoning, such as "place the farthest ...
- **p. 4 / 3.3. Language Annotations - extractive body cue:** For tasks without pre-defined templates, ChatGPT is also asked to generate prompts and answers as language inputs and outputs of these tasks by itself.
- **p. 4 / 3.1. Dataset Collection - extractive body cue:** Therefore, we utilize several human-object interaction datasets, including datasets without depth information, such as Epic-Kitchens (Damen et al., 2018), and datasets with better 3D annotations, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Evaluation on reasoning ability using held-in data. ∗denotes zero-shot transfer results without training on our pre-train datasets. modal content to output. Between the ...
- **p. 7 / 5.1. 3D Reasoning and Localization - extractive body cue:** RGB image goal generation results. ∗denotes the model is trained on our pretrained dataset.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Examples from our 3D Embodied Instruction Tuning Dataset. added tokens enable our model to perform a wider range of embodied tasks and support ...
- **p. 5 / 4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS - extractive body cue:** FOR GOAL GENERATION To address the limitations of current diffusion models for goal generation in an embodied environment, we train RGBD to RGB-D and point-cloud ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4.3. Injecting Goal Generation Ability into 3D-VLA), p. 5 (4.2.2. INTERACTION TOKENS), p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION), p. 4 (4.1. Overview), p. 4 (4.1. Overview), p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION), objective p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION), p. 5 (4.3. Injecting Goal Generation Ability into 3D-VLA), p. 7 (5.3. Embodied Action Planning), p. 8 (5.3. Embodied Action Planning), temporal p. 5 (4.2.2. INTERACTION TOKENS), p. 5 (4.3. Injecting Goal Generation Ability into 3D-VLA), p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION), p. 7 (5.2. Multi-modal Goal Generation), p. 1 (1. Introduction), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Based on this, we can apply a transformer-based projector, which is capable of mapping the decoder features and embeddings from the Large Language Model (LLM) into the space of the ... (p. 6, 4.3.2. BRIDGING LLM AND GOAL GENERATION).
- **Objective/update evidence:** We minimize both the LLM and DM denoising loss. (p. 6, 4.3.2. BRIDGING LLM AND GOAL GENERATION).
- **Temporal/runtime evidence:** Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene. (p. 5, 4.2.2. INTERACTION TOKENS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
