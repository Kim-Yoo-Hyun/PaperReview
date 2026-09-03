# Method - Scaling Diffusion Models to Real-World 3D LiDAR Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Nunes_Scaling_Diffusion_Models_to_Real-World_3D_LiDAR_Scene_Completion_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Nunes_Scaling_Diffusion_Models_to_Real-World_3D_LiDAR_Scene_Completion_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.6. Noise predictor architecture), p. 4 (3.2. Diffusion scene completion), p. 5 (3.6. Noise predictor architecture), p. 3 (3.1. Denoising diffusion probabilistic models), p. 3 (3.1. Denoising diffusion probabilistic models), p. 6 (4.1. Scene reconstruction)): As the refinement network, we use the same MinkUNet architecture used for the noise predictor without the conditioning encoder.

## Method Body Digest

- **p. 5 / 3.6. Noise predictor architecture - extractive body cue:** As the refinement network, we use the same MinkUNet architecture used for the noise predictor without the conditioning encoder.
- **p. 4 / 3.2. Diffusion scene completion - extractive body cue:** Then, we use the model to predict the noise from Gt conditioned to the LiDAR scan P or a null token ∅ given a probability ...
- **p. 5 / 3.6. Noise predictor architecture - extractive body cue:** To encode information from the conditioning scan P, we use the encoder part from MinkUNet with the same architecture as the noise predictor.
- **p. 3 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** Then, from xt, c and t, the model computes the noise prediction, supervising it with an L2 loss:
- **p. 3 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** In our case, we use the classifier-free guidance since it does not require a pre-trained encoder.
- **p. 6 / 4.1. Scene reconstruction - extractive body cue:** First, we can notice that the state-of-the-art shape generation diffusion method, PVD, achieves the lowest performance, showKITTI-360 Our data Method CD [m] ↓JSDBEV [m] ↓CD ...
- **p. 4 / 3.4. Noise prediction regularization - extractive body cue:** This formulation has only to optimize an L2 loss between the added noise and the model prediction.
- **p. 4 / 3.4. Noise prediction regularization - extractive body cue:** We compute the mean ϵθ and the standard deviation ˆϵθ over ϵθ(Gt, P, t) and calculate the regularization losses: \ma t hc a l { ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions are: • We propose a novel scene-scale diffusion scheme for 3D sensor data that operates at the point level. • ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose a regularization to stabilize the DDPMs during training, approximating the predicted noise distribution closer to the real data.
- **p. 3 / 3. Approach - extractive body cue:** We propose using DDPMs to achieve scene completion from a single 3D LiDAR scan as input.

## Source Evidence Cues

- **p. 5 / 3.6. Noise predictor architecture - extractive body cue:** As the refinement network, we use the same MinkUNet architecture used for the noise predictor without the conditioning encoder.
- **p. 4 / 3.2. Diffusion scene completion - extractive body cue:** Then, we use the model to predict the noise from Gt conditioned to the LiDAR scan P or a null token ∅ given a probability ...
- **p. 5 / 3.6. Noise predictor architecture - extractive body cue:** To encode information from the conditioning scan P, we use the encoder part from MinkUNet with the same architecture as the noise predictor.
- **p. 3 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** Then, from xt, c and t, the model computes the noise prediction, supervising it with an L2 loss:
- **p. 3 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** In our case, we use the classifier-free guidance since it does not require a pre-trained encoder.
- **p. 6 / 4.1. Scene reconstruction - extractive body cue:** First, we can notice that the state-of-the-art shape generation diffusion method, PVD, achieves the lowest performance, showKITTI-360 Our data Method CD [m] ↓JSDBEV [m] ↓CD ...
- **p. 4 / 3.4. Noise prediction regularization - extractive body cue:** This formulation has only to optimize an L2 loss between the added noise and the model prediction.
- **Detected method headings:** 3. Approach (p. 3); 3.1. Denoising diffusion probabilistic models (p. 3); 3.6. Noise predictor architecture (p. 5); Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | As the refinement network, we use the same MinkUNet architecture used for the noise predictor without the conditioning encoder. | p. 5 (3.6. Noise predictor architecture), p. 4 (3.2. Diffusion scene completion) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Then, we use the model to predict the noise from Gt conditioned to the LiDAR scan P or a null token ∅ ... | p. 4 (3.2. Diffusion scene completion), p. 5 (3.6. Noise predictor architecture) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To encode information from the conditioning scan P, we use the encoder part from MinkUNet with the same architecture as the noise ... | p. 5 (3.6. Noise predictor architecture), p. 3 (3.1. Denoising diffusion probabilistic models) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.4. Noise prediction regularization - extractive body cue:** This formulation has only to optimize an L2 loss between the added noise and the model prediction.
- **p. 4 / 3.4. Noise prediction regularization - extractive body cue:** We compute the mean ϵθ and the standard deviation ˆϵθ over ϵθ(Gt, P, t) and calculate the regularization losses: \ma t hc a l { ...
- **p. 3 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** Then, from xt, c and t, the model computes the noise prediction, supervising it with an L2 loss:
- **p. 5 / 3.4. Noise prediction regularization - extractive body cue:** Diagram of the conditioning in each layer l. then our final loss becomes: \math c a l {L} = \mat hcal {L}_{\text {diff}} + r ...
- **p. 6 / 4.1. Scene reconstruction - extractive body cue:** This is expected since our data has denser point clouds, which is an advantage for such methods since they rely on the input points to ...
- **p. 6 / 4.1. Scene reconstruction - extractive body cue:** Even though our method is not optimized over a voxel representation, we still achieve the best performance, showing that our scene completion is at the ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Denoising diffusion probabilistic models), p. 4 (3.4. Noise prediction regularization), p. 4 (3.4. Noise prediction regularization), p. 5 (3.4. Noise prediction regularization), p. 6 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Similarly, shape, completion, input, partial, point, cloud, where, output, should, complete, Commonly, model, starts | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Similarly, shape, completion, input, partial, point, cloud, where, output, should | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, novel, scene-scale, diffusion, scheme, sensor, data, operates, point | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | formulation, only, optimize, loss, between, added, noise, model, prediction, compute | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. Diffusion scene completion - extractive body cue:** Similarly to shape completion [19, 20, 47], the input is a partial point cloud P = {p1, . . . , pN} where p ∈R3, ...
- **p. 3 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** Commonly, the model starts from Gaussian noise [6, 11, 27] and iteratively removes noise from the input until it converges to the target output (e.g., ...
- **p. 4 / 3.2. Diffusion scene completion - extractive body cue:** Comparison between Gaussian noise with standard deviation σ and mean µ over non-normalized and normalized input point cloud and our proposed local point-wise noise formulation.
- **p. 6 / 4.1. Scene reconstruction - extractive body cue:** This is expected since our data has denser point clouds, which is an advantage for such methods since they rely on the input points to ...
- **p. 6 / Method - extractive body cue:** Given that our point cloud generation is done over a scan with a radius of 50 m, we divide the input scan into four quadrants ...
- **p. 4 / 3.3. Local point denoising - extractive body cue:** Besides, to complete the LiDAR scan, we need more points than the input scan.
- **p. 5 / 3.6. Noise predictor architecture - extractive body cue:** Then, we compute F′ l = W′ l ⊙Fl as an element-wise multiplication, which is then feed as the input to layer l, as depicted ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For evaluation, we used the validation set from SemanticKITTI, i.e., sequence 08. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For SemanticKITTI and KITTI-360, we used the ground truth poses to build the map, and for our data, we used KISS-ICP [41] ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | As optimizer, we used Adam [13] with a learning rate of 10-4 decreased by half every 5 epochs, and decay of 10-4, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** In our case, we use the classifier-free guidance since it does not require a pre-trained encoder.
- **p. 5 / 4. Experiments - extractive body cue:** We train our model for 20 epochs, using only the training set from SemanticKITTI.
- **p. 6 / Method - extractive body cue:** For all baselines, we used their official code and the provided weights also trained on SemanticKITTI.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** refinement, network, same, MinkUNet, architecture, noise, predictor, without, conditioning, encoder, Then, model, predict, conditioned, LiDAR, scan, null, token, given, probability.
- **Relevant PDF headings:** 3. Approach (p. 3); 3.1. Denoising diffusion probabilistic models (p. 3); 3.6. Noise predictor architecture (p. 5); Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For training our DDPM, we used the SemanticKITTI dataset [2, 9], an autonomous driving benchmark with point-wise annotations over sequences of LiDAR ... | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Semantic / temporal fusion | Table 4. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. Tab. 3 shows ... | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Robot query / planning handoff | Figure 6. Mean and standard deviation of the predicted noise ϵθ over different regularization weights. In this experiment we use DPMSolver [17] ... | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 4. Experiments - extractive body cue:** For the ground truth, we randomly sample 180, 000 points without replacement.
- **p. 5 / 4. Experiments - extractive body cue:** To remove the moving objects from the map in KITTI-360 and our data, we used an off-the-shelf moving object segmentation [24].
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Mean and standard deviation of the predicted noise ϵθ without the noise regularization. In this experiment we use DPM- Solver [17] to reduce ...
- **p. 8 / 5. Conclusion - extractive body cue:** For future work, we plan on extending our method to generate unconditional data, creating novel 3D point cloud scenes.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Mean chamfer distance and Jensen-Shannon divergence evaluation on KITTI-360 sequence 00 and our data. ing that current 3D diffusion methods cannot directly be ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. Tab. 3 shows the IoU of ...
- **p. 8 / 5. Conclusion - extractive body cue:** We define each point as the origin of the sampled Gaussian noise, learning an iterative denoising process to gradually predict offsets to reconstruct the scene ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.6. Noise predictor architecture), p. 4 (3.2. Diffusion scene completion), p. 5 (3.6. Noise predictor architecture), p. 3 (3.1. Denoising diffusion probabilistic models), p. 3 (3.1. Denoising diffusion probabilistic models), p. 6 (4.1. Scene reconstruction), objective p. 4 (3.4. Noise prediction regularization), p. 4 (3.4. Noise prediction regularization), p. 3 (3.1. Denoising diffusion probabilistic models), p. 5 (3.4. Noise prediction regularization), p. 6 (4.1. Scene reconstruction), p. 6 (4.1. Scene reconstruction), temporal p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (Method), p. 6 (4.1. Scene reconstruction), p. 8 (4.3. Noise regularization), p. 8 (4.3. Noise regularization).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
