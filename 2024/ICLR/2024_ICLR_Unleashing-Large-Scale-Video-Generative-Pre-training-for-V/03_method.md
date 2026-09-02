# Method - Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/2c37c5bcef24b9541550261dcd63261b-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2312.13139.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 14 (A.1 NETWORK AND TRAINING DETAILS), p. 14 (A.1 NETWORK AND TRAINING DETAILS)): Each trajectory consists of a language instruction and a sequence of observation images, robot states, and actions: τ = {l, o1, s1, a1, o2, s2, a2, ..., oT , sT ...

## Method Body Digest

- **p. 4 / 3 METHOD - extractive body cue:** Each trajectory consists of a language instruction and a sequence of observation images, robot states, and actions: τ = {l, o1, s1, a1, o2, s2, ...
- **p. 5 / 3 METHOD - extractive body cue:** Since the arm action is continuous, we use Smooth-L1 loss Larm for training.
- **p. 5 / 3 METHOD - extractive body cue:** 3.2.3 OUTPUTS For video prediction, we attach a transformer decoder consisting of self-attention blocks and multilayer perceptrons (MLPs).
- **p. 4 / 3 METHOD - extractive body cue:** We formulate multi-task language-conditioned visual robot manipulation as learning a model π that maps a language instruction l and a sequence of observation images ot-h:t ...
- **p. 14 / A.1 NETWORK AND TRAINING DETAILS - extractive body cue:** The output layer for video prediction is a transformer consisting of self-attention blocks and linear layers.
- **p. 14 / A.1 NETWORK AND TRAINING DETAILS - extractive body cue:** Hyperparameters for pre-training and finetuning on CALVIN data are shown in Tab 3.
- **p. 5 / 3 METHOD - extractive body cue:** Gripper actions are optimized using Binary Cross Entropy (BCE) loss Lgripper .
- **p. 5 / 3 METHOD - extractive body cue:** The network is optimized with causal video prediction loss Lvideo.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Key contributions of the paper includes: • We show that large-scale video generative pre-training is able to effectively benefit visual robot manipulation learning. • We ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Large-scale pre-training allows these models to learn general patterns from large datasets and thus enables them to easily generalize to related finetuning tasks with inherited ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose to leverage large-scale video generative pre-training for efficient and effective learning of multi-task visual robot manipulation.

## Source Evidence Cues

- **p. 4 / 3 METHOD - extractive body cue:** Each trajectory consists of a language instruction and a sequence of observation images, robot states, and actions: τ = {l, o1, s1, a1, o2, s2, ...
- **p. 5 / 3 METHOD - extractive body cue:** Since the arm action is continuous, we use Smooth-L1 loss Larm for training.
- **p. 5 / 3 METHOD - extractive body cue:** 3.2.3 OUTPUTS For video prediction, we attach a transformer decoder consisting of self-attention blocks and multilayer perceptrons (MLPs).
- **p. 4 / 3 METHOD - extractive body cue:** We formulate multi-task language-conditioned visual robot manipulation as learning a model π that maps a language instruction l and a sequence of observation images ot-h:t ...
- **p. 14 / A.1 NETWORK AND TRAINING DETAILS - extractive body cue:** The output layer for video prediction is a transformer consisting of self-attention blocks and linear layers.
- **p. 14 / A.1 NETWORK AND TRAINING DETAILS - extractive body cue:** Hyperparameters for pre-training and finetuning on CALVIN data are shown in Tab 3.
- **Detected method headings:** 3 METHOD (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Each trajectory consists of a language instruction and a sequence of observation images, robot states, and actions: τ = {l, o1, s1, ... | p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Since the arm action is continuous, we use Smooth-L1 loss Larm for training. | p. 5 (3 METHOD), p. 5 (3 METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | 3.2.3 OUTPUTS For video prediction, we attach a transformer decoder consisting of self-attention blocks and multilayer perceptrons (MLPs). | p. 5 (3 METHOD), p. 4 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 METHOD - extractive body cue:** Gripper actions are optimized using Binary Cross Entropy (BCE) loss Lgripper .
- **p. 5 / 3 METHOD - extractive body cue:** The network is optimized with causal video prediction loss Lvideo.
- **p. 4 / 3 METHOD - extractive body cue:** For action prediction, we learn an action prediction token MLP 𝑧! "slide left the red block" CLIP Text Encoder MLP MLP MLP 𝑧" 0.195 -0.102 ...
- **p. 14 / A.1 NETWORK AND TRAINING DETAILS - extractive body cue:** The output layer for action prediction is a three-layer MLP in which the last layer contains two heads for predicting arm actions and gripper actions, ...
- **p. 4 / 3 METHOD - extractive body cue:** Before being fed into the causal transformer, the embeddings of all modalities are passed through linear layers to align the dimension.
- **p. 14 / A.1 NETWORK AND TRAINING DETAILS - extractive body cue:** The causal transformer of GR-1 contains 12 layers and 12 heads with a hidden size of 384.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3 METHOD), p. 5 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | straightforward, GPT-style, model, takes, input, language, instruction, sequence, observation, images, robot, states, predicts, actions | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | straightforward, GPT-style, model, takes, input, language, instruction, sequence, observation, images | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Key, contributions, includes, large-scale, video, generative, pre-training, able, effectively, benefit | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Gripper, actions, optimized, Binary, Cross, Entropy, BCE, loss, Lgripper, network | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** 1), a straightforward GPT-style model which takes as input a language instruction, a sequence of observation images, and a sequence of robot states and predicts ...
- **p. 4 / 3 METHOD - extractive body cue:** Each trajectory consists of a language instruction and a sequence of observation images, robot states, and actions: τ = {l, o1, s1, a1, o2, s2, ...
- **p. 4 / 3 METHOD - extractive body cue:** We formulate multi-task language-conditioned visual robot manipulation as learning a model π that maps a language instruction l and a sequence of observation images ot-h:t ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Moreover, robot data is multi-modal, including images, robot states, actions, and language instructions.
- **p. 5 / 3 METHOD - extractive body cue:** The outputs from the [ACT] tokens are passed through linear layers to predict the arm and gripper actions (Fig.
- **p. 5 / 3 METHOD - extractive body cue:** The data for the large-scale video generative pre-training are sourced from the recently proposed Ego4D dataset (Grauman et al., 2022) which contains massive-scale human-object interactions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Robotics data is also generative in a sense that the observation is only revealed after the action is taken.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Specifically, we pre-train a model π to predict the video frame at timestep t + ∆t given the language description of the ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We formulate multi-task language-conditioned visual robot manipulation as learning a model π that maps a language instruction l and a sequence of ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 METHOD - extractive body cue:** Since the arm action is continuous, we use Smooth-L1 loss Larm for training.
- **p. 14 / A.1 NETWORK AND TRAINING DETAILS - extractive body cue:** Hyperparameters for pre-training and finetuning on CALVIN data are shown in Tab 3.
- **p. 15 / A.3 REAL ROBOT EXPERIMENTS - extractive body cue:** In both experiments, we use the same training setting as in the CALVIN experiments except that the batch size and training epochs are changed to ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** We freeze the R3M image encoder during training as in Nair et al.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** trajectory, consists, language, instruction, sequence, observation, images, robot, states, actions, ARCHITECTURE, GR-1, Fig, Since, action, continuous, Smooth-L1, loss, Larm, training.
- **Relevant PDF headings:** 3 METHOD (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 3) Can GR-1 handle challenging settings including small dataset, generalization to unseen scenes, generalization to unseen objects, and generalization to unseen languages? | p. 5 (4 EXPERIMENT), p. 5 (4 EXPERIMENT) |
| Action / skill decoding | GR-1 outperforms all the comparing baseline methods. | p. 7 (4 EXPERIMENT), p. 6 (4 EXPERIMENT) |
| Receding execution / feedback | GR-1 significantly outperforms all the comparing baseline methods, achieving a success rate of 77.8% and an average length of 2.00. | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |

## Failure and Ablation Link

- **p. 5 / 4 EXPERIMENT - extractive body cue:** Ablation studies and more results can be found in the appendix.
- **p. 5 / 4 EXPERIMENT - extractive body cue:** We also perform ablation studies to understand how different modules of GR-1 help visual robot manipulation learning.
- **p. 7 / 4 EXPERIMENT - extractive body cue:** MCIL and HULC are trained on the full CALVIN dataset containing data with and without language annotations.
- **p. 7 / 4 EXPERIMENT - extractive body cue:** And this is very important as it allows GR-1 to quickly learn skills without collecting a large amount of data.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of GR-1. GR-1 is first pre-trained on the task of video prediction with a large- scale video dataset. It is then finetuned ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 4: Ablation Studies. Pre-Training Video Prediction Data Tasks completed in a row 1 2 3
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 7: Ablation Studies. (a) We show the average length (averaged number of completed tasks in a row of 5) on CALVIN benchmark. (b) We ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 14 (A.1 NETWORK AND TRAINING DETAILS), p. 14 (A.1 NETWORK AND TRAINING DETAILS), objective p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 14 (A.1 NETWORK AND TRAINING DETAILS), p. 4 (3 METHOD), p. 14 (A.1 NETWORK AND TRAINING DETAILS), temporal p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 14 (A.1 NETWORK AND TRAINING DETAILS), p. 7 (4 EXPERIMENT).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
