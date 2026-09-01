# Method - VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/xu25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/xu25c/xu25c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3 Methodology), p. 8 (3 Methodology), p. 3 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology)): Without model training, VLM-Grounder's overall performance also competes with supervised learning methods like InstanceRefer (38.8%) and 3DVG-Transformer (40.8%).

## Method Body Digest

- **p. 7 / 3 Methodology - extractive PDF cue:** Without model training, VLM-Grounder's overall performance also competes with supervised learning methods like InstanceRefer (38.8%) and 3DVG-Transformer (40.8%).
- **p. 8 / 3 Methodology - extractive PDF cue:** VLM-Grounder has several appealing properties: it leverages foundation models from the language and 2D domains without training, and offers a more transparent and explainable grounding ...
- **p. 3 / 3 Methodology - extractive PDF cue:** 3.1), and detail the motivations and specifics of three key modules: dynamic stitching (Sec.
- **p. 3 / 3 Methodology - extractive PDF cue:** VLM-Grounder is an agent framework where the VLM is equipped with various tools and modules to enable its grounding capability.
- **p. 4 / 3 Methodology - extractive PDF cue:** 3) More images increase inference costs, including token usage, latency, and timeout risk.
- **p. 4 / 3 Methodology - extractive PDF cue:** The target image and bounding box are input into the Segment Anything Model (SAM) [52] to obtain a fine-grained mask.
- **p. 5 / 3 Methodology - extractive PDF cue:** In scenes with many objects of identical appearance, the image-matching module may produce mismatched results.
- **p. 4 / 3 Methodology - extractive PDF cue:** To maximize performance, we propose a dynamic stitching strategy that dynamically utilizes the top three layouts.

## Design Rationale

- **p. 1 / 1 Introduction - extractive PDF cue:** While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like "find ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts identified by the benchmark to stitch images, enhancing VLM's performance.
- **p. 3 / 3 Methodology - extractive PDF cue:** In this section, we present the overall framework of VLM-Grounder (Sec.

## Source Evidence Cues

- **p. 7 / 3 Methodology - extractive PDF cue:** Without model training, VLM-Grounder's overall performance also competes with supervised learning methods like InstanceRefer (38.8%) and 3DVG-Transformer (40.8%).
- **p. 8 / 3 Methodology - extractive PDF cue:** VLM-Grounder has several appealing properties: it leverages foundation models from the language and 2D domains without training, and offers a more transparent and explainable grounding ...
- **p. 3 / 3 Methodology - extractive PDF cue:** 3.1), and detail the motivations and specifics of three key modules: dynamic stitching (Sec.
- **p. 3 / 3 Methodology - extractive PDF cue:** VLM-Grounder is an agent framework where the VLM is equipped with various tools and modules to enable its grounding capability.
- **p. 4 / 3 Methodology - extractive PDF cue:** 3) More images increase inference costs, including token usage, latency, and timeout risk.
- **p. 4 / 3 Methodology - extractive PDF cue:** The target image and bounding box are input into the Segment Anything Model (SAM) [52] to obtain a fine-grained mask.
- **p. 5 / 3 Methodology - extractive PDF cue:** In scenes with many objects of identical appearance, the image-matching module may produce mismatched results.
- **Detected method headings:** 3 Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Without model training, VLM-Grounder's overall performance also competes with supervised learning methods like InstanceRefer (38.8%) and 3DVG-Transformer (40.8%). | p. 7 (3 Methodology), p. 8 (3 Methodology) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | VLM-Grounder has several appealing properties: it leverages foundation models from the language and 2D domains without training, and offers a more transparent ... | p. 8 (3 Methodology), p. 3 (3 Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 3.1), and detail the motivations and specifics of three key modules: dynamic stitching (Sec. | p. 3 (3 Methodology), p. 3 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Methodology - extractive PDF cue:** 3) More images increase inference costs, including token usage, latency, and timeout risk.
- **p. 4 / 3 Methodology - extractive PDF cue:** To maximize performance, we propose a dynamic stitching strategy that dynamically utilizes the top three layouts.
- **p. 5 / 3 Methodology - extractive PDF cue:** To reduce costs, we randomly select 250 validation samples from each dataset for testing.
- **p. 7 / 3 Methodology - extractive PDF cue:** This benchmark allows us to assess the extent of information loss caused by the stitching strategy through retrieval accuracy.
- **p. 8 / 3 Methodology - extractive PDF cue:** 4.3, increasing the number of images leads to higher inference costs and a greater risk of timeouts.
- **p. 6 / 3 Methodology - extractive PDF cue:** This provides an important advantage as it serves as a strong prior.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3 Methodology), p. 4 (3 Methodology), p. 7 (3 Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Inputting, many, images, quickly, consumes, VLM, context, length, limiting, output, content, potentially, affecting, performance | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Inputting, many, images, quickly, consumes, VLM, context, length, limiting, output | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | While, methods, achieve, strong, performance, they, only, objectcentric, information, often | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | More, images, increase, inference, costs, including, token, usage, latency, timeout | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Methodology - extractive PDF cue:** 2) Inputting many images quickly consumes the VLM's context length, limiting output content and potentially affecting performance.
- **p. 4 / 3 Methodology - extractive PDF cue:** The target image and bounding box are input into the Segment Anything Model (SAM) [52] to obtain a fine-grained mask.
- **p. 7 / 3 Methodology - extractive PDF cue:** Additionally, we measure the retrieval time for different numbers of input images.
- **p. 7 / 3 Methodology - extractive PDF cue:** 4.3 Visual-Retrieval Benchmark Stitching multiple images into one can reduce the number of images input to a VLM, but its impact on the VLM's visual ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Inputting image sequences to the VLM can exceed the VLM's maximum image limit, overly consume the VLM's context length, and lead to degraded performance and ...
- **p. 5 / 3 Methodology - extractive PDF cue:** Details of different feedbacks are provided in the supplementary material.
- **p. 5 / 3 Methodology - extractive PDF cue:** VLM-Grounder does not need such priors for input, so we match our predicted box to the ground truth box with the closest center and use ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For our experiments, we sample one frame from every 20 frames of the original ScanNet image sequences. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Inputting image sequences to the VLM can exceed the VLM's maximum image limit, overly consume the VLM's context length, and lead to ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For our experiments, we sample one frame from every 20 frames of the original ScanNet image sequences. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3 Methodology - extractive PDF cue:** Without model training, VLM-Grounder's overall performance also competes with supervised learning methods like InstanceRefer (38.8%) and 3DVG-Transformer (40.8%).
- **p. 8 / 3 Methodology - extractive PDF cue:** VLM-Grounder has several appealing properties: it leverages foundation models from the language and 2D domains without training, and offers a more transparent and explainable grounding ...
- **p. 4 / 3 Methodology - extractive PDF cue:** 3) More images increase inference costs, including token usage, latency, and timeout risk.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Without, model, training, VLM-Grounder, overall, performance, competes, supervised, learning, methods, like, InstanceRefer, DVG-Transformer, several, appealing, properties, leverages, foundation, models, language.
- **Relevant PDF headings:** 3 Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We introduced a novel Visual-Retrieval benchmark to evaluate the impact of stitching operations on VLM's visual understanding. | p. 8 (3 Methodology), p. 8 (3 Methodology) |
| Semantic / temporal fusion | Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves ... | p. 6 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Robot query / planning handoff | Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves ... | p. 6 (Figure/Table caption), p. 8 (3 Methodology) |

## Failure and Ablation Link

- **p. 8 / 3 Methodology - extractive PDF cue:** Without stitching, the system often encounters timeouts and fails to complete the task, underscoring the necessity of an effective stitching strategy.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable to ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: 3D visual grounding results on Nr3D. VLM-Grounder surpasses the previous SOTA zero- shot method without requiring access to point clouds or ground-truth bounding ...
- **p. 8 / 3 Methodology - extractive PDF cue:** Ops 45.2 +Point Filtering 48.4 +Multi-View 51.6 4.4 Ablation Studies Stitching strategies.
- **p. 20 / Figure/Table caption - extractive PDF cue:** Figure 5: Failure cases of the VLM grounding module. 20
- **p. 21 / Figure/Table caption - extractive PDF cue:** Figure 8: A failure case of the projection module. 21
- **p. 6 / 3 Methodology - extractive PDF cue:** Although our multi-view ensemble projection module helps mitigate this issue, it cannot entirely eliminate it.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3 Methodology), p. 8 (3 Methodology), p. 3 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology), objective p. 4 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 7 (3 Methodology), p. 8 (3 Methodology), p. 6 (3 Methodology), temporal p. 5 (3 Methodology), p. 1 (1 Introduction), p. 3 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
