# Method - CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=a3ptUbuzbW; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114864. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD)): 4, it first pre-trains a coarse model on full training data with the schedule of 3DGS.

## Method Body Digest

- **p. 4 / 3 METHOD - extractive body cue:** 4, it first pre-trains a coarse model on full training data with the schedule of 3DGS.
- **p. 6 / 3 METHOD - extractive body cue:** To bypass the distillation step, we use an SH degree of 2 from the start, reducing the SH feature dimension from 48 to 27.
- **p. 5 / 3 METHOD - extractive body cue:** The derived outputs are used for loss calculation.
- **p. 6 / 3 METHOD - extractive body cue:** We first evaluate each point's contribution across all training data.
- **p. 7 / 3 METHOD - extractive body cue:** 5, we begin by initializing a 3DGS field with the ground-truth point cloud, then traverse all training views to rasterize and count visible frequency through ...
- **p. 4 / 3 METHOD - extractive body cue:** The loss L that supervises 3DGS's optimization is the weighted sum of two parts, L1 loss L1 and D-SSIM loss LSSIM.
- **p. 5 / 3 METHOD - extractive body cue:** 3.2 OPTIMIZATION MECHANISM This section elaborates on the proposed optimization mechanism for convergence acceleration and stable training.
- **p. 6 / 3 METHOD - extractive body cue:** To alleviate this problem, we prioritize the gradient from SSIM loss and introduce a Decomposed-Gradient-based Densification (DGD) strategy.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to be ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, our contribution-based vectree quantization enables a tenfold reduction in storage requirements for large-scale 2DGS.
- **p. 6 / 3 METHOD - extractive body cue:** To resolve these issues, we propose a novel pipeline, as shown in Fig.

## Source Evidence Cues

- **p. 4 / 3 METHOD - extractive body cue:** 4, it first pre-trains a coarse model on full training data with the schedule of 3DGS.
- **p. 6 / 3 METHOD - extractive body cue:** To bypass the distillation step, we use an SH degree of 2 from the start, reducing the SH feature dimension from 48 to 27.
- **p. 5 / 3 METHOD - extractive body cue:** The derived outputs are used for loss calculation.
- **p. 6 / 3 METHOD - extractive body cue:** We first evaluate each point's contribution across all training data.
- **p. 7 / 3 METHOD - extractive body cue:** 5, we begin by initializing a 3DGS field with the ground-truth point cloud, then traverse all training views to rasterize and count visible frequency through ...
- **p. 4 / 3 METHOD - extractive body cue:** The loss L that supervises 3DGS's optimization is the weighted sum of two parts, L1 loss L1 and D-SSIM loss LSSIM.
- **p. 5 / 3 METHOD - extractive body cue:** 3.2 OPTIMIZATION MECHANISM This section elaborates on the proposed optimization mechanism for convergence acceleration and stable training.
- **Detected method headings:** 3 METHOD (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 4, it first pre-trains a coarse model on full training data with the schedule of 3DGS. | p. 4 (3 METHOD), p. 6 (3 METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To bypass the distillation step, we use an SH degree of 2 from the start, reducing the SH feature dimension from 48 ... | p. 6 (3 METHOD), p. 5 (3 METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The derived outputs are used for loss calculation. | p. 5 (3 METHOD), p. 6 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 METHOD - extractive body cue:** To alleviate this problem, we prioritize the gradient from SSIM loss and introduce a Decomposed-Gradient-based Densification (DGD) strategy.
- **p. 6 / 3 METHOD - extractive body cue:** Specifically, the gradient for densification is reformulated as: ∇densify = max  ω × /∇L/avg /∇LSSIM/avg , 1  × ∇LSSIM, (2) where ∇LSSIM is ...
- **p. 4 / 3 METHOD - extractive body cue:** The loss L that supervises 3DGS's optimization is the weighted sum of two parts, L1 loss L1 and D-SSIM loss LSSIM.
- **p. 5 / 3 METHOD - extractive body cue:** As the training progresses, we decrease the loss weight α exponentially to suppress the adverse effect of imperfect depth estimation gradually.
- **p. 4 / 3 METHOD - extractive body cue:** The Gaussians with a gradient larger than a certain threshold would be cloned or split.
- **p. 5 / 3 METHOD - extractive body cue:** The derived outputs are used for loss calculation.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | begin, initializing, DGS, field, ground-truth, point, cloud, then, traverse, training, views, rasterize, count, visible | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | begin, initializing, DGS, field, ground-truth, point, cloud, then, traverse, training | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, four-fold, novel, optimization, strategy, DGS, accelerates, convergence, under | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | alleviate, problem, prioritize, gradient, SSIM, loss, introduce, Decomposed-Gradient-based, Densification, DGD | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 3 METHOD - extractive body cue:** 5, we begin by initializing a 3DGS field with the ground-truth point cloud, then traverse all training views to rasterize and count visible frequency through ...
- **p. 17 / C MORE IMPLEMENTATION DETAILS - extractive body cue:** Secondly, for mesh extraction, occlusion and lack of observation hinder reconstruction of some road surfaces and building facades.
- **p. 5 / 3 METHOD - extractive body cue:** The derived outputs are used for loss calculation.
- **p. 5 / 3 METHOD - extractive body cue:** In light of this observation, we implement a straightforward yet effective Elongation Filter to address this problem.
- **p. 7 / 3 METHOD - extractive body cue:** Moreover, GauU-Scene does not align the surface points extraction process across methods, leading to unfair comparison.
- **p. 6 / 3 METHOD - extractive body cue:** Suppose that the images assigned to m-th block using CityGS (Liu et al., 2024)'s strategy is Vm, then the average contribution is: Cn = 1 ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Another challenge lies in the evaluation protocol: due to insufficient observations in boundary regions, geometry estimation becomes error-prone and unstable in these areas.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The total number of Gaussians can increase to 19.3 million during parallel training, resulting in a storage requirement of 4.6 GB and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 3, this filter mitigates out-ofmemory errors and facilitates a more steady Gaussian count evolution. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | The total number of Gaussians can increase to 19.3 million during parallel training, resulting in a storage requirement of 4.6 GB and ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The total number of Gaussians can increase to 19.3 million during parallel training, resulting in a storage requirement of 4.6 GB and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 METHOD - extractive body cue:** 4, it first pre-trains a coarse model on full training data with the schedule of 3DGS.
- **p. 6 / 3 METHOD - extractive body cue:** We first evaluate each point's contribution across all training data.
- **p. 7 / 3 METHOD - extractive body cue:** 5, we begin by initializing a 3DGS field with the ground-truth point cloud, then traverse all training views to rasterize and count visible frequency through ...
- **p. 5 / 3 METHOD - extractive body cue:** 3.2 OPTIMIZATION MECHANISM This section elaborates on the proposed optimization mechanism for convergence acceleration and stable training.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** The tiny version (ours-t) can even halve the training time.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 2, the small version of CityGaussianV2 (ours-s) reduces training time by 25% and memory usage by over 50%, while delivering superior geometric performance and on-par ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, pre-trains, coarse, model, full, training, data, schedule, DGS, bypass, distillation, step, degree, start, reducing, feature, dimension, derived, outputs, loss.
- **Relevant PDF headings:** 3 METHOD (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Therefore, we utilize the realistic dataset GauU-Scene (Xiong et al., 2024) and the synthetic dataset MatrixCity (Li et al., 2023a). | p. 7 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Semantic / temporal fusion | 5.2 COMPARISON WITH SOTA METHODS In this section, we compare CityGaussianV2 with state-of-the-art (SOTA) methods both quantitatively and qualitatively. | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Robot query / planning handoff | For MatrixCity-Aerial, our method achieves the best surface quality among all algorithms, with the F1 score being twice that of 2DGS and ... | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 14 / Figure/Table caption - extractive body cue:** Figure 10: Qualitative ablation of 7K iteration results among different methods. This section provides additional qualitative comparisons. As illustrated in Fig. 8, the mesh produced ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Ablation on model components. The experiments are conducted on Residence scene of GauU-Scene dataset ((Xiong et al., 2024)). Here we take 2DGS ((Huang ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 1 shows that even without parallel tuning, our proposed optimization strategy enables our model to achieve significantly better 8
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of our optimization mechanism. We densify Gaussians exclusively according to the gradient of SSIM loss. This helps remove large and blurry Gaussians ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Illustration of pipeline modification. The pipeline of CityGS (Liu et al., 2024) (dashed boxes and arrows) is compared with ours. We successfully removed ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 4: Detailed comparison among SOTA among parallel training methods. 2DGS* here means applying CityGS's training strategy to 2DGS without our proposed optimization mechanism. And ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 7: Ablation on gradient source of densification. The experiments are conducted on the Resi- dence scene of the GauU-Scene dataset ((Xiong et al., 2024)). ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD), objective p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), temporal p. 2 (1 INTRODUCTION), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
