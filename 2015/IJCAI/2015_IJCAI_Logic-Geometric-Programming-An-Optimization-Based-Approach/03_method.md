# Method - Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf; PDF retrieval source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory where the symbolic state-action sequence ...

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...
- **p. 1 / 1 Introduction - extractive body cue:** First, we aim for planners that can deal with arbitrary objective functions ψ(x(T)) on the final geometric configuration x(T) and overall control costs.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper we propose three levels on which geometric reasoning (that is, optimization over geometric configurations and paths) may inform symbolic search towards a ...
- **p. 2 / 1 Introduction - extractive body cue:** This implies the challenge of motion optimization across kinematic switches of the world configuration (across action boundaries) to allow for the optimization over the full ...
- **p. 1 / Abstract - extractive body cue:** We consider problems of sequential robot manipulation (aka. combined task and motion planning) where the objective is primarily given in terms of a cost function ...
- **p. 1 / 1 Introduction - extractive body cue:** But crucially, the objective is given only in terms of an evaluation function of the final configuration and potential control costs.
- **p. 2 / 1 Introduction - extractive body cue:** Roughly, it "moves" the objects in the final construction into place to maximize (e.g.) stability-and thereby informs also the early actions in the action sequence ...
- **p. 2 / 1 Introduction - extractive body cue:** All three levels raise novel interesting challenges for motion (or configuration) optimizers.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a ...
- **p. 1 / 1 Introduction - extractive body cue:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper we propose three levels on which geometric reasoning (that is, optimization over geometric configurations and paths) may inform symbolic search towards a ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...
- **p. 1 / 1 Introduction - extractive body cue:** First, we aim for planners that can deal with arbitrary objective functions ψ(x(T)) on the final geometric configuration x(T) and overall control costs.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper we propose three levels on which geometric reasoning (that is, optimization over geometric configurations and paths) may inform symbolic search towards a ...
- **p. 2 / 1 Introduction - extractive body cue:** This implies the challenge of motion optimization across kinematic switches of the world configuration (across action boundaries) to allow for the optimization over the full ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the ... | p. 1 (Abstract), p. 1 (1 Introduction) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | First, we aim for planners that can deal with arbitrary objective functions ψ(x(T)) on the final geometric configuration x(T) and overall control ... | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | In this paper we propose three levels on which geometric reasoning (that is, optimization over geometric configurations and paths) may inform symbolic ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** We consider problems of sequential robot manipulation (aka. combined task and motion planning) where the objective is primarily given in terms of a cost function ...
- **p. 1 / 1 Introduction - extractive body cue:** But crucially, the objective is given only in terms of an evaluation function of the final configuration and potential control costs.
- **p. 2 / 1 Introduction - extractive body cue:** Roughly, it "moves" the objects in the final construction into place to maximize (e.g.) stability-and thereby informs also the early actions in the action sequence ...
- **p. 2 / 1 Introduction - extractive body cue:** All three levels raise novel interesting challenges for motion (or configuration) optimizers.
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 1 (1 Introduction), p. 1 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | formulate, problem, holistically, storder, logic, extension, mathematical, program, non-linear, constrained, over, full, world, trajectory | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | formulate, problem, holistically, storder, logic, extension, mathematical, program, non-linear, constrained | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | Besides, novel, formulation, manipulation, planning, LGP, think, concept, effective, space | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | consider, problems, sequential, robot, manipulation, combined, task, motion, planning, where | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...
- **p. 1 / Abstract - extractive body cue:** We tackle the challenge of solving such programs by proposing three levels of approximation: The coarsest level introduces the concept of the effective end state ...
- **p. 2 / 1 Introduction - extractive body cue:** This implies the challenge of motion optimization across kinematic switches of the world configuration (across action boundaries) to allow for the optimization over the full ...
- **p. 2 / 1 Introduction - extractive body cue:** The highest level, which plays the crucial role of the heuristic for informed search, is perhaps most interesting and will optimize over the end configuration ...
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | Further, the paths have 20 time steps per manipulation; for 25 objects this is a (15dimensional) trajectory with 1000 time steps across ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | This computes explicit geometric instantiations of the action operators and optimizes the respective configurations to account also for long-term effects, e.g., optimizes ... | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not recovered | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | Further, the paths have 20 time steps per manipulation; for 25 objects this is a (15dimensional) trajectory with 1000 time steps across ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** formulate, problem, holistically, storder, logic, extension, mathematical, program, non-linear, constrained, over, full, world, trajectory, where, symbolic, state-action, sequence, defines, equality.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | Instead we optimize the grasp pose (the relative object-hand pose), assuming that a compliant real-world gripper could perform the actual grasp. | p. 5 (5 Experiments), p. 5 (5 Experiments) |
| Search / trajectory decision | no linked comparison cue | 본문 anchor 없음 |
| Execution interface | For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. | p. 5 (5 Experiments), p. 6 (5 Experiments) |

## Failure and Ablation Link

- **p. 5 / 2 Related Work - extractive body cue:** Further constraints concern standard motion optimization aspects such as collision avoidance.
- **p. 5 / 5 Experiments - extractive body cue:** The geometric and differential constraints hpath, gpath implement zero velocity of the object-hand pose while inhand, zero velocities and accelerations during pick and place, and ...
- **p. 6 / 5 Experiments - extractive body cue:** The resulting trajectories are smooth and collision free (if keyframe optimization indicated feasibility) and generate the optimized end state.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), objective p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), temporal p. 6 (5 Experiments), p. 4 (2 Related Work), p. 5 (2 Related Work), p. 2 (1 Introduction), p. 6 (5 Experiments), p. 1 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
