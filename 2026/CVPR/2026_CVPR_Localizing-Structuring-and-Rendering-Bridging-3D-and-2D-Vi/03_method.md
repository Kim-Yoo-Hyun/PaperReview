# Method - Localizing, Structuring, and Rendering: Bridging 3D and 2D Vision-Language-Action Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Localizing_Structuring_and_Rendering_Bridging_3D_and_2D_Vision-Language-Action_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Localizing_Structuring_and_Rendering_Bridging_3D_and_2D_Vision-Language-Action_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3.4. Fine-Grained Action Prediction), p. 5 (3.4. Fine-Grained Action Prediction), p. 3 (3.1. Localizing Coarse Target Region), p. 3 (3.1. Localizing Coarse Target Region), p. 4 (3.2. Structuring Differential Spatial Information), p. 4 (3.3. Rendering Adaptive Viewpoint)): For gripper state, we use a binary classification head: Qgrip = hgrip(MaxPool(Zfused)), g = arg max Qgrip (7) The complete action is a = (p, r, g), where each component ...

## Method Body Digest

- **p. 6 / 3.4. Fine-Grained Action Prediction - extractive body cue:** For gripper state, we use a binary classification head: Qgrip = hgrip(MaxPool(Zfused)), g = arg max Qgrip (7) The complete action is a = (p, ...
- **p. 5 / 3.4. Fine-Grained Action Prediction - extractive body cue:** We fuse VLA features with coarse spatial context through bidirectional cross-attention: Zfused = CrossAttn(Zcoarse, ZVLA)+CrossAttn(ZVLA, Zcoarse) (4) The first term guides VLA features toward spatially ...
- **p. 3 / 3.1. Localizing Coarse Target Region - extractive body cue:** Given a natural language instruction I which is transformed to elang by VLM, like [43], and multi-view RGB-D observations O = {oi}Mobs i=1 , our ...
- **p. 3 / 3.1. Localizing Coarse Target Region - extractive body cue:** A Perceiver IO encoder [18] jointly processes voxels and language embeddings: (Qcoarse, Zcoarse, θview) = Φenc(V, elang) (1) where Qcoarse ∈RD×H×W predicts coarse target voxel ...
- **p. 4 / 3.2. Structuring Differential Spatial Information - extractive body cue:** Critically, the entire process is differentiable with respect to pcoarse: when action prediction improves, gradients backpropagate through rendered images to refine cube placement and beam ...
- **p. 4 / 3.3. Rendering Adaptive Viewpoint - extractive body cue:** We learn viewpoint parameters θview (predicted alongside Qcoarse and Zcoarse by Φenc above) through action-loss backpropagation.
- **p. 5 / 3.4. Fine-Grained Action Prediction - extractive body cue:** The bidirectional fusion enables both components to co-adapt during training.
- **p. 4 / 3.3. Rendering Adaptive Viewpoint - extractive body cue:** By learning viewpoints end-to-end through task loss, the model discovers task-relevant perspectives: clearly revealing color gradients from multiple faces (maximizing directional information), minimizing occlusions of ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • We propose DiffRender-VLA, a unified framework that bridges 3D spatial reasoning and 2D visual perception to transfer geometric ...
- **p. 3 / 3. Method - extractive body cue:** We present DiffRender-VLA, which, instead of choosing between image-based and 3D reasoning, enables gradient flow to transfer the 3D perception capabilities into 2D VLA models.
- **p. 4 / 3.2. Structuring Differential Spatial Information - extractive body cue:** As shown in Figure 3, our method creates differentiable point clouds with key properties: hue indicates spatial direction aligned with world axes; intensity encodes relative ...

## Source Evidence Cues

- **p. 6 / 3.4. Fine-Grained Action Prediction - extractive body cue:** For gripper state, we use a binary classification head: Qgrip = hgrip(MaxPool(Zfused)), g = arg max Qgrip (7) The complete action is a = (p, ...
- **p. 5 / 3.4. Fine-Grained Action Prediction - extractive body cue:** We fuse VLA features with coarse spatial context through bidirectional cross-attention: Zfused = CrossAttn(Zcoarse, ZVLA)+CrossAttn(ZVLA, Zcoarse) (4) The first term guides VLA features toward spatially ...
- **p. 3 / 3.1. Localizing Coarse Target Region - extractive body cue:** Given a natural language instruction I which is transformed to elang by VLM, like [43], and multi-view RGB-D observations O = {oi}Mobs i=1 , our ...
- **p. 3 / 3.1. Localizing Coarse Target Region - extractive body cue:** A Perceiver IO encoder [18] jointly processes voxels and language embeddings: (Qcoarse, Zcoarse, θview) = Φenc(V, elang) (1) where Qcoarse ∈RD×H×W predicts coarse target voxel ...
- **p. 4 / 3.2. Structuring Differential Spatial Information - extractive body cue:** Critically, the entire process is differentiable with respect to pcoarse: when action prediction improves, gradients backpropagate through rendered images to refine cube placement and beam ...
- **p. 4 / 3.3. Rendering Adaptive Viewpoint - extractive body cue:** We learn viewpoint parameters θview (predicted alongside Qcoarse and Zcoarse by Φenc above) through action-loss backpropagation.
- **p. 5 / 3.4. Fine-Grained Action Prediction - extractive body cue:** The bidirectional fusion enables both components to co-adapt during training.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | For gripper state, we use a binary classification head: Qgrip = hgrip(MaxPool(Zfused)), g = arg max Qgrip (7) The complete action is ... | p. 6 (3.4. Fine-Grained Action Prediction), p. 5 (3.4. Fine-Grained Action Prediction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We fuse VLA features with coarse spatial context through bidirectional cross-attention: Zfused = CrossAttn(Zcoarse, ZVLA)+CrossAttn(ZVLA, Zcoarse) (4) The first term guides VLA ... | p. 5 (3.4. Fine-Grained Action Prediction), p. 3 (3.1. Localizing Coarse Target Region) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Given a natural language instruction I which is transformed to elang by VLM, like [43], and multi-view RGB-D observations O = {oi}Mobs ... | p. 3 (3.1. Localizing Coarse Target Region), p. 3 (3.1. Localizing Coarse Target Region) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3. Rendering Adaptive Viewpoint - extractive body cue:** By learning viewpoints end-to-end through task loss, the model discovers task-relevant perspectives: clearly revealing color gradients from multiple faces (maximizing directional information), minimizing occlusions of ...
- **p. 4 / 3.2. Structuring Differential Spatial Information - extractive body cue:** Critically, the entire process is differentiable with respect to pcoarse: when action prediction improves, gradients backpropagate through rendered images to refine cube placement and beam ...
- **p. 3 / 3. Method - extractive body cue:** We present DiffRender-VLA, which, instead of choosing between image-based and 3D reasoning, enables gradient flow to transfer the 3D perception capabilities into 2D VLA models.
- **p. 6 / 3.4. Fine-Grained Action Prediction - extractive body cue:** The guided features are max-pooled spatially and decoded to rotation logits: Qrot = hrot(MaxPool(Zfused)), r = arg max Qrot (6) where rotation is discretized into ...
- **p. 6 / 3.4. Fine-Grained Action Prediction - extractive body cue:** This refinement transforms the initial workspacewide coarse localization into precise, semantically aware position estimates. p(i) is the transofrmed location of arg maxx,y,z Qi trans based ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.3. Rendering Adaptive Viewpoint), p. 3 (3. Method), p. 4 (3.3. Rendering Adaptive Viewpoint), p. 6 (3.4. Fine-Grained Action Prediction), p. 6 (3.4. Fine-Grained Action Prediction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, natural, language, instruction, transformed, elang, VLM, like, multi-view, RGB-D, observations, Mobs, final, goal | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Given, natural, language, instruction, transformed, elang, VLM, like, multi-view, RGB-D | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | main, contributions, follows, DiffRender-VLA, unified, framework, bridges, spatial, reasoning, visual | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | learning, viewpoints, end-to-end, through, task, loss, model, discovers, task-relevant, perspectives | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Localizing Coarse Target Region - extractive body cue:** Given a natural language instruction I which is transformed to elang by VLM, like [43], and multi-view RGB-D observations O = {oi}Mobs i=1 , our ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • We propose DiffRender-VLA, a unified framework that bridges 3D spatial reasoning and 2D visual perception to transfer geometric ...
- **p. 6 / 3.4. Fine-Grained Action Prediction - extractive body cue:** For gripper state, we use a binary classification head: Qgrip = hgrip(MaxPool(Zfused)), g = arg max Qgrip (7) The complete action is a = (p, ...
- **p. 2 / 1. Introduction - extractive body cue:** 3D spatial VLAs, such as PerAct [39] and VoxPoser [17], emphasize precise geometric reasoning through point clouds or voxels, achieving physically grounded action prediction but ...
- **p. 3 / 3.1. Localizing Coarse Target Region - extractive body cue:** A Perceiver IO encoder [18] jointly processes voxels and language embeddings: (Qcoarse, Zcoarse, θview) = Φenc(V, elang) (1) where Qcoarse ∈RD×H×W predicts coarse target voxel ...
- **p. 4 / 3.4. Fine-Grained Action Prediction - extractive body cue:** We bridge pretrained visual-language capabilities with 3D manipulation by presenting spatially enriched observations and training the VLA backbone jointly with our spatial embeddings.
- **p. 4 / 3.2. Structuring Differential Spatial Information - extractive body cue:** Critically, the entire process is differentiable with respect to pcoarse: when action prediction improves, gradients backpropagate through rendered images to refine cube placement and beam ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Unlike temporal history or semantic cues, our spatial beams explicitly encode 3D geometry through color intensity gradients (distance) and world-aligned hues (direction: ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Trajectory traces (inspired by TraceVLA [55]): 75.3% (-5.2%)-temporal history lacks instantaneous 3D geometry. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Unlike temporal history or semantic cues, our spatial beams explicitly encode 3D geometry through color intensity gradients (distance) and world-aligned hues (direction: ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Real-World Deployment Situation. lation heatmaps Qcoarse, world-aligned cube markers with adaptive sizing (ℓcube = 10-15cm, scaled to 0.8× object size for small ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Fine-Grained Action Prediction - extractive body cue:** The bidirectional fusion enables both components to co-adapt during training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** gripper, state, binary, classification, head, Qgrip, hgrip, MaxPool, Zfused, complete, action, where, component, predicted, independently, fused, features, combining, coarse, spatial.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Real-World Deployment Situation. lation heatmaps Qcoarse, world-aligned cube markers with adaptive sizing (ℓcube = 10-15cm, scaled to 0.8× object size for small ... | p. 7 (4. Experiments), p. 7 (4. Experiments) |
| Action / skill decoding | Best Baseline +10.0 +10.0 +25.0 +20.0 +20.0 +20.0 +17.5 (b) Visibility improvements (a) Camera Pose Density Figure 7. | p. 7 (4.1. Simulation Results), p. 7 (4.2. Real-World Deployment Results) |
| Receding execution / feedback | Figure 8. Beam parameters improvement for small objects. deployment confirm that color-encoded spatial beams and world-aligned cube markers generalize beyond synthetic environments. ... | p. 8 (Figure/Table caption), p. 7 (4.1. Simulation Results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Component ablation. Trans./Rot. Error in cm/degrees. Variant Stack Blk Insert Peg Sort Shape
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** (3) Two-stage training: 76.2% (-4.3%)-without end-to-end gradient flow, stages cannot co-adapt.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of DiffRender-VLA. The framework bridges spatial and 2D VLA paradigms through differentiable rendering: localiz- ing anchors the next manipulation target, structuring encodes ...
- **p. 6 / 4. Experiments - extractive body cue:** We initialize from OpenVLA [22] (SigLIP [53] + DinoV2 [35], Llama-2-7B [42] backbone) pretrained on Open X-Embodiment [34] and RH20T [10].
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** (3) Two-stage training: 76.2% (-4.3%)-without end-to-end gradient flow, stages cannot co-adapt.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** (1) Non-differentiable beams: 74.8% (-5.7%)-beams provide visual cues but cannot optimize placement.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Simulation Tasks for Occlusion and Clutter enviroments.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3.4. Fine-Grained Action Prediction), p. 5 (3.4. Fine-Grained Action Prediction), p. 3 (3.1. Localizing Coarse Target Region), p. 3 (3.1. Localizing Coarse Target Region), p. 4 (3.2. Structuring Differential Spatial Information), p. 4 (3.3. Rendering Adaptive Viewpoint), objective p. 4 (3.3. Rendering Adaptive Viewpoint), p. 4 (3.2. Structuring Differential Spatial Information), p. 3 (3. Method), p. 6 (3.4. Fine-Grained Action Prediction), p. 6 (3.4. Fine-Grained Action Prediction), temporal p. 7 (4.1. Simulation Results), p. 8 (4.3. Ablation Studies), p. 5 (3.4. Fine-Grained Action Prediction), p. 5 (3.4. Fine-Grained Action Prediction), p. 6 (4. Experiments), p. 7 (4. Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
