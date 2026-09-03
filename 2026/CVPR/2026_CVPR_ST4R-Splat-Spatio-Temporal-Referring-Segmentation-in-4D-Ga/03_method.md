# Method - ST4R-Splat: Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Overview), p. 3 (3.3. Object Captioning via Multimodal Prompting), p. 5 (3.5. Instance-Level Temporal State Modeling), p. 5 (3.5. Instance-Level Temporal State Modeling)): The objective is to achieve spatial instance grounding within the 4D representation, rendering its segmentation masks across all frames during inference. • Time-sensitive referring queries Esensitive: The target instance is ...

## Method Body Digest

- **p. 3 / 3.2. Overview - extractive body cue:** The objective is to achieve spatial instance grounding within the 4D representation, rendering its segmentation masks across all frames during inference. • Time-sensitive referring queries ...
- **p. 3 / 3.3. Object Captioning via Multimodal Prompting - extractive body cue:** To avoid the issue of inconsistent referring granularity, we first define a set of object categories of interest, then leverage off-the-shelf vision foundation models to ...
- **p. 5 / 3.5. Instance-Level Temporal State Modeling - extractive body cue:** Formally, our objective is to model a function F that maps an instance's representative feature ¯ek and a given time t to its corresponding dynamic ...
- **p. 5 / 3.5. Instance-Level Temporal State Modeling - extractive body cue:** (13) This cache, which binds temporal states directly to instance identities, is then used during inference.
- **p. 3 / 3.2. Overview - extractive body cue:** This avoids 2D rendering losses and ensures consistent temporal localization across viewpoints.
- **p. 3 / 3.2. Overview - extractive body cue:** The objective is to jointly achieve spatial instance grounding and temporal state localization within the 4D representation, rendering segmentation masks within the active time interval(s).
- **p. 3 / 3.1. Preliminaries - extractive body cue:** This is achieved by learning a deformation field that predicts the offset from a canonical Gaussian gi to its deformed state gi(t) at a given ...
- **p. 1 / 1. Introduction - extractive body cue:** This requires jointly solving two sub-tasks: (i) spatial disambiguation ("where") to locate the target object based on its attributes or spatial relations, and (ii) temporal ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • We introduce the novel task of STRS-4DGS (SpatioTemporal Referring Segmentation in 4D Gaussian Splatting) and construct ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose ST4R-Splat, the pioneering framework for STRS-4DGS.
- **p. 2 / 1. Introduction - extractive body cue:** These results validate our framework and establish a strong foundation for languagedriven scene understanding in dynamic 4D environments.

## Source Evidence Cues

- **p. 3 / 3.2. Overview - extractive body cue:** The objective is to achieve spatial instance grounding within the 4D representation, rendering its segmentation masks across all frames during inference. • Time-sensitive referring queries ...
- **p. 3 / 3.3. Object Captioning via Multimodal Prompting - extractive body cue:** To avoid the issue of inconsistent referring granularity, we first define a set of object categories of interest, then leverage off-the-shelf vision foundation models to ...
- **p. 5 / 3.5. Instance-Level Temporal State Modeling - extractive body cue:** Formally, our objective is to model a function F that maps an instance's representative feature ¯ek and a given time t to its corresponding dynamic ...
- **p. 5 / 3.5. Instance-Level Temporal State Modeling - extractive body cue:** (13) This cache, which binds temporal states directly to instance identities, is then used during inference.
- **Detected method headings:** 3. Method (p. 3); 3.5. Instance-Level Temporal State Modeling (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The objective is to achieve spatial instance grounding within the 4D representation, rendering its segmentation masks across all frames during inference. • ... | p. 3 (3.2. Overview), p. 3 (3.3. Object Captioning via Multimodal Prompting) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To avoid the issue of inconsistent referring granularity, we first define a set of object categories of interest, then leverage off-the-shelf vision ... | p. 3 (3.3. Object Captioning via Multimodal Prompting), p. 5 (3.5. Instance-Level Temporal State Modeling) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Formally, our objective is to model a function F that maps an instance's representative feature ¯ek and a given time t to ... | p. 5 (3.5. Instance-Level Temporal State Modeling), p. 5 (3.5. Instance-Level Temporal State Modeling) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.2. Overview - extractive body cue:** This avoids 2D rendering losses and ensures consistent temporal localization across viewpoints.
- **p. 3 / 3.2. Overview - extractive body cue:** The objective is to jointly achieve spatial instance grounding and temporal state localization within the 4D representation, rendering segmentation masks within the active time interval(s).
- **p. 5 / 3.5. Instance-Level Temporal State Modeling - extractive body cue:** Formally, our objective is to model a function F that maps an instance's representative feature ¯ek and a given time t to its corresponding dynamic ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.2. Overview), p. 3 (3.2. Overview), p. 5 (3.5. Instance-Level Temporal State Modeling).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | objective, achieve, spatial, instance, grounding, within, representation, rendering, segmentation, masks, across, frames, during, inference | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | objective, achieve, spatial, instance, grounding, within, representation, rendering, segmentation, masks | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, main, contributions, follows, introduce, novel, task, STRS-4DGS, SpatioTemporal, Referring | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | avoids, rendering, losses, ensures, consistent, temporal, localization, across, viewpoints, objective | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. Overview - extractive body cue:** The objective is to achieve spatial instance grounding within the 4D representation, rendering its segmentation masks across all frames during inference. • Time-sensitive referring queries ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** This is achieved by learning a deformation field that predicts the offset from a canonical Gaussian gi to its deformed state gi(t) at a given ...
- **p. 1 / 1. Introduction - extractive body cue:** This requires jointly solving two sub-tasks: (i) spatial disambiguation ("where") to locate the target object based on its attributes or spatial relations, and (ii) temporal ...
- **p. 1 / 1. Introduction - extractive body cue:** Enabling natural language interaction within reconstructed dynamic environments is a central goal in computer vision and robotics [7, 11].
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • We introduce the novel task of STRS-4DGS (SpatioTemporal Referring Segmentation in 4D Gaussian Splatting) and construct ...
- **p. 5 / 3.5. Instance-Level Temporal State Modeling - extractive body cue:** Our goal is to model the state changes of a specific instance ok over time, binding its temporal dynamics directly to its identity.
- **p. 2 / 1. Introduction - extractive body cue:** and timestamp to a unique semantic state feature.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Each object instance ok is represented by a sequence of masks {Mk,t} across frames, 17600 | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 1, the ST4R-Splat framework explicitly decouples instance identification and temporal state modeling through three key components: • Object Captioning via Multimodal Prompting ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.2. Overview - extractive body cue:** The objective is to achieve spatial instance grounding within the 4D representation, rendering its segmentation masks across all frames during inference. • Time-sensitive referring queries ...
- **p. 5 / 3.5. Instance-Level Temporal State Modeling - extractive body cue:** (13) This cache, which binds temporal states directly to instance identities, is then used during inference.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** objective, achieve, spatial, instance, grounding, within, representation, rendering, segmentation, masks, across, frames, during, inference, Time-sensitive, referring, queries, Esensitive, target, specified.
- **Relevant PDF headings:** 3. Method (p. 3); 3.5. Instance-Level Temporal State Modeling (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To adapt it to our dynamic 4D benchmark as a strong baseline for timeagnostic queries, we train the model utilizing the exact ... | p. 6 (4.1. Setup), p. 6 (4.1. Setup) |
| Semantic / temporal fusion | Consequently, we adapt state-of-the-art approaches from closely related domains to establish strong baselines: • ReferSplat [9]: The current state-of-the-art for referring segmentation ... | p. 6 (4.1. Setup), p. 6 (4.1. Setup) |
| Robot query / planning handoff | ST4RSplat achieves an average accuracy of 83.44% and vIoU 17603 | p. 6 (4.2. Results), p. 6 (4.2. Results) |

## Failure and Ablation Link

- **p. 8 / 4.3. Ablation Studies - extractive body cue:** To validate the effectiveness of our design choices, we conduct ablation studies on our extended HyperNeRF dataset, as summarized in Table 2.
- **p. 8 / 4.2. Results - extractive body cue:** Ablation study of different components in our ST4R-Splat framework.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. Overview of the ST4R-Splat framework. It mainly consists of three main components: (I) MLLM-based object captioning for generating decoupled textual supervision, (II) an ...
- **p. 7 / 4.2. Results - extractive body cue:** 4DLangSplat often fails to parse complex spatial relations within referring expressions.
- **p. 8 / 4.2. Results - extractive body cue:** It fails to effectively obtain features representing the temporal state, resulting in a substantial drop in accuracy (51.92% Acc).
- **p. 8 / 5. Conclusion - extractive body cue:** To tackle this, we proposed ST4RSplat, which incorporates an Instance-Aware 4D Referring Field for robust spatial grounding and an Instance-Level Temporal State Mapping module for ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. Overview of the ST4R-Splat framework. It mainly consists of three main components: (I) MLLM-based object captioning for generating decoupled textual supervision, (II) an ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.2. Overview), p. 3 (3.3. Object Captioning via Multimodal Prompting), p. 5 (3.5. Instance-Level Temporal State Modeling), p. 5 (3.5. Instance-Level Temporal State Modeling), objective p. 3 (3.2. Overview), p. 3 (3.2. Overview), p. 5 (3.5. Instance-Level Temporal State Modeling), temporal p. 3 (3.3. Object Captioning via Multimodal Prompting), p. 3 (3.2. Overview), p. 6 (4.1. Setup), p. 6 (4.1. Setup), p. 8 (4.2. Results), p. 8 (4.2. Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
