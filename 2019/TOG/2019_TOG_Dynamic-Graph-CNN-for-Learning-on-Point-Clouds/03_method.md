# Method - Dynamic Graph CNN for Learning on Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1801.07829; PDF retrieval source: https://arxiv.org/pdf/1801.07829. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered))): To this end, we propose a new neural network module dubbed EdgeConv suitable for CNN-based high-level tasks on point clouds including classification and segmentation.

## Method Body Digest

- **p. 1 / Body text (section not recovered) - extractive body cue:** To this end, we propose a new neural network module dubbed EdgeConv suitable for CNN-based high-level tasks on point clouds including classification and segmentation.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** One common approach to process point cloud data using deep learning models is to first convert raw point cloud data into a volumetric representation, namely ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2017]; these allow the network to exploit local features, improving upon performance of the basic model.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Bottom: schematic neural network architecture.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Point clouds provide a flexible geometric representation suitable for countless applications in computer graphics; they also comprise the raw output of most 3D data acquisition ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** State-of-the-art deep neural networks are designed specifically to handle the irregularity of point clouds, directly manipulating raw point cloud data rather than passing to an ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Point clouds, or scattered collections of points in 2D or 3D, are arguably the simplest shape representation; they also comprise the output of 3D sensing ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better capture ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these drawbacks, we propose a novel simple operation, called EdgeConv, which captures local geometric structure while maintaining permutation invariance.
- **p. 1 / Body text (section not recovered) - extractive body cue:** To this end, we propose a new neural network module dubbed EdgeConv suitable for CNN-based high-level tasks on point clouds including classification and segmentation.

## Source Evidence Cues

- **p. 1 / Body text (section not recovered) - extractive body cue:** To this end, we propose a new neural network module dubbed EdgeConv suitable for CNN-based high-level tasks on point clouds including classification and segmentation.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** One common approach to process point cloud data using deep learning models is to first convert raw point cloud data into a volumetric representation, namely ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2017]; these allow the network to exploit local features, improving upon performance of the basic model.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Bottom: schematic neural network architecture.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To this end, we propose a new neural network module dubbed EdgeConv suitable for CNN-based high-level tasks on point clouds including classification ... | p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | One common approach to process point cloud data using deep learning models is to first convert raw point cloud data into a ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 2017]; these allow the network to exploit local features, improving upon performance of the basic model. | p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Body text (section not recovered) - extractive body cue:** Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Point, clouds, provide, flexible, geometric, representation, suitable, countless, applications, computer, graphics, they, comprise, output | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Point, clouds, provide, flexible, geometric, representation, suitable, countless, applications, computer | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, contributions, follows, present, novel, operation, learning, point, clouds, EdgeConv | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Permission, make, digital, hard, copies, part, personal, classroom, granted, without | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Body text (section not recovered) - extractive body cue:** Point clouds provide a flexible geometric representation suitable for countless applications in computer graphics; they also comprise the raw output of most 3D data acquisition ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** State-of-the-art deep neural networks are designed specifically to handle the irregularity of point clouds, directly manipulating raw point cloud data rather than passing to an ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Point clouds, or scattered collections of points in 2D or 3D, are arguably the simplest shape representation; they also comprise the output of 3D sensing ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** While hand-designed features on point clouds have long been proposed in graphics and vision, however, the recent overwhelming success of convolutional neural networks (CNNs) for ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This approach, however, usually introduces quantization artifacts and excessive memory usage, making it difficult to go to capture high-resolution or fine-grained features. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | These features do not fit cleanly into the frameworks of computational or differential geometry and typically require learning-based approaches that derive relevant ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | This approach, however, usually introduces quantization artifacts and excessive memory usage, making it difficult to go to capture high-resolution or fine-grained features. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4 EVALUATION - extractive body cue:** A distributed training scheme is further implemented on two NVIDIA TITAN X GPUs to maintain the training batch size.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** neural, network, module, dubbed, EdgeConv, suitable, CNN-based, high-level, tasks, point, clouds, including, classification, segmentation, One, common, process, cloud, data, deep.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The dataset contains 16,881 3D shapes from 16 object categories, annotated with 50 parts in total. | p. 8 (4 EVALUATION), p. 8 (4 EVALUATION) |
| Semantic / temporal fusion | Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 ... | p. 7 (4 EVALUATION), p. 7 (4 EVALUATION) |
| Robot query / planning handoff | Our model achieves the best results on this dataset. | p. 7 (4 EVALUATION), p. 7 (4 EVALUATION) |

## Failure and Ablation Link

- **p. 7 / 4 EVALUATION - extractive body cue:** The network architecture used for the classification task is shown in Figure 3 (top branch without spatial transformer network).
- **p. 8 / 4 EVALUATION - extractive body cue:** Effectiveness of different components.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Left: Computing an edge feature, eij (top), from a point pair, xi and xj (bottom). In this example, hΘ() is instantiated using a ...
- **p. 8 / 4 EVALUATION - extractive body cue:** This confirms our hypothesis that for certain density, with large k the Euclidean distance fails to approximate geodesic distance, destroying the geometry of each patch.
- **p. 8 / 4 EVALUATION - extractive body cue:** We further evaluate the robustness of our model (trained on 1,024 points with k = 20) to point cloud density.
- **p. 9 / 4 EVALUATION - extractive body cue:** Our model is robust to partial data.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)), objective p. 1 (Body text (section not recovered)), temporal p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 RELATED WORK), p. 4 (2 RELATED WORK), p. 5 (2 RELATED WORK), p. 11 (5 DISCUSSION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
