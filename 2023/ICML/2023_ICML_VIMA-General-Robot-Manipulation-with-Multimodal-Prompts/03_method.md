# Method - VIMA: General Robot Manipulation with Multimodal Prompts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.03094; PDF retrieval source: https://arxiv.org/pdf/2210.03094. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4. Novel task generalization. New tasks with novel), p. 6 (5.1. Baselines), p. 2 (1. Introduction), p. 4 (6. Visual reasoning), p. 1 (1. Introduction), p. 5 (4. Novel task generalization. New tasks with novel)): To learn an effective multi-task robot policy, we propose VIMA, a robot agent with a multi-task encoderdecoder architecture and object-centric design (Fig.

## Method Body Digest

- **p. 4 / 4. Novel task generalization. New tasks with novel - extractive body cue:** To learn an effective multi-task robot policy, we propose VIMA, a robot agent with a multi-task encoderdecoder architecture and object-centric design (Fig.
- **p. 6 / 5.1. Baselines - extractive body cue:** Because there is no prior method that works out of the box with our multimodal prompting setup, we make our best effort to select a ...
- **p. 2 / 1. Introduction - extractive body cue:** The model architecture follows the encoderdecoder transformer design proven to be effective and scalable in NLP (Raffel et al., 2020).
- **p. 4 / 6. Visual reasoning - extractive body cue:** The controller is a causal transformer decoder consisting of alternating self and cross attention layers that predicts motor commands conditioned on prompts and interaction history.
- **p. 1 / 1. Introduction - extractive body cue:** Previously, different robot manipulation tasks required distinct policy architectures, objective functions, data pipelines, and training 1.
- **p. 5 / 4. Novel task generalization. New tasks with novel - extractive body cue:** 3), the robot controller (decoder) is conditioned on the prompt sequence P by a series of cross-attention layers between P and the trajectory history sequence ...
- **p. 1 / Abstract - extractive body cue:** We design a transformer-based robot agent, VIMA, that processes these prompts and outputs motor actions autoregressively.
- **p. 5 / 4. Novel task generalization. New tasks with novel - extractive body cue:** We follow behavioral cloning to train our models by minimizing the negative log-likelihood of predicted actions.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** To enable a single agent with all these capabilities, we make three key contributions in this work: 1) a novel multimodal prompting formulation that converts ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce the VisuoMotor Attention agent (VIMA) to learn robot manipulation from multimodal prompts.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce VIMA, an embodied agent capable of processing mulitimodal prompts (left) and controlling a robot arm to solve the task (right). procedures (Aceituno et ...

## Source Evidence Cues

- **p. 4 / 4. Novel task generalization. New tasks with novel - extractive body cue:** To learn an effective multi-task robot policy, we propose VIMA, a robot agent with a multi-task encoderdecoder architecture and object-centric design (Fig.
- **p. 6 / 5.1. Baselines - extractive body cue:** Because there is no prior method that works out of the box with our multimodal prompting setup, we make our best effort to select a ...
- **p. 2 / 1. Introduction - extractive body cue:** The model architecture follows the encoderdecoder transformer design proven to be effective and scalable in NLP (Raffel et al., 2020).
- **p. 4 / 6. Visual reasoning - extractive body cue:** The controller is a causal transformer decoder consisting of alternating self and cross attention layers that predicts motor commands conditioned on prompts and interaction history.
- **p. 1 / 1. Introduction - extractive body cue:** Previously, different robot manipulation tasks required distinct policy architectures, objective functions, data pipelines, and training 1.
- **p. 5 / 4. Novel task generalization. New tasks with novel - extractive body cue:** 3), the robot controller (decoder) is conditioned on the prompt sequence P by a series of cross-attention layers between P and the trajectory history sequence ...
- **p. 1 / Abstract - extractive body cue:** We design a transformer-based robot agent, VIMA, that processes these prompts and outputs motor actions autoregressively.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | To learn an effective multi-task robot policy, we propose VIMA, a robot agent with a multi-task encoderdecoder architecture and object-centric design (Fig. | p. 4 (4. Novel task generalization. New tasks with novel), p. 6 (5.1. Baselines) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Because there is no prior method that works out of the box with our multimodal prompting setup, we make our best effort ... | p. 6 (5.1. Baselines), p. 2 (1. Introduction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The model architecture follows the encoderdecoder transformer design proven to be effective and scalable in NLP (Raffel et al., 2020). | p. 2 (1. Introduction), p. 4 (6. Visual reasoning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4. Novel task generalization. New tasks with novel - extractive body cue:** We follow behavioral cloning to train our models by minimizing the negative log-likelihood of predicted actions.
- **p. 1 / 1. Introduction - extractive body cue:** Finally, to ensure safe deployment, we can further specify visual constraints like "do not enter <image> room".
- **p. 1 / 1. Introduction - extractive body cue:** Previously, different robot manipulation tasks required distinct policy architectures, objective functions, data pipelines, and training 1.
- **p. 3 / 5. Visual constraint satisfaction. The robot must ma - extractive body cue:** nipulate the objects carefully and avoid violating the (safety) constraints;
- **p. 4 / 6. Visual reasoning - extractive body cue:** Each task in VIMA-BENCH has a binary success criterion and does not provide partial reward.
- **p. 2 / 1. Introduction - extractive body cue:** The transformer decoder is conditioned on the prompt via cross-attention layers that alternate with the usual causal self-attention.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (5. Visual constraint satisfaction. The robot must ma).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Concretely, learn, robot, policy, at/P, where, denotes, past, interaction, history, observations, actions, steps, VIMA | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Concretely, learn, robot, policy, at/P, where, denotes, past, interaction, history | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | enable, single, agent, capabilities, make, three, contributions, novel, multimodal, prompting | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | follow, behavioral, cloning, train, models, minimizing, negative, log-likelihood, predicted, actions | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4. Novel task generalization. New tasks with novel - extractive body cue:** Concretely, we learn a robot policy π(at/P, H), where H := o1, a1, o2, a2, . . . , ot  denotes the past interaction ...
- **p. 2 / 1. Introduction - extractive body cue:** VIMA encodes an input sequence of interleaving textual and visual prompt tokens with a pre-trained language model (Tsimpoukelli et al., 2021) and decodes robot control ...
- **p. 6 / 5.1. Baselines - extractive body cue:** Input images are divided into patches and encoded by a ViT model to produce observation tokens.
- **p. 1 / 1. Introduction - extractive body cue:** We start with the observation that many robot manipulation tasks can be formulated by multimodal prompts that interleave language and images or video frames (Fig.
- **p. 3 / 2. Multimodal Prompts for Task Specification - extractive body cue:** Our key insight is that various task specification paradigms (such as goal conditioning, video demonstration, natural language instruction) can all be instantiated as multimodal prompts ...
- **p. 1 / Abstract - extractive body cue:** We design a transformer-based robot agent, VIMA, that processes these prompts and outputs motor actions autoregressively.
- **p. 3 / 6. Visual reasoning - extractive body cue:** Our simulator also features scripted oracle programs that can generate expert demonstrations by using privileged simulator state information, such as the precise location of all ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | VIMA encodes an input sequence of interleaving textual and visual prompt tokens with a pre-trained language model (Tsimpoukelli et al., 2021) and ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Concretely, we learn a robot policy π(at/P, H), where H := o1, a1, o2, a2, . . . , ot  denotes ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / 1. Introduction - extractive body cue:** Previously, different robot manipulation tasks required distinct policy architectures, objective functions, data pipelines, and training 1.
- **p. 2 / 1. Introduction - extractive body cue:** We open-source the simulation environment, training dataset, algorithm code, and pre-trained model checkpoints to ensure reproducibility and facilitate future work from the community.
- **p. 4 / 6. Visual reasoning - extractive body cue:** We encode the multimodal prompts with a pre-trained T5 model, and condition the robot controller on the prompt through cross-attention layers.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** learn, effective, multi-task, robot, policy, VIMA, agent, encoderdecoder, architecture, object-centric, design, Fig, Because, there, prior, works, multimodal, prompting, setup, make.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We compare VIMA against the baseline variants on four levels of generalization provided in our benchmark for different model and training dataset ... | p. 6 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results) |
| Action / skill decoding | Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. ... | p. 5 (Figure/Table caption), p. 7 (5.2. Evaluation Results) |
| Receding execution / feedback | Although models like VIMA-Gato and VIMA-Flamingo show improved performance with bigger model sizes, VIMA consistently achieves superior performance over all model sizes. | p. 6 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. Across all model ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Ablation on visual tokenizers. We compare the performance of VIMA-200M model across different visual tokenizers. Our proposed object tokens outperform all methods that ...
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly degrade the performance, ...
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** Finally, we compare the relative performance degradation as we test the models on progressively challenging zero-shot evaluation levels without further fine-tuning (Fig.
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** We compare VIMA against the baseline variants on four levels of generalization provided in our benchmark for different model and training dataset sizes.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Ablation on prompt conditioning. We compare our method (xattn: cross-attention prompt conditioning) with a vanilla transformer decoder (gpt-decoder) across different model sizes. Cross-attention ...
- **p. 41 / Figure/Table caption - extractive body cue:** Table 12: Data scaling when baseline variants' ViT is trained from scratch, indicated inside parentheses. ↑and ↓denote performance increase and decrease. Numbers in the first ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4. Novel task generalization. New tasks with novel), p. 6 (5.1. Baselines), p. 2 (1. Introduction), p. 4 (6. Visual reasoning), p. 1 (1. Introduction), p. 5 (4. Novel task generalization. New tasks with novel), objective p. 5 (4. Novel task generalization. New tasks with novel), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (5. Visual constraint satisfaction. The robot must ma), p. 4 (6. Visual reasoning), p. 2 (1. Introduction), temporal p. 2 (1. Introduction), p. 6 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 4 (4. Novel task generalization. New tasks with novel), p. 5 (4. Novel task generalization. New tasks with novel), p. 5 (4. Novel task generalization. New tasks with novel).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (48 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Previously, different robot manipulation tasks required distinct policy architectures, objective functions, data pipelines, and training. (p. 1, 1. Introduction).
- **Objective/update evidence:** Finally, to ensure safe deployment, we can further specify visual constraints like "do not enter <image> room". (p. 1, 1. Introduction).
- **Temporal/runtime evidence:** We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly degrade the performance, especially in the low model ... (p. 6, 5.2. Evaluation Results).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
