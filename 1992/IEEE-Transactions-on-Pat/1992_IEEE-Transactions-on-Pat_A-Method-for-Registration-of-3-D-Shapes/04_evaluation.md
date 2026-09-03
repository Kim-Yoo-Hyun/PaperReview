# Evaluation - A Method for Registration of 3-D Shapes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://doi.org/10.1109/34.121791; PDF retrieval source: https://doi.org/10.1109/34.121791. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (A. Point Ser Matching), p. 14 (A BN), p. 15 (A BN), p. 16 (A BN), p. 16 (A BN), p. 6 (B. Convergence Theorem)): translations to achieve local matching.

## Evaluation Body Digest

- **p. 10 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Any quoted approximate times are given for execution ona single-processor computer rated at 1.6 ‘flops on the 100 x 100 double-precision Linpack benchmark,
- **p. 14 / A BN - extractive body cue:** The registration process for these larger datasets took about 1 hr.
- **p. 6 / B. Convergence Theorem - extractive body cue:** Theorem: ‘The iterative closes point algorithm always converges monotonically toa local minimum with respect to the smean-square distance objective funetion.
- **p. 8 / B. Convergence Theorem - extractive body cue:** Unfortunately ifthe objective function evaluator changes the ‘values inthe state vector duting the optimization iteration, this
- **p. 8 / B. Convergence Theorem - extractive body cue:** For any given nonpathological shape X that represents a realworld surface or object (es pathological shape descriptions based on sin(1/z) near 2er0 not allowed) and ...
- **p. 9 / A. Initial States for Global Matching - extractive body cue:** The exact value of could be computed for any given class of object shapes via exhaustive testing if tha is desired.
- **p. 9 / A. Initial States for Global Matching - extractive body cue:** Aga, the exact value of a could be computed for any given set of objects and any given level of sensor noise via exhaustive testing ...
- **p. 10 / A. Initial States for Global Matching - extractive body cue:** The general rule of thumb is the more complicated the ‘object, the more initial states required.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** VI. EXPERIMENTAL RESULTS (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| A. Point Ser Matching | SYSTEM / EVALUATION SCOPE UNRESOLVED | translations to achieve local matching. | p. 11 (A. Point Ser Matching) |
| A BN | SYSTEM / EVALUATION SCOPE UNRESOLVED | 17, The registration algorithm locked in on the solution and gave a slightly improved rms distance in less time than the full data set | p. 14 (A BN) |
| A BN | SYSTEM / EVALUATION SCOPE UNRESOLVED | The accelerated ICP algorithm converges to a local mini ‘mum quickly in comparison with generic nonlinear optimization methods, It is fast enough that global ... | p. 15 (A BN) |
| A BN | SYSTEM / EVALUATION SCOPE UNRESOLVED | Local matching is achieved at predictable cost based | p. 16 (A BN) |
| A BN | SYSTEM / EVALUATION SCOPE UNRESOLVED | + The accelerated ICP algorithm can achieve Newton-type {quadratic convergence steps at less cost than « numerical steepest descent step. | p. 16 (A BN) |

## Dataset / Benchmark Role

- **p. 10 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Any quoted approximate times are given for execution ona single-processor computer rated at 1.6 ‘flops on the 100 x 100 double-precision Linpack benchmark,
- **p. 14 / A BN - extractive body cue:** The registration process for these larger datasets took about 1 hr.
- **p. 6 / B. Convergence Theorem - extractive body cue:** Theorem: ‘The iterative closes point algorithm always converges monotonically toa local minimum with respect to the smean-square distance objective funetion.
- **p. 8 / B. Convergence Theorem - extractive body cue:** Unfortunately ifthe objective function evaluator changes the ‘values inthe state vector duting the optimization iteration, this
- **p. 8 / B. Convergence Theorem - extractive body cue:** For any given nonpathological shape X that represents a realworld surface or object (es pathological shape descriptions based on sin(1/z) near 2er0 not allowed) and ...
- **p. 9 / A. Initial States for Global Matching - extractive body cue:** The exact value of could be computed for any given class of object shapes via exhaustive testing if tha is desired.
- **p. 9 / A. Initial States for Global Matching - extractive body cue:** Aga, the exact value of a could be computed for any given set of objects and any given level of sensor noise via exhaustive testing ...
- **p. 10 / A. Initial States for Global Matching - extractive body cue:** The general rule of thumb is the more complicated the ‘object, the more initial states required.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 9. Noiy point stand srtace patch ferritin
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 12. This data will serve asthe model surface description with $442 triangles (4221 quadrilateral polygons). A thinned
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 15. Surface puch hounds of et of parametric surfaces: 97 cubic Becerpches

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Any quoted approximate times are given for execution ona single-processor computer rated at 1.6 ‘flops on the 100 x 100 double-precision Linpack benchmark, | embodiment, simulator version and control stack | p. 10 (VI. EXPERIMENTAL RESULTS), p. 14 (A BN) |
| Task/environment | The registration process for these larger datasets took about 1 hr. | reset, timeout, object/scene variation | p. 14 (A BN), p. 6 (B. Convergence Theorem) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1) Point sets), p. 1 (1) Point sets) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1) Point sets), p. 2 (1) Point sets) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 4d, Terminate the iteration when the change in meansquare error falls below a preset threshold > > 0 specifying the desired precision ofthe registration: ... | definition/direction/unit from same section | p. 6 (B. Point to Implicit Entity Distance) |
| To give a quantitative example comparison, the registration values, RMS error, maximum error, angular change, and cu ‘mulative are length values were recorded during ... | definition/direction/unit from same section | p. 7 (B. Convergence Theorem) |
| errors as indicated by the performance of the registration, | definition/direction/unit from same section | p. 16 (A BN) |
| Any quoted approximate times are given for execution ona single-processor computer rated at 1.6 ‘flops on the 100 x 100 double-precision Linpack benchmark, | definition/direction/unit from same section | p. 10 (VI. EXPERIMENTAL RESULTS) |
| The mean squared error ex of that correspondence is given by | definition/direction/unit from same section | p. 6 (B. Convergence Theorem) |
| To be rigorous, one can simply ignore the suggested update if it causes a worse mean square error. | definition/direction/unit from same section | p. 7 (B. Convergence Theorem) |
| No expensive closest point evaluations are spent ‘on egistration vectors that have worse mean square errors than ‘the current state, Because ofthe ICP convergence ... | definition/direction/unit from same section | p. 8 (B. Convergence Theorem) |
| By using a sufficiently dense uniform sampling of quater- ‘ions on the unit sphere combined with a sufficiently dense sampling of translation vectors occupying ... | definition/direction/unit from same section | p. 9 (B. Convergence Theorem) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The 3 range of 0.6 units is clearly visible compared withthe size ofthe object. | comparison identity and matched condition | p. 11 (B. Curve Matching) |
| The computation reduction ratio of the ICP algorithm compared with brute-force testing for this simple case is 462:1. | comparison identity and matched condition | p. 11 (A. Point Ser Matching) |
| To give a quantitative example comparison, the registration values, RMS error, maximum error, angular change, and cu ‘mulative are length values were recorded during ... | comparison identity and matched condition | p. 7 (B. Convergence Theorem) |
| In this section, we demonstrate the ability of the ICP algorithm to perform local point set matching without correspondence. | comparison identity and matched condition | p. 10 (A. Point Ser Matching) |
| The accelerated ICP algorithm converges to a local mini ‘mum quickly in comparison with generic nonlinear optimization methods, It is fast enough that global ... | comparison identity and matched condition | p. 15 (A BN) |
| This is important for using CAD data in its native form without elaborate user-guided reprocessing. | comparison identity and matched condition | p. 16 (A BN) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In this section, we demonstrate the ability of the ICP algorithm to perform local point set matching without correspondence. | component/input/data sensitivity | p. 10 (A. Point Ser Matching) |
| Compared with basic point st matching, which requires the same numberof points listed in direc cortespondence, we are essentially trading off additional CPU time ... | component/input/data sensitivity | p. 11 (A. Point Ser Matching) |
| This is important for using CAD data in its native form without elaborate user-guided reprocessing. | component/input/data sensitivity | p. 16 (A BN) |
| large problems, even remote execution procedures and distributed file systems on networks of workstations can provide worthwhile speedup without significant overhead, | component/input/data sensitivity | p. 16 (A BN) |
| If a dimensionless threshold is desired, one can replace + with Vira), where the square root of the trace of the covaranee of the ... | component/input/data sensitivity | p. 6 (B. Point to Implicit Entity Distance) |
| "To be precise, consider a 6=D slate space 9, where the ‘quaternion component gy is determined from the oer quaterrion components: go = yt ... | component/input/data sensitivity | p. 8 (B. Convergence Theorem) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The SVD approach, based on the eross- ‘covariance matrix of two point distributions, does, however, ‘generalize easily ton dimensions and would be our method ... | translations to achieve local matching. | PDF body cue; verify exact table/figure and matched conditions | p. 11 (A. Point Ser Matching), p. 14 (A BN), p. 15 (A BN), p. 16 (A BN), p. 16 (A BN), p. 6 (B. Convergence Theorem) |
| Primary metric/result | 17, The registration algorithm locked in on the solution and gave a slightly improved rms distance in less time than the full data set | numeric claim only at cited anchor | p. 14 (A BN) |

- Numeric sentences retained from the body:
- **p. 7 / B. Convergence Theorem - extractive body cue:** Any optimization method that does not use explicit vector gradient estimates, such 8s Powell's direction set method, the Nelder-Mead downhill simplex method, of simulated annealling, ...
- **p. 9 / B. Convergence Theorem - extractive body cue:** Such methods can be very memory intensive; a 20x 20> 20 x 20 x 20 x 20 hypercubic-hypervoxel ‘rid of the smallest hypercylinder containing all ...
- **p. 10 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Any quoted approximate times are given for execution ona single-processor computer rated at 1.6 ‘flops on the 100 x 100 double-precision Linpack benchmark,
- **p. 10 / A. Point Ser Matching - extractive body cue:** 5 shows the two point sets after regisiration by the ICP algorithm aftr six iterations, Which took less than 1s.
- **p. 11 / A. Point Ser Matching - extractive body cue:** In the African mask example in the surface section below, we accurately registered a point set with Nj=2500 points 10 a point set with V-=4200 ...
- **p. 11 / B. Curve Matching - extractive body cue:** The rotated and translated curve was converted to a polyline description ‘with 64 points.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This is a problem with almost all of the shape ‘matching algorithms in the literature For any given fixed initial set of rotations, the ... | p. 16 (A BN) |
| body limitation/failure cue | ‘would yield a smaller mean square error than the least squares registration, which cannot possibly be the case. | p. 6 (B. Convergence Theorem) |
| body limitation/failure cue | 4d, Terminate the iteration when the change in meansquare error falls below a preset threshold > > 0 specifying the desired precision ofthe registration: ... | p. 6 (B. Point to Implicit Entity Distance) |
| body limitation/failure cue | Note the smooth character ofall the curves. | p. 7 (B. Convergence Theorem) |
| body limitation/failure cue | The only way to be sure isto find the minimum ofall the local minima. | p. 8 (B. Convergence Theorem) |
| body limitation/failure cue | This is an interesting accomplishment for a function where derivatives cannot be evaluated. | p. 8 (B. Convergence Theorem) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Any quoted approximate times are given for execution ona single-processor computer rated at 1.6 ‘flops on the 100 x 100 double-precision Linpack benchmark, | p. 10 (VI. EXPERIMENTAL RESULTS) |
| From an implementation point of view, one has the option of using precomputed lists or nested loops. | p. 9 (A. Initial States for Global Matching) |
| form curves and surfaces as well as point sets were described in [3] in an attempt to formalize and unify the description of a ... | p. 1 (1. Istmopuction) |
| Manuscript recived October 3,199; revised May 6, 1994 ‘The ators ae withthe Computer Science Deparment, General Moors Research Laborato, Warren, MI S090 55, TEEE ... | p. 1 (1. Istmopuction) |
| His approach is based on a regular "zy-arid structure, and true 3-D point-to-surface distances are ‘not computed. | p. 2 (1) Point sets) |
| This work popularized the use of quaternions for least squares registration of corresponding 3-D point sets inthe computer vision community. ‘The alternative use of ... | p. 2 (1) Point sets) |
| For a parametic space curve C= (7(u)} one can compute a polyline L(C, 6) such thatthe Piecewise-lnear approximation never deviate from the space ture ... | p. 3 (A. Point to Parametric Entity Distance) |
| Similaty, for a purametic surface S = {Fu}, one can compute a tangle set T(S,8) such thatthe piecewisetriangular approximation never deviates from the surace ... | p. 3 (A. Point to Parametric Entity Distance) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / A BN - extractive body cue:** This is a problem with almost all of the shape ‘matching algorithms in the literature For any given fixed initial set of rotations, the global ...
- **p. 6 / B. Convergence Theorem - extractive body cue:** ‘would yield a smaller mean square error than the least squares registration, which cannot possibly be the case.
- **p. 6 / B. Point to Implicit Entity Distance - extractive body cue:** 4d, Terminate the iteration when the change in meansquare error falls below a preset threshold > > 0 specifying the desired precision ofthe registration: dem ...
- **p. 7 / B. Convergence Theorem - extractive body cue:** Note the smooth character ofall the curves.
- **p. 8 / B. Convergence Theorem - extractive body cue:** The only way to be sure isto find the minimum ofall the local minima.
- **p. 8 / B. Convergence Theorem - extractive body cue:** This is an interesting accomplishment for a function where derivatives cannot be evaluated.

- **Evidence anchors reviewed:** datasets p. 10 (VI. EXPERIMENTAL RESULTS), p. 14 (A BN), p. 6 (B. Convergence Theorem), p. 8 (B. Convergence Theorem), p. 8 (B. Convergence Theorem), p. 9 (A. Initial States for Global Matching), metrics p. 6 (B. Point to Implicit Entity Distance), p. 7 (B. Convergence Theorem), p. 16 (A BN), p. 10 (VI. EXPERIMENTAL RESULTS), p. 6 (B. Convergence Theorem), p. 7 (B. Convergence Theorem), baselines p. 11 (B. Curve Matching), p. 11 (A. Point Ser Matching), p. 7 (B. Convergence Theorem), p. 10 (A. Point Ser Matching), p. 15 (A BN), p. 16 (A BN), results p. 11 (A. Point Ser Matching), p. 14 (A BN), p. 15 (A BN), p. 16 (A BN), p. 16 (A BN), p. 6 (B. Convergence Theorem).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** To give a quantitative example comparison, the registration values, RMS error, maximum error, angular change, and cu ‘mulative are length values were recorded during 50 iterations of both the basic ... (p. 7, B. Convergence Theorem).
- **Metric evidence:** errors as indicated by the performance of the registration, (p. 16, A BN).
- **Baseline/ablation evidence:** To give a quantitative example comparison, the registration values, RMS error, maximum error, angular change, and cu ‘mulative are length values were recorded during 50 iterations of both the basic ... (p. 7, B. Convergence Theorem).
- **Failure/negative evidence:** allowable occlusion percentages, e-., 10% oles, We do not advocate our proposed method if feature extraction techniques will successfully solve the problem. ‘The generalization to matching deformable models with high ... (p. 16, A BN).
