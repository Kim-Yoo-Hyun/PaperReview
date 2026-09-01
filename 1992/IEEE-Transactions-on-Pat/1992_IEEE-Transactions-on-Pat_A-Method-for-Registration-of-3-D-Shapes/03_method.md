# Method - A Method for Registration of 3-D Shapes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://doi.org/10.1109/34.121791; PDF retrieval source: https://doi.org/10.1109/34.121791. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (1) Point sets), p. 8 (B. Convergence Theorem), p. 2 (1) Point sets), p. 2 (1) Point sets), p. 6 (B. Convergence Theorem), p. 7 (B. Convergence Theorem)): Then, the iterative closest point (ICP) algorithm is stated, and a theorem is proven concerning its monotonic convergence property.

## Method Body Digest

- **p. 1 / 1) Point sets - extractive body cue:** Then, the iterative closest point (ICP) algorithm is stated, and a theorem is proven concerning its monotonic convergence property.
- **p. 8 / B. Convergence Theorem - extractive body cue:** Unfortunately ifthe objective function evaluator changes the ‘values inthe state vector duting the optimization iteration, this
- **p. 2 / 1) Point sets - extractive body cue:** Then, a conventional steepest descent algorithm is used to rotate and translate the second data set so tat it minimizes the sum of the covariance-weighted ...
- **p. 2 / 1) Point sets - extractive body cue:** His method forms an attributed relational graph of fundamental surface regions for data and ‘model shapes and then performs graph matching using an inexact approach ...
- **p. 6 / B. Convergence Theorem - extractive body cue:** then there is good direction a registration state vectors: Gis de.
- **p. 7 / B. Convergence Theorem - extractive body cue:** The most important feature is that the cos( 68) plot indicates a consistent direction of updates forall but the first few iterations.
- **p. 1 / 1. Istmopuction - extractive body cue:** ‘The proposed shape registration algorithm can be used with the following representations of geometric data:
- **p. 2 / 1) Point sets - extractive body cue:** Horn and Harris [33] also addressed the problem of estimating the exact rigid-body motion of the observer given sequentially digitized range image frames of the ...

## Design Rationale

- **p. 4 / B. Point to Implicit Entity Distance - extractive body cue:** The SVD approach, based on the eross- ‘covariance matrix of two point distributions, does, however, ‘generalize easily ton dimensions and would be our method of ...
- **p. 2 / 1) Point sets - extractive body cue:** A recent conference proceedings [47] contains new contributions on this subject.
- **p. 2 / 1) Point sets - extractive body cue:** ‘Schwartz and Sharir [50] developed a solution to the freeform space curve matching problem without feature extraction in late 1985.

## Source Evidence Cues

- **p. 1 / 1) Point sets - extractive body cue:** Then, the iterative closest point (ICP) algorithm is stated, and a theorem is proven concerning its monotonic convergence property.
- **p. 8 / B. Convergence Theorem - extractive body cue:** Unfortunately ifthe objective function evaluator changes the ‘values inthe state vector duting the optimization iteration, this
- **p. 2 / 1) Point sets - extractive body cue:** Then, a conventional steepest descent algorithm is used to rotate and translate the second data set so tat it minimizes the sum of the covariance-weighted ...
- **p. 2 / 1) Point sets - extractive body cue:** His method forms an attributed relational graph of fundamental surface regions for data and ‘model shapes and then performs graph matching using an inexact approach ...
- **p. 6 / B. Convergence Theorem - extractive body cue:** then there is good direction a registration state vectors: Gis de.
- **p. 7 / B. Convergence Theorem - extractive body cue:** The most important feature is that the cos( 68) plot indicates a consistent direction of updates forall but the first few iterations.
- **p. 1 / 1. Istmopuction - extractive body cue:** ‘The proposed shape registration algorithm can be used with the following representations of geometric data:
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, the iterative closest point (ICP) algorithm is stated, and a theorem is proven concerning its monotonic convergence property. | p. 1 (1) Point sets), p. 8 (B. Convergence Theorem) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Unfortunately ifthe objective function evaluator changes the ‘values inthe state vector duting the optimization iteration, this | p. 8 (B. Convergence Theorem), p. 2 (1) Point sets) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Then, a conventional steepest descent algorithm is used to rotate and translate the second data set so tat it minimizes the sum ... | p. 2 (1) Point sets), p. 2 (1) Point sets) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1) Point sets - extractive body cue:** Horn and Harris [33] also addressed the problem of estimating the exact rigid-body motion of the observer given sequentially digitized range image frames of the ...
- **p. 3 / A. Point to Parametric Entity Distance - extractive body cue:** The sealar objective function to be minimized is
- **p. 4 / B. Point to Implicit Entity Distance - extractive body cue:** ‘4 quadratic objective function subject to a nonlinear constraint
- **p. 4 / B. Point to Implicit Entity Distance - extractive body cue:** To find the closest point on an implicit entity defined by Gl?) = 0 to a given point 7, one must solve a constrained optimization ...
- **p. 7 / B. Convergence Theorem - extractive body cue:** Any optimization method that does not use explicit vector gradient estimates, such 8s Powell's direction set method, the Nelder-Mead downhill simplex method, of simulated annealling, ...
- **p. 8 / B. Convergence Theorem - extractive body cue:** Unfortunately ifthe objective function evaluator changes the ‘values inthe state vector duting the optimization iteration, this
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (1) Point sets), p. 4 (B. Point to Implicit Entity Distance), p. 3 (A. Point to Parametric Entity Distance), p. 3 (A. Point to Parametric Entity Distance), p. 4 (A. Point to Parametric Entity Distance), p. 6 (B. Convergence Theorem).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | describe, registration, multiple, overlapping, range, images, without, distinctive, feature, extraction, Then, iterative, closest, point | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | describe, registration, multiple, overlapping, range, images, without, distinctive, feature, extraction | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | SVD, eross-, covariance, matrix, point, distributions, does, however, generalize, easily | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Horn, Harris, addressed, problem, estimating, exact, rigid-body, motion, observer, given | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1) Point sets - extractive body cue:** [36] also describe a method for the registration of multiple overlapping range images without distinctive feature extraction.
- **p. 1 / 1) Point sets - extractive body cue:** Then, the iterative closest point (ICP) algorithm is stated, and a theorem is proven concerning its monotonic convergence property.
- **p. 1 / 1) Point sets - extractive body cue:** The issue of the initial registration states is addressed next, Finally, experimental results for point sets, curves, and surfaces are presented 10 demonstrate the capabilities ...
- **p. 2 / 1) Point sets - extractive body cue:** This seems to be ‘reasonable approach but relies on extraction of derivativebased quantities.
- **p. 4 / A. Point to Parametric Entity Distance - extractive body cue:** 2 [EE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL.
- **p. 6 / B. Convergence Theorem - extractive body cue:** which defines a direction in the registration state space.
- **p. 6 / B. Convergence Theorem - extractive body cue:** then there is good direction a registration state vectors: Gis de.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Similarly, the removal of statistical outliers is considered a preprocessing step, is probably best implemented as such, and will also not be ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Given the set of points from one frame, he applies a smoothness assumption to create a smoothing spine approximation of the | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Any quoted approximate times are given for execution ona single-processor computer rated at 1.6 ‘flops on the 100 x 100 double-precision Linpack ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, iterative, closest, point, ICP, algorithm, stated, theorem, proven, concerning, monotonic, convergence, property, Unfortunately, ifthe, objective, function, evaluator, changes, values.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Any quoted approximate times are given for execution ona single-processor computer rated at 1.6 ‘flops on the 100 x 100 double-precision Linpack ... | p. 10 (VI. EXPERIMENTAL RESULTS), p. 14 (A BN) |
| Semantic / temporal fusion | The 3 range of 0.6 units is clearly visible compared withthe size ofthe object. | p. 11 (B. Curve Matching), p. 11 (A. Point Ser Matching) |
| Robot query / planning handoff | translations to achieve local matching. | p. 11 (A. Point Ser Matching), p. 14 (A BN) |

## Failure and Ablation Link

- **p. 10 / A. Point Ser Matching - extractive body cue:** In this section, we demonstrate the ability of the ICP algorithm to perform local point set matching without correspondence.
- **p. 11 / A. Point Ser Matching - extractive body cue:** Compared with basic point st matching, which requires the same numberof points listed in direc cortespondence, we are essentially trading off additional CPU time for ...
- **p. 16 / A BN - extractive body cue:** This is important for using CAD data in its native form without elaborate user-guided reprocessing.
- **p. 16 / A BN - extractive body cue:** large problems, even remote execution procedures and distributed file systems on networks of workstations can provide worthwhile speedup without significant overhead,
- **p. 6 / B. Point to Implicit Entity Distance - extractive body cue:** If a dimensionless threshold is desired, one can replace + with Vira), where the square root of the trace of the covaranee of the model ...
- **p. 8 / B. Convergence Theorem - extractive body cue:** "To be precise, consider a 6=D slate space 9, where the ‘quaternion component gy is determined from the oer quaterrion components: go = yt - ...
- **p. 9 / A. Initial States for Global Matching - extractive body cue:** (One must ‘ensure that the ist nonzero quatenion component is postive to avoid duplication of sates.) Fora really complicated set

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (1) Point sets), p. 8 (B. Convergence Theorem), p. 2 (1) Point sets), p. 2 (1) Point sets), p. 6 (B. Convergence Theorem), p. 7 (B. Convergence Theorem), objective p. 2 (1) Point sets), p. 3 (A. Point to Parametric Entity Distance), p. 4 (B. Point to Implicit Entity Distance), p. 4 (B. Point to Implicit Entity Distance), p. 7 (B. Convergence Theorem), p. 8 (B. Convergence Theorem), temporal p. 1 (1. Istmopuction), p. 2 (1) Point sets), p. 2 (1) Point sets), p. 3 (A. Point to Parametric Entity Distance), p. 4 (B. Point to Implicit Entity Distance), p. 4 (B. Point to Implicit Entity Distance).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
