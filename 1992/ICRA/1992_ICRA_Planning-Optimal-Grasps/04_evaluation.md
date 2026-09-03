# Evaluation - Planning Optimal Grasps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.1992.219918; PDF retrieval source: https://doi.org/10.1109/ROBOT.1992.219918. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (4.1 Representing Anger forces)): We therefore want to guarantee a level of performance as judged by the local quality measure over all possible wrenches, and this is the measure Q Notice that for a ...

## Evaluation Body Digest

- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Avoiding large forces minimizes the deformation of both the object and the jaws.
- **p. 2 / 2 Working hypotheses - extractive body cue:** Any force and torque on the object can be represented by a point in the wrench space.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given a grasp configuration (i.e. a set of point contacts on the object), Q is defined as follows: Q = minLQw W We take the ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine the actual wrench acting on the object ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** i=l j=1 and a i j >_ 0, Cy=1 Cy==, aj,j 5 1 the object can be expressed by: Similarly we have that the total ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object ...
- **p. 5 / 5.1 Two-jaw gripper grasping a polygonal object - extractive body cue:** Again let's start considering convex objects.
- **p. 5 / 4.3 Minimizing the maximum Anger force - extractive body cue:** In the following we will use the criterion for minimizing the total force exerted on the object.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1 Representing Anger forces | SYSTEM / EVALUATION SCOPE UNRESOLVED | We therefore want to guarantee a level of performance as judged by the local quality measure over all possible wrenches, and this is the ... | p. 3 (4.1 Representing Anger forces) |

## Dataset / Benchmark Role

- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Avoiding large forces minimizes the deformation of both the object and the jaws.
- **p. 2 / 2 Working hypotheses - extractive body cue:** Any force and torque on the object can be represented by a point in the wrench space.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given a grasp configuration (i.e. a set of point contacts on the object), Q is defined as follows: Q = minLQw W We take the ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine the actual wrench acting on the object ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** i=l j=1 and a i j >_ 0, Cy=1 Cy==, aj,j 5 1 the object can be expressed by: Similarly we have that the total ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object ...
- **p. 5 / 5.1 Two-jaw gripper grasping a polygonal object - extractive body cue:** Again let's start considering convex objects.
- **p. 5 / 4.3 Minimizing the maximum Anger force - extractive body cue:** In the following we will use the criterion for minimizing the total force exerted on the object.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 1: Graphic Evaluation of the Quality Criteria 5 An Example of Using the Quality Criteria In the next subsections, we will present an algo- ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Avoiding large forces minimizes the deformation of both the object and the jaws. | embodiment, simulator version and control stack | p. 2 (4 The Quality of Grasp), p. 2 (2 Working hypotheses) |
| Task/environment | Any force and torque on the object can be represented by a point in the wrench space. | reset, timeout, object/scene variation | p. 2 (2 Working hypotheses), p. 3 (4.1 Representing Anger forces) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 4 (4.3 Minimizing the maximum Anger force), p. 2 (2 Working hypotheses) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Without loss of generality, we choose llwll so that 11g11 = 1. | definition/direction/unit from same section | p. 3 (4.1 Representing Anger forces) |
| Then, Q is just the distance of the nearest point to the origin, from the origin itself. | definition/direction/unit from same section | p. 3 (4.1 Representing Anger forces) |
| The f i , j are the vectors that generate the friction cone. | definition/direction/unit from same section | p. 4 (4.3 Minimizing the maximum Anger force) |
| The quality measure (Q,) is the distance of the nearest facet of the convex hull, from the origin. | definition/direction/unit from same section | p. 4 (4.3 Minimizing the maximum Anger force) |
| 0 Compute the convex hull and determine the facet of minimum distance from the origin. | definition/direction/unit from same section | p. 5 (5.1 Two-jaw gripper grasping a polygonal object) |
| Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces. | comparison identity and matched condition | p. 2 (4 The Quality of Grasp) |
| Without loss of generality, we choose llwll so that 11g11 = 1. | comparison identity and matched condition | p. 3 (4.1 Representing Anger forces) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces. | component/input/data sensitivity | p. 2 (4 The Quality of Grasp) |
| Without loss of generality, we choose llwll so that 11g11 = 1. | component/input/data sensitivity | p. 3 (4.1 Representing Anger forces) |
| In general f i is given by a convex combination of forces along the extrema of the friction cone, whose normal component is ft. | component/input/data sensitivity | p. 2 (4.1 Representing Anger forces) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In section four, we introduce and discuss the quality criteria we are proposing. | We therefore want to guarantee a level of performance as judged by the local quality measure over all possible wrenches, and this is the ... | PDF body cue; verify exact table/figure and matched conditions | p. 3 (4.1 Representing Anger forces) |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine the actual wrench acting on the ... | p. 3 (4.1 Representing Anger forces) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our criteria can be calculated easily for a wide variety of gripper and part types, although the implementation so far has been for planar ... | p. 1 (1 Introduction) |
| Hence it is enough to compute the convex hull over the elements of that set. | p. 4 (4.3 Minimizing the maximum Anger force) |
| Again, the formula gives a way to compute WL, , by computing the convex hull over a finite set of points. | p. 4 (4.3 Minimizing the maximum Anger force) |
| 0 Compute the convex hull and determine the facet of minimum distance from the origin. | p. 5 (5.1 Two-jaw gripper grasping a polygonal object) |
| The number of possible configuration grows linearly as the number of edges of the polygons The planning algorithms can be summarized as follows: Given ... | p. 5 (5.1 Two-jaw gripper grasping a polygonal object) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine the actual wrench acting on the object ...

- **Evidence anchors reviewed:** datasets p. 2 (4 The Quality of Grasp), p. 2 (2 Working hypotheses), p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force), p. 4 (4.3 Minimizing the maximum Anger force), metrics p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force), p. 4 (4.3 Minimizing the maximum Anger force), p. 5 (5.1 Two-jaw gripper grasping a polygonal object), p. 6 (Figure/Table caption), baselines p. 2 (4 The Quality of Grasp), p. 3 (4.1 Representing Anger forces), results p. 3 (4.1 Representing Anger forces).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (6 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 1: Graphic Evaluation of the Quality Criteria 5 An Example of Using the Quality Criteria In the next subsections, we will present an algo- rithm that can evaluate the ... (p. 5, Figure/Table caption).
- **Metric evidence:** Then, Q is just the distance of the nearest point to the origin, from the origin itself. (p. 3, 4.1 Representing Anger forces).
- **Baseline/ablation evidence:** Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces. (p. 2, 4 The Quality of Grasp).
- **Failure/negative evidence:** In a force closure grasp, finger locations do not change to counter external forces. (p. 1, 2 Working hypotheses).
