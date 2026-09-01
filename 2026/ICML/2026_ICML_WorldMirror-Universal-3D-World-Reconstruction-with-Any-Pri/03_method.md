# Method - WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=HFNJOpXHfm; PDF retrieval source: https://openreview.net/pdf/d37648c3826e3031b270765b6a36790ab19140f8.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Unified Spatial Prediction), p. 4 (3.2. Unified Spatial Prediction), p. 3 (3. Method), p. 5 (3.2. Unified Spatial Prediction), p. 3 (3.1. Multi-modal Tokenization), p. 5 (3.2. Unified Spatial Prediction)): To address these issues, we introduce a decoupled modeling strategy that separates geometry prediction from appearance reconstruction, along with a curriculum learning scheme that progressively balances task difficulties during training.

## Method Body Digest

- **p. 4 / 3.2. Unified Spatial Prediction - extractive PDF cue:** To address these issues, we introduce a decoupled modeling strategy that separates geometry prediction from appearance reconstruction, along with a curriculum learning scheme that progressively ...
- **p. 4 / 3.2. Unified Spatial Prediction - extractive PDF cue:** Inspired by the architecture used in VGGT (Wang et al., 2025a), we construct a Transformer backbone with a global-local attention mechanism and multi-head decoders for ...
- **p. 3 / 3. Method - extractive PDF cue:** 3.2), a multi-task architecture with curriculum learning that produces comprehensive geometric outputs, including point maps, camera poses, depth maps, surface normals, and 3D Gaussians.
- **p. 5 / 3.2. Unified Spatial Prediction - extractive PDF cue:** We then incorporate the normal prediction task into the joint training scheme.
- **p. 3 / 3.1. Multi-modal Tokenization - extractive PDF cue:** Below, we describe tokenization for each modality, followed by merging and training strategies for inference with any available priors.
- **p. 5 / 3.2. Unified Spatial Prediction - extractive PDF cue:** Camera Pose Estimation on RealEstate10K, Sintel, and TUM-dynamics.
- **p. 6 / 4. Model Training - extractive PDF cue:** A.1 for the details of training losses and the specific values of these weights.
- **p. 5 / 4. Model Training - extractive PDF cue:** Our model is trained end-to-end by minimizing a composite loss function L that integrates supervision for all prediction 5

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** We summarize our contributions as follows: (1) We present WorldMirror, a unified end-to-end framework for 3D geometry that jointly addresses flexible prior conditioning and comprehensive ...
- **p. 2 / 1. Introduction - extractive PDF cue:** (3) We introduce a Unified Spatial Prediction architecture with a decoupled sequential training that effectively coordinates multi-task training across camera poses, depth, normals, point maps, ...
- **p. 3 / 3. Method - extractive PDF cue:** We introduce two core components: (1) Multi-modal Tokenization (Sec.

## Source Evidence Cues

- **p. 4 / 3.2. Unified Spatial Prediction - extractive PDF cue:** To address these issues, we introduce a decoupled modeling strategy that separates geometry prediction from appearance reconstruction, along with a curriculum learning scheme that progressively ...
- **p. 4 / 3.2. Unified Spatial Prediction - extractive PDF cue:** Inspired by the architecture used in VGGT (Wang et al., 2025a), we construct a Transformer backbone with a global-local attention mechanism and multi-head decoders for ...
- **p. 3 / 3. Method - extractive PDF cue:** 3.2), a multi-task architecture with curriculum learning that produces comprehensive geometric outputs, including point maps, camera poses, depth maps, surface normals, and 3D Gaussians.
- **p. 5 / 3.2. Unified Spatial Prediction - extractive PDF cue:** We then incorporate the normal prediction task into the joint training scheme.
- **p. 3 / 3.1. Multi-modal Tokenization - extractive PDF cue:** Below, we describe tokenization for each modality, followed by merging and training strategies for inference with any available priors.
- **p. 5 / 3.2. Unified Spatial Prediction - extractive PDF cue:** Camera Pose Estimation on RealEstate10K, Sintel, and TUM-dynamics.
- **p. 6 / 4. Model Training - extractive PDF cue:** A.1 for the details of training losses and the specific values of these weights.
- **Detected method headings:** 3. Method (p. 3); 4. Model Training (p. 5); 5.3. Comparison with Prior-guided Methods (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To address these issues, we introduce a decoupled modeling strategy that separates geometry prediction from appearance reconstruction, along with a curriculum learning ... | p. 4 (3.2. Unified Spatial Prediction), p. 4 (3.2. Unified Spatial Prediction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Inspired by the architecture used in VGGT (Wang et al., 2025a), we construct a Transformer backbone with a global-local attention mechanism and ... | p. 4 (3.2. Unified Spatial Prediction), p. 3 (3. Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 3.2), a multi-task architecture with curriculum learning that produces comprehensive geometric outputs, including point maps, camera poses, depth maps, surface normals, and ... | p. 3 (3. Method), p. 5 (3.2. Unified Spatial Prediction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4. Model Training - extractive PDF cue:** Our model is trained end-to-end by minimizing a composite loss function L that integrates supervision for all prediction 5
- **p. 4 / 3.1. Multi-modal Tokenization - extractive PDF cue:** Depth maps, however, are spatially dense; concatenating them would double the token count and incur quadratic attention cost.
- **p. 5 / 3.2. Unified Spatial Prediction - extractive PDF cue:** 5, we find that the gain arises from the 3D geometric consistency constraints imposed by the universal spatial representation.
- **p. 6 / 4. Model Training - extractive PDF cue:** A.1 for the details of training losses and the specific values of these weights.
- **p. 6 / 4. Model Training - extractive PDF cue:** Our approach surpasses baselines in both appearance fidelity and geometric perception. tasks: L = λ1Lpoints + λ2Ldepth + λ3Lcam + λ4Lnormal + λ5L3dgs (3) where ...
- **p. 3 / 3.1. Multi-modal Tokenization - extractive PDF cue:** (1) During training, we randomly drop each of T cam i , T intr i , and T depth i independently with probability 0.5, setting ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4. Model Training), p. 5 (3.2. Unified Spatial Prediction), p. 6 (4. Model Training), p. 6 (4. Model Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Multi-modal, Tokenization, treats, multiple, input, types, including, RGB, images, camera, intrinsics, poses, depth, tokens | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Multi-modal, Tokenization, treats, multiple, input, types, including, RGB, images, camera | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, contributions, follows, present, WorldMirror, unified, end-to-end, framework, geometry, jointly | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | model, trained, end-to-end, minimizing, composite, loss, function, integrates, supervision, prediction | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** (2) We propose Multi-modal Tokenization, which treats multiple input types including RGB images, camera intrinsics, poses, and depth as tokens, enabling seamless integration of these ...
- **p. 3 / 3. Method - extractive PDF cue:** 3.1), which encodes diverse input modalities, including camera intrinsics, poses, and depth maps, into a unified token sequence; and (2) Unified Spatial Prediction (Sec.
- **p. 3 / 3. Method - extractive PDF cue:** 3.2), a multi-task architecture with curriculum learning that produces comprehensive geometric outputs, including point maps, camera poses, depth maps, surface normals, and 3D Gaussians.
- **p. 5 / 3.2. Unified Spatial Prediction - extractive PDF cue:** Moreover, the GS head predicts Gaussian positions independently instead of reusing outputs from the depth or point map heads, enabling the rendering task to autonomously ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Pow3R (Jang et al., 2025) enables prior-conditioned binocular reconstruction but outputs only point maps, while VGGT (Wang et al., 2025a) predicts multiple geometric quantities but ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Recently, the field has shifted toward feed-forward foundation models, with models like DUSt3R (Wang et al., 2024) and VGGT (Wang et al., 2025a) demonstrating remarkable ...
- **p. 4 / 3.2. Unified Spatial Prediction - extractive PDF cue:** The input images along with optional priors are tokenized as described in Sec.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 3.1), which encodes diverse input modalities, including camera intrinsics, poses, and depth maps, into a unified token sequence; and (2) Unified Spatial ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We merge all modality tokens into a unified sequence: pose and intrinsic tokens are concatenated with image tokens T img i ∈R(Hp×Wp)×D, ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Unified Spatial Prediction - extractive PDF cue:** To address these issues, we introduce a decoupled modeling strategy that separates geometry prediction from appearance reconstruction, along with a curriculum learning scheme that progressively ...
- **p. 5 / 3.2. Unified Spatial Prediction - extractive PDF cue:** We then incorporate the normal prediction task into the joint training scheme.
- **p. 3 / 3.1. Multi-modal Tokenization - extractive PDF cue:** Below, we describe tokenization for each modality, followed by merging and training strategies for inference with any available priors.
- **p. 6 / 4. Model Training - extractive PDF cue:** A.1 for the details of training losses and the specific values of these weights.
- **p. 4 / 3.1. Multi-modal Tokenization - extractive PDF cue:** This enables flexible control over input modalities at inference time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, issues, introduce, decoupled, modeling, strategy, separates, geometry, prediction, appearance, reconstruction, along, curriculum, learning, scheme, progressively, balances, task, difficulties, during.
- **Relevant PDF headings:** 3. Method (p. 3); 4. Model Training (p. 5); 5.3. Comparison with Prior-guided Methods (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate point map reconstruction on scene-level datasets, including 7-Scenes (Shotton et al., 2013), NRGBD (Azinovi´c et al., 2022) and objectlevel dataset ... | p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5. Experiments) |
| Semantic / temporal fusion | Incorporating priors further improves results; using all priors yields 58.1% and 53.1% accuracy gains on 7-Scenes and NRGBD over our no-prior baseline, ... | p. 7 (5.1. Evaluation on Different Tasks), p. 8 (5.3. Comparison with Prior-guided Methods) |
| Robot query / planning handoff | 3 shows substantial improvements over existing methods, demonstrating that multi-task learning with shared representations can outperform specialized single-task approaches. | p. 8 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks) |

## Failure and Ablation Link

- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** 6 reports ablation analysis on novel view synthesis: (1) We replace groundtruth camera parameters with predicted ones for 3DGS rendering to examine their importance.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Geometric Priors Unlock Enhanced Scene Reconstruction of WorldMirror. (Top) Camera poses help the model to capture relative view positions accurately. (Middle) Calibrated intrinsic ...
- **p. 7 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** 1, our method without priors already surpasses VGGT and π3, with 10.4% and 17.8% accuracy gains on 7-Scenes and DTU.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. Novel View Synthesis Ablation. Best and second best results are highlighted.
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 11. Two-view NVS comparison on RealEstate10K and DL3DV. WorldMirror demonstrates strong generalization ability, even without being trained specifically for the two-view NVS setting.
- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 13. Ablation study comparing our decoupled training strategy against joint training. Lower is better for all error metrics (↓); higher is better for PSNR ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 14. Sensitivity analysis on the prior dropout probability p. Performance is reported under both no-prior and all-prior inference conditions. Lower is better for all ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Unified Spatial Prediction), p. 4 (3.2. Unified Spatial Prediction), p. 3 (3. Method), p. 5 (3.2. Unified Spatial Prediction), p. 3 (3.1. Multi-modal Tokenization), p. 5 (3.2. Unified Spatial Prediction), objective p. 5 (4. Model Training), p. 4 (3.1. Multi-modal Tokenization), p. 5 (3.2. Unified Spatial Prediction), p. 6 (4. Model Training), p. 6 (4. Model Training), p. 3 (3.1. Multi-modal Tokenization), temporal p. 3 (3. Method), p. 3 (3.1. Multi-modal Tokenization), p. 4 (3.1. Multi-modal Tokenization), p. 4 (3.2. Unified Spatial Prediction), p. 7 (5.1. Evaluation on Different Tasks), p. 8 (5.4. Ablation Study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
