# Method - OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction)): Mask: Given a 3D point cloud, the first part of OpenIns3D learns class-agnostic mask proposals with a Mask Proposal Module (MPM).

## Method Body Digest

- **p. 3 / 1 Introduction - extractive PDF cue:** Mask: Given a 3D point cloud, the first part of OpenIns3D learns class-agnostic mask proposals with a Mask Proposal Module (MPM).
- **p. 2 / 1 Introduction - extractive PDF cue:** This means that posed 2D images, associated depth maps and camera models need to be accessible as inputs to the network.
- **p. 2 / 1 Introduction - extractive PDF cue:** These works leverage well-aligned 2D images and 3D point clouds to conduct feature distillation or employ 2D caption models to construct 3D-text pairs.
- **p. 4 / 1 Introduction - extractive PDF cue:** Reconstructed 3D RGB Depth Camera models Input Reconstructed 3D RGB Depth Camera models Input Reconstructed 3D Input Bbox /Mask proposal 3D backbone 2D backbone 2D ...
- **p. 4 / 1 Introduction - extractive PDF cue:** 3: Four Categories of Open-Vocabulary 3D Scene Understanding Models. a) 3D feature distillation frameworks, where 2D images are used as a bridge to distil language-aligned ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The design of OpenIns3D also allows 2D detectors to be changed without the need for retraining.
- **p. 3 / 1 Introduction - extractive PDF cue:** These images are specifically designed to encompass part or all of the relevant masks, aiming to minimize the need for multiple renderings.
- **p. 2 / 1 Introduction - extractive PDF cue:** Thanks to internet-scale image-text datasets, significant progress has been made in 2D image open-vocabulary understanding [4, 7, 11, 16, 24, 33, 38, 39].

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** To this end, we introduce OpenIns3D, a framework designed to effectively perform 3D open-vocabulary scene understanding tasks without relying on 2D aligned images.
- **p. 4 / 1 Introduction - extractive PDF cue:** In summary, our contributions are: - OpenIns3D employs a distinct pipeline that operates without the need for well-aligned images.
- **p. 2 / 1 Introduction - extractive PDF cue:** While the development of 3D closed-set understanding is relatively mature, scene understanding in an open-vocabulary setting is still in its infancy.

## Source Evidence Cues

- **p. 3 / 1 Introduction - extractive PDF cue:** Mask: Given a 3D point cloud, the first part of OpenIns3D learns class-agnostic mask proposals with a Mask Proposal Module (MPM).
- **p. 2 / 1 Introduction - extractive PDF cue:** This means that posed 2D images, associated depth maps and camera models need to be accessible as inputs to the network.
- **p. 2 / 1 Introduction - extractive PDF cue:** These works leverage well-aligned 2D images and 3D point clouds to conduct feature distillation or employ 2D caption models to construct 3D-text pairs.
- **p. 4 / 1 Introduction - extractive PDF cue:** Reconstructed 3D RGB Depth Camera models Input Reconstructed 3D RGB Depth Camera models Input Reconstructed 3D Input Bbox /Mask proposal 3D backbone 2D backbone 2D ...
- **p. 4 / 1 Introduction - extractive PDF cue:** 3: Four Categories of Open-Vocabulary 3D Scene Understanding Models. a) 3D feature distillation frameworks, where 2D images are used as a bridge to distil language-aligned ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The design of OpenIns3D also allows 2D detectors to be changed without the need for retraining.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Mask: Given a 3D point cloud, the first part of OpenIns3D learns class-agnostic mask proposals with a Mask Proposal Module (MPM). | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | This means that posed 2D images, associated depth maps and camera models need to be accessible as inputs to the network. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | These works leverage well-aligned 2D images and 3D point clouds to conduct feature distillation or employ 2D caption models to construct 3D-text ... | p. 2 (1 Introduction), p. 4 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1 Introduction - extractive PDF cue:** These images are specifically designed to encompass part or all of the relevant masks, aiming to minimize the need for multiple renderings.
- **p. 2 / 1 Introduction - extractive PDF cue:** Thanks to internet-scale image-text datasets, significant progress has been made in 2D image open-vocabulary understanding [4, 7, 11, 16, 24, 33, 38, 39].
- **p. 3 / 1 Introduction - extractive PDF cue:** Snap: Multiple synthetic scene-level images are generated with calibrated and optimized camera poses and intrinsic parameters.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | achieves, state-of-the-art, across, range, benchmarks, possesses, ability, comprehend, highly, complex, input, queries, Snap, Lookup | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | achieves, state-of-the-art, across, range, benchmarks, possesses, ability, comprehend, highly, complex | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, OpenIns3D, framework, designed, effectively, perform, open-vocabulary, scene, understanding, tasks | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | images, specifically, designed, encompass, part, relevant, masks, aiming, minimize, need | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 1 Introduction - extractive PDF cue:** This approach achieves state-of-the-art results across a range of benchmarks and possesses the ability to comprehend highly complex input queries. - The proposed "Snap and ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This means that posed 2D images, associated depth maps and camera models need to be accessible as inputs to the network.
- **p. 2 / 1 Introduction - extractive PDF cue:** In cases where point clouds are obtained from the registration of multiple scans from different sensors or are converted from 3D simulations/CAD models [12, 21], ...
- **p. 3 / 1 Introduction - extractive PDF cue:** To control the quality of the mask, MPM proposes a learnable Mask Scoring module to predict the quality of each mask output and implements a ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Lastly, when converting mask proposals into 3D bounding boxes, OpenIns3D also achieved state-of-the-art results in open-vocabulary object detection (OVOD) on ScanNet, outperforming previous image-dependent methods ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Reconstructed 3D RGB Depth Camera models Input Reconstructed 3D RGB Depth Camera models Input Reconstructed 3D Input Bbox /Mask proposal 3D backbone 2D backbone 2D ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Switching from Grounding Dino [19] to the latest ODISE [33] also brings gains in performance, indicating that the OpenIns3D framework can easily ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The OpenIns3D framework employs a "Mask-Snap-Lookup" scheme. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 Introduction - extractive PDF cue:** The design of OpenIns3D also allows 2D detectors to be changed without the need for retraining.
- **p. 13 / 4 Experiments - extractive PDF cue:** OpenIns3D requires less rendering and inference time.
- **p. 13 / 4 Experiments - extractive PDF cue:** OpenIns3D: 3D Open-vocabulary Instance Segmentation 13 Table 7: Rendering and Inference Time Ablations.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Mask, Given, point, cloud, first, part, OpenIns3D, learns, class-agnostic, proposals, Proposal, Module, MPM, means, posed, images, associated, depth, maps, camera.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Model 2D AP AP50 AP25 OpenScene [23] (2D Fusion) ✓ 10.9 15.6 17.3 OpenScene [23] (2D/3D Ens.) ✓ 8.2 10.4 13.3 OpenMask3D ... | p. 12 (4 Experiments), p. 11 (4 Experiments) |
| Semantic / temporal fusion | For STPLS3D, we compared OpenIns3D with baseline models whose classification module is PointCLIP and PointCLIPV2 [43] (Table 5). | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Robot query / planning handoff | Significant improvements are achieved on the S3DIS dataset, and competitive results are observed on ScanNetv2 (B/N: Base/Novel). | p. 11 (4 Experiments), p. 12 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive PDF cue:** For the S3DIS, ScanNetv2, Scannet200, and STPLS datasets, the MPM module is trained without utilizing any category labels, and
- **p. 10 / 4 Experiments - extractive PDF cue:** The top 0.5 m of the scene is removed for S3DIS, as the rooms are enclosed.
- **p. 12 / 4 Experiments - extractive PDF cue:** 5.2 Ablation study Mask quality ablation.
- **p. 13 / 4 Experiments - extractive PDF cue:** Projection and 2D backbone ablation.
- **p. 13 / 4 Experiments - extractive PDF cue:** OpenIns3D: 3D Open-vocabulary Instance Segmentation 13 Table 7: Rendering and Inference Time Ablations.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 1. In summary, our contributions are: - OpenIns3D employs a distinct pipeline that operates without the need for well-aligned images. This approach achieves state-of-the-art ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 10: Cross-domain Ablation. We trained and tested OpenIns3D on two differ- ent datasets to examine its cross-domain capability. While S3DIS and ScanNetV2 have non-overlapping ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), objective p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), temporal p. 13 (4 Experiments), p. 1 (Front matter), p. 1 (Front matter), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
