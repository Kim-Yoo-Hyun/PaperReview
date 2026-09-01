# Method - SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (Model), p. 3 (3.1. Problem Formulation), p. 3 (3.2. Architecture), p. 4 (3.2. Architecture), p. 5 (3.4. ActiveViewPose-200K and ActiveManip-Bench), p. 5 (3.3. Two-Stage Training Strategy)): Therefore, we propose Decoupled Action Heads and Camera Adapter to enable our model to acquire rich semantic active perception priors and retain general manipulation knowledge in a data-efficient manner.

## Method Body Digest

- **p. 4 / Model - extractive PDF cue:** Therefore, we propose Decoupled Action Heads and Camera Adapter to enable our model to acquire rich semantic active perception priors and retain general manipulation knowledge ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Given an observation Ot ∈O and a language instruction L ∈L, the policy predicts a joint action trajectory At = {Ahead,t, Aother,t} ∈A.
- **p. 3 / 3.2. Architecture - extractive PDF cue:** First, directly adding camera movement into the existing VLA action space would break the large-scale fixed-view manipulation priors learned from previous training.
- **p. 4 / 3.2. Architecture - extractive PDF cue:** VLM Vision Encoder Text Tokenizer Camera Adapter Get a white bowl from the cabinet then stack the bowls on the right Task Instruction Active Ego ...
- **p. 5 / 3.4. ActiveViewPose-200K and ActiveManip-Bench - extractive PDF cue:** Next, we use a heuristic algorithm to produce a large number of image-to-camera movement pairs.
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive PDF cue:** We freeze the Camera Adapter and train the Decoupled Action Head using MSE loss, such that Lstage2 = λhead Lhead + λother Lother, Therefore, the ...
- **p. 6 / 3.4. ActiveViewPose-200K and ActiveManip-Bench - extractive PDF cue:** ActiveManip-Bench features 12 richly annotated tasks across 100 objects and 20 diverse scenes.
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive PDF cue:** The objective is to minimize the Mean Squared Error between the predicted ego camera movement Ahead and the groundtruth A∗ head,t, defined as Lstage1 = ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy in ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address the limitations of fixed-viewpoint manipulation evaluation, we introduce the first simulated active manipulation benchmark, featuring 12 richly annotated tasks across 100 objects and ...
- **p. 4 / Model - extractive PDF cue:** To bridge this gap, we propose Universal Spatial Knowledge Injection, which efficiently leverages as much 3D information as possible to directly optimize the action output.

## Source Evidence Cues

- **p. 4 / Model - extractive PDF cue:** Therefore, we propose Decoupled Action Heads and Camera Adapter to enable our model to acquire rich semantic active perception priors and retain general manipulation knowledge ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Given an observation Ot ∈O and a language instruction L ∈L, the policy predicts a joint action trajectory At = {Ahead,t, Aother,t} ∈A.
- **p. 3 / 3.2. Architecture - extractive PDF cue:** First, directly adding camera movement into the existing VLA action space would break the large-scale fixed-view manipulation priors learned from previous training.
- **p. 4 / 3.2. Architecture - extractive PDF cue:** VLM Vision Encoder Text Tokenizer Camera Adapter Get a white bowl from the cabinet then stack the bowls on the right Task Instruction Active Ego ...
- **p. 5 / 3.4. ActiveViewPose-200K and ActiveManip-Bench - extractive PDF cue:** Next, we use a heuristic algorithm to produce a large number of image-to-camera movement pairs.
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive PDF cue:** We freeze the Camera Adapter and train the Decoupled Action Head using MSE loss, such that Lstage2 = λhead Lhead + λother Lother, Therefore, the ...
- **p. 6 / 3.4. ActiveViewPose-200K and ActiveManip-Bench - extractive PDF cue:** ActiveManip-Bench features 12 richly annotated tasks across 100 objects and 20 diverse scenes.
- **Detected method headings:** 3. Method (p. 3); 3.2. Architecture (p. 3); Model (p. 4); 4.4. Comparison with existing VLA models (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Therefore, we propose Decoupled Action Heads and Camera Adapter to enable our model to acquire rich semantic active perception priors and retain ... | p. 4 (Model), p. 3 (3.1. Problem Formulation) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Given an observation Ot ∈O and a language instruction L ∈L, the policy predicts a joint action trajectory At = {Ahead,t, Aother,t} ... | p. 3 (3.1. Problem Formulation), p. 3 (3.2. Architecture) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | First, directly adding camera movement into the existing VLA action space would break the large-scale fixed-view manipulation priors learned from previous training. | p. 3 (3.2. Architecture), p. 4 (3.2. Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Two-Stage Training Strategy - extractive PDF cue:** The objective is to minimize the Mean Squared Error between the predicted ego camera movement Ahead and the groundtruth A∗ head,t, defined as Lstage1 = ...
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive PDF cue:** We freeze the Camera Adapter and train the Decoupled Action Head using MSE loss, such that Lstage2 = λhead Lhead + λother Lother, Therefore, the ...
- **p. 4 / Model - extractive PDF cue:** Second, mixed data together with Universal Spatial Knowledge Injection flexibly incorporate various geometric configurations (e.g., absolute depth, camera intrinsics), thereby enhancing spatial precision for active-view ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** This approach first enrich the model with semantic active perception priors in a data-efficient way, and further optimize both camera control and manipulation actions for ...
- **p. 4 / Model - extractive PDF cue:** To bridge this gap, we propose Universal Spatial Knowledge Injection, which efficiently leverages as much 3D information as possible to directly optimize the action output.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.3. Two-Stage Training Strategy), p. 5 (3.3. Two-Stage Training Strategy).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, observation, language, instruction, policy, predicts, joint, action, trajectory, Ahead, Aother, SaPaVe, process, RGB | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Given, observation, language, instruction, policy, predicts, joint, action, trajectory, Ahead | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, threefold, SaPaVe, novel, end-to-end, framework, first, achieves, active | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | objective, minimize, Mean, Squared, Error, between, predicted, camera, movement, Ahead | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Given an observation Ot ∈O and a language instruction L ∈L, the policy predicts a joint action trajectory At = {Ahead,t, Aother,t} ∈A.
- **p. 4 / Model - extractive PDF cue:** SaPaVe can process RGB images and task instructions and output camera movement and manipulation actions in a decoupled action space.
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** To ensure temporal consistency and smooth execution, we adopt an action chunking strategy where the policy predicts an action sequence over a horizon k.
- **p. 4 / 3.2. Architecture - extractive PDF cue:** VLM Vision Encoder Text Tokenizer Camera Adapter Get a white bowl from the cabinet then stack the bowls on the right Task Instruction Active Ego ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Recent advances in Vision-Language Models (VLMs) [10, 25, 48, 53] have improved semantic instruction understanding.
- **p. 2 / 1. Introduction - extractive PDF cue:** End-to-end Vision-LanguageAction (VLA) models [5, 6] aim to bridge this gap, but are typically trained on fixed near-optimal head-camera views, making them sensitive to viewpoint ...
- **p. 5 / 3.4. ActiveViewPose-200K and ActiveManip-Bench - extractive PDF cue:** These templates, along with the images, are sent to GPT-4o to generate relevant instructions, which are then manually refined.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | To ensure temporal consistency and smooth execution, we adopt an action chunking strategy where the policy predicts an action sequence over a ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | At each timestep t, the observation Ot comprises the current RGB image It ∈RH×W ×3 and optional 3D geometric information Gt (e.g., ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.2. Architecture - extractive PDF cue:** First, directly adding camera movement into the existing VLA action space would break the large-scale fixed-view manipulation priors learned from previous training.
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive PDF cue:** We freeze the Camera Adapter and train the Decoupled Action Head using MSE loss, such that Lstage2 = λhead Lhead + λother Lother, Therefore, the ...
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive PDF cue:** We thus use this dataset to train Camera Adapter and Camera Action Decoder by supervising camera movement (see Fig.
- **p. 8 / 4.6. Ablation Studies - extractive PDF cue:** Forcing the use of a unified action decoder couples the two training stages in the action space, not only disrupting the semantic active perception priors ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Therefore, Decoupled, Action, Heads, Camera, Adapter, enable, model, acquire, rich, semantic, active, perception, priors, retain, general, manipulation, knowledge, data-efficient, manner.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. Architecture (p. 3); Model (p. 4); 4.4. Comparison with existing VLA models (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Pick-and-Place Pick-and-Place Arti-Manip Arti-Manip π0 [6] 55 45 45 35 45.00 GR00T-N1 [5] 60 55 50 50 53.75 Ours 90 85 85 ... | p. 7 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Action / skill decoding | Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former ... | p. 1 (Figure/Table caption), p. 7 (4.1. Experimental Setup) |
| Receding execution / feedback | Table 3. Performance on active manipulation in real-world set- tings. We report the success rate (%) compared to the existing VLA models. ... | p. 7 (Figure/Table caption), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 4.6. Ablation Studies - extractive PDF cue:** We conduct a series of ablation experiments on 4 real-world tasks to evaluate the effectiveness of different components in our method.
- **p. 8 / 4.6. Ablation Studies - extractive PDF cue:** Ablation Study on the effect about training strategy of Stage 1 and Stage2, decoupled action head (D.A.H.), camera adapter (C.A.), and universal spatial knowledge injection ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** (2) For the second experiment to evaluate the effect of fixed or dynamic cameras across different types (Sec.
- **p. 6 / 4. Experiments - extractive PDF cue:** (5) What role do each of the system components play in enhancing its overall performance (Sec.
- **p. 7 / 4.4. Comparison with existing VLA models - extractive PDF cue:** Both are fine-tuned for active manipulation tasks.
- **p. 7 / 4.4. Comparison with existing VLA models - extractive PDF cue:** Directly fine-tuning existing VLA models is insufficient to fully address active manipulation tasks In Tab.
- **p. 7 / 4.4. Comparison with existing VLA models - extractive PDF cue:** Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (Model), p. 3 (3.1. Problem Formulation), p. 3 (3.2. Architecture), p. 4 (3.2. Architecture), p. 5 (3.4. ActiveViewPose-200K and ActiveManip-Bench), p. 5 (3.3. Two-Stage Training Strategy), objective p. 5 (3.3. Two-Stage Training Strategy), p. 5 (3.3. Two-Stage Training Strategy), p. 4 (Model), p. 3 (3.1. Problem Formulation), p. 4 (Model), temporal p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 6 (4. Experiments), p. 4 (Model), p. 1 (Abstract), p. 1 (Front matter).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
