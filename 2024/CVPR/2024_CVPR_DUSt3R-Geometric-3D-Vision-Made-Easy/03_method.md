# Method - DUSt3R: Geometric 3D Vision Made Easy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.14132; PDF retrieval source: https://arxiv.org/pdf/2312.14132. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3. Method), p. 4 (3.1. Overview), p. 5 (3.2. Training Objective), p. 5 (3.2. Training Objective), p. 6 (3.4. Global Alignment), p. 6 (3.4. Global Alignment)): The resulting token representations F 1 and F 2 are then passed to two transformer decoders that constantly exchange information via cross-attention.

## Method Body Digest

- **p. 4 / 3. Method - extractive body cue:** The resulting token representations F 1 and F 2 are then passed to two transformer decoders that constantly exchange information via cross-attention.
- **p. 4 / 3.1. Overview - extractive body cue:** To that aim, we train a network F that takes as input 2 RGB images I1, I2 ∈RW ×H×3 and outputs 2 corresponding pointmaps X1,1, ...
- **p. 5 / 3.2. Training Objective - extractive body cue:** The final training objective is the confidence-weighted regression loss from Eq.
- **p. 5 / 3.2. Training Objective - extractive body cue:** Training network F with this objective allows to estimate confidence scores without an explicit supervision.
- **p. 6 / 3.4. Global Alignment - extractive body cue:** We then formulate the following optimization problem: χ∗= arg min χ,P,σ X e∈E X v∈e HW X i=1 Cv,e i ∥χv i -σePeXv,e i ∥.
- **p. 6 / 3.4. Global Alignment - extractive body cue:** Reconstruction examples on two scenes never seen during training.
- **p. 5 / 3.3. Downstream Applications - extractive body cue:** To minimize errors, we typically retain reciprocal (mutual) correspondences M1,2 between images I1 and I2, i.e. we have: M1,2 = {(i, j) / i = ...
- **p. 6 / 3.4. Global Alignment - extractive body cue:** The optimization is carried out using standard gradient descent and typically converges after a few hundred steps, requiring mere seconds on a standard GPU.

## Design Rationale

- **p. 3 / 3. Method - extractive body cue:** Before delving into the details of our method, we introduce below the essential concept of pointmaps.
- **p. 2 / 1. Introduction - extractive body cue:** Second, we introduce the pointmap representation for MVS applications, that enables the network to predict the 3D shape in a canonical frame, while preserving the ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present DUSt3R, a radically novel approach for Dense Unconstrained Stereo 3D Reconstruction from un-calibrated and un-posed cameras.

## Source Evidence Cues

- **p. 4 / 3. Method - extractive body cue:** The resulting token representations F 1 and F 2 are then passed to two transformer decoders that constantly exchange information via cross-attention.
- **p. 4 / 3.1. Overview - extractive body cue:** To that aim, we train a network F that takes as input 2 RGB images I1, I2 ∈RW ×H×3 and outputs 2 corresponding pointmaps X1,1, ...
- **p. 5 / 3.2. Training Objective - extractive body cue:** The final training objective is the confidence-weighted regression loss from Eq.
- **p. 5 / 3.2. Training Objective - extractive body cue:** Training network F with this objective allows to estimate confidence scores without an explicit supervision.
- **p. 6 / 3.4. Global Alignment - extractive body cue:** We then formulate the following optimization problem: χ∗= arg min χ,P,σ X e∈E X v∈e HW X i=1 Cv,e i ∥χv i -σePeXv,e i ∥.
- **p. 6 / 3.4. Global Alignment - extractive body cue:** Reconstruction examples on two scenes never seen during training.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The resulting token representations F 1 and F 2 are then passed to two transformer decoders that constantly exchange information via cross-attention. | p. 4 (3. Method), p. 4 (3.1. Overview) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To that aim, we train a network F that takes as input 2 RGB images I1, I2 ∈RW ×H×3 and outputs 2 ... | p. 4 (3.1. Overview), p. 5 (3.2. Training Objective) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The final training objective is the confidence-weighted regression loss from Eq. | p. 5 (3.2. Training Objective), p. 5 (3.2. Training Objective) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Training Objective - extractive body cue:** The final training objective is the confidence-weighted regression loss from Eq.
- **p. 5 / 3.3. Downstream Applications - extractive body cue:** To minimize errors, we typically retain reciprocal (mutual) correspondences M1,2 between images I1 and I2, i.e. we have: M1,2 = {(i, j) / i = ...
- **p. 6 / 3.4. Global Alignment - extractive body cue:** The optimization is carried out using standard gradient descent and typically converges after a few hundred steps, requiring mere seconds on a standard GPU.
- **p. 4 / 3. Method - extractive body cue:** The network F is trained using a simple regression loss (Eq.
- **p. 4 / 3.2. Training Objective - extractive body cue:** Our sole training objective is based on regression in the 3D space.
- **p. 6 / 3.4. Global Alignment - extractive body cue:** Indeed, we are not minimizing 2D reprojection errors, as bundle adjustment normally does, but 3D projection errors.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.2. Training Objective), p. 4 (3. Method), p. 4 (3.2. Training Objective), p. 5 (3.2. Training Objective), p. 6 (3.4. Global Alignment), p. 6 (3.4. Global Alignment).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | train, network, takes, input, RGB, images, outputs, corresponding, pointmaps, associated, confidence, maps, Examples, image | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | train, network, takes, input, RGB, images, outputs, corresponding, pointmaps, associated | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Before, delving, details, introduce, below, essential, concept, pointmaps, Second, pointmap | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | final, training, objective, confidence-weighted, regression, loss, minimize, errors, typically, retain | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. Overview - extractive body cue:** To that aim, we train a network F that takes as input 2 RGB images I1, I2 ∈RW ×H×3 and outputs 2 corresponding pointmaps X1,1, ...
- **p. 5 / 3.2. Training Objective - extractive body cue:** Examples of input image pairs with their corresponding outputs are shown in Fig.
- **p. 2 / 1. Introduction - extractive body cue:** Fourth, we demonstrate promising performance on a range of 3D vision tasks In particular, our all-in-one model achieves state-of-the-art results on monocular and multi-view depth ...
- **p. 4 / 3.1. Overview - extractive body cue:** The two input images are first encoded in a Siamese manner by the same weight-sharing ViT encoder [27], yielding two token representations F 1 and ...
- **p. 2 / 1. Introduction - extractive body cue:** This is concerning, because in the end, "an MVS algorithm is only as good as the quality of the input images and camera parameters" [32].
- **p. 5 / 3.3. Downstream Applications - extractive body cue:** The rich properties of the output pointmaps allows us to perform various convenient operations with relative ease.
- **p. 6 / 3.4. Global Alignment - extractive body cue:** The left scene shows the raw result output from F(I1, I2).
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For each sequence, we random select 10 frames and feed all possible 45 pairs to DUSt3R. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Most recently, GO-SLAM [179] proposed real-time global pose optimization by considering the complete history of input frames and continuously aligning all poses ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Most recently, GO-SLAM [179] proposed real-time global pose optimization by considering the complete history of input frames and continuously aligning all poses ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For each sequence, we random select 10 frames and feed all possible 45 pairs to DUSt3R. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Overview - extractive body cue:** To that aim, we train a network F that takes as input 2 RGB images I1, I2 ∈RW ×H×3 and outputs 2 corresponding pointmaps X1,1, ...
- **p. 5 / 3.2. Training Objective - extractive body cue:** The final training objective is the confidence-weighted regression loss from Eq.
- **p. 5 / 3.2. Training Objective - extractive body cue:** Training network F with this objective allows to estimate confidence scores without an explicit supervision.
- **p. 6 / 3.4. Global Alignment - extractive body cue:** Reconstruction examples on two scenes never seen during training.
- **p. 5 / 3.4. Global Alignment - extractive body cue:** To that aim, we either use existing off-the-shelf image retrieval methods, or we pass all pairs through network F (inference takes ≈40ms on a H100 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** resulting, token, representations, then, passed, transformer, decoders, constantly, exchange, information, cross-attention, train, network, takes, input, RGB, images, outputs, corresponding, pointmaps.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | These datasets feature diverse scenes types: indoor, outdoor, synthetic, real-world, object-centric, etc. | p. 6 (4. Experiments with DUSt3R), p. 8 (4.4. Multi-view Depth) |
| Semantic / temporal fusion | Our method obtains comparable accuracy compared to existing approaches, being feature-matching ones [101, 103] or end-to-end learningbased methods [11, 55, 102, 125, ... | p. 7 (4.1. Visual Localization), p. 7 (4.3. Monocular Depth) |
| Robot query / planning handoff | We observe in Table 3 that DUSt3R achieves stateof-the-art accuracy on ETH-3D and outperforms most recent state-of-the-art methods overall, even those using ... | p. 8 (4.4. Multi-view Depth), p. 7 (4.2. Multi-view Pose Estimation) |

## Failure and Ablation Link

- **p. 6 / 4. Experiments with DUSt3R - extractive body cue:** We emphasize that all results are obtained with the same DUSt3R model (our default model is denoted as ‘DUSt3R 512', other DUSt3R models serves for ...
- **p. 7 / 4.1. Visual Localization - extractive body cue:** For results obtained without using ground-truth intrinsics parameters, refer to the appendix in Sec.
- **p. 7 / 4.1. Visual Localization - extractive body cue:** In other words, we simply use the raw pointmaps output from F(IQ, IB) without any refinement, where IQ is the query image and IB is ...
- **p. 9 / 15.6 51.5 17.4 (374.2) - extractive body cue:** Yet, without prior knowledge about the cameras, we reach an average accuracy of 2.7mm, with a completeness of 0.8mm, for an overall average distance of ...
- **p. 9 / 15.6 51.5 17.4 (374.2) - extractive body cue:** Multi-view depth evaluation with different settings: a) Classical approaches; b) with poses and depth range, without alignment; c) absolute scale evaluation with poses, without depth ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview: Given an unconstrained image collection, i.e. a set of photographs with unknown camera poses and intrinsics, our proposed method DUSt3R outputs a ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4. Example of 3D reconstruction of an unseen MegaDepth scene from two images (top-left). Note this is the raw output of the network, i.e. ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3. Method), p. 4 (3.1. Overview), p. 5 (3.2. Training Objective), p. 5 (3.2. Training Objective), p. 6 (3.4. Global Alignment), p. 6 (3.4. Global Alignment), objective p. 5 (3.2. Training Objective), p. 5 (3.3. Downstream Applications), p. 6 (3.4. Global Alignment), p. 4 (3. Method), p. 4 (3.2. Training Objective), p. 6 (3.4. Global Alignment), temporal p. 7 (4.2. Multi-view Pose Estimation), p. 14 (Appendix), p. 4 (3. Method), p. 4 (3. Method), p. 5 (3.3. Downstream Applications), p. 6 (3.4. Global Alignment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The resulting token representations F 1 and F 2 are then passed to two transformer decoders that constantly exchange information via cross-attention. (p. 4, 3. Method).
- **Objective/update evidence:** The final training objective is the confidence-weighted regression loss from Eq. (p. 5, 3.2. Training Objective).
- **Temporal/runtime evidence:** For each sequence, we random select 10 frames and feed all possible 45 pairs to DUSt3R. (p. 7, 4.2. Multi-view Pose Estimation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
