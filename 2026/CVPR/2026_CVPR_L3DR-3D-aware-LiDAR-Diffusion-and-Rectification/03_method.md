# Method - L3DR: 3D-aware LiDAR Diffusion and Rectification

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 5 (4.3. Residual Regression Training), p. 4 (4.2. LiDAR Diffusion Training), p. 4 (4. Method), p. 5 (4.3. Residual Regression Training), p. 6 (4.4. Diffusion-agnostic Inference)): After obtaining the model output and GT, we propose Welsch Loss to remove the effect of erratic high-bias areas in training data to focus on rectifying highvariance RV artifacts.

## Method Body Digest

- **p. 5 / 4.3. Residual Regression Training - extractive body cue:** After obtaining the model output and GT, we propose Welsch Loss to remove the effect of erratic high-bias areas in training data to focus on ...
- **p. 4 / 4.2. LiDAR Diffusion Training - extractive body cue:** Specifically, the RV image is first compressed with a VQ-VAE [44], then a classical diffusion UNet is leveraged to predict Gaussian noise added in the ...
- **p. 4 / 4. Method - extractive body cue:** In the LiDAR diffusion training, we leverage the RV representation to train a LiDAR diffusion model with conditional semantic input.
- **원문 대조:** RRN loss는 보정 point cloud를 range view로 투영한 값과 ground truth의 residual에 Welsch 함수 ψ_ν를 적용해 평균한다. 큰 bias residual의 영향을 줄이기 위한 robust loss이며 단순 L2로 치환하지 않는다. ([PDF p. 5](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.pdf#page=5), §4.3 Residual Regression Training, Eqs. (5)–(6)).
- **p. 6 / 4.4. Diffusion-agnostic Inference - extractive body cue:** Specifically, during inference, we generate novel x′ gen with arbitrary LiDAR diffusion model, project RV into a point cloud P ′ gen = RRVP(x′ gen), ...
- **p. 4 / 4.1. Range View Projection - extractive body cue:** Empirically, RVP is lossless when the point cloud projection structure is preserved and RV image size is equal to or larger than the laser angular ...
- **p. 4 / 4. Method - extractive body cue:** In the residual regression training, we apply such data pairs to train a 3D residual regression network (RRN) that rectifies RV artifacts under the supervision ...
- **p. 5 / 4.3. Residual Regression Training - extractive body cue:** Decomposition of the learning objective.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work can be summarized in three major aspects: • We propose a 3D-aware LiDAR Diffusion and Rectification framework that rectifies RV ...
- **p. 5 / 4.3. Residual Regression Training - extractive body cue:** After obtaining the model output and GT, we propose Welsch Loss to remove the effect of erratic high-bias areas in training data to focus on ...
- **p. 5 / 4.2. LiDAR Diffusion Training - extractive body cue:** However, we also highlight that our framework is general and not restricted to LiDM, given that an alternative LiDAR diffusion method can generate such closely ...

## Source Evidence Cues

- **p. 5 / 4.3. Residual Regression Training - extractive body cue:** After obtaining the model output and GT, we propose Welsch Loss to remove the effect of erratic high-bias areas in training data to focus on ...
- **p. 4 / 4.2. LiDAR Diffusion Training - extractive body cue:** Specifically, the RV image is first compressed with a VQ-VAE [44], then a classical diffusion UNet is leveraged to predict Gaussian noise added in the ...
- **p. 4 / 4. Method - extractive body cue:** In the LiDAR diffusion training, we leverage the RV representation to train a LiDAR diffusion model with conditional semantic input.
- **원문 대조:** RRN loss는 보정 point cloud를 range view로 투영한 값과 ground truth의 residual에 Welsch 함수 ψ_ν를 적용해 평균한다. 큰 bias residual의 영향을 줄이기 위한 robust loss이며 단순 L2로 치환하지 않는다. ([PDF p. 5](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.pdf#page=5), §4.3 Residual Regression Training, Eqs. (5)–(6)).
- **p. 6 / 4.4. Diffusion-agnostic Inference - extractive body cue:** Specifically, during inference, we generate novel x′ gen with arbitrary LiDAR diffusion model, project RV into a point cloud P ′ gen = RRVP(x′ gen), ...
- **Detected method headings:** 2.1. Diffusion Models (p. 2); 4. Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | After obtaining the model output and GT, we propose Welsch Loss to remove the effect of erratic high-bias areas in training data ... | p. 5 (4.3. Residual Regression Training), p. 4 (4.2. LiDAR Diffusion Training) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Specifically, the RV image is first compressed with a VQ-VAE [44], then a classical diffusion UNet is leveraged to predict Gaussian noise ... | p. 4 (4.2. LiDAR Diffusion Training), p. 4 (4. Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In the LiDAR diffusion training, we leverage the RV representation to train a LiDAR diffusion model with conditional semantic input. | p. 4 (4. Method), p. 5 (4.3. Residual Regression Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.1. Range View Projection - extractive body cue:** Empirically, RVP is lossless when the point cloud projection structure is preserved and RV image size is equal to or larger than the laser angular ...
- **p. 4 / 4. Method - extractive body cue:** In the residual regression training, we apply such data pairs to train a 3D residual regression network (RRN) that rectifies RV artifacts under the supervision ...
- **p. 5 / 4.3. Residual Regression Training - extractive body cue:** Decomposition of the learning objective.
- **원문 대조:** RRN loss는 보정 point cloud를 range view로 투영한 값과 ground truth의 residual에 Welsch 함수 ψ_ν를 적용해 평균한다. 큰 bias residual의 영향을 줄이기 위한 robust loss이며 단순 L2로 치환하지 않는다. ([PDF p. 5](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.pdf#page=5), §4.3 Residual Regression Training, Eqs. (5)–(6)).
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4.1. Range View Projection), p. 4 (4. Method), p. 5 (4.3. Residual Regression Training), p. 5 (4.3. Residual Regression Training).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | order, generate, ground-truth, diffusion-generated, point, cloud, pairs, following, training, stage, retrain, state-of-the-art, conditional, LiDAR | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | order, generate, ground-truth, diffusion-generated, point, cloud, pairs, following, training, stage | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, three, major, aspects, D-aware, LiDAR, Diffusion, Rectification, framework | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Empirically, RVP, lossless, when, point, cloud, projection, structure, preserved, image | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.2. LiDAR Diffusion Training - extractive body cue:** In order to generate ground-truth and diffusion-generated point cloud pairs for the following training stage, we retrain a state-of-the-art conditional LiDAR diffusion model, LiDM [34], ...
- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work can be summarized in three major aspects: • We propose a 3D-aware LiDAR Diffusion and Rectification framework that rectifies RV ...
- **원문 대조:** 3D backbone이 예측한 point offset을 원래 generated point cloud의 radial direction으로 투영해 최종 residual을 만든다. 깨진 diag·제곱근·나눗셈 표기는 추정 복원하지 않고 원문의 projection 식을 참조한다. ([PDF p. 5](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.pdf#page=5), §4.3 Pipeline).
- **p. 4 / 4.2. LiDAR Diffusion Training - extractive body cue:** To enable conditional generation, a down-sampled segmentation color map is appended to latent space as control input.
- **p. 5 / 4.3. Residual Regression Training - extractive body cue:** For a normal unconditional 3D RRN, k = 3 which represents the input point coordinates; otherwise, k = 6 which accepts both the coordinates and ...
- **p. 6 / 4.4. Diffusion-agnostic Inference - extractive body cue:** For the semantic-conditioned experiments, RRN takes segmentation map as additional input for optimal performance.
- **p. 2 / 1. Introduction - extractive body cue:** However, although RV enables DM-based point cloud generation by projecting 3D point clouds to 2D images, it hinders accurate discernment of sparsity and selfocclusion in ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | They are usually anisotropic, i.e., the vertical resolution is sparse while horizontal resolution is dense. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Depthshifted walls Misaligned random points Small isolated chunks Figure 4. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All networks are trained with 4× RTX 4090 24G up to 150 epochs. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.3. Residual Regression Training - extractive body cue:** After obtaining the model output and GT, we propose Welsch Loss to remove the effect of erratic high-bias areas in training data to focus on ...
- **p. 4 / 4. Method - extractive body cue:** In the LiDAR diffusion training, we leverage the RV representation to train a LiDAR diffusion model with conditional semantic input.
- **p. 6 / 4.4. Diffusion-agnostic Inference - extractive body cue:** Specifically, during inference, we generate novel x′ gen with arbitrary LiDAR diffusion model, project RV into a point cloud P ′ gen = RRVP(x′ gen), ...
- **p. 6 / 5.2. Experiment Setup - extractive body cue:** All networks are trained with 4× RTX 4090 24G up to 150 epochs.

## Method-Specific Formal Details

- **Body-defined terms:** After, obtaining, model, output, Welsch, Loss, remove, effect, erratic, high-bias, areas, training, data, focus, rectifying, highvariance, artifacts, Specifically, image, first.
- **Relevant PDF headings:** 2.1. Diffusion Models (p. 2); 4. Method (p. 4).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | All datasets are split into trainvalidation-test according to official recommendations. | p. 6 (5.2. Experiment Setup), p. 6 (5.2. Experiment Setup) |
| Semantic / temporal fusion | We conclude that L3DR significantly improves conditional generation capability compared to the baselines. | p. 7 (5.2. Experiment Setup), p. 7 (5.3. Other Results) |
| Robot query / planning handoff | We conclude that L3DR significantly improves conditional generation capability compared to the baselines. | p. 7 (5.2. Experiment Setup), p. 7 (5.2. Experiment Setup) |

## Failure and Ablation Link

- **p. 4 / 3.3. Empirical Analysis - extractive body cue:** We remove the dominant ∥∇x∥≤0.3m on planar regions and rare ∥∇x∥≥10m which exceed network ERFs, so that we can compare the remaining geometryrelated gradients.
- **p. 4 / 3.2. Theoretical Analysis - extractive body cue:** In the residual regression training stage, such data pairs are employed to train a 3D network to remove RV artifacts present in the residuals to ...
- **p. 6 / 5.1. Main Results - extractive body cue:** Module ablation and time analysis are listed in Table 3-4.
- **p. 6 / 5.2. Experiment Setup - extractive body cue:** Our diffusion model processes depth values of size without logarithmic scaling.
- **p. 8 / 5.3. Other Results - extractive body cue:** Ablation experiment on SemanticKITTI, including RRN backbone structure, loss function, semantic-map input to RRN, and a fair baseline using a 2D image Unet instead of ...
- **p. 7 / 5.3. Other Results - extractive body cue:** We ablate various components of the L3DR framework, including the backbone architecture between SPUNET [7] and PTV3 [46], loss choice, the usage of semantic-map input ...
- **p. 3 / 3.2. Theoretical Analysis - extractive body cue:** As a result of Lipschitz continuity throughout the DDIM sampling process, the generated image in theory cannot exhibit arbitrarily sharp spatial transitions.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4.3. Residual Regression Training), p. 4 (4.2. LiDAR Diffusion Training), p. 4 (4. Method), p. 5 (4.3. Residual Regression Training), p. 6 (4.4. Diffusion-agnostic Inference), objective p. 4 (4.1. Range View Projection), p. 4 (4. Method), p. 5 (4.3. Residual Regression Training), p. 5 (4.3. Residual Regression Training), temporal p. 4 (4.1. Range View Projection), p. 5 (4.2. LiDAR Diffusion Training), p. 5 (4.2. LiDAR Diffusion Training), p. 7 (5.2. Experiment Setup), p. 7 (5.3. Other Results), p. 8 (5.3. Other Results).
