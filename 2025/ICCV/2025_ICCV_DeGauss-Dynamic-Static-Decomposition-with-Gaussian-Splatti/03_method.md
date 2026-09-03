# Method - DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.4. Background Brightness Control), p. 3 (3.2. Foreground deformable gaussian), p. 3 (3.2. Foreground deformable gaussian), p. 4 (3.4. Background Brightness Control), p. 5 (3.7. Loss function), p. 5 (3.8. Partial Opacity Reset)): To address this, we introduce a brightness control mask that enhances the background branch's capacity to model non-Lambertian effects.

## Method Body Digest

- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** To address this, we introduce a brightness control mask that enhances the background branch's capacity to model non-Lambertian effects.
- **p. 3 / 3.2. Foreground deformable gaussian - extractive body cue:** The spatial-temporal module comprises an encoder H and a decoder D.
- **p. 3 / 3.2. Foreground deformable gaussian - extractive body cue:** The encoder, based on Hexplane [3], extracts spatio-temporal features based on reference time t with fd = H(Gf, t), and the multi-head decoder D predicts ...
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** This decoupled formulation guarantee flexible yet accurate scene decomposition result. appearance modeling.
- **p. 5 / 3.7. Loss function - extractive body cue:** We refer readers to Appendix A. for a detailed definition of each loss term.
- **p. 5 / 3.8. Partial Opacity Reset - extractive body cue:** This guarantees stable training, effectively controls gaussian density, and handles local minima.
- **p. 5 / 3.7. Loss function - extractive body cue:** (11) While both main loss Lmain and utility loss Luti are used for optimizable parameters' update, only the gradient magnitude of Lmain are used to ...
- **p. 5 / 3.7. Loss function - extractive body cue:** As the loss gradient magnitude controls the densification process of gaussians [10], we design the loss function L, which comprises two parts Lmain and Luti, ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • ...
- **p. 2 / 1. Introduction - extractive body cue:** We show that our method achieves superior results compared to baseline dynamic scene modeling approaches, with notable advantages across diverse datasets [13, 21].
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** To address this, we introduce a brightness control mask that enhances the background branch's capacity to model non-Lambertian effects.

## Source Evidence Cues

- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** To address this, we introduce a brightness control mask that enhances the background branch's capacity to model non-Lambertian effects.
- **p. 3 / 3.2. Foreground deformable gaussian - extractive body cue:** The spatial-temporal module comprises an encoder H and a decoder D.
- **p. 3 / 3.2. Foreground deformable gaussian - extractive body cue:** The encoder, based on Hexplane [3], extracts spatio-temporal features based on reference time t with fd = H(Gf, t), and the multi-head decoder D predicts ...
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** This decoupled formulation guarantee flexible yet accurate scene decomposition result. appearance modeling.
- **p. 5 / 3.7. Loss function - extractive body cue:** We refer readers to Appendix A. for a detailed definition of each loss term.
- **p. 5 / 3.8. Partial Opacity Reset - extractive body cue:** This guarantees stable training, effectively controls gaussian density, and handles local minima.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To address this, we introduce a brightness control mask that enhances the background branch's capacity to model non-Lambertian effects. | p. 4 (3.4. Background Brightness Control), p. 3 (3.2. Foreground deformable gaussian) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The spatial-temporal module comprises an encoder H and a decoder D. | p. 3 (3.2. Foreground deformable gaussian), p. 3 (3.2. Foreground deformable gaussian) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The encoder, based on Hexplane [3], extracts spatio-temporal features based on reference time t with fd = H(Gf, t), and the multi-head ... | p. 3 (3.2. Foreground deformable gaussian), p. 4 (3.4. Background Brightness Control) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.7. Loss function - extractive body cue:** (11) While both main loss Lmain and utility loss Luti are used for optimizable parameters' update, only the gradient magnitude of Lmain are used to ...
- **p. 5 / 3.7. Loss function - extractive body cue:** As the loss gradient magnitude controls the densification process of gaussians [10], we design the loss function L, which comprises two parts Lmain and Luti, ...
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** The raw background render Cb is rasterized by background gaussian Gb with equation (2).
- **p. 4 / 3.6. Unsupervised scene decomposition - extractive body cue:** This design enables full gradient flow and allow gradually formulated composition mask during training, as shown in Fig.
- **p. 3 / 3.3. Probabilistic Composition Mask Rasterization - extractive body cue:** Given the predicted mask elements \if mm od e \lbrace \else \textbraceleft \fi m_f^\prime , m_b^\prime \ } and the deformed attributes \ifm mod e ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.7. Loss function), p. 5 (3.7. Loss function), p. 4 (3.4. Background Brightness Control), p. 4 (3.6. Unsupervised scene decomposition).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summary, contributions, DeGauss, decoupled, foregroundbackground, design, leverages, dynamic-static, Gaussian, splatting, robust, generalizable, dynamicstatic, decomposition | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | summary, contributions, DeGauss, decoupled, foregroundbackground, design, leverages, dynamic-static, Gaussian, splatting | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, DeGauss, decoupled, foregroundbackground, design, leverages, dynamic-static, Gaussian, splatting | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | While, main, loss, Lmain, utility, Luti, optimizable, parameters, update, only | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. • ...
- **p. 4 / 3.4. Background Brightness Control - extractive body cue:** SH Attributes Foreground Render Probabilistic Mask Brightness Control Background Render Controlled Background Composed Render Input Image Activation Rasterize Mask Rasterize Rasterize Foreground Gaussians Background Gaussians ...
- **p. 2 / 1. Introduction - extractive body cue:** To model dynamics in 3D reconstruction, recent methods such as NeRF-on-the-go, WildGaussians, and SpotlessSplats [12, 22, 24] propose to suppress transient regions during training, achieving ...
- **p. 5 / 3.6. Unsupervised scene decomposition - extractive body cue:** Input Training Iterations SpotlessSplats Mask SpotSplats Render Our Foreground Brightness Control Our controlled background Composition Mask Figure 3.
- **p. 3 / 3.1. 3D Gaussian Splatting - extractive body cue:** The final color \protect \mathbf {C} at each pixel is then computed by blending the contribution of all Gaussians, sorted by their depth:
- **p. 3 / 3.1. 3D Gaussian Splatting - extractive body cue:** To render these Gaussians onto the image plane, we use differentiable splatting [40], which applies a projection transformation \protect \mathcal {P}(\mathcal {G} ).
- **p. 4 / 3.6. Unsupervised scene decomposition - extractive body cue:** In our decoupled design, the dynamic/static gaussians rasterize the foreground/background renders Cf and Cb independently and compose (after rending) with the probabilistic mask Pf.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For each sequence, every 1 out of 5 frames is held out during training. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We take one sequence from ADT [20], AEA [16], Hot3D [2], and Epic-Field [32] dataset, respectively, ranging from 28005000 frames, to evaluate ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For each sequence, every 1 out of 5 frames is held out during training. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.8. Partial Opacity Reset - extractive body cue:** This guarantees stable training, effectively controls gaussian density, and handles local minima.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, introduce, brightness, control, mask, enhances, background, branch, capacity, model, non-Lambertian, effects, spatial-temporal, module, comprises, encoder, decoder, Hexplane, extracts, spatio-temporal.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | HyperNeRF Dataset [21] features real-world activities captured with smooth trajectories. | p. 5 (4.2. Datasets), p. 7 (4.3. Results) |
| Semantic / temporal fusion | Compared to baseline methods [10, 24, 31], our method models high-quality distractor-free static background with accurate foreground separation. | p. 6 (4.3. Results), p. 7 (4.3. Results) |
| Robot query / planning handoff | Notably, our method consistently achieves significantly better LPIPS scores over the previous SOTA method SpotlessSplats [24]. | p. 7 (4.3. Results), p. 7 (4.3. Results) |

## Failure and Ablation Link

- **p. 6 / 4.3. Results - extractive body cue:** Left of the dashed line: composed render comparisons; right: static reconstruction comparison(without camera masks).
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9. Ablation Study on AEA [16] dataset. w/o Ldepth Ours
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10. Ablation Study on Neu3D dataet [13] cut beef scene.
- **p. 8 / 6. Conclusion - extractive body cue:** This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting.
- **p. 7 / 4.3. Results - extractive body cue:** We show our method robustly handles occlusion and reconstructs fine static details compared to SpotlessSplats [24]in Fig.
- **p. 7 / 4.3. Results - extractive body cue:** Our method robustly handles various challenges, preserving clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference test views, we report detailed per-scene metrics ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Compared to SpotlessSplats [24], which is constrained by initialization and overfit to floaters. Our method offers signifi- cantly greater robustness in handling local ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.4. Background Brightness Control), p. 3 (3.2. Foreground deformable gaussian), p. 3 (3.2. Foreground deformable gaussian), p. 4 (3.4. Background Brightness Control), p. 5 (3.7. Loss function), p. 5 (3.8. Partial Opacity Reset), objective p. 5 (3.7. Loss function), p. 5 (3.7. Loss function), p. 4 (3.4. Background Brightness Control), p. 4 (3.6. Unsupervised scene decomposition), p. 3 (3.3. Probabilistic Composition Mask Rasterization), temporal p. 5 (4.2. Datasets), p. 5 (4.2. Datasets), p. 3 (3.2. Foreground deformable gaussian), p. 3 (3.2. Foreground deformable gaussian), p. 4 (3.4. Background Brightness Control), p. 6 (4.3. Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
