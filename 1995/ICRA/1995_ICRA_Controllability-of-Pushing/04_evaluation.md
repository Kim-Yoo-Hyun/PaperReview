# Evaluation - Controllability of Pushing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.cmu.edu/afs/cs/Web/People/mlab/stable/papers.html; PDF retrieval source: https://www.ri.cmu.edu/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (C H can be followed)): Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact.

## Evaluation Body Digest

- **p. 3 / X. The Lie algebra - extractive PDF cue:** A car-like mobile robot can drive both forward and backward, and this symmetry, coupled with small-time accessibility, implies small-time local controllability.
- **p. 3 / X. The Lie algebra - extractive PDF cue:** Then the slider can be rotated to the desired goal configuration.  Proposition 1 is a straightforward generalization of a result due to Barraquand and ...
- **p. 7 / C H can be followed - extractive PDF cue:** Our planner is adapted from Barraquand and Latombe's path planner for nonholonomicmobile robots [5].
- **p. 4 / C H can be followed - extractive PDF cue:** 3 Mechanics and controllability of pushing In this section we study the problem of determining the motion of a pushed object.
- **p. 4 / C H can be followed - extractive PDF cue:** Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact.
- **p. 5 / C H can be followed - extractive PDF cue:** If the object is small-time locally controllable, however, it can followany path arbitrarilyclosely.
- **p. 5 / C H can be followed - extractive PDF cue:** 3.1.2 Solving for the motion of a pushed object Each contact point between the pusher and the slider may be sticking, breaking free, or sliding ...
- **p. 6 / C H can be followed - extractive PDF cue:** If the contact is frictionless, however, the object cannot be rotated.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| C H can be followed | SYSTEM / EVALUATION SCOPE UNRESOLVED | Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact. | p. 4 (C H can be followed) |

## Dataset / Benchmark Role

- **p. 3 / X. The Lie algebra - extractive PDF cue:** A car-like mobile robot can drive both forward and backward, and this symmetry, coupled with small-time accessibility, implies small-time local controllability.
- **p. 3 / X. The Lie algebra - extractive PDF cue:** Then the slider can be rotated to the desired goal configuration.  Proposition 1 is a straightforward generalization of a result due to Barraquand and ...
- **p. 7 / C H can be followed - extractive PDF cue:** Our planner is adapted from Barraquand and Latombe's path planner for nonholonomicmobile robots [5].
- **p. 4 / C H can be followed - extractive PDF cue:** 3 Mechanics and controllability of pushing In this section we study the problem of determining the motion of a pushed object.
- **p. 4 / C H can be followed - extractive PDF cue:** Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact.
- **p. 5 / C H can be followed - extractive PDF cue:** If the object is small-time locally controllable, however, it can followany path arbitrarilyclosely.
- **p. 5 / C H can be followed - extractive PDF cue:** 3.1.2 Solving for the motion of a pushed object Each contact point between the pusher and the slider may be sticking, breaking free, or sliding ...
- **p. 6 / C H can be followed - extractive PDF cue:** If the contact is frictionless, however, the object cannot be rotated.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The world frame F W and the slider frame F S.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure2: Theconvexhullofthreevelocitydirectionsin the rotation center space and on the velocity sphere. the frictional force can act in any tangential direction with any magnitude less than ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Examples of rotation center sets that yield small-time local controllability: (a) three rotation centers positively spanning a great circle of the velocity sphere; ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Limit surface mapping of a force to a velocity direction. If the support friction distribution s(x) becomes infinite at anypoint,however, the mappingis nolongerone-to-one. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5: (a) The forces that the pusher can apply to the slider during sticking contact are represented by the two friction cones. (b) The ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6: Examples of line contact. with contact normals perpendicular to the line (Figure 6). We also assume that the coefficient of friction at all ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7: Procedure STABLE. 3.3.2 Controllabilityby stable pushing with line contact If the composite friction cone F from the line pushing contact contains a pure ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 8: The slider of Figure 7 is small-time locally controllable by stable pushing at two edges. The friction coefficient is 0.5. (zero moment about ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | A car-like mobile robot can drive both forward and backward, and this symmetry, coupled with small-time accessibility, implies small-time local controllability. | embodiment, simulator version and control stack | p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra) |
| Task/environment | Then the slider can be rotated to the desired goal configuration.  Proposition 1 is a straightforward generalization of a result due to Barraquand ... | reset, timeout, object/scene variation | p. 3 (X. The Lie algebra), p. 7 (C H can be followed) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 4 (C H can be followed), p. 5 (C H can be followed) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| To see this is sufficient, recall that two nonopposite velocity directions that are not both translationsare sufficient forsmall-timeaccessibility. | definition/direction/unit from same section | p. 4 (C H can be followed) |
| A slider that is controllable by pushing may have to be pushed a long distance to reach nearby configurations. | definition/direction/unit from same section | p. 5 (C H can be followed) |
| In orderto find conditions for small-time local controllability of a slider, first recall that the set of available pushing contacts is given by  , ... | definition/direction/unit from same section | p. 5 (C H can be followed) |
| Proof: The center of friction only lies on a vertex of the convex hullif the supportfrictiondistribution s(x) integrates to zero everywhere else. | definition/direction/unit from same section | p. 7 (C H can be followed) |
| The other is a distance r2 =p from the center of friction and on the opposite side from the endpoint, where p is the ... | definition/direction/unit from same section | p. 7 (C H can be followed) |

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
| At least one of the force directions has nonzero moment, so at least one of the velocity directions has a nonzero angular component. | component/input/data sensitivity | p. 5 (C H can be followed) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity | Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact. | PDF body cue; verify exact table/figure and matched conditions | p. 4 (C H can be followed) |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- **p. 3 / X. The Lie algebra - extractive PDF cue:** 2.3 Controllability of the pushing control system If n = 1 for the control system , then the slider is confined to a one-dimensional integral ...
- **p. 3 / X. The Lie algebra - extractive PDF cue:** If n = 2, the Lie algebra L(X ) is spanned by X1, X2, and X3 = [X1 ; X2 ].
- **p. 3 / X. The Lie algebra - extractive PDF cue:** 2.3 Controllability of the pushing control system If n = 1 for the control system , then the slider is confined to a one-dimensional integral ...
- **p. 3 / X. The Lie algebra - extractive PDF cue:** If n = 2, the Lie algebra L(X ) is spanned by X1, X2, and X3 = [X1 ; X2 ].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | If condition (1) holds, the slider cannot rotate. | p. 3 (X. The Lie algebra) |
| body limitation/failure cue | The slider cannot be rotated (unless its limit surface contains vertices). | p. 5 (C H can be followed) |
| body limitation/failure cue | If V k ;i \ V f ;i = ;, contact mode i cannot occur; otherwise, contact mode i is feasible and any of ... | p. 5 (C H can be followed) |
| body limitation/failure cue | If the contact is frictionless, however, the object cannot be rotated. | p. 6 (C H can be followed) |
| body limitation/failure cue | In fact, with no information about the support friction distribution s(x) other than the center of friction, no velocity direction is guaranteed to be ... | p. 6 (C H can be followed) |
| body limitation/failure cue | Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / X. The Lie algebra - extractive PDF cue:** If condition (1) holds, the slider cannot rotate.
- **p. 5 / C H can be followed - extractive PDF cue:** The slider cannot be rotated (unless its limit surface contains vertices).
- **p. 5 / C H can be followed - extractive PDF cue:** If V k ;i \ V f ;i = ;, contact mode i cannot occur; otherwise, contact mode i is feasible and any of the ...
- **p. 6 / C H can be followed - extractive PDF cue:** If the contact is frictionless, however, the object cannot be rotated.
- **p. 6 / C H can be followed - extractive PDF cue:** In fact, with no information about the support friction distribution s(x) other than the center of friction, no velocity direction is guaranteed to be in ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition 2, ...

- **PDF anchors reviewed:** datasets p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra), p. 7 (C H can be followed), p. 4 (C H can be followed), p. 4 (C H can be followed), p. 5 (C H can be followed), metrics p. 8 (Figure/Table caption), p. 4 (C H can be followed), p. 5 (C H can be followed), p. 5 (C H can be followed), p. 7 (C H can be followed), p. 7 (C H can be followed), baselines 본문 anchor 없음, results p. 4 (C H can be followed).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
