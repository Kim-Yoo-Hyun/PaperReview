# Method - 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/li25g.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method)): 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is paired with a task description ...

## Method Body Digest

- **p. 3 / 3 Method - extractive body cue:** 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is ...
- **p. 4 / 3 Method - extractive body cue:** The model π consists of a 2D visual encoder, LLM (LLaMA) [63], a cross-modality projection module [62], and LoRA adapters [64].
- **p. 3 / 3 Method - extractive body cue:** The objective of policy model π is to learn action generation in SE(3) space: π : (ot, l, kt, rt) →ˆat+1.
- **p. 4 / 3 Method - extractive body cue:** 3.2), 2D images and 3D point clouds are first tokenized and encoded using pretrained 2D positional embeddings (PEa), then fused and processed by the shared ...
- **p. 5 / 3 Method - extractive body cue:** To model spatial constraints, we use task-specific 3D keypoints corresponding to scene entities.
- **p. 5 / 3 Method - extractive body cue:** After generating 3D keypoints, instead of directly using them as task goals [60], we propose a text-based formulation to integrate these constraints into the VLA ...
- **p. 3 / 3 Method - extractive body cue:** The model supports the output of 7 or 14-DoF end-effector pose for single or dual arms and generates the predicted action ˆat+1 autoregressively, supervised by ...
- **p. 4 / 3 Method - extractive body cue:** Others leverage 2D pretrained models, either by projecting 3D data into multi-view images [25, 26, 27], causing spatial information loss, or by lifting 2D features ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction.
- **p. 4 / 3 Method - extractive body cue:** Therefore, we propose a 2D-to-3D positional alignment mechanism that allows the original 2D PEs, which are interpretable to pretrained models, to encode semantically aligned 2D ...
- **p. 2 / 1 Introduction - extractive body cue:** 1 (left), we propose 3DS-VLA, which equips pretrained 2D vision-language models (2D VLMs) with 3D spatial awareness for robust action generation.

## Source Evidence Cues

- **p. 3 / 3 Method - extractive body cue:** 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is ...
- **p. 4 / 3 Method - extractive body cue:** The model π consists of a 2D visual encoder, LLM (LLaMA) [63], a cross-modality projection module [62], and LoRA adapters [64].
- **p. 3 / 3 Method - extractive body cue:** The objective of policy model π is to learn action generation in SE(3) space: π : (ot, l, kt, rt) →ˆat+1.
- **p. 4 / 3 Method - extractive body cue:** 3.2), 2D images and 3D point clouds are first tokenized and encoded using pretrained 2D positional embeddings (PEa), then fused and processed by the shared ...
- **p. 5 / 3 Method - extractive body cue:** To model spatial constraints, we use task-specific 3D keypoints corresponding to scene entities.
- **p. 5 / 3 Method - extractive body cue:** After generating 3D keypoints, instead of directly using them as task goals [60], we propose a text-based formulation to integrate these constraints into the VLA ...
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each ... | p. 3 (3 Method), p. 4 (3 Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The model π consists of a 2D visual encoder, LLM (LLaMA) [63], a cross-modality projection module [62], and LoRA adapters [64]. | p. 4 (3 Method), p. 3 (3 Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The objective of policy model π is to learn action generation in SE(3) space: π : (ot, l, kt, rt) →ˆat+1. | p. 3 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 Method - extractive body cue:** The model supports the output of 7 or 14-DoF end-effector pose for single or dual arms and generates the predicted action ˆat+1 autoregressively, supervised by ...
- **p. 3 / 3 Method - extractive body cue:** The objective of policy model π is to learn action generation in SE(3) space: π : (ot, l, kt, rt) →ˆat+1.
- **p. 4 / 3 Method - extractive body cue:** Others leverage 2D pretrained models, either by projecting 3D data into multi-view images [25, 26, 27], causing spatial information loss, or by lifting 2D features ...
- **p. 5 / 3 Method - extractive body cue:** 3.3 3D Spatial Constraint Motivation.
- **p. 5 / 3 Method - extractive body cue:** These relationships are shaped by both spatial and temporal constraints [60, 14, 69].
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, visual, inputs, where, image, point, cloud, while, language, keypoints, robot, state, provided, structured | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | takes, visual, inputs, where, image, point, cloud, while, language, keypoints | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, follows, DS-VLA, equipping, pretrained, VLMs, comprehensive, awareness, robust, end-effector | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | model, supports, output, DoF, end-effector, pose, single, dual, arms, generates | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 Method - extractive body cue:** It takes visual inputs ot = {it, pt}, where it is the image and pt is the point cloud, while language l, keypoints kt, and ...
- **p. 3 / 3 Method - extractive body cue:** 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is ...
- **p. 5 / 3 Method - extractive body cue:** Previous VLA models [11, 41, 10, 47] map observations to end-effector poses, but often overlook the understanding of constraints that govern the interaction between the ...
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, most methods learn a direct mapping from perception-to-action [14], predicting end-effector poses only conditioned on vision and language inputs.
- **p. 4 / 3 Method - extractive body cue:** 3.3), we formulate them as language condition to LLaMA, which then generates SE(3) actions conditioned on both visual and language input.
- **p. 5 / 3 Method - extractive body cue:** To understand when to act, we define temporal constraints as the relationship between the current robot state (e.g., keypoint0) and the keypoint spatial constraint (e.g., ...
- **p. 4 / 3 Method - extractive body cue:** For 3D input, we generate a singleview point cloud with P points (e.g., P = 2048) using the depth map and camera parameters.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The keyframes represent important or bottleneck steps of the gripper during task execution, such as a pre-pick, grasp, or place pose. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 Method - extractive body cue:** 3.2), 2D images and 3D point clouds are first tokenized and encoded using pretrained 2D positional embeddings (PEa), then fused and processed by the shared ...
- **p. 5 / 3 Method - extractive body cue:** To model spatial constraints, we use task-specific 3D keypoints corresponding to scene entities.
- **p. 5 / 3 Method - extractive body cue:** After generating 3D keypoints, instead of directly using them as task goals [60], we propose a text-based formulation to integrate these constraints into the VLA ...
- **p. 5 / 4 Experiment - extractive body cue:** The fine-tuning stage trains on 2,400 demonstrations and runs for 10 epochs, taking approximately 8 hours on an NVIDIA RTX A100 GPU, achieving a 5Hz ...
- **p. 7 / 4 Experiment - extractive body cue:** For each task, we train an agent and evaluate it over 10 trials with diverse object poses.
- **p. 7 / 4 Experiment - extractive body cue:** We fine-tune the model with 10 epochs using pretrained weights obtained from simulation training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Task, Formulation, Model, Architecture, Given, dataset, expert, demonstrations, demonstration, paired, description, consists, visual, observations, robot, state, actions, over, frames, encoder.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Since we establish associations between the robot and its environment through structured text input, our model learns to focus on task-relevant objects ... | p. 8 (4 Experiment), p. 6 (4 Experiment) |
| Action / skill decoding | 2, in the dual-arm setting, our method outperforms all baselines by a significant margin. | p. 6 (4 Experiment), p. 8 (4 Experiment) |
| Receding execution / feedback | Both Ours and Ours-s achieve the same average success rate of 0.66 on single-arm tasks, demonstrating that our model can effectively handle ... | p. 7 (4 Experiment), p. 8 (4 Experiment) |

## Failure and Ablation Link

- **p. 7 / 4 Experiment - extractive body cue:** Both Ours and Ours-s achieve the same average success rate of 0.66 on single-arm tasks, demonstrating that our model can effectively handle different embodiments within ...
- **p. 7 / 4 Experiment - extractive body cue:** 4.3 Ablation Study Does each component work?
- **p. 6 / 4 Experiment - extractive body cue:** 0.18 0.29 0.22 0.46 ±0.30 Table 3: The effectiveness of each proposed component.
- **p. 6 / 4 Experiment - extractive body cue:** This stems from their reliance on single-view 2D images without explicit 3D geometric understanding, which is essential for precise action prediction.
- **p. 8 / 4 Experiment - extractive body cue:** To illustrate this, we test the "slide box" and "unplug charger" tasks with randomly set backgrounds, without additional training.
- **p. 8 / 4 Experiment - extractive body cue:** Stack Pour Pick Stack Water Bottle at Slide Unplug Wipe Open Models Success ↑ Cup Water Place* Block* Plants Rack Box Charger Table Drawer DP3 ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: 3DS-VLA achieves comprehensive 3D spatial awareness by encoding 3D spatial observations with a pretrained 2D vision-language model and establishing 3D spatial constraints to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), objective p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), temporal p. 5 (4 Experiment), p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 7 (4 Experiment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
