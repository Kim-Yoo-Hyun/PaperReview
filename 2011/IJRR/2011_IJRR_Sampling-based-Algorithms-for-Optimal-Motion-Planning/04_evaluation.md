# Evaluation - Sampling-based Algorithms for Optimal Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (76 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1105.1186; PDF retrieval source: https://arxiv.org/pdf/1105.1186. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 31 (V RRT∗), p. 33 (V RRT∗), p. 33 (V RRT∗), p. 34 (V RRT∗), p. 5 (Figure/Table caption), p. 29 (V RRT∗)): An approximate nearest neighbor can be computed using balanced-box decomposition (BBD) trees, which achieves O(cd,ε log n) query time using O(d n) space (Arya et al., 1999), where cd,ε ≤ ...

## Evaluation Body Digest

- **p. 31 / V RRT∗ - extractive body cue:** However, in many online real-time applications such as robotics, it is highly desirable to reduce the computation time of each iteration under sublinear bounds, e.g., ...
- **p. 25 / V RRT∗ - extractive body cue:** A single tile is shown in the left; a tiling of the optimal trajectory σ∗is shown on the right.
- **p. 29 / V RRT∗ - extractive body cue:** 4.3 Computational Complexity The objective of this section is to compare the computational complexity of the algorithms provided in Section 3.
- **p. 31 / V RRT∗ - extractive body cue:** Complexity of the CollisionFree procedure In this section, complexity of the CollisionFree procedure in terms of the number of obstacles in the environment is analyzed, ...
- **p. 32 / V RRT∗ - extractive body cue:** Let n denote the total number of iterations (or, alternatively, the number of samples), and m denote the number of obstacles in the environment.
- **p. 33 / V RRT∗ - extractive body cue:** Both algorithms are run in a square environment.
- **p. 61 / Figure/Table caption - extractive body cue:** Figure 25: The set eBn,m of non-intersection balls is illustrated. Finally, the following lemma states that the cost of the minimum cost path in the ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 1: An illustration of the δ-interior of Xfree. The obstacle region Xobs is shown in dark grey and the δ-interior of Xfree is shown ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V RRT∗ | SYSTEM / EVALUATION SCOPE UNRESOLVED | An approximate nearest neighbor can be computed using balanced-box decomposition (BBD) trees, which achieves O(cd,ε log n) query time using O(d n) space (Arya ... | p. 31 (V RRT∗) |
| V RRT∗ | SYSTEM / EVALUATION SCOPE UNRESOLVED | On the other hand, running the RRT∗algorithm further improves the paths in the tree to lower cost ones. | p. 33 (V RRT∗) |
| V RRT∗ | SYSTEM / EVALUATION SCOPE UNRESOLVED | The figure illustrates that, in this case, the RRT algorithm does not improve the feasible solution to converge to an optimum solution. | p. 33 (V RRT∗) |
| V RRT∗ | SYSTEM / EVALUATION SCOPE UNRESOLVED | Moreover, as the number of samples increase, the RRT∗improves its tree to include paths with smaller cost and eventually discovers a path in a ... | p. 34 (V RRT∗) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: Summary of results. Time and space complexity are expressed as a function of the number of samples n, for a fixed environment. | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 31 / V RRT∗ - extractive body cue:** However, in many online real-time applications such as robotics, it is highly desirable to reduce the computation time of each iteration under sublinear bounds, e.g., ...
- **p. 25 / V RRT∗ - extractive body cue:** A single tile is shown in the left; a tiling of the optimal trajectory σ∗is shown on the right.
- **p. 29 / V RRT∗ - extractive body cue:** 4.3 Computational Complexity The objective of this section is to compare the computational complexity of the algorithms provided in Section 3.
- **p. 31 / V RRT∗ - extractive body cue:** Complexity of the CollisionFree procedure In this section, complexity of the CollisionFree procedure in terms of the number of obstacles in the environment is analyzed, ...
- **p. 32 / V RRT∗ - extractive body cue:** Let n denote the total number of iterations (or, alternatively, the number of samples), and m denote the number of obstacles in the environment.
- **p. 33 / V RRT∗ - extractive body cue:** Both algorithms are run in a square environment.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Summary of results. Time and space complexity are expressed as a function of the number of samples n, for a fixed environment.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 1: An illustration of the δ-interior of Xfree. The obstacle region Xobs is shown in dark grey and the δ-interior of Xfree is shown ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 2: An illustration of a path σ with weak δ-clearance. The path σ′ that lies inside intδ(Xfree) and is in the same homotopy class ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 3: An illustration of an example path σ that does not have weak δ-clearance. For any positive value of δ, there is no path ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 4: An illustration of a path that has weak δ-clearance. The path passes through a point where two spheres representing the obstacle region are ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 5: An illustration of the tiles mention in the proof of Theorem 31. A single tile is shown in the left; a tiling of ...
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 6: The event that the inner cube contains no points and each outer cube contains at least k points of the point process is ...
- **p. 27 / Figure/Table caption - extractive body cue:** Figure 7: An illustration of the covering of the optimal path, σ∗, with openly disjoint balls. The balls cover only a portion of σ∗that lies ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, in many online real-time applications such as robotics, it is highly desirable to reduce the computation time of each iteration under sublinear bounds, ... | embodiment, simulator version and control stack | p. 31 (V RRT∗), p. 25 (V RRT∗) |
| Task/environment | A single tile is shown in the left; a tiling of the optimal trajectory σ∗is shown on the right. | reset, timeout, object/scene variation | p. 25 (V RRT∗), p. 29 (V RRT∗) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 11 (1 Introduction) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 13 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 25: The set eBn,m of non-intersection balls is illustrated. Finally, the following lemma states that the cost of the minimum cost path in ... | definition/direction/unit from same section | p. 61 (Figure/Table caption) |
| Figure 1: An illustration of the δ-interior of Xfree. The obstacle region Xobs is shown in dark grey and the δ-interior of Xfree is ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| A first set of experiments were run to illustrate the different performance of k-nearest PRM and of PRM∗. | definition/direction/unit from same section | p. 33 (V RRT∗) |
| The high variance in solutions returned by the RRT algorithm stems from the fact that there are two different homotopy classes of paths that ... | definition/direction/unit from same section | p. 34 (V RRT∗) |
| Figure 3: An illustration of an example path σ that does not have weak δ-clearance. For any positive value of δ, there is no ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Let Mn denote the maximum number of tiles that can be generated in this manner and note Mn ≥s∗ 2 n1/d. | definition/direction/unit from same section | p. 25 (V RRT∗) |
| Hence, the graph returned by sPRM includes all the paths that are present in the graph returned by PRM∗. | definition/direction/unit from same section | p. 25 (V RRT∗) |
| Thus, no edge can cross the white cube illustrated in Figure 6. | definition/direction/unit from same section | p. 26 (V RRT∗) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Using these results, a thorough analysis of the computational complexity of the all the algorithms is given in terms of the number of simple ... | comparison identity and matched condition | p. 29 (V RRT∗) |
| Time complexity of the processing phase The following results characterize the asymptotic computational complexity of various sampling-based algorithms in terms of the number of ... | comparison identity and matched condition | p. 32 (V RRT∗) |
| The main bulk of the experiments were aimed at demonstrating the performance of the RRT∗ algorithm, especially in comparison with its "standard" counterpart, i.e., ... | comparison identity and matched condition | p. 33 (V RRT∗) |
| A comparison with the RRT algorithm is provided in the same figure. | comparison identity and matched condition | p. 34 (V RRT∗) |
| Figure 18: A comparison of the running time of the RRT∗and the RRT algorithms. The ratio of the running time of the RRT∗over that ... | comparison identity and matched condition | p. 42 (Figure/Table caption) |
| Figure 19: A comparison of the running time of the RRT∗and the RRT algorithms in an environ- ment with obstacles. The ratio of the ... | comparison identity and matched condition | p. 43 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 11: Cost of the best path in the PRM∗algorithm is shown in up to 2, 3, 4, and 5 dimensional configuration spaces, in ... | component/input/data sensitivity | p. 36 (Figure/Table caption) |
| Moreover, none of these vertices can be in the same connected component with Xn. | component/input/data sensitivity | p. 29 (V RRT∗) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| As in the early seminal papers on incremental samplingbased motion planning algorithms such as Kuffner and LaValle (2000), no differential constraints are considered (i.e., ... | An approximate nearest neighbor can be computed using balanced-box decomposition (BBD) trees, which achieves O(cd,ε log n) query time using O(d n) space (Arya ... | PDF body cue; verify exact table/figure and matched conditions | p. 31 (V RRT∗), p. 33 (V RRT∗), p. 33 (V RRT∗), p. 34 (V RRT∗), p. 5 (Figure/Table caption), p. 29 (V RRT∗) |
| Primary metric/result | On the other hand, running the RRT∗algorithm further improves the paths in the tree to lower cost ones. | numeric claim only at cited anchor | p. 33 (V RRT∗) |

- Numeric sentences retained from the body:
- **p. 25 / V RRT∗ - extractive body cue:** Let In,m denote the indicator random variable for the event that the center cube of this tile contains no samples, whereas every outer cube contains ...
- **p. 25 / V RRT∗ - extractive body cue:** The probability that an outer cube contains at least k + 1 samples is 1 -P  {Poisson(2-d/µ(Xfree)) ≥k + 1}  = 1 - P({Poisson(2-d/µ(Xfree)) ...
- **p. 30 / V RRT∗ - extractive body cue:** Similarly, for the RRT, MRRT n = 1 for all n ∈N.
- **p. 34 / V RRT∗ - extractive body cue:** The number of iterations versus the cost of the best path averaged over 100 trials is shown in Figure 20.
- **p. 8 / 1 Introduction - extractive body cue:** In the case of random r-disc graphs, Theorem 6 (Percolation of random r-disc graphs (Penrose, 2003)) Let Gdisc(n, r) be a random r-disc graph in ...
- **p. 8 / 1 Introduction - extractive body cue:** Then, almost surely, lim n→∞ Nmax(Gdisc(n, rn)) n = 0, if rn < (λc/n)1/d , and lim n→∞ Nmax(Gdisc(n, r)) n > 0, if rn ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational ... | p. 35 (6 Conclusion) |
| body limitation/failure cue | Figure 1: An illustration of the δ-interior of Xfree. The obstacle region Xobs is shown in dark grey and the δ-interior of Xfree is ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | First, each algorithm is analyzed in terms of the number of calls to the CollisionFree procedure. | p. 29 (V RRT∗) |
| body limitation/failure cue | Number of calls to the CollisionFree procedure Let MALG n denote the total number of calls to the CollisionFree procedure by algorithm ALG in ... | p. 29 (V RRT∗) |
| body limitation/failure cue | The next lemma upper-bounds the number of calls to the CollisionFree procedure in the proposed algorithms. | p. 30 (V RRT∗) |
| body limitation/failure cue | Let A denote the event that the sample Xn drawn at the last iteration falls into the rn interior of Xfree. | p. 30 (V RRT∗) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All algorithms were implemented in C and run on a computer with 2.66 GHz processor and 4GB RAM running the Linux operating system. | p. 33 (V RRT∗) |
| Moreover, this problem is relevant to other disciplines such as verification, computational biology, and computer animation (Latombe, 1999; Bhatia and Frazzoli, 2004; Branicky et ... | p. 1 (1 Introduction) |
| The incremental nature of these algorithms avoids the necessity to set the number of samples a priori, and returns a solution as soon as ... | p. 3 (1 Introduction) |
| For example, in many field implementations of sampling-based planning algorithms (see, e.g., Kuwata et al., 2009), it is often the case that since a ... | p. 3 (1 Introduction) |
| They showed that each run of the algorithm results in a path with smaller cost, even though the procedure is not guaranteed to converge ... | p. 4 (1 Introduction) |
| In particular, they were extended to run in an anytime fashion (Likhachev et al., 2004, 2008), deal with dynamic environments (Stentz, 1995; Likhachev et ... | p. 4 (1 Introduction) |
| More precisely, the algorithm is analyzed when it is run with Poisson(n) samples. | p. 25 (V RRT∗) |
| For n ∈N and m ∈{1, 2, . . . , Mn}, consider the tile m when the algorithm is run with Poisson(n) samples. | p. 25 (V RRT∗) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 35 / 6 Conclusion - extractive body cue:** In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 1: An illustration of the δ-interior of Xfree. The obstacle region Xobs is shown in dark grey and the δ-interior of Xfree is shown ...
- **p. 29 / V RRT∗ - extractive body cue:** First, each algorithm is analyzed in terms of the number of calls to the CollisionFree procedure.
- **p. 29 / V RRT∗ - extractive body cue:** Number of calls to the CollisionFree procedure Let MALG n denote the total number of calls to the CollisionFree procedure by algorithm ALG in iteration ...
- **p. 30 / V RRT∗ - extractive body cue:** The next lemma upper-bounds the number of calls to the CollisionFree procedure in the proposed algorithms.
- **p. 30 / V RRT∗ - extractive body cue:** Let A denote the event that the sample Xn drawn at the last iteration falls into the rn interior of Xfree.

- **Evidence anchors reviewed:** datasets p. 31 (V RRT∗), p. 25 (V RRT∗), p. 29 (V RRT∗), p. 31 (V RRT∗), p. 32 (V RRT∗), p. 33 (V RRT∗), metrics p. 61 (Figure/Table caption), p. 17 (Figure/Table caption), p. 33 (V RRT∗), p. 34 (V RRT∗), p. 21 (Figure/Table caption), p. 25 (V RRT∗), baselines p. 29 (V RRT∗), p. 32 (V RRT∗), p. 33 (V RRT∗), p. 34 (V RRT∗), p. 42 (Figure/Table caption), p. 43 (Figure/Table caption), results p. 31 (V RRT∗), p. 33 (V RRT∗), p. 33 (V RRT∗), p. 34 (V RRT∗), p. 5 (Figure/Table caption), p. 29 (V RRT∗).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
