# Method - Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ycPVp0577R; PDF retrieval source: https://arxiv.org/pdf/2503.22204.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 5 (3 Method)): Specifically, we introduce an additional object-level loss term, 5

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** Specifically, we introduce an additional object-level loss term, 5
- **p. 6 / 3 Method - extractive body cue:** To robustly address this, we propose a partial mask filtering strategy applied at the end of training.
- **p. 4 / 3 Method - extractive body cue:** Following Deformable 3D Gaussian Splatting [17], we incorporate a deformation field to capture scene dynamics: (δx, δr, δs) = Fθ(γ(x), γ(t)), (3) where Fθ represents ...
- **p. 6 / 3 Method - extractive body cue:** 1 101 2 101 3 101 4 102 5 102 6 102 : Small-Level ID : Mid-Level ID Optimize small-level first Supervise Small-level Objects 1 ...
- **p. 4 / 3 Method - extractive body cue:** During optimization & reconstruction (Sec.
- **p. 5 / 3 Method - extractive body cue:** 3.4 Optimization & Reconstruction Optimization Goal.
- **p. 7 / 3 Method - extractive body cue:** CLIPi(·) represents the CLIP image encoder and crop(·) denotes the cropping function to extract the mask region.
- **p. 7 / 3 Method - extractive body cue:** Given an input text prompt, we perform open vocabulary query following the below strategy: fq = CLIPt(q), (10) qreturn = arg max p cos(fq, fp), ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** This enables unified static/dynamic open-vocabulary segmentation, eliminates auxiliary language fields, and significantly reduces training complexity. • Our framework features a robust object tracking module that ...
- **p. 4 / 3 Method - extractive body cue:** We introduce Segment then Splat, a unified approach for 3D open-vocabulary segmentation based on Gaussian Splatting, as illustrated in Fig.

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** Specifically, we introduce an additional object-level loss term, 5
- **p. 6 / 3 Method - extractive body cue:** To robustly address this, we propose a partial mask filtering strategy applied at the end of training.
- **p. 4 / 3 Method - extractive body cue:** Following Deformable 3D Gaussian Splatting [17], we incorporate a deformation field to capture scene dynamics: (δx, δr, δs) = Fθ(γ(x), γ(t)), (3) where Fθ represents ...
- **p. 6 / 3 Method - extractive body cue:** 1 101 2 101 3 101 4 102 5 102 6 102 : Small-Level ID : Mid-Level ID Optimize small-level first Supervise Small-level Objects 1 ...
- **p. 4 / 3 Method - extractive body cue:** During optimization & reconstruction (Sec.
- **p. 5 / 3 Method - extractive body cue:** 3.4 Optimization & Reconstruction Optimization Goal.
- **p. 7 / 3 Method - extractive body cue:** CLIPi(·) represents the CLIP image encoder and crop(·) denotes the cropping function to extract the mask region.
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Specifically, we introduce an additional object-level loss term, 5 | p. 5 (3 Method), p. 6 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To robustly address this, we propose a partial mask filtering strategy applied at the end of training. | p. 6 (3 Method), p. 4 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Following Deformable 3D Gaussian Splatting [17], we incorporate a deformation field to capture scene dynamics: (δx, δr, δs) = Fθ(γ(x), γ(t)), (3) ... | p. 4 (3 Method), p. 6 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 Method - extractive body cue:** Given an input text prompt, we perform open vocabulary query following the below strategy: fq = CLIPt(q), (10) qreturn = arg max p cos(fq, fp), ...
- **p. 5 / 3 Method - extractive body cue:** Specifically, we introduce an additional object-level loss term, 5
- **p. 5 / 3 Method - extractive body cue:** During this process, we enforce constraints to ensure that each set of Gaussians contributes only to its corresponding object.
- **p. 6 / 3 Method - extractive body cue:** The overall loss function is as follows: L = Lrender + Lobj.
- **p. 6 / 3 Method - extractive body cue:** This discrepancy can lead to incorrect constraints, ultimately distorting the geometric structure of the 3D objects.
- **p. 4 / 3 Method - extractive body cue:** During optimization & reconstruction (Sec.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Chopsticks, Initialized, Objectspecific, Gaussians, Reconstruction, Rasterize, Object, Query, Result, Trained, CLIP, Rendered, Image, Feature | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Chopsticks, Initialized, Objectspecific, Gaussians, Reconstruction, Rasterize, Object, Query, Result, Trained | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, include, Segment, then, Splat, novel, paradigm, segments, Gaussians | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Given, input, text, prompt, perform, open, vocabulary, query, following, below | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** "Chopsticks" Initialized Objectspecific Gaussians Reconstruction Rasterize Object Query Result Trained Objectspecific Gaussians "Chopsticks" Gaussians CLIP Rasterize Rendered Image & 2D Feature Map Queried 2D Mask ...
- **p. 4 / 3 Method - extractive body cue:** Following Deformable 3D Gaussian Splatting [17], we incorporate a deformation field to capture scene dynamics: (δx, δr, δs) = Fθ(γ(x), γ(t)), (3) where Fθ represents ...
- **p. 5 / 3 Method - extractive body cue:** 3.2 Robust Object Tracking Given a set of input images {Ii}n i=0, our goal is to extract multi-view masks for all objects at different granularity ...
- **p. 2 / 1 Introduction - extractive body cue:** During object queries, it renders Gaussian language embeddings into a 2D feature map to identify relevant pixels based on the input text embedding.
- **p. 1 / 1 Introduction - extractive body cue:** 3D open-vocabulary querying marks a pivotal step in language-driven interaction with 3D environments, removing the need for predefined labels.
- **p. 1 / 1 Introduction - extractive body cue:** By rendering the language field into 2D feature maps, they enable pixel-based querying by retrieving relevant pixels based on the input text embedding.
- **p. 5 / 3 Method - extractive body cue:** After object IDs are determined, we handle the lost tracking issue stated in Sec.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | As our method enforce object-Gaussian correspondence, it applies directly to dynamic scenes and performs well, whereas DGD and LSeg tend to include ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Leveraging ground-truth labels, we adopt two metrics: Object Recall Rate (ORR), defined as ORR = 1 k k X i=1 number of ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive body cue:** To robustly address this, we propose a partial mask filtering strategy applied at the end of training.
- **p. 8 / 4 Experiments - extractive body cue:** Additionally, since our method follows a single-pass reconstruction process and the scene scale is relatively small, our training time is significantly shorter compared to the ...
- **p. 9 / 4 Experiments - extractive body cue:** We omit training time results for LSeg, as it is a zero-shot method requiring no additional optimization.
- **p. 10 / 4 Experiments - extractive body cue:** To balance training time and performance, we choose three objects for LERF_OVS, Neu3D and HyperNeRF in our experiments.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, introduce, additional, object-level, loss, term, robustly, address, partial, mask, filtering, strategy, applied, training, Following, Deformable, Gaussian, Splatting, incorporate, deformation.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | (a) Static scenes LERF_OVS 3DOVS Method mIoU↑ Time↓ mIoU↑ Time↓ 2D LangSplat [10] 46.37 62.00 82.49 68.90 LEGaussians [11] 18.79 72.00 52.12 ... | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Semantic / temporal fusion | Our method outperforms all baseline approaches. | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Robot query / planning handoff | Similar to the 3DOVS dataset, 2D pixel-based methods produce less precise object boundaries, while our method demonstrates significantly improved results. | p. 8 (4 Experiments), p. 9 (4 Experiments) |

## Failure and Ablation Link

- **p. 10 / 4 Experiments - extractive body cue:** We conduct an ablation study on each component of our robust object tracking module, as shown in Tab.
- **p. 8 / 4 Experiments - extractive body cue:** Since our method explicitly enforces Gaussian-object correspondence, it can be directly applied to dynamic scenes, achieving good segmentation performance without the Gaussian-object misalignment issue encountered ...
- **p. 9 / 4 Experiments - extractive body cue:** 4.3 Ablation Study Number of Supervised Objects.
- **p. 10 / 4 Experiments - extractive body cue:** In this ablation study, we investigate the impact of the partial mask filtering strategy on segmentation performance as well as reconstruction quality.
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Effect of stride size on object recall rate (ORR) and runtime. ramen teatime Stride ORR↑ Time↓ ORR↑ Time↓
- **p. 10 / 5 Conclusion - extractive body cue:** Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such as "a sheep sitting on the chair ...
- **p. 10 / 4 Experiments - extractive body cue:** However, this minor failure does not affect the final reconstruction, as sufficient information is retained from other views.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 5 (3 Method), objective p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 4 (3 Method), temporal p. 9 (4 Experiments), p. 10 (4 Experiments), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
