# Method - LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=MaN2x3O2Rk&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3. Methodology), p. 4 (3. Methodology), p. 3 (3. Methodology), p. 5 (3. Methodology), p. 5 (3. Methodology), p. 6 (3. Methodology)): Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence Feature Extraction Net Voxel Pooling ...

## Method Body Digest

- **p. 4 / 3. Methodology - extractive body cue:** Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence ...
- **p. 4 / 3. Methodology - extractive body cue:** BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D image backbone network ...
- **p. 3 / 3. Methodology - extractive body cue:** In this work, we propose LSSInst, which looks back for the more geometry-aware and finegrained target feature extraction to bridge the adaptation between scene-level and ...
- **p. 5 / 3. Methodology - extractive body cue:** Instance Adapter: Scene-to-instance adaptation For the sake of preserving a coherent and solid semantic consistency between BEV and instance representations, we propose the instance adapter ...
- **p. 5 / 3. Methodology - extractive body cue:** To that end, the proposed adapter module first performs a reprojection of the proposal box coordinates Po ∈RNβ×3 obtained through the BEV proposal head, returning ...
- **p. 6 / 3. Methodology - extractive body cue:** Then the multi-frame features are fed into the sparse temporal encoder fenc, a naive three-layer MLP, for temporal iterative fusion.
- **p. 6 / 3. Methodology - extractive body cue:** Then the per-frame sampled feature Fδt, t ∈{0, 1, ..., Tχ} is formulated by Fδt = Wχ K X k=1 Akt·W ′ χΦ[Fimg, (Mt(pχ -τt ...
- **p. 4 / 3. Methodology - extractive body cue:** Lastly, the model makes the final prediction based on the updated output. briefly introduces the BEV branch.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with ...
- **p. 2 / 1. Introduction - extractive body cue:** With this in mind, we propose the instance adaptor module to establish semantic coherence between the scene and instances and an instance branch for detection.
- **p. 3 / 3. Methodology - extractive body cue:** The overview of our framework is shown in Fig.

## Source Evidence Cues

- **p. 4 / 3. Methodology - extractive body cue:** Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence ...
- **p. 4 / 3. Methodology - extractive body cue:** BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D image backbone network ...
- **p. 3 / 3. Methodology - extractive body cue:** In this work, we propose LSSInst, which looks back for the more geometry-aware and finegrained target feature extraction to bridge the adaptation between scene-level and ...
- **p. 5 / 3. Methodology - extractive body cue:** Instance Adapter: Scene-to-instance adaptation For the sake of preserving a coherent and solid semantic consistency between BEV and instance representations, we propose the instance adapter ...
- **p. 5 / 3. Methodology - extractive body cue:** To that end, the proposed adapter module first performs a reprojection of the proposal box coordinates Po ∈RNβ×3 obtained through the BEV proposal head, returning ...
- **p. 6 / 3. Methodology - extractive body cue:** Then the multi-frame features are fed into the sparse temporal encoder fenc, a naive three-layer MLP, for temporal iterative fusion.
- **p. 6 / 3. Methodology - extractive body cue:** Then the per-frame sampled feature Fδt, t ∈{0, 1, ..., Tχ} is formulated by Fδt = Wχ K X k=1 Akt·W ′ χΦ[Fimg, (Mt(pχ -τt ...
- **Detected method headings:** 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View ... | p. 4 (3. Methodology), p. 4 (3. Methodology) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D ... | p. 4 (3. Methodology), p. 3 (3. Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In this work, we propose LSSInst, which looks back for the more geometry-aware and finegrained target feature extraction to bridge the adaptation ... | p. 3 (3. Methodology), p. 5 (3. Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3. Methodology - extractive body cue:** Lastly, the model makes the final prediction based on the updated output. briefly introduces the BEV branch.
- **p. 4 / 3. Methodology - extractive body cue:** Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence ...
- **p. 5 / 3. Methodology - extractive body cue:** To that end, the proposed adapter module first performs a reprojection of the proposal box coordinates Po ∈RNβ×3 obtained through the BEV proposal head, returning ...
- **p. 5 / 3. Methodology - extractive body cue:** Instance Branch: Looking back for instancelevel representation Given the sequential image features {F t img}Tχ t=0 (Tχ ≤T) from the image backbone network and the ...
- **p. 6 / 3. Methodology - extractive body cue:** Spatiotemporal Sampling and Fusion The sparse feature Fχ with the box embedding Gχ will be updated by the spatial and temporal sampling after being fed ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3. Methodology), p. 4 (3. Methodology), p. 5 (3. Methodology), p. 6 (3. Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | BEV, Branch, Looking, around, scene-level, representation, multi-view, sequential, images, previous, frames, first, input, image | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | BEV, Branch, Looking, around, scene-level, representation, multi-view, sequential, images, previous | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, concluded, follows, LSSInst, two-stage, framework, improves, geometric, details | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Lastly, model, makes, final, prediction, updated, output, briefly, introduces, BEV | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3. Methodology - extractive body cue:** BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D image backbone network ...
- **p. 4 / 3. Methodology - extractive body cue:** Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence ...
- **p. 2 / 1. Introduction - extractive body cue:** The instance branch focuses on fine-grained sparse feature extraction and geometric matching using prepared inputs, such as box embeddings and spatiotemporal sampling and fusion.
- **p. 3 / 3. Methodology - extractive body cue:** In this work, we propose LSSInst, which looks back for the more geometry-aware and finegrained target feature extraction to bridge the adaptation between scene-level and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, unlike LiDAR sensors that provide direct and accurate depth information, detecting objects solely based on camera sensor images poses a significant challenge.
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, it outperforms BEVDet by 5.0%, BEVDepth by 2.2%, BEVStereo by 2.6%, and surpasses the state-ofthe-art LSS-based method SOLOFusion by 1.6%.
- **p. 5 / 3. Methodology - extractive body cue:** With it combined with the sparse instance features, there will be more geometric priors and implicit compensation in subsequent attention interactions.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This branch can be briefly divided into temporally-shared view transformation for BEV generation and BEV sequence fusion. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Backbone, Multi-frame, Multi-view, Features, Images, Previous, Frames, Depth, Distribution, Map, BEV, Feature, Temporal, Encoder, Branch, Temporally-shared, View, Transformation, Sequence, Extraction.
- **Relevant PDF headings:** 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Dataset We conducted extensive experiments on the nuScenes 3D detection benchmark [1], a large-scale dataset in the autonomous driving scene. | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Semantic / temporal fusion | We compared our approach with LSS-based and two-stage state-of-the-art methods on the nuScenes val and test sets. | p. 6 (4.2. Benchmark Results), p. 8 (4.5. Multiplicate Queries Ablations) |
| Robot query / planning handoff | The table reveals that our LSSInst achieves notable improvements in mAP and NDS compared to standalone BEV detectors at a minor cost. | p. 6 (4.3. Generalization Ability and Geometric-Wise), p. 6 (4.2. Benchmark Results) |

## Failure and Ablation Link

- **p. 6 / 4.2. Benchmark Results - extractive body cue:** On the test set, our LSSInst achieves an mAP of 54.6% and an NDS of 62.9% without any additional augmentation, outperforming all LSS-based methods.
- **p. 6 / 4.2. Benchmark Results - extractive body cue:** On the val set, we evaluated the performance of LSSInst against other models with the same setting and without the CBGS strategy and future frame ...
- **p. 7 / 4.3. Generalization Ability and Geometric-Wise - extractive body cue:** Comparison results of LSS-based and two-stage detectors on 3D detection on the nuScenes val set. † denotes the performance without future frames for a fair ...
- **p. 7 / 4.5. Multiplicate Queries Ablations - extractive body cue:** We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 13. Point Ablation Points mAP↑ NDS↑ 1 0.365 0.477 2
- **p. 14 / Figure/Table caption - extractive body cue:** Table 14. Weight Ablation Weight mAP↑ NDS↑ 1 0.365 0.477 2
- **p. 7 / 4.5. Multiplicate Queries Ablations - extractive body cue:** We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3. Methodology), p. 4 (3. Methodology), p. 3 (3. Methodology), p. 5 (3. Methodology), p. 5 (3. Methodology), p. 6 (3. Methodology), objective p. 4 (3. Methodology), p. 4 (3. Methodology), p. 5 (3. Methodology), p. 5 (3. Methodology), p. 6 (3. Methodology), temporal p. 4 (3. Methodology), p. 4 (3. Methodology), p. 6 (3. Methodology), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 5 (3. Methodology).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
