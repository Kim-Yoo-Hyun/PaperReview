# Method - FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=QI6HrBseVF&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction)): Alongside the use of point tracks to encourage long-term geometric consistency, we introduce differentiable re-parameterizations of depth, intrinsics, and pose that are amenable to first-order optimization.

## Method Body Digest

- **p. 1 / Body text (section not recovered) - extractive body cue:** Alongside the use of point tracks to encourage long-term geometric consistency, we introduce differentiable re-parameterizations of depth, intrinsics, and pose that are amenable to first-order ...
- **p. 2 / 1 Introduction - extractive body cue:** Rather, we introduce differentiable feed-forward estimates of each one: depth is parameterized via a neural network, pose is parameterized as the solution to a least-squares ...
- **p. 2 / 1 Introduction - extractive body cue:** In other words, FlowMap solves SfM by learning the depth network's parameters; camera poses and intrinsics are computed via analytical feed-forward modules without free parameters ...
- **p. 3 / 1 Introduction - extractive body cue:** Gaussian Splats obtained from FlowMap reconstructions far outperform the state-of-the-art gradient-based bundle-adjustment method, NoPe-NeRF [2], and those obtained using the SLAM algorithm DROIDSLAM [67], even ...
- **p. 1 / 1 Introduction - extractive body cue:** Today, essentially all state-ofthe-art approaches are built on top of Structure-from-Motion (SfM) methods like COLMAP [58].
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our method performs per-video gradient-descent minimization of a simple least-squares objective that compares the optical flow induced by depth, intrinsics, and poses against correspondences obtained ...
- **p. 2 / 1 Introduction - extractive body cue:** Its loss is minimized only via gradient descent, leading to high-quality camera poses, camera intrinsics, and per-pixel depth.
- **p. 1 / 1 Introduction - extractive body cue:** These approaches extract sparse correspondences across frames, match them, discard outliers, and then optimize the correspondences' 3D positions alongside the camera parameters by minimizing reprojection ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we present FlowMap, a differentiable and surprisingly simple camera and geometry estimation method whose outputs enable photorealistic novel view synthesis.
- **p. 2 / 1 Introduction - extractive body cue:** We show that this uniquely enables high-quality SfM via gradient descent while making FlowMap compatible with standard deep-learning pipelines.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We empirically show that camera parameters and dense depth recovered by our method enable photo-realistic novel view synthesis on 360◦trajectories using Gaussian Splatting.

## Source Evidence Cues

- **p. 1 / Body text (section not recovered) - extractive body cue:** Alongside the use of point tracks to encourage long-term geometric consistency, we introduce differentiable re-parameterizations of depth, intrinsics, and pose that are amenable to first-order ...
- **p. 2 / 1 Introduction - extractive body cue:** Rather, we introduce differentiable feed-forward estimates of each one: depth is parameterized via a neural network, pose is parameterized as the solution to a least-squares ...
- **p. 2 / 1 Introduction - extractive body cue:** In other words, FlowMap solves SfM by learning the depth network's parameters; camera poses and intrinsics are computed via analytical feed-forward modules without free parameters ...
- **p. 3 / 1 Introduction - extractive body cue:** Gaussian Splats obtained from FlowMap reconstructions far outperform the state-of-the-art gradient-based bundle-adjustment method, NoPe-NeRF [2], and those obtained using the SLAM algorithm DROIDSLAM [67], even ...
- **p. 1 / 1 Introduction - extractive body cue:** Today, essentially all state-ofthe-art approaches are built on top of Structure-from-Motion (SfM) methods like COLMAP [58].
- **Detected method headings:** A method (p. 17); 23 Method (p. 23)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Alongside the use of point tracks to encourage long-term geometric consistency, we introduce differentiable re-parameterizations of depth, intrinsics, and pose that are ... | p. 1 (Body text (section not recovered)), p. 2 (1 Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Rather, we introduce differentiable feed-forward estimates of each one: depth is parameterized via a neural network, pose is parameterized as the solution ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In other words, FlowMap solves SfM by learning the depth network's parameters; camera poses and intrinsics are computed via analytical feed-forward modules ... | p. 2 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Body text (section not recovered) - extractive body cue:** Our method performs per-video gradient-descent minimization of a simple least-squares objective that compares the optical flow induced by depth, intrinsics, and poses against correspondences obtained ...
- **p. 2 / 1 Introduction - extractive body cue:** Its loss is minimized only via gradient descent, leading to high-quality camera poses, camera intrinsics, and per-pixel depth.
- **p. 1 / 1 Introduction - extractive body cue:** These approaches extract sparse correspondences across frames, match them, discard outliers, and then optimize the correspondences' 3D positions alongside the camera parameters by minimizing reprojection ...
- **p. 2 / 1 Introduction - extractive body cue:** FlowMap is supervised only with offthe-shelf optical flow and point track correspondences, and optimized per-scene with gradient descent.
- **p. 3 / 1 Introduction - extractive body cue:** FlowMap: Camera Poses, Intrinsics and Depth via Gradient Descent 3 using Gaussian Splatting [29].
- **p. 3 / 1 Introduction - extractive body cue:** Gaussian Splats obtained from FlowMap are on par with those obtained from COLMAP [58], even though FlowMap only leverages gradient descent, is fully differentiable, and ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | present, FlowMap, end-to-end, differentiable, recovers, poses, intrinsics, depth, maps, input, video, Unlike, conventional, SfM | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | present, FlowMap, end-to-end, differentiable, recovers, poses, intrinsics, depth, maps, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, FlowMap, differentiable, surprisingly, simple, camera, geometry, estimation, whose, outputs | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | performs, per-video, gradient-descent, minimization, simple, least-squares, objective, compares, optical, flow | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** 1: We present FlowMap, an end-to-end differentiable method that recovers poses, intrinsics, and depth maps of an input video.
- **p. 2 / 1 Introduction - extractive body cue:** Unlike conventional SfM, which outputs sparse 3D points that are each constrained by several views, FlowMap outputs dense per-frame depth estimates.
- **p. 1 / Body text (section not recovered) - extractive body cue:** This paper introduces FlowMap, an end-to-end differentiable method that solves for precise camera poses, camera intrinsics, and perframe dense depth of a video sequence.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our method performs per-video gradient-descent minimization of a simple least-squares objective that compares the optical flow induced by depth, intrinsics, and poses against correspondences obtained ...
- **p. 3 / 1 Introduction - extractive body cue:** Gaussian Splats obtained from FlowMap reconstructions far outperform the state-of-the-art gradient-based bundle-adjustment method, NoPe-NeRF [2], and those obtained using the SLAM algorithm DROIDSLAM [67], even ...
- **p. 3 / 1 Introduction - extractive body cue:** FlowMap: Camera Poses, Intrinsics and Depth via Gradient Descent 3 using Gaussian Splatting [29].
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This paper introduces FlowMap, an end-to-end differentiable method that solves for precise camera poses, camera intrinsics, and perframe dense depth of a ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Meanwhile, simultaneous localization and mapping (SLAM) usually refers to real-time, online methods. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | FlowMap's complexity in time and memory is linear with the number of input video frames. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Alongside, point, tracks, encourage, long-term, geometric, consistency, introduce, differentiable, re-parameterizations, depth, intrinsics, pose, amenable, first-order, optimization, Rather, feed-forward, estimates, parameterized.
- **Relevant PDF headings:** A method (p. 17); 23 Method (p. 23).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We benchmark FlowMap via the downstream task of 3D Gaussian reconstruction [29]. | p. 10 (6 Results), p. 14 (6 Results) |
| Semantic / temporal fusion | Table 1: Camera parameter and geometry intializations from FlowMap produce 3D Gaussian reconstruction results that far outperform prior gradient-based baselines and are ... | p. 10 (Figure/Table caption), p. 10 (6 Results) |
| Robot query / planning handoff | Quantitatively, FlowMap performs slightly better than COLMAP SfM and significantly outperforms DROID-SLAM and NoPE-NeRF. | p. 11 (6 Results), p. 13 (6 Results) |

## Failure and Ablation Link

- **p. 10 / 6 Results - extractive body cue:** This allows us to measure the quality of the camera parameters and geometry (depth maps) it outputs without having access to ground-truth scene geometry and ...
- **p. 13 / 6 Results - extractive body cue:** See the supplemental document for more ablations.
- **p. 13 / 6 Results - extractive body cue:** We find that free-variable variants of FlowMap produce significantly worse reconstruction results and converge much more slowly, confirming that FlowMap's reparameterizations are crucial.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 10: Effects of pretraining. While a randomly initialized FlowMap network often provides accurate poses after optimization, pre-training leads to faster convergence and slightly improved ...
- **p. 11 / 6 Results - extractive body cue:** During 3D Gaussian fitting, we follow the common [63] practice of fine-tuning the initial camera poses and intrinsics.
- **p. 14 / 8 Discussion - extractive body cue:** FlowMap has several limitations that suggest exciting directions for future work.
- **p. 13 / 6 Results - extractive body cue:** However, on about 20 percent of scenes, this approach falls into a local minimum and reconstruction fails catastrophically.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), objective p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), temporal p. 1 (Body text (section not recovered)), p. 3 (2 Related Work), p. 5 (2 Related Work), p. 5 (2 Related Work), p. 8 (2 Related Work), p. 8 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
