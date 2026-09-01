# Method - Open-Vocabulary Octree-Graph for 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.5. Octree-Graph Construction and Applications), p. 4 (3.4. Instance Feature Aggregation), p. 3 (3.1. Framework Overview), p. 3 (3.2. Segment Proposal and Comprehension), p. 5 (3.5. Octree-Graph Construction and Applications)): The node Ni consists of correlated semantics ns i (e.g., captions and features), center nc i, and adaptive-octree no i .

## Method Body Digest

- **p. 4 / 3.5. Octree-Graph Construction and Applications - extractive PDF cue:** The node Ni consists of correlated semantics ns i (e.g., captions and features), center nc i, and adaptive-octree no i .
- **p. 4 / 3.4. Instance Feature Aggregation - extractive PDF cue:** Hence, we propose a weighted average method to fuse an instance's features for an optimal feature both representative and distinctive, as shown in Fig.
- **p. 3 / 3.1. Framework Overview - extractive PDF cue:** Then we dynamically aggregate the redundant semantics of each instance into a distinctive feature (§ 3.4).
- **p. 3 / 3.2. Segment Proposal and Comprehension - extractive PDF cue:** Next, each mi is fed into the visual encoder and caption generator to obtain the visual feature f v i and caption feature f c ...
- **p. 5 / 3.5. Octree-Graph Construction and Applications - extractive PDF cue:** The proposed Octree-Graph supports such queries, enabling us to easily implement path planning algorithms like classical A∗[9] and the recent [52].
- **p. 2 / 1. Introduction - extractive PDF cue:** First, given input images, 2D proposals are segmented via an off-the-shelf segmenter, and corresponding visual-language features are extracted by pretrained VLMs.
- **p. 4 / 3.3. Chronological Group-wise Segment Merging - extractive PDF cue:** Subsequently, we iteratively take the union {Mk-1, Gk} as input for the kth merging, until the final instance map M is constructed.
- **p. 1 / 1. Introduction - extractive PDF cue:** Given an RGB-D sequence with camera poses, mainstream methods leverage the off-theshelf foundation models to generate 2D object masks and corresponding visual-language features, and then ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are summarized as follows. • We propose the Octree-Graph for open-vocabulary 3D scene understanding, which efficiently depicts objects' occupancies, semantics, and relations, benefiting ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To alleviate these problems, we propose Octree-Graph as shown in Fig.
- **p. 3 / 3.3. Chronological Group-wise Segment Merging - extractive PDF cue:** To this end, we propose a Chronological Group-wise Segment Merging (CGSM) strategy with semantic-guided under-segment filtering and a dynamic threshold decay strategy.

## Source Evidence Cues

- **p. 4 / 3.5. Octree-Graph Construction and Applications - extractive PDF cue:** The node Ni consists of correlated semantics ns i (e.g., captions and features), center nc i, and adaptive-octree no i .
- **p. 4 / 3.4. Instance Feature Aggregation - extractive PDF cue:** Hence, we propose a weighted average method to fuse an instance's features for an optimal feature both representative and distinctive, as shown in Fig.
- **p. 3 / 3.1. Framework Overview - extractive PDF cue:** Then we dynamically aggregate the redundant semantics of each instance into a distinctive feature (§ 3.4).
- **p. 3 / 3.2. Segment Proposal and Comprehension - extractive PDF cue:** Next, each mi is fed into the visual encoder and caption generator to obtain the visual feature f v i and caption feature f c ...
- **p. 5 / 3.5. Octree-Graph Construction and Applications - extractive PDF cue:** The proposed Octree-Graph supports such queries, enabling us to easily implement path planning algorithms like classical A∗[9] and the recent [52].
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The node Ni consists of correlated semantics ns i (e.g., captions and features), center nc i, and adaptive-octree no i . | p. 4 (3.5. Octree-Graph Construction and Applications), p. 4 (3.4. Instance Feature Aggregation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Hence, we propose a weighted average method to fuse an instance's features for an optimal feature both representative and distinctive, as shown ... | p. 4 (3.4. Instance Feature Aggregation), p. 3 (3.1. Framework Overview) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Then we dynamically aggregate the redundant semantics of each instance into a distinctive feature (§ 3.4). | p. 3 (3.1. Framework Overview), p. 3 (3.2. Segment Proposal and Comprehension) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, given, input, images, proposals, segmented, off-the-shelf, segmenter, corresponding, visual-language, features, extracted, pretrained, VLMs | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | First, given, input, images, proposals, segmented, off-the-shelf, segmenter, corresponding, visual-language | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, Octree-Graph, open-vocabulary, scene, understanding, efficiently, depicts, objects | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** First, given input images, 2D proposals are segmented via an off-the-shelf segmenter, and corresponding visual-language features are extracted by pretrained VLMs.
- **p. 4 / 3.3. Chronological Group-wise Segment Merging - extractive PDF cue:** Subsequently, we iteratively take the union {Mk-1, Gk} as input for the kth merging, until the final instance map M is constructed.
- **p. 1 / 1. Introduction - extractive PDF cue:** Given an RGB-D sequence with camera poses, mainstream methods leverage the off-theshelf foundation models to generate 2D object masks and corresponding visual-language features, and then ...
- **p. 4 / 3.5. Octree-Graph Construction and Applications - extractive PDF cue:** Each sub-region serves as a child node, and the process continues recursively for each node until the desired octree depth Lmax is reached or no ...
- **p. 3 / 3.1. Framework Overview - extractive PDF cue:** As shown in Fig 2, given a sequence of RGB images Ic = {Ic t}T t=1 and depth images Id = {Id t }T t=1 ...
- **p. 5 / 3.5. Octree-Graph Construction and Applications - extractive PDF cue:** For more complex queries, we leverage the reasoning capabilities of LLMs to decompose the task and flexibly call two types of functions to achieve the ...
- **p. 2 / 1. Introduction - extractive PDF cue:** object segmentation and feature extraction, inevitably causing imprecise 3D object segments and degraded semantics.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 2) graph-wise, which merges segments across all frames [44, 48]. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Given the prior that an instance often appears in multiple consecutive frames, as shown in Fig. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** node, consists, correlated, semantics, captions, features, center, adaptive-octree, Hence, weighted, average, fuse, instance, optimal, feature, representative, distinctive, Fig, Then, dynamically.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For the path planning task, we employ the HM3DSem [46] dataset used in HOV-SG [44], where 8 scenes are selected for evaluation. | p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics) |
| Semantic / temporal fusion | Compared to the existing SoTA 3D scene graph, HOV-SG [44], we achieve +8.9% mIoU and +11.0% mAcc on the Replica dataset. | p. 6 (4.3. Quantitative Comparison), p. 8 (4.5. Qualitative Analysis) |
| Robot query / planning handoff | Table 4. Path planning results on HM3DSem. SR denotes success rate (%). s is the threshold within which the distance between the ... | p. 6 (Figure/Table caption), p. 7 (4.4. Ablation Studies) |

## Failure and Ablation Link

- **p. 5 / 4. Experiment - extractive PDF cue:** We compare our method with different SOTA methods in these tasks, and conduct comprehensive ablation studies to investigate several key components, demonstrating the effectiveness of ...
- **p. 7 / 4.4. Ablation Studies - extractive PDF cue:** Effect of Instance Feature Aggregation.
- **p. 6 / 4.3. Quantitative Comparison - extractive PDF cue:** When using supervised 3D models for proposal generation, our method significantly outperforms OpenMask3D [40] and the Open3DIS [29] variant with only the 3D proposals, validating ...
- **p. 7 / 4.3. Quantitative Comparison - extractive PDF cue:** Ablation study on path planning efficiency.
- **p. 8 / 4.5. Qualitative Analysis - extractive PDF cue:** 8 demonstrates the segment merging results of our CGSM and its baseline (i.e., frame-wise sequential merging), where CGSM correctly resolves the over-segmented long table without ...
- **p. 7 / 4.4. Ablation Studies - extractive PDF cue:** We also analyze the impact of hyper-parameter I, and the results in Rows 3-5 show that our method exhibits robustness to I ranging from 100 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.5. Octree-Graph Construction and Applications), p. 4 (3.4. Instance Feature Aggregation), p. 3 (3.1. Framework Overview), p. 3 (3.2. Segment Proposal and Comprehension), p. 5 (3.5. Octree-Graph Construction and Applications), objective 본문 anchor 없음, temporal p. 3 (3.3. Chronological Group-wise Segment Merging), p. 3 (3.3. Chronological Group-wise Segment Merging), p. 4 (3.3. Chronological Group-wise Segment Merging), p. 4 (3.3. Chronological Group-wise Segment Merging), p. 5 (4.2. Dataset and Evaluation Metrics), p. 7 (4.4. Ablation Studies).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
