# Method - GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=0fib2BYc0L; PDF retrieval source: https://openreview.net/pdf/94dff9ec5dcdca1b79537df06addeb9d3d3b2185.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (2 METHODOLOGY), p. 5 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 4 (2 METHODOLOGY)): Here we introduce GPT4Scene's architecture.

## Method Body Digest

- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** Here we introduce GPT4Scene's architecture.
- **p. 5 / 2 METHODOLOGY - extractive PDF cue:** Published as a conference paper at ICLR 2026 2.3 ENHANCING VLMS WITH SCANALIGN FINE-TUNING Table 2: ScanAlign: Datasets used for training GPT4Scene (Supervised Fine-Tuning), Source ...
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** In a zero-shot setting, the model must create a global-local understanding of a 3D scene by fusing local 2D frame features with global BEV (Bird's-Eye ...
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** In contrast, large-scale models like Qwen2-VL-72B and GPT-4o possess the architectural complexity to inherently grasp these feature associations, allowing them to form a preliminary 3D ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our analysis shows that directly inputting scene videos into VLMs fails in 3D scene understanding due to two factors: i) the lack of a global ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The desk is wooden and beige in color Object 47, 16, 2, 19, 20, 28 3D Dense Caption A wooden desk against the wall Describe ...
- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** Given an input video sequence V = {I1, . . . , IN} captured during indoor scene traversal, we first reconstruct the 3D scene from ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Our paper makes these major contributions: • We introduce GPT4Scene, a framework that enhances Vision-Language Models (VLMs) to comprehend 3D scenes directly from pure vision ...

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Our paper makes these major contributions: • We introduce GPT4Scene, a framework that enhances Vision-Language Models (VLMs) to comprehend 3D scenes directly from pure vision ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To address this, we propose GPT4Scene, a framework that enhances VLMs' spatial understanding (see Figure 1).
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** For smaller open-source vision-language models (VLMs), we introduce ScanAlign, a multimodal dataset comprising 165K aligned data pairs featuring STO-marker-annotated video frames, BEV images, and textual ...

## Source Evidence Cues

- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** Here we introduce GPT4Scene's architecture.
- **p. 5 / 2 METHODOLOGY - extractive PDF cue:** Published as a conference paper at ICLR 2026 2.3 ENHANCING VLMS WITH SCANALIGN FINE-TUNING Table 2: ScanAlign: Datasets used for training GPT4Scene (Supervised Fine-Tuning), Source ...
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** In a zero-shot setting, the model must create a global-local understanding of a 3D scene by fusing local 2D frame features with global BEV (Bird's-Eye ...
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** In contrast, large-scale models like Qwen2-VL-72B and GPT-4o possess the architectural complexity to inherently grasp these feature associations, allowing them to form a preliminary 3D ...
- **Detected method headings:** 2 METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Here we introduce GPT4Scene's architecture. | p. 3 (2 METHODOLOGY), p. 5 (2 METHODOLOGY) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Published as a conference paper at ICLR 2026 2.3 ENHANCING VLMS WITH SCANALIGN FINE-TUNING Table 2: ScanAlign: Datasets used for training GPT4Scene ... | p. 5 (2 METHODOLOGY), p. 4 (2 METHODOLOGY) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In a zero-shot setting, the model must create a global-local understanding of a 3D scene by fusing local 2D frame features with ... | p. 4 (2 METHODOLOGY), p. 4 (2 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | analysis, directly, inputting, scene, videos, VLMs, fails, understanding, factors, lack, global, representation, misalignment, between | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | analysis, directly, inputting, scene, videos, VLMs, fails, understanding, factors, lack | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | makes, major, contributions, introduce, GPT4Scene, framework, enhances, Vision-Language, Models, VLMs | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our analysis shows that directly inputting scene videos into VLMs fails in 3D scene understanding due to two factors: i) the lack of a global ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The desk is wooden and beige in color Object 47, 16, 2, 19, 20, 28 3D Dense Caption A wooden desk against the wall Describe ...
- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** Given an input video sequence V = {I1, . . . , IN} captured during indoor scene traversal, we first reconstruct the 3D scene from ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Our paper makes these major contributions: • We introduce GPT4Scene, a framework that enhances Vision-Language Models (VLMs) to comprehend 3D scenes directly from pure vision ...
- **p. 5 / 2 METHODOLOGY - extractive PDF cue:** To this end, we constructed ScanAlign, a large-scale instruction-tuning dataset designed to empower 2D VLMs with 3D understanding.
- **p. 5 / 2 METHODOLOGY - extractive PDF cue:** Published as a conference paper at ICLR 2026 2.3 ENHANCING VLMS WITH SCANALIGN FINE-TUNING Table 2: ScanAlign: Datasets used for training GPT4Scene (Supervised Fine-Tuning), Source ...
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** From the 3D point cloud P reconstructed from the video V, we apply 3D instance segmentation (e.g., Mask3D) to obtain instance masks M = {M1, ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | To establish Spatio-Temporal Object markers (STO-markers), we perform uniform frame sampling by selecting n frames at indices: si =  (i -1) ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To help VLMs focus on specific objects, we introduce Spatial-Temporal Object markers (STO-markers), ensuring consistency between 2D frames and the 3D BEV ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Training is done for one epoch with a base learning rate of 5e-6 and cosine annealing, completing in about 6 hours on ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 2 METHODOLOGY - extractive PDF cue:** Published as a conference paper at ICLR 2026 2.3 ENHANCING VLMS WITH SCANALIGN FINE-TUNING Table 2: ScanAlign: Datasets used for training GPT4Scene (Supervised Fine-Tuning), Source ...
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** In contrast, large-scale models like Qwen2-VL-72B and GPT-4o possess the architectural complexity to inherently grasp these feature associations, allowing them to form a preliminary 3D ...
- **p. 5 / 3 EXPERIMENTS - extractive PDF cue:** Training is done for one epoch with a base learning rate of 5e-6 and cosine annealing, completing in about 6 hours on 8×A100 GPUs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Here, introduce, GPT4Scene, architecture, Published, conference, ICLR, ENHANCING, VLMS, SCANALIGN, FINE-TUNING, Table, Datasets, training, Supervised, Source, Data, Type, Task, Samples.
- **Relevant PDF headings:** 2 METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The experiments are conducted across two different datasets, ScanNet ("S") and ARKitScenes ("NS"), to test the framework's robustness in various types of ... | p. 9 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS) |
| Semantic / temporal fusion | These models not only significantly outperform the untuned baseline VLMs but also comprehensively outperform the previous SOTA models in the 3D point ... | p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |
| Robot query / planning handoff | In terms of specific metrics, models fine-tuned using the GPT4Scene framework (based on the ScanAlign dataset) show outstanding performance: Qwen2-VL-7B (GPT4Scene) achieves ... | p. 5 (3 EXPERIMENTS), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 3 EXPERIMENTS - extractive PDF cue:** Finally, Subsection 3.3 details the ablation study, demonstrating the effectiveness of individual components.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6: Ablation study on the Efficacy of GPT4Scene. (1) on fully fine-tuned models with GPT4Scene; (2) on pure-video fine-tuned models; (3) in a zero-shot ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 6. First, we remove the regularized formatting from the answers. Next, we clean the answers by addressing singular/plural forms and case sensitivity. This final ...
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** 3.3 ABLATION STUDY In this section, we conduct ablation studies to validate the effectiveness of GPT4Scene.
- **p. 5 / 3 EXPERIMENTS - extractive PDF cue:** Our experimental analysis demonstrates that the baseline Qwen2-VL-7B model without fine-tuning shows constrained capability in 3D QA scenarios.
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** Next, we perform module-wise ablation to assess individual components.
- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** This ablation study in Table 9 provides a detailed analysis of GPT4Scene's two core components: the BEV image and STO-Markers.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (2 METHODOLOGY), p. 5 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), objective 본문 anchor 없음, temporal p. 3 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 5 (3 EXPERIMENTS), p. 5 (2 METHODOLOGY), p. 9 (3 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
