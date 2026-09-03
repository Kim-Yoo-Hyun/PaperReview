# Method - Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (6.3. More implementation details and discussions), p. 1 (6. Implementation Details), p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction)): Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 0.051 0.012 0.084 0.023 0.080 0.010 0.071 0.014 ...

## Method Body Digest

- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 0.051 0.012 0.084 ...
- **p. 1 / 6. Implementation Details - extractive body cue:** For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training process takes approximately ...
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** 10: From a single input image, we first estimate the camera intrinsics and metric depth map, transform them into a 3D point cloud using the ...
- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** Based on this setting, we treat the metric depth with different scale factor for indoor and outdoor: s = {sin, sout}, and the depth label ...
- **p. 1 / 6.1. Camera intrinsic prediction - extractive body cue:** We train our model on a diverse range of datasets, ensuring balance by selecting one dataset per batch with equal probability and sampling from it.
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Dust3r [73] delivers less accurate intrinsic estimation because it focuses on sparseview reconstruction by generating point clouds for image pairs and performing global alignment to ...
- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** For metric depth prediction, we do not pad the images.

## Design Rationale

- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** In contrast, our method is specifically designed to recover camera intrinsics.
- **p. 2 / 7.5. Mesh Reconstruction - extractive body cue:** We present the reconstruction result of Pisa tower in Fig.
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** We present the predicted metric depth in both outdoor and indoor scenes.

## Source Evidence Cues

- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 0.051 0.012 0.084 ...
- **p. 1 / 6. Implementation Details - extractive body cue:** For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training process takes approximately ...
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** 10: From a single input image, we first estimate the camera intrinsics and metric depth map, transform them into a 3D point cloud using the ...
- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** Based on this setting, we treat the metric depth with different scale factor for indoor and outdoor: s = {sin, sout}, and the depth label ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 ... | p. 2 (6.3. More implementation details and discussions), p. 1 (6. Implementation Details) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training ... | p. 1 (6. Implementation Details), p. 2 (6.3. More implementation details and discussions) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 10: From a single input image, we first estimate the camera intrinsics and metric depth map, transform them into a 3D point ... | p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 0.051 0.012 0.084 ...
- **p. 1 / 6.1. Camera intrinsic prediction - extractive body cue:** We train our model on a diverse range of datasets, ensuring balance by selecting one dataset per batch with equal probability and sampling from it.
- **p. 1 / 6. Implementation Details - extractive body cue:** For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training process takes approximately ...
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Dust3r [73] delivers less accurate intrinsic estimation because it focuses on sparseview reconstruction by generating point clouds for image pairs and performing global alignment to ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (6.3. More implementation details and discussions).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | single, input, image, first, estimate, camera, intrinsics, metric, depth, transform, them, point, cloud, pinhole | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | single, input, image, first, estimate, camera, intrinsics, metric, depth, transform | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contrast, specifically, designed, recover, camera, intrinsics, present, reconstruction, result, Pisa | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Waymo, RGBD, ScanNet, MVS, Scenes11, Average, Ours-small, Ours, Pre-trained, Latent | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** 10: From a single input image, we first estimate the camera intrinsics and metric depth map, transform them into a 3D point cloud using the ...
- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** Based on this setting, we treat the metric depth with different scale factor for indoor and outdoor: s = {sin, sout}, and the depth label ...
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Dust3r [73] delivers less accurate intrinsic estimation because it focuses on sparseview reconstruction by generating point clouds for image pairs and performing global alignment to ...
- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** For metric depth prediction, we do not pad the images.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Additionally, we apply random horizontal flipping and random cropping to enhance dataset diversity even in one dataset. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | , R, t } \s u m _ { i} \left \Vert \sigma (R \X {1}{1}_i + t) - \X {1}{2}_i \right ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 0.051 0.012 0.084 ...
- **p. 1 / 6. Implementation Details - extractive body cue:** For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training process takes approximately ...
- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** Based on this setting, we treat the metric depth with different scale factor for indoor and outdoor: s = {sin, sout}, and the depth label ...
- **p. 1 / 6. Implementation Details - extractive body cue:** For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training process takes approximately ...
- **p. 1 / 6. Implementation Details - extractive body cue:** To train camera intrinsic estimation model, we employ the AdamW optimizer with a learning rate of 3e-5 and train the model for 30,000 iterations with ...
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** The encoded image and camera image zx and zc are concatenated and sent to pretrained U-Net.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Waymo, RGBD, ScanNet, MVS, Scenes11, Average, Ours-small, Ours, Pre-trained, Latent, Encoder, Stable, Diffusion, U-Net, Single, Step, Decoder, Training, Objective, Predicted.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Dataset Images Scene Intrinsic Training Set NuScenes [7] 28k Outdoor Calibrated KITTI [11] 18 k Outdoor Calibrated CityScapes [11] 23k Outdoor Calibrated ... | p. 1 (6.2. Metric depth prediction), p. 1 (6.2. Metric depth prediction) |
| Semantic / temporal fusion | 10: The pose estimation is compared against pseudo | p. 1 (6.3. More implementation details and discussions), p. 1 (6.1. Camera intrinsic prediction) |
| Robot query / planning handoff | Despite targeting metric depth, we achieve performance comparable to SoTA affine-invariant depth methods. | p. 4 (7.7. The Importance of Principal Point Evaluation), p. 5 (7.8. The Importance of camera image in metric) |

## Failure and Ablation Link

- **p. 5 / 7.8. The Importance of camera image in metric - extractive body cue:** Ablation study on the effectiveness of camera images for metric depth estimation. ibims Diode indoor Diode outdoor w. cam img 88.7 50.1 41.0 w.o cam ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 8. The overview of metric depth training pipeline. The encoded image and camera image zx and zc are concatenated and sent to pretrained U-Net. ...
- **p. 3 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** To validate this, we conduct an ablation study comparing
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** Quantitative Comparison on 5 Zero-shot Affine-invariant Depth Benchmarks.
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** Despite targeting metric depth, we achieve performance comparable to SoTA affine-invariant depth methods.
- **p. 5 / 7.9. Test-time ensembling - extractive body cue:** Without the aggregation, the standard deviation is sometimes not negligible, as presented in Tab.
- **p. 6 / 7.9. Test-time ensembling - extractive body cue:** Standard Deviation of estimated intrinsics without ensembling.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (6.3. More implementation details and discussions), p. 1 (6. Implementation Details), p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction), objective p. 2 (6.3. More implementation details and discussions), p. 1 (6.1. Camera intrinsic prediction), p. 1 (6. Implementation Details), p. 2 (6.3. More implementation details and discussions), temporal p. 1 (6.2. Metric depth prediction), p. 2 (6.3. More implementation details and discussions), p. 2 (6.3. More implementation details and discussions), p. 3 (7.7. The Importance of Principal Point Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
