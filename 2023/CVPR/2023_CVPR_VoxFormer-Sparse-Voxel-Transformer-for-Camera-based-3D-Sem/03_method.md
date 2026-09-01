# Method - VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2302.12251; PDF retrieval source: https://arxiv.org/pdf/2302.12251. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Preliminary), p. 5 (3.3. Predefined Parameters), p. 5 (3.3. Predefined Parameters), p. 3 (3.2. Overall Architecture), p. 4 (3.3. Predefined Parameters), p. 4 (3.3. Predefined Parameters)): Motivated by reconstruction-beforehallucination and sparsity-in-3D-space, we build a twostage framework: stage-1 based on CNN proposes a sparse set of voxel queries from image depth to attend to images since the ...

## Method Body Digest

- **p. 3 / 3.1. Preliminary - extractive PDF cue:** Motivated by reconstruction-beforehallucination and sparsity-in-3D-space, we build a twostage framework: stage-1 based on CNN proposes a sparse set of voxel queries from image depth to ...
- **p. 5 / 3.3. Predefined Parameters - extractive PDF cue:** Then we use deformable self-attention to get the refined voxel features ˆF3D ∈R×h×w×z×d: DSA(F3D, F3D) = DA(f, p, F3D), (5) where f could be either ...
- **p. 5 / 3.3. Predefined Parameters - extractive PDF cue:** Finally, we perform a weighted sum of the sampled features as the output of deformable cross-attention (DCA): DCA(qp, F2D) = 1 /Vt/ X t∈Vt DA(qp, ...
- **p. 3 / 3.2. Overall Architecture - extractive PDF cue:** 2: our architecture extracts 2D features from RGB images and then uses a sparse set of 3D voxel queries to index into these 2D features, ...
- **p. 4 / 3.3. Predefined Parameters - extractive PDF cue:** Given a 2D RGB observation, we first obtain a 2.5D representation of the scene based on depth estimation.
- **p. 4 / 3.3. Predefined Parameters - extractive PDF cue:** Then we can predict the occupancy by Mout = Θocc(Min), where Mout ∈{0, 1}h×w×z has a lower resolution than the input Min ∈{0, 1}H×W ×Z ...
- **p. 5 / 3.6. Training Loss - extractive PDF cue:** We train stage-2 with a weighted cross-entropy loss.
- **p. 5 / 3.6. Training Loss - extractive PDF cue:** For stage-1, we employ a binary cross-entropy loss for occupancy prediction at a lower spatial resolution.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions in this work can be summarized as follows: • A novel two-stage framework that lifts images into a complete 3D voxelized semantic scene. ...
- **p. 2 / 1. Introduction - extractive PDF cue:** VoxFormer consists of class-agnostic query proposal (stage-1) and class-specific semantic segmentation (stage2), where stage-1 proposes a sparse set of occupied voxels, and stage-2 completes the ...
- **p. 3 / 3.2. Overall Architecture - extractive PDF cue:** Our framework is a two-stage cascade composed of class-agnostic proposals and class-specific segmentation similar to [68]: stage-1 generates class-agnostic query proposals, and stage-2 uses an ...

## Source Evidence Cues

- **p. 3 / 3.1. Preliminary - extractive PDF cue:** Motivated by reconstruction-beforehallucination and sparsity-in-3D-space, we build a twostage framework: stage-1 based on CNN proposes a sparse set of voxel queries from image depth to ...
- **p. 5 / 3.3. Predefined Parameters - extractive PDF cue:** Then we use deformable self-attention to get the refined voxel features ˆF3D ∈R×h×w×z×d: DSA(F3D, F3D) = DA(f, p, F3D), (5) where f could be either ...
- **p. 5 / 3.3. Predefined Parameters - extractive PDF cue:** Finally, we perform a weighted sum of the sampled features as the output of deformable cross-attention (DCA): DCA(qp, F2D) = 1 /Vt/ X t∈Vt DA(qp, ...
- **p. 3 / 3.2. Overall Architecture - extractive PDF cue:** 2: our architecture extracts 2D features from RGB images and then uses a sparse set of 3D voxel queries to index into these 2D features, ...
- **p. 4 / 3.3. Predefined Parameters - extractive PDF cue:** Given a 2D RGB observation, we first obtain a 2.5D representation of the scene based on depth estimation.
- **p. 4 / 3.3. Predefined Parameters - extractive PDF cue:** Then we can predict the occupancy by Mout = Θocc(Min), where Mout ∈{0, 1}h×w×z has a lower resolution than the input Min ∈{0, 1}H×W ×Z ...
- **Detected method headings:** 3. Methodology (p. 3); 3.2. Overall Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Motivated by reconstruction-beforehallucination and sparsity-in-3D-space, we build a twostage framework: stage-1 based on CNN proposes a sparse set of voxel queries from ... | p. 3 (3.1. Preliminary), p. 5 (3.3. Predefined Parameters) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Then we use deformable self-attention to get the refined voxel features ˆF3D ∈R×h×w×z×d: DSA(F3D, F3D) = DA(f, p, F3D), (5) where f ... | p. 5 (3.3. Predefined Parameters), p. 5 (3.3. Predefined Parameters) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Finally, we perform a weighted sum of the sampled features as the output of deformable cross-attention (DCA): DCA(qp, F2D) = 1 /Vt/ ... | p. 5 (3.3. Predefined Parameters), p. 3 (3.2. Overall Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.6. Training Loss - extractive PDF cue:** We train stage-2 with a weighted cross-entropy loss.
- **p. 5 / 3.6. Training Loss - extractive PDF cue:** For stage-1, we employ a binary cross-entropy loss for occupancy prediction at a lower spatial resolution.
- **p. 3 / 3.1. Preliminary - extractive PDF cue:** In summary, the overall objective is to learn a neural network Θ to generate a semantic voxel Yt = Θ(It) as close to the ground ...
- **p. 3 / 3.2. Overall Architecture - extractive PDF cue:** A more specific procedure is as follows: • Extract 2D features F2D t ∈Rb×c×d from RGB image It using ResNet-50 backbone [61], where b × ...
- **p. 4 / 3.3. Predefined Parameters - extractive PDF cue:** Depthbased Query Proposal Feature Extractor Depth Prediction Voxel Queries 𝑸 𝑤 ℎ 𝑧 Voxel Features 𝑭𝒕𝟑𝑫 … Query Proposals 𝑸𝒑 Image 𝐼%, 𝐼%&', … Image ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.3. Predefined Parameters), p. 3 (3.1. Preliminary), p. 5 (3.6. Training Loss), p. 3 (3.2. Overall Architecture), p. 4 (3.3. Predefined Parameters), p. 4 (3.3. Predefined Parameters).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | More, specifically, input, current, previous, images, denoted, It-1, output, voxel, grid, defined, coordinate, egovehicle | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | More, specifically, input, current, previous, images, denoted, It-1, output, voxel | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, novel, two-stage, framework, lifts, images, complete, voxelized | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | train, stage-2, weighted, cross-entropy, loss, stage-1, employ, binary, occupancy, prediction | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Preliminary - extractive PDF cue:** More specifically, we use as input current and previous images denoted by It = {It, It-1, ...}, and use as output a voxel grid Yt ...
- **p. 3 / 3.1. Preliminary - extractive PDF cue:** Motivated by reconstruction-beforehallucination and sparsity-in-3D-space, we build a twostage framework: stage-1 based on CNN proposes a sparse set of voxel queries from image depth to ...
- **p. 4 / 3.3. Predefined Parameters - extractive PDF cue:** Depthbased Query Proposal Feature Extractor Depth Prediction Voxel Queries 𝑸 𝑤 ℎ 𝑧 Voxel Features 𝑭𝒕𝟑𝑫 … Query Proposals 𝑸𝒑 Image 𝐼%, 𝐼%&', … Image ...
- **p. 2 / 1. Introduction - extractive PDF cue:** It first strengthens the featurization of the proposed voxels by allowing them to attend to the image observations.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions in this work can be summarized as follows: • A novel two-stage framework that lifts images into a complete 3D voxelized semantic scene. ...
- **p. 4 / 3.3. Predefined Parameters - extractive PDF cue:** Note that our framework supports the input of single or multiple images. computations.
- **p. 5 / 3.3. Predefined Parameters - extractive PDF cue:** Finally, we perform a weighted sum of the sampled features as the output of deformable cross-attention (DCA): DCA(qp, F2D) = 1 /Vt/ X t∈Vt DA(qp, ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Our framework is a two-stage cascade composed of class-agnostic proposals and class-specific segmentation similar to [68]: stage-1 generates class-agnostic query proposals, and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Motivated by reconstruction-beforehallucination and sparsity-in-3D-space, we build a twostage framework: stage-1 based on CNN proposes a sparse set of voxel queries from ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We train stage-1 and stage-2 separately with 24 epochs, a learning rate of 2×10-4. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We train stage-1 and stage-2 separately with 24 epochs, a learning rate of 2×10-4.
- **p. 7 / 4.2. Performance - extractive PDF cue:** Besides, VoxFormer needs less than 16GB GPU memory during training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Motivated, reconstruction-beforehallucination, sparsity-in-3D-space, build, twostage, framework, stage-1, CNN, proposes, sparse, voxel, queries, image, depth, attend, images, since, features, correspond, visible.
- **Relevant PDF headings:** 3. Methodology (p. 3); 3.2. Overall Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | SemanticKITTI SSC benchmark is interested in a volume of 51.2m ahead of the car, 25.6m to left and right side, and 6.4m ... | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Semantic / temporal fusion | We compare VoxFormer against the state-of-the-art SSC methods with public resources: (1) a camera-based SSC method MonoScene [4] based on 2D-to-3D feature ... | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Performance) |
| Robot query / planning handoff | VoxFormer-T can achieve mIoU scores of 21.55 and 18.42 within 12.8 meters and 25.6 meters, which outperforms the state-of-the-art MonoScene by 75.92% ... | p. 7 (4.2. Performance), p. 6 (4.2. Performance) |

## Failure and Ablation Link

- **p. 6 / 4.2. Performance - extractive PDF cue:** Meanwhile, the semantic score is also improved by 9.29% without sacrificing IoU.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study for image depth. With monocular depth, VoxFormer-S performs better than MonoScene in geome- try (12.8m, 25.6m, and 51.2m) and semantics (12.8m ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation study for query proposal. Our depth-based query proposal performs best. t
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. Ablation study for 2D image feature layers. Spatial resolution is relative to the input image size. Methods IoU (%) mIoU (%) Ours 44.02 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Preliminary), p. 5 (3.3. Predefined Parameters), p. 5 (3.3. Predefined Parameters), p. 3 (3.2. Overall Architecture), p. 4 (3.3. Predefined Parameters), p. 4 (3.3. Predefined Parameters), objective p. 5 (3.6. Training Loss), p. 5 (3.6. Training Loss), p. 3 (3.1. Preliminary), p. 3 (3.2. Overall Architecture), p. 4 (3.3. Predefined Parameters), temporal p. 3 (3.2. Overall Architecture), p. 3 (3.1. Preliminary), p. 4 (3.3. Predefined Parameters), p. 4 (3.3. Predefined Parameters), p. 5 (4.1. Experimental Setup), p. 5 (3.6. Training Loss).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
