# Method - MonoScene: Monocular 3D Semantic Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.00726; PDF retrieval source: https://arxiv.org/pdf/2112.00726. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (3. Method), p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), p. 4 (3.2. 3D Context Relation Prior (3D CRP)), p. 4 (3.3. Losses)): To guide the SSC training, we introduce new complementary losses.

## Method Body Digest

- **p. 2 / 3. Method - extractive body cue:** To guide the SSC training, we introduce new complementary losses.
- **p. 3 / 3.1. Features Line of Sight Projection (FLoSP) - extractive body cue:** We argue this enables 2D-3D disentangled representations, providing the 3D network with the freedom to use high-level 2D features for fine-grained 3D disambiguation.
- **p. 2 / 3. Method - extractive body cue:** First, a Scene-Class Affinity Loss (Sec.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** We then optimize a weighted multilabel binary cross entropy loss: Lrel=- X m∈M,i [(1-Am i ) log(1- ˆAm i )+wmAm i log ˆAm i ], ...
- **p. 4 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** The feature dimension is omitted for clarity.
- **p. 4 / 3.3. Losses - extractive body cue:** We now introduce new losses pursuing distinct global (Sec.
- **p. 4 / 3.3. Losses - extractive body cue:** For more generality, our loss Lscal maximizes the above class-wise metrics with: Lscal(ˆp, p) = -1
- **p. 4 / 3.4. Training strategy - extractive body cue:** MonoScene is trained end-to-end from scratch by optimizing our 4 losses and the standard cross-entropy (Lce): Ltotal = Lce + Lrel + Lsem scal + ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** Our framework infers dense semantic scenes, hallucinating scenery outside the field of view of the image (dark voxels, right). and outdoor scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Here, we present MonoScene which - unlike the literature - relies on a single RGB image to infer the dense 3D voxelized semantic scene working ...
- **p. 2 / 3. Method - extractive body cue:** To guide the SSC training, we introduce new complementary losses.

## Source Evidence Cues

- **p. 2 / 3. Method - extractive body cue:** To guide the SSC training, we introduce new complementary losses.
- **p. 3 / 3.1. Features Line of Sight Projection (FLoSP) - extractive body cue:** We argue this enables 2D-3D disentangled representations, providing the 3D network with the freedom to use high-level 2D features for fine-grained 3D disambiguation.
- **p. 2 / 3. Method - extractive body cue:** First, a Scene-Class Affinity Loss (Sec.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** We then optimize a weighted multilabel binary cross entropy loss: Lrel=- X m∈M,i [(1-Am i ) log(1- ˆAm i )+wmAm i log ˆAm i ], ...
- **p. 4 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** The feature dimension is omitted for clarity.
- **p. 4 / 3.3. Losses - extractive body cue:** We now introduce new losses pursuing distinct global (Sec.
- **Detected method headings:** 3. Method (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To guide the SSC training, we introduce new complementary losses. | p. 2 (3. Method), p. 3 (3.1. Features Line of Sight Projection (FLoSP)) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We argue this enables 2D-3D disentangled representations, providing the 3D network with the freedom to use high-level 2D features for fine-grained 3D ... | p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | First, a Scene-Class Affinity Loss (Sec. | p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3. Losses - extractive body cue:** For more generality, our loss Lscal maximizes the above class-wise metrics with: Lscal(ˆp, p) = -1
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** We then optimize a weighted multilabel binary cross entropy loss: Lrel=- X m∈M,i [(1-Am i ) log(1- ˆAm i )+wmAm i log ˆAm i ], ...
- **p. 4 / 3.4. Training strategy - extractive body cue:** MonoScene is trained end-to-end from scratch by optimizing our 4 losses and the standard cross-entropy (Lce): Ltotal = Lce + Lrel + Lsem scal + ...
- **p. 2 / 3. Method - extractive body cue:** Second, a Frustum Proportion Loss (Sec.
- **p. 2 / 3. Method - extractive body cue:** First, a Scene-Class Affinity Loss (Sec.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** This writes, V↔ν = {ν1↔ν, . . . , νs3↔ν}̸=, (2) where {·}̸= returns distinct elements of a set.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (3. Method), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), p. 4 (3.3. Losses), p. 4 (3.3. Losses).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | output, F3D, UNet, input, been, almost, exclusively, addressed, inputs, point, cloud, depth, else, strong | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | output, F3D, UNet, input, been, almost, exclusively, addressed, inputs, point | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | framework, infers, dense, semantic, scenes, hallucinating, scenery, outside, field, view | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | more, generality, loss, Lscal, maximizes, above, class-wise, metrics, then, optimize | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Features Line of Sight Projection (FLoSP) - extractive body cue:** The output map F3D is used as 3D UNet input.
- **p. 2 / 3. Method - extractive body cue:** This has been almost exclusively addressed with 2.5D or 3D inputs [56], such as point cloud, depth or else, which act as strong geometrical cues.
- **p. 2 / 3. Method - extractive body cue:** The 2D UNet bases on a pre-trained EfficientNetB7 [61] taking as input the image xrgb.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** It takes as input a 3D map of spatial dimension HxWxD, on which is applied a serie of ASPP convolutions [7] to gather a large ...
- **p. 1 / 1. Introduction - extractive body cue:** Here, we present MonoScene which - unlike the literature - relies on a single RGB image to infer the dense 3D voxelized semantic scene working ...
- **p. 4 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** The matrices are multiplied with the supervoxels features to gather context, and later combined (concate, conv, DDR [40]) with input features.
- **p. 1 / 1. Introduction - extractive body cue:** 1, where it outperformed all comparable baselines and even some 3D input baselines.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | (b) For memory reason, we encode Supervoxel↔Voxel relations framed as multi-label classification. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Main results are from the hidden test set (online server), and ablations are from the validation set. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | (b) For memory reason, we encode Supervoxel↔Voxel relations framed as multi-label classification. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We train 30 epochs with an AdamW [46] optimizer, a batch size of 4 and a weight decay of 1e-4. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 3. Method - extractive body cue:** To guide the SSC training, we introduce new complementary losses.
- **p. 5 / 4. Experiments - extractive body cue:** We train 30 epochs with an AdamW [46] optimizer, a batch size of 4 and a weight decay of 1e-4.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** guide, SSC, training, introduce, complementary, losses, argue, enables, D-3D, disentangled, representations, providing, network, freedom, high-level, features, fine-grained, disambiguation, First, Scene-Class.
- **Relevant PDF headings:** 3. Method (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate MonoScene on popular real-world SSC datasets being, indoor NYUv2 [58] and outdoor Se4 | p. 4 (4. Experiments), p. 5 (4.2.1 Evaluation) |
| Semantic / temporal fusion | 7b), compared to baselines, MonoScene evidently captures better the scene layout, e.g. cross-roads (rows 1,3). | p. 5 (4.2.1 Evaluation), p. 6 (4.2.1 Evaluation) |
| Robot query / planning handoff | Despite the various indoor and outdoor setups, we significantly outperform other RGB-inferred baselines, in both mIoU and IoU. | p. 6 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation) |

## Failure and Ablation Link

- **p. 8 / 4.3. Ablation studies - extractive body cue:** To properly evaluate only the effect of features projection, we remove our other components, producing a light version (‘Ours-light') with the same 2D encoder (E), ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Type of 2D-3D features projections. (a) Comparing our FLoSP and ‘Ray-traced skip connections' from CoReNet [52] (cf. text) shows in (b) we get ...
- **p. 7 / 4.3. Ablation studies - extractive body cue:** We now study in-depth the effect of FLoSP (Sec.
- **p. 5 / 4. Experiments - extractive body cue:** Main results are from the hidden test set (online server), and ablations are from the validation set.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Architecture ablation. Our components boost perfor- mance on NYUv2 [58] (test set) and SemanticKitti [3] (val. set). a comfortable margin (+6.48 and +3.17), ...
- **p. 5 / 4.1. Baselines - extractive body cue:** We use the pretrained AdaBin [4] to infer a depth map (ˆxdepth) serving as input for AICNetrgb.
- **p. 6 / 4.2.1 Evaluation - extractive body cue:** (0.05%) ■fence (3.90%) ■pole (0.29%) ■traf.-sign (0.08%) mIoU LMSCNetrgb [55] ˆxocc 31.38 46.70 19.50 13.50 3.10 10.30 14.30 0.30 0.00 0.00 0.00 10.80 0.00 10.40 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (3. Method), p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), p. 4 (3.2. 3D Context Relation Prior (3D CRP)), p. 4 (3.3. Losses), objective p. 4 (3.3. Losses), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), p. 4 (3.4. Training strategy), p. 2 (3. Method), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), temporal p. 3 (3.2. 3D Context Relation Prior (3D CRP)), p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.2.1 Evaluation), p. 7 (4.3. Ablation studies), p. 8 (4.3. Ablation studies).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
