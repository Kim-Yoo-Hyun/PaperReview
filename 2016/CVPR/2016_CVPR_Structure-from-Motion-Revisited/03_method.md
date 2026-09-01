# Method - Structure-from-Motion Revisited

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_cvpr_2016/papers/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (2.2. Incremental Reconstruction), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction)): Starting from a metric reconstruction, new images can be registered to the current model by solving the Perspective-n-Point (PnP) problem [18] using feature correspondences to triangulated points in already registered ...

## Method Body Digest

- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** Starting from a metric reconstruction, new images can be registered to the current model by solving the Perspective-n-Point (PnP) problem [18] using feature correspondences to ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** Without further refinement, SfM usually drifts quickly to a non-recoverable state.
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** and a loss function ρj to potentially down-weight outliers.
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** In this case, indirect algorithms are the method of choice.
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** These methods suffer from limited robustness or high computational cost for use in SfM, which we address by proposing a robust and efficient triangulation method ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** BA [58] is the joint non-linear refinement of camera parameters Pc and point parameters Xk that minimizes the reprojection error E = X j ρj ...
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** Inexact methods approximately solve the system, usually by using an iterative solver, e.g. preconditioned conjugate gradients (PCG), which has O(NP ) time and space complexity ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** The outputs are pose estimates P = {Pc ∈SE(3) / c = 1...NP } for registered images and the reconstructed scene structure as a set ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** In this paper, we propose a new SfM algorithm to approach this ultimate goal.
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** We propose a novel robust next best image selection method for accurate pose estimation and reliable triangulation in Sec.
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** 4.5, we propose a method to identify and parameterize highly overlapping images for efficient BA of dense collections.

## Source Evidence Cues

- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** Starting from a metric reconstruction, new images can be registered to the current model by solving the Perspective-n-Point (PnP) problem [18] using feature correspondences to ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** Without further refinement, SfM usually drifts quickly to a non-recoverable state.
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** and a loss function ρj to potentially down-weight outliers.
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** In this case, indirect algorithms are the method of choice.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Starting from a metric reconstruction, new images can be registered to the current model by solving the Perspective-n-Point (PnP) problem [18] using ... | p. 2 (2.2. Incremental Reconstruction), p. 2 (2.2. Incremental Reconstruction) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Without further refinement, SfM usually drifts quickly to a non-recoverable state. | p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | and a loss function ρj to potentially down-weight outliers. | p. 3 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** These methods suffer from limited robustness or high computational cost for use in SfM, which we address by proposing a robust and efficient triangulation method ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** BA [58] is the joint non-linear refinement of camera parameters Pc and point parameters Xk that minimizes the reprojection error E = X j ρj ...
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** and a loss function ρj to potentially down-weight outliers.
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** Inexact methods approximately solve the system, usually by using an iterative solver, e.g. preconditioned conjugate gradients (PCG), which has O(NP ) time and space complexity ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | outputs, pose, estimates, registered, images, reconstructed, scene, structure, points, While, existing, systems, have, advanced | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | outputs, pose, estimates, registered, images, reconstructed, scene, structure, points, While | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | SfM, algorithm, ultimate, goal, novel, robust, next, best, image, selection | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | methods, suffer, limited, robustness, high, computational, cost, SfM, address, proposing | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** The outputs are pose estimates P = {Pc ∈SE(3) / c = 1...NP } for registered images and the reconstructed scene structure as a set ...
- **p. 1 / 1. Introduction - extractive PDF cue:** While the existing systems have advanced the state of the art tremendously, robustness, accuracy, completeness, and scalability remain the key problems in incremental SfM that ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** The input to the reconstruction stage is the scene graph.
- **p. 1 / 1. Introduction - extractive PDF cue:** In this paper, we propose a new SfM algorithm to approach this ultimate goal.
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** 4.5, we propose a method to identify and parameterize highly overlapping images for efficient BA of dense collections.
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** Especially for Internet photos, BA spends significant time on optimizing many near-duplicate images.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | We propose a new SfM technique that improves upon the state of the art to make a further step towards this ultimate ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Triangulation is a crucial step in SfM, as it increases the stability of the existing model through redundancy [58] and it enables ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Starting, metric, reconstruction, images, registered, current, model, solving, Perspective-n-Point, PnP, problem, feature, correspondences, triangulated, points, already, D-3D, Without, further, refinement.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | An experiment on the Dubrovnik dataset (Fig. | p. 7 (5. Experiments), p. 7 (5. Experiments) |
| Global / local decision | We run experiments on a large variety of datasets to evaluate both the proposed components and the overall system compared to state-of-the-art ... | p. 7 (5. Experiments), p. 8 (7.82 M) |
| Motion execution / recovery | For all datasets, we significantly outperform any other method in terms of completeness, especially for the larger models. | p. 8 (7.82 M), p. 8 (7.82 M) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Next best view scores for Gaussian distributed points xj ∈[0, 1]×[0, 1] with mean µ and std. dev. σ. Score S w.r.t. uni- ...
- **p. 7 / 5. Experiments - extractive PDF cue:** We run experiments on a large variety of datasets to evaluate both the proposed components and the overall system compared to state-of-the-art incremental (Bundler [53], ...
- **p. 8 / 7.82 M - extractive PDF cue:** For each dataset, we report the largest reconstructed component.
- **p. 8 / 7.82 M - extractive PDF cue:** Reconstruction of Gendarmenmarkt [61] for Bundler (left) and our method (right). of the overall system and thereby also evaluate the performance of the individual proposed ...
- **p. 8 / 6. Conclusion - extractive PDF cue:** The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, and efficiency.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. late ...
- **p. 7 / 5. Experiments - extractive PDF cue:** Robust and Efficient Triangulation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (2.2. Incremental Reconstruction), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), objective p. 2 (2.2. Incremental Reconstruction), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), temporal p. 1 (Abstract), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), p. 3 (3. Challenges), p. 4 (4.2. Next Best View Selection), p. 4 (4.2. Next Best View Selection).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
