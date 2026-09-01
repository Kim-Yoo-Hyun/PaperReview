# Method - LSD-SLAM: Large-Scale Direct Monocular SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://cvg.cit.tum.de/research/vslam/lsdslam; PDF retrieval source: https://jakobengel.github.io/pdf/engel14eccv.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 4 (2 Preliminaries), p. 4 (2 Preliminaries)): 3.1 The Complete Method The algorithm consists of three major components: tracking, depth map estimation and map optimization as visualized in Fig.

## Method Body Digest

- **p. 6 / 2 Preliminaries - extractive PDF cue:** 3.1 The Complete Method The algorithm consists of three major components: tracking, depth map estimation and map optimization as visualized in Fig.
- **p. 7 / 2 Preliminaries - extractive PDF cue:** 3.2 Map Representation The map is represented as a pose graph of keyframes: Each keyframe Ki consists of a camera image Ii : Ωi →R, ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** The three main components of the algorithm are then described in Sec.
- **p. 7 / 2 Preliminaries - extractive PDF cue:** Given sufficient translational camera movement in the first seconds, the algorithm "locks" to a certain configuration, and after a couple of keyframe propagations converges to ...
- **p. 4 / 2 Preliminaries - extractive PDF cue:** (1) During optimization, a minimal representation for the camera pose is required, which is given by the corresponding element ξ ∈se(3) of the associated Lie-algebra.
- **p. 4 / 2 Preliminaries - extractive PDF cue:** In particular, we summarize the representation of 3D poses as elements of Lie-Algebras (Sec.
- **p. 5 / 2 Preliminaries - extractive PDF cue:** LSD-SLAM: Large-Scale Direct Monocular SLAM 5 As for rigid body transformations, a minimal representation is given by elements of the associated Lie-algebra ξ ∈sim(3), which ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** 2.2 Weighted Gauss-Newton Optimization on Lie-Manifolds Two images are aligned by Gauss-Newton minimization of the photometric error E(ξ) = X i (Iref(pi) -I(ω(pi, Dref(pi), ξ)))2 ...

## Design Rationale

- **p. 6 / 2 Preliminaries - extractive PDF cue:** 3.1 The Complete Method The algorithm consists of three major components: tracking, depth map estimation and map optimization as visualized in Fig.
- **p. 7 / 2 Preliminaries - extractive PDF cue:** 3.2 Map Representation The map is represented as a pose graph of keyframes: Each keyframe Ki consists of a camera image Ii : Ωi →R, ...
- **p. 1 / 1 Introduction - extractive PDF cue:** The advantage is that this allows to seamlessly switch between differently scaled environments, such as a desk environment indoors and large-scale outdoor environments.

## Source Evidence Cues

- **p. 6 / 2 Preliminaries - extractive PDF cue:** 3.1 The Complete Method The algorithm consists of three major components: tracking, depth map estimation and map optimization as visualized in Fig.
- **p. 7 / 2 Preliminaries - extractive PDF cue:** 3.2 Map Representation The map is represented as a pose graph of keyframes: Each keyframe Ki consists of a camera image Ii : Ωi →R, ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** The three main components of the algorithm are then described in Sec.
- **p. 7 / 2 Preliminaries - extractive PDF cue:** Given sufficient translational camera movement in the first seconds, the algorithm "locks" to a certain configuration, and after a couple of keyframe propagations converges to ...
- **p. 4 / 2 Preliminaries - extractive PDF cue:** (1) During optimization, a minimal representation for the camera pose is required, which is given by the corresponding element ξ ∈se(3) of the associated Lie-algebra.
- **p. 4 / 2 Preliminaries - extractive PDF cue:** In particular, we summarize the representation of 3D poses as elements of Lie-Algebras (Sec.
- **p. 5 / 2 Preliminaries - extractive PDF cue:** LSD-SLAM: Large-Scale Direct Monocular SLAM 5 As for rigid body transformations, a minimal representation is given by elements of the associated Lie-algebra ξ ∈sim(3), which ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | 3.1 The Complete Method The algorithm consists of three major components: tracking, depth map estimation and map optimization as visualized in Fig. | p. 6 (2 Preliminaries), p. 7 (2 Preliminaries) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | 3.2 Map Representation The map is represented as a pose graph of keyframes: Each keyframe Ki consists of a camera image Ii ... | p. 7 (2 Preliminaries), p. 6 (2 Preliminaries) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The three main components of the algorithm are then described in Sec. | p. 6 (2 Preliminaries), p. 7 (2 Preliminaries) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 2 Preliminaries - extractive PDF cue:** 2.2 Weighted Gauss-Newton Optimization on Lie-Manifolds Two images are aligned by Gauss-Newton minimization of the photometric error E(ξ) = X i (Iref(pi) -I(ω(pi, Dref(pi), ξ)))2 ...
- **p. 4 / 2 Preliminaries - extractive PDF cue:** 2.1), derive direct image alignment as weighted least-squares minimization on Lie-manifolds (Sec.
- **p. 7 / 2 Preliminaries - extractive PDF cue:** Note that the depth map and variance are only defined for a subset of pixels ΩDi ⊂Ωi, containing all image regions in the vicinity of ...
- **p. 7 / 2 Preliminaries - extractive PDF cue:** 3.3 Tracking new Frames: Direct se(3) Image Alignment Starting from an existing keyframe Ki = (Ii, Di, Vi), the relative 3D pose ξji ∈ se(3) ...
- **p. 8 / I. Mini - extractive PDF cue:** Note that no depth information for the new camera image is available - therefore, the scale of the new image is not defined, and the ...
- **p. 8 / 2 Preliminaries - extractive PDF cue:** For z translation depth noise has no effect for pixels in the center of the image, while for x translation it only affects residuals with ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 7 (2 Preliminaries), p. 8 (2 Preliminaries), p. 5 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Propagation, Uncertainty, statistical, tool, derive, output, function, caused, input, Map, Representation, represented, pose, graph | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Propagation, Uncertainty, statistical, tool, derive, output, function, caused, input, Map | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Complete, algorithm, consists, three, major, components, tracking, depth, estimation, optimization | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Weighted, Gauss-Newton, Optimization, Lie-Manifolds, Two, images, aligned, minimization, photometric, error | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 2 Preliminaries - extractive PDF cue:** 2.3 Propagation of Uncertainty Propagation of uncertainty is a statistical tool to derive the uncertainty of the output of a function f(X), caused by uncertainty ...
- **p. 7 / 2 Preliminaries - extractive PDF cue:** 3.2 Map Representation The map is represented as a pose graph of keyframes: Each keyframe Ki consists of a camera image Ii : Ωi →R, ...
- **p. 4 / 2 Preliminaries - extractive PDF cue:** Images I : Ω→ R, the per-pixel inverse depth map D: Ω→R+ and the inverse depth variance map V : Ω→R+ are written as functions, ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** Tracking Depth Map Estimation Map Optimization New Image (640 x 480 at 30Hz) Track on Current KF: → estimate SE(3) transformation Current KF Refine Current ...
- **p. 7 / 2 Preliminaries - extractive PDF cue:** Note that the depth map and variance are only defined for a subset of pixels ΩDi ⊂Ωi, containing all image regions in the vicinity of ...
- **p. 4 / 2 Preliminaries - extractive PDF cue:** (2) Further, we define the 3D projective warp function ω, which projects an image point p and its inverse depth d into a by ξ ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** The exponential and logarithmic map, pose concatenation and a projective warp function ωs can be defined analogously to the se(3) case, for further details see ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Along with highly accurate pose estimation based on direct image alignment, the 3D environment is reconstructed in real-time as pose-graph of keyframes ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | The fundamental idea behind feature-based approaches (both filtering-based [15, 19] and keyframe-based [15]) is to split the overall problem - estimating geometric ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Complete, algorithm, consists, three, major, components, tracking, depth, estimation, optimization, visualized, Fig, Map, Representation, represented, pose, graph, keyframes, keyframe, camera.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | 9: Results on the TUM RGB-D benchmark [25], and two simulated sequences from [12], measured as absolute trajectory RMSE (cm). | p. 13 (4 Results), p. 12 (4 Results) |
| Global / local decision | Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to right: Accumulated pointcloud thesholded ... | p. 3 (Figure/Table caption), p. 13 (4 Results) |
| Motion execution / recovery | 4.1 Qualitative Results on Large Trajectories We tested the algorithm on several long and challenging trajectories, which include many camera rotations, large ... | p. 12 (4 Results), p. 13 (4 Results) |

## Failure and Ablation Link

- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 10: Convergence radius and accuracy of sim(3) direct image alignment with and without ESM minimization (indicated by light / dark) for a different num- ...
- **p. 13 / 4 Results - extractive PDF cue:** For LSD-SLAM, we also show the number of keyframes created. 'x' denotes tracking failure, '-' no available data.
- **p. 14 / 5 Conclusion - extractive PDF cue:** Major components of the proposed method are two key novelties: (1) a direct method to align two keyframes on sim(3), explicitly incorporating and detecting scale-drift ...
- **p. 14 / 5 Conclusion - extractive PDF cue:** We experimentally showed that the approach reliably tracks and maps even challenging hand-held trajectories with a length of over 500 m, in particular including large ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to right: Accumulated pointcloud thesholded with different maximum ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: Overview over the complete LSD-SLAM algorithm. In practice, the residuals are highly correlated, such that Σξ is only a lower bound - yet ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 4: Statistic normalization: (a) reference image. (b-d): tracked images and inverse variance σ-2 rp of the residual. For pure rotation, depth noise has no ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 4 (2 Preliminaries), p. 4 (2 Preliminaries), objective p. 5 (2 Preliminaries), p. 4 (2 Preliminaries), p. 7 (2 Preliminaries), p. 7 (2 Preliminaries), p. 8 (I. Mini), p. 8 (2 Preliminaries), temporal p. 1 (Front matter), p. 1 (1.1 Related Work), p. 2 (1.1 Related Work), p. 14 (4 Results), p. 2 (1.1 Related Work), p. 3 (1.1 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
