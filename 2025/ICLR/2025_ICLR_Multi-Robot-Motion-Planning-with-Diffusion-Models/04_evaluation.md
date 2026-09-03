# Evaluation - Multi-Robot Motion Planning with Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=AUCYptvAf3; PDF retrieval source: https://arxiv.org/pdf/2410.03072. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 15 (Figure/Table caption), p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 16 (Figure/Table caption), p. 19 (Figure/Table caption)): Figure 3: Analysis of success rates and data adherence scores, in randomly generated planning queries, of all MMD instantiations and a MAPF method with and without a learned cost map. ...

## Evaluation Body Digest

- **p. 20 / A.7 TRAINING AND DATASET GENERATION DETAILS - extractive body cue:** Importantly, each dataset trajectory respects the motion pattern dictated by the map within which it is embedded.
- **p. 20 / A.7 TRAINING AND DATASET GENERATION DETAILS - extractive body cue:** There, each data point is one, single-robot, trajectory from a random collision-free start configuration to a random collision-free goal configuration.
- **p. 16 / A.3 ADDITIONAL QUALITATIVE RESULTS - extractive body cue:** We keep the number of robots low for clarity.
- **p. 17 / A.3 ADDITIONAL QUALITATIVE RESULTS - extractive body cue:** The top two rows show test cases with 3 robots, and the bottom two rows with 6.
- **p. 17 / A.4 IMPLEMENTATION DETAILS - extractive body cue:** In our experiments, the size of each local map was 2 × 2 units, and the diameter of each disk robot was 0.1 units.
- **p. 16 / A.3 ADDITIONAL QUALITATIVE RESULTS - extractive body cue:** To better capture the behavior of the various trajectory generators discussed in this paper, Fig.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Analysis of success rates and data adherence scores, in randomly generated planning queries, of all MMD instantiations and a MAPF method with and ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 1: Comparison of methods by number of agents in the Empty environment (left) and the Highways environment (right). S is the success rate (%), ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** A.3 ADDITIONAL QUALITATIVE RESULTS (p. 16); A.4 IMPLEMENTATION DETAILS (p. 17); A.7 TRAINING AND DATASET GENERATION DETAILS (p. 20).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 3: Analysis of success rates and data adherence scores, in randomly generated planning queries, of all MMD instantiations and a MAPF method with ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: Comparison of methods by number of agents in the Empty environment (left) and the Highways environment (right). S is the success rate ... | p. 15 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5: Experimental setup and results for scaling MMD to larger environments and longer plan- ning horizons. MMD still relies on single agent data ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2: A comparison between MMD and "composite" diffusion models that generate trajectories for all agents at once. We observed consistent performance from MMD ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2: Additional results for a subset of our MMD and MAPF evaluation. Table columns are similar to Table 1. We omit acceleration information ... | p. 16 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 20 / A.7 TRAINING AND DATASET GENERATION DETAILS - extractive body cue:** Importantly, each dataset trajectory respects the motion pattern dictated by the map within which it is embedded.
- **p. 20 / A.7 TRAINING AND DATASET GENERATION DETAILS - extractive body cue:** There, each data point is one, single-robot, trajectory from a random collision-free start configuration to a random collision-free goal configuration.
- **p. 16 / A.3 ADDITIONAL QUALITATIVE RESULTS - extractive body cue:** We keep the number of robots low for clarity.
- **p. 17 / A.3 ADDITIONAL QUALITATIVE RESULTS - extractive body cue:** The top two rows show test cases with 3 robots, and the bottom two rows with 6.
- **p. 17 / A.4 IMPLEMENTATION DETAILS - extractive body cue:** In our experiments, the size of each local map was 2 × 2 units, and the diameter of each disk robot was 0.1 units.
- **p. 16 / A.3 ADDITIONAL QUALITATIVE RESULTS - extractive body cue:** To better capture the behavior of the various trajectory generators discussed in this paper, Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: An illustration of how MMD- CBS generates collision-free trajectories with constrained diffusion models. 3.1 CONSTRAINTS IN DIFFUSION MODELS An intuitive and effective constraint ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: A comparison between MMD and "composite" diffusion models that generate trajectories for all agents at once. We observed consistent performance from MMD but ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Analysis of success rates and data adherence scores, in randomly generated planning queries, of all MMD instantiations and a MAPF method with and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Scalability tests in high-congestion free-space MRMP. Circle (top row) asks robots to swap positions between opposite points on the perimeter. Weave (below), asks ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Experimental setup and results for scaling MMD to larger environments and longer plan- ning horizons. MMD still relies on single agent data in ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 1: Comparison of methods by number of agents in the Empty environment (left) and the Highways environment (right). S is the success rate (%), ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 2: Additional results for a subset of our MMD and MAPF evaluation. Table columns are similar to Table 1. We omit acceleration information from ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 6: Visual examples of trajectories generated by MMD-xECBS, MMD-PP, MPD-Composite, and A*Data-ECBS in tests within the Empty and Highways maps. The top two rows ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Importantly, each dataset trajectory respects the motion pattern dictated by the map within which it is embedded. | embodiment, simulator version and control stack | p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS), p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS) |
| Task/environment | There, each data point is one, single-robot, trajectory from a random collision-free start configuration to a random collision-free goal configuration. | reset, timeout, object/scene variation | p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS), p. 16 (A.3 ADDITIONAL QUALITATIVE RESULTS) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 4 (3 METHOD), p. 6 (3 METHOD) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 9 (3 METHOD), p. 4 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 3: Analysis of success rates and data adherence scores, in randomly generated planning queries, of all MMD instantiations and a MAPF method with ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 1: Comparison of methods by number of agents in the Empty environment (left) and the Highways environment (right). S is the success rate ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Figure 2: A comparison between MMD and "composite" diffusion models that generate trajectories for all agents at once. We observed consistent performance from MMD ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 7: Illustrations of our different maps. In the top row, we show an example trajectory that follows the data distribution prescribed by maps' ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| 6 shows a series of images of generated trajectories in two problems. | definition/direction/unit from same section | p. 16 (A.3 ADDITIONAL QUALITATIVE RESULTS) |
| 4.2) with radius 0.6 for the Highways map and 0.8 for the Empty map. | definition/direction/unit from same section | p. 17 (A.3 ADDITIONAL QUALITATIVE RESULTS) |
| Figure 1: An illustration of how MMD- CBS generates collision-free trajectories with constrained diffusion models. 3.1 CONSTRAINTS IN DIFFUSION MODELS An intuitive and effective ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| To create the datasets, we endow each map with a motion pattern function that, given start and goal configurations, generates the critical motions that ... | definition/direction/unit from same section | p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 2: A comparison between MMD and "composite" diffusion models that generate trajectories for all agents at once. We observed consistent performance from MMD ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 3: Analysis of success rates and data adherence scores, in randomly generated planning queries, of all MMD instantiations and a MAPF method with ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 1: Comparison of methods by number of agents in the Empty environment (left) and the Highways environment (right). S is the success rate ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |
| We also include details on our baseline implementations. | comparison identity and matched condition | p. 18 (A.4 IMPLEMENTATION DETAILS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2: A comparison between MMD and "composite" diffusion models that generate trajectories for all agents at once. We observed consistent performance from MMD ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 3: Analysis of success rates and data adherence scores, in randomly generated planning queries, of all MMD instantiations and a MAPF method with ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 5: Experimental setup and results for scaling MMD to larger environments and longer plan- ning horizons. MMD still relies on single agent data ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| The guidance function cost components we used were Jsmooth to encourage dynamically feasible trajectory generation with GPMP, Jobj for obstacle avoidance (both from Carvalho ... | component/input/data sensitivity | p. 17 (A.4 IMPLEMENTATION DETAILS) |
| Figure 7: Illustrations of our different maps. In the top row, we show an example trajectory that follows the data distribution prescribed by maps' ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions in this paper are threefold: (1) We propose a novel data-efficient framework for multirobot diffusion planning inspired by constraint-based search algorithms. | Figure 3: Analysis of success rates and data adherence scores, in randomly generated planning queries, of all MMD instantiations and a MAPF method with ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 15 (Figure/Table caption), p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 16 (Figure/Table caption), p. 19 (Figure/Table caption) |
| Primary metric/result | Table 1: Comparison of methods by number of agents in the Empty environment (left) and the Highways environment (right). S is the success rate ... | numeric claim only at cited anchor | p. 15 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 17 / A.3 ADDITIONAL QUALITATIVE RESULTS - extractive body cue:** The top two rows show test cases with 3 robots, and the bottom two rows with 6.
- **p. 20 / A.7 TRAINING AND DATASET GENERATION DETAILS - extractive body cue:** The trajectory connecting the start and goal is discretized uniformly to 64 points such that the time between consecutive trajectory configurations is constant.
- **p. 5 / 3 METHOD - extractive body cue:** This can be utilized in MMD replanning by initially adding noise to the stored trajectory for a limited number of steps (3 in our experiments; ...
- **p. 7 / 3 METHOD - extractive body cue:** We created three models: for 3, 6, and 9 robots.
- **p. 7 / 3 METHOD - extractive body cue:** The composite model achieved perfect success rates and high data adherence scores with 3 robots but struggled as the number of robots increased to 6.
- **p. 8 / 3 METHOD - extractive body cue:** The left column shows our test maps, the middle column compares success rates across 10 trials per robot count, and the right column presents the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Currently, MMD focuses on coordinating robots, seeking to produce collision-free data-driven trajectories. | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | In this paper, we present MMD, a multi-robot motion planner that learns to generate smooth collision-free trajectories for dozens of robots in complex environments. | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | Resembling their outcomes, we also observed a significant runtime improvement between prioritizing CT nodes based on their geometric quality and their collision count. | p. 14 (A.1 ADDITIONAL ALGORITHMIC DISCUSSION) |
| body limitation/failure cue | Once the batch is generated, MMD iterates over the new resulting trajectories N.τ i and marks the one with the least collisions as the ... | p. 14 (A.1 ADDITIONAL ALGORITHMIC DISCUSSION) |
| body limitation/failure cue | Figure 4: Scalability tests in high-congestion free-space MRMP. Circle (top row) asks robots to swap positions between opposite points on the perimeter. Weave (below), ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Figure 1: An illustration of how MMD- CBS generates collision-free trajectories with constrained diffusion models. 3.1 CONSTRAINTS IN DIFFUSION MODELS An intuitive and effective ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We based our diffusion planning implementation on the official code of Carvalho et al. | p. 17 (A.4 IMPLEMENTATION DETAILS) |
| We implemented all of our algorithms in Python and ran our experiments on a laptop with an Intel Core i9-12900H CPU, 32GB RAM (5.2GHz), ... | p. 17 (A.4 IMPLEMENTATION DETAILS) |
| We note that our code for generating data, training models, and multi-robot motion planning with MMD is publicly available, and we encourage readers to ... | p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS) |
| Therefore, during training time, they are not required to reason about other robots. | p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS) |
| We also include details on our baseline implementations. | p. 18 (A.4 IMPLEMENTATION DETAILS) |
| That is, N.τ i may be a set of B ∈Z>0 trajectories, with B being a batch size. | p. 14 (A.1 ADDITIONAL ALGORITHMIC DISCUSSION) |
| This can be utilized in MMD replanning by initially adding noise to the stored trajectory for a limited number of steps (3 in our ... | p. 5 (3 METHOD) |
| Each experiment with n robots begins by randomly picking start and goal states on a map for various algorithms to compute valid trajectories τ ... | p. 6 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6 CONCLUSION - extractive body cue:** Currently, MMD focuses on coordinating robots, seeking to produce collision-free data-driven trajectories.
- **p. 10 / 6 CONCLUSION - extractive body cue:** In this paper, we present MMD, a multi-robot motion planner that learns to generate smooth collision-free trajectories for dozens of robots in complex environments.
- **p. 14 / A.1 ADDITIONAL ALGORITHMIC DISCUSSION - extractive body cue:** Resembling their outcomes, we also observed a significant runtime improvement between prioritizing CT nodes based on their geometric quality and their collision count.
- **p. 14 / A.1 ADDITIONAL ALGORITHMIC DISCUSSION - extractive body cue:** Once the batch is generated, MMD iterates over the new resulting trajectories N.τ i and marks the one with the least collisions as the representative ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Scalability tests in high-congestion free-space MRMP. Circle (top row) asks robots to swap positions between opposite points on the perimeter. Weave (below), asks ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: An illustration of how MMD- CBS generates collision-free trajectories with constrained diffusion models. 3.1 CONSTRAINTS IN DIFFUSION MODELS An intuitive and effective constraint ...

- **Evidence anchors reviewed:** datasets p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS), p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS), p. 16 (A.3 ADDITIONAL QUALITATIVE RESULTS), p. 17 (A.3 ADDITIONAL QUALITATIVE RESULTS), p. 17 (A.4 IMPLEMENTATION DETAILS), p. 16 (A.3 ADDITIONAL QUALITATIVE RESULTS), metrics p. 8 (Figure/Table caption), p. 15 (Figure/Table caption), p. 6 (Figure/Table caption), p. 19 (Figure/Table caption), p. 16 (A.3 ADDITIONAL QUALITATIVE RESULTS), p. 17 (A.3 ADDITIONAL QUALITATIVE RESULTS), baselines p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 15 (Figure/Table caption), p. 18 (A.4 IMPLEMENTATION DETAILS), results p. 8 (Figure/Table caption), p. 15 (Figure/Table caption), p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 16 (Figure/Table caption), p. 19 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
