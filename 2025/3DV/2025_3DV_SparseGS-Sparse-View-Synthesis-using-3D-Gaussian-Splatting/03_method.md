# Method - SparseGS: Sparse View Synthesis using 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=O9GMl5UJbe&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Methods), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)), p. 3 (3. Methods), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)), p. 6 (3.4. Advanced Floater Pruning), p. 4 (3.2. Patch-based Depth Correlation Loss)): Then, we dissect the UVR module into two parts: a Score Distillation Sampling (SDS) loss and a depth warping loss, which are designed for regularizing viewpoints distant and close to ...

## Method Body Digest

- **p. 3 / 3. Methods - extractive body cue:** Then, we dissect the UVR module into two parts: a Score Distillation Sampling (SDS) loss and a depth warping loss, which are designed for regularizing ...
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Then, the renderings at the sampled viewpoints are encoded and decoded by the diffusion model, where the predicted noise is then supervised with our SDS ...
- **p. 3 / 3. Methods - extractive body cue:** Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth correlation ...
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Inspired by recent diffusion models [5, 9, 25, 26, 31, 45] and Score Distillation Sampling (SDS) [38] for zero-shot 3D reconstruction [6, 15, 16, 36], ...
- **p. 6 / 3.4. Advanced Floater Pruning - extractive body cue:** Therefore, we propose a novel pruning operator to remove the Gaussians at false modes at the end of training.
- **p. 4 / 3.2. Patch-based Depth Correlation Loss - extractive body cue:** We compute pseudo-ground truth depth maps using pretrained depth estimation models on the training views.
- **p. 4 / 3.2. Patch-based Depth Correlation Loss - extractive body cue:** Since the monocular estimation model predicts relative depth, while alpha-blending, softmax-scaling, and modeselection depths are COLMAP-anchored, directly applying an L2 loss, such as mean squared ...
- **p. 6 / 3.4. Advanced Floater Pruning - extractive body cue:** Because the softmax depth loss is a soft constraint, there may exist regions where dmode and dalpha do not align.

## Design Rationale

- **p. 3 / 3. Methods - extractive body cue:** Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth correlation ...
- **p. 2 / 1. Introduction - extractive body cue:** Next, we introduce a module designed to tackle background collapse by leveraging a 2D generative diffusion prior [16, 26] and depth warping [22, 44].
- **p. 2 / 1. Introduction - extractive body cue:** We propose a novel framework, SparseGS, for training coherent and robust 3D Gaussian representations from limited inputs, outperforming SOTA methods in sparse view synthesis.

## Source Evidence Cues

- **p. 3 / 3. Methods - extractive body cue:** Then, we dissect the UVR module into two parts: a Score Distillation Sampling (SDS) loss and a depth warping loss, which are designed for regularizing ...
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Then, the renderings at the sampled viewpoints are encoded and decoded by the diffusion model, where the predicted noise is then supervised with our SDS ...
- **p. 3 / 3. Methods - extractive body cue:** Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth correlation ...
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Inspired by recent diffusion models [5, 9, 25, 26, 31, 45] and Score Distillation Sampling (SDS) [38] for zero-shot 3D reconstruction [6, 15, 16, 36], ...
- **p. 6 / 3.4. Advanced Floater Pruning - extractive body cue:** Therefore, we propose a novel pruning operator to remove the Gaussians at false modes at the end of training.
- **p. 4 / 3.2. Patch-based Depth Correlation Loss - extractive body cue:** We compute pseudo-ground truth depth maps using pretrained depth estimation models on the training views.
- **p. 4 / 3.2. Patch-based Depth Correlation Loss - extractive body cue:** Since the monocular estimation model predicts relative depth, while alpha-blending, softmax-scaling, and modeselection depths are COLMAP-anchored, directly applying an L2 loss, such as mean squared ...
- **Detected method headings:** 3. Methods (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, we dissect the UVR module into two parts: a Score Distillation Sampling (SDS) loss and a depth warping loss, which are ... | p. 3 (3. Methods), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Then, the renderings at the sampled viewpoints are encoded and decoded by the diffusion model, where the predicted noise is then supervised ... | p. 5 (3.3. Unseen Viewpoints Regularization (UVR)), p. 3 (3. Methods) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: ... | p. 3 (3. Methods), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.4. Advanced Floater Pruning - extractive body cue:** Because the softmax depth loss is a soft constraint, there may exist regions where dmode and dalpha do not align.
- **p. 4 / 3.1. Mode-selection & Softmax-scaling Depth Ren - extractive body cue:** While rendering depth using the mode identifies the most significant Gaussians contributing to the depth, the arg max operator restricts the gradient during backpropagation flow ...
- **p. 3 / 3. Methods - extractive body cue:** Then, we dissect the UVR module into two parts: a Score Distillation Sampling (SDS) loss and a depth warping loss, which are designed for regularizing ...
- **p. 3 / 3. Methods - extractive body cue:** Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth correlation ...
- **p. 4 / 3.1. Mode-selection & Softmax-scaling Depth Ren - extractive body cue:** (7) With the softmax-scaling add-on, we can approximate the mode depth while still propagating gradients to Gaussians off the mode.
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Illustration of benefits from the SDS loss.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3.4. Advanced Floater Pruning), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 3 (3. Methods), p. 3 (3. Methods), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Combined, pipeline, achieves, state-of-the-art, SOTA, performance, sparse-input, novel, view, synthesis, NVS, problems, only, forward-facing | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Combined, pipeline, achieves, state-of-the-art, SOTA, performance, sparse-input, novel, view, synthesis | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | consists, three, components, designed, function, cohesively, improve, view, consistency, depth | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Because, softmax, depth, loss, soft, constraint, there, exist, regions, where | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Combined, our pipeline achieves state-of-the-art (SOTA) performance in sparse-input novel view synthesis (NVS) problems, not only on forward-facing datasets but also on 360-degree unbounded scenes, ...
- **p. 6 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Mathematically, we define our image re-projection as follows: For pixel pi(xi, yi) in training image Isrc, the warping to the corresponding pixel pj(xj, yj) at ...
- **p. 1 / 1. Introduction - extractive body cue:** However, 3DGS still suffers from artifacts caused by the inherent ambiguity in projection from 3D to 2D posed by sparse input views.
- **p. 2 / 1. Introduction - extractive body cue:** Our objective is to accurately reconstruct 360-degree unbounded 3D scenes using as few as 12 input images.
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Specifically, we implement a strategy that samples random viewpoints around the center of scene estimated from input cameras.
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** In the sparse-view setting, Gaussians that are well constrained under input viewpoints often appear as small fragmentation rendered from other sampled viewpoints.
- **p. 6 / 3.4. Advanced Floater Pruning - extractive body cue:** As a result, some floaters may remain along the rays of the input views.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 4, where the module successfully removes high-frequency artifacts while leaving the scene structure untouched. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | While the scene structure is well preserved, the high-frequency noise in both geometry and texture is significantly reduced (red box). | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Methods - extractive body cue:** Then, we dissect the UVR module into two parts: a Score Distillation Sampling (SDS) loss and a depth warping loss, which are designed for regularizing ...
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Inspired by recent diffusion models [5, 9, 25, 26, 31, 45] and Score Distillation Sampling (SDS) [38] for zero-shot 3D reconstruction [6, 15, 16, 36], ...
- **p. 6 / 3.4. Advanced Floater Pruning - extractive body cue:** Therefore, we propose a novel pruning operator to remove the Gaussians at false modes at the end of training.
- **p. 4 / 3.2. Patch-based Depth Correlation Loss - extractive body cue:** We compute pseudo-ground truth depth maps using pretrained depth estimation models on the training views.
- **p. 4 / 3.2. Patch-based Depth Correlation Loss - extractive body cue:** We compute pseudo-ground truth depth maps using pretrained depth estimation models on the training views.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, dissect, UVR, module, parts, Score, Distillation, Sampling, SDS, loss, depth, warping, designed, regularizing, viewpoints, distant, close, training, cameras, respectively.
- **Relevant PDF headings:** 3. Methods (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The LLFF dataset comprises eight complex forward-facing real scenes, while the DTU dataset includes object-centric scenes with foreground masks. | p. 7 (4.2. Comparison), p. 6 (4.1. Experimental Settings) |
| Semantic / temporal fusion | 1, SparseGS significantly outperforms previous NeRF-based methods and concurrent works, FSGS and DNGaussian, in both 12-view and 24-view settings. | p. 7 (4.2. Comparison), p. 7 (4.3. Ablation Studies) |
| Robot query / planning handoff | 1, SparseGS significantly outperforms previous NeRF-based methods and concurrent works, FSGS and DNGaussian, in both 12-view and 24-view settings. | p. 7 (4.2. Comparison), p. 3 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 4.1. Experimental Settings - extractive body cue:** The proposed floater pruning technique removes Gaussians at inaccurate depths.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** The pruning method removes all Gaussians on that pixel before the mode and as a result, dmode = dalpha.
- **p. 7 / 4.2. Comparison - extractive body cue:** In order to prove robustness of our method, we also evaluate performance with even sparser point clouds output by Structure From Motion (i.e., without the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation Studies. We ablate our components on the Mip-NeRF360 dataset under 12-view setting. regions, where input coverage is insufficient, NeRF-based methods often produce ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Ablation studies. The reference depth map is produced by a monocular depth estimation model. Our complete model outputs a cleaner and more consistent ...
- **p. 7 / 4.2. Comparison - extractive body cue:** This limitation actually prompted the introduction of positional encoding [20, 37].
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** In contrast, FSGS excels in preserving fine details due to its densification technique but fails to reconstruct background geometry.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Methods), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)), p. 3 (3. Methods), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)), p. 6 (3.4. Advanced Floater Pruning), p. 4 (3.2. Patch-based Depth Correlation Loss), objective p. 6 (3.4. Advanced Floater Pruning), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 3 (3. Methods), p. 3 (3. Methods), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)), temporal p. 5 (3.3. Unseen Viewpoints Regularization (UVR)), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)), p. 7 (4.3. Ablation Studies), p. 7 (4.1. Experimental Settings), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
