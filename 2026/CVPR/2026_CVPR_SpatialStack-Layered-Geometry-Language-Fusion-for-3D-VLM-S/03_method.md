# Method - SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 8 (Model), p. 8 (Model)): 4, our two versions of SpatialStack surpass all baselines of similar scale and same base models on both 2D and 3D subsets, demonstrating the benefits of multi-level geometry feature stacking ...

## Method Body Digest

- **p. 8 / Model - extractive PDF cue:** 4, our two versions of SpatialStack surpass all baselines of similar scale and same base models on both 2D and 3D subsets, demonstrating the benefits ...
- **p. 8 / Model - extractive PDF cue:** (%) Proprietary Models (API) GPT-4o [14] 74.8 83.0 78.9 Open-source Models Mini-Gemini-HD-34B [22] 71.5 79.2 75.4 LLaVA-NeXT-34B [19] 73.0 74.8 73.9 Cambrian-1-34B [40] 74.0 79.7 ...
- **p. 2 / 1. Introduction - extractive PDF cue:** An initial line of work sought to compensate for these weaknesses by integrating explicit geometric inputs (e.g., precomputed point clouds or depth maps) into VLMs.
- **p. 1 / 1. Introduction - extractive PDF cue:** Despite remarkable progress in large vision-language models (VLMs), reliable spatial reasoning remains challenging, as these models often fail to effectively encode 3D geometry and spatial ...
- **p. 2 / 1. Introduction - extractive PDF cue:** These models can infer rich geometric attributes such as depth, camera pose, and 3D structure directly from multi-view images, thereby bypassing traditional, computationally expensive geometric ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Motivated by this, recent work on spatial reasoning aims to enable embodied agents to interpret scene layouts, predict interactions, and plan actions in 3D environments, ...
- **p. 8 / Model - extractive PDF cue:** Scaling to Qwen3.5, SpatialStack-5B further improves upon its baseline to set a new state-of-the-art.
- **p. 8 / Model - extractive PDF cue:** Evaluation on General-purpose Capabilities.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** We summarize our contributions as follows: • We present the first systematic analysis of how fusion layers across vision encoders, geometry encoders, and LLM decoders ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Building on these insights, we introduce SpatialStack, a general hierarchical fusion framework that integrates multi-level geometric features into multimodal LLMs.
- **p. 8 / Model - extractive PDF cue:** 5 shows that our method maintains robust general capabilities while specializing in spatial-temporal tasks, confirming no catastrophic forgetting.

## Source Evidence Cues

- **p. 8 / Model - extractive PDF cue:** 4, our two versions of SpatialStack surpass all baselines of similar scale and same base models on both 2D and 3D subsets, demonstrating the benefits ...
- **p. 8 / Model - extractive PDF cue:** (%) Proprietary Models (API) GPT-4o [14] 74.8 83.0 78.9 Open-source Models Mini-Gemini-HD-34B [22] 71.5 79.2 75.4 LLaVA-NeXT-34B [19] 73.0 74.8 73.9 Cambrian-1-34B [40] 74.0 79.7 ...
- **Detected method headings:** Model (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 4, our two versions of SpatialStack surpass all baselines of similar scale and same base models on both 2D and 3D subsets, ... | p. 8 (Model), p. 8 (Model) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (%) Proprietary Models (API) GPT-4o [14] 74.8 83.0 78.9 Open-source Models Mini-Gemini-HD-34B [22] 71.5 79.2 75.4 LLaVA-NeXT-34B [19] 73.0 74.8 73.9 Cambrian-1-34B ... | p. 8 (Model) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 4, our two versions of SpatialStack surpass all baselines of similar scale and same base models on both 2D and 3D subsets, ... | p. 8 (Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | initial, line, sought, compensate, weaknesses, integrating, explicit, geometric, inputs, precomputed, point, clouds, depth, maps | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | initial, line, sought, compensate, weaknesses, integrating, explicit, geometric, inputs, precomputed | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, contributions, follows, present, first, systematic, analysis, fusion, layers, across | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** An initial line of work sought to compensate for these weaknesses by integrating explicit geometric inputs (e.g., precomputed point clouds or depth maps) into VLMs.
- **p. 1 / 1. Introduction - extractive PDF cue:** Despite remarkable progress in large vision-language models (VLMs), reliable spatial reasoning remains challenging, as these models often fail to effectively encode 3D geometry and spatial ...
- **p. 2 / 1. Introduction - extractive PDF cue:** These models can infer rich geometric attributes such as depth, camera pose, and 3D structure directly from multi-view images, thereby bypassing traditional, computationally expensive geometric ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Motivated by this, recent work on spatial reasoning aims to enable embodied agents to interpret scene layouts, predict interactions, and plan actions in 3D environments, ...
- **p. 8 / Model - extractive PDF cue:** Scaling to Qwen3.5, SpatialStack-5B further improves upon its baseline to set a new state-of-the-art.
- **p. 8 / Model - extractive PDF cue:** Evaluation on General-purpose Capabilities.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Bridging this gap requires unifying geometric awareness with vision-language reasoning within a single framework, which is a key step toward reliable spatial ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Applying our framework to both Qwen2.5 [2] and Qwen3.5 [38] yields substantial improvements over their untuned base models. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 5.1. Training - extractive PDF cue:** Training is performed with a batch size of 64 and a learning rate of 1 × 10-5, optimized using the AdamW optimizer with a warmup ...
- **p. 7 / 5.1. Training - extractive PDF cue:** During instruction tuning, the geometry encoder (VGGT) and the vision encoder are kept frozen, while the geometry token merger modules and the LLM decoder are ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** versions, SpatialStack, surpass, baselines, similar, scale, same, base, models, subsets, demonstrating, benefits, multi-level, geometry, feature, stacking, unified, spatial, perception, Proprietary.
- **Relevant PDF headings:** Model (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | VLM-3R reformulates spatial question-answer pairs in a VSI-Bench-style format, producing diverse reasoning tasks such as relative direction, object counting, and absolute distance ... | p. 7 (5.1. Training), p. 7 (5.2. Evaluation) |
| Semantic / temporal fusion | Table 4. Comparison on CV-Bench. Built on Qwen2.5, SpatialStack-4B outperforms its base model alongside VG-LLM and Cambrian-S. Scaling to Qwen3.5, SpatialStack-5B further ... | p. 8 (Figure/Table caption), p. 7 (5.2. Evaluation) |
| Robot query / planning handoff | Furthermore, under a fair comparison using the identical Qwen2.5 base model, SpatialStack significantly outperforms other concurrent geometry-aware MLLMs, such as Spatial-MLLM [45], ... | p. 7 (5.2. Evaluation), p. 5 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 5. Experiments - extractive PDF cue:** 5.2, and provide extensive ablation studies in Sec.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Effect of Geometry Injection Layers on Spatial Tasks. Deeper layers improve high-level tasks, while low-level tasks peak at layer 11 and decline at ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Ablation Results on Geometry Token Fusion Depth. Simply fusing multi-layer geometry features to the visual features yields suboptimal performance, while selecting an appropriate ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Cross-benchmark Ablation. SpatialStack achieves the best cross-task transfer ability, obtaining the highest scores on VSI-Bench, SPAR-Bench, CV-Bench, and the overall aver- age, while ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. Layer Selection Ablation. Performance comparison of extracting geometry features from different deep VGGT lay- ers (L21, L22, L23) and their multi-layer combinations. Methods ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 7. Geometry-Language Fusion Order Ablation. Com- parison of our progressive hierarchical alignment against a reverse fusion strategy and baseline models. deep features. Tab. 6 ...
- **p. 7 / 5.1. Training - extractive PDF cue:** We fine-tune the model using the standard language modeling cross-entropy loss.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 8 (Model), p. 8 (Model), objective 본문 anchor 없음, temporal p. 2 (1. Introduction), p. 7 (5.2. Evaluation), p. 5 (4.2. VLM-SpatialStack), p. 6 (4.2. VLM-SpatialStack), p. 1 (Front matter), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
