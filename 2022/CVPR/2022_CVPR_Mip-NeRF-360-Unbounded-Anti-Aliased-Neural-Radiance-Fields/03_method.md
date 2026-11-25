# Method - Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2111.12077; PDF retrieval source: https://arxiv.org/pdf/2111.12077. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 7 (5. Optimization), p. 6 (4. Regularization for Interval-Based Models), p. 6 (4. Regularization for Interval-Based Models), p. 7 (5. Optimization)): For Lrecon we use Charbonnier loss [10]: p (x -x∗)2 + ϵ2 with ϵ = 0.001, which achieves slightly more stable optimization than the mean squared error used in mip-NeRF.

## Method Body Digest

- **p. 7 / 5. Optimization - extractive body cue:** For Lrecon we use Charbonnier loss [10]: p (x -x∗)2 + ϵ2 with ϵ = 0.001, which achieves slightly more stable optimization than the mean ...
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** This reformulation also provides some intuition for how this loss behaves: the first term minimizes the weighted distances between all pairs of interval midpoints, and ...
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** + 1 3 X i w2 i (si+1 -si) (15) In this form, our distortion loss is trivial to compute.
- **p. 7 / 5. Optimization - extractive body cue:** We train our model (and all reported NeRF-like baselines) using a slightly modified version of mip-NeRF's learning schedule: 250k iterations of optimization with a batch ...
- **원문 대조:** 학습 손실은 재구성 항 L_recon, λ로 가중한 distortion 항 L_dist, 두 proposal 단계(k=0,1)의 L_prop 합으로 구성되며 batch의 ray에 대해 평균한다. 이 식 자체는 정량 평가 결과가 아니다. ([PDF p. 6](https://arxiv.org/pdf/2111.12077#page=6), §5 Optimization, Eq. (16)).
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** This loss is minimized by setting w = 0 (recall that w sums to no more than 1, not exactly (a) no Ldist (b) no ...
- **p. 7 / 5. Optimization - extractive body cue:** The stop-gradient used in Lprop makes the optimization of Θprop independent from the optimization of ΘNeRF, and as such there is no need for a ...
- **p. 3 / 3. Ambiguity. The content of unbounded scenes may lie - extractive body cue:** These features are used as input to an MLP parameterized by weights ΘNeRF that outputs a density τ and color c: ∀Ti ∈t, (τi, ci) ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, and a novel ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present an extension to mip-NeRF we call "mip-NeRF 360" that is capable of producing realistic renderings of these unbounded scenes, as ...
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** Here we presents a regularizer that, as shown in Figure 5, prevents floaters and background collapse more effectively than the approach used by NeRF of ...

## Source Evidence Cues

- **p. 7 / 5. Optimization - extractive body cue:** For Lrecon we use Charbonnier loss [10]: p (x -x∗)2 + ϵ2 with ϵ = 0.001, which achieves slightly more stable optimization than the mean ...
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** This reformulation also provides some intuition for how this loss behaves: the first term minimizes the weighted distances between all pairs of interval midpoints, and ...
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** + 1 3 X i w2 i (si+1 -si) (15) In this form, our distortion loss is trivial to compute.
- **p. 7 / 5. Optimization - extractive body cue:** We train our model (and all reported NeRF-like baselines) using a slightly modified version of mip-NeRF's learning schedule: 250k iterations of optimization with a batch ...
- **Detected method headings:** 4. Regularization for Interval-Based Models (p. 6); A. Additional Model Details (p. 11)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | For Lrecon we use Charbonnier loss [10]: p (x -x∗)2 + ϵ2 with ϵ = 0.001, which achieves slightly more stable optimization ... | p. 7 (5. Optimization), p. 6 (4. Regularization for Interval-Based Models) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | This reformulation also provides some intuition for how this loss behaves: the first term minimizes the weighted distances between all pairs of ... | p. 6 (4. Regularization for Interval-Based Models), p. 6 (4. Regularization for Interval-Based Models) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | + 1 3 X i w2 i (si+1 -si) (15) In this form, our distortion loss is trivial to compute. | p. 6 (4. Regularization for Interval-Based Models), p. 7 (5. Optimization) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **원문 대조:** 학습 손실은 재구성 항 L_recon, λ로 가중한 distortion 항 L_dist, 두 proposal 단계(k=0,1)의 L_prop 합으로 구성되며 batch의 ray에 대해 평균한다. 이 식 자체는 정량 평가 결과가 아니다. ([PDF p. 6](https://arxiv.org/pdf/2111.12077#page=6), §5 Optimization, Eq. (16)).
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** This loss is minimized by setting w = 0 (recall that w sums to no more than 1, not exactly (a) no Ldist (b) no ...
- **p. 7 / 5. Optimization - extractive body cue:** For Lrecon we use Charbonnier loss [10]: p (x -x∗)2 + ϵ2 with ϵ = 0.001, which achieves slightly more stable optimization than the mean ...
- **p. 7 / 5. Optimization - extractive body cue:** The stop-gradient used in Lprop makes the optimization of Θprop independent from the optimization of ΘNeRF, and as such there is no need for a ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (4. Regularization for Interval-Based Models), p. 6 (4. Regularization for Interval-Based Models), p. 7 (5. Optimization), p. 7 (5. Optimization).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | features, input, MLP, parameterized, weights, NeRF, outputs, density, color, example, could, recreate, images, simply | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | features, input, MLP, parameterized, weights, NeRF, outputs, density, color, example | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, extension, mip-NeRF, NeRF, variant, addresses, sampling, aliasing, uses, non-linear | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | minimize, following, loss, Lrecon, Ldist, Lprop, averaged, over, rays, batch | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Ambiguity. The content of unbounded scenes may lie - extractive body cue:** These features are used as input to an MLP parameterized by weights ΘNeRF that outputs a density τ and color c: ∀Ti ∈t, (τi, ci) ...
- **p. 2 / 3. Ambiguity. The content of unbounded scenes may lie - extractive body cue:** For example, a NeRF could recreate all input images by simply reconstructing each im2
- **p. 2 / 3. Ambiguity. The content of unbounded scenes may lie - extractive body cue:** Crucially, the weights produced by the proposal MLP are not supervised using the input image, but are instead supervised with the histogram weights generated by ...
- **p. 3 / 3. Ambiguity. The content of unbounded scenes may lie - extractive body cue:** A mip-NeRF is recovered by optimizing MLP parameters ΘNeRF via gradient descent to minimize a weighted combination of coarse and fine reconstruction losses: X r∈R ...
- **p. 1 / Abstract - extractive body cue:** However, NeRF models the input to the MLP using infinitesimally small 3D points along a ray, which causes aliasing when rendering views of varying resolutions.
- **p. 4 / 3. Coarse-to-Fine Online Distillation - extractive body cue:** The proposal MLP is trained to produce proposal weights ˆw that are consistent with the NeRF MLP's w output.
- **p. 4 / 2. Scene and Ray Parameterization - extractive body cue:** We apply this contraction to mip-NeRF Gaussians in Euclidean 3D space (gray ellipses) similarly to a Kalman filter to produce our contracted Gaussians (red ellipses), ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our online distillation approach is similar in spirit to the "sampling oracle networks" used in DONeRF, though that approach uses ground-truth depth ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 5. Optimization - extractive body cue:** We train our model (and all reported NeRF-like baselines) using a slightly modified version of mip-NeRF's learning schedule: 250k iterations of optimization with a batch ...
- **p. 8 / 6. Results - extractive body cue:** D) Removing the proposal MLP and using a single MLP to model both the scene and the proposal weights does not degrade performance but increases ...

## Method-Specific Formal Details

- **Body-defined terms:** Lrecon, Charbonnier, loss, achieves, slightly, more, stable, optimization, mean, squared, error, mip-NeRF, reformulation, provides, some, intuition, behaves, first, term, minimizes.
- **Relevant PDF headings:** 4. Regularization for Interval-Based Models (p. 6); A. Additional Model Details (p. 11).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate our model on a novel dataset: 9 scenes (5 outdoors and 4 indoors) each containing a complex central object or ... | p. 7 (6. Results), p. 7 (6. Results) |
| Semantic / temporal fusion | Though mip-NeRF 360 significantly outperforms mip-NeRF and other prior work, it is not perfect. | p. 8 (6. Results), p. 8 (6. Results) |
| Robot query / planning handoff | The mip-NeRF and NeRF++ baselines that use larger MLPs are more competitive, but are ∼3× slower to train than our model and ... | p. 7 (6. Results), p. 8 (6. Results) |

## Failure and Ablation Link

- **p. 8 / 6. Results - extractive body cue:** An ablation study in which we remove or replace model components to measure their effect.
- **p. 7 / 6. Results - extractive body cue:** We also present a variant of our own model in which we use the latent appearance embedding (4 dimensions) presented in NeRF-W [6, 30] which ...
- **p. 7 / 6. Results - extractive body cue:** In Table 2 we present an ablation study of our model on the bicycle scene in our dataset, the findings of which we summarize here.
- **p. 18 / Figure/Table caption - extractive body cue:** Table 6. The average performance of our model and all NeRF baselines, as well as the top-performing non-NeRF baseline on our own dataset (Stable View ...
- **p. 8 / 6. Results - extractive body cue:** B) Removing Ldist does not substantially affect our metrics but results in "floater" artifacts in scene geometry, as shown in Figure 5.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 12. A visualization of our model with Stable View Synthesis [41] on scenes from the Tanks and Temples dataset [25]. Image quality is roughly ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. (a) A test-set image from our dataset's stump scene, with (b) our model's rendered image and depth map (median ray termination distance [37]). ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (5. Optimization), p. 6 (4. Regularization for Interval-Based Models), p. 6 (4. Regularization for Interval-Based Models), p. 7 (5. Optimization), objective p. 6 (5. Optimization), p. 6 (4. Regularization for Interval-Based Models), p. 7 (5. Optimization), p. 7 (5. Optimization), temporal p. 1 (Abstract), p. 2 (3. Ambiguity. The content of unbounded scenes may lie), p. 2 (3. Ambiguity. The content of unbounded scenes may lie), p. 5 (3. Coarse-to-Fine Online Distillation), p. 5 (3. Coarse-to-Fine Online Distillation), p. 6 (4. Regularization for Interval-Based Models).
