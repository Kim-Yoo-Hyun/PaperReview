# Method - SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3. Method), p. 4 (3.1. Simulation Construction), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3. Method)): 1, our planner takes as input the initial RGB-D observation I0, the initial simulator state s0, task description `task, VLM, and SIM.

## Method Body Digest

- **p. 4 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** 1, our planner takes as input the initial RGB-D observation I0, the initial simulator state s0, task description `task, VLM, and SIM.
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** In particular, at each selected time step t, we render a simulator observation image Ii t and include the numerical action ai t and state ...
- **p. 3 / 3. Method - extractive body cue:** The resulting visual observations and object states from each rollout are then fed back to the VLM as additional context for iterative refinement.
- **p. 4 / 3.1. Simulation Construction - extractive body cue:** Each reconstructed mesh is then centered and scaled according to the size of its corresponding real-world bounding box obtained from point cloud segmentation, yielding Mi ...
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** Given sampled action sequences A = {ai}K i=1, we first perform simulation rollouts to obtain their corresponding state trajectories S = {si}K i=1.
- **p. 3 / 3. Method - extractive body cue:** Next, we instantiate a manipulation planner that integrates the simulator with a VLM as its core reasoning module.
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** If the VLM determines that the proposed action sequence achieves the task objective, the sequence is executed in the real environment.
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** From these proposals, the VLM optimizer reasons a non-trivial action update that pushes the bottle for the correct distance without toppling in both simulation and ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We present ...
- **p. 2 / 1. Introduction - extractive body cue:** By augmenting VLMs with physical simulation, our framework enables them to anticipate action consequences, evaluate predicted outcomes, and iteratively adjust their decisions at test time, ...
- **p. 3 / 3. Method - extractive body cue:** Our framework enables zero-shot robotic manipulation action generation from a single RGB-D image input I0 and natural language instruction `task and outputs robot action sequence ...

## Source Evidence Cues

- **p. 4 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** 1, our planner takes as input the initial RGB-D observation I0, the initial simulator state s0, task description `task, VLM, and SIM.
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** In particular, at each selected time step t, we render a simulator observation image Ii t and include the numerical action ai t and state ...
- **p. 3 / 3. Method - extractive body cue:** The resulting visual observations and object states from each rollout are then fed back to the VLM as additional context for iterative refinement.
- **p. 4 / 3.1. Simulation Construction - extractive body cue:** Each reconstructed mesh is then centered and scaled according to the size of its corresponding real-world bounding box obtained from point cloud segmentation, yielding Mi ...
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** Given sampled action sequences A = {ai}K i=1, we first perform simulation rollouts to obtain their corresponding state trajectories S = {si}K i=1.
- **p. 3 / 3. Method - extractive body cue:** Next, we instantiate a manipulation planner that integrates the simulator with a VLM as its core reasoning module.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 1, our planner takes as input the initial RGB-D observation I0, the initial simulator state s0, task description `task, VLM, and SIM. | p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 5 (3.2. Action Planning via Simulation-enabled VLM) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In particular, at each selected time step t, we render a simulator observation image Ii t and include the numerical action ai ... | p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3. Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The resulting visual observations and object states from each rollout are then fed back to the VLM as additional context for iterative ... | p. 3 (3. Method), p. 4 (3.1. Simulation Construction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** If the VLM determines that the proposed action sequence achieves the task objective, the sequence is executed in the real environment.
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** From these proposals, the VLM optimizer reasons a non-trivial action update that pushes the bottle for the correct distance without toppling in both simulation and ...
- **p. 3 / 3. Method - extractive body cue:** Finally, the optimized action sequence is executed as end-effector commands on the real robot system.
- **p. 4 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** Using both A and S, a VLM-based optimizer refines the proposed action sequences and produces a new action sequence ak.
- **p. 4 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** I0, `task, s0; VLM " }; 5 S S [ {si SIMROLLOUT ! s0, ai; SIM " }; // Iterative action optimization 6 for k ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 5 (3.2. Action Planning via Simulation-enabled VLM).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | framework, enables, zero-shot, robotic, manipulation, action, generation, single, RGB-D, image, input, natural, language, instruction | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | framework, enables, zero-shot, robotic, manipulation, action, generation, single, RGB-D, image | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, makes, following, contributions, introduce, test-time, zero-shot, framework, enabling, VLMs | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | VLM, determines, action, sequence, achieves, task, objective, executed, real, environment | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive body cue:** Our framework enables zero-shot robotic manipulation action generation from a single RGB-D image input I0 and natural language instruction `task and outputs robot action sequence ...
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** In particular, at each selected time step t, we render a simulator observation image Ii t and include the numerical action ai t and state ...
- **p. 4 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** 1, our planner takes as input the initial RGB-D observation I0, the initial simulator state s0, task description `task, VLM, and SIM.
- **p. 3 / 3.1. Simulation Construction - extractive body cue:** We initialize the state as s0, assuming objects remain static prior to interaction, and construct parameters via ✓= CreateSim(I0) from the initial RGBD image I0.
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** Given the simulation rollout sk, we render the final simulation state and extract both an observation image Ik T and the simulator state sk T ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose a framework that augments VLMs with physical simulation rollouts as contextual feedback, enabling test-time physical reasoning for action planning.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We present ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | For each action sequence, we construct an optimization context ci by subsampling time steps and gathering intermediate information. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The simulation follows the discrete-time state transition: st = SIM(st-1, at; ✓) (1) where st denotes the state at time step t, ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For each task, we run 10 trials per method. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Method - extractive body cue:** The resulting visual observations and object states from each rollout are then fed back to the VLM as additional context for iterative refinement.
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** Given sampled action sequences A = {ai}K i=1, we first perform simulation rollouts to obtain their corresponding state trajectories S = {si}K i=1.
- **p. 8 / 4.3. Ablation study - extractive body cue:** 1) affects performance, reporting success rates over 10 trials in Table 4: using only 3 samples degrades performance, as limited rollouts fail to provide sufficient ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** planner, takes, input, initial, RGB-D, observation, simulator, state, task, description, VLM, SIM, particular, selected, time, step, render, image, include, numerical.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We use ⇡0.5 [2], a recent open-source VLA model pretrained on a large robot manipulation dataset, as a representative baseline. | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Action / skill decoding | Overall, our method consistently outperforms baseline methods across all evaluated tasks, highlighting its strong performance on challenging, physicsaware, fine-grained manipulation tasks. | p. 7 (4.2. Results), p. 8 (4.3. Ablation study) |
| Receding execution / feedback | Our approach consistently achieves a substantially higher success rate than baselines, highlighting the effectiveness of simulation-enabled VLMs for action planning. | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results) |

## Failure and Ablation Link

- **p. 7 / 4.3. Ablation study - extractive body cue:** (2) Removing simulation rollout context: We evaluate whether current VLMs can reason effectively without simulation rollouts.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation. Success rates (%) over 10 trials for each task after removing each component of our method. Results demonstrate the importance of VLM-conditioned ...
- **p. 5 / 4. Experiments - extractive body cue:** We validate our design choices through systematic ablation studies.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For simulation, we implement the projective dynamics variant solver using PyTorch [47] and the MPM simulator using Warp [39].
- **p. 8 / 4.3. Ablation study - extractive body cue:** This indicates that language-based reasoning without physical grounding cannot reliably infer successful action.
- **p. 8 / 4.3. Ablation study - extractive body cue:** However, the variant still outperforms baseline methods, largely due to the hierarchical action sampling strategy introduced in Sec.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Action optimization process. We show a representative example from the non-toppling push task. The left three images show simulation rollouts from initial VLM-sampled ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3. Method), p. 4 (3.1. Simulation Construction), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3. Method), objective p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3. Method), p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 4 (3.2. Action Planning via Simulation-enabled VLM), temporal p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3.1. Simulation Construction), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3. Method), p. 4 (3.1. Simulation Construction), p. 4 (3.1. Simulation Construction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 1, our planner takes as input the initial RGB-D observation I0, the initial simulator state s0, task description `task, VLM, and SIM. (p. 4, 3.2. Action Planning via Simulation-enabled VLM).
- **Objective/update evidence:** From these proposals, the VLM optimizer reasons a non-trivial action update that pushes the bottle for the correct distance without toppling in both simulation and real-world execution. (p. 5, 3.2. Action Planning via Simulation-enabled VLM).
- **Temporal/runtime evidence:** For each action sequence, we construct an optimization context ci by subsampling time steps and gathering intermediate information. (p. 5, 3.2. Action Planning via Simulation-enabled VLM).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
