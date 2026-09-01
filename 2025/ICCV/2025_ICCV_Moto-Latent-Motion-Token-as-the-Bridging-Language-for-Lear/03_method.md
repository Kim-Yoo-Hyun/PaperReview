# Method - Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Overview), p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.2. Latent Motion Tokenizer), p. 3 (3.2. Latent Motion Tokenizer)): 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for robot action policy.

## Method Body Digest

- **p. 3 / 3.1. Overview - extractive PDF cue:** 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive PDF cue:** The total action loss Laction is defined as: \math c al {L } _{act i on} = \mathcal {L} (\Delta x) + \mathcal {L} (\Delta ...
- **p. 4 / 3.2. Latent Motion Tokenizer - extractive PDF cue:** For de-tokenization, we use a ViT Decoder for image reconstruction, which takes the linearly embedded patches of o_{t-1} and recovers the pixel values for o_ ...
- **p. 3 / 3.2. Latent Motion Tokenizer - extractive PDF cue:** The output query features are then processed by a VQ codebook with a vocabulary size of 128 to produce discrete latent motion tokens.
- **p. 4 / 3.3. Motion Token Autoregressive Pre-training - extractive PDF cue:** The pre-training objective maximizes the likelihood of the ground-truth latent motion token sequence given the language instruction and the initial video frame: \math c a ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive PDF cue:** An MLP-based action head projects the output hidden state of each action query token into the real robot action space.
- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving ...
- **p. 4 / 3.3. Motion Token Autoregressive Pre-training - extractive PDF cue:** Additionally, we prepend the text features from the instruction and the visual features from the initial video frame as input prompts.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving ...
- **p. 3 / 3.1. Overview - extractive PDF cue:** 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive PDF cue:** To address this, during fine-tuning, we introduce special action query tokens into Moto-GPT's input, enabling the generation of real robot actions through a flexible action ...

## Source Evidence Cues

- **p. 3 / 3.1. Overview - extractive PDF cue:** 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive PDF cue:** The total action loss Laction is defined as: \math c al {L } _{act i on} = \mathcal {L} (\Delta x) + \mathcal {L} (\Delta ...
- **p. 4 / 3.2. Latent Motion Tokenizer - extractive PDF cue:** For de-tokenization, we use a ViT Decoder for image reconstruction, which takes the linearly embedded patches of o_{t-1} and recovers the pixel values for o_ ...
- **p. 3 / 3.2. Latent Motion Tokenizer - extractive PDF cue:** The output query features are then processed by a VQ codebook with a vocabulary size of 128 to produce discrete latent motion tokens.
- **Detected method headings:** 3. Methodology (p. 3); 5.3. Moto-GPT as an Effective Robot Policy (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and ... | p. 3 (3.1. Overview), p. 4 (3.4. Co-fine-tuning for Robot Manipulation) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The total action loss Laction is defined as: \math c al {L } _{act i on} = \mathcal {L} (\Delta x) + ... | p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.2. Latent Motion Tokenizer) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | For de-tokenization, we use a ViT Decoder for image reconstruction, which takes the linearly embedded patches of o_{t-1} and recovers the pixel ... | p. 4 (3.2. Latent Motion Tokenizer), p. 3 (3.2. Latent Motion Tokenizer) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive PDF cue:** The total action loss Laction is defined as: \math c al {L } _{act i on} = \mathcal {L} (\Delta x) + \mathcal {L} (\Delta ...
- **p. 4 / 3.3. Motion Token Autoregressive Pre-training - extractive PDF cue:** The pre-training objective maximizes the likelihood of the ground-truth latent motion token sequence given the language instruction and the initial video frame: \math c a ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.2. Latent Motion Tokenizer), p. 4 (3.4. Co-fine-tuning for Robot Manipulation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | MLP-based, action, head, projects, output, hidden, state, query, token, real, robot, space, summary, contributions | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | MLP-based, action, head, projects, output, hidden, state, query, token, real | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, below, Introduction, Latent, Motion, Tokens, model, visual, motions | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | total, action, loss, Laction, defined, math, mathcal, Delta, theta, grip | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive PDF cue:** An MLP-based action head projects the output hidden state of each action query token into the real robot action space.
- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving ...
- **p. 4 / 3.3. Motion Token Autoregressive Pre-training - extractive PDF cue:** Additionally, we prepend the text features from the instruction and the visual features from the initial video frame as input prompts.
- **p. 3 / 3.1. Overview - extractive PDF cue:** 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for ...
- **p. 3 / 3.1. Overview - extractive PDF cue:** Moto utilizes autoregressive generative pre-training on latent motion token sequences to learn motion priors from videos, followed by co-fine-tuning on action-labeled data for robot control.
- **p. 2 / 1. Introduction - extractive PDF cue:** Given the abundance of interaction-rich video data [1, 57], we ask: Can we leverage autoregressive pre-training on video data to improve robot learning?
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Specifically, N query tokens are added after the latent motion token chunk at each time step, where N corresponds to the number ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | For a video clip [o0, o1, ..., oT ], we derive a chunk of latent motion tokens for each pair of consecutive ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Len. is a comprehensive metric indicating the average number of tasks accomplished in a row across 1,000 trial sequences. "Static RGB" and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Overview - extractive PDF cue:** 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive PDF cue:** The total action loss Laction is defined as: \math c al {L } _{act i on} = \mathcal {L} (\Delta x) + \mathcal {L} (\Delta ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive PDF cue:** Illustration of real-world evaluation tasks. bles the policy inference of real robots if we take the codebook of latent motion tokens as an abstract action ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Moto, consists, three, stages, unsupervised, training, Latent, Motion, Tokenizer, pre-training, generative, model, MotoGPT, co-fine-tuning, robot, action, policy, total, loss, Laction.
- **Relevant PDF headings:** 3. Methodology (p. 3); 5.3. Moto-GPT as an Effective Robot Policy (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We conduct real-world evaluations with a FANUC LR Mate 200iD robot on three tasks: "pick-place banana", "close laptop", and "disassembly" (Fig. | p. 5 (4. Benchmarks and Datasets), p. 5 (4. Benchmarks and Datasets) |
| Action / skill decoding | Figure 8. Evaluation results in the real-world environment. also generalizes well in the unseen CALVIN environment, outperforming baseline models that use various ... | p. 7 (Figure/Table caption), p. 6 (5.3. Moto-GPT as an Effective Robot Policy) |
| Receding execution / feedback | 8, Moto-GPT consistently outperforms Moto w/o Motion Token on these tasks, improving the average success rate from 23.33% to Moto w/o Motion ... | p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |

## Failure and Ablation Link

- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** 11 shows that Moto-GPT fine-tuned with varying amounts of labeled data consistently outperforms its variant trained from scratch without latent motion tokens, especially with limited ...
- **p. 6 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** It significantly outperforms Moto w/o Motion Token, which is trained from scratch without latent motion tokens, underscoring the effectiveness of transferring motion priors learned from ...
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** Ablations on Policy Fine-tuning Methods.
- **p. 5 / 5. Experiments - extractive PDF cue:** To comprehensively evaluate the effectiveness of Moto, we study three key experimental questions: • Q1 (Interpretability): Does the Latent Motion Tokenizer learn interpretable latent motion ...
- **p. 6 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** After fine-tuning, Moto-GPT3 was evaluated on the SIMPLER and CALVIN benchmarks, demonstrating promising results as shown in Tables 2 and 3.
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive PDF cue:** Method Pick Coke Can Move Near Open / Close Drawer Overall Horizontal Vertical Standing Average Average Open Close Average Average RT-1-X [4] 0.820 0.330 0.550 ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. The overview of Moto, which utilizes Latent Motion Tokens as a bridging "language" for autoregressive pretraining on video data. The Moto-GPT pre-trained through ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Overview), p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.2. Latent Motion Tokenizer), p. 3 (3.2. Latent Motion Tokenizer), objective p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.3. Motion Token Autoregressive Pre-training), temporal p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.3. Motion Token Autoregressive Pre-training), p. 2 (1. Introduction), p. 3 (3.2. Latent Motion Tokenizer), p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner), p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
