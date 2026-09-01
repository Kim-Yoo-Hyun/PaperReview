# Method - Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33610; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33610. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (Problem Formulation), p. 4 (Problem Formulation), p. 4 (Problem Formulation), p. 6 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation)): Given the PDDL problem P of a specific task, domain D, and user instruction i, we first query the LLM planner to generate K candidates actions {a1 t, · · ...

## Method Body Digest

- **p. 5 / Problem Formulation - extractive body cue:** Given the PDDL problem P of a specific task, domain D, and user instruction i, we first query the LLM planner to generate K candidates ...
- **p. 4 / Problem Formulation - extractive body cue:** Then, the robot executes the actions generated and selected by the LLM planner based on the constructed PDDL problem.
- **p. 4 / Problem Formulation - extractive body cue:** First, the feasibility of executing the action at at state st, such as whether the object to be manipulated can be grasped.
- **p. 6 / Problem Formulation - extractive body cue:** For instance, when the robot is at the paper box (as determined by the visiting records) and the paper box is detected (as determined by ...
- **p. 7 / Problem Formulation - extractive body cue:** We then Figure 7: All failure cases of predicate checking in the realworld experiments across five long-horizon tasks. recorded the success cases of the LLM ...
- **p. 3 / Problem Formulation - extractive body cue:** We use an interactive planning method that considers action feedback and proposes several candidates at each time step.
- **p. 3 / Problem Formulation - extractive body cue:** This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding ...
- **p. 3 / Problem Formulation - extractive body cue:** The later term of Equation 1 represents the probability that the action sequence at:H achieve rewards rt:H when executed from the state st, which is ...

## Design Rationale

- **p. 3 / Problem Formulation - extractive body cue:** This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding ...
- **p. 3 / Problem Formulation - extractive body cue:** 2, we propose the InstructionAugmented Long-Horizon Planning (IALP) system to inPromptable on, in, holding, opened Grounding Mechanism at, find, graspable, placeable, detected, reachable Table 1: ...
- **p. 5 / Problem Formulation - extractive body cue:** We introduce six feasibility predicates, comprising two navigation predicates and four manipulation predicates, to maximize the feasibility score Sfb thereby increasing the likelihood that the ...

## Source Evidence Cues

- **p. 5 / Problem Formulation - extractive body cue:** Given the PDDL problem P of a specific task, domain D, and user instruction i, we first query the LLM planner to generate K candidates ...
- **p. 4 / Problem Formulation - extractive body cue:** Then, the robot executes the actions generated and selected by the LLM planner based on the constructed PDDL problem.
- **p. 4 / Problem Formulation - extractive body cue:** First, the feasibility of executing the action at at state st, such as whether the object to be manipulated can be grasped.
- **p. 6 / Problem Formulation - extractive body cue:** For instance, when the robot is at the paper box (as determined by the visiting records) and the paper box is detected (as determined by ...
- **p. 7 / Problem Formulation - extractive body cue:** We then Figure 7: All failure cases of predicate checking in the realworld experiments across five long-horizon tasks. recorded the success cases of the LLM ...
- **p. 3 / Problem Formulation - extractive body cue:** We use an interactive planning method that considers action feedback and proposes several candidates at each time step.
- **p. 3 / Problem Formulation - extractive body cue:** This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | Given the PDDL problem P of a specific task, domain D, and user instruction i, we first query the LLM planner to ... | p. 5 (Problem Formulation), p. 4 (Problem Formulation) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | Then, the robot executes the actions generated and selected by the LLM planner based on the constructed PDDL problem. | p. 4 (Problem Formulation), p. 4 (Problem Formulation) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | First, the feasibility of executing the action at at state st, such as whether the object to be manipulated can be grasped. | p. 4 (Problem Formulation), p. 6 (Problem Formulation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / Problem Formulation - extractive body cue:** The later term of Equation 1 represents the probability that the action sequence at:H achieve rewards rt:H when executed from the state st, which is ...
- **p. 3 / Problem Formulation - extractive body cue:** Thus, the objective at time step t ∈{1 : H} can be expressed as the joint probability of skill sequence at:H and binary rewards rt:H ...
- **p. 4 / Problem Formulation - extractive body cue:** We aim to maximize the probability p(1/st, at) of achieving a reward of 1 at state st by performing action at, as determined by the ...
- **p. 5 / Problem Formulation - extractive body cue:** Given our interactive planning method, which involves planning actions at every time step, the objective of the optimality score for planning at a single time ...
- **p. 5 / Problem Formulation - extractive body cue:** We introduce six feasibility predicates, comprising two navigation predicates and four manipulation predicates, to maximize the feasibility score Sfb thereby increasing the likelihood that the ...
- **p. 4 / Problem Formulation - extractive body cue:** A reward of 1 is received if the robot successfully executes with the effects representing the expected state changes.
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 5 (Problem Formulation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | captures, utility, action, sequence, respect, satisfying, instruction, current, state, later, term, Equation, represents, probability | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | captures, utility, action, sequence, respect, satisfying, instruction, current, state, later | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | library, consists, four, promptable, predicates, addressed, through, prompt, engineering, reasoning | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | later, term, Equation, represents, probability, action, sequence, achieve, rewards, when | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / Problem Formulation - extractive body cue:** It captures the utility of the action sequence at:H with respect to satisfying the instruction i on current state st.
- **p. 3 / Problem Formulation - extractive body cue:** The later term of Equation 1 represents the probability that the action sequence at:H achieve rewards rt:H when executed from the state st, which is ...
- **p. 5 / Problem Formulation - extractive body cue:** Given the PDDL problem P of a specific task, domain D, and user instruction i, we first query the LLM planner to generate K candidates ...
- **p. 6 / Problem Formulation - extractive body cue:** Given the instruction, "Pick the paper box on the wooden table and place it on the black table," and with the 2D and 3D images ...
- **p. 5 / Problem Formulation - extractive body cue:** Each task was accompanied by a natural language instruction i, and the robot initiated from the initial state at the beginning of each task.
- **p. 4 / Problem Formulation - extractive body cue:** First, the feasibility of executing the action at at state st, such as whether the object to be manipulated can be grasped.
- **p. 4 / Problem Formulation - extractive body cue:** We aim to maximize the probability p(1/st, at) of achieving a reward of 1 at state st by performing action at, as determined by the ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | Thus, the objective at time step t ∈{1 : H} can be expressed as the joint probability of skill sequence at:H and ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | Optimality We aim to maximize the optimality score Sop of the action sequence at:H at time step t. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | Discussion To investigate the types of failure cases in real-world experiments, we conducted 20 trials for each task within a realworld environment ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Given, PDDL, problem, specific, task, domain, user, instruction, first, query, LLM, planner, generate, candidates, actions, state, Then, robot, executes, generated.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | While 15 errors out of 100 may appear insignificant, they represent a considerable workload in real-world hardware experiments compared with numerical simulations ... | p. 7 (Problem Formulation), p. 3 (Problem Formulation) |
| Base-arm task decision | Figure 6: The success rate of IALP compared with that of IALP without feasibility feedback and without optimal se- lection, respectively. list ... | p. 7 (Figure/Table caption), p. 3 (Problem Formulation) |
| Execution / correction | The results indicate that IALP achieves a success rate of over 80% in all long-term tasks. | p. 7 (Problem Formulation), p. 7 (Problem Formulation) |

## Failure and Ablation Link

- **p. 7 / Problem Formulation - extractive body cue:** For the system without optimal selection, denoted as IALP w/o Optimal Selection, a relatively high success rate is still maintained because feasibility checks are applied ...
- **p. 7 / Problem Formulation - extractive body cue:** Ablation Study on Feasibility and Optimality To evaluate the impact of feasibility feedback and optimal selection on system performance, we conducted two ablation experiments, excluding ...
- **p. 3 / Problem Formulation - extractive body cue:** We assume an open-world setting, wherein the robot operates without prior knowledge of task-relevant objects or other ground truth information.
- **p. 7 / Problem Formulation - extractive body cue:** Planning failures occur when the planner fails to generate the correct action sequence.
- **p. 7 / Problem Formulation - extractive body cue:** All instances of predicate-checking failures were systematically aggregated and classified into three categories: planning, promptable, and grounding mechanisms failures.
- **p. 3 / Problem Formulation - extractive body cue:** If even one skill fails, then the entire action sequence fails.
- **p. 4 / Problem Formulation - extractive body cue:** For instance, a robot cannot move toward a blue jacket if it cannot identify a 14693

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (Problem Formulation), p. 4 (Problem Formulation), p. 4 (Problem Formulation), p. 6 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation), objective p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 4 (Problem Formulation), p. 5 (Problem Formulation), p. 5 (Problem Formulation), p. 4 (Problem Formulation), temporal p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Problem Formulation), p. 4 (Problem Formulation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
