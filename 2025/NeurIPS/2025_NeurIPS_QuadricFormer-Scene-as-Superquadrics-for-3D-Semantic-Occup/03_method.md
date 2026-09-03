# Method - QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eZNdkwJYbN; PDF retrieval source: https://arxiv.org/pdf/2506.10977. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (6 Superquadrics), p. 6 (6 Superquadrics), p. 6 (6 Superquadrics), p. 1 (Abstract), p. 1 (12800 Gaussians), p. 2 (1 Introduction)): Superquadrics Image Input Image Features 3D Occupancy Refined Superquadrics Figure 3: Overall Framework of QuadricFormer.We use several quadric-encoder blocks to update superquadrics, and employ a pruning-and-splitting module to further ...

## Method Body Digest

- **p. 5 / 6 Superquadrics - extractive body cue:** Superquadrics Image Input Image Features 3D Occupancy Refined Superquadrics Figure 3: Overall Framework of QuadricFormer.We use several quadric-encoder blocks to update superquadrics, and employ a ...
- **p. 6 / 6 Superquadrics - extractive body cue:** (11) We then use 3D sparse convolution Econv for superquadric feature self-encoding and deformable attention Eattn for interaction between superquadric and image features: FQ = ...
- **p. 6 / 6 Superquadrics - extractive body cue:** To address this, we introduce a pruning-splitting module after initial training.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent ...
- **p. 1 / 12800 Gaussians - extractive body cue:** 20.02 mIoU 1600 Superquadrics 20.12 mIoU GaussianFormer QuadricFormer Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose an efficient and expressive object-centric 3D representation using superquadrics [1] as scene primitives.
- **p. 2 / 1 Introduction - extractive body cue:** Building on this representation, we introduce QuadricFormer, a superquadric-based framework for efficient 3D semantic occupancy prediction.
- **p. 6 / 6 Superquadrics - extractive body cue:** (14) For optimization, we adopt the cross entropy loss and the lovaszsoftmax [2] loss for training.

## Design Rationale

- **p. 3 / 6 Superquadrics - extractive body cue:** 3 Proposed Approach In this section, we present our method based on the superquadric representation for efficient 3D semantic occupancy prediction.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose an efficient and expressive object-centric 3D representation using superquadrics [1] as scene primitives.
- **p. 2 / 1 Introduction - extractive body cue:** Building on this representation, we introduce QuadricFormer, a superquadric-based framework for efficient 3D semantic occupancy prediction.

## Source Evidence Cues

- **p. 5 / 6 Superquadrics - extractive body cue:** Superquadrics Image Input Image Features 3D Occupancy Refined Superquadrics Figure 3: Overall Framework of QuadricFormer.We use several quadric-encoder blocks to update superquadrics, and employ a ...
- **p. 6 / 6 Superquadrics - extractive body cue:** (11) We then use 3D sparse convolution Econv for superquadric feature self-encoding and deformable attention Eattn for interaction between superquadric and image features: FQ = ...
- **p. 6 / 6 Superquadrics - extractive body cue:** To address this, we introduce a pruning-splitting module after initial training.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent ...
- **p. 1 / 12800 Gaussians - extractive body cue:** 20.02 mIoU 1600 Superquadrics 20.12 mIoU GaussianFormer QuadricFormer Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose an efficient and expressive object-centric 3D representation using superquadrics [1] as scene primitives.
- **p. 2 / 1 Introduction - extractive body cue:** Building on this representation, we introduce QuadricFormer, a superquadric-based framework for efficient 3D semantic occupancy prediction.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Superquadrics Image Input Image Features 3D Occupancy Refined Superquadrics Figure 3: Overall Framework of QuadricFormer.We use several quadric-encoder blocks to update superquadrics, ... | p. 5 (6 Superquadrics), p. 6 (6 Superquadrics) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (11) We then use 3D sparse convolution Econv for superquadric feature self-encoding and deformable attention Eattn for interaction between superquadric and image ... | p. 6 (6 Superquadrics), p. 6 (6 Superquadrics) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To address this, we introduce a pruning-splitting module after initial training. | p. 6 (6 Superquadrics), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 6 Superquadrics - extractive body cue:** (14) For optimization, we adopt the cross entropy loss and the lovaszsoftmax [2] loss for training.
- **p. 5 / 6 Superquadrics - extractive body cue:** While point cloud reconstruction directly optimizes the distance between points and the superquadric surfaces, occupancy prediction requires fine-grained scene understanding, which lacks clear surface-based constraints.
- **p. 2 / 1 Introduction - extractive body cue:** Vision-centric autonomous driving systems have gained much attention for their cost-effectiveness over LiDAR-based solutions [4, 14, 42, 21, 19].
- **p. 2 / 1 Introduction - extractive body cue:** While voxel-based methods [19, 36] use dense 3D grids to capture fine details, they ignore the sparsity of driving scenes and suffer from high computational ...
- **p. 3 / 6 Superquadrics - extractive body cue:** While efficient, non-empty regions may be falsely pruned, leading to irreversible loss of critical geometry.
- **p. 1 / Abstract - extractive body cue:** We develop a probabilistic superquadric mixture model, which interprets each superquadric as an occupancy probability distribution with a corresponding geometry prior, and calculates semantics through ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (6 Superquadrics), p. 5 (6 Superquadrics), p. 6 (6 Superquadrics), p. 5 (6 Superquadrics), p. 6 (6 Superquadrics).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Furthermore, surface-based, methods, rely, explicit, structure, point, cloud, inputs, whereas, visual, introduce, structural, uncertainty | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Furthermore, surface-based, methods, rely, explicit, structure, point, cloud, inputs, whereas | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | section, present, superquadric, representation, efficient, semantic, occupancy, prediction, expressive, object-centric | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | optimization, adopt, cross, entropy, loss, lovaszsoftmax, training, While, point, cloud | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 6 Superquadrics - extractive body cue:** Furthermore, surface-based methods rely on the explicit structure from point cloud inputs, whereas visual inputs introduce structural uncertainty, making deterministic modeling unstable.
- **p. 3 / 6 Superquadrics - extractive body cue:** Differently, we present the first superquadric-based framework for holistic scene reconstruction directly from multi-view images, delivering state-of-the-art performance with superior efficiency.
- **p. 4 / 6 Superquadrics - extractive body cue:** Formally, given input images I = {Ii}N i=1 from N views, the model aims to predict voxel-level semantic labels O ∈CX×Y ×Z of the 3D ...
- **p. 5 / 6 Superquadrics - extractive body cue:** Superquadrics Image Input Image Features 3D Occupancy Refined Superquadrics Figure 3: Overall Framework of QuadricFormer.We use several quadric-encoder blocks to update superquadrics, and employ a ...
- **p. 6 / 6 Superquadrics - extractive body cue:** (11) We then use 3D sparse convolution Econv for superquadric feature self-encoding and deformable attention Eattn for interaction between superquadric and image features: FQ = ...
- **p. 6 / 6 Superquadrics - extractive body cue:** Starting from the image inputs of N views I = {Ii}N i=1, we first employ an image backbone EI to extract multi-scale image features FI: ...
- **p. 1 / 12800 Gaussians - extractive body cue:** Our QuadricFormer achieves state-of-the-art performance with superior efficiency for 3D occupancy prediction.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Each sequence spans a duration of 20 seconds with RGB images captured by 6 surrounding cameras, and the key frames are annotated ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In terms of efficiency, QuadricFormer significantly reduces both latency and memory usage. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In terms of efficiency, QuadricFormer significantly reduces both latency and memory usage. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Each sequence spans a duration of 20 seconds with RGB images captured by 6 surrounding cameras, and the key frames are annotated ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 6 Superquadrics - extractive body cue:** To address this, we introduce a pruning-splitting module after initial training.
- **p. 8 / 4 Experiments - extractive body cue:** For optimization, we train our model using AdamW with weight decay of 0.01, and maximum learning rate of 4 × 10-4, which decays with a ...
- **p. 7 / 6 Superquadrics - extractive body cue:** The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during inference, in accordance with Gaussian-based methods [15, 12].
- **p. 8 / 4 Experiments - extractive body cue:** We train our model for 20 epochs on nuScenes with a batch of 8.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Superquadrics, Image, Input, Features, Occupancy, Refined, Figure, Overall, Framework, QuadricFormer, several, quadric-encoder, blocks, update, employ, pruning-and-splitting, module, further, enhance, modeling.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The dataset is officially split into 700 sequences for training, 150 for validation, and 150 for testing. | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Semantic / temporal fusion | Compared to other methods, our approach achieves state-of-the-art performance. | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Robot query / planning handoff | The results demonstrate that increasing the crop & split number consistently improves performance. | p. 9 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive body cue:** 4.4 Ablation Study Effect of the ϵ range.
- **p. 9 / 4 Experiments - extractive body cue:** We conduct ablation studies on the effect of the pruningsplitting module, as shown in Table 4.
- **p. 8 / 4 Experiments - extractive body cue:** The table explores the effect of different ϵ ranges on 3D semantic occupancy prediction performance.
- **p. 9 / 4 Experiments - extractive body cue:** Effect of the pruning-splitting module.
- **p. 9 / 5 Conclusion - extractive body cue:** With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing representation efficiency.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (6 Superquadrics), p. 6 (6 Superquadrics), p. 6 (6 Superquadrics), p. 1 (Abstract), p. 1 (12800 Gaussians), p. 2 (1 Introduction), objective p. 6 (6 Superquadrics), p. 5 (6 Superquadrics), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (6 Superquadrics), p. 1 (Abstract), temporal p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 2 (1 Introduction), p. 3 (6 Superquadrics).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
