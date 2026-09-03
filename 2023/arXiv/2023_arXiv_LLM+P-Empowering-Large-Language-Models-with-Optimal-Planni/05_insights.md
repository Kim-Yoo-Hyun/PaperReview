# Insights — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.11477; PDF retrieval source: https://arxiv.org/pdf/2304.11477. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Given how LLMs are designed and trained, this phenomenon should come as no surprise.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, they can be (relatively) easily fooled by, for example, asking for the result of a straightforward arithmetic problem that does not appear in their ...
- **p. 3 / III. METHOD - extractive body cue:** Large Language Model + Classical Planner (LLM+P) Having introduced the LLM's ability to encode problems in PDDL and in-context learning, we are ready to introduce ...
- **p. 3 / III. METHOD - extractive body cue:** When the context is included with the prompt from the example above, the resulting PDDL problem file is directly solvable by the planner.
- **p. 4 / III. METHOD - extractive body cue:** 2) A domain PDDL is provided to define the actions that the robot is capable of.
- **p. 4 / III. METHOD - extractive body cue:** Once the problem PDDL file is generated, we feed it into any classical planner, together with the provided domain PDDL file, to generate a PDDL ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** A Failure Example of GPT-4 in Planning Problem (P1): You have 5 blocks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** One cannot place more than one block on another block. b5 is on top of b3. b4 is on top of b2. b2 is on ...
- **p. 2 / II. BACKGROUND - extractive body cue:** The PDDL representation of a planning problem P is separated into two files: a domain file and a problem file.
- **p. 2 / II. BACKGROUND - extractive body cue:** The problem PDDL file provides a list of objects to ground the domain, the problem's initial state sinit and goal conditions S G.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to a ...
- **p. 2 / 3. Move b4 from b2 to the table - extractive body cue:** Limitation: In this paper, we do not ask the LLM to recognize that it has been posed a prompt that is suitable for processing using ...
- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive body cue:** Robots can move around and change colors but cannot step on painted tiles.
- **Boundary to test:** Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to a room with the side table and the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Given how LLMs are designed and trained, this phenomenon should come as no surprise. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | We report the success rate of the optimal alias, and for the domains that time out, we show the success rate of the sub-optimal alias in parentheses. | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent) |
| Failure/limitation | Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to a room with the side table and the ... | p. 6 (Figure/Table caption), p. 2 (3. Move b4 from b2 to the table) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 S G are usually specified as a list of goal conditions, all of which must hold in a goal state. • A is a set of symbolic actions. • f is the ...를 It includes a set of predicates that define the state space S and the actions (i.e., A ) with their preconditions and effects (i.e., the transition function f).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to a room with the side table and the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Given how LLMs are designed and trained, this phenomenon should come as no surprise.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Planning and control`; tags: `Robotics, LLM planning, classical planning, PDDL, plan verification`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to a room with the side table and the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Benchmark Problems We present seven robot planning domains borrowed from past International Planning Competitions and 20 automatically generated tasks for each domain [67]..
3. Compare against the body-reported baseline or a matched simpler baseline: can state-of-the-art LLMs and LLM-based reasoning methods be directly used for planning?.
4. Report the body metric and its denominator/aggregation: We report the success rate of the optimal alias, and for the domains that time out, we show the success rate of the sub-optimal alias in parentheses..
5. Re-run the body-reported ablation/failure condition: Here we provide an example of a PDDL problem file written by GPT-4 without any promptengineering..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 2 (II. BACKGROUND); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Given, LLMs, designed mechanism이 can state-of-the-art LLMs and LLM-based reasoning methods be directly used for planning? 대비 We report the success rate of the optimal alias, and for the domains that time out, we show ...을 개선하고, Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
