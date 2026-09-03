# Method - MapDream: Task-Driven Map Learning for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IkXFH6alZN; PDF retrieval source: https://openreview.net/pdf/6e898fbe18f2ef7449852473b4a8ab53fd0fda57.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Overview), p. 4 (3.3. Supervised Pre-training), p. 5 (3.4. Reinforcement Fine-tuning), p. 5 (3.4. Reinforcement Fine-tuning)): Specifically, it features (1) a two-module system composed of a task-driven map module and a VLN policy for spatial representation learning and action prediction; (2) a supervised pre-training stage that ...

## Method Body Digest

- **p. 4 / 3.1. Overview - extractive body cue:** Specifically, it features (1) a two-module system composed of a task-driven map module and a VLN policy for spatial representation learning and action prediction; (2) ...
- **p. 4 / 3.3. Supervised Pre-training - extractive body cue:** It consists of three parts: task-driven map supervision, pre-training the map module, and pre-training the VLN policy.
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** The optimization objective follows a GRPO-style formulation: LVLN = -Ek " min
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** Ot, ot, I , (7) where πnav θ and pbev ϕ denote the VLN policy and map module, respectively.
- **p. 4 / 3.3.3. PRE-TRAINING THE VLN POLICY - extractive body cue:** The VLN policy is trained to predict multi-step action sequences conditioned on the predicted maps and visuallanguage context by minimizing a cross-entropy loss, LAction = ...
- **p. 4 / 3.2. Map-in-the-Loop Architecture - extractive body cue:** Across both supervised pretraining and reinforcement fine-tuning, the two components are optimized either with separate objectives or under a unified navigation reward, while remaining connected ...
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** MapDream: Task-Driven Map Learning for Vision-Language Navigation reward-and is carried out using Group Relative Policy Optimization (GRPO) (Shao et al., 2024).
- **p. 2 / 1. Introduction - extractive body cue:** First, the map-inthe-loop architecture comprises a task-driven map module and a VLN policy, where BEV maps are autoregressively generated from egocentric observation histories and language ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are: • We first introduce a task-driven perspective on map representations for VLN, reframing maps as representations shaped by downstream navigation objectives ...
- **p. 2 / 1. Introduction - extractive body cue:** Based on this insight, we propose MapDream, a framework that unifies spatial representation learning and decision making.
- **p. 4 / 3.3. Supervised Pre-training - extractive body cue:** It consists of three parts: task-driven map supervision, pre-training the map module, and pre-training the VLN policy.

## Source Evidence Cues

- **p. 4 / 3.1. Overview - extractive body cue:** Specifically, it features (1) a two-module system composed of a task-driven map module and a VLN policy for spatial representation learning and action prediction; (2) ...
- **p. 4 / 3.3. Supervised Pre-training - extractive body cue:** It consists of three parts: task-driven map supervision, pre-training the map module, and pre-training the VLN policy.
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** The optimization objective follows a GRPO-style formulation: LVLN = -Ek " min
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** Ot, ot, I , (7) where πnav θ and pbev ϕ denote the VLN policy and map module, respectively.
- **Detected method headings:** 3. Method (p. 4); 3.2. Map-in-the-Loop Architecture (p. 4); 3.3.3. PRE-TRAINING THE VLN POLICY (p. 4); 4.3. Comparison with State-of-the-Art Methods (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Specifically, it features (1) a two-module system composed of a task-driven map module and a VLN policy for spatial representation learning and ... | p. 4 (3.1. Overview), p. 4 (3.3. Supervised Pre-training) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | It consists of three parts: task-driven map supervision, pre-training the map module, and pre-training the VLN policy. | p. 4 (3.3. Supervised Pre-training), p. 5 (3.4. Reinforcement Fine-tuning) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The optimization objective follows a GRPO-style formulation: LVLN = -Ek " min | p. 5 (3.4. Reinforcement Fine-tuning), p. 5 (3.4. Reinforcement Fine-tuning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3.3. PRE-TRAINING THE VLN POLICY - extractive body cue:** The VLN policy is trained to predict multi-step action sequences conditioned on the predicted maps and visuallanguage context by minimizing a cross-entropy loss, LAction = ...
- **p. 4 / 3.2. Map-in-the-Loop Architecture - extractive body cue:** Across both supervised pretraining and reinforcement fine-tuning, the two components are optimized either with separate objectives or under a unified navigation reward, while remaining connected ...
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** The optimization objective follows a GRPO-style formulation: LVLN = -Ek " min
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** MapDream: Task-Driven Map Learning for Vision-Language Navigation reward-and is carried out using Group Relative Policy Optimization (GRPO) (Shao et al., 2024).
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.4. Reinforcement Fine-tuning), p. 4 (3.3. Supervised Pre-training), p. 4 (3.4. Reinforcement Fine-tuning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, map-inthe-loop, architecture, comprises, task-driven, module, VLN, policy, where, BEV, maps, autoregressively, generated, egocentric | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | First, map-inthe-loop, architecture, comprises, task-driven, module, VLN, policy, where, BEV | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, first, introduce, task-driven, perspective, representations, VLN, reframing, maps | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | VLN, policy, trained, predict, multi-step, action, sequences, conditioned, predicted, maps | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** First, the map-inthe-loop architecture comprises a task-driven map module and a VLN policy, where BEV maps are autoregressively generated from egocentric observation histories and language ...
- **p. 4 / 3.1. Overview - extractive body cue:** Specifically, it features (1) a two-module system composed of a task-driven map module and a VLN policy for spatial representation learning and action prediction; (2) ...
- **p. 1 / 1. Introduction - extractive body cue:** Abbreviations: Obs denotes observations, Inst instructions, and Act actions. in the field of embodied artificial intelligence that requires agents to ground natural language instructions into ...
- **p. 4 / 3.3.2. PRE-TRAINING THE MAP MODULE - extractive body cue:** Using the generated task-driven maps as supervision, we train an autoregressive model to predict BEV maps from egocentric observations and language instructions: Mt = G(Ot, ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are: • We first introduce a task-driven perspective on map representations for VLN, reframing maps as representations shaped by downstream navigation objectives ...
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** MapDream: Task-Driven Map Learning for Vision-Language Navigation reward-and is carried out using Group Relative Policy Optimization (GRPO) (Shao et al., 2024).
- **p. 1 / 1. Introduction - extractive body cue:** As a result, in current VLN pipelines, aggregating past observations into a persistent spatial state is a standard and integral component.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At each time step t, the map module receives an egocentric observation history Ot, the current frame ot, and the instruction I, ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | In particular, inference latency per decision step drops from 12.7 s to 1.3 s, making compact maps far more suitable for real-time ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | At each time step t, the map module receives an egocentric observation history Ot, the current frame ot, and the instruction I, ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | In particular, inference latency per decision step drops from 12.7 s to 1.3 s, making compact maps far more suitable for real-time ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Overview - extractive body cue:** Specifically, it features (1) a two-module system composed of a task-driven map module and a VLN policy for spatial representation learning and action prediction; (2) ...
- **p. 4 / 3.3. Supervised Pre-training - extractive body cue:** It consists of three parts: task-driven map supervision, pre-training the map module, and pre-training the VLN policy.
- **p. 5 / 4.2.2. TRAINING DETAILS - extractive body cue:** Janus-Pro is trained for one epoch with a batch size of 40 and a learning rate of 1 × 10-4 in a supervised pre-training manner ...
- **p. 6 / 4.2.2. TRAINING DETAILS - extractive body cue:** The model is trained for 2000 steps with a learning rate of 1 × 10-6, jointly fine-tuning both the map module and the VLN policy.
- **p. 4 / 3.3.1. MAP SUPERVISION - extractive body cue:** We adopt lightweight ground-truth map signals during supervised pre-training to encode navigation-critical cues; this design is not exclusive, and alternative compact variants are possible.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, features, two-module, system, composed, task-driven, module, VLN, policy, spatial, representation, learning, action, prediction, supervised, pre-training, stage, establishes, reliable, mapping-to-control.
- **Relevant PDF headings:** 3. Method (p. 4); 3.2. Map-in-the-Loop Architecture (p. 4); 3.3.3. PRE-TRAINING THE VLN POLICY (p. 4); 4.3. Comparison with State-of-the-Art Methods (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Notably, the model is trained only on the R2R-CE and RxR-CE simulators, yet transfers in a zeroshot manner to real-world, previously unseen ... | p. 8 (4.6. Real-world Generalization), p. 6 (4.2.2. TRAINING DETAILS) |
| Global / local decision | We evaluate the effect of two-stage training in MapDream by comparing three configurations: a baseline VLN policy without maps, the map-conditioned model ... | p. 7 (4.5.1. TWO-STAGE TRAINING), p. 5 (4.2.1. DATASET COLLECTION) |
| Motion execution / recovery | Across all settings, MapDream improves both success rate and path efficiency, which we attribute to its task-driven generative maps that are refined ... | p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.1.2. METRICS) |

## Failure and Ablation Link

- **p. 7 / 4.5.1. TWO-STAGE TRAINING - extractive body cue:** We evaluate the effect of two-stage training in MapDream by comparing three configurations: a baseline VLN policy without maps, the map-conditioned model after Stage 1 ...
- **p. 7 / 4.5. Ablation Study - extractive body cue:** Concretely, we analyze the effect of two-stage training, the sensitivity of reinforcement finetuning to different channel initializations, and the trade-off between BEV map compactness and ...
- **p. 8 / 4.5.2. REINFORCEMENT FINE-TUNING UNDER - extractive body cue:** MapDream: Task-Driven Map Learning for Vision-Language Navigation performance after supervised pretraining, reinforcement fine-tuning narrows these gaps, bringing all variants to similar final SR (43.6-45.6) and ...
- **p. 8 / 4.5.2. REINFORCEMENT FINE-TUNING UNDER - extractive body cue:** Effect of Reinforcement Fine-tuning under Different Channel Initializations.
- **p. 6 / 4.2.2. TRAINING DETAILS - extractive body cue:** Observations used include single RGB camera (S.RGB), depth sensor (Depth), panoramic view (Pano.) and map representation (Map). † indicates methods without using LLMs.
- **p. 5 / 4.2.2. TRAINING DETAILS - extractive body cue:** Stage 1 performs supervised pre-training of both the map module and the VLN policy, while Stage 2 jointly fine-tunes them with reinforcement learning.
- **p. 6 / 4.2.2. TRAINING DETAILS - extractive body cue:** The model is trained for 2000 steps with a learning rate of 1 × 10-6, jointly fine-tuning both the map module and the VLN policy.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Overview), p. 4 (3.3. Supervised Pre-training), p. 5 (3.4. Reinforcement Fine-tuning), p. 5 (3.4. Reinforcement Fine-tuning), objective p. 4 (3.3.3. PRE-TRAINING THE VLN POLICY), p. 4 (3.2. Map-in-the-Loop Architecture), p. 5 (3.4. Reinforcement Fine-tuning), p. 5 (3.4. Reinforcement Fine-tuning), temporal p. 4 (3.2. Map-in-the-Loop Architecture), p. 8 (4.5.3. BEV MAP RESOLUTION AND TOKEN BUDGET), p. 6 (4.2.2. TRAINING DETAILS), p. 4 (3.2. Map-in-the-Loop Architecture), p. 5 (3.4. Reinforcement Fine-tuning), p. 5 (3.4. Reinforcement Fine-tuning).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
