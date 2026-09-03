# Method - 3D-SPATIAL MULTIMODAL MEMORY

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=XYdstv3ySl; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114814. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD), p. 3 (3 METHOD)): We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered features ( ˆR), which can be linked back ...

## Method Body Digest

- **p. 4 / 3 METHOD - extractive body cue:** We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered features ( ˆR), ...
- **p. 4 / 3 METHOD - extractive body cue:** To maintain efficiency while preserving the global representation of foundation model features, we compress the extracted features from foundation models into principal scene components (PSC) ...
- **p. 3 / 3 METHOD - extractive body cue:** The organic integration of Gaussian splatting and Foundation Models infuses scene structure with multi3
- **p. 3 / 3 METHOD - extractive body cue:** Gaussian splatting serves as a framework for constructing scene structure with finest granularity, represented as gaussian primitives, while foundation models provide vast world knowledge spanning ...
- **p. 4 / 3 METHOD - extractive body cue:** We formally define the input of M3 as a video sequence with frames, where each frame corresponds to a view V∗.
- **p. 4 / 3 METHOD - extractive body cue:** Visual granularity (VG) typically represents the clustering pixel scope of an image, a concept introduced in Semantic-SAM [20].
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To evaluate M3, we employ a diverse set of foundation models, including vision-language models, LMM/LLMs, and perception models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, we also design a heuristic algorithm to minimize redundancy in the memory bank by reducing the raw features from the video stream.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Specifically, we propose to store the original high-dimensional 2D feature maps in a memory bank called principal scene components and use the low-dimensional principal queries ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these issues, we present MultiModal Memory (M3), a better integration of Gaussian splatting and multimodal foundation models that efficiently store expressive multimodal memory ...
- **p. 3 / 3 METHOD - extractive body cue:** A real-world visual perception scene (V) consists of both structure (S) and knowledge (I).

## Source Evidence Cues

- **p. 4 / 3 METHOD - extractive body cue:** We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered features ( ˆR), ...
- **p. 4 / 3 METHOD - extractive body cue:** To maintain efficiency while preserving the global representation of foundation model features, we compress the extracted features from foundation models into principal scene components (PSC) ...
- **p. 3 / 3 METHOD - extractive body cue:** The organic integration of Gaussian splatting and Foundation Models infuses scene structure with multi3
- **p. 3 / 3 METHOD - extractive body cue:** Gaussian splatting serves as a framework for constructing scene structure with finest granularity, represented as gaussian primitives, while foundation models provide vast world knowledge spanning ...
- **Detected method headings:** 3 METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered ... | p. 4 (3 METHOD), p. 4 (3 METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To maintain efficiency while preserving the global representation of foundation model features, we compress the extracted features from foundation models into principal ... | p. 4 (3 METHOD), p. 3 (3 METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The organic integration of Gaussian splatting and Foundation Models infuses scene structure with multi3 | p. 3 (3 METHOD), p. 3 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 METHOD - extractive body cue:** We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered features ( ˆR), ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | formally, define, input, video, sequence, frames, where, frame, corresponds, view, Visual, granularity, typically, represents | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | formally, define, input, video, sequence, frames, where, frame, corresponds, view | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Specifically, store, original, high-dimensional, feature, maps, memory, bank, called, principal | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | introduce, optimizable, attribute, queries, Gaussian, primitives, apply, Memory, Attention, Agm | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 METHOD - extractive body cue:** We formally define the input of M3 as a video sequence with frames, where each frame corresponds to a view V∗.
- **p. 4 / 3 METHOD - extractive body cue:** Visual granularity (VG) typically represents the clustering pixel scope of an image, a concept introduced in Semantic-SAM [20].
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To evaluate M3, we employ a diverse set of foundation models, including vision-language models, LMM/LLMs, and perception models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, we also design a heuristic algorithm to minimize redundancy in the memory bank by reducing the raw features from the video stream.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We formally define the input of M3 as a video sequence with frames, where each frame corresponds to a view V∗. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For temporal aspects, previous works have focused on using memory bank embeddings to store information across frames. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | For temporal aspects, previous works have focused on using memory bank embeddings to store information across frames. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Previous methods [26; 51] compute the patch-wise distance loss on the rendered features, this not only has a high volume of GPU memory consumption that ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 1, where the average training time and the auxiliary low-level metrics are reported.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** While maintaining a very efficient training time, our method has independent results from different foundation models.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, optimizable, attribute, queries, Gaussian, primitives, apply, Memory, Attention, Agm, mechanism, produce, final, rendered, features, linked, back, various, heads, foundation.
- **Relevant PDF headings:** 3 METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To support extensive quantitative and qualitative evaluation, we perform experiments using several existing scene datasets [3; 18; 10] and collected a custom ... | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Semantic / temporal fusion | 4.2 QUANTITATIVE RESULTS Baseline Implementation For quantitative experiments, we compare M3 with two recent distillation-based feature GS methods [26; 51]. | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Robot query / planning handoff | Our method, M3, outperforms F-Splat while reducing significantly compute than F-3DGS. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 3 shows the ablation of the number of foundation models involved in M3.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Cosine↓ L2↓ Cosine↓ L2↓ Cosine↓ L2↓ Cosine↓ L2↓ Cosine↓ L2↓ Cosine↓ L2↓ Tabletop +CLIP 21.91 ∼6 0.3100 0.2956 - - - - - - - ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Given a video sequence, we utilize foundation models (F) to extract raw features (R). These features are reduced using Algorithm 1, producing principal ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth feature extraction procedure, where duplication was performed ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD), p. 3 (3 METHOD), objective p. 4 (3 METHOD), temporal p. 4 (3 METHOD), p. 3 (2 RELATED WORK), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 6 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
