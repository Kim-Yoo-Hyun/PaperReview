# Method - DiSCO-3D : Discovering and Segmenting Sub-Concepts from Open-vocabulary Queries in NeRF

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.5. Method extensions), p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 5 (3.5. Method extensions), p. 8 (4.3.2. Unsupervised Semantic Segmentation)): First, the projector requires at least one spatially precise feature field to perform segmentation (e.g., dense encoders).

## Method Body Digest

- **p. 5 / 3.5. Method extensions - extractive body cue:** First, the projector requires at least one spatially precise feature field to perform segmentation (e.g., dense encoders).
- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** Since SmooSeg only produces 2D segmentations, we recover a 3D segmentation by training a Semantic-NeRF [39] on its outputs.
- **p. 5 / 3.5. Method extensions - extractive body cue:** Given these conditions, the input 3D representations and query modalities can vary widely-from a single feature field satisfying both requirements (e.g.
- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** Finally, K-Means on the feature field yields slightly lower but comparable results.
- **p. 5 / 3.5. Method extensions - extractive body cue:** While the losses Lproj and Lproto remain unchanged, a loss Lqi irr is added for each query qi following Equation 4.
- **p. 5 / 3.5. Method extensions - extractive body cue:** Each of these losses is guided by a unique one-hot vector Hqi that defines the relevant prototypes for each query.
- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** Regarding GrowSP, although it succeeds in performing accurate segmentation, the global performances are lower, probably due to the input data modalities, as the discrete nature ...
- **p. 2 / 1. Introduction - extractive body cue:** We evaluate DiSCO-3D on both real and synthetic data, demonstrating better performance than hand-designed naive baselines on the proposed OV-SD task and experimentally show that ...

## Design Rationale

- **p. 5 / 3.5. Method extensions - extractive body cue:** Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) as ...
- **p. 3 / 3.1. Problem Statement and Overview - extractive body cue:** In the following, we present our method in three parts.
- **p. 2 / 1. Introduction - extractive body cue:** We present DiSCO-3D, the first method designed to solve the 3D OV-SD problem, combining Unsupervised Semantic Segmentation with Open-Vocabulary Segmentation guidance to serve as a ...

## Source Evidence Cues

- **p. 5 / 3.5. Method extensions - extractive body cue:** First, the projector requires at least one spatially precise feature field to perform segmentation (e.g., dense encoders).
- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** Since SmooSeg only produces 2D segmentations, we recover a 3D segmentation by training a Semantic-NeRF [39] on its outputs.
- **p. 5 / 3.5. Method extensions - extractive body cue:** Given these conditions, the input 3D representations and query modalities can vary widely-from a single feature field satisfying both requirements (e.g.
- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** Finally, K-Means on the feature field yields slightly lower but comparable results.
- **Detected method headings:** 3.5. Method extensions (p. 5); 4.2.1. Evaluated methods (p. 6); Method (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | First, the projector requires at least one spatially precise feature field to perform segmentation (e.g., dense encoders). | p. 5 (3.5. Method extensions), p. 8 (4.3.2. Unsupervised Semantic Segmentation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Since SmooSeg only produces 2D segmentations, we recover a 3D segmentation by training a Semantic-NeRF [39] on its outputs. | p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 5 (3.5. Method extensions) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Given these conditions, the input 3D representations and query modalities can vary widely-from a single feature field satisfying both requirements (e.g. | p. 5 (3.5. Method extensions), p. 8 (4.3.2. Unsupervised Semantic Segmentation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.5. Method extensions - extractive body cue:** While the losses Lproj and Lproto remain unchanged, a loss Lqi irr is added for each query qi following Equation 4.
- **p. 5 / 3.5. Method extensions - extractive body cue:** Each of these losses is guided by a unique one-hot vector Hqi that defines the relevant prototypes for each query.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.5. Method extensions), p. 5 (3.5. Method extensions).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Regarding, GrowSP, although, succeeds, performing, accurate, segmentation, global, performances, lower, probably, input, data, modalities | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Regarding, GrowSP, although, succeeds, performing, accurate, segmentation, global, performances, lower | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Although, present, pre-trained, LeRF, input, DiSCO-3D, compatible, wide, range, feature | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | While, losses, Lproj, Lproto, remain, unchanged, loss, Lqi, added, query | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** Regarding GrowSP, although it succeeds in performing accurate segmentation, the global performances are lower, probably due to the input data modalities, as the discrete nature ...
- **p. 2 / 1. Introduction - extractive body cue:** We evaluate DiSCO-3D on both real and synthetic data, demonstrating better performance than hand-designed naive baselines on the proposed OV-SD task and experimentally show that ...
- **p. 3 / 3.1. Problem Statement and Overview - extractive body cue:** DiSCO-3D inputs pairs of features from 3D samples into a projector network learnt to accentuate semantic disparities.
- **p. 3 / 3.2. Preliminaries - extractive body cue:** Neural Radiance Fields [25] (NeRFs) are learnable neural networks (possibly coupled with multi-resolution feature hashgrids [27]) overfitted to individual scenes, which output density (σ) and ...
- **p. 5 / 3.5. Method extensions - extractive body cue:** OpenSeg in subsection 4.2) to alternative inputs such as user clicks, as demonstrated in Figure 3.
- **p. 5 / 3.5. Method extensions - extractive body cue:** Given these conditions, the input 3D representations and query modalities can vary widely-from a single feature field satisfying both requirements (e.g.
- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** GrowSP uses features obtained from SparseConv while every other baselines uses DINO as input.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We implemented our method in the Nerfstudio [34] framework and every evaluation is based on the same Nerfacto model, a grid-based NeRF ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This line of research has recently expanded with methods like ACSeg [20], EAGLE [13], and SmooSeg [18], which focus on online clustering ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All our experiments were run on the same single RTX 4090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** Since SmooSeg only produces 2D segmentations, we recover a 3D segmentation by training a Semantic-NeRF [39] on its outputs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, projector, requires, least, spatially, precise, feature, field, perform, segmentation, dense, encoders, Since, SmooSeg, only, produces, segmentations, recover, training, Semantic-NeRF.
- **Relevant PDF headings:** 3.5. Method extensions (p. 5); 4.2.1. Evaluated methods (p. 6); Method (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We also display some qualitative examples in Figure 3 across various scenes (both indoor and outdoor from various datasets [12, 21, 33]), ... | p. 7 (4.2.2. Results), p. 6 (4.1. Implementation and evaluation details) |
| Semantic / temporal fusion | All quantitative experiments, including DiSCO3D and the comparative baselines, use the same pre-trained Nerfacto models and feature fields as input. | p. 5 (4.1. Implementation and evaluation details), p. 5 (4. Experimental evaluations) |
| Robot query / planning handoff | Notice that the only difference between DiSCO-3D and those baselines relies on the fact that DiSCO-3D achieves USS and OVSeg jointly whereas ... | p. 6 (4.2.1. Evaluated methods), p. 7 (4.2.3. Ablations studies) |

## Failure and Ablation Link

- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** Sensitivity to Number of Prototypes and influence of Lproto.
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** Finally, the last column, corresponding to our main experiment with a fixed N = 10, shows that performance is maintained without requiring prior knowledge of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. DiSCO-3D Quantitative Evaluation for OV-Seg. form of OV-SD where each query asks for a single sub- concept, and to USS, which can be ...
- **p. 5 / 4. Experimental evaluations - extractive body cue:** Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's limitations.
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** The last column refers to the main experiment where the number of prototypes is fixed and does not depend on NGT .

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.5. Method extensions), p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 5 (3.5. Method extensions), p. 8 (4.3.2. Unsupervised Semantic Segmentation), objective p. 5 (3.5. Method extensions), p. 5 (3.5. Method extensions), temporal p. 5 (4.1. Implementation and evaluation details), p. 2 (2. Related Works).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
