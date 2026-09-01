# Method - OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2509.19480. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (Method), p. 5 (Method)): A state lattice motion planner is then used to generate velocity commands.

## Method Body Digest

- **p. 5 / Method - extractive PDF cue:** A state lattice motion planner is then used to generate velocity commands.
- **p. 5 / Method - extractive PDF cue:** Other VLA backbones: To further understand the role of VLA architectures and pre-training, we also implement our omni-modal goal-conditioning strategy for the 1B MiniVLA [38] ...
- **p. 5 / Method - extractive PDF cue:** SR and Prog. indicate the success rate and the partial progress towards the goal, respectively. "SRS" averages over simple experiments without obstacles. "SRC" averages over ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple modalities, leveraging information ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** As a result, our policy exhibits strong generalization and fine-tuning capabilities, following language instructions not seen in the training data, and adapting to completely new ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** For example, a user can specify a target pose and provide instructions on how to reach it through language.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** We train our model with goals specified through three primary modalities: (1) 2D poses, (2) egocentric images, and (3) natural language.
- **p. 5 / Method - extractive PDF cue:** Language 2D Pose Image SR Behavior SRS SRC SR Prog.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to leverage ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple modalities, leveraging information ...
- **p. 5 / Method - extractive PDF cue:** To ensure fair comparison with our approach, which relies solely on a single RGB camera without depth or LiDAR, we estimate depth using Depth360 [37] ...

## Source Evidence Cues

- **p. 5 / Method - extractive PDF cue:** A state lattice motion planner is then used to generate velocity commands.
- **p. 5 / Method - extractive PDF cue:** Other VLA backbones: To further understand the role of VLA architectures and pre-training, we also implement our omni-modal goal-conditioning strategy for the 1B MiniVLA [38] ...
- **Detected method headings:** Method (p. 5); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | A state lattice motion planner is then used to generate velocity commands. | p. 5 (Method), p. 5 (Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Other VLA backbones: To further understand the role of VLA architectures and pre-training, we also implement our omni-modal goal-conditioning strategy for the ... | p. 5 (Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | A state lattice motion planner is then used to generate velocity commands. | p. 5 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / Method - extractive PDF cue:** SR and Prog. indicate the success rate and the partial progress towards the goal, respectively. "SRS" averages over simple experiments without obstacles. "SRC" averages over ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | study, family, Omni-Modal, VisionLanguage-Action, Models, OmniVLA, autonomous, navigation, ingest, goals, expressed, multiple, modalities, leveraging | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | study, family, Omni-Modal, VisionLanguage-Action, Models, OmniVLA, autonomous, navigation, ingest, goals | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Moreover, allows, user, instruct, robot, multiple, modalities, making, more, friendly | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Prog, indicate, success, rate, partial, progress, towards, goal, respectively, SRS | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple modalities, leveraging information ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** As a result, our policy exhibits strong generalization and fine-tuning capabilities, following language instructions not seen in the training data, and adapting to completely new ...
- **p. 5 / Method - extractive PDF cue:** A state lattice motion planner is then used to generate velocity commands.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** For example, a user can specify a target pose and provide instructions on how to reach it through language.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** We train our model with goals specified through three primary modalities: (1) 2D poses, (2) egocentric images, and (3) natural language.
- **p. 5 / Method - extractive PDF cue:** Language 2D Pose Image SR Behavior SRS SRC SR Prog.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | During deployment, we initialize from the first observation and, at each time step, estimate the closest node as the current location, as ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | To build the goal graph, we record image observations at 1 Hz. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | To build the goal graph, we record image observations at 1 Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / Method - extractive PDF cue:** Other VLA backbones: To further understand the role of VLA architectures and pre-training, we also implement our omni-modal goal-conditioning strategy for the 1B MiniVLA [38] ...
- **p. 4 / Dataset - extractive PDF cue:** In training OmniVLA with OpenVLA checkpoints on eight H100 GPUs, we use a per-GPU batch size of 7 and accumulate gradients for 4 steps, yielding ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** state, lattice, motion, planner, then, generate, velocity, commands, Other, VLA, backbones, further, understand, role, architectures, pre-training, implement, omni-modal, goal-conditioning, strategy.
- **Relevant PDF headings:** Method (p. 5); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Training OmniVLA While using multi-modal inputs is enticing, training policies to accept omni-modal inputs requires compiling robot datasets that support training and ... | p. 3 (Dataset), p. 3 (Dataset) |
| Global / local decision | We conduct extensive real-world evaluations and compare against state-of-the-art specialist and generalist baselines. | p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP) |
| Motion execution / recovery | Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can ... | p. 7 (Figure/Table caption), p. 3 (Dataset) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural language ...
- **p. 3 / Dataset - extractive PDF cue:** Training on these mixed-modality batches encourages the model to better represent goal information, yielding improved representations for generalization and fine-tuning.
- **p. 3 / Dataset - extractive PDF cue:** Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets ...
- **p. 4 / Dataset - extractive PDF cue:** Since we cannot secure a sufficiently large batch size for some models even on a server with multiple GPUs, we accumulate the gradient for several ...
- **p. 5 / V. EVALUATING OMNI-MODAL NAVIGATION - extractive PDF cue:** However, NaVILA fails, scoring 0.0 on all metrics, due to a domain gap in prompt style: it requires
- **p. 6 / V. EVALUATING OMNI-MODAL NAVIGATION - extractive PDF cue:** The smaller OmniVLA variant fails to handle the language instructions due to limited modal capacity.
- **p. 3 / Dataset - extractive PDF cue:** While large datasets enable generalization, large-scale data collection efforts can result in more noise and therefore, be less accurate.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (Method), p. 5 (Method), objective p. 5 (Method), temporal p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP), p. 6 (V. EVALUATING OMNI-MODAL NAVIGATION), p. 1 (Abstract), p. 1 (Front matter), p. 2 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
