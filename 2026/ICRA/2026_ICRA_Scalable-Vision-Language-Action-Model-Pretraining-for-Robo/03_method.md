# Method - Scalable Vision-Language-Action Model Pretraining for Robotic Dexterous Manipulation with Real-Life Human Activity Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2510.21571. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 25 (A.2.2 Diffusion Action Expert), p. 25 (A.4 Inference Details), p. 24 (A.1 Hand V-L-A Data Construction), p. 24 (A.1 Hand V-L-A Data Construction), p. 26 (A.5.2 Hand Pose Retargeting), p. 26 (A.5.2 Hand Pose Retargeting)): The cognition feature fc, the hand state st, and the noisy action chunk are first projected via an MLP and subsequently processed through a causal self-attention layer.

## Method Body Digest

- **p. 25 / A.2.2 Diffusion Action Expert - extractive PDF cue:** The cognition feature fc, the hand state st, and the noisy action chunk are first projected via an MLP and subsequently processed through a causal ...
- **p. 25 / A.4 Inference Details - extractive PDF cue:** Predicted end-effector actions in the camera coordinate frame are first converted to absolute 6D poses in the robot coordinate frame, then transformed into joint angles ...
- **p. 24 / A.1 Hand V-L-A Data Construction - extractive PDF cue:** In our initial exploration, we found that replacing these depth modules with direct outputs from MoGe-2 yields more accurate and stable results, while significantly improving ...
- **p. 24 / A.1 Hand V-L-A Data Construction - extractive PDF cue:** For static cameras, we first employ DeepCalib to estimate intrinsics under the same unified camera model assumption.
- **p. 26 / A.5.2 Hand Pose Retargeting - extractive PDF cue:** Their optimization follows the same formulation as Eq.
- **p. 26 / A.5.2 Hand Pose Retargeting - extractive PDF cue:** The switching weight function s(di) increases as the distance di between the fingertip and wrist decreases, encouraging fingertip contact.
- **p. 26 / A.5.2 Hand Pose Retargeting - extractive PDF cue:** The objective is to minimize the squared difference between the glove keypoint vectors vh i and the corresponding robot vectors vr i (qt) obtained through ...
- **p. 25 / A.3 Training Details - extractive PDF cue:** AdamW [54] is used as the optimizer with a weight decay of 1e-1 and a gradient clipping value of 1.0, applied consistently in both pretraining ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Pretraining Unseen Object & BG Finetuning Pick up popcorn box Grasp whisk Grasp electric drill Pour into pot Sweep paper balls Pick up charger Pick ...
- **p. 3 / 1 Introduction - extractive PDF cue:** For temporal atomic action segmentation, we propose a simple yet surprisingly effective algorithm based on the hand movement speed in the 3D space, obtained from ...
- **p. 3 / 1 Introduction - extractive PDF cue:** To this end, we introduce a holistic human activity analytic framework that converts any human hand activity video of arbitrary length into multiple V-L-A trajectories ...

## Source Evidence Cues

- **p. 25 / A.2.2 Diffusion Action Expert - extractive PDF cue:** The cognition feature fc, the hand state st, and the noisy action chunk are first projected via an MLP and subsequently processed through a causal ...
- **p. 25 / A.4 Inference Details - extractive PDF cue:** Predicted end-effector actions in the camera coordinate frame are first converted to absolute 6D poses in the robot coordinate frame, then transformed into joint angles ...
- **p. 24 / A.1 Hand V-L-A Data Construction - extractive PDF cue:** In our initial exploration, we found that replacing these depth modules with direct outputs from MoGe-2 yields more accurate and stable results, while significantly improving ...
- **p. 24 / A.1 Hand V-L-A Data Construction - extractive PDF cue:** For static cameras, we first employ DeepCalib to estimate intrinsics under the same unified camera model assumption.
- **p. 26 / A.5.2 Hand Pose Retargeting - extractive PDF cue:** Their optimization follows the same formulation as Eq.
- **p. 26 / A.5.2 Hand Pose Retargeting - extractive PDF cue:** The switching weight function s(di) increases as the distance di between the fingertip and wrist decreases, encouraging fingertip contact.
- **Detected method headings:** A.2 Model Architecture (p. 24)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The cognition feature fc, the hand state st, and the noisy action chunk are first projected via an MLP and subsequently processed ... | p. 25 (A.2.2 Diffusion Action Expert), p. 25 (A.4 Inference Details) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Predicted end-effector actions in the camera coordinate frame are first converted to absolute 6D poses in the robot coordinate frame, then transformed ... | p. 25 (A.4 Inference Details), p. 24 (A.1 Hand V-L-A Data Construction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | In our initial exploration, we found that replacing these depth modules with direct outputs from MoGe-2 yields more accurate and stable results, ... | p. 24 (A.1 Hand V-L-A Data Construction), p. 24 (A.1 Hand V-L-A Data Construction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 26 / A.5.2 Hand Pose Retargeting - extractive PDF cue:** The objective is to minimize the squared difference between the glove keypoint vectors vh i and the corresponding robot vectors vr i (qt) obtained through ...
- **p. 25 / A.3 Training Details - extractive PDF cue:** AdamW [54] is used as the optimizer with a weight decay of 1e-1 and a gradient clipping value of 1.0, applied consistently in both pretraining ...
- **p. 25 / A.3 Training Details - extractive PDF cue:** Similarly, the cognition token is dropped with a probability of 0.1 in the action expert to leverage classifier-free guidance (CFG) [36].
- **p. 26 / A.5.2 Hand Pose Retargeting - extractive PDF cue:** Notably, only the lateral-swing degrees of freedom (i.e., abduction and adduction) of the thumb and index finger are updated based on this optimization, while their ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 25 (A.3 Training Details), p. 26 (A.5.2 Hand Pose Retargeting), p. 26 (A.5.2 Hand Pose Retargeting).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | state, input, action, expert, dropped, probability, encouraging, model, rely, solely, vision-language, preventing, overfitting, inputs | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | state, input, action, expert, dropped, probability, encouraging, model, rely, solely | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Pretraining, Unseen, Object, Finetuning, Pick, popcorn, Grasp, whisk, electric, drill | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | objective, minimize, squared, difference, between, glove, keypoint, vectors, corresponding, robot | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 25 / A.3 Training Details - extractive PDF cue:** The state input st to the action expert is dropped with a probability of 0.1, encouraging the model to rely solely on vision-language input and ...
- **p. 25 / A.2.3 State and Action Normalization - extractive PDF cue:** For both state and action inputs to the action expert, we apply mean-variance normalization to each dimension, standardizing them to zero mean and unit variance.
- **p. 2 / 1 Introduction - extractive PDF cue:** These videos are typically unstructured: they come unscripted and unsegmented, vary in length and task granularity, contain noisy and irrelevant actions, and lack language instruction ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Recently, video-input VLMs [18, 20] with broad action understanding capabilities are proposed but they still face challenges in action localization accuracy.
- **p. 2 / 1 Introduction - extractive PDF cue:** Additionally, we need precise language instruction labels to describe the actions.
- **p. 4 / 1 Introduction - extractive PDF cue:** Some methods use explicit human actions extracted from mocap videos [23, 24, 43, 69, 71, 84] or web videos [65, 76] to guide robot policy ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Finally, for each segmented video clip, we visualize hand trajectories on sampled video frames and prompt VLM to determine whether the action constitutes meaningful manipulation ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Each data episode comprises a language instruction, a video frame sequence, and frame-aligned 3D action chunks of the end-effector in the robot ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | At time step t, the hand action at is defined as: at = [∆tl, ∆rl, θl h, ∆tr, ∆rr, θr h] ∈R102, ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For fine-tuning on real robot data, we optimize the model for 20K steps with a batch size of 256 and a learning ... | hardware, batch and throughput |

## Training vs Inference

- **p. 24 / A.1 Hand V-L-A Data Construction - extractive PDF cue:** In our initial exploration, we found that replacing these depth modules with direct outputs from MoGe-2 yields more accurate and stable results, while significantly improving ...
- **p. 8 / 5 Experiments - extractive PDF cue:** For fine-tuning on real robot data, we optimize the model for 20K steps with a batch size of 256 and a learning rate of 1e-5, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** cognition, feature, hand, state, noisy, action, chunk, first, projected, MLP, subsequently, processed, through, causal, self-attention, layer, Predicted, end-effector, actions, camera.
- **Relevant PDF headings:** A.2 Model Architecture (p. 24).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We compare our dataset with existing VLA datasets, including EgoDex [37], a human-hand VLA dataset of over 300K episodes collected in lab ... | p. 9 (5 Experiments), p. 14 (5 Experiments) |
| Action / skill decoding | As shown, our method consistently outperforms all baselines. | p. 11 (5 Experiments), p. 11 (5 Experiments) |
| Receding execution / feedback | By contrast, our approach achieves significantly better performance, benefiting from more explicit action supervision, which leads to a smaller pretraining-finetuning gap. | p. 15 (5 Experiments), p. 14 (5 Experiments) |

## Failure and Ablation Link

- **p. 14 / 5 Experiments - extractive PDF cue:** We also analyze the effect of different pretraining data and action representations, the data scaling behavior, and the relationship between robot performance and the performance ...
- **p. 11 / 5 Experiments - extractive PDF cue:** Method Grasp General action Avg./med. dhand-obj (cm) ↓ User Score ↑ Initial position 20.0 / 20.0 - Being-H0 (8B) 19.1 / 18.4 0.15 Ablations Lab ...
- **p. 14 / 5 Experiments - extractive PDF cue:** Compared to the model without human VLA data pretraining, our approach achieves superior execution success and stronger generalization on unseen tasks.
- **p. 15 / 5 Experiments - extractive PDF cue:** For this experiment, we compare with models pretrained on human-hand data using 50%, 20%, and 10% of the dataset (we do not include the 1% ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: We present a pretraining approach for robotic Vision-Language-Action (VLA) models by trans- forming unstructured real-life videos of human activity into structured V-L-A formats ...
- **p. 11 / 5 Experiments - extractive PDF cue:** 5.2.2 Performance Analysis Comparison of Pretraining Data We first compare the performance of models trained with different pretraining datasets to validate the effectiveness of our ...
- **p. 12 / 5 Experiments - extractive PDF cue:** To improve efficiency, this ablation study is conducted on a subset of 350K episodes from Ego4D.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 25 (A.2.2 Diffusion Action Expert), p. 25 (A.4 Inference Details), p. 24 (A.1 Hand V-L-A Data Construction), p. 24 (A.1 Hand V-L-A Data Construction), p. 26 (A.5.2 Hand Pose Retargeting), p. 26 (A.5.2 Hand Pose Retargeting), objective p. 26 (A.5.2 Hand Pose Retargeting), p. 25 (A.3 Training Details), p. 25 (A.3 Training Details), p. 26 (A.5.2 Hand Pose Retargeting), temporal p. 4 (3 Transforming Human Hand Video to VLA Data), p. 7 (3 Transforming Human Hand Video to VLA Data), p. 9 (5 Experiments), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 15 (5 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
