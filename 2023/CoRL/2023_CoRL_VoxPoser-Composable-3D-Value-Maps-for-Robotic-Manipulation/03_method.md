# Method - VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.05973; PDF retrieval source: https://arxiv.org/pdf/2307.05973. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 8 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method)): Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment observation at time t and at = MPC(ot), ...

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment observation at time ...
- **p. 8 / 3 Method - extractive body cue:** We conduct experiments in simulation where we have access to ground-truth perception and dynamics model (i.e., the simulator). . "Dynamics error" refers to errors made ...
- **p. 4 / 3 Method - extractive body cue:** We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where each waypoint consists ...
- **p. 5 / 3 Method - extractive body cue:** We use simple zeroth-order optimization by randomly sampling trajectories and scoring them with the proposed objective.
- **p. 6 / 3 Method - extractive body cue:** We use a heuristic-based dynamics model that translates an input point cloud along the push direction by the push distance.
- **p. 6 / 3 Method - extractive body cue:** We use the known robot dynamics model in all tasks, where it is used in motion planning for the end-effector to follow the waypoints.
- **p. 4 / 3 Method - extractive body cue:** The composed value maps then serve as objective functions for motion planners to synthesize trajectories for robot manipulation (b).
- **p. 5 / 3 Method - extractive body cue:** Note that while these additional trajectory parametrizations are not mapped to a real-valued "cost", they can also be factored in the optimization procedure (Equation 1) ...

## Design Rationale

- **p. 4 / 3 Method - extractive body cue:** We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where each waypoint consists ...
- **p. 2 / 1 Introduction - extractive body cue:** Rather than relying on robotic data that are often of limited amount or variability, the method leverages LLMs for open-world reasoning and VLMs for generalizable ...
- **p. 3 / 3 Method - extractive body cue:** The central problem 2Note that the decomposition and sequencing of these sub-tasks are also done by LLMs in this work, though we do not investigate ...

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment observation at time ...
- **p. 8 / 3 Method - extractive body cue:** We conduct experiments in simulation where we have access to ground-truth perception and dynamics model (i.e., the simulator). . "Dynamics error" refers to errors made ...
- **p. 4 / 3 Method - extractive body cue:** We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where each waypoint consists ...
- **p. 5 / 3 Method - extractive body cue:** We use simple zeroth-order optimization by randomly sampling trajectories and scoring them with the proposed objective.
- **p. 6 / 3 Method - extractive body cue:** We use a heuristic-based dynamics model that translates an input point cloud along the push direction by the push distance.
- **p. 6 / 3 Method - extractive body cue:** We use the known robot dynamics model in all tasks, where it is used in motion planning for the end-effector to follow the waypoints.
- **p. 4 / 3 Method - extractive body cue:** The composed value maps then serve as objective functions for motion planners to synthesize trajectories for robot manipulation (b).
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment ... | p. 5 (3 Method), p. 8 (3 Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We conduct experiments in simulation where we have access to ground-truth perception and dynamics model (i.e., the simulator). . "Dynamics error" refers ... | p. 8 (3 Method), p. 4 (3 Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where ... | p. 4 (3 Method), p. 5 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Method - extractive body cue:** Note that while these additional trajectory parametrizations are not mapped to a real-valued "cost", they can also be factored in the optimization procedure (Equation 1) ...
- **p. 4 / 3 Method - extractive body cue:** Ftask scores the extent of Ti completes the instruction ℓi while Fcontrol specifies the control costs, e.g., to encourage τ r i to minimize total ...
- **p. 5 / 3 Method - extractive body cue:** 3.3 Zero-Shot Trajectory Synthesis with VoxPoser After obtaining the task cost Ftask, we can now approach the full problem defined in Equation 1 to plan ...
- **p. 7 / 3 Method - extractive body cue:** Compared to learned cost specification, LLMs generalize better by explicitly reasoning about affordances and constraints.
- **p. 4 / 3 Method - extractive body cue:** def affordance_map(): msize = (100,100,100) map = np.zeros(msize) handles = detect('handle') k = lambda x: x.pos[2] handles.sort(key=k) top_handle = handles[-1] x,y,z = top_handle.pos map[x,y,z] = ...
- **p. 7 / 3 Method - extractive body cue:** We find that compared to chaining sequential policy logic, the ability to compose spatially while considering other constraints under a joint optimization scheme is a ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 7 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | value, LMPs, define, high-level, orchestrate, behaviors, planner, takes, user, instruction, input, open, drawer, outputs | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | value, LMPs, define, high-level, orchestrate, behaviors, planner, takes, user, instruction | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | represent, sequence, dense, end-effector, waypoints, executed, Operational, Space, Controller, where | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Note, while, additional, trajectory, parametrizations, mapped, real-valued, cost, they, factored | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3 Method - extractive body cue:** On top of value map LMPs, we define two high-level LMPs to orchestrate their behaviors: planner takes user instruction L as input (e.g., "open drawer") ...
- **p. 4 / 3 Method - extractive body cue:** Given the RGB-D observation of the environment and a language instruction, LLMs generate code, which interacts with VLMs, to produce a sequence of 3D affordance ...
- **p. 6 / 3 Method - extractive body cue:** Each type uses a different LMP, which takes in an instruction and outputs a voxel map of shape (100, 100, 100, k), where k differs ...
- **p. 3 / 3 Method - extractive body cue:** Then we describe how VoxPoser can be used as a general zero-shot framework to map language instructions to 3D value maps (Sec.
- **p. 2 / 1 Introduction - extractive body cue:** We look at the problem of grounding abstract language instructions (e.g., "set up the table") in robot actions [5].
- **p. 2 / 1 Introduction - extractive body cue:** We term this approach VOXPOSER , a formulation that extracts affordances and constraints from LLMs to compose 3D value maps in observation space for guiding ...
- **p. 5 / 3 Method - extractive body cue:** Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment observation at time ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | 3.3 presents a zero-shot framework for synthesizing trajectories for robot manipulation, VoxPoser can also benefit from online experiences by efficiently learning a ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The optimization is implemented in a model predictive control framework that iteratively replans the trajectory at every step using the current observation ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | At the start of each rollout, both cameras start recording and return the real-time RGB-D observations at 20 Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Method - extractive body cue:** Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment observation at time ...
- **p. 4 / 3 Method - extractive body cue:** Given the RGB-D observation of the environment and a language instruction, LLMs generate code, which interacts with VLMs, to produce a sequence of 3D affordance ...
- **p. 5 / 3 Method - extractive body cue:** Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment observation at time ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Consider, standard, setup, where, robot, interleaves, between, collecting, environment, transition, data, observation, time, MPC, training, dynamics, model, parametrized, minimizing, loss.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 4.2 Generalization to Unseen Instructions and Attributes To provide rigorous quantitative evaluations on generalization, we set up a simulated block-world environment that ... | p. 7 (3 Method), p. 18 (A.1 Code Release) |
| Action / skill decoding | VoxPoser outperforms both baselines across 13 tasks from two categories on both seen and unseen tasks and maintains similar success rates. smoother ... | p. 7 (3 Method), p. 7 (3 Method) |
| Receding execution / feedback | VoxPoser outperforms both baselines across 13 tasks from two categories on both seen and unseen tasks and maintains similar success rates. smoother ... | p. 7 (3 Method), p. 22 (A.5.2 Full Results on Simulated Environments) |

## Failure and Ablation Link

- **p. 7 / 3 Method - extractive body cue:** For baselines, we ablate the two components of VoxPoser, LLM and motion planner, by comparing to a variant of [75] that combines an LLM with ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: VOXPOSER extracts language-conditioned affordances and constraints from LLMs and grounds them to the perceptual space using VLMs, using a code interface and without ...
- **p. 7 / 3 Method - extractive body cue:** We further compare to a variant of Code as Policies [75] that uses LLMs to parameterize a pre-defined list of simple primitives (e.g., move to ...
- **p. 8 / 3 Method - extractive body cue:** In comparison, exploring without prior all exceed the maximum 12-hour limit.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Error breakdown of components. Vox- Poser significantly reduces specification error. each represented as a sequence of end-effector waypoints, that act as priors for ...
- **p. 20 / A.4 Real-World Environment Setup - extractive body cue:** For each task, we evaluate each method on two settings: without and with disturbances.
- **p. 20 / A.4 Real-World Environment Setup - extractive body cue:** We compare to a variant of Code as Policies [75] as a baseline that uses an LLM with action primitives.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Method), p. 8 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), objective p. 5 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 7 (3 Method), temporal p. 5 (3 Method), p. 5 (3 Method), p. 20 (A.4 Real-World Environment Setup), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment observation at time t and at = MPC(ot), ... (p. 5, 3 Method).
- **Objective/update evidence:** Note that while these additional trajectory parametrizations are not mapped to a real-valued "cost", they can also be factored in the optimization procedure (Equation 1) to parametrize the trajectories. (p. 5, 3 Method).
- **Temporal/runtime evidence:** The optimization is implemented in a model predictive control framework that iteratively replans the trajectory at every step using the current observation to robustly execute the trajectories even under dynamic ... (p. 5, 3 Method).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
