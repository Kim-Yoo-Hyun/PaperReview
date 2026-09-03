# Method - FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms)): The aggregated global trunk module is then redistributed to clients for the next training round.

## Method Body Digest

- **p. 5 / 3.4. Algorithms - extractive body cue:** The aggregated global trunk module is then redistributed to clients for the next training round.
- **p. 5 / 3.4. Algorithms - extractive body cue:** At the start of each training round t, each client processes task-specific data using Instruction-Oriented Scene-Parsing to extract structured features, followed by Dual Gating MoE ...
- **p. 6 / 3.4. Algorithms - extractive body cue:** Algorithm 2 FedVLA: Server Input: T is the number of training rounds. θ represents the global trunk parameters.
- **p. 5 / 3.4. Algorithms - extractive body cue:** On the server side, the server receives expert selection statistics and trunk updates from all participating clients and performs Expert-Driven Aggregation, which dynamically assigns aggregation ...
- **p. 6 / 3.4. Algorithms - extractive body cue:** 1: Server Execute: 2: for each round t from 1 to T do 3: // Expert-Driven Aggregation 4: for each trunk layer l do 5: ...
- **p. 2 / 1. Introduction - extractive body cue:** In contrast, VLA models operate in multi-modal environments, requiring the joint processing of visual observations, language instructions, and robotic actions, which significantly increases the complexity ...
- **p. 2 / 1. Introduction - extractive body cue:** IOSP decomposes observation images into object-level representations guided by task instructions and leverages vision-language alignment techniques to improve contextual understanding.
- **p. 1 / 1. Introduction - extractive body cue:** Our federated VLA framework enables decentralized training on user devices, preserving privacy while utilizing expertdriven aggregation to enhance model generalization across diverse tasks. enabling robots ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce the ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions in this work can be summarized as follows: • We propose FedVLA, the first privacy-preserving federated learning framework for VLA training, ensuring ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike traditional centralized training, which requires aggregating all user data on a central server, FL enables distributed model training across multiple clients without transferring raw ...

## Source Evidence Cues

- **p. 5 / 3.4. Algorithms - extractive body cue:** The aggregated global trunk module is then redistributed to clients for the next training round.
- **p. 5 / 3.4. Algorithms - extractive body cue:** At the start of each training round t, each client processes task-specific data using Instruction-Oriented Scene-Parsing to extract structured features, followed by Dual Gating MoE ...
- **p. 6 / 3.4. Algorithms - extractive body cue:** Algorithm 2 FedVLA: Server Input: T is the number of training rounds. θ represents the global trunk parameters.
- **Detected method headings:** 2.1. Vision-Language-Action Models (p. 2); 2.3. Mixture of Experts in Large Models (p. 3); 3.4. Algorithms (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The aggregated global trunk module is then redistributed to clients for the next training round. | p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | At the start of each training round t, each client processes task-specific data using Instruction-Oriented Scene-Parsing to extract structured features, followed by ... | p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Algorithm 2 FedVLA: Server Input: T is the number of training rounds. θ represents the global trunk parameters. | p. 6 (3.4. Algorithms) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Algorithms - extractive body cue:** On the server side, the server receives expert selection statistics and trunk updates from all participating clients and performs Expert-Driven Aggregation, which dynamically assigns aggregation ...
- **p. 5 / 3.4. Algorithms - extractive body cue:** At the start of each training round t, each client processes task-specific data using Instruction-Oriented Scene-Parsing to extract structured features, followed by Dual Gating MoE ...
- **p. 6 / 3.4. Algorithms - extractive body cue:** 1: Server Execute: 2: for each round t from 1 to T do 3: // Expert-Driven Aggregation 4: for each trunk layer l do 5: ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contrast, VLA, models, operate, multi-modal, environments, requiring, joint, processing, visual, observations, language, instructions, robotic | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | contrast, VLA, models, operate, multi-modal, environments, requiring, joint, processing, visual | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Extensive, experiments, simulation, real-world, environments, demonstrate, FedVLA, achieves, performance, comparable | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | server, side, receives, expert, selection, statistics, trunk, updates, participating, clients | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** In contrast, VLA models operate in multi-modal environments, requiring the joint processing of visual observations, language instructions, and robotic actions, which significantly increases the complexity ...
- **p. 2 / 1. Introduction - extractive body cue:** IOSP decomposes observation images into object-level representations guided by task instructions and leverages vision-language alignment techniques to improve contextual understanding.
- **p. 1 / 1. Introduction - extractive body cue:** Our federated VLA framework enables decentralized training on user devices, preserving privacy while utilizing expertdriven aggregation to enhance model generalization across diverse tasks. enabling robots ...
- **p. 1 / 1. Introduction - extractive body cue:** Vision-language-action (VLA) models, which integrate visual perception, linguistic understanding, and robotic control, have significantly enhanced robotic manipulation by *Corresponding author "Put pill bottle1 in red ...
- **p. 5 / 3.4. Algorithms - extractive body cue:** At the start of each training round t, each client processes task-specific data using Instruction-Oriented Scene-Parsing to extract structured features, followed by Dual Gating MoE ...
- **p. 6 / 3.4. Algorithms - extractive body cue:** Algorithm 2 FedVLA: Server Input: T is the number of training rounds. θ represents the global trunk parameters.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | For each task, we collect approximately 30-80 episodes, each consisting of 40-100 steps. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | A RealSense D435i RGB-D camera is mounted above the robot, capturing RGB images in real time at a resolution of 1280 × ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For each task, we collect approximately 30-80 episodes, each consisting of 40-100 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Algorithms - extractive body cue:** The aggregated global trunk module is then redistributed to clients for the next training round.
- **p. 5 / 3.4. Algorithms - extractive body cue:** At the start of each training round t, each client processes task-specific data using Instruction-Oriented Scene-Parsing to extract structured features, followed by Dual Gating MoE ...
- **p. 6 / 3.4. Algorithms - extractive body cue:** Algorithm 2 FedVLA: Server Input: T is the number of training rounds. θ represents the global trunk parameters.
- **p. 6 / 4. Experiments - extractive body cue:** Each client trains locally with a batch size of 256 using the Adam optimizer.
- **p. 6 / 4. Experiments - extractive body cue:** In simulation, the model is trained with a learning rate of 5 × 10-6, while in real-world settings, the learning rate is set to 2×10-5.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** aggregated, global, trunk, module, then, redistributed, clients, next, training, round, start, client, processes, task-specific, data, Instruction-Oriented, Scene-Parsing, extract, structured, features.
- **Relevant PDF headings:** 2.1. Vision-Language-Action Models (p. 2); 2.3. Mixture of Experts in Large Models (p. 3); 3.4. Algorithms (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We collect real-world robotic demonstrations for household-related tasks, including Clean Up, Trash Collection, Open Drawer, and Sorting Pills, as shown in Figure ... | p. 6 (4.2. Real-World), p. 6 (4.1. Simulation) |
| Action / skill decoding | Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%. | p. 6 (4.1. Simulation), p. 6 (4. Experiments) |
| Receding execution / feedback | Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%. | p. 6 (4.1. Simulation), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 4.3. Ablation Studies - extractive body cue:** To further explore the effectiveness of the IOSP, DGMOE and EDA in FedVLA, we conduct ablation experiments by individually removing each module while keeping the ...
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** Ablation studies of proposed FedVLA without IOSP, DGMoE, and EDA.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Validation loss comparison in ablation study across four tasks.
- **p. 6 / 4. Experiments - extractive body cue:** We employ the pretrained HPT [28] as the backbone of our VLA model and train it for 1,000 communication rounds between clients and the server, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Illustration of the proposed FedVLA framework and its key component. (a) An overview of the FedVLA, which consists of multiple clients and a ...
- **p. 6 / 4. Experiments - extractive body cue:** For evaluation, the success and failure of a trial are recoreded as 1 and 0.
- **p. 6 / 4.1. Simulation - extractive body cue:** For collision detection and dynamics simulation, we employ official physics engines to ensure accurate robotic interactions within the simulation environment.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms), objective p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms), temporal p. 6 (4.1. Simulation), p. 6 (4.2. Real-World), p. 7 (4.2. Real-World), p. 7 (4.3. Ablation Studies), p. 1 (Abstract), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
