# Method - How Do Images Align and Complement LiDAR? Towards a Harmonized Multi-modal 3D Panoptic Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=F7BOaYmWl7; PDF retrieval source: https://openreview.net/pdf/ea38ded40d57a840cbde86fb7bfa9588256ea489.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3. Methodology), p. 6 (3.3. Prior-Based Query Generation), p. 4 (3. Methodology), p. 6 (3.3. Prior-Based Query Generation), p. 3 (3. Methodology), p. 5 (3.2. Geometric-Guided Token Fusion)): Next, we use F3D and F2D to create tokens and queries for a transformer decoder, enabling cross-modal interaction.

## Method Body Digest

- **p. 4 / 3. Methodology - extractive PDF cue:** Next, we use F3D and F2D to create tokens and queries for a transformer decoder, enabling cross-modal interaction.
- **p. 6 / 3.3. Prior-Based Query Generation - extractive PDF cue:** Inspired by this observation, we propose the Prior-based Query Generation (PQG) module to explicitly leverage texture features from the image domain, and geometric information from ...
- **p. 4 / 3. Methodology - extractive PDF cue:** The augmented 3D voxels and images are then processed by 3D encoder E3D and 2D encoder E2D, extracting voxelwise features F3D ∈RM×D and image features ...
- **p. 6 / 3.3. Prior-Based Query Generation - extractive PDF cue:** We then extract the query content by indexing into the corresponding voxel features Ffuse, and finally add the SPE to this content to form the ...
- **p. 3 / 3. Methodology - extractive PDF cue:** In this paper, we introduce ImageAssist-LiDAR (IAL), a novel transformer-based framework for multi-modal 3D panoptic segmentation, as illustrated in Fig.
- **p. 5 / 3.2. Geometric-Guided Token Fusion - extractive PDF cue:** Specifically, we align features at the voxel level by projecting all physical points within a voxel vi onto the image plane and averaging their corresponding ...
- **p. 5 / 3.2. Geometric-Guided Token Fusion - extractive PDF cue:** Position embedding (PE) has proven effective in aligning features from different modalities (Yan et al., 2023).
- **p. 5 / 3.2. Geometric-Guided Token Fusion - extractive PDF cue:** Even when using physical points for PE, capturing the full perceptive field of a voxel or its corresponding image region image coord. view image ✘ ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions can be summarized as: 1) We present IAL, a novel transformer-based multi-modal framework for multimodal 3D panoptic segmentation, eliminating the cumbersome post-processing steps ...
- **p. 3 / 3. Methodology - extractive PDF cue:** In this paper, we introduce ImageAssist-LiDAR (IAL), a novel transformer-based framework for multi-modal 3D panoptic segmentation, as illustrated in Fig.
- **p. 1 / 1. Introduction - extractive PDF cue:** To address the first limitation, we propose a modality1

## Source Evidence Cues

- **p. 4 / 3. Methodology - extractive PDF cue:** Next, we use F3D and F2D to create tokens and queries for a transformer decoder, enabling cross-modal interaction.
- **p. 6 / 3.3. Prior-Based Query Generation - extractive PDF cue:** Inspired by this observation, we propose the Prior-based Query Generation (PQG) module to explicitly leverage texture features from the image domain, and geometric information from ...
- **p. 4 / 3. Methodology - extractive PDF cue:** The augmented 3D voxels and images are then processed by 3D encoder E3D and 2D encoder E2D, extracting voxelwise features F3D ∈RM×D and image features ...
- **p. 6 / 3.3. Prior-Based Query Generation - extractive PDF cue:** We then extract the query content by indexing into the corresponding voxel features Ffuse, and finally add the SPE to this content to form the ...
- **p. 3 / 3. Methodology - extractive PDF cue:** In this paper, we introduce ImageAssist-LiDAR (IAL), a novel transformer-based framework for multi-modal 3D panoptic segmentation, as illustrated in Fig.
- **p. 5 / 3.2. Geometric-Guided Token Fusion - extractive PDF cue:** Specifically, we align features at the voxel level by projecting all physical points within a voxel vi onto the image plane and averaging their corresponding ...
- **p. 5 / 3.2. Geometric-Guided Token Fusion - extractive PDF cue:** Position embedding (PE) has proven effective in aligning features from different modalities (Yan et al., 2023).
- **Detected method headings:** 3. Methodology (p. 3); 4.4. Augmentation Methods Comparison (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Next, we use F3D and F2D to create tokens and queries for a transformer decoder, enabling cross-modal interaction. | p. 4 (3. Methodology), p. 6 (3.3. Prior-Based Query Generation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Inspired by this observation, we propose the Prior-based Query Generation (PQG) module to explicitly leverage texture features from the image domain, and ... | p. 6 (3.3. Prior-Based Query Generation), p. 4 (3. Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The augmented 3D voxels and images are then processed by 3D encoder E3D and 2D encoder E2D, extracting voxelwise features F3D ∈RM×D ... | p. 4 (3. Methodology), p. 6 (3.3. Prior-Based Query Generation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Geometric-Guided Token Fusion - extractive PDF cue:** Even when using physical points for PE, capturing the full perceptive field of a voxel or its corresponding image region image coord. view image ✘ ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.2. Geometric-Guided Token Fusion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Inspired, observation, Prior-based, Query, Generation, PQG, module, explicitly, leverage, texture, features, image, domain, geometric | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Inspired, observation, Prior-based, Query, Generation, PQG, module, explicitly, leverage, texture | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, present, IAL, novel, transformer-based, multi-modal, framework, multimodal, panoptic | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Even, when, physical, points, capturing, full, perceptive, field, voxel, corresponding | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3.3. Prior-Based Query Generation - extractive PDF cue:** Inspired by this observation, we propose the Prior-based Query Generation (PQG) module to explicitly leverage texture features from the image domain, and geometric information from ...
- **p. 1 / 1. Introduction - extractive PDF cue:** LiDAR is an indispensable sensor for perceiving the 3D world, with its LiDAR point cloud typically serving as the sole input for 3D panoptic segmentation ...
- **p. 2 / 1. Introduction - extractive PDF cue:** GTF module integrates the sparse, cylinder-shaped LiDAR features with the compact, grid-shaped image features to create input tokens.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our PQG module leverages prior knowledge from LiDAR and image inputs, which provide complementary strengths for object perception, to improve query initialization.
- **p. 4 / 3. Methodology - extractive PDF cue:** Next, we use F3D and F2D to create tokens and queries for a transformer decoder, enabling cross-modal interaction.
- **p. 3 / 3. Methodology - extractive PDF cue:** The point cloud is associated with K view images, represented as I = {Ik ∈RH×W ×3}K k=1, H and W denote the height and width ...
- **p. 4 / 3.1. Modality-Synchronized Augmentation - extractive PDF cue:** Point clouds are projected on camera images, with colors indicating semantic labels or data sources.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Top and runner-up results are marked in bold and underline, respectively. "*" indicates the use of additional temporal frames and detection annotations. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our contributions can be summarized as: 1) We present IAL, a novel transformer-based multi-modal framework for multimodal 3D panoptic segmentation, eliminating the ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | It includes 40,157 frames of outdoor scenes, with 34,149 frames labeled for training and validation, and the remaining reserved for testing. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.1. Experimental Setting - extractive PDF cue:** The entire model is trained from scratch with a batch size of 2, using 4 NVIDIA A40 GPUs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Next, F3D, F2D, create, tokens, queries, transformer, decoder, enabling, cross-modal, interaction, Inspired, observation, Prior-based, Query, Generation, PQG, module, explicitly, leverage.
- **Relevant PDF headings:** 3. Methodology (p. 3); 4.4. Augmentation Methods Comparison (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | SemanticKITTI (Behley et al., 2019; 2021) is an outdoor dataset derived from KITTI Vision Benchmark (Geiger et al., 2012). | p. 6 (4.1. Experimental Setting), p. 6 (4.1. Experimental Setting) |
| Semantic / temporal fusion | As shown in Table 5, compared to the baseline that uses only basic point cloud transformations (row 1), PieAug improves PQ by ... | p. 8 (4.3. Ablation Studies), p. 8 (4.2. Benchmark Results) |
| Robot query / planning handoff | As shown in Table 4, despite these constraints, our IAL achieves a 4.1% improvement in PQ over the state-of-the-art multi-modal baseline LCPS, ... | p. 8 (4.2. Benchmark Results), p. 8 (4.2. Benchmark Results) |

## Failure and Ablation Link

- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** To validate the effectiveness of our proposed components, we conduct comprehensive ablation studies on the overall proposal framework in Table 5 and provide detailed analyses ...
- **p. 7 / 4.1. Experimental Setting - extractive PDF cue:** Our method is evaluated without test-time augmentation or ensembling.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Ablation study of the proposed modules in our framework. "PIE" denotes the PieAug module.
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 8. Ablation study of the GTF module. "Sel" and "PE" denote the designs for token selection and positional embedding, respectively. We evaluate different configurations ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1. The architecture overview of our Image-Assists-LiDAR (IAL) framework. We first voxelize the point cloud into cylindrical voxels. In PieAug, we synchronize augmentation by ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Motivation and implementation variants of PieAug. Each column illustrates the motivation for LiDAR-image syn- chronized augmentation. Each row displays a different pie-cut strategy. ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 6. Qualitative comparison of the ablation study for GTF and PQG modules. To emphasize the differences, we mark false positive and false negative predictions, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3. Methodology), p. 6 (3.3. Prior-Based Query Generation), p. 4 (3. Methodology), p. 6 (3.3. Prior-Based Query Generation), p. 3 (3. Methodology), p. 5 (3.2. Geometric-Guided Token Fusion), objective p. 5 (3.2. Geometric-Guided Token Fusion), temporal p. 7 (4.1. Experimental Setting), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 6 (3.3. Prior-Based Query Generation), p. 6 (4.1. Experimental Setting), p. 8 (4.3. Ablation Studies).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
