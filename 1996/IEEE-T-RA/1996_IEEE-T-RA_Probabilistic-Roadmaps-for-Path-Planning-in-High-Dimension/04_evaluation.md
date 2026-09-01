# Evaluation - Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://kavrakilab.rice.edu/publications/kavraki-svestka1996probabilistic-roadmaps-for.html; PDF retrieval source: https://kavrakilab.org/publications/kavraki-svestka1996probabilistic-roadmaps-for.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 10 (Figure/Table caption)): For each such pair of times we report the success rate in answering the query (s, 9).

## Evaluation Body Digest

- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** Stil, the cases treated here are considerably easier than in the scenes of Section V, due 10, the relatively low number of dofs of the ...
- **p. 13 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** Ress with gee planer fr scenes of Fi 9 and 10. _oe ot, [aaa nae THF problems in several minutes, but itis silvery ficient in ...
- **p. 11 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** The customized implementation used in the previous section solves efficiently path planning problems involving planar articulated robots.
- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** "The experiments conducted with these two test scenes are similar to those in Section V.
- **p. 13 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** IEEE TRANSACTIONS ON ROBOTICS AND AUTOMATION, VOL.
- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** For each such pair of times we report the success rate in answering the query (s, 9).
- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** Unlike the ‘customized implementation, this implementation does not use any specific techniques for local path planning, collision ‘checking, or distance computation.
- **p. 11 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** In this section we demonstrate that the

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** VI. RESULTS WITH GENERAL IMPLEMENTATION (p. 11).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| VI. RESULTS WITH GENERAL IMPLEMENTATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | For each such pair of times we report the success rate in answering the query (s, 9). | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| VI. RESULTS WITH GENERAL IMPLEMENTATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | We present results obtained with two representative examples. | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| VI. RESULTS WITH GENERAL IMPLEMENTATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | 12 reports some experimental results obtained over many independently ‘constructed roadmaps, for different learning times. | p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 4. Results wih customized planner for scene of Fig. 2 (20 expansion) Pee. all / Sie of all chock for connection to roadinap ... | p. 10 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** Stil, the cases treated here are considerably easier than in the scenes of Section V, due 10, the relatively low number of dofs of the ...
- **p. 13 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** Ress with gee planer fr scenes of Fi 9 and 10. _oe ot, [aaa nae THF problems in several minutes, but itis silvery ficient in ...
- **p. 11 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** The customized implementation used in the previous section solves efficiently path planning problems involving planar articulated robots.
- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** "The experiments conducted with these two test scenes are similar to those in Section V.
- **p. 13 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** IEEE TRANSACTIONS ON ROBOTICS AND AUTOMATION, VOL.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 4. Results wih customized planner for scene of Fig. 2 (20 expansion) Pee. all / Sie of all chock for connection to roadinap see) ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7. Ress with customized planner for scene of Fig. 6 (with expanse,

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Stil, the cases treated here are considerably easier than in the scenes of Section V, due 10, the relatively low number of dofs of ... | embodiment, simulator version and control stack | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| Task/environment | Ress with gee planer fr scenes of Fi 9 and 10. _oe ot, [aaa nae THF problems in several minutes, but itis silvery ficient ... | reset, timeout, object/scene variation | p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 11 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 6 (B. The Query Phase), p. 1 (Front matter) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 1 (Abstract), p. 2 (1. IntRopuction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For each such pair of times we report the success rate in answering the query (s, 9). | definition/direction/unit from same section | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| Unlike the ‘customized implementation, this implementation does not use any specific techniques for local path planning, collision ‘checking, or distance computation. | definition/direction/unit from same section | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| In this section we demonstrate that the | definition/direction/unit from same section | p. 11 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| AS in Section V, we estimate the average number of collision checks needed during learning and the percentage of times that our planner succeeds ... | definition/direction/unit from same section | p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| no baseline sentence selected | not reported | verify comparison table |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 4. Results wih customized planner for scene of Fig. 2 (20 expansion) Pee. all / Sie of all chock for connection to roadinap ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| For each of these roadmaps we only consider its main connected component and we test whether the query with configurations (s,9) succeeds within 2.5 ... | component/input/data sensitivity | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| In other words, we test whether both s and g can be quickly connected to the main connected component of the roadmap with the ... | component/input/data sensitivity | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method emphasizes efficiency and is primarily developed for robots with many dofs which move in static ‘environments. | For each such pair of times we report the success rate in answering the query (s, 9). | PDF body cue; verify exact table/figure and matched conditions | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 10 (Figure/Table caption) |
| Primary metric/result | We present results obtained with two representative examples. | numeric claim only at cited anchor | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |

- Numeric sentences retained from the body:
- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** tte / te] cl ae ‘Suosaas Rate (RY (ove) / (ore) / (see) / checks / nodes // Cy_/ Cr / Cy / Cr / ...
- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** For each of these roadmaps we only consider its main connected component and we test whether the query with configurations (s,9) succeeds within 2.5 s.
- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** The query in scene I is solved in all 30 cases after having learned for 7.5 s.
- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** Learning for 5s though suffices to successfully answer the query in mote than 90% of the cases.
- **p. 6 / 6) N.- a set of candidate neighbors - extractive body cue:** Alternatively, rather than using the structure of R to identify difficult regions, we could define 1x(e) according to the behavior of the local planner.
- **p. 8 / IV. APPLICATION 10 PLANAR ARTICULATED ROBOTS - extractive body cue:** In any case, experiments show ‘that computing a 3-D bitmap with a size on the order of 128 x 128 x 18 takes a few ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Unlike the ‘customized implementation, this implementation does not use any specific techniques for local path planning, collision ‘checking, or distance computation. | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| body limitation/failure cue | The collision checker in [44] considers successive approximations of the objects and, its running time, on the average, does not depend much on the | p. 13 (VI. Coxctusion) |
| body limitation/failure cue | The actual number of collision checks for connecting C;,...,Cs of Fig. | p. 11 (IV. APPLICATION 10 PLANAR ARTICULATED ROBOTS) |
| body limitation/failure cue | (1); and collision checking is done analytically, using routines from the PLAGEO library [19]. | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| body limitation/failure cue | For more complicated ‘geometries, the use of an iterative collision checker, like the ‘one in {4}, will be advantageous. | p. 13 (VI. Coxctusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The customized implementation used in the previous section solves efficiently path planning problems involving planar articulated robots. | p. 11 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| general implementation of the planner still gives very good results for a variety of examples | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| ‘The planner considered here is essentially an implementation of the method described in Section IL. | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |
| Note also that, like most practical methods for many-dof robots (one exception is the method in (17), RPP is a oneshot method, ie, it ... | p. 3 (I. RELATION 70 Previous Work) |
| (On many workstations, this second operation can be done very quickly using rastersean hardware originally designed to efficiently display filled polygons on graphic terminals.) ... | p. 8 (IV. APPLICATION 10 PLANAR ARTICULATED ROBOTS) |
| Overall, we found the method quite easy to implement and run. | p. 1 (1. IntRopuction) |
| These paths are computed using a simple and fast local planner. | p. 1 (Abstract) |
| This planner has been used to compute paths of an 8-dof manipulator among vertical | p. 2 (I. RELATION 70 Previous Work) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** Unlike the ‘customized implementation, this implementation does not use any specific techniques for local path planning, collision ‘checking, or distance computation.
- **p. 13 / VI. Coxctusion - extractive body cue:** The collision checker in [44] considers successive approximations of the objects and, its running time, on the average, does not depend much on the
- **p. 11 / IV. APPLICATION 10 PLANAR ARTICULATED ROBOTS - extractive body cue:** The actual number of collision checks for connecting C;,...,Cs of Fig.
- **p. 12 / VI. RESULTS WITH GENERAL IMPLEMENTATION - extractive body cue:** (1); and collision checking is done analytically, using routines from the PLAGEO library [19].
- **p. 13 / VI. Coxctusion - extractive body cue:** For more complicated ‘geometries, the use of an iterative collision checker, like the ‘one in {4}, will be advantageous.

- **PDF anchors reviewed:** datasets p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 11 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION), metrics p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 11 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION), baselines 본문 anchor 없음, results p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 13 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
