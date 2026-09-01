# Method - Text2Motion: From Natural Language Instructions to Feasible Plans

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.12153; PDF retrieval source: https://arxiv.org/pdf/2303.12153. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (4.2 Shooting-based planning), p. 5 (4.1 Goal prediction), p. 6 (4.3 Search-based planning), p. 7 (4.4 Text2Motion), p. 6 (4.3 Search-based planning), p. 4 (4 Methods)): To this end, the first strategy we propose is a shooting-based Algorithm 1 Shooting-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP 2: function Shooting(i, s1, G; K) 3: ...

## Method Body Digest

- **p. 5 / 4.2 Shooting-based planning - extractive PDF cue:** To this end, the first strategy we propose is a shooting-based Algorithm 1 Shooting-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP 2: function ...
- **p. 5 / 4.1 Goal prediction - extractive PDF cue:** We define a satisfaction function F G sat (s) : S →{0, 1} which takes as input a geometric state s and evaluates to 1 ...
- **p. 6 / 4.3 Search-based planning - extractive PDF cue:** We then compute the usefulness scores Sllm(ψk t ) by summing the token Algorithm 2 Search-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP ...
- **p. 7 / 4.4 Text2Motion - extractive PDF cue:** Algorithm 3 Text2Motion hybrid planner 1: globals: Lχ, SatFunc, Shooting, Greedy-Step 2: function Text2Motion(i, s1, G; K, dmax) 3: F G sat ←SatFunc(G, Lχ) ▷Goal ...
- **p. 6 / 4.3 Search-based planning - extractive PDF cue:** We propose a second planner, greedy-search (see Figure 2, Right), which at each planning iteration ranks candidate skills predicted by the LLM and adds the ...
- **p. 4 / 4 Methods - extractive PDF cue:** We then introduce the full planning algorithm, Text2Motion, which synergistically integrates the strengths of both strategies.
- **p. 7 / 4.3 Search-based planning - extractive PDF cue:** See Figure 2 for a visualization of the shooting and greedy-search planners. are then multiplied to produce the overall skill score (Eq.
- **p. 5 / 4.2 Shooting-based planning - extractive PDF cue:** 13 15: if C == ∅then 16: raise planning failure 17: end if 18: j∗= arg maxj∈C p(j) success 19: return ψ(j∗) 1:t-1 ▷Return best ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to solve ...
- **p. 5 / 4.2 Shooting-based planning - extractive PDF cue:** To this end, the first strategy we propose is a shooting-based Algorithm 1 Shooting-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP 2: function ...
- **p. 6 / 4.3 Search-based planning - extractive PDF cue:** We propose a second planner, greedy-search (see Figure 2, Right), which at each planning iteration ranks candidate skills predicted by the LLM and adds the ...

## Source Evidence Cues

- **p. 5 / 4.2 Shooting-based planning - extractive PDF cue:** To this end, the first strategy we propose is a shooting-based Algorithm 1 Shooting-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP 2: function ...
- **p. 5 / 4.1 Goal prediction - extractive PDF cue:** We define a satisfaction function F G sat (s) : S →{0, 1} which takes as input a geometric state s and evaluates to 1 ...
- **p. 6 / 4.3 Search-based planning - extractive PDF cue:** We then compute the usefulness scores Sllm(ψk t ) by summing the token Algorithm 2 Search-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP ...
- **p. 7 / 4.4 Text2Motion - extractive PDF cue:** Algorithm 3 Text2Motion hybrid planner 1: globals: Lχ, SatFunc, Shooting, Greedy-Step 2: function Text2Motion(i, s1, G; K, dmax) 3: F G sat ←SatFunc(G, Lχ) ▷Goal ...
- **p. 6 / 4.3 Search-based planning - extractive PDF cue:** We propose a second planner, greedy-search (see Figure 2, Right), which at each planning iteration ranks candidate skills predicted by the LLM and adds the ...
- **p. 4 / 4 Methods - extractive PDF cue:** We then introduce the full planning algorithm, Text2Motion, which synergistically integrates the strengths of both strategies.
- **p. 7 / 4.3 Search-based planning - extractive PDF cue:** See Figure 2 for a visualization of the shooting and greedy-search planners. are then multiplied to produce the overall skill score (Eq.
- **Detected method headings:** 4 Methods (p. 4); 5.2 Large language model (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | To this end, the first strategy we propose is a shooting-based Algorithm 1 Shooting-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, ... | p. 5 (4.2 Shooting-based planning), p. 5 (4.1 Goal prediction) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | We define a satisfaction function F G sat (s) : S →{0, 1} which takes as input a geometric state s and ... | p. 5 (4.1 Goal prediction), p. 6 (4.3 Search-based planning) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | We then compute the usefulness scores Sllm(ψk t ) by summing the token Algorithm 2 Search-based LLM planner 1: globals: Lψ, Lχ, ... | p. 6 (4.3 Search-based planning), p. 7 (4.4 Text2Motion) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.2 Shooting-based planning - extractive PDF cue:** 13 15: if C == ∅then 16: raise planning failure 17: end if 18: j∗= arg maxj∈C p(j) success 19: return ψ(j∗) 1:t-1 ▷Return best ...
- **p. 4 / 3.3 Geometric feasibility planning - extractive PDF cue:** STAP resolves geometric dependencies across the skill sequence ψ1:H by maximizing the product of step reward probabilities of parameters a1:H: a∗ 1:H = arg max ...
- **p. 4 / 4 Methods - extractive PDF cue:** These strategies represent different ways of maximizing the overall planning objective in Eq.
- **p. 5 / 4.2 Shooting-based planning - extractive PDF cue:** Each candidate skill sequence is processed by the geometric feasibility planner which returns an estimate of the sequence's success probability (Eq.
- **p. 6 / 4.3 Search-based planning - extractive PDF cue:** This iterative approach can be described as a decomposition of the planning objective in Eq.
- **p. 6 / 4.3 Search-based planning - extractive PDF cue:** (8) Each planning iteration of greedy-search is responsible for finding the skill ψt that maximizes the skill score (Eq.
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 4 (4.1 Goal prediction), p. 4 (4 Methods), p. 5 (4.2 Shooting-based planning), p. 6 (4.3 Search-based planning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | define, satisfaction, function, takes, input, geometric, state, evaluates, goal, proposition, predicted, LLM, holds, skill | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | define, satisfaction, function, takes, input, geometric, state, evaluates, goal, proposition | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | Text2Motion, language-based, planning, framework, interfaces, LLM, library, learned, skills, geometric | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | then, raise, planning, failure, maxj, success, return, best, plan, function | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4.1 Goal prediction - extractive PDF cue:** We define a satisfaction function F G sat (s) : S →{0, 1} which takes as input a geometric state s and evaluates to 1 ...
- **p. 3 / 3.1 LLM and skill library - extractive PDF cue:** Each skill ψ consists of a policy π(a/s) and a parameterized manipulation primitive ϕ(a) [59], and is associated with a contextual bandit, or a single-timestep ...
- **p. 5 / 4.1 Goal prediction - extractive PDF cue:** Both shooting and greedy-search planners use the LLM to predict the set of valid goal states given the user's natural language instruction and a description ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are twofold: (i) a hybrid LLM planner that synergistically integrates shooting-based and search-based planning strategies to construct geometrically feasible plans for tasks not ...
- **p. 3 / 3.1 LLM and skill library - extractive PDF cue:** When a skill ψ is executed, an action a ∈A is sampled from its policy π(a/s) and fed to its primitive ϕ(a), which consumes the ...
- **p. 4 / 3.2 The planning objective - extractive PDF cue:** 3 represents the probability that skills ψ1:H achieve rewards r1:H when executed from initial state s1 with parameters a1:H; which is independent of the instruction ...
- **p. 4 / 3.2 The planning objective - extractive PDF cue:** This objective can be expressed as the joint probability of skill sequence ψ1:H and binary rewards r1:H given the instruction i and initial state s1: ...
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | If F G sat(st) evaluates to 1 for a geometric state st at timestep t ≤H + 1, then the planner returns ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | In particular, shooting offers efficiency when geometrically feasible skill sequences can be easily predicted by the LLM given the initial state and ... | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not recovered | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 5.2 Large language model - extractive PDF cue:** We use two pretrained language models, both of which were accessed through the OpenAI API: i) text-davinci-003, a variant of the InstructGPT [61] language model ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, strategy, shooting-based, Algorithm, LLM, planner, globals, SatFunc, STAP, function, Shooting, Goal, checker, Gen, plans, Init, candidate, define, satisfaction, takes.
- **Relevant PDF headings:** 4 Methods (p. 4); 5.2 Large language model (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | For example, Task 1 in Figure 4 requires the robot to pick and place three objects for a total of six skills. | p. 9 (5.4 Task suite), p. 9 (5.4 Task suite) |
| Search / trajectory decision | Top: Our method (Text2Motion) significantly outperforms all baselines on tasks involving partial affordance perception (Task 4, 5, 6). | p. 10 (6.1 Feasibility planning is required), p. 10 (6.1 Feasibility planning is required) |
| Execution interface | In the first two tasks (LH, Figure 5), we find that shooting achieves slightly higher success rates than greedy-search, while both methods ... | p. 11 (6.2 Search-based reasoning is), p. 11 (6.2 Search-based reasoning is) |

## Failure and Ablation Link

- **p. 8 / 5.2 Large language model - extractive PDF cue:** We use two pretrained language models, both of which were accessed through the OpenAI API: i) text-davinci-003, a variant of the InstructGPT [61] language model ...
- **p. 8 / 5.1 Baselines - extractive PDF cue:** Execution terminates when the score of the stop "skill" is larger than the other skills. innermono-gs: We implement the Object + Scene variant of Inner ...
- **p. 10 / 5.5 Evaluation and metrics - extractive PDF cue:** We do not perform task-level replanning, which would involve querying the LLM at timestep t + 1 for a new sequence of skills ψt+1:H. saycan-gs ...
- **p. 10 / 6.1 Feasibility planning is required - extractive PDF cue:** Bottom: Methods without geometric feasibility planning tend to have high sub-goal completion rates but very low success rates.
- **p. 11 / 6.1 Feasibility planning is required - extractive PDF cue:** In this plot, we analyse the various types of failure modes that occur with Text2Motion, shooting and greedy-search when evaluated on tasks with partial affordance ...
- **p. 12 / 6.2 Search-based reasoning is - extractive PDF cue:** Plan Length 5.0 7.0 7.0 Table 1 Ablation on hybrid planning method.
- **p. 12 / 6.4 Plan termination is made - extractive PDF cue:** We test this hypothesis in an ablation experiment (Figure 7), comparing our plan termination method to that of SayCan and Inner Monologue's, while keeping all ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (4.2 Shooting-based planning), p. 5 (4.1 Goal prediction), p. 6 (4.3 Search-based planning), p. 7 (4.4 Text2Motion), p. 6 (4.3 Search-based planning), p. 4 (4 Methods), objective p. 5 (4.2 Shooting-based planning), p. 4 (3.3 Geometric feasibility planning), p. 4 (4 Methods), p. 5 (4.2 Shooting-based planning), p. 6 (4.3 Search-based planning), p. 6 (4.3 Search-based planning), temporal p. 5 (4.1 Goal prediction), p. 7 (4.4 Text2Motion), p. 10 (5.5 Evaluation and metrics), p. 2 (2.1 Language for robot planning), p. 2 (2.1 Language for robot planning), p. 5 (4.1 Goal prediction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
