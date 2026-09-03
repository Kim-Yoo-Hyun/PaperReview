# Method - SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3. Method), p. 4 (3. Method), p. 3 (3. Method), p. 3 (3. Method), p. 5 (3. Method), p. 5 (3. Method)): E.g. the camera parameters are initialized using the following: E_ { t+ 1} = E_t + (E_t - E_{t \text {-} 1} ) (7) The camera pose is then updated ...

## Method Body Digest

- **p. 4 / 3. Method - extractive body cue:** E.g. the camera parameters are initialized using the following: E_ { t+ 1} = E_t + (E_t - E_{t \text {-} 1} ) (7) The ...
- **p. 4 / 3. Method - extractive body cue:** We begin with a brief overview and then describe each module in detail.
- **p. 3 / 3. Method - extractive body cue:** By modeling the world as a collection of 3D Gaussians which can be rendered into highfidelity color and depth images, we are able to directly ...
- **p. 3 / 3. Method - extractive body cue:** We made a number of simplifications to the representation proposed in [14], by using only view-independent color and forcing Gaussians to be isotropic.
- **p. 5 / 3. Method - extractive body cue:** Instead of starting from scratch, we warm-start the optimization from the most recently constructed map.
- **p. 5 / 3. Method - extractive body cue:** This phase optimizes a similar loss as during tracking, except we don't use the silhouette mask as we want to optimize over all pixels.
- **p. 4 / 3. Method - extractive body cue:** This differentiable rendering allows us to directly calculate the gradients in the underlying scene representation (Gaussians) and camera parameters with respect to the error between ...
- **p. 5 / 3. Method - extractive body cue:** This is done again by differentiablerendering and gradient-based-optimization, however unlike tracking, in this setting the camera poses are fixed, and the parameters of the Gaussians ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We show across all our experiments on simulated and real data that our approach, SplaTAM, achieves state-of-the-art results compared to all previous approaches for camera ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce several simple modifications that make splatting even faster for SLAM, including the removal of view-dependent appearance and the use of isotropic Gaussians.
- **p. 4 / 3. Method - extractive body cue:** We propose to similarly differentiably render depth: D( \ m a thb f {p}) = \ s um _{i = 1}^{n} d_i f_i(\mathbf {p}) \prod ...

## Source Evidence Cues

- **p. 4 / 3. Method - extractive body cue:** E.g. the camera parameters are initialized using the following: E_ { t+ 1} = E_t + (E_t - E_{t \text {-} 1} ) (7) The ...
- **p. 4 / 3. Method - extractive body cue:** We begin with a brief overview and then describe each module in detail.
- **p. 3 / 3. Method - extractive body cue:** By modeling the world as a collection of 3D Gaussians which can be rendered into highfidelity color and depth images, we are able to directly ...
- **p. 3 / 3. Method - extractive body cue:** We made a number of simplifications to the representation proposed in [14], by using only view-independent color and forcing Gaussians to be isotropic.
- **p. 5 / 3. Method - extractive body cue:** Instead of starting from scratch, we warm-start the optimization from the most recently constructed map.
- **p. 5 / 3. Method - extractive body cue:** This phase optimizes a similar loss as during tracking, except we don't use the silhouette mask as we want to optimize over all pixels.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | E.g. the camera parameters are initialized using the following: E_ { t+ 1} = E_t + (E_t - E_{t \text {-} 1} ... | p. 4 (3. Method), p. 4 (3. Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We begin with a brief overview and then describe each module in detail. | p. 4 (3. Method), p. 3 (3. Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | By modeling the world as a collection of 3D Gaussians which can be rendered into highfidelity color and depth images, we are ... | p. 3 (3. Method), p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3. Method - extractive body cue:** E.g. the camera parameters are initialized using the following: E_ { t+ 1} = E_t + (E_t - E_{t \text {-} 1} ) (7) The ...
- **p. 4 / 3. Method - extractive body cue:** This differentiable rendering allows us to directly calculate the gradients in the underlying scene representation (Gaussians) and camera parameters with respect to the error between ...
- **p. 5 / 3. Method - extractive body cue:** This is done again by differentiablerendering and gradient-based-optimization, however unlike tracking, in this setting the camera poses are fixed, and the parameters of the Gaussians ...
- **p. 3 / 3. Method - extractive body cue:** By modeling the world as a collection of 3D Gaussians which can be rendered into highfidelity color and depth images, we are able to directly ...
- **p. 5 / 3. Method - extractive body cue:** This phase optimizes a similar loss as during tracking, except we don't use the silhouette mask as we want to optimize over all pixels.
- **p. 3 / 3. Method - extractive body cue:** Each Gaussian influences a point in 3D space x ∈R3 according to the standard (unnormalized) Gaussian equation weighted by its opacity: f( \ math b ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3. Method), p. 4 (3. Method), p. 5 (3. Method), p. 3 (3. Method), p. 3 (3. Method), p. 5 (3. Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | similarly, differentiably, render, depth, mathbf, prod, compared, against, input, return, gradients, respect, Gaussians, rendered | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | similarly, differentiably, render, depth, mathbf, prod, compared, against, input, return | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | across, experiments, simulated, real, data, SplaTAM, achieves, state-of-the-art, compared, previous | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | camera, parameters, initialized, following, E_t, text, pose, then, updated, iteratively | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3. Method - extractive body cue:** We propose to similarly differentiably render depth: D( \ m a thb f {p}) = \ s um _{i = 1}^{n} d_i f_i(\mathbf {p}) \prod ...
- **p. 4 / 3. Method - extractive body cue:** We add new Gaussians to the map based on the rendered silhouette and input depth.
- **p. 3 / 3. Method - extractive body cue:** By modeling the world as a collection of 3D Gaussians which can be rendered into highfidelity color and depth images, we are able to directly ...
- **p. 2 / 1. Introduction - extractive body cue:** We show across all our experiments on simulated and real data that our approach, SplaTAM, achieves state-of-the-art results compared to all previous approaches for camera ...
- **p. 5 / 3. Method - extractive body cue:** Overlap is determined by taking the point cloud of the current frame depth map and determining the number of points inside the frustum of each ...
- **p. 1 / 1. Introduction - extractive body cue:** Visual simultaneous localization and mapping (SLAM)- the task of estimating the pose of a vision sensor (such as a depth camera) and a map of ...
- **p. 3 / 3. Method - extractive body cue:** The core of our approach is the ability to render high-fidelity color, depth, and silhouette images from our underlying Gaussian Map 21359
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Given a new RGB-D frame t + 1, our SLAM system performs the following steps (see Fig. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | For the first frame, the tracking step is skipped, and the camera pose is set to identity. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Furthermore, for all comparisons to prior baselines, we present results as the average of 3 seeds (0-2) and use seed 0 for ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** camera, parameters, initialized, following, E_t, text, pose, then, updated, iteratively, gradientbased, optimization, through, differentiably, rendering, RGB, depth, silhouette, maps, updating.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Replica [35] is the simplest benchmark as it contains synthetic scenes, highly accurate and complete (synthetic) depth maps, and small displacements between ... | p. 5 (4. Experimental Setup), p. 6 (5. Results & Discussion) |
| Global / local decision | The main baseline method we compare to is Point-SLAM [30], the previous state-of-the-art (SOTA) method for dense radiance-field-based SLAM. | p. 5 (4. Experimental Setup), p. 6 (5. Results & Discussion) |
| Motion execution / recovery | Compared to prior methods in this category [30, 54], SplaTAM still significantly outperforms, decreasing the trajectory error of the prior SOTA in ... | p. 6 (5. Results & Discussion), p. 6 (5. Results & Discussion) |

## Failure and Ablation Link

- **p. 5 / 4. Experimental Setup - extractive body cue:** Furthermore, for all comparisons to prior baselines, we present results as the average of 3 seeds (0-2) and use seed 0 for the ablations.
- **p. 5 / 5. Results & Discussion - extractive body cue:** Finally, we discuss pipeline ablations and provide a runtime comparison.
- **p. 6 / 5. Results & Discussion - extractive body cue:** On ScanNet++ [49], both SOTA SLAM approaches Point-SLAM [30] and ORB-SLAM3 [3] (RGB-D variant) completely fail to correctly track the camera pose due to the ...
- **p. 7 / 5. Results & Discussion - extractive body cue:** Color & Depth Loss Ablation on Replica/Room 0.
- **p. 7 / 5. Results & Discussion - extractive body cue:** Camera Tracking Ablations on Replica/Room 0. depth loss.
- **p. 8 / 5. Results & Discussion - extractive body cue:** Silhouette is critical as without it tracking completely fails.
- **p. 8 / 5. Results & Discussion - extractive body cue:** Although SplaTAM achieves state-of-the-art performance, we find our method to show some sensitivity to motion blur, large depth noise, and aggressive rotation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3. Method), p. 4 (3. Method), p. 3 (3. Method), p. 3 (3. Method), p. 5 (3. Method), p. 5 (3. Method), objective p. 4 (3. Method), p. 4 (3. Method), p. 5 (3. Method), p. 3 (3. Method), p. 5 (3. Method), p. 3 (3. Method), temporal p. 4 (3. Method), p. 4 (3. Method), p. 3 (2. Related Work), p. 3 (3. Method), p. 5 (4. Experimental Setup), p. 5 (4. Experimental Setup).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
