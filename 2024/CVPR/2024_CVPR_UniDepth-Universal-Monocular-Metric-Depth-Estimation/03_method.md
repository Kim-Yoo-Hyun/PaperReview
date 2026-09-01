# Method - UniDepth: Universal Monocular Metric Depth Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.18913; PDF retrieval source: https://arxiv.org/pdf/2403.18913. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss)): To this end, we propose a geometric invariance loss to enforce the consistency of camera-prompted depth features of the same scene from different acquisition sensors.

## Method Body Digest

- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** To this end, we propose a geometric invariance loss to enforce the consistency of camera-prompted depth features of the same scene from different acquisition sensors.
- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** Otherwise, the loss would enforce consistency across features that inherently carry distinct camera information.
- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** The bi-directional loss can be computed as: 1 2(Lcon(D1/E1, D2/E2)+Lcon(D2/E2, D1/E1)).
- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** Therefore, the geometric invariance loss can be expressed as \begin {s plit} & \mat h c al
- **p. 1 / 1. Introduction - extractive PDF cue:** We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, delivering reliable metric scaled depth outputs is necessary to perform 3D reconstruction effectively, thus motivating the challenging and inherently illposed task of Monocular Metric ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We propose an effective pseudo-spherical representation of the output space to disentangle the camera and depth dimensions of this space.
- **p. 2 / 1. Introduction - extractive PDF cue:** Second, we propose a pseudo-spherical representation of the output space, thus solving the intertwined nature of camera and depth prediction.

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.
- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, we introduce a geometric invariance loss to enhance the robustness of depth estimation.
- **p. 2 / 1. Introduction - extractive PDF cue:** We propose an effective pseudo-spherical representation of the output space to disentangle the camera and depth dimensions of this space.

## Source Evidence Cues

- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** To this end, we propose a geometric invariance loss to enforce the consistency of camera-prompted depth features of the same scene from different acquisition sensors.
- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** Otherwise, the loss would enforce consistency across features that inherently carry distinct camera information.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To this end, we propose a geometric invariance loss to enforce the consistency of camera-prompted depth features of the same scene from ... | p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Otherwise, the loss would enforce consistency across features that inherently carry distinct camera information. | p. 4 (3.3. Geometric Invariance Loss) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To this end, we propose a geometric invariance loss to enforce the consistency of camera-prompted depth features of the same scene from ... | p. 4 (3.3. Geometric Invariance Loss) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** The bi-directional loss can be computed as: 1 2(Lcon(D1/E1, D2/E2)+Lcon(D2/E2, D1/E1)).
- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** Therefore, the geometric invariance loss can be expressed as \begin {s plit} & \mat h c al
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | introduce, UniDepth, novel, directly, predicts, points, scene, only, image, input, However, delivering, reliable, metric | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | introduce, UniDepth, novel, directly, predicts, points, scene, only, image, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, UniDepth, novel, directly, predicts, points, scene, only, image, input | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | bi-directional, loss, computed, Lcon, D1/E1, D2/E2, Therefore, geometric, invariance, expressed | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, delivering reliable metric scaled depth outputs is necessary to perform 3D reconstruction effectively, thus motivating the challenging and inherently illposed task of Monocular Metric ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We propose an effective pseudo-spherical representation of the output space to disentangle the camera and depth dimensions of this space.
- **p. 2 / 1. Introduction - extractive PDF cue:** Second, we propose a pseudo-spherical representation of the output space, thus solving the intertwined nature of camera and depth prediction.
- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** To this end, we propose a geometric invariance loss to enforce the consistency of camera-prompted depth features of the same scene from different acquisition sensors.
- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** Relying on external input inherently leads to being subject to its noise.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For the sake of fair comparison, we provide in Table 4 a comparison between Metric3D, iDisc, and UniDepth where the latter two ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The critical step involves extracting azimuth and elevation from the backprojected rays, effectively creating a "dense" angular camera representation. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We run 1M optimization iterations with a batch size of 128, each training dataset is uniformly represented in each batch.
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** As the learning rate scheduler, we exploit Cosine Annealing to one-tenth starting from 30% of the training.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** The required training time amounts to roughly 12 days on 8 NVIDIA A100.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Ablations are conducted with three different seeds and for 100k training iterations, using a randomly sampled subset with a size equal to 20% of the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** geometric, invariance, loss, enforce, consistency, camera-prompted, depth, features, same, scene, different, acquisition, sensors, Otherwise, would, across, inherently, carry, distinct, camera.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The resulting dataset amounts roughly to 3M real-world images with different cameras and domains, compared to, e.g. | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Semantic / temporal fusion | The Oracle model demonstrates more robust scale-dependent performance during zero-shot testing compared to the Full model, highlighting how the proposed task is ... | p. 7 (4.3. Ablation Study), p. 8 (Figure/Table caption) |
| Robot query / planning handoff | Importantly, the KITTI Depth Prediction Benchmark, which provides a perfectly fair evaluation, underscores the excellent zero-shot performance of our method and its ... | p. 6 (4.2. Comparison with the State of the Art), p. 6 (4.2. Comparison with the State of the Art) |

## Failure and Ablation Link

- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** In Table 5, row 3, the benefit of the Camera Module becomes apparent, revealing a substantial disparity in the effect of this module on scale-invariant ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** Nonetheless, we present results both with and without GT intrinsics for UniDepth.
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** More precisely, each method is tested on validation splits from SUN-RGBD [48] without NYU split, Diode Indoor [50] , IBims-1 [26], VOID [54] HAMMER [25], ...
- **p. 6 / 4.2. Comparison with the State of the Art - extractive PDF cue:** FA drop is 11.8% and 31.4%, respectively, although having a clear scale-invariant improvement of 36.9% and 28.5%.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** All methods are tested in a zero-shot setting on eight different datasets without overlap with any of the sets used for training.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** All ablations exploit the predicted camera representation, if not stated otherwise.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** All ablations employ the same loss LλMSE, but across different output spaces.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss), objective p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss), temporal p. 6 (4.2. Comparison with the State of the Art), p. 4 (3.2. Self-Promptable Camera).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
