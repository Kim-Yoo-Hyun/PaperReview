# Method - OpenMask3D: Open-Vocabulary 3D Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.13631; PDF retrieval source: https://arxiv.org/pdf/2306.13631. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3 Method), p. 7 (Model), p. 4 (3 Method), p. 8 (Model), p. 5 (3 Method), p. 8 (Model)): The architecture consists of a sparse convolutional backbone based on the MinkowskiUNet [9], and a transformer decoder.

## Method Body Digest

- **p. 4 / 3 Method - extractive PDF cue:** The architecture consists of a sparse convolutional backbone based on the MinkowskiUNet [9], and a transformer decoder.
- **p. 7 / Model - extractive PDF cue:** In order to compute image features on the mask-crops, we use CLIP [55] visual encoder from the ViT-L/14 model pre-trained at a 336 pixel resolution, ...
- **p. 4 / 3 Method - extractive PDF cue:** We propose OpenMask3D, the first open-vocabulary 3D instance segmentation model.
- **p. 8 / Model - extractive PDF cue:** First, we analyze the performance of our model when we use class-agnostic masks from a mask-predictor trained on the 20 original ScanNet classes [10], and ...
- **p. 5 / 3 Method - extractive PDF cue:** In b⃝, we compute a 2D object mask in each selected frame, which is used to obtain multi-scale image-crops in order to extract effective CLIP ...
- **p. 8 / Model - extractive PDF cue:** To assess how well our model generalizes to other datasets, we use instance masks from the mask proposal module trained on ScanNet200, and test it ...
- **p. 6 / 3 Method - extractive PDF cue:** Algorithm 1 - 2D mask selection algorithm score∗←0, m2D ∗ ←0, r ←0 while r < krounds do Sample ksample points among the projected points ...
- **p. 9 / Model - extractive PDF cue:** For this experiment, we perform Hungarian matching between the predicted masks and oracle masks discarding all class-losses, and we only match based on the masks.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given text-query ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our approach is intrinsically different from the existing 3D open-vocabulary scene understanding approaches [24, 32, 52] as we propose an instance-based feature computation approach instead ...
- **p. 4 / 3 Method - extractive PDF cue:** Our pipeline consists of four subsequent steps: 1⃝Our approach takes as input posed RGB-D images of a 3D indoor scene along with its reconstructed point ...

## Source Evidence Cues

- **p. 4 / 3 Method - extractive PDF cue:** The architecture consists of a sparse convolutional backbone based on the MinkowskiUNet [9], and a transformer decoder.
- **p. 7 / Model - extractive PDF cue:** In order to compute image features on the mask-crops, we use CLIP [55] visual encoder from the ViT-L/14 model pre-trained at a 336 pixel resolution, ...
- **p. 4 / 3 Method - extractive PDF cue:** We propose OpenMask3D, the first open-vocabulary 3D instance segmentation model.
- **p. 8 / Model - extractive PDF cue:** First, we analyze the performance of our model when we use class-agnostic masks from a mask-predictor trained on the 20 original ScanNet classes [10], and ...
- **p. 5 / 3 Method - extractive PDF cue:** In b⃝, we compute a 2D object mask in each selected frame, which is used to obtain multi-scale image-crops in order to extract effective CLIP ...
- **p. 8 / Model - extractive PDF cue:** To assess how well our model generalizes to other datasets, we use instance masks from the mask proposal module trained on ScanNet200, and test it ...
- **p. 6 / 3 Method - extractive PDF cue:** Algorithm 1 - 2D mask selection algorithm score∗←0, m2D ∗ ←0, r ←0 while r < krounds do Sample ksample points among the projected points ...
- **Detected method headings:** 3 Method (p. 3); Model (p. 7); Model (p. 20)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The architecture consists of a sparse convolutional backbone based on the MinkowskiUNet [9], and a transformer decoder. | p. 4 (3 Method), p. 7 (Model) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | In order to compute image features on the mask-crops, we use CLIP [55] visual encoder from the ViT-L/14 model pre-trained at a ... | p. 7 (Model), p. 4 (3 Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We propose OpenMask3D, the first open-vocabulary 3D instance segmentation model. | p. 4 (3 Method), p. 8 (Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 9 / Model - extractive PDF cue:** For this experiment, we perform Hungarian matching between the predicted masks and oracle masks discarding all class-losses, and we only match based on the masks.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 9 (Model), p. 6 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | pipeline, takes, input, collection, posed, RGB-D, images, captured, indoor, scene, reconstructed, point, cloud, representation | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | pipeline, takes, input, collection, posed, RGB-D, images, captured, indoor, scene | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contributions, three-fold, introduce, open-vocabulary, instance, segmentation, task, object, instances, similar | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | experiment, perform, Hungarian, matching, between, predicted, masks, oracle, discarding, class-losses | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 Method - extractive PDF cue:** Our pipeline takes as input a collection of posed RGB-D images captured in an indoor scene, and the reconstructed point cloud representation of the scene.
- **p. 6 / 3 Method - extractive PDF cue:** 3.2.3 CLIP feature extraction and mask-feature aggregation For each instance mask, we collect k ⋅L images by selecting top-k views and obtaining L multi-level crops ...
- **p. 3 / 3 Method - extractive PDF cue:** Given a set of posed RGB-D images captured in a scene, along with the reconstructed scene point cloud 1⃝, OpenMask3D predicts 3D instance masks with ...
- **p. 4 / 3 Method - extractive PDF cue:** In the original setup, [58] produces two outputs: a set of M binary instance masks obtained from the predicted heatmaps, along with predicted class labels ...
- **p. 5 / 3 Method - extractive PDF cue:** SAM is sensitive to the set of input points (see Appendix A.2.3, A.2.4).
- **p. 5 / 3 Method - extractive PDF cue:** The output of SAM at a given iteration r is a 2D mask (m2D r ) and a mask confidence score (scorer).
- **p. 4 / 3 Method - extractive PDF cue:** 3.2.1 Frame selection Obtaining representative images of the proposed object instances is crucial for extracting accurate CLIP features.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | In the next step, we compute a 2D object mask in each selected frame, which is then used to obtain multi-scale image-crops ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | For each instance mask-proposal, we first compute the visibility of the object instance in each frame of the RGB-D sequence, and select ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / Model - extractive PDF cue:** In order to compute image features on the mask-crops, we use CLIP [55] visual encoder from the ViT-L/14 model pre-trained at a 336 pixel resolution, ...
- **p. 8 / Model - extractive PDF cue:** First, we analyze the performance of our model when we use class-agnostic masks from a mask-predictor trained on the 20 original ScanNet classes [10], and ...
- **p. 8 / Model - extractive PDF cue:** To assess how well our model generalizes to other datasets, we use instance masks from the mask proposal module trained on ScanNet200, and test it ...
- **p. 7 / Model - extractive PDF cue:** In order to compute image features on the mask-crops, we use CLIP [55] visual encoder from the ViT-L/14 model pre-trained at a 336 pixel resolution, ...
- **p. 3 / 3 Method - extractive PDF cue:** The mask-feature computation module leverages pre-trained CLIP [55] vision-language model in order to compute meaningful and flexible features for each mask.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** architecture, consists, sparse, convolutional, backbone, MinkowskiUNet, transformer, decoder, order, compute, image, features, mask-crops, CLIP, visual, encoder, ViT-L/14, model, pre-trained, pixel.
- **Relevant PDF headings:** 3 Method (p. 3); Model (p. 7); Model (p. 20).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | To assess the generalization capability of our method, we further experiment with the Replica [61] dataset, and evaluate on the office0, office1, ... | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Global / local decision | Table 5: 3D instance segmentation results on the ScanNet200 validation set, using oracle masks. We use ground truth instance masks for computing ... | p. 9 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Motion execution / recovery | Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green ... | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 19 / Figure/Table caption - extractive PDF cue:** Table 7: Ablation study of the multi-scale cropping hyperparameters on the Replica dataset. We analyze the effect of varying number of levels, and the ratio ...
- **p. 6 / 4 Experiments - extractive PDF cue:** Furthermore, we provide an ablation study for OpenMask3D.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: OpenMask3D Ablation Study. 2D mask and multi-scale crop components. 2D mask refers to whether SAM [36] was employed for computing 2D masks. Results ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: 3D instance segmentation results using masks from mask module trained on ScanNet20 annota- tions, evaluated on the ScanNet200 dataset [57]. We identify 53 ...
- **p. 19 / Figure/Table caption - extractive PDF cue:** Table 6: Ablation study of the top-k frame selection parameter k. This analysis is conducted on the ScanNet200 validation set. Levels Ratio of Exp. AP ...
- **p. 20 / Figure/Table caption - extractive PDF cue:** Figure 12: Visualization of the Replica RGB images. Original RGB images from the Replica dataset (left), and RGB images rendered from the scene point cloud ...
- **p. 18 / Figure/Table caption - extractive PDF cue:** Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected 3D mask as input. A.2.4 Why do ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3 Method), p. 7 (Model), p. 4 (3 Method), p. 8 (Model), p. 5 (3 Method), p. 8 (Model), objective p. 9 (Model), temporal p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 3 (3 Method), p. 5 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
