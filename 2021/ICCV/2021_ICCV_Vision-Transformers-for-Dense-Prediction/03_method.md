# Method - Vision Transformers for Dense Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.13413; PDF retrieval source: https://arxiv.org/pdf/2103.13413. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3. Architecture), p. 4 (3. Architecture), p. 3 (3. Architecture), p. 2 (3. Architecture), p. 2 (3. Architecture), p. 4 (3. Architecture)): We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: Reassemble ˆ D s (t) = (Resamples ◦Concatenate ...

## Method Body Digest

- **p. 3 / 3. Architecture - extractive PDF cue:** We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: Reassemble ˆ D ...
- **p. 4 / 3. Architecture - extractive PDF cue:** We use features from the first and second ResNet block from the embedding network and stages l = {9, 12} when using ViT-Hybrid.
- **p. 3 / 3. Architecture - extractive PDF cue:** We use three variants in our work: ViT-Base, which uses the patch-based embedding procedure and features 12 transformer layers; ViT-Large, which uses the same embedding ...
- **p. 2 / 3. Architecture - extractive PDF cue:** Transformers transform the set of tokens using sequential blocks of multi-headed self-attention (MHSA) [39], which relate tokens to each other to transform the representation.
- **p. 2 / 3. Architecture - extractive PDF cue:** We leverage vision transformers [11] as the backbone, show how the representation that is produced by this encoder can be effectively transformed into dense predictions, ...
- **p. 4 / 3. Architecture - extractive PDF cue:** As a set-to-set architecture, the transformer encoder can trivially handle a varying number of tokens.
- **p. 2 / 3. Architecture - extractive PDF cue:** This is in stark contrast to convolutional networks, which progressively increase their receptive field as features pass through consecutive convolution and downsampling layers.
- **p. 3 / 3. Architecture - extractive PDF cue:** The feature representations are progressively fused into the final dense prediction.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In this work, we introduce the dense prediction transformer (DPT).
- **p. 1 / 1. Introduction - extractive PDF cue:** Downsampling enables a progressive increase of the receptive field, the grouping of low-level features into abstract highlevel features, and simultaneously ensures that memory and computational ...
- **p. 3 / 3. Architecture - extractive PDF cue:** We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: Reassemble ˆ D ...

## Source Evidence Cues

- **p. 3 / 3. Architecture - extractive PDF cue:** We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: Reassemble ˆ D ...
- **p. 4 / 3. Architecture - extractive PDF cue:** We use features from the first and second ResNet block from the embedding network and stages l = {9, 12} when using ViT-Hybrid.
- **p. 3 / 3. Architecture - extractive PDF cue:** We use three variants in our work: ViT-Base, which uses the patch-based embedding procedure and features 12 transformer layers; ViT-Large, which uses the same embedding ...
- **p. 2 / 3. Architecture - extractive PDF cue:** Transformers transform the set of tokens using sequential blocks of multi-headed self-attention (MHSA) [39], which relate tokens to each other to transform the representation.
- **p. 2 / 3. Architecture - extractive PDF cue:** We leverage vision transformers [11] as the backbone, show how the representation that is produced by this encoder can be effectively transformed into dense predictions, ...
- **p. 4 / 3. Architecture - extractive PDF cue:** As a set-to-set architecture, the transformer encoder can trivially handle a varying number of tokens.
- **Detected method headings:** 3. Architecture (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: ... | p. 3 (3. Architecture), p. 4 (3. Architecture) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We use features from the first and second ResNet block from the embedding network and stages l = {9, 12} when using ... | p. 4 (3. Architecture), p. 3 (3. Architecture) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We use three variants in our work: ViT-Base, which uses the patch-based embedding procedure and features 12 transformer layers; ViT-Large, which uses ... | p. 3 (3. Architecture), p. 2 (3. Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 3. Architecture - extractive PDF cue:** This is in stark contrast to convolutional networks, which progressively increase their receptive field as features pass through consecutive convolution and downsampling layers.
- **p. 3 / 3. Architecture - extractive PDF cue:** The feature representations are progressively fused into the final dense prediction.
- **p. 3 / 3. Architecture - extractive PDF cue:** Fusion modules (purple) progressively fuse and upsample the representations to generate a fine-grained prediction.
- **p. 4 / 3. Architecture - extractive PDF cue:** We finally combine the extracted feature maps from consecutive stages using a RefineNet-based feature fusion block [23, 45] (see Figure1 (right)) and progressively upsample the ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | simple, three-stage, Reassemble, operation, recover, image-like, representations, output, tokens, arbitrary, layers, transformer, encoder, Resamples | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | simple, three-stage, Reassemble, operation, recover, image-like, representations, output, tokens, arbitrary | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, dense, prediction, transformer, DPT, Downsampling, enables, progressive, increase, receptive | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | stark, contrast, convolutional, networks, progressively, increase, receptive, field, features, pass | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Architecture - extractive PDF cue:** We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: Reassemble ˆ D ...
- **p. 3 / 3. Architecture - extractive PDF cue:** The input tokens are transformed using L transformer layers into new representations tl, where l refers to the output of the l-th transformer layer.
- **p. 1 / 1. Introduction - extractive PDF cue:** Convolutional backbones progressively downsample the input image to extract features at multiple scales.
- **p. 1 / 1. Introduction - extractive PDF cue:** While feature resolution and granularity may not matter for some tasks, such as image classification, they are critical for dense prediction, where the architecture should ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The architecture can also be fine-tuned to small monocular depth prediction datasets, such as NYUv2 [35] and KITTI [15], where it also sets the new ...
- **p. 4 / 3. Architecture - extractive PDF cue:** The final representation size has half the resolution of the input image.
- **p. 4 / 3. Architecture - extractive PDF cue:** However, the position embedding has a dependency on the image size as it encodes the locations of the patches in the input image.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We perform random horizontal flips for data augmentation. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Note that both architectures have similar latency to MiDaS (Table 9). | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Downsampling enables a progressive increase of the receptive field, the grouping of low-level features into abstract highlevel features, and simultaneously ensures that ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We train for 60 epochs, where one epoch consists of 72,000 steps with a batch size of 16. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. Monocular Depth Estimation - extractive PDF cue:** We train for 60 epochs, where one epoch consists of 72,000 steps with a batch size of 16.
- **p. 6 / 4.2. Semantic Segmentation - extractive PDF cue:** We use batch normalization in the fusion layers and train with batch size 48.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** simple, three-stage, Reassemble, operation, recover, image-like, representations, output, tokens, arbitrary, layers, transformer, encoder, Resamples, Concatenate, Read, where, denotes, size, ratio.
- **Relevant PDF headings:** 3. Architecture (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We split each dataset into a training set and a small validation set of about 1,000 images total. | p. 7 (4.3. Ablations), p. 5 (4.1. Monocular Depth Estimation) |
| Semantic / temporal fusion | The hybrid and large backbones consistently outperform the convolutional baselines. | p. 8 (4.3. Ablations), p. 8 (4.3. Ablations) |
| Robot query / planning handoff | Table 3. Evaluation on KITTI (Eigen split). Zero-shot cross-dataset transfer. Table 1 shows the re- sults of zero-shot transfer to different datasets ... | p. 5 (Figure/Table caption), p. 4 (4. Experiments) |

## Failure and Ablation Link

- **p. 4 / 4. Experiments - extractive PDF cue:** We first present our main results using the default configuration and show comprehensive ablations of different DPT configurations at the end of this section.
- **p. 4 / 4.1. Monocular Depth Estimation - extractive PDF cue:** We learn a monocular depth prediction network using a scale- and shift-invariant trimmed loss that operates on an inverse depth representation, together with the gradient-matching ...
- **p. 5 / 4.1. Monocular Depth Estimation - extractive PDF cue:** Both DPT variants significantly outperform the state of the art.
- **p. 5 / 4.1. Monocular Depth Estimation - extractive PDF cue:** Since the network was trained with an affine-invariant loss, its predictions are arbitrarily scaled and shifted and can have large magnitudes.
- **p. 7 / 4.3. Ablations - extractive PDF cue:** We examine a number of aspects and technical choices in DPT via ablation studies.
- **p. 7 / 4.3. Ablations - extractive PDF cue:** We choose monocular depth estimation as the task for our ablations and follow the same protocol and hyper-parameter settings as previously described.
- **p. 8 / 4.3. Ablations - extractive PDF cue:** We finally compare to a recent variant of ViT called DeIT [38].

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3. Architecture), p. 4 (3. Architecture), p. 3 (3. Architecture), p. 2 (3. Architecture), p. 2 (3. Architecture), p. 4 (3. Architecture), objective p. 2 (3. Architecture), p. 3 (3. Architecture), p. 3 (3. Architecture), p. 4 (3. Architecture), temporal p. 5 (4.1. Monocular Depth Estimation), p. 5 (4.1. Monocular Depth Estimation), p. 6 (4.2. Semantic Segmentation), p. 8 (4.3. Ablations), p. 8 (4.3. Ablations), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
