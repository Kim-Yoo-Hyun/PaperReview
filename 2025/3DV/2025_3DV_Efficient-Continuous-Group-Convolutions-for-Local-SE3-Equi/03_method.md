# Method - Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=c6RR0bqNVI&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 5 (3.2. Efficient group convolution), p. 5 (3.2. Efficient group convolution), p. 4 (3.2. Efficient group convolution)): equivariance, the feature maps need to be lifted to the group itself Y = G since then the stabilizer subgroup only consists of the trivial element H = {e}, and ...

## Method Body Digest

- **p. 4 / 3.1. Group equivariant convolution - extractive PDF cue:** equivariance, the feature maps need to be lifted to the group itself Y = G since then the stabilizer subgroup only consists of the trivial ...
- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** A more formal definition of a convolution layer is then given as a learnable kernel operator Φ : X →Y that transforms feature maps f ...
- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** We say that an operator Φ is equivariant to a specific Group G if it commutes with group representations on the input and output feature ...
- **p. 5 / 3.2. Efficient group convolution - extractive PDF cue:** (7) during training by only sampling a subset of the elements of F(x) for input and output domains of the feature maps.
- **p. 5 / 3.2. Efficient group convolution - extractive PDF cue:** Although F(x) only has 4 elements, this might still be restrictive for modern state-ofthe-art deep architectures used to process large 3D scenes.
- **p. 4 / 3.2. Efficient group convolution - extractive PDF cue:** However, sampling O rotations per point increases the model's memory by a factor of O.
- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** One solution is to use ∥x -y∥as input to the kernel at the cost of losing the capacity to capture directional features.
- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** Further, considering Y = G/H as quotient space with H = {g ∈G/gy0 = y0} as the stabilizer subgroup StabG(y0), which consists of group elements ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose using a finite subset F(x) ⊂ SE(3), referred to as a frame, to solve the group equivariant integral, which allows ...
- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** Further, considering Y = G/H as quotient space with H = {g ∈G/gy0 = y0} as the stabilizer subgroup StabG(y0), which consists of group elements ...
- **p. 4 / 3.2. Efficient group convolution - extractive PDF cue:** To achieve exact equivariance with tractable computational load, we propose a carefully constructed grid F(xj) ⊂SE(3) specific to each point xj ∈R3.

## Source Evidence Cues

- **p. 4 / 3.1. Group equivariant convolution - extractive PDF cue:** equivariance, the feature maps need to be lifted to the group itself Y = G since then the stabilizer subgroup only consists of the trivial ...
- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** A more formal definition of a convolution layer is then given as a learnable kernel operator Φ : X →Y that transforms feature maps f ...
- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** We say that an operator Φ is equivariant to a specific Group G if it commutes with group representations on the input and output feature ...
- **p. 5 / 3.2. Efficient group convolution - extractive PDF cue:** (7) during training by only sampling a subset of the elements of F(x) for input and output domains of the feature maps.
- **p. 5 / 3.2. Efficient group convolution - extractive PDF cue:** Although F(x) only has 4 elements, this might still be restrictive for modern state-ofthe-art deep architectures used to process large 3D scenes.
- **p. 4 / 3.2. Efficient group convolution - extractive PDF cue:** However, sampling O rotations per point increases the model's memory by a factor of O.
- **Detected method headings:** 3. Methods (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | equivariance, the feature maps need to be lifted to the group itself Y = G since then the stabilizer subgroup only consists ... | p. 4 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | A more formal definition of a convolution layer is then given as a learnable kernel operator Φ : X →Y that transforms ... | p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We say that an operator Φ is equivariant to a specific Group G if it commutes with group representations on the input ... | p. 3 (3.1. Group equivariant convolution), p. 5 (3.2. Efficient group convolution) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** One solution is to use ∥x -y∥as input to the kernel at the cost of losing the capacity to capture directional features.
- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** Further, considering Y = G/H as quotient space with H = {g ∈G/gy0 = y0} as the stabilizer subgroup StabG(y0), which consists of group elements ...
- **p. 4 / 3.2. Efficient group convolution - extractive PDF cue:** Previous works such as [9, 48] have relied on the discretization of SO(3) using platonic solids that assign to each spatial component the same finite ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Group equivariant convolution), p. 4 (3.2. Efficient group convolution).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Note, definition, given, cross-correlation, instead, convolution, since, aligns, better, template-matching, well, known, layers, translation | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Note, definition, given, cross-correlation, instead, convolution, since, aligns, better, template-matching | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | finite, subset, referred, frame, solve, group, equivariant, integral, allows, exact | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | One, solution, input, kernel, cost, losing, capacity, capture, directional, features | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** (Note that the definition given is cross-correlation instead of convolution since this aligns better with template-matching.) It is well known that convolution layers are translation ...
- **p. 3 / 3.1. Group equivariant convolution - extractive PDF cue:** We say that an operator Φ is equivariant to a specific Group G if it commutes with group representations on the input and output feature ...
- **p. 5 / 3.2. Efficient group convolution - extractive PDF cue:** (7) during training by only sampling a subset of the elements of F(x) for input and output domains of the feature maps.
- **p. 1 / 1. Introduction - extractive PDF cue:** Equivariance is the property of an operator that allows the prediction of the transformation of the output given an input transformation, while group-invariant operators produce ...
- **p. 5 / 3.2. Efficient group convolution - extractive PDF cue:** Then, the input to the group convolution kernel is the relative position plus the relative orientations between points.
- **p. 4 / 3.2. Efficient group convolution - extractive PDF cue:** Note that the point cloud is treated as a sparse feature map that defines the sampling of the spatial component.
- **p. 1 / 1. Introduction - extractive PDF cue:** Baking SE(3)- equivariance into the network architecture can thus be beneficial since equivariant features maintain information about the input group transform across neural layers, making ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We can see that using only one sample to approximate the integral over SO(3) has approximately similar memory consumption and frames per ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We sample only one orientation from the frame for all experiments, which does not pose additional memory or computational burden on the ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | We can see that using only one sample to approximate the integral over SO(3) has approximately similar memory consumption and frames per ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Analyzing the effect of different samples used to compute the integral over SO(3) for training and testing, we can see that Ours, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Group equivariant convolution - extractive PDF cue:** equivariance, the feature maps need to be lifted to the group itself Y = G since then the stabilizer subgroup only consists of the trivial ...
- **p. 5 / 3.2. Efficient group convolution - extractive PDF cue:** (7) during training by only sampling a subset of the elements of F(x) for input and output domains of the feature maps.
- **p. 5 / 4. Experiments - extractive PDF cue:** Due to space constraints, additional experiments, ablation studies, detailed dataset description and implementation are provided in the supplementary materials.
- **p. 6 / 4.2. Shape classification - extractive PDF cue:** Analyzing the effect of different samples used to compute the integral over SO(3) for training and testing, we can see that Ours, even with 1 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** equivariance, feature, maps, need, lifted, group, itself, since, then, stabilizer, subgroup, only, consists, trivial, element, kernel, longer, constrained, more, formal.
- **Relevant PDF headings:** 3. Methods (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We test our method on ScanNet [14], a dataset composed of several indoor 3D scene scans, to show its applicability to real-world ... | p. 7 (4.3. Semantic segmentation), p. 5 (4.2. Shape classification) |
| Semantic / temporal fusion | When comparing to current state-of-the-art local equivariant methods, we can see that while they also outperform global equivariant methods by a large ... | p. 7 (4.3. Semantic segmentation), p. 5 (4.2. Shape classification) |
| Robot query / planning handoff | When we look at the SO(3) / SO(3) setup, all three methods achieve good performance; MC and Ours are able to outperform ... | p. 6 (4.2. Shape classification), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 4.3. Semantic segmentation - extractive PDF cue:** This shows that with our method, we can introduce the equivariant property without extra costs, demonstrating the efficiency of our proposed model.
- **p. 6 / 4.2. Shape classification - extractive PDF cue:** Analyzing the effect of different samples used to compute the integral over SO(3) for training and testing, we can see that Ours, even with 1 ...
- **p. 5 / 4.2. Shape classification - extractive PDF cue:** All models are evaluated when trained and tested without any rotation, I / I.
- **p. 5 / 4.2. Shape classification - extractive PDF cue:** For this task, predictions must be invariant of the rotation applied to the model.
- **p. 6 / 4.3. Semantic segmentation - extractive PDF cue:** The same is true for our non-equivariant version, STD.
- **p. 7 / 4.3. Semantic segmentation - extractive PDF cue:** Global equivariant methods such as VN, or FA struggle with out-of-distribution models.
- **p. 8 / 4.3. Semantic segmentation - extractive PDF cue:** Comparison to equivariant models on the classification task of ModelNet40 for different setups.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 5 (3.2. Efficient group convolution), p. 5 (3.2. Efficient group convolution), p. 4 (3.2. Efficient group convolution), objective p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 4 (3.2. Efficient group convolution), temporal p. 7 (4.3. Semantic segmentation), p. 7 (4.3. Semantic segmentation), p. 4 (3.2. Efficient group convolution), p. 4 (3.2. Efficient group convolution), p. 5 (3.2. Efficient group convolution), p. 5 (3.2. Efficient group convolution).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
