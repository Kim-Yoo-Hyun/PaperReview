# Method - GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=UkBwyp3aXG; PDF retrieval source: https://openreview.net/pdf/b288be2e77239176daf3dd0989250da05bea4f5d.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 4 (3 Method)): We use this color encoder in feature extraction at different levels.

## Method Body Digest

- **p. 5 / 3 Method - extractive PDF cue:** We use this color encoder in feature extraction at different levels.
- **p. 5 / 3 Method - extractive PDF cue:** 3.1.2 Geometric-3DGS Module The Geometric-3DGS module mainly consists of three components: the 3DGS encoder, attention with 3DGS embeddings, and Gaussian superpoint registration, as shown in ...
- **p. 4 / 3 Method - extractive PDF cue:** The feature extraction module extracts and integrates geometric and color information from the input point clouds P and Q using the color encoder and geometric ...
- **p. 6 / 3 Method - extractive PDF cue:** Therefore, we introduce LORA optimization within the overall Transformer structure to reduce unnecessary computational overhead.
- **p. 6 / 3 Method - extractive PDF cue:** 3.2 Fine Registration With Photometric Optimization To improve point cloud registration accuracy, we propose a fine registration method based on photometric optimization.
- **p. 4 / 3 Method - extractive PDF cue:** 3.1 Coarse Registration With Color Features 3.1.1 Color Encoder Module We design a dedicated color encoder module to inject effective color information into point cloud ...
- **p. 22 / A.1 Proof of photometric optimization - extractive PDF cue:** (18) This guarantees that the loss function will decrease monotonically and converge to a local minimum.
- **p. 6 / 3 Method - extractive PDF cue:** Using differentiable rendering, we backpropagate the loss to the transformation parameters R∗, t∗and update them with gradient descent.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Additionally, we introduce a joint photometric loss to improve the utilization of color information during the registration process.
- **p. 2 / 1 Introduction - extractive PDF cue:** To address the challenges of point cloud registration in low-overlap real-world scenarios, we propose GeGS-PCR, a two-stage method that integrates Geometric-3DGS for colored point cloud ...
- **p. 3 / 1 Introduction - extractive PDF cue:** • We propose the Geometric-3DGS module to encode multimodal representations of superpoint neighborhood information.

## Source Evidence Cues

- **p. 5 / 3 Method - extractive PDF cue:** We use this color encoder in feature extraction at different levels.
- **p. 5 / 3 Method - extractive PDF cue:** 3.1.2 Geometric-3DGS Module The Geometric-3DGS module mainly consists of three components: the 3DGS encoder, attention with 3DGS embeddings, and Gaussian superpoint registration, as shown in ...
- **p. 4 / 3 Method - extractive PDF cue:** The feature extraction module extracts and integrates geometric and color information from the input point clouds P and Q using the color encoder and geometric ...
- **p. 6 / 3 Method - extractive PDF cue:** Therefore, we introduce LORA optimization within the overall Transformer structure to reduce unnecessary computational overhead.
- **p. 6 / 3 Method - extractive PDF cue:** 3.2 Fine Registration With Photometric Optimization To improve point cloud registration accuracy, we propose a fine registration method based on photometric optimization.
- **p. 4 / 3 Method - extractive PDF cue:** 3.1 Coarse Registration With Color Features 3.1.1 Color Encoder Module We design a dedicated color encoder module to inject effective color information into point cloud ...
- **p. 22 / A.1 Proof of photometric optimization - extractive PDF cue:** (18) This guarantees that the loss function will decrease monotonically and converge to a local minimum.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We use this color encoder in feature extraction at different levels. | p. 5 (3 Method), p. 5 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | 3.1.2 Geometric-3DGS Module The Geometric-3DGS module mainly consists of three components: the 3DGS encoder, attention with 3DGS embeddings, and Gaussian superpoint registration, ... | p. 5 (3 Method), p. 4 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The feature extraction module extracts and integrates geometric and color information from the input point clouds P and Q using the color ... | p. 4 (3 Method), p. 6 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 Method - extractive PDF cue:** Using differentiable rendering, we backpropagate the loss to the transformation parameters R∗, t∗and update them with gradient descent.
- **p. 6 / 3 Method - extractive PDF cue:** After coarse registration, we optimize point cloud alignment by rendering the 3DGS of the target and source point clouds under the new pose and minimizing ...
- **p. 22 / A.1 Proof of photometric optimization - extractive PDF cue:** Under the assumptions of local convexity of the photometric loss Lphoto near the optimal pose T ∗and bounded gradient noise, the proposed joint loss Ltotal ...
- **p. 4 / 3 Method - extractive PDF cue:** Therefore, we can optimize the following objective to solve for the rigid transformation: min R,t X (p∗xi,q∗yi)∈C∗ ∥R · p∗ xi + t -q∗ yi∥2 ...
- **p. 4 / 3 Method - extractive PDF cue:** The main objective of point cloud registration is to estimate a rigid transformation, represented by T = {R, t}, where R ∈SO(3) is the 3D ...
- **p. 5 / 3 Method - extractive PDF cue:** By minimizing the 3DGS distance between the source and target point clouds pi, pj, we iteratively 5
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3 Method), p. 22 (A.1 Proof of photometric optimization), p. 4 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 22 (A.1 Proof of photometric optimization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | feature, extraction, module, extracts, integrates, geometric, color, information, input, point, clouds, encoder, producing, superpoint | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | feature, extraction, module, extracts, integrates, geometric, color, information, input, point | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Additionally, introduce, joint, photometric, loss, improve, utilization, color, information, during | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | differentiable, rendering, backpropagate, loss, transformation, parameters, update, them, gradient, descent | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Method - extractive PDF cue:** The feature extraction module extracts and integrates geometric and color information from the input point clouds P and Q using the color encoder and geometric ...
- **p. 4 / 3 Method - extractive PDF cue:** The noise-robust color mapping is as follows: F ′ C = δ(LN(W3 · δ(LN(W2 · (δ(LN(W1δ))))))), (2) where W1, W2, and W3 ∈Rdin×dout are learnable ...
- **p. 5 / 3 Method - extractive PDF cue:** This module implements feature extraction at different granularities and provides a global, transformation-invariant geometric-color representation, which is crucial for fine point cloud registration.
- **p. 5 / 3 Method - extractive PDF cue:** We use this color encoder in feature extraction at different levels.
- **p. 3 / 3 Method - extractive PDF cue:** Suppose we have two point clouds representing the target point cloud P = {pi∈R3/i = 1, ..., N} and the source point cloud Q = ...
- **p. 6 / 3 Method - extractive PDF cue:** 3.2 Fine Registration With Photometric Optimization To improve point cloud registration accuracy, we propose a fine registration method based on photometric optimization.
- **p. 6 / 3 Method - extractive PDF cue:** After coarse registration, we optimize point cloud alignment by rendering the 3DGS of the target and source point clouds under the new pose and minimizing ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Directly parameterizing all point cloud information with 3DGS at the beginning would result in a large amount of redundant parameters and very ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The specific steps of the 3DGS encoder are as follows: We calculate the covariance matrix of each local neighborhood in the point ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Directly parameterizing all point cloud information with 3DGS at the beginning would result in a large amount of redundant parameters and very ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We implemented and evaluated our GeGS-PCR using PyTorch [15] on an AMD 610M CPU and an NVIDIA RTX 4070 GPU. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** color, encoder, feature, extraction, different, levels, Geometric-3DGS, Module, mainly, consists, three, components, DGS, attention, embeddings, Gaussian, superpoint, registration, Fig, extracts.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To validate the performance of the GeGS-PCR model, we evaluate it on the indoor benchmarks Color3DMatch (C3DM) and Color3DLoMatch (C3DLM), as well ... | p. 7 (4 Experiments), p. 25 (A.5 Additional Experiments) |
| Semantic / temporal fusion | We compared GeGS-PCR with several SOTA methods (metrics in Appendix A.3). | p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Robot query / planning handoff | The photometric optimization loss achieves the highest performance with 87.6% PIR, 98.2% FMR, 71.6% IR, and 91.9% RR on C3DM, and 56.1% ... | p. 26 (A.5 Additional Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive PDF cue:** More detailed ablation analysis is shown in Appendix A.5.
- **p. 9 / 4 Experiments - extractive PDF cue:** Without the color encoder (row d), performance drops slightly, especially in FMR.
- **p. 26 / A.5 Additional Experiments - extractive PDF cue:** 6 shows the training loss curves for both the standard model (without LoRA) and the model with LoRA applied on the Color3DMatch dataset.
- **p. 27 / A.5 Additional Experiments - extractive PDF cue:** Specifically, the losses for the LoRA-enhanced model decrease more steadily and reach a lower final value compared to the model without LoRA, suggesting that the ...
- **p. 27 / A.5 Additional Experiments - extractive PDF cue:** Model Estimator C3DM C3DLM RRE(°) RTE(m) RRE(°) RTE(m) Predator [28] RANSAC-50k 2.029 0.064 3.048 0.093 CoFiNet [44] RANSAC-50k 2.002 0.064 3.271 0.090 GeoTransformer [15] RANSAC-free ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation results based on ColorPCR baseline C3DM C3DLM
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Performance of ablation experiments C3DM C3DLM Overlap PIR(%) FMR(%) IR(%) RR(%)

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 4 (3 Method), objective p. 6 (3 Method), p. 6 (3 Method), p. 22 (A.1 Proof of photometric optimization), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), temporal p. 5 (3 Method), p. 5 (3 Method), p. 7 (4 Experiments), p. 25 (A.5 Additional Experiments), p. 25 (A.5 Additional Experiments), p. 1 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
