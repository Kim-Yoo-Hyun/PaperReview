# Method - ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.08830; PDF retrieval source: https://arxiv.org/pdf/1912.08830. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (5 Method), p. 7 (5 Method), p. 9 (5 Method), p. 6 (5 Method), p. 8 (5 Method), p. 8 (5 Method)): 6: ScanRefer architecture: The PointNet++ [51] backbone takes as input a point cloud and aggregates it to high-level point feature maps, which are then clustered and fused as object proposals ...

## Method Body Digest

- **p. 7 / 5 Method - extractive PDF cue:** 6: ScanRefer architecture: The PointNet++ [51] backbone takes as input a point cloud and aggregates it to high-level point feature maps, which are then clustered ...
- **p. 7 / 5 Method - extractive PDF cue:** 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input description and outputs ...
- **p. 9 / 5 Method - extractive PDF cue:** 5.4 Training and Inference Training During training, the detection and encoding modules propose object candidates as point clusters, which are then fed into the fusion ...
- **p. 6 / 5 Method - extractive PDF cue:** Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.
- **p. 8 / 5 Method - extractive PDF cue:** Object detection loss We use the same detection loss Ldet as introduced in Qi et al.
- **p. 8 / 5 Method - extractive PDF cue:** Next, the proposal module takes in the point clusters and processes those clusters to predict the objectness mask Dobjn ∈RM×1 and the axis-aligned bounding boxes ...
- **p. 9 / 5 Method - extractive PDF cue:** In the localization module, we use a softmax function to compress the raw scores to [0, 1].
- **p. 8 / 5 Method - extractive PDF cue:** We then use a cross-entropy loss as the localization loss Lloc = -PM i=1 ti log(si).

## Design Rationale

- **p. 6 / 5 Method - extractive PDF cue:** Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.
- **p. 7 / 5 Method - extractive PDF cue:** 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input description and outputs ...
- **p. 8 / 5 Method - extractive PDF cue:** Conceptually, our localization pipeline consists of the following four stages: detection, encoding, fusion and localization.

## Source Evidence Cues

- **p. 7 / 5 Method - extractive PDF cue:** 6: ScanRefer architecture: The PointNet++ [51] backbone takes as input a point cloud and aggregates it to high-level point feature maps, which are then clustered ...
- **p. 7 / 5 Method - extractive PDF cue:** 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input description and outputs ...
- **p. 9 / 5 Method - extractive PDF cue:** 5.4 Training and Inference Training During training, the detection and encoding modules propose object candidates as point clusters, which are then fed into the fusion ...
- **p. 6 / 5 Method - extractive PDF cue:** Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.
- **p. 8 / 5 Method - extractive PDF cue:** Object detection loss We use the same detection loss Ldet as introduced in Qi et al.
- **p. 8 / 5 Method - extractive PDF cue:** Next, the proposal module takes in the point clusters and processes those clusters to predict the objectness mask Dobjn ∈RM×1 and the axis-aligned bounding boxes ...
- **p. 9 / 5 Method - extractive PDF cue:** In the localization module, we use a softmax function to compress the raw scores to [0, 1].
- **Detected method headings:** 5 Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 6: ScanRefer architecture: The PointNet++ [51] backbone takes as input a point cloud and aggregates it to high-level point feature maps, which ... | p. 7 (5 Method), p. 7 (5 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input ... | p. 7 (5 Method), p. 9 (5 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 5.4 Training and Inference Training During training, the detection and encoding modules propose object candidates as point clusters, which are then fed ... | p. 9 (5 Method), p. 6 (5 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 5 Method - extractive PDF cue:** We then use a cross-entropy loss as the localization loss Lloc = -PM i=1 ti log(si).
- **p. 9 / 5 Method - extractive PDF cue:** The language to object classification loss Lcls is a multi-class cross-entropy loss.
- **p. 7 / 5 Method - extractive PDF cue:** In addition, an extra language-to-object classifier serves as a proxy loss.
- **p. 8 / 5 Method - extractive PDF cue:** Object detection loss We use the same detection loss Ldet as introduced in Qi et al.
- **p. 9 / 5 Method - extractive PDF cue:** We train the detection backbone end-to-end with the detection loss.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 7 (5 Method), p. 8 (5 Method), p. 8 (5 Method), p. 9 (5 Method), p. 9 (5 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | detection, encoding, module, encodes, input, point, cloud, description, outputs, object, proposals, language, embedding, fusion | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | detection, encoding, module, encodes, input, point, cloud, description, outputs, object | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | architecture, consists, main, modules, detection, encoding, fusion, localization, Fig, Network | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | then, cross-entropy, loss, localization, Lloc, language, object, classification, Lcls, multi-class | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 5 Method - extractive PDF cue:** The detection & encoding module encodes the input point cloud and description, and outputs the object proposals and the language embedding, which are fed into ...
- **p. 7 / 5 Method - extractive PDF cue:** 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input description and outputs ...
- **p. 7 / 5 Method - extractive PDF cue:** 6: ScanRefer architecture: The PointNet++ [51] backbone takes as input a point cloud and aggregates it to high-level point feature maps, which are then clustered ...
- **p. 8 / 5 Method - extractive PDF cue:** [49] to process the point cloud input and aggregate all object candidates to individual clusters.
- **p. 8 / 5 Method - extractive PDF cue:** We take the final hidden state e ∈R256 of the GRU cell as the final language embedding.
- **p. 9 / 5 Method - extractive PDF cue:** Language to object classification loss To further supervise the training, we include an object classification loss based on the input description.
- **p. 9 / 5 Method - extractive PDF cue:** The higher the predicted confidence is, the more likely the proposal will be chosen as output.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Detection As the first step in our network, we detect all probable objects in the given point cloud. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The detection & encoding module encodes the input point cloud and description, and outputs the object proposals and the language embedding, which ... | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 5 Method - extractive PDF cue:** 5.4 Training and Inference Training During training, the detection and encoding modules propose object candidates as point clusters, which are then fed into the fusion ...
- **p. 10 / 6 Experiments - extractive PDF cue:** At inference time, we sample frames from the scans (using every 20th frame) and predict the target 2D bounding boxes in each frame.
- **p. 9 / 5 Method - extractive PDF cue:** Implementation Details We implement our architecture using PyTorch and train the model end-to-end using ADAM [29] with a learning rate of 1e-3.
- **p. 12 / 6 Experiments - extractive PDF cue:** Image best viewed in color. we take the average of 5 differently seeded subsamplings (of seed points and vote points) during inference (see supplemental for ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ScanRefer, architecture, PointNet, backbone, takes, input, point, cloud, aggregates, high-level, feature, maps, then, clustered, fused, object, proposals, voting, module, similar.
- **Relevant PDF headings:** 5 Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4: Description lengths Number of descriptions 51,583 Number of scenes 800 Number of objects 11,046 Number of objects per scene 13.81 Number ... | p. 5 (4 Dataset), p. 9 (6 Experiments) |
| Semantic / temporal fusion | We outperform all baselines by a significant margin. | p. 11 (6 Experiments), p. 11 (6 Experiments) |
| Robot query / planning handoff | The additional 3D information improves performance. | p. 14 (6 Experiments), p. 14 (6 Experiments) |

## Failure and Ablation Link

- **p. 14 / 6 Experiments - extractive PDF cue:** To show the effectiveness of the extra supervision on input descriptions, we conduct an experiment with the language to object classifier (+lobjcls) and without.
- **p. 13 / 6 Experiments - extractive PDF cue:** 6.4 Ablation Studies We conduct an ablation study on our model to examine what components and point cloud features contribute to the performance (see Tab.
- **p. 14 / 6 Experiments - extractive PDF cue:** Architectures with a language to object classifier outperform ones without it.
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 5: Ablation study with different features. We measure the percentages of predictions whose IoU with the ground truth boxes are greater than 0.25 and ...
- **p. 28 / B.1 Fusion Module - extractive PDF cue:** As expected, models with the language-based object classifier (rows [g-k]) does not results in better object detection compared to models without such a module (rows ...
- **p. 30 / Figure/Table caption - extractive PDF cue:** Table 10: Variance between evaluation runs due to the random sampling of points in the VoteNet [49]. We train our model (xyz+multiview+normal+lobjcls) with the a ...
- **p. 31 / Figure/Table caption - extractive PDF cue:** Table 11: Ablation study with different input lengths. We measure the percent- ages of predictions whose IoU with the ground truth boxes are greater than ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (5 Method), p. 7 (5 Method), p. 9 (5 Method), p. 6 (5 Method), p. 8 (5 Method), p. 8 (5 Method), objective p. 8 (5 Method), p. 9 (5 Method), p. 7 (5 Method), p. 8 (5 Method), p. 9 (5 Method), temporal p. 7 (5 Method), p. 8 (5 Method), p. 8 (5 Method), p. 9 (5 Method), p. 9 (5 Method), p. 10 (6 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
