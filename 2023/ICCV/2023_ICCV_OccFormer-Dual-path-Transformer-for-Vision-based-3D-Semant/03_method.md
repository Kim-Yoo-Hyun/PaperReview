# Method - OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.05316; PDF retrieval source: https://arxiv.org/pdf/2304.05316. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Overview), p. 2 (3.1. Overview), p. 2 (3.1. Overview), p. 3 (3.2. Dual-path Transformer Encoder), p. 4 (3.3. Transformer Occupancy Decoder), p. 4 (3.3. Transformer Occupancy Decoder)): The pipeline consists of the image encoder for extracting multi-scale 2D features, the image-to-3D transformation for lifting the 2D features to 3D volumes, and the transformer-based encoder-decoder for obtaining 3D ...

## Method Body Digest

- **p. 3 / 3.1. Overview - extractive PDF cue:** The pipeline consists of the image encoder for extracting multi-scale 2D features, the image-to-3D transformation for lifting the 2D features to 3D volumes, and the ...
- **p. 2 / 3.1. Overview - extractive PDF cue:** The image encoder consists of a backbone network for extracting multi-scale features and a neck for further fusion.
- **p. 2 / 3.1. Overview - extractive PDF cue:** With the monocular image or multi-camera images as the input, the multi-scale features are first extracted by the image encoder, and then lifted to 3D ...
- **p. 3 / 3.2. Dual-path Transformer Encoder - extractive PDF cue:** To pursue long-range, dynamic, and efficient processing of the 3D feature volumes, we propose the dual-path transformer block to build the 3D encoder.
- **p. 4 / 3.3. Transformer Occupancy Decoder - extractive PDF cue:** With the above interactions, each processed feature volume is enhanced by the multi-scale semantic information, which facilitates the following transformer decoder.
- **p. 4 / 3.3. Transformer Occupancy Decoder - extractive PDF cue:** The self-attention is then conducted to exchange context information, followed by the FFN for feature projection.
- **p. 5 / 3.3. Transformer Occupancy Decoder - extractive PDF cue:** More specifically, we first compute the class frequencies nc ∈RNc from the training set, where Nc is the number of classes.
- **p. 5 / 3.4. Loss Functions - extractive PDF cue:** The matching cost includes the class loss and the binary mask loss.

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** For the encoder part, we propose the dual-path transformer block to unleash the capacity of selfattention while limiting the quadratic complexity.
- **p. 2 / 3.1. Overview - extractive PDF cue:** The image encoder consists of a backbone network for extracting multi-scale features and a neck for further fusion.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our method surpasses TPVFormer by 1.4% mIoU and generates more complete and realistic predictions for 3D semantic occupancy prediction.

## Source Evidence Cues

- **p. 3 / 3.1. Overview - extractive PDF cue:** The pipeline consists of the image encoder for extracting multi-scale 2D features, the image-to-3D transformation for lifting the 2D features to 3D volumes, and the ...
- **p. 2 / 3.1. Overview - extractive PDF cue:** The image encoder consists of a backbone network for extracting multi-scale features and a neck for further fusion.
- **p. 2 / 3.1. Overview - extractive PDF cue:** With the monocular image or multi-camera images as the input, the multi-scale features are first extracted by the image encoder, and then lifted to 3D ...
- **p. 3 / 3.2. Dual-path Transformer Encoder - extractive PDF cue:** To pursue long-range, dynamic, and efficient processing of the 3D feature volumes, we propose the dual-path transformer block to build the 3D encoder.
- **p. 4 / 3.3. Transformer Occupancy Decoder - extractive PDF cue:** With the above interactions, each processed feature volume is enhanced by the multi-scale semantic information, which facilitates the following transformer decoder.
- **p. 4 / 3.3. Transformer Occupancy Decoder - extractive PDF cue:** The self-attention is then conducted to exchange context information, followed by the FFN for feature projection.
- **p. 5 / 3.3. Transformer Occupancy Decoder - extractive PDF cue:** More specifically, we first compute the class frequencies nc ∈RNc from the training set, where Nc is the number of classes.
- **Detected method headings:** 3. Approach (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The pipeline consists of the image encoder for extracting multi-scale 2D features, the image-to-3D transformation for lifting the 2D features to 3D ... | p. 3 (3.1. Overview), p. 2 (3.1. Overview) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The image encoder consists of a backbone network for extracting multi-scale features and a neck for further fusion. | p. 2 (3.1. Overview), p. 2 (3.1. Overview) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | With the monocular image or multi-camera images as the input, the multi-scale features are first extracted by the image encoder, and then ... | p. 2 (3.1. Overview), p. 3 (3.2. Dual-path Transformer Encoder) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Loss Functions - extractive PDF cue:** The matching cost includes the class loss and the binary mask loss.
- **p. 5 / 3.4. Loss Functions - extractive PDF cue:** With the optimal matching computed by the Hungarian algorithm [23], the mask classification loss Lmask-cls is computed following the matching cost.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions), p. 4 (3.3. Transformer Occupancy Decoder).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | output, image, encoder, fused, feature, input, resolution, Transformer, Occupancy, Decoder, Depth, Distribution, Voxel, Pooling | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | output, image, encoder, fused, feature, input, resolution, Transformer, Occupancy, Decoder | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | encoder, part, dual-path, transformer, block, unleash, capacity, selfattention, while, limiting | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | matching, cost, includes, class, loss, binary, mask, optimal, computed, Hungarian | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3.1. Overview - extractive PDF cue:** The output of the image encoder is one fused feature map with 1 16 of the input resolution.
- **p. 3 / 3.1. Overview - extractive PDF cue:** Input Image Image Encoder Transformer Occupancy Decoder Depth Distribution Voxel Pooling Depth Net Context Net 3D Feature Volume Masked Attention Query Features Mask Context Feature ...
- **p. 1 / 1. Introduction - extractive PDF cue:** With the multiview camera images as input, various attempts for 2D-to3D transformation [40, 31, 20, 29] have been proposed for applications including 3D object detection ...
- **p. 2 / 3.1. Overview - extractive PDF cue:** With the monocular image or multi-camera images as the input, the multi-scale features are first extracted by the image encoder, and then lifted to 3D ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The task of 3D semantic occupancy prediction aims to reconstruct the surrounding 3D environment with finegrained geometry and semantics, which is also known as 3D ...
- **p. 3 / 3.2. Dual-path Transformer Encoder - extractive PDF cue:** Next, the dual-path outputs are fused through the sigmoid-weighted summation.
- **p. 4 / 3.3. Transformer Occupancy Decoder - extractive PDF cue:** With the above interactions, each processed feature volume is enhanced by the multi-scale semantic information, which facilitates the following transformer decoder.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Each sequence lasts for around 20 seconds and the key-frames are annotated at 2Hz with 3D bounding boxes. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The learning rate is decayed by a multi-step scheduler. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Each sequence lasts for around 20 seconds and the key-frames are annotated at 2Hz with 3D bounding boxes. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Transformer Occupancy Decoder - extractive PDF cue:** More specifically, we first compute the class frequencies nc ∈RNc from the training set, where Nc is the number of classes.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** pipeline, consists, image, encoder, extracting, multi-scale, features, image-to-3D, transformation, lifting, volumes, transformer-based, encoder-decoder, obtaining, semantic, predicting, occupancy, backbone, network, neck.
- **Relevant PDF headings:** 3. Approach (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The SemanticKITTI dataset [2] is based on the popular KITTI Odometry Benchmark [16] and focuses on the semantic scene understanding with LiDAR ... | p. 5 (4.1. Datasets), p. 6 (4.1. Datasets) |
| Semantic / temporal fusion | 3, our method outperforms the only vision-based method TPVFormer and achieves comparable performance with the state-of-the-art LiDAR-based methods. | p. 7 (4.4. Main Results), p. 6 (4.2. Implementation Details) |
| Robot query / planning handoff | The proposed OccFormer outperforms the only vision-based method TPVFormer [21] and achieves comparable performance with LiDAR-based methods. | p. 6 (4.1. Datasets), p. 7 (4.4. Main Results) |

## Failure and Ablation Link

- **p. 7 / 4.5. Ablation Studies - extractive PDF cue:** The ablation is conducted on SemanticKITTI validation set and from three perspectives: the dual-path encoder, the pixel decoder, and the transformer decoder.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation study on the dual-path encoder. Local Global Params GFLOPs IoU↑mIoU↑  74.1M 494.2 36.42
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5: Ablation study on the pixel decoder.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Qualitative results on nuScenes validation set. The leftmost column shows the input surrounding images, the following three columns visualize the LiDAR segmentation from ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 10: Ablation study on augmentations. Image Aug. 3D Aug. IoU↑mIoU↑  36.37 12.72  35.73 12.94  
- **p. 9 / 5. Conclusion - extractive PDF cue:** It indicates that the predicted semantic occupancy from TPVFormer, despite reasonable visualizations, fails to contain accurate 3D positions.
- **p. 7 / 4.4. Main Results - extractive PDF cue:** Note that our method requires only one model to perform both the LiDAR segmentation and the semantic occupancy prediction, while the TPVFormer [21] model trained ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Overview), p. 2 (3.1. Overview), p. 2 (3.1. Overview), p. 3 (3.2. Dual-path Transformer Encoder), p. 4 (3.3. Transformer Occupancy Decoder), p. 4 (3.3. Transformer Occupancy Decoder), objective p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions), temporal p. 6 (4.1. Datasets), p. 6 (4.2. Implementation Details), p. 1 (1. Introduction), p. 1 (Abstract), p. 3 (3.2. Dual-path Transformer Encoder), p. 3 (3.2. Dual-path Transformer Encoder).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
