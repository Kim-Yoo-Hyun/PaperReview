# Method - Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.08605; PDF retrieval source: https://arxiv.org/pdf/2403.08605. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 4 (IV. MOMA-LLM), p. 1 (2 Toyota Motor Europe (TME)), p. 3 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM)): In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the environment is explored.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the ...
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the following high-level actions: navigate(room_name, object_name): Navigation to an object in a room via an A∗planner in the explored BEV-map Bt, inflated ...
- **p. 1 / 2 Toyota Motor Europe (TME) - extractive body cue:** These diverse representations are then tightly interweaved with an object-centric action space.
- **p. 3 / IV. MOMA-LLM - extractive body cue:** To address the challenges of interactive open-vocabulary household tasks, we propose MoMa-LLM, which intertwines high-level reasoning with scalable dynamic scene representations.
- **p. 5 / IV. MOMA-LLM - extractive body cue:** If a subpolicy attempted execution but failed to complete its task, we re-encode the latest scene, update the action history, and let the LLM make ...
- **p. 4 / IV. MOMA-LLM - extractive body cue:** The subpolicies then generate actions in the low-level action space and return once they succeed or encounter a failure.
- **p. 5 / IV. MOMA-LLM - extractive body cue:** The realigned history will then correctly reflect this action as explore(kitchen).
- **p. 4 / IV. MOMA-LLM - extractive body cue:** Objects are then assigned to the room label R of the node no that minimizes Eq.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene ∗Equal contribution.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs.
- **p. 3 / IV. MOMA-LLM - extractive body cue:** To address the challenges of interactive open-vocabulary household tasks, we propose MoMa-LLM, which intertwines high-level reasoning with scalable dynamic scene representations.

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the ...
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the following high-level actions: navigate(room_name, object_name): Navigation to an object in a room via an A∗planner in the explored BEV-map Bt, inflated ...
- **p. 1 / 2 Toyota Motor Europe (TME) - extractive body cue:** These diverse representations are then tightly interweaved with an object-centric action space.
- **p. 3 / IV. MOMA-LLM - extractive body cue:** To address the challenges of interactive open-vocabulary household tasks, we propose MoMa-LLM, which intertwines high-level reasoning with scalable dynamic scene representations.
- **p. 5 / IV. MOMA-LLM - extractive body cue:** If a subpolicy attempted execution but failed to complete its task, we re-encode the latest scene, update the action history, and let the LLM make ...
- **p. 4 / IV. MOMA-LLM - extractive body cue:** The subpolicies then generate actions in the low-level action space and return once they succeed or encounter a failure.
- **p. 5 / IV. MOMA-LLM - extractive body cue:** The realigned history will then correctly reflect this action as explore(kitchen).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically ... | p. 1 (Abstract), p. 4 (IV. MOMA-LLM) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | It consists of the following high-level actions: navigate(room_name, object_name): Navigation to an object in a room via an A∗planner in the explored ... | p. 4 (IV. MOMA-LLM), p. 1 (2 Toyota Motor Europe (TME)) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | These diverse representations are then tightly interweaved with an object-centric action space. | p. 1 (2 Toyota Motor Europe (TME)), p. 3 (IV. MOMA-LLM) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. MOMA-LLM - extractive body cue:** Objects are then assigned to the room label R of the node no that minimizes Eq.
- **p. 4 / IV. MOMA-LLM - extractive body cue:** For each object o ∈GS, we identify the node that minimizes the distance dvo to the closest viewpoint vp from which the object was seen.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the ...
- **p. 3 / IV. MOMA-LLM - extractive body cue:** As we tackle an interactive problem, our map is dynamically updated based on novel explored areas or the occurrence of object dynamics in the scene.
- **p. 5 / IV. MOMA-LLM - extractive body cue:** As the scene representation is dynamically updated, this automatically encodes all newly acquired knowledge.
- **p. 5 / IV. MOMA-LLM - extractive body cue:** If a subpolicy attempted execution but failed to complete its task, we re-encode the latest scene, update the action history, and let the LLM make ...
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 3 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | rely, simple, success, state, action, history, stating, failure, invalid, argument, case, output, LLM, could | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | rely, simple, success, state, action, history, stating, failure, invalid, argument | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | incorporates, scene, understanding, module, given, object, detections, constructs, open-vocabulary, Equal | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | Objects, then, assigned, room, label, node, minimizes, object, identify, distance | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / IV. MOMA-LLM - extractive body cue:** We rely on a simple success state to the action history, stating "success", "failure", or "invalid argument" in case the output of the LLM could ...
- **p. 5 / IV. MOMA-LLM - extractive body cue:** If a subpolicy attempted execution but failed to complete its task, we re-encode the latest scene, update the action history, and let the LLM make ...
- **p. 3 / IV. MOMA-LLM - extractive body cue:** 3) 3D Scene Graph: The MoMa-LLM-policy operates on an attributed 3D scene graph GS that holds different abstraction levels, namely rooms and objects.
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the following high-level actions: navigate(room_name, object_name): Navigation to an object in a room via an A∗planner in the explored BEV-map Bt, inflated ...
- **p. 1 / Abstract - extractive body cue:** We tightly interleave these representations with an object-centric action space.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Furthermore, the presence of interactive scenes and articulated objects introduces a multitude of potential states and failure cases.
- **p. 2 / 2 Toyota Motor Europe (TME) - extractive body cue:** 2 exceptional results, outperforming state-of-the-art approaches across diverse fields.
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | For simplicity, we recompute the scene graph each time step. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | We terminate an episode if the agent reaches 50 high-level steps, indicating being stuck. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | Removing the history also leads to a, although smaller, drop in performance. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** MoMa-LLM, novel, grounds, language, models, within, structured, representations, derived, openvocabulary, scene, graphs, dynamically, updated, environment, explored, consists, following, high-level, actions.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | Simulation Experiments We instantiate the task in the iGibson simulator [32] with a Fetch robot. | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Base-arm task decision | Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure to the language model. | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Execution / correction | Similarly, while HIMOS achieves a high success rate, it is unable to explore efficiently. | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure to the language model.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We then perform a number of ablations of the language encodings.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Removing the history also leads to a, although smaller, drop in performance.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The two failures stemmed from irrecoverable failures of the subpolicies, in particular, collisions of the base during navigation or of the arm while opening the ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Object interactions, distance travelled and infeasible actions averaged over all episodes, including early terminated failures.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** This metric does not take into account the costs of object interactions.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 4 (IV. MOMA-LLM), p. 1 (2 Toyota Motor Europe (TME)), p. 3 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), objective p. 4 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 1 (Abstract), p. 3 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), temporal p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
