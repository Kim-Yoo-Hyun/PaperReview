# Method - Total-Decom: Decomposed 3D Scene Reconstruction with Minimal Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (5. Neural Implicit Feature Distillation and Sur), p. 5 (5. Neural Implicit Feature Distillation and Sur), p. 4 (4. Overview), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (5. Neural Implicit Feature Distillation and Sur)): Then, we use the volume rendering formula [13] to obtain outputs E of the target pixel, ˆE(r) = M X i=1 T r i αiˆer i , (2) where ˆe ...

## Method Body Digest

- **p. 4 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** Then, we use the volume rendering formula [13] to obtain outputs E of the target pixel, ˆE(r) = M X i=1 T r i αiˆer ...
- **p. 5 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** Additionally, we use the L2 loss Lf to optimize the rendered generalized feature ˆF(r) for distilling the F(r) from the SAM encoder.
- **p. 4 / 4. Overview - extractive body cue:** 5, we first adopt an implicit neural surface representation to achieve dense and complete 3D reconstruction from images while incorporating object-aware information by distilling image ...
- **p. 2 / 1. Introduction - extractive body cue:** In sum, our main contributions are as follows: • We introduce a novel pipeline that seamlessly integrates the segment anything model with hybrid implicit-explicit neural ...
- **p. 2 / 1. Introduction - extractive body cue:** Our approach requires minimal human annotations (approximately one click per object on average) while achieving high decomposition quality. • We propose a new mesh-based region-growing ...
- **p. 5 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** We firstly extract the SAM feature from the feature network into the vertices of the reconstruction mesh.
- **p. 6 / 6. Interactive Decomposition - extractive body cue:** Thus, we introduce human annotations to identify each object and aim to minimize human interactions.
- **p. 2 / 1. Introduction - extractive body cue:** Thanks to the segmentation capability of SAM and our feature rendering design, this interactive process also allows users to obtain the desired objects at different ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In sum, our main contributions are as follows: • We introduce a novel pipeline that seamlessly integrates the segment anything model with hybrid implicit-explicit neural ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce Total-Decom, a novel method designed for decomposed 3D reconstruction with minimal human interaction.
- **p. 3 / 3. Empirical Study on General Visual Features - extractive body cue:** Consequently, we propose a novel approach that leverages SAM features and a mesh-based region-growing method to decompose a 3D scene with minimal human an20862

## Source Evidence Cues

- **p. 4 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** Then, we use the volume rendering formula [13] to obtain outputs E of the target pixel, ˆE(r) = M X i=1 T r i αiˆer ...
- **p. 5 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** Additionally, we use the L2 loss Lf to optimize the rendered generalized feature ˆF(r) for distilling the F(r) from the SAM encoder.
- **p. 4 / 4. Overview - extractive body cue:** 5, we first adopt an implicit neural surface representation to achieve dense and complete 3D reconstruction from images while incorporating object-aware information by distilling image ...
- **p. 2 / 1. Introduction - extractive body cue:** In sum, our main contributions are as follows: • We introduce a novel pipeline that seamlessly integrates the segment anything model with hybrid implicit-explicit neural ...
- **p. 2 / 1. Introduction - extractive body cue:** Our approach requires minimal human annotations (approximately one click per object on average) while achieving high decomposition quality. • We propose a new mesh-based region-growing ...
- **p. 5 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** We firstly extract the SAM feature from the feature network into the vertices of the reconstruction mesh.
- **p. 6 / 6. Interactive Decomposition - extractive body cue:** Thus, we introduce human annotations to identify each object and aim to minimize human interactions.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, we use the volume rendering formula [13] to obtain outputs E of the target pixel, ˆE(r) = M X i=1 T ... | p. 4 (5. Neural Implicit Feature Distillation and Sur), p. 5 (5. Neural Implicit Feature Distillation and Sur) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Additionally, we use the L2 loss Lf to optimize the rendered generalized feature ˆF(r) for distilling the F(r) from the SAM encoder. | p. 5 (5. Neural Implicit Feature Distillation and Sur), p. 4 (4. Overview) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 5, we first adopt an implicit neural surface representation to achieve dense and complete 3D reconstruction from images while incorporating object-aware information ... | p. 4 (4. Overview), p. 2 (1. Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1. Introduction - extractive body cue:** Thanks to the segmentation capability of SAM and our feature rendering design, this interactive process also allows users to obtain the desired objects at different ...
- **p. 4 / 4. Overview - extractive body cue:** Our objective is to reconstruct a 3D scene from multi-view images and decompose it into individual object entities and the background while minimizing the need ...
- **p. 5 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** (6)) and the background is regularized with Manhattan loss (Eq.
- **p. 5 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** We follow the loss function Lrgb and Lgeo in MonoSDF [41] to optimize the rendered color, depth, and normal.
- **p. 6 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** 6, applying this constraint to regularize background reconstruction will yield more regular geometry but there still exist many undesired structures due to the inaccurate semantic ...
- **p. 3 / 3. Empirical Study on General Visual Features - extractive body cue:** While existing methods have explored the use of ground-truth multi-view consistent instance-level annotations [17, 20, 36, 37], these approaches suffer from high annotation costs and ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4. Overview), p. 5 (5. Neural Implicit Feature Distillation and Sur), p. 5 (5. Neural Implicit Feature Distillation and Sur), p. 6 (5. Neural Implicit Feature Distillation and Sur), p. 6 (5. Neural Implicit Feature Distillation and Sur).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | present, Total-Decom, novel, decomposed, reconstruction, minimal, human, interaction, stage, integrate, object-aware, information, distilling, image | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | present, Total-Decom, novel, decomposed, reconstruction, minimal, human, interaction, stage, integrate | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, follows, introduce, novel, pipeline, seamlessly, integrates, segment, anything | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Thanks, segmentation, capability, SAM, feature, rendering, design, interactive, process, allows | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** In this paper, we present Total-Decom, a novel method for decomposed 3D reconstruction with minimal human interaction.
- **p. 2 / 1. Introduction - extractive body cue:** At this stage, we also integrate object-aware information by distilling image features from the SAM model for follow-up efficient interaction and accurate decomposition.
- **p. 2 / 1. Introduction - extractive body cue:** Consequently, we are motivated to investigate decomposed 3D reconstruction, which enables the extraction of desired object-level shapes and facilitates scene manipulations such as reorganizing objects ...
- **p. 4 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** Then, we use the volume rendering formula [13] to obtain outputs E of the target pixel, ˆE(r) = M X i=1 T r i αiˆer ...
- **p. 4 / 4. Overview - extractive body cue:** 5: Interactive Decomposition ) and allow users control over granularity and quality while minimizing human interactions.
- **p. 6 / 6. Interactive Decomposition - extractive body cue:** Thus, we introduce human annotations to identify each object and aim to minimize human interactions.
- **p. 6 / 6. Interactive Decomposition - extractive body cue:** The following details how we realize object decomposition based on a designed mesh-based region-growing method with human interactions using our designed method.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Total-Decom requires minimal human annotations while providing users with real-time control over the granularity and quality of decomposition. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | [17] build an object-level scene model from a real-time RGBD input stream for object-compositional SLAM. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Our method is implemented using Pytorch and uses the Adam optimizer with a learning rate of 5e -4 for the tiny MLP ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, volume, rendering, formula, obtain, outputs, target, pixel, where, represent, predicted, color, normal, depth, semantic, logits, generalized, feature, Additionally, loss.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes. | p. 7 (7.1. Experiment Setup), p. 7 (7.2. Results) |
| Semantic / temporal fusion | We mainly compared our approach with the ObjSDF++, the state-of-the-art method that decomposes the scene structure with pseudo geometry priors as far ... | p. 7 (7.2. Results), p. 7 (7.1. Experiment Setup) |
| Robot query / planning handoff | Our reconstructed results also outperform ObjSDF++ qualitatively. | p. 7 (7.2. Results), p. 7 (7.1. Experiment Setup) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. The effect of different constraint on Replica room 1. where ˆpf, ˆpw represent the probabilities of the pixel being floor and wall derived ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Comparison on different decomposition methods with SAM feature. SAM + region growing represents object extraction with our method. SAM + similarity indicates object ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Visualization for distilled generalized features. ever, these methods rely heavily on accurate multi-view consistent ground-truth instance-level labels and cannot ef- fectively preserve all ...
- **p. 7 / 7.1. Experiment Setup - extractive body cue:** Since this type of method does not introduce geometric constraints, we mainly compare the way of decomposition.
- **p. 7 / 7.1. Experiment Setup - extractive body cue:** To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (5. Neural Implicit Feature Distillation and Sur), p. 5 (5. Neural Implicit Feature Distillation and Sur), p. 4 (4. Overview), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (5. Neural Implicit Feature Distillation and Sur), objective p. 2 (1. Introduction), p. 4 (4. Overview), p. 5 (5. Neural Implicit Feature Distillation and Sur), p. 5 (5. Neural Implicit Feature Distillation and Sur), p. 6 (5. Neural Implicit Feature Distillation and Sur), p. 3 (3. Empirical Study on General Visual Features), temporal p. 1 (Abstract), p. 2 (2. Related Work), p. 2 (1. Introduction), p. 6 (5. Neural Implicit Feature Distillation and Sur), p. 8 (8. Conclusion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
