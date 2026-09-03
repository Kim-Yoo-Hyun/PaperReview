# Method - SDGS: Spatial Difference Guided Gaussian Splatting for Simultaneous Localization and 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3.2. SD Loss), p. 5 (3.2.2. Tracking), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation), p. 3 (3.1.2. Edge-aligned 3D Gaussian Representation), p. 6 (3.4.2. SD-guided Mutually Exclusive RGB Supervision), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation)): For SD photometric mapping, we use the loss defined as follows: \ m at hcal {L} _ { \te xt {sd}}=\bigl \/\, I(\mathcal {G}_A,T_{CW})-I_{\text {SD}} \,\bigr \/_{1}, (10) The final ...

## Method Body Digest

- **p. 5 / 3.3.2. SD Loss - extractive body cue:** For SD photometric mapping, we use the loss defined as follows: \ m at hcal {L} _ { \te xt {sd}}=\bigl \/\, I(\mathcal {G}_A,T_{CW})-I_{\text {SD}} ...
- **p. 5 / 3.2.2. Tracking - extractive body cue:** At each level, the SD observation is downsampled and its distance transform is computed once; we then directly render I(\mat hca l {G}_{\mathrm {SD}}, T_{CW} ...
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** With the estimated poses, we then promote keyframes for dense RGB reconstruction using SD-guided initialization and optimization.
- **p. 3 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** Our representation builds upon 3D Gaussian splatting, which uses spherical-harmonics (SH) coefficients to model view-dependent color.
- **p. 6 / 3.4.2. SD-guided Mutually Exclusive RGB Supervision - extractive body cue:** (15) For the total dense RGB mapping objective, our mutually exclusive training minimizes: \mat hc al { L} \;=\ ; \lambda _{\text {sd}}^{\text {rgb}}\,\mathcal {L}_{\text ...
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** This provides a compact and geometrically meaningful 3D edge representation of the scene.
- **p. 6 / 3.4.2. SD-guided Mutually Exclusive RGB Supervision - extractive body cue:** The SD loss is \m at h cal {L}_{\text {sd} } ^ {\ t e xt {r gb}}= \big \/\big (\mathcal {Q}_{b,\theta }(k\!\cdot \!
- **p. 4 / 3.2.2. Tracking - extractive body cue:** We minimize \mathca l { L}_{\t ext { trackin g} } = \big \/\, I(\mathcal {G}_{\mathrm {SD}}, T_{CW}) \odot DT(I_{\text {SD}}) \,\big \/_{1}, \label {eq:track-loss} ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We introduce a sparse edge descriptor using Gaussian ellipsoids as 3D representation, providing clear geometric cues while ...
- **p. 2 / 1. Introduction - extractive body cue:** Moreover, our method substantially reduces the resource overhead required for representing key geometries relative to fully dense approaches.
- **p. 5 / 3.2.2. Tracking - extractive body cue:** A Gaussian is marked as visible in the current view if its center falls within the observed depth range and has a non-negligible opacity contribution.

## Source Evidence Cues

- **p. 5 / 3.3.2. SD Loss - extractive body cue:** For SD photometric mapping, we use the loss defined as follows: \ m at hcal {L} _ { \te xt {sd}}=\bigl \/\, I(\mathcal {G}_A,T_{CW})-I_{\text {SD}} ...
- **p. 5 / 3.2.2. Tracking - extractive body cue:** At each level, the SD observation is downsampled and its distance transform is computed once; we then directly render I(\mat hca l {G}_{\mathrm {SD}}, T_{CW} ...
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** With the estimated poses, we then promote keyframes for dense RGB reconstruction using SD-guided initialization and optimization.
- **p. 3 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** Our representation builds upon 3D Gaussian splatting, which uses spherical-harmonics (SH) coefficients to model view-dependent color.
- **p. 6 / 3.4.2. SD-guided Mutually Exclusive RGB Supervision - extractive body cue:** (15) For the total dense RGB mapping objective, our mutually exclusive training minimizes: \mat hc al { L} \;=\ ; \lambda _{\text {sd}}^{\text {rgb}}\,\mathcal {L}_{\text ...
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** This provides a compact and geometrically meaningful 3D edge representation of the scene.
- **p. 6 / 3.4.2. SD-guided Mutually Exclusive RGB Supervision - extractive body cue:** The SD loss is \m at h cal {L}_{\text {sd} } ^ {\ t e xt {r gb}}= \big \/\big (\mathcal {Q}_{b,\theta }(k\!\cdot \!
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | For SD photometric mapping, we use the loss defined as follows: \ m at hcal {L} _ { \te xt {sd}}=\bigl \/\, ... | p. 5 (3.3.2. SD Loss), p. 5 (3.2.2. Tracking) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | At each level, the SD observation is downsampled and its distance transform is computed once; we then directly render I(\mat hca l ... | p. 5 (3.2.2. Tracking), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | With the estimated poses, we then promote keyframes for dense RGB reconstruction using SD-guided initialization and optimization. | p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation), p. 3 (3.1.2. Edge-aligned 3D Gaussian Representation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2.2. Tracking - extractive body cue:** We minimize \mathca l { L}_{\t ext { trackin g} } = \big \/\, I(\mathcal {G}_{\mathrm {SD}}, T_{CW}) \odot DT(I_{\text {SD}}) \,\big \/_{1}, \label {eq:track-loss} ...
- **p. 6 / 3.4.2. SD-guided Mutually Exclusive RGB Supervision - extractive body cue:** (15) For the total dense RGB mapping objective, our mutually exclusive training minimizes: \mat hc al { L} \;=\ ; \lambda _{\text {sd}}^{\text {rgb}}\,\mathcal {L}_{\text ...
- **p. 3 / 3.1.1. Sparse Edge Descriptor - extractive body cue:** Edges provide strong cues for object structure and geometry, and can be obtained from a variety of sources, ranging from simple image gradients to classical ...
- **p. 4 / 3.2.2. Tracking - extractive body cue:** We estimate the camera pose by aligning the rendered SD prediction of the sparse 3D map to the observed SD geometry with a DT-weighted objective.
- **p. 5 / 3.4.2. SD-guided Mutually Exclusive RGB Supervision - extractive body cue:** This removes supervision ambiguity between sharp gradients and 4864
- **p. 5 / 3.2.2. Tracking - extractive body cue:** While classical stereo matching methods can produce dense disparity on textured RGB frames, their window-based matching costs degrade under extreme blur or on binary/sparse edge ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1.1. Sparse Edge Descriptor), p. 4 (3.2.2. Tracking), p. 4 (3.2.2. Tracking), p. 5 (3.4.2. SD-guided Mutually Exclusive RGB Supervision), p. 5 (3.4.2. SD-guided Mutually Exclusive RGB Supervision), p. 6 (3.4.2. SD-guided Mutually Exclusive RGB Supervision).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | estimate, camera, poses, aligning, rendered, sparse, edge, input, image, distance, transform, SDGS, overview, uses | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | estimate, camera, poses, aligning, rendered, sparse, edge, input, image, distance | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, introduce, sparse, edge, descriptor, Gaussian, ellipsoids | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | minimize, mathca, trackin, mathcal, mathrm, odot, text, label, track-loss, rendered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** We estimate camera poses by aligning the rendered sparse edge map with the input edge image using a distance transform.
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** SDGS overview: our approach uses high-frame-rate SD inputs to optimize a sparse Gaussian map and performs camera pose estimation via edge alignment.
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We introduce a sparse edge descriptor using Gaussian ellipsoids as 3D representation, providing clear geometric cues while ...
- **p. 5 / 3.2.2. Tracking - extractive body cue:** At each level, the SD observation is downsampled and its distance transform is computed once; we then directly render I(\mat hca l {G}_{\mathrm {SD}}, T_{CW} ...
- **p. 5 / 3.3.1. SD Keyframe - extractive body cue:** To address this contradiction between sparse map and SD input, we then mark all visible Gaussians in the sliding window as active Gaussians \protect \mathcal ...
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, online systems must process input in real-time and can hardly control the quality of the incoming image stream.
- **p. 6 / 3.4.2. SD-guided Mutually Exclusive RGB Supervision - extractive body cue:** We gate pixel pairs whose input SD has strong responses with valid masks MSD.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Online Gaussian Splatting SLAM To enable real-time applications, recent works have attempted to integrate 6DoF camera pose estimation with 3DGS-based mapping into ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our main contributions are summarized as follows: • We introduce a sparse edge descriptor using Gaussian ellipsoids as 3D representation, providing clear ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3.4.2. SD-guided Mutually Exclusive RGB Supervision - extractive body cue:** (15) For the total dense RGB mapping objective, our mutually exclusive training minimizes: \mat hc al { L} \;=\ ; \lambda _{\text {sd}}^{\text {rgb}}\,\mathcal {L}_{\text ...
- **p. 5 / 3.2.2. Tracking - extractive body cue:** Instead, we run a pyramidal Lucas-Kanade (LK) [11] search constrained along the epipolar line, which exploits the high information content of SD edges and yields ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** photometric, mapping, loss, defined, follows, hcal, bigl, mathcal, text, bigr, final, then, lambda, semi-iso, level, observation, downsampled, distance, transform, computed.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To analyze our method under controllable settings, we construct a SD-Replica dataset by simulating the hybrid pixel camera's sampling process on the ... | p. 6 (4.1.2. Datasets), p. 6 (4.1.3. Evaluation Metrics) |
| Semantic / temporal fusion | 3, on SD-Replica room0, we consistently outperform the baseline MonoGS-RGBD in terms of PSNR, SSIM, and LPIPS. | p. 7 (4.2.2. Deblurring Metrics), p. 7 (4.2.1. Tracking Accuracy) |
| Robot query / planning handoff | 2, across three complex scenarios, while our method exhibits marginally lower overall tracking accuracy compared to the baseline approaches, it achieves a ... | p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.3. Ablation Study) |

## Failure and Ablation Link

- **p. 8 / 4.2.3. Performance Analysis - extractive body cue:** Ablation on TUM-RGBD (RMSE ATE [cm]). w/o = without; w/ = with; Pyr. = pyramid; Semi-iso = semi-isotropic.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** We conduct the ablation study of image pyramids and semiisotropic loss on TUM-RGBD dataset.
- **p. 8 / 5. Conclusion - extractive body cue:** By combining emerging hybrid pixel cameras, we not only maintain robust tracking accuracy under extreme motions where other methods fail, but also reconstruct dense maps ...
- **p. 8 / 5. Conclusion - extractive body cue:** Our system balances tracking robustness, high-fidelity reconstruction, and system efficiency.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Our approach follows a "sketch-then-paint" paradigm. Similar to drawing the outline before adding colors, we first generate a discrete outline (skeleton) for efficient ...
- **p. 6 / 4.1.2. Datasets - extractive body cue:** We evaluate our method on three datasets to verify both the robustness and generalization ability: SD-Replica Datasets.
- **p. 7 / 4.2.1. Tracking Accuracy - extractive body cue:** We first evaluate our method against state-of-the-art approaches in terms of tracking 6-DoF pose accuracy and robustness under various motion conditions, based on the stereo ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3.2. SD Loss), p. 5 (3.2.2. Tracking), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation), p. 3 (3.1.2. Edge-aligned 3D Gaussian Representation), p. 6 (3.4.2. SD-guided Mutually Exclusive RGB Supervision), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation), objective p. 4 (3.2.2. Tracking), p. 6 (3.4.2. SD-guided Mutually Exclusive RGB Supervision), p. 3 (3.1.1. Sparse Edge Descriptor), p. 4 (3.2.2. Tracking), p. 5 (3.4.2. SD-guided Mutually Exclusive RGB Supervision), p. 5 (3.2.2. Tracking), temporal p. 2 (2. Related Work), p. 2 (1. Introduction), p. 5 (3.4.1. RGB Keyframe Promotion), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1.1. Sparse Edge Descriptor).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
