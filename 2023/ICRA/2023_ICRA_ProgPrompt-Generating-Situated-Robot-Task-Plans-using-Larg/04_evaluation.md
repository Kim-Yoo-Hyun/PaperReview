# Evaluation - ProgPrompt: Generating Situated Robot Task Plans using Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/10161317; PDF retrieval source: https://arxiv.org/pdf/2209.11302. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (IV. EXPERIMENTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS)): Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec).

## Evaluation Body Digest

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We create a dataset of 70 household tasks.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We evaluate our method with experiments in a virtual household environment and on a physical robot manipulator.
- **p. 6 / V. RESULTS - extractive body cue:** 4: Robot plan execution rollout example on the sorting task showing relevant objects banana, strawberry, bottle, plate and box, and a distractor object drill.
- **p. 5 / V. RESULTS - extractive body cue:** For each, we append a new object list representing the new environment after the example tasks in the prompt, followed by the task to be ...
- **p. 5 / V. RESULTS - extractive body cue:** We evaluate on 10 tasks each in two additional VH scenes beyond scene ENV-0 where other reported results take place.
- **p. 6 / V. RESULTS - extractive body cue:** Therefore, we intend the physical results to serve as a qualitative demonstration of the ease with which our prompting approach allows constraining and grounding LLM-generated ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec).
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight prompt ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4); V. RESULTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec). | p. 4 (IV. EXPERIMENTS) |
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that while this method achieves reasonable partial success through GCR, it does not match [2] for program executability Exec and does not ... | p. 5 (V. RESULTS) |
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, we find that FEEDBACK mechanisms in the example programs, namely the assertions and recovery actions, improve performance (rows 3 versus 4 and 5 ... | p. 5 (V. RESULTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | SR is the fraction of executions that achieved all task-relevant goal-conditions. | p. 4 (IV. EXPERIMENTS) |
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | All results shown use PROGPROMPT with comments, but not feedback. | p. 6 (V. RESULTS) |

## Dataset / Benchmark Role

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We create a dataset of 70 household tasks.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We evaluate our method with experiments in a virtual household environment and on a physical robot manipulator.
- **p. 6 / V. RESULTS - extractive body cue:** 4: Robot plan execution rollout example on the sorting task showing relevant objects banana, strawberry, bottle, plate and box, and a distractor object drill.
- **p. 5 / V. RESULTS - extractive body cue:** For each, we append a new object list representing the new environment after the example tasks in the prompt, followed by the task to be ...
- **p. 5 / V. RESULTS - extractive body cue:** We evaluate on 10 tasks each in two additional VH scenes beyond scene ENV-0 where other reported results take place.
- **p. 6 / V. RESULTS - extractive body cue:** Therefore, we intend the physical results to serve as a qualitative demonstration of the ease with which our prompting approach allows constraining and grounding LLM-generated ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. words, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight prompt ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Pythonic PROGPROMPT plan for "put salmon in the microwave." ended task plan generation (answer search); and 3) 1:1 prediction to action matching. The ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Robot plan execution rollout example on the sorting task showing relevant objects banana, strawberry, bottle, plate and box, and a distractor object drill. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We create a dataset of 70 household tasks. | embodiment, simulator version and control stack | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Task/environment | We evaluate our method with experiments in a virtual household environment and on a physical robot manipulator. | reset, timeout, object/scene variation | p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec). | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We use the system of [37] to implement the policy, and use MPPI for motion generation, SceneCollisionNet [37] to avoid collisions, and generate grasp ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Thus, we finetune GPT2 to learn a policy P(at/st, GPT3 step, a1:t-1) to map those generated sequences to executable actions in the simulation environment. | definition/direction/unit from same section | p. 5 (V. RESULTS) |
| We find that while this method achieves reasonable partial success through GCR, it does not match [2] for program executability Exec and does not ... | definition/direction/unit from same section | p. 5 (V. RESULTS) |
| Fig. 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The executability for the generated plans was always Exec=1. | definition/direction/unit from same section | p. 6 (V. RESULTS) |
| One possibility is to query the LLM again with the prompt and partially generated plan. | definition/direction/unit from same section | p. 6 (V. RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| First, PROGPROMPT (rows 3-6) outperforms prior work [2] (row 8) by a substantial margin on all metrics using the same large language model backbone. | comparison identity and matched condition | p. 5 (V. RESULTS) |
| We explore several ablations of PROGPROMPT. | comparison identity and matched condition | p. 5 (V. RESULTS) |
| The run without distractors failed due to a random gripper failure. | comparison identity and matched condition | p. 6 (V. RESULTS) |
| The real world introduces randomness that complicates a quantitative comparison between systems. | comparison identity and matched condition | p. 6 (V. RESULTS) |
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
| We explore several ablations of PROGPROMPT. | component/input/data sensitivity | p. 5 (V. RESULTS) |
| Second, we observe that the CODEX [28] and DAVINCI models [27]-themselves GPT3 variants-show mixed success at the task. | component/input/data sensitivity | p. 5 (V. RESULTS) |
| The run without distractors failed due to a random gripper failure. | component/input/data sensitivity | p. 6 (V. RESULTS) |
| Across tasks, with and without distractor objects, the system almost always succeeds, failing only on the sort task. | component/input/data sensitivity | p. 6 (V. RESULTS) |
| Fig. 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks. | Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec). | PDF body cue; verify exact table/figure and matched conditions | p. 4 (IV. EXPERIMENTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS) |
| Primary metric/result | We find that while this method achieves reasonable partial success through GCR, it does not match [2] for program executability Exec and does not ... | numeric claim only at cited anchor | p. 5 (V. RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / V. RESULTS - extractive body cue:** In particular, DAVINCI does not match base GPT3 performance (row 2 versus row 3), possibly because its prompt length constraints limit it to 2 task ...
- **p. 5 / V. RESULTS - extractive body cue:** We use the 35 tasks in the training set, and annotate the text steps and the corresponding action sequence to get 400 data points for ...
- **p. 5 / V. RESULTS - extractive body cue:** Task Desc /A/ SR Exec GCR watch tv 3 0.20±0.40 0.42±0.13 0.63±0.28 turn off light 3 0.40±0.49 1.00±0.00 0.65±0.30 brush teeth 8 0.80±0.40 0.74±0.09 0.87±0.26 ...
- **p. 5 / V. RESULTS - extractive body cue:** We evaluate on 10 tasks each in two additional VH scenes beyond scene ENV-0 where other reported results take place.
- **p. 5 / V. RESULTS - extractive body cue:** VH Scene SR Exec GCR ENV-0 0.34±0.08 0.84±0.01 0.65±0.05 ENV-1 0.56±0.08 0.85±0.02 0.81±0.07 ENV-2 0.56±0.05 0.85±0.03 0.72±0.09 Average 0.48±0.13 0.85±0.02 0.73±0.10 Other Environments We evaluate ...
- **p. 5 / V. RESULTS - extractive body cue:** We evaluate on 10 tasks with 5 runs each.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Qualitative Analysis and Limitations We manually inspect generated programs and their execution traces from PROGPROMPT and characterize common failure modes. | p. 5 (V. RESULTS) |
| body limitation/failure cue | Many failures stem from the decision to make PROGPROMPT agnostic to the deployed environment and its peculiarities, which may be resolved through explicitly communicating, ... | p. 5 (V. RESULTS) |
| body limitation/failure cue | Our physical robot setup did not allow reliably tracking system state and checking assertions, and is prone to random failures due to things like ... | p. 6 (V. RESULTS) |
| body limitation/failure cue | Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | The run without distractors failed due to a random gripper failure. | p. 6 (V. RESULTS) |
| body limitation/failure cue | We use the system of [37] to implement the policy, and use MPPI for motion generation, SceneCollisionNet [37] to avoid collisions, and generate grasp ... | p. 4 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| P encodes information like in(salmon, microwave) and agent close to(salmon). | p. 4 (IV. EXPERIMENTS) |
| PROGPROMPT utilizes programming language structures, leveraging the fact that LLMs are trained on vast web corpora that includes many programming tutorials and code documentation ... | p. 1 (I. INTRODUCTION) |
| However, such methods either require enumerating all possible next steps for scoring, or generate free-form text that may contain actions not possible on a ... | p. 1 (Abstract) |
| We highlight prompt comments, actions as imported function calls with objects as arguments, and assertions with recovery steps. | p. 2 (I. INTRODUCTION) |
| Second, we observe that the CODEX [28] and DAVINCI models [27]-themselves GPT3 variants-show mixed success at the task. | p. 5 (V. RESULTS) |
| Additionally, CODEX exceeds GPT3 performance on every metric (row 1 versus row 3), likely because CODEX is explicitly trained on programming language data. | p. 5 (V. RESULTS) |
| The run without distractors failed due to a random gripper failure. | p. 6 (V. RESULTS) |
| When run in a different VH environment, the agent cooks chicken instead. | p. 6 (V. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / V. RESULTS - extractive body cue:** Qualitative Analysis and Limitations We manually inspect generated programs and their execution traces from PROGPROMPT and characterize common failure modes.
- **p. 5 / V. RESULTS - extractive body cue:** Many failures stem from the decision to make PROGPROMPT agnostic to the deployed environment and its peculiarities, which may be resolved through explicitly communicating, for ...
- **p. 6 / V. RESULTS - extractive body cue:** Our physical robot setup did not allow reliably tracking system state and checking assertions, and is prone to random failures due to things like grasps ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight prompt ...
- **p. 6 / V. RESULTS - extractive body cue:** The run without distractors failed due to a random gripper failure.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We use the system of [37] to implement the policy, and use MPPI for motion generation, SceneCollisionNet [37] to avoid collisions, and generate grasp poses ...

- **Evidence anchors reviewed:** datasets p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 6 (V. RESULTS), metrics p. 4 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 4 (IV. EXPERIMENTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 1 (Figure/Table caption), baselines p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 3 (Figure/Table caption), results p. 4 (IV. EXPERIMENTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
