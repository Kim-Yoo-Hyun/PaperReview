# Method - RayI2P: Learning Rays for Image-to-Point Cloud Registration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=arfeGsDWoq; PDF retrieval source: https://openreview.net/pdf/09c38982c905d883a78e5402e6aec9db26ab7455.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD)): We then apply a transformer-based fusion module (Vaswani et al., 2017) consisting of multiple self and cross attention layers, executed in an alternate fashion for L iterations.

## Method Body Digest

- **p. 5 / 3 METHOD - extractive PDF cue:** We then apply a transformer-based fusion module (Vaswani et al., 2017) consisting of multiple self and cross attention layers, executed in an alternate fashion for ...
- **p. 5 / 3 METHOD - extractive PDF cue:** To encourage each image patch to attend more to geometrically relevant 3D points, we propose a focus loss that guides the attention distribution in cross ...
- **p. 6 / 3 METHOD - extractive PDF cue:** To address this, we propose a learnable ray-guided pose regression module that estimates the camera pose from fused patch features Ff, predicted patch rays r, ...
- **p. 4 / 3 METHOD - extractive PDF cue:** In this paper, we propose a ray-based imageto-point cloud registration method composed of two main stages: a ray prediction module to infer consistent 3D rays ...
- **p. 6 / 3 METHOD - extractive PDF cue:** The overall loss consists of three terms: a ray regression loss Lray, a camera pose loss Lcam, and a focus loss Lfoc introduced in Equation ...
- **p. 4 / 3 METHOD - extractive PDF cue:** While compact, this low-dimensional representation is difficult to regress directly from complex visual and geometric features because of strong geometric constraints and nonlinearities.
- **p. 18 / A.7 THE USE OF LARGE LANGUAGE MODELS (LLMS) - extractive PDF cue:** In this extreme case, the cross attention module is misled and lacks any informative guidance due to completely incorrect overlap prediction, leading to failed ray ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Camera center c is obtained by minimizing distances from a point to all rays: c = arg minp∈R3 X i //p × di -mi//2.

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** The main contributions are summarized as follows: (1) We propose a novel ray-based paradigm for image-to-point cloud registration, which effectively addresses the core limitations of ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To realize this idea, we propose a novel ray-based framework for image-to-point cloud registration as shown in Figure 1(c).
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** (2) Extensive experiments on KITTI and nuScenes demonstrate that our method achieves state-of-the-art performance in cross-modal registration accuracy, validating the effectiveness of our ray-based representation.

## Source Evidence Cues

- **p. 5 / 3 METHOD - extractive PDF cue:** We then apply a transformer-based fusion module (Vaswani et al., 2017) consisting of multiple self and cross attention layers, executed in an alternate fashion for ...
- **p. 5 / 3 METHOD - extractive PDF cue:** To encourage each image patch to attend more to geometrically relevant 3D points, we propose a focus loss that guides the attention distribution in cross ...
- **p. 6 / 3 METHOD - extractive PDF cue:** To address this, we propose a learnable ray-guided pose regression module that estimates the camera pose from fused patch features Ff, predicted patch rays r, ...
- **p. 4 / 3 METHOD - extractive PDF cue:** In this paper, we propose a ray-based imageto-point cloud registration method composed of two main stages: a ray prediction module to infer consistent 3D rays ...
- **p. 6 / 3 METHOD - extractive PDF cue:** The overall loss consists of three terms: a ray regression loss Lray, a camera pose loss Lcam, and a focus loss Lfoc introduced in Equation ...
- **p. 4 / 3 METHOD - extractive PDF cue:** While compact, this low-dimensional representation is difficult to regress directly from complex visual and geometric features because of strong geometric constraints and nonlinearities.
- **p. 18 / A.7 THE USE OF LARGE LANGUAGE MODELS (LLMS) - extractive PDF cue:** In this extreme case, the cross attention module is misled and lacks any informative guidance due to completely incorrect overlap prediction, leading to failed ray ...
- **Detected method headings:** 3 METHOD (p. 4); A.7 THE USE OF LARGE LANGUAGE MODELS (LLMS) (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We then apply a transformer-based fusion module (Vaswani et al., 2017) consisting of multiple self and cross attention layers, executed in an ... | p. 5 (3 METHOD), p. 5 (3 METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To encourage each image patch to attend more to geometrically relevant 3D points, we propose a focus loss that guides the attention ... | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To address this, we propose a learnable ray-guided pose regression module that estimates the camera pose from fused patch features Ff, predicted ... | p. 6 (3 METHOD), p. 4 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 METHOD - extractive PDF cue:** The overall loss consists of three terms: a ray regression loss Lray, a camera pose loss Lcam, and a focus loss Lfoc introduced in Equation ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Camera center c is obtained by minimizing distances from a point to all rays: c = arg minp∈R3 X i //p × di -mi//2.
- **p. 6 / 3 METHOD - extractive PDF cue:** (9) To jointly optimize all components, we define the total loss as the sum of the three sub-losses: Ltotal = Lray + Lcam + Lfoc.
- **p. 4 / 3 METHOD - extractive PDF cue:** While compact, this low-dimensional representation is difficult to regress directly from complex visual and geometric features because of strong geometric constraints and nonlinearities.
- **p. 5 / 3 METHOD - extractive PDF cue:** To encourage each image patch to attend more to geometrically relevant 3D points, we propose a focus loss that guides the attention distribution in cross ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | output, feature, downsampled, factor, relative, input, image, yielding, resolution, KITTI, nuScenes, Through, rounds, alternate | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | output, feature, downsampled, factor, relative, input, image, yielding, resolution, KITTI | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, novel, ray-based, paradigm, image-to-point, cloud, registration | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | overall, loss, consists, three, terms, regression, Lray, camera, pose, Lcam | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 16 / A.6 MORE IMPLEMENTATION DETAILS - extractive PDF cue:** The output feature map is downsampled by a factor of 8 relative to the input image, yielding a resolution of 20 × 64 for KITTI ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Through L rounds of alternate interaction, the patch features are progressively refined with both global image context and geometry-aware cues from the point cloud, enabling ...
- **p. 4 / 3 METHOD - extractive PDF cue:** 3.1 OVERVIEW Given an image I ∈RH×W ×3 and a point cloud P ∈RN×3 from the same scene, our goal is to determine the camera ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** The central challenge lies in the heterogeneous nature of the input modalities: 2D images encode appearance information in dense, regular grids, whereas 3D point clouds ...
- **p. 5 / 3 METHOD - extractive PDF cue:** For the input point cloud P ∈RN×3, we use KPConv (Thomas et al., 2019) to extract downsampled point features FP ∈RNc×C.
- **p. 6 / 3 METHOD - extractive PDF cue:** Finally, two lightweight MLP heads take vpose as input and predict the rotation R and translation t, respectively.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Image-to-point cloud registration refers to the process of estimating the 6-degree-of-freedom (6DoF) camera pose of a given 2D image relative to a pre-constructed 3D point ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | While compact, this low-dimensional representation is difficult to regress directly from complex visual and geometric features because of strong geometric constraints and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | By bridging compact camera parameters and overparameterized ray bundles, this two-way conversion yields a representation that combines geometric interpretability with modeling flexibility, ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | In Table 2, we provide a comparison of model size and inference time across different methods, with results obtained on the same ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 METHOD - extractive PDF cue:** While compact, this low-dimensional representation is difficult to regress directly from complex visual and geometric features because of strong geometric constraints and nonlinearities.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** In Table 2, we provide a comparison of model size and inference time across different methods, with results obtained on the same machine using a ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** 4.1 IMPLEMENTATION DETAILS In this work, we implement the proposed model in Pytorch (Paszke et al., 2019) and adopt a single NVIDIA RTX 3090 GPU ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** As a result, our method achieves much faster inference time, making it more efficient without compromising performance.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We train the whole network with the total loss Ltotal for 20 epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** then, apply, transformer-based, fusion, module, Vaswani, consisting, multiple, self, cross, attention, layers, executed, alternate, fashion, iterations, encourage, image, patch, attend.
- **Relevant PDF headings:** 3 METHOD (p. 4); A.7 THE USE OF LARGE LANGUAGE MODELS (LLMS) (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.2 DATASETS We conduct experiments on two mostly used benchmarks: KITTI and nuScenes. | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Semantic / temporal fusion | 4.4 COMPARISON WITH STATE-OF-THE-ART METHODS Baselines. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Robot query / planning handoff | As a result, our method achieves much faster inference time, making it more efficient without compromising performance. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** To better understand the contribution of each component in our Ray-guided Pose Regression Module, we conduct ablation studies by selectively removing or replacing fused patch ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We investigate the effect of focus radius σ, which governs the spatial constraints in cross-attention between patch and point features.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** As a result, our method achieves much faster inference time, making it more efficient without compromising performance.
- **p. 15 / Figure/Table caption - extractive PDF cue:** Table 5: Ablation studies on patch size associated with each ray. Each ray corresponds to a p × p local image patch. p KITTI nuScenes ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 6: Ablation studies on focus radius σ. Here ✗indicates method that doesn't use Lfoc. σ KITTI nuScenes RTE(m)↓ RRE(◦)↓ Acc(%)↑ RTE(m)↓
- **p. 16 / A.5.2 FAILURE CASES UNDER COMPLETELY INCORRECT OVERLAP PREDICTION - extractive PDF cue:** This failure mode, although observed only in rare extreme cases, reveals a fundamental limitation of the current framework: when the predicted overlap region is entirely ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 5: Visual comparison between classical pose solver and our proposed ray-guided pose re- gression module. Classical pose solver suffers from unstable predictions under noisy ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), objective p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), temporal p. 4 (3 METHOD), p. 5 (3 METHOD), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
