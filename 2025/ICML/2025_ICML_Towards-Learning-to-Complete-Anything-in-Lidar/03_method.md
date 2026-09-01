# Method - Towards Learning to Complete Anything in Lidar

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vWPzKn6usZ; PDF retrieval source: https://openreview.net/pdf/8fbe2a59d85d4f1be15c6351679cc46349d858df.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.2. Learning To Complete Objects), p. 4 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects), p. 4 (3.2. Learning To Complete Objects), p. 3 (3. Method)): The Transformer decoder then predicts segmentation masks over the completed scene and regresses CLIP features. tive decoder (●) uses three decoding blocks D1:L estimating occupancy at three different resolution levels ...

## Method Body Digest

- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** The Transformer decoder then predicts segmentation masks over the completed scene and regresses CLIP features. tive decoder (●) uses three decoding blocks D1:L estimating occupancy ...
- **p. 4 / 3.2. Learning To Complete Objects - extractive PDF cue:** The backbone consists of a sparse feature encoder (●) (Choy et al., 2019) followed by a dense 3D convolutional block (●).
- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** The transformer decoder produces instance masks and CLIP features, supervised by the mask-loss (Lmask: binary-cross entropy and Dice loss) and the feature distillation loss (LCLIP: ...
- **p. 4 / 3.2. Learning To Complete Objects - extractive PDF cue:** (2024) and employ a sparse-generative 3D U-Net (Dai et al., 2018) architecture that estimates scene-level occupancy, and a Transformer instance decoder (Cheng et al., 2022) ...
- **p. 3 / 3. Method - extractive PDF cue:** 2) that mines pairs of partially observed point clouds with completed 3D shapes and CLIP features (Radford et al., 2021), and (ii) a model for ...
- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** During each training iteration, the generative decoder produces coarse-to-fine voxel grids for each scale L, supervised with a binary occupancy loss (Locc: binary-cross entropy wrt. ...
- **p. 4 / 3.2. Learning To Complete Objects - extractive PDF cue:** CAL takes a single input Lidar scan P, providing sparse and incomplete observations of scene geometry (Fig.
- **p. 3 / 3. Method - extractive PDF cue:** Semantic Scene Completion (SSC) (Behley et al., 2019) assumes input in the form of a single Lidar point cloud P = {pn}N n=1, pn ∈R4, ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** We propose the first method for Zero-Shot Lidar Panoptic Scene Completion.
- **p. 2 / 1. Introduction - extractive PDF cue:** 1, 2⃝) and demonstrate that our method can recognize and complete arbitrary objects not captured in canonical semantic vocabularies (Fig.
- **p. 4 / 3. Method - extractive PDF cue:** Our method takes a semantic vocabulary consisting of free-form semantic class descriptions only at test time.

## Source Evidence Cues

- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** The Transformer decoder then predicts segmentation masks over the completed scene and regresses CLIP features. tive decoder (●) uses three decoding blocks D1:L estimating occupancy ...
- **p. 4 / 3.2. Learning To Complete Objects - extractive PDF cue:** The backbone consists of a sparse feature encoder (●) (Choy et al., 2019) followed by a dense 3D convolutional block (●).
- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** The transformer decoder produces instance masks and CLIP features, supervised by the mask-loss (Lmask: binary-cross entropy and Dice loss) and the feature distillation loss (LCLIP: ...
- **p. 4 / 3.2. Learning To Complete Objects - extractive PDF cue:** (2024) and employ a sparse-generative 3D U-Net (Dai et al., 2018) architecture that estimates scene-level occupancy, and a Transformer instance decoder (Cheng et al., 2022) ...
- **p. 3 / 3. Method - extractive PDF cue:** 2) that mines pairs of partially observed point clouds with completed 3D shapes and CLIP features (Radford et al., 2021), and (ii) a model for ...
- **Detected method headings:** 3. Method (p. 3); 4.4. CAL model analysis (p. 9)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The Transformer decoder then predicts segmentation masks over the completed scene and regresses CLIP features. tive decoder (●) uses three decoding blocks ... | p. 5 (3.2. Learning To Complete Objects), p. 4 (3.2. Learning To Complete Objects) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The backbone consists of a sparse feature encoder (●) (Choy et al., 2019) followed by a dense 3D convolutional block (●). | p. 4 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The transformer decoder produces instance masks and CLIP features, supervised by the mask-loss (Lmask: binary-cross entropy and Dice loss) and the feature ... | p. 5 (3.2. Learning To Complete Objects), p. 4 (3.2. Learning To Complete Objects) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** During each training iteration, the generative decoder produces coarse-to-fine voxel grids for each scale L, supervised with a binary occupancy loss (Locc: binary-cross entropy wrt. ...
- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** The transformer decoder produces instance masks and CLIP features, supervised by the mask-loss (Lmask: binary-cross entropy and Dice loss) and the feature distillation loss (LCLIP: ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | CAL, takes, single, input, Lidar, scan, providing, sparse, incomplete, observations, scene, geometry, Fig, Semantic | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | CAL, takes, single, input, Lidar, scan, providing, sparse, incomplete, observations | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | first, Zero-Shot, Lidar, Panoptic, Scene, Completion, demonstrate, recognize, complete, arbitrary | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | During, training, iteration, generative, decoder, produces, coarse-to-fine, voxel, grids, scale | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Learning To Complete Objects - extractive PDF cue:** CAL takes a single input Lidar scan P, providing sparse and incomplete observations of scene geometry (Fig.
- **p. 3 / 3. Method - extractive PDF cue:** Semantic Scene Completion (SSC) (Behley et al., 2019) assumes input in the form of a single Lidar point cloud P = {pn}N n=1, pn ∈R4, ...
- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** Given a Lidar point cloud as input, CAL produces a set of object instance masks over the voxel grid and a CLIP feature for each ...
- **p. 4 / 3.1. Mining 3D Shape Priors From Unlabeled Data - extractive PDF cue:** The output is a set of ≤K class-agnostic masklets, providing temporal instance association in the video v.
- **p. 2 / 1. Introduction - extractive PDF cue:** This is far below the label diversity and scale compared to state-of-the-art image-based datasets (Kirillov et al., 2023).
- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** The input to the Transformer decoder (●) is a set of learnable queries that interact with the multi-resolution features learned by the generative decoder in ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Objects may be only partially completed, and not all objects are static - however, in practice, we learn to fully complete static and dynamic objects ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We propagate the masks from the reference frame at time t to the frames within the given temporal window [t -Tbw, t ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Once masks m3D t,k are localized in the Lidar sequence, we project them into the reference coordinate frame using known ego-poses and ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Transformer, decoder, then, predicts, segmentation, masks, over, completed, scene, regresses, CLIP, features, tive, uses, three, decoding, blocks, estimating, occupancy, different.
- **Relevant PDF headings:** 3. Method (p. 3); 4.4. CAL model analysis (p. 9).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We quantitatively assess CAL's zero-shot completion and recognition performance on Semantic Scene Completion (SSC) (Behley et al., 2019) and Panoptic Scene Completion ... | p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Semantic / temporal fusion | As there are no prior works tackling Lidar PSC in zero-shot setting, we construct two baselines adhering to the following criteria for ... | p. 7 (4.2. Experimental results), p. 7 (4.2. Experimental results) |
| Robot query / planning handoff | While the best results are achieved with Tfw = 64, Tbw = 16, w = 1 (13.10 PQ†), we use the combination ... | p. 8 (4.3. Pseudo-labeling engine analysis), p. 7 (4.2. Experimental results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. CRF refinement ablation. We evaluate pseudo-label quality with and without CRF refinement on SemanticKITTI and SSCBench- KITTI360. Results show that CRF refinement significantly ...
- **p. 21 / Figure/Table caption - extractive PDF cue:** Table 12. Model ablations for data on SemanticKITTI. We train the CAL model using two different sets of data: pseudo-labels w/o CRF refinement, and pseudo-labels ...
- **p. 5 / 4. Experiments - extractive PDF cue:** 4.2), and ablations on design choices (Sec.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** (2024), we focus on the modified variant of PQ, i.e.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** In contrast to baselines trained on ground-truth (GT) data, we use GT labels solely for evaluation and ablations.
- **p. 7 / 4.2. Experimental results - extractive PDF cue:** We employ the LODE variant that does not use any semantic labels.
- **p. 7 / 4.2. Experimental results - extractive PDF cue:** LiDiff is a diffusion-based completion method that learns to complete Lidar point clouds from GT completion data without semantic labels.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.2. Learning To Complete Objects), p. 4 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects), p. 4 (3.2. Learning To Complete Objects), p. 3 (3. Method), objective p. 5 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects), temporal p. 4 (3.1. Mining 3D Shape Priors From Unlabeled Data), p. 4 (3.1. Mining 3D Shape Priors From Unlabeled Data), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 8 (4.3. Pseudo-labeling engine analysis).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
