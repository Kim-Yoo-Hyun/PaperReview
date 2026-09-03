# Evaluation - SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (50 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/rana23a.html; PDF retrieval source: https://arxiv.org/pdf/2307.06135. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5 Results), p. 7 (Figure/Table caption), p. 46 (Figure/Table caption), p. 6 (5 Results), p. 7 (Figure/Table caption), p. 21 (Figure/Table caption)): The table shows the semantic search success rate in finding a suitable subgraph for planning.

## Evaluation Body Digest

- **p. 13 / A Implementation Details - extractive body cue:** This static prompt is both task- and environment-agnostic and takes up ≈3900 tokens of the LLM's input.
- **p. 13 / A Implementation Details - extractive body cue:** We define the agent's role, details pertaining to the scene graph environment, the desired output structure and a set of input-output examples which together form ...
- **p. 6 / 5 Results - extractive body cue:** 5.1 Semantic Search Office Home Subtask Human SayPlan (GPT-3.5) SayPlan (GPT-4) Human SayPlan (GPT-3.5) SayPlan (GPT-4) Simple Search 100% 6.6% 86.7% 100% 0.0% 86.7% Complex ...
- **p. 6 / 5 Results - extractive body cue:** The table shows the semantic search success rate in finding a suitable subgraph for planning.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Causal Planning Results. Left: Correctness and Executability on Simple and Long Horizon planning tasks and Right: Types of execution errors encountered when planning ...
- **p. 32 / Figure/Table caption - extractive body cue:** Table 18: Correctness, Executability and Number of Replanning Iterations for Long-Horizon Planning Instructions. Evaluating the performance of SayPlan on each long-horizon planning instruction. Values indicated ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: SayPlan Overview (top). SayPlan operates across two stages to ensure scalability: (left) Given a collapsed 3D scene graph and a task instruction, semantic ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene graphs. Note the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** 5 Results (p. 6); A Implementation Details (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The table shows the semantic search success rate in finding a suitable subgraph for planning. | p. 6 (5 Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene graphs. Note ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 8: Evaluating the performance of SayPlan's causal planning capabilities as the scale of the environment increases. For the office environment used in this ... | p. 46 (Figure/Table caption) |
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We summarise the results for the semantic search evaluation in Table | p. 6 (5 Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Causal Planning Results. Left: Correctness and Executability on Simple and Long Horizon planning tasks and Right: Types of execution errors encountered when ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 13 / A Implementation Details - extractive body cue:** This static prompt is both task- and environment-agnostic and takes up ≈3900 tokens of the LLM's input.
- **p. 13 / A Implementation Details - extractive body cue:** We define the agent's role, details pertaining to the scene graph environment, the desired output structure and a set of input-output examples which together form ...
- **p. 6 / 5 Results - extractive body cue:** 5.1 Semantic Search Office Home Subtask Human SayPlan (GPT-3.5) SayPlan (GPT-4) Human SayPlan (GPT-3.5) SayPlan (GPT-4) Simple Search 100% 6.6% 86.7% 100% 0.0% 86.7% Complex ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: SayPlan Overview (top). SayPlan operates across two stages to ensure scalability: (left) Given a collapsed 3D scene graph and a task instruction, semantic ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Hierarchical Structure of a 3D Scene Graph. This graph consists of 4 levels. Notes that the room nodes are connected to one another ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Evaluating the semantic search capabilities of GPT-4. The table shows the semantic search success rate in finding a suitable subgraph for planning. We ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Causal Planning Results. Left: Correctness and Executability on Simple and Long Horizon planning tasks and Right: Types of execution errors encountered when planning ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene graphs. Note the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 4: Large-scale environments used to evaluate SayPlan. The environments span multiple rooms and floors including a vast range of We evaluate SayPlan across a ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 4: Detailed 3DSG breakdown for the Office Environment. The table summarises the num- ber of different entities present in the 3DSG, the total LLM ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This static prompt is both task- and environment-agnostic and takes up ≈3900 tokens of the LLM's input. | embodiment, simulator version and control stack | p. 13 (A Implementation Details), p. 13 (A Implementation Details) |
| Task/environment | We define the agent's role, details pertaining to the scene graph environment, the desired output structure and a set of input-output examples which together ... | reset, timeout, object/scene variation | p. 13 (A Implementation Details), p. 6 (5 Results) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 2 (1 Introduction), p. 13 (A Implementation Details) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The table shows the semantic search success rate in finding a suitable subgraph for planning. | definition/direction/unit from same section | p. 6 (5 Results) |
| Table 3: Causal Planning Results. Left: Correctness and Executability on Simple and Long Horizon planning tasks and Right: Types of execution errors encountered when ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 18: Correctness, Executability and Number of Replanning Iterations for Long-Horizon Planning Instructions. Evaluating the performance of SayPlan on each long-horizon planning instruction. Values ... | definition/direction/unit from same section | p. 32 (Figure/Table caption) |
| Figure 1: SayPlan Overview (top). SayPlan operates across two stages to ensure scalability: (left) Given a collapsed 3D scene graph and a task instruction, ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene graphs. Note ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 19: Causal Planning Evaluation. Task planning action sequences generated for a mobile manipulator robot to follow for both the simple and long-horizon planning ... | definition/direction/unit from same section | p. 45 (Figure/Table caption) |
| Figure 7: Evaluating the performance of the underlying LLMs semantic search capabilities as the scale of the environment increases. For the office environment used ... | definition/direction/unit from same section | p. 46 (Figure/Table caption) |
| Figure 9: Real World Execution of a Generated Long Horizon Plan. Execution of a generated and validated task plan on a real-world mobile manipulator ... | definition/direction/unit from same section | p. 47 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene graphs. Note ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 18: Correctness, Executability and Number of Replanning Iterations for Long-Horizon Planning Instructions. Evaluating the performance of SayPlan on each long-horizon planning instruction. Values ... | comparison identity and matched condition | p. 32 (Figure/Table caption) |
| Figure 5: 3D Scene Graph - Fully Expanded Office Environment. Full 3D scene graph exposing all the rooms, assets and objects available in the ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 5: 3D Scene Graph - Fully Expanded Office Environment. Full 3D scene graph exposing all the rooms, assets and objects available in the ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |
| Figure 1: SayPlan Overview (top). SayPlan operates across two stages to ensure scalability: (left) Given a collapsed 3D scene graph and a task instruction, ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning ... | component/input/data sensitivity | p. 13 (A Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of ... | The table shows the semantic search success rate in finding a suitable subgraph for planning. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5 Results), p. 7 (Figure/Table caption), p. 46 (Figure/Table caption), p. 6 (5 Results), p. 7 (Figure/Table caption), p. 21 (Figure/Table caption) |
| Primary metric/result | Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene graphs. Note ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 13 / A Implementation Details - extractive body cue:** This static prompt is both task- and environment-agnostic and takes up ≈3900 tokens of the LLM's input.
- **p. 13 / A Implementation Details - extractive body cue:** This static prompt is both task- and environment-agnostic and takes up ≈3900 tokens of the LLM's input.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 8: Evaluating the performance of SayPlan's causal planning capabilities as the scale of the environment increases. For the office environment used in this ... | p. 46 (Figure/Table caption) |
| body limitation/failure cue | Table 18: Correctness, Executability and Number of Replanning Iterations for Long-Horizon Planning Instructions. Evaluating the performance of SayPlan on each long-horizon planning instruction. Values ... | p. 32 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple ...
- **p. 46 / Figure/Table caption - extractive body cue:** Figure 8: Evaluating the performance of SayPlan's causal planning capabilities as the scale of the environment increases. For the office environment used in this study, ...
- **p. 32 / Figure/Table caption - extractive body cue:** Table 18: Correctness, Executability and Number of Replanning Iterations for Long-Horizon Planning Instructions. Evaluating the performance of SayPlan on each long-horizon planning instruction. Values indicated ...

- **Evidence anchors reviewed:** datasets p. 13 (A Implementation Details), p. 13 (A Implementation Details), p. 6 (5 Results), metrics p. 6 (5 Results), p. 7 (Figure/Table caption), p. 32 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 45 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 32 (Figure/Table caption), p. 20 (Figure/Table caption), results p. 6 (5 Results), p. 7 (Figure/Table caption), p. 46 (Figure/Table caption), p. 6 (5 Results), p. 7 (Figure/Table caption), p. 21 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (50 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We summarise the results for the semantic search evaluation in Table (p. 6, 5 Results).
- **Metric evidence:** The table shows the semantic search success rate in finding a suitable subgraph for planning. (p. 6, 5 Results).
- **Baseline/ablation evidence:** We summarise the results for the semantic search evaluation in Table (p. 6, 5 Results).
- **Failure/negative evidence:** An odd failure case in the simple search instructions involved negation, where the agent consistently failed when presented with questions such as "Find me an office that does not have ... (p. 7, 1. SayPlan (GPT-3.5) consistently).
