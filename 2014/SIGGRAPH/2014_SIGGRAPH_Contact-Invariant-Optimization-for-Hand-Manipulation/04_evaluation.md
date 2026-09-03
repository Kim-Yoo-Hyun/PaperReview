# Evaluation - Contact-Invariant Optimization for Hand Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://homes.cs.washington.edu/~zoran/behavior-discovery.html; PDF retrieval source: https://homes.cs.washington.edu/~zoran/behavior-discovery.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5 Results), p. 6 (5 Results)): Because contacts can be made with the surfaces of other characters, the task is achieved by one character climbing on top of the other.

## Evaluation Body Digest

- **p. 6 / 5 Results - extractive body cue:** Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object.
- **p. 6 / 5 Results - extractive body cue:** For the task of moving the object above, multiple characters distribute the workload and cooperate to pass the object from one to the other.
- **p. 6 / 5 Results - extractive body cue:** The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, K., COROS, S., BEAUDOIN, P., AND VAN ...
- **p. 6 / 5 Results - extractive body cue:** Because contacts can be made with the surfaces of other characters, the task is achieved by one character climbing on top of the other.
- **p. 6 / 5 Results - extractive body cue:** Two characters also cooperate to achieve tasks impossible for one, such as ℓpos for one of the characters specifying a target location above character's height.
- **p. 6 / 5 Results - extractive body cue:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.
- **p. 6 / 5 Results - extractive body cue:** These limitations may be removed by using full-body inverse dynamics to calculate the character's joint torques, and penalizing the torques or some related quantity.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** 5 Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Because contacts can be made with the surfaces of other characters, the task is achieved by one character climbing on top of the other. | p. 6 (5 Results) |
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Two characters also cooperate to achieve tasks impossible for one, such as ℓpos for one of the characters specifying a target location above character's ... | p. 6 (5 Results) |

## Dataset / Benchmark Role

- **p. 6 / 5 Results - extractive body cue:** Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object.
- **p. 6 / 5 Results - extractive body cue:** For the task of moving the object above, multiple characters distribute the workload and cooperate to pass the object from one to the other.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: A selection of motions synthesized by our algorithm.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, K., COROS, S., BEAUDOIN, P., AND VAN ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object. | embodiment, simulator version and control stack | p. 6 (5 Results), p. 6 (5 Results) |
| Task/environment | For the task of moving the object above, multiple characters distribute the workload and cooperate to pass the object from one to the other. | reset, timeout, object/scene variation | p. 6 (5 Results) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology. | definition/direction/unit from same section | p. 6 (5 Results) |
| For the task of moving the object above, multiple characters distribute the workload and cooperate to pass the object from one to the other. | definition/direction/unit from same section | p. 6 (5 Results) |
| Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, K., COROS, S., BEAUDOIN, P., AND ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For example, animal trot pattern of contacts (moving front leg and opposite hind leg together) emerges for quadruped walking without explicitly being specified. | comparison identity and matched condition | p. 6 (5 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density. | component/input/data sensitivity | p. 6 (5 Results) |
| For example, animal trot pattern of contacts (moving front leg and opposite hind leg together) emerges for quadruped walking without explicitly being specified. | component/input/data sensitivity | p. 6 (5 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| At the core of our framework is the contact-invariant optimization (CIO) method we introduce here. | Because contacts can be made with the surfaces of other characters, the task is achieved by one character climbing on top of the other. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5 Results), p. 6 (5 Results) |
| Primary metric/result | Two characters also cooperate to achieve tasks impossible for one, such as ℓpos for one of the characters specifying a target location above character's ... | numeric claim only at cited anchor | p. 6 (5 Results) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density. | p. 6 (5 Results) |
| body limitation/failure cue | These limitations may be removed by using full-body inverse dynamics to calculate the character's joint torques, and penalizing the torques or some related quantity. | p. 6 (5 Results) |
| body limitation/failure cue | Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, K., COROS, S., BEAUDOIN, P., AND ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Exactly the same continuation scheme was successful in all of the diverse behaviors we studied, and so our method does not need behavior-specific adjustments. | p. 5 (2 Related Work) |
| body limitation/failure cue | The solution obtained at the end of each phase is perturbed with small zero-mean Gaussian noise (to break any symmetries) and used to initialize ... | p. 5 (2 Related Work) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| CR Categories: I.3.1 [Computer Graphics]: Three-Dimensional Graphics and Realism-Animation I.6.8 [Simulation and Modeling]: Types of Simulation-Animation Keywords: Physics-Based Animation, Control | p. 1 (Abstract) |
| Automated synthesis of complex human behaviors is one of the long-standing grand challenges in computer graphics, that would also have an impact on robotics, ... | p. 1 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5 Results - extractive body cue:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.
- **p. 6 / 5 Results - extractive body cue:** These limitations may be removed by using full-body inverse dynamics to calculate the character's joint torques, and penalizing the torques or some related quantity.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, K., COROS, S., BEAUDOIN, P., AND VAN ...
- **p. 5 / 2 Related Work - extractive body cue:** Exactly the same continuation scheme was successful in all of the diverse behaviors we studied, and so our method does not need behavior-specific adjustments.
- **p. 5 / 2 Related Work - extractive body cue:** The solution obtained at the end of each phase is perturbed with small zero-mean Gaussian noise (to break any symmetries) and used to initialize the ...

- **Evidence anchors reviewed:** datasets p. 6 (5 Results), p. 6 (5 Results), metrics p. 6 (5 Results), p. 6 (5 Results), p. 8 (Figure/Table caption), baselines p. 6 (5 Results), results p. 6 (5 Results), p. 6 (5 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object. (p. 6, 5 Results).
- **Metric evidence:** The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology. (p. 6, 5 Results).
- **Baseline/ablation evidence:** For example, animal trot pattern of contacts (moving front leg and opposite hind leg together) emerges for quadruped walking without explicitly being specified. (p. 6, 5 Results).
- **Failure/negative evidence:** Another simplification we make is to penalize any relative velocity at contacting end effectors (see (2)), which results in trajectories that do not have any noticeable slipping. (p. 6, 5 Results).
