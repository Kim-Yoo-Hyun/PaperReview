# Method - E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Edge-guided 3D reconstruction), p. 4 (3.1. Framework overview), p. 4 (3.1. Framework overview), p. 3 (3.1. Framework overview), p. 3 (3.1. Framework overview), p. 5 (3.4. Edge-guided 3D reconstruction)): To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.

## Method Body Digest

- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive PDF cue:** To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.
- **p. 4 / 3.1. Framework overview - extractive PDF cue:** This edgeaware initialization and optimization jointly refine the 3D Gaussian representation and camera trajectory, enabling robust pose estimation and high-quality reconstruction even in extended real-world ...
- **p. 4 / 3.1. Framework overview - extractive PDF cue:** During reconstruction, an edge-guided loss spatially weights the photometric error based on edge confidence, prioritizing optimization at geometrically salient boundaries (Sec.
- **p. 3 / 3.1. Framework overview - extractive PDF cue:** We adopt 3DGS [13] as our scene representation, where each Gaussian primitive is parameterized by center position µ ∈R3, covariance Σ ∈R3×3, opacity o, and ...
- **p. 3 / 3.1. Framework overview - extractive PDF cue:** Following IncEventGS [11], we process event streams in temporal chunks, each associated with a continuous trajectory parameterized by boundary poses Tstart and Tend ∈ SE(3).
- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive PDF cue:** This prioritizes optimization at geometrically salient boundaries, enabling faster convergence and more accurate depth estimation at object edges.
- **p. 3 / 3.1. Framework overview - extractive PDF cue:** Event supervision minimizes the discrepancy between the measured event map Et(x) and synthesized event map ˆEt(x) = log ˆIt+∆t(x) -log ˆIt(x), where ˆIt denotes the ...
- **p. 4 / 3.2. Robust edge detection with patch-based tem - extractive PDF cue:** This approach is inspired by contrast maximization [4], but rather than performing expensive trajectory estimation, we directly exploit temporal coherence to identify edge locations efficiently.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To overcome these limitations, we propose event-toedge Gaussian splatting (E2EGS), a pose-free framework that leverages edge information derived solely from event streams.
- **p. 2 / 1. Introduction - extractive PDF cue:** By initializing Gaussians along detected edges and applying edge-weighted losses throughout optimization, our framework prioritizes geometric constraints over texture matching, enabling accurate pose estimation and ...
- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive PDF cue:** To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.

## Source Evidence Cues

- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive PDF cue:** To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.
- **p. 4 / 3.1. Framework overview - extractive PDF cue:** This edgeaware initialization and optimization jointly refine the 3D Gaussian representation and camera trajectory, enabling robust pose estimation and high-quality reconstruction even in extended real-world ...
- **p. 4 / 3.1. Framework overview - extractive PDF cue:** During reconstruction, an edge-guided loss spatially weights the photometric error based on edge confidence, prioritizing optimization at geometrically salient boundaries (Sec.
- **p. 3 / 3.1. Framework overview - extractive PDF cue:** We adopt 3DGS [13] as our scene representation, where each Gaussian primitive is parameterized by center position µ ∈R3, covariance Σ ∈R3×3, opacity o, and ...
- **p. 3 / 3.1. Framework overview - extractive PDF cue:** Following IncEventGS [11], we process event streams in temporal chunks, each associated with a continuous trajectory parameterized by boundary poses Tstart and Tend ∈ SE(3).
- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive PDF cue:** This prioritizes optimization at geometrically salient boundaries, enabling faster convergence and more accurate depth estimation at object edges.
- **Detected method headings:** 3. Proposed Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence. | p. 5 (3.4. Edge-guided 3D reconstruction), p. 4 (3.1. Framework overview) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | This edgeaware initialization and optimization jointly refine the 3D Gaussian representation and camera trajectory, enabling robust pose estimation and high-quality reconstruction even ... | p. 4 (3.1. Framework overview), p. 4 (3.1. Framework overview) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | During reconstruction, an edge-guided loss spatially weights the photometric error based on edge confidence, prioritizing optimization at geometrically salient boundaries (Sec. | p. 4 (3.1. Framework overview), p. 3 (3.1. Framework overview) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Framework overview - extractive PDF cue:** During reconstruction, an edge-guided loss spatially weights the photometric error based on edge confidence, prioritizing optimization at geometrically salient boundaries (Sec.
- **p. 3 / 3.1. Framework overview - extractive PDF cue:** Event supervision minimizes the discrepancy between the measured event map Et(x) and synthesized event map ˆEt(x) = log ˆIt+∆t(x) -log ˆIt(x), where ˆIt denotes the ...
- **p. 4 / 3.2. Robust edge detection with patch-based tem - extractive PDF cue:** This approach is inspired by contrast maximization [4], but rather than performing expensive trajectory estimation, we directly exploit temporal coherence to identify edge locations efficiently.
- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive PDF cue:** To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.
- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive PDF cue:** Edge-weighted loss over pixel domain Ωcan be calculated with given edge map M, synthesized event accumulation ˆE, and ground truth event accumulation E as follows: ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.1. Framework overview), p. 5 (3.4. Edge-guided 3D reconstruction), p. 5 (3.4. Edge-guided 3D reconstruction), p. 4 (3.3. Edge-guided Gaussian initialization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | volumetric, representation, methods, typically, take, camera, poses, views, input, leveraging, multiview, images, learn, implicit | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | volumetric, representation, methods, typically, take, camera, poses, views, input, leveraging | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | overcome, limitations, event-toedge, Gaussian, splatting, E2EGS, pose-free, framework, leverages, edge | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | During, reconstruction, edge-guided, loss, spatially, weights, photometric, error, edge, confidence | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** These volumetric representation methods typically take camera poses and 2D views as input, leveraging multiview images to learn implicit or explicit 3D scene representations.
- **p. 4 / 3.2. Robust edge detection with patch-based tem - extractive PDF cue:** Edges with incorrectly estimated depth in previous frames can be identified and removed based on their inconsistency with current observations, ensuring only geometrically consistent edges ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Despite their remarkable success, these approaches fundamentally assume high-quality input images.
- **p. 3 / 3.1. Framework overview - extractive PDF cue:** Given consecutive event maps from the input stream, we first extract robust edge maps 4924
- **p. 3 / 3.1. Framework overview - extractive PDF cue:** Given camera pose T, images are rendered through differentiable α-blending of projected 2D Gaussians.
- **p. 4 / 3.3. Edge-guided Gaussian initialization - extractive PDF cue:** This distribution is geometrically motivated, as distant points exhibit larger pixel displacements under camera rotation, making them more informative for joint depth-pose optimization.
- **p. 5 / 3.3. Edge-guided Gaussian initialization - extractive PDF cue:** Our method achieves superior reconstruction quality solely using event data. † denotes no depth supervision and ∗denotes that the method uses camera poses obtained through ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Following IncEventGS [11], we process event streams in temporal chunks, each associated with a continuous trajectory parameterized by boundary poses Tstart and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For each spatial patch location Px,y = [x : x + p, y : y + p], we extract the temporal sequence ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** leverage, detected, edges, during, reconstruction, introduce, edge-guided, loss, spatially, weights, error, edge, confidence, edgeaware, initialization, optimization, jointly, refine, Gaussian, representation.
- **Relevant PDF headings:** 3. Proposed Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | IncEventGS† fails to reconstruct recognizable figurines and produces distorted scenes due to severe trajectory drift. | p. 6 (4.3. Qualitative evaluations), p. 5 (4.1. Experiment settings) |
| Semantic / temporal fusion | Our method produces sharper boundaries and cleaner surfaces compared with baselines. | p. 7 (4.3. Qualitative evaluations), p. 6 (4.2. Quantitative evaluations) |
| Robot query / planning handoff | Figure 6. Effect of edge ratio on reconstruction quality. Red boxes highlight comparison regions. (a) Ground truth. (b) Without edge guidance, fine ... | p. 8 (Figure/Table caption), p. 6 (4.2. Quantitative evaluations) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Effect of edge ratio on reconstruction quality. Red boxes highlight comparison regions. (a) Ground truth. (b) Without edge guidance, fine details such as ...
- **p. 7 / 4.4. Ablation study - extractive PDF cue:** To validate the contribution of each proposed component, we conduct component-wise ablation experiments.
- **p. 5 / 4.2. Quantitative evaluations - extractive PDF cue:** Without edge guidance, photometric error from event noise uniformly affects 3D reconstruction, causing optimization process to receive 4926
- **p. 6 / 4.2. Quantitative evaluations - extractive PDF cue:** Without requiring any depth supervision, our edge-guided approach outperforms DEVO [16] and IncEventGS† by substantial margins.
- **p. 7 / 4.3. Qualitative evaluations - extractive PDF cue:** Ablation study on edge ratio (redge).
- **p. 8 / 4.4. Ablation study - extractive PDF cue:** Without edge initialization, the system experiences trajectory drift, leading to loss of details in 3D reconstruction.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study on edge components.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.4. Edge-guided 3D reconstruction), p. 4 (3.1. Framework overview), p. 4 (3.1. Framework overview), p. 3 (3.1. Framework overview), p. 3 (3.1. Framework overview), p. 5 (3.4. Edge-guided 3D reconstruction), objective p. 4 (3.1. Framework overview), p. 3 (3.1. Framework overview), p. 4 (3.2. Robust edge detection with patch-based tem), p. 5 (3.4. Edge-guided 3D reconstruction), p. 5 (3.4. Edge-guided 3D reconstruction), temporal p. 3 (3.1. Framework overview), p. 4 (3.2. Robust edge detection with patch-based tem), p. 3 (3.1. Framework overview), p. 4 (3.1. Framework overview), p. 5 (4.1. Experiment settings), p. 5 (3.3. Edge-guided Gaussian initialization).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
