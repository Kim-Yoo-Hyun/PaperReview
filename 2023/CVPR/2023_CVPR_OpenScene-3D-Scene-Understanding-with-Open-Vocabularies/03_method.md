# Method - OpenScene: 3D Scene Understanding with Open Vocabularies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2211.15654; PDF retrieval source: https://arxiv.org/pdf/2211.15654. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. 3D Distillation), p. 3 (3.1. Image Feature Fusion), p. 3 (3. Method), p. 4 (3.3. 2D-3D Feature Ensemble)): To enforce the output of the network F3D to be consistent with the fused features F2D, we use a cosine similarity loss: \ c L = 1 - \text {cos}(\bF ...

## Method Body Digest

- **p. 4 / 3.2. 3D Distillation - extractive PDF cue:** To enforce the output of the network F3D to be consistent with the fused features F2D, we use a cosine similarity loss: \ c L ...
- **p. 3 / 3.1. Image Feature Fusion - extractive PDF cue:** The first step in our approach is to extract dense perpixel embeddings for each RGB image from a 2D visuallanguage segmentation model, and then back-project ...
- **p. 3 / 3. Method - extractive PDF cue:** We first compute per-pixel features for every image using a model pre-trained for open-vocabulary 2D semantic segmentation.
- **p. 4 / 3.3. 2D-3D Feature Ensemble - extractive PDF cue:** We first compute the embeddings for all the text prompts using the CLIP [43] text encoder Etext, denoted as T = {t1, · · · ...
- **p. 4 / 3.2. 3D Distillation - extractive PDF cue:** Specifically, given an input point cloud P, we seek to learn an encoder that outputs per-point embeddings: \ b F ^\tex t { 3 D} ...
- **p. 3 / 3. Method - extractive PDF cue:** We next distill a 3D network to reproduce the fused features using only the 3D point cloud as input Sec.
- **p. 4 / 3.2. 3D Distillation - extractive PDF cue:** Therefore, we can distill such 2D visual-language knowledge into a 3D point network that only takes 3D point positions as input.
- **p. 1 / 1. Introduction - extractive PDF cue:** Given a 3D mesh or point cloud with a set of posed RGB images, the goal is to infer the semantics, affordances, functions, and physical ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Overall, our contributions are summarized as follows: • We introduce open vocabulary 3D scene understanding tasks where arbitrary text queries are used for semantic segmentation, ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We present OpenScene, a simple yet effective zero-shot approach for open-vocabulary 3D scene understanding.
- **p. 4 / 3.3. 2D-3D Feature Ensemble - extractive PDF cue:** Although one can already perform open-vocabulary queries with the 2D fused features F2D or 3D distilled features F3D, here we introduce a 2D-3D ensemble method ...

## Source Evidence Cues

- **p. 4 / 3.2. 3D Distillation - extractive PDF cue:** To enforce the output of the network F3D to be consistent with the fused features F2D, we use a cosine similarity loss: \ c L ...
- **p. 3 / 3.1. Image Feature Fusion - extractive PDF cue:** The first step in our approach is to extract dense perpixel embeddings for each RGB image from a 2D visuallanguage segmentation model, and then back-project ...
- **p. 3 / 3. Method - extractive PDF cue:** We first compute per-pixel features for every image using a model pre-trained for open-vocabulary 2D semantic segmentation.
- **p. 4 / 3.3. 2D-3D Feature Ensemble - extractive PDF cue:** We first compute the embeddings for all the text prompts using the CLIP [43] text encoder Etext, denoted as T = {t1, · · · ...
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To enforce the output of the network F3D to be consistent with the fused features F2D, we use a cosine similarity loss: ... | p. 4 (3.2. 3D Distillation), p. 3 (3.1. Image Feature Fusion) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The first step in our approach is to extract dense perpixel embeddings for each RGB image from a 2D visuallanguage segmentation model, ... | p. 3 (3.1. Image Feature Fusion), p. 3 (3. Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We first compute per-pixel features for every image using a model pre-trained for open-vocabulary 2D semantic segmentation. | p. 3 (3. Method), p. 4 (3.3. 2D-3D Feature Ensemble) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. 3D Distillation - extractive PDF cue:** To enforce the output of the network F3D to be consistent with the fused features F2D, we use a cosine similarity loss: \ c L ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3.4. Inference), p. 4 (3.2. 3D Distillation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, given, input, point, cloud, seek, learn, encoder, outputs, per-point, embeddings, text, quad, times | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Specifically, given, input, point, cloud, seek, learn, encoder, outputs, per-point | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Overall, contributions, summarized, follows, introduce, open, vocabulary, scene, understanding, tasks | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | enforce, output, network, F3D, consistent, fused, features, F2D, cosine, similarity | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. 3D Distillation - extractive PDF cue:** Specifically, given an input point cloud P, we seek to learn an encoder that outputs per-point embeddings: \ b F ^\tex t { 3 D} ...
- **p. 3 / 3. Method - extractive PDF cue:** We next distill a 3D network to reproduce the fused features using only the 3D point cloud as input Sec.
- **p. 4 / 3.2. 3D Distillation - extractive PDF cue:** Therefore, we can distill such 2D visual-language knowledge into a 3D point network that only takes 3D point positions as input.
- **p. 1 / 1. Introduction - extractive PDF cue:** Given a 3D mesh or point cloud with a set of posed RGB images, the goal is to infer the semantics, affordances, functions, and physical ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Next, we train a sparse 3D convolutional network to perform feature extraction from only the 3D point cloud geometry with a loss that minimizes differences ...
- **p. 3 / 3.1. Image Feature Fusion - extractive PDF cue:** The first step in our approach is to extract dense perpixel embeddings for each RGB image from a 2D visuallanguage segmentation model, and then back-project ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To achieve this, we establish associations between 3D points and pixels from posed images in the 3D scene, and train a 3D network to embed ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | The first step in our approach is to extract dense perpixel embeddings for each RGB image from a 2D visuallanguage segmentation model, ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | With the 2D-3D pairing, the corresponding 2D features in frame i for point p can be written as fi = Ii(u) ∈RC. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | There is a long history of work on 3D scene understanding for vision and robotics applications. | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Method - extractive PDF cue:** We first compute per-pixel features for every image using a model pre-trained for open-vocabulary 2D semantic segmentation.
- **p. 3 / 3. Method - extractive PDF cue:** We first compute per-pixel features for every image using a model pre-trained for open-vocabulary 2D semantic segmentation.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** enforce, output, network, F3D, consistent, fused, features, F2D, cosine, similarity, loss, text, label, MinkowskiNet18A, backbone, E3D, change, dimension, outputs, first.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | To test our method in a variety of settings, we evaluate on three popular public benchmarks: ScanNet [11,46], Matterport3D [4], and nuScenes ... | p. 4 (4. Experiments), p. 4 (4. Experiments) |
| Global / local decision | Again, we outperform the zero-shot baseline (MSeg Voting) on both mIoU and mAcc metrics all three datasets. | p. 5 (4.1. Comparisons), p. 5 (4. Experiments) |
| Motion execution / recovery | Again, we outperform the zero-shot baseline (MSeg Voting) on both mIoU and mAcc metrics all three datasets. | p. 5 (4.1. Comparisons), p. 5 (4. Experiments) |

## Failure and Ablation Link

- **p. 5 / 4. Experiments - extractive PDF cue:** Still, both of our variants show significantly better performance in both mIoU and mAcc. detailed scenes, and thus provides the opportunity to stress open-vocabulary queries.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Open-vocabulary 3D Scene Understanding. We propose OpenScene, a zero-shot approach to 3D scene understanding that co-embeds dense 3D point features with image pixels ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation Study. Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 classes ...
- **p. 8 / 6. Limitations and Future Work - extractive PDF cue:** There are several limitations of our work and still much to do to realize the full potential of the proposed approach.
- **p. 8 / 6. Limitations and Future Work - extractive PDF cue:** In future work, it will be interesting to design experiments to quantify the success of open vocabulary queries for tasks where ground truth is not ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Unlike [39], which requires training on 16 seen classes, our approach does not train with any 2D or 3D ground labels on any classes.
- **p. 5 / 4.1. Comparisons - extractive PDF cue:** Our results on those classes is significantly better than [39] (7.7% vs 62.8% mIoU), even though 3DGenz [39] utilizes ground truth data for 16 seen ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. 3D Distillation), p. 3 (3.1. Image Feature Fusion), p. 3 (3. Method), p. 4 (3.3. 2D-3D Feature Ensemble), objective p. 4 (3.2. 3D Distillation), temporal p. 3 (3.1. Image Feature Fusion), p. 4 (3.1. Image Feature Fusion), p. 4 (3.1. Image Feature Fusion), p. 6 (4.1. Comparisons), p. 3 (2. Related Work), p. 2 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
