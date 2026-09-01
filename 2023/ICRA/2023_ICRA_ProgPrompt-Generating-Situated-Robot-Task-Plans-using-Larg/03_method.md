# Method - ProgPrompt: Generating Situated Robot Task Plans using Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/10161317; PDF retrieval source: https://arxiv.org/pdf/2209.11302. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 Pythonic task plan examples per prompt after evaluating), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (3 Pythonic task plan examples per prompt after evaluating), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): We use the 35 tasks in the training set, and annotate the text steps and the corresponding action sequence to get 400 data points for training and validation of this ...

## Method Body Digest

- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** We use the 35 tasks in the training set, and annotate the text steps and the corresponding action sequence to get 400 data points for ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. words, which ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** PROGPROMPT provides an LLM a Pythonic program header that imports available actions and their expected parameters, shows a list of environment objects, and then defines ...
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** The outputs of LANGPROMPT are generated action sequences, rather than our proposed, program-like structures.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** PROMPT for State Feedback represents example assertion checks.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning).
- **p. 1 / Abstract - extractive PDF cue:** We make concrete recommendations about prompt structure and generation constraints through ablation experiments, demonstrate state of the art success rates in VirtualHome household tasks, and ...
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** In particular, DAVINCI does not match base GPT3 performance (row 2 versus row 3), possibly because its prompt length constraints limit it to 2 task ...

## Design Rationale

- **p. 1 / Abstract - extractive PDF cue:** We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** We introduce PROGPROMPT, a prompting scheme that goes beyond conditioning LLMs in natural language.

## Source Evidence Cues

- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** We use the 35 tasks in the training set, and annotate the text steps and the corresponding action sequence to get 400 data points for ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. words, which ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** PROGPROMPT provides an LLM a Pythonic program header that imports available actions and their expected parameters, shows a list of environment objects, and then defines ...
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** The outputs of LANGPROMPT are generated action sequences, rather than our proposed, program-like structures.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** PROMPT for State Feedback represents example assertion checks.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | We use the 35 tasks in the training set, and annotate the text steps and the corresponding action sequence to get 400 ... | p. 5 (3 Pythonic task plan examples per prompt after evaluating), p. 1 (I. INTRODUCTION) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly ... | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | PROGPROMPT provides an LLM a Pythonic program header that imports available actions and their expected parameters, shows a list of environment objects, ... | p. 1 (I. INTRODUCTION), p. 5 (3 Pythonic task plan examples per prompt after evaluating) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive PDF cue:** We make concrete recommendations about prompt structure and generation constraints through ablation experiments, demonstrate state of the art success rates in VirtualHome household tasks, and ...
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** In particular, DAVINCI does not match base GPT3 performance (row 2 versus row 3), possibly because its prompt length constraints limit it to 2 task ...
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 5 (3 Pythonic task plan examples per prompt after evaluating).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | example, LLM, produced, reach, pick, pickles, string, would, have, neatly, executable, action, like, component | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | example, LLM, produced, reach, pick, pickles, string, would, have, neatly | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | present, programmatic, LLM, prompt, structure, enables, plan, generation, functional, across | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | make, concrete, recommendations, about, prompt, structure, generation, constraints, through, ablation | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** For example, if the LLM produced "reach in and pick up the jar of pickles," that string would have to neatly map to an executable ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** We incorporate situated state feedback from the environment by asserting preconditions of our plan, such as being close to the fridge before attempting to open ...
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** The outputs of LANGPROMPT are generated action sequences, rather than our proposed, program-like structures.
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** Thus, we finetune GPT2 to learn a policy P(at/st, GPT3 step, a1:t-1) to map those generated sequences to executable actions in the simulation environment.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** PROMPT for State Feedback represents example assertion checks.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning).
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | We collect a ground-truth sequence of actions that completes the task from an initial state, and record the final state g that ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | Thus, we finetune GPT2 to learn a policy P(at/st, GPT3 step, a1:t-1) to map those generated sequences to executable actions in the ... | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not recovered | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | We use the 35 tasks in the training set, and annotate the text steps and the corresponding action sequence to get 400 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** We use the 35 tasks in the training set, and annotate the text steps and the corresponding action sequence to get 400 data points for ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** PROGPROMPT utilizes programming language structures, leveraging the fact that LLMs are trained on vast web corpora that includes many programming tutorials and code documentation (Fig.
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** Additionally, CODEX exceeds GPT3 performance on every metric (row 1 versus row 3), likely because CODEX is explicitly trained on programming language data.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** tasks, training, annotate, text, steps, corresponding, action, sequence, data, points, validation, policy, PROGPROMPT, leverages, LLMs, strengths, world, knowledge, programming, language.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | We create a dataset of 70 household tasks. | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Search / trajectory decision | Fig. 3: Pythonic PROGPROMPT plan for "put salmon in the microwave." ended task plan generation (answer search); and 3) 1:1 prediction to ... | p. 3 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Execution interface | Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec). | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Pythonic PROGPROMPT plan for "put salmon in the microwave." ended task plan generation (answer search); and 3) 1:1 prediction to action matching. The ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. words, ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight prompt ...
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We use the system of [37] to implement the policy, and use MPPI for motion generation, SceneCollisionNet [37] to avoid collisions, and generate grasp poses ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 Pythonic task plan examples per prompt after evaluating), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (3 Pythonic task plan examples per prompt after evaluating), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective p. 1 (Abstract), p. 5 (3 Pythonic task plan examples per prompt after evaluating), temporal p. 4 (IV. EXPERIMENTS), p. 5 (3 Pythonic task plan examples per prompt after evaluating), p. 5 (3 Pythonic task plan examples per prompt after evaluating), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (II. BACKGROUND AND RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
