# Method - Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=pZIeK0Xvph; PDF retrieval source: https://openreview.net/pdf/7543305cf2956c454b415330b7bf04eda9e451f9.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 4 (3 Method)): enforces robust multi-view matching while mitigating potential feature shift; to ensure this loss is applied only to multi-view samples, we introduce an indicator function 1mv(i) that equals 1 if the ...

## Method Body Digest

- **p. 6 / 3 Method - extractive PDF cue:** enforces robust multi-view matching while mitigating potential feature shift; to ensure this loss is applied only to multi-view samples, we introduce an indicator function 1mv(i) ...
- **p. 5 / 3 Method - extractive PDF cue:** Recall that feed-forward 3D reconstruction models typically consist of a shared encoder, which extracts features from input images, followed by a decoder that correlates these ...
- **p. 6 / 3 Method - extractive PDF cue:** The overall training objective is the average loss over all N images, given by L = 1 N PN i=1  L(i) distill + L(i) ...
- **p. 5 / 3 Method - extractive PDF cue:** To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.
- **p. 4 / 3 Method - extractive PDF cue:** Although CUT3R [65] leverages extensive depth supervision and VGGT [61] employs gradient-based loss to refine local geometry-with both methods incorporating dedicated self-view pointmap or depth ...
- **p. 4 / 3 Method - extractive PDF cue:** (3) Scale Uncertainty: During training, both predicted and ground-truth pointmap require normalization to ensure scale consistency.2 However, this scale uncertainty tends to erode fine foreground ...
- **p. 5 / 3 Method - extractive PDF cue:** 3.3 Training We optimize two loss functions computed over images indexed by i in the training set.
- **p. 5 / 3 Method - extractive PDF cue:** For each image, the monocular distillation loss refines single-view details by aligning the predicted depth Di with the high-fidelity pseudo-label ˆDi provided by a monocular ...

## Design Rationale

- **p. 5 / 3 Method - extractive PDF cue:** To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.
- **p. 3 / 1 Introduction - extractive PDF cue:** To summarize, we propose a simple, effective, and general fine-tuning approach.
- **p. 5 / 3 Method - extractive PDF cue:** Teacher 𝐿!"#$"%% 𝐿&'"($)*& Unlabeled SingleView ~90% Figure 4: Pipeline of our method.

## Source Evidence Cues

- **p. 6 / 3 Method - extractive PDF cue:** enforces robust multi-view matching while mitigating potential feature shift; to ensure this loss is applied only to multi-view samples, we introduce an indicator function 1mv(i) ...
- **p. 5 / 3 Method - extractive PDF cue:** Recall that feed-forward 3D reconstruction models typically consist of a shared encoder, which extracts features from input images, followed by a decoder that correlates these ...
- **p. 6 / 3 Method - extractive PDF cue:** The overall training objective is the average loss over all N images, given by L = 1 N PN i=1  L(i) distill + L(i) ...
- **p. 5 / 3 Method - extractive PDF cue:** To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.
- **p. 4 / 3 Method - extractive PDF cue:** Although CUT3R [65] leverages extensive depth supervision and VGGT [61] employs gradient-based loss to refine local geometry-with both methods incorporating dedicated self-view pointmap or depth ...
- **p. 4 / 3 Method - extractive PDF cue:** (3) Scale Uncertainty: During training, both predicted and ground-truth pointmap require normalization to ensure scale consistency.2 However, this scale uncertainty tends to erode fine foreground ...
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | enforces robust multi-view matching while mitigating potential feature shift; to ensure this loss is applied only to multi-view samples, we introduce an ... | p. 6 (3 Method), p. 5 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Recall that feed-forward 3D reconstruction models typically consist of a shared encoder, which extracts features from input images, followed by a decoder ... | p. 5 (3 Method), p. 6 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The overall training objective is the average loss over all N images, given by L = 1 N PN i=1  L(i) ... | p. 6 (3 Method), p. 5 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Method - extractive PDF cue:** Although CUT3R [65] leverages extensive depth supervision and VGGT [61] employs gradient-based loss to refine local geometry-with both methods incorporating dedicated self-view pointmap or depth ...
- **p. 6 / 3 Method - extractive PDF cue:** The overall training objective is the average loss over all N images, given by L = 1 N PN i=1  L(i) distill + L(i) ...
- **p. 5 / 3 Method - extractive PDF cue:** 3.3 Training We optimize two loss functions computed over images indexed by i in the training set.
- **p. 5 / 3 Method - extractive PDF cue:** For each image, the monocular distillation loss refines single-view details by aligning the predicted depth Di with the high-fidelity pseudo-label ˆDi provided by a monocular ...
- **p. 6 / 3 Method - extractive PDF cue:** enforces robust multi-view matching while mitigating potential feature shift; to ensure this loss is applied only to multi-view samples, we introduce an indicator function 1mv(i) ...
- **p. 4 / 3 Method - extractive PDF cue:** (2) Drift: As the views progressively move further away from the initial reference frame, progressive drift becomes inevitable.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Input, Image, VGGT, Avg, LoRA, Only, Replay, Full, Figure, Heatmaps, spatial, variations, norms, encoder | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Input, Image, VGGT, Avg, LoRA, Only, Replay, Full, Figure, Heatmaps | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | directly, address, challenge, refined, integration, LoRA, re-normalization, strategy, specifically, designed | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Although, CUT3R, leverages, extensive, depth, supervision, VGGT, employs, gradient-based, loss | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive PDF cue:** (a) Input Image (b) VGGT Avg: 9.61 (c) LoRA Only Avg: 10.53 (d) LoRA+Replay Avg: 10.34 (e) Full Avg: 9.73 Figure 3: Heatmaps show spatial ...
- **p. 4 / 3 Method - extractive PDF cue:** Although CUT3R [65] leverages extensive depth supervision and VGGT [61] employs gradient-based loss to refine local geometry-with both methods incorporating dedicated self-view pointmap or depth ...
- **p. 5 / 3 Method - extractive PDF cue:** Recall that feed-forward 3D reconstruction models typically consist of a shared encoder, which extracts features from input images, followed by a decoder that correlates these ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Subsequent task-specific heads then regress pointmaps while optionally simultaneously estimating auxiliary outputs like camera parameters and depth.
- **p. 2 / 1 Introduction - extractive PDF cue:** At their core, these architectures share a common structure: a shared encoder extracts features from input images, followed by a decoder correlating these features across ...
- **p. 4 / 3 Method - extractive PDF cue:** These observations not only underscore the necessity for high-quality supervision from diverse datasets but also highlight the inherent challenges associated with multi-view pointmap regression.
- **p. 6 / 3 Method - extractive PDF cue:** enforces robust multi-view matching while mitigating potential feature shift; to ensure this loss is applied only to multi-view samples, we introduce an indicator function 1mv(i) ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The fine-tuned models consistently deliver sharper boundaries, recover complex structures, and achieve higher geometric accuracy in both single- and multi-view settings, while ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | (2) Drift: As the views progressively move further away from the initial reference frame, progressive drift becomes inevitable. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | The fine-tuned models consistently deliver sharper boundaries, recover complex structures, and achieve higher geometric accuracy in both single- and multi-view settings, while ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Training runs for 10 epochs on four NVIDIA L20 GPUs over a single day. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive PDF cue:** The overall training objective is the average loss over all N images, given by L = 1 N PN i=1  L(i) distill + L(i) ...
- **p. 5 / 3 Method - extractive PDF cue:** To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.
- **p. 4 / 3 Method - extractive PDF cue:** (3) Scale Uncertainty: During training, both predicted and ground-truth pointmap require normalization to ensure scale consistency.2 However, this scale uncertainty tends to erode fine foreground ...
- **p. 10 / 4.7 Discussion - extractive PDF cue:** By carefully fine-tuning the encoder, it avoids the resource-intensive decoder tuning, which typically requires long-sequence inputs from diverse datasets with large batch sizes.
- **p. 6 / 4 Experiment - extractive PDF cue:** Training runs for 10 epochs on four NVIDIA L20 GPUs over a single day.
- **p. 10 / 4.7 Discussion - extractive PDF cue:** This demonstrates that a robustly trained encoder benefits downstream heads even without direct supervision.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** enforces, robust, multi-view, matching, while, mitigating, potential, feature, shift, ensure, loss, applied, only, samples, introduce, indicator, function, equals, i-th, image.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Method ETH3D [49] T&T [27] KITTI [58] Sintel [6] Bonn [40] rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ δ1 ... | p. 8 (4 Experiment), p. 7 (4 Experiment) |
| Semantic / temporal fusion | Interestingly, we observe that although DUSt3R's depth estimates rank last among the evaluated models, they exhibit the sharpest boundaries compared with the ... | p. 6 (4 Experiment), p. 7 (4 Experiment) |
| Robot query / planning handoff | The results indicate that models enhanced with our distillation method consistently achieve lower Acc and Comp as well as improved NC scores ... | p. 8 (4 Experiment), p. 9 (4 Experiment) |

## Failure and Ablation Link

- **p. 6 / 4 Experiment - extractive PDF cue:** Since the depth predicted by MoGe is affine-invariant, we subtract the shift in the z-component and then apply the normalization used in DUSt3R.
- **p. 9 / 4 Experiment - extractive PDF cue:** Teacher SA-1B Rel (↓) δ1 (↑) Acc (↓) ✗ ✗ ✗ 5.68 94.1 0.017 ✓ ✗ ✗ 5.21 95.0 0.014 ✗ ✓ ✗ 5.00 95.3 ...
- **p. 9 / 4 Experiment - extractive PDF cue:** The top row represents VGGT model without fine-tuning, which can benefit from single-view distillation (second row) on a subset of training datasets (see appendix) with ...
- **p. 6 / 4 Experiment - extractive PDF cue:** Since CUT3R [65] is designed for long sequences and unsuitable for pairwise correspondences, we remove it in the two-view evaluation.
- **p. 8 / 4 Experiment - extractive PDF cue:** Because both DUSt3R and VGGT produce scale-invariant point maps, we apply Umeyama alignment [59] to align scale.
- **p. 10 / 4.7 Discussion - extractive PDF cue:** This demonstrates that a robustly trained encoder benefits downstream heads even without direct supervision.
- **p. 10 / 4.7 Discussion - extractive PDF cue:** Although further decoder tuning may yield additional gains, our method minimizes complexity without compromising quality.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 4 (3 Method), objective p. 4 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 4 (3 Method), temporal p. 2 (Abstract), p. 4 (3 Method), p. 4 (3 Method), p. 6 (4 Experiment), p. 6 (4 Experiment), p. 10 (4.7 Discussion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
