# Method - RVT: Robotic View Transformer for 3D Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14896; PDF retrieval source: https://arxiv.org/pdf/2306.14896. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 3 (3 Method)): The training time and inference speed of PerAct and RVT are measured on the same GPU model. we use global features (G).

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** The training time and inference speed of PerAct and RVT are measured on the same GPU model. we use global features (G).
- **p. 4 / 3 Method - extractive body cue:** The model outputs an 8-dimensional action, including the 6-DoF target end effector pose (3-DoF for translation and 3-DoF for rotation), 1-DoF gripper state (open or ...
- **p. 4 / 3 Method - extractive body cue:** Our proposed method (RVT) is a transformer model [27] that processes images re-rendered around the robot workspace, produces an output for each view, and then ...
- **p. 5 / 3 Method - extractive body cue:** We use binary classification loss for the gripper state and collision indicator.
- **p. 3 / 3 Method - extractive body cue:** The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state ...
- **p. 3 / 3 Method - extractive body cue:** The model should predict an action, specified by a target end-effector pose and gripper state at the next key-frame.
- **p. 5 / 3 Method - extractive body cue:** For heatmaps, we use the cross-entropy loss for each image.
- **p. 5 / 3 Method - extractive body cue:** For rotation, we use the cross-entropy loss for each of the Euler angles.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose RVT (Robotic View Transformer) that significantly outperforms the SOTA voxel-based method both in terms of success rate and training time, ...
- **p. 3 / 3 Method - extractive body cue:** The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state ...

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** The training time and inference speed of PerAct and RVT are measured on the same GPU model. we use global features (G).
- **p. 4 / 3 Method - extractive body cue:** The model outputs an 8-dimensional action, including the 6-DoF target end effector pose (3-DoF for translation and 3-DoF for rotation), 1-DoF gripper state (open or ...
- **p. 4 / 3 Method - extractive body cue:** Our proposed method (RVT) is a transformer model [27] that processes images re-rendered around the robot workspace, produces an output for each view, and then ...
- **p. 5 / 3 Method - extractive body cue:** We use binary classification loss for the gripper state and collision indicator.
- **p. 3 / 3 Method - extractive body cue:** The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state ...
- **p. 3 / 3 Method - extractive body cue:** The model should predict an action, specified by a target end-effector pose and gripper state at the next key-frame.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The training time and inference speed of PerAct and RVT are measured on the same GPU model. we use global features (G). | p. 5 (3 Method), p. 4 (3 Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The model outputs an 8-dimensional action, including the 6-DoF target end effector pose (3-DoF for translation and 3-DoF for rotation), 1-DoF gripper ... | p. 4 (3 Method), p. 4 (3 Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Our proposed method (RVT) is a transformer model [27] that processes images re-rendered around the robot workspace, produces an output for each ... | p. 4 (3 Method), p. 5 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Method - extractive body cue:** For heatmaps, we use the cross-entropy loss for each image.
- **p. 5 / 3 Method - extractive body cue:** For rotation, we use the cross-entropy loss for each of the Euler angles.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3 Method), p. 5 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | model, outputs, dimensional, action, including, DoF, target, effector, pose, translation, rotation, gripper, state, open | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | model, outputs, dimensional, action, including, DoF, target, effector, pose, translation | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summarize, contributions, threefold, first, RVT, multi-view, transformer, object, manipulation, accurate | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | heatmaps, cross-entropy, loss, image, rotation, Euler, angles | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Method - extractive body cue:** The model outputs an 8-dimensional action, including the 6-DoF target end effector pose (3-DoF for translation and 3-DoF for rotation), 1-DoF gripper state (open or ...
- **p. 4 / 3 Method - extractive body cue:** Each demonstration Di = ({oi 1...mi}, {ai 1...mi}, li) is a successful roll-out of length mi, where li is the language description of the task, ...
- **p. 3 / 3 Method - extractive body cue:** The model should predict an action, specified by a target end-effector pose and gripper state at the next key-frame.
- **p. 3 / 3 Method - extractive body cue:** The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state ...
- **p. 2 / 1 Introduction - extractive body cue:** Also, since the multi-view input to RVT is obtained via re-rendering, we can use RVT even with a single sensor camera - as done in ...
- **p. 5 / 3 Method - extractive body cue:** We use binary classification loss for the gripper state and collision indicator.
- **p. 5 / 3 Method - extractive body cue:** RVT outperforms state-of-the-art methods while being faster to train and execute.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The key-frames represent important or bottleneck steps of the gripper during the task execution [55], such as a prepick, grasp, or place ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The model should predict an action, specified by a target end-effector pose and gripper state at the next key-frame. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Method - extractive body cue:** The training time and inference speed of PerAct and RVT are measured on the same GPU model. we use global features (G).
- **p. 8 / 4 Experiments - extractive body cue:** We train on real-world data for 10K steps, with the same optimizer, batch size, and learning rate schedule as the simulation data.
- **p. 6 / 4 Experiments - extractive body cue:** We report the total training time for both models in Tab.
- **p. 5 / 3 Method - extractive body cue:** The training time and inference speed of PerAct and RVT are measured on the same GPU model. we use global features (G).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, time, inference, speed, PerAct, RVT, measured, same, GPU, model, global, features, outputs, dimensional, action, including, DoF, target, effector, pose.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Just like the baselines, we use the RLBench training dataset with 100 expert demonstrations per task (1800 demonstrations over all tasks). | p. 5 (4 Experiments), p. 8 (4 Experiments) |
| Action / skill decoding | Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks. | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Receding execution / feedback | Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks. | p. 6 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 5 / 4 Experiments - extractive body cue:** We compare with two variants with CNN and ViT vision encoders respectively.
- **p. 6 / 4 Experiments - extractive body cue:** 2 (left) summarizes the ablation experiment results.
- **p. 6 / 4 Experiments - extractive body cue:** We test our models (including the models in the ablation study, Tab.
- **p. 7 / 4 Experiments - extractive body cue:** The sensor camera images are rendered with perspective projection (physical rendering process) and are not straightforward to apply 3D augmentations (e.g., rotation) without re-rendering.
- **p. 7 / 4 Experiments - extractive body cue:** Task vari. train test (+ mark.) (- mark.) Stack 3 14 10 100% 100% blocks Press sanitizer 1 7 10 80% 80% Put marker 4 ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 4: Ablations results for RVT on RLBench with metrics for each task. 16
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Overview of the transformer used in RVT. The input to the transformer is a language description of the task and virtual images of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 3 (3 Method), objective p. 5 (3 Method), p. 5 (3 Method), temporal p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (4 Experiments), p. 5 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
