# Method - SSRFlow: Semantic-aware Fusion with Spatial Temporal Re-embedding for Real-world Scene Flow

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=9abfUtE6iQ&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (2 Methodology), p. 3 (2 Methodology), p. 4 (2 Methodology), p. 6 (2 Methodology), p. 6 (2 Methodology), p. 4 (2 Methodology)): (2019) as the feature extraction backbone to build a pyramid network.

## Method Body Digest

- **p. 3 / 2 Methodology - extractive PDF cue:** (2019) as the feature extraction backbone to build a pyramid network.
- **p. 3 / 2 Methodology - extractive PDF cue:** 2.2 Hierarchical Feature Extraction The overview of our proposed network is shown in Figure 1.
- **p. 4 / 2 Methodology - extractive PDF cue:** During the dual cross-attentive fusion phase, the semantic context in the latent feature space is obtained for S∗and T ∗through linear networks Q K and ...
- **p. 6 / 2 Methodology - extractive PDF cue:** Cross-frame Feature Similarity (CFS) Loss The semantic features of the points in the warped source frame are similar to those in the surrounding target frame, ...
- **p. 6 / 2 Methodology - extractive PDF cue:** 3 Training Losses 3.1 Hierarchical Supervised Loss A supervised loss is directly hooked to the GT of scene flow, and we leverage multi-level loss functions ...
- **p. 4 / 2 Methodology - extractive PDF cue:** Firstly, to establish the relative positional association between each point-pair, a position encoder PE∗in Euclidean space is introduced as follows, where η denotes concatenation.
- **p. 5 / 2 Methodology - extractive PDF cue:** Then, the initial temporal re-embedding feature is derived using the following formula: TRFij = MLP(η(gj, fi, PEij)).
- **p. 6 / 2 Methodology - extractive PDF cue:** Lastly, we establish a similarity threshold TH and employ function F to penalize points that exhibit a similarity lower than TH: Lcfs = 1 N1 ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames ...
- **p. 2 / 1 Introduction - extractive PDF cue:** (2023), we introduce the Dual Cross Attentive (DCA) Fusion to merge the semantic contexts of point clouds from two frames in latent space, which allows ...
- **p. 3 / 2 Methodology - extractive PDF cue:** 2.3 Global Fusion Flow Embedding The GF module is designed to capture the global relation between consecutive frames during the flow initialization.

## Source Evidence Cues

- **p. 3 / 2 Methodology - extractive PDF cue:** (2019) as the feature extraction backbone to build a pyramid network.
- **p. 3 / 2 Methodology - extractive PDF cue:** 2.2 Hierarchical Feature Extraction The overview of our proposed network is shown in Figure 1.
- **p. 4 / 2 Methodology - extractive PDF cue:** During the dual cross-attentive fusion phase, the semantic context in the latent feature space is obtained for S∗and T ∗through linear networks Q K and ...
- **p. 6 / 2 Methodology - extractive PDF cue:** Cross-frame Feature Similarity (CFS) Loss The semantic features of the points in the warped source frame are similar to those in the surrounding target frame, ...
- **p. 6 / 2 Methodology - extractive PDF cue:** 3 Training Losses 3.1 Hierarchical Supervised Loss A supervised loss is directly hooked to the GT of scene flow, and we leverage multi-level loss functions ...
- **p. 4 / 2 Methodology - extractive PDF cue:** Firstly, to establish the relative positional association between each point-pair, a position encoder PE∗in Euclidean space is introduced as follows, where η denotes concatenation.
- **p. 5 / 2 Methodology - extractive PDF cue:** Then, the initial temporal re-embedding feature is derived using the following formula: TRFij = MLP(η(gj, fi, PEij)).
- **Detected method headings:** 2 Methodology (p. 3); A.1 Network Architecture (p. 12); B.2 Search Methods (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | (2019) as the feature extraction backbone to build a pyramid network. | p. 3 (2 Methodology), p. 3 (2 Methodology) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | 2.2 Hierarchical Feature Extraction The overview of our proposed network is shown in Figure 1. | p. 3 (2 Methodology), p. 4 (2 Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | During the dual cross-attentive fusion phase, the semantic context in the latent feature space is obtained for S∗and T ∗through linear networks ... | p. 4 (2 Methodology), p. 6 (2 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 2 Methodology - extractive PDF cue:** 3 Training Losses 3.1 Hierarchical Supervised Loss A supervised loss is directly hooked to the GT of scene flow, and we leverage multi-level loss functions ...
- **p. 6 / 2 Methodology - extractive PDF cue:** Lastly, we establish a similarity threshold TH and employ function F to penalize points that exhibit a similarity lower than TH: Lcfs = 1 N1 ...
- **p. 5 / 2 Methodology - extractive PDF cue:** As shown in Figure 1, the STR module is followed by LFE, which computes the patch-to-patch cost volume of each point wsi by utilizing the ...
- **p. 5 / 2 Methodology - extractive PDF cue:** Upon acquiring the temporal re-embedding features TRF ∗= {TRF ∗ i } and spatial re-embedding features SRF ∗= {SRF ∗ i } of each point ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (2 Methodology), p. 6 (2 Methodology), p. 5 (2 Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Hierarchical, Feature, Extraction, overview, network, Figure, rely, stereo, RGB-D, images, input, backbone, build, pyramid | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Hierarchical, Feature, Extraction, overview, network, Figure, rely, stereo, RGB-D, images | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Overall, contributions, follows, module, leverages, dual, cross-attentive, mechanism, fuse, align | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Training, Losses, Hierarchical, Supervised, Loss, directly, hooked, scene, flow, leverage | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2 Methodology - extractive PDF cue:** 2.2 Hierarchical Feature Extraction The overview of our proposed network is shown in Figure 1.
- **p. 2 / 1 Introduction - extractive PDF cue:** (2008) rely on stereo or RGB-D images as input.
- **p. 3 / 2 Methodology - extractive PDF cue:** (2019) as the feature extraction backbone to build a pyramid network.
- **p. 4 / 2 Methodology - extractive PDF cue:** AS→T = σ(Q(T ∗) · K(S∗) √da ), (1) FusionS→T = A · V(S∗), (2) where da is the output dimension of linear network K ...
- **p. 5 / 2 Methodology - extractive PDF cue:** The final output is the scene flow sfi, regressed through the FC layer.
- **p. 5 / 2 Methodology - extractive PDF cue:** For each point si in the source frame, its local flow embedding feature, along with the warped coordinates and STRFi are input into the module.
- **p. 6 / 2 Methodology - extractive PDF cue:** (13) We utilize the features of source frame points derived from the last layer of the STR module (the rightmost re-embedding feature in Figure 1) ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 2.5 Spatial Temporal Re-embedding After the warping layer, the spatiotemporal relation between the consecutive frames may change. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Lastly, we establish a similarity threshold TH and employ function F to penalize points that exhibit a similarity lower than TH: Lcfs ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 2 Methodology - extractive PDF cue:** 3 Training Losses 3.1 Hierarchical Supervised Loss A supervised loss is directly hooked to the GT of scene flow, and we leverage multi-level loss functions ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We train our model in an end-to-end manner for 900 epochs (or reached convergence) with batch size 8.
- **p. 7 / 4 Experiments - extractive PDF cue:** The AdamW optimizer Loshchilov and Hutter (2017) with β1 = 0.9 and β2 = 0.99 is used for model tuning during the training phase, with ...
- **p. 8 / 4 Experiments - extractive PDF cue:** Specifically, on the FT3Ds dataset, SSRFlow is on par with previous SOTACheng and Ko (2023) while achieving a 63% reduction in inference time, as listed ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** feature, extraction, backbone, build, pyramid, network, Hierarchical, overview, Figure, During, dual, cross-attentive, fusion, phase, semantic, context, latent, space, obtained, through.
- **Relevant PDF headings:** 2 Methodology (p. 3); A.1 Network Architecture (p. 12); B.2 Search Methods (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | (a) FT3Ds (b) KITTIs (c) SF-KITTI (d) LiDAR-KITTI Figure 4: Comparisons of scene flow datasets, including (a) synthetic stereo, (b) real-world stereo, ... | p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Semantic / temporal fusion | Figure 6: Illustration of results on other datasets of our proposed SSRFlow method. Colors mean the same as Figure 5. More visualization ... | p. 8 (Figure/Table caption), p. 8 (4 Experiments) |
| Robot query / planning handoff | Figure 6: Illustration of results on other datasets of our proposed SSRFlow method. Colors mean the same as Figure 5. More visualization ... | p. 8 (Figure/Table caption), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive PDF cue:** More visualization results are exhibited in Appendix, Sec F FT3Do and KITTIo Similar to the above, we train our model on FT3Do and test on ...
- **p. 9 / 4 Experiments - extractive PDF cue:** Lcfs Llfs KNN Radius FT3Ds EPE3D↓ KITTIs EPE3D↓ ✔ ✔ ✔ 0.0171 0.0109 ✔ ✔ ✔ 0.0169 0.0101 ✔ ✔ ✔ 0.0136 0.0082 ✔ ✔ ...
- **p. 7 / 4 Experiments - extractive PDF cue:** (2019): FT3Ds and KITTIs remove non-corresponding points between consecutive frames, while FT3Do and KITTIo retain occluded points using mask labels.
- **p. 9 / 4 Experiments - extractive PDF cue:** The comprehensive results of the ablation experiments can be found in Table 5, while detailed information is presented in Table 6 and Table 7.
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 10: Ablation studies and analysis of adaption losses. From Figure 9 it can be observed that using only KNN introduces noise points that do ...
- **p. 7 / 4 Experiments - extractive PDF cue:** All models in the table are only trained on FT3Ds and no fine-tuning is applied when tested on KITTIs.
- **p. 6 / 2 Methodology - extractive PDF cue:** The KNN+Radius search strategy effectively mitigates the influence of noise points resulting from occlusion and sparsity in point clouds, as demonstrated in Sec B.2 of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (2 Methodology), p. 3 (2 Methodology), p. 4 (2 Methodology), p. 6 (2 Methodology), p. 6 (2 Methodology), p. 4 (2 Methodology), objective p. 6 (2 Methodology), p. 6 (2 Methodology), p. 5 (2 Methodology), p. 5 (2 Methodology), temporal p. 2 (1 Introduction), p. 5 (2 Methodology), p. 5 (2 Methodology), p. 6 (2 Methodology), p. 1 (Abstract), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
