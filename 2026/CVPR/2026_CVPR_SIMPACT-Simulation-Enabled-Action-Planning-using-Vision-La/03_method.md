# Method - SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Front matter), p. 1 (Front matter), p. 3 (Front matter), p. 3 (Front matter), p. 2 (Front matter), p. 2 (Front matter)): For rigid objects, the numerical state consists of their full 6-DoF rigid transformation.

## Method Body Digest

- **p. 1 / Front matter - extractive body cue:** For rigid objects, the numerical state consists of their full 6-DoF rigid transformation.
- **p. 1 / Front matter - extractive body cue:** Optimization Context c Generation To instantiate the OPTIMIZE function, we construct the context ci from the action sequence ai and the simulated state rollout si.
- **p. 3 / Front matter - extractive body cue:** These tasks appear more sensitive to accurate physical modeling and contact dynamics.
- **p. 3 / Front matter - extractive body cue:** Only the first entry is shown for repeated fields, with omitted entries summarized using comments. quences for task success, we also include 10 unoptimized VLM ...
- **p. 2 / Front matter - extractive body cue:** Action Optimization We provide details the action optimization prompt `opt in Fig.
- **p. 2 / Front matter - extractive body cue:** Your objective is to decompose a high-level natural language instruction into multiple distinct, high-level action plans.
- **p. 4 / Front matter - extractive body cue:** Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task.
- **p. 2 / Front matter - extractive body cue:** Additional Qualitative Results We show qualitative results for the sweeping task that was not included in the main paper due to space constraints in Fig.

## Design Rationale

- **p. 1 / Front matter - extractive body cue:** For rigid objects, the numerical state consists of their full 6-DoF rigid transformation.
- **p. 1 / Front matter - extractive body cue:** Additionally, we present more qualitative examples, an ablation on the number of VLM-sampled action proposals, and a study comparing a CEM-based Prompting-with-theFuture-style variant [45], which ...
- **p. 2 / Front matter - extractive body cue:** Further Ablation Analysis We additionally consider a variant of our method in which we simultaneously replace the VLM sampler with a random sampler and switch ...

## Source Evidence Cues

- **p. 1 / Front matter - extractive body cue:** For rigid objects, the numerical state consists of their full 6-DoF rigid transformation.
- **p. 1 / Front matter - extractive body cue:** Optimization Context c Generation To instantiate the OPTIMIZE function, we construct the context ci from the action sequence ai and the simulated state rollout si.
- **p. 3 / Front matter - extractive body cue:** These tasks appear more sensitive to accurate physical modeling and contact dynamics.
- **p. 3 / Front matter - extractive body cue:** Only the first entry is shown for repeated fields, with omitted entries summarized using comments. quences for task success, we also include 10 unoptimized VLM ...
- **p. 2 / Front matter - extractive body cue:** Action Optimization We provide details the action optimization prompt `opt in Fig.
- **p. 2 / Front matter - extractive body cue:** Your objective is to decompose a high-level natural language instruction into multiple distinct, high-level action plans.
- **p. 4 / Front matter - extractive body cue:** Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | For rigid objects, the numerical state consists of their full 6-DoF rigid transformation. | p. 1 (Front matter), p. 1 (Front matter) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Optimization Context c Generation To instantiate the OPTIMIZE function, we construct the context ci from the action sequence ai and the simulated ... | p. 1 (Front matter), p. 3 (Front matter) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | These tasks appear more sensitive to accurate physical modeling and contact dynamics. | p. 3 (Front matter), p. 3 (Front matter) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / Front matter - extractive body cue:** Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task.
- **p. 2 / Front matter - extractive body cue:** Your objective is to decompose a high-level natural language instruction into multiple distinct, high-level action plans.
- **p. 2 / Front matter - extractive body cue:** Additional Qualitative Results We show qualitative results for the sweeping task that was not included in the main paper due to space constraints in Fig.
- **p. 1 / Front matter - extractive body cue:** Optimization Context c Generation To instantiate the OPTIMIZE function, we construct the context ci from the action sequence ai and the simulated state rollout si.
- **p. 1 / Front matter - extractive body cue:** We describe the full simulation-construction pipeline, including VLMbased prediction of rigid and deformable object parameters, as well as the symbolic action space and prompting strategy ...
- **p. 3 / Front matter - extractive body cue:** Example rollout context for action optimization in pivoting task.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 2 (Front matter), p. 2 (Front matter), p. 4 (Front matter), p. 5 (Front matter), p. 5 (Front matter), p. 6 (Front matter).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Input, Specification, Task, Instruction, Main, goal, Real-World, Context, Workspace, limits, safe, ranges, Simulation, Rollouts | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Input, Specification, Task, Instruction, Main, goal, Real-World, Context, Workspace, limits | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | rigid, objects, numerical, state, consists, full, DoF, transformation, Additionally, present | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Your, objective, analyze, simulation, rollouts, optimized, action, plan, real-world, task | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / Front matter - extractive body cue:** Input Specification • Task Instruction: Main task goal. • Real-World Context: Workspace limits, safe ranges • Simulation Rollouts: Specify the format of input context describing ...
- **p. 2 / Front matter - extractive body cue:** Input Specification • Image of the Scene: Visual observation of the workspace. • Additional Scene Context: Object and end-effector coordinates in the world frame, workspace ...
- **p. 2 / Front matter - extractive body cue:** This prompt includes task specifications, input requirements, action primitive definitions, planning guidelines, and output format.
- **p. 3 / Front matter - extractive body cue:** The context contains the action waypoints and the simulated state snapshots at each waypoint, including gripper pose, object poses, and screenshot paths.
- **p. 1 / Front matter - extractive body cue:** We sample the state at the end of each symbolic action, where each action specifies the gripper's Cartesian position (x, y, z) and orientation (roll, ...
- **p. 1 / Front matter - extractive body cue:** Optimization Context c Generation To instantiate the OPTIMIZE function, we construct the context ci from the action sequence ai and the simulated state rollout si.
- **p. 4 / Front matter - extractive body cue:** It is combined with simulation rollout context as input to the VLM action optimizer to generate optimized action sequences.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Optimization Context c Generation To instantiate the OPTIMIZE function, we construct the context ci from the action sequence ai and the simulated ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | 1) Analyze Rollouts: Inspect each rollout's action sequence, robot/object poses at each waypoint, and screenshots. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Front matter - extractive body cue:** Optimization Context c Generation To instantiate the OPTIMIZE function, we construct the context ci from the action sequence ai and the simulated state rollout si.
- **p. 4 / Front matter - extractive body cue:** Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** rigid, objects, numerical, state, consists, full, DoF, transformation, Optimization, Context, Generation, instantiate, OPTIMIZE, function, construct, action, sequence, simulated, rollout, tasks.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task. | p. 4 (Front matter), p. 3 (Front matter) |
| Action / skill decoding | Our zero-shot method outperforms imitation learning baseline HULC [40] and VLA baseline Figure 14. | p. 5 (Front matter), p. 5 (Front matter) |
| Receding execution / feedback | We evaluate this variant and find that it consistently achieves a zero success rate across all of our real-world tasks. | p. 2 (Front matter), p. 5 (Front matter) |

## Failure and Ablation Link

- **p. 2 / Front matter - extractive body cue:** Further Ablation Analysis We additionally consider a variant of our method in which we simultaneously replace the VLM sampler with a random sampler and switch ...
- **p. 2 / Front matter - extractive body cue:** Notably, this simplified variant is algorithmically identical to Prompting-with-the-Future (PWTF) [45].
- **p. 5 / Front matter - extractive body cue:** These execution failures highlight the sensitivity and difficulty of our tasks: even minor errors in the planned actions can lead to failure.
- **p. 3 / Front matter - extractive body cue:** The VLM planning stage is the most time-consuming component.
- **p. 3 / Front matter - extractive body cue:** Computation Time Table 5 reports the runtime of each component in our method.
- **p. 4 / Front matter - extractive body cue:** Component Time (mins) simulation construction 1.9 action sampling 2.8 simulation rollout 0.8 action optimization 0.9 on the task.
- **p. 2 / Front matter - extractive body cue:** Correlation Between Simulation and RealWorld Performance This section examines the correlation between simulation and real-world results, specifically whether success or failure in simulation predicts the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Front matter), p. 1 (Front matter), p. 3 (Front matter), p. 3 (Front matter), p. 2 (Front matter), p. 2 (Front matter), objective p. 4 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 1 (Front matter), p. 1 (Front matter), p. 3 (Front matter), temporal p. 1 (Front matter), p. 4 (Front matter), p. 4 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 2 (Front matter).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
