# Method - C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 4 (3.3. Generated-RGB Branch), p. 4 (3.3. Generated-RGB Branch), p. 3 (3.2. C-GenReg - Overview), p. 3 (3.1. Problem Definition)): To meet these goals, we propose a "match-then-fuse" probabilistic strategy, where putative correspondences are first established independently for each modality by computing feature similarity matrices between source and target points.

## Method Body Digest

- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive PDF cue:** To meet these goals, we propose a "match-then-fuse" probabilistic strategy, where putative correspondences are first established independently for each modality by computing feature similarity matrices ...
- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive PDF cue:** To approximate the modality-specific correspondence posterior Pr(Mij/Sm ij ), where m∈{geo,img}, we first compute the source-target feature similarity matrices for each modality and then apply ...
- **p. 4 / 3.3. Generated-RGB Branch - extractive PDF cue:** Specifically, we use MASt3R [14], a VFM trained to produce dense correspondence-aware features.
- **p. 4 / 3.3. Generated-RGB Branch - extractive PDF cue:** To ensure coherent and controllable generation, we use prompt-based text guidance with a fixed structure: a shared prefix that instructs the model to interpret the ...
- **p. 3 / 3.2. C-GenReg - Overview - extractive PDF cue:** C-GenReg extracts complementary features for point cloud registration through a dual-branch architecture followed by a probabilistic fusion stage (Fig.
- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** Most learning-based methods address this by extracting discriminative point-wise feature descriptors and match point pairs based on feature similarity.
- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive PDF cue:** The fusion module is designed with two main objectives: (1) to preserve the inductive biases of the pretrained feature extractors, which are optimized for point ...
- **p. 4 / 3.3. Generated-RGB Branch - extractive PDF cue:** This choice is motivated by the inductive bias and feature structure of taskoriented VFMs, which better aligns with the objectives of ge3007

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** Standard point cloud registration consists of feature extraction, feature matching, and robust pose estimation (e.g.
- **p. 2 / 1. Introduction - extractive PDF cue:** In contrast, our method, C-GenReg (stands for Consistent Generative Registration), leverages WFMs to generate multiview-consistent RGB views directly from geometry, eliminating the need for any ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Instead, we introduce a "Matchthen-Fuse" scheme that combines two independent correspondence posteriors, one from the WFM + VFM branch and one from the geometric branch, ...

## Source Evidence Cues

- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive PDF cue:** To meet these goals, we propose a "match-then-fuse" probabilistic strategy, where putative correspondences are first established independently for each modality by computing feature similarity matrices ...
- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive PDF cue:** To approximate the modality-specific correspondence posterior Pr(Mij/Sm ij ), where m∈{geo,img}, we first compute the source-target feature similarity matrices for each modality and then apply ...
- **p. 4 / 3.3. Generated-RGB Branch - extractive PDF cue:** Specifically, we use MASt3R [14], a VFM trained to produce dense correspondence-aware features.
- **p. 4 / 3.3. Generated-RGB Branch - extractive PDF cue:** To ensure coherent and controllable generation, we use prompt-based text guidance with a fixed structure: a shared prefix that instructs the model to interpret the ...
- **p. 3 / 3.2. C-GenReg - Overview - extractive PDF cue:** C-GenReg extracts complementary features for point cloud registration through a dual-branch architecture followed by a probabilistic fusion stage (Fig.
- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** Most learning-based methods address this by extracting discriminative point-wise feature descriptors and match point pairs based on feature similarity.
- **Detected method headings:** 3. Method (p. 3); 4.2. Method Evaluation (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To meet these goals, we propose a "match-then-fuse" probabilistic strategy, where putative correspondences are first established independently for each modality by computing ... | p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To approximate the modality-specific correspondence posterior Pr(Mij/Sm ij ), where m∈{geo,img}, we first compute the source-target feature similarity matrices for each modality ... | p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 4 (3.3. Generated-RGB Branch) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Specifically, we use MASt3R [14], a VFM trained to produce dense correspondence-aware features. | p. 4 (3.3. Generated-RGB Branch), p. 4 (3.3. Generated-RGB Branch) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive PDF cue:** The fusion module is designed with two main objectives: (1) to preserve the inductive biases of the pretrained feature extractors, which are optimized for point ...
- **p. 4 / 3.3. Generated-RGB Branch - extractive PDF cue:** This choice is motivated by the inductive bias and feature structure of taskoriented VFMs, which better aligns with the objectives of ge3007
- **p. 5 / 3.3. Generated-RGB Branch - extractive PDF cue:** While increasing K improves viewpoint coverage, it also increases computational cost.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Problem Definition), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, point, cloud, render, depth, Cosmos-Transfer, WFM, generate, multi-view-consistent, RGB, images, preserve, Generated, source | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | input, point, cloud, render, depth, Cosmos-Transfer, WFM, generate, multi-view-consistent, RGB | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Standard, point, cloud, registration, consists, feature, extraction, matching, robust, pose | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | fusion, module, designed, main, objectives, preserve, inductive, biases, pretrained, feature | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. C-GenReg - Overview - extractive PDF cue:** From each input point cloud, we render a depth map and use the Cosmos-Transfer WFM [18] to generate multi-view-consistent RGB images that preserve 3006
- **p. 4 / 3.2. C-GenReg - Overview - extractive PDF cue:** Generated source and target images with a subset of matched points (color-coded correspondences), and the corresponding matches visualized on the input point clouds.
- **p. 4 / 3.3. Generated-RGB Branch - extractive PDF cue:** When the data is provided as LiDAR point clouds, we simulate the same input format by mounting a virtual camera and projecting the 3D points ...
- **p. 5 / 3.3. Generated-RGB Branch - extractive PDF cue:** Since the generated RGB frames originate from depth inputs, we can lift the 2D image features back to 3D space using the known depth camera ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Standard point cloud registration consists of feature extraction, feature matching, and robust pose estimation (e.g.
- **p. 1 / 1. Introduction - extractive PDF cue:** The pipeline operates in two parallel branches: (1) GeneratedRGB Branch - a World Foundation Model generates RGB views that are geometrically aligned with the input ...
- **p. 5 / 3.4. Geometric Branch - extractive PDF cue:** The parallel geometric branch directly processes the input point clouds.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In common 3D datasets such as 3DMatch and ScanNet [6, 31], point clouds are constructed by aggregating a temporal sequence of L ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We use this temporal depth sequence as the conditioning signal for Cosmos-Transfer. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We follow the ScanNet Hard protocol introduced in [12, 13], where source and target frames are 50 frames apart, resulting in significantly ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.3. Generated-RGB Branch - extractive PDF cue:** Specifically, we use MASt3R [14], a VFM trained to produce dense correspondence-aware features.
- **p. 4 / 3.2. C-GenReg - Overview - extractive PDF cue:** In parallel, the geometric branch encodes the raw point clouds using a pretrained registration-oriented 3D feature extractor, yielding complementary geometric descriptors.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** meet, goals, match-then-fuse, probabilistic, strategy, where, putative, correspondences, first, established, independently, modality, computing, feature, similarity, matrices, between, source, target, points.
- **Relevant PDF headings:** 3. Method (p. 3); 4.2. Method Evaluation (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For outdoor evaluation, we employ the Waymo Open Dataset [24], which contains large-scale LiDAR scans, and serves as a generalization benchmark for ... | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Semantic / temporal fusion | CGenReg is compared against both the hand-crafted descriptor FPFH [22] and several state-of-the-art (SOTA) learning-based baselines, including GeoTransformer [20], FCGF [4], Predator ... | p. 6 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation) |
| Robot query / planning handoff | Although this comparison is not strictly fair, since C-GenReg relies solely on 3D point cloud inputs, it is noteworthy that C-GenReg achieves ... | p. 7 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation) |

## Failure and Ablation Link

- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** All models in the pipeline are kept frozen with their publicly released pretrained weights, without any additional fine-tuning.
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** We perform an extensive ablation studies to analyze the contribution of each component in the C-GenReg pipeline.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation Study on the 3DMatch Benchmark. Top: impact of different Vision Foundation Models (no geometric features or fusion). Bottom: impact of geometric feature ...
- **p. 7 / 4.2. Method Evaluation - extractive PDF cue:** For reference, we additionally report C-GenReg-Oracle, which replaces the generated RGB with the real RGB input to provide an empirical upper bound on our pipeline's ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. C-GenReg Overview: A training-free, zero-shot point cloud registration framework with two parallel branches. (1) Generated-RGB Branch - source and target point clouds are ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Prompt robustness on 3DMatch. Relative rotation (RRE,◦) and translation (RTE, cm) errors under different prompt types. geometric coherence across viewpoints. A task-specific VFM ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Prompt robustness on 3DMatch. Relative rotation (RRE,◦) and translation (RTE, cm) errors under different prompt types. geometric coherence across viewpoints. A task-specific VFM ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 4 (3.3. Generated-RGB Branch), p. 4 (3.3. Generated-RGB Branch), p. 3 (3.2. C-GenReg - Overview), p. 3 (3.1. Problem Definition), objective p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.3. Generated-RGB Branch), temporal p. 4 (3.3. Generated-RGB Branch), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.3. Generated-RGB Branch), p. 3 (2. Related Work), p. 5 (3.3. Generated-RGB Branch), p. 7 (4.2. Method Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
