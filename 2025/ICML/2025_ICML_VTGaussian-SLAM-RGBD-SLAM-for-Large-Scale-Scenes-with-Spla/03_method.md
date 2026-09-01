# Method - VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vkmi3jZtYG; PDF retrieval source: https://openreview.net/pdf/dae8bd9e8c76def61a96abb84032adda148950a0.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 4 (3.3. Tracking Cameras), p. 5 (3.5. Bundle Adjustment)): We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where LS is the SSIM loss, Ui is a ...

## Method Body Digest

- **p. 5 / 3.4. Mapping Scenes - extractive PDF cue:** We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where LS is the ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** At each frame out of a 2000 frame video, the average error of relative pose to the previous frame is pretty small, while the average ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** Although better renderings are helpful for more accurate camera pose estimations, the higher accuracy is merely meaningful relative to the neighboring frames, resulting in a ...
- **p. 5 / 3.5. Bundle Adjustment - extractive PDF cue:** 2 in the optimization, but also back-propagate gradients to update the camera pose of the head frame.
- **p. 3 / 3.3. Tracking Cameras - extractive PDF cue:** When tracking cameras, we keep all Gaussians in the scene fixed, and merely optimize the pose pi by minimizing rendering errors with respect to {Vi, ...
- **p. 3 / 3.1. Overview - extractive PDF cue:** For tracking the latest frame, we select Gaussians in a section, render them from the camera pose initialized by the constant speed assumption, and optimize ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** Otherwise, if the latest frame {Vi, Di} is a regular frame in the current section Sk, we will optimize the camera pose pi using the ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** We optimize pi to minimize rendering errors, min pi αWi//Vi -V ′ i //1 + βWi//Di -D′ i//1, (1) where {V ′ i , D′ ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions are listed below. • We propose view-tied Gaussian splatting that significantly reduces storage but improves rendering quality with 3DGS in SLAM. • ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Our method introduces a novel point-based volume representation, dubbed view-tied 3D Gaussians, to represent the color and 1
- **p. 1 / 1. Introduction - extractive PDF cue:** To overcome this challenge, we propose an RGBD SLAM system with splatting view-tied 3D Gaussians.

## Source Evidence Cues

- **p. 5 / 3.4. Mapping Scenes - extractive PDF cue:** We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where LS is the ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** At each frame out of a 2000 frame video, the average error of relative pose to the previous frame is pretty small, while the average ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** Although better renderings are helpful for more accurate camera pose estimations, the higher accuracy is merely meaningful relative to the neighboring frames, resulting in a ...
- **p. 5 / 3.5. Bundle Adjustment - extractive PDF cue:** 2 in the optimization, but also back-propagate gradients to update the camera pose of the head frame.
- **Detected method headings:** 3. Methods (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where ... | p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | At each frame out of a 2000 frame video, the average error of relative pose to the previous frame is pretty small, ... | p. 4 (3.3. Tracking Cameras), p. 4 (3.3. Tracking Cameras) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Although better renderings are helpful for more accurate camera pose estimations, the higher accuracy is merely meaningful relative to the neighboring frames, ... | p. 4 (3.3. Tracking Cameras), p. 5 (3.5. Bundle Adjustment) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Mapping Scenes - extractive PDF cue:** We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where LS is the ...
- **p. 5 / 3.5. Bundle Adjustment - extractive PDF cue:** 2 in the optimization, but also back-propagate gradients to update the camera pose of the head frame.
- **p. 3 / 3.3. Tracking Cameras - extractive PDF cue:** When tracking cameras, we keep all Gaussians in the scene fixed, and merely optimize the pose pi by minimizing rendering errors with respect to {Vi, ...
- **p. 3 / 3.1. Overview - extractive PDF cue:** For tracking the latest frame, we select Gaussians in a section, render them from the camera pose initialized by the constant speed assumption, and optimize ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** Otherwise, if the latest frame {Vi, Di} is a regular frame in the current section Sk, we will optimize the camera pose pi using the ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** We optimize pi to minimize rendering errors, min pi αWi//Vi -V ′ i //1 + βWi//Di -D′ i//1, (1) where {V ′ i , D′ ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.5. Bundle Adjustment), p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 4 (3.3. Tracking Cameras).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | minimize, rendering, errors, respect, observations, Vi-V, Ui//Di-D, i//1, where, SSIM, loss, mask, removes, pixels | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | minimize, rendering, errors, respect, observations, Vi-V, Ui//Di-D, i//1, where, SSIM | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, listed, below, view-tied, Gaussian, splatting, significantly, reduces, storage | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | minimize, rendering, errors, respect, observations, Vi-V, Ui//Di-D, i//1, where, SSIM | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.4. Mapping Scenes - extractive PDF cue:** We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where LS is the ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** We optimize pi to minimize rendering errors, min pi αWi//Vi -V ′ i //1 + βWi//Di -D′ i//1, (1) where {V ′ i , D′ ...
- **p. 3 / 3.2. View-tied Gaussians - extractive PDF cue:** For the i-th frame with a RGB Vi and a depth map Di, we will initialize Gaussians {gi j} on Di.
- **p. 3 / 3.2. View-tied Gaussians - extractive PDF cue:** We remove the need of learning and storing locations by tying a Gaussian g at each pixel with a valid depth value on the depth ...
- **p. 4 / 3.3. Tracking Cameras - extractive PDF cue:** For a head frame {Vi, Di}, we project the depth Di from the initialized pose to each one frame in the overlap candidate view list.
- **p. 5 / 3.4. Mapping Scenes - extractive PDF cue:** In each section, we first initialize Gaussians at all pixels on the depth map at the head frame, and then complement Gaussians at pixels uncovered ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our tracking and mapping strategies remove the need of holding and optimizing all Gaussians in memory throughout the training, which improves the scalability of 3DGS ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | With view-tied Gaussians, we manage to keep learnable Gaussians that are the most relevant to the latest frame in the GPU memory. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We organize view-tied 3D Gaussians from several consecutive frames as a section so that we can keep as many Gaussians as the ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | With view-tied Gaussians, we manage to keep learnable Gaussians that are the most relevant to the latest frame in the GPU memory. | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Note that ScanNet++ is not a dataset designed for SLAM tasks, some sudden large motions are occurring in the DSLR-captured sequences, we ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** minimize, rendering, errors, respect, observations, Vi-V, Ui//Di-D, i//1, where, SSIM, loss, mask, removes, pixels, without, valid, depth, values, balance, weights.
- **Relevant PDF headings:** 3. Methods (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | TUM-RGBD, ScanNet, and ScanNet++ are real-world datasets. | p. 5 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis) |
| Global / local decision | Compared to previous GS-based SLAM methods, our method can use many more Gaussians tied at each pixel on depth images to fit ... | p. 7 (4.1. Comparisons), p. 6 (4.1. Comparisons) |
| Motion execution / recovery | Based on the camera poses, our method also significantly improves the rendering quality on ScanNet, as shown in Fig. | p. 7 (4.1. Comparisons), p. 8 (4.2. Ablation Studies and Analysis) |

## Failure and Ablation Link

- **p. 8 / 4.2. Ablation Studies and Analysis - extractive PDF cue:** We conduct experiments to highlight the effect of view-tied Gaussians in Tab.
- **p. 8 / 4.2. Ablation Studies and Analysis - extractive PDF cue:** We also show the effect of learnable locations with our simplified Gaussians ("iso + w/o VT").
- **p. 7 / 4.1. Comparisons - extractive PDF cue:** Compared to previous GS-based SLAM methods, our method can use many more Gaussians tied at each pixel on depth images to fit sudden color change ...
- **p. 9 / 4.2. Ablation Studies and Analysis - extractive PDF cue:** Ablation study on the length of section S, overlap selecting strategy, and visible mask.
- **p. 9 / 4.2. Ablation Studies and Analysis - extractive PDF cue:** Ablation study on attributes of 3D Gaussians (aniso: anisotropic Gaussians, iso: isotropic Gaussians, VT: view-tied Gaussians).
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview. (a) and (c) are tracking strategies, while (b) and (d) are mapping strategies. Please refer to Sec. 3.1 for more details. geometry ...
- **p. 8 / 4.2. Ablation Studies and Analysis - extractive PDF cue:** We cannot use a large number of Gaussians 8

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 4 (3.3. Tracking Cameras), p. 5 (3.5. Bundle Adjustment), objective p. 5 (3.4. Mapping Scenes), p. 5 (3.5. Bundle Adjustment), p. 3 (3.3. Tracking Cameras), p. 3 (3.1. Overview), p. 4 (3.3. Tracking Cameras), p. 4 (3.3. Tracking Cameras), temporal p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.3. Tracking Cameras), p. 5 (4. Experiments and Analysis), p. 9 (4.2. Ablation Studies and Analysis), p. 4 (3.3. Tracking Cameras).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
