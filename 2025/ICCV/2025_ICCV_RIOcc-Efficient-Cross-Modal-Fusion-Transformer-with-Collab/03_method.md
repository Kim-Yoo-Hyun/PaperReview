# Method - RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fan_RIOcc_Efficient_Cross-Modal_Fusion_Transformer_with_Collaborative_Feature_Refinement_for_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fan_RIOcc_Efficient_Cross-Modal_Fusion_Transformer_with_Collaborative_Feature_Refinement_for_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Dual-branch Pooling), p. 5 (3.4.2. Semantic Encoder), p. 6 (3.7. Loss), p. 3 (3.1. Overall Architecture), p. 4 (3.4.2. Semantic Encoder), p. 5 (3.5. Deformable Dual-Attention)): Then, the features are passed through the Channel-wise Attention and Grid-wise Attention modules, optimizing information representation across different dimensions.

## Method Body Digest

- **p. 4 / 3.3. Dual-branch Pooling - extractive PDF cue:** Then, the features are passed through the Channel-wise Attention and Grid-wise Attention modules, optimizing information representation across different dimensions.
- **p. 5 / 3.4.2. Semantic Encoder - extractive PDF cue:** Additionally, we introduce an Auxiliary Semantic Loss at the output stage to enhance the semantic consistency of the features and improve the model's understanding of ...
- **p. 6 / 3.7. Loss - extractive PDF cue:** Additionally, we introduce an Auxiliary Semantic Loss Laux to optimize the refined semantic features extracted by the semantic encoder.
- **p. 3 / 3.1. Overall Architecture - extractive PDF cue:** Then, we design the Deformable Dual-Attention (DDA) to strengthen the interaction of BEV features at different scales between modalities (Sec 3.5).
- **p. 4 / 3.4.2. Semantic Encoder - extractive PDF cue:** To enhance the semantic expressiveness of the BEV features, we propose a lightweight 2D Semantic Encoder for efficiently extracting rich semantic information.
- **p. 5 / 3.5. Deformable Dual-Attention - extractive PDF cue:** After cross-modal interaction, the LiDAR and Camera BEV features are each combined with their respective linear weights and then concatenated.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** During training, we use the AdamW optimizer, set the weight decay to 0.01, and an initial learning rate of 1e-4, with a multi-step learning rate ...
- **p. 6 / 3.7. Loss - extractive PDF cue:** The cross-entropy loss Lce and Lovasz-Softmax loss Lls are used to optimize the overall framework.

## Design Rationale

- **p. 2 / C Vox - extractive PDF cue:** Our contributions are summarized as follows: • We propose a novel multi-modal 3D semantic occupancy prediction framework, RIOcc.
- **p. 2 / C Vox - extractive PDF cue:** To address the aforementioned issues, we propose RIOcc, a novel multi-modal 3D semantic occupancy prediction method.
- **p. 4 / 3.4.2. Semantic Encoder - extractive PDF cue:** To enhance the semantic expressiveness of the BEV features, we propose a lightweight 2D Semantic Encoder for efficiently extracting rich semantic information.

## Source Evidence Cues

- **p. 4 / 3.3. Dual-branch Pooling - extractive PDF cue:** Then, the features are passed through the Channel-wise Attention and Grid-wise Attention modules, optimizing information representation across different dimensions.
- **p. 5 / 3.4.2. Semantic Encoder - extractive PDF cue:** Additionally, we introduce an Auxiliary Semantic Loss at the output stage to enhance the semantic consistency of the features and improve the model's understanding of ...
- **p. 6 / 3.7. Loss - extractive PDF cue:** Additionally, we introduce an Auxiliary Semantic Loss Laux to optimize the refined semantic features extracted by the semantic encoder.
- **p. 3 / 3.1. Overall Architecture - extractive PDF cue:** Then, we design the Deformable Dual-Attention (DDA) to strengthen the interaction of BEV features at different scales between modalities (Sec 3.5).
- **p. 4 / 3.4.2. Semantic Encoder - extractive PDF cue:** To enhance the semantic expressiveness of the BEV features, we propose a lightweight 2D Semantic Encoder for efficiently extracting rich semantic information.
- **p. 5 / 3.5. Deformable Dual-Attention - extractive PDF cue:** After cross-modal interaction, the LiDAR and Camera BEV features are each combined with their respective linear weights and then concatenated.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** During training, we use the AdamW optimizer, set the weight decay to 0.01, and an initial learning rate of 1e-4, with a multi-step learning rate ...
- **Detected method headings:** 3. Method (p. 3); 3.1. Overall Architecture (p. 3); Method (p. 6); 4.3. Comparison with State-of-the-Art Methods (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, the features are passed through the Channel-wise Attention and Grid-wise Attention modules, optimizing information representation across different dimensions. | p. 4 (3.3. Dual-branch Pooling), p. 5 (3.4.2. Semantic Encoder) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Additionally, we introduce an Auxiliary Semantic Loss at the output stage to enhance the semantic consistency of the features and improve the ... | p. 5 (3.4.2. Semantic Encoder), p. 6 (3.7. Loss) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Additionally, we introduce an Auxiliary Semantic Loss Laux to optimize the refined semantic features extracted by the semantic encoder. | p. 6 (3.7. Loss), p. 3 (3.1. Overall Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.7. Loss - extractive PDF cue:** The cross-entropy loss Lce and Lovasz-Softmax loss Lls are used to optimize the overall framework.
- **p. 6 / 3.7. Loss - extractive PDF cue:** Additionally, we introduce an Auxiliary Semantic Loss Laux to optimize the refined semantic features extracted by the semantic encoder.
- **p. 5 / 3.4.2. Semantic Encoder - extractive PDF cue:** Additionally, we introduce an Auxiliary Semantic Loss at the output stage to enhance the semantic consistency of the features and improve the model's understanding of ...
- **p. 4 / 3.3. Dual-branch Pooling - extractive PDF cue:** Then, the features are passed through the Channel-wise Attention and Grid-wise Attention modules, optimizing information representation across different dimensions.
- **p. 5 / 3.5. Deformable Dual-Attention - extractive PDF cue:** For the Camera stream, the input features are tokenized and undergo self-attention, generating updated Qc, Kc, and Vc, which allow for a comprehensive understanding of ...
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** During training, we use the AdamW optimizer, set the weight decay to 0.01, and an initial learning rate of 1e-4, with a multi-step learning rate ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.4.2. Semantic Encoder), p. 6 (3.7. Loss), p. 6 (3.7. Loss), p. 4 (3.3. Dual-branch Pooling), p. 4 (3.3. Dual-branch Pooling), p. 5 (3.5. Deformable Dual-Attention).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | During, feature, extraction, stage, design, LiDAR, camera, branches, encode, multi-modal, input, following, BEVFusion, setup | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | During, feature, extraction, stage, design, LiDAR, camera, branches, encode, multi-modal | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, novel, multi-modal, semantic, occupancy, prediction, framework, RIOcc | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | cross-entropy, loss, Lce, Lovasz-Softmax, Lls, optimize, overall, framework, Additionally, introduce | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. Features Extraction - extractive PDF cue:** During the feature extraction stage, we design LiDAR and camera branches to encode multi-modal input, following the BEVFusion [25] setup.
- **p. 4 / 3.3. Dual-branch Pooling - extractive PDF cue:** The output from the Channel-wise Attention are given by: F_{cha n n el}= \sigma \le ft (M L P\left (F_{A v g}\right )+M L P\left ...
- **p. 3 / 3.1. Overall Architecture - extractive PDF cue:** The framework takes images and LiDAR point clouds as inputs, extracting consistent BEV features for subsequent fusion (Sec 3.2).
- **p. 6 / 3.7. Loss - extractive PDF cue:** Affinity loss Lgeo and Lsem are applied to optimize scene-wise and class-wise metrics, while Ld provides feedback for the depth-aware view transform module.
- **p. 2 / C Vox - extractive PDF cue:** The LiDAR and camera branches respectively extract refined structural information and semantic features, with balanced computational load and performance. • The proposed Deformable Dual-Attention facilitates ...
- **p. 4 / 3.4.2. Semantic Encoder - extractive PDF cue:** The Semantic Encoder first downsamples the input BEV features to capture global contextual information.
- **p. 5 / 3.5. Deformable Dual-Attention - extractive PDF cue:** As shown in Figure 5, the LiDAR BEV features FLiDAR ∈ RH×W ×C and Camera BEV features FCamera ∈RH×W ×C are used as inputs.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We apply Discrete Wavelet Transform (DWT) to the input features F BEV C to obtain low-frequency features Flow and high-frequency features Fhigh ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The framework takes images and LiDAR point clouds as inputs, extracting consistent BEV features for subsequent fusion (Sec 3.2). | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Training is conducted on four NVIDIA 3090 GPUs with a batch size of 4, for a total of 24 epochs. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** During training, we use the AdamW optimizer, set the weight decay to 0.01, and an initial learning rate of 1e-4, with a multi-step learning rate ...
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** Training is conducted on four NVIDIA 3090 GPUs with a batch size of 4, for a total of 24 epochs.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** During training, we use the AdamW optimizer, set the weight decay to 0.01, and an initial learning rate of 1e-4, with a multi-step learning rate ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, features, passed, through, Channel-wise, Attention, Grid-wise, modules, optimizing, information, representation, across, different, dimensions, Additionally, introduce, Auxiliary, Semantic, Loss, output.
- **Relevant PDF headings:** 3. Method (p. 3); 3.1. Overall Architecture (p. 3); Method (p. 6); 4.3. Comparison with State-of-the-Art Methods (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Both datasets inherit the data format of nuScenes, containing 700 training scenes and 150 validation scenes, with annotations for 17 categories. | p. 6 (4.1. Dataset and Metrics), p. 6 (4.1. Dataset and Metrics) |
| Semantic / temporal fusion | In comparison, the data coverage for Occ3D-nuScenes is [-40 m, 40 m] in the X and Y directions, and [-1 m, 5.4 ... | p. 6 (4.1. Dataset and Metrics), p. 1 (Figure/Table caption) |
| Robot query / planning handoff | Figure 1. Comparison between OpenOccupancy and the pro- posed RIOcc. Instead of processing voxel features like OpenOc- cupancy, we choose BEV features ... | p. 1 (Figure/Table caption), p. 3 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 7. Ablation study of the Dual-BEV fusion strategy. representation and improving scene understanding. Feature Alignment on Heatmaps. To demonstrate that our model effectively enhances ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. Ablation Study of Aggregation Region Size. # Strategy mIoU 1 Addition 46.58 2
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** For the camera branch, we use ResNet50 pretrained on ImageNet as the image backbone, and the input image size is cropped to 256×704.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Detailed structure diagram of the wavelet encoder. The input BEV features undergo DWT and IWT to obtain richer structure and details. noise impact, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.3. Dual-branch Pooling), p. 5 (3.4.2. Semantic Encoder), p. 6 (3.7. Loss), p. 3 (3.1. Overall Architecture), p. 4 (3.4.2. Semantic Encoder), p. 5 (3.5. Deformable Dual-Attention), objective p. 6 (3.7. Loss), p. 6 (3.7. Loss), p. 5 (3.4.2. Semantic Encoder), p. 4 (3.3. Dual-branch Pooling), p. 5 (3.5. Deformable Dual-Attention), p. 7 (4.2. Implementation Details), temporal p. 4 (3.4.1. Wavelet Encoder), p. 3 (3.1. Overall Architecture), p. 4 (3.4.1. Wavelet Encoder), p. 5 (3.6. Occupancy Prediction Module), p. 6 (3.7. Loss), p. 6 (3.7. Loss).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
