# Method - Lift3D Policy: Lifting 2D Foundation Models for Robust 3D Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Task-aware Masked Autoencoder), p. 4 (3.2. Task-aware Masked Autoencoder), p. 5 (3.3. 2D Model-lifting Strategy), p. 3 (3.1. Problem Statement), p. 3 (3.2. Task-aware Masked Autoencoder), p. 7 (Method)): Guide a) Implicit 3D robotic representation (Stage 1) Robot State Point Cloud CLIP Image Encoder CLIP Text Encoder Similarity matrix Text MAE Decoder 2D Foundation Model Attention maps All tokens ...

## Method Body Digest

- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Guide a) Implicit 3D robotic representation (Stage 1) Robot State Point Cloud CLIP Image Encoder CLIP Text Encoder Similarity matrix Text MAE Decoder 2D Foundation ...
- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Finally, to preserve the inherent capabilities of the foundation model, we introduce a distillation loss that constrains the distance between our model's visible token outputs ...
- **p. 5 / 3.3. 2D Model-lifting Strategy - extractive PDF cue:** The 3D tokenizer consists of farthest point sampling [51] for downsampling the number of points, the k-Nearest Neighbor algorithm for local aggregation, and learnable linear ...
- **p. 3 / 3.1. Problem Statement - extractive PDF cue:** We then use a simple policy head π to predict the action a = π(2De(P, RS)).
- **p. 3 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Building on this, Lift3D first enhances the implicit 3D robotic representations within 2D foundation models.
- **p. 7 / Method - extractive PDF cue:** For evaluation, we use the model from the final epoch and evaluate it 20 times in diverse spatial positions.
- **p. 5 / 3.3. 2D Model-lifting Strategy - extractive PDF cue:** The output features (i.e., B ×128×768) from the 2D foundation model are processed through a simple policy head to predict the pose for imitation learning.
- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** As shown in Figure 2 a), during the stage 1 training process, we fine-tune the injected adapter [28] and decoder using reconstruction and distillation losses, ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are as follows: • We propose Lift3D, which elevates 2D foundation models 17348
- **p. 2 / 1. Introduction - extractive PDF cue:** Building on the challenges in the aforementioned 3D policies, we raise a question: "Can we develop a 3D policy model that integrates large-scale pretrained knowledge ...
- **p. 3 / 3. Lift3D Method - extractive PDF cue:** In Section 3.1, we introduce the problem statement of our proposed Lift3D framework.

## Source Evidence Cues

- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Guide a) Implicit 3D robotic representation (Stage 1) Robot State Point Cloud CLIP Image Encoder CLIP Text Encoder Similarity matrix Text MAE Decoder 2D Foundation ...
- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Finally, to preserve the inherent capabilities of the foundation model, we introduce a distillation loss that constrains the distance between our model's visible token outputs ...
- **p. 5 / 3.3. 2D Model-lifting Strategy - extractive PDF cue:** The 3D tokenizer consists of farthest point sampling [51] for downsampling the number of points, the k-Nearest Neighbor algorithm for local aggregation, and learnable linear ...
- **p. 3 / 3.1. Problem Statement - extractive PDF cue:** We then use a simple policy head π to predict the action a = π(2De(P, RS)).
- **p. 3 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Building on this, Lift3D first enhances the implicit 3D robotic representations within 2D foundation models.
- **p. 7 / Method - extractive PDF cue:** For evaluation, we use the model from the final epoch and evaluate it 20 times in diverse spatial positions.
- **p. 5 / 3.3. 2D Model-lifting Strategy - extractive PDF cue:** The output features (i.e., B ×128×768) from the 2D foundation model are processed through a simple policy head to predict the pose for imitation learning.
- **Detected method headings:** 3. Lift3D Method (p. 3); 3.3. 2D Model-lifting Strategy (p. 4); Method (p. 7); 4.5. Exploration of Model Scalability (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Guide a) Implicit 3D robotic representation (Stage 1) Robot State Point Cloud CLIP Image Encoder CLIP Text Encoder Similarity matrix Text MAE ... | p. 4 (3.2. Task-aware Masked Autoencoder), p. 4 (3.2. Task-aware Masked Autoencoder) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Finally, to preserve the inherent capabilities of the foundation model, we introduce a distillation loss that constrains the distance between our model's ... | p. 4 (3.2. Task-aware Masked Autoencoder), p. 5 (3.3. 2D Model-lifting Strategy) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The 3D tokenizer consists of farthest point sampling [51] for downsampling the number of points, the k-Nearest Neighbor algorithm for local aggregation, ... | p. 5 (3.3. 2D Model-lifting Strategy), p. 3 (3.1. Problem Statement) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Finally, to preserve the inherent capabilities of the foundation model, we introduce a distillation loss that constrains the distance between our model's visible token outputs ...
- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** As shown in Figure 2 a), during the stage 1 training process, we fine-tune the injected adapter [28] and decoder using reconstruction and distillation losses, ...
- **p. 5 / 3.3. 2D Model-lifting Strategy - extractive PDF cue:** In this way, we utilize the n combined original 2D PEs to encode the 3D tokens, which effectively provides diverse positional relations within 2D space ...
- **p. 5 / 3.3. 2D Model-lifting Strategy - extractive PDF cue:** However, directly creating new 3D PEs to encode 3D tokens could introduce semantic discrepancies between the pretrained 2D foundation model and the newly added 3D ...
- **p. 8 / 4.4. Exploration of Generalization - extractive PDF cue:** Lift3D demonstrates robustness across various manipulated objects, achieving the smallest accuracy loss.
- **p. 8 / 4.4. Exploration of Generalization - extractive PDF cue:** Additionally, the affordance-guided masking strategy enhances the model's understanding of the spatial geometry of the foreground region through reconstruction, while minimizing the impact of background ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.2. Task-aware Masked Autoencoder), p. 4 (3.2. Task-aware Masked Autoencoder), p. 5 (3.3. 2D Model-lifting Strategy), p. 5 (3.3. 2D Model-lifting Strategy), p. 8 (4.4. Exploration of Generalization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Finally, output, features, foundation, model, processed, through, policy, head, predict, pose, imitation, learning, masking | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Finally, output, features, foundation, model, processed, through, policy, head, predict | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, follows, Lift3D, elevates, foundation, models, Building, challenges, aforementioned | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Finally, preserve, inherent, capabilities, foundation, model, introduce, distillation, loss, constrains | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Finally, the output features from the 2D foundation model are processed through a policy head to predict the pose for imitation learning. masking strategy, where ...
- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Guide a) Implicit 3D robotic representation (Stage 1) Robot State Point Cloud CLIP Image Encoder CLIP Text Encoder Similarity matrix Text MAE Decoder 2D Foundation ...
- **p. 7 / Method - extractive PDF cue:** During the training process, point clouds and action poses in the world coordinate system are used as inputs and supervision, respectively.
- **p. 3 / 3.1. Problem Statement - extractive PDF cue:** Following previous manipulation works [22, 23], we adopt 7DoF action to express the end-effector pose of the robot arm, which includes 3-DoF for translation, 3-DoF ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Building on the challenges in the aforementioned 3D policies, we raise a question: "Can we develop a 3D policy model that integrates large-scale pretrained knowledge ...
- **p. 3 / 3.1. Problem Statement - extractive PDF cue:** We then use a simple policy head π to predict the action a = π(2De(P, RS)).
- **p. 7 / Method - extractive PDF cue:** Lift3D achieves a success rate of 62.5%, which is a 17-point improvement over the state-of-the-art 3D policy, DP3, which achieves 45.5%.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | We select 30 episodes and extract key frames to construct the training set for each task. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Demonstrations in RLBench are collected through pre-defined waypoints and the Open Motion Planning Library [63], with 100 episodes gathered, each containing several ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We select 30 episodes and extract key frames to construct the training set for each task. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Guide a) Implicit 3D robotic representation (Stage 1) Robot State Point Cloud CLIP Image Encoder CLIP Text Encoder Similarity matrix Text MAE Decoder 2D Foundation ...
- **p. 4 / 3.2. Task-aware Masked Autoencoder - extractive PDF cue:** Finally, to preserve the inherent capabilities of the foundation model, we introduce a distillation loss that constrains the distance between our model's visible token outputs ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Guide, Implicit, robotic, representation, Stage, Robot, State, Point, Cloud, CLIP, Image, Encoder, Text, Similarity, matrix, MAE, Decoder, Foundation, Model, Attention.
- **Relevant PDF headings:** 3. Lift3D Method (p. 3); 3.3. 2D Model-lifting Strategy (p. 4); Method (p. 7); 4.5. Exploration of Model Scalability (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Comparison of manipulation success rates between Lift3D and 2D & 3D baselines in simulation benchmarks. ‘2D Rep.' and ‘3D Rep.' refer to ... | p. 6 (4.1. Simulation Experiment), p. 5 (4.1. Simulation Experiment) |
| Action / skill decoding | In addition, compared to the previous SOTA 3D policy (DP3), Lift3D achieves an accuracy improvement of 18.6. | p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment) |
| Receding execution / feedback | In Table 1, Lift3D(CLIP) achieves an average success rate of 83.9 on the MetaWorld benchmark, with 78.8 accuracy on medium-level tasks and ... | p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment) |

## Failure and Ablation Link

- **p. 5 / 4. Experiments - extractive PDF cue:** The effectiveness of each component is validated through an ablation study in Section 4.3.
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** These results demonstrate that Lift3D effectively enhances the 2D foundation model with robust manipulation capabilities, enabling a deeper understanding of robotic 3D scenes by leveraging ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study. In the Task-aware MAE, AMS refers to the affordance-guided masking strategy, Depth and RGB refer to the reconstruction targets, and VD ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Lift3D empowers 2D foundation models with 3D manipulation capabilities by refining implicit 3D robotic representations through task-related affordance masking and depth reconstruction, while ...
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** Additionally, we examine SPA [87], the previous SOTA 3D robotic pretraining method.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overall pipeline of Lift3D. a) For implicit 3D robotic representation, we leverage CLIP [55] to offline extract image attention maps based on task ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Generalization. ‘Object', ‘Background', and ‘Brightness' represent different manipulated objects, background scenes, and lighting conditions, respectively. The image above illustrates the three test scenarios, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Task-aware Masked Autoencoder), p. 4 (3.2. Task-aware Masked Autoencoder), p. 5 (3.3. 2D Model-lifting Strategy), p. 3 (3.1. Problem Statement), p. 3 (3.2. Task-aware Masked Autoencoder), p. 7 (Method), objective p. 4 (3.2. Task-aware Masked Autoencoder), p. 4 (3.2. Task-aware Masked Autoencoder), p. 5 (3.3. 2D Model-lifting Strategy), p. 5 (3.3. 2D Model-lifting Strategy), p. 8 (4.4. Exploration of Generalization), p. 8 (4.4. Exploration of Generalization), temporal p. 6 (4.2. Real-World Experiment), p. 6 (4.1. Simulation Experiment), p. 2 (1. Introduction), p. 3 (3. Lift3D Method), p. 5 (4.1. Simulation Experiment), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
