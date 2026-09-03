# Method - TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=9wYjjPydfe; PDF retrieval source: https://openreview.net/pdf/111f8ac3ef90d847bb2191b2bd71a573458c6810.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Latency-Consistent Training Pipeline), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 4 (3.2. Think-in-Control VLA), p. 4 (3.2. Think-in-Control VLA), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation)): Pooling Concatenate Value State + Goal MLP MLP (a) (b) +++ Asynchronous Inference in Closed-loop Multi-stage Training IL with Delayed Inference VLM SFT (d) (c) Online RL Cross-Attention Cross-Attention VLM ...

## Method Body Digest

- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** Pooling Concatenate Value State + Goal MLP MLP (a) (b) +++ Asynchronous Inference in Closed-loop Multi-stage Training IL with Delayed Inference VLM SFT (d) (c) ...
- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** The value network, shown in Figure 3(b), takes as input the current image tokens, the goal position, and the robot state, and outputs the Pos.
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** Visual tokens and VLM cache features are first projected into a shared latent space via MLP layers, while the robot state and latency metadata are ...
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** As shown in Figure 3(a), the action policy utilizes a dedicated action query token that attends to the scene context through a stack of cross-attention ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** As a result, semantic outputs may become temporally misaligned with the agent's current observations and state, creating a key challenge for real-time navigation.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At each control timestep t, the agent receives: (1) a natural language instruction and context I, specifying the navigation goal and historical trajectory; (2) an ...
- **p. 6 / 3.4. DynaNav - extractive body cue:** Human-robot and robot-scene interactions are fully physics-based with realistic contact dynamics.
- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** We optimize the standard autoregressive crossentropy loss over the target token sequence: Ll = -1 Nl Nl X t=1 log pϕ(yt / y<t, I, V), ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly exposes inference delay to the control policy.
- **p. 1 / 1. Introduction - extractive body cue:** TIC-VLA enables real-time, language-conditioned navigation by decoupling slow vision-language reasoning from fast reactive control via a delayed semantic-control interface.
- **p. 2 / 1. Introduction - extractive body cue:** The primary contributions can be summarized as:

## Source Evidence Cues

- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** Pooling Concatenate Value State + Goal MLP MLP (a) (b) +++ Asynchronous Inference in Closed-loop Multi-stage Training IL with Delayed Inference VLM SFT (d) (c) ...
- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** The value network, shown in Figure 3(b), takes as input the current image tokens, the goal position, and the robot state, and outputs the Pos.
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** Visual tokens and VLM cache features are first projected into a shared latent space via MLP layers, while the robot state and latency metadata are ...
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** As shown in Figure 3(a), the action policy utilizes a dedicated action query token that attends to the scene context through a stack of cross-attention ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** As a result, semantic outputs may become temporally misaligned with the agent's current observations and state, creating a key challenge for real-time navigation.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At each control timestep t, the agent receives: (1) a natural language instruction and context I, specifying the navigation goal and historical trajectory; (2) an ...
- **p. 6 / 3.4. DynaNav - extractive body cue:** Human-robot and robot-scene interactions are fully physics-based with realistic contact dynamics.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Pooling Concatenate Value State + Goal MLP MLP (a) (b) +++ Asynchronous Inference in Closed-loop Multi-stage Training IL with Delayed Inference VLM ... | p. 5 (3.3. Latency-Consistent Training Pipeline), p. 5 (3.3. Latency-Consistent Training Pipeline) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The value network, shown in Figure 3(b), takes as input the current image tokens, the goal position, and the robot state, and ... | p. 5 (3.3. Latency-Consistent Training Pipeline), p. 4 (3.2. Think-in-Control VLA) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Visual tokens and VLM cache features are first projected into a shared latent space via MLP layers, while the robot state and ... | p. 4 (3.2. Think-in-Control VLA), p. 4 (3.2. Think-in-Control VLA) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** We optimize the standard autoregressive crossentropy loss over the target token sequence: Ll = -1 Nl Nl X t=1 log pϕ(yt / y<t, I, V), ...
- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** The reward function is defined as: rt = wgrgoal t + wprprogress t + wcrcollision t + wsrspeed t , (5) where rgoal t rewards ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Conditioned on these inputs, the agent must output an action at at each timestep to safely and efficiently progress toward the goal.
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** This latency-aware semantic-control coupling enables robust navigation despite asynchronous and delayed reasoning updates.
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** These inputs are concatenated as key-value tokens, and the updated action query representation is passed through an MLP to generate the action outputs.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.3. Latency-Consistent Training Pipeline), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 4 (3.2. Think-in-Control VLA), p. 4 (3.2. Think-in-Control VLA).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, sample, reasoning, delays, uniformly, seconds, condition, policy, current, image, input, robot, state, cache | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Specifically, sample, reasoning, delays, uniformly, seconds, condition, policy, current, image | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | introduce, Think-in-Control, TIC, VLA, latency-aware, framework, explicitly, exposes, inference, delay | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | optimize, standard, autoregressive, crossentropy, loss, over, target, token, sequence, where | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** Specifically, we sample reasoning delays ∆t uniformly from [0, 10] seconds and condition the policy on: (1) the current image input and robot state, (2) ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At each control timestep t, the agent receives: (1) a natural language instruction and context I, specifying the navigation goal and historical trajectory; (2) an ...
- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** The value network, shown in Figure 3(b), takes as input the current image tokens, the goal position, and the robot state, and outputs the Pos.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Conditioned on these inputs, the agent must output an action at at each timestep to safely and efficiently progress toward the goal.
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** The key design principle is to expose reasoning latency to the action policy and train the policy to act under delayed semantic observations.
- **p. 4 / 3.2. Think-in-Control VLA - extractive body cue:** At a high level, a VLM performs semantic reasoning over delayed visual context and language instructions, while a reactive action policy executes at a high ...
- **p. 6 / 3.4. DynaNav - extractive body cue:** For each task, standardized initial and goal positions are specified with a language instruction.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At each control timestep t, the agent receives: (1) a natural language instruction and context I, specifying the navigation goal and historical ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Vision-languageaction (VLA) models offer a promising framework, but they assume temporally aligned reasoning and control, despite semantic inference being inherently delayed relative ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | At each control timestep t, the agent receives: (1) a natural language instruction and context I, specifying the navigation goal and historical ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | All experiments are conducted on an NVIDIA L40S GPU, with the action policy running at 10 Hz and asynchronous VLM reasoning running ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** Pooling Concatenate Value State + Goal MLP MLP (a) (b) +++ Asynchronous Inference in Closed-loop Multi-stage Training IL with Delayed Inference VLM SFT (d) (c) ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For training the action expert, we increase the batch size to 16 per GPU and set the initial learning rate to 2 × 10-4.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Training is performed using Distributed Data Parallel on eight NVIDIA L40S GPUs, with a batch size of 2 per GPU.
- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** We mix waypoint-only and scene-reasoningaugmented targets during training for flexible prompting at inference time.
- **p. 5 / 3.3. Latency-Consistent Training Pipeline - extractive body cue:** Pooling Concatenate Value State + Goal MLP MLP (a) (b) +++ Asynchronous Inference in Closed-loop Multi-stage Training IL with Delayed Inference VLM SFT (d) (c) ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Pooling, Concatenate, Value, State, Goal, MLP, Asynchronous, Inference, Closed-loop, Multi-stage, Training, Delayed, VLM, SFT, Online, Cross-Attention, Offline, Data, Action, Env.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We train the model using three datasets featuring dynamic human-robot interactions: (1) SCAND (Karnan et al., 2022), which contains 8.7 hours of ... | p. 6 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study) |
| Global / local decision | Without RL finetuning, TIC-VLA is competitive with NavDP, a point-goal method with privileged state access, and outperforms the vanilla BC and RL ... | p. 7 (4.2. Simulation Testing), p. 7 (4.2. Simulation Testing) |
| Motion execution / recovery | After RL fine-tuning, TICVLA achieves the highest success rate and the lowest collision rate, indicating improved closed-loop robustness in dynamic scenes. | p. 7 (4.2. Simulation Testing), p. 8 (4.2. Simulation Testing) |

## Failure and Ablation Link

- **p. 9 / 4.4. Ablation Study - extractive body cue:** As shown in Table 5, the 3-second horizon achieves the best overall performance among TICVLA variants without RL fine-tuning.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5. Effect of action prediction horizon. Results are reported without RL fine-tuning. Horizon NE (↓) SR (↑) SPL (↑) CR (↓) 1s
- **p. 8 / 4.2. Simulation Testing - extractive body cue:** Specifically, we compare interface variants that use waypoint-based guidance and KV-cache-based features, each trained with and without explicit latency-aware modeling and training.
- **p. 8 / 4.2. Simulation Testing - extractive body cue:** The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all latency settings, demonstrating ...
- **p. 7 / 4.2. Simulation Testing - extractive body cue:** In contrast, TIC-VLA uses only egocentric observations and language instructions, without access to privileged goals or maps.
- **p. 7 / 4.2. Simulation Testing - extractive body cue:** The synchronous TIC-VLA variant also degrades substantially, confirming that blocking control on slow VLM inference harms real-time navigation.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 7. Overview of the annotation pipeline for VLM SFT. Representative frames and future trajectory information are used to generate long-horizon navigation instructions and concise ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Latency-Consistent Training Pipeline), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 4 (3.2. Think-in-Control VLA), p. 4 (3.2. Think-in-Control VLA), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), objective p. 5 (3.3. Latency-Consistent Training Pipeline), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Think-in-Control VLA), p. 4 (3.2. Think-in-Control VLA), temporal p. 3 (3.1. Problem Formulation), p. 1 (Abstract), p. 4 (3.2. Think-in-Control VLA), p. 4 (3.2. Think-in-Control VLA), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 5 (3.3. Latency-Consistent Training Pipeline).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
