# Method - EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Lf0W2gmNBg; PDF retrieval source: https://arxiv.org/pdf/2512.00771. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 19 (A.5.4 Feature Strategy for Global Optimization)): These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure.

## Method Body Digest

- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure.
- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** To improve the stability of global optimization, the feature selection strategy in EAG3R focuses on Harris corners, which represent sparse yet highly stable points with ...
- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** It is observed in A.6 that random sampling introduces noisy gradients by selecting unreliable regions, thereby degrading optimization stability.
- **p. 20 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** Method ATE ↓ RPE trans ↓ RPE rot ↓ Computation Cost Random Sampling 0.687 0.261 0.153 Low SuperPoint [12] 0.685 0.260 0.153 High Harris Corner ...
- **p. 2 / 1 Introduction - extractive body cue:** EAG3R Input low light video Input event stream Lalign Lflow Lsmooth Levent Pointmaps Variables of Optimization {X, P, K} Depth Camera Pose Camera Intrinsics Object ...
- **p. 1 / 1 Introduction - extractive body cue:** Estimating geometry from videos or images is a fundamental problem in 3D vision, with broad applications in camera pose estimation, novel view synthesis, geometry reconstruction, ...
- **p. 2 / 1 Introduction - extractive body cue:** These pointmaps are jointly optimized under alignment, flow, smoothness, and event-based consistency losses to recover a global dynamic point cloud and per-frame camera poses and ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent methods like DUSt3R [64] have shown that regressing dense pointmaps from image pairs using transformer-based foundation models enables accurate and efficient pose-free 3D reconstruction.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose EAG3R, an event-augemented MonST3R framework to enhance pointmapbased 3D geometry estimation under dynamic and extremely low-light conditions.
- **p. 1 / 1 Introduction - extractive body cue:** Recent methods like DUSt3R [64] have shown that regressing dense pointmaps from image pairs using transformer-based foundation models enables accurate and efficient pose-free 3D reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** This unified representation enables efficient downstream tasks such as depth estimation and camera pose estimation, under challenging lighting conditions. and neural rendering [48, 25], but ...

## Source Evidence Cues

- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure.
- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** To improve the stability of global optimization, the feature selection strategy in EAG3R focuses on Harris corners, which represent sparse yet highly stable points with ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure. | p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 19 (A.5.4 Feature Strategy for Global Optimization) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To improve the stability of global optimization, the feature selection strategy in EAG3R focuses on Harris corners, which represent sparse yet highly ... | p. 19 (A.5.4 Feature Strategy for Global Optimization) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure. | p. 19 (A.5.4 Feature Strategy for Global Optimization) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure.
- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** It is observed in A.6 that random sampling introduces noisy gradients by selecting unreliable regions, thereby degrading optimization stability.
- **p. 20 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** Method ATE ↓ RPE trans ↓ RPE rot ↓ Computation Cost Random Sampling 0.687 0.261 0.153 Low SuperPoint [12] 0.685 0.260 0.153 High Harris Corner ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 19 (A.5.4 Feature Strategy for Global Optimization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | EAG3R, Input, light, video, event, stream, Lalign, Lflow, Lsmooth, Levent, Pointmaps, Variables, Optimization, Depth | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | EAG3R, Input, light, video, event, stream, Lalign, Lflow, Lsmooth, Levent | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | EAG3R, event-augemented, MonST3R, framework, enhance, pointmapbased, geometry, estimation, under, dynamic | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | features, provide, high-confidence, geometric, constraints, enhance, convergence, optimization, camera, pose | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** EAG3R Input low light video Input event stream Lalign Lflow Lsmooth Levent Pointmaps Variables of Optimization {X, P, K} Depth Camera Pose Camera Intrinsics Object ...
- **p. 1 / 1 Introduction - extractive body cue:** Estimating geometry from videos or images is a fundamental problem in 3D vision, with broad applications in camera pose estimation, novel view synthesis, geometry reconstruction, ...
- **p. 2 / 1 Introduction - extractive body cue:** These pointmaps are jointly optimized under alignment, flow, smoothness, and event-based consistency losses to recover a global dynamic point cloud and per-frame camera poses and ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent methods like DUSt3R [64] have shown that regressing dense pointmaps from image pairs using transformer-based foundation models enables accurate and efficient pose-free 3D reconstruction.
- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure.
- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** The proposed Harris-based strategy provides a balanced solution, introducing stable and targeted supervision signals that improve convergence while maintaining computational efficiency.
- **p. 20 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** The proposed Harris-corner approach achieves the best trade-off between accuracy and computational efficiency.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For daytime sequences, where APS operates at 100 Hz, we associate each depth ground truth from the Velodyne Puck LITE with the ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | During nighttime sequences, the APS frame rate drops to 10 Hz, resulting in multiple depth measurements (at 20 Hz) per APS frame. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For daytime sequences, where APS operates at 100 Hz, we associate each depth ground truth from the Velodyne Puck LITE with the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** features, provide, high-confidence, geometric, constraints, enhance, convergence, optimization, camera, pose, structure, improve, stability, global, feature, selection, strategy, EAG3R, focuses, Harris.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To assess the model's performance in high-dynamic-range (HDR) conditions, we evaluated EAG3R on the challenging M3ED robot dog dataset penno_plaza_lights split, which ... | p. 21 (A.7 Generalization to More Datasets), p. 18 (A.4 Summary of Existing Event-RGB Datasets) |
| Semantic / temporal fusion | Our method, EAG3R, outperforms all baselines across all three nighttime sequences, indicating both accurate and reliable depth predictions. | p. 8 (4 Experiments), p. 20 (A.6 Runtime and Memory Analysis) |
| Robot query / planning handoff | Each addition improves performance, with the full EAG3R system achieving the best results. | p. 9 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive body cue:** Fine-tuning MonST3R leads to substantial gains, particularly in RPE trans and RPE rot, with further improvements from Easi3R variants.
- **p. 9 / 4 Experiments - extractive body cue:** 4.5 Ablation Study To better understand the contribution of each design component in EAG3R, we conduct a systematic ablation study on the MVSEC outdoor_night3 sequence ...
- **p. 7 / 4 Experiments - extractive body cue:** We perform ablation studies in Section 4.5.
- **p. 7 / 4 Experiments - extractive body cue:** We report results using standard metrics: Absolute Relative Error (Abs Rel ↓), Scale-invariant RMSE log (RMSE log ↓), and the threshold accuracy δ < 1.25 ...
- **p. 8 / 4 Experiments - extractive body cue:** Prior methods such as DUSt3R and MonST3R serve as RGB-based baselines, with MonST3R extending pointmap prediction to dynamic scenes and Easi3R variants incorporating motion-aware masking.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Ablation study on depth estimation performance on the Night3 sequence. Modules are incrementally added to the MonST3R baseline. Each addition improves performance, with ...
- **p. 21 / A.7 Generalization to More Datasets - extractive body cue:** As reported in Table A.12, EAG3R achieves the best results across all key depth metrics, surpassing both the baseline and its finetuned variant by a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 19 (A.5.4 Feature Strategy for Global Optimization), objective p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 20 (A.5.4 Feature Strategy for Global Optimization), temporal p. 16 (A.1.1 Daytime Sequence Processing), p. 16 (A.1.2 Nighttime Sequence Processing), p. 2 (1 Introduction), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
