# Method - LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.11477; PDF retrieval source: https://arxiv.org/pdf/2304.11477. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD)): Large Language Model + Classical Planner (LLM+P) Having introduced the LLM's ability to encode problems in PDDL and in-context learning, we are ready to introduce the proposed LLM+P solution (the ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** Large Language Model + Classical Planner (LLM+P) Having introduced the LLM's ability to encode problems in PDDL and in-context learning, we are ready to introduce ...
- **p. 3 / III. METHOD - extractive body cue:** When the context is included with the prompt from the example above, the resulting PDDL problem file is directly solvable by the planner.
- **p. 4 / III. METHOD - extractive body cue:** 2) A domain PDDL is provided to define the actions that the robot is capable of.
- **p. 4 / III. METHOD - extractive body cue:** Once the problem PDDL file is generated, we feed it into any classical planner, together with the provided domain PDDL file, to generate a PDDL ...
- **p. 2 / II. BACKGROUND - extractive body cue:** S G are usually specified as a list of goal conditions, all of which must hold in a goal state. • A is a set ...
- **p. 2 / II. BACKGROUND - extractive body cue:** It includes a set of predicates that define the state space S and the actions (i.e., A ) with their preconditions and effects (i.e., the ...
- **p. 3 / III. METHOD - extractive body cue:** Large Language Model as a PDDL Writer LLMs are bad at planning (or long-horizon reasoning) [9] but they are good at describing and translating textual ...
- **p. 3 / III. METHOD - extractive body cue:** By in-context learning, we mean LLMs' ability to perform unseen downstream tasks by simply conditioning on a few input-label pairs (demonstrations) [10].

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Given how LLMs are designed and trained, this phenomenon should come as no surprise.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, they can be (relatively) easily fooled by, for example, asking for the result of a straightforward arithmetic problem that does not appear in their ...

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** Large Language Model + Classical Planner (LLM+P) Having introduced the LLM's ability to encode problems in PDDL and in-context learning, we are ready to introduce ...
- **p. 3 / III. METHOD - extractive body cue:** When the context is included with the prompt from the example above, the resulting PDDL problem file is directly solvable by the planner.
- **p. 4 / III. METHOD - extractive body cue:** 2) A domain PDDL is provided to define the actions that the robot is capable of.
- **p. 4 / III. METHOD - extractive body cue:** Once the problem PDDL file is generated, we feed it into any classical planner, together with the provided domain PDDL file, to generate a PDDL ...
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | Large Language Model + Classical Planner (LLM+P) Having introduced the LLM's ability to encode problems in PDDL and in-context learning, we are ... | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | When the context is included with the prompt from the example above, the resulting PDDL problem file is directly solvable by the ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | 2) A domain PDDL is provided to define the actions that the robot is capable of. | p. 4 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | usually, specified, list, goal, conditions, must, hold, state, symbolic, actions, underlying, transition, function, takes | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | usually, specified, list, goal, conditions, must, hold, state, symbolic, actions | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | Given, LLMs, designed, trained, phenomenon, should, come, surprise, Specifically, they | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | not recovered | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / II. BACKGROUND - extractive body cue:** S G are usually specified as a list of goal conditions, all of which must hold in a goal state. • A is a set ...
- **p. 2 / II. BACKGROUND - extractive body cue:** It includes a set of predicates that define the state space S and the actions (i.e., A ) with their preconditions and effects (i.e., the ...
- **p. 3 / III. METHOD - extractive body cue:** Large Language Model as a PDDL Writer LLMs are bad at planning (or long-horizon reasoning) [9] but they are good at describing and translating textual ...
- **p. 3 / III. METHOD - extractive body cue:** By in-context learning, we mean LLMs' ability to perform unseen downstream tasks by simply conditioning on a few input-label pairs (demonstrations) [10].
- **p. 4 / III. METHOD - extractive body cue:** 2) A domain PDDL is provided to define the actions that the robot is capable of.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Indeed the internet is now awash with examples of people reveling in getting ChatGPT to generate output that even a 5-year-old human child would know ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While even relatively simple models, such as Eliza from 1966 [1], can generate responses to some prompts that seem reasonable, it has always been relatively ...
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | Large Language Model as a PDDL Writer LLMs are bad at planning (or long-horizon reasoning) [9] but they are good at describing ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | However, so far, LLMs cannot reliably solve long-horizon robot planning problems. | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not recovered | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Large, Language, Model, Classical, Planner, LLM, Having, introduced, ability, encode, problems, PDDL, in-context, learning, ready, introduce, solution, bottom, Fig, When.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | Benchmark Problems We present seven robot planning domains borrowed from past International Planning Competitions and 20 automatically generated tasks for each domain ... | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent) |
| Search / trajectory decision | can state-of-the-art LLMs and LLM-based reasoning methods be directly used for planning? | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent) |
| Execution interface | We report the success rate of the optimal alias, and for the domains that time out, we show the success rate of ... | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent) |

## Failure and Ablation Link

- **p. 3 / III. METHOD - extractive body cue:** Here we provide an example of a PDDL problem file written by GPT-4 without any promptengineering.
- **p. 3 / III. METHOD - extractive body cue:** In-Context Learning LLMs are known to be capable of in-context learning without finetuning their parameters.
- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive body cue:** Domain Success Rate % LLMLLM LLMToT LLM+PLLM+P BARMAN 0 0 0 0 20 (100) BLOCKSWORLD 20 15 (30) 0 (5) 0 90 FLOORTILE 0 0 ...
- **p. 6 / 1) We observe that though LLM-AS-P provides a plan - extractive body cue:** The LLM-AS-P methods (with or without context) completely fail at this type of problems.
- **p. 6 / 1) We observe that though LLM-AS-P provides a plan - extractive body cue:** 2) In most cases, LLM-AS-P fails in the same way with or without the example plan as context.
- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive body cue:** 7) TYREWORLD: The robot is given a task to replace flat tires by, for example, inflating tires, tightening nuts, and moving tools back to the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), objective 본문 anchor 없음, temporal p. 3 (III. METHOD), p. 1 (Abstract), p. 1 (Abstract), p. 4 (IV. RELATED WORK), p. 4 (IV. RELATED WORK), p. 5 (1) How well does LLM-AS-P work? To what extent).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
