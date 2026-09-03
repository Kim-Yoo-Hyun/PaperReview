# Method - CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Cross-modality Features Extraction), p. 4 (3.1. Cross-modality Features Extraction), p. 3 (3.1. Cross-modality Features Extraction), p. 3 (3.1. Cross-modality Features Extraction), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses)): Drawing from the VL-SAT method described in [48], we use a pretrained CLIP vision encoder Iθ to produce features for multi-view images.

## Method Body Digest

- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** Drawing from the VL-SAT method described in [48], we use a pretrained CLIP vision encoder Iθ to produce features for multi-view images.
- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** There is a wooden rectangle table behind of the beige armchair. %%% 3DSG Feature Extractor I3D Loss √ Positive term × Negative term T3D Loss ...
- **p. 3 / 3.1. Cross-modality Features Extraction - extractive body cue:** After generating these negative samples, we use Tθ to denote the text feature extractor from CLIP and extract the text feature FT ∈Rw×512.
- **p. 3 / 3.1. Cross-modality Features Extraction - extractive body cue:** To enhance the discriminative power of text features and ensure precise cross-modality feature alignment, we propose segmenting text based on grammatical analysis [43, 50].
- **p. 5 / 3.2. Cross-Modality Contrastive Losses - extractive body cue:** (3) For the object feature f i o ∈FP of the ith object, we first assign the text feature f i t ∈T + o ...
- **p. 5 / 3.2. Cross-Modality Contrastive Losses - extractive body cue:** (5) Then, we align the predicate words in the text with 3DSG features using the following formula: LT 3D p = M X i=1 -log ...
- **p. 3 / 1) Prompt learning based methods adjust to downstream - extractive body cue:** 2) Contrastive loss optimization based methods refine representations by augmenting similarity for positive samples and diminishing it for negative ones [7, 18, 35].
- **p. 3 / 3. Methods - extractive body cue:** In the final step, we employ crossmodality contrastive losses to align text with 3DSG features and images with 3DSG features independently (Section 3.2).

## Design Rationale

- **p. 2 / 1) Visual contextual - extractive body cue:** The primary contributions are summarized as: • We propose the new and practical tasks of OV 3DSGG.
- **p. 1 / Abstract - extractive body cue:** Specifically, we propose a novel Cross-Modality Contrastive Learning 3DSGG (CCL-3DSGG) method.
- **p. 3 / 3. Methods - extractive body cue:** Our framework is depicted in Figure 2.

## Source Evidence Cues

- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** Drawing from the VL-SAT method described in [48], we use a pretrained CLIP vision encoder Iθ to produce features for multi-view images.
- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** There is a wooden rectangle table behind of the beige armchair. %%% 3DSG Feature Extractor I3D Loss √ Positive term × Negative term T3D Loss ...
- **p. 3 / 3.1. Cross-modality Features Extraction - extractive body cue:** After generating these negative samples, we use Tθ to denote the text feature extractor from CLIP and extract the text feature FT ∈Rw×512.
- **p. 3 / 3.1. Cross-modality Features Extraction - extractive body cue:** To enhance the discriminative power of text features and ensure precise cross-modality feature alignment, we propose segmenting text based on grammatical analysis [43, 50].
- **p. 5 / 3.2. Cross-Modality Contrastive Losses - extractive body cue:** (3) For the object feature f i o ∈FP of the ith object, we first assign the text feature f i t ∈T + o ...
- **p. 5 / 3.2. Cross-Modality Contrastive Losses - extractive body cue:** (5) Then, we align the predicate words in the text with 3DSG features using the following formula: LT 3D p = M X i=1 -log ...
- **Detected method headings:** 1) Prompt learning based methods adjust to downstream (p. 3); 3. Methods (p. 3); 4.3. Comparisons with SOTA Methods on Close-Set (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Drawing from the VL-SAT method described in [48], we use a pretrained CLIP vision encoder Iθ to produce features for multi-view images. | p. 4 (3.1. Cross-modality Features Extraction), p. 4 (3.1. Cross-modality Features Extraction) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | There is a wooden rectangle table behind of the beige armchair. %%% 3DSG Feature Extractor I3D Loss √ Positive term × Negative ... | p. 4 (3.1. Cross-modality Features Extraction), p. 3 (3.1. Cross-modality Features Extraction) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | After generating these negative samples, we use Tθ to denote the text feature extractor from CLIP and extract the text feature FT ... | p. 3 (3.1. Cross-modality Features Extraction), p. 3 (3.1. Cross-modality Features Extraction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1) Prompt learning based methods adjust to downstream - extractive body cue:** 2) Contrastive loss optimization based methods refine representations by augmenting similarity for positive samples and diminishing it for negative ones [7, 18, 35].
- **p. 3 / 3. Methods - extractive body cue:** In the final step, we employ crossmodality contrastive losses to align text with 3DSG features and images with 3DSG features independently (Section 3.2).
- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** The T3D loss aligns text with 3DSG features.
- **p. 4 / 3.2. Cross-Modality Contrastive Losses - extractive body cue:** More specifically, these semantic label embeddings can be propagated to 3DSG features by designed contrastive loss.
- **p. 5 / 3.2. Cross-Modality Contrastive Losses - extractive body cue:** The final T3D loss is the mean of the two: LT 3D = (LT 3D o + LT 3D p) /2.
- **p. 5 / 3.2. Cross-Modality Contrastive Losses - extractive body cue:** Finally, our complete loss function is formed by the following combination of loss functions: LCCL-3DSGG = λ1LI3D + λ2LT 3D, (7) where the hyper-parameters λ1 ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (3. Methods), p. 3 (1) Prompt learning based methods adjust to downstream), p. 4 (3.1. Cross-modality Features Extraction), p. 4 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | begins, extraction, cross-modality, features, text, image, point, clouds, Section, CCL-3DSGG, architecture, inputting, image-text, pairs | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | begins, extraction, cross-modality, features, text, image, point, clouds, Section, CCL-3DSGG | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | primary, contributions, summarized, practical, tasks, DSGG, Specifically, novel, Cross-Modality, Contrastive | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Contrastive, loss, optimization, methods, refine, representations, augmenting, similarity, positive, samples | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Methods - extractive body cue:** Our approach begins with the extraction of cross-modality features from text T , image I, and 3D point clouds P (Section 3.1).
- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** The CCL-3DSGG architecture begins with inputting image-text pairs and unlabeled 3D point clouds, aiming to train the 3DSG feature extractor Pθ.
- **p. 5 / 3.2. Cross-Modality Contrastive Losses - extractive body cue:** During inference, we input the prompt "a point cloud of a {object class}" into Tθ to obtain features Finf T for all object classes.
- **p. 3 / 3.1. Cross-modality Features Extraction - extractive body cue:** 3.1.2 Image Features In point cloud data, each 3D scan is complemented by RGB sequences with associated camera poses, enabling us 27865
- **p. 2 / 1) Visual contextual - extractive body cue:** Collision Likelihood: 0.15 × ? ? ? lying on ? box item √ √ car car lying in overtaking box box Input Point Cloud Previous ...
- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** 3.1.3 3DSG Features Given the point set P of a scene s and the class-agnostic instance segmentation M, the task of 3DSGG first parses the ...
- **p. 1 / 1) Visual contextual - extractive body cue:** Despite notable advancements in 3DSGG, existing stateof-the-art (SOTA) methods still encounter two obstacles that constrain their practicality in the open-vocabulary (OV) settings.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Our framework is depicted in Figure 2. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | 3.1.2 Image Features In point cloud data, each 3D scan is complemented by RGB sequences with associated camera poses, enabling us 27865 | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Training is conducted using the Adam optimizer [24], with a batch size of 8, over 100 epochs. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** Drawing from the VL-SAT method described in [48], we use a pretrained CLIP vision encoder Iθ to produce features for multi-view images.
- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** There is a wooden rectangle table behind of the beige armchair. %%% 3DSG Feature Extractor I3D Loss √ Positive term × Negative term T3D Loss ...
- **p. 5 / 4.2. Implementation Details - extractive body cue:** Training is conducted using the Adam optimizer [24], with a batch size of 8, over 100 epochs.
- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** Drawing from the VL-SAT method described in [48], we use a pretrained CLIP vision encoder Iθ to produce features for multi-view images.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Drawing, VL-SAT, described, pretrained, CLIP, vision, encoder, produce, features, multi-view, images, There, wooden, rectangle, table, behind, beige, armchair, DSG, Feature.
- **Relevant PDF headings:** 1) Prompt learning based methods adjust to downstream (p. 3); 3. Methods (p. 3); 4.3. Comparisons with SOTA Methods on Close-Set (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | The training set of 3DSSG [47] contains 3582 scenes, while the testing set comprises 548 scenes. | p. 5 (4.1. Task Description), p. 5 (4.1. Task Description) |
| Global / local decision | Comparisons with state-of-the-arts on the 3DSSG dataset. | p. 6 (4.2. Implementation Details), p. 7 (4.4. Predicting Novel Classes) |
| Motion execution / recovery | Despite introducing additional information, our model achieves a significant performance boost without a substantial increase in time (24 to 30). | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |

## Failure and Ablation Link

- **p. 5 / 4. Experiments - extractive body cue:** We provide a detailed account of the task description and experimental settings, compare our model to SOTA methods, and conduct ablation studies to emphasize the ...
- **p. 6 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** Unsupervised experimental results of mR on the 3DSSG dataset. w/o CL means without classification losses.
- **p. 6 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** Despite introducing additional information, our model achieves a significant performance boost without a substantial increase in time (24 to 30).
- **p. 7 / 4.4. Predicting Novel Classes - extractive body cue:** Ablation studies on CCL-3DSGG with unsupervised.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** In this section, we show the ablation performance on the 3DSSG dataset in Table 5.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** In EXP 10, we employed the prediction head from VL-SAT to infer features without prompts during the testing phase.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. (a) Difference in training: Previous 3DSGG models trained on closed-set classes by fully supervised [12, 48, 61]. Our method trains a 3DSG feature ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Cross-modality Features Extraction), p. 4 (3.1. Cross-modality Features Extraction), p. 3 (3.1. Cross-modality Features Extraction), p. 3 (3.1. Cross-modality Features Extraction), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses), objective p. 3 (1) Prompt learning based methods adjust to downstream), p. 3 (3. Methods), p. 4 (3.1. Cross-modality Features Extraction), p. 4 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 5 (3.2. Cross-Modality Contrastive Losses), temporal p. 3 (3. Methods), p. 3 (3.1. Cross-modality Features Extraction), p. 2 (1) Visual contextual), p. 2 (1) Visual con), p. 8 (5. Conclusion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
