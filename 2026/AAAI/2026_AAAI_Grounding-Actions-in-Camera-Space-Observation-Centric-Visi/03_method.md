# Method - Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38947; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38947. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD)): While these representations are widely used as supervision signals for Vision-Language-Action (VLA) models, they are tightly coupled with specific robot embodiment configurations, rather than being derived from the observation space.

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** While these representations are widely used as supervision signals for Vision-Language-Action (VLA) models, they are tightly coupled with specific robot embodiment configurations, rather than being ...
- **p. 3 / III. METHOD - extractive body cue:** Consequently, it is difficult for the model to achieve a reasonable projection from image observation to corresponding actions, and thus the model generalization is limited, ...
- **p. 4 / III. METHOD - extractive body cue:** For instance, Droid [9] features 1417 distinct camera viewpoints, requiring the model to internally infer the correct transformation T for each view to predict actions ...
- **p. 2 / III. METHOD - extractive body cue:** We then analyze the differences between camera-coordinate and robotcoordinate optimization.
- **p. 2 / III. METHOD - extractive body cue:** In this section, we provide a detailed overview of OCVLA, i.e., grounding actions in the observation (camera) space.
- **p. 4 / III. METHOD - extractive body cue:** matrix T to be driven from representations in observation space.
- **p. 3 / III. METHOD - extractive body cue:** Meanwhile, given an end-effector pose Pworld of the robot, we can get, Pcam = TPworld (5) Equations 4 and 5 present that both the end ...
- **p. 3 / III. METHOD - extractive body cue:** In details, we can get Acam from equations 1, 2 and 3 as follow, Acam = TAworldT-1 (4) where Acam is the camera-based action, Aworld ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Notably, our method exhibits markedly improved adaptability to previously unseen camera viewarXiv:2508.13103v1 [cs.RO] 18 Aug 2025
- **p. 2 / I. INTRODUCTION - extractive body cue:** We introduce the Observation-Centric VLA (OC-VLA) framework.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** While these representations are widely used as supervision signals for Vision-Language-Action (VLA) models, they are tightly coupled with specific robot embodiment configurations, rather than being ...
- **p. 3 / III. METHOD - extractive body cue:** Consequently, it is difficult for the model to achieve a reasonable projection from image observation to corresponding actions, and thus the model generalization is limited, ...
- **p. 4 / III. METHOD - extractive body cue:** For instance, Droid [9] features 1417 distinct camera viewpoints, requiring the model to internally infer the correct transformation T for each view to predict actions ...
- **p. 2 / III. METHOD - extractive body cue:** We then analyze the differences between camera-coordinate and robotcoordinate optimization.
- **p. 2 / III. METHOD - extractive body cue:** In this section, we provide a detailed overview of OCVLA, i.e., grounding actions in the observation (camera) space.
- **p. 4 / III. METHOD - extractive body cue:** matrix T to be driven from representations in observation space.
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | While these representations are widely used as supervision signals for Vision-Language-Action (VLA) models, they are tightly coupled with specific robot embodiment configurations, ... | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Consequently, it is difficult for the model to achieve a reasonable projection from image observation to corresponding actions, and thus the model ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | For instance, Droid [9] features 1417 distinct camera viewpoints, requiring the model to internally infer the correct transformation T for each view ... | p. 4 (III. METHOD), p. 2 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** Meanwhile, given an end-effector pose Pworld of the robot, we can get, Pcam = TPworld (5) Equations 4 and 5 present that both the end ...
- **p. 3 / III. METHOD - extractive body cue:** In details, we can get Acam from equations 1, 2 and 3 as follow, Acam = TAworldT-1 (4) where Acam is the camera-based action, Aworld ...
- **p. 2 / III. METHOD - extractive body cue:** We begin with the model structure and action modeling as preliminaries, followed by an introduction to the camera-centric action prediction approach.
- **p. 2 / III. METHOD - extractive body cue:** Preliminary: Model Structure, Action Modeling Vision-language-action (VLA) models have converged toward a common architectural pattern [3], [2], [5], [6], where action prediction is built upon ...
- **p. 4 / III. METHOD - extractive body cue:** As a result, learning this translation for robot space action prediction becomes more challenging due to the diversity in camera poses.
- **p. 4 / III. METHOD - extractive body cue:** In contrast, observationcentric action prediction inherently avoids these issues, offering a more consistent mapping between observation and action.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (III. METHOD), p. 3 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | OC-VLA, transforms, effector, pose, whether, defined, discrete, continuous, action, space, robot, base, coordinate, third-person | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | OC-VLA, transforms, effector, pose, whether, defined, discrete, continuous, action, space | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | address, issues, novel, paradigm, decouples, end-effector, action, robot, base, coordinate | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Meanwhile, given, end-effector, pose, Pworld, robot, Pcam, TPworld, Equations, present | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive body cue:** OC-VLA transforms the end effector pose whether defined in a discrete or continuous action space from the robot base coordinate to the third-person camera coordinate, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view ...
- **p. 2 / III. METHOD - extractive body cue:** Following this paradigm, we adopt a lightweight 300M VLA model [6] for evaluation, which has demonstrated competitive performance using only a third-person camera image and ...
- **p. 3 / III. METHOD - extractive body cue:** Observation-Centric Action Prediction In current robotic datasets, action/pose annotations are often defined at a low level, either as joint commands or end-effector poses within the ...
- **p. 2 / III. METHOD - extractive body cue:** In this section, we provide a detailed overview of OCVLA, i.e., grounding actions in the observation (camera) space.
- **p. 1 / I. INTRODUCTION - extractive body cue:** By anchoring the action target in the same space as the observation (i.e., the image plane), this formulation alleviates the misalignment between perception and action ...
- **p. 4 / III. METHOD - extractive body cue:** In contrast, observationcentric action prediction inherently avoids these issues, offering a more consistent mapping between observation and action.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | In addition to language and image tokens, we concatenate the current timestep and the noise-perturbed action as inputs to the causal transformer. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | For models with a continuous action space, the objective is to minimize the mean squared error (MSE) between the robot's action (augmented ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Both models are optimized with AdamW [61] for 20,000 steps with a batch size of 512. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHOD - extractive body cue:** Consequently, it is difficult for the model to achieve a reasonable projection from image observation to corresponding actions, and thus the model generalization is limited, ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Training is conducted with a batch size of 2048 across 8 NVIDIA A100 GPUs, with 256 samples per GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** While, representations, widely, supervision, signals, Vision-Language-Action, VLA, models, they, tightly, coupled, specific, robot, embodiment, configurations, rather, being, derived, observation, space.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms. | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Action / skill decoding | These models serve as baselines in our evaluation. | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Receding execution / feedback | However, when the prediction target is switched from robot-base coordinate actions to camera-base coordinate actions, the model achieves a further 10% improvement ... | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For model finetuning, we fine-tune the model pretrained on the Droid dataset, using either end effector actions defined in the third-person camera coordinate or those ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** As illustrated in the Figure 4, we introduce a novel, previously unseen camera mounted near Camera 1, and perform all evaluations under this new fixed ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** METHODS ANNOTATED WITH "(VAR)" INDICATE RESULTS OBTAINED UNDER ZERO-SHOT CAMERA EVALUATION, WHILE THOSE WITHOUT THE ANNOTATION CORRESPOND TO EVALUATIONS CONDUCTED USING THE TRAINING CAM 1.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For a fair performance comparison, we also fine-tune the pretrained versions of OpenVLA-OFT [2], π0 [5] on our collected datasets, using their official training protocols.
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7. Full Pipeline of our method. We introduce OC-VLA framework, aligning the observation space and the prediction target with the camera extrinsic calibration matrix. ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** For this purpose, we choose the Droid dataset [9] for pretraining.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Pretraining Data To ensure a comprehensive and fair evaluation of our proposed approach, we incorporate a pretraining stage in selected experiments.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD), objective p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), temporal p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
