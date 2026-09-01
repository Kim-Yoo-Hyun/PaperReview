# Evaluation - A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/TSSC.1968.300136; PDF retrieval source: https://doi.org/10.1109/TSSC.1968.300136. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (6. The value of 0(no) remains), p. 5 (6. The value of 0(no) remains), p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (1) Mark s "open" and calculatef(s)), p. 3 (1) Mark s "open" and calculatef(s))): 0 ,On (3) We assume the infimum is achieved for some fOn In actual problems one probably never has an explicit representation for {Gn,0 but instead one selects a pro103 ...

## Evaluation Body Digest

- **p. 5 / 6. The value of 0(no) remains - extractive body cue:** This error occurs because the estimates h(s) = 8 and h(n2) = 1 are inconsistent in view of the fact that n2 is only six ...
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Starting with the node s, they generate some part of the subgraph G, by repetitive application of the successor operator r.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Application of r to the source nodes, to their successors, and so forth as long as new nodes can be generated results in an explicit ...
- **p. 3 / 1) Mark s "open" and calculatef(s) - extractive body cue:** Starting with s, we obtain successors ni and n2.
- **p. 3 / 1) Mark s "open" and calculatef(s) - extractive body cue:** Suppose A * expands ni next with successors n2 and n3.
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** In our example with cities connected by roads, no subgraph G01 is possible for which h(n) is less than the airline distance between city n ...
- **p. 5 / 6. The value of 0(no) remains - extractive body cue:** Nodes n2 and n3 are the successors of n, along arcs with costs as indicated.
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** 0 ,On (3) We assume the infimum is achieved for some fOn In actual problems one probably never has an explicit representation for {Gn,0 but ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6. The value of 0(no) remains | SYSTEM / EVALUATION SCOPE UNRESOLVED | 0 ,On (3) We assume the infimum is achieved for some fOn In actual problems one probably never has an explicit representation for {Gn,0 ... | p. 4 (6. The value of 0(no) remains) |
| 6. The value of 0(no) remains | SYSTEM / EVALUATION SCOPE UNRESOLVED | It means that any estimate h(n) calculated from data available in the "physical" situation represented by node n alone would not be improved by ... | p. 5 (6. The value of 0(no) remains) |
| 2) The heuristic approach typically uses special knowl | SYSTEM / EVALUATION SCOPE UNRESOLVED | Application of r to the source nodes, to their successors, and so forth as long as new nodes can be generated results in an ... | p. 2 (2) The heuristic approach typically uses special knowl) |
| 2) The heuristic approach typically uses special knowl | SYSTEM / EVALUATION SCOPE UNRESOLVED | The following is a typical illustration of the sort of problem to which our results are applicable. | p. 2 (2) The heuristic approach typically uses special knowl) |
| 1) Mark s "open" and calculatef(s) | SYSTEM / EVALUATION SCOPE UNRESOLVED | Starting with s, we obtain successors ni and n2. | p. 3 (1) Mark s "open" and calculatef(s)) |

## Dataset / Benchmark Role

- dataset/benchmark/environment role cue 없음

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | not recovered | embodiment, simulator version and control stack | 본문 anchor 없음 |
| Task/environment | not recovered | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This error occurs because the estimates h(s) = 8 and h(n2) = 1 are inconsistent in view of the fact that n2 is only ... | definition/direction/unit from same section | p. 5 (6. The value of 0(no) remains) |
| Starting with the node s, they generate some part of the subgraph G, by repetitive application of the successor operator r. | definition/direction/unit from same section | p. 2 (2) The heuristic approach typically uses special knowl) |
| Application of r to the source nodes, to their successors, and so forth as long as new nodes can be generated results in an ... | definition/direction/unit from same section | p. 2 (2) The heuristic approach typically uses special knowl) |
| Starting with s, we obtain successors ni and n2. | definition/direction/unit from same section | p. 3 (1) Mark s "open" and calculatef(s)) |
| Suppose A * expands ni next with successors n2 and n3. | definition/direction/unit from same section | p. 3 (1) Mark s "open" and calculatef(s)) |
| In our example with cities connected by roads, no subgraph G01 is possible for which h(n) is less than the airline distance between city ... | definition/direction/unit from same section | p. 4 (6. The value of 0(no) remains) |
| Nodes n2 and n3 are the successors of n, along arcs with costs as indicated. | definition/direction/unit from same section | p. 5 (6. The value of 0(no) remains) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared with other no more informed admissible algorithms, it expands the fewest possible nodes necessary to guarantee finding an optimal path. | comparison identity and matched condition | p. 6 (6. The value of 0(no) remains) |
| We can now prove a theorem about the optimality of A * as compared with any other admissible algorithm A that uses no more ... | comparison identity and matched condition | p. 6 (6. The value of 0(no) remains) |
| Case 3 Termination is at a goal node without achieving minimum cost. | comparison identity and matched condition | p. 4 (6. The value of 0(no) remains) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Case 3 Termination is at a goal node without achieving minimum cost. | component/input/data sensitivity | p. 4 (6. The value of 0(no) remains) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found. | 0 ,On (3) We assume the infimum is achieved for some fOn In actual problems one probably never has an explicit representation for {Gn,0 ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (6. The value of 0(no) remains), p. 5 (6. The value of 0(no) remains), p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (1) Mark s "open" and calculatef(s)), p. 3 (1) Mark s "open" and calculatef(s)) |
| Primary metric/result | It means that any estimate h(n) calculated from data available in the "physical" situation represented by node n alone would not be improved by ... | numeric claim only at cited anchor | p. 5 (6. The value of 0(no) remains) |

- Numeric sentences retained from the body:
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** Since the cost on any arc is at least 3, then for any node n further than Mf(s)/6 steps from s, we have f(n) > ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), ... | p. 7 (6. The value of 0(no) remains) |
| body limitation/failure cue | In this case, an admissible algorithm cannot rule out the possibility that the goal might be as close as a to that node with ... | p. 7 (IV. DiscussION AND CONCLUSIONS) |
| body limitation/failure cue | Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s. | p. 4 (6. The value of 0(no) remains) |
| body limitation/failure cue | If it expands nodes which obviously cannot be on an optimal path, it is wasting effort. | p. 2 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |
| body limitation/failure cue | Our algorithm prescribes how to use special knowledge-e.g., the knowledge that the shortest road route between any pair of cities cannot be less than ... | p. 2 (2) The heuristic approach typically uses special knowl) |
| body limitation/failure cue | Limitation of Subgraphs by Informationfrom the Problem In the preceding section, we proved that if h(n) is any lower bound on h(n), then A* ... | p. 4 (6. The value of 0(no) remains) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s. | p. 4 (6. The value of 0(no) remains) |
| Let %(M) be the set of nodes accessible within M steps from s, and let P(M) be the number of nodes in %(M). | p. 4 (6. The value of 0(no) remains) |
| Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), ... | p. 7 (6. The value of 0(no) remains) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 6. The value of 0(no) remains - extractive body cue:** Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), this ...
- **p. 7 / IV. DiscussION AND CONCLUSIONS - extractive body cue:** In this case, an admissible algorithm cannot rule out the possibility that the goal might be as close as a to that node with minimum ...
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s.
- **p. 2 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** If it expands nodes which obviously cannot be on an optimal path, it is wasting effort.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Our algorithm prescribes how to use special knowledge-e.g., the knowledge that the shortest road route between any pair of cities cannot be less than the ...
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** Limitation of Subgraphs by Informationfrom the Problem In the preceding section, we proved that if h(n) is any lower bound on h(n), then A* is ...

- **PDF anchors reviewed:** datasets 본문 anchor 없음, metrics p. 5 (6. The value of 0(no) remains), p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (1) Mark s "open" and calculatef(s)), p. 3 (1) Mark s "open" and calculatef(s)), p. 4 (6. The value of 0(no) remains), baselines p. 6 (6. The value of 0(no) remains), p. 6 (6. The value of 0(no) remains), p. 4 (6. The value of 0(no) remains), results p. 4 (6. The value of 0(no) remains), p. 5 (6. The value of 0(no) remains), p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (1) Mark s "open" and calculatef(s)), p. 3 (1) Mark s "open" and calculatef(s)).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
