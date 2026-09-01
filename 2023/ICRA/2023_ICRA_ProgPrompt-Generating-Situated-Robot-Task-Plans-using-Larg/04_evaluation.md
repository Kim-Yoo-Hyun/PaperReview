# Evaluation - ProgPrompt: Generating Situated Robot Task Plans using Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/10161317; PDF retrieval source: https://arxiv.org/pdf/2209.11302. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (V. RESULTS), p. 6 (Figure/Table caption)): Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec).

## Evaluation Body Digest

- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We create a dataset of 70 household tasks.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We evaluate our method with experiments in a virtual household environment and on a physical robot manipulator.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec).
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight prompt ...
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We use the system of [37] to implement the policy, and use MPPI for motion generation, SceneCollisionNet [37] to avoid collisions, and generate grasp poses ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. words, ...
- **p. 5 / V. RESULTS - extractive PDF cue:** The variability in performance across runs arises from sampling LLM output.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: Robot plan execution rollout example on the sorting task showing relevant objects banana, strawberry, bottle, plate and box, and a distractor object drill. ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4); V. RESULTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec). | p. 4 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | SR is the fraction of executions that achieved all task-relevant goal-conditions. | p. 4 (IV. EXPERIMENTS) |
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The variability in performance across runs arises from sampling LLM output. | p. 5 (V. RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 4: Robot plan execution rollout example on the sorting task showing relevant objects banana, strawberry, bottle, plate and box, and a distractor object ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We create a dataset of 70 household tasks.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We evaluate our method with experiments in a virtual household environment and on a physical robot manipulator.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. words, ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight prompt ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Pythonic PROGPROMPT plan for "put salmon in the microwave." ended task plan generation (answer search); and 3) 1:1 prediction to action matching. The ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: Robot plan execution rollout example on the sorting task showing relevant objects banana, strawberry, bottle, plate and box, and a distractor object drill. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We create a dataset of 70 household tasks. | embodiment, simulator version and control stack | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Task/environment | We evaluate our method with experiments in a virtual household environment and on a physical robot manipulator. | reset, timeout, object/scene variation | p. 4 (IV. EXPERIMENTS) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 5 (3 Pythonic task plan examples per prompt after evaluating), p. 5 (3 Pythonic task plan examples per prompt after evaluating) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec). | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We use the system of [37] to implement the policy, and use MPPI for motion generation, SceneCollisionNet [37] to avoid collisions, and generate grasp ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Fig. 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The variability in performance across runs arises from sampling LLM output. | definition/direction/unit from same section | p. 5 (V. RESULTS) |
| Fig. 4: Robot plan execution rollout example on the sorting task showing relevant objects banana, strawberry, bottle, plate and box, and a distractor object ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 3: Pythonic PROGPROMPT plan for "put salmon in the microwave." ended task plan generation (answer search); and 3) 1:1 prediction to action matching. ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 3: Pythonic PROGPROMPT plan for "put salmon in the microwave." ended task plan generation (answer search); and 3) 1:1 prediction to action matching. ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 3: Pythonic PROGPROMPT plan for "put salmon in the microwave." ended task plan generation (answer search); and 3) 1:1 prediction to action matching. ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Fig. 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks. | Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec). | PDF body cue; verify exact table/figure and matched conditions | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (V. RESULTS), p. 6 (Figure/Table caption) |
| Primary metric/result | SR is the fraction of executions that achieved all task-relevant goal-conditions. | numeric claim only at cited anchor | p. 4 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** In particular, DAVINCI does not match base GPT3 performance (row 2 versus row 3), possibly because its prompt length constraints limit it to 2 task ...
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** We use the 35 tasks in the training set, and annotate the text steps and the corresponding action sequence to get 400 data points for ...
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** Task Desc /A/ SR Exec GCR watch tv 3 0.20±0.40 0.42±0.13 0.63±0.28 turn off light 3 0.40±0.49 1.00±0.00 0.65±0.30 brush teeth 8 0.80±0.40 0.74±0.09 0.87±0.26 ...
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** We evaluate on 10 tasks each in two additional VH scenes beyond scene ENV-0 where other reported results take place.
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** VH Scene SR Exec GCR ENV-0 0.34±0.08 0.84±0.01 0.65±0.05 ENV-1 0.56±0.08 0.85±0.02 0.81±0.07 ENV-2 0.56±0.05 0.85±0.03 0.72±0.09 Average 0.48±0.13 0.85±0.02 0.73±0.10 Other Environments We evaluate ...
- **p. 5 / 3 Pythonic task plan examples per prompt after evaluating - extractive PDF cue:** We evaluate on 10 tasks with 5 runs each.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | We use the system of [37] to implement the policy, and use MPPI for motion generation, SceneCollisionNet [37] to avoid collisions, and generate grasp ... | p. 4 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| P encodes information like in(salmon, microwave) and agent close to(salmon). | p. 4 (IV. EXPERIMENTS) |
| PROGPROMPT utilizes programming language structures, leveraging the fact that LLMs are trained on vast web corpora that includes many programming tutorials and code documentation ... | p. 1 (I. INTRODUCTION) |
| However, such methods either require enumerating all possible next steps for scoring, or generate free-form text that may contain actions not possible on a ... | p. 1 (Abstract) |
| We highlight prompt comments, actions as imported function calls with objects as arguments, and assertions with recovery steps. | p. 2 (I. INTRODUCTION) |
| Second, we observe that the CODEX [28] and DAVINCI models [27]-themselves GPT3 variants-show mixed success at the task. | p. 5 (3 Pythonic task plan examples per prompt after evaluating) |
| Additionally, CODEX exceeds GPT3 performance on every metric (row 1 versus row 3), likely because CODEX is explicitly trained on programming language data. | p. 5 (3 Pythonic task plan examples per prompt after evaluating) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight prompt ...
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We use the system of [37] to implement the policy, and use MPPI for motion generation, SceneCollisionNet [37] to avoid collisions, and generate grasp poses ...

- **PDF anchors reviewed:** datasets p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), metrics p. 4 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 4 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), p. 5 (V. RESULTS), p. 6 (Figure/Table caption), baselines p. 3 (Figure/Table caption), results p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (V. RESULTS), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
