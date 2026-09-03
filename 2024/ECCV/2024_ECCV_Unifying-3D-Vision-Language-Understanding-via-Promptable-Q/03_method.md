# Method - Unifying 3D Vision-Language Understanding via Promptable Queries

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6043_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06043.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 8 (3 Method)): Within the decoder layer l, the instance queries Ql retrieve task-relevant information by first attending to the scene features {V, I, P} in parallel and then the task prompt t, ...

## Method Body Digest

- **p. 7 / 3 Method - extractive body cue:** Within the decoder layer l, the instance queries Ql retrieve task-relevant information by first attending to the scene features {V, I, P} in parallel and ...
- **p. 6 / 3 Method - extractive body cue:** 3: The model architecture of PQ3D, which consists of Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning modules.
- **p. 8 / 3 Method - extractive body cue:** To support flexible inference when only some representations are available, we randomly drop out some scene features with rate 0.6 in masked-attention computation during training.
- **p. 7 / 3 Method - extractive body cue:** Then, we encode these scene representations by the corresponding encoders and pool the features to the segments in total of M.
- **p. 6 / 3 Method - extractive body cue:** In scene encoding, point clouds, voxel grids, and multi-view images of a scene are first encoded by corresponding encoders and then aligned into a shared ...
- **p. 8 / 3 Method - extractive body cue:** During training, we follow [54, 70] to apply Hungarian Matching between queries and ground-truth objects, then calculate the mask loss: \ma t hcal {L} _ ...
- **p. 5 / 3 Method - extractive body cue:** Next, we will explain the details of each module.
- **p. 8 / 3 Method - extractive body cue:** During training, if text responses are provided as supervision for dense caption and QA task, we calculate the cross-entropy loss as the generation loss Lgen.

## Design Rationale

- **p. 5 / 3 Method - extractive body cue:** In this section, we present PQ3D, which consists of three main modules: Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning, as depicted in ...
- **p. 7 / 3 Method - extractive body cue:** 3.3 Prompt-guided Query Learning We propose a novel Transformer-like decoder to instruct the instance queries to assimilate scene and prompt information.
- **p. 6 / 3 Method - extractive body cue:** With such unification, we do not distinguish different prompt formats anymore and this design enables the model to transfer knowledge between different prompts.

## Source Evidence Cues

- **p. 7 / 3 Method - extractive body cue:** Within the decoder layer l, the instance queries Ql retrieve task-relevant information by first attending to the scene features {V, I, P} in parallel and ...
- **p. 6 / 3 Method - extractive body cue:** 3: The model architecture of PQ3D, which consists of Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning modules.
- **p. 8 / 3 Method - extractive body cue:** To support flexible inference when only some representations are available, we randomly drop out some scene features with rate 0.6 in masked-attention computation during training.
- **p. 7 / 3 Method - extractive body cue:** Then, we encode these scene representations by the corresponding encoders and pool the features to the segments in total of M.
- **p. 6 / 3 Method - extractive body cue:** In scene encoding, point clouds, voxel grids, and multi-view images of a scene are first encoded by corresponding encoders and then aligned into a shared ...
- **p. 8 / 3 Method - extractive body cue:** During training, we follow [54, 70] to apply Hungarian Matching between queries and ground-truth objects, then calculate the mask loss: \ma t hcal {L} _ ...
- **p. 5 / 3 Method - extractive body cue:** Next, we will explain the details of each module.
- **Detected method headings:** 3 Method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Within the decoder layer l, the instance queries Ql retrieve task-relevant information by first attending to the scene features {V, I, P} ... | p. 7 (3 Method), p. 6 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | 3: The model architecture of PQ3D, which consists of Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning modules. | p. 6 (3 Method), p. 8 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To support flexible inference when only some representations are available, we randomly drop out some scene features with rate 0.6 in masked-attention ... | p. 8 (3 Method), p. 7 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 3 Method - extractive body cue:** During training, if text responses are provided as supervision for dense caption and QA task, we calculate the cross-entropy loss as the generation loss Lgen.
- **p. 8 / 3 Method - extractive body cue:** Formally, we have: p_ \ mathrm {grd} = \sigma (f_g(\mathbf {Q})) (6) During training, if grounding labels are provided as supervision, we calculate a binary ...
- **p. 6 / 3 Method - extractive body cue:** 3.2 3D Scene Encoding There are three widely used representations for 3D scenes: point clouds, voxel grids, and multi-view images, which have their unique advantages ...
- **p. 6 / 3 Method - extractive body cue:** The prompt-guided query learning module takes in zero-initialized instance queries and progressively retrieves task-relevant information from aligned scene features under the guidance of task prompts.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Finally, updated, instance, query, three, output, heads, predict, mask, task-relevance, score, sentence, model, allows | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Finally, updated, instance, query, three, output, heads, predict, mask, task-relevance | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | section, present, PQ3D, consists, three, main, modules, Task, Prompt, Encoding | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | During, training, text, responses, provided, supervision, dense, caption, task, calculate | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3 Method - extractive body cue:** Finally, each updated instance query is fed into three output heads to predict an instance mask, a task-relevance score, and a sentence. model [49], which ...
- **p. 8 / 3 Method - extractive body cue:** Generation head We choose the decoder of a pre-trained T5-small [12,50] as the generation head to generate a text response, using all instance queries as ...
- **p. 8 / 3 Method - extractive body cue:** 3.4 Output Heads and Losses We adopt the following three output heads to support a variety of 3D-VL tasks: Mask head For each instance query, ...
- **p. 6 / 3 Method - extractive body cue:** In scene encoding, point clouds, voxel grids, and multi-view images of a scene are first encoded by corresponding encoders and then aligned into a shared ...
- **p. 1 / 1 Introduction - extractive body cue:** This step is crucial for embodied agents to understand and execute human instructions in real-world scenarios [4,51].
- **p. 7 / 3 Method - extractive body cue:** Point Cloud To process the point cloud of a 3D scene, we first partition the full point cloud into the pre-generated segments.
- **p. 1 / 1 Introduction - extractive body cue:** In recent years, numerous tasks and datasets for benchmarking 3D scene understanding with languages have been proposed, including 3D semantic segmentation [52], 3D vision-language ⋆Work ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This step is crucial for embodied agents to understand and execute human instructions in real-world scenarios [4,51]. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 2.3 Promptable Segmentation The concept of promptable segmentation, as presented in the SAM framework [34], centers around the utilization of prompts to ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 3 Method - extractive body cue:** To support flexible inference when only some representations are available, we randomly drop out some scene features with rate 0.6 in masked-attention computation during training.
- **p. 8 / 3 Method - extractive body cue:** During training, we follow [54, 70] to apply Hungarian Matching between queries and ground-truth objects, then calculate the mask loss: \ma t hcal {L} _ ...
- **p. 5 / 3 Method - extractive body cue:** We encode the textual and visual prompts by the pre-trained CLIP

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Within, decoder, layer, instance, queries, retrieve, task-relevant, information, first, attending, scene, features, parallel, then, task, prompt, followed, spatial, self-attention, model.
- **Relevant PDF headings:** 3 Method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To further demonstrate the capability of PQ3D, we also transfer it to an embodied agent for object navigation using the ObjNav task ... | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Semantic / temporal fusion | On the ScanRefer, Nr3D, and Sr3D benchmarks, our model outperforms SOTA by 5.4%, 2.3%, and 3.3%, respectively. | p. 10 (4 Experiments), p. 4 (Figure/Table caption) |
| Robot query / planning handoff | Furthermore, on the Multi3DRefer benchmark, our model outperforms others in the ST (single target) and MT (multiple targets) categories and achieves the ... | p. 10 (4 Experiments), p. 11 (4 Experiments) |

## Failure and Ablation Link

- **p. 12 / Figure/Table caption - extractive body cue:** Table 7: Results on ObjNav from CortexBench [42]. Note we reproduce the result of "VC-1 (ViT-B)" ourselves due to the slight mismatch we have found. ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 8: Ablation study of scene features. Each entry denotes PQ3D "trained with specific scene features" and "trained with all features but some removed during ...
- **p. 12 / 4 Experiments - extractive body cue:** 4: Ablation study of query decoder depth.
- **p. 13 / 4 Experiments - extractive body cue:** Voxel Point Image Refer QA Caption ✓ 46.1 / 47.1 43.7 / 44.2 67.8 / 68.1 ✓ ✓ 49.2 / 49.4 45.4 / 45.8 74.6 ...
- **p. 14 / 4 Experiments - extractive body cue:** Vacuum or sweep the floor to remove any dirt or debris.
- **p. 10 / 4 Experiments - extractive body cue:** However, our model trained only on the Multi3DRefer dataset "PQ3D (sg.)" exhibits better performance in the ZT and MT metric, but falls short of the ...
- **p. 11 / 4 Experiments - extractive body cue:** As our model utilizes the CLIP text encoder, it may face limitations in understanding long sentences.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 8 (3 Method), objective p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method), p. 6 (3 Method), temporal p. 1 (1 Introduction), p. 5 (2 Related Work), p. 5 (2 Related Work), p. 14 (4. Adjust the temperature or settings of the heater).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
