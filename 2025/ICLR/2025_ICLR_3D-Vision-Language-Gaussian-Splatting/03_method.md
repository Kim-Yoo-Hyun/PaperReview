# Method - 3D Vision-Language Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SSE9myD9SG; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114008. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY)): To train these semantically-enriched 3DGS models, the standard procedure consists of first generating the set of 2D language-feature maps H corresponding to the input images I.

## Method Body Digest

- **p. 4 / 3 METHODOLOGY - extractive body cue:** To train these semantically-enriched 3DGS models, the standard procedure consists of first generating the set of 2D language-feature maps H corresponding to the input images ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** In this paper, we propose to adapt the usual rasterization scheme to better fit the language-feature modality.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** A) We propose a novel multi-modal Gaussian splatting model; B) we enrich the input images and poses for the model to better fit the semantic ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** For two randomly selected samples (I1, W1) and (I2, W2) from the training set T r, where W1̸ = W2, we first utilize the camera ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** This scene representation is learned from a training set T r = {(Ir 1, W r 1 ), (Ir 2, W r 2 ), . ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** 1) to rasterize language embeddings, only substituting the 3D color features c with 3D semantic representations f (Eq.
- **p. 6 / 3 METHODOLOGY - extractive body cue:** Based on the above, we formulate the loss function to optimize the overall scene representation as follows, ∀(I, W) ∈T r: Lraster(W) = Ev∈I  ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** 2) and the ground-truth 2D semantic embeddings: L = E(I,W )∈T rEv∈ILsem(F W (v), HW (v)), (3) where L is the overall optimization objective.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Besides, we introduce a language-specific parameter that enables the meaningful blending of language features from different Gaussians.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** All in all, our 3D vision-language Gaussian splatting can be summarized into the following contributions: • We propose a cross-modal rasterizer that places greater emphasis ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** To address this problem, we propose a novel α-blending strategy specifically designed for exploring semantic information.

## Source Evidence Cues

- **p. 4 / 3 METHODOLOGY - extractive body cue:** To train these semantically-enriched 3DGS models, the standard procedure consists of first generating the set of 2D language-feature maps H corresponding to the input images ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** In this paper, we propose to adapt the usual rasterization scheme to better fit the language-feature modality.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** A) We propose a novel multi-modal Gaussian splatting model; B) we enrich the input images and poses for the model to better fit the semantic ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** For two randomly selected samples (I1, W1) and (I2, W2) from the training set T r, where W1̸ = W2, we first utilize the camera ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** This scene representation is learned from a training set T r = {(Ir 1, W r 1 ), (Ir 2, W r 2 ), . ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** 1) to rasterize language embeddings, only substituting the 3D color features c with 3D semantic representations f (Eq.
- **p. 6 / 3 METHODOLOGY - extractive body cue:** Based on the above, we formulate the loss function to optimize the overall scene representation as follows, ∀(I, W) ∈T r: Lraster(W) = Ev∈I  ...
- **Detected method headings:** 3 METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To train these semantically-enriched 3DGS models, the standard procedure consists of first generating the set of 2D language-feature maps H corresponding to ... | p. 4 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In this paper, we propose to adapt the usual rasterization scheme to better fit the language-feature modality. | p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | A) We propose a novel multi-modal Gaussian splatting model; B) we enrich the input images and poses for the model to better ... | p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 METHODOLOGY - extractive body cue:** 2) and the ground-truth 2D semantic embeddings: L = E(I,W )∈T rEv∈ILsem(F W (v), HW (v)), (3) where L is the overall optimization objective.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Once the data is prepared, the 3D Gaussians can be iteratively optimized by minimizing the distance between its rasterized 2D semantic embeddings (c.f.
- **p. 6 / 3 METHODOLOGY - extractive body cue:** Based on the above, we formulate the loss function to optimize the overall scene representation as follows, ∀(I, W) ∈T r: Lraster(W) = Ev∈I  ...
- **p. 7 / 3 METHODOLOGY - extractive body cue:** By combining the rasterization loss (Eq.
- **p. 7 / 3 METHODOLOGY - extractive body cue:** 8) and the camera view blending loss (Eq.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** 3, which shows how much the distribution of semantic indicator values differs from the color opacity after optimization.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 7 (3 METHODOLOGY), p. 7 (3 METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | solutions, rely, supervision, learn, multi-modal, color, semantic, scene, representation, projecting, learned, back, views, comparison | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | solutions, rely, supervision, learn, multi-modal, color, semantic, scene, representation, projecting | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Besides, introduce, language-specific, parameter, enables, meaningful, blending, language, features, different | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | ground-truth, semantic, embeddings, rEv, ILsem, where, overall, optimization, objective, Once | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** These solutions rely on 2D supervision to learn a multi-modal (color and semantic) 3D scene representation, i.e., projecting the learned 3D representation back to 2D ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Modality fusion occurs prior to rasterization, accompanied by a learnable and independent semantic indicator parameter for the α-blending of language features, enabling a more accurate ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Given an input image, these models can generate a dense 2D language map, i.e., assigning semantically-rich language embeddings to each pixel (e.g., a pixel depicting ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** A) We propose a novel multi-modal Gaussian splatting model; B) we enrich the input images and poses for the model to better fit the semantic ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** To train these semantically-enriched 3DGS models, the standard procedure consists of first generating the set of 2D language-feature maps H corresponding to the input images ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** 3.1 PROBLEM STATEMENT According to the vanilla Gaussian splatting (3DGS) paradigm applied to RGB image rendering (Kerbl et al., 2023), a scene is represented by ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** Expressing the input rotations with quaternions q1 and q2, we apply spherical linear interpolation (Slerp) (Shoemake, 1985).
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | rasterizer 𝐹 𝐶 view blending 𝐼2 𝐻2 𝐻𝒃= 𝑳𝑬𝑹𝑷(𝑯𝟏, 𝑯𝟐, 𝒌) 𝐼1 𝐻1 Ԧ𝑞1 𝑡1 Ԧ𝑞𝑏 𝑡𝑏= LERP(𝑡1, 𝑡2, 𝑘) Ԧ𝑞𝑏= SLERP( ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Method Training Time ↓ FPS ↑ # of Gaussians ↓ LangSplat 96min 40 86k GS-Grouping 130min 76 107k GOI 73min 42 92k ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 METHODOLOGY - extractive body cue:** To train these semantically-enriched 3DGS models, the standard procedure consists of first generating the set of 2D language-feature maps H corresponding to the input images ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** For two randomly selected samples (I1, W1) and (I2, W2) from the training set T r, where W1̸ = W2, we first utilize the camera ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** This scene representation is learned from a training set T r = {(Ir 1, W r 1 ), (Ir 2, W r 2 ), . ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For each scene, our model is trained for 15,000 iterations using an Adam optimizer (Kingma, 2014), and the learning rates of different components are shown ...
- **p. 10 / 4.2 RESULTS - extractive body cue:** Method Training Time ↓ FPS ↑ # of Gaussians ↓ LangSplat 96min 40 86k GS-Grouping 130min 76 107k GOI 73min 42 92k Ours 65min 79 ...
- **p. 21 / A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION - extractive body cue:** 19-22, our proposed method consistently outperforms others in terms of the training time, FPS, number of Gaussians, and storage size.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** train, semantically-enriched, DGS, models, standard, procedure, consists, first, generating, language-feature, maps, corresponding, input, images, adapt, usual, rasterization, scheme, better, modality.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | (1) LERF dataset (Kerr et al., 2023), captured using the Polycam application on an iPhone, comprises complex, in-the-wild scenes and is specifically ... | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Semantic / temporal fusion | Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 ... | p. 8 (4.2 RESULTS), p. 10 (4.2 RESULTS) |
| Robot query / planning handoff | Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 ... | p. 8 (4.2 RESULTS), p. 14 (A.2.2 QUALITATIVE RESULTS) |

## Failure and Ablation Link

- **p. 8 / 4.2 RESULTS - extractive body cue:** 4.3 ABLATION STUDIES Ablation on cross-modal rasterizer.
- **p. 8 / 4.2 RESULTS - extractive body cue:** 4.C, we present an ablation study on the interpolation ratio k.
- **p. 10 / 4.2 RESULTS - extractive body cue:** (A) Fusion module No Fusion 57.8 69.6 54.2 51.5 58.3 Single-layer MLP Fusion 55.9 68.2 53.0 49.9 56.8 Cross-attention Modality Fusion 57.3 70.7 54.6 52.0 ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 5: Ablation results of Camera View Blending on the LERF dataset, in terms of mIoU. Rotation Translation SSIM ramen teatime figurines kitchen
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 11: Qualitative semantic segmentation comparisons on the room scene of Mip-NeRF 360. A.3 ADDITIONAL ABLATION STUDIES A.3.1 HIGH-LEVEL ABLATION OF PROPOSED CONTRIBUTIONS. We first ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 10: Ablation results of three key contributions on the 3D-OVS dataset, in terms of mIoU. modal. fus. sem. indic. view blend. bed bench room ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 17: Ablation results on different levels of disentanglement between the per-modality Gaussian parameters, evaluated on the downstream open-vocabulary semantic-segmentation task on LERF. Parameters shared ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), objective p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 7 (3 METHODOLOGY), p. 7 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), temporal p. 4 (3 METHODOLOGY), p. 10 (4.2 RESULTS), p. 21 (A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION), p. 21 (A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION), p. 22 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION), p. 2 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
