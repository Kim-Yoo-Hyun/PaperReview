# Method - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.15818; PDF retrieval source: https://arxiv.org/pdf/2307.15818. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3. Vision-Language-Action Models), p. 5 (3.2. Robot-Action Fine-tuning), p. 4 (3. Vision-Language-Action Models), p. 6 (3.2. Robot-Action Fine-tuning), p. 6 (3.2. Robot-Action Fine-tuning), p. 5 (3.1. Pre-Trained Vision-Language Models)): Then, we introduce the recipe and challenges of fine-tuning large VLMs that are pre-trained on web-scale data to directly output robot actions, becoming VLA models.

## Method Body Digest

- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** Then, we introduce the recipe and challenges of fine-tuning large VLMs that are pre-trained on web-scale data to directly output robot actions, becoming VLA models.
- **p. 5 / 3.2. Robot-Action Fine-tuning - extractive body cue:** The action space consists of 6-DoF positional and rotational displacement of the robot end-effector, as well as the level of extension of the robot gripper ...
- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** First, we describe the general architecture of our models and how they can be derived from models that are commonly used for vision-language tasks.
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** Thus, to ensure that RT-2 outputs valid action tokens during decoding, we constrain its output vocabulary via only sampling valid action tokens when the model ...
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** For the PaLM-E model, which does not provide this convenient representation of numbers, we simply overwrite the 256 least frequently used tokens to represent the ...
- **p. 5 / 3.1. Pre-Trained Vision-Language Models - extractive body cue:** We provide a detailed description of the architecture of these two models in Appendix D.
- **p. 2 / 1. Introduction - extractive body cue:** Although such models are typically trained to produce natural language tokens, we can train them on robotic trajectories by tokenizing the actions into text tokens ...
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** Taking the action representation described above, we convert our robot data to be suitable for VLM model fine-tuning, where our inputs include robot camera image ...

## Design Rationale

- **p. 3 / 1. Introduction - extractive body cue:** Our main contribution is RT-2, a family of models derived from fine-tuning large vision-language models trained on web-scale data to directly act as generalizable and ...
- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** In this section, we present our model family and the design choices for enabling training VLMs to directly perform closed-loop robot control.
- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** Then, we introduce the recipe and challenges of fine-tuning large VLMs that are pre-trained on web-scale data to directly output robot actions, becoming VLA models.

## Source Evidence Cues

- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** Then, we introduce the recipe and challenges of fine-tuning large VLMs that are pre-trained on web-scale data to directly output robot actions, becoming VLA models.
- **p. 5 / 3.2. Robot-Action Fine-tuning - extractive body cue:** The action space consists of 6-DoF positional and rotational displacement of the robot end-effector, as well as the level of extension of the robot gripper ...
- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** First, we describe the general architecture of our models and how they can be derived from models that are commonly used for vision-language tasks.
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** Thus, to ensure that RT-2 outputs valid action tokens during decoding, we constrain its output vocabulary via only sampling valid action tokens when the model ...
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** For the PaLM-E model, which does not provide this convenient representation of numbers, we simply overwrite the 256 least frequently used tokens to represent the ...
- **p. 5 / 3.1. Pre-Trained Vision-Language Models - extractive body cue:** We provide a detailed description of the architecture of these two models in Appendix D.
- **Detected method headings:** 3. Vision-Language-Action Models (p. 4); 3.1. Pre-Trained Vision-Language Models (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Then, we introduce the recipe and challenges of fine-tuning large VLMs that are pre-trained on web-scale data to directly output robot actions, ... | p. 4 (3. Vision-Language-Action Models), p. 5 (3.2. Robot-Action Fine-tuning) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The action space consists of 6-DoF positional and rotational displacement of the robot end-effector, as well as the level of extension of ... | p. 5 (3.2. Robot-Action Fine-tuning), p. 4 (3. Vision-Language-Action Models) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | First, we describe the general architecture of our models and how they can be derived from models that are commonly used for ... | p. 4 (3. Vision-Language-Action Models), p. 6 (3.2. Robot-Action Fine-tuning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Although, models, typically, trained, produce, natural, language, tokens, train, them, robotic, trajectories, tokenizing, actions | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Although, models, typically, trained, produce, natural, language, tokens, train, them | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | main, contribution, RT-2, family, models, derived, fine-tuning, large, vision-language, trained | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | not recovered | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Although such models are typically trained to produce natural language tokens, we can train them on robotic trajectories by tokenizing the actions into text tokens ...
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** Taking the action representation described above, we convert our robot data to be suitable for VLM model fine-tuning, where our inputs include robot camera image ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we explore an approach that is both simple and surprisingly effective: we directly train vision-language models designed for open-vocabulary visual question answering ...
- **p. 5 / 3.2. Robot-Action Fine-tuning - extractive body cue:** To enable vision-language models to control a robot, they must be trained to output actions.
- **p. 5 / 3.2. Robot-Action Fine-tuning - extractive body cue:** We take a direct approach to this problem, representing actions as tokens in the model's output, which are treated in the same way as language ...
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** Thus, to ensure that RT-2 outputs valid action tokens during decoding, we constrain its output vocabulary via only sampling valid action tokens when the model ...
- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** Then, we introduce the recipe and challenges of fine-tuning large VLMs that are pre-trained on web-scale data to directly output robot actions, becoming VLA models.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Due to its reduced size, the resulting model can run inference at a similar rate (5 Hz) as the other baselines. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | To reduce the variance of these experiment, we evaluate all of the methods using the A/B testing framework (Fisher, 1936), where all ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Due to its reduced size, the resulting model can run inference at a similar rate (5 Hz) as the other baselines. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** Then, we introduce the recipe and challenges of fine-tuning large VLMs that are pre-trained on web-scale data to directly output robot actions, becoming VLA models.
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** Thus, to ensure that RT-2 outputs valid action tokens during decoding, we constrain its output vocabulary via only sampling valid action tokens when the model ...
- **p. 7 / 4. Experiments - extractive body cue:** For all RT-2 training runs we adopt the hyperparameters from the original PaLI-X (Chen et al., 2023a) and PaLM-E (Driess et al., 2023) papers, including ...
- **p. 8 / 4. Experiments - extractive body cue:** Due to its reduced size, the resulting model can run inference at a similar rate (5 Hz) as the other baselines.
- **p. 10 / 4. Experiments - extractive body cue:** Inspired by the chain-of-thought prompting method in LLMs (Wei et al., 2022), we fine-tune a variant of RT-2 with PaLM-E for just a few hundred ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, introduce, recipe, challenges, fine-tuning, large, VLMs, pre-trained, web-scale, data, directly, output, robot, actions, becoming, VLA, models, action, space, consists.
- **Relevant PDF headings:** 3. Vision-Language-Action Models (p. 4); 3.1. Pre-Trained Vision-Language Models (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Each robot demonstration trajectory is annotated with a natural language instruction that describes the task performed, consisting of a verb describing the ... | p. 7 (4. Experiments), p. 8 (4. Experiments) |
| Action / skill decoding | We compare our method to multiple state-of-the-art baselines that challenge different aspects of our method. | p. 7 (4. Experiments), p. 8 (4. Experiments) |
| Receding execution / feedback | We observe that our VLA models significantly outperform the baselines across all categories, with our best RT-2-PaLI-X model achieving more than 3x ... | p. 9 (4. Experiments), p. 8 (4. Experiments) |

## Failure and Ablation Link

- **p. 10 / 4. Experiments - extractive body cue:** Inspired by the chain-of-thought prompting method in LLMs (Wei et al., 2022), we fine-tune a variant of RT-2 with PaLM-E for just a few hundred ...
- **p. 10 / 4. Experiments - extractive body cue:** In particular, we compare two different model sizes, 5B and 55B, as well as three different training routines: training a model from scratch, without using ...
- **p. 7 / 4. Experiments - extractive body cue:** To compare against state-of-the-art pretrained representations, we use VC-1 (Majumdar et al., 2023a) and R3M (Nair et al., 2022b), with policies implemented by training an ...
- **p. 8 / 4. Experiments - extractive body cue:** We co-fine-tune a smaller PaLI 3B model on several prediction tasks, including in-domain VQA tasks, for the Language-Table dataset, and evaluate the resulting policy in ...
- **p. 8 / 4. Experiments - extractive body cue:** The difference between the RT-2 models and the baseline is most pronounced in the various generalization experiments, suggesting that the strength of vision-language-action models lies ...
- **p. 9 / 4. Experiments - extractive body cue:** We refer to such capabilities as emergent, in the sense that they emerge by transferring Internet-scale pretraining.
- **p. 9 / 4. Experiments - extractive body cue:** The first we term symbol understanding, which explicitly tests whether the RT-2 policy transfers semantic knowledge from vision-language pretraining that was not present in any ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3. Vision-Language-Action Models), p. 5 (3.2. Robot-Action Fine-tuning), p. 4 (3. Vision-Language-Action Models), p. 6 (3.2. Robot-Action Fine-tuning), p. 6 (3.2. Robot-Action Fine-tuning), p. 5 (3.1. Pre-Trained Vision-Language Models), objective 본문 anchor 없음, temporal p. 8 (4. Experiments), p. 9 (4. Experiments), p. 10 (4. Experiments), p. 10 (4. Experiments), p. 6 (3.3. Real-Time Inference), p. 6 (3.3. Real-Time Inference).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
