# Method - Details Matter for Indoor Open-vocabulary 3D Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.2. Open-Vocabulary Instance Classification), p. 3 (3.1. Image-based Proposal Generation), p. 5 (3.2. Open-Vocabulary Instance Classification), p. 3 (3. Method), p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation)): Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset of images with the highest visibility for multiscale ...

## Method Body Digest

- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset of images with ...
- **p. 3 / 3.1. Image-based Proposal Generation - extractive body cue:** Leveraging VFMs [28, 35, 43], image-based proposals provide a complementary approach for detecting novel classes not covered during the training of the 3D instance segmentation ...
- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** Alpha-CLIP incorporates object masks as an additional input to guide the model's attention.
- **p. 3 / 3. Method - extractive body cue:** For point cloudbased 3D proposals, we utilize pre-trained 3D instance segmentation models [38, 45] and discard the class predictions, retaining only the class-agnostic masks.
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** Matching tracklets with a new observation.
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** To address this, we merge these partial proposals into a complete 3D representation.
- **p. 5 / 3.1. Image-based Proposal Generation - extractive body cue:** Using this ratio, we construct an inclusion cost matrix Cincl ∈[0, 1]K×K, which is a full matrix since the inclusion ratio is asymmetric.
- **p. 5 / 3.1. Image-based Proposal Generation - extractive body cue:** For each merging iteration, we compute IOU between a pair of 3D proposals, constructing a cost matrix Cmerge ∈[0, 1]K×K that is a strictly upper-triangular ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions and ...
- **p. 1 / 1. Introduction - extractive body cue:** Examples of open-vocabulary predictions from our method in the ScanNet200 dataset [7].
- **p. 1 / 1. Introduction - extractive body cue:** Our method effectively retrieves instances based on functional descriptions (e.g., drink water, heat mac & cheese) and object attributes (e.g., red chair). dicted proposals into ...

## Source Evidence Cues

- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset of images with ...
- **p. 3 / 3.1. Image-based Proposal Generation - extractive body cue:** Leveraging VFMs [28, 35, 43], image-based proposals provide a complementary approach for detecting novel classes not covered during the training of the 3D instance segmentation ...
- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** Alpha-CLIP incorporates object masks as an additional input to guide the model's attention.
- **p. 3 / 3. Method - extractive body cue:** For point cloudbased 3D proposals, we utilize pre-trained 3D instance segmentation models [38, 45] and discard the class predictions, retaining only the class-agnostic masks.
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** Matching tracklets with a new observation.
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** To address this, we merge these partial proposals into a complete 3D representation.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset ... | p. 5 (3.2. Open-Vocabulary Instance Classification), p. 3 (3.1. Image-based Proposal Generation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Leveraging VFMs [28, 35, 43], image-based proposals provide a complementary approach for detecting novel classes not covered during the training of the ... | p. 3 (3.1. Image-based Proposal Generation), p. 5 (3.2. Open-Vocabulary Instance Classification) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Alpha-CLIP incorporates object masks as an additional input to guide the model's attention. | p. 5 (3.2. Open-Vocabulary Instance Classification), p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.1. Image-based Proposal Generation - extractive body cue:** Using this ratio, we construct an inclusion cost matrix Cincl ∈[0, 1]K×K, which is a full matrix since the inclusion ratio is asymmetric.
- **p. 5 / 3.1. Image-based Proposal Generation - extractive body cue:** For each merging iteration, we compute IOU between a pair of 3D proposals, constructing a cost matrix Cmerge ∈[0, 1]K×K that is a strictly upper-triangular ...
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** Moreover, we apply this merging iteratively so that we can progressively enlarge instances at each iteration.
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** If the highest sIOU exceeds a predefined threshold τ tracking, the new observation is assigned to the corresponding tracklet for update.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, proposal, visual, encoder, Alpha-CLIP, project, onto, images, select, subset, highest, visibility, multiscale, feature | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, proposal, visual, encoder, Alpha-CLIP, project, onto, images, select, subset | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, carefully, combine, existing, concepts, refine, proposal, generation | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | ratio, construct, inclusion, cost, matrix, Cincl, full, since, asymmetric, merging | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset of images with ...
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** Matching tracklets with a new observation.
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** We conduct frame-wise sIOU comparisons between a new observation and each tracked instance in tracklets.
- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** We adopt a similar approach to OpenMask3D [49] for visual embedding extraction.
- **p. 3 / 3. Method - extractive body cue:** We generate proposals from both images and point clouds.
- **p. 3 / 3. Method - extractive body cue:** The task of OV-3DIS is to predict a list of 3D instance masks m ∈{0, 1}K×N that correspond to a list of user queries Q ...
- **p. 6 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** We evaluate methods under three settings: image-based 3D proposals only (i.e., 2D only), point cloud-based 3D proposals only (i.e., 3D only), and a combination of ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Each object region is then lifted to 3D point clouds and temporally aggregated across frames to find complete 3D masks. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Image-based 3D proposal generation [37, 39, 63] involves many design choices in three steps: 1) frame-wise 2D object grounding, 2) lifting 2D ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Image-based Proposal Generation - extractive body cue:** Leveraging VFMs [28, 35, 43], image-based proposals provide a complementary approach for detecting novel classes not covered during the training of the 3D instance segmentation ...
- **p. 3 / 3. Method - extractive body cue:** For point cloudbased 3D proposals, we utilize pre-trained 3D instance segmentation models [38, 45] and discard the class predictions, retaining only the class-agnostic masks.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Given, proposal, visual, encoder, Alpha-CLIP, project, onto, images, select, subset, highest, visibility, multiscale, feature, extraction, Leveraging, VFMs, image-based, proposals, provide.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Replica is a synthetic dataset created from digital replicas of real-world scenes, featuring 48 object classes across 8 different scenes. | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Semantic / temporal fusion | As reported in Table 2, our method consistently outperforms the baselines by a large margin in each experiment setting: 2D-only, 3D-only, and ... | p. 7 (4.2. Quantitative Results), p. 7 (4.2. Quantitative Results) |
| Robot query / planning handoff | These visual results are consistent with the recall metrics: Open3DIS and OpenYOLO3D achieve the mAR of 43.3% and 47.7%, respectively, whereas our ... | p. 7 (4.3. Qualitative Results), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Effectiveness of 3D proposal refinement. Red boxes indicate the object of interest, and segments of different colors de- note 3D superpoints. Without refinement, ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** This is because overlap removal effectively separates masks spanning multiple instances into each instance or partial masks, which later can be merged/removed.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Visualization of merged and removed proposals in the ScanNet200 dataset. Overlapping and noisy proposals often emerge after instance tracking. We effectively handle these ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For the Replica dataset, we adjust τ merge to 0.7 and disable multiview consensus ratiobased filtering, as Replica is a synthetic dataset without projection errors.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Full ablation study on all three datasets can be found in the supplementary materials.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Examples of open-vocabulary predictions from our method in the ScanNet200 dataset [7]. Our method effectively retrieves instances based on functional descriptions (e.g., drink ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of image-based 3D proposal generation. We first remove overlaps between 2D predictions within each frame and lift them to 3D point cloud ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.2. Open-Vocabulary Instance Classification), p. 3 (3.1. Image-based Proposal Generation), p. 5 (3.2. Open-Vocabulary Instance Classification), p. 3 (3. Method), p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation), objective p. 5 (3.1. Image-based Proposal Generation), p. 5 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation), temporal p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Method), p. 3 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
