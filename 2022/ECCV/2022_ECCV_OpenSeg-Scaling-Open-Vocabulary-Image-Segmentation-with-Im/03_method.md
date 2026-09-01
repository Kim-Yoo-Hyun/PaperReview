# Method - OpenSeg: Scaling Open-Vocabulary Image Segmentation with Image-Level Labels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.12143; PDF retrieval source: https://arxiv.org/pdf/2112.12143. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 7 (3 Method), p. 8 (3 Method)): 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction and a cross-attention module for segmentation region proposal.

## Method Body Digest

- **p. 6 / 3 Method - extractive PDF cue:** 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction and a cross-attention ...
- **p. 6 / 3 Method - extractive PDF cue:** We use a cross-attention module taking inputs as FP E s and a randomly initialized queries q0 ∈RN×D to generate mask queries q ∈RN×D.
- **p. 7 / 3 Method - extractive PDF cue:** We follow MuST [17] and first train a teacher model on a segmentation dataset with only the segmentation loss LS.
- **p. 8 / 3 Method - extractive PDF cue:** 3.4 Inference Up to this point, we learn a vision model that predicts segmentation masks s ∈RN×H×W and corresponding features z ∈RN×D.
- **p. 7 / 3 Method - extractive PDF cue:** Then we annotate a large image-text dataset with pseudo segmentation labels using the teacher model.
- **p. 8 / 3 Method - extractive PDF cue:** Given an evaluation segmentation dataset, we encode its categories using the text encoder.
- **p. 7 / 3 Method - extractive PDF cue:** The grounding loss aims at maximizing the normalized score of a labeled image-caption pair ⟨Ib, Cb⟩over all images and all captions in a mini-batch.
- **p. 6 / 3 Method - extractive PDF cue:** We compute Dice coefficient [34] between predicted masks s and classagnostic labeled masks sl ∈RM×H×W and maximize the Dice coefficient of the best matched mask ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** We call our method OpenSeg, standing for open-vocabulary image segmentation.
- **p. 3 / 1 Introduction - extractive PDF cue:** To evaluate our method, we measure performances on holdout image segmentation datasets.
- **p. 6 / 3 Method - extractive PDF cue:** 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction and a cross-attention ...

## Source Evidence Cues

- **p. 6 / 3 Method - extractive PDF cue:** 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction and a cross-attention ...
- **p. 6 / 3 Method - extractive PDF cue:** We use a cross-attention module taking inputs as FP E s and a randomly initialized queries q0 ∈RN×D to generate mask queries q ∈RN×D.
- **p. 7 / 3 Method - extractive PDF cue:** We follow MuST [17] and first train a teacher model on a segmentation dataset with only the segmentation loss LS.
- **p. 8 / 3 Method - extractive PDF cue:** 3.4 Inference Up to this point, we learn a vision model that predicts segmentation masks s ∈RN×H×W and corresponding features z ∈RN×D.
- **p. 7 / 3 Method - extractive PDF cue:** Then we annotate a large image-text dataset with pseudo segmentation labels using the teacher model.
- **p. 8 / 3 Method - extractive PDF cue:** Given an evaluation segmentation dataset, we encode its categories using the text encoder.
- **Detected method headings:** 3 Method (p. 6); B Limitations of our approach (p. 18); C Architecture of the cross-attention module (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction ... | p. 6 (3 Method), p. 6 (3 Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We use a cross-attention module taking inputs as FP E s and a randomly initialized queries q0 ∈RN×D to generate mask queries ... | p. 6 (3 Method), p. 7 (3 Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We follow MuST [17] and first train a teacher model on a segmentation dataset with only the segmentation loss LS. | p. 7 (3 Method), p. 8 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 Method - extractive PDF cue:** The grounding loss aims at maximizing the normalized score of a labeled image-caption pair ⟨Ib, Cb⟩over all images and all captions in a mini-batch.
- **p. 6 / 3 Method - extractive PDF cue:** We compute Dice coefficient [34] between predicted masks s and classagnostic labeled masks sl ∈RM×H×W and maximize the Dice coefficient of the best matched mask ...
- **p. 7 / 3 Method - extractive PDF cue:** We follow the grounding loss in prior works [19,58] to learn region-word alignments.
- **p. 6 / 3 Method - extractive PDF cue:** Therefore, a subset of proposal masks are optimized to best match labeled masks.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method), p. 6 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | argue, what, missing, state-of-the-art, open-vocabulary, classification, models, mid-level, representations, visual, groupings, organize, image, small | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | argue, what, missing, state-of-the-art, open-vocabulary, classification, models, mid-level, representations, visual | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | call, OpenSeg, standing, open-vocabulary, image, segmentation, evaluate, measure, performances, holdout | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | grounding, loss, aims, maximizing, normalized, score, labeled, image-caption, pair, over | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** We argue that what is missing in these state-of-the-art open-vocabulary classification models are mid-level representations from visual groupings [48], which organize an image into a ...
- **p. 6 / 3 Method - extractive PDF cue:** We use a cross-attention module taking inputs as FP E s and a randomly initialized queries q0 ∈RN×D to generate mask queries q ∈RN×D.
- **p. 6 / 3 Method - extractive PDF cue:** 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction and a cross-attention ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The segmentation model takes text queries as inputs and produces segmented regions accordingly.
- **p. 7 / 3 Method - extractive PDF cue:** We generate image features Fz using the same architecture as Fs.
- **p. 7 / 3 Method - extractive PDF cue:** Then we annotate a large image-text dataset with pseudo segmentation labels using the teacher model.
- **p. 3 / 1 Introduction - extractive PDF cue:** To our knowledge, OpenSeg is the first work in image segmentation to demonstrate zero-shot transfer results across datasets using language.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | We train OpenSeg on COCO dataset for 30k steps. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | For training on COCO and Localized Narrative datasets, we sample examples from the datasets with equal probability and we train the model ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3 Method - extractive PDF cue:** We follow MuST [17] and first train a teacher model on a segmentation dataset with only the segmentation loss LS.
- **p. 8 / 3 Method - extractive PDF cue:** 3.4 Inference Up to this point, we learn a vision model that predicts segmentation masks s ∈RN×H×W and corresponding features z ∈RN×D.
- **p. 8 / 4 Experiments - extractive PDF cue:** Unless otherwise stated, for each core we compute the loss over the local batch of examples (See Appendix F for the comparison between sync and ...
- **p. 13 / 4 Experiments - extractive PDF cue:** For training these models, we use the same hyper-parameters, and only tune the learning rate (0.32 for scratch, 0.08 for NoisyStudent init. and 0.005 for ...
- **p. 13 / 4 Experiments - extractive PDF cue:** We may be able to reduce the gap by increasing the batch size and training with more data.
- **p. 12 / 4 Experiments - extractive PDF cue:** For the strongest OpenSeg (last two rows), we initialize EfficientNet-b7 backbone with ALIGN pre-trained image encoder [23].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Learning, Segmentation, Masks, design, model, architecture, consists, feature, pyramid, network, FPN, multi-scale, extraction, cross-attention, module, region, proposal, taking, inputs, randomly.
- **Relevant PDF headings:** 3 Method (p. 6); B Limitations of our approach (p. 18); C Architecture of the cross-attention module (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Training Datasets COCO: We use the panoptic segmentation [26] and caption [9] annotations in the 2017 splits which include 118k/5k train/val images. | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Global / local decision | Then we discuss the experimental results with our open-vocabulary baselines and state-of-the-art open-vocabulary and zero-shot methods. | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Motion execution / recovery | OpenSeg significantly outperforms pre-trained ALIGN [23]: OpenSeg trained on COCO outperforms ALIGN baseline on all of the benchmarks significantly. | p. 11 (4 Experiments), p. 12 (4 Experiments) |

## Failure and Ablation Link

- **p. 10 / 4 Experiments - extractive PDF cue:** ALIGN w/proposal baseline: The ALIGN, LSeg and LSeg+ baselines are methods that perform visual-semantic alignments without explicit visual grouping.
- **p. 13 / 4 Experiments - extractive PDF cue:** This method performs inference without mask proposals.
- **p. 13 / 4 Experiments - extractive PDF cue:** Narr.  8.8 12.2 28.6 48.2 72.2 4.4 Ablation Experiments Importance of backbone initialization: In order to save the computation, we initialize OpenSeg from the ...
- **p. 14 / 4 Experiments - extractive PDF cue:** This procedure removes conjunctions, pronouns, adverbs, verbs, etc. which reduces the noises.
- **p. 24 / Figure/Table caption - extractive PDF cue:** Figure 8. Predictions of OpenSeg on random examples in the A-150 dataset (Part1). For each example, top left is the input image, top right is ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Since we initialize the backbone of OpenSeg from ALIGN's pretrained checkpoint, we use ALIGN as a baseline.
- **p. 12 / 4 Experiments - extractive PDF cue:** We initialize ResNet101 backbone of OpenSeg and LSeg+ with ImageNet pretrained weights similar to the baselines.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 7 (3 Method), p. 8 (3 Method), objective p. 7 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 6 (3 Method), temporal p. 8 (4 Experiments), p. 8 (4 Experiments), p. 13 (4 Experiments), p. 1 (Front matter), p. 2 (1 Introduction), p. 3 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
