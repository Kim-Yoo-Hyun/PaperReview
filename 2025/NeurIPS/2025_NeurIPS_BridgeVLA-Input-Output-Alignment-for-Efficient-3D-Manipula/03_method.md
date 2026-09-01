# Method - BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ffBF6hYuQv; PDF retrieval source: https://openreview.net/pdf/26f13e74e0fd6da3fdd307ba96da6dc4438d93a3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 8 (Method), p. 8 (Method), p. 10 (1) The images in the pre-training dataset are), p. 10 (1) The images in the pre-training dataset are), p. 9 (Method), p. 9 (Method)): To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [37]: A state-of-the-art 3D VLA model that incorporates 3D information through ...

## Method Body Digest

- **p. 8 / Method - extractive PDF cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [37]: A state-of-the-art 3D VLA model ...
- **p. 8 / Method - extractive PDF cue:** 3) ACT [51]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions.
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** This design preserves alignment between the input feature spaces of fine-tuning and VLM pretraining, which we find crucial for effective vision-language-action (VLA) modeling.
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** For ablation, we replaced the convex upsampling module (309M parameters) with a similarly sized Transformer decoder (303M) to directly predict target positions, supervised by MSE ...
- **p. 9 / Method - extractive PDF cue:** To simulate the multi-view inputs during fine-tuning, we repeat each pre-training image three times and feed them into the fine-tuned model to generate heatmaps.
- **p. 9 / Method - extractive PDF cue:** Experimental results show that BridgeVLA outperforms the state-of-the-art baseline method RVT-2 [15] by an average of 32%. per-task results are provided in Appendix C.5 and ...
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** Our approach avoids direct action prediction by first generating 2D heatmaps using a convex upsampling module.
- **p. 2 / 1 Introduction - extractive PDF cue:** The 2D heatmaps, generated from the tokens corresponding to the projection images, share the same resolution as these images, aligning the input observations and output ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D robot ...
- **p. 2 / 1 Introduction - extractive PDF cue:** 1, we present BridgeVLA, a novel 3D VLA model that achieves remarkable sample efficiency and strong generalization capabilities.
- **p. 2 / 1 Introduction - extractive PDF cue:** 2D Finetune 2D Pretrain Real World Simulation BridgeVLA 2D Heatmap Image Instructions 3D Projection 3D actions [ Our framework VLM BridgeVLA ... ... "Find all ...

## Source Evidence Cues

- **p. 8 / Method - extractive PDF cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [37]: A state-of-the-art 3D VLA model ...
- **p. 8 / Method - extractive PDF cue:** 3) ACT [51]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions.
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** This design preserves alignment between the input feature spaces of fine-tuning and VLM pretraining, which we find crucial for effective vision-language-action (VLA) modeling.
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** For ablation, we replaced the convex upsampling module (309M parameters) with a similarly sized Transformer decoder (303M) to directly predict target positions, supervised by MSE ...
- **p. 9 / Method - extractive PDF cue:** To simulate the multi-view inputs during fine-tuning, we repeat each pre-training image three times and feed them into the fine-tuned model to generate heatmaps.
- **p. 9 / Method - extractive PDF cue:** Experimental results show that BridgeVLA outperforms the state-of-the-art baseline method RVT-2 [15] by an average of 32%. per-task results are provided in Appendix C.5 and ...
- **Detected method headings:** Method (p. 8); Method (p. 24); Method (p. 27); Method (p. 28)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [37]: A state-of-the-art ... | p. 8 (Method), p. 8 (Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | 3) ACT [51]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions. | p. 8 (Method), p. 10 (1) The images in the pre-training dataset are) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | This design preserves alignment between the input feature spaces of fine-tuning and VLM pretraining, which we find crucial for effective vision-language-action (VLA) ... | p. 10 (1) The images in the pre-training dataset are), p. 10 (1) The images in the pre-training dataset are) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** For ablation, we replaced the convex upsampling module (309M parameters) with a similarly sized Transformer decoder (303M) to directly predict target positions, supervised by MSE ...
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** Our approach avoids direct action prediction by first generating 2D heatmaps using a convex upsampling module.
- **p. 8 / Method - extractive PDF cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [37]: A state-of-the-art 3D VLA model ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 10 (1) The images in the pre-training dataset are).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | heatmaps, generated, tokens, corresponding, projection, images, share, same, resolution, aligning, input, observations, output, actions | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | heatmaps, generated, tokens, corresponding, projection, images, share, same, resolution, aligning | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, threefold, introduce, BridgeVLA, novel, VLA, model, efficiently, effectively | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | ablation, replaced, convex, upsampling, module, parameters, similarly, sized, Transformer, decoder | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** The 2D heatmaps, generated from the tokens corresponding to the projection images, share the same resolution as these images, aligning the input observations and output ...
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** Keys to our method are that (1) it converts 3D inputs to 2D images to align with the 2D image inputs of the pre-trained VLM; ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This strategy fails to take advantage of the 3D structural priors as previous efficient 3D policies [39, 25, 13-15] that align the observation input and ...
- **p. 8 / Method - extractive PDF cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [37]: A state-of-the-art 3D VLA model ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D robot ...
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** We hypothesize that the 2D-heatmap pre-training equips BridgeVLA with the ability to connect the semantics in language instructions with image observations in the heatmap space.
- **p. 8 / Method - extractive PDF cue:** 3) ACT [51]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Each task contains 3-9 keyframes (see Fig. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | And each demonstration is paired with language instruction and multiple keyframes. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial. | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / Method - extractive PDF cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [37]: A state-of-the-art 3D VLA model ...
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** This design preserves alignment between the input feature spaces of fine-tuning and VLM pretraining, which we find crucial for effective vision-language-action (VLA) modeling.
- **p. 9 / Method - extractive PDF cue:** To simulate the multi-view inputs during fine-tuning, we repeat each pre-training image three times and feed them into the fine-tuned model to generate heatmaps.
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** The ablated model was also harder to train and more sensitive to hyperparameters-requiring a batch size of 192 and careful learning rate tuning-while our original ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** demonstrate, BridgeVLA, advantages, over, existing, manipulation, policy, compare, four, types, representative, methods, SpatialVLA, state-of-the-art, VLA, model, incorporates, information, through, Ego3D.
- **Relevant PDF headings:** Method (p. 8); Method (p. 24); Method (p. 27); Method (p. 28).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | mostly captured from third-person views, which differ significantly from the projection images in our robot data; 2) The pre-training task focuses solely ... | p. 9 (1) The images in the pre-training dataset are), p. 6 (4 Experiments) |
| Action / skill decoding | Figure 3: Real-Robot Experiments and Results. We use a Franka Research 3 robot arm and a ZED 2i camera to capture point ... | p. 9 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Receding execution / feedback | Table 5: Results on GemBench. We show the average success rates on the four evaluation settings of GemBench. BridgeVLA establishes a new ... | p. 24 (Figure/Table caption), p. 23 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** 4.3 Ablation Studies To prove the effectiveness of our model design and provide insights for the community, we conduct three ablation studies: Whether we need ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Model Architecture. (a) 2D Heatmap Pre-training: we train BridgeVLA on 2D object detection datasets. The model takes as inputs an image and a ...
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** This design preserves alignment between the input feature spaces of fine-tuning and VLM pretraining, which we find crucial for effective vision-language-action (VLA) modeling.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Overview. BridgeVLA is a novel 3D VLA model that aligns the input and output within a unified 2D image space. It is pre-trained ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Results on RLBench. The "Avg. Rank" column reports the average rank of each method across all 18 tasks, where lower values indicate better ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 4: Prediction on Pre-training Data after Fine-tuning. To simulate the multi-view inputs during fine-tuning, we repeat each pre-training im- age three times and feed ...
- **p. 22 / Figure/Table caption - extractive PDF cue:** Table 3: Training hyperparameters for BridgeVLA Pretrain RLBench Finetune Colosseum Finetune Real-robot Finetune learning rate 5e-5 8e-5

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 8 (Method), p. 8 (Method), p. 10 (1) The images in the pre-training dataset are), p. 10 (1) The images in the pre-training dataset are), p. 9 (Method), p. 9 (Method), objective p. 10 (1) The images in the pre-training dataset are), p. 10 (1) The images in the pre-training dataset are), p. 8 (Method), temporal p. 7 (4 Experiments), p. 7 (4 Experiments), p. 4 (3.1 Preliminaries), p. 4 (3.1 Preliminaries), p. 2 (1 Introduction), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
