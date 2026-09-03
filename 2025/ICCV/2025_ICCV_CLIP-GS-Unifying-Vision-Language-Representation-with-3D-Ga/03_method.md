# Method - CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jiao_CLIP-GS_Unifying_Vision-Language_Representation_with_3D_Gaussian_Splatting_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jiao_CLIP-GS_Unifying_Vision-Language_Representation_with_3D_Gaussian_Splatting_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (4. Methodology), p. 4 (4.2. Multi-model Alignment), p. 7 (Method), p. 8 (Method), p. 8 (Method), p. 3 (4. Methodology)): We introduce the feature extraction process from 3DGS, detailed in Sec.

## Method Body Digest

- **p. 3 / 4. Methodology - extractive body cue:** We introduce the feature extraction process from 3DGS, detailed in Sec.
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** In response, we propose the image voting loss (Limg).
- **p. 7 / Method - extractive body cue:** 5). • Baseline: We use the point cloud-based method, Uni3D [63], as the baseline model (1st row), and extract the P and C attributes of ...
- **p. 8 / Method - extractive body cue:** loss learns effective 3DGS and image alignment representation, further enhancing performance to establish stateof-the-art benchmarks (last row).
- **p. 8 / Method - extractive body cue:** 7, exploring the effectiveness of initializing transformer layers in CLIP-GS with either 2D pretraining models or point cloud pretraining models.
- **p. 3 / 4. Methodology - extractive body cue:** We also introduce a novel loss function, termed image voting loss, to guide the convergence of gradient optimization.
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** The pre-trained vision language model EVA-CLIP [38] is adopted during training.
- **p. 8 / Method - extractive body cue:** Therefore, we opt for 5000 iterations and an SH degree of 0, accepting a slight decrease in reconstruction quality in exchange for a × 3.9 ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions are summarized as follows: • We propose CLIP-GS, a simple yet effective framework for encoding 3DGS into features, leveraging a contrastive learning ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce a multimodal representation learning method leveraging 3DGS, termed CLIP-GS.
- **p. 3 / 4. Methodology - extractive body cue:** We introduce the feature extraction process from 3DGS, detailed in Sec.

## Source Evidence Cues

- **p. 3 / 4. Methodology - extractive body cue:** We introduce the feature extraction process from 3DGS, detailed in Sec.
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** In response, we propose the image voting loss (Limg).
- **p. 7 / Method - extractive body cue:** 5). • Baseline: We use the point cloud-based method, Uni3D [63], as the baseline model (1st row), and extract the P and C attributes of ...
- **p. 8 / Method - extractive body cue:** loss learns effective 3DGS and image alignment representation, further enhancing performance to establish stateof-the-art benchmarks (last row).
- **p. 8 / Method - extractive body cue:** 7, exploring the effectiveness of initializing transformer layers in CLIP-GS with either 2D pretraining models or point cloud pretraining models.
- **p. 3 / 4. Methodology - extractive body cue:** We also introduce a novel loss function, termed image voting loss, to guide the convergence of gradient optimization.
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** The pre-trained vision language model EVA-CLIP [38] is adopted during training.
- **Detected method headings:** 4. Methodology (p. 3); 4.2. Multi-model Alignment (p. 4); Method (p. 7); 5.5. Scaling up model size (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We introduce the feature extraction process from 3DGS, detailed in Sec. | p. 3 (4. Methodology), p. 4 (4.2. Multi-model Alignment) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In response, we propose the image voting loss (Limg). | p. 4 (4.2. Multi-model Alignment), p. 7 (Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 5). • Baseline: We use the point cloud-based method, Uni3D [63], as the baseline model (1st row), and extract the P and ... | p. 7 (Method), p. 8 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 4. Methodology - extractive body cue:** We also introduce a novel loss function, termed image voting loss, to guide the convergence of gradient optimization.
- **p. 8 / Method - extractive body cue:** Therefore, we opt for 5000 iterations and an SH degree of 0, accepting a slight decrease in reconstruction quality in exchange for a × 3.9 ...
- **p. 8 / Method - extractive body cue:** Restruction of 3DGS We analyzed the reconstruction quality (PSNR, SSIM), optimization cost (optimization time per 3D shape), and storage cost (average 3DGS storage size) of ...
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** In response, we propose the image voting loss (Limg).
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** Existing point cloud pre-training approaches randomly sample one image from the rendering set and impose a contrastive loss restriction, similar to Eq.
- **p. 5 / 4.2. Multi-model Alignment - extractive body cue:** as described by the following formula: Limg = -1 2N N X i=1 Si · (Contra(EG i , EI) + Contra(EI i , EG)) (4) ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (4. Methodology), p. 4 (4.2. Multi-model Alignment), p. 4 (4.2. Multi-model Alignment), p. 7 (Method), p. 7 (Method), p. 8 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Here, position, color, attributes, extracted, input, point, cloud, encoder, detailed, Baseline, cloud-based, Uni3D, model | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Here, position, color, attributes, extracted, input, point, cloud, encoder, detailed | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Overall, contributions, summarized, follows, CLIP-GS, simple, effective, framework, encoding, DGS | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | introduce, novel, loss, function, termed, image, voting, guide, convergence, gradient | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 4.1. Feature Extraction - extractive body cue:** Here, position and color attributes (P & C) are extracted and input into a point cloud encoder, as detailed in [63].
- **p. 7 / Method - extractive body cue:** 5). • Baseline: We use the point cloud-based method, Uni3D [63], as the baseline model (1st row), and extract the P and C attributes of ...
- **p. 8 / Method - extractive body cue:** loss learns effective 3DGS and image alignment representation, further enhancing performance to establish stateof-the-art benchmarks (last row).
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** Existing point cloud pre-training approaches randomly sample one image from the rendering set and impose a contrastive loss restriction, similar to Eq.
- **p. 2 / 1. Introduction - extractive body cue:** Remarkably, our approach outperforms the existing point cloud-based models, and establishes new state-of-the-art results on all benchmarks.
- **p. 3 / 4. Methodology - extractive body cue:** We introduce the feature extraction process from 3DGS, detailed in Sec.
- **p. 4 / 4.1. Feature Extraction - extractive body cue:** The outputs of these processes are finally fused to obtain GS tokens ˆ GSt ∈Rg×d, where d denotes the dimension of GS tokens.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The complete framework is shown in Fig. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Within CLIP-GS, the FPS & kNN is first used to form 3DGS into gaussian patches. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / Method - extractive body cue:** 7, exploring the effectiveness of initializing transformer layers in CLIP-GS with either 2D pretraining models or point cloud pretraining models.
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** The pre-trained vision language model EVA-CLIP [38] is adopted during training.
- **p. 5 / 5.2. Zero-Shot 3D Classification - extractive body cue:** ULIP, OpenShape, and Uni3D train 3D encoders to align the visual-text representation and use point clouds for classification.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, feature, extraction, process, DGS, detailed, Sec, response, image, voting, loss, Limg, Baseline, point, cloud-based, Uni3D, model, extract, attributes, gaussian.
- **Relevant PDF headings:** 4. Methodology (p. 3); 4.2. Multi-model Alignment (p. 4); Method (p. 7); 5.5. Scaling up model size (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 3 to construct the ModelNet-GS dataset. | p. 5 (5.2. Zero-Shot 3D Classification), p. 5 (5.1. Multimodal Retrieval) |
| Semantic / temporal fusion | Comparisons with state-of-the-art methods. | p. 5 (5.1. Multimodal Retrieval), p. 1 (Figure/Table caption) |
| Robot query / planning handoff | CLIP-GS demonstrates a comprehensive improvement over existing zero-shot 3D classification models, achieving a performance boost of + 0.8, + 0.5 on Objaverse-GS ... | p. 5 (5.2. Zero-Shot 3D Classification), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Visualization of different order strategies. We project the 3D space onto a 2D plane. Effect of pre-initialized weights. We conduct ablation studies on ...
- **p. 6 / 5.4. Ablation Study - extractive body cue:** To understand the effect of each component in the CLIP-GS, we start with the official 4675
- **p. 5 / 5. Experiments - extractive body cue:** Furthermore, we perform ablation studies (Sec.
- **p. 6 / 5.3. Few-Shot 3D Classification - extractive body cue:** For a fair comparison, all methods are trained without Objaverse-LVIS shapes.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 9. Scaling up model size in CLIP-GS. Top1 accuracy in Objaverse-GS is used for analysis. We explore the effect of scaling up the model ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Zero-shot classification on Objaverse-GS, and ModelNet-GS. "no LVIS" denotes model is trained without Objaverse-LVIS shapes.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Ablation of diverse designs of CLIP-GS. We use the Objaverse-GS for analysis. P&C denotes only P and C attributes of gaussian points from ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (4. Methodology), p. 4 (4.2. Multi-model Alignment), p. 7 (Method), p. 8 (Method), p. 8 (Method), p. 3 (4. Methodology), objective p. 3 (4. Methodology), p. 8 (Method), p. 8 (Method), p. 4 (4.2. Multi-model Alignment), p. 4 (4.2. Multi-model Alignment), p. 5 (4.2. Multi-model Alignment), temporal p. 3 (4. Methodology), p. 3 (4.1. Feature Extraction), p. 4 (4.1. Feature Extraction), p. 1 (Abstract), p. 2 (2. Related Work), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
