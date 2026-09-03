# Method - ODG: Occupancy Prediction Using Dual Gaussians

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=CkmLys7ipp; PDF retrieval source: https://arxiv.org/pdf/2506.09417.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 3 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 6 (3 Method)): 3.4 Attention across Dynamic and Static Queries To enable effective interaction between dynamic Gaussian queries Qd and static Gaussian queries Qs, we first concatenate their features representations.

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** 3.4 Attention across Dynamic and Static Queries To enable effective interaction between dynamic Gaussian queries Qd and static Gaussian queries Qs, we first concatenate their ...
- **p. 3 / 3 Method - extractive body cue:** Formally, 3D occupancy prediction can be defined as O = G(V), V = F(I), (1) where F(·) consists of an image backbone that extract multi-camera ...
- **p. 5 / 3 Method - extractive body cue:** We then apply Self-Attention [50] to the combined features, allowing for rich information exchange cross both query types.
- **p. 4 / 3 Method - extractive body cue:** For each layer Tℓ, it takes as input static Gaussian means Gs :µ,ℓ-1 and query features Qs ℓ-1 from the previous layer, and predict the ...
- **p. 3 / 3 Method - extractive body cue:** 3.3) and leverage attention to enable feature interaction between the dual queries (Sec.
- **p. 6 / 3 Method - extractive body cue:** Label assignment is done using the Hungarian algorithm [29] during training.
- **p. 4 / 3 Method - extractive body cue:** We observe that the box representation from 3D object detection [54, 33, 32] is a good candidate that is tailored to capture dynamic objects.
- **p. 6 / 3 Method - extractive body cue:** For rendered depth and semantic maps from Gaussians at all stages, we supervise depth with L1 loss and semantics with cross-entropy loss Lr = L ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions can be summarized as follows: • Dual Gaussian Query Design: We propose a novel dual-query architecture comprising two distinct sets of Gaussian queries ...
- **p. 2 / 1 Introduction - extractive body cue:** To establish communication between queries, we propose a simple and effective attention scheme to achieve this.
- **p. 3 / 1 Introduction - extractive body cue:** In contrast, our method predicts Gaussians in a hierarchical coarse-to-fine fashion allowing a much larger number of Gaussians, effectively resulting in higher learning capacity.

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** 3.4 Attention across Dynamic and Static Queries To enable effective interaction between dynamic Gaussian queries Qd and static Gaussian queries Qs, we first concatenate their ...
- **p. 3 / 3 Method - extractive body cue:** Formally, 3D occupancy prediction can be defined as O = G(V), V = F(I), (1) where F(·) consists of an image backbone that extract multi-camera ...
- **p. 5 / 3 Method - extractive body cue:** We then apply Self-Attention [50] to the combined features, allowing for rich information exchange cross both query types.
- **p. 4 / 3 Method - extractive body cue:** For each layer Tℓ, it takes as input static Gaussian means Gs :µ,ℓ-1 and query features Qs ℓ-1 from the previous layer, and predict the ...
- **p. 3 / 3 Method - extractive body cue:** 3.3) and leverage attention to enable feature interaction between the dual queries (Sec.
- **p. 6 / 3 Method - extractive body cue:** Label assignment is done using the Hungarian algorithm [29] during training.
- **p. 4 / 3 Method - extractive body cue:** We observe that the box representation from 3D object detection [54, 33, 32] is a good candidate that is tailored to capture dynamic objects.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 3.4 Attention across Dynamic and Static Queries To enable effective interaction between dynamic Gaussian queries Qd and static Gaussian queries Qs, we ... | p. 5 (3 Method), p. 3 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Formally, 3D occupancy prediction can be defined as O = G(V), V = F(I), (1) where F(·) consists of an image backbone ... | p. 3 (3 Method), p. 5 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We then apply Self-Attention [50] to the combined features, allowing for rich information exchange cross both query types. | p. 5 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 Method - extractive body cue:** For rendered depth and semantic maps from Gaussians at all stages, we supervise depth with L1 loss and semantics with cross-entropy loss Lr = L ...
- **p. 3 / 3 Method - extractive body cue:** Finally, we describe the training objectives in Sec.
- **p. 4 / 3 Method - extractive body cue:** We aim to reduce the spatial artifacts of 3D occupancy through projective constraints.
- **p. 5 / 3 Method - extractive body cue:** 3.5 Loss Functions We supervise predicted Gaussian means G:µ and corresponding class scores C with Chamfer distance [15] and focal loss [31] Locc = CD(G:µ,0, ...
- **p. 6 / 3 Method - extractive body cue:** Therefore the final loss can be written as L = L3d + λLr, (20) where λ is the weighting factor.
- **p. 5 / 3 Method - extractive body cue:** We leverage 3D Gaussian splatting [27, 28] which offers real-time rendering: ˆDp = G X i=1 Tiσidi, ˆSp = G X i=1 Tiαici, (11) where ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 3 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | cross, query, attention, introduced, establish, effective, interaction, between, queries, enhancing, occupancy, prediction, Hierarchical, Coarse-to-Fine | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | cross, query, attention, introduced, establish, effective, interaction, between, queries, enhancing | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, Dual, Gaussian, Query, Design, novel, dual-query, architecture | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | rendered, depth, semantic, maps, Gaussians, stages, supervise, loss, semantics, cross-entropy | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** A cross query attention is also introduced to establish effective interaction between queries, enhancing 3D occupancy prediction. • Hierarchical Coarse-to-Fine Refinement: We refine the Gaussian ...
- **p. 3 / 3 Method - extractive body cue:** 3.1 Problem Definition Given an ego-vehicle at time T, the task of 3D occupancy prediction takes Nc multi-camera images (with k × Nc optional history ...
- **p. 2 / 1 Introduction - extractive body cue:** This allows supervision from 2D labels across views, improving spatial coherence and prediction accuracy. • State-of-the-Art Performance: Extensive experiments on the Occ3D [48] benchmark demonstrates ...
- **p. 3 / 3 Method - extractive body cue:** 3.3) and leverage attention to enable feature interaction between the dual queries (Sec.
- **p. 4 / 3 Method - extractive body cue:** For each layer Tℓ, it takes as input static Gaussian means Gs :µ,ℓ-1 and query features Qs ℓ-1 from the previous layer, and predict the ...
- **p. 5 / 3 Method - extractive body cue:** 3.4 Attention across Dynamic and Static Queries To enable effective interaction between dynamic Gaussian queries Qd and static Gaussian queries Qs, we first concatenate their ...
- **p. 1 / 1 Introduction - extractive body cue:** 3D object detection [54, 22, 33, 32] has been the primary task that outputs bounding boxes to capture different entities in the scene.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 3.1 Problem Definition Given an ego-vehicle at time T, the task of 3D occupancy prediction takes Nc multi-camera images (with k × ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Under the setting of having history frames, it is critical to move the Gaussians according to its motion to sample features correctly. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | 3.1 Problem Definition Given an ego-vehicle at time T, the task of 3D occupancy prediction takes Nc multi-camera images (with k × ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Unless otherwise specified, we train all our models with a global batch size of 8 for 100 epochs using NVIDIA A100 GPUs. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive body cue:** Label assignment is done using the Hungarian algorithm [29] during training.
- **p. 6 / 4 Experiments - extractive body cue:** Unless otherwise specified, we train all our models with a global batch size of 8 for 100 epochs using NVIDIA A100 GPUs.
- **p. 6 / 4 Experiments - extractive body cue:** Inference runtime is measured on a single idle A100 GPU with PyTorch fp32 backend. ∗nuScenes is under a CC BY-NC-SA 4.0 license and Waymo license ...
- **p. 7 / 4 Experiments - extractive body cue:** Specifically, ODG-T (8f) achieves an mIoU of 35.54 with a RayIoU of 39.2, outperforming OPUS-T (8f) who has an mIoU of 33.2 (-2.34) and a ...
- **p. 8 / 4 Experiments - extractive body cue:** For all our ablation studies, we adopt ODG-T and train on the Occ3D-nuScenes for 24 epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Attention, across, Dynamic, Static, Queries, enable, effective, interaction, between, Gaussian, first, concatenate, features, representations, Formally, occupancy, prediction, defined, where, consists.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.1 Experiment Setup Datasets: We evaluate our model on the Occ3D benchmark [48] which bootstraps the nuScenes [6] and Waymo-Open [43] dataset.∗nuScenes ... | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Semantic / temporal fusion | One can see that our method achieves new state-of-the-art results in terms of both mIoU and RayIoU, while maintaining competitive inference speed ... | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Robot query / planning handoff | ODG achieves consistent improvement across all dynamic categories. | p. 7 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive body cue:** 4.4 Ablation Studies In this section, we conduct multiple ablation studies to analyze the effects of various components in our proposed ODG.
- **p. 9 / 4 Experiments - extractive body cue:** We summarize the effect of the different components in our proposed method in Tab.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5: Ablation studies on components related to dynamic Gaussian queries. (a) Effects of Query Attention. Query Attention mIoU RayIoU Cross Attn 31.95 36.3
- **p. 8 / 4 Experiments - extractive body cue:** We analyze the effect of different attention mechanisms in Tab.
- **p. 7 / 4 Experiments - extractive body cue:** We note that for fair comparison, both ODG-T and ODG-L here are trained without using future frames.
- **p. 7 / 4 Experiments - extractive body cue:** Meanwhile, our heavy variant ODG-L sets new best result eventually obtaining an mIoU of 38.18 with a RayIoU of 42.3, surpassing previous best with a ...
- **p. 9 / 4 Experiments - extractive body cue:** However, as promising as ODG is, it does not come without limitations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Method), p. 3 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 6 (3 Method), objective p. 6 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 5 (3 Method), temporal p. 3 (3 Method), p. 5 (3 Method), p. 8 (4 Experiments), p. 4 (3 Method), p. 5 (3 Method), p. 7 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
