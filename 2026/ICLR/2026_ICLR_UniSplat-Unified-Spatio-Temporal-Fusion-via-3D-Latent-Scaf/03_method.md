# Method - UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Ng2VDbKD4r; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247830. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 15 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS), p. 15 (A.1 IMPLEMENTATION DETAILS)): To supervise the dynamic attributes of the Gaussians in Gt, we introduce a dynamics rendering mechanism that renders dynamic masks using the standard differentiable 15

## Method Body Digest

- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** To supervise the dynamic attributes of the Gaussians in Gt, we introduce a dynamics rendering mechanism that renders dynamic masks using the standard differentiable 15
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For a fair comparison, evaluation is performed by resizing our model's outputs to 224 × 400, aligning with the baseline's resolution before metric computation.
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For MVSplat, we initialize the model using its official weights pre-trained on RealEstate10K (Zhou et al., 2018).
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** The model is trained in a streaming manner using clips of 20 frames for 20 epochs, with an initial learning rate of 1.5 × 10-4 ...
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** To address the severe class imbalance in the dynamic segmentation loss, we incorporate a negative sampling strategy that randomly selects 50,000 negative pixels per sample ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Due to the patch size constraint of our geometry foundation model, which requires image dimensions to be divisible by 14, we train our model at ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Method FPS↑Mem.(GB)↓Param(M) PSNR↑SSIM↑LPIPS↓ Omin-Scene (Wei et al., 2025) 2.5 8.22 81.7 24.27 0.736 0.237 UniSplat 4.0 8.30 91.0 25.37 0.765 0.246 Gaussian-splatting pipeline, with dynamic ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Experimental results demonstrate that our approach achieves state-of-the-art performance across both datasets in input-view reconstruction and novelview synthesis.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our main contributions are as follows: • We introduce UniSplat, a novel feed-forward framework for dynamic scene reconstruction from multi-camera videos via a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these challenges, we propose UniSplat, a general feed-forward framework for dynamic scene modeling from multi-camera videos.
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** To supervise the dynamic attributes of the Gaussians in Gt, we introduce a dynamics rendering mechanism that renders dynamic masks using the standard differentiable 15

## Source Evidence Cues

- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** To supervise the dynamic attributes of the Gaussians in Gt, we introduce a dynamics rendering mechanism that renders dynamic masks using the standard differentiable 15
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For a fair comparison, evaluation is performed by resizing our model's outputs to 224 × 400, aligning with the baseline's resolution before metric computation.
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For MVSplat, we initialize the model using its official weights pre-trained on RealEstate10K (Zhou et al., 2018).
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** The model is trained in a streaming manner using clips of 20 frames for 20 epochs, with an initial learning rate of 1.5 × 10-4 ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To supervise the dynamic attributes of the Gaussians in Gt, we introduce a dynamics rendering mechanism that renders dynamic masks using the ... | p. 15 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | For a fair comparison, evaluation is performed by resizing our model's outputs to 224 × 400, aligning with the baseline's resolution before ... | p. 16 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | For MVSplat, we initialize the model using its official weights pre-trained on RealEstate10K (Zhou et al., 2018). | p. 16 (A.1 IMPLEMENTATION DETAILS), p. 15 (A.1 IMPLEMENTATION DETAILS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** To address the severe class imbalance in the dynamic segmentation loss, we incorporate a negative sampling strategy that randomly selects 50,000 negative pixels per sample ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Due to the patch size constraint of our geometry foundation model, which requires image dimensions to be divisible by 14, we train our model at ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Method FPS↑Mem.(GB)↓Param(M) PSNR↑SSIM↑LPIPS↓ Omin-Scene (Wei et al., 2025) 2.5 8.22 81.7 24.27 0.736 0.237 UniSplat 4.0 8.30 91.0 25.37 0.765 0.246 Gaussian-splatting pipeline, with dynamic ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 15 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Experimental, demonstrate, achieves, state-of-the-art, performance, across, datasets, input-view, reconstruction, novelview, synthesis, Despite, advances, robust | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Experimental, demonstrate, achieves, state-of-the-art, performance, across, datasets, input-view, reconstruction, novelview | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, main, contributions, follows, introduce, UniSplat, novel, feed-forward, framework, dynamic | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | address, severe, class, imbalance, dynamic, segmentation, loss, incorporate, negative, sampling | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Experimental results demonstrate that our approach achieves state-of-the-art performance across both datasets in input-view reconstruction and novelview synthesis.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Despite these advances, robust reconstruction in urban driving scenarios remains challenging, particularly in maintaining a unified latent representation that evolves smoothly over time, handling partial ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, these methods typically assume substantial viewpoint overlap among input images and rely on perscene optimization, which limits their applicability in real-time driving scenarios.
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For MVSplat, we initialize the model using its official weights pre-trained on RealEstate10K (Zhou et al., 2018).
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For a fair comparison, evaluation is performed by resizing our model's outputs to 224 × 400, aligning with the baseline's resolution before metric computation.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These methods typically encode inter-view correlations within the image domain via cross-attention or by constructing a multi-view stereo (MVS) cost volume, and subsequently decode the ...
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** We employ the SpConv (Contributors, 2022) library to implement the sparse 3D U-Net, which comprises convolutional and transposed convolutional layers and achieves a maximum downsampling ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We then perform a unified spatio-temporal fusion, integrating information across views within the current scaffold and aggregating it with the latent scaffold ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In summary, our main contributions are as follows: • We introduce UniSplat, a novel feed-forward framework for dynamic scene reconstruction from multi-camera ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In summary, our main contributions are as follows: • We introduce UniSplat, a novel feed-forward framework for dynamic scene reconstruction from multi-camera ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All models are trained for 20 epochs with a batch size of 32 on 16 GPUs. | hardware, batch and throughput |

## Training vs Inference

- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For MVSplat, we initialize the model using its official weights pre-trained on RealEstate10K (Zhou et al., 2018).
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** The model is trained in a streaming manner using clips of 20 frames for 20 epochs, with an initial learning rate of 1.5 × 10-4 ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** All models are trained for 20 epochs with a batch size of 32 on 16 GPUs.
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** The model is trained in a streaming manner using clips of 20 frames for 20 epochs, with an initial learning rate of 1.5 × 10-4 ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Training is conducted with a batch size of 16 on 8 H20 GPUs for 40,000 iterations, as further training empirically degrades performance.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For the general methods MVSplat and DepthSplat, we retrain them on the Waymo Open Dataset using their official codebases.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** supervise, dynamic, attributes, Gaussians, introduce, dynamics, rendering, mechanism, renders, masks, standard, differentiable, fair, comparison, evaluation, performed, resizing, model, outputs, aligning.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We conduct experiments on two large-scale autonomous driving benchmarks: Waymo Open (Sun et al., 2020) and nuScenes (Caesar et al., 2020) datasets. | p. 6 (4 EXPERIMENTS), p. 16 (A.2 EFFICIENCY ANALYSIS) |
| Semantic / temporal fusion | UniSplat consistently outperforms all baselines across every metric for both input view reconstruction and novel view synthesis. | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Robot query / planning handoff | As shown in 1st and 2nd rows, the incorporation of spatial scaffold fusion, which aggregates spatial information in 3D space, improves performance ... | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We also compare against a variant that explicitly uses two consecutive frames without latent-space temporal propagation.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 4.3 ABLATION STUDY In this section, we conduct ablation studies on the Waymo Open Dataset (Sun et al., 2020) to investigate the individual components of ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Ablation on Geometric and Semantic Features in Scaffold.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Top: Aggregated scene without dynamic filtering, where red boxes indicate ghosting artifacts caused by accumulating the dynamic car.
- **p. 10 / Figure/Table caption - extractive body cue:** Table 5: Ablation study on the two branches of our Gaussian decoder. Point Voxel PSNR↑SSIM↑LPIPS↓ ✓ 24.62 0.72 0.38
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For DepthSplat, we initialize from its official weights pre-trained on dl3dV (Ling et al., 2024) and use the variant equipped with a ViT-B backbone (Dosovitskiy ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For our 3D scaffold reconstruction, we employ a frozen pretrained geometry transformer π3 (Wang et al., 2025f) for initial geometry generation and a pretrained DINOv2 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 15 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS), p. 15 (A.1 IMPLEMENTATION DETAILS), objective p. 15 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS), temporal p. 3 (2 RELATED WORK), p. 2 (1 INTRODUCTION), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 16 (A.1 IMPLEMENTATION DETAILS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
