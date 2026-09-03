# Method - 3D Question Answering via only 2D Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IkhJApkJQ3; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168051. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 6 (3. Preliminaries), p. 2 (1. Introduction), p. 4 (3. Preliminaries), p. 6 (3. Preliminaries), p. 4 (3. Preliminaries)): To train this module, we design a viewAnnotator that automatically generates training data in two steps. viewAnnotator firstly converts question-answer pairs into descriptive captions.

## Method Body Digest

- **p. 2 / 1. Introduction - extractive body cue:** To train this module, we design a viewAnnotator that automatically generates training data in two steps. viewAnnotator firstly converts question-answer pairs into descriptive captions.
- **p. 6 / 3. Preliminaries - extractive body cue:** Views are classified as "uncertain" when the model chooses the option of "Uncertain, insufficient or unclear information" or outputs none of the given options, and ...
- **p. 2 / 1. Introduction - extractive body cue:** 2D features extracted from LVLMs are already well-aligned with language, but further alignment with 3D features requires careful model design and advanced training techniques.
- **p. 4 / 3. Preliminaries - extractive body cue:** Following (Mo & Liu, 2024), we use the BLIP's image-text retrieval model (Li et al., 2022) to select views that best match the question Q ...
- **p. 6 / 3. Preliminaries - extractive body cue:** We apply crossattention in each transformer layer between the question embedding Q and the visual embeddings {Vi}N i=1, in order to enhance the model's ability ...
- **p. 4 / 3. Preliminaries - extractive body cue:** Then, M′ and the question Q are input into the model to produce the answer A: A = LVLM(M′, Q).
- **p. 5 / 3. Preliminaries - extractive body cue:** Step 1: Caption Generation Step 2: View Matching Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light ...
- **p. 6 / 3. Preliminaries - extractive body cue:** The mismatch loss is used to optimize the parameters of viewSelector.

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views ...
- **p. 1 / 1. Introduction - extractive body cue:** All of these methods require computationally intensive 3D-language alignment using point cloud data for spatial reasoning. a4 is our method that leverages pre-trained LVLMs operating ...
- **p. 2 / 1. Introduction - extractive body cue:** (2) We introduce cdViews that integrates a viewSelector with a viewNMS to capture critical and diverse views.

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive body cue:** To train this module, we design a viewAnnotator that automatically generates training data in two steps. viewAnnotator firstly converts question-answer pairs into descriptive captions.
- **p. 6 / 3. Preliminaries - extractive body cue:** Views are classified as "uncertain" when the model chooses the option of "Uncertain, insufficient or unclear information" or outputs none of the given options, and ...
- **p. 2 / 1. Introduction - extractive body cue:** 2D features extracted from LVLMs are already well-aligned with language, but further alignment with 3D features requires careful model design and advanced training techniques.
- **p. 4 / 3. Preliminaries - extractive body cue:** Following (Mo & Liu, 2024), we use the BLIP's image-text retrieval model (Li et al., 2022) to select views that best match the question Q ...
- **p. 6 / 3. Preliminaries - extractive body cue:** We apply crossattention in each transformer layer between the question embedding Q and the visual embeddings {Vi}N i=1, in order to enhance the model's ability ...
- **p. 4 / 3. Preliminaries - extractive body cue:** Then, M′ and the question Q are input into the model to produce the answer A: A = LVLM(M′, Q).
- **p. 5 / 3. Preliminaries - extractive body cue:** Step 1: Caption Generation Step 2: View Matching Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To train this module, we design a viewAnnotator that automatically generates training data in two steps. viewAnnotator firstly converts question-answer pairs into ... | p. 2 (1. Introduction), p. 6 (3. Preliminaries) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Views are classified as "uncertain" when the model chooses the option of "Uncertain, insufficient or unclear information" or outputs none of the ... | p. 6 (3. Preliminaries), p. 2 (1. Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 2D features extracted from LVLMs are already well-aligned with language, but further alignment with 3D features requires careful model design and advanced ... | p. 2 (1. Introduction), p. 4 (3. Preliminaries) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3. Preliminaries - extractive body cue:** The mismatch loss is used to optimize the parameters of viewSelector.
- **p. 6 / 3. Preliminaries - extractive body cue:** (7) The score ˆSi is supervised with the corresponding label Si by binary cross-entropy loss: LBCE = -1 N ′ N′ X i=1  ˆSi ...
- **p. 2 / 1. Introduction - extractive body cue:** This constraint makes it crucial to carefully select the most informative views.
- **p. 2 / 1. Introduction - extractive body cue:** (2) Enhance View Diversity: The aim is to improve spatial diversity and minimize redundancy for the selected views.
- **p. 4 / 3. Preliminaries - extractive body cue:** As for inference, our cdViews has two modules to run: the viewSelector identifies critical views, and the viewNMS enhances view diversity and minimizes redundancy.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (1. Introduction), p. 6 (3. Preliminaries), p. 6 (3. Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, question, embedding, visual, input, outputs, binary, label, Since, LVLMs, fundamentally, designed, process, images | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | takes, question, embedding, visual, input, outputs, binary, label, Since, LVLMs | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | cdViews, novel, automatically, selecting, critical, diverse, Views, D-QA, consists, components | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | mismatch, loss, optimize, parameters, viewSelector, score, supervised, corresponding, label, binary | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3. Preliminaries - extractive body cue:** It takes the question embedding Q and the visual embedding set {Vi}N i=1 as input and outputs a binary label ˆSi (0 or 1) for ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since 2D LVLMs are fundamentally designed to process 2D images as input, we propose cdViews to efficiently select the most informative 2D views of 3D ...
- **p. 1 / 1. Introduction - extractive body cue:** We respectively use ① uniform sampling, ②image retrieval, and ③our cdViews, to select views as input to LLAVA-OV. significant breakthroughs in addressing 2D visual question ...
- **p. 4 / 3. Preliminaries - extractive body cue:** Then, M′ and the question Q are input into the model to produce the answer A: A = LVLM(M′, Q).
- **p. 5 / 3. Preliminaries - extractive body cue:** This process aims to identify the critical views that match mostly the content of both input questions and the corresponding answers.
- **p. 5 / 3. Preliminaries - extractive body cue:** Step 1: Caption Generation Step 2: View Matching Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light ...
- **p. 6 / 3. Preliminaries - extractive body cue:** Similarly, for visual inputs, each visual embedding Vi is processed through the same modules.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | To train this module, we design a viewAnnotator that automatically generates training data in two steps. viewAnnotator firstly converts question-answer pairs into ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To tackle the challenges, we introduce a new framework cdViews to select critical and diverse Views <Question>: What is the black couch ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. Introduction - extractive body cue:** To train this module, we design a viewAnnotator that automatically generates training data in two steps. viewAnnotator firstly converts question-answer pairs into descriptive captions.
- **p. 6 / 3. Preliminaries - extractive body cue:** Views are classified as "uncertain" when the model chooses the option of "Uncertain, insufficient or unclear information" or outputs none of the given options, and ...
- **p. 2 / 1. Introduction - extractive body cue:** 2D features extracted from LVLMs are already well-aligned with language, but further alignment with 3D features requires careful model design and advanced training techniques.
- **p. 7 / 5. Experiments - extractive body cue:** Training of the viewSelector is conducted with a learning rate of 5 × 10-5 and a batch size of
- **p. 4 / 3. Preliminaries - extractive body cue:** As for inference, our cdViews has two modules to run: the viewSelector identifies critical views, and the viewNMS enhances view diversity and minimizes redundancy.
- **p. 5 / 3. Preliminaries - extractive body cue:** The training of viewSelector contains two steps: data annotation and model training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** train, module, design, viewAnnotator, automatically, generates, training, data, steps, firstly, converts, question-answer, pairs, descriptive, captions, Views, classified, uncertain, when, model.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or ... | p. 7 (5. Experiments), p. 7 (5. Experiments) |
| Semantic / temporal fusion | Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at ... | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at ... | p. 5 (Figure/Table caption), p. 4 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 5. Experiments - extractive body cue:** ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects).
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). For ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: An ablation study performed on ScanQA. We show the best EM@1 scores with the corresponding (optimal) k. selected views is shown in Figure ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: The results of EM@1 using two configurations: optimal k (blue) vs. fixed k=9 (green). X-axis is the thresh- old T of viewNMS. T ...
- **p. 7 / 5.1. Comparisons with the State-of-the-Arts - extractive body cue:** The reason is that the uniform sampling method ignores the question and the image retrieval method often fails to capture critical views or introduces redundancy ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1. Introduction), p. 6 (3. Preliminaries), p. 2 (1. Introduction), p. 4 (3. Preliminaries), p. 6 (3. Preliminaries), p. 4 (3. Preliminaries), objective p. 6 (3. Preliminaries), p. 6 (3. Preliminaries), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Preliminaries), temporal p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Related Works), p. 3 (2. Related Works), p. 5 (3. Preliminaries), p. 5 (3. Preliminaries).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
