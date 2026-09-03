# Method - OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vSLzoUoJt6; PDF retrieval source: https://arxiv.org/pdf/2506.04217. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology)): Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to calculate the low-level action at.

## Method Body Digest

- **p. 5 / 3 Methodology - extractive body cue:** Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to ...
- **p. 6 / 3 Methodology - extractive body cue:** We instruct the VLM model to monitor the state through robot history and to infer the subsequent action by considering both the history and the ...
- **p. 4 / 3 Methodology - extractive body cue:** The right panel showcases the Agent Space, where OWMM-VLM processes task instructions, robot history, and visual inputs to perform chain-of-thought reasoning and generate high-level actions ...
- **p. 6 / 3 Methodology - extractive body cue:** Our dataset consists of four subsets, each corresponding to one of the four primary task actions: Pick, Place, Navigate to Point, and Search Scene Frame.
- **p. 4 / 3 Methodology - extractive body cue:** Let's Fagent note the logical function of the agent policy model, and we have at = Fagent(L, G, I, Ic t , Dc t, xt), ...
- **p. 5 / 3 Methodology - extractive body cue:** The high-level actions that aim to actuate the robot will be associated with planners and controllers through predefined functions.
- **p. 13 / C Implementation Details - extractive body cue:** The 8B model is composed of InternViT-300M and InternLM-2.5-7B[3], and the 38B model is composed of InternViT-6B and Qwen2.5[35].
- **p. 5 / 3 Methodology - extractive body cue:** These planners generate waypoints that satisfy mechanical constraints for base chassis and arm joints through sampling-based methods.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose OWMM-Agent, a unified VLM-based agent architecture for open-world mobile manipulation, capable of global scene understanding, ...
- **p. 2 / 1 Introduction - extractive body cue:** Based on the aforementioned observations, we propose a novel VLM agent framework, OWMM-Agent, to address these challenges and leverage the power of VLMs for OWMM ...
- **p. 3 / 1 Introduction - extractive body cue:** • We introduce a foundation model for OWMM, capable of multi-image reasoning and executable multi-modal action generation, with extensive experiments analyzing the model's performance.

## Source Evidence Cues

- **p. 5 / 3 Methodology - extractive body cue:** Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to ...
- **p. 6 / 3 Methodology - extractive body cue:** We instruct the VLM model to monitor the state through robot history and to infer the subsequent action by considering both the history and the ...
- **p. 4 / 3 Methodology - extractive body cue:** The right panel showcases the Agent Space, where OWMM-VLM processes task instructions, robot history, and visual inputs to perform chain-of-thought reasoning and generate high-level actions ...
- **p. 6 / 3 Methodology - extractive body cue:** Our dataset consists of four subsets, each corresponding to one of the four primary task actions: Pick, Place, Navigate to Point, and Search Scene Frame.
- **p. 4 / 3 Methodology - extractive body cue:** Let's Fagent note the logical function of the agent policy model, and we have at = Fagent(L, G, I, Ic t , Dc t, xt), ...
- **p. 5 / 3 Methodology - extractive body cue:** The high-level actions that aim to actuate the robot will be associated with planners and controllers through predefined functions.
- **p. 13 / C Implementation Details - extractive body cue:** The 8B model is composed of InternViT-300M and InternLM-2.5-7B[3], and the 38B model is composed of InternViT-6B and Qwen2.5[35].
- **Detected method headings:** 3 Methodology (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an ... | p. 5 (3 Methodology), p. 6 (3 Methodology) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | We instruct the VLM model to monitor the state through robot history and to infer the subsequent action by considering both the ... | p. 6 (3 Methodology), p. 4 (3 Methodology) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | The right panel showcases the Agent Space, where OWMM-VLM processes task instructions, robot history, and visual inputs to perform chain-of-thought reasoning and ... | p. 4 (3 Methodology), p. 6 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Methodology - extractive body cue:** These planners generate waypoints that satisfy mechanical constraints for base chassis and arm joints through sampling-based methods.
- **p. 16 / C Implementation Details - extractive body cue:** This threshold approach ensures successful placement recognition when robots position objects near goal receptacles,and reasonable constraint boundaries to prevent excessive leniency in evaluation.
- **p. 5 / 3 Methodology - extractive body cue:** At, Ht = Fvlm(L, G, I, Ic t , Ht-1), (2) at = At(xt, Dc t), (3) where Ht, Ht are the high-level robot history, ...
- **p. 16 / C Implementation Details - extractive body cue:** E.2 Agent Setting We employed GPT-4o for agent construction.GPT-4o first receives our instruction inputs and returns JSON-formatted responses.
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 5 (3 Methodology), p. 16 (C Implementation Details), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 16 (C Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Thus, introduce, pose, graph, associated, RGB, images, output, pre-mapping, stage, basis, define, OWMM, problem | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | Thus, introduce, pose, graph, associated, RGB, images, output, pre-mapping, stage | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | summary, contributions, follows, OWMM-Agent, unified, VLM-based, agent, architecture, open-world, mobile | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | planners, generate, waypoints, satisfy, mechanical, constraints, base, chassis, joints, through | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Methodology - extractive body cue:** Thus, we introduce a pose graph G and associated RGB images I as the output of the pre-mapping stage on the basis of [37], and ...
- **p. 5 / 3 Methodology - extractive body cue:** Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to ...
- **p. 2 / 1 Introduction - extractive body cue:** To address the problem of domain adaptation, we further introduce an agentic data synthesis pipeline tailored for OWMM, to generate large-scale and instruction-driven episodes that ...
- **p. 3 / 1 Introduction - extractive body cue:** Octo [31] advances generalist robot policies, handling language commands and goal images while adapting quickly to new inputs and actions with standard GPUs. π0 [2] ...
- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose OWMM-Agent, a unified VLM-based agent architecture for open-world mobile manipulation, capable of global scene understanding, ...
- **p. 4 / 3 Methodology - extractive body cue:** The right panel showcases the Agent Space, where OWMM-VLM processes task instructions, robot history, and visual inputs to perform chain-of-thought reasoning and generate high-level actions ...
- **p. 5 / 3 Methodology - extractive body cue:** Following this insight, we train a versatile VLM model that takes the task instruction L, multimodal observations I, Ic t , and history Ht-1, and ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | Thus, we introduce a pose graph G and associated RGB images I as the output of the pre-mapping stage on the basis ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | This indicates that there is significant variation in the sizes of the goal receptacles in the test set. time step of duration ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | Given multiple posed frames and an egocentric frame, the VLM model needs to decide which action to conduct based on the task ... | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | As for the training time, OWMM-VLM-8B is trained on 8X NVIDIA A100 GPUs for about 7 hours, and OWMM-VLM-38B is trained on ... | hardware, batch and throughput |

## Training vs Inference

- **p. 13 / C Implementation Details - extractive body cue:** As for the training time, OWMM-VLM-8B is trained on 8X NVIDIA A100 GPUs for about 7 hours, and OWMM-VLM-38B is trained on 24X NVIDIA A100 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, linked, planner, takes, state, robot, point, clouds, converted, depth, additional, input, calculate, low-level, action, instruct, VLM, model, monitor, through.
- **Relevant PDF headings:** 3 Methodology (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, resulting in 400 episodes per ... | p. 7 (4 Dataset), p. 13 (C Implementation Details) |
| Base-arm task decision | OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | p. 9 (5 Experiments), p. 17 (C Implementation Details) |
| Execution / correction | Figure 5: OVMM-VLM-8B Sub-task Performance with the Increase of Training Data Size. The task scores consistently improve as the training data size ... | p. 15 (Figure/Table caption), p. 9 (5 Experiments) |

## Failure and Ablation Link

- **p. 17 / C Implementation Details - extractive body cue:** Hence, its effect is briefly shown only in the ablation study.
- **p. 7 / 5 Experiments - extractive body cue:** For the ablation study on model design, such as the choice of generating bounding boxes rather than points, please see Appendix G.
- **p. 17 / C Implementation Details - extractive body cue:** G Ablation Study on OWMM-VLM The ablation study evaluates the contributions of the components of the OWMM-VLM model.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: OWMM-Agent Operates Fetch Robot for Tidying Task. OWMM-Agent receives natural language instructions and leverages both long-term environment memory (scene images) and transient robot ...
- **p. 13 / C Implementation Details - extractive body cue:** Regarding the model's architecture, we have trained two variants consisting of 8 billion and 38 billion parameters, based on the pre-trained model from InternVL-2.5[5].
- **p. 8 / 5 Experiments - extractive body cue:** In other words, using the data from our data synthesis pipeline to conduct a supervised fine-tuning yields a significant enhancement in robotic decision-making performance.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Overview of OWMM-VLM. Our model is fine-tuned on InternVL-2.5[5], comprising a ViT, a 2-layer projection MLP, and a LLM. During training, ViT parameters ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), objective p. 5 (3 Methodology), p. 16 (C Implementation Details), p. 5 (3 Methodology), p. 16 (C Implementation Details), temporal p. 4 (3 Methodology), p. 17 (C Implementation Details), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 16 (C Implementation Details), p. 16 (C Implementation Details).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
