# Method - MAPo: Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for High-Fidelity Dynamic Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Jiao_MAPo_Motion-Aware_Partitioning_of_Deformable_3D_Gaussian_Splatting_for_High-Fidelity_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Jiao_MAPo_Motion-Aware_Partitioning_of_Deformable_3D_Gaussian_Splatting_for_High-Fidelity_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (4.2. Cross-Frame Consistency Loss), p. 4 (4. Method), p. 5 (4.2. Cross-Frame Consistency Loss), p. 4 (4. Method), p. 6 (4.2. Cross-Frame Consistency Loss), p. 6 (4.2. Cross-Frame Consistency Loss)): To ensure temporal smoothness, we introduce the cross-frame consistency loss Lcross, which consists of two components: Lcurrent and Lgt.

## Method Body Digest

- **p. 5 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** To ensure temporal smoothness, we introduce the cross-frame consistency loss Lcross, which consists of two components: Lcurrent and Lgt.
- **p. 4 / 4. Method - extractive PDF cue:** Our approach consists of two main components: a dynamic score-based partitioning strategy and a cross-frame consistency loss.
- **p. 5 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** Since Lcurrent only enforces self-consistency between adjacent segments without an external reference, continuous optimization can cause them to converge to a consistent but over-smoothed state, ...
- **p. 4 / 4. Method - extractive PDF cue:** Subsequently, we describe our cross-frame consistency loss, which is designed to address the visual discontinuities caused by partitioning.
- **p. 6 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** We apply Lcross only for training views whose frame indices are within 5 frames of any partition boundary.
- **p. 6 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** This contextual enrichment forces Gt′ to learn to represent the sharp details of the current frame, thereby preventing over-smoothing and enhancing overall fidelity.
- **p. 7 / 5.2. Implementation Details - extractive PDF cue:** Storage, training time, and FPS are calculated on discussion.
- **p. 5 / 4.1.3. Static 3D Gaussian Partitioning - extractive PDF cue:** Subsequently, they are excluded from computations involving the deformation network during rendering while their attributes remain optimizable, significantly reducing computational costs.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our key contributions are summarized as follows: • We propose MAPo, a novel framework for high-fidelity dynamic scene reconstruction based on a dynamic scorebased partitioning ...
- **p. 5 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** To ensure temporal smoothness, we introduce the cross-frame consistency loss Lcross, which consists of two components: Lcurrent and Lgt.
- **p. 4 / 4. Method - extractive PDF cue:** Our approach consists of two main components: a dynamic score-based partitioning strategy and a cross-frame consistency loss.

## Source Evidence Cues

- **p. 5 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** To ensure temporal smoothness, we introduce the cross-frame consistency loss Lcross, which consists of two components: Lcurrent and Lgt.
- **p. 4 / 4. Method - extractive PDF cue:** Our approach consists of two main components: a dynamic score-based partitioning strategy and a cross-frame consistency loss.
- **p. 5 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** Since Lcurrent only enforces self-consistency between adjacent segments without an external reference, continuous optimization can cause them to converge to a consistent but over-smoothed state, ...
- **p. 4 / 4. Method - extractive PDF cue:** Subsequently, we describe our cross-frame consistency loss, which is designed to address the visual discontinuities caused by partitioning.
- **p. 6 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** We apply Lcross only for training views whose frame indices are within 5 frames of any partition boundary.
- **p. 6 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** This contextual enrichment forces Gt′ to learn to represent the sharp details of the current frame, thereby preventing over-smoothing and enhancing overall fidelity.
- **p. 7 / 5.2. Implementation Details - extractive PDF cue:** Storage, training time, and FPS are calculated on discussion.
- **Detected method headings:** 4. Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To ensure temporal smoothness, we introduce the cross-frame consistency loss Lcross, which consists of two components: Lcurrent and Lgt. | p. 5 (4.2. Cross-Frame Consistency Loss), p. 4 (4. Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Our approach consists of two main components: a dynamic score-based partitioning strategy and a cross-frame consistency loss. | p. 4 (4. Method), p. 5 (4.2. Cross-Frame Consistency Loss) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Since Lcurrent only enforces self-consistency between adjacent segments without an external reference, continuous optimization can cause them to converge to a consistent ... | p. 5 (4.2. Cross-Frame Consistency Loss), p. 4 (4. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.1.3. Static 3D Gaussian Partitioning - extractive PDF cue:** Subsequently, they are excluded from computations involving the deformation network during rendering while their attributes remain optimizable, significantly reducing computational costs.
- **p. 6 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** Finally, the overall cross-frame consistency loss, Lcross, is defined as a weighted combination of Lcurrent and Lgt: {L}_ { \te x t {cross } } ...
- **p. 4 / 4. Method - extractive PDF cue:** Our approach consists of two main components: a dynamic score-based partitioning strategy and a cross-frame consistency loss.
- **p. 4 / 4. Method - extractive PDF cue:** Subsequently, we describe our cross-frame consistency loss, which is designed to address the visual discontinuities caused by partitioning.
- **p. 5 / 4.1.1. Dynamic Score Calculation - extractive PDF cue:** Effectiveness of temporal partitioning strategy and consistency loss on a toy example.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4. Method), p. 4 (4. Method), p. 5 (4.1.1. Dynamic Score Calculation), p. 5 (4.2. Cross-Frame Consistency Loss), p. 6 (4.2. Cross-Frame Consistency Loss).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | harmonic, mean, fuse, protect, tilde, requires, inputs, high, output, Since, Lcurrent, only, enforces, self-consistency | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | harmonic, mean, fuse, protect, tilde, requires, inputs, high, output, Since | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, MAPo, novel, framework, high-fidelity, dynamic, scene, reconstruction | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Subsequently, they, excluded, computations, involving, deformation, network, during, rendering, while | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4.1.1. Dynamic Score Calculation - extractive PDF cue:** We use the harmonic mean to fuse \protect \tilde {r}_ i and \protect \tilde {v}_ i, as it requires both inputs to be high for ...
- **p. 5 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** Since Lcurrent only enforces self-consistency between adjacent segments without an external reference, continuous optimization can cause them to converge to a consistent but over-smoothed state, ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Reconstructing high-fidelity dynamic scenes from multiview video inputs is a fundamental challenge in computer vision, with broad applications in virtual reality, visual effects, and autonomous ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To further mitigate visual discontinuities introduced by temporal partitioning, we introduce a cross-frame consistency loss that enforces two constraints: (i) the renderings of two sets ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The region highlighted in red in (c) is visually distant from this average. ploying deformable 3D Gaussians-where a learned deformation field maps a canonical set ...
- **p. 3 / 3. Preliminaries - extractive PDF cue:** 3D Gaussian Splatting 3D Gaussian Splatting introduces an explicit point-based representation where each point in the point cloud is equipped with four fundamental properties: mean ...
- **p. 3 / 3. Preliminaries - extractive PDF cue:** For a given viewpoint, all 3DGs are first projected onto the 2D image plane.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This loss is designed to enrich the adjacent segment's 3DGs with valuable spatio-temporal context from the current frame. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To ensure temporal smoothness, we introduce the cross-frame consistency loss Lcross, which consists of two components: Lcurrent and Lgt. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** We apply Lcross only for training views whose frame indices are within 5 frames of any partition boundary.
- **p. 7 / 5.2. Implementation Details - extractive PDF cue:** Storage, training time, and FPS are calculated on discussion.
- **p. 6 / 5.1. Dataset and Metrics - extractive PDF cue:** Storage, training time, and FPS are measured on flame salmon frag1.
- **p. 7 / 5.2. Implementation Details - extractive PDF cue:** Storage, training time, and FPS are calculated on discussion.
- **p. 7 / 5.2. Implementation Details - extractive PDF cue:** Method PSNR↑ SSIM↑ LPIPS↓ Storage↓ Training Time↓ FPS↑ D3DGS 25.81 0.890 0.233

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ensure, temporal, smoothness, introduce, cross-frame, consistency, loss, Lcross, consists, components, Lcurrent, Lgt, main, dynamic, score-based, partitioning, strategy, Since, only, enforces.
- **Relevant PDF headings:** 4. Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate our method on two real-world dynamic scene datasets: N3DV [15] and Meet Room [14]. | p. 6 (5.1. Dataset and Metrics), p. 6 (5.1. Dataset and Metrics) |
| Semantic / temporal fusion | In addition to these SOTA baselines, we additionally introduce a simple segmentation baseline, E-D3DGS (seg), for comparison to highlight the advantages of ... | p. 7 (5.3.1. Quantitative Comparisons), p. 7 (5.3.2. Qualitative Comparisons) |
| Robot query / planning handoff | Figure 1. Overview. (a-b) Deformation-based methods often blur details in regions with complex or rapid motion. (c) Our MAPo significantly improves rendering ... | p. 1 (Figure/Table caption), p. 7 (5.3.1. Quantitative Comparisons) |

## Failure and Ablation Link

- **p. 7 / 5.4. Ablation Study and Analysis - extractive PDF cue:** Progressive component ablation on Meet Room.
- **p. 7 / 5.4. Ablation Study and Analysis - extractive PDF cue:** To evaluate our method, we present a progressive ablation study in Tab.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation study on the partition level parameter. All experiments are conducted on the flame salmon frag3.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 9. Ablation study on the Lcross. We visualize how Lcross improves temporal consistency and rendering quality across a par- tition boundary (frames 74-75). The ...
- **p. 7 / 5.3.2. Qualitative Comparisons - extractive PDF cue:** The comparison highlights that baseline methods often produce degraded results in areas with complex or rapid motion.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (4.2. Cross-Frame Consistency Loss), p. 4 (4. Method), p. 5 (4.2. Cross-Frame Consistency Loss), p. 4 (4. Method), p. 6 (4.2. Cross-Frame Consistency Loss), p. 6 (4.2. Cross-Frame Consistency Loss), objective p. 5 (4.1.3. Static 3D Gaussian Partitioning), p. 6 (4.2. Cross-Frame Consistency Loss), p. 4 (4. Method), p. 4 (4. Method), p. 5 (4.1.1. Dynamic Score Calculation), temporal p. 5 (4.2. Cross-Frame Consistency Loss), p. 5 (4.2. Cross-Frame Consistency Loss), p. 6 (4.2. Cross-Frame Consistency Loss), p. 7 (5.3.1. Quantitative Comparisons), p. 1 (Abstract), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
