# Method - BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ffBF6hYuQv; PDF retrieval source: https://arxiv.org/pdf/2506.07961.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 10 (Method), p. 10 (Method), p. 11 (Method), p. 12 (Method), p. 11 (Method), p. 12 (Method)): To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [16]: A state-of-the-art 3D VLA model that incorporates 3D information through ...

## Method Body Digest

- **p. 10 / Method - extractive body cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [16]: A state-of-the-art 3D VLA model ...
- **p. 10 / Method - extractive body cue:** 3) ACT [24]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions.
- **p. 11 / Method - extractive body cue:** For ablation, we replaced the convex upsampling module (309M parameters) with a similarly sized Transformer decoder (303M) to directly predict target positions, supervised by MSE ...
- **p. 12 / Method - extractive body cue:** This design preserves alignment between the input feature spaces of fine-tuning and VLM pretraining, which we find crucial for effective vision-language-action (VLA) modeling.
- **p. 11 / Method - extractive body cue:** Our approach avoids direct action prediction by first generating 2D heatmaps using a convex upsampling module.
- **p. 12 / Method - extractive body cue:** Keys to our method are that (1) it converts 3D inputs to 2D images to align with the 2D image inputs of the pre-trained VLM; ...
- **p. 9 / Method - extractive body cue:** (1) Basic: The model is evaluated in environments that are similar to the training data.
- **p. 2 / 1 Introduction - extractive body cue:** The 2D heatmaps, generated from the tokens corresponding to the projection images, share the same resolution as these images, aligning the input observations and output ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D robot ...
- **p. 2 / 1 Introduction - extractive body cue:** 1, we present BridgeVLA, a novel 3D VLA model that achieves remarkable sample efficiency and strong generalization capabilities.
- **p. 2 / 1 Introduction - extractive body cue:** 2D Finetune 2D Pretrain Real World Simulation BridgeVLA 2D Heatmap Image Instructions 3D Projection 3D actions [ Our framework VLM BridgeVLA ... ... "Find all ...

## Source Evidence Cues

- **p. 10 / Method - extractive body cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [16]: A state-of-the-art 3D VLA model ...
- **p. 10 / Method - extractive body cue:** 3) ACT [24]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions.
- **p. 11 / Method - extractive body cue:** For ablation, we replaced the convex upsampling module (309M parameters) with a similarly sized Transformer decoder (303M) to directly predict target positions, supervised by MSE ...
- **p. 12 / Method - extractive body cue:** This design preserves alignment between the input feature spaces of fine-tuning and VLM pretraining, which we find crucial for effective vision-language-action (VLA) modeling.
- **p. 11 / Method - extractive body cue:** Our approach avoids direct action prediction by first generating 2D heatmaps using a convex upsampling module.
- **p. 12 / Method - extractive body cue:** Keys to our method are that (1) it converts 3D inputs to 2D images to align with the 2D image inputs of the pre-trained VLM; ...
- **p. 9 / Method - extractive body cue:** (1) Basic: The model is evaluated in environments that are similar to the training data.
- **Detected method headings:** Method (p. 9); Method (p. 10); Method (p. 20); Method (p. 21)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [16]: A state-of-the-art ... | p. 10 (Method), p. 10 (Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | 3) ACT [24]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions. | p. 10 (Method), p. 11 (Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | For ablation, we replaced the convex upsampling module (309M parameters) with a similarly sized Transformer decoder (303M) to directly predict target positions, ... | p. 11 (Method), p. 12 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 11 / Method - extractive body cue:** For ablation, we replaced the convex upsampling module (309M parameters) with a similarly sized Transformer decoder (303M) to directly predict target positions, supervised by MSE ...
- **p. 11 / Method - extractive body cue:** Our approach avoids direct action prediction by first generating 2D heatmaps using a convex upsampling module.
- **p. 12 / Method - extractive body cue:** Keys to our method are that (1) it converts 3D inputs to 2D images to align with the 2D image inputs of the pre-trained VLM; ...
- **p. 10 / Method - extractive body cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [16]: A state-of-the-art 3D VLA model ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 11 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Keys, converts, inputs, images, align, image, pre-trained, VLM, aligns, input, observation, output, action, unified | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Keys, converts, inputs, images, align, image, pre-trained, VLM, aligns, input | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, threefold, introduce, BridgeVLA, novel, VLA, model, efficiently, effectively | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | ablation, replaced, convex, upsampling, module, parameters, similarly, sized, Transformer, decoder | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 12 / Method - extractive body cue:** Keys to our method are that (1) it converts 3D inputs to 2D images to align with the 2D image inputs of the pre-trained VLM; ...
- **p. 2 / 1 Introduction - extractive body cue:** The 2D heatmaps, generated from the tokens corresponding to the projection images, share the same resolution as these images, aligning the input observations and output ...
- **p. 2 / 1 Introduction - extractive body cue:** This strategy fails to take advantage of the 3D structural priors as previous efficient 3D policies [10-14] that align the observation input and action output ...
- **p. 10 / Method - extractive body cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [16]: A state-of-the-art 3D VLA model ...
- **p. 12 / Method - extractive body cue:** We hypothesize that the 2D-heatmap pre-training equips BridgeVLA with the ability to connect the semantics in language instructions with image observations in the heatmap space.
- **p. 3 / 1 Introduction - extractive body cue:** In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D robot ...
- **p. 10 / Method - extractive body cue:** 3) ACT [24]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | And each demonstration is paired with language instruction and multiple keyframes. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | (2) C2F-ARM-BC [29] predicts the next keyframe action in the voxel space with a coarse-to-fine strategy. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial. | hardware, batch and throughput |

## Training vs Inference

- **p. 10 / Method - extractive body cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [16]: A state-of-the-art 3D VLA model ...
- **p. 12 / Method - extractive body cue:** This design preserves alignment between the input feature spaces of fine-tuning and VLM pretraining, which we find crucial for effective vision-language-action (VLA) modeling.
- **p. 12 / Method - extractive body cue:** Keys to our method are that (1) it converts 3D inputs to 2D images to align with the 2D image inputs of the pre-trained VLM; ...
- **p. 9 / Method - extractive body cue:** (1) Basic: The model is evaluated in environments that are similar to the training data.
- **p. 11 / Method - extractive body cue:** The ablated model was also harder to train and more sensitive to hyperparameters-requiring a batch size of 192 and careful learning rate tuning-while our original ...
- **p. 7 / 4 Experiments - extractive body cue:** Specifically, our evaluation includes three steps: 1) train the model with the original RLBench data without perturbations (100 trajectories per task) on 20 tasks, 2) ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** demonstrate, BridgeVLA, advantages, over, existing, manipulation, policy, compare, four, types, representative, methods, SpatialVLA, state-of-the-art, VLA, model, incorporates, information, through, Ego3D.
- **Relevant PDF headings:** Method (p. 9); Method (p. 10); Method (p. 20); Method (p. 21).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Both visual encoders show strong adaptability on various robotics tasks in both simulation and the real world. | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Action / skill decoding | Compared to the state-of-the-art baseline, BridgeVLA improves the average success rate by 7.3%. perturbation, 3) compute the average success rate of all ... | p. 8 (4 Experiments), p. 6 (4 Experiments) |
| Receding execution / feedback | BridgeVLA outperforms all the comparing baseline methods in terms of average success rate, significantly outperforming the best baseline method by 7.3%. | p. 8 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 7 / 4 Experiments - extractive body cue:** Specifically, our evaluation includes three steps: 1) train the model with the original RLBench data without perturbations (100 trajectories per task) on 20 tasks, 2) ...
- **p. 10 / Method - extractive body cue:** A common failure mode is that the robot often ignores the target object and moves directly to the 10
- **p. 10 / Method - extractive body cue:** As we can see, most methods completely fails when given only 10 trajectories per task except two 3D related methods: RVT-2 and BridgeVLA.
- **p. 6 / 4 Experiments - extractive body cue:** Q3: How robust is BridgeVLA in handling visual disturbances (e.g., distractors, background, and lighting)?
- **p. 12 / Method - extractive body cue:** 5 Conclusions & Future Work This paper has introduced BridgeVLA, a novel and efficient 3D vision-language-action (VLA) model built on top of a pre-trained vision-language ...
- **p. 8 / 4 Experiments - extractive body cue:** These results address Q3, showcasing that BridgeVLA possesses strong robustness against visual perturbation.
- **p. 9 / Method - extractive body cue:** Distractor, Lighting, Background, and Height aim to evaluate the robustness 9

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 10 (Method), p. 10 (Method), p. 11 (Method), p. 12 (Method), p. 11 (Method), p. 12 (Method), objective p. 11 (Method), p. 11 (Method), p. 12 (Method), p. 10 (Method), temporal p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (Method), p. 9 (Method), p. 12 (Method), p. 4 (3.1 Preliminaries).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
