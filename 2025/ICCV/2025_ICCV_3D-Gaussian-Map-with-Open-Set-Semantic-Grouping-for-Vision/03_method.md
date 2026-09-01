# Method - 3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.5. Implementation Details), p. 5 (3.3. Multi-Level Action Prediction (MAP)), p. 4 (3.2. Open-Set Semantic Grouping (OSG)), p. 3 (3. Method), p. 3 (3.1. Egocentric Scene Map (ESM)), p. 4 (3.1. Egocentric Scene Map (ESM))): For R2R [3] and R4R [32], Masked Language Modeling (MLM) [12, 36] and Single-step Action Prediction (SAP) [12, 30] are adopted as auxiliary objectives during pretraining.

## Method Body Digest

- **p. 5 / 3.5. Implementation Details - extractive PDF cue:** For R2R [3] and R4R [32], Masked Language Modeling (MLM) [12, 36] and Single-step Action Prediction (SAP) [12, 30] are adopted as auxiliary objectives during ...
- **p. 5 / 3.3. Multi-Level Action Prediction (MAP) - extractive PDF cue:** These features are then stacked into a combined representation F i, followed by FMLT to generate the instance-level score pi: pi = Softmax(F MLT([F i, ...
- **p. 4 / 3.2. Open-Set Semantic Grouping (OSG) - extractive PDF cue:** To bridge this gap, we introduce OSG operation, enriching ESM with open-set semantics by associating each Gaussian primitive with semantic properties derived from visual observations.
- **p. 3 / 3. Method - extractive PDF cue:** Built upon this, the agent is required to learn a navigation policy that predicts the next step action at ∈ At.
- **p. 3 / 3.1. Egocentric Scene Map (ESM) - extractive PDF cue:** ESM models the spatial structure of scenes using differentiable 3D Gaussians, initialized from sparse pseudo-lidar point clouds derived from multi-view RGB-D observations.
- **p. 4 / 3.1. Egocentric Scene Map (ESM) - extractive PDF cue:** The differentiable rendering process enables gradients from pixel-level loss functions to backpropagate through the Gaussian parameters.
- **p. 6 / 3.5. Implementation Details - extractive PDF cue:** R2R val unseen test unseen Models TL↓ NE↓SR↑SPL↑ TL↓ NE↓SR↑SPL↑ Seq2Seq [3] 8.39 7.81 22 - 8.13 7.85 20 18 SF [22] - 6.62 35 ...
- **p. 4 / 3.1. Egocentric Scene Map (ESM) - extractive PDF cue:** Gaussian parameters (position µ, scale s, rotation r, opacity α, color c, and semantic σ) are optimized through the differential rendering process, where the parameters ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** In contrast, our method introduces a set of sparse and adaptive 3D Gaussians to model the 3D scene, efficiently capturing spatial structures and integrating open-set ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our method is evaluated on three public benchmarks: R2R [3], R4R [32], and REVERIE [56].
- **p. 4 / 3.3. Multi-Level Action Prediction (MAP) - extractive PDF cue:** The 3D Gaussian Map G, constructed by integrating ESM and OSG, consists of Gaussians gi parameterized by {µi, si, ri, αi, ci, σi}.

## Source Evidence Cues

- **p. 5 / 3.5. Implementation Details - extractive PDF cue:** For R2R [3] and R4R [32], Masked Language Modeling (MLM) [12, 36] and Single-step Action Prediction (SAP) [12, 30] are adopted as auxiliary objectives during ...
- **p. 5 / 3.3. Multi-Level Action Prediction (MAP) - extractive PDF cue:** These features are then stacked into a combined representation F i, followed by FMLT to generate the instance-level score pi: pi = Softmax(F MLT([F i, ...
- **p. 4 / 3.2. Open-Set Semantic Grouping (OSG) - extractive PDF cue:** To bridge this gap, we introduce OSG operation, enriching ESM with open-set semantics by associating each Gaussian primitive with semantic properties derived from visual observations.
- **p. 3 / 3. Method - extractive PDF cue:** Built upon this, the agent is required to learn a navigation policy that predicts the next step action at ∈ At.
- **p. 3 / 3.1. Egocentric Scene Map (ESM) - extractive PDF cue:** ESM models the spatial structure of scenes using differentiable 3D Gaussians, initialized from sparse pseudo-lidar point clouds derived from multi-view RGB-D observations.
- **p. 4 / 3.1. Egocentric Scene Map (ESM) - extractive PDF cue:** The differentiable rendering process enables gradients from pixel-level loss functions to backpropagate through the Gaussian parameters.
- **p. 6 / 3.5. Implementation Details - extractive PDF cue:** R2R val unseen test unseen Models TL↓ NE↓SR↑SPL↑ TL↓ NE↓SR↑SPL↑ Seq2Seq [3] 8.39 7.81 22 - 8.13 7.85 20 18 SF [22] - 6.62 35 ...
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | For R2R [3] and R4R [32], Masked Language Modeling (MLM) [12, 36] and Single-step Action Prediction (SAP) [12, 30] are adopted as ... | p. 5 (3.5. Implementation Details), p. 5 (3.3. Multi-Level Action Prediction (MAP)) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | These features are then stacked into a combined representation F i, followed by FMLT to generate the instance-level score pi: pi = ... | p. 5 (3.3. Multi-Level Action Prediction (MAP)), p. 4 (3.2. Open-Set Semantic Grouping (OSG)) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | To bridge this gap, we introduce OSG operation, enriching ESM with open-set semantics by associating each Gaussian primitive with semantic properties derived ... | p. 4 (3.2. Open-Set Semantic Grouping (OSG)), p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Egocentric Scene Map (ESM) - extractive PDF cue:** The differentiable rendering process enables gradients from pixel-level loss functions to backpropagate through the Gaussian parameters.
- **p. 4 / 3.1. Egocentric Scene Map (ESM) - extractive PDF cue:** Gaussian parameters (position µ, scale s, rotation r, opacity α, color c, and semantic σ) are optimized through the differential rendering process, where the parameters ...
- **p. 5 / 3.5. Implementation Details - extractive PDF cue:** For R2R [3] and R4R [32], Masked Language Modeling (MLM) [12, 36] and Single-step Action Prediction (SAP) [12, 30] are adopted as auxiliary objectives during ...
- **p. 5 / 3.4. Loss Function for Gaussian Rendering - extractive PDF cue:** A combination of L1 and Structural Similarity [76] (SSIM) loss is used to optimize the rendered color ˆI with respect to the ground truth I: ...
- **p. 3 / 3. Method - extractive PDF cue:** Based on this map, the agent performs Multi-Level Action Prediction (MAP, §3.3) strategy, using multi-level cues for decision-making (see Fig.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3.1. Egocentric Scene Map (ESM)), p. 4 (3.1. Egocentric Scene Map (ESM)), p. 5 (3.5. Implementation Details), p. 5 (3.4. Loss Function for Gaussian Rendering).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | design, MAP, strategy, predict, action, probabilities, aggregating, spatial-semantic, cues, candidate, waypoints, guided, L-word, instruction | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | design, MAP, strategy, predict, action, probabilities, aggregating, spatial-semantic, cues, candidate | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contrast, introduces, sparse, adaptive, Gaussians, model, scene, efficiently, capturing, spatial | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | differentiable, rendering, process, enables, gradients, pixel-level, loss, functions, backpropagate, through | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.3. Multi-Level Action Prediction (MAP) - extractive PDF cue:** Based on g, we design MAP strategy to predict action probabilities by aggregating spatial-semantic cues from candidate waypoints V, guided by the L-word instruction embedding ...
- **p. 3 / 3. Method - extractive PDF cue:** Built upon this, the agent is required to learn a navigation policy that predicts the next step action at ∈ At.
- **p. 3 / 3. Method - extractive PDF cue:** At each navigation step t, the agent receives a 360-degree panoramic observation comprising RGB images It = {It,k}K k=1 and associated depth images Dt ={Dt,k}K ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In contrast, our method introduces a set of sparse and adaptive 3D Gaussians to model the 3D scene, efficiently capturing spatial structures and integrating open-set ...
- **p. 4 / 3.1. Egocentric Scene Map (ESM) - extractive PDF cue:** After initializing Gaussian primitives Gt, a tile-based renderer M3D→2D rasterizes these primitives to synthesize corresponding 2D observation {ˆIt, ˆDt} of the scene from a specific ...
- **p. 5 / 3.5. Implementation Details - extractive PDF cue:** To ensure efficiency and sparse sampling, the RGB-D observations are resized to 224 × 224, and the 3D Gaussian Map is constructed at this resolution.
- **p. 5 / 3.5. Implementation Details - extractive PDF cue:** At each waypoint, our agent constructs the 3D Gaussian Map using multi-view RGB-D observations and applies MAP strategy to assist in its decision-making process.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | In addition, during navigation, constructing the 3D Gaussian Map at each time step takes approximately 0.07 seconds, ensuring compatibility with real-time robotic ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | At time step t, multi-view RGB-D observations {It, Dt} are back-projected into the pseudo-lidar point cloud Pt. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | Early VLN approaches often rely on sequence-to-sequence models to establish connections between language and visual cues, encoding trajectory history within hidden states ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Offline pretraining is conducted on a single NVIDIA RTX 4090 GPU for 15 iterations (see more details in Appendix). | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.5. Implementation Details - extractive PDF cue:** For R2R [3] and R4R [32], Masked Language Modeling (MLM) [12, 36] and Single-step Action Prediction (SAP) [12, 30] are adopted as auxiliary objectives during ...
- **p. 5 / 3.5. Implementation Details - extractive PDF cue:** Offline pretraining is conducted on a single NVIDIA RTX 4090 GPU for 15 iterations (see more details in Appendix).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** R2R, R4R, Masked, Language, Modeling, MLM, Single-step, Action, Prediction, SAP, adopted, auxiliary, objectives, during, pretraining, features, then, stacked, combined, representation.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We evaluate our method on three benchmark datasets: R2R [3], R4R [32], and REVERIE [56]. | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Global / local decision | As shown in Table 3, our method maintains a strong performance on R4R, consistently outperforming existing approaches. | p. 6 (4.2. Comparison to State-of-the-Arts), p. 6 (4.2. Comparison to State-of-the-Arts) |
| Motion execution / recovery | Our agent achieves consistent improvements across all splits, which outperforms BEVBert [1] by 2% in both SR and SPL on the val ... | p. 6 (4.2. Comparison to State-of-the-Arts), p. 6 (4.2. Comparison to State-of-the-Arts) |

## Failure and Ablation Link

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** On REVERIE, Remote Grounding Success (RGS) and its SPL-weighted variant (RGSPL) evaluate object grounding accuracy.
- **p. 8 / 4.3. Diagnostic Experiment - extractive PDF cue:** Ablation studies of MAP strategy on val unseen split of R2R [3] and REVERIE [56].
- **p. 8 / 4.3. Diagnostic Experiment - extractive PDF cue:** To evaluate each component, we conduct diagnostic studies on val unseen splits of both R2R [3] and REVERIE [56].
- **p. 5 / 3.5. Implementation Details - extractive PDF cue:** Following classical paradigm [13], the pretrained model is finetuned using DAgger [62].
- **p. 5 / 3.5. Implementation Details - extractive PDF cue:** Offline pretraining is conducted on a single NVIDIA RTX 4090 GPU for 15 iterations (see more details in Appendix).
- **p. 7 / 4.2. Comparison to State-of-the-Arts - extractive PDF cue:** (b) Our agent precisely identifies and localizes the "bathroom" and "rug", while BEVBert [1] stops in the wrong place since critical landmarks cannot be identified, ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Dense Features vs 3D Gaussians. Recent VLN meth- ods [1, 47, 49, 78] rely on dense sampling to construct scene maps, which often ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.5. Implementation Details), p. 5 (3.3. Multi-Level Action Prediction (MAP)), p. 4 (3.2. Open-Set Semantic Grouping (OSG)), p. 3 (3. Method), p. 3 (3.1. Egocentric Scene Map (ESM)), p. 4 (3.1. Egocentric Scene Map (ESM)), objective p. 4 (3.1. Egocentric Scene Map (ESM)), p. 4 (3.1. Egocentric Scene Map (ESM)), p. 5 (3.5. Implementation Details), p. 5 (3.4. Loss Function for Gaussian Rendering), p. 3 (3. Method), temporal p. 5 (3.5. Implementation Details), p. 3 (3.1. Egocentric Scene Map (ESM)), p. 1 (1. Introduction), p. 2 (2. Related Work), p. 3 (3. Method), p. 4 (3.2. Open-Set Semantic Grouping (OSG)).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
