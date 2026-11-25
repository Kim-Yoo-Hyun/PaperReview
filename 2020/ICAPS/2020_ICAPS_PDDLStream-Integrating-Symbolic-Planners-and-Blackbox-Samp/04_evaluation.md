# Evaluation - PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/ICAPS/article/view/6739; PDF retrieval source: https://cdn.aaai.org/ojs/6739/6739-40-9968-1-10-20200522.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (9 Experiments), p. 8 (9 Experiments)): Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan.

## Evaluation Body Digest

- **p. 8 / 9 Experiments - extractive body cue:** 9.1 Real-World Validation We applied PDDLStream to four real-world task and motion planning problems.
- **p. 8 / 9 Experiments - extractive body cue:** For each task, a PR2 robot observes the initial state, solves for a plan, and executes it in an open-loop fashion.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: From left to right: Domain 3 success percent, Domain 3 mean runtime, and plan cost over time for Domain 2. evaluation time. An ...
- **p. 7 / 9 Experiments - extractive body cue:** We experimented using the Incremental, Focused, Binding, and Adaptive algorithms on 100 randomly-generated problems within 3 domains in section 4.
- **p. 8 / 9 Experiments - extractive body cue:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.
- **p. 8 / 9 Experiments - extractive body cue:** Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan.
- **p. 8 / 9 Experiments - extractive body cue:** Focused, Binding, and Adaptive all outperform Incremental and perform about equivalently due to the less geometrically constrained nature of the domain.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** 9 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 9 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan. | p. 8 (9 Experiments) |
| 9 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Focused, Binding, and Adaptive all outperform Incremental and perform about equivalently due to the less geometrically constrained nature of the domain. | p. 8 (9 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 9 Experiments - extractive body cue:** 9.1 Real-World Validation We applied PDDLStream to four real-world task and motion planning problems.
- **p. 8 / 9 Experiments - extractive body cue:** For each task, a PR2 robot observes the initial state, solves for a plan, and executes it in an open-loop fashion.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Left: Domain 1 (with 5 blocks). Right: A real- world robot planning to "serve a meal" on the brown tray. pling procedures in ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Domain 3 (with 4 objectives). 5 PDDLStream Algorithms We present four PDDLStream algorithms that share several common subroutines. The first two algorithms (Incremen- ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: From left to right: Domain 1 success percent, Domain 1 mean runtime, and Domain 2.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: From left to right: Domain 3 success percent, Domain 3 mean runtime, and plan cost over time for Domain 2. evaluation time. An ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 9.1 Real-World Validation We applied PDDLStream to four real-world task and motion planning problems. | embodiment, simulator version and control stack | p. 8 (9 Experiments), p. 8 (9 Experiments) |
| Task/environment | For each task, a PR2 robot observes the initial state, solves for a plan, and executes it in an open-loop fashion. | reset, timeout, object/scene variation | p. 8 (9 Experiments) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: From left to right: Domain 3 success percent, Domain 3 mean runtime, and plan cost over time for Domain 2. evaluation time. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We experimented using the Incremental, Focused, Binding, and Adaptive algorithms on 100 randomly-generated problems within 3 domains in section 4. | definition/direction/unit from same section | p. 7 (9 Experiments) |
| Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. | definition/direction/unit from same section | p. 8 (9 Experiments) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). | comparison identity and matched condition | p. 7 (9 Experiments) |
| Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan. | comparison identity and matched condition | p. 8 (9 Experiments) |
| Focused, Binding, and Adaptive all outperform Incremental and perform about equivalently due to the less geometrically constrained nature of the domain. | comparison identity and matched condition | p. 8 (9 Experiments) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1: Left: Domain 1 (with 5 blocks). Right: A real- world robot planning to "serve a meal" on the brown tray. pling procedures ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and ... | Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (9 Experiments), p. 8 (9 Experiments) |
| Primary metric/result | Focused, Binding, and Adaptive all outperform Incremental and perform about equivalently due to the less geometrically constrained nature of the domain. | numeric claim only at cited anchor | p. 8 (9 Experiments) |

- Numeric sentences retained from the body:
- **p. 1 / 1 Introduction - extractive body cue:** Consider planning for an 11 degree-of-freedom (DOF) robot tasked with rearranging blocks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. | p. 8 (9 Experiments) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The additional stream binding computation only marginally increases the runtime of Adaptive. | p. 8 (9 Experiments) |
| We extend PDDL to support a generic, declarative specification for these procedures that treats their implementation as black boxes. | p. 1 (Abstract) |
| Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black ... | p. 1 (1 Introduction) |

## Limitations and Verification Questions

- **p. 8 / 9 Experiments - extractive body cue:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.

- **Evidence anchors reviewed:** datasets p. 8 (9 Experiments), p. 8 (9 Experiments), metrics p. 8 (Figure/Table caption), p. 7 (9 Experiments), p. 8 (9 Experiments), baselines p. 7 (9 Experiments), p. 8 (9 Experiments), p. 8 (9 Experiments), results p. 8 (9 Experiments), p. 8 (9 Experiments).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). (p. 7, 9 Experiments).
- **Metric evidence:** We experimented using the Incremental, Focused, Binding, and Adaptive algorithms on 100 randomly-generated problems within 3 domains in section 4. (p. 7, 9 Experiments).
- **Baseline/ablation evidence:** The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). (p. 7, 9 Experiments).
- **Failure/negative evidence:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. (p. 8, 9 Experiments).
