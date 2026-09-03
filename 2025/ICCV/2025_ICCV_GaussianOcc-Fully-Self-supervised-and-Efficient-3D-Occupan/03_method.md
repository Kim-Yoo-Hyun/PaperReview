# Method - GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gan_GaussianOcc_Fully_Self-supervised_and_Efficient_3D_Occupancy_Estimation_with_Gaussian_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gan_GaussianOcc_Fully_Self-supervised_and_Efficient_3D_Occupancy_Estimation_with_Gaussian_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Fast rendering by Gaussian Splatting), p. 4 (3.2. Scale-aware training by Gaussian Splatting), p. 5 (4.2. Implementation details), p. 5 (4.2. Implementation details), p. 7 (Method), p. 3 (3.2. Scale-aware training by Gaussian Splatting)): Overlap mask in nuScenes [3] and DDAD [13]. though we have the vertices at that region during the splatting rendering, after the optimization, the network would predict the opacity as ...

## Method Body Digest

- **p. 4 / 3.3. Fast rendering by Gaussian Splatting - extractive body cue:** Overlap mask in nuScenes [3] and DDAD [13]. though we have the vertices at that region during the splatting rendering, after the optimization, the network ...
- **p. 4 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** We propose Gaussian splatting for projection in stage 1 for better scale-aware training as follows.
- **p. 5 / 4.2. Implementation details - extractive body cue:** For occupancy estimation, we use the same network as OccNeRF [53] to ensure a fair comparison.
- **p. 5 / 4.2. Implementation details - extractive body cue:** In the depth estimation benchmark, we use the network proposed by SimpleOcc, where the final output size is 256×256×16.
- **p. 7 / Method - extractive body cue:** Scale-aware training in [26, 43] Scale-aware training by ours RMSE Loss in [43] Loss in [26] GS loss Mask Erode Refine Abs Rel Sq Rel ...
- **p. 3 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** Inspired by the explicit sparse depth supervision in [43], we ask whether we can enforce the cross-view constraint on adjacent views more explicitly.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Our design allows us to benefit from the Gaussian splatting rendering for the scale-aware training by cross-view constraint and faster rendering on voxel grids, as ...
- **p. 7 / Method - extractive body cue:** GS loss means using the spatial context constraint by our proposed Gaussian splatting for projection.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our core contributions are as follows: • We introduce the first fully self-supervised method for efficient surrounding-view 3D occupancy estimation, featuring the exploration ...
- **p. 2 / 1. Introduction - extractive body cue:** Instead, we propose performing Gaussian splatting directly from the 3D voxel space.
- **p. 4 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** We propose Gaussian splatting for projection in stage 1 for better scale-aware training as follows.

## Source Evidence Cues

- **p. 4 / 3.3. Fast rendering by Gaussian Splatting - extractive body cue:** Overlap mask in nuScenes [3] and DDAD [13]. though we have the vertices at that region during the splatting rendering, after the optimization, the network ...
- **p. 4 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** We propose Gaussian splatting for projection in stage 1 for better scale-aware training as follows.
- **p. 5 / 4.2. Implementation details - extractive body cue:** For occupancy estimation, we use the same network as OccNeRF [53] to ensure a fair comparison.
- **p. 5 / 4.2. Implementation details - extractive body cue:** In the depth estimation benchmark, we use the network proposed by SimpleOcc, where the final output size is 256×256×16.
- **p. 7 / Method - extractive body cue:** Scale-aware training in [26, 43] Scale-aware training by ours RMSE Loss in [43] Loss in [26] GS loss Mask Erode Refine Abs Rel Sq Rel ...
- **p. 3 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** Inspired by the explicit sparse depth supervision in [43], we ask whether we can enforce the cross-view constraint on adjacent views more explicitly.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Our design allows us to benefit from the Gaussian splatting rendering for the scale-aware training by cross-view constraint and faster rendering on voxel grids, as ...
- **Detected method headings:** 3. Method (p. 3); Method (p. 5); Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Overlap mask in nuScenes [3] and DDAD [13]. though we have the vertices at that region during the splatting rendering, after the ... | p. 4 (3.3. Fast rendering by Gaussian Splatting), p. 4 (3.2. Scale-aware training by Gaussian Splatting) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We propose Gaussian splatting for projection in stage 1 for better scale-aware training as follows. | p. 4 (3.2. Scale-aware training by Gaussian Splatting), p. 5 (4.2. Implementation details) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | For occupancy estimation, we use the same network as OccNeRF [53] to ensure a fair comparison. | p. 5 (4.2. Implementation details), p. 5 (4.2. Implementation details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / Method - extractive body cue:** GS loss means using the spatial context constraint by our proposed Gaussian splatting for projection.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** The original Gaussian splatting is for scene-specific, fast 3D novel view synthesis, where the attributes of Gaussian points are optimized by the multi-view constraint.
- **p. 3 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** Inspired by the explicit sparse depth supervision in [43], we ask whether we can enforce the cross-view constraint on adjacent views more explicitly.
- **p. 4 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** that the nature of Gaussian splatting is scale-aware projection that could serve for the cross-view stereo constraint.
- **p. 4 / 3.4. Loss function - extractive body cue:** Note that \protect \hat {I}_ t in the temporal-view photometric loss \protect \mathcal {L}_{temporal} is generated by projecting pixels from the source image using the ...
- **p. 5 / 4.2. Implementation details - extractive body cue:** In our Gaussian splatting setting, we further upsample the final output to 512×512×32 for improved performance since we observe that a finer voxel grid leads ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 7 (Method), p. 3 (3.2. Scale-aware training by Gaussian Splatting), p. 3 (3.1. Preliminaries), p. 4 (3.2. Scale-aware training by Gaussian Splatting), p. 4 (3.4. Loss function), p. 7 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | depth, estimation, benchmark, network, SimpleOcc, where, final, output, size, Gaussian, splatting, setting, further, upsample | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | depth, estimation, benchmark, network, SimpleOcc, where, final, output, size, Gaussian | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, core, contributions, follows, introduce, first, fully, self-supervised, efficient, surrounding-view | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | loss, means, spatial, context, constraint, Gaussian, splatting, projection, original, scene-specific | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4.2. Implementation details - extractive body cue:** In the depth estimation benchmark, we use the network proposed by SimpleOcc, where the final output size is 256×256×16.
- **p. 5 / 4.2. Implementation details - extractive body cue:** In our Gaussian splatting setting, we further upsample the final output to 512×512×32 for improved performance since we observe that a finer voxel grid leads ...
- **p. 4 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** If the depth map is accurately learned, the rendered image should resemble the original images, providing the necessary scale information for the joint training with ...
- **p. 7 / Method - extractive body cue:** The comparison of the depth map and its synthesis overlap image with (1) direct bilinear interpolation cross-view synthesis [43] and (2) our cross-view Gaussian splatting ...
- **p. 3 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** Inspired by the explicit sparse depth supervision in [43], we ask whether we can enforce the cross-view constraint on adjacent views more explicitly.
- **p. 3 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** Therefore, apart from the spatial loss, [43] proposes to facilitate the Structure-fromMotion (SFM) to extract sparse depth information for direct depth supervision to provide a ...
- **p. 4 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** Due to the presence of the other side's overlap region, the unprojected 3D scene remains complete if the depth map is predicted well.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | R3D3 [37] is a temporal offline refinement method that requires multiframe optimization, as discussed in [21]. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Different from [43], [26] enhances the depth estimation performance with spatio-temporal context that does not need the sparse depth from SFM but ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | The render time is calculated from surround 6 images. "N/A" indicates out-of-memory errors running in NVIDIA A 100 (40 GB). | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We train the models for 12 epochs on both the nuScenes and DDAD. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** We propose Gaussian splatting for projection in stage 1 for better scale-aware training as follows.
- **p. 7 / Method - extractive body cue:** Scale-aware training in [26, 43] Scale-aware training by ours RMSE Loss in [43] Loss in [26] GS loss Mask Erode Refine Abs Rel Sq Rel ...
- **p. 3 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** Inspired by the explicit sparse depth supervision in [43], we ask whether we can enforce the cross-view constraint on adjacent views more explicitly.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Our design allows us to benefit from the Gaussian splatting rendering for the scale-aware training by cross-view constraint and faster rendering on voxel grids, as ...
- **p. 5 / 4.2. Implementation details - extractive body cue:** We train the models for 12 epochs on both the nuScenes and DDAD.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Overlap, mask, nuScenes, DDAD, though, have, vertices, region, during, splatting, rendering, after, optimization, network, would, predict, opacity, zero, then, contribute.
- **Relevant PDF headings:** 3. Method (p. 3); Method (p. 5); Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Tasks, datasets, and metric nuScenes [3]: For 3D occupancy estimation, we utilize annotations from Occ3D [40]. | p. 4 (4. Experiment), p. 5 (4.3. Main results) |
| Semantic / temporal fusion | 3D occupancy estimation in nuScenes: In Table 1, the proposed GaussianOcc achieves the best performance compared to other self-supervised methods. | p. 5 (4.3. Main results), p. 5 (4.3. Main results) |
| Robot query / planning handoff | In stage 1, GaussianOcc ‡ achieves top performance on the nuScenes dataset and delivers competitive results on the DDAD. | p. 5 (4.3. Main results), p. 5 (4.3. Main results) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Problem setting of GaussianOcc. Given a surround image sequence, the spatial camera extrinsic and its correspond- ing 2D semantic annotation, GaussianOcc is able ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Comparisons for self-supervised multi-camera depth estimation on the nuScenes [3] and DDAD datasets [13]. The results are averaged over all views without median ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation study for scale-aware depth estimation on the nuScenes dataset [3]. ✓* means the result from the original paper and ✓means the result ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Comparison of the render result between the volume ren- dering (VR) [53] and splatting rendering (SR, Ours) on depth es- timation task [3]. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. The comparison for the depth map in the different set- ting, corresponding to the training strategy in Table 4 and render- ing type ...
- **p. 5 / 4.3. Main results - extractive body cue:** As highlighted by the red rectangle, the sky region has a short-range depth value, but this does not appear in the rendered 3D occupancy estimation ...
- **p. 5 / 4.3. Main results - extractive body cue:** Note that RenderOcc [36] does not require the 3D occupancy label, but it is not a self-supervised method since it uses the ground truth depth ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.3. Fast rendering by Gaussian Splatting), p. 4 (3.2. Scale-aware training by Gaussian Splatting), p. 5 (4.2. Implementation details), p. 5 (4.2. Implementation details), p. 7 (Method), p. 3 (3.2. Scale-aware training by Gaussian Splatting), objective p. 7 (Method), p. 3 (3.1. Preliminaries), p. 3 (3.2. Scale-aware training by Gaussian Splatting), p. 4 (3.2. Scale-aware training by Gaussian Splatting), p. 4 (3.4. Loss function), p. 5 (4.2. Implementation details), temporal p. 5 (4.3. Main results), p. 3 (3.2. Scale-aware training by Gaussian Splatting), p. 4 (3.2. Scale-aware training by Gaussian Splatting), p. 4 (3.4. Loss function), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
