# Method - MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Model Architecture), p. 4 (4.2. Data and Training), p. 6 (Model), p. 6 (Model), p. 7 (Model), p. 7 (Model)): We use the MM1.5 architecture [85, 128] (focusing on the mobile-friendly 3B variant), comprising of a DFN-CLIP [34, 89] image encoder and a decoder-only LLM backbone, which are bridged via ...

## Method Body Digest

- **p. 4 / 4.1. Model Architecture - extractive PDF cue:** We use the MM1.5 architecture [85, 128] (focusing on the mobile-friendly 3B variant), comprising of a DFN-CLIP [34, 89] image encoder and a decoder-only LLM ...
- **p. 4 / 4.2. Data and Training - extractive PDF cue:** We use AXLearn [7] for model training.
- **p. 6 / Model - extractive PDF cue:** 13 ), suggesting that our model can successfully use additional views to improve 3D perception. • Multi-view 19 vs.
- **p. 6 / Model - extractive PDF cue:** 2D object grounding and depth prediction) and/or leveraging more test-time compute benefits model accuracy. • Depth (GT): Tool-use vs.
- **p. 7 / Model - extractive PDF cue:** We evaluate the metric depth estimates of our CoT model produced as part of its responses on the CA-VQA benchmark.
- **p. 7 / Model - extractive PDF cue:** MM-Spatial-3B substantially outperforms the (much larger) SOTA models, with CoT and depth input further improving performance.
- **p. 8 / Model - extractive PDF cue:** Training on a mixture of CA-VQAω and OSD performs best.
- **p. 8 / Model - extractive PDF cue:** MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, outperforming SpatialRGPT-VILA-1.5-8B (which fully encodes depth).

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** To address these †Equal contribution.

## Source Evidence Cues

- **p. 4 / 4.1. Model Architecture - extractive PDF cue:** We use the MM1.5 architecture [85, 128] (focusing on the mobile-friendly 3B variant), comprising of a DFN-CLIP [34, 89] image encoder and a decoder-only LLM ...
- **p. 4 / 4.2. Data and Training - extractive PDF cue:** We use AXLearn [7] for model training.
- **p. 6 / Model - extractive PDF cue:** 13 ), suggesting that our model can successfully use additional views to improve 3D perception. • Multi-view 19 vs.
- **p. 6 / Model - extractive PDF cue:** 2D object grounding and depth prediction) and/or leveraging more test-time compute benefits model accuracy. • Depth (GT): Tool-use vs.
- **p. 7 / Model - extractive PDF cue:** We evaluate the metric depth estimates of our CoT model produced as part of its responses on the CA-VQA benchmark.
- **p. 7 / Model - extractive PDF cue:** MM-Spatial-3B substantially outperforms the (much larger) SOTA models, with CoT and depth input further improving performance.
- **p. 8 / Model - extractive PDF cue:** Training on a mixture of CA-VQAω and OSD performs best.
- **Detected method headings:** 4. Model (p. 4); 4.1. Model Architecture (p. 4); 5.1. Model Variants (p. 4); Model (p. 6); Model (p. 7); Model (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We use the MM1.5 architecture [85, 128] (focusing on the mobile-friendly 3B variant), comprising of a DFN-CLIP [34, 89] image encoder and ... | p. 4 (4.1. Model Architecture), p. 4 (4.2. Data and Training) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We use AXLearn [7] for model training. | p. 4 (4.2. Data and Training), p. 6 (Model) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 13 ), suggesting that our model can successfully use additional views to improve 3D perception. • Multi-view 19 vs. | p. 6 (Model), p. 6 (Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | MM-Spatial-3B, achieves, SOTA, image-only, input, tool-use, monocular, depth, outperforming, SpatialRGPT-VILA-1, fully, encodes, There, have | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | MM-Spatial-3B, achieves, SOTA, image-only, input, tool-use, monocular, depth, outperforming, SpatialRGPT-VILA-1 | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, Equal, contribution, MM-Spatial-3B, achieves, SOTA, image-only, input, tool-use, monocular | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / Model - extractive PDF cue:** MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, outperforming SpatialRGPT-VILA-1.5-8B (which fully encodes depth).
- **p. 1 / 1. Introduction - extractive PDF cue:** There have been comparatively few works on 3D object perception with MLLMs [15, 20, 27, 28, 32, 98]; moreover, they only consider a subset of ...
- **p. 4 / 4.1. Model Architecture - extractive PDF cue:** Our model supports multi-image input, allowing us to concatenate multiple views into sequences It→N, ..., It→1, It.
- **p. 4 / 4.1. Model Architecture - extractive PDF cue:** We also consider variants of our model that incorporate either multiple views or depth maps as additional inputs: • Multi-view.
- **p. 6 / Model - extractive PDF cue:** Model performance is further improved by incorporating multi-view and/or depth as additional input signals, as well as by leveraging CoT, which relies on our model's ...
- **p. 7 / Model - extractive PDF cue:** MM-Spatial-3B substantially outperforms the (much larger) SOTA models, with CoT and depth input further improving performance.
- **p. 8 / Model - extractive PDF cue:** MM-Spatial-3B outperforms the SOTA SpatialRGPT-VILA-1.5-8B 5 with different data mixtures 10 - 12 , with and without 8 depth input (SpatialRGPT uses depth maps via ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We use up to four support frames plus one reference frame. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We also study the benefits of providing additional views (images) to the model, i.e., frames preceding the main image in the video. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4.2. Data and Training - extractive PDF cue:** We use AXLearn [7] for model training.
- **p. 8 / Model - extractive PDF cue:** Training on a mixture of CA-VQAω and OSD performs best.
- **p. 4 / 4.2. Data and Training - extractive PDF cue:** We use the same training hyperparameters as MM1.5 [128], with unfrozen image encoder and LLM.
- **p. 4 / 4.2. Data and Training - extractive PDF cue:** For the 3) supervised fine-tuning (SFT) stage, we start from the MM1.5 single-image SFT mixture, which includes datasets across multiple categories: General VQA, Knowledge (math, ...
- **p. 5 / 5.1. Model Variants - extractive PDF cue:** Trained on singleview RGB inputs plus fully encoded depth maps, as described in Sec.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** MM1, architecture, focusing, mobile-friendly, variant, comprising, DFN-CLIP, image, encoder, decoder-only, LLM, backbone, bridged, C-Abstractor, AXLearn, model, training, suggesting, successfully, additional.
- **Relevant PDF headings:** 4. Model (p. 4); 4.1. Model Architecture (p. 4); 5.1. Model Variants (p. 4); Model (p. 6); Model (p. 7); Model (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from sensors and monocular) and ... | p. 2 (Dataset), p. 2 (Dataset) |
| Semantic / temporal fusion | In contrast, on our CA-VQA benchmark, using vision input outperforms the blind baseline on Counting by →13 points. | p. 7 (5.4. CV-Bench Results), p. 6 (Figure/Table caption) |
| Robot query / planning handoff | Table 3. CA-VQA Results. MM-Spatial-3B significantly outperforms (much larger) top open-source and commercial models across all tasks, demonstrating its strong spatial understanding ... | p. 6 (Figure/Table caption), p. 5 (5.2. Overview of Benchmark Category Results) |

## Failure and Ablation Link

- **p. 4 / 5.1. Model Variants - extractive PDF cue:** Trained on single-view RGB inputs, without depth information.
- **p. 4 / 5.1. Model Variants - extractive PDF cue:** We explore the following model variants in our study, leveraging the various input signals provided within CA-VQA: • MM-Spatial.
- **p. 5 / 5.3. Results on our CA-VQA Benchmark - extractive PDF cue:** We assess the model variants outlined in Sec.
- **p. 5 / 5.2. Overview of Benchmark Category Results - extractive PDF cue:** 4.2 by default; some ablations use Specialist Models trained only on CA-VQA.
- **p. 7 / 5.5. SpatialRGPT-Bench Results - extractive PDF cue:** To enable a fair comparison of model capabilities, we thus align with the benchmark by generating CA-VQAω, a variant of CA-VQA adopting their AABB-based definitions, ...
- **p. 2 / Dataset - extractive PDF cue:** We apply this pipeline to CA-1M [61] to generate Cubify Anything VQA (CAVQA), a new spatial understanding dataset for MLLM fine-tuning, covering diverse indoor scenes.
- **p. 2 / Dataset - extractive PDF cue:** CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from sensors and monocular) and multi-view images, covers ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.1. Model Architecture), p. 4 (4.2. Data and Training), p. 6 (Model), p. 6 (Model), p. 7 (Model), p. 7 (Model), objective 본문 anchor 없음, temporal p. 5 (5.1. Model Variants), p. 3 (2.2. 3D Spatial Understanding with MLLMs), p. 4 (3.3. Multi-view and Metric Depth Data), p. 1 (Front matter), p. 3 (2.2. 3D Spatial Understanding with MLLMs), p. 4 (3.3. Multi-view and Metric Depth Data).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
