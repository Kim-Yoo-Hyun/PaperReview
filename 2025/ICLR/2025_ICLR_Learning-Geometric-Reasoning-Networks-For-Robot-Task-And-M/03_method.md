# Method - Learning Geometric Reasoning Networks For Robot Task And Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ajxAJ8GUX4; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/112460. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 14 (A IMPLEMENTATION DETAILS), p. 14 (A IMPLEMENTATION DETAILS)): Exceptionally, when training on the PR2-3D-4 dataset, we use a hidden size of 256 for the GO module as it yields better results.

## Method Body Digest

- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Exceptionally, when training on the PR2-3D-4 dataset, we use a hidden size of 256 for the GO module as it yields better results.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** During the pre-training stage, each module is trained for 100 epochs.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** The total inference time of GRN is 5.5 ms in average, with the most significant portion spent on scene graph construction with an average time ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** The IK feasibility and GO modules take each a computation time of 0.5 ms.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** In summary, the task at hand is to learn two classification functions fF , fκ, and a regression function fρ s.t.:  Fa FG  ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Task and Motion Planning (TAMP) (Garrett et al., 2021) is a robotics problem in which the goal is to find a sequence of robot actions ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** Once the multi-attention weights computed, our model computes a weighted average of the concatenated node and edge embeddings, followed by a LeakyReLU activation: h′ u ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** These methods, however, lack interpretability and can not provide feedback on why actions are infeasible.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The contributions of this paper are threefold: (1) We propose a novel GNN-based model for efficient and accurate action and grasp feasibility prediction in complex ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address these limitations, we propose a novel approach that leverages a GNN-based model for robot action and grasp feasibility prediction.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Our method constructs a graph representation of 3D environments, where fixed and movable objects are represented as nodes, and edges capture spatial relationships and interaction ...

## Source Evidence Cues

- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Exceptionally, when training on the PR2-3D-4 dataset, we use a hidden size of 256 for the GO module as it yields better results.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** During the pre-training stage, each module is trained for 100 epochs.
- **Detected method headings:** B DATA GENERATION AND ANNOTATION METHOD (p. 15); C.1 GRN PLANNING ALGORITHM (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Exceptionally, when training on the PR2-3D-4 dataset, we use a hidden size of 256 for the GO module as it yields better ... | p. 14 (A IMPLEMENTATION DETAILS), p. 14 (A IMPLEMENTATION DETAILS) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | During the pre-training stage, each module is trained for 100 epochs. | p. 14 (A IMPLEMENTATION DETAILS) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Exceptionally, when training on the PR2-3D-4 dataset, we use a hidden size of 256 for the GO module as it yields better ... | p. 14 (A IMPLEMENTATION DETAILS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** The total inference time of GRN is 5.5 ms in average, with the most significant portion spent on scene graph construction with an average time ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** The IK feasibility and GO modules take each a computation time of 0.5 ms.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summary, task, hand, learn, classification, functions, regression, function, where, GEOMETRIC, REASONING, NETWORKS, GRN, three-module | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | summary, task, hand, learn, classification, functions, regression, function, where, GEOMETRIC | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, threefold, novel, GNN-based, model, efficient, accurate, action, grasp, feasibility | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | total, inference, time, GRN, average, most, significant, portion, spent, scene | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 1 INTRODUCTION - extractive body cue:** In summary, the task at hand is to learn two classification functions fF , fκ, and a regression function fρ s.t.:  Fa FG  ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Task and Motion Planning (TAMP) (Garrett et al., 2021) is a robotics problem in which the goal is to find a sequence of robot actions ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** Once the multi-attention weights computed, our model computes a weighted average of the concatenated node and edge embeddings, followed by a LeakyReLU activation: h′ u ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** These methods, however, lack interpretability and can not provide feedback on why actions are infeasible.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (2022) also use multiple views, combined with text descriptions of actions and predicates as input to a transformer.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** It takes as input the feature vector xu of each node u ∈V corresponding to a movable object, and simultaneously outputs the predicted inverse kinematics ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Finally, the AGF module takes 1.5 ms to output the action and grasp feasibility prediction modules.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | 1As explained is Section 4.1, our model can be applied to different arms of the same type simply by expressing the objects' ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The AGF module, on the other hand, has a hidden size of 256, 4 attention heads and one message-passing step. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | During the fine-tuning stage, the complete GRN model is trained for 100 epochs with a batch size of 2048 and a learning ... | hardware, batch and throughput |

## Training vs Inference

- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Exceptionally, when training on the PR2-3D-4 dataset, we use a hidden size of 256 for the GO module as it yields better results.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** During the pre-training stage, each module is trained for 100 epochs.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** During the fine-tuning stage, the complete GRN model is trained for 100 epochs with a batch size of 2048 and a learning rate of 0.0001.
- **p. 8 / 6 RESULTS - extractive body cue:** In robotic manipulation planning, feasibility prediction must not only be accurate, it must also have a low inference time and memory footprint.
- **p. 8 / 6 RESULTS - extractive body cue:** The inference time incorporates the complete prediction process from the model's input construction to the output, for each movable object in the environment.
- **p. 9 / 6 RESULTS - extractive body cue:** Furthermore, GRN has a 99.6% lower inference time than traditional geometric planning.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Exceptionally, when, training, PR2-3D-4, dataset, hidden, size, module, yields, better, During, pre-training, stage, trained, epochs, total, inference, time, GRN, average.
- **Relevant PDF headings:** B DATA GENERATION AND ANNOTATION METHOD (p. 15); C.1 GRN PLANNING ALGORITHM (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Panda-3D-4: This is dataset is composed of 3D environments containing 4 movable objects, 1 to 4 structures and 0 to 4 obstacles ... | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Action / skill decoding | 6.1 COMPARISON TO PRIOR WORK Table 1 shows that our proposed model outperforms all prior works on both action feasibility and grasp ... | p. 8 (6 RESULTS), p. 7 (5 EXPERIMENTS) |
| Receding execution / feedback | The results show that GRN achieves a better performance than the state-of-the-art on robots with various kinematics. | p. 9 (6 RESULTS), p. 8 (6 RESULTS) |

## Failure and Ablation Link

- **p. 9 / 6 RESULTS - extractive body cue:** We conduct two ablations to demonstrate the effectiveness of our training strategy.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** MLP: This is a simple baseline which uses a 4-layer MLP that takes as input the feature vector x of an object to predict action ...
- **p. 9 / 6 RESULTS - extractive body cue:** Our full model shows a 7.1% gain in performance compared to the one without IK feasibility and GO predictions.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Feasibility-GCN (F-GCN): This baseline uses the same scene representation as F-GAT, except that GAT is replaced with a Graph Convolution Network (GCN), which does not ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** During the fine-tuning stage, the complete GRN model is trained for 100 epochs with a batch size of 2048 and a learning rate of 0.0001.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 5: Annotations statistics for the Panda-3D-4 training set. (a) Number of feasible and infeasi- ble actions (b) Number of feasible and infeasi- ble cases ...
- **p. 8 / 6 RESULTS - extractive body cue:** CNN-based methods, DVH and AGFP-Net, fall short compared to our approach, with a difference in F1 score on the Panda-3D-4 of 10% (resp.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 14 (A IMPLEMENTATION DETAILS), p. 14 (A IMPLEMENTATION DETAILS), objective p. 14 (A IMPLEMENTATION DETAILS), p. 14 (A IMPLEMENTATION DETAILS), temporal p. 7 (5 EXPERIMENTS), p. 14 (A IMPLEMENTATION DETAILS), p. 14 (A IMPLEMENTATION DETAILS), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
