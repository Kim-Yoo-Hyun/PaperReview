# Method - GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7jXxQ9bGoU; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/246879. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (20560 M), p. 1 (ABSTRACT), p. 6 (6 Cameras), p. 2 (20560 M), p. 1 (ABSTRACT), p. 6 (6 Cameras)): Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally aggregated through the Gaussian mixture ...

## Method Body Digest

- **p. 2 / 20560 M - extractive body cue:** Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally ...
- **p. 1 / ABSTRACT - extractive body cue:** However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception.
- **p. 6 / 6 Cameras - extractive body cue:** We then project the 3D reference points onto the BEV feature map, where each Gaussian query qi ↔Qi is updated through deformable attention, expressed as: ...
- **p. 2 / 20560 M - extractive body cue:** To address these challenges, we introduce a fusion approach based on 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) to achieve more fine-grained information modeling ...
- **p. 1 / ABSTRACT - extractive body cue:** To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on ...
- **p. 6 / 6 Cameras - extractive body cue:** To update the Gaussian properties, we propose an iterative optimization strategy of predicting offsets instead of predicting a set of new Gaussian distributions as adopted ...
- **p. 5 / 6 Cameras - extractive body cue:** This encoder includes a deformable attention with Gaussian module and a Gaussian Updating module.
- **p. 2 / 20560 M - extractive body cue:** BEV directly discretizes and quantizes data, leading to inevitable information loss.

## Design Rationale

- **p. 2 / 20560 M - extractive body cue:** Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally ...
- **p. 2 / 20560 M - extractive body cue:** To address these challenges, we introduce a fusion approach based on 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) to achieve more fine-grained information modeling ...
- **p. 1 / ABSTRACT - extractive body cue:** The bird's-eye view (BEV) representation enables multi-sensor features to be fused within a unified space, serving as the primary approach for achieving comprehensive 3D perception.

## Source Evidence Cues

- **p. 2 / 20560 M - extractive body cue:** Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally ...
- **p. 1 / ABSTRACT - extractive body cue:** However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception.
- **p. 6 / 6 Cameras - extractive body cue:** We then project the 3D reference points onto the BEV feature map, where each Gaussian query qi ↔Qi is updated through deformable attention, expressed as: ...
- **p. 2 / 20560 M - extractive body cue:** To address these challenges, we introduce a fusion approach based on 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) to achieve more fine-grained information modeling ...
- **p. 1 / ABSTRACT - extractive body cue:** To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on ...
- **p. 6 / 6 Cameras - extractive body cue:** To update the Gaussian properties, we propose an iterative optimization strategy of predicting offsets instead of predicting a set of new Gaussian distributions as adopted ...
- **p. 5 / 6 Cameras - extractive body cue:** This encoder includes a deformable attention with Gaussian module and a Gaussian Updating module.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian ... | p. 2 (20560 M), p. 1 (ABSTRACT) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal ... | p. 1 (ABSTRACT), p. 6 (6 Cameras) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We then project the 3D reference points onto the BEV feature map, where each Gaussian query qi ↔Qi is updated through deformable ... | p. 6 (6 Cameras), p. 2 (20560 M) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 20560 M - extractive body cue:** Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally ...
- **p. 1 / ABSTRACT - extractive body cue:** However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception.
- **p. 2 / 20560 M - extractive body cue:** BEV directly discretizes and quantizes data, leading to inevitable information loss.
- **p. 7 / 6 Cameras - extractive body cue:** 3.5 PERCEPTION TASK SETUP Without loss of generality, we follow BEVFusion (Liu et al., 2023b), GaussianFusion can be applied to most 3D perception tasks based ...
- **p. 6 / 6 Cameras - extractive body cue:** To update the Gaussian properties, we propose an iterative optimization strategy of predicting offsets instead of predicting a set of new Gaussian distributions as adopted ...
- **p. 1 / ABSTRACT - extractive body cue:** To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 1 (ABSTRACT), p. 2 (20560 M), p. 2 (20560 M), p. 7 (6 Cameras), p. 1 (ABSTRACT), p. 5 (6 Cameras).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | However, discrete, grid, representation, BEV, leads, significant, detail, loss, limits, feature, alignment, cross-modal, information | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | However, discrete, grid, representation, BEV, leads, significant, detail, loss, limits | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Main, contributions, follows, first, unified, Gaussian, representation, multi-modal, fusion, framework | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Main, contributions, follows, first, unified, Gaussian, representation, multi-modal, fusion, framework | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / ABSTRACT - extractive body cue:** However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception.
- **p. 2 / 20560 M - extractive body cue:** During feature extraction, perception data are projected onto a fixed-resolution BEV grid, which compresses spatial information.
- **p. 2 / 20560 M - extractive body cue:** Additionally, BEV fusion strategies often rely on simple feature concatenation or weighted summation, which are insufficient for effective cross-modal feature interaction and alignment, ultimately leading ...
- **p. 4 / 6 Cameras - extractive body cue:** Specifically, inspired by (Huang & Huang, 2022b;a; Liu et al., 2023b; Philion & Fidler, 2020), given surround camera input features Fc,i ↔RC↑Hc↑Wc, i = 1, ...
- **p. 4 / 6 Cameras - extractive body cue:** The image features Fc,i are processed through a context network composed of multiple convolutional layers to obtain the semantic features F ↓ c,i.
- **p. 5 / 6 Cameras - extractive body cue:** Since directly extracting information from the massive raw lidar point clouds to construct 3D Gaussian representations is both difficult and computationally intensive, grid-based representations offer ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Fusing complementary signals captured by different sensors is essential for autonomous driving perception systems.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In Equation (5), the mean µm, scale sm, rotation rm, and query qm encompass not only the multi-modal (image and LiDAR) Gaussians ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Benefiting from the unified architecture, it achieves an excellent performance of 71.7 mAP while maintaining lower inference latency (132 ms) and memory ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In Equation (5), the mean µm, scale sm, rotation rm, and query qm encompass not only the multi-modal (image and LiDAR) Gaussians ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Benefiting from the unified architecture, it achieves an excellent performance of 71.7 mAP while maintaining lower inference latency (132 ms) and memory ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Main, contributions, follows, first, unified, Gaussian, representation, multi-modal, fusion, framework, where, cross-view, cross-modal, representations, naturally, aggregated, through, mixture, model, progressive.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | It is a large-scale multimodal dataset officially split into 700/150/150 scenes for training, validation, and testing, respectively. | p. 7 (4.1 DATASET), p. 7 (4.1 DATASET) |
| Semantic / temporal fusion | In addition, compared with recent SOTA fusion works, such as UniTR (Wang et al., 2023a), EA-LSS (Hu et al., 2023b), and FusionFormer-S ... | p. 7 (4.1 DATASET), p. 8 (4.1 DATASET) |
| Robot query / planning handoff | Experimental results show that, compared to BEVFusion4D (Liu et al., 2023b), our temporal variant GaussianFusion-T achieves significant improvements. | p. 8 (4.1 DATASET), p. 9 (4.1 DATASET) |

## Failure and Ablation Link

- **p. 9 / 4.1 DATASET - extractive body cue:** Share Separate DA.G PE Offset NDS mAP ↭ ↭ ↭ ↭ 74.0 71.7 ↭ ↭ ↭ 73.6 71.1 ↭ ↭ ↭ ↭ 73.4 71.0 ↭ ...
- **p. 7 / 4.1 DATASET - extractive body cue:** To highlight the effect of Gaussian representation, we only compare the BEV-based method.
- **p. 8 / 4.1 DATASET - extractive body cue:** Experimental results show that, compared to BEVFusion4D (Liu et al., 2023b), our temporal variant GaussianFusion-T achieves significant improvements.
- **p. 8 / 4.1 DATASET - extractive body cue:** Moreover, even without sophisticated temporal modeling, GaussianFusion-T achieves competitive NDS against advanced temporal fusion methods such as SparseLIF-T (Zhang et al., 2024a).
- **p. 9 / 4.1 DATASET - extractive body cue:** Gaussian Initialization NDS mAP Random Initialization 71.2 68.3 Backward Projection 72.4 70.0 Lidar Projection 73.6 71.1 Forward Projection 74.0 71.7 Table 9: Ablation of the ...
- **p. 10 / 4.1 DATASET - extractive body cue:** We then conduct an ablation study on the deformable attention module.
- **p. 10 / 4.1 DATASET - extractive body cue:** Results show that deformable attention with Gaussian priors outperforms the vanilla variant by +0.4 NDS, demonstrating that the shape prior encoded by Gaussians facilitates model ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (20560 M), p. 1 (ABSTRACT), p. 6 (6 Cameras), p. 2 (20560 M), p. 1 (ABSTRACT), p. 6 (6 Cameras), objective p. 2 (20560 M), p. 1 (ABSTRACT), p. 2 (20560 M), p. 7 (6 Cameras), p. 6 (6 Cameras), p. 1 (ABSTRACT), temporal p. 8 (4.1 DATASET), p. 8 (4.1 DATASET), p. 10 (4.1 DATASET), p. 9 (4.1 DATASET), p. 9 (4.1 DATASET), p. 10 (4.1 DATASET).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
