# Evaluation - LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.11477; PDF retrieval source: https://arxiv.org/pdf/2304.11477. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 2 (II. BACKGROUND)): We report the success rate of the optimal alias, and for the domains that time out, we show the success rate of the sub-optimal alias in parentheses.

## Evaluation Body Digest

- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive PDF cue:** Benchmark Problems We present seven robot planning domains borrowed from past International Planning Competitions and 20 automatically generated tasks for each domain [67].
- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive PDF cue:** 4) GRIPPERS: A set of robots with two grippers is given a task to move objects among different rooms.
- **p. 6 / 1) We observe that though LLM-AS-P provides a plan - extractive PDF cue:** Robot Demonstration We verify that LLM+P can efficiently solve realistic service robot problems by deploying it on a real robot tasked with tidying up a ...
- **p. 3 / III. METHOD - extractive PDF cue:** The LLM+P method is directly applicable as a natural language interface for giving tasks to robot systems.
- **p. 3 / III. METHOD - extractive PDF cue:** By in-context learning, we mean LLMs' ability to perform unseen downstream tasks by simply conditioning on a few input-label pairs (demonstrations) [10].
- **p. 2 / 3. Move b4 from b2 to the table - extractive PDF cue:** 1: LLM+P makes use of a large language model (LLM) to produce the PDDL description of the given problem, then leverages a classical planner for ...
- **p. 4 / III. METHOD - extractive PDF cue:** 2) A domain PDDL is provided to define the actions that the robot is capable of.
- **p. 4 / III. METHOD - extractive PDF cue:** To summarize, the assumptions we need for LLM+P are: 1) A robot knows when to trigger LLM+P based on its conversation with a human user.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 1) How well does LLM-AS-P work? To what extent | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the success rate of the optimal alias, and for the domains that time out, we show the success rate of the sub-optimal ... | p. 5 (1) How well does LLM-AS-P work? To what extent) |
| 1) How well does LLM-AS-P work? To what extent | EMPIRICAL / REAL-ROBOT OR HARDWARE | Domain Success Rate % LLMLLM LLMToT LLM+PLLM+P BARMAN 0 0 0 0 20 (100) BLOCKSWORLD 20 15 (30) 0 (5) 0 90 FLOORTILE 0 ... | p. 5 (1) How well does LLM-AS-P work? To what extent) |
| II. BACKGROUND | EMPIRICAL / REAL-ROBOT OR HARDWARE | A solution to a planning problem P is a symbolic plan π in the form of ⟨a1,a2,...,aN⟩, such that the preconditions of a1 hold ... | p. 2 (II. BACKGROUND) |

## Dataset / Benchmark Role

- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive PDF cue:** Benchmark Problems We present seven robot planning domains borrowed from past International Planning Competitions and 20 automatically generated tasks for each domain [67].
- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive PDF cue:** 4) GRIPPERS: A set of robots with two grippers is given a task to move objects among different rooms.
- **p. 6 / 1) We observe that though LLM-AS-P provides a plan - extractive PDF cue:** Robot Demonstration We verify that LLM+P can efficiently solve realistic service robot problems by deploying it on a real robot tasked with tidying up a ...
- **p. 3 / III. METHOD - extractive PDF cue:** The LLM+P method is directly applicable as a natural language interface for giving tasks to robot systems.
- **p. 3 / III. METHOD - extractive PDF cue:** By in-context learning, we mean LLMs' ability to perform unseen downstream tasks by simply conditioning on a few input-label pairs (demonstrations) [10].
- **p. 2 / 3. Move b4 from b2 to the table - extractive PDF cue:** 1: LLM+P makes use of a large language model (LLM) to produce the PDDL description of the given problem, then leverages a classical planner for ...
- **p. 4 / III. METHOD - extractive PDF cue:** 2) A domain PDDL is provided to define the actions that the robot is capable of.
- **p. 4 / III. METHOD - extractive PDF cue:** To summarize, the assumptions we need for LLM+P are: 1) A robot knows when to trigger LLM+P based on its conversation with a human user.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: LLM+P makes use of a large language model (LLM) to produce the PDDL description of the given problem, then leverages a classical planner ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to a ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Benchmark Problems We present seven robot planning domains borrowed from past International Planning Competitions and 20 automatically generated tasks for each domain [67]. | embodiment, simulator version and control stack | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent) |
| Task/environment | 4) GRIPPERS: A set of robots with two grippers is given a task to move objects among different rooms. | reset, timeout, object/scene variation | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 6 (1) We observe that though LLM-AS-P provides a plan) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 3 (III. METHOD), p. 3 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the success rate of the optimal alias, and for the domains that time out, we show the success rate of the sub-optimal ... | definition/direction/unit from same section | p. 5 (1) How well does LLM-AS-P work? To what extent) |
| Domain Success Rate % LLMLLM LLMToT LLM+PLLM+P BARMAN 0 0 0 0 20 (100) BLOCKSWORLD 20 15 (30) 0 (5) 0 90 FLOORTILE 0 ... | definition/direction/unit from same section | p. 5 (1) How well does LLM-AS-P work? To what extent) |
| Problem PDDL generated by LLM+P: (:objects coffee-table side-table recycle-bin pantry - location mustard-bottle soup-can - object) (:init (= (total-cost) 0) (= (distance coffee-table side-table) ... | definition/direction/unit from same section | p. 6 (1) We observe that though LLM-AS-P provides a plan) |
| The PDDL representation of a planning problem P is separated into two files: a domain file and a problem file. | definition/direction/unit from same section | p. 2 (II. BACKGROUND) |
| Our extensive empirical evaluations indicate that LLM+P is able to generate correct solutions to many more planning problems than are LLMs on their own. | definition/direction/unit from same section | p. 2 (3. Move b4 from b2 to the table) |
| Moreover, we assume the agent is provided with a minimal example that demonstrates what an example problem PDDL looks like for a simple | definition/direction/unit from same section | p. 3 (III. METHOD) |
| As we see, the generated file appears to have the correct PDDL syntax but uses a made-up predicate (empty) and misses the initial condition ... | definition/direction/unit from same section | p. 3 (III. METHOD) |
| This specification is taskagnostic - the entities relevant to the task are specified in the LLM-generated problem PDDL. | definition/direction/unit from same section | p. 4 (III. METHOD) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| can state-of-the-art LLMs and LLM-based reasoning methods be directly used for planning? | comparison identity and matched condition | p. 5 (1) How well does LLM-AS-P work? To what extent) |
| For the baseline methods, we manually count the number of optimal plans, and report the number of correct plans in parentheses (if there are ... | comparison identity and matched condition | p. 5 (1) How well does LLM-AS-P work? To what extent) |
| Here we provide an example of a PDDL problem file written by GPT-4 without any promptengineering. | comparison identity and matched condition | p. 3 (III. METHOD) |
| In-Context Learning LLMs are known to be capable of in-context learning without finetuning their parameters. | comparison identity and matched condition | p. 3 (III. METHOD) |
| The LLM-AS-P methods (with or without context) completely fail at this type of problems. | comparison identity and matched condition | p. 6 (1) We observe that though LLM-AS-P provides a plan) |
| 2) In most cases, LLM-AS-P fails in the same way with or without the example plan as context. | comparison identity and matched condition | p. 6 (1) We observe that though LLM-AS-P provides a plan) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Here we provide an example of a PDDL problem file written by GPT-4 without any promptengineering. | component/input/data sensitivity | p. 3 (III. METHOD) |
| In-Context Learning LLMs are known to be capable of in-context learning without finetuning their parameters. | component/input/data sensitivity | p. 3 (III. METHOD) |
| Domain Success Rate % LLMLLM LLMToT LLM+PLLM+P BARMAN 0 0 0 0 20 (100) BLOCKSWORLD 20 15 (30) 0 (5) 0 90 FLOORTILE 0 ... | component/input/data sensitivity | p. 5 (1) How well does LLM-AS-P work? To what extent) |
| The LLM-AS-P methods (with or without context) completely fail at this type of problems. | component/input/data sensitivity | p. 6 (1) We observe that though LLM-AS-P provides a plan) |
| 2) In most cases, LLM-AS-P fails in the same way with or without the example plan as context. | component/input/data sensitivity | p. 6 (1) We observe that though LLM-AS-P provides a plan) |
| 7) TYREWORLD: The robot is given a task to replace flat tires by, for example, inflating tires, tightening nuts, and moving tools back to ... | component/input/data sensitivity | p. 5 (1) How well does LLM-AS-P work? To what extent) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Given how LLMs are designed and trained, this phenomenon should come as no surprise. | We report the success rate of the optimal alias, and for the domains that time out, we show the success rate of the sub-optimal ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 2 (II. BACKGROUND) |
| Primary metric/result | Domain Success Rate % LLMLLM LLMToT LLM+PLLM+P BARMAN 0 0 0 0 20 (100) BLOCKSWORLD 20 15 (30) 0 (5) 0 90 FLOORTILE 0 ... | numeric claim only at cited anchor | p. 5 (1) How well does LLM-AS-P work? To what extent) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Limitation: In this paper, we do not ask the LLM to recognize that it has been posed a prompt that is suitable for processing ... | p. 2 (3. Move b4 from b2 to the table) |
| body limitation/failure cue | Robots can move around and change colors but cannot step on painted tiles. | p. 5 (1) How well does LLM-AS-P work? To what extent) |
| body limitation/failure cue | In particular, in the BLOCKSWORLD domain, LLM-AS-P cannot keep track of properties like ON and CLEAR. | p. 6 (1) We observe that though LLM-AS-P provides a plan) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Large Language Model + Classical Planner (LLM+P) Having introduced the LLM's ability to encode problems in PDDL and in-context learning, we are ready to ... | p. 3 (III. METHOD) |
| This dataset is made publicly available in our codebase for reproducibility. | p. 5 (1) How well does LLM-AS-P work? To what extent) |
| We adapt the breadth-first-search algorithm from the original ToT implementation4 for planning. | p. 5 (1) How well does LLM-AS-P work? To what extent) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to a ...
- **p. 2 / 3. Move b4 from b2 to the table - extractive PDF cue:** Limitation: In this paper, we do not ask the LLM to recognize that it has been posed a prompt that is suitable for processing using ...
- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive PDF cue:** Robots can move around and change colors but cannot step on painted tiles.
- **p. 6 / 1) We observe that though LLM-AS-P provides a plan - extractive PDF cue:** In particular, in the BLOCKSWORLD domain, LLM-AS-P cannot keep track of properties like ON and CLEAR.

- **PDF anchors reviewed:** datasets p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 6 (1) We observe that though LLM-AS-P provides a plan), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (3. Move b4 from b2 to the table), metrics p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 6 (1) We observe that though LLM-AS-P provides a plan), p. 2 (II. BACKGROUND), p. 2 (3. Move b4 from b2 to the table), p. 3 (III. METHOD), baselines p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 6 (1) We observe that though LLM-AS-P provides a plan), p. 6 (1) We observe that though LLM-AS-P provides a plan), results p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 2 (II. BACKGROUND).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
