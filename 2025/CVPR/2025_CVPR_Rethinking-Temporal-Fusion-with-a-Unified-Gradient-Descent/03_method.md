# Method - Rethinking Temporal Fusion with a Unified Gradient Descent View for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Rethinking_Temporal_Fusion_with_a_Unified_Gradient_Descent_View_for_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Rethinking_Temporal_Fusion_with_a_Unified_Gradient_Descent_View_for_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (Method), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 7 (5.1. Memory Consumption), p. 3 (3.2. Temporal Cue Analysis and Formulation), p. 4 (4.1. Modeling RNN Dynamics via Gradient Descent)): Following prior work [5, 23, 51], we use a ResNet-50 [16] backbone and a 256 × 704 image size for most experiments, scaling up to Swin Transformer Base [31] with ...

## Method Body Digest

- **p. 7 / Method - extractive body cue:** Following prior work [5, 23, 51], we use a ResNet-50 [16] backbone and a 256 × 704 image size for most experiments, scaling up to ...
- **p. 5 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** Historical Residual Fused Feature Backward Current-History Aligned Loss Figure 3.
- **p. 5 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** 1 guides the fusion of distinct temporal cues, deriving loss functions and historical state update equations for each fusion type.
- **p. 7 / 5.1. Memory Consumption - extractive body cue:** GDFusion reduces inference memory by storing all historical information in a single-frame-sized hidden state.
- **p. 3 / 3.2. Temporal Cue Analysis and Formulation - extractive body cue:** Inspired by testtime adaptation [6, 39, 40], we introduce additional sceneadaptive network parameters St (Sec.
- **p. 4 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** This perspective allows us to integrate diverse temporal representation types within one theoretical framework.
- **p. 4 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** The RNN update step ht = Aht-1 + Bxt is equivalent to a gradient descent step on ht-1 minimizing the loss function Lt = ∥Aht-1 ...
- **p. 4 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** To unify temporal fusion, we reinterpret standard RNN updates as gradient descent steps to minimize discrepancies between current and historical information.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** This allows the RNN to operate on a wide array of diverse representation forms. iii) Through this reinterpretation, we propose a unified RNN-style temporal fusion ...
- **p. 2 / 1. Introduction - extractive body cue:** To integrate temporal information from heterogeneous representations, we propose a unified fusion framework, GDFusion.
- **p. 8 / 5.4. Wall-Clock Time - extractive body cue:** 5, our method outperforms the multi-frame stacking method SOLOFusion in total time consumption.

## Source Evidence Cues

- **p. 7 / Method - extractive body cue:** Following prior work [5, 23, 51], we use a ResNet-50 [16] backbone and a 256 × 704 image size for most experiments, scaling up to ...
- **p. 5 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** Historical Residual Fused Feature Backward Current-History Aligned Loss Figure 3.
- **p. 5 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** 1 guides the fusion of distinct temporal cues, deriving loss functions and historical state update equations for each fusion type.
- **p. 7 / 5.1. Memory Consumption - extractive body cue:** GDFusion reduces inference memory by storing all historical information in a single-frame-sized hidden state.
- **p. 3 / 3.2. Temporal Cue Analysis and Formulation - extractive body cue:** Inspired by testtime adaptation [6, 39, 40], we introduce additional sceneadaptive network parameters St (Sec.
- **p. 4 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** This perspective allows us to integrate diverse temporal representation types within one theoretical framework.
- **p. 4 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** The RNN update step ht = Aht-1 + Bxt is equivalent to a gradient descent step on ht-1 minimizing the loss function Lt = ∥Aht-1 ...
- **Detected method headings:** 4.1. Modeling RNN Dynamics via Gradient Descent (p. 4); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Following prior work [5, 23, 51], we use a ResNet-50 [16] backbone and a 256 × 704 image size for most experiments, ... | p. 7 (Method), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Historical Residual Fused Feature Backward Current-History Aligned Loss Figure 3. | p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 1 guides the fusion of distinct temporal cues, deriving loss functions and historical state update equations for each fusion type. | p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 7 (5.1. Memory Consumption) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** The RNN update step ht = Aht-1 + Bxt is equivalent to a gradient descent step on ht-1 minimizing the loss function Lt = ∥Aht-1 ...
- **p. 4 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** To unify temporal fusion, we reinterpret standard RNN updates as gradient descent steps to minimize discrepancies between current and historical information.
- **p. 5 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** 1 guides the fusion of distinct temporal cues, deriving loss functions and historical state update equations for each fusion type.
- **p. 5 / 4.1. Modeling RNN Dynamics via Gradient Descent - extractive body cue:** Update dynamics of gradient descent-based temporal fusion pipeline. f t denotes the (geometry, motion, voxel-level, scene-level) feature of the current frame.
- **p. 8 / 5.4. Wall-Clock Time - extractive body cue:** Moreover, our custom matrix multiplication method for backpropagation outperforms PyTorch's built-in AutoGrad, achieving 32% and 22% efficiency gains in scene-level and motion fusion, respectively, demonstrating ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 4 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | D-to-3D, Lifting, Voxel-Level, Temporal, Fusion, Chronological, Inputs, Motion, Geometry, Task, Head, Night, Rainy, Scene | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | D-to-3D, Lifting, Voxel-Level, Temporal, Fusion, Chronological, Inputs, Motion, Geometry, Task | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | allows, RNN, operate, wide, array, diverse, representation, forms, Through, reinterpretation | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | RNN, update, step, Aht-1, Bxt, equivalent, gradient, descent, ht-1, minimizing | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** 2D-to-3D Lifting Voxel-Level Temporal Fusion Chronological Inputs Motion Geometry Task Head Night Rainy Scene Consistency Prior in Short Time Spans Scene-Level Temporal Cue … (a) ...
- **p. 7 / 5.1. Memory Consumption - extractive body cue:** GDFusion reduces inference memory by storing all historical information in a single-frame-sized hidden state.
- **p. 7 / Method - extractive body cue:** The top three rows feature an input size of 900 × 1600, while the remaining use 512 × 1408. training, 150 for validation, and 150 ...
- **p. 2 / 1. Introduction - extractive body cue:** 2, voxel-level information is encoded in 3D volume feature maps; scene-level information is represented as network parameters, inspired by test-time adaptation [6, 39] and large ...
- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive body cue:** They are dynamically updated with temporal inputs to enable continuous scene adaptation.
- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive body cue:** Single-frame-sized historical states Ht-1 v , Ht-1 g , Ht-1 m , and Ht-1 s are stored in memory and updated frame-by-frame. information.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Despite utilizing less memory, GDFusion harnesses information from all historical frames and outperforms the long-history fusion variant of SOLOFusion. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 4, the memory consumption of SOLOFusion scales linearly with the number of stored historical frames, whereas GDFusion maintains memory usage comparable to ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Despite utilizing less memory, GDFusion harnesses information from all historical frames and outperforms the long-history fusion variant of SOLOFusion. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Each temporal fusion component consumes less than 6% of the total inference time (146.6ms), demonstrating the efficiency of GDFusion. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 5.1. Memory Consumption - extractive body cue:** GDFusion reduces inference memory by storing all historical information in a single-frame-sized hidden state.
- **p. 8 / 5.4. Wall-Clock Time - extractive body cue:** Each temporal fusion component consumes less than 6% of the total inference time (146.6ms), demonstrating the efficiency of GDFusion.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Following, prior, ResNet-50, backbone, image, size, most, experiments, scaling, Swin, Transformer, Base, images, larger-scale, tests, Historical, Residual, Fused, Feature, Backward.
- **Relevant PDF headings:** 4.1. Modeling RNN Dynamics via Gradient Descent (p. 4); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | This dataset comprises 1,000 scenes in total, with 700 designated for 1510 | p. 6 (5. Experiment), p. 6 (5. Experiment) |
| Semantic / temporal fusion | Table 4. Ablations on different temporal cues. B, G, V, S, and M represent baseline, temporal geometry fusion, voxel-level fusion, scene-level fusion, ... | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Robot query / planning handoff | Table 4. Ablations on different temporal cues. B, G, V, S, and M represent baseline, temporal geometry fusion, voxel-level fusion, scene-level fusion, ... | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablations on improving RNN-based voxel-level fusion. epochs using CBGS [34] with a learning rate of 2 × 10-4 and a global batch size ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablations on different temporal cues. B, G, V, S, and M represent baseline, temporal geometry fusion, voxel-level fusion, scene-level fusion, and temporal motion ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Runtime analysis of key components, vs. SOLOFusion (16 frames). AutoGrad refers to PyTorch's automatic differentia- tion; Custom Matmul is our custom matrix multiplication. ...
- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive body cue:** Thus, we propose temporal geometry fusion to yield a more robust geometric prior, detailed in Sec.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (Method), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 7 (5.1. Memory Consumption), p. 3 (3.2. Temporal Cue Analysis and Formulation), p. 4 (4.1. Modeling RNN Dynamics via Gradient Descent), objective p. 4 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 4 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 5 (4.1. Modeling RNN Dynamics via Gradient Descent), p. 8 (5.4. Wall-Clock Time), temporal p. 7 (5.1. Memory Consumption), p. 7 (5.1. Memory Consumption), p. 3 (3.1. VisionOcc Pipeline), p. 8 (5.3. Ablation Study), p. 8 (5.3. Ablation Study), p. 6 (4.5. Memory-Efficient Voxel-Level Temporal Fusion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
