# Method - AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Continual Learning with Skill Expansion), p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.1. Overview), p. 5 (3.5. Task Planning Embodied Data Generation), p. 3 (3.1. Overview), p. 3 (3.1. Overview)): The left row shows the initial task state (top) and the skill-expert activation during inference (bottom). design inherently enables incremental learning in lifelong settings: when a new atomic skill is ...

## Method Body Digest

- **p. 5 / 3.4. Continual Learning with Skill Expansion - extractive body cue:** The left row shows the initial task state (top) and the skill-expert activation during inference (bottom). design inherently enables incremental learning in lifelong settings: when ...
- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** As illustrated in Algorithm 1, given the current visual observations O1:n t and task instruction ℓ, the model first predicts identifier either [think] or [act].
- **p. 4 / 3.1. Overview - extractive body cue:** Algorithm 1 Inference Pipeline of AtomicVLA Require: VLA model πθ, language instruction ℓ 1: t ←0, O1:n t ←initial image, Atomic ←none 2: while "task ...
- **p. 5 / 3.5. Task Planning Embodied Data Generation - extractive body cue:** To obtain accurate and reliable annotations of atomic actions, we propose a trajectory-based atomic decomposition method grounded in principal-axis analysis.
- **p. 3 / 3.1. Overview - extractive body cue:** Building upon this architecture, we develop a skill-guided library of atomic action experts (Sec.
- **p. 3 / 3.1. Overview - extractive body cue:** 2, AtomicVLA integrates the thinking modality for task planning and the acting modality for action execution within a unified framework (Sec.
- **p. 4 / 3.3. Skill-guided Mixture of Experts Architecture - extractive body cue:** The router computes a probability distribution over experts as: w _{k} = \tex t {Ro ut e r } ( Z_\sigma ), \quad k \in ...
- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** When the model outputs [think], it enters the thinking mode, in which it generates a task chain C0-k that outlines the high-level plan, tracks the ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions are as follows: • We introduce AtomicVLA, an end-to-end framework that unifies task planning and action execution for longhorizon tasks and continual ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose AtomicVLA, as illustrated in Fig.
- **p. 3 / 3.1. Overview - extractive body cue:** To further ensure the generation of high-quality task planning data, we introduce an embodiment data generation pipeline (Sec.

## Source Evidence Cues

- **p. 5 / 3.4. Continual Learning with Skill Expansion - extractive body cue:** The left row shows the initial task state (top) and the skill-expert activation during inference (bottom). design inherently enables incremental learning in lifelong settings: when ...
- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** As illustrated in Algorithm 1, given the current visual observations O1:n t and task instruction ℓ, the model first predicts identifier either [think] or [act].
- **p. 4 / 3.1. Overview - extractive body cue:** Algorithm 1 Inference Pipeline of AtomicVLA Require: VLA model πθ, language instruction ℓ 1: t ←0, O1:n t ←initial image, Atomic ←none 2: while "task ...
- **p. 5 / 3.5. Task Planning Embodied Data Generation - extractive body cue:** To obtain accurate and reliable annotations of atomic actions, we propose a trajectory-based atomic decomposition method grounded in principal-axis analysis.
- **p. 3 / 3.1. Overview - extractive body cue:** Building upon this architecture, we develop a skill-guided library of atomic action experts (Sec.
- **p. 3 / 3.1. Overview - extractive body cue:** 2, AtomicVLA integrates the thinking modality for task planning and the acting modality for action execution within a unified framework (Sec.
- **Detected method headings:** 2.1. Vision-Language-Action Models (p. 2); 3. Method (p. 3); 3.3. Skill-guided Mixture of Experts Architecture (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The left row shows the initial task state (top) and the skill-expert activation during inference (bottom). design inherently enables incremental learning in ... | p. 5 (3.4. Continual Learning with Skill Expansion), p. 4 (3.2. Unified Task Planning and Action Execution) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | As illustrated in Algorithm 1, given the current visual observations O1:n t and task instruction ℓ, the model first predicts identifier either ... | p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.1. Overview) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Algorithm 1 Inference Pipeline of AtomicVLA Require: VLA model πθ, language instruction ℓ 1: t ←0, O1:n t ←initial image, Atomic ←none ... | p. 4 (3.1. Overview), p. 5 (3.5. Task Planning Embodied Data Generation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3. Skill-guided Mixture of Experts Architecture - extractive body cue:** The router computes a probability distribution over experts as: w _{k} = \tex t {Ro ut e r } ( Z_\sigma ), \quad k \in ...
- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** When the model outputs [think], it enters the thinking mode, in which it generates a task chain C0-k that outlines the high-level plan, tracks the ...
- **p. 5 / 3.5. Task Planning Embodied Data Generation - extractive body cue:** Concurrently, gripper state transitions are tracked to infer action semantics and execution progress.
- **p. 5 / 3.4. Continual Learning with Skill Expansion - extractive body cue:** For each task, the top row shows the task progression, and the bottom row shows AtomicVLA's inferred outputs.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, thinking, mode, policy, takes, multiple, cameras, observations, language, instruction, input, outputs, high-level, task | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Specifically, thinking, mode, policy, takes, multiple, cameras, observations, language, instruction | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Overall, contributions, follows, introduce, AtomicVLA, end-to-end, framework, unifies, task, planning | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | router, computes, probability, distribution, over, experts, sigma, quad, dots, where | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** Specifically, in thinking mode, the policy takes multiple cameras observations O1:n t and a language instruction ℓas input and outputs a high-level task plan [C0-k, ...
- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** In contrast, in acting mode, the policy generates a concrete action command conditioned on the robot's proprioceptive state St and the most recent planning output ...
- **p. 2 / 1. Introduction - extractive body cue:** AtomicVLA first infers the current execution state from the input observations and dynamically activates either its thinking module or its acting module.
- **p. 2 / 1. Introduction - extractive body cue:** At task initialization or during transitions between sub-skills, the model triggers thinking to produce a task chain, create a task chain plan based on the ...
- **p. 5 / 3.5. Task Planning Embodied Data Generation - extractive body cue:** Based on the output of principal-axis analysis, we decompose a full task trajectory into a temporally ordered sequence of atomic action segments.
- **p. 1 / 1. Introduction - extractive body cue:** To support high-level reasoning and task planning, some existing approaches employ a two-stage architecture [1, 13, 18, 31, 37, 40], where a pretrained vision-language model ...
- **p. 5 / 3.5. Task Planning Embodied Data Generation - extractive body cue:** Concurrently, gripper state transitions are tracked to infer action semantics and execution progress.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Typically, this mode is activated only at key time steps, such as task initiation or during the transition between sub-skills. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Conversely, when [act] is predicted, the model switches to acting mode, where it produces a lowlevel action chunk At based on the ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Continual Learning with Skill Expansion - extractive body cue:** The left row shows the initial task state (top) and the skill-expert activation during inference (bottom). design inherently enables incremental learning in lifelong settings: when ...
- **p. 4 / 3.1. Overview - extractive body cue:** Algorithm 1 Inference Pipeline of AtomicVLA Require: VLA model πθ, language instruction ℓ 1: t ←0, O1:n t ←initial image, Atomic ←none 2: while "task ...
- **p. 8 / 4.3. Results on Real-world Robot - extractive body cue:** Red and green boxes highlight the key differences. number of training steps, AtomicVLA* acquires new skills more efficiently and achieves an overall improvement of 21% ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** left, initial, task, state, skill-expert, activation, during, inference, bottom, design, inherently, enables, incremental, learning, lifelong, settings, when, atomic, skill, introduced.
- **Relevant PDF headings:** 2.1. Vision-Language-Action Models (p. 2); 3. Method (p. 3); 3.3. Skill-guided Mixture of Experts Architecture (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We use 5 skill experts for both the LIBERO benchmark suite and real-world robot experiments. | p. 6 (4.1. Experiments Setup), p. 6 (4.1. Experiments Setup) |
| Action / skill decoding | When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the strong baseline by ... | p. 6 (4.2. Results on Simulation), p. 7 (4.3. Results on Real-world Robot) |
| Receding execution / feedback | 5, AtomicVLA achieves a success rate of 95.2%, outperforming the MoE baseline by 6.6% and the timestep-conditioned MoDE variant by 5.7%. | p. 8 (4.4. Ablation Study), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 4.4. Ablation Study - extractive body cue:** We conduct ablation experiments on the LIBERO-LONG benchmark to evaluate the effectiveness of our skill-aware routing mechanism.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** As a result, each expert still learns a mixture of skills without clear specialization.
- **p. 6 / 4.1. Experiments Setup - extractive body cue:** We build AtomicVLA and AtomicVLA* upon the pretrained \pi _ 0 and \pi _{0.5} foundation model.
- **p. 7 / 4.3. Results on Real-world Robot - extractive body cue:** Specifically, we first perform mixed training on four short-horizon tasks and train the "open" skill independently on top of the pretrained model.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Mixed-Training Skill Interference and Continual- Learning Degradation. The top two rows illustrate skill interfer- ence in long-horizon tasks: the first shows successful single-skill ...
- **p. 6 / 4.2. Results on Simulation - extractive body cue:** Importantly, when an execution failure occurs, for example, the butter is grasped but subsequently dropped as illustrated in Fig.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.4. Continual Learning with Skill Expansion), p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.1. Overview), p. 5 (3.5. Task Planning Embodied Data Generation), p. 3 (3.1. Overview), p. 3 (3.1. Overview), objective p. 4 (3.3. Skill-guided Mixture of Experts Architecture), p. 4 (3.2. Unified Task Planning and Action Execution), p. 5 (3.5. Task Planning Embodied Data Generation), p. 5 (3.4. Continual Learning with Skill Expansion), temporal p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.2. Unified Task Planning and Action Execution), p. 5 (3.5. Task Planning Embodied Data Generation), p. 5 (3.5. Task Planning Embodied Data Generation), p. 6 (4.2. Results on Simulation), p. 8 (4.4. Ablation Study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** In contrast, in acting mode, the policy generates a concrete action command conditioned on the robot's proprioceptive state St and the most recent planning output σ. (p. 4, 3.2. Unified Task Planning and Action Execution).
- **Objective/update evidence:** Building upon this architecture, we develop a skill-guided library of atomic action experts (Sec. (p. 3, 3.1. Overview).
- **Temporal/runtime evidence:** By aligning these refined labels with the full trajectory, we construct a structured reasoning chain comprising the sequence of executed atomic actions and the associated high-level plan for subsequent steps. (p. 5, 3.5. Task Planning Embodied Data Generation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
