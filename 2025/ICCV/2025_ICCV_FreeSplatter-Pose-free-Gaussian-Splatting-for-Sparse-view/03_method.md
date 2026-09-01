# Method - FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Xu_FreeSplatter_Pose-free_Gaussian_Splatting_for_Sparse-view_3D_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_FreeSplatter_Pose-free_Gaussian_Splatting_for_Sparse-view_3D_Reconstruction_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Training Details), p. 8 (4.5. Applications in 3D AIGC), p. 3 (3.2. Model Architecture), p. 3 (3.2. Model Architecture), p. 4 (3.3. Training Details), p. 4 (3.3. Training Details)): The overall training objective is: \mathca l { L } = \m a thcal {L} _ {\mathrm {render}} + \lambda _\mathrm {a} \cdot \mathcal {L}_\mathrm {align} + \1_\mathrm {t\le T_\mathrm ...

## Method Body Digest

- **p. 5 / 3.3. Training Details - extractive PDF cue:** The overall training objective is: \mathca l { L } = \m a thcal {L} _ {\mathrm {render}} + \lambda _\mathrm {a} \cdot \mathcal {L}_\mathrm ...
- **p. 8 / 4.5. Applications in 3D AIGC - extractive PDF cue:** In our supplementary material (Section 2.4), we provide comprehensive image-to3D generation results across a range of multi-view diffusion models, demonstrating that FreeSplatter achieves superior reconstruction ...
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** As Figure 2 shows, FreeSplatter adopts a transformer architecture inspired by GS-LRM [65].
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** Instead, we directly predict Gaussian locations in the reference frame and enforce pixel alignment through a dedicated loss term to restrict Gaussians to lie on ...
- **p. 4 / 3.3. Training Details - extractive PDF cue:** In our experiments, this pre-training is essential to model's convergence.
- **p. 4 / 3.3. Training Details - extractive PDF cue:** We apply Lpos in the pre-training stage, so that the model learns to predict approximately correct Gaussian positions.
- **p. 5 / 3.3. Training Details - extractive PDF cue:** We focus on reconstructing observed areas and adopt Splatt3R's [42] target-view masking strategy, computing rendering loss only for visible regions to prevent negative training guidance ...
- **p. 5 / 3.3. Training Details - extractive PDF cue:** To provide a more stable geometric supervision, we adopt a pixel-alignment loss to enforce each predicted Gaussian to be aligned with its corresponding pixel through ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** We introduce FreeSplatter, a feed-forward reconstruction framework that jointly predicts pixel-wise Gaussians from uncalibrated sparse-view images and estimates their camera parameters.
- **p. 7 / 0.027 Method - extractive PDF cue:** Qualitative comparisons in Figure 4 reveal superior detail preservation by our method, particularly evident in text rendering (4th column), while competitors exhibit blurring artifacts.
- **p. 2 / 1. Introduction - extractive PDF cue:** Despite their pioneering contributions, their approaches suffer from inefficient volume rendering and limited resolution, hampering training efficiency and scalability to complex scenes.

## Source Evidence Cues

- **p. 5 / 3.3. Training Details - extractive PDF cue:** The overall training objective is: \mathca l { L } = \m a thcal {L} _ {\mathrm {render}} + \lambda _\mathrm {a} \cdot \mathcal {L}_\mathrm ...
- **p. 8 / 4.5. Applications in 3D AIGC - extractive PDF cue:** In our supplementary material (Section 2.4), we provide comprehensive image-to3D generation results across a range of multi-view diffusion models, demonstrating that FreeSplatter achieves superior reconstruction ...
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** As Figure 2 shows, FreeSplatter adopts a transformer architecture inspired by GS-LRM [65].
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** Instead, we directly predict Gaussian locations in the reference frame and enforce pixel alignment through a dedicated loss term to restrict Gaussians to lie on ...
- **p. 4 / 3.3. Training Details - extractive PDF cue:** In our experiments, this pre-training is essential to model's convergence.
- **p. 4 / 3.3. Training Details - extractive PDF cue:** We apply Lpos in the pre-training stage, so that the model learns to predict approximately correct Gaussian positions.
- **p. 5 / 3.3. Training Details - extractive PDF cue:** We focus on reconstructing observed areas and adopt Splatt3R's [42] target-view masking strategy, computing rendering loss only for visible regions to prevent negative training guidance ...
- **Detected method headings:** 3. Method (p. 3); 3.2. Model Architecture (p. 3); Method (p. 7); 0.027 Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The overall training objective is: \mathca l { L } = \m a thcal {L} _ {\mathrm {render}} + \lambda _\mathrm {a} ... | p. 5 (3.3. Training Details), p. 8 (4.5. Applications in 3D AIGC) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In our supplementary material (Section 2.4), we provide comprehensive image-to3D generation results across a range of multi-view diffusion models, demonstrating that FreeSplatter ... | p. 8 (4.5. Applications in 3D AIGC), p. 3 (3.2. Model Architecture) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | As Figure 2 shows, FreeSplatter adopts a transformer architecture inspired by GS-LRM [65]. | p. 3 (3.2. Model Architecture), p. 3 (3.2. Model Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Training Details - extractive PDF cue:** The overall training objective is: \mathca l { L } = \m a thcal {L} _ {\mathrm {render}} + \lambda _\mathrm {a} \cdot \mathcal {L}_\mathrm ...
- **p. 5 / 3.3. Training Details - extractive PDF cue:** To provide a more stable geometric supervision, we adopt a pixel-alignment loss to enforce each predicted Gaussian to be aligned with its corresponding pixel through ...
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** Instead, we directly predict Gaussian locations in the reference frame and enforce pixel alignment through a dedicated loss term to restrict Gaussians to lie on ...
- **p. 4 / 3.3. Training Details - extractive PDF cue:** Prior pose-dependent LRMs leverage pure rendering loss for supervision [23, 29, 58, 65].
- **p. 4 / 3.3. Training Details - extractive PDF cue:** While sharing architectural elements and parameter scale, these variants employ distinct training objectives and strategies.
- **p. 7 / 0.027 Method - extractive PDF cue:** This disparity can be attributed to PF-LRM's GSO evaluation images being rendered under identical conditions (e.g., light intensity, camera distribution) as their training data, whereas ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.3. Training Details), p. 3 (3.2. Model Architecture), p. 4 (3.3. Training Details), p. 4 (3.3. Training Details), p. 5 (3.3. Training Details), p. 7 (0.027 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Input, Images, Ours, Render, pred, poses, PF-LRM, Novel, supplementary, material, Section, provide, comprehensive, image-to3D | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Input, Images, Ours, Render, pred, poses, PF-LRM, Novel, supplementary, material | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, FreeSplatter, feed-forward, reconstruction, framework, jointly, predicts, pixel-wise, Gaussians, uncalibrated | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | overall, training, objective, mathca, thcal, mathrm, render, lambda, cdot, mathcal | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Model Architecture - extractive PDF cue:** Input Images Ours (Render w/ pred. poses) PF-LRM (Render w/ pred. poses) Novel G.T.
- **p. 8 / 4.5. Applications in 3D AIGC - extractive PDF cue:** In our supplementary material (Section 2.4), we provide comprehensive image-to3D generation results across a range of multi-view diffusion models, demonstrating that FreeSplatter achieves superior reconstruction ...
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** The model processes N input images  In ∈RH×W ×3 / n = 1, . . . , N
- **p. 3 / 3. Method - extractive PDF cue:** Given N input images {In / n = 1, . . . , N} without known camera parameters, FreeSplatter performs joint scene reconstruction and camera ...
- **p. 5 / 3.3. Training Details - extractive PDF cue:** Sparse-view Reconstruction on GSO dataset. * indicates that ground truth camera poses are used as input. at other pixels remain unconstrained.
- **p. 5 / 3.3. Training Details - extractive PDF cue:** (ii) For Method GSO OmniObject3D PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Evaluate renderings at G.T. novel-view poses PF-LRM 25.08 ...
- **p. 7 / 4.3. Camera Pose Estimation - extractive PDF cue:** For all of our evaluation datasets, we benchmark against MASt3R, the current state-of-the-art in zero-shot multi-view pose estimation.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Specifically, we take the first image as the reference view and predict all Gaussian in its camera frame. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Compared to NeRF's computationally intensive volume rendering, 3DGS achieves comparable visual quality with significantly reduced computational and memory requirements. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Compared to NeRF's computationally intensive volume rendering, 3DGS achieves comparable visual quality with significantly reduced computational and memory requirements. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For input images {In / n = 1, . . . , N}, the model patchifies them into tokens {en,m / n ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Training Details - extractive PDF cue:** The overall training objective is: \mathca l { L } = \m a thcal {L} _ {\mathrm {render}} + \lambda _\mathrm {a} \cdot \mathcal {L}_\mathrm ...
- **p. 4 / 3.3. Training Details - extractive PDF cue:** In our experiments, this pre-training is essential to model's convergence.
- **p. 4 / 3.3. Training Details - extractive PDF cue:** We apply Lpos in the pre-training stage, so that the model learns to predict approximately correct Gaussian positions.
- **p. 5 / 3.3. Training Details - extractive PDF cue:** We focus on reconstructing observed areas and adopt Splatt3R's [42] target-view masking strategy, computing rendering loss only for visible regions to prevent negative training guidance ...
- **p. 7 / 0.027 Method - extractive PDF cue:** Due to the lack of code, we benchmark against PF-LRM using their provided evaluation datasets and inference results.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** overall, training, objective, mathca, thcal, mathrm, render, lambda, cdot, mathcal, align, label, loss, where, rendering, Lrender, combination, MSE, LPIPS, Tmax.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. Model Architecture (p. 3); Method (p. 7); 0.027 Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | FreeSplatterS leverages a diverse training set comprising BlendedMVS [61], ScanNet++[62], and CO3Dv2[37]-a subset of DUSt3R's [51] training data encompassing outdoor scenes, indoor ... | p. 5 (4.1. Experimental Settings), p. 5 (4. Experiments) |
| Semantic / temporal fusion | Prior pose-free object reconstruction approaches like LEAP [26] exhibits limited generalization due to its small-scale training, while PF-LRM [49] is highly relevant ... | p. 6 (4.2. Sparse-view Reconstruction), p. 5 (4.1. Experimental Settings) |
| Robot query / planning handoff | Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using ... | p. 8 (Figure/Table caption), p. 5 (4. Experiments) |

## Failure and Ablation Link

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. FreeSplatter Pipeline. Given N uncalibrated input views without any known camera extrinsics or intrinsics, we first patchify each image into tokens and feed ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. Ablation Study on Pixel-alignment Loss. The results on GSO and ScanNet++ are evaluated with FreeSplatter-O and FreeSplatter-S, respectively. Number of Input Views. We ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation and ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Sparse-view Reconstruction on Object-centric and Scene-level Datasets. We did not test pixelSplat/MVSplat on CO3Dv2 due to the significant domain gap. * indicates that ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Sparse-view Reconstruction on PF-LRM's Evaluation Datasets. FreeSplatter-O synthesizes significantly better visual details than PF-LRM. The 1st row is from the GSO dataset, while ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Sparse-view Reconstruction on GSO dataset. * indi- cates that ground truth camera poses are used as input. at other pixels remain unconstrained. Besides, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.3. Training Details), p. 8 (4.5. Applications in 3D AIGC), p. 3 (3.2. Model Architecture), p. 3 (3.2. Model Architecture), p. 4 (3.3. Training Details), p. 4 (3.3. Training Details), objective p. 5 (3.3. Training Details), p. 5 (3.3. Training Details), p. 3 (3.2. Model Architecture), p. 4 (3.3. Training Details), p. 4 (3.3. Training Details), p. 7 (0.027 Method), temporal p. 3 (3.2. Model Architecture), p. 3 (3.1. Preliminary), p. 4 (3.2. Model Architecture), p. 5 (3.3. Training Details), p. 8 (4.4. Ablation Studies), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
