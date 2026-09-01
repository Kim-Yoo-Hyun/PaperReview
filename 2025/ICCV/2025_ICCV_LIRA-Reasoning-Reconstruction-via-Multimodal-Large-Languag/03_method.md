# Method - LIRA: Reasoning Reconstruction via Multimodal Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 7 (4.5. Runtime Analysis), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 5 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 7 (4.4. Explicit Instruction-Guided Reconstruction)): (3) Then, fimg and ˆhseg (text feature prompt) are input into the mask decoder Fdec of the segmentation foundation model to output the binary mask mseg of the candidate instance.

## Method Body Digest

- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** (3) Then, fimg and ˆhseg (text feature prompt) are input into the mask decoder Fdec of the segmentation foundation model to output the binary mask ...
- **p. 7 / 4.5. Runtime Analysis - extractive PDF cue:** To achieve real-time inference, we propose LIRA-Fast.
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** The image features directly use the image embeddings fimg of the segmentation foundation model in the 2D reasoning segmentation module.
- **p. 5 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** Current Instances Global Instances Mask Confidence Branch Similarity Matrix Calculation x y z w h l 3D Bounding Boxes Masked Cross-Attention MLP Add & Norm ...
- **p. 7 / 4.4. Explicit Instruction-Guided Reconstruction - extractive PDF cue:** For example, an inStage Method AP AP50 AP25 I Replace with SEEM [59] 3.68 11.00 19.57 Replace with Grounded-SAM [25] 3.06 10.12 18.26 Replace with ...
- **p. 3 / 3. Method - extractive PDF cue:** The perceptual information is progressively constructed into a global map containing multiple candidate instances in the brain.
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** If there are no candidate instances in the image, this module returns "No object".
- **p. 4 / 3.1.1. Incremental Geometric Reconstruction - extractive PDF cue:** To perform global TSDF fusion, only the global TSDF values within the current FBV Bt are updated.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To achieve higher-quality instance fusion, we propose TIFF, a Text-enhanced Instance Fusion module operating within a Fragment bounding volume (FBV), which is learning-based and fuses ...

## Source Evidence Cues

- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** (3) Then, fimg and ˆhseg (text feature prompt) are input into the mask decoder Fdec of the segmentation foundation model to output the binary mask ...
- **p. 7 / 4.5. Runtime Analysis - extractive PDF cue:** To achieve real-time inference, we propose LIRA-Fast.
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** The image features directly use the image embeddings fimg of the segmentation foundation model in the 2D reasoning segmentation module.
- **p. 5 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** Current Instances Global Instances Mask Confidence Branch Similarity Matrix Calculation x y z w h l 3D Bounding Boxes Masked Cross-Attention MLP Add & Norm ...
- **p. 7 / 4.4. Explicit Instruction-Guided Reconstruction - extractive PDF cue:** For example, an inStage Method AP AP50 AP25 I Replace with SEEM [59] 3.68 11.00 19.57 Replace with Grounded-SAM [25] 3.06 10.12 18.26 Replace with ...
- **Detected method headings:** 3. Method (p. 3); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | (3) Then, fimg and ˆhseg (text feature prompt) are input into the mask decoder Fdec of the segmentation foundation model to output ... | p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 7 (4.5. Runtime Analysis) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To achieve real-time inference, we propose LIRA-Fast. | p. 7 (4.5. Runtime Analysis), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The image features directly use the image embeddings fimg of the segmentation foundation model in the 2D reasoning segmentation module. | p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 5 (3.1.2. 2D Reasoning Segmentation within the FBV) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Method - extractive PDF cue:** The perceptual information is progressively constructed into a global map containing multiple candidate instances in the brain.
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** If there are no candidate instances in the image, this module returns "No object".
- **p. 4 / 3.1.1. Incremental Geometric Reconstruction - extractive PDF cue:** To perform global TSDF fusion, only the global TSDF values within the current FBV Bt are updated.
- **p. 7 / 4.5. Runtime Analysis - extractive PDF cue:** Compared with other methods, our LIRA-Fast has advantages in both reasoning reconstruction speed and accuracy.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.1.1. Incremental Geometric Reconstruction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, implicit, complex, instruction, posed, RGB-D, sequences, input, LIRA, first, incrementally, performs, geometric, reconstruction | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, implicit, complex, instruction, posed, RGB-D, sequences, input, LIRA, first | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, major, contributions, follows, introduce, reasoning, reconstruction, task, requires, online | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | perceptual, information, progressively, constructed, global, containing, multiple, candidate, instances, brain | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive PDF cue:** Given an implicit and complex instruction L and posed RGB-D sequences as input, LIRA first incrementally performs geometric reconstruction, and leverages a MLLM to actively ...
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** An image can only provide instance information within a local field of view, and the complex language instruction requires reasoning based on the global map.
- **p. 1 / 1. Introduction - extractive PDF cue:** Online 3D reconstruction guided by language instructions serves as a key task for embodied agents to understand environment and human intentions, enabling many applications such ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Also, we propose a reasoning reconstruction method LIRA, which outperforms existing methods and is capable of running in real time. • To achieve higher instance ...
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive PDF cue:** (3) Then, fimg and ˆhseg (text feature prompt) are input into the mask decoder Fdec of the segmentation foundation model to output the binary mask ...
- **p. 1 / 1. Introduction - extractive PDF cue:** It inputs RGB-D sequences and reconstructs instruction-relevant instances and background environment.
- **p. 2 / 1. Introduction - extractive PDF cue:** However, these methods contain much instruction-irrelevant information, and exhibit limited interaction and reasoning between target instance features and instruction features.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 4, consistent with the evaluation criteria in [3, 41, 58], since keyframes are created at a far lower frequency than the framerate ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | As the process is online, LIRA can halt at any time step between 1 and 4, and identify the target "the smallest ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.5. Runtime Analysis - extractive PDF cue:** To achieve real-time inference, we propose LIRA-Fast.
- **p. 7 / 4.5. Runtime Analysis - extractive PDF cue:** The average inference time for each RGB-D keyframe in the FBV is provided.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, fimg, hseg, text, feature, prompt, input, mask, decoder, Fdec, segmentation, foundation, model, output, binary, mseg, candidate, instance, achieve, real-time.
- **Relevant PDF headings:** 3. Method (p. 3); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To establish a comprehensive evaluation system suitable for the reasoning reconstruction task, a benchmark ReasonRecon is constructed and the data collection pipeline ... | p. 5 (3.4. Benchmark), p. 6 (3.4. Benchmark) |
| Semantic / temporal fusion | Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by can- celing top-down projection. LIRA* represents ... | p. 7 (Figure/Table caption), p. 7 (4.5. Runtime Analysis) |
| Robot query / planning handoff | Table 5. Ablation studies of the three stages of LIRA. struction "Appliances or furniture used to store food" is replaced with "Cabinet, ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation studies of the three stages of LIRA. struction "Appliances or furniture used to store food" is replaced with "Cabinet, Refrigerator". The generated ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Future work will consider further optimization in 3D space.
- **p. 6 / 3.4. Benchmark - extractive PDF cue:** Erroneous projected pixels caused by occlusion are filtered out.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 7 (4.5. Runtime Analysis), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 5 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 7 (4.4. Explicit Instruction-Guided Reconstruction), objective p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 4 (3.1.1. Incremental Geometric Reconstruction), p. 7 (4.5. Runtime Analysis), temporal p. 7 (4.5. Runtime Analysis), p. 1 (1. Introduction), p. 6 (4.1. Implementation Details), p. 3 (3.1.1. Incremental Geometric Reconstruction), p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
