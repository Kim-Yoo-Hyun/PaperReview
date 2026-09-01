# Method - ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vQFw9ryKyK; PDF retrieval source: https://openreview.net/pdf/e349d69236fa6d97f504e96881ee34405d7de516.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 METHODOLOGY), p. 16 (A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS), p. 17 (A.3 TRAINING DATASET FOR WHERE2IMAGINE), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 4 (3 METHODOLOGY)): 3.2 FUTURE-VIEW IMAGINATION To better leverage the spatial perception and reasoning capabilities of VLMs for open-vocabulary object navigation in unknown environments, we propose an future-view imagination model, which is composed ...

## Method Body Digest

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** 3.2 FUTURE-VIEW IMAGINATION To better leverage the spatial perception and reasoning capabilities of VLMs for open-vocabulary object navigation in unknown environments, we propose an future-view ...
- **p. 16 / A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS - extractive PDF cue:** The process of inputting data into the VLM is as follows: First, the agent acquires an RGB observation based on its current pose and the ...
- **p. 17 / A.3 TRAINING DATASET FOR WHERE2IMAGINE - extractive PDF cue:** By replicating human demonstration trajectories, we collect first-person perspective images It from the trajectory and, after T frames, use the relative camera pose Pt+T = ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** The discrete action space consists of the following commands: {Stop, MoveAhead, TurnLeft, TurnRight, LookUp, LookDown}.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** To determine the execution actions at each step of the PointNav process, we use Variable Experience Rollout (VER) (Wijmans et al., 2022) as our underlying ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Subsequently, the visual observations at these locations are imagined by a NVS model.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Through the Where2Imagine module, our imagination model aligns with human navigation habits.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Compared to larger models (e.g., GPT-4o), GPT-4o-mini is lightweight and cost-effective.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In summary, our contributions are: • We propose a mapless navigation approach ImagineNav.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We also provide a detailed ablation analysis to help understand the important conclusions in our framework.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We propose a new decision-making paradigm based on imagined imagery, wherein decisions are made on imaginations, enabling more nuanced, context-aware interactions that better harness VLMs' ...

## Source Evidence Cues

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** 3.2 FUTURE-VIEW IMAGINATION To better leverage the spatial perception and reasoning capabilities of VLMs for open-vocabulary object navigation in unknown environments, we propose an future-view ...
- **p. 16 / A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS - extractive PDF cue:** The process of inputting data into the VLM is as follows: First, the agent acquires an RGB observation based on its current pose and the ...
- **p. 17 / A.3 TRAINING DATASET FOR WHERE2IMAGINE - extractive PDF cue:** By replicating human demonstration trajectories, we collect first-person perspective images It from the trajectory and, after T frames, use the relative camera pose Pt+T = ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** The discrete action space consists of the following commands: {Stop, MoveAhead, TurnLeft, TurnRight, LookUp, LookDown}.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** To determine the execution actions at each step of the PointNav process, we use Variable Experience Rollout (VER) (Wijmans et al., 2022) as our underlying ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Subsequently, the visual observations at these locations are imagined by a NVS model.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Through the Where2Imagine module, our imagination model aligns with human navigation habits.
- **Detected method headings:** 3 METHODOLOGY (p. 4); A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | 3.2 FUTURE-VIEW IMAGINATION To better leverage the spatial perception and reasoning capabilities of VLMs for open-vocabulary object navigation in unknown environments, we ... | p. 5 (3 METHODOLOGY), p. 16 (A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The process of inputting data into the VLM is as follows: First, the agent acquires an RGB observation based on its current ... | p. 16 (A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS), p. 17 (A.3 TRAINING DATASET FOR WHERE2IMAGINE) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | By replicating human demonstration trajectories, we collect first-person perspective images It from the trajectory and, after T frames, use the relative camera ... | p. 17 (A.3 TRAINING DATASET FOR WHERE2IMAGINE), p. 4 (3 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Compared to larger models (e.g., GPT-4o), GPT-4o-mini is lightweight and cost-effective.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Based on the prompt, 'Your choice should first be based on discovering navigation targets, followed by the potential of unexplored areas...' , the VLM analyzes ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** By examining different future-view scenarios, the VLM pinpoints the direction most likely to incorporate the target object couch. ineNav offers significant advantages in spatial reasoning ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** VER combines the advantages of synchronous and asynchronous reinforcement learning, improving training efficiency and sample utilization in PointNav tasks, thereby enabling the agent to demonstrate ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | illustrated, Figure, VLM, receives, synthesized, observations, future, navigation, waypoints, goal, inputs, Cap, Liang, generates | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | illustrated, Figure, VLM, receives, synthesized, observations, future, navigation, waypoints, goal | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, contributions, mapless, navigation, ImagineNav, provide, detailed, ablation, analysis, help | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Compared, larger, models, GPT-4o, GPT-4o-mini, lightweight, cost-effective, prompt, Your, choice | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** As illustrated in Figure 3, the VLM receives the synthesized observations at future navigation waypoints and the navigation goal as inputs.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Cap (Liang et al., 2023) generates robotic policy code directly from example language commands, enabling autonomous control and task execution based on natural language instructions.
- **p. 16 / A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS - extractive PDF cue:** The RGB observation and the relative pose predicted by Where2Imagine are jointly input into the NVS to generate a new view image.
- **p. 16 / A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS - extractive PDF cue:** Answer= {‘Reason': ‘This image leads to a hallway that may connect to other rooms, increasing the chance of finding a monitor/TV.', ‘Choice': 4} Option 5 ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** This process iterates, where each new observation serves as input for further imagination, reasoning, and navigation, until the agent successfully identifies an instance of the ...
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Subsequently, the system executes the PointNav policy to determine the next navigational action.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Such 3D navigation waypoints indicate relative poses with respect to the current frame and can be easily translated into new observation images using novel view ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At each time step t, the agent receives an egocentric panorama view It, divided into 6 separate views, each represented by an ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Instead, our ImagineNav directly translates the longhorizon object goal navigation task into a sequence of best-view image selection tasks for VLM, which ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Each episode has a maximum limit of 500 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / A.3 TRAINING DATASET FOR WHERE2IMAGINE - extractive PDF cue:** By replicating human demonstration trajectories, we collect first-person perspective images It from the trajectory and, after T frames, use the relative camera pose Pt+T = ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** To determine the execution actions at each step of the PointNav process, we use Variable Experience Rollout (VER) (Wijmans et al., 2022) as our underlying ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** The Where2Imagine model with T=11, utilizing ResNet-18 trained from scratch and GPT-4o-mini as the VLM, was evaluated over 200 epochs on the HM3D and HSSD ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** FUTURE-VIEW, IMAGINATION, better, leverage, spatial, perception, reasoning, capabilities, VLMs, open-vocabulary, object, navigation, unknown, environments, model, composed, Where2Imagine, module, NVS, process.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 4); A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | The HM3D dataset offers high-fidelity reconstructions of 20 entire buildings, including 80 training scenes and 20 validation scenes. | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Global / local decision | Method Open-Vocabulary Mapless HM3D HSSD Success Rate SPL Success Rate SPL FBE (Topiwala et al., 2018) ✗ ✗ 33.7 15.3 36.0 17.7 ... | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Motion execution / recovery | On the HM3D dataset, ImagineNav achieves a success rate of 53.0% and a SPL of 23.8%, significantly outperforming most of the methods ... | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Imagination Where2Imagine NVS HM3D Success Rate SPL ✗ ✗ ✗ 43.0 24.7 ✓ ✗ ✗ 55.0 27.6 ✓ ✓ ✗ 64.0 28.3 ✓ ✗ ✓ ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Moreover, for models of the same architecture, it is possible to opt for more cost-effective variants without compromising navigation performance, thus enabling more resource-efficient and ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: ImagineNav: ablation study on the imagination module. ‘Imagination' refers to whether the future imagi- nations are used as visual prompts of the VLM. ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Furthermore, since the pretrained NVS is directly employed without finetunned on the HM3D and HSSD datasets, we see a disparity between 7
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** 4.7 ANALYSIS OF VLM PLANNER Table 5: Effect of different VLM.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Each variant was tested for 100 epochs under conditions where the agent had access to real panoramic observations.
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 7: Complete prompt input and decision output of vision-language model. A.2 COMPARISON BETWEEN THE WHERE2IMAGINE MODULE AND UNIFORM SAMPLING As shown in Figure 8, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 METHODOLOGY), p. 16 (A.1 DECISION-MAKING DETAILS OF VISION-LANGUAGE MODELS), p. 17 (A.3 TRAINING DATASET FOR WHERE2IMAGINE), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), objective p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), temporal p. 4 (3 METHODOLOGY), p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 1 (1 INTRODUCTION), p. 5 (3 METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
