# Evaluation - Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf; PDF retrieval source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (5 Experiments), p. 6 (5 Experiments)): For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage.

## Evaluation Body Digest

- **p. 5 / 5 Experiments - extractive body cue:** Instead we optimize the grasp pose (the relative object-hand pose), assuming that a compliant real-world gripper could perform the actual grasp.
- **p. 5 / 5 Experiments - extractive body cue:** The control costs penalized accelerations and implemented a weak prior for the robot arm to be in the homing posi1934
- **p. 6 / 5 Experiments - extractive body cue:** Further, the paths have 20 time steps per manipulation; for 25 objects this is a (15dimensional) trajectory with 1000 time steps across 50 manipulations.
- **p. 6 / 5 Experiments - extractive body cue:** But this demonstration shows that such problems can be solved also when the objective is given in terms of an objective function ψ(x(T)), and that ...
- **p. 5 / 5 Experiments - extractive body cue:** When blocks are placed on a board, we reward more central positionings.
- **p. 5 / 5 Experiments - extractive body cue:** For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage.
- **p. 6 / 5 Experiments - extractive body cue:** The resulting trajectories are smooth and collision free (if keyframe optimization indicated feasibility) and generate the optimized end state.
- **p. 6 / 5 Experiments - extractive body cue:** The example demonstrates success on our construction problems, leading to (locally, approximately) optimal full manipulation paths across up to 50 manipulations.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** 5 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. | p. 5 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The example demonstrates success on our construction problems, leading to (locally, approximately) optimal full manipulation paths across up to 50 manipulations. | p. 6 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 5 Experiments - extractive body cue:** Instead we optimize the grasp pose (the relative object-hand pose), assuming that a compliant real-world gripper could perform the actual grasp.
- **p. 5 / 5 Experiments - extractive body cue:** The control costs penalized accelerations and implemented a weak prior for the robot arm to be in the homing posi1934
- **p. 6 / 5 Experiments - extractive body cue:** Further, the paths have 20 time steps per manipulation; for 25 objects this is a (15dimensional) trajectory with 1000 time steps across 50 manipulations.
- **p. 6 / 5 Experiments - extractive body cue:** But this demonstration shows that such problems can be solved also when the objective is given in terms of an objective function ψ(x(T)), and that ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 1: Typical initial configuration. action sequences a1:K. We put substantial effort in efficiently computing the combinatorial set of all feasible actions (unifi- cations of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Samples of optimized end state configurations. Right: Snapshot of an optimized smooth full manipulation trajectory. tion throughout (implying a useful preference to reach ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Running times of (a) a single MCTS rollout and a single end space optimization and (b) a keyframe optimiza- tion and full path ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Instead we optimize the grasp pose (the relative object-hand pose), assuming that a compliant real-world gripper could perform the actual grasp. | embodiment, simulator version and control stack | p. 5 (5 Experiments), p. 5 (5 Experiments) |
| Task/environment | The control costs penalized accelerations and implemented a weak prior for the robot arm to be in the homing posi1934 | reset, timeout, object/scene variation | p. 5 (5 Experiments), p. 6 (5 Experiments) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 1 (Abstract) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| When blocks are placed on a board, we reward more central positionings. | definition/direction/unit from same section | p. 5 (5 Experiments) |
| For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. | definition/direction/unit from same section | p. 5 (5 Experiments) |
| The resulting trajectories are smooth and collision free (if keyframe optimization indicated feasibility) and generate the optimized end state. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| The example demonstrates success on our construction problems, leading to (locally, approximately) optimal full manipulation paths across up to 50 manipulations. | definition/direction/unit from same section | p. 6 (5 Experiments) |

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
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as ... | For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (5 Experiments), p. 6 (5 Experiments) |
| Primary metric/result | The example demonstrates success on our construction problems, leading to (locally, approximately) optimal full manipulation paths across up to 50 manipulations. | numeric claim only at cited anchor | p. 6 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiments - extractive body cue:** Even for up to 100 objects-implying up to 200 pick and place manipulations and hundreds of effective DoFs in the end configuration-optimization over the end ...
- **p. 6 / 5 Experiments - extractive body cue:** Further, the paths have 20 time steps per manipulation; for 25 objects this is a (15dimensional) trajectory with 1000 time steps across 50 manipulations.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Further constraints concern standard motion optimization aspects such as collision avoidance. | p. 5 (2 Related Work) |
| body limitation/failure cue | The geometric and differential constraints hpath, gpath implement zero velocity of the object-hand pose while inhand, zero velocities and accelerations during pick and place, ... | p. 5 (5 Experiments) |
| body limitation/failure cue | The resulting trajectories are smooth and collision free (if keyframe optimization indicated feasibility) and generate the optimized end state. | p. 6 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| There is no doubt that existing TAMP approaches could solve an analogous feasibility problem if the objective was instead encoded in a symbolic way. | p. 6 (5 Experiments) |
| Further, the paths have 20 time steps per manipulation; for 25 objects this is a (15dimensional) trajectory with 1000 time steps across 50 manipulations. | p. 6 (5 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 2 Related Work - extractive body cue:** Further constraints concern standard motion optimization aspects such as collision avoidance.
- **p. 5 / 5 Experiments - extractive body cue:** The geometric and differential constraints hpath, gpath implement zero velocity of the object-hand pose while inhand, zero velocities and accelerations during pick and place, and ...
- **p. 6 / 5 Experiments - extractive body cue:** The resulting trajectories are smooth and collision free (if keyframe optimization indicated feasibility) and generate the optimized end state.

- **Evidence anchors reviewed:** datasets p. 5 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), metrics p. 5 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), baselines 본문 anchor 없음, results p. 5 (5 Experiments), p. 6 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. (p. 5, 5 Experiments).
- **Metric evidence:** When blocks are placed on a board, we reward more central positionings. (p. 5, 5 Experiments).
- **Baseline/ablation evidence:** For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. (p. 5, 5 Experiments).
- **Failure/negative evidence:** We did not consider articulated fingers and optimize over finger motions for grasping as this is unrealistic to transfer to real-world. (p. 5, 5 Experiments).
