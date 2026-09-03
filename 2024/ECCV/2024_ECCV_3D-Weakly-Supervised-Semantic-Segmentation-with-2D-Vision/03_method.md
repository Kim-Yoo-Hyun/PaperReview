# Method - 3D Weakly Supervised Semantic Segmentation with 2D Vision-Language Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9223_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Body text (section not recovered)), p. 2 (X. Xu et al), p. 4 (X. Xu et al), p. 8 (X. Xu et al), p. 3 (X. Xu et al), p. 6 (X. Xu et al)): Moreover, we introduce the Embeddings Specialization Stage to purify the feature representation with the help of a given scene-level label, specifying a better feature supervised by the corresponding text embedding.

## Method Body Digest

- **p. 1 / Body text (section not recovered) - extractive body cue:** Moreover, we introduce the Embeddings Specialization Stage to purify the feature representation with the help of a given scene-level label, specifying a better feature supervised ...
- **p. 2 / X. Xu et al - extractive body cue:** Point clouds are first processed by several Multi-Layer Perception (MLP) layers and thus get a point cloud feature map, and then this point cloud feature ...
- **p. 4 / X. Xu et al - extractive body cue:** In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D ...
- **p. 8 / X. Xu et al - extractive body cue:** Finally, we use the pseudo labels Y to supervise the model, and the green dashed lines denote back-propagation of the loss La.
- **p. 3 / X. Xu et al - extractive body cue:** We first process these multi-view images using the image encoder of the pretrained off-the-shelf 2D OVSS model such as Openseg [12] to get the 2D ...
- **p. 6 / X. Xu et al - extractive body cue:** 2, we first implement dense 2D embeddings extraction for each RGB image via the frozen visual encoder of Openseg [12], and back-project them onto the ...
- **p. 8 / X. Xu et al - extractive body cue:** For (a), we first utilize the text encoder εtext of Openseg to obtain embeddings of the category labels FC, which are frozen during the training ...
- **p. 8 / X. Xu et al - extractive body cue:** The red dashed lines denote back-propagation of the loss Ls. a classification cross-entropy loss La is introduced to supervise the procedure.

## Design Rationale

- **p. 4 / X. Xu et al - extractive body cue:** In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Moreover, we introduce the Embeddings Specialization Stage to purify the feature representation with the help of a given scene-level label, specifying a better feature supervised ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Specifically, our method exploits the superior generalization ability of the 2D visionlanguage models and proposes the Embeddings Soft-Guidance Stage to utilize it to implicitly align ...

## Source Evidence Cues

- **p. 1 / Body text (section not recovered) - extractive body cue:** Moreover, we introduce the Embeddings Specialization Stage to purify the feature representation with the help of a given scene-level label, specifying a better feature supervised ...
- **p. 2 / X. Xu et al - extractive body cue:** Point clouds are first processed by several Multi-Layer Perception (MLP) layers and thus get a point cloud feature map, and then this point cloud feature ...
- **p. 4 / X. Xu et al - extractive body cue:** In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D ...
- **p. 8 / X. Xu et al - extractive body cue:** Finally, we use the pseudo labels Y to supervise the model, and the green dashed lines denote back-propagation of the loss La.
- **p. 3 / X. Xu et al - extractive body cue:** We first process these multi-view images using the image encoder of the pretrained off-the-shelf 2D OVSS model such as Openseg [12] to get the 2D ...
- **p. 6 / X. Xu et al - extractive body cue:** 2, we first implement dense 2D embeddings extraction for each RGB image via the frozen visual encoder of Openseg [12], and back-project them onto the ...
- **p. 8 / X. Xu et al - extractive body cue:** For (a), we first utilize the text encoder εtext of Openseg to obtain embeddings of the category labels FC, which are frozen during the training ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Moreover, we introduce the Embeddings Specialization Stage to purify the feature representation with the help of a given scene-level label, specifying a ... | p. 1 (Body text (section not recovered)), p. 2 (X. Xu et al) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Point clouds are first processed by several Multi-Layer Perception (MLP) layers and thus get a point cloud feature map, and then this ... | p. 2 (X. Xu et al), p. 4 (X. Xu et al) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, ... | p. 4 (X. Xu et al), p. 8 (X. Xu et al) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / X. Xu et al - extractive body cue:** The red dashed lines denote back-propagation of the loss Ls. a classification cross-entropy loss La is introduced to supervise the procedure.
- **p. 8 / X. Xu et al - extractive body cue:** The cosine similarity loss Ls will be integrated to train the model.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 8 (X. Xu et al), p. 8 (X. Xu et al).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Moreover, Embeddings, Specialization, Stage, make, embedding, space, more, robust, pseudo, label, filtering, indoor, point | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Moreover, Embeddings, Specialization, Stage, make, embedding, space, more, robust, pseudo | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, main, contributions, follows, weakly, supervised, DSS-VLG, WSSS, takes, images | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | dashed, lines, denote, back-propagation, loss, classification, cross-entropy, introduced, supervise, procedure | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / X. Xu et al - extractive body cue:** Moreover, we propose Embeddings Specialization Stage to make the embedding space to be more robust based on the pseudo label filtering with indoor point cloud ...
- **p. 3 / X. Xu et al - extractive body cue:** Specifically, for the input 3D point cloud, the dataset also provides a set of multi-view images corresponding to it.
- **p. 6 / X. Xu et al - extractive body cue:** Given an input point cloud with multi-view images as shown in Fig.
- **p. 6 / X. Xu et al - extractive body cue:** The inputs of 3DSS-VLG comprise a scene with 3D point cloud, scene-level labels and the associated multi-view RGB images
- **p. 4 / X. Xu et al - extractive body cue:** In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D ...
- **p. 2 / X. Xu et al - extractive body cue:** Given the simple GAP connectivity structure, these methods can easily identify the importance of each point by projecting back the output classification weight onto the ...
- **p. 7 / X. Xu et al - extractive body cue:** After ranking the filtered classification logits Lf, we can get the more precise pseudo label Y ∈RN of the input point cloud.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Finally, ablation studies are provided to further demonstrate the necessity and effectiveness of each component of our framework. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We also evaluate our 3DSS-VLG on the ScanNet online test set and the validation set and presented the performance results of 3DSS-VLG ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We reduce the learning rate by a multiplying factor of 0.7 every 20 epochs for a total of 80 epochs. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / X. Xu et al - extractive body cue:** Point clouds are first processed by several Multi-Layer Perception (MLP) layers and thus get a point cloud feature map, and then this point cloud feature ...
- **p. 4 / X. Xu et al - extractive body cue:** In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D ...
- **p. 3 / X. Xu et al - extractive body cue:** We first process these multi-view images using the image encoder of the pretrained off-the-shelf 2D OVSS model such as Openseg [12] to get the 2D ...
- **p. 8 / X. Xu et al - extractive body cue:** For (a), we first utilize the text encoder εtext of Openseg to obtain embeddings of the category labels FC, which are frozen during the training ...
- **p. 3 / X. Xu et al - extractive body cue:** We first process these multi-view images using the image encoder of the pretrained off-the-shelf 2D OVSS model such as Openseg [12] to get the 2D ...
- **p. 7 / X. Xu et al - extractive body cue:** Similarly, we also freeze the text encoder and directly load the pretrained Openseg parameters.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Moreover, introduce, Embeddings, Specialization, Stage, purify, feature, representation, help, given, scene-level, label, specifying, better, supervised, corresponding, text, embedding, Point, clouds.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We adopt the default train-val split setting, where there are 1201 training scenes and 312 validation scenes. | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Semantic / temporal fusion | The competing methods are then presented and compared. | p. 9 (4 Experiments), p. 14 (Figure/Table caption) |
| Robot query / planning handoff | Table 1: Performance comparison on the S3DIS dataset. "Sup." indicates the type of supervision. "100%" represents full annotation. "scene." denotes scene-level annotation. | p. 10 (Figure/Table caption), p. 12 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive body cue:** Finally, ablation studies are provided to further demonstrate the necessity and effectiveness of each component of our framework.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Ablation studies of the 3DSS-VLG components on S3DIS dataset. ESGS Filtering ESS mIoU (a) 37.7 (b) ✓ 38.2 (c)
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: The proposed pseudo label generation procedure. We first leverage the text encoder εtext of Openseg to get embeddings of the full category labels ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Body text (section not recovered)), p. 2 (X. Xu et al), p. 4 (X. Xu et al), p. 8 (X. Xu et al), p. 3 (X. Xu et al), p. 6 (X. Xu et al), objective p. 8 (X. Xu et al), p. 8 (X. Xu et al), temporal p. 9 (4 Experiments), p. 10 (X. Xu et al), p. 12 (X. Xu et al), p. 13 (X. Xu et al), p. 14 (X. Xu et al).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
