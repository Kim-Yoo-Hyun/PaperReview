# Method - Language-driven Semantic Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.03546; PDF retrieval source: https://arxiv.org/pdf/2201.03546. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (C Input Label Set), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 4 (C Input Label Set)): We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into an embedding space and to ...

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Since the text encoder is trained to embed closely related concepts near one another (for example, "dog" is closer to "pet" than to "vehicle"), we ...
- **p. 4 / C Input Label Set - extractive body cue:** We use an additional post-processing module that spatially regularizes and upsamples the predictions to the original input resolution.
- **p. 1 / ABSTRACT - extractive body cue:** The image encoder is trained with a contrastive objective to align pixel embeddings to the text embedding of the corresponding semantic class.
- **p. 1 / ABSTRACT - extractive body cue:** LSeg uses a text encoder to compute embeddings of descriptive input labels (e.g., "grass" or "building") together with a transformer-based image encoder that computes dense ...
- **p. 4 / C Input Label Set - extractive body cue:** An image encoder extracts per-pixel embeddings from the image and correlates the feature of each pixel to all label embeddings.
- **p. 5 / C Input Label Set - extractive body cue:** During training we freeze the text encoder and only update the weights of the image encoder.
- **p. 4 / C Input Label Set - extractive body cue:** During training, we minimize a per-pixel softmax with cross-entropy loss (with temperature scaling) as is standard in semantic segmentation1.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our approach enables the synthesis of zero-shot semantic segmentation models on the fly.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work, we present a simple approach to leveraging modern language models to increase the flexibility and generality of semantic segmentation models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into ...

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Since the text encoder is trained to embed closely related concepts near one another (for example, "dog" is closer to "pet" than to "vehicle"), we ...
- **p. 4 / C Input Label Set - extractive body cue:** We use an additional post-processing module that spatially regularizes and upsamples the predictions to the original input resolution.
- **p. 1 / ABSTRACT - extractive body cue:** The image encoder is trained with a contrastive objective to align pixel embeddings to the text embedding of the corresponding semantic class.
- **p. 1 / ABSTRACT - extractive body cue:** LSeg uses a text encoder to compute embeddings of descriptive input labels (e.g., "grass" or "building") together with a transformer-based image encoder that computes dense ...
- **p. 4 / C Input Label Set - extractive body cue:** An image encoder extracts per-pixel embeddings from the image and correlates the feature of each pixel to all label embeddings.
- **p. 5 / C Input Label Set - extractive body cue:** During training we freeze the text encoder and only update the weights of the image encoder.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Since the text encoder is trained to embed closely related concepts near one another (for example, "dog" is closer to "pet" than ... | p. 2 (1 INTRODUCTION), p. 4 (C Input Label Set) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We use an additional post-processing module that spatially regularizes and upsamples the predictions to the original input resolution. | p. 4 (C Input Label Set), p. 1 (ABSTRACT) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / C Input Label Set - extractive body cue:** During training, we minimize a per-pixel softmax with cross-entropy loss (with temperature scaling) as is standard in semantic segmentation1.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The main reason for the restricted label sets in existing methods is the cost of annotating images to produce sufficient training data.
- **p. 1 / ABSTRACT - extractive body cue:** The image encoder is trained with a contrastive objective to align pixel embeddings to the text embedding of the corresponding semantic class.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our experiments also show that introducing the text embeddings incurs only a negligible loss in performance when compared to standard fixed-label segmentation methods.
- **p. 4 / C Input Label Set - extractive body cue:** 1In practice we implement this using the standard nn.CrossEntropyLoss from Pytorch.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We further introduce an output module that can spatially regularize the predictions while maintaining this flexibility.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 4 (C Input Label Set), p. 4 (C Input Label Set), p. 1 (1 INTRODUCTION), p. 5 (C Input Label Set).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | state-of-the-art, text, encoders, have, been, co-trained, visual, data, CLIP, embed, labels, training, embedding, space | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | state-of-the-art, text, encoders, have, been, co-trained, visual, data, CLIP, embed | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | enables, synthesis, zero-shot, semantic, segmentation, models, present, simple, leveraging, modern | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | During, training, minimize, per-pixel, softmax, cross-entropy, loss, temperature, scaling, standard | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into ...
- **p. 4 / C Input Label Set - extractive body cue:** In other words, there should be no interactions between the input channels, whose order is defined by the order of the words and can thus ...
- **p. 1 / ABSTRACT - extractive body cue:** LSeg uses a text encoder to compute embeddings of descriptive input labels (e.g., "grass" or "building") together with a transformer-based image encoder that computes dense ...
- **p. 4 / C Input Label Set - extractive body cue:** Assume H × W is the input image size and s is a user-defined downsampling factor (s = 2 in our implementation).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** LSeg is able to output different segmentation maps based on the provided label set.
- **p. 5 / C Input Label Set - extractive body cue:** Existing semantic segmentation models assign a fixed channel in the output to represent the probability of a pixel being the corresponding semantic class.
- **p. 1 / ABSTRACT - extractive body cue:** We present LSeg, a novel model for language-driven semantic image segmentation.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | We follow their official code, training setting and training steps on the basis of their provided model pretrained on ImageNet (Deng et ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Model Backbone Method 200 201 202 203 mean FB-IoU PPNet ResNet50 1-shot 28.1 30.8 29.5 27.7 29.0 - PMM 1-shot 29.3 34.8 ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | Due to memory constraints, the image encoder predicts pixel embeddings at lower resolution than the input image resolution. | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | We follow the same training protocol as on ADE20K and train LSeg with a ViT-L/16 backbone and a ViT-B/32 text encoder for ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Since the text encoder is trained to embed closely related concepts near one another (for example, "dog" is closer to "pet" than to "vehicle"), we ...
- **p. 1 / ABSTRACT - extractive body cue:** The image encoder is trained with a contrastive objective to align pixel embeddings to the text embedding of the corresponding semantic class.
- **p. 5 / C Input Label Set - extractive body cue:** During training we freeze the text encoder and only update the weights of the image encoder.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We follow the same training protocol as on ADE20K and train LSeg with a ViT-L/16 backbone and a ViT-B/32 text encoder for 200 epochs with ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** We follow their official code, training setting and training steps on the basis of their provided model pretrained on ImageNet (Deng et al., 2009).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** state-of-the-art, text, encoders, have, been, co-trained, visual, data, CLIP, embed, labels, training, embedding, space, train, encoder, produce, per-pixel, embeddings, input.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | However, due to a lack of a standardized protocol and sufficient datasets and baselines for the zero-shot setting, we compare LSeg to ... | p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Global / local decision | Our model (with the same ResNet101 backbone) outperforms the zero-shot baseline by a considerable margin across folds and datasets and is even ... | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Motion execution / recovery | We notice that a consistent improvement can be achieved by adding a few regularization blocks. | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We first conduct an ablation study on the two variants of the spatial regularization blocks for cleaning up the output.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** A similar effect is shown in the second row, where LSeg successfully Method Backbone Text Encoder (fixed) embedding dimension pixAcc [%] mIoU [%] LSeg ViT-B/32 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4: Ablation study on the depth of BottleneckBlock and DepthwiseBlock before the last layer. For both Pixel Accuracy (pixAcc) and mIoU, higher is better. ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Note that we train our model on the original label sets that are provided by these datasets without any preprocessing or relabeling.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Going from left to right, labels that are removed between runs are underlined, whereas labels that are added are marked in bold red. segments the ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Example results. LSeg is able to handle unseen labels as well as label sets of arbitrary length and order. This enables flexible synthesis ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** These few-shot methods propose strategies to segment unseen objects based on pretraining on seen categories and finetuning with a few images from the target class.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (C Input Label Set), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 4 (C Input Label Set), objective p. 4 (C Input Label Set), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 4 (C Input Label Set), p. 2 (1 INTRODUCTION), temporal p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 3 (2 RELATED WORK), p. 4 (C Input Label Set), p. 4 (C Input Label Set).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
