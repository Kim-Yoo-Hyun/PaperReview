# Method - VIP: Vision Instructed Pre-training for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ccUNMIbpcf; PDF retrieval source: https://openreview.net/pdf/fc80bd3b42c458d1d871411db0d2aec7f70c9c37.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train), p. 3 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train), p. 4 (3.1. Vision Intructed Pre-training), p. 3 (3.1. Vision Intructed Pre-training)): In VIP, we first transform I1 and It as visual features F1 and Ft by a shared encoder like ResNet (He et al., 2016) in the pre-trained policy.

## Method Body Digest

- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** In VIP, we first transform I1 and It as visual features F1 and Ft by a shared encoder like ResNet (He et al., 2016) in ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive PDF cue:** First of all, the future observation ot+1 is affected by both the current state st and action at.
- **p. 3 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** A data sample for robotic manipulation pre-training consists of two parts, a video sequence V = {I1, I2, · · · , IT } and ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive PDF cue:** To bridge this gap, we propose to replace the future frame in pre-training as the cropped image region of the object to manipulate during fine-tuning ...
- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** F1, FT , and Fp are input to the action decoder (e.g., Transformer decoders or diffusion heads) of the pre-trained policy to produce T action ...
- **p. 3 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** In a real robotic manipulation application, future information is unavailable, and a policy π needs to predict future actions A using only the current observation ...
- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** We optimize the pre-trained policy by minimizing a loss L constructed based on {at}T t=1, {σt}T t=1, and {¯at}T t=1 as: L= 1 T T ...
- **p. 4 / 3.2. Sparse Point Flow - extractive PDF cue:** Therefore, employing a video sequence to describe manipulation procedures to a pre-trained policy leads to huge computation cost.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To specify the manipulation procedures clearly while maintaining an acceptable computational burden, we propose to represent the intermediate action information with sparse point flows.
- **p. 3 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** A data sample for robotic manipulation pre-training consists of two parts, a video sequence V = {I1, I2, · · · , IT } and ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive PDF cue:** 2, the vision instruction in pretraining consists of two parts, the future frame and sparse point flows.

## Source Evidence Cues

- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** In VIP, we first transform I1 and It as visual features F1 and Ft by a shared encoder like ResNet (He et al., 2016) in ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive PDF cue:** First of all, the future observation ot+1 is affected by both the current state st and action at.
- **p. 3 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** A data sample for robotic manipulation pre-training consists of two parts, a video sequence V = {I1, I2, · · · , IT } and ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive PDF cue:** To bridge this gap, we propose to replace the future frame in pre-training as the cropped image region of the object to manipulate during fine-tuning ...
- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** F1, FT , and Fp are input to the action decoder (e.g., Transformer decoders or diffusion heads) of the pre-trained policy to produce T action ...
- **p. 3 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** In a real robotic manipulation application, future information is unavailable, and a policy π needs to predict future actions A using only the current observation ...
- **Detected method headings:** 3. Method (p. 3); 4.3. Method Analysis (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | In VIP, we first transform I1 and It as visual features F1 and Ft by a shared encoder like ResNet (He et ... | p. 4 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | First of all, the future observation ot+1 is affected by both the current state st and action at. | p. 5 (3.3. Vision Instruction after Pre-train), p. 3 (3.1. Vision Intructed Pre-training) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | A data sample for robotic manipulation pre-training consists of two parts, a video sequence V = {I1, I2, · · · , ... | p. 3 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** We optimize the pre-trained policy by minimizing a loss L constructed based on {at}T t=1, {σt}T t=1, and {¯at}T t=1 as: L= 1 T T ...
- **p. 4 / 3.2. Sparse Point Flow - extractive PDF cue:** Therefore, employing a video sequence to describe manipulation procedures to a pre-trained policy leads to huge computation cost.
- **p. 5 / 3.2. Sparse Point Flow - extractive PDF cue:** VIP: Vision Instructed Pre-training for Robotic Manipulation lems, we gradually remove point flows during pre-training by masking them with an increasing probability.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.1. Vision Intructed Pre-training), p. 5 (3.2. Sparse Point Flow).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | natural, idea, vision, instruction, feeding, policy, future, images, besides, current, observation, optimized, predict, correct | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | natural, idea, vision, instruction, feeding, policy, future, images, besides, current | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | specify, manipulation, procedures, clearly, while, maintaining, acceptable, computational, burden, represent | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | optimize, pre-trained, policy, minimizing, loss, constructed, Therefore, employing, video, sequence | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** A natural idea of using vision instruction is feeding the policy with future images besides the current observation, and the policy is optimized to predict ...
- **p. 1 / 1. Introduction - extractive PDF cue:** These paradigms expect that the trained policy understands what the green block is in the input image and predicts the action sequence of picking it ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Vision Observation Text Instruction Pick up the green block Vision Instruction Text Instructed Policy Vision Instructed Policy Policy Attention Map Policy Attention Map Fail to ...
- **p. 3 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** In a real robotic manipulation application, future information is unavailable, and a policy π needs to predict future actions A using only the current observation ...
- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** These methods take vision observation and text description as input to predict actions, the process of which demands aligning the information among three domains (vision, ...
- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** F1, FT , and Fp are input to the action decoder (e.g., Transformer decoders or diffusion heads) of the pre-trained policy to produce T action ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive PDF cue:** First of all, the future observation ot+1 is affected by both the current state st and action at.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | A simple implementation of using CoTracker is first randomly sample some points in the first frame of a video sequence and then ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Compared with using an image sequence where every frame comprises tens of thounsands of pixels, the sparse point flows only have tens ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** In VIP, we first transform I1 and It as visual features F1 and Ft by a shared encoder like ResNet (He et al., 2016) in ...
- **p. 3 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** A data sample for robotic manipulation pre-training consists of two parts, a video sequence V = {I1, I2, · · · , IT } and ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive PDF cue:** To bridge this gap, we propose to replace the future frame in pre-training as the cropped image region of the object to manipulate during fine-tuning ...
- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** F1, FT , and Fp are input to the action decoder (e.g., Transformer decoders or diffusion heads) of the pre-trained policy to produce T action ...
- **p. 7 / 4. Experiments - extractive PDF cue:** In VIP, the pre-trained model parameters are updated using AdamW (Loshchilov, 2017) and the learning rate is 1e-5.
- **p. 4 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** In VIP, we first transform I1 and It as visual features F1 and Ft by a shared encoder like ResNet (He et al., 2016) in ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** VIP, first, transform, visual, features, shared, encoder, like, ResNet, pre-trained, policy, future, observation, affected, current, state, action, data, sample, robotic.
- **Relevant PDF headings:** 3. Method (p. 3); 4.3. Method Analysis (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | A Franka Panda robotic arm is deployed in each simulation environment to manipulate objects, with four cameras strategically positioned to observe the ... | p. 6 (4. Experiments), p. 5 (4. Experiments) |
| Action / skill decoding | Among them, ConvMLP is the most commonly adopted baseline, which first extracts image feature using convolutional neural network (CNN) and then regresses ... | p. 7 (4.1. VIP Effectiveness), p. 4 (Figure/Table caption) |
| Receding execution / feedback | As shown, all these designs improve the success rates of VIRT on the three evaluated tasks significantly. | p. 8 (4.3. Method Analysis), p. 8 (4.3. Method Analysis) |

## Failure and Ablation Link

- **p. 6 / 4. Experiments - extractive PDF cue:** After a series of twists, the robot gradually unscrews and removes the lid from the bottle.
- **p. 6 / 4. Experiments - extractive PDF cue:** In the Pour Blueberries task, the robot needs to first remove the juicer cup from the juicer and place it on the table.
- **p. 7 / 4. Experiments - extractive PDF cue:** Without a special statement, the cropped image is obtained from YOLOv10-small (Wang et al., 2024).
- **p. 8 / 4.3. Method Analysis - extractive PDF cue:** This part conducts an ablation study on the designs in VIRT that are not clearly analyzed before.
- **p. 8 / 4.3. Method Analysis - extractive PDF cue:** Ramdomly masking pixels of input images forces the Transformer-based policy to maintain its sensitivity to local features.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overall pipeline of VIP. The input to the pre-trained policy includes two image frames (the observation frame and future frame) and sparse point ...
- **p. 7 / 4. Experiments - extractive PDF cue:** The pre-training consists of 120K iterations and fine-tuning comprises 8K iterations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train), p. 3 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train), p. 4 (3.1. Vision Intructed Pre-training), p. 3 (3.1. Vision Intructed Pre-training), objective p. 4 (3.1. Vision Intructed Pre-training), p. 4 (3.2. Sparse Point Flow), p. 5 (3.2. Sparse Point Flow), temporal p. 4 (3.2. Sparse Point Flow), p. 4 (3.2. Sparse Point Flow), p. 3 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train), p. 5 (3.3. Vision Instruction after Pre-train), p. 6 (4. Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
