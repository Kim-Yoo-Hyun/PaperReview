# Method - OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 4 (3.1. Notation and Preliminaries), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 3 (3.1. Notation and Preliminaries)): Cross-Modal Target Preparation 2D Image Features 3D Annotations CLIP Image Encoder Adaptive 3D Box Search Predicted Objects Selective Alignment Filter CLIP Image Encoder Adaptive 3D Box Search Grounding DINO + ...

## Method Body Digest

- **p. 4 / 3.1. Notation and Preliminaries - extractive body cue:** Cross-Modal Target Preparation 2D Image Features 3D Annotations CLIP Image Encoder Adaptive 3D Box Search Predicted Objects Selective Alignment Filter CLIP Image Encoder Adaptive 3D ...
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** These alignment features are then used for prompt-based classification by comparing them with text embeddings generated from class prompts, enabling fine-grained recognition of novel objects.
- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** The continuous nonlinear optimization problem is then formulated in standard form: min ω J (ω, Pobj, e, bimg) = J3D(ω, Pobj, e) + J2D(ω, bimg) ...
- **p. 4 / 3.1. Notation and Preliminaries - extractive body cue:** Case 1: Fit for Alignment Case 2: Noisy Alignment Selective Alignment Filter FIT FOR ALIGNMENT OCCLUDED Does not incur alignment losses Incurs alignment losses LiDAR ...
- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** (7) The optimization is governed by a cost function that balances multiple objectives.
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** In traditional LiDAR-based 3D object detection, the objective is to train a detector using inputtarget pairs D = {P, !}.
- **p. 6 / 3.3. Model Architecture - extractive body cue:** Meanwhile, H2SA transforms the 3D object embeddings into predicted alignment features for prompt-based classification.
- **p. 4 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** Additionally, while their cost function considers only point density and multi-view alignment, our method extends it to incorporate surface alignment, further mitigating annotation errors.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig.
- **p. 2 / 1. Introduction - extractive body cue:** More specifically, we introduce the Semantically-Consistent Novel-Object Discovery (SCNOD) module to handle the inherent challenges of noisy cross-modal alignment.
- **p. 4 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** Our method relies on CLIP to classify the object into its corresponding novel class c.

## Source Evidence Cues

- **p. 4 / 3.1. Notation and Preliminaries - extractive body cue:** Cross-Modal Target Preparation 2D Image Features 3D Annotations CLIP Image Encoder Adaptive 3D Box Search Predicted Objects Selective Alignment Filter CLIP Image Encoder Adaptive 3D ...
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** These alignment features are then used for prompt-based classification by comparing them with text embeddings generated from class prompts, enabling fine-grained recognition of novel objects.
- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** The continuous nonlinear optimization problem is then formulated in standard form: min ω J (ω, Pobj, e, bimg) = J3D(ω, Pobj, e) + J2D(ω, bimg) ...
- **p. 4 / 3.1. Notation and Preliminaries - extractive body cue:** Case 1: Fit for Alignment Case 2: Noisy Alignment Selective Alignment Filter FIT FOR ALIGNMENT OCCLUDED Does not incur alignment losses Incurs alignment losses LiDAR ...
- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** (7) The optimization is governed by a cost function that balances multiple objectives.
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** In traditional LiDAR-based 3D object detection, the objective is to train a detector using inputtarget pairs D = {P, !}.
- **p. 6 / 3.3. Model Architecture - extractive body cue:** Meanwhile, H2SA transforms the 3D object embeddings into predicted alignment features for prompt-based classification.
- **Detected method headings:** 3. Method (p. 3); 3.3. Model Architecture (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Cross-Modal Target Preparation 2D Image Features 3D Annotations CLIP Image Encoder Adaptive 3D Box Search Predicted Objects Selective Alignment Filter CLIP Image ... | p. 4 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | These alignment features are then used for prompt-based classification by comparing them with text embeddings generated from class prompts, enabling fine-grained recognition ... | p. 3 (3.1. Notation and Preliminaries), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The continuous nonlinear optimization problem is then formulated in standard form: min ω J (ω, Pobj, e, bimg) = J3D(ω, Pobj, e) ... | p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 4 (3.1. Notation and Preliminaries) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** (7) The optimization is governed by a cost function that balances multiple objectives.
- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** The continuous nonlinear optimization problem is then formulated in standard form: min ω J (ω, Pobj, e, bimg) = J3D(ω, Pobj, e) + J2D(ω, bimg) ...
- **p. 4 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** Additionally, while their cost function considers only point density and multi-view alignment, our method extends it to incorporate surface alignment, further mitigating annotation errors.
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** In traditional LiDAR-based 3D object detection, the objective is to train a detector using inputtarget pairs D = {P, !}.
- **p. 4 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** Given a cross-modal proposal, comprising a 2D bounding box bimg and a set of object points Pobj, the objective is to determine the 3D bounding ...
- **p. 6 / 3.4. Training - extractive body cue:** To train OV-SCAN, our method employs the TransFusionL loss [1].
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Notation and Preliminaries), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 4 (3.1. Notation and Preliminaries), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 6 (3.4. Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | addition, H2SA, head, effectively, aligns, D-to-2D, alignment, pairs, introducing, two-stage, process, validate, OV-SCAN, nuScenes | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | addition, H2SA, head, effectively, aligns, D-to-2D, alignment, pairs, introducing, two-stage | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, main, contributions, follows, present, OV-SCAN, OV-3D, object, detector, benefiting | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | optimization, governed, cost, function, balances, multiple, objectives, continuous, nonlinear, problem | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** In addition, the proposed H2SA head effectively aligns 3D-to-2D alignment pairs by introducing a two-stage alignment process. • We validate OV-SCAN on the nuScenes [2] ...
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** In traditional LiDAR-based 3D object detection, the objective is to train a detector using inputtarget pairs D = {P, !}.
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** Traditional LiDAR-based 3D object detection methods are designed to regress 3D object features O3D →RH given the input point-cloud P.
- **p. 4 / 3.1. Notation and Preliminaries - extractive body cue:** Case 1: Fit for Alignment Case 2: Noisy Alignment Selective Alignment Filter FIT FOR ALIGNMENT OCCLUDED Does not incur alignment losses Incurs alignment losses LiDAR ...
- **p. 1 / 1. Introduction - extractive body cue:** In these offline pipelines, OV-2D detectors such as Grounding DINO [21] and OWL-ViT [27] first generate 2D proposals from multiview images, which are typically paired ...
- **p. 4 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** For each LiDAR frame, novel object proposals P2D are generated on K multi-view images, capturing objects from multiple perspectives.
- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** These transformations project the 3D bounding box ω into its 2D counterpart in the image space using P3D↔2D.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We assume that each LiDAR frame is accompanied by a set of K images from different perspectives (multi-view), represented as I = ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The complete set for a given frame is P2D = !K k=1 P2D,k. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | OV-SCAN is trained on 8 NVIDIA V100 GPUs with a batch size of four for 20 epochs. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Notation and Preliminaries - extractive body cue:** Cross-Modal Target Preparation 2D Image Features 3D Annotations CLIP Image Encoder Adaptive 3D Box Search Predicted Objects Selective Alignment Filter CLIP Image Encoder Adaptive 3D ...
- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** The continuous nonlinear optimization problem is then formulated in standard form: min ω J (ω, Pobj, e, bimg) = J3D(ω, Pobj, e) + J2D(ω, bimg) ...
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** In traditional LiDAR-based 3D object detection, the objective is to train a detector using inputtarget pairs D = {P, !}.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** OV-SCAN is trained on 8 NVIDIA V100 GPUs with a batch size of four for 20 epochs.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** OV-SCAN-Fusion is trained for five additional epochs using a cosine annealing schedule initialized at a learning rate of 0.0001.
- **p. 4 / 3.1. Notation and Preliminaries - extractive body cue:** Cross-Modal Target Preparation 2D Image Features 3D Annotations CLIP Image Encoder Adaptive 3D Box Search Predicted Objects Selective Alignment Filter CLIP Image Encoder Adaptive 3D ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Cross-Modal, Target, Preparation, Image, Features, Annotations, CLIP, Encoder, Adaptive, Box, Search, Predicted, Objects, Selective, Alignment, Filter, Grounding, DINO, SAM, Ground.
- **Relevant PDF headings:** 3. Method (p. 3); 3.3. Model Architecture (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Our OV-3D object detection experiments are conducted on the nuScenes [2] and KITTI [12] datasets. | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Main Results) |
| Semantic / temporal fusion | OV-SCAN outperforms OV-3DET [25] and ImOV3D [42] in the overall metric, achieving comparable results to ImOV3D [42] in the car category while ... | p. 7 (4.2. Main Results), p. 8 (4.3. Ablation Studies) |
| Robot query / planning handoff | A simple occlusion filter with a fixed threshold ςocc yields a notable performance gain, while class-based thresholds achieve the highest improvement (+1.7 ... | p. 8 (4.3. Ablation Studies), p. 7 (4.2. Main Results) |

## Failure and Ablation Link

- **p. 8 / 4.3. Ablation Studies - extractive body cue:** This variant removes the classification loss term, merges TransFusion-L's class heatmaps into a single class-agnostic heatmap, and replaces the text-guided alignment network with a simple ...
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Ablations on Adaptive 3D Box Search.
- **p. 7 / 4.2. Main Results - extractive body cue:** Without being given 3D human-annotations, OV-SCAN achieves an AP score above 60 for both car and pedestrian categories.
- **p. 8 / 4.4. Limitations - extractive body cue:** The primary limitation of SC-NOD is its limited annotation recovery (Fig.
- **p. 8 / 4.4. Limitations - extractive body cue:** These insights motivate future work exploring alternative methods less dependent on 2D proposals and anchor-free box-parameterization strategies.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. 3D Annotation Errors. Common 3D annotation errors during box parametrization, including but not limited to, poor L- shape fitting, misinterpreted surfaces, and misaligned ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases result in an ambiguous 2D image feature. ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 4 (3.1. Notation and Preliminaries), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 3 (3.1. Notation and Preliminaries), objective p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 3 (3.1. Notation and Preliminaries), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 6 (3.4. Training), temporal p. 3 (3.1. Notation and Preliminaries), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 8 (4.3. Ablation Studies).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
