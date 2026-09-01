# Method - Detecting Twenty-thousand Classes using Image-level Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.02605; PDF retrieval source: https://arxiv.org/pdf/2201.02605. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (X. Zhou et al), p. 5 (3 Preliminaries), p. 6 (X. Zhou et al), p. 8 (X. Zhou et al), p. 4 (X. Zhou et al), p. 4 (X. Zhou et al)): We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise other outputs for imagelabeled data.

## Method Body Digest

- **p. 2 / X. Zhou et al - extractive PDF cue:** We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise other outputs for ...
- **p. 5 / 3 Preliminaries - extractive PDF cue:** We use the region proposal network to extract N object features {(b, f, o)j}N j=1.
- **p. 6 / X. Zhou et al - extractive PDF cue:** We then apply the classification loss to its RoI features f ′ for all classes c ∈{ck}K k=1: Limage-box = BCE(Wf ′, c) where BCE(s, ...
- **p. 8 / X. Zhou et al - extractive PDF cue:** To shorten the experimental cycle and have a good initialization for prediction-based WSOD losses [44, 45], we always first train a converged base-class-only model (4× ...
- **p. 4 / X. Zhou et al - extractive PDF cue:** Unlike prior work, we use a simple image-supervised loss.
- **p. 4 / X. Zhou et al - extractive PDF cue:** Instead, we use additional image-labeled data for co-training.
- **p. 6 / X. Zhou et al - extractive PDF cue:** We introduce two alternatives: the proposal with the max object score or the proposal with the max size: Lmax-object-score = BCE(Wfj, c), j = argmaxjoj ...
- **p. 4 / X. Zhou et al - extractive PDF cue:** Equalization losses [55, 56] and SeeSaw loss [64] reweights the per-class loss by balancing the gradients [55] or number of samples [64].

## Design Rationale

- **p. 2 / X. Zhou et al - extractive PDF cue:** This also enables our method to learn detectors for new classes which would have been impossible to predict and assign.
- **p. 1 / 1 Introduction - extractive PDF cue:** Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).
- **p. 1 / 1 Introduction - extractive PDF cue:** In this paper, we propose Detector with image classes (Detic) that uses image-level supervision in addition to detection supervision.

## Source Evidence Cues

- **p. 2 / X. Zhou et al - extractive PDF cue:** We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise other outputs for ...
- **p. 5 / 3 Preliminaries - extractive PDF cue:** We use the region proposal network to extract N object features {(b, f, o)j}N j=1.
- **p. 6 / X. Zhou et al - extractive PDF cue:** We then apply the classification loss to its RoI features f ′ for all classes c ∈{ck}K k=1: Limage-box = BCE(Wf ′, c) where BCE(s, ...
- **p. 8 / X. Zhou et al - extractive PDF cue:** To shorten the experimental cycle and have a good initialization for prediction-based WSOD losses [44, 45], we always first train a converged base-class-only model (4× ...
- **p. 4 / X. Zhou et al - extractive PDF cue:** Unlike prior work, we use a simple image-supervised loss.
- **p. 4 / X. Zhou et al - extractive PDF cue:** Instead, we use additional image-labeled data for co-training.
- **p. 6 / X. Zhou et al - extractive PDF cue:** We introduce two alternatives: the proposal with the max object score or the proposal with the max size: Lmax-object-score = BCE(Wfj, c), j = argmaxjoj ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise ... | p. 2 (X. Zhou et al), p. 5 (3 Preliminaries) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We use the region proposal network to extract N object features {(b, f, o)j}N j=1. | p. 5 (3 Preliminaries), p. 6 (X. Zhou et al) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We then apply the classification loss to its RoI features f ′ for all classes c ∈{ck}K k=1: Limage-box = BCE(Wf ′, ... | p. 6 (X. Zhou et al), p. 8 (X. Zhou et al) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / X. Zhou et al - extractive PDF cue:** Equalization losses [55, 56] and SeeSaw loss [64] reweights the per-class loss by balancing the gradients [55] or number of samples [64].
- **p. 6 / X. Zhou et al - extractive PDF cue:** The overall training objective is L(I) = ( Lrpn + Lreg + Lcls, if I ∈Ddet λLmax-size, if I ∈Dcls where Lrpn, Lreg, Lcls are ...
- **p. 6 / X. Zhou et al - extractive PDF cue:** We then apply the classification loss to its RoI features f ′ for all classes c ∈{ck}K k=1: Limage-box = BCE(Wf ′, c) where BCE(s, ...
- **p. 2 / X. Zhou et al - extractive PDF cue:** We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise other outputs for ...
- **p. 3 / X. Zhou et al - extractive PDF cue:** (b) Prediction-based label assignment Person Sports ball (c) Our non-prediction-based loss Fig.
- **p. 3 / X. Zhou et al - extractive PDF cue:** We show that this loss is both simpler and performs better than prior work. outperforms the previous state-of-the-art OVR-CNN [72] by 5 point with the ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 6 (X. Zhou et al), p. 4 (X. Zhou et al), p. 6 (X. Zhou et al), p. 2 (X. Zhou et al), p. 3 (X. Zhou et al), p. 3 (X. Zhou et al).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | simple, classification, loss, applies, image-level, supervision, proposal, largest, size, supervise, other, outputs, imagelabeled, data | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | simple, classification, loss, applies, image-level, supervision, proposal, largest, size, supervise | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | enables, learn, detectors, classes, would, have, been, impossible, predict, assign | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Equalization, losses, SeeSaw, loss, reweights, per-class, balancing, gradients, number, samples | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / X. Zhou et al - extractive PDF cue:** We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise other outputs for ...
- **p. 5 / 3 Preliminaries - extractive PDF cue:** The second stage takes the object feature and outputs a classification score and a refined box location for each object, sj = Wfj, ˆbj = ...
- **p. 4 / 3 Preliminaries - extractive PDF cue:** We propose a simple way to leverage image supervision to learn object detectors, including for classes without box labels.
- **p. 5 / 3 Preliminaries - extractive PDF cue:** During training, we compose a mini-batch using images from both types of datasets.
- **p. 3 / X. Zhou et al - extractive PDF cue:** We show that this loss is both simpler and performs better than prior work. outperforms the previous state-of-the-art OVR-CNN [72] by 5 point with the ...
- **p. 1 / 1 Introduction - extractive PDF cue:** In this paper, we propose Detector with image classes (Detic) that uses image-level supervision in addition to detection supervision.
- **p. 4 / 3 Preliminaries - extractive PDF cue:** We train object detectors using both object detection and image classification datasets.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Our method completely side-steps the prediction-based label assignment process by supervising the classification sub-problem alone when using classification data. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | MosaicOS [73] handles domain differences between detection and image datasets by mosaic augmentation [4] and proposed a three-stage self-training and finetuning framework. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | We use large scale jittering [15] with input resolution 640×640 and train for a 4× (∼48 LVIS epochs) schedule. | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / X. Zhou et al - extractive PDF cue:** To shorten the experimental cycle and have a good initialization for prediction-based WSOD losses [44, 45], we always first train a converged base-class-only model (4× ...
- **p. 4 / X. Zhou et al - extractive PDF cue:** Instead, we use additional image-labeled data for co-training.
- **p. 7 / 5 Experiments - extractive PDF cue:** We use large scale jittering [15] with input resolution 640×640 and train for a 4× (∼48 LVIS epochs) schedule.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** simple, classification, loss, applies, image-level, supervision, proposal, largest, size, supervise, other, outputs, imagelabeled, data, region, network, extract, object, features, then.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We evaluate Detic on the large-vocabulary object detection dataset LVIS [18]. | p. 7 (5 Experiments), p. 7 (5 Experiments) |
| Global / local decision | Table 11: Ablations of the resolution change. We report mask mAP on the open- vocabulary LVIS following the setting of Table 1. ... | p. 22 (Figure/Table caption), p. 11 (Figure/Table caption) |
| Motion execution / recovery | Table 5: Detic with different classifiers. We vary the classifier used with Detic and observe that it works well with different choices. ... | p. 13 (Figure/Table caption), p. 26 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 5 Experiments - extractive PDF cue:** Following ViLD [17], we remove the labels of 337 rare-class from training and consider them as novel classes in testing.
- **p. 7 / 5 Experiments - extractive PDF cue:** Notation Definition #Images #Classes LVIS-all The original LVIS dataset [18] 100K 1203 LVIS-base LVIS without rare-class annotations 100K 866 IN-21K The original ImageNet-21K dataset [10] ...
- **p. 24 / Figure/Table caption - extractive PDF cue:** Table 12: Comparison between predicted loss and and max-size loss. (a): comparison under different baselines. (b): comparison in customized metrics. G ViLD baseline details The ...
- **p. 21 / Figure/Table caption - extractive PDF cue:** Table 10: LVIS baseline evolution. First row: the configuration from the detectron2 model zoo. The following rows change components one by one. Last row: removing ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Prediction-based vs non-prediction-based methods. We show overall and novel-class mAP on open-vocabulary LVIS [17] (with 866 base classes and 337 novel classes) with ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Open-vocabulary LVIS compared to ViLD [17]. We train our model using their training settings and architecture (MaskRCNN-ResNet50, training from scratch). We report mask ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visualization of the assigned boxes during training. We show all boxes with score > 0.5 in blue and the assigned (selected) box in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (X. Zhou et al), p. 5 (3 Preliminaries), p. 6 (X. Zhou et al), p. 8 (X. Zhou et al), p. 4 (X. Zhou et al), p. 4 (X. Zhou et al), objective p. 4 (X. Zhou et al), p. 6 (X. Zhou et al), p. 6 (X. Zhou et al), p. 2 (X. Zhou et al), p. 3 (X. Zhou et al), p. 3 (X. Zhou et al), temporal p. 2 (X. Zhou et al), p. 3 (2 Related Work), p. 4 (3 Preliminaries), p. 6 (X. Zhou et al), p. 6 (X. Zhou et al), p. 8 (X. Zhou et al).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
