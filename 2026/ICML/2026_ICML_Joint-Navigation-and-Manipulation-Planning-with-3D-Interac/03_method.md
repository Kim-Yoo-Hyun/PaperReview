# Method - Joint Navigation and Manipulation Planning with 3D Interaction Chains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=oVB2xYWvpv; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/327408. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 4 (4.1. Unified Modeling of Multi-stage Interaction), p. 5 (4.2. 3D-IC Construction), p. 6 (4.3. Joint Planning with 3D-IC), p. 4 (4.1. Unified Modeling of Multi-stage Interaction)): Formally, given RGB-D observations It, the robot first builds a 3D feature map Mt.

## Method Body Digest

- **p. 3 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** Formally, given RGB-D observations It, the robot first builds a 3D feature map Mt.
- **p. 3 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** On the action side, the policy is decomposed into: (1) a high-level policy operating on Mt that outputs a sequence of interaction waypoints and action ...
- **p. 4 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** In the chain decision stage, joint planning is employed to ultimately select the interaction waypoints for execution, which are then dispatched to the local policy ...
- **p. 5 / 4.2. 3D-IC Construction - extractive PDF cue:** To obtain an interaction chain ct = {(wk, uk)}K k=1, candidate interaction waypoints wk and their associated action tokens uk are first generated from the ...
- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** Then we execute actions on sampled waypoints to gather simulator feedback and post-execution RGB images.
- **p. 4 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** Candidate interaction waypoints are generated on the 3D feature map to construct candidate interaction chains.
- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** For training data collection, we traverse scenes to construct 3D feature maps, from which interaction waypoints, 3D tokens, and valid trajectories are collected.
- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** The policy is optimized using a standard autoregressive cross-entropy loss: L(θ) = -PT t=1 log pθ (xt / xprompt, x<t), where the loss is computed ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our 3D-IC includes: (1) a 3D feature map that captures information needed for both navigation and manipulation, (2) an interaction chain that enables unified planning ...
- **p. 5 / 4.2. 3D-IC Construction - extractive PDF cue:** Following frontier-based exploration (FBE) (Yamauchi, 1997), repeatedly navigating to frontier locations enables the robot to progressively reveal unknown areas and discover targets.

## Source Evidence Cues

- **p. 3 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** Formally, given RGB-D observations It, the robot first builds a 3D feature map Mt.
- **p. 3 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** On the action side, the policy is decomposed into: (1) a high-level policy operating on Mt that outputs a sequence of interaction waypoints and action ...
- **p. 4 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** In the chain decision stage, joint planning is employed to ultimately select the interaction waypoints for execution, which are then dispatched to the local policy ...
- **p. 5 / 4.2. 3D-IC Construction - extractive PDF cue:** To obtain an interaction chain ct = {(wk, uk)}K k=1, candidate interaction waypoints wk and their associated action tokens uk are first generated from the ...
- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** Then we execute actions on sampled waypoints to gather simulator feedback and post-execution RGB images.
- **p. 4 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** Candidate interaction waypoints are generated on the 3D feature map to construct candidate interaction chains.
- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** For training data collection, we traverse scenes to construct 3D feature maps, from which interaction waypoints, 3D tokens, and valid trajectories are collected.
- **Detected method headings:** 4.1. Unified Modeling of Multi-stage Interaction (p. 3); 5.4. Comparison with SOTA Methods (p. 9)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | Formally, given RGB-D observations It, the robot first builds a 3D feature map Mt. | p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | On the action side, the policy is decomposed into: (1) a high-level policy operating on Mt that outputs a sequence of interaction ... | p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 4 (4.1. Unified Modeling of Multi-stage Interaction) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | In the chain decision stage, joint planning is employed to ultimately select the interaction waypoints for execution, which are then dispatched to ... | p. 4 (4.1. Unified Modeling of Multi-stage Interaction), p. 5 (4.2. 3D-IC Construction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** The policy is optimized using a standard autoregressive cross-entropy loss: L(θ) = -PT t=1 log pθ (xt / xprompt, x<t), where the loss is computed ...
- **p. 5 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** The optimal chain is selected by balancing (1) progress toward completion, (2) waypoint feasibility, and (3) travel cost: c⋆ t = arg max ct∈C h ...
- **p. 5 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** During inference, all candidate chains are first pre-ranked according to the progress toward completion and travel cost.
- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** To enable the VLM to accurately estimate the feasibility probability P(wk) and reason over candidate interaction chains, we fine-tune Qwen2.5-VL-7B on a curriculum of decision-oriented ...
- **p. 4 / 4.2. 3D-IC Construction - extractive PDF cue:** Since Mt is continuously updated, features from multiple viewpoints may be projected to the same 3D location.
- **p. 4 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** Notably, selecting c⋆ t performs joint planning over multiple stages, which accounts for both long-horizon navigational feasibility and local interaction feasibility.
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 6 (4.3. Joint Planning with 3D-IC), p. 6 (4.3. Joint Planning with 3D-IC), p. 4 (4.2. 3D-IC Construction), p. 5 (4.2. 3D-IC Construction), p. 5 (4.2. 3D-IC Construction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | navigation, policy, takes, input, outputs, base, actions, Forward, Left, Right, whereas, manipulation, single-step, observation | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | navigation, policy, takes, input, outputs, base, actions, Forward, Left, Right | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | summary, Interaction, Chains, D-IC, OVMM, task, includes, feature, captures, information | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | policy, optimized, standard, autoregressive, cross-entropy, loss, xprompt, where, computed, only | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Preliminaries of Mobile Manipulation - extractive PDF cue:** The navigation policy πn takes mt as input and outputs base actions an t ∈{Forward, Left, Right}, whereas the manipulation policy πm takes the single-step ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our goal is joint planning for OVMM, while navigation and manipulation differ substantially in both inputs and outputs: navigation typically conditions on the accumulated history ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The shared high-level policy takes the 3D feature map as input and predicts interaction waypoints along with discrete action tokens (e.g., move or grasp), while ...
- **p. 3 / 4.1. Unified Modeling of Multi-stage Interaction - extractive PDF cue:** On the action side, the policy is decomposed into: (1) a high-level policy operating on Mt that outputs a sequence of interaction waypoints and action ...
- **p. 4 / 4.2. 3D-IC Construction - extractive PDF cue:** The 3D feature map Mt grounds semantic observations in the 3D geometry of the environment, and subsequent interaction waypoints are selected from it.
- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** Then we execute actions on sampled waypoints to gather simulator feedback and post-execution RGB images.
- **p. 4 / 4.2. 3D-IC Construction - extractive PDF cue:** As the robot moves through the environment, it continuously acquires egocentric RGB-D observations It = (Ir t , Id t ) and the camera pose ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | Under these rules, a set of candidate interaction chains Ct = {ct} can be generated at each time step t, and updated ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive PDF cue:** For training data collection, we traverse scenes to construct 3D feature maps, from which interaction waypoints, 3D tokens, and valid trajectories are collected.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Formally, given, RGB-D, observations, robot, first, builds, feature, action, side, policy, decomposed, high-level, operating, outputs, sequence, interaction, waypoints, tokens, lowlevel.
- **Relevant PDF headings:** 4.1. Unified Modeling of Multi-stage Interaction (p. 3); 5.4. Comparison with SOTA Methods (p. 9).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including ... | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Base-arm task decision | Our method consistently outperforms prior works, establishing new state-of-the-art performance across all metrics. | p. 9 (5.3. Real-world Evaluation), p. 8 (5.2. Evaluation Results) |
| Execution / correction | Experimental results validate improvements in both success rate and efficiency (SPL). | p. 7 (5.2. Evaluation Results), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 5.2. Evaluation Results - extractive PDF cue:** Ablation on 3D Interaction Point Representations.
- **p. 8 / 5.2. Evaluation Results - extractive PDF cue:** Ablation study on multi stage planning.
- **p. 8 / 5.2. Evaluation Results - extractive PDF cue:** 8, we find that adding TI consistently improves performance over training without it.
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** The decision-making component employs a fine-tuned Qwen2.5-VL-7B model.
- **p. 7 / 5.2. Evaluation Results - extractive PDF cue:** Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to table baseline baseline 3D-IC 3D-IC High Navigation ...
- **p. 8 / 5.3. Real-world Evaluation - extractive PDF cue:** Consequently, the agent navigated back to a nightstand in the initial room to complete the placement, thereby avoiding a potential failure.
- **p. 9 / 5.4. Comparison with SOTA Methods - extractive PDF cue:** The consistently high SPL scores indicate that our method achieves efficient trajectory, rather than merely reducing step counts through premature termination or failure cases (i.e., ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 4 (4.1. Unified Modeling of Multi-stage Interaction), p. 5 (4.2. 3D-IC Construction), p. 6 (4.3. Joint Planning with 3D-IC), p. 4 (4.1. Unified Modeling of Multi-stage Interaction), objective p. 6 (4.3. Joint Planning with 3D-IC), p. 5 (4.3. Joint Planning with 3D-IC), p. 5 (4.3. Joint Planning with 3D-IC), p. 6 (4.3. Joint Planning with 3D-IC), p. 4 (4.2. 3D-IC Construction), p. 4 (4.1. Unified Modeling of Multi-stage Interaction), temporal p. 5 (4.2. 3D-IC Construction), p. 6 (5.1. Experimental Setup), p. 1 (1. Introduction), p. 2 (2. Related Work), p. 6 (5.1. Experimental Setup), p. 7 (5.2. Evaluation Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
