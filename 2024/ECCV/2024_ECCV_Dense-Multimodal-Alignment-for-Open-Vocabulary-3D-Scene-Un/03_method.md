# Method - Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6612_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 4 (3 Method), p. 8 (3 Method), p. 6 (3 Method)): Firstly, we use the image tagging foundation model such as RAM [23] to extract all possible categories from an image, and utilize category names and short descriptions derived from the ...

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** Firstly, we use the image tagging foundation model such as RAM [23] to extract all possible categories from an image, and utilize category names and ...
- **p. 7 / 3 Method - extractive body cue:** On one hand, we use the frozen CLIP visual encoder to ensure the intactness of image-text alignment, obtaining CLIP features f2D clip.
- **p. 8 / 3 Method - extractive body cue:** Firstly, we extract 3D features for the point cloud by utilizing a 3D network, denoted as ε3D.
- **p. 4 / 3 Method - extractive body cue:** 1, we propose a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding, where we construct dense correspondences across 2D image pixels, 3D points ...
- **p. 8 / 3 Method - extractive body cue:** We use the text-to-3D label map M 3D as the pseudo label to facilitate the alignment of point and text features.
- **p. 6 / 3 Method - extractive body cue:** Finally, we generate the text embeddings fT tag and fT llm using CLIP text encoder based on the generated tags Ttag and scene descriptions Tllm, ...
- **p. 6 / 3 Method - extractive body cue:** Firstly, they are fine-tuned on in-vocabulary datasets, which leads to a misalignment between image and text features and consequently results in poor performance on open-vocabulary ...
- **p. 9 / 3 Method - extractive body cue:** For 3D-2D pairs, we follow the previous work [42] to fuse pixel embeddings across K different views, represented as [f2D 1 , · · · ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In order to leverage the synergistic benefits of multiple modalities for dense prediction tasks, we propose a dense multimodal alignment (DMA) strategy to co-embed 3D ...
- **p. 4 / 3 Method - extractive body cue:** 1, we propose a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding, where we construct dense correspondences across 2D image pixels, 3D points ...
- **p. 9 / 3 Method - extractive body cue:** By densely aligning these modalities in a shared space, our method can maximize the synergistic benefits among them and achieve outstanding segmentation performance without compromising ...

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** Firstly, we use the image tagging foundation model such as RAM [23] to extract all possible categories from an image, and utilize category names and ...
- **p. 7 / 3 Method - extractive body cue:** On one hand, we use the frozen CLIP visual encoder to ensure the intactness of image-text alignment, obtaining CLIP features f2D clip.
- **p. 8 / 3 Method - extractive body cue:** Firstly, we extract 3D features for the point cloud by utilizing a 3D network, denoted as ε3D.
- **p. 4 / 3 Method - extractive body cue:** 1, we propose a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding, where we construct dense correspondences across 2D image pixels, 3D points ...
- **p. 8 / 3 Method - extractive body cue:** We use the text-to-3D label map M 3D as the pseudo label to facilitate the alignment of point and text features.
- **p. 6 / 3 Method - extractive body cue:** Finally, we generate the text embeddings fT tag and fT llm using CLIP text encoder based on the generated tags Ttag and scene descriptions Tllm, ...
- **p. 6 / 3 Method - extractive body cue:** Firstly, they are fine-tuned on in-vocabulary datasets, which leads to a misalignment between image and text features and consequently results in poor performance on open-vocabulary ...
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Firstly, we use the image tagging foundation model such as RAM [23] to extract all possible categories from an image, and utilize ... | p. 5 (3 Method), p. 7 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | On one hand, we use the frozen CLIP visual encoder to ensure the intactness of image-text alignment, obtaining CLIP features f2D clip. | p. 7 (3 Method), p. 8 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Firstly, we extract 3D features for the point cloud by utilizing a 3D network, denoted as ε3D. | p. 8 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 9 / 3 Method - extractive body cue:** For 3D-2D pairs, we follow the previous work [42] to fuse pixel embeddings across K different views, represented as [f2D 1 , · · · ...
- **p. 8 / 3 Method - extractive body cue:** Consequently, The Binary Cross Entropy (BCE) loss is used to effectively penalize both positive and negative samples: \mathcal {L } _{3d-t ext (t ag)} = ...
- **p. 8 / 3 Method - extractive body cue:** In this work, we do not employ the Cross-Entropy loss because it would result in a mutually exclusive relationship between different classes, meaning that each ...
- **p. 5 / 3 Method - extractive body cue:** Although well-trained human annotators could potentially provide detailed language descriptions of 3D scenes, such a method is costly and lacks scalability.
- **p. 9 / 3 Method - extractive body cue:** (6) Since 2D mask head is also trainable, we additionally add the text-to-2D supervision and compute the BCE loss between 2D predictions and 2D masks, ...
- **p. 6 / 3 Method - extractive body cue:** 2D model has advantages in segmenting background objects (in blue boxes), while 3D model is more favorable for foreground objects with distinct structures (in red ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, input, list, instruct, GPT, examine, words, perform, reasoning, according, chain, thought, outputting, boolean | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, input, list, instruct, GPT, examine, words, perform, reasoning, according | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | order, leverage, synergistic, benefits, multiple, modalities, dense, prediction, tasks, multimodal | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | D-2D, pairs, follow, previous, fuse, pixel, embeddings, across, different, views | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive body cue:** Given the input list, we instruct GPT to examine the words one by one and perform reasoning according to the chain of thought, outputting a ...
- **p. 6 / 3 Method - extractive body cue:** Owing to the exposure to a diverse range of linguistic patterns and contextual nuances, the MLLMs can generate comprehensive and in-depth descriptions based on input ...
- **p. 6 / 3 Method - extractive body cue:** 3.2 Structure-aware Image Feature Extraction Compared to language modality, the image modality offers a wealth of contextual information and exhibits significant variations among different pixels, ...
- **p. 2 / 1 Introduction - extractive body cue:** Based on these observations, researchers have attempted to use image or natural language modalities to provide supervisory signals for learning 3D representations [13,36,42,55].
- **p. 7 / 3 Method - extractive body cue:** Firstly, we construct the associations between image and language modalities by taking C different text embeddings fT = {fT 1 , · · · , ...
- **p. 5 / 3 Method - extractive body cue:** 1 of supplemental material for the detailed instructions and examples to reduce the noisy tags.
- **p. 7 / 3 Method - extractive body cue:** M 3D can be regarded as the pseudo label map for point cloud, serving as the supervision signal for training 3D models.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 1, we propose a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding, where we construct dense correspondences across 2D image ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We address this issue in two steps. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | As for nuScenes dataset, we use 8 GPUs for training and set the batch size as 16. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive body cue:** Finally, we generate the text embeddings fT tag and fT llm using CLIP text encoder based on the generated tags Ttag and scene descriptions Tllm, ...
- **p. 6 / 3 Method - extractive body cue:** Firstly, they are fine-tuned on in-vocabulary datasets, which leads to a misalignment between image and text features and consequently results in poor performance on open-vocabulary ...
- **p. 9 / 4 Experiments - extractive body cue:** As for nuScenes dataset, we use 8 GPUs for training and set the batch size as 16.
- **p. 13 / 4 Experiments - extractive body cue:** 53.5% mIoU(F), and hence significantly reducing inference time.
- **p. 10 / 4 Experiments - extractive body cue:** 1, although OpenScene(LSeg) attains better results (54.2% mIoU) by using both 2D and 3D encoders, it results in significantly increased inference latency.
- **p. 10 / 4 Experiments - extractive body cue:** This is because the parameter size of 2D encoder is much larger than 3D encoder, and the 2D encoder needs to perform inference on multi-view ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Firstly, image, tagging, foundation, model, RAM, extract, possible, categories, utilize, category, names, short, descriptions, derived, metadata, text, query, referred, Ttag.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | As for nuScenes dataset, we use 8 GPUs for training and set the batch size as 16. | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Semantic / temporal fusion | We conduct comparisons with state-of-the-art methods on each of these datasets. | p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Robot query / planning handoff | Our DMA(OpenSeg) using only 3D model for prediction outperforms OpenScene(OpenSeg)-2D3D by 5.4% mIoU at a significantly lower latency, wherein the mIoU (F) ... | p. 10 (4 Experiments), p. 14 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 12 / 4 Experiments - extractive body cue:** This can be attributed to that OpenScene heavily relies on 2D model for supervision without aligning with text prompts, which limits its open-vocabulary ability.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 1: Framework of our proposed Dense Multimodal Alignment (DMA) method. We generate comprehensive language modality data by leveraging a tagging model and an MLLM. ...
- **p. 11 / 4 Experiments - extractive body cue:** Besides, by fine-tuning the mask head, FC-CLIP could incorporate the 3D structural priors into mask features and produce better results.
- **p. 11 / 4 Experiments - extractive body cue:** Our method does not rely on ground truth 3D labels but instead distill knowledge from pretrained vision-language models, thus it is more robust to rare ...
- **p. 13 / 4 Experiments - extractive body cue:** Comparisons of Different Fine-Tuning Methods.
- **p. 13 / 4 Experiments - extractive body cue:** For the enhanced version, we replace RAM with RAM++ [22], and LLaVA-7B with LLaVA-13B.
- **p. 14 / 4 Experiments - extractive body cue:** 6, by fully fine-tuning the mask head, the performances of 2D and 3D masks are improved by 3.8% and 1.9%, respectively.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 4 (3 Method), p. 8 (3 Method), p. 6 (3 Method), objective p. 9 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 5 (3 Method), p. 9 (3 Method), p. 6 (3 Method), temporal p. 4 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 10 (4 Experiments), p. 10 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
