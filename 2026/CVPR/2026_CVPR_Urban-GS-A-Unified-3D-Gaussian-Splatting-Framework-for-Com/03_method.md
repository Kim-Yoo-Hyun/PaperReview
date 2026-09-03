# Method - Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4. Methods), p. 5 (4.3. Global-to-Local Optimization), p. 5 (4.2. Contribution-based Anchor Pruning), p. 4 (4. Methods), p. 6 (4.3. Global-to-Local Optimization), p. 6 (4.4. Loss Function)): In this section, we first analyze the conflicts during gradient accumulation in unified aerial-street modeling (Sec.

## Method Body Digest

- **p. 4 / 4. Methods - extractive body cue:** In this section, we first analyze the conflicts during gradient accumulation in unified aerial-street modeling (Sec.
- **p. 5 / 4.3. Global-to-Local Optimization - extractive body cue:** In the global training stage, the entire view set is used for scene modeling based on the methods described in Sec.
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** To achieve this goal, we integrate the structured 3D Gaussian representation [23] with probabilistic masks [17] and progressively prune redundant anchors throughout the training process.
- **p. 4 / 4. Methods - extractive body cue:** 4.4 elaborates on the training details.
- **p. 6 / 4.3. Global-to-Local Optimization - extractive body cue:** For each selected target unstable view vus, we construct an optimization view group Vus.
- **p. 6 / 4.4. Loss Function - extractive body cue:** 11), the overall objective function is formulated as: L = L1+λssimLssim+λvolLvol+λdLd+λoLo+λmLm.
- **p. 4 / 4.1. Aerial-Street Joint Adaptive Densification - extractive body cue:** Quantitative comparison across accumulating gradients for densification from aerial views only, street views only and merged views on Colosseum scene [10].
- **p. 6 / 4.3. Global-to-Local Optimization - extractive body cue:** This leads to more stable gradient accumulation and parameter updates during adaptive densification, while effectively mitigating forgetting problems.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** This method resolves densification conflicts, enabling joint contributions and enhancing overall reconstruction fidelity. • A Contribution-based Anchor Pruning method that enables reliable and efficient removal ...
- **p. 2 / 1. Introduction - extractive body cue:** To summarize, the main contributions of our method are: • An in-depth analysis of the densification conflicts in aerial-street scene reconstruction, and a corresponding Aerial-Street ...
- **p. 4 / 4. Methods - extractive body cue:** 4.2, we present a contribution-based anchor pruning strategy adopted in Urban-GS to mitigate the excessive memory consumption caused by capturing multi-scale scene details.

## Source Evidence Cues

- **p. 4 / 4. Methods - extractive body cue:** In this section, we first analyze the conflicts during gradient accumulation in unified aerial-street modeling (Sec.
- **p. 5 / 4.3. Global-to-Local Optimization - extractive body cue:** In the global training stage, the entire view set is used for scene modeling based on the methods described in Sec.
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** To achieve this goal, we integrate the structured 3D Gaussian representation [23] with probabilistic masks [17] and progressively prune redundant anchors throughout the training process.
- **p. 4 / 4. Methods - extractive body cue:** 4.4 elaborates on the training details.
- **p. 6 / 4.3. Global-to-Local Optimization - extractive body cue:** For each selected target unstable view vus, we construct an optimization view group Vus.
- **p. 6 / 4.4. Loss Function - extractive body cue:** 11), the overall objective function is formulated as: L = L1+λssimLssim+λvolLvol+λdLd+λoLo+λmLm.
- **Detected method headings:** 4. Methods (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In this section, we first analyze the conflicts during gradient accumulation in unified aerial-street modeling (Sec. | p. 4 (4. Methods), p. 5 (4.3. Global-to-Local Optimization) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In the global training stage, the entire view set is used for scene modeling based on the methods described in Sec. | p. 5 (4.3. Global-to-Local Optimization), p. 5 (4.2. Contribution-based Anchor Pruning) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To achieve this goal, we integrate the structured 3D Gaussian representation [23] with probabilistic masks [17] and progressively prune redundant anchors throughout ... | p. 5 (4.2. Contribution-based Anchor Pruning), p. 4 (4. Methods) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.1. Aerial-Street Joint Adaptive Densification - extractive body cue:** Quantitative comparison across accumulating gradients for densification from aerial views only, street views only and merged views on Colosseum scene [10].
- **p. 6 / 4.3. Global-to-Local Optimization - extractive body cue:** This leads to more stable gradient accumulation and parameter updates during adaptive densification, while effectively mitigating forgetting problems.
- **p. 4 / 4.1. Aerial-Street Joint Adaptive Densification - extractive body cue:** However, densification strategies that average gradient accumulation across all views (Eq.
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** In such cases, applying a global loss function like the one in Eq.
- **p. 5 / 4.1. Aerial-Street Joint Adaptive Densification - extractive body cue:** As derived previously, weighting the gradient magnitudes by the projected area yields a more balanced weighting scheme across different projection scales, promoting a more reliable ...
- **p. 6 / 4.4. Loss Function - extractive body cue:** 11), the overall objective function is formulated as: L = L1+λssimLssim+λvolLvol+λdLd+λoLo+λmLm.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.3. Global-to-Local Optimization), p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 5 (4.2. Contribution-based Anchor Pruning), p. 5 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.4. Loss Function).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Concurrently, drastic, variation, projection, areas, across, different, views, arises, precisely, large, observation, distances, inherent | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Concurrently, drastic, variation, projection, areas, across, different, views, arises, precisely | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | resolves, densification, conflicts, enabling, joint, contributions, enhancing, overall, reconstruction, fidelity | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Quantitative, comparison, across, accumulating, gradients, densification, aerial, views, only, street | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.1. Aerial-Street Joint Adaptive Densification - extractive body cue:** Concurrently, the drastic variation in projection areas across different views arises precisely from the large variation in observation distances inherent to the joint aerial-street view ...
- **p. 4 / 4.1. Aerial-Street Joint Adaptive Densification - extractive body cue:** Counterintuitively, involving richer inputs in the densification process yields poorer performance than using a single view type, which indicates the presence of gradient conflicts between ...
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** If this state persists for a certain period, the anchor is considered to have a low contribution and will be pruned.
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** This approach would cause anchors representing the aforementioned local details to be improperly pruned due to their infrequent observations, regardless of their critical contributions to ...
- **p. 3 / 3. Preliminaries - extractive body cue:** (1) To render images, the Gaussians are projected as 2D splats G′(x′), sorted by depth, and combined with α-blending using a tile-based rasterizer: C(p) = ...
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we start with investigating the counterintuitive phenomenon where rendering quality degrades despite using rich aerial-to-street view inputs.
- **p. 2 / 1. Introduction - extractive body cue:** This method resolves densification conflicts, enabling joint contributions and enhancing overall reconstruction fidelity. • A Contribution-based Anchor Pruning method that enables reliable and efficient removal ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The efficiency of models is measured by their number of anchors and rendering speed in Frames Per Second (FPS). | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Scene Colosseum Elvenruin Citysample Road Park Method/Metrics Anchors ↓ FPS ↑ Anchors ↓ FPS ↑ Anchors ↓ FPS ↑ Anchors ↓ FPS ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | This method resolves densification conflicts, enabling joint contributions and enhancing overall reconstruction fidelity. • A Contribution-based Anchor Pruning method that enables reliable ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The rendering speeds are tested on a RTX 4090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.3. Global-to-Local Optimization - extractive body cue:** In the global training stage, the entire view set is used for scene modeling based on the methods described in Sec.
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** To achieve this goal, we integrate the structured 3D Gaussian representation [23] with probabilistic masks [17] and progressively prune redundant anchors throughout the training process.
- **p. 4 / 4. Methods - extractive body cue:** 4.4 elaborates on the training details.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** For the global training stage, we set the learning rate of the mask scores to 0.01 and λm to 0.003, while retaining other parameter settings ...
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** 6, the aggregated contribution wi across the training views can be formulated as: wi = P v∈V /Pv i / · wv i · γscale ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** section, first, analyze, conflicts, during, gradient, accumulation, unified, aerial-street, modeling, Sec, global, training, stage, entire, view, scene, methods, described, achieve.
- **Relevant PDF headings:** 4. Methods (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Following Horizon-GS [10], we conduct comprehensive evaluations across 7 scenes containing both aerial and street views, sourced from the UC-GS dataset [40], ... | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Semantic / temporal fusion | 2, our method outperforms the performance of all baselines on the HorizonGS dataset. | p. 7 (5.2. Experiment Results and Analysis), p. 7 (5.2. Experiment Results and Analysis) |
| Robot query / planning handoff | 5 and 8 show that additional iterations under uniform sampling yield no significant performance improvement, whereas our proposed strategy achieves a more ... | p. 8 (5.3. Ablations Study and Analysis), p. 7 (5.2. Experiment Results and Analysis) |

## Failure and Ablation Link

- **p. 8 / 5.3. Ablations Study and Analysis - extractive body cue:** Ablation on main model components. "+" means adding components in addition to all components in the above rows. "AJAD", "CAP", and "GLO" denote our proposed ...
- **p. 8 / 5.3. Ablations Study and Analysis - extractive body cue:** Detailed ablation study on the proposed Global-toLocal Optimization.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The overview pipeline of Urban-GS. Top (Gloabal Training): We start by initializing LOD-structured anchors from SfM- derived points of the aerial-to-street urban scene, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Efficiency comparison between our method and Horizon-GS [10] on the Horizon-GS dataset. stage. For each selected target unstable view vus, we con- struct ...
- **p. 8 / 5.3. Ablations Study and Analysis - extractive body cue:** This limitation is evident in its struggles in the unified aerial-street setting.
- **p. 8 / 5.3. Ablations Study and Analysis - extractive body cue:** However, this approach fundamentally fails to account for the contribution variations caused by drastic changes in projection areas.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Average position gradient (a) and average projection radius (b) for two sets of neural Gaussians over the densification process. Left plots: Analysis of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4. Methods), p. 5 (4.3. Global-to-Local Optimization), p. 5 (4.2. Contribution-based Anchor Pruning), p. 4 (4. Methods), p. 6 (4.3. Global-to-Local Optimization), p. 6 (4.4. Loss Function), objective p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.3. Global-to-Local Optimization), p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 5 (4.2. Contribution-based Anchor Pruning), p. 5 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.4. Loss Function), temporal p. 6 (5.1. Experimental Setup), p. 6 (4.3. Global-to-Local Optimization), p. 1 (body section not recovered), p. 2 (1. Introduction), p. 4 (4. Methods), p. 5 (4.2. Contribution-based Anchor Pruning).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
