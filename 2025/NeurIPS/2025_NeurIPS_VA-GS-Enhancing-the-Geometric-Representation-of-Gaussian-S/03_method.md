# Method - VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via View Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ZnsR3waLUo; PDF retrieval source: https://openreview.net/pdf/74577aad9a08ae8d5d8bdf6091974f7d026891a3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4 Method), p. 6 (4 Method), p. 6 (4 Method), p. 5 (4 Method), p. 5 (4 Method), p. 4 (4 Method)): To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary details: LI = (1 -β1)L1( ˜I -I) + ...

## Method Body Digest

- **p. 4 / 4 Method - extractive PDF cue:** To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary details: LI = ...
- **p. 6 / 4 Method - extractive PDF cue:** To address these limitations, we introduce a multi-view feature alignment loss.
- **p. 6 / 4 Method - extractive PDF cue:** Then the pixel-wise feature alignment loss is defined as: Lf = 1 N X Fs∈{Fs,i} 1 V X pr∈Ir υrs(pr) · ω(pr) ·
- **p. 5 / 4 Method - extractive PDF cue:** To address these, we use a normal smoothing loss that encourages local continuity of surface normals by penalizing large discrepancies between adjacent pixels: Lns = ...
- **p. 5 / 4 Method - extractive PDF cue:** By introducing a photometric consistency loss based on plane patches, we leverage multi-view observations to resolve geometric ambiguities, particularly at object boundaries, and enhance reconstruction ...
- **p. 4 / 4 Method - extractive PDF cue:** The original 3DGS [21] and its variants typically employ a color rendering loss, which combines the L1 reconstruction error with a D-SSIM term.
- **p. 5 / 4 Method - extractive PDF cue:** 1 , (4) where δ = (1 -∇I)2 serves as a per-pixel weight [4] that downweights loss contributions from edge regions, and I denotes the ...
- **p. 4 / 4 Method - extractive PDF cue:** We introduce novel constraints to enable accurate surface reconstruction while preserving high-quality novel view synthesis.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are summarized as follows. • Incorporating edge information and visibility-aware multi-view alignment to enhance surface boundary delineation and improve geometric consistency. • Aligning ...
- **p. 2 / 1 Introduction - extractive PDF cue:** In this work, we propose a novel method for accurate and detailed surface reconstruction by enhancing the geometric representation of 3D Gaussians.
- **p. 4 / 4 Method - extractive PDF cue:** We introduce novel constraints to enable accurate surface reconstruction while preserving high-quality novel view synthesis.

## Source Evidence Cues

- **p. 4 / 4 Method - extractive PDF cue:** To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary details: LI = ...
- **p. 6 / 4 Method - extractive PDF cue:** To address these limitations, we introduce a multi-view feature alignment loss.
- **p. 6 / 4 Method - extractive PDF cue:** Then the pixel-wise feature alignment loss is defined as: Lf = 1 N X Fs∈{Fs,i} 1 V X pr∈Ir υrs(pr) · ω(pr) ·
- **p. 5 / 4 Method - extractive PDF cue:** To address these, we use a normal smoothing loss that encourages local continuity of surface normals by penalizing large discrepancies between adjacent pixels: Lns = ...
- **p. 5 / 4 Method - extractive PDF cue:** By introducing a photometric consistency loss based on plane patches, we leverage multi-view observations to resolve geometric ambiguities, particularly at object boundaries, and enhance reconstruction ...
- **p. 4 / 4 Method - extractive PDF cue:** The original 3DGS [21] and its variants typically employ a color rendering loss, which combines the L1 reconstruction error with a D-SSIM term.
- **Detected method headings:** 4 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary ... | p. 4 (4 Method), p. 6 (4 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To address these limitations, we introduce a multi-view feature alignment loss. | p. 6 (4 Method), p. 6 (4 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Then the pixel-wise feature alignment loss is defined as: Lf = 1 N X Fs∈{Fs,i} 1 V X pr∈Ir υrs(pr) · ω(pr) ... | p. 6 (4 Method), p. 5 (4 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4 Method - extractive PDF cue:** To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary details: LI = ...
- **p. 5 / 4 Method - extractive PDF cue:** 1 , (4) where δ = (1 -∇I)2 serves as a per-pixel weight [4] that downweights loss contributions from edge regions, and I denotes the ...
- **p. 4 / 4 Method - extractive PDF cue:** We introduce novel constraints to enable accurate surface reconstruction while preserving high-quality novel view synthesis.
- **p. 5 / 4 Method - extractive PDF cue:** gradients are likely to correspond to surface discontinuities.
- **p. 6 / 4 Method - extractive PDF cue:** To address these limitations, we introduce a multi-view feature alignment loss.
- **p. 6 / 4 Method - extractive PDF cue:** However, image-based losses are susceptible to noise, blur, and low-texture regions.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4 Method), p. 5 (4 Method), p. 4 (4 Method), p. 5 (4 Method), p. 6 (4 Method), p. 6 (4 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, posed, RGB, images, goal, learn, bunch, Gaussian, functions, associated, attributes, color, opacity, position | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, posed, RGB, images, goal, learn, bunch, Gaussian, functions, associated | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, Incorporating, edge, information, visibility-aware, multi-view, alignment, enhance | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | address, limitation, edge-aware, image, reconstruction, loss, encourages, model, better, preserve | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4 Method - extractive PDF cue:** Given a set of posed RGB images, our goal is to learn a bunch of 3D Gaussian functions with associated attributes, such as color, opacity, ...
- **p. 5 / 4 Method - extractive PDF cue:** 1 , (4) where δ = (1 -∇I)2 serves as a per-pixel weight [4] that downweights loss contributions from edge regions, and I denotes the ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are summarized as follows. • Incorporating edge information and visibility-aware multi-view alignment to enhance surface boundary delineation and improve geometric consistency. • Aligning ...
- **p. 5 / 4 Method - extractive PDF cue:** By introducing a photometric consistency loss based on plane patches, we leverage multi-view observations to resolve geometric ambiguities, particularly at object boundaries, and enhance reconstruction ...
- **p. 4 / 4 Method - extractive PDF cue:** 2DGS [16] introduces a normal consistency loss that aligns the normals of Gaussian primitives with those derived from the rendered depth map, ensuring that each ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Experiments on standard benchmarks demonstrate that our method achieves state-of-the-art performance in both surface reconstruction and novel view synthesis.
- **p. 3 / 3 Preliminaries - extractive PDF cue:** Normal and Depth Estimation from Gaussians.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 2 illustrates the overall framework of our approach. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | While effective for overall image quality, this loss alone is insufficient for accurately capturing object boundaries during surface reconstruction, and it tends ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For novel view synthesis, we continue training for an additional 10,000 steps to optimize rendering quality. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 5 Experiments - extractive PDF cue:** Our overall pipeline, training strategy, and hyperparameter settings generally follow 3DGS [21].
- **p. 7 / 5 Experiments - extractive PDF cue:** For novel view synthesis, we continue training for an additional 10,000 steps to optimize rendering quality.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, limitation, edge-aware, image, reconstruction, loss, encourages, model, better, preserve, sharp, structures, boundary, details, LSSIM, where, rendered, ground-truth, denotes, gradient.
- **Relevant PDF headings:** 4 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Following prior works [16, 55, 4, 56], we use 15 scenes from the DTU dataset and 6 scenes from the TNT dataset ... | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Semantic / temporal fusion | We first compare our method with state-of-the-art implicit and explicit surface reconstruction approaches on the DTU dataset [18]. | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Robot query / planning handoff | Although our method is slightly slower than 3DGS [21] and 2DGS [16] due to the use of multi-view alignment, it achieves significant ... | p. 8 (5 Experiments), p. 8 (5 Experiments) |

## Failure and Ablation Link

- **p. 9 / 5 Experiments - extractive PDF cue:** Our ablation results in Table 4 further confirm that flattening 3D Gaussians into planar Gaussian disks is ineffective for our framework.
- **p. 9 / 5 Experiments - extractive PDF cue:** Precision ↑Recall ↑F1-score ↑ Only LI 0.09 0.23 0.13 w/o edge item 0.49 0.59 0.53 w/o weight δ 0.50 0.59 0.53 w/o Lnc 0.48 0.60 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Visual comparison of surface reconstruction results on the Mip-NeRF 360 dataset. Our approach effectively handles the challenges posed by cluttered lighting and boundaries. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of our method. The training includes five loss functions: LI, Lnc, Lns, Lp and Lf. The occlusion weight ω, visibility item υ ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Our method addresses illumination and boundary artifacts that previous methods fail to resolve. In this work, we propose a novel method for accurate ...
- **p. 5 / 4 Method - extractive PDF cue:** The definitions of υrs(pr) and ω(pr) are detailed in the following. • Due to viewpoint changes, a 2D pixel pr in the reference view may ...
- **p. 6 / 4 Method - extractive PDF cue:** To address these limitations, we introduce a multi-view feature alignment loss.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4 Method), p. 6 (4 Method), p. 6 (4 Method), p. 5 (4 Method), p. 5 (4 Method), p. 4 (4 Method), objective p. 4 (4 Method), p. 5 (4 Method), p. 4 (4 Method), p. 5 (4 Method), p. 6 (4 Method), p. 6 (4 Method), temporal p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method), p. 5 (4 Method), p. 7 (5 Experiments), p. 7 (5 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
