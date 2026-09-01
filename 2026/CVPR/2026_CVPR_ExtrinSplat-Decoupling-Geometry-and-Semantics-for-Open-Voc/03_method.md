# Method - ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Object-level Grouping), p. 3 (3.1. Overall Architecture), p. 7 (2) Baselines. We compare our method with several recent), p. 5 (3.5. Extrinsic Semantic Index Layer), p. 6 (2) Baselines. We compare our method with several recent), p. 5 (3.5. Extrinsic Semantic Index Layer)): Specifically, for each group, we first identify the object's high-confidence core via mask back-projection, then refine its boundaries by identifying and excluding ambiguous points with our neutral point processing module, ...

## Method Body Digest

- **p. 4 / 3.3. Object-level Grouping - extractive PDF cue:** Specifically, for each group, we first identify the object's high-confidence core via mask back-projection, then refine its boundaries by identifying and excluding ambiguous points with ...
- **p. 3 / 3.1. Overall Architecture - extractive PDF cue:** Then, the instance feature extraction stage (§3.4) uses a VLM to generate textual hypotheses for each object group.
- **p. 7 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** Method Ramen Teatime Figurines Waldo Mean 2D Methods LEGaussians 46.0 60.3 40.8 39.4 46.6 LangSplat 51.2 65.1 44.7 44.5 51.4 Feature-3DGS 43.7 58.8 40.5 39.6 ...
- **p. 5 / 3.5. Extrinsic Semantic Index Layer - extractive PDF cue:** Each map i consists of a geometric component, Gi = Fi \ Ci, which is the set of indices for all 3D Gaussian points in ...
- **p. 6 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** 1, our extrinsic, decoupled architecture eliminates per-scene optimization, leading to a ∼1000x reduction in feature storage and a significantly lower VRAM footprint.
- **p. 5 / 3.5. Extrinsic Semantic Index Layer - extractive PDF cue:** This query s is then compared against the set of semantic features Qi for each object group i.
- **p. 6 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** Peak VRAM LEGaussians CVPR'24 2D Embedding Required ∼2h ∼3GB ∼20 GB LangSplat CVPR'24 2D Embedding Required ∼2h ∼3GB ∼20 GB Feature-3DGS CVPR'24 2D Embedding Required ...
- **p. 4 / 3.2. Data Preparation - extractive PDF cue:** This design minimizes the requirements for perfect input data (see Appendix for details).

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We propose ExtrinSplat, a new framework realizing the extrinsic paradigm, which efficiently decouples 3D geometry and semantics through ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To overcome these limitations, we propose the extrinsic paradigm, a distinct, decoupled and layered architecture.
- **p. 3 / 3.1. Overall Architecture - extractive PDF cue:** Our method takes an optimized 3DGS scene representation and its corresponding image sequence as input.

## Source Evidence Cues

- **p. 4 / 3.3. Object-level Grouping - extractive PDF cue:** Specifically, for each group, we first identify the object's high-confidence core via mask back-projection, then refine its boundaries by identifying and excluding ambiguous points with ...
- **p. 3 / 3.1. Overall Architecture - extractive PDF cue:** Then, the instance feature extraction stage (§3.4) uses a VLM to generate textual hypotheses for each object group.
- **p. 7 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** Method Ramen Teatime Figurines Waldo Mean 2D Methods LEGaussians 46.0 60.3 40.8 39.4 46.6 LangSplat 51.2 65.1 44.7 44.5 51.4 Feature-3DGS 43.7 58.8 40.5 39.6 ...
- **p. 5 / 3.5. Extrinsic Semantic Index Layer - extractive PDF cue:** Each map i consists of a geometric component, Gi = Fi \ Ci, which is the set of indices for all 3D Gaussian points in ...
- **p. 6 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** 1, our extrinsic, decoupled architecture eliminates per-scene optimization, leading to a ∼1000x reduction in feature storage and a significantly lower VRAM footprint.
- **p. 5 / 3.5. Extrinsic Semantic Index Layer - extractive PDF cue:** This query s is then compared against the set of semantic features Qi for each object group i.
- **p. 6 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** Peak VRAM LEGaussians CVPR'24 2D Embedding Required ∼2h ∼3GB ∼20 GB LangSplat CVPR'24 2D Embedding Required ∼2h ∼3GB ∼20 GB Feature-3DGS CVPR'24 2D Embedding Required ...
- **Detected method headings:** A Vision-Language Model (VLM) then interprets these groups (p. 1); 3. Method (p. 3); 3.1. Overall Architecture (p. 3); 2) Baselines. We compare our method with several recent (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Specifically, for each group, we first identify the object's high-confidence core via mask back-projection, then refine its boundaries by identifying and excluding ... | p. 4 (3.3. Object-level Grouping), p. 3 (3.1. Overall Architecture) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Then, the instance feature extraction stage (§3.4) uses a VLM to generate textual hypotheses for each object group. | p. 3 (3.1. Overall Architecture), p. 7 (2) Baselines. We compare our method with several recent) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Method Ramen Teatime Figurines Waldo Mean 2D Methods LEGaussians 46.0 60.3 40.8 39.4 46.6 LangSplat 51.2 65.1 44.7 44.5 51.4 Feature-3DGS 43.7 ... | p. 7 (2) Baselines. We compare our method with several recent), p. 5 (3.5. Extrinsic Semantic Index Layer) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Data Preparation - extractive PDF cue:** This design minimizes the requirements for perfect input data (see Appendix for details).
- **p. 5 / 3.4. Instance Feature Extraction - extractive PDF cue:** Extracting and storing high-dimensional visual features for every object mask in all views introduces heavy computational and storage costs, making the 3D scene representation inefficient ...
- **p. 6 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** This highlights the efficacy of our decoupled architecture in maximizing both segmentation accuracy and resource efficiency.
- **p. 7 / 4.2. Open-Vocabulary 3D Semantic Segmentation - extractive PDF cue:** The objective is to automatically extract 3D Gaussian points corresponding to input class names (e.g., wall, chair, table).
- **p. 1 / A Vision-Language Model (VLM) then interprets these groups - extractive PDF cue:** By replacing costly feature embedding with lightweight indices, ExtrinSplat reduces scene adaptation time from hours to minutes and lowers storage overhead by several orders of ...
- **p. 3 / 3.1. Overall Architecture - extractive PDF cue:** Our method takes an optimized 3DGS scene representation and its corresponding image sequence as input.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 7 (4.2. Open-Vocabulary 3D Semantic Segmentation), p. 5 (3.5. Extrinsic Semantic Index Layer).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, optimized, DGS, scene, representation, corresponding, image, sequence, input, Mainstream, direct, extraction, object, masks | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | takes, optimized, DGS, scene, representation, corresponding, image, sequence, input, Mainstream | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, ExtrinSplat, framework, realizing, extrinsic, paradigm, efficiently, decouples | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | design, minimizes, requirements, perfect, input, data, Appendix, details, Extracting, storing | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Overall Architecture - extractive PDF cue:** Our method takes an optimized 3DGS scene representation and its corresponding image sequence as input.
- **p. 5 / 3.3. Object-level Grouping - extractive PDF cue:** (a) Mainstream method (via direct extraction): All object masks, typically generated by SAM, are used to directly extract CLIP image features.
- **p. 3 / 3.1. Overall Architecture - extractive PDF cue:** Then, the instance feature extraction stage (§3.4) uses a VLM to generate textual hypotheses for each object group.
- **p. 4 / 3.2. Data Preparation - extractive PDF cue:** This design minimizes the requirements for perfect input data (see Appendix for details).
- **p. 6 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** 2, our method achieves a new state-of-the-art (SOTA) result, outperforming the previous best-performing method by 3.9 mIoU.
- **p. 6 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** In contrast, our method correctly interprets fine-grained instructions to generate precise selections with well-defined boundaries.
- **p. 7 / 4.2. Open-Vocabulary 3D Semantic Segmentation - extractive PDF cue:** The objective is to automatically extract 3D Gaussian points corresponding to input class names (e.g., wall, chair, table).
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The core of the ExtrinSplat framework is to treat each object in a 3D scene as an independent entity. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our method takes an optimized 3DGS scene representation and its corresponding image sequence as input. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** Method Ramen Teatime Figurines Waldo Mean 2D Methods LEGaussians 46.0 60.3 40.8 39.4 46.6 LangSplat 51.2 65.1 44.7 44.5 51.4 Feature-3DGS 43.7 58.8 40.5 39.6 ...
- **p. 5 / 2) Baselines. We compare our method with several recent - extractive PDF cue:** To provide a clear comparison, we detail the comparative aspects such as training time and search thresholds for these methods in Tab.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, group, first, identify, object, high-confidence, core, mask, back-projection, then, refine, boundaries, identifying, excluding, ambiguous, points, neutral, point, processing, module.
- **Relevant PDF headings:** A Vision-Language Model (VLM) then interprets these groups (p. 1); 3. Method (p. 3); 3.1. Overall Architecture (p. 3); 2) Baselines. We compare our method with several recent (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Given a text query as input, the task is to produce multi-view renderings of the semantically corresponding 3D instance(s). | p. 5 (4.1. Open-Vocabulary Object Selection in 3D Space), p. 3 (Figure/Table caption) |
| Semantic / temporal fusion | Table 5. Ablation on feature extraction. We compare VLM-based text distillation against CLIP image baselines. Case Feature Source View Aggregation mIoU↑ #1 ... | p. 8 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Robot query / planning handoff | Figure 4. Qualitative results of our 3D object segmentation on the ScanNet dataset. OpenGaussian and InstanceGaussian rely on matching CLIP features extracted ... | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation on neutral point processing. We evaluate the impact of our two-stage filtering on the LERF dataset. Case
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation on feature extraction. We compare VLM-based text distillation against CLIP image baselines. Case Feature Source View Aggregation mIoU↑ #1 Image
- **p. 8 / 5. Conclusion and Limitation - extractive PDF cue:** Despite its strong performance, our method has certain limitations: 1) The accuracy of our object-level grouping can be compromised by substantially inaccurate initial segmentation masks ...
- **p. 8 / 5. Conclusion and Limitation - extractive PDF cue:** Addressing these issues remains a promising direction for future work.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative results on object selection from the LERF dataset. OpenGaussian fails to separate nearby objects or maintain sharp boundaries, while Dr.Splat struggles to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.3. Object-level Grouping), p. 3 (3.1. Overall Architecture), p. 7 (2) Baselines. We compare our method with several recent), p. 5 (3.5. Extrinsic Semantic Index Layer), p. 6 (2) Baselines. We compare our method with several recent), p. 5 (3.5. Extrinsic Semantic Index Layer), objective p. 4 (3.2. Data Preparation), p. 5 (3.4. Instance Feature Extraction), p. 6 (2) Baselines. We compare our method with several recent), p. 7 (4.2. Open-Vocabulary 3D Semantic Segmentation), p. 1 (A Vision-Language Model (VLM) then interprets these groups), p. 3 (3.1. Overall Architecture), temporal p. 3 (3.1. Overall Architecture), p. 3 (3.1. Overall Architecture), p. 5 (3.4. Instance Feature Extraction), p. 1 (Abstract), p. 1 (A Vision-Language Model (VLM) then interprets these groups), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
