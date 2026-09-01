# Method - SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=GtImvTta8x; PDF retrieval source: https://openreview.net/pdf/fe4aa0ae2832afb0c90d1b334f1ddb76078909eb.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology)): Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for decoding pixel-aligned 2D cross-view masks, ...

## Method Body Digest

- **p. 4 / 3 Methodology - extractive PDF cue:** Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for ...
- **p. 6 / 3 Methodology - extractive PDF cue:** Specifically, we propose Multi-View Mask Aggregation module, which first lifts 2D semantic information (i.e., query logits M and C) from different views to the 3D ...
- **p. 6 / 3 Methodology - extractive PDF cue:** Algorithm 1 Pixel-aligned 2D-to-3D lifting for simultaneous understanding and 3D recontruction. /* Model forward pass */ G ←Gaussian Decoder ▷Pixel-aligned 3D Gaussians Q, M, C ...
- **p. 4 / 3 Methodology - extractive PDF cue:** Moreover, to improve reconstruction by understanding, we introduce Mask-Guided Geometry Refinement module that leverages 2D masks to enforce intrainstance depth continuity for refining reconstructed 3D ...
- **p. 5 / 3 Methodology - extractive PDF cue:** As shown in Fig.3 (b), to enable text features ftext = {f t text}Nt t=1 as input for open-vocabulary 3D understanding, we further incorporate cross-modal ...
- **p. 5 / 3 Methodology - extractive PDF cue:** … … Cross Attention Layer ×L1 Self Attention Layer 𝒌,𝒗= 𝒇𝑈 𝒒= 𝓠 … 𝒒= 𝒇𝑡𝑒𝑥𝑡 Unified Queries SemanticFocused Features Text Features (optional) … ×L2 ...
- **p. 7 / 3 Methodology - extractive PDF cue:** In our training, we leverage both photometric loss and segmentation loss to simultaneously supervise 3D reconstruction and understanding.
- **p. 6 / 3 Methodology - extractive PDF cue:** 3.4 Training Objective Through holistic integration of components, our framework enables end-to-end optimization across the complete learning pipeline.

## Design Rationale

- **p. 4 / 3 Methodology - extractive PDF cue:** Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for ...
- **p. 2 / 1 Introduction - extractive PDF cue:** In summary, our main contributions are as follows: • We propose SIU3R, the first alignment-free framework for generalizable simultaneous understanding and 3D reconstruction, which bridges ...
- **p. 6 / 3 Methodology - extractive PDF cue:** 3.4 Training Objective Through holistic integration of components, our framework enables end-to-end optimization across the complete learning pipeline.

## Source Evidence Cues

- **p. 4 / 3 Methodology - extractive PDF cue:** Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for ...
- **p. 6 / 3 Methodology - extractive PDF cue:** Specifically, we propose Multi-View Mask Aggregation module, which first lifts 2D semantic information (i.e., query logits M and C) from different views to the 3D ...
- **p. 6 / 3 Methodology - extractive PDF cue:** Algorithm 1 Pixel-aligned 2D-to-3D lifting for simultaneous understanding and 3D recontruction. /* Model forward pass */ G ←Gaussian Decoder ▷Pixel-aligned 3D Gaussians Q, M, C ...
- **p. 4 / 3 Methodology - extractive PDF cue:** Moreover, to improve reconstruction by understanding, we introduce Mask-Guided Geometry Refinement module that leverages 2D masks to enforce intrainstance depth continuity for refining reconstructed 3D ...
- **p. 5 / 3 Methodology - extractive PDF cue:** As shown in Fig.3 (b), to enable text features ftext = {f t text}Nt t=1 as input for open-vocabulary 3D understanding, we further incorporate cross-modal ...
- **p. 5 / 3 Methodology - extractive PDF cue:** … … Cross Attention Layer ×L1 Self Attention Layer 𝒌,𝒗= 𝒇𝑈 𝒒= 𝓠 … 𝒒= 𝒇𝑡𝑒𝑥𝑡 Unified Queries SemanticFocused Features Text Features (optional) … ×L2 ...
- **p. 7 / 3 Methodology - extractive PDF cue:** In our training, we leverage both photometric loss and segmentation loss to simultaneously supervise 3D reconstruction and understanding.
- **Detected method headings:** 3 Methodology (p. 3); A.2 Network Architecture and Hyperparameters (p. 23); B Comparisons with Per-Scene Optimization Methods (p. 24)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified ... | p. 4 (3 Methodology), p. 6 (3 Methodology) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Specifically, we propose Multi-View Mask Aggregation module, which first lifts 2D semantic information (i.e., query logits M and C) from different views ... | p. 6 (3 Methodology), p. 6 (3 Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Algorithm 1 Pixel-aligned 2D-to-3D lifting for simultaneous understanding and 3D recontruction. /* Model forward pass */ G ←Gaussian Decoder ▷Pixel-aligned 3D Gaussians ... | p. 6 (3 Methodology), p. 4 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 Methodology - extractive PDF cue:** 3.4 Training Objective Through holistic integration of components, our framework enables end-to-end optimization across the complete learning pipeline.
- **p. 4 / 3 Methodology - extractive PDF cue:** Formally, the learning objective implements the mapping: F Θ,Q : {I, K} 7→{G, M, C} (1) As illustrated in Fig.2, our pipeline comprises Image Encoder, ...
- **p. 5 / 3 Methodology - extractive PDF cue:** We also introduce the following loss in training to enable matching supervision: Ltext = 1 Nt Nt X t=1 CrossEntropy(Softmax(Attn(f t text, Q) · qn), ...
- **p. 6 / 3 Methodology - extractive PDF cue:** The overall training objective is derived as follows: L = λ1//I(G) -ˆI// + λ2LPIPS(I(G), ˆI) + λ3Lmask + λ4Lcont + λ5Ltext, (5) 6
- **p. 7 / 3 Methodology - extractive PDF cue:** In our training, we leverage both photometric loss and segmentation loss to simultaneously supervise 3D reconstruction and understanding.
- **p. 5 / 3 Methodology - extractive PDF cue:** The matching process is derived as follows: qt text = arg max qn∈Q  Attn(f t text, Q) · qn  , (2) where Attn(·, ·) ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology), p. 7 (3 Methodology), p. 5 (3 Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Algorithm, Pixel-aligned, D-to-3D, lifting, simultaneous, understanding, recontruction, Model, forward, pass, Gaussian, Decoder, Gaussians, Unified | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Algorithm, Pixel-aligned, D-to-3D, lifting, simultaneous, understanding, recontruction, Model, forward, pass | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | consists, Image, Text, Encoders, extracting, multi-view, features, Gaussian, Decoder, decoding | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Training, Objective, Through, holistic, integration, components, framework, enables, end-to-end, optimization | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3 Methodology - extractive PDF cue:** Algorithm 1 Pixel-aligned 2D-to-3D lifting for simultaneous understanding and 3D recontruction. /* Model forward pass */ G ←Gaussian Decoder ▷Pixel-aligned 3D Gaussians Q, M, C ...
- **p. 3 / 3 Methodology - extractive PDF cue:** 3.1 Problem Formulation and Pipeline SIU3R processes sparse unposed multi-view images with corresponding camera intrinsics {Iv, Kv}V v=1, where V ≥2 in our setting and ...
- **p. 4 / 3 Methodology - extractive PDF cue:** The network establishes two key outputs: 1) pixel-aligned multi-view 3D Gaussians G = {gij v }V,H,W v,i,j=1 for 3D reconstruction, where g = {µ, α, ...
- **p. 6 / 3 Methodology - extractive PDF cue:** Thus, to make 3D Gaussians within the same mask to be more clustered, we propose Mask-Guided Geometry Refinement module, which utilizes masks as guidance to ...
- **p. 4 / 3 Methodology - extractive PDF cue:** This configuration enables simultaneous extraction of geometry-focused features {f v R}V v=1 for reconstruction and semantic-focused features {f v U}V v=1 for understanding.
- **p. 5 / 3 Methodology - extractive PDF cue:** Specifically, we employ L2 cross-attention layers to enable interaction between ftext and Q.
- **p. 5 / 3 Methodology - extractive PDF cue:** As shown in Fig.3 (b), to enable text features ftext = {f t text}Nt t=1 as input for open-vocabulary 3D understanding, we further incorporate cross-modal ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 3.4 Training Objective Through holistic integration of components, our framework enables end-to-end optimization across the complete learning pipeline. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | However, due to extremely high dimension of 2D features, we have to perform feature compression before rasterization to avoid memory exhaustion, which ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | However, due to extremely high dimension of 2D features, we have to perform feature compression before rasterization to avoid memory exhaustion, which ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We conduct training on 8 NVIDIA GeForce RTX 4090 GPUs, with our model trained for 100 epochs using a per-GPU batch size ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 Methodology - extractive PDF cue:** Moreover, to improve reconstruction by understanding, we introduce Mask-Guided Geometry Refinement module that leverages 2D masks to enforce intrainstance depth continuity for refining reconstructed 3D ...
- **p. 7 / 3 Methodology - extractive PDF cue:** In our training, we leverage both photometric loss and segmentation loss to simultaneously supervise 3D reconstruction and understanding.
- **p. 7 / 4 Experiments - extractive PDF cue:** We conduct training on 8 NVIDIA GeForce RTX 4090 GPUs, with our model trained for 100 epochs using a per-GPU batch size of 3 (total ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** consists, Image, Text, Encoders, extracting, multi-view, features, Gaussian, Decoder, decoding, pixel-aligned, Gaussians, Unified, Query, cross-view, masks, Mutual, Benefit, Mechanism, enabling.
- **Relevant PDF headings:** 3 Methodology (p. 3); A.2 Network Architecture and Hyperparameters (p. 23); B Comparisons with Per-Scene Optimization Methods (p. 24).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We adopt the official training and validation dataset splitting of ScanNet, and then resize and crop original images to centered images at ... | p. 22 (A.1 Data Preprocessing), p. 7 (4 Experiments) |
| Semantic / temporal fusion | Therefore, we evaluate our method against three types of baseline methods, all of which are state-of-the-arts on their respective tasks: 1) Sparse-view ... | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Robot query / planning handoff | We can see that this module can significantly w/ R→U w/o R→U RGB w/ R→U w/o R→U RGB ✓ ☓ ✓ ☓ ... | p. 9 (4 Experiments), p. 9 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: Ablation on Multi-View Mask Aggregation (R→U). improve our performance in both 2D-only and 3D-aware scene understanding, without sacrificing 3D reconstruction accuracy due to ...
- **p. 7 / 4 Experiments - extractive PDF cue:** Specifically, without reconstructed 3D structures, 2D-based methods can only perform segmentation on the input context views.
- **p. 9 / 4 Experiments - extractive PDF cue:** However, as shown in Table 2, such early aggregation leads to poor performance without re-training our model.
- **p. 24 / A.3 Implementation Details about Versatile 3D Editing - extractive PDF cue:** Remove Gaussians for a specified instance (ID = ins_id): G′ = G \ {gij v /M v,ij ins = ins_id} 3.
- **p. 24 / A.3 Implementation Details about Versatile 3D Editing - extractive PDF cue:** The modified Gaussians G′ are rendered into original context views to obtain images I′, with an off-the-shelf diffusion-based inpainting model [60] applied to fill the ...
- **p. 23 / A.3 Implementation Details about Versatile 3D Editing - extractive PDF cue:** As shown in Fig.1 of main manuscript, our simultaneous modeling of scene understanding and 3D reconstruction enables diverse 3D scene manipulations through unified pixel-aligned representations, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology), objective p. 6 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 7 (3 Methodology), p. 5 (3 Methodology), temporal p. 6 (3 Methodology), p. 6 (3 Methodology), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
