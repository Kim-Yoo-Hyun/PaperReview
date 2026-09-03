# Method - Segment Any 3D Object with Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ENv1CeTwxc; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114011. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD)): 4, we first extract all the noun phrases ei for each mask caption ci and obtain the text feature of each noun phrase from CLIP text encoder T as below: ...

## Method Body Digest

- **p. 6 / 3 METHOD - extractive body cue:** 4, we first extract all the noun phrases ei for each mask caption ci and obtain the text feature of each noun phrase from CLIP ...
- **p. 5 / 3 METHOD - extractive body cue:** To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework.
- **p. 6 / 3 METHOD - extractive body cue:** To this end, we propose a soft matching to get mask-entity association by multimodal attention.
- **p. 7 / 3 METHOD - extractive body cue:** For benchmark evaluation, we use CLIP textual features of all category names as the classifier.
- **p. 7 / 3 METHOD - extractive body cue:** For responding to other language instructions, we use the CLIP textual feature of corresponding language instruction as binary classifier.
- **p. 4 / 3 METHOD - extractive body cue:** Our SOLE leverages the mask prediction paradigm with transformer-based architecture, where the model is only trained with masks without ground truth labels to achieve generalizable ...
- **p. 4 / 3 METHOD - extractive body cue:** To realize open-vocabulary instance segmentation with free-form language instructions, we improve the transformer-based instance segmentation model with multimodal information: point-wise CLIP features in the backbone ...
- **p. 7 / 3 METHOD - extractive body cue:** The overall training loss is the combination of mask loss and semantic loss:

## Design Rationale

- **p. 5 / 3 METHOD - extractive body cue:** To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We propose a visual-language learning framework for OV-3DIS, SOLE.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** A multimodal fusion network is designed for SOLE, which can directly predict semantic-related masks from 3D point clouds with multimodal information, leading to high-quality and ...

## Source Evidence Cues

- **p. 6 / 3 METHOD - extractive body cue:** 4, we first extract all the noun phrases ei for each mask caption ci and obtain the text feature of each noun phrase from CLIP ...
- **p. 5 / 3 METHOD - extractive body cue:** To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework.
- **p. 6 / 3 METHOD - extractive body cue:** To this end, we propose a soft matching to get mask-entity association by multimodal attention.
- **p. 7 / 3 METHOD - extractive body cue:** For benchmark evaluation, we use CLIP textual features of all category names as the classifier.
- **p. 7 / 3 METHOD - extractive body cue:** For responding to other language instructions, we use the CLIP textual feature of corresponding language instruction as binary classifier.
- **p. 4 / 3 METHOD - extractive body cue:** Our SOLE leverages the mask prediction paradigm with transformer-based architecture, where the model is only trained with masks without ground truth labels to achieve generalizable ...
- **p. 4 / 3 METHOD - extractive body cue:** To realize open-vocabulary instance segmentation with free-form language instructions, we improve the transformer-based instance segmentation model with multimodal information: point-wise CLIP features in the backbone ...
- **Detected method headings:** 3 METHOD (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 4, we first extract all the noun phrases ei for each mask caption ci and obtain the text feature of each noun ... | p. 6 (3 METHOD), p. 5 (3 METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework. | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To this end, we propose a soft matching to get mask-entity association by multimodal attention. | p. 6 (3 METHOD), p. 7 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 METHOD - extractive body cue:** The overall training loss is the combination of mask loss and semantic loss:
- **p. 7 / 3 METHOD - extractive body cue:** The semantic multimodal association loss Lj MMA for j-th ground truth mask is:
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 7 (3 METHOD), p. 7 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goal, open-vocabulary, instance, segmentation, OV-3DIS, free-form, language, instructions, defined, follows, Given, point, cloud, corresponding | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | goal, open-vocabulary, instance, segmentation, OV-3DIS, free-form, language, instructions, defined, follows | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | circumvent, issue, introduce, Cross, Modality, Decoder, CMD, incorporate, textual, information | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | overall, training, loss, combination, mask, semantic, multimodal, association, MMA, j-th | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 METHOD - extractive body cue:** The goal of open-vocabulary 3D instance segmentation (OV-3DIS) with free-form language instructions is defined as follows: Given a 3D point cloud P ∈RM×C, the corresponding ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The associations improve the mask quality and the response ability to language instructions. • SOLE achieves state-of-the-art results on ScanNetv2, Scannet200 and Replica benchmarks, and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The 3D segmentation network is required to be aligned with language instructions to directly segment and classify instances from point clouds.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To realize generalizable open-set 3D instance segmentation, our SOLE requires two main attributes: generating and classifying 3D masks directly from 3D point clouds, and responsive ...
- **p. 4 / 3 METHOD - extractive body cue:** To realize open-vocabulary instance segmentation with free-form language instructions, we improve the transformer-based instance segmentation model with multimodal information: point-wise CLIP features in the backbone ...
- **p. 5 / 3 METHOD - extractive body cue:** The three multimodal associations are used for supervising SOLE to acquire the ability to segment 3D objects with free-form language instructions. to train SOLE.
- **p. 5 / 3 METHOD - extractive body cue:** 3.2 CROSS MODALITY DECODER (CMD) Projected 2D CLIP features provide generalizable visual information but the language information is not explicitly integrated, limiting the responsive ability ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We build our framework on the transformer-based 3D instance segmentation model Mask3D (Schult et al., 2022), which treats the instance segmentation task ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Equipped with the multimodal framework and associations, our SOLE can effectively segment instances given various language prompts. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Larger voxel size can save the memory requirements and speed up the model with the loss of precision. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Our model is trained for 600 epochs with AdamW (Loshchilov & Hutter, 2017) optimizer. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 METHOD - extractive body cue:** Our SOLE leverages the mask prediction paradigm with transformer-based architecture, where the model is only trained with masks without ground truth labels to achieve generalizable ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Our model is trained for 600 epochs with AdamW (Loshchilov & Hutter, 2017) optimizer.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, extract, noun, phrases, mask, caption, obtain, text, feature, phrase, CLIP, encoder, below, dots, N_e, quad, mathbf, mathcal, mathbb, times.
- **Relevant PDF headings:** 3 METHOD (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Therefore, despite slightly impairing the performance on benchmark, mask-visual association and mask-caption association are crucial to recognizing free-form language instructions, benefiting the ... | p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Semantic / temporal fusion | Table 2: The comparison of closed-set 3D instance segmentation setting on ScanNet200. SOLE is compared with mask training methods on the overall ... | p. 8 (Figure/Table caption), p. 9 (4 EXPERIMENTS) |
| Robot query / planning handoff | SOLE outperforms all the OV-3DIS methods and achieves competitive results with the fully-supervised model. | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Finally, we provide two variants of SOLE to further verify our effectiveness.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Furthermore, we verify that the effectiveness of our framework is not limited to the caption model and NLP tools by conducting experiments without any additional ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 5, we conduct component analysis on multimodal fusion network, validating the effectiveness of backbone feature ensemble and Cross-Modality Decoder (CMD).
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 6: K-means clustering of different backbone features. Different colors denote different clusters. OCRand and VoteRand where training is not required, the other four baseline ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** We analyze the components of multimodal associations (f MVA, f MCA, and f MEA) in Tab.
- **p. 19 / Figure/Table caption - extractive body cue:** Table 8: Analysis on classification probability ensemble. Results are reported on the ScanNetv2 (Dai et al., 2017) dataset in 2cm voxel size. Component AP AP50 ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Left (a) : Previous works train class-agnostic mask proposal module with only using mask annotations. In the inference time, generated 3D masks are ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD), objective p. 7 (3 METHOD), p. 7 (3 METHOD), temporal p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 18 (A IMPLEMENTATION DETAILS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
