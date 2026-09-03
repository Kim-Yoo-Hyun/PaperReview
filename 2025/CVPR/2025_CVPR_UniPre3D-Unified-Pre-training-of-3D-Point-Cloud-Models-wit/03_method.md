# Method - UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 4 (3.2. Overall Pipeline), p. 5 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 5 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 3 (3.2. Overall Pipeline), p. 3 (3.2. Overall Pipeline)): To modulate the difficulty of the pretraining task and enhance the point cloud model's focus on geometry extraction, we propose the integration of pretrained image features with the intermediate 3D ...

## Method Body Digest

- **p. 4 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** To modulate the difficulty of the pretraining task and enhance the point cloud model's focus on geometry extraction, we propose the integration of pretrained image ...
- **p. 4 / 3.2. Overall Pipeline - extractive body cue:** These 2D features are then encoded into the 3D domain using a learnable but lightweight adaptation block A, followed by back-projection to the 3D space, ...
- **p. 5 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** We then treat the back-projected pixels as a pseudo point cloud P2D and merge it with P3D, the output from the first encoding layer of ...
- **p. 5 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** The voxelized Pfuse is then passed through the remaining point cloud model to extract the fused features Ffuse.
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** Based on this observation, we propose using the image domain as an intermediary to reduce the scale differences in point cloud data.
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** To further enhance the scale adaptability, we propose the integration of a pre-trained image model, which provides supplementary color and texture information through our novel ...
- **p. 5 / 3.4. Optimization Objectives - extractive body cue:** We employ a pixel-wise supervision Mean Squared Error (MSE) loss during the pre-training process: \ma thca l
- **p. 3 / 3. Approach - extractive body cue:** Generalizable 3DGS eliminates the need for sample-wise optimization of Gaussian primitive parameters.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In conclusion, the contributions of our paper are as follows: (1) We propose UniPre3D, the first unified pretraining method for point clouds of any scale ...
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** To further enhance the scale adaptability, we propose the integration of a pre-trained image model, which provides supplementary color and texture information through our novel ...
- **p. 2 / 1. Introduction - extractive body cue:** This enables end-toend optimization and allows for precise pixel-wise supervision in the image domain.

## Source Evidence Cues

- **p. 4 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** To modulate the difficulty of the pretraining task and enhance the point cloud model's focus on geometry extraction, we propose the integration of pretrained image ...
- **p. 4 / 3.2. Overall Pipeline - extractive body cue:** These 2D features are then encoded into the 3D domain using a learnable but lightweight adaptation block A, followed by back-projection to the 3D space, ...
- **p. 5 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** We then treat the back-projected pixels as a pseudo point cloud P2D and merge it with P3D, the output from the first encoding layer of ...
- **p. 5 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** The voxelized Pfuse is then passed through the remaining point cloud model to extract the fused features Ffuse.
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** Based on this observation, we propose using the image domain as an intermediary to reduce the scale differences in point cloud data.
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** To further enhance the scale adaptability, we propose the integration of a pre-trained image model, which provides supplementary color and texture information through our novel ...
- **Detected method headings:** 3. Approach (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To modulate the difficulty of the pretraining task and enhance the point cloud model's focus on geometry extraction, we propose the integration ... | p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 4 (3.2. Overall Pipeline) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | These 2D features are then encoded into the 3D domain using a learnable but lightweight adaptation block A, followed by back-projection to ... | p. 4 (3.2. Overall Pipeline), p. 5 (3.3. Scale-Adaptive Cross-Modal Fusion) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We then treat the back-projected pixels as a pseudo point cloud P2D and merge it with P3D, the output from the first ... | p. 5 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 5 (3.3. Scale-Adaptive Cross-Modal Fusion) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Optimization Objectives - extractive body cue:** We employ a pixel-wise supervision Mean Squared Error (MSE) loss during the pre-training process: \ma thca l
- **p. 3 / 3. Approach - extractive body cue:** Generalizable 3DGS eliminates the need for sample-wise optimization of Gaussian primitive parameters.
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** Additionally, generating projected images as the 3D pre-training task offers the advantage of adaptive difficulty.
- **p. 4 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** Appropriately supplementing pretrained image features can facilitate a smoother optimization process, assisting the backbone in gradually mastering the task and preventing premature convergence.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.4. Optimization Objectives).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observation, image, domain, intermediary, reduce, scale, differences, point, cloud, data, modulate, difficulty, pretraining, task | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | observation, image, domain, intermediary, reduce, scale, differences, point, cloud, data | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | conclusion, contributions, follows, UniPre3D, first, unified, pretraining, point, clouds, scale | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | employ, pixel-wise, supervision, Mean, Squared, Error, MSE, loss, during, pre-training | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** Based on this observation, we propose using the image domain as an intermediary to reduce the scale differences in point cloud data.
- **p. 4 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** To modulate the difficulty of the pretraining task and enhance the point cloud model's focus on geometry extraction, we propose the integration of pretrained image ...
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** Our proposed pretraining task involves predicting Gaussian parameters from the input point cloud.
- **p. 4 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** In the context of object pre-training, the input point clouds are devoid of color, while the rendered images are expected to be rich in color.
- **p. 2 / 1. Introduction - extractive body cue:** Since the scale complexity of the projected images aligns with that of the input point cloud, and due to the inherent flexibility of Gaussian primitives, ...
- **p. 5 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** We then treat the back-projected pixels as a pseudo point cloud P2D and merge it with P3D, the output from the first encoding layer of ...
- **p. 5 / 3.4. Optimization Objectives - extractive body cue:** However, in the context of scene pre-training, we impose a restriction on the perspective gap between the reference and rendered images, maintaining it within a ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Object models are pre-trained for 50 epochs with the Adam optimizer [21] and a StepLR learning rate scheduler, set to an initial ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Results for PTv3 on S3DIS are omitted, as the official implementation requires disabling flash-attention, which significantly increases CUDA memory usage beyond the ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Results for PTv3 on S3DIS are omitted, as the official implementation requires disabling flash-attention, which significantly increases CUDA memory usage beyond the ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Object models are pre-trained for 50 epochs with the Adam optimizer [21] and a StepLR learning rate scheduler, set to an initial ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** To modulate the difficulty of the pretraining task and enhance the point cloud model's focus on geometry extraction, we propose the integration of pretrained image ...
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** To further enhance the scale adaptability, we propose the integration of a pre-trained image model, which provides supplementary color and texture information through our novel ...
- **p. 5 / 4.1. Pre-training - extractive body cue:** The model is pre-trained for 100 epochs and the batch size is set to 8, with each point cloud taking eight input images and supervised ...
- **p. 5 / 4.1. Pre-training - extractive body cue:** Object models are pre-trained for 50 epochs with the Adam optimizer [21] and a StepLR learning rate scheduler, set to an initial learning rate of ...
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Furthermore, point fusion proves to be more effective for scene pre-training than feature fusion, with optimal fine-tuning results across all datasets achieved when fusing 2D ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** modulate, difficulty, pretraining, task, enhance, point, cloud, model, focus, geometry, extraction, integration, pretrained, image, features, intermediate, derived, backbone, then, encoded.
- **Relevant PDF headings:** 3. Approach (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For scene-level pre-training, we utilize the real-world ScanNetV2 dataset [10] with more than 1,500 scans of indoor scenes. | p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning) |
| Semantic / temporal fusion | Additionally, we use the advanced PointTransformerV3 [59] as the backbone, which demonstrates significantly higher baseline performance than SparseUNet, to show that UniPre3D ... | p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning) |
| Robot query / planning handoff | For part segmentation in Table 2, UniPre3D achieves the best performance on the mIoUC metric and competitive results with TAP on mIoUI. | p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning) |

## Failure and Ablation Link

- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Furthermore, point fusion proves to be more effective for scene pre-training than feature fusion, with optimal fine-tuning results across all datasets achieved when fusing 2D ...
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** The ablation results confirm our findings from object pre-training, that supplementary image knowledge is essential for enhancing our pre-training pipeline, particularly on the challenging long-tail ...
- **p. 5 / 4.1. Pre-training - extractive body cue:** For object-level pre-training, we begin with the standard Transformer architecture [48], ensuring a fair comparison with previous MAE-based pretraining methods [24, 31, 40, 67].
- **p. 6 / 4.2.2. Scene-level Fine-tuning - extractive body cue:** When fine-tuning on scene-level segmentation, we first assess the pre-training dataset itself, ScanNetV2 [10], which comprises 20 classes.
- **p. 6 / 4.2.2. Scene-level Fine-tuning - extractive body cue:** Subsequently, we fine-tune on the ScanNet200 [43] dataset, which shares the same 2D and 3D data with ScanNetV2 but features more fine-grained annotations covering 200 ...
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** For object-level pre-training, we ablate on the integration layer with classification fine-tuning on ScanObjectNN (PB T50 RS), shown in Table 5.
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive body cue:** Model Pre-train mIoUC mIoUI PointNet [34] ✗ 80.4 83.7 PointNet++ [35] ✗ 81.9 85.1 DGCNN [55] ✗ 82.3 85.2 KPConv [45] ✗ 85.1 86.4 Standard ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 4 (3.2. Overall Pipeline), p. 5 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 5 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 3 (3.2. Overall Pipeline), p. 3 (3.2. Overall Pipeline), objective p. 5 (3.4. Optimization Objectives), p. 3 (3. Approach), p. 3 (3.2. Overall Pipeline), p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion), temporal p. 5 (4.1. Pre-training), p. 7 (4.2.2. Scene-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 2 (2. Related Work), p. 2 (2. Related Work), p. 3 (3.2. Overall Pipeline).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
