# Method - Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4. Method), p. 4 (4. Method), p. 3 (3.1. Brief introduction of diffusion models), p. 5 (4.2. Structural loss), p. 5 (4.2. Structural loss), p. 3 (3.2. 3D LiDAR scene completion diffusion models)): Firstly, we introduce the distillation method tailored for 3D LiDAR scene completion diffusion models in Sec.

## Method Body Digest

- **p. 4 / 4. Method - extractive body cue:** Firstly, we introduce the distillation method tailored for 3D LiDAR scene completion diffusion models in Sec.
- **p. 4 / 4. Method - extractive body cue:** Then, we introduce the structural loss to improve the distillation process with both scene-wise loss and point-wise loss in Sec.
- **p. 3 / 3.1. Brief introduction of diffusion models - extractive body cue:** The diffusion model ϵθ predicts the noise according to xt, c, t and is then optimized by calculating the ℓ2 loss between the predicted and ...
- **p. 5 / 4.2. Structural loss - extractive body cue:** Thus, we introduce a structural loss to further refine the distillation process and improve the completion quality.
- **p. 5 / 4.2. Structural loss - extractive body cue:** Thus, we introduce the point-wise loss to capture the relative structural information between different points in the 3D LiDAR scene.
- **p. 3 / 3.2. 3D LiDAR scene completion diffusion models - extractive body cue:** In this case, the training loss of the diffusion model is given by: LDM = Et,ϵ h
- **p. 6 / 4.3. Optimization procedure - extractive body cue:** Then, Gstu is optimized with the following objective Lstu = LKL + Lstructural (18) We set λscene = 0.5 and λpoint = 0.01 defaultly.
- **p. 5 / 4.2. Structural loss - extractive body cue:** To solve this issue, we introduce the scene-wise loss, which minimizes the distance between the ground truth scene G and the completed scene G0, Lscene ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose ScoreLiDAR, a novel distillation method tailored for 3D LiDAR scene completion diffusion models, which enables efficient and high-quality scene completion ...
- **p. 2 / 1. Introduction - extractive body cue:** Finally, we introduce a Structural Loss consisting of a scene-wise term and a point-wise term constraining the key landmark points and their relative configuration.
- **p. 4 / 4. Method - extractive body cue:** Then, we introduce the structural loss to improve the distillation process with both scene-wise loss and point-wise loss in Sec.

## Source Evidence Cues

- **p. 4 / 4. Method - extractive body cue:** Firstly, we introduce the distillation method tailored for 3D LiDAR scene completion diffusion models in Sec.
- **p. 4 / 4. Method - extractive body cue:** Then, we introduce the structural loss to improve the distillation process with both scene-wise loss and point-wise loss in Sec.
- **p. 3 / 3.1. Brief introduction of diffusion models - extractive body cue:** The diffusion model ϵθ predicts the noise according to xt, c, t and is then optimized by calculating the ℓ2 loss between the predicted and ...
- **p. 5 / 4.2. Structural loss - extractive body cue:** Thus, we introduce a structural loss to further refine the distillation process and improve the completion quality.
- **p. 5 / 4.2. Structural loss - extractive body cue:** Thus, we introduce the point-wise loss to capture the relative structural information between different points in the 3D LiDAR scene.
- **p. 3 / 3.2. 3D LiDAR scene completion diffusion models - extractive body cue:** In this case, the training loss of the diffusion model is given by: LDM = Et,ϵ h
- **p. 6 / 4.3. Optimization procedure - extractive body cue:** Then, Gstu is optimized with the following objective Lstu = LKL + Lstructural (18) We set λscene = 0.5 and λpoint = 0.01 defaultly.
- **Detected method headings:** 3.1. Brief introduction of diffusion models (p. 3); 3.2. 3D LiDAR scene completion diffusion models (p. 3); 4. Method (p. 4); Model (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Firstly, we introduce the distillation method tailored for 3D LiDAR scene completion diffusion models in Sec. | p. 4 (4. Method), p. 4 (4. Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Then, we introduce the structural loss to improve the distillation process with both scene-wise loss and point-wise loss in Sec. | p. 4 (4. Method), p. 3 (3.1. Brief introduction of diffusion models) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The diffusion model ϵθ predicts the noise according to xt, c, t and is then optimized by calculating the ℓ2 loss between ... | p. 3 (3.1. Brief introduction of diffusion models), p. 5 (4.2. Structural loss) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.2. Structural loss - extractive body cue:** To solve this issue, we introduce the scene-wise loss, which minimizes the distance between the ground truth scene G and the completed scene G0, Lscene ...
- **p. 4 / 4.1. Distillation for 3D LiDAR scene completion - extractive body cue:** Thus, decenting along the bidirectional gradient [ϵθ (Gt, P, t) -ϵϕ (Gt, P, t)] updates the student model's generative distribution toward the pre-trained distribution, achieving ...
- **p. 5 / 4.2. Structural loss - extractive body cue:** (11) to optimize the student model may lead to loss of local details.
- **p. 6 / 4.3. Optimization procedure - extractive body cue:** Then, Gstu is optimized with the following objective Lstu = LKL + Lstructural (18) We set λscene = 0.5 and λpoint = 0.01 defaultly.
- **p. 4 / 4. Method - extractive body cue:** Then, we introduce the structural loss to improve the distillation process with both scene-wise loss and point-wise loss in Sec.
- **p. 3 / 3.1. Brief introduction of diffusion models - extractive body cue:** The diffusion model ϵθ predicts the noise according to xt, c, t and is then optimized by calculating the ℓ2 loss between the predicted and ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4.1. Distillation for 3D LiDAR scene completion), p. 5 (4.2. Structural loss), p. 3 (3.2. 3D LiDAR scene completion diffusion models), p. 3 (3.1. Brief introduction of diffusion models), p. 4 (3.2. 3D LiDAR scene completion diffusion models), p. 5 (4.2. Structural loss).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, input, condition, optional, noisy, data, calculated, LiDAR, scan, ground, truth, diffusion, model, trained | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, input, condition, optional, noisy, data, calculated, LiDAR, scan, ground | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | ScoreLiDAR, novel, distillation, tailored, LiDAR, scene, completion, diffusion, models, enables | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | solve, issue, introduce, scene-wise, loss, minimizes, distance, between, ground, truth | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Brief introduction of diffusion models - extractive body cue:** Given the input x0 and the condition c (optional), the noisy data xt can be calculated by Eq.
- **p. 3 / 3.2. 3D LiDAR scene completion diffusion models - extractive body cue:** Given the input LiDAR scan P and ground truth G, a diffusion model can be trained to perform 3D LiDAR scene completion.
- **p. 4 / 3.2. 3D LiDAR scene completion diffusion models - extractive body cue:** (2) The sparse scan and noisy completed scene are input to ϵθ and ϵϕ.
- **p. 5 / 4.2. Structural loss - extractive body cue:** This is because the student model often generates subpar results at the early stage due to the complexity of the point cloud data.
- **p. 5 / 4.2. Structural loss - extractive body cue:** This is because the point cloud in LiDAR scenes includes complex geometric information that is not explicitly captured by diffusion models.
- **p. 6 / 4.3. Optimization procedure - extractive body cue:** As for Gstu, we follow the proposed method to select 1 30 of the points from the entire point cloud as key points for calculating ...
- **p. 2 / 1. Introduction - extractive body cue:** Generally, our proposed ScoreLiDAR achieves better scene completion performance and speed trade-off. widely adopted sensors due to its broader detection range and higher detection precision ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | (7) by minimizing the KL divergence between two distributions at different noise levels as: min η LKL = Et,ϵ  DKL  pt ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our goal is to distill a pre-trained 3D LiDAR scene completion diffusion model into a student model with significantly fewer sampling steps, ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | In contrast, the scene completed by ScoreLiDAR with only 8 steps in Fig. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.2. 3D LiDAR scene completion diffusion models - extractive body cue:** In this case, the training loss of the diffusion model is given by: LDM = Et,ϵ h
- **p. 3 / 3.1. Brief introduction of diffusion models - extractive body cue:** During the training, the diffusion model tries to predict the added noise at different timesteps t.
- **p. 3 / 3.1. Brief introduction of diffusion models - extractive body cue:** In this process, the number of required inference steps varies depending on different sampling methods.
- **p. 4 / 4. Method - extractive body cue:** Our goal is to distill a pre-trained 3D LiDAR scene completion diffusion model into a student model with significantly fewer sampling steps, enabling efficient and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Firstly, introduce, distillation, tailored, LiDAR, scene, completion, diffusion, models, Sec, Then, structural, loss, improve, process, scene-wise, point-wise, model, predicts, noise.
- **Relevant PDF headings:** 3.1. Brief introduction of diffusion models (p. 3); 3.2. 3D LiDAR scene completion diffusion models (p. 3); 4. Method (p. 4); Model (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Ablation study of different sampling steps on the SemanticKITTI dataset. completion tasks (Sec. | p. 6 (5. Experiment), p. 7 (5.2. Ablation study) |
| Semantic / temporal fusion | Compared to the SOTA method LiDiff [23] with refinement, which takes 30.55 seconds to complete a scene, ScoreLiDAR completes a scene in ... | p. 6 (5.1. Scene completion), p. 7 (5.2. Ablation study) |
| Robot query / planning handoff | However, after considering the structural loss, the performance of ScoreLiDAR improves significantly, which achieves better performance on all metrics. | p. 7 (5.2. Ablation study), p. 7 (5.1. Scene completion) |

## Failure and Ablation Link

- **p. 7 / 5.2. Ablation study - extractive body cue:** The results show that the variant without structural loss exhibits lower performance in scene completion on both datasets.
- **p. 8 / 5.3. Qualitative analysis - extractive body cue:** 5, on both datasets, the difference of point distance matrix between the completed scene of LiDiff [23] and the ground truth is the largest, followed ...
- **p. 6 / 5. Experiment - extractive body cue:** Secondly, we present the results of ablation studies showing the effectiveness of the structural loss and the performances of ScoreLiDAR given different sampling steps (Sec.
- **p. 7 / 5.2. Ablation study - extractive body cue:** In this part, we conduct the ablation study to verify the effectiveness of the structural loss in the training of the proposed ScoreLiDAR.
- **p. 6 / 5. Experiment - extractive body cue:** Ablation study of different sampling steps on the SemanticKITTI dataset. completion tasks (Sec.
- **p. 8 / 6. Conclusion - extractive body cue:** Thus, further exploration is required to find a more effective method to improve the training process of ScoreLiDAR and avoid the limitations of the teacher ...
- **p. 7 / 5.2. Ablation study - extractive body cue:** We compared the scene completion performances of the proposed ScoreLiDAR with a variant that does not incorporate structural loss.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4. Method), p. 4 (4. Method), p. 3 (3.1. Brief introduction of diffusion models), p. 5 (4.2. Structural loss), p. 5 (4.2. Structural loss), p. 3 (3.2. 3D LiDAR scene completion diffusion models), objective p. 5 (4.2. Structural loss), p. 4 (4.1. Distillation for 3D LiDAR scene completion), p. 5 (4.2. Structural loss), p. 6 (4.3. Optimization procedure), p. 4 (4. Method), p. 3 (3.1. Brief introduction of diffusion models), temporal p. 4 (4.1. Distillation for 3D LiDAR scene completion), p. 4 (4. Method), p. 5 (4.2. Structural loss), p. 6 (5. Experiment), p. 6 (5. Experiment), p. 7 (5.2. Ablation study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
