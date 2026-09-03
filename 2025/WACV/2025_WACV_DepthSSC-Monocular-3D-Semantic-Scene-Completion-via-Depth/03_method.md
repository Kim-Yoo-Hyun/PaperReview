# Method - DepthSSC: Monocular 3D Semantic Scene Completion via Depth-Spatial Alignment and Voxel Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Yao_DepthSSC_Monocular_3D_Semantic_Scene_Completion_via_Depth-Spatial_Alignment_and_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Yao_DepthSSC_Monocular_3D_Semantic_Scene_Completion_via_Depth-Spatial_Alignment_and_WACV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 3 (3.1. Preliminary), p. 3 (3. Method)): The ST-GF module is designed with three primary objectives: (1) correcting geometric distortions by predicting a 3D affine transformation matrix Θijk, which allows flexible adjustments in voxel position, including rotation, ...

## Method Body Digest

- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** The ST-GF module is designed with three primary objectives: (1) correcting geometric distortions by predicting a 3D affine transformation matrix Θijk, which allows flexible adjustments ...
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** To address these spatial alignment issues, we propose the Spatially-Transformed Graph Fusion (ST-GF) module, as shown in Figure 3.
- **p. 3 / 3.1. Preliminary - extractive body cue:** The Deformable Self-Attention (DSA) mechanism refines voxel features by enabling interactions within the 3D space: DSA(F3D, F3D) = DA(f, p, F3D), (2) where f is ...
- **p. 3 / 3. Method - extractive body cue:** In this part, we first introduce the baseline model VoxFormer [15] in Section 3.1.
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** We substitute equation 5, equation 4, and Tijk into equation 3, and obtain: Θijk = " cθcϕsx (cθsϕsψ-sθcψ)sy (cθsϕcψ+sθsψ)sz tx sθcϕsx (sθsϕsψ+cθcψ)sy (sθsϕcψ-cθsψ)sz ty -sϕsx ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** The final output Yt ∈RH×W ×Z×(M+1) represents the semantic segmentation map, where H×W ×Z is the output resolution and M +1 indicates M semantic classes ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** From an input RGB image It, 2D features F2Dt ∈ Rb×c×d are extracted using a convolutional neural network backbone, where b × c is the ...
- **p. 1 / 1. Introduction - extractive body cue:** (a)Input (b)VoxFormer (c)DepthSSC Figure 1.

## Design Rationale

- **p. 2 / 44.89 IoU on the SemanticKITTI benchmark (hidden - extractive body cue:** test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels to ...
- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions are: • We propose DepthSSC, a new method that integrates spatial transformation with geometric awareness to address the issues of inaccurate depth ...
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** To address these spatial alignment issues, we propose the Spatially-Transformed Graph Fusion (ST-GF) module, as shown in Figure 3.

## Source Evidence Cues

- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** The ST-GF module is designed with three primary objectives: (1) correcting geometric distortions by predicting a 3D affine transformation matrix Θijk, which allows flexible adjustments ...
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** To address these spatial alignment issues, we propose the Spatially-Transformed Graph Fusion (ST-GF) module, as shown in Figure 3.
- **p. 3 / 3.1. Preliminary - extractive body cue:** The Deformable Self-Attention (DSA) mechanism refines voxel features by enabling interactions within the 3D space: DSA(F3D, F3D) = DA(f, p, F3D), (2) where f is ...
- **p. 3 / 3. Method - extractive body cue:** In this part, we first introduce the baseline model VoxFormer [15] in Section 3.1.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The ST-GF module is designed with three primary objectives: (1) correcting geometric distortions by predicting a 3D affine transformation matrix Θijk, which ... | p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 4 (3.2. Spatially-Transformed Graph Fusion) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To address these spatial alignment issues, we propose the Spatially-Transformed Graph Fusion (ST-GF) module, as shown in Figure 3. | p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 3 (3.1. Preliminary) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The Deformable Self-Attention (DSA) mechanism refines voxel features by enabling interactions within the 3D space: DSA(F3D, F3D) = DA(f, p, F3D), (2) ... | p. 3 (3.1. Preliminary), p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** We substitute equation 5, equation 4, and Tijk into equation 3, and obtain: Θijk = " cθcϕsx (cθsϕsψ-sθcψ)sy (cθsϕcψ+sθsψ)sz tx sθcϕsx (sθsϕsψ+cθcψ)sy (sθsϕcψ-cθsψ)sz ty -sϕsx ...
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** The ST-GF module is designed with three primary objectives: (1) correcting geometric distortions by predicting a 3D affine transformation matrix Θijk, which allows flexible adjustments ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** The Deformable Self-Attention (DSA) mechanism refines voxel features by enabling interactions within the 3D space: DSA(F3D, F3D) = DA(f, p, F3D), (2) where f is ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 3 (3.1. Preliminary).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | final, output, represents, semantic, segmentation, where, resolution, indicates, classes, plus, void, class, input, RGB | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | final, output, represents, semantic, segmentation, where, resolution, indicates, classes, plus | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | test, surpassing, latest, approaches, introduce, Spatially-Transformed, Graph, Fusion, module, facilitates | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | substitute, equation, Tijk, obtain, Once, transformation, applied, grid, generator, creates | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Preliminary - extractive body cue:** The final output Yt ∈RH×W ×Z×(M+1) represents the semantic segmentation map, where H×W ×Z is the output resolution and M +1 indicates M semantic classes ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** From an input RGB image It, 2D features F2Dt ∈ Rb×c×d are extracted using a convolutional neural network backbone, where b × c is the ...
- **p. 1 / 1. Introduction - extractive body cue:** (a)Input (b)VoxFormer (c)DepthSSC Figure 1.
- **p. 2 / 1. Introduction - extractive body cue:** DepthSSC achieves state-of-the-art results with 15.22 mIoU and
- **p. 1 / 1. Introduction - extractive body cue:** 3D Semantic Scene Completion (SSC) [21] is crucial for autonomous driving, predicting voxel occupancy in 3D scenes from partial inputs.
- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions are: • We propose DepthSSC, a new method that integrates spatial transformation with geometric awareness to address the issues of inaccurate depth ...
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** To address these spatial alignment issues, we propose the Spatially-Transformed Graph Fusion (ST-GF) module, as shown in Figure 3.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Given the transformed voxels q′ ijk, we perform the following steps. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | H2GFormer [25] introduces a horizontal-to-global voxel transformer for improved semantic feature fusion, while HASSC [23] employs a hardness-aware design and self-distillation strategy ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ST-GF, module, designed, three, primary, objectives, correcting, geometric, distortions, predicting, affine, transformation, matrix, allows, flexible, adjustments, voxel, position, including, rotation.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion ... | p. 2 (44.89 IoU on the SemanticKITTI benchmark (hidden), p. 8 (4.4. Robustness experiment) |
| Semantic / temporal fusion | Quantitative comparison against RGB-inferred baselines and the state-of-the-art monocular SSC method on SemanticKITTI [1] (hidden test set).The best results compared to the ... | p. 8 (4.4. Robustness experiment), p. 8 (4.4. Robustness experiment) |
| Robot query / planning handoff | The addition of the dynamic resolution in GAV also contributes significantly to the final performance. ing intensities into the depth input, defined ... | p. 8 (4.4. Robustness experiment), p. 3 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 4.4. Robustness experiment - extractive body cue:** Ablation and alternative methods evaluation.
- **p. 8 / 5. Conclusion - extractive body cue:** By integrating the Spatially-Transformed Graph Fusion (ST-GF) module and Geometrically-aware Voxelization, DepthSSC dynamically adjusts voxel resolutions based on the geometric complexity of 3D space, addressing ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Robustness evaluation under noisy depth inputs. This table shows the performance degradation in mIoU under increas- ing depth noise levels. Our ST-GF module ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Goal of Our Approach. Demonstrates DepthSSC's su- periority in handling complex 3D environments for semantic scene completion. Contrasted with VoxFormer, DepthSSC excels in ...
- **p. 7 / 4.4. Robustness experiment - extractive body cue:** To evaluate the robustness of the ST-GF module under depth input errors, we simulate errors in depth measurements by artificially introducing Gaussian noise with vary2160

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 3 (3.1. Preliminary), p. 3 (3. Method), objective p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 3 (3.1. Preliminary), temporal p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 1 (1. Introduction), p. 2 (44.89 IoU on the SemanticKITTI benchmark (hidden).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
