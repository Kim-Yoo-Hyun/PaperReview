# Method - Digging Into Self-Supervised Monocular Depth Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1806.01260; PDF retrieval source: https://arxiv.org/pdf/1806.01260. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 5 (3.3. Additional Considerations), p. 3 (3.1. Self-Supervised Training), p. 4 (3.2. Improved Self-Supervised Depth Estimation), p. 5 (3.3. Additional Considerations), p. 4 (3.1. Self-Supervised Training)): We first review the key ideas behind self-supervised training for monocular depth estimation, and then describe our depth estimation network and joint training loss.

## Method Body Digest

- **p. 3 / 3. Method - extractive PDF cue:** We first review the key ideas behind self-supervised training for monocular depth estimation, and then describe our depth estimation network and joint training loss.
- **p. 5 / 3.3. Additional Considerations - extractive PDF cue:** Our depth estimation network is based on the general U-Net architecture [53], i.e. an encoder-decoder network, with skip connections, enabling us to represent both deep ...
- **p. 3 / 3.1. Self-Supervised Training - extractive PDF cue:** By constraining the network to perform image synthesis using an intermediary variable, in our case depth or disparity, we can then extract this interpretable depth ...
- **p. 4 / 3.2. Improved Self-Supervised Depth Estimation - extractive PDF cue:** To close this gap, we propose several improvements that significantly increase predicted depth quality, without adding additional model components that also require training (see Fig.
- **p. 5 / 3.3. Additional Considerations - extractive PDF cue:** We use a ResNet18 [17] as our encoder, which contains 11M parameters, compared to the larger, and slower, DispNet and ResNet50 models used in existing ...
- **p. 4 / 3.1. Self-Supervised Training - extractive PDF cue:** For monocular training, we use the two frames temporally adjacent to It as our source frames, i.e.
- **p. 7 / 4.2. Additional Datasets - extractive PDF cue:** Like [1], we use these instead of the reprojected LIDAR scans to compare our method against several existing baseline algorithms, still showing superior performance.
- **p. 5 / 3.2. Improved Self-Supervised Depth Estimation - extractive PDF cue:** Multi-scale Estimation Due to the gradient locality of the bilinear sampler [21], and to prevent the training objective getting stuck in local minima, existing models ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our method succeeds here where others, and our baseline with our contributions turned off, fail. motion is observed in monocular training.
- **p. 1 / 1. Introduction - extractive PDF cue:** We propose three architectural and loss innovations that combined, lead to large improvements in monocular depth estimation when training with monocular video, stereo pairs, or ...
- **p. 4 / 3.2. Improved Self-Supervised Depth Estimation - extractive PDF cue:** We propose an improvement that deals with both issues Figure 5.

## Source Evidence Cues

- **p. 3 / 3. Method - extractive PDF cue:** We first review the key ideas behind self-supervised training for monocular depth estimation, and then describe our depth estimation network and joint training loss.
- **p. 5 / 3.3. Additional Considerations - extractive PDF cue:** Our depth estimation network is based on the general U-Net architecture [53], i.e. an encoder-decoder network, with skip connections, enabling us to represent both deep ...
- **p. 3 / 3.1. Self-Supervised Training - extractive PDF cue:** By constraining the network to perform image synthesis using an intermediary variable, in our case depth or disparity, we can then extract this interpretable depth ...
- **p. 4 / 3.2. Improved Self-Supervised Depth Estimation - extractive PDF cue:** To close this gap, we propose several improvements that significantly increase predicted depth quality, without adding additional model components that also require training (see Fig.
- **p. 5 / 3.3. Additional Considerations - extractive PDF cue:** We use a ResNet18 [17] as our encoder, which contains 11M parameters, compared to the larger, and slower, DispNet and ResNet50 models used in existing ...
- **p. 4 / 3.1. Self-Supervised Training - extractive PDF cue:** For monocular training, we use the two frames temporally adjacent to It as our source frames, i.e.
- **p. 7 / 4.2. Additional Datasets - extractive PDF cue:** Like [1], we use these instead of the reprojected LIDAR scans to compare our method against several existing baseline algorithms, still showing superior performance.
- **Detected method headings:** 3. Method (p. 3); Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We first review the key ideas behind self-supervised training for monocular depth estimation, and then describe our depth estimation network and joint ... | p. 3 (3. Method), p. 5 (3.3. Additional Considerations) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Our depth estimation network is based on the general U-Net architecture [53], i.e. an encoder-decoder network, with skip connections, enabling us to ... | p. 5 (3.3. Additional Considerations), p. 3 (3.1. Self-Supervised Training) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | By constraining the network to perform image synthesis using an intermediary variable, in our case depth or disparity, we can then extract ... | p. 3 (3.1. Self-Supervised Training), p. 4 (3.2. Improved Self-Supervised Depth Estimation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Improved Self-Supervised Depth Estimation - extractive PDF cue:** Multi-scale Estimation Due to the gradient locality of the bilinear sampler [21], and to prevent the training objective getting stuck in local minima, existing models ...
- **p. 3 / 3.1. Self-Supervised Training - extractive PDF cue:** Similar to [12, 15, 76], we also formulate our problem as the minimization of a photometric reprojection error at training time.
- **p. 3 / 3.1. Self-Supervised Training - extractive PDF cue:** We predict a dense depth map Dt that minimizes the photometric reprojection error Lp, where Lp = X t′ pe(It, It′→t), (1) and It′→t = ...
- **p. 4 / 3.2. Improved Self-Supervised Depth Estimation - extractive PDF cue:** 4 for an example of this loss in practice.
- **p. 4 / 3.1. Self-Supervised Training - extractive PDF cue:** Benefit of min. reprojection loss in MS training.
- **p. 5 / 3.2. Improved Self-Supervised Depth Estimation - extractive PDF cue:** µ prevents the pixels which remain stationary in the image from contaminating the loss.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.2. Improved Self-Supervised Depth Estimation), p. 4 (3.1. Self-Supervised Training), p. 4 (3.2. Improved Self-Supervised Depth Estimation), p. 3 (3. Method), p. 5 (3.2. Improved Self-Supervised Depth Estimation), p. 6 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | typically, involves, training, pose, estimation, network, takes, finite, sequence, frames, input, outputs, corresponding, camera | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | typically, involves, training, pose, estimation, network, takes, finite, sequence, frames | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | succeeds, here, where, others, baseline, contributions, turned, fail, motion, observed | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Multi-scale, Estimation, Due, gradient, locality, bilinear, sampler, prevent, training, objective | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** This typically involves training a pose estimation network that takes a finite sequence of frames as input, and outputs the corresponding camera transformations.
- **p. 5 / 3.3. Additional Considerations - extractive PDF cue:** Our models are implemented in PyTorch [46], trained for 20 epochs using Adam [26], with a batch size of 12 and an input/output resolution of ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Estimating absolute, or even relative depth, seems ill-posed without a second input image to enable triangulation.
- **p. 3 / 3. Method - extractive PDF cue:** Here, we describe our depth prediction network that takes a single color input It and produces a depth map Dt.
- **p. 5 / 3.2. Improved Self-Supervised Depth Estimation - extractive PDF cue:** This effectively constrains the depth maps at each scale to work toward the same objective i.e. reconstructing the high resolution input target image as accurately ...
- **p. 7 / 4.2. Additional Datasets - extractive PDF cue:** However, caution should be taken with Make3D, as its ground truth depth and input images are not well aligned, causing potential evaluation issues.
- **p. 7 / Method - extractive PDF cue:** While some other monocular depth prediction works have elected not to use ImageNet pretraining, we show in Table 1 that even without pretraining, we still ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | However, occlusions and disocclusions result in pixels from the current time step not appearing in both the previous and next frames. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In mixed training (MS), It′ includes the temporally adjacent frames and the opposite stereo view. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We use a learning rate of 10-4 for the first 15 epochs which is then dropped to 10-5 for the remainder. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Method - extractive PDF cue:** We first review the key ideas behind self-supervised training for monocular depth estimation, and then describe our depth estimation network and joint training loss.
- **p. 3 / 3.1. Self-Supervised Training - extractive PDF cue:** By constraining the network to perform image synthesis using an intermediary variable, in our case depth or disparity, we can then extract this interpretable depth ...
- **p. 4 / 3.2. Improved Self-Supervised Depth Estimation - extractive PDF cue:** To close this gap, we propose several improvements that significantly increase predicted depth quality, without adding additional model components that also require training (see Fig.
- **p. 4 / 3.1. Self-Supervised Training - extractive PDF cue:** For monocular training, we use the two frames temporally adjacent to It as our source frames, i.e.
- **p. 3 / 3.1. Self-Supervised Training - extractive PDF cue:** Similar to [12, 15, 76], we also formulate our problem as the minimization of a photometric reprojection error at training time.
- **p. 5 / 3.3. Additional Considerations - extractive PDF cue:** Our models are implemented in PyTorch [46], trained for 20 epochs using Adam [26], with a batch size of 12 and an input/output resolution of ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, review, ideas, behind, self-supervised, training, monocular, depth, estimation, then, describe, network, joint, loss, general, U-Net, architecture, encoder-decoder, skip, connections.
- **Relevant PDF headings:** 3. Method (p. 3); Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | KITTI Depth Prediction Benchmark We also perform experiments on the recently introduced KITTI Depth Prediction Evaluation dataset [59], which features more accurate ... | p. 7 (4.2. Additional Datasets), p. 7 (4.2. Additional Datasets) |
| Semantic / temporal fusion | Figure 12. Additional Wander results. We observe that our model (Ours M) results in fewer visual artifacts when compared to the the ... | p. 17 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen split. ... | p. 7 (Figure/Table caption), p. 5 (4. Experiments) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen split. (a) The baseline ...
- **p. 5 / 4.1. KITTI Eigen Split - extractive PDF cue:** Except in ablation experiments, for training which uses monocular sequences (i.e. monocular and monocular plus stereo) we follow Zhou et al.'s [76] pre-processing to remove ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 9. Qualitative ablation study. We can see that our model with all components added result in the smallest amount of depth artifacts. ‘Baseline (M)' ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 12. Ablation of the effect of pose networks on depth prediction. Results shown are on depth prediction on the KITTI dataset, when trained from ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 10. Effect of post-processing. We observe that post-processing, originally motivated only for stereo training, also brings consistent benefits to all our monocular-trained models. Interestingly, ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 11. Effect of varying resolutions on the KITTI Eigen split. All predicted disparity maps have been resized to the same size for visualization. Our ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 5. Auto-masking. We show auto-masks computed after one epoch, where black pixels are removed from the loss (i.e. µ = 0). The mask prevents ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3. Method), p. 5 (3.3. Additional Considerations), p. 3 (3.1. Self-Supervised Training), p. 4 (3.2. Improved Self-Supervised Depth Estimation), p. 5 (3.3. Additional Considerations), p. 4 (3.1. Self-Supervised Training), objective p. 5 (3.2. Improved Self-Supervised Depth Estimation), p. 3 (3.1. Self-Supervised Training), p. 3 (3.1. Self-Supervised Training), p. 4 (3.2. Improved Self-Supervised Depth Estimation), p. 4 (3.1. Self-Supervised Training), p. 5 (3.2. Improved Self-Supervised Depth Estimation), temporal p. 3 (2.2. Self-supervised Depth Estimation), p. 4 (3.1. Self-Supervised Training), p. 4 (3.1. Self-Supervised Training), p. 5 (4.1. KITTI Eigen Split), p. 5 (3.3. Additional Considerations), p. 6 (Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
