# Method - Self-Supervised Pretraining of 3D Features on any Point-Cloud

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2101.02691; PDF retrieval source: https://arxiv.org/pdf/2101.02691. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Extension to Multiple 3D Input Formats), p. 4 (3.3. Model Architecture), p. 3 (3. Approach), p. 4 (3.3. Model Architecture), p. 2 (3. Approach), p. 2 (3. Approach)): (2) When the input formats a, b are identical, this objective reduces to the within format loss of Eq 1, and when a̸ = b this objective aligns the feature ...

## Method Body Digest

- **p. 3 / 3.2. Extension to Multiple 3D Input Formats - extractive PDF cue:** (2) When the input formats a, b are identical, this objective reduces to the within format loss of Eq 1, and when a̸ = b ...
- **p. 4 / 3.3. Model Architecture - extractive PDF cue:** We use PointNet++ [67] as the backbone network which takes as input the XYZ coordinates of the 3D data.
- **p. 3 / 3. Approach - extractive PDF cue:** We use format-specific encoders to get spatial features which are pooled and projected to obtain global features v.
- **p. 4 / 3.3. Model Architecture - extractive PDF cue:** Our U-Net consists of four layers of feature extraction and pooling and four layers of feature aggregation and upsampling.
- **p. 2 / 3. Approach - extractive PDF cue:** We develop a scalable pretraining method, DepthContrast, for 3D representations that uses unprocessed singleview or multi-view depth maps without human annotations.
- **p. 2 / 3. Approach - extractive PDF cue:** DepthContrast learns 3D representations across multiple 3D input formats like points and voxels, and 2
- **p. 3 / 3.2. Extension to Multiple 3D Input Formats - extractive PDF cue:** Extending Eq 1, we can minimize a single objective that performs instance discrimination within and across input formats a, b: lab i = -log exp(va⊤ ...
- **p. 4 / 3.5. Implementation Details - extractive PDF cue:** We use a standard SGD optimizer with momentum 0.9, cosine learning rate scheduler [53] starting from 0.12 to 0.00012 and train the model for 1000 ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions can be summarized as follows: • We show that single view 3D depth scans can be used to learn powerful feature representations using ...
- **p. 2 / 3. Approach - extractive PDF cue:** Our method, illustrated in Fig 2, is based on the instance discrimination framework of Wu et al.
- **p. 3 / 3.1. Instance Discrimination - extractive PDF cue:** Our method uses 3D data where X can be represented by point coordinates or voxels1.

## Source Evidence Cues

- **p. 3 / 3.2. Extension to Multiple 3D Input Formats - extractive PDF cue:** (2) When the input formats a, b are identical, this objective reduces to the within format loss of Eq 1, and when a̸ = b ...
- **p. 4 / 3.3. Model Architecture - extractive PDF cue:** We use PointNet++ [67] as the backbone network which takes as input the XYZ coordinates of the 3D data.
- **p. 3 / 3. Approach - extractive PDF cue:** We use format-specific encoders to get spatial features which are pooled and projected to obtain global features v.
- **p. 4 / 3.3. Model Architecture - extractive PDF cue:** Our U-Net consists of four layers of feature extraction and pooling and four layers of feature aggregation and upsampling.
- **p. 2 / 3. Approach - extractive PDF cue:** We develop a scalable pretraining method, DepthContrast, for 3D representations that uses unprocessed singleview or multi-view depth maps without human annotations.
- **p. 2 / 3. Approach - extractive PDF cue:** DepthContrast learns 3D representations across multiple 3D input formats like points and voxels, and 2
- **Detected method headings:** 3. Approach (p. 2); 3.3. Model Architecture (p. 3); B.2.1 Modelnet Classification (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | (2) When the input formats a, b are identical, this objective reduces to the within format loss of Eq 1, and when ... | p. 3 (3.2. Extension to Multiple 3D Input Formats), p. 4 (3.3. Model Architecture) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We use PointNet++ [67] as the backbone network which takes as input the XYZ coordinates of the 3D data. | p. 4 (3.3. Model Architecture), p. 3 (3. Approach) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We use format-specific encoders to get spatial features which are pooled and projected to obtain global features v. | p. 3 (3. Approach), p. 4 (3.3. Model Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.2. Extension to Multiple 3D Input Formats - extractive PDF cue:** Extending Eq 1, we can minimize a single objective that performs instance discrimination within and across input formats a, b: lab i = -log exp(va⊤ ...
- **p. 3 / 3.2. Extension to Multiple 3D Input Formats - extractive PDF cue:** (2) When the input formats a, b are identical, this objective reduces to the within format loss of Eq 1, and when a̸ = b ...
- **p. 4 / 3.5. Implementation Details - extractive PDF cue:** We use a standard SGD optimizer with momentum 0.9, cosine learning rate scheduler [53] starting from 0.12 to 0.00012 and train the model for 1000 ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.2. Extension to Multiple 3D Input Formats), p. 3 (3.1. Instance Discrimination), p. 4 (3.3. Model Architecture).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Inspired, random, crop, images, define, cuboid, augmentation, extracts, cuboids, input, point, cloud, design, makes | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Inspired, random, crop, images, define, cuboid, augmentation, extracts, cuboids, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, single, view, depth, scans, learn, powerful, feature | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Extending, minimize, single, objective, performs, instance, discrimination, within, across, input | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.4. Data Augmentation for 3D - extractive PDF cue:** Inspired by the random crop in 2D images [92], we define a random cuboid augmentation that extracts random cuboids from the input point cloud.
- **p. 3 / 3.1. Instance Discrimination - extractive PDF cue:** Our method, by design, makes minimal assumptions about the input X, i.e., it is an unprocessed single-view depth map.
- **p. 3 / 3. Approach - extractive PDF cue:** Given a depth map we construct two augmented versions using data augmentation and represent them with different input formats (point coordinates and voxels).
- **p. 2 / 3. Approach - extractive PDF cue:** DepthContrast learns 3D representations across multiple 3D input formats like points and voxels, and 2
- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions can be summarized as follows: • We show that single view 3D depth scans can be used to learn powerful feature representations using ...
- **p. 4 / 3.3. Model Architecture - extractive PDF cue:** The network takes a 3D occupancy grid as the input representation of the 3D data.
- **p. 1 / 1. Introduction - extractive PDF cue:** The resulting 3D scene is a point cloud composed of thousands of 3D *Work done during an internship at Facebook.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Following the train/val split from [67], we extract around 190K RGB-D scans (one frame every 15 frames) from about 1200 video sequences ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We finetune the voxel UNet models on segmentation using the framework from Spatio-Temporal Segmentation [17] which uses a UNet backbone network. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Following the train/val split from [67], we extract around 190K RGB-D scans (one frame every 15 frames) from about 1200 video sequences ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 3. Approach - extractive PDF cue:** We develop a scalable pretraining method, DepthContrast, for 3D representations that uses unprocessed singleview or multi-view depth maps without human annotations.
- **p. 4 / 3.5. Implementation Details - extractive PDF cue:** We use a standard SGD optimizer with momentum 0.9, cosine learning rate scheduler [53] starting from 0.12 to 0.00012 and train the model for 1000 ...
- **p. 7 / 4.3. Pretraining with Multiple Input Formats - extractive PDF cue:** We pretrain DepthContrast using both the point and voxel input formats and use two format-specific encoders - PointNet++ for points and UNet for voxels.
- **p. 3 / 3.1. Instance Discrimination - extractive PDF cue:** This allows us to use a large number K of negative samples without increasing the training batch size.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** When, input, formats, identical, objective, reduces, within, format, loss, aligns, feature, representations, obtained, across, different, network, architectures, PointNet, backbone, takes.
- **Relevant PDF headings:** 3. Approach (p. 2); 3.3. Model Architecture (p. 3); B.2.1 Modelnet Classification (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We use diverse downstream datasets - full scenes/object centric; using different 3D sensors; single/multi-view; real/synthetic; indoor/outdoor. | p. 5 (4.1. Transfer Datasets and Tasks), p. 5 (4. Experiments) |
| Semantic / temporal fusion | Table 3: Transfer using state-of-the-art detection frameworks. We use our pretrained model (PointNet++ 3× on Redwood-vid +ScanNet-vid) and transfer it using two ... | p. 5 (Figure/Table caption), p. 5 (4.2. Pretraining with Point Input Format) |
| Robot query / planning handoff | DepthContrast outperforms training from scratch on all the four datasets, and improves performance by 12.1% mAP on the small S3DIS dataset that ... | p. 5 (4.2. Pretraining with Point Input Format), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 4.3. Pretraining with Multiple Input Formats - extractive PDF cue:** To analyze which of these loss terms matter for pretraining, we consider three variants - (1) Within format which independently trains format-specific models for each ...
- **p. 7 / 5.1. Importance of Data Augmentation - extractive PDF cue:** Thus, we analyze the effect of our proposed augmentations from § 3.4 on transfer performance.
- **p. 8 / 5.2. Impact of Single-view or Multi-view 3D Data - extractive PDF cue:** Our self-supervised method does not make assumptions on the input data and can use single-view depth maps without 3D preprocessing as input.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1: Pretraining datasets and transfer tasks used in this paper. We use two different pretraining datasets without post-processing like 3D registration, camera calibration. We ...
- **p. 4 / 4. Experiments - extractive PDF cue:** We evaluate DepthContrast pretraining by transfer learning, i.e., fine-tuning on downstream tasks and datasets.
- **p. 5 / 4.2. Pretraining with Point Input Format - extractive PDF cue:** This suggests that pretraining is crucial for training large 3D detection models.
- **p. 5 / 4.2. Pretraining with Point Input Format - extractive PDF cue:** As a supervised pretraining baseline, we use the VoteNet model trained on ScanNet detection.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.2. Extension to Multiple 3D Input Formats), p. 4 (3.3. Model Architecture), p. 3 (3. Approach), p. 4 (3.3. Model Architecture), p. 2 (3. Approach), p. 2 (3. Approach), objective p. 3 (3.2. Extension to Multiple 3D Input Formats), p. 3 (3.2. Extension to Multiple 3D Input Formats), p. 4 (3.5. Implementation Details), temporal p. 5 (4. Experiments), p. 7 (4.3. Pretraining with Multiple Input Formats), p. 5 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format), p. 7 (4.3. Pretraining with Multiple Input Formats).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
