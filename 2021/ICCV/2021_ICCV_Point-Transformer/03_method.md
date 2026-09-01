# Method - Point Transformer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2012.09164; PDF retrieval source: https://arxiv.org/pdf/2012.09164. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture), p. 5 (3.5. Network Architecture), p. 4 (3.5. Network Architecture), p. 6 (4.2. Shape Classification), p. 4 (3.5. Network Architecture)): It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.

## Method Body Digest

- **p. 6 / 4.3. Object Part Segmentation - extractive PDF cue:** It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.
- **p. 5 / 3.5. Network Architecture - extractive PDF cue:** The feature encoder in point transformer networks for semantic segmentation and classification has five stages that operate on progressively downsampled point sets.
- **p. 5 / 3.5. Network Architecture - extractive PDF cue:** To pool feature vectors from P1 onto P2, we use a kNN graph on P1.
- **p. 4 / 3.5. Network Architecture - extractive PDF cue:** Note that the point transformer is the primary feature aggregation operator throughout the network.
- **p. 6 / 4.2. Shape Classification - extractive PDF cue:** To probe the representation learned by the Point Transformer, we conduct shape retrieval by retrieving nearest neighbors in the space of the output features produced ...
- **p. 4 / 3.5. Network Architecture - extractive PDF cue:** The network architectures are visualized in Figure 3.
- **p. 7 / Method - extractive PDF cue:** Pos. encoding mIoU mAcc OA none 64.6 71.9 88.2 absolute 66.5 73.2 88.9 relative 70.4 76.5 90.8 relative for attention 67.0 73.0 89.3 relative for ...
- **p. 6 / 4.3. Object Part Segmentation - extractive PDF cue:** (Note that we did not use loss-balancing during training, which can boost category mIoU.)

## Design Rationale

- **p. 6 / 4.3. Object Part Segmentation - extractive PDF cue:** It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.
- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our main contributions include the following. • We design a highly expressive Point Transformer layer for point cloud processing.
- **p. 1 / 1. Introduction - extractive PDF cue:** We show that Point Transformers are remarkably effective in 3D deep learning tasks, both at the level of detailed object analysis and large-scale parsing of ...

## Source Evidence Cues

- **p. 6 / 4.3. Object Part Segmentation - extractive PDF cue:** It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.
- **p. 5 / 3.5. Network Architecture - extractive PDF cue:** The feature encoder in point transformer networks for semantic segmentation and classification has five stages that operate on progressively downsampled point sets.
- **p. 5 / 3.5. Network Architecture - extractive PDF cue:** To pool feature vectors from P1 onto P2, we use a kNN graph on P1.
- **p. 4 / 3.5. Network Architecture - extractive PDF cue:** Note that the point transformer is the primary feature aggregation operator throughout the network.
- **p. 6 / 4.2. Shape Classification - extractive PDF cue:** To probe the representation learned by the Point Transformer, we conduct shape retrieval by retrieving nearest neighbors in the space of the output features produced ...
- **p. 4 / 3.5. Network Architecture - extractive PDF cue:** The network architectures are visualized in Figure 3.
- **p. 7 / Method - extractive PDF cue:** Pos. encoding mIoU mAcc OA none 64.6 71.9 88.2 absolute 66.5 73.2 88.9 relative 70.4 76.5 90.8 relative for attention 67.0 73.0 89.3 relative for ...
- **Detected method headings:** 3.5. Network Architecture (p. 4); Method (p. 6); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing. | p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The feature encoder in point transformer networks for semantic segmentation and classification has five stages that operate on progressively downsampled point sets. | p. 5 (3.5. Network Architecture), p. 5 (3.5. Network Architecture) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To pool feature vectors from P1 onto P2, we use a kNN graph on P1. | p. 5 (3.5. Network Architecture), p. 4 (3.5. Network Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4.3. Object Part Segmentation - extractive PDF cue:** (Note that we did not use loss-balancing during training, which can boost category mIoU.)
- **p. 5 / 3.5. Network Architecture - extractive PDF cue:** The feature encoder in point transformer networks for semantic segmentation and classification has five stages that operate on progressively downsampled point sets.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Denote, point, provided, input, transition, down, module, output, mAcc, DShapeNets, voxel, VoxNet, Subvolume, MVCNN | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Denote, point, provided, input, transition, down, module, output, mAcc, DShapeNets | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | consists, models, shape, categories, training, testing, summary, main, contributions, include | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Note, loss-balancing, during, training, boost, category, mIoU, feature, encoder, point | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.5. Network Architecture - extractive PDF cue:** Denote the point set provided as input to the transition down module as P1 and denote the output point set as P2.
- **p. 6 / Method - extractive PDF cue:** Method input mAcc OA 3DShapeNets [47] voxel 77.3 84.7 VoxNet [23] voxel 83.0 85.9 Subvolume [26] voxel 86.0 89.2 MVCNN [34] image - 90.1 PointNet ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The transformer family of models is particularly appropriate for point cloud processing because the self-attention operator, which is at the core of transformer networks, is ...
- **p. 6 / 4.2. Shape Classification - extractive PDF cue:** The Point Transformer sets the new state of the art in both metrics.
- **p. 1 / 1. Introduction - extractive PDF cue:** The Point Transformer can serve as the backbone for various 3D point cloud understanding tasks such as object classification, object part segmentation, and semantic scene ...
- **p. 5 / 3.5. Network Architecture - extractive PDF cue:** Their primary function is to map features from the downsampled input point set P2 onto its superset P1 ⊃P2.
- **p. 2 / 1. Introduction - extractive PDF cue:** We conduct controlled studies to examine specific choices in the Point Transformer design and set the new state of the art on multiple highly competitive ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For semantic segmentation on S3DIS, we train for 40K iterations with initial learning rate 0.5, dropped by 10x at steps 24K and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The Point Transformer outperforms MLPs-based frameworks such as PointNet [25], voxelbased architectures such as SegCloud [36], graph-based methods such as SPGraph [15], ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | This induces massive computational and memory costs and underutilizes the sparsity of point sets in 3D. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For semantic segmentation on S3DIS, we train for 40K iterations with initial learning rate 0.5, dropped by 10x at steps 24K and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.3. Object Part Segmentation - extractive PDF cue:** It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.
- **p. 5 / 4. Experiments - extractive PDF cue:** For 3D shape classification on ModelNet40 and 3D object part segmentation on ShapeNetPart, we train for 200 epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** consists, models, shape, categories, training, testing, feature, encoder, point, transformer, networks, semantic, segmentation, classification, five, stages, operate, progressively, downsampled, sets.
- **Relevant PDF headings:** 3.5. Network Architecture (p. 4); Method (p. 6); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The S3DIS [1] dataset for semantic scene parsing consists of 271 rooms in six areas from three different buildings. | p. 5 (4.1. Semantic Segmentation), p. 5 (4. Experiments) |
| Semantic / temporal fusion | On Area 5, the Point Transformer attains mIoU/mAcc/OA of 70.4%/76.5%/90.8%, outperforming all prior work by multiple percentage points in each metric. | p. 5 (4.1. Semantic Segmentation), p. 5 (4.1. Semantic Segmentation) |
| Robot query / planning handoff | Point Transformer also substantially outperforms all prior models under 6-fold cross-validation. | p. 5 (4.1. Semantic Segmentation), p. 5 (4.1. Semantic Segmentation) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. The Point Transformer can serve as the backbone for var- ious 3D point cloud understanding tasks such as object classifica- tion, object part ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 6. Ablation study: position encoding. Operator mIoU mAcc OA MLP 61.7 68.6
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 7. Ablation study: form of self-attention operator. Visualization. Object part segmentation results on a num- ber of models are shown in Figure 7. The ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture), p. 5 (3.5. Network Architecture), p. 4 (3.5. Network Architecture), p. 6 (4.2. Shape Classification), p. 4 (3.5. Network Architecture), objective p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture), temporal p. 5 (4. Experiments), p. 5 (4.1. Semantic Segmentation), p. 6 (4.2. Shape Classification), p. 6 (Method), p. 7 (Method), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
