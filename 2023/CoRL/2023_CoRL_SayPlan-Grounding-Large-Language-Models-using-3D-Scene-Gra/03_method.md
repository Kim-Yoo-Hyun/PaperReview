# Method - SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (50 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/rana23a.html; PDF retrieval source: https://arxiv.org/pdf/2307.06135. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 13 (A Implementation Details), p. 13 (A Implementation Details)): We utilise GPT-4 [3] as the underlying LLM agent unless otherwise stated.

## Method Body Digest

- **p. 13 / A Implementation Details - extractive body cue:** We utilise GPT-4 [3] as the underlying LLM agent unless otherwise stated.
- **p. 13 / A Implementation Details - extractive body cue:** During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning only ...
- **p. 2 / 1 Introduction - extractive body cue:** Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan using feedback from ...
- **p. 1 / 1 Introduction - extractive body cue:** For LLMs to be effective planners in robotics, they must be grounded in reality, that is, they must adhere to the constraints presented by the ...
- **p. 2 / 1 Introduction - extractive body cue:** Secondly, as the horizon of the task plans across such environments tends to grow with the complexity and range of the given task instructions, there ...
- **p. 13 / A Implementation Details - extractive body cue:** We define the agent's role, details pertaining to the scene graph environment, the desired output structure and a set of input-output examples which together form ...
- **p. 1 / 1 Introduction - extractive body cue:** To address this, recent works have explored the utilization of vision-based value functions [4], object detectors [7, 8], or Planning Domain Definition Language (PDDL) descriptions ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a scalable approach to ground LLM-based task planners across environments spanning multiple rooms and floors.
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.

## Source Evidence Cues

- **p. 13 / A Implementation Details - extractive body cue:** We utilise GPT-4 [3] as the underlying LLM agent unless otherwise stated.
- **p. 13 / A Implementation Details - extractive body cue:** During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning only ...
- **Detected method headings:** 3.3 Approach (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | We utilise GPT-4 [3] as the underlying LLM agent unless otherwise stated. | p. 13 (A Implementation Details), p. 13 (A Implementation Details) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during ... | p. 13 (A Implementation Details) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | We utilise GPT-4 [3] as the underlying LLM agent unless otherwise stated. | p. 13 (A Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 13 / A Implementation Details - extractive body cue:** During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning only ...
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 13 (A Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Finally, ensure, feasibility, plan, introduce, iterative, replanning, pipeline, verifies, refines, initial, feedback, scene, graph | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | Finally, ensure, feasibility, plan, introduce, iterative, replanning, pipeline, verifies, refines | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | Firstly, present, mechanism, enables, LLM, conduct, semantic, search, taskrelevant, subgraph | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | During, semantic, search, Scene, Graph, Memory, components, input, prompt, updated | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan using feedback from ...
- **p. 1 / 1 Introduction - extractive body cue:** For LLMs to be effective planners in robotics, they must be grounded in reality, that is, they must adhere to the constraints presented by the ...
- **p. 2 / 1 Introduction - extractive body cue:** Secondly, as the horizon of the task plans across such environments tends to grow with the complexity and range of the given task instructions, there ...
- **p. 13 / A Implementation Details - extractive body cue:** We define the agent's role, details pertaining to the scene graph environment, the desired output structure and a set of input-output examples which together form ...
- **p. 13 / A Implementation Details - extractive body cue:** During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning only ...
- **p. 1 / 1 Introduction - extractive body cue:** To address this, recent works have explored the utilization of vision-based value functions [4], object detectors [7, 8], or Planning Domain Definition Language (PDDL) descriptions ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | To avoid expanding already-contracted nodes, we maintain a list of previously expanded nodes, passed as an additional Memory input to the LLM, ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during ... | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** utilise, GPT-4, underlying, LLM, agent, unless, otherwise, stated, During, semantic, search, Scene, Graph, Memory, components, input, prompt, updated, step, while.
- **Relevant PDF headings:** 3.3 Approach (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | This static prompt is both task- and environment-agnostic and takes up ≈3900 tokens of the LLM's input. | p. 13 (A Implementation Details), p. 13 (A Implementation Details) |
| Base-arm task decision | Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene ... | p. 7 (Figure/Table caption), p. 32 (Figure/Table caption) |
| Execution / correction | The table shows the semantic search success rate in finding a suitable subgraph for planning. | p. 6 (5 Results), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 20 / Figure/Table caption - extractive body cue:** Figure 5: 3D Scene Graph - Fully Expanded Office Environment. Full 3D scene graph exposing all the rooms, assets and objects available in the scene. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: SayPlan Overview (top). SayPlan operates across two stages to ensure scalability: (left) Given a collapsed 3D scene graph and a task instruction, semantic ...
- **p. 13 / A Implementation Details - extractive body cue:** During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning only ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple ...
- **p. 46 / Figure/Table caption - extractive body cue:** Figure 8: Evaluating the performance of SayPlan's causal planning capabilities as the scale of the environment increases. For the office environment used in this study, ...
- **p. 32 / Figure/Table caption - extractive body cue:** Table 18: Correctness, Executability and Number of Replanning Iterations for Long-Horizon Planning Instructions. Evaluating the performance of SayPlan on each long-horizon planning instruction. Values indicated ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 13 (A Implementation Details), p. 13 (A Implementation Details), objective p. 13 (A Implementation Details), temporal p. 13 (A Implementation Details), p. 5 (3.3 Approach), p. 2 (1 Introduction), p. 5 (3.3 Approach), p. 6 (3.3 Approach), p. 8 (1. SayPlan (GPT-3.5) consistently).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
