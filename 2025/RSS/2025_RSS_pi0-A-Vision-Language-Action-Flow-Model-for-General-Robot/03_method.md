# Method - π0: A Vision-Language-Action Flow Model for General Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p010.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p010.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (IV. THE x MODEL), p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL), p. 4 (IV. THE x MODEL), p. 7 (A. Evaluating the base model), p. 7 (A. Evaluating the base model)): Formally, we want to model the data distribution p(A,/o,), where Ar = [ar,r¢1,.rs 11-1] corresponds to an action chunk of future actions (we use H ~ 50 for our tasks), ...

## Method Body Digest

- **p. 5 / IV. THE x MODEL - extractive body cue:** Formally, we want to model the data distribution p(A,/o,), where Ar = [ar,r¢1,.rs 11-1] corresponds to an action chunk of future actions (we use H ...
- **p. 5 / IV. THE x MODEL - extractive body cue:** In practice, the network is trained by sampling random noise « ~ \'(0, 1), computing the "noisy actions" Aj = rAy + (1 -r)e, and ...
- **p. 4 / IV. THE x MODEL - extractive body cue:** Our architecture is inspired by Transfusion [59], which trains a single transformer using multiple objectives, with tokens! corresponding to continuous outputs supervised via a flow ...
- **p. 4 / IV. THE x MODEL - extractive body cue:** We further augment this backbone with roboties-specific inputs and outputs - namely, proprioceptive state and robot actions.
- **p. 7 / A. Evaluating the base model - extractive body cue:** In our first set of experiments, we evaluate the model after pre-training on our full mixture, without any post-training, to evaluate how well our base ...
- **p. 7 / A. Evaluating the base model - extractive body cue:** OpenVLA struggles on these tasks because its autoregressive diseretization architecture does not support action chunks.
- **p. 8 / A. Evaluating the base model - extractive body cue:** Octo does support action chunks, but has a comparatively limited representational capacity.
- **p. 5 / IV. THE x MODEL - extractive body cue:** During training, we supervise these action tokens using a conditional flow matching loss [28, 32],

## Design Rationale

- **p. 4 / 1. INTRODUCTION - extractive body cue:** ‘of more complex and dexterous behaviors, such as tying shoelaces [58] or cooking shrimp [17], we show that our framework can leam very long tasks, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this paper, we present a prototype model and learning framework, which we call zo, that illustrates how each of these three bottlenecks could be ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The contributions of our work consist of a novel generalist robot policy architecture based on VLM pre-training and flow matching, and an empirical investigation of ...

## Source Evidence Cues

- **p. 5 / IV. THE x MODEL - extractive body cue:** Formally, we want to model the data distribution p(A,/o,), where Ar = [ar,r¢1,.rs 11-1] corresponds to an action chunk of future actions (we use H ...
- **p. 5 / IV. THE x MODEL - extractive body cue:** In practice, the network is trained by sampling random noise « ~ \'(0, 1), computing the "noisy actions" Aj = rAy + (1 -r)e, and ...
- **p. 4 / IV. THE x MODEL - extractive body cue:** Our architecture is inspired by Transfusion [59], which trains a single transformer using multiple objectives, with tokens! corresponding to continuous outputs supervised via a flow ...
- **p. 4 / IV. THE x MODEL - extractive body cue:** We further augment this backbone with roboties-specific inputs and outputs - namely, proprioceptive state and robot actions.
- **p. 7 / A. Evaluating the base model - extractive body cue:** In our first set of experiments, we evaluate the model after pre-training on our full mixture, without any post-training, to evaluate how well our base ...
- **p. 7 / A. Evaluating the base model - extractive body cue:** OpenVLA struggles on these tasks because its autoregressive diseretization architecture does not support action chunks.
- **p. 8 / A. Evaluating the base model - extractive body cue:** Octo does support action chunks, but has a comparatively limited representational capacity.
- **Detected method headings:** IV. THE x MODEL (p. 4); A. Evaluating the base model (p. 7); B. Model Architecture Details (p. 15); C. Non-VLM Baseline Architecture (p. 16); A. Evaluating the base model (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Formally, we want to model the data distribution p(A,/o,), where Ar = [ar,r¢1,.rs 11-1] corresponds to an action chunk of future actions ... | p. 5 (IV. THE x MODEL), p. 5 (IV. THE x MODEL) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In practice, the network is trained by sampling random noise « ~ \'(0, 1), computing the "noisy actions" Aj = rAy + ... | p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Our architecture is inspired by Transfusion [59], which trains a single transformer using multiple objectives, with tokens! corresponding to continuous outputs supervised ... | p. 4 (IV. THE x MODEL), p. 4 (IV. THE x MODEL) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. THE x MODEL - extractive body cue:** Our architecture is inspired by Transfusion [59], which trains a single transformer using multiple objectives, with tokens! corresponding to continuous outputs supervised via a flow ...
- **p. 5 / IV. THE x MODEL - extractive body cue:** During training, we supervise these action tokens using a conditional flow matching loss [28, 32],
- **p. 7 / A. Evaluating the base model - extractive body cue:** Due to time constraints, we were unable 0 train OpenVLA and Octo for the same number of epochs as our full model.
- **p. 5 / IV. THE x MODEL - extractive body cue:** Recent work in high-resolution image [4] and video [38] synthesis has shown that flow matching can achieve strong emPirical performance when combined with a simple ...
- **p. 8 / A. Evaluating the base model - extractive body cue:** 7: Out-of-box evaluation results: We evaluate 7p trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of updates ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (IV. THE x MODEL), p. 5 (IV. THE x MODEL), p. 7 (A. Evaluating the base model), p. 8 (A. Evaluating the base model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Formally, want, model, data, distribution, where, corresponds, action, chunk, future, actions, tasks, observation, consists | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Formally, want, model, data, distribution, where, corresponds, action, chunk, future | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | more, complex, dexterous, behaviors, tying, shoelaces, cooking, shrimp, framework, leam | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | architecture, inspired, Transfusion, trains, single, transformer, multiple, objectives, tokens, corresponding | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / IV. THE x MODEL - extractive body cue:** Formally, we want to model the data distribution p(A,/o,), where Ar = [ar,r¢1,.rs 11-1] corresponds to an action chunk of future actions (we use H ...
- **p. 4 / IV. THE x MODEL - extractive body cue:** We further augment this backbone with roboties-specific inputs and outputs - namely, proprioceptive state and robot actions.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We evaluate ‘our model out of the box with language commands, with fine-tuning to downstream tasks, and in combination with a high-level semantic policy that ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** While such models have been shown to exhibit broad instruction-following and problem-solving abilities (53, 27], they are not truly situated in a physical world the ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** This can resolve the data scarcity challenge, because many more sources of data are available to a generalist model - including data from other tasks, ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** This enables our model to control robots at frequencies of up to 50 Hz for dexterous tasks such as laundry folding (see Figure 1), To ...
- **p. 4 / 1. INTRODUCTION - extractive body cue:** To turn the base PaliGemma VLM_ into 7, we add action outputs that use flow matching [32, 28] to generate continuous action distributions.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | In contrast, our model employs a novel design that fine-tunes a VLM to produce actions via flow matching (52, 28], a variant ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | ur empirical evaluation studies tasks that combine dexterity, generalization, and temporally extended multi-stage behaviors. ur model incorporates Internet-scale vision-language model (VLM) pre-training ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | In contrast, our model employs a novel design that fine-tunes a VLM to produce actions via flow matching (52, 28], a variant ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / IV. THE x MODEL - extractive body cue:** In practice, the network is trained by sampling random noise « ~ \'(0, 1), computing the "noisy actions" Aj = rAy + (1 -r)e, and ...
- **p. 4 / IV. THE x MODEL - extractive body cue:** Our architecture is inspired by Transfusion [59], which trains a single transformer using multiple objectives, with tokens! corresponding to continuous outputs supervised via a flow ...
- **p. 7 / A. Evaluating the base model - extractive body cue:** In our first set of experiments, we evaluate the model after pre-training on our full mixture, without any post-training, to evaluate how well our base ...
- **p. 5 / A. Prectraining and post-training - extractive body cue:** Since each training example corresponds to a timestep - i.e. a tuple (0, A), - we will quantify data in terms of timesteps in this ...
- **p. 7 / VI. EXPERIMENTAL EVALUATION - extractive body cue:** 6: Out-of-box evaluation tasks: To evaluate our base ‘model, we run it after pre-training on five tasks: shirt folding, bussing easy, bussing hard, grocery bagging. ...
- **p. 8 / A. Evaluating the base model - extractive body cue:** 7: Out-of-box evaluation results: We evaluate 7p trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of updates ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Formally, want, model, data, distribution, where, corresponds, action, chunk, future, actions, tasks, observation, consists, multiple, RGB, images, language, command, robot.
- **Relevant PDF headings:** IV. THE x MODEL (p. 4); A. Evaluating the base model (p. 7); B. Model Architecture Details (p. 15); C. Non-VLM Baseline Architecture (p. 16); A. Evaluating the base model (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We study this question by directly evaluating 79, with comparisons to other robot foundation models. | p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Action / skill decoding | Fig. 7: Out-of-box evaluation results: We evaluate 7p trained for the full 700k steps, a version trained for 160k steps that ‘matches ... | p. 8 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Receding execution / feedback | Fig. 9: Language evaluation. We compare "flat" versions of ‘our policies, -#1at, which receive only the overall task com- mand (e.g, "bag ... | p. 9 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / VI. EXPERIMENTAL EVALUATION - extractive body cue:** How well does xo follow language commands? ‘These experiments compare xo to xo-Small, a smaller version of our ‘model without VLM initialization, to evaluate its ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Language evaluation. We compare "flat" versions of ‘our policies, -#1at, which receive only the overall task com- mand (e.g, "bag the groceries") with ...
- **p. 7 / VI. EXPERIMENTAL EVALUATION - extractive body cue:** In our final set of experiments, we fine-tune 9 to a set of particularly ‘complex tasks, including folding laundry and bussing a table.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 10: Fine-tuning evaluation tasks: We fine-tune our model to a variety of downstream tasks that are distinct from, the tasks seen in pre-training. Our ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Our generalist robot policy uses a pre-trained vision-language model (VLM) backbone, as well as a diverse cross- ‘embodiment dataset with a variety of ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: 79 controls a mobile manipulator to fold laundry. Our model is pre-trained on diverse data from 7 distinet robot configurations and 68 tasks, ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 11: Fine-tuning with varying amounts of data. =) can learn some easier tasks even with smaller amounts of data, and

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (IV. THE x MODEL), p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL), p. 4 (IV. THE x MODEL), p. 7 (A. Evaluating the base model), p. 7 (A. Evaluating the base model), objective p. 4 (IV. THE x MODEL), p. 5 (IV. THE x MODEL), p. 7 (A. Evaluating the base model), p. 5 (IV. THE x MODEL), p. 8 (A. Evaluating the base model), temporal p. 3 (1. INTRODUCTION), p. 11 (C. Learning new dexterous tasks), p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 5 (IV. THE x MODEL), p. 5 (IV. THE x MODEL).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
