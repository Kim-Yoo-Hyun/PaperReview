# Method - OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vSLzoUoJt6; PDF retrieval source: https://openreview.net/pdf/b83bcc6b13bf3bed81ebb73be9bae7cc2be710e7.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 5 (3 Methodology), p. 28 (C.2 Camera Pose Selection)): Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to calculate the low-level action at.

## Method Body Digest

- **p. 5 / 3 Methodology - extractive PDF cue:** Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to ...
- **p. 6 / 3 Methodology - extractive PDF cue:** We instruct the VLM model to monitor the state through robot history and to infer the subsequent action by considering both the history and the ...
- **p. 4 / 3 Methodology - extractive PDF cue:** The right panel showcases the Agent Space, where OWMM-VLM processes task instructions, robot history, and visual inputs to perform chain-of-thought reasoning and generate high-level actions ...
- **p. 6 / 3 Methodology - extractive PDF cue:** During our baseline evaluation, we observed three key hallucination-related failure modes: (i) Error location outputs: Base models achieve very low affordance success rates (0.05-0.18) due ...
- **p. 5 / 3 Methodology - extractive PDF cue:** The high-level actions that aim to actuate the robot will be associated with planners and controllers through predefined functions.
- **p. 28 / C.2 Camera Pose Selection - extractive PDF cue:** Potential Optimization for Real-time Deployment While these timings reflect comprehensive processing (multi-image processing, chain-of-thought reasoning, and action generation), real-time deployment could benefit from optimization techn ...
- **p. 27 / C.2 Camera Pose Selection - extractive PDF cue:** Typical scenarios include: • The robot is close enough to the target but outputs a navigation action, leading it to move away and lose the ...
- **p. 5 / 3 Methodology - extractive PDF cue:** These planners generate waypoints that satisfy mechanical constraints for base chassis and arm joints through sampling-based methods.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** In summary, our contributions are as follows: • We propose OWMM-Agent, a unified VLM-based agent architecture for open-world mobile manipulation, capable of global scene understanding, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** • We introduce a simulation-based agentic data synthesis pipeline that enables scalable data collection for instruction fine-tuning for domain adaptation with minimized human effort, with ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Based on the aforementioned observations, we propose a novel VLM agent framework, OWMM-Agent, to address these challenges and leverage the power of VLMs for OWMM ...

## Source Evidence Cues

- **p. 5 / 3 Methodology - extractive PDF cue:** Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to ...
- **p. 6 / 3 Methodology - extractive PDF cue:** We instruct the VLM model to monitor the state through robot history and to infer the subsequent action by considering both the history and the ...
- **p. 4 / 3 Methodology - extractive PDF cue:** The right panel showcases the Agent Space, where OWMM-VLM processes task instructions, robot history, and visual inputs to perform chain-of-thought reasoning and generate high-level actions ...
- **p. 6 / 3 Methodology - extractive PDF cue:** During our baseline evaluation, we observed three key hallucination-related failure modes: (i) Error location outputs: Base models achieve very low affordance success rates (0.05-0.18) due ...
- **p. 5 / 3 Methodology - extractive PDF cue:** The high-level actions that aim to actuate the robot will be associated with planners and controllers through predefined functions.
- **p. 28 / C.2 Camera Pose Selection - extractive PDF cue:** Potential Optimization for Real-time Deployment While these timings reflect comprehensive processing (multi-image processing, chain-of-thought reasoning, and action generation), real-time deployment could benefit from optimization techn ...
- **p. 27 / C.2 Camera Pose Selection - extractive PDF cue:** Typical scenarios include: • The robot is close enough to the target but outputs a navigation action, leading it to move away and lose the ...
- **Detected method headings:** 3 Methodology (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an ... | p. 5 (3 Methodology), p. 6 (3 Methodology) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | We instruct the VLM model to monitor the state through robot history and to infer the subsequent action by considering both the ... | p. 6 (3 Methodology), p. 4 (3 Methodology) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | The right panel showcases the Agent Space, where OWMM-VLM processes task instructions, robot history, and visual inputs to perform chain-of-thought reasoning and ... | p. 4 (3 Methodology), p. 6 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Methodology - extractive PDF cue:** These planners generate waypoints that satisfy mechanical constraints for base chassis and arm joints through sampling-based methods.
- **p. 28 / C.2 Camera Pose Selection - extractive PDF cue:** Potential Optimization for Real-time Deployment While these timings reflect comprehensive processing (multi-image processing, chain-of-thought reasoning, and action generation), real-time deployment could benefit from optimization techn ...
- **p. 25 / C.2 Camera Pose Selection - extractive PDF cue:** This threshold approach ensures successful placement recognition when robots position objects near goal receptacles,and reasonable constraint boundaries to prevent excessive leniency in evaluation.
- **p. 5 / 3 Methodology - extractive PDF cue:** At, Ht = Fvlm(L, G, I, Ic t , Ht-1), (2) at = At(xt, Dc t), (3) where Ht, Ht-1 are the high-level robot history, ...
- **p. 6 / 3 Methodology - extractive PDF cue:** This structured reasoning, learned through supervised fine-tuning on CoT-annotated data, enables the model to track task progress and avoid repetitive actions or dead loops.
- **p. 25 / C.2 Camera Pose Selection - extractive PDF cue:** E.2 Agent Setting We employed GPT-4o for agent construction.GPT-4o first receives our instruction inputs and returns JSON-formatted responses.
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 5 (3 Methodology), p. 25 (C.2 Camera Pose Selection), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 26 (C.2 Camera Pose Selection).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Thus, introduce, pose, graph, associated, RGB, images, output, pre-mapping, stage, basis, define, OWMM, problem | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | Thus, introduce, pose, graph, associated, RGB, images, output, pre-mapping, stage | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | summary, contributions, follows, OWMM-Agent, unified, VLM-based, agent, architecture, open-world, mobile | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | planners, generate, waypoints, satisfy, mechanical, constraints, base, chassis, joints, through | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Methodology - extractive PDF cue:** Thus, we introduce a pose graph G and associated RGB images I as the output of the pre-mapping stage on the basis of [40], and ...
- **p. 6 / 3 Methodology - extractive PDF cue:** Our CoT reasoning approach generates structured reasoning chains that include: 1) Task instruction reasoning and summarization for decision-making; 2) Perception and grounding of current egocentricview ...
- **p. 5 / 3 Methodology - extractive PDF cue:** Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To address the problem of domain adaptation, we further introduce an agentic data synthesis pipeline tailored for OWMM, to generate large-scale and instruction-driven episodes that ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Octo [33] advances generalist robot policies, handling language commands and goal images while adapting quickly to new inputs and actions with standard GPUs. π0 [1] ...
- **p. 4 / 3 Methodology - extractive PDF cue:** The right panel showcases the Agent Space, where OWMM-VLM processes task instructions, robot history, and visual inputs to perform chain-of-thought reasoning and generate high-level actions ...
- **p. 6 / 3 Methodology - extractive PDF cue:** We instruct the VLM model to monitor the state through robot history and to infer the subsequent action by considering both the history and the ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | Thus, we introduce a pose graph G and associated RGB images I as the output of the pre-mapping stage on the basis ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | The robot state and observations updates can be expressed mathematically as: xt+1 = fk(xt, at, ∆t) Ic t+1, Dc t+1 = fobs(xt+1) ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | Crucially, the model summarizes historical context after each decision, enabling each subsequent step to jointly reason over prior history and current observations. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | As for the training time, OWMM-VLM-8B is trained on 8X NVIDIA A100 GPUs for about 7 hours, and OWMM-VLM-38B is trained on ... | hardware, batch and throughput |

## Training vs Inference

- **p. 28 / C.2 Camera Pose Selection - extractive PDF cue:** Potential Optimization for Real-time Deployment While these timings reflect comprehensive processing (multi-image processing, chain-of-thought reasoning, and action generation), real-time deployment could benefit from optimization techn ...
- **p. 27 / C.2 Camera Pose Selection - extractive PDF cue:** I Computational Efficiency Analysis To address concerns about real-world deployment efficiency and scalability to large scenes, we conducted experiments evaluating GPU memory consumption and inference ...
- **p. 21 / C Implementation Details - extractive PDF cue:** As for the training time, OWMM-VLM-8B is trained on 8X NVIDIA A100 GPUs for about 7 hours, and OWMM-VLM-38B is trained on 24X NVIDIA A100 ...
- **p. 28 / C.2 Camera Pose Selection - extractive PDF cue:** For the 8B model, doubling frames from 8+1 to 16+1 increases inference time by only 46% (4.84s to 7.09s).
- **p. 28 / C.2 Camera Pose Selection - extractive PDF cue:** Input Frames Prompt Tokens Time (s) Memory (GB) 8+1 (default) 2810.37 4.39 98.22 16+1 4922.37 5.04 99.13 32+1 9146.37 7.34 100.65 64+1 17594.37 15.33 104.30 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, linked, planner, takes, state, robot, point, clouds, converted, depth, additional, input, calculate, low-level, action, instruct, VLM, model, monitor, through.
- **Relevant PDF headings:** 3 Methodology (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | D Details of Datasets sectionDetails of Datasets D.1 Extra Dataset Construction Details Our evaluation pipeline is constructed using the HomeRobot [40] framework, ... | p. 22 (C.2 Camera Pose Selection), p. 8 (4 Dataset) |
| Base-arm task decision | OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | p. 10 (5 Experiments), p. 28 (C.2 Camera Pose Selection) |
| Execution / correction | OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | p. 10 (5 Experiments), p. 8 (5 Experiments) |

## Failure and Ablation Link

- **p. 26 / C.2 Camera Pose Selection - extractive PDF cue:** Hence, its effect is briefly shown only in the ablation study.
- **p. 8 / 5 Experiments - extractive PDF cue:** For the ablation study on model design, such as the choice of generating bounding boxes rather than points, please see Appendix G.
- **p. 26 / C.2 Camera Pose Selection - extractive PDF cue:** G Ablation Study on OWMM-VLM The ablation study evaluates the contributions of the components of the OWMM-VLM model.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: OWMM-Agent Operates Fetch Robot for Tidying Task. OWMM-Agent receives natural language instructions and leverages both long-term environment memory (scene images) and transient robot ...
- **p. 7 / 4 Dataset - extractive PDF cue:** This increases robustness to natural language variation without compromising annotation precision.
- **p. 21 / C Implementation Details - extractive PDF cue:** Regarding the model's architecture, we have trained two variants consisting of 8 billion and 38 billion parameters, based on the pre-trained model from InternVL-2.5[5].
- **p. 23 / C.2 Camera Pose Selection - extractive PDF cue:** This process increases linguistic diversity by generating 3-5 paraphrases per template, resulting in more robust language understanding without additional manual annotation effort.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 5 (3 Methodology), p. 28 (C.2 Camera Pose Selection), objective p. 5 (3 Methodology), p. 28 (C.2 Camera Pose Selection), p. 25 (C.2 Camera Pose Selection), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 25 (C.2 Camera Pose Selection), temporal p. 4 (3 Methodology), p. 26 (C.2 Camera Pose Selection), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology), p. 22 (C.2 Camera Pose Selection).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
