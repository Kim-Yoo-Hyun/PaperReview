# Method - Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Learning Patch-based UDF Priors), p. 4 (3.2. Learning Patch-based UDF Priors), p. 5 (3.3. Band-limited Knowledge Distillation), p. 4 (3.2. Learning Patch-based UDF Priors), p. 5 (3.4. Visibility and Geometry Aware Weighting), p. 3 (3.2. Learning Patch-based UDF Priors)): Considering the strengths of LoSF-UDF [19] including robustness to noise and local feature representation, we use it as the teacher UDF model for distillation, denoted as ft.

## Method Body Digest

- **p. 3 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** Considering the strengths of LoSF-UDF [19] including robustness to noise and local feature representation, we use it as the teacher UDF model for distillation, denoted ...
- **p. 4 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** To integrate this patch-based UDF prior into the 3DGS optimization, we use it to regularize the student UDF model fs.
- **p. 5 / 3.3. Band-limited Knowledge Distillation - extractive body cue:** representation to fit the scene geometry and appearance, and then optimize the student network within this band.
- **p. 4 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** We then can synthesize a series of point cloud patches using Eq.(4) for training patch-based UDF priors with groundtruth UDF values for queries [19].
- **p. 5 / 3.4. Visibility and Geometry Aware Weighting - extractive body cue:** Let gt(q) and gs(q) are gradient from the teacher and student module, then normalize them as: ˆgt(q) = gt(q) ∥gt(q)∥, ˆgs(q) = gs(q) ∥gs(q)∥, (10) ...
- **p. 3 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** Given (q, P), the network ft(q/P) predicts the unsigned distance d to the underlying surface represented by the patch.
- **p. 3 / 3. Method - extractive body cue:** The Gaussian parameters are optimized by minimizing the L1 photometric loss between the rendered image C′(u, v) and the ground-truth image C(u, v): Lr = ...
- **원문 대조:** Teacher distance에 per-scene affine calibration a·u_t(q)+b를 적용한다. a>0 조건 아래 confidence-weighted squared residual을 최소화해 scale·offset을 맞추며, a와 b에는 gradient를 흘리지 않는다. ([PDF p. 4](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=4), §3.3 Band-limited Knowledge Distillation, Eq. (6)).

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into ...
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we introduce a visibility- and geometry-aware confidence weighting, together with a joint optimization scheme, to further steer the student toward accurate surfaces from ...
- **p. 3 / 3. Method - extractive body cue:** Our framework integrates Gaussian Splatting with UDF learning via a band-limited distillation scheme: a frozen local-shape UDF teacher ut provides supervision in a narrow nearsurface ...

## Source Evidence Cues

- **p. 3 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** Considering the strengths of LoSF-UDF [19] including robustness to noise and local feature representation, we use it as the teacher UDF model for distillation, denoted ...
- **p. 4 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** To integrate this patch-based UDF prior into the 3DGS optimization, we use it to regularize the student UDF model fs.
- **p. 5 / 3.3. Band-limited Knowledge Distillation - extractive body cue:** representation to fit the scene geometry and appearance, and then optimize the student network within this band.
- **p. 4 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** We then can synthesize a series of point cloud patches using Eq.(4) for training patch-based UDF priors with groundtruth UDF values for queries [19].
- **p. 5 / 3.4. Visibility and Geometry Aware Weighting - extractive body cue:** Let gt(q) and gs(q) are gradient from the teacher and student module, then normalize them as: ˆgt(q) = gt(q) ∥gt(q)∥, ˆgs(q) = gs(q) ∥gs(q)∥, (10) ...
- **p. 3 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** Given (q, P), the network ft(q/P) predicts the unsigned distance d to the underlying surface represented by the patch.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Considering the strengths of LoSF-UDF [19] including robustness to noise and local feature representation, we use it as the teacher UDF model ... | p. 3 (3.2. Learning Patch-based UDF Priors), p. 4 (3.2. Learning Patch-based UDF Priors) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To integrate this patch-based UDF prior into the 3DGS optimization, we use it to regularize the student UDF model fs. | p. 4 (3.2. Learning Patch-based UDF Priors), p. 5 (3.3. Band-limited Knowledge Distillation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | representation to fit the scene geometry and appearance, and then optimize the student network within this band. | p. 5 (3.3. Band-limited Knowledge Distillation), p. 4 (3.2. Learning Patch-based UDF Priors) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Method - extractive body cue:** The Gaussian parameters are optimized by minimizing the L1 photometric loss between the rendered image C′(u, v) and the ground-truth image C(u, v): Lr = ...
- **원문 대조:** Teacher distance에 per-scene affine calibration a·u_t(q)+b를 적용한다. a>0 조건 아래 confidence-weighted squared residual을 최소화해 scale·offset을 맞추며, a와 b에는 gradient를 흘리지 않는다. ([PDF p. 4](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=4), §3.3 Band-limited Knowledge Distillation, Eq. (6)).
- **p. 5 / 3.5. Joint Optimization - extractive body cue:** Our complete training objective jointly optimizes several components that together enable accurate and geometryaware surface reconstruction.
- **p. 3 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** However, its gradient is undefined exactly on the surface [11], which makes gradient-based UDF learning framework unstable, especially in the absence of groundtruth surface supervision.
- **p. 4 / 3.3. Band-limited Knowledge Distillation - extractive body cue:** When learning UDFs, gradient-based priors that ignore non-differentiability at the target surface can cause unstable training and oversmoothing of fine details.
- **p. 5 / 3.5. Joint Optimization - extractive body cue:** This composite objective integrates fine-grained local shape priors and encourages the recovery of detailed, smooth, and topologically consistent surfaces.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.3. Band-limited Knowledge Distillation), p. 3 (3. Method), p. 3 (3.2. Learning Patch-based UDF Priors), p. 4 (3.3. Band-limited Knowledge Distillation), p. 5 (3.5. Joint Optimization), p. 5 (3.5. Joint Optimization).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | main, contributions, follows, novel, framework, learns, UDF, over, Gaussian, primitives, distilling, patch-based, predictor, lightweight | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | main, contributions, follows, novel, framework, learns, UDF, over, Gaussian, primitives | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, follows, novel, framework, learns, UDF, over, Gaussian, primitives | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Gaussian, parameters, optimized, minimizing, photometric, loss, between, rendered, image, ground-truth | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into ...
- **p. 3 / 3. Method - extractive body cue:** Our goal is to reconstruct accurate, geometrically consistent open surfaces from calibrated multi-view images.
- **p. 3 / 3. Method - extractive body cue:** Preliminaries: 2D Gaussian Splatting To fit 3D Gaussians to the scene surfaces, we follow the differentiable α-compositing strategy proposed in 2DGS [21] to render a ...
- **p. 5 / 3.5. Joint Optimization - extractive body cue:** For each pixel (u, v) and each Gaussian k that contributes to that pixel, we define LGN as: LGN = Σkwk(1 -/ˆgs(k) · nk/), (13) ...
- **p. 1 / 1. Introduction - extractive body cue:** The core idea is to use a teacher network that predicts UDF values for a query point by conditioning on its nearest geometric patch in ...
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, unsigned distance function (UDF) dispenses with the global sign and †Corresponding authors. can represent open geometry directly, attractive for objects or scenes containing ...
- **p. 4 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** We then can synthesize a series of point cloud patches using Eq.(4) for training patch-based UDF priors with groundtruth UDF values for queries [19].
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Hybrid frameworks [5, 16, 20, 36, 44, 55, 60] go one step further by jointly learning SDF and Gaussian parameters, demonstrate the ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All experiments are conducted on an NVIDIA RTX 3090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** We then can synthesize a series of point cloud patches using Eq.(4) for training patch-based UDF priors with groundtruth UDF values for queries [19].
- **p. 5 / 4.1. Experiment Settings - extractive body cue:** We train the UDF network with the Adam optimizer and an initial learning rate of 1 × 10-3, using a cosine learning rate decay strategy ...

## Method-Specific Formal Details

- **Body-defined terms:** Considering, strengths, LoSF-UDF, including, robustness, noise, local, feature, representation, teacher, UDF, model, distillation, denoted, integrate, patch-based, prior, DGS, optimization, regularize.
- **Relevant PDF headings:** 3. Method (p. 3).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We further evaluate our method on the DTU dataset [22], which contains 15 widely used multi-view scenes for surface reconstruction. | p. 8 (4.3. DTU Dataset), p. 5 (4.1. Experiment Settings) |
| Semantic / temporal fusion | As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared methods, including classical NeRF-style SDF baselines ... | p. 8 (4.3. DTU Dataset), p. 7 (4.2. DF3D Dataset) |
| Robot query / planning handoff | Among UDF-based approaches, our model further achieves competitive runtime 4897 | p. 7 (4.2. DF3D Dataset), p. 8 (4.2. DF3D Dataset) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Ablation study on the DTU [51]. report the numbers from the original papers [29, 32, 45, 61]. Our experiments follow [29] for surface ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation studies on DTU dataset. Settings CD ↓ Baseline ✓ 0.99 + UDF distillation ✓
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared methods, including classical NeRF-style SDF baselines (NeuS [48]), Gaussian-based ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. Overview. Given calibrated multi-view images, we jointly optimize a 3DGS and a student UDF us. For a local query point p and its ...
- **p. 8 / 5. Conclusion - extractive body cue:** In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to further ...
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** It is well known that learning unsigned distance functions (UDFs) is intrinsically more challenging than learning signed distance fields (SDFs), due to sign ambiguity and ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.2. Learning Patch-based UDF Priors), p. 4 (3.2. Learning Patch-based UDF Priors), p. 5 (3.3. Band-limited Knowledge Distillation), p. 4 (3.2. Learning Patch-based UDF Priors), p. 5 (3.4. Visibility and Geometry Aware Weighting), p. 3 (3.2. Learning Patch-based UDF Priors), objective p. 3 (3. Method), p. 4 (3.3. Band-limited Knowledge Distillation), p. 5 (3.5. Joint Optimization), p. 3 (3.2. Learning Patch-based UDF Priors), p. 4 (3.3. Band-limited Knowledge Distillation), p. 5 (3.5. Joint Optimization), temporal p. 2 (2.2. Learning SDFs with Multiview Images), p. 2 (1. Introduction), p. 3 (3.2. Learning Patch-based UDF Priors), p. 3 (3. Method), p. 1 (1. Introduction), p. 7 (4.2. DF3D Dataset).
