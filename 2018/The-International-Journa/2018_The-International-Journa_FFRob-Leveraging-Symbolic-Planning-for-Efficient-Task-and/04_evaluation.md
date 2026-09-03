# Evaluation - FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://journals.sagepub.com/doi/10.1177/0278364917739114; PDF retrieval source: https://journals.sagepub.com/doi/10.1177/0278364917739114. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 30 (11.4 Results), p. 30 (11.4 Results), p. 31 (11.4 Results), p. 31 (11.4 Results), p. 32 (Figure/Table caption)): HF F Rob, HA gave the best performance in both success rate and runtime.

## Evaluation Body Digest

- **p. 30 / 11 Experiments - extractive body cue:** We will restrict the robot to four side grasps per objects except on problems 1-1 & 1-2 where we use a single top grasp.
- **p. 30 / 11 Experiments - extractive body cue:** 11.3 Implementation We implemented FFROB in Python using the OpenRAVE robotics framework (Diankov and Kuffner 2008) for simulation.
- **p. 31 / 11.4 Results - extractive body cue:** Problem 5 demonstrates that FFROB is able to quickly solve a long-horizon, real-world problem involving symbolic actions, cluttered environments, and nonmonotonic requirements.
- **p. 27 / 11 Experiments - extractive body cue:** In order to reach the blue blocks, the robot must first move several red pillars out of way to clear a path for its base.
- **p. 27 / 11 Experiments - extractive body cue:** They require the robot to move the two blue blocks from the right table to the left table and return to its initial configuration.
- **p. 28 / 11 Experiments - extractive body cue:** The robot must retrieve the red cylinder from within the cluttered table of cyan cylinders.
- **p. 28 / 11 Experiments - extractive body cue:** The robot must also wash the cups (blue and cyan blocks) and set the table using the blue cups.
- **p. 31 / 11.4 Results - extractive body cue:** Because each object has an explicit goal, HGoals corresponds well with the actual distance to the goal, which is approximately twice HGoals.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** 11 Experiments (p. 27); 11.4 Results (p. 30).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 11.4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | HF F Rob, HA gave the best performance in both success rate and runtime. | p. 30 (11.4 Results) |
| 11.4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Helpful actions improved the performance of HF F Rob, HA over HF F Rob. | p. 30 (11.4 Results) |
| 11.4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Experiment results over 50 trials. informative heuristic estimate. | p. 31 (11.4 Results) |
| 11.4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | All but 1 of our algorithms were able to solve it with an above 95 percent success ratio in less than 40 seconds. | p. 31 (11.4 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 27. Best-first search extract and process procedures. A.2 Deferred Best-First Search Deferred best-first search (also called lazy greedy search) is a variant of ... | p. 32 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 30 / 11 Experiments - extractive body cue:** We will restrict the robot to four side grasps per objects except on problems 1-1 & 1-2 where we use a single top grasp.
- **p. 30 / 11 Experiments - extractive body cue:** 11.3 Implementation We implemented FFROB in Python using the OpenRAVE robotics framework (Diankov and Kuffner 2008) for simulation.
- **p. 31 / 11.4 Results - extractive body cue:** Problem 5 demonstrates that FFROB is able to quickly solve a long-horizon, real-world problem involving symbolic actions, cluttered environments, and nonmonotonic requirements.
- **p. 27 / 11 Experiments - extractive body cue:** In order to reach the blue blocks, the robot must first move several red pillars out of way to clear a path for its base.
- **p. 27 / 11 Experiments - extractive body cue:** They require the robot to move the two blue blocks from the right table to the left table and return to its initial configuration.
- **p. 28 / 11 Experiments - extractive body cue:** The robot must retrieve the red cylinder from within the cluttered table of cyan cylinders.
- **p. 28 / 11 Experiments - extractive body cue:** The robot must also wash the cups (blue and cyan blocks) and set the table using the blue cups.
- **p. 31 / 11.4 Results - extractive body cue:** Because each object has an explicit goal, HGoals corresponds well with the actual distance to the goal, which is approximately twice HGoals.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. A task and motion planning problem requiring cooking dinner. The robot must obtain two green cabbages from the shelves, clean them on the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2. The FFROB algorithm. 5.1 Extended Action Specification We model discretized PPM problems using a rep- resentation that extends Simple Action Specification (SAS+) (B¨ackstr¨om ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Pick, place, and move action schemas. Although we focus on PPM problems using these actions, we could easily define other action schemas to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Additional clean and cook action schemas. Definition 12. An EAS planning problem ⟨s0, C∗, A⟩is specified by an initial state s0, goal partial ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5. The primary search control procedure. problem, not just PPM problems. However, we explore the physical interpretation of these heuristics in the context of ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 6. Method for computing relaxed planning costs. Despite this, several relaxed planning heuristics have been shown to give effective estimates of the distance to ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 7. Visualization of compute-costs for a PPM problem requiring picking up the blue block. Each object o is made transparent at the level when ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 8. Method for extracting a relaxed plan. is separately computed before EXTRACT-RELAXED-PLAN. Our EASIEST procedure uses the original cost and additionally discounts the cost ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We will restrict the robot to four side grasps per objects except on problems 1-1 & 1-2 where we use a single top grasp. | embodiment, simulator version and control stack | p. 30 (11 Experiments), p. 30 (11 Experiments) |
| Task/environment | 11.3 Implementation We implemented FFROB in Python using the OpenRAVE robotics framework (Diankov and Kuffner 2008) for simulation. | reset, timeout, object/scene variation | p. 30 (11 Experiments), p. 31 (11.4 Results) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 2 (1.1 Approach) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 2 (1.1 Approach), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| HF F Rob, HA gave the best performance in both success rate and runtime. | definition/direction/unit from same section | p. 30 (11.4 Results) |
| A bar graph of the overall success rate across all problems per algorithm. | definition/direction/unit from same section | p. 30 (11 Experiments) |
| In practice, terminating the search after a finite amount of time to generate new samples will result in better performance. | definition/direction/unit from same section | p. 31 (11.4 Results) |
| They require the robot to move the two blue blocks from the right table to the left table and return to its initial configuration. | definition/direction/unit from same section | p. 27 (11 Experiments) |
| However, the turnips must be returned to the shelves if moved. | definition/direction/unit from same section | p. 28 (11 Experiments) |
| For all heuristics, as previously described, we automatically generate new samples if the FFROB heuristic is infinite before planning because a finite heuristic value ... | definition/direction/unit from same section | p. 29 (11 Experiments) |
| All but 1 of our algorithms were able to solve it with an above 95 percent success ratio in less than 40 seconds. | definition/direction/unit from same section | p. 31 (11.4 Results) |
| Figure 6. Method for computing relaxed planning costs. Despite this, several relaxed planning heuristics have been shown to give effective estimates of the distance ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The following heuristics are compared in the experiments: 1. | comparison identity and matched condition | p. 29 (11 Experiments) |
| Deferred best-first search typically outperforms standard best-first search because of its lazy evaluation of successors. | comparison identity and matched condition | p. 30 (11 Experiments) |
| Table 1. Experiment results over 50 trials. informative heuristic estimate. HF F performed worse than HF F Rob indicating that reachability information is vital ... | comparison identity and matched condition | p. 31 (Figure/Table caption) |
| This allows a large number of placements to be created for constrained problems without greatly increasing the branching factor. | comparison identity and matched condition | p. 30 (11 Experiments) |
| Figure 2. The FFROB algorithm. 5.1 Extended Action Specification We model discretized PPM problems using a rep- resentation that extends Simple Action Specification (SAS+) ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 15. A star-graph CRG visualized using end-effector poses. PATH(q, q′; (V, E)) (without considering any placed or held objects). In practice, we only ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 15. A star-graph CRG visualized using end-effector poses. PATH(q, q′; (V, E)) (without considering any placed or held objects). In practice, we only ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| This allows a large number of placements to be created for constrained problems without greatly increasing the branching factor. | component/input/data sensitivity | p. 30 (11 Experiments) |
| Figure 2. The FFROB algorithm. 5.1 Extended Action Specification We model discretized PPM problems using a rep- resentation that extends Simple Action Specification (SAS+) ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 27. Best-first search extract and process procedures. A.2 Deferred Best-First Search Deferred best-first search (also called lazy greedy search) is a variant of ... | component/input/data sensitivity | p. 32 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions. | HF F Rob, HA gave the best performance in both success rate and runtime. | PDF body cue; verify exact table/figure and matched conditions | p. 30 (11.4 Results), p. 30 (11.4 Results), p. 31 (11.4 Results), p. 31 (11.4 Results), p. 32 (Figure/Table caption) |
| Primary metric/result | Helpful actions improved the performance of HF F Rob, HA over HF F Rob. | numeric claim only at cited anchor | p. 30 (11.4 Results) |

- Numeric sentences retained from the body:
- **p. 30 / 11.4 Results - extractive body cue:** Each problem and algorithm combination was simulated over 50 trials.
- **p. 31 / 11.4 Results - extractive body cue:** Experiment results over 50 trials. informative heuristic estimate.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In practice, we do not increase the sampling parameter sizes upon a sampling failure. | p. 30 (11 Experiments) |
| body limitation/failure cue | We enforce timeouts of 30 iterations for S-PICK-PLACE due to inverse reachability, inverse kinematics, or motion planning failures. | p. 30 (11 Experiments) |
| body limitation/failure cue | Finally, each segment from q0 to q0 ∈B0 or from q∗to qk ∈Bk is collision-free by the problem being robustly feasible. | p. 33 (B.1 Proof of Theorem 1) |
| body limitation/failure cue | For any robustly feasible motion planning problem, there exists a sequence of k + 1, where k = l 2L δ m , d-spheres ... | p. 33 (B.1 Proof of Theorem 1) |
| body limitation/failure cue | Future work includes analytically and empirically investigating the quality of solutions returned by FFROB with respect to costs. | p. 31 (12 Conclusion) |
| body limitation/failure cue | Future work involves using the planning to guide the sampling such as done by Garrett et al. | p. 32 (12 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each problem and algorithm combination was simulated over 50 trials. | p. 30 (11.4 Results) |
| HF F Rob, HA gave the best performance in both success rate and runtime. | p. 30 (11.4 Results) |
| Experiment results over 50 trials. informative heuristic estimate. | p. 31 (11.4 Results) |
| 3 We prove completeness results for FFROB by identifying a class of non-degenerate PPM problems and proving FFROB will solve them with finite expected ... | p. 3 (1.1 Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 30 / 11 Experiments - extractive body cue:** In practice, we do not increase the sampling parameter sizes upon a sampling failure.
- **p. 30 / 11 Experiments - extractive body cue:** We enforce timeouts of 30 iterations for S-PICK-PLACE due to inverse reachability, inverse kinematics, or motion planning failures.
- **p. 33 / B.1 Proof of Theorem 1 - extractive body cue:** Finally, each segment from q0 to q0 ∈B0 or from q∗to qk ∈Bk is collision-free by the problem being robustly feasible.
- **p. 33 / B.1 Proof of Theorem 1 - extractive body cue:** For any robustly feasible motion planning problem, there exists a sequence of k + 1, where k = l 2L δ m , d-spheres (B0, ...
- **p. 31 / 12 Conclusion - extractive body cue:** Future work includes analytically and empirically investigating the quality of solutions returned by FFROB with respect to costs.
- **p. 32 / 12 Conclusion - extractive body cue:** Future work involves using the planning to guide the sampling such as done by Garrett et al.

- **Evidence anchors reviewed:** datasets p. 30 (11 Experiments), p. 30 (11 Experiments), p. 31 (11.4 Results), p. 27 (11 Experiments), p. 27 (11 Experiments), p. 28 (11 Experiments), metrics p. 30 (11.4 Results), p. 30 (11 Experiments), p. 31 (11.4 Results), p. 27 (11 Experiments), p. 28 (11 Experiments), p. 29 (11 Experiments), baselines p. 29 (11 Experiments), p. 30 (11 Experiments), p. 31 (Figure/Table caption), p. 30 (11 Experiments), p. 7 (Figure/Table caption), p. 17 (Figure/Table caption), results p. 30 (11.4 Results), p. 30 (11.4 Results), p. 31 (11.4 Results), p. 31 (11.4 Results), p. 32 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Experiment results over 50 trials. informative heuristic estimate. (p. 31, 11.4 Results).
- **Metric evidence:** HF F Rob, HA gave the best performance in both success rate and runtime. (p. 30, 11.4 Results).
- **Baseline/ablation evidence:** The following heuristics are compared in the experiments: 1. (p. 29, 11 Experiments).
- **Failure/negative evidence:** In practice, we do not increase the sampling parameter sizes upon a sampling failure. (p. 30, 11 Experiments).
