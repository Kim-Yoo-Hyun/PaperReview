# Evaluation - MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (Figure/Table caption), p. 1 (1.1. Construction of Primitive-Mesh), p. 2 (2.2. Training Strategy Analysis), p. 1 (1.1. Construction of Primitive-Mesh)): Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed by the KNN-based Primitive-Mesh. Pre- training on large-scale ...

## Evaluation Body Digest

- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** We utilize 128 A800 GPUs and spent over three days constructing this dataset.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** We further employ the zero-shot 3D part segmentation method, SamPart3D [7], to construct the Semantic-based Primitive-Mesh dataset.
- **p. 2 / 2.2. Training Strategy Analysis - extractive body cue:** In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on specific ...
- **p. 1 / 2.1. Shape Novelty Analysis - extractive body cue:** We compute the Chamfer Distance between samples to identify the three most similar training meshes to the generated meshes for comparison.
- **p. 1 / 2.1. Shape Novelty Analysis - extractive body cue:** This demonstrates that our model possesses generalization ability and creativity rather than merely replicating training samples.
- **p. 2 / 2.1. Shape Novelty Analysis - extractive body cue:** (b) The Semantic-based method generates mesh parts at the semantic level and includes corresponding textual annotations, which better aid LLMs in accurately understanding and generating ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Shape novelty. We compute the Chamfer Distance be- tween the generated meshes and those in the training set, selecting the three closest matches. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed by the KNN-based ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 1. Additional Implementation Details (p. 1); 2. Additional Results (p. 1).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed by the ... | p. 3 (Figure/Table caption) |
| 1.1. Construction of Primitive-Mesh | SYSTEM / EVALUATION SCOPE UNRESOLVED | By integrating these segments with their corresponding textual labels, our proposed MeshLLM significantly enhances performance. | p. 1 (1.1. Construction of Primitive-Mesh) |
| 2.2. Training Strategy Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | As shown in Table 1, training on semantic Primitive-Mesh samples later yields better results. | p. 2 (2.2. Training Strategy Analysis) |
| 1.1. Construction of Primitive-Mesh | SYSTEM / EVALUATION SCOPE UNRESOLVED | This strategy is highly efficient, requiring only 0.2 seconds to segment a 3D mesh, enabling the rapid generation of large-scale results. | p. 1 (1.1. Construction of Primitive-Mesh) |

## Dataset / Benchmark Role

- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** We utilize 128 A800 GPUs and spent over three days constructing this dataset.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** We further employ the zero-shot 3D part segmentation method, SamPart3D [7], to construct the Semantic-based Primitive-Mesh dataset.
- **p. 2 / 2.2. Training Strategy Analysis - extractive body cue:** In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on specific ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Examples of the constructed Primitive-Mesh. (a) The KNN-based method is simple and efficient, enabling the rapid con- struction of large-scale trainable mesh parts ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Shape novelty. We compute the Chamfer Distance be- tween the generated meshes and those in the training set, selecting the three closest matches. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed by the KNN-based ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Failure case. The limited semantic dataset size reduces text-geometry alignment for more fine-grained generations.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We utilize 128 A800 GPUs and spent over three days constructing this dataset. | embodiment, simulator version and control stack | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |
| Task/environment | We further employ the zero-shot 3D part segmentation method, SamPart3D [7], to construct the Semantic-based Primitive-Mesh dataset. | reset, timeout, object/scene variation | p. 1 (1.1. Construction of Primitive-Mesh), p. 2 (2.2. Training Strategy Analysis) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We compute the Chamfer Distance between samples to identify the three most similar training meshes to the generated meshes for comparison. | definition/direction/unit from same section | p. 1 (2.1. Shape Novelty Analysis) |
| This demonstrates that our model possesses generalization ability and creativity rather than merely replicating training samples. | definition/direction/unit from same section | p. 1 (2.1. Shape Novelty Analysis) |
| (b) The Semantic-based method generates mesh parts at the semantic level and includes corresponding textual annotations, which better aid LLMs in accurately understanding and ... | definition/direction/unit from same section | p. 2 (2.1. Shape Novelty Analysis) |
| In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on ... | definition/direction/unit from same section | p. 2 (2.2. Training Strategy Analysis) |
| Figure 2. Shape novelty. We compute the Chamfer Distance be- tween the generated meshes and those in the training set, selecting the three closest ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed by the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| And NX in the 1-NNA metric is a point cloud that is closest to X in both the generated and reference dataset, i.e., NX ... | comparison identity and matched condition | p. 1 (1.2. Metric Details) |
| We compute the Chamfer Distance between samples to identify the three most similar training meshes to the generated meshes for comparison. | comparison identity and matched condition | p. 1 (2.1. Shape Novelty Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed by the ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features. | component/input/data sensitivity | p. 1 (1.1. Construction of Primitive-Mesh) |
| To obtain semantic labels for each part, we render multiview images and annotate the corresponding 2D regions for each segmented 3D component. | component/input/data sensitivity | p. 1 (1.1. Construction of Primitive-Mesh) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on ... | Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed by the ... | PDF body cue; verify exact table/figure and matched conditions | p. 3 (Figure/Table caption), p. 1 (1.1. Construction of Primitive-Mesh), p. 2 (2.2. Training Strategy Analysis), p. 1 (1.1. Construction of Primitive-Mesh) |
| Primary metric/result | By integrating these segments with their corresponding textual labels, our proposed MeshLLM significantly enhances performance. | numeric claim only at cited anchor | p. 1 (1.1. Construction of Primitive-Mesh) |

- Numeric sentences retained from the body:
- **p. 1 / 1.2. Metric Details - extractive body cue:** And NX in the 1-NNA metric is a point cloud that is closest to X in both the generated and reference dataset, i.e., NX = ...
- **p. 1 / 1.2. Metric Details - extractive body cue:** And NX in the 1-NNA metric is a point cloud that is closest to X in both the generated and reference dataset, i.e., NX = ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Failure case. The limited semantic dataset size reduces text-geometry alignment for more fine-grained generations. | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We compute the Chamfer Distance between samples to identify the three most similar training meshes to the generated meshes for comparison. | p. 1 (2.1. Shape Novelty Analysis) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Failure case. The limited semantic dataset size reduces text-geometry alignment for more fine-grained generations.

- **Evidence anchors reviewed:** datasets p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh), p. 2 (2.2. Training Strategy Analysis), metrics p. 1 (2.1. Shape Novelty Analysis), p. 1 (2.1. Shape Novelty Analysis), p. 2 (2.1. Shape Novelty Analysis), p. 2 (2.2. Training Strategy Analysis), p. 3 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 1 (1.2. Metric Details), p. 1 (2.1. Shape Novelty Analysis), results p. 3 (Figure/Table caption), p. 1 (1.1. Construction of Primitive-Mesh), p. 2 (2.2. Training Strategy Analysis), p. 1 (1.1. Construction of Primitive-Mesh).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
