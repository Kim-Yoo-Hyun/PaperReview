# Method - MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Overview), p. 5 (3.3. Surface reconstruction with 2DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 5 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 3 (3.2. Illumination decomposition with 3DGS)): To address this limitation, we introduce a geometry-guided illumination decomposition module, which leverages depth information from the 2DGS branch to enhance rendering performance under diverse light conditions.

## Method Body Digest

- **p. 3 / 3.1. Overview - extractive body cue:** To address this limitation, we introduce a geometry-guided illumination decomposition module, which leverages depth information from the 2DGS branch to enhance rendering performance under diverse ...
- **p. 5 / 3.3. Surface reconstruction with 2DGS - extractive body cue:** The overall loss of the 2DGS branch consists of a weighted combination: L2D = Lrender + λ3(γLn + λ4Ln-TV) + λ5Ld-TV, (11) where λ3, λ4, ...
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** The total loss Ltotal of the alternating optimization is: Ltotal = w2DL2D + w3DL3D + wdepth-mutualLZ, (15) where the losses of the 3D module L3D ...
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** Specifically, as one branch reaches convergence, it will initiate our alternating optimization process first.
- **p. 5 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** In the alternating optimization stage, the loss function of 2DGS branch will be promoted to: L2D = Lrender-m +λ3(γLn +λ4Ln-TV-m)+λ5Ld-TV-m, (13) where γ is the ...
- **p. 3 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** 3DGS is constrained in modeling transparent or translucent materials, such as glass.
- **p. 4 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** Subsequently, the rendering loss is applied to encourage rendered color C to be similar to the GT color CGT.
- **p. 5 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** Lmutual denotes the rendering loss between the 2DGS branch rendered images and the transmitted images from the 3DGS branch, L2D-render is the rendering loss between ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy (Figure ...
- **p. 2 / 1. Introduction - extractive body cue:** The input consists of multi-view images captured from various camera positions and angles, under significantly varying light conditions.
- **p. 3 / 3.1. Overview - extractive body cue:** MGSR is a 2D/3D mutual-boosted framework that consists of two branches: improved 3DGS branch (Section 3.2) and 2DGS branch (Section 3.3).

## Source Evidence Cues

- **p. 3 / 3.1. Overview - extractive body cue:** To address this limitation, we introduce a geometry-guided illumination decomposition module, which leverages depth information from the 2DGS branch to enhance rendering performance under diverse ...
- **p. 5 / 3.3. Surface reconstruction with 2DGS - extractive body cue:** The overall loss of the 2DGS branch consists of a weighted combination: L2D = Lrender + λ3(γLn + λ4Ln-TV) + λ5Ld-TV, (11) where λ3, λ4, ...
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** The total loss Ltotal of the alternating optimization is: Ltotal = w2DL2D + w3DL3D + wdepth-mutualLZ, (15) where the losses of the 3D module L3D ...
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** Specifically, as one branch reaches convergence, it will initiate our alternating optimization process first.
- **p. 5 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** In the alternating optimization stage, the loss function of 2DGS branch will be promoted to: L2D = Lrender-m +λ3(γLn +λ4Ln-TV-m)+λ5Ld-TV-m, (13) where γ is the ...
- **p. 3 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** 3DGS is constrained in modeling transparent or translucent materials, such as glass.
- **p. 4 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** Subsequently, the rendering loss is applied to encourage rendered color C to be similar to the GT color CGT.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To address this limitation, we introduce a geometry-guided illumination decomposition module, which leverages depth information from the 2DGS branch to enhance rendering ... | p. 3 (3.1. Overview), p. 5 (3.3. Surface reconstruction with 2DGS) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The overall loss of the 2DGS branch consists of a weighted combination: L2D = Lrender + λ3(γLn + λ4Ln-TV) + λ5Ld-TV, (11) ... | p. 5 (3.3. Surface reconstruction with 2DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The total loss Ltotal of the alternating optimization is: Ltotal = w2DL2D + w3DL3D + wdepth-mutualLZ, (15) where the losses of the ... | p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** The total loss Ltotal of the alternating optimization is: Ltotal = w2DL2D + w3DL3D + wdepth-mutualLZ, (15) where the losses of the 3D module L3D ...
- **p. 5 / 3.3. Surface reconstruction with 2DGS - extractive body cue:** The overall loss of the 2DGS branch consists of a weighted combination: L2D = Lrender + λ3(γLn + λ4Ln-TV) + λ5Ld-TV, (11) where λ3, λ4, ...
- **p. 5 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** Lmutual denotes the rendering loss between the 2DGS branch rendered images and the transmitted images from the 3DGS branch, L2D-render is the rendering loss between ...
- **p. 3 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** When splatting 3D Gaussians to 2D images, β is accumulated as described in Equation (1) to obtain the pixelwise reflected confidence W, and the transmitted ...
- **p. 4 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** Subsequently, the rendering loss is applied to encourage rendered color C to be similar to the GT color CGT.
- **p. 4 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** (4) A total variation (TV) loss Ltrans-TV is utilized to smooth in local regions of the transmitted components.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.3. Surface reconstruction with 2DGS), p. 5 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 3 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Gaussians, Normals, Images, Depths, D-GS, Branch, Ref-images, Ref-map, Trans-images, Mutual-boosted, Supervision, NVS, Inputs, under | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Gaussians, Normals, Images, Depths, D-GS, Branch, Ref-images, Ref-map, Trans-images, Mutual-boosted | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | solve, contradictions, MGSR, D/3D, Mutual-boosted, Gaussian, splatting, Surface, Reconstruction, enhances | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | total, loss, Ltotal, alternating, optimization, w2DL2D, w3DL3D, wdepth-mutualLZ, where, losses | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** 2D Gaussians Normals Images Depths 2D-GS Branch Ref-images Ref-map × + Trans-images 3D Gaussians 3D-GS Branch Depths Mutual-boosted Supervision NVS SR Inputs under Various Light ...
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** Input images NeuS2 2D-GS GOF MGSR (Ours) Coffee MuscleCar Figure 5.
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** To encourage the alternating optimization to focus on the foreground part of the input images, masks are used to avoid the calculation of background by ...
- **p. 2 / 1. Introduction - extractive body cue:** The input consists of multi-view images captured from various camera positions and angles, under significantly varying light conditions.
- **p. 4 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** Upon receiving inputs from various light conditions, the two branches initially undergo a warm-up stage of initialization for mutual-boosted optimization.
- **p. 3 / 3.1. Overview - extractive body cue:** In the subsequent alternating optimization phase, the 3DGS branch is supervised by depth maps generated by the 2DGS branch, while reflection-free images rendered by the ...
- **p. 5 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** Moreover, both TV losses on depths (Ld-TV-m) and normals (Ln-TV-m) in 2DGS branch are retained, but GT images are replaced with the transmitted images.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | MGSR is a 2D/3D mutual-boosted framework that consists of two branches: improved 3DGS branch (Section 3.2) and 2DGS branch (Section 3.3). | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | not recovered | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.2. Illumination decomposition with 3DGS - extractive body cue:** 3DGS is constrained in modeling transparent or translucent materials, such as glass.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, limitation, introduce, geometry-guided, illumination, decomposition, module, leverages, depth, information, DGS, branch, enhance, rendering, performance, under, diverse, light, conditions, overall.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | DTU [7] is a large MVS dataset, where some scenes feature unfavorable light conditions for surface reconstruction, such as overexposure, underexposure, and ... | p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.1. Datasets and evaluation metrics) |
| Semantic / temporal fusion | MGSR visually outperforms all baselines, resulting in the best NC, with smooth surfaces and accurate color modeling. | p. 7 (4.2. Results), p. 6 (4.1. Datasets and evaluation metrics) |
| Robot query / planning handoff | Figure 1. MGSR achieves strong NVS and SR results compared with methods based on 2DGS [6] and 3DGS [24]. The input consists ... | p. 2 (Figure/Table caption), p. 8 (4.2. Results) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. MGSR is a 2D/3D mutual-boosted framework with two branches: 2DGS branch (upper) for SR and 3DGS branch (bottom) for NVS. Each branch is ...
- **p. 8 / 4.2. Results - extractive body cue:** The best-performing model in each ablation study is highlighted.
- **p. 8 / 4.2. Results - extractive body cue:** Ablations of loss weights (Models A-F), iterations of mutual-boosted optimization (Models G-J), bidrectional BP and auto-stop warm-up strategy (Models K-L) on OmniObject3D dataset.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Geometry enhancement in 3DGS branch for realistic rendering through our mutual-boosted optimization. information for the 3DGS branch for better illumination de- composition. Specifically, ...
- **p. 7 / 4.2. Results - extractive body cue:** To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, which fail to capture surface holes or ...
- **p. 8 / 6. Conclusion - extractive body cue:** A possible way for addressing this issue is to incorporate exposure compensation for input images, which we will investigate as a future work.
- **p. 6 / 4.1. Datasets and evaluation metrics - extractive body cue:** Due to the limitation of CD, we mainly focus on NC metric, which aligns better 27300

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Overview), p. 5 (3.3. Surface reconstruction with 2DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 5 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 3 (3.2. Illumination decomposition with 3DGS), objective p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 5 (3.3. Surface reconstruction with 2DGS), p. 5 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 3 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS), temporal p. 3 (3.1. Overview).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
