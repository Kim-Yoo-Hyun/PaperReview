# Method - OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Local Consistent Map Construction), p. 3 (3. Method), p. 4 (3.2. Local Consistent Map Construction), p. 4 (3.2. Local Consistent Map Construction), p. 5 (3.3. Local-to-Global Map Fusion), p. 5 (3.3. Local-to-Global Map Fusion)): For i-th keyframe inside the sliding window W, we use LSeg [17] and EntitySeg [21] to extract its 2D feature map fi ∈RH×W ×Df and instance mask mi ∈RH×W .

## Method Body Digest

- **p. 3 / 3.2. Local Consistent Map Construction - extractive PDF cue:** For i-th keyframe inside the sliding window W, we use LSeg [17] and EntitySeg [21] to extract its 2D feature map fi ∈RH×W ×Df and ...
- **p. 3 / 3. Method - extractive PDF cue:** To mitigate the inconsistencies of 2D segmentation results, we propose an effective segment clustering algorithm that synergistically leverages geometric and semantic cues to obtain consistent ...
- **p. 4 / 3.2. Local Consistent Map Construction - extractive PDF cue:** The semantic cue is then computed as the cosine similarity between language features: X(Si, Sj) = zi · zj/(//zi// · //zj//).
- **p. 4 / 3.2. Local Consistent Map Construction - extractive PDF cue:** Through this multi-cue graph clustering algorithm, we obtain geometrically and semantically consistent 3D Gaussian instances I from the local sliding window.
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive PDF cue:** For each voxel v occupied by a clustered instance I, we update the global feature grid Ft g and confidence grid Ct g using weighted ...
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive PDF cue:** construct a forward correspondence score matrix Ml→g ∈ Rnl×ng: Ml→g = zl · zg //zl// · //zg// + /Il ∩Ig/ Cont.(Il, Ig), (10) where nl ...
- **p. 3 / 3.1. Scene Representation - extractive PDF cue:** Following previous works [11, 23], we adopt the L1 loss terms for appearance and geometry optimization: L = α · Lc + (1 -α) · ...
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive PDF cue:** Since spatial attributes store discrete instance information in voxel form, we cannot perform continuous gradient updates.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Overall, the technical contributions of our approach are summarized as follows: • We propose an online open-vocabulary panoptic mapping framework that unifies geometric reconstruction and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we present OnlinePG, an efficient online open-vocabulary panoptic mapping system based on 3D Gaussian Splatting that integrates geometric reconstruction with semantic understanding.
- **p. 3 / 3. Method - extractive PDF cue:** To mitigate the inconsistencies of 2D segmentation results, we propose an effective segment clustering algorithm that synergistically leverages geometric and semantic cues to obtain consistent ...

## Source Evidence Cues

- **p. 3 / 3.2. Local Consistent Map Construction - extractive PDF cue:** For i-th keyframe inside the sliding window W, we use LSeg [17] and EntitySeg [21] to extract its 2D feature map fi ∈RH×W ×Df and ...
- **p. 3 / 3. Method - extractive PDF cue:** To mitigate the inconsistencies of 2D segmentation results, we propose an effective segment clustering algorithm that synergistically leverages geometric and semantic cues to obtain consistent ...
- **p. 4 / 3.2. Local Consistent Map Construction - extractive PDF cue:** The semantic cue is then computed as the cosine similarity between language features: X(Si, Sj) = zi · zj/(//zi// · //zj//).
- **p. 4 / 3.2. Local Consistent Map Construction - extractive PDF cue:** Through this multi-cue graph clustering algorithm, we obtain geometrically and semantically consistent 3D Gaussian instances I from the local sliding window.
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive PDF cue:** For each voxel v occupied by a clustered instance I, we update the global feature grid Ft g and confidence grid Ct g using weighted ...
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive PDF cue:** construct a forward correspondence score matrix Ml→g ∈ Rnl×ng: Ml→g = zl · zg //zl// · //zg// + /Il ∩Ig/ Cont.(Il, Ig), (10) where nl ...
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | For i-th keyframe inside the sliding window W, we use LSeg [17] and EntitySeg [21] to extract its 2D feature map fi ... | p. 3 (3.2. Local Consistent Map Construction), p. 3 (3. Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | To mitigate the inconsistencies of 2D segmentation results, we propose an effective segment clustering algorithm that synergistically leverages geometric and semantic cues ... | p. 3 (3. Method), p. 4 (3.2. Local Consistent Map Construction) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The semantic cue is then computed as the cosine similarity between language features: X(Si, Sj) = zi · zj/(//zi// · //zj//). | p. 4 (3.2. Local Consistent Map Construction), p. 4 (3.2. Local Consistent Map Construction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Scene Representation - extractive PDF cue:** Following previous works [11, 23], we adopt the L1 loss terms for appearance and geometry optimization: L = α · Lc + (1 -α) · ...
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive PDF cue:** Since spatial attributes store discrete instance information in voxel form, we cannot perform continuous gradient updates.
- **p. 3 / 3.1. Scene Representation - extractive PDF cue:** The 3D scene properties can be rasterized to the 2D image plane via fast differentiable rasterization [24] for differentiable optimization.
- **p. 4 / 3.2. Local Consistent Map Construction - extractive PDF cue:** After clustering the 3D Gaussian segments, we voxelize the 3D space to efficiently compute and update spatial attributes.
- **p. 4 / 3.2. Local Consistent Map Construction - extractive PDF cue:** We formulate the clustering graph as ({Si}, {Eij}), where 3D segments are defined as the vertices Si, and the edges Eij represent the affinity between ...
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive PDF cue:** Instead, we update the instance label T t g and weight Kt g grids similar to [25, 28]: • For matched instances: We merge the ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.3. Local-to-Global Map Fusion), p. 3 (3.1. Scene Representation), p. 4 (3.2. Local Consistent Map Construction), p. 5 (3.3. Local-to-Global Map Fusion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | voxel, occupied, instance, assign, local, label, weight, grids, IDi, where, denotes, time, index, number | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | voxel, occupied, instance, assign, local, label, weight, grids, IDi, where | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Overall, technical, contributions, summarized, follows, online, open-vocabulary, panoptic, mapping, framework | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Following, previous, works, adopt, loss, terms, appearance, geometry, optimization, where | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Local Consistent Map Construction - extractive PDF cue:** For each voxel v occupied by instance Ii, we assign the local instance label and weight grids: T t l (v) = IDi, Kt l(v) ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Open-vocabulary 3D scene understanding is fundamental for embodied tasks, enabling robots to perceive, reason about, and interact with complex environments using natural language and instruction ...
- **p. 3 / 3.2. Local Consistent Map Construction - extractive PDF cue:** Therefore, we maintain a sliding window over the input stream and perform 3D segment clustering to obtain consistent instances while mitigating noise from 2D priors.
- **p. 4 / 3.2. Local Consistent Map Construction - extractive PDF cue:** (2) Semantic cue: To obtain the language feature for segment Si, we pool the language feature map according to its 2D mask: zi = Φ({f(u, ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Overall, the technical contributions of our approach are summarized as follows: • We propose an online open-vocabulary panoptic mapping framework that unifies geometric reconstruction and ...
- **p. 3 / 3.1. Scene Representation - extractive PDF cue:** The 3D scene properties can be rasterized to the 2D image plane via fast differentiable rasterization [24] for differentiable optimization.
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive PDF cue:** However, since the local map contains newly explored regions while the global map contains historical regions, the correspondence matrix is inherently asymmetric, particularly in geometric ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Since clustering and fusion process multiple keyframes per sliding window movement (frequency much lower than framerate), our system achieves 18 FPS on ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Extensive experiments on widely used datasets demonstrate that our method achieves better performance among online approaches, while maintaining real-time efficiency. †Corresponding author. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Since clustering and fusion process multiple keyframes per sliding window movement (frequency much lower than framerate), our system achieves 18 FPS on ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** We evaluate the runtime performance of OnlinePG on a desktop computer equipped with an AMD Ryzen 9 7950X CPU and an NVIDIA RTX 4090 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** i-th, keyframe, inside, sliding, window, LSeg, EntitySeg, extract, feature, instance, mask, mitigate, inconsistencies, segmentation, effective, segment, clustering, algorithm, synergistically, leverages.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Following [50, 58], we take the commonly-used 8 scenes {room0-2,office0-4} for Replica dataset. | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings) |
| Global / local decision | Figure 3. Qualitative 3D Semantic Segmentation Comparison of ScanNetV2 Dataset. Our approach outperforms recent online ap- proaches, O2V-Mapping [42] and OnlineAnySeg [41], ... | p. 6 (Figure/Table caption), p. 7 (4.2. Main Experiments) |
| Motion execution / recovery | Compared to single-cue clustering, multi-cue clustering achieves 8 to 18 PRQ improvement with only ∼40 33275 | p. 7 (4.3. Ablation Studies), p. 6 (4.2. Main Experiments) |

## Failure and Ablation Link

- **p. 5 / 4. Experiments - extractive PDF cue:** Additionally, we perform a detailed ablation study to validate the effect of each design in our system.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Ablation studies of our system components.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Right: ablation studies of using different feature grid resolutions.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Limitations: (1) Our method currently cannot reconstruct dynamic objects.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Our future work will explore feed-forward approaches [20, 46, 47] that eliminate these requirements for fully pose-free and depth-free openvocabulary reconstruction.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Since the baselines [31, 33, 50] marked with ∗ cannot obtain 3D panoptic results, we use the performance reported in [58], which uses a supervised ...
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** While OnlineAnySeg can handle simple queries (e.g., "television"), it fails on some fine-grained and multi-instance queries (e.g., "pillow", "toilet paper", "bag") due to inaccurate 3D ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.2. Local Consistent Map Construction), p. 3 (3. Method), p. 4 (3.2. Local Consistent Map Construction), p. 4 (3.2. Local Consistent Map Construction), p. 5 (3.3. Local-to-Global Map Fusion), p. 5 (3.3. Local-to-Global Map Fusion), objective p. 3 (3.1. Scene Representation), p. 5 (3.3. Local-to-Global Map Fusion), p. 3 (3.1. Scene Representation), p. 4 (3.2. Local Consistent Map Construction), p. 4 (3.2. Local Consistent Map Construction), p. 5 (3.3. Local-to-Global Map Fusion), temporal p. 7 (4.2. Main Experiments), p. 1 (Abstract), p. 2 (1. Introduction), p. 3 (3.2. Local Consistent Map Construction), p. 3 (3.1. Scene Representation), p. 4 (3.2. Local Consistent Map Construction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
