# Evaluation - Hierarchical Task and Motion Planning in the Now

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980391; PDF retrieval source: https://doi.org/10.1109/ICRA.2011.5980391. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (B C), p. 6 (C C), p. 6 (C C), p. 7 (VI. CORRECTNESS), p. 2 (III. EXAMPLE), p. 5 (C C)): Note that executing the operator for removing c from the swept volume of a requires no further planning or execution, as the condition it was intended to establish has already ...

## Evaluation Body Digest

- **p. 2 / III. EXAMPLE - extractive PDF cue:** The first requires that a swept volume of the robot moving to object a and picking it up be free.
- **p. 2 / III. EXAMPLE - extractive PDF cue:** The swept volume is shown in figure 3.1 as a complex brown polygon; it was computed using a fast planner that considered only translations of ...
- **p. 3 / B C - extractive PDF cue:** Washing domain, in which the robot must move object A to the washing area, wash it, and put it in the storage area. tree we ...
- **p. 3 / IV. REPRESENTATION - extractive PDF cue:** The fluents used to characterize the washing example are: • In(O, R): has value True if object O is entirely contained in region R, otherwise ...
- **p. 5 / C C - extractive PDF cue:** The pick operation results in the robot holding object O: Holding() = O: define: Ts = {T : ClearX (T, X) ∈goal ∧O̸ ∈X} exists: ...
- **p. 5 / C C - extractive PDF cue:** In our implementation, the world state is represented by a configuration of the robot and a set of objects, each of which has attributes including ...
- **p. 6 / C C - extractive PDF cue:** To guarantee that the robot can move to the object at that location and pick it up, we find a path from the robot's home ...
- **p. 6 / C C - extractive PDF cue:** Note that the taboo regions are only taboos for placing objects: they must be kept free, but the robot may take paths that move through ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** VII. EMPIRICAL RESULTS (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B C | SYSTEM / EVALUATION SCOPE UNRESOLVED | Note that executing the operator for removing c from the swept volume of a requires no further planning or execution, as the condition it ... | p. 3 (B C) |
| C C | SYSTEM / EVALUATION SCOPE UNRESOLVED | In this case, the planner will achieve p1, ...., pn in whatever way it can, and then execute o and r will be achieved; ... | p. 6 (C C) |
| C C | SYSTEM / EVALUATION SCOPE UNRESOLVED | For example, if it is important that the object not be regrasped as part of the Place operation, it is possible to 'expose' the ... | p. 6 (C C) |
| VI. CORRECTNESS | SYSTEM / EVALUATION SCOPE UNRESOLVED | So, we need to examine the effects of hierarchy and of operating in infinite domains on the ability of HPN to achieve feasible goals. | p. 7 (VI. CORRECTNESS) |
| III. EXAMPLE | SYSTEM / EVALUATION SCOPE UNRESOLVED | The primitive operation is executed in the world, which results in the robot grasping c. | p. 2 (III. EXAMPLE) |

## Dataset / Benchmark Role

- **p. 2 / III. EXAMPLE - extractive PDF cue:** The first requires that a swept volume of the robot moving to object a and picking it up be free.
- **p. 2 / III. EXAMPLE - extractive PDF cue:** The swept volume is shown in figure 3.1 as a complex brown polygon; it was computed using a fast planner that considered only translations of ...
- **p. 3 / B C - extractive PDF cue:** Washing domain, in which the robot must move object A to the washing area, wash it, and put it in the storage area. tree we ...
- **p. 3 / IV. REPRESENTATION - extractive PDF cue:** The fluents used to characterize the washing example are: • In(O, R): has value True if object O is entirely contained in region R, otherwise ...
- **p. 5 / C C - extractive PDF cue:** The pick operation results in the robot holding object O: Holding() = O: define: Ts = {T : ClearX (T, X) ∈goal ∧O̸ ∈X} exists: ...
- **p. 5 / C C - extractive PDF cue:** In our implementation, the world state is represented by a configuration of the robot and a set of objects, each of which has attributes including ...
- **p. 6 / C C - extractive PDF cue:** To guarantee that the robot can move to the object at that location and pick it up, we find a path from the robot's home ...
- **p. 6 / C C - extractive PDF cue:** Note that the taboo regions are only taboos for placing objects: they must be kept free, but the robot may take paths that move through ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 1. Washing domain, in which the robot must move object A to the washing area, wash it, and put it in the storage area. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2. Planning and execution tree for washing and putting away an object. A B A A B B
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3. Suggestions for swept paths and parking locations. The region sweptb is clear in the starting state, so it never appears in the planning ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The first requires that a swept volume of the robot moving to object a and picking it up be free. | embodiment, simulator version and control stack | p. 2 (III. EXAMPLE), p. 2 (III. EXAMPLE) |
| Task/environment | The swept volume is shown in figure 3.1 as a complex brown polygon; it was computed using a fast planner that considered only translations ... | reset, timeout, object/scene variation | p. 2 (III. EXAMPLE), p. 3 (B C) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To operate in infinite domains, we augment the standard operator descriptions with the following features: Suggesters, which are procedures that map current start and ... | definition/direction/unit from same section | p. 5 (C C) |
| It returns the union of the swept volumes of the base, the gripper, and the object. | definition/direction/unit from same section | p. 2 (III. EXAMPLE) |
| Procedural operator definitions, which map variable bindings into lists of preconditions, side effects, new bindings, and costs. | definition/direction/unit from same section | p. 5 (C C) |
| Because these variables both have infinite domains in our setting, we cannot enumerate them. | definition/direction/unit from same section | p. 6 (C C) |
| A standard symbolic planner enumerates all possible values of free variables, and then rules out instantiations later if they conflict with other aspects of ... | definition/direction/unit from same section | p. 6 (C C) |
| In the examples in this paper, it was constrained to do translation only and to return a single path. | definition/direction/unit from same section | p. 7 (V. ALGORITHMS) |
| The implementation generates poses in the region and discard those that fail that grasping accessibility tests. | definition/direction/unit from same section | p. 7 (V. ALGORITHMS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| First, it may not be possible to make pn true without undoing p1, . . . , pn-1. | comparison identity and matched condition | p. 6 (C C) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In goal regression, when applying an operation to a goal g, the goal fluent and any side effect fluents are always removed from g; ... | component/input/data sensitivity | p. 5 (C C) |
| Because our cost model is still somewhat weak, it chooses to remove b first. | component/input/data sensitivity | p. 2 (III. EXAMPLE) |
| To remove b from the swept volume, a parking place, shown as PB in figure 3.1, is suggested. | component/input/data sensitivity | p. 2 (III. EXAMPLE) |
| First, it may not be possible to make pn true without undoing p1, . . . , pn-1. | component/input/data sensitivity | p. 6 (C C) |
| Note that executing the operator for removing c from the swept volume of a requires no further planning or execution, as the condition it ... | component/input/data sensitivity | p. 3 (B C) |
| There is one additional primitive that has no geometric component: Wash() simply causes the washing machine to be run, and any objects that are ... | component/input/data sensitivity | p. 5 (C C) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper we outline an approach to the integration of task planning and motion planning that has the following key properties: It is ... | Note that executing the operator for removing c from the swept volume of a requires no further planning or execution, as the condition it ... | PDF body cue; verify exact table/figure and matched conditions | p. 3 (B C), p. 6 (C C), p. 6 (C C), p. 7 (VI. CORRECTNESS), p. 2 (III. EXAMPLE), p. 5 (C C) |
| Primary metric/result | In this case, the planner will achieve p1, ...., pn in whatever way it can, and then execute o and r will be achieved; ... | numeric claim only at cited anchor | p. 6 (C C) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Because these variables both have infinite domains in our setting, we cannot enumerate them. | p. 6 (C C) |
| body limitation/failure cue | If at attempt at serializing operations at an abstract level fails, then the planning problem is | p. 6 (C C) |
| body limitation/failure cue | SuggestPoses(O, R, Taboos): finds a set of poses for O where it is completely inside region R, there is no collision with taboo regions, ... | p. 7 (V. ALGORITHMS) |
| body limitation/failure cue | SuggestParking(O, Taboos, start): find an "out of the way" location for O that does not overlap any of the regions in Taboos. | p. 7 (V. ALGORITHMS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At this point, a grasp location is selected and a robot motion planner (in this case, a simple RRT implementation) is called to plan ... | p. 2 (III. EXAMPLE) |
| The swept volume is shown in figure 3.1 as a complex brown polygon; it was computed using a fast planner that considered only translations ... | p. 2 (III. EXAMPLE) |
| The entails attachment of fluent φ computes whether φ logically entails another fluent φ′. | p. 5 (C C) |
| There is one additional primitive that has no geometric component: Wash() simply causes the washing machine to be run, and any objects that are ... | p. 5 (C C) |
| To model the inability of the plan at the abstract level to determine which particular realization of an abstract plan step will take place, ... | p. 6 (C C) |
| Our implementation uses an RRT-based planner. | p. 7 (V. ALGORITHMS) |
| In our implementation, absLevel is a dictionary, mapping ground fluents to numeric abstraction levels. | p. 7 (V. ALGORITHMS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / C C - extractive PDF cue:** Because these variables both have infinite domains in our setting, we cannot enumerate them.
- **p. 6 / C C - extractive PDF cue:** If at attempt at serializing operations at an abstract level fails, then the planning problem is
- **p. 7 / V. ALGORITHMS - extractive PDF cue:** SuggestPoses(O, R, Taboos): finds a set of poses for O where it is completely inside region R, there is no collision with taboo regions, and ...
- **p. 7 / V. ALGORITHMS - extractive PDF cue:** SuggestParking(O, Taboos, start): find an "out of the way" location for O that does not overlap any of the regions in Taboos.

- **PDF anchors reviewed:** datasets p. 2 (III. EXAMPLE), p. 2 (III. EXAMPLE), p. 3 (B C), p. 3 (IV. REPRESENTATION), p. 5 (C C), p. 5 (C C), metrics p. 5 (C C), p. 2 (III. EXAMPLE), p. 5 (C C), p. 6 (C C), p. 6 (C C), p. 7 (V. ALGORITHMS), baselines p. 6 (C C), results p. 3 (B C), p. 6 (C C), p. 6 (C C), p. 7 (VI. CORRECTNESS), p. 2 (III. EXAMPLE), p. 5 (C C).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
