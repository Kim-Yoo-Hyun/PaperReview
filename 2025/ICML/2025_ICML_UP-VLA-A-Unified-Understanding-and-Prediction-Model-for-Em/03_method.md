# Method - UP-VLA:  A Unified Understanding and Prediction Model for Embodied Agent

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=V7JPraxi5j; PDF retrieval source: https://openreview.net/pdf/a31d9729845e48950a82af3a4935b4f181940e6e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.3. Enhancing Action Learning with Joint Prediction), p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 5 (4.4.2. TRAINING OBJECTIVE), p. 3 (4.1. Backbone), p. 5 (4.4.2. TRAINING OBJECTIVE), p. 3 (4.2. Bridging Visual Prediction and Multi-modal)): Finally, we generate actions via joint prediction: ( ˆOt+∆t, ˆAt:t+∆t) = πP RE θ (Ot, L′) We use a small policy head to output low-level actions, consisting of a MAP ...

## Method Body Digest

- **p. 4 / 4.3. Enhancing Action Learning with Joint Prediction - extractive PDF cue:** Finally, we generate actions via joint prediction: ( ˆOt+∆t, ˆAt:t+∆t) = πP RE θ (Ot, L′) We use a small policy head to output low-level ...
- **p. 4 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** It takes the current visual scene and language instructions as inputs, produces a high-level understanding of the scene, and subsequently predicts future images and robotic ...
- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** For the future image prediction task, given M current image tokens vt = {vi}M i=0 N and instruction tokens l = {li}N i=0, we use ...
- **p. 3 / 4.1. Backbone - extractive PDF cue:** These projected image features are then concatenated with language embeddings and fed into the large language model.
- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** The discrete status aend of the end-effector is optimized with binary cross-entropy loss (BCE): LACT = X //ˆapos -apos//2 2 + BCE(ˆaend, aend) We use ...
- **p. 3 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** Unlike multi-modal understanding tasks, the objective in visual prediction is to encode future visual observation by focusing on the instruction prompts.
- **p. 6 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** A Unified Understanding and Prediction Model for Embodied Agent
- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** Given M visual tokens u = {ui}M i=0 and N text tokens l = {li}N i=0, we maximize the likelihood of the next token using ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** We introduce a novel training paradigm for VLA models that combines both vision-language understanding and future prediction objectives, enabling the capture of both high-level semantic ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Inspired by prior papers on visual pre-training (Wu et al., 2023; Guo et al., 2024), we introduce a novel training paradigm for VLA models that ...
- **p. 3 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** Meanwhile, we introduce a new special token PRE to denote this new task.

## Source Evidence Cues

- **p. 4 / 4.3. Enhancing Action Learning with Joint Prediction - extractive PDF cue:** Finally, we generate actions via joint prediction: ( ˆOt+∆t, ˆAt:t+∆t) = πP RE θ (Ot, L′) We use a small policy head to output low-level ...
- **p. 4 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** It takes the current visual scene and language instructions as inputs, produces a high-level understanding of the scene, and subsequently predicts future images and robotic ...
- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** For the future image prediction task, given M current image tokens vt = {vi}M i=0 N and instruction tokens l = {li}N i=0, we use ...
- **p. 3 / 4.1. Backbone - extractive PDF cue:** These projected image features are then concatenated with language embeddings and fed into the large language model.
- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** The discrete status aend of the end-effector is optimized with binary cross-entropy loss (BCE): LACT = X //ˆapos -apos//2 2 + BCE(ˆaend, aend) We use ...
- **p. 3 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** Unlike multi-modal understanding tasks, the objective in visual prediction is to encode future visual observation by focusing on the instruction prompts.
- **p. 6 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** A Unified Understanding and Prediction Model for Embodied Agent
- **Detected method headings:** 4. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Finally, we generate actions via joint prediction: ( ˆOt+∆t, ˆAt:t+∆t) = πP RE θ (Ot, L′) We use a small policy head ... | p. 4 (4.3. Enhancing Action Learning with Joint Prediction), p. 4 (4.2. Bridging Visual Prediction and Multi-modal) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | It takes the current visual scene and language instructions as inputs, produces a high-level understanding of the scene, and subsequently predicts future ... | p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 5 (4.4.2. TRAINING OBJECTIVE) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | For the future image prediction task, given M current image tokens vt = {vi}M i=0 N and instruction tokens l = {li}N ... | p. 5 (4.4.2. TRAINING OBJECTIVE), p. 3 (4.1. Backbone) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** Given M visual tokens u = {ui}M i=0 and N text tokens l = {li}N i=0, we maximize the likelihood of the next token using ...
- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** The discrete status aend of the end-effector is optimized with binary cross-entropy loss (BCE): LACT = X //ˆapos -apos//2 2 + BCE(ˆaend, aend) We use ...
- **p. 3 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** Unlike multi-modal understanding tasks, the objective in visual prediction is to encode future visual observation by focusing on the instruction prompts.
- **p. 4 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** A Unified Understanding and Prediction Model for Embodied Agent UP-VLA Model "What is on the table?" Future Images Tokenizer CLIP ViT Projector Language Understanding loss ...
- **p. 4 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** Robot Pose Continuous image tokens Discrete image tokens Text tokens Action Token UP-VLA Model VQ-GAN Codebook Instruction Tokenizer Copy Language Answer Autoregressive Generate Direct Generation ...
- **p. 3 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** Instead of using next token prediction, we model the future image tokens at the 3
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (4.2. Bridging Visual Prediction and Multi-modal), p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 5 (4.4.2. TRAINING OBJECTIVE), p. 5 (4.4.2. TRAINING OBJECTIVE).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, current, visual, scene, language, instructions, inputs, produces, high-level, understanding, subsequently, predicts, future, images | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | takes, current, visual, scene, language, instructions, inputs, produces, high-level, understanding | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | introduce, novel, training, paradigm, VLA, models, combines, vision-language, understanding, future | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Given, visual, tokens, text, maximize, likelihood, next, token, cross-entropy, loss | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** It takes the current visual scene and language instructions as inputs, produces a high-level understanding of the scene, and subsequently predicts future images and robotic ...
- **p. 4 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** Robot Pose Continuous image tokens Discrete image tokens Text tokens Action Token UP-VLA Model VQ-GAN Codebook Instruction Tokenizer Copy Language Answer Autoregressive Generate Direct Generation ...
- **p. 3 / 3. Preliminaries - extractive PDF cue:** Vision-LanguageAction (VLA) models typically train VLMπθ as a robotic action policy by minimizing the error between ˆa ∼πθ(o, l).
- **p. 3 / 4.2. Bridging Visual Prediction and Multi-modal - extractive PDF cue:** Future Visual Prediction For image prediction, given an image and instruction pair (Ot, L) at time t, we encode the current visual observation using a ...
- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** For the future image prediction task, given M current image tokens vt = {vi}M i=0 N and instruction tokens l = {li}N i=0, we use ...
- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive PDF cue:** The UP-VLA method involves three modeling targets: language modeling for multi-modal understanding, image modeling for visual prediction, and action modeling for embodied tasks.
- **p. 1 / 1. Introduction - extractive PDF cue:** Constructing Vision-Language-Action (VLA) models (Brohan et al., 2023; Li et al., 2023b) capable of solving multiple tasks in open environments has become a central focus ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Given the current observation-instruction pair (Ot, L), our model predicts both future observations and a sequence of actions at each time step: ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The expanded input prompt is: L′ = [E1(O′ t), πMMU θ (Ot, Lprompt), L] where L is the language instruction and O′ ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 5.3. Real Robot Evaluation - extractive PDF cue:** For real-world experimental results, we train RT-1 (Brohan et al., 2022), Diffusion Policy (Chi et al., 2023) on our datasets (using the open-source code and ...
- **p. 4 / 4.4. Training Strategy - extractive PDF cue:** During training, we fully fine-tune the parameters of the LLM and freeze all encoders.
- **p. 6 / 5.1. Experiment Setup and baseline - extractive PDF cue:** All baselines in our experiment are listed as below: • RT-1 (Brohan et al., 2022): a small robot action transformer using pretrained Efficient-Net (Tan & ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Finally, generate, actions, joint, prediction, small, policy, head, output, low-level, consisting, MAP, module, single-layer, attention, linear, layer, MLP, takes, current.
- **Relevant PDF headings:** 4. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | For real-world experimental results, we train RT-1 (Brohan et al., 2022), Diffusion Policy (Chi et al., 2023) on our datasets (using the ... | p. 7 (5.3. Real Robot Evaluation), p. 6 (5. Experiments) |
| Action / skill decoding | Compared to other baselines, which perform significantly worse on ABC→D than on ABCD→D, UP-VLA achieves higher completion lengths in both scenarios, indicating ... | p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation) |
| Receding execution / feedback | Compared to UPVLA-RT-2, which uses only action learning and achieves a completion length of 1.44, UP-VLA with visual prediction significantly improves the ... | p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Ablating components of UP-VLA. and UP-VLA-w/o-MMU-Condition, which omits the mech- anism described in sec 4.3 that extends visual prediction prompts using MMU. Table ...
- **p. 6 / 5.2. Simulation Evaluation - extractive PDF cue:** This suggests that relying solely on vision-language understanding pretraining can be limiting in tasks that emphasize visual generalization.
- **p. 6 / 5.2. Simulation Evaluation - extractive PDF cue:** This method initializes UP-VLA using a pure LLM, phi1.5 (Li et al., 2023c) and performs pretraining on the Bridge dataset for future prediction and is ...
- **p. 7 / 5.4. Ablation Studies - extractive PDF cue:** We compare the full UP-VLA with the following methods: UP-VLA-w/o-MMU, which does not utilize the LLava tuning dataset for multi-modal understanding, UPVLA-w/o-Bridge-Pretrain, which skips visual ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 7. Visualization of VQA results and predicted future images. Black, K., Nakamoto, M., Atreya, P., Walke, H., Finn, C., Kumar, A., and Levine, S. ...
- **p. 6 / 5.2. Simulation Evaluation - extractive PDF cue:** Our method addresses this limitation by incorporating visual prediction into the original VLA framework.
- **p. 6 / 5.2. Simulation Evaluation - extractive PDF cue:** Unlike UP-VLA, UP-VLA-phi-w/o-mmu does not include multi-modal understanding training, nor does it incorporate 6

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.3. Enhancing Action Learning with Joint Prediction), p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 5 (4.4.2. TRAINING OBJECTIVE), p. 3 (4.1. Backbone), p. 5 (4.4.2. TRAINING OBJECTIVE), p. 3 (4.2. Bridging Visual Prediction and Multi-modal), objective p. 5 (4.4.2. TRAINING OBJECTIVE), p. 5 (4.4.2. TRAINING OBJECTIVE), p. 3 (4.2. Bridging Visual Prediction and Multi-modal), p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 3 (4.2. Bridging Visual Prediction and Multi-modal), temporal p. 4 (4.3. Enhancing Action Learning with Joint Prediction), p. 4 (4.3. Enhancing Action Learning with Joint Prediction), p. 3 (4.2. Bridging Visual Prediction and Multi-modal), p. 3 (4.1. Backbone), p. 5 (4.4.1. TRAINING PIPELINE), p. 6 (5.2. Simulation Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
