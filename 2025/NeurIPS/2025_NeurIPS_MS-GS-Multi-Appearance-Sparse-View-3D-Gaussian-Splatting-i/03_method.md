# Method - MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=efDNv5XvVo; PDF retrieval source: https://openreview.net/pdf/804e98743d0bf960af90c596755d72e4736d2c39.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 24 (A.3 Implementation details)): To improve its robustness in sparse-view synthesis and multi-appearance modeling, MS-GS consists of two parts: Semantic Depth Alignment first constructs a dense point cloud by expanding SfM points based on ...

## Method Body Digest

- **p. 4 / 3 Method - extractive PDF cue:** To improve its robustness in sparse-view synthesis and multi-appearance modeling, MS-GS consists of two parts: Semantic Depth Alignment first constructs a dense point cloud by ...
- **p. 6 / 3 Method - extractive PDF cue:** A 3D point cloud is back-projected given a training view IT and its corresponding rendered depth DT , and then forward-projected onto the virtual view ...
- **p. 6 / 3 Method - extractive PDF cue:** Thus, we propose to use a coarse semantic feature supervision at the local patch level, i.e, the receptive field of each feature-map element.
- **p. 7 / 3 Method - extractive PDF cue:** Optimization Incorporating all the aforementioned techniques, the training objective of MS-GS is: Ltotal " λI }IT ´ I˚ T }1 ` p1 ´ λIqSSIMpIT , ...
- **p. 7 / 3 Method - extractive PDF cue:** Formally, the feature map of the training view FT is transformed to F ˚ V , which is computed using cosine distance loss with FV ...
- **p. 24 / A.3 Implementation details - extractive PDF cue:** We use features extracted from blocks 3 and 4 of VGG-16 [32, 46, 47] for feature loss at different resolutions and receptive fields.
- **p. 4 / 3 Method - extractive PDF cue:** MS-GS then introduces a series of geometry-guided supervisions based on 3D warping at a fine-grained pixel level and coarse feature level.
- **p. 5 / 3 Method - extractive PDF cue:** (1) is minimized, it's unclear whether regions without sufficient constraints, i.e. dsfm n , are properly aligned.

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in local semantic regions ...
- **p. 2 / 1 Introduction - extractive PDF cue:** 1, they synthesize overly smooth regions, while our method recovers fine details.
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we present MS-GS, which improves the robustness of 3DGS in dealing with unconstrained images when limited viewpoints and varying appearances exist, which ...

## Source Evidence Cues

- **p. 4 / 3 Method - extractive PDF cue:** To improve its robustness in sparse-view synthesis and multi-appearance modeling, MS-GS consists of two parts: Semantic Depth Alignment first constructs a dense point cloud by ...
- **p. 6 / 3 Method - extractive PDF cue:** A 3D point cloud is back-projected given a training view IT and its corresponding rendered depth DT , and then forward-projected onto the virtual view ...
- **p. 6 / 3 Method - extractive PDF cue:** Thus, we propose to use a coarse semantic feature supervision at the local patch level, i.e, the receptive field of each feature-map element.
- **p. 7 / 3 Method - extractive PDF cue:** Optimization Incorporating all the aforementioned techniques, the training objective of MS-GS is: Ltotal " λI }IT ´ I˚ T }1 ` p1 ´ λIqSSIMpIT , ...
- **p. 7 / 3 Method - extractive PDF cue:** Formally, the feature map of the training view FT is transformed to F ˚ V , which is computed using cosine distance loss with FV ...
- **p. 24 / A.3 Implementation details - extractive PDF cue:** We use features extracted from blocks 3 and 4 of VGG-16 [32, 46, 47] for feature loss at different resolutions and receptive fields.
- **p. 4 / 3 Method - extractive PDF cue:** MS-GS then introduces a series of geometry-guided supervisions based on 3D warping at a fine-grained pixel level and coarse feature level.
- **Detected method headings:** 3 Method (p. 4); A.4.2 Dense init. for other in-the-wild methods (p. 25); A.5 Semantic alignment algorithm (p. 26)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To improve its robustness in sparse-view synthesis and multi-appearance modeling, MS-GS consists of two parts: Semantic Depth Alignment first constructs a dense ... | p. 4 (3 Method), p. 6 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | A 3D point cloud is back-projected given a training view IT and its corresponding rendered depth DT , and then forward-projected onto ... | p. 6 (3 Method), p. 6 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Thus, we propose to use a coarse semantic feature supervision at the local patch level, i.e, the receptive field of each feature-map ... | p. 6 (3 Method), p. 7 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Method - extractive PDF cue:** (1) is minimized, it's unclear whether regions without sufficient constraints, i.e. dsfm n , are properly aligned.
- **p. 7 / 3 Method - extractive PDF cue:** Optimization Incorporating all the aforementioned techniques, the training objective of MS-GS is: Ltotal " λI }IT ´ I˚ T }1 ` p1 ´ λIqSSIMpIT , ...
- **p. 5 / 3 Method - extractive PDF cue:** A noisy Xmono does not improve NVS quality, as the dense but inaccurate points give rise to artifacts due to noisy gradients and lead to ...
- **p. 6 / 3 Method - extractive PDF cue:** This explicit pixel-wise loss is formulated as: Lpix " }Mocl d pIV ´ I˚ V q}1 .
- **p. 6 / 3 Method - extractive PDF cue:** The correspondences from IT to I˚ V are mapped to feature maps extracted from these two images to form a feature loss.
- **p. 7 / 3 Method - extractive PDF cue:** Formally, the feature map of the training view FT is transformed to F ˚ V , which is computed using cosine distance loss with FV ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summary, main, contributions, introduce, Semantic, Depth, Alignment, leverages, monocular, depths, local, regions, construct, dense | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | summary, main, contributions, introduce, Semantic, Depth, Alignment, leverages, monocular, depths | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, main, contributions, introduce, Semantic, Depth, Alignment, leverages, monocular, depths | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | minimized, unclear, whether, regions, without, sufficient, constraints, dsfm, properly, aligned | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive PDF cue:** In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in local semantic regions ...
- **p. 4 / 3 Method - extractive PDF cue:** SfM-anchored alignment After camera calibration, we have a set of N images tIn/n " 1, 2, ..., Nu, an initial SfM point cloud X P ...
- **p. 6 / 3 Method - extractive PDF cue:** A 3D point cloud is back-projected given a training view IT and its corresponding rendered depth DT , and then forward-projected onto the virtual view ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The resulting point cloud is denser and better structured than the original sparse SfM output, helping regularize 3DGS structures and promote Gaussian densification.
- **p. 3 / 1 Introduction - extractive PDF cue:** Accurate reflection of performance in the wild needs to account for realistic registration noise, especially when the underlying SfM point cloud is the input to ...
- **p. 5 / 3 Method - extractive PDF cue:** (4) 3.2 Multi-view geometry-guided supervisions Modeling multi-appearance scenes under sparse-view constraints is especially difficult: view-specific lighting and weather variations demand more observations to disentangle appearance ...
- **p. 4 / 3 Method - extractive PDF cue:** Therefore, we seek to densify the initial sparse point cloud based on monocular depth estimation.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Our proposed method, MS-GS, builds on the efficient 3DGS framework, in which a scene is represented by a set of Gaussian primitives ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | These results show the efficacy of our semantic dense initialization in regularizing scene structure and facilitating the optimizations of the 3DGS framework. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive PDF cue:** A 3D point cloud is back-projected given a training view IT and its corresponding rendered depth DT , and then forward-projected onto the virtual view ...
- **p. 7 / 3 Method - extractive PDF cue:** Optimization Incorporating all the aforementioned techniques, the training objective of MS-GS is: Ltotal " λI }IT ´ I˚ T }1 ` p1 ´ λIqSSIMpIT , ...
- **p. 7 / 3 Method - extractive PDF cue:** Formally, the feature map of the training view FT is transformed to F ˚ V , which is computed using cosine distance loss with FV ...
- **p. 9 / 4 Experiments - extractive PDF cue:** Furthermore, our design is lightweight, requiring >3× less GPU time for training over Wild-GS and rendering at 300+ FPS.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** improve, robustness, sparse-view, synthesis, multi-appearance, modeling, MS-GS, consists, parts, Semantic, Depth, Alignment, first, constructs, dense, point, cloud, expanding, SfM, points.
- **Relevant PDF headings:** 3 Method (p. 4); A.4.2 Dense init. for other in-the-wild methods (p. 25); A.5 Semantic alignment algorithm (p. 26).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.1 Datasets We evaluate the performance of MS-GS and current SoTA methods on three real-world scenes with sparse inputs-one with single appearance ... | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Semantic / temporal fusion | On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, ... | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Robot query / planning handoff | On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, ... | p. 9 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive PDF cue:** 4.3 Ablation Study We conduct an ablation study to validate the effectiveness of our method in Table 1 and Fig.
- **p. 9 / 4 Experiments - extractive PDF cue:** Without sufficient constraints, the appearance-affine head and uncertainty weighting in WildGaussians can absorb photometric error instead of correcting structures, leaving as off-view aliasing and texture ...
- **p. 9 / 4 Experiments - extractive PDF cue:** While recent methods leverage uncertainty masks to remove transients and allow other observations to fill in the blank, often no other observations exist under a ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Ablation studies on different components of MS-GS. The metrics are reported as the average on the Sparse Unbounded drone dataset; bold numbers are ...
- **p. 24 / A.3 Implementation details - extractive PDF cue:** The baseline introduced in our ablation study Section 4.3 uses the same Splatfacto model.
- **p. 24 / Figure/Table caption - extractive PDF cue:** Figure 10: As MS-GS favors more accurate local alignment, areas without dense initialization can introduce artifacts in (a) and (b). Specular highlights can be smoothed ...
- **p. 8 / 4 Experiments - extractive PDF cue:** All proposed components are complementary, and the best results are achieved when combined.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 24 (A.3 Implementation details), objective p. 5 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), temporal p. 4 (3 Method), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 3 (1 Introduction), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
