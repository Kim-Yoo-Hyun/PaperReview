# Method - LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2510.19655. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD), p. 4 (III. PROPOSED METHOD), p. 5 (III. PROPOSED METHOD), p. 5 (III. PROPOSED METHOD)): (Right) The prompt for the Vision Action model, which uses the output from the first stage to ground the decision in a specific visual target.

## Method Body Digest

- **p. 4 / III. PROPOSED METHOD - extractive PDF cue:** (Right) The prompt for the Vision Action model, which uses the output from the first stage to ground the decision in a specific visual target.
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** Specifically, the model receives three types of input: • Language Instruction I: The given natural language instruction provided at the start of the task. • ...
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** Language Action: High-Level Planning The first stage of our framework addresses the question: Where should I generally go next?
- **p. 4 / III. PROPOSED METHOD - extractive PDF cue:** It outputs a Vision Action Avis t in a structured format containing a bounding box and its description.
- **p. 5 / III. PROPOSED METHOD - extractive PDF cue:** A low-level controller then executes this path with local obstacle avoidance.
- **p. 5 / III. PROPOSED METHOD - extractive PDF cue:** This deterministic final step grounds the reasoning chain in physical action, ensuring interpretability and making the system adaptable to different robot platforms by simply swapping ...
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** This explicit reasoning step forces the model to track its progress against the overall instruction.
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** First, it generates a Progress Estimation Pt, a natural language assessment of how much of the instruction has been completed.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our contributions are as follows: • We propose a general action decomposition strategy for zero-shot VLN-CE that separates navigation into language-level planning, vision-level grounding, and ...
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** Language Action: High-Level Planning The first stage of our framework addresses the question: Where should I generally go next?
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** To address this, our method decomposes the navigation process into a sequence of three hierarchical actions: a high-level directional plan (Language Action), the grounding of ...

## Source Evidence Cues

- **p. 4 / III. PROPOSED METHOD - extractive PDF cue:** (Right) The prompt for the Vision Action model, which uses the output from the first stage to ground the decision in a specific visual target.
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** Specifically, the model receives three types of input: • Language Instruction I: The given natural language instruction provided at the start of the task. • ...
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** Language Action: High-Level Planning The first stage of our framework addresses the question: Where should I generally go next?
- **p. 4 / III. PROPOSED METHOD - extractive PDF cue:** It outputs a Vision Action Avis t in a structured format containing a bounding box and its description.
- **p. 5 / III. PROPOSED METHOD - extractive PDF cue:** A low-level controller then executes this path with local obstacle avoidance.
- **p. 5 / III. PROPOSED METHOD - extractive PDF cue:** This deterministic final step grounds the reasoning chain in physical action, ensuring interpretability and making the system adaptable to different robot platforms by simply swapping ...
- **Detected method headings:** III. PROPOSED METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | (Right) The prompt for the Vision Action model, which uses the output from the first stage to ground the decision in a ... | p. 4 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Specifically, the model receives three types of input: • Language Instruction I: The given natural language instruction provided at the start of ... | p. 3 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Language Action: High-Level Planning The first stage of our framework addresses the question: Where should I generally go next? | p. 3 (III. PROPOSED METHOD), p. 4 (III. PROPOSED METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** This explicit reasoning step forces the model to track its progress against the overall instruction.
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** First, it generates a Progress Estimation Pt, a natural language assessment of how much of the instruction has been completed.
- **p. 4 / III. PROPOSED METHOD - extractive PDF cue:** As shown in Figure 3, the prompt instructs the model to select a target that is not too close, encouraging meaningful progress.
- **p. 4 / III. PROPOSED METHOD - extractive PDF cue:** The model is prompted with: • Language Instruction I: The original instruction. • Progress Estimation Pt: The text generated by the Language Action model. • ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, model, receives, three, types, input, Language, Instruction, given, natural, provided, start, task, Current | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Specifically, model, receives, three, types, input, Language, Instruction, given, natural | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contributions, follows, general, action, decomposition, strategy, zero-shot, VLN-CE, separates, navigation | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | explicit, reasoning, step, forces, model, track, progress, against, overall, instruction | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** Specifically, the model receives three types of input: • Language Instruction I: The given natural language instruction provided at the start of the task. • ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** 1) Language Action: A powerful MLLM acts as a highlevel planner, analyzing the instruction, history, and current observation to produce a coarse strategic decision, such ...
- **p. 4 / III. PROPOSED METHOD - extractive PDF cue:** The model is prompted with: • Language Instruction I: The original instruction. • Progress Estimation Pt: The text generated by the Language Action model. • ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our contributions are as follows: • We propose a general action decomposition strategy for zero-shot VLN-CE that separates navigation into language-level planning, vision-level grounding, and ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Vision-and-Language Navigation (VLN) presents the challenge of grounding natural language instructions within visual observations to enable an embodied agent to navigate through previously unseen environments ...
- **p. 3 / III. PROPOSED METHOD - extractive PDF cue:** At each timestep t, it uses an egocentric observation It to choose its next action At from a continuous space.
- **p. 4 / III. PROPOSED METHOD - extractive PDF cue:** It outputs a Vision Action Avis t in a structured format containing a bounding box and its description.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At each timestep t, it uses an egocentric observation It to choose its next action At from a continuous space. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Specifically, the model receives three types of input: • Language Instruction I: The given natural language instruction provided at the start of ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | Specifically, the model receives three types of input: • Language Instruction I: The given natural language instruction provided at the start of ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Configuration NE↓ OSR↑ SR↑ SPL↑ LaViRA (Full) 6.43±0.28 43.3±3.2 36.0±1.7 28.3±0.8 Framework Decomposition w/o LA 8.94±0.53 13.0±3.0 6.7±0.6 4.4±1.2 w/o VA 7.28±0.23 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / V. REAL-WORLD EXPERIMENTS - extractive PDF cue:** These qualitative results confirm that LaViRA's hierarchical reasoning generalizes effectively from simulation to physical hardware without any training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Right, prompt, Vision, Action, model, uses, output, first, stage, ground, decision, specific, visual, target, Specifically, receives, three, types, input, Language.
- **Relevant PDF headings:** III. PROPOSED METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We use the Habitat simulator [34] with the VLN-CE dataset [2], which extends the R2R benchmark from Matterport3D (MP3D) [10] for continuous ... | p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (V. REAL-WORLD EXPERIMENTS) |
| Global / local decision | Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an ... | p. 7 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS) |
| Motion execution / recovery | Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an ... | p. 7 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive PDF cue:** Although the Gemini-2.5-Pro variant delivered superior performance, we used the GPT4o variant for ablations due to documented stability issues with the Gemini-2.5-Pro API during our ...
- **p. 6 / V. REAL-WORLD EXPERIMENTS - extractive PDF cue:** These qualitative results confirm that LaViRA's hierarchical reasoning generalizes effectively from simulation to physical hardware without any training.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive PDF cue:** Ablation Studies We performed a series of ablation studies to analyze LaViRA's performance and quantify the contribution of its core components.
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive PDF cue:** We conducted further ablations on key design choices, as shown in Table III.
- **p. 7 / VI. CONCLUSION - extractive PDF cue:** Its performance ceiling is bounded by off-the-shelf models, as seen in failures on ambiguous instructions and large-area grounding.
- **p. 7 / VI. CONCLUSION - extractive PDF cue:** (Right) Failure cases visualization: Language Action misjudges direction due to ambiguous instructions; Vision Action selects the wrong region despite correct target description; simulation reconstruction errors ...
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive PDF cue:** Qualitative Analysis To offer qualitative insights into LaViRA's decisionmaking, Figure 4 shows a successful navigation run and common failures.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD), p. 4 (III. PROPOSED METHOD), p. 5 (III. PROPOSED METHOD), p. 5 (III. PROPOSED METHOD), objective p. 3 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD), p. 4 (III. PROPOSED METHOD), p. 4 (III. PROPOSED METHOD), temporal p. 3 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD), p. 6 (IV. SIMULATION EXPERIMENTS), p. 4 (III. PROPOSED METHOD), p. 4 (III. PROPOSED METHOD), p. 5 (IV. SIMULATION EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
