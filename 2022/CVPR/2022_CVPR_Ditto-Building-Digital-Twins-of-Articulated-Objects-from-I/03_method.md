# Method - Ditto: Building Digital Twins of Articulated Objects from Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2202.08227; PDF retrieval source: https://arxiv.org/pdf/2202.08227. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4.2. Implicit Decoders), p. 4 (4.1. Two-Stream Encoder), p. 3 (4. Method), p. 5 (4.3. Training), p. 3 (4. Method), p. 5 (4.4. Explicit Articulated Object Extraction)): First, we use an implicit decoder to predict joint type pjtype: \begin {a li gned } f_{\theta _\text {type}}(\mathbf {p}_\text {in}, \psi _{\mathbf {p}_\text {in}}^c) \rightarrow p_{j_\text {type}}(\mathbf {p}_\text {in}). ...

## Method Body Digest

- **p. 4 / 4.2. Implicit Decoders - extractive body cue:** First, we use an implicit decoder to predict joint type pjtype: \begin {a li gned } f_{\theta _\text {type}}(\mathbf {p}_\text {in}, \psi _{\mathbf {p}_\text {in}}^c) ...
- **p. 4 / 4.1. Two-Stream Encoder - extractive body cue:** Then we use two PointNet++ decoder νgeo and νart to propagate the fused subsampled point features into dense features aligned with the original points f_ ...
- **p. 3 / 4. Method - extractive body cue:** Ditto consists of a two-stream encoder that fuses two input point clouds and multiple implicit decoders for geometry and articulation.
- **p. 5 / 4.3. Training - extractive body cue:** The loss for training consists of two parts: the geometry loss and the joint loss.
- **p. 3 / 4. Method - extractive body cue:** Upon inference, we extract explicit models of articulated objects from the implicit decoders.
- **p. 5 / 4.4. Explicit Articulated Object Extraction - extractive body cue:** Then we apply Multiresolution IsoSurface Extraction [33] and Marching Cube [29] to extract per-part surface meshes.
- **p. 5 / 4.3. Training - extractive body cue:** For joint type prediction, we also apply the standard binary cross entropy loss.
- **p. 3 / 4. Method - extractive body cue:** The model is jointly optimized with a combination of loss functions on geometry reconstruction and articulation estimation.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** Given visual observations before and after interaction, our method jointly reconstructs the part-level geometry and articulation model of the object.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we apply our method to real-world articulated objects for recreating digital twins.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce Ditto (Digital twin of articulated objects), an implicit neural representation-based model that jointly predicts part-level geometry and kinematic articulation between the parts.

## Source Evidence Cues

- **p. 4 / 4.2. Implicit Decoders - extractive body cue:** First, we use an implicit decoder to predict joint type pjtype: \begin {a li gned } f_{\theta _\text {type}}(\mathbf {p}_\text {in}, \psi _{\mathbf {p}_\text {in}}^c) ...
- **p. 4 / 4.1. Two-Stream Encoder - extractive body cue:** Then we use two PointNet++ decoder νgeo and νart to propagate the fused subsampled point features into dense features aligned with the original points f_ ...
- **p. 3 / 4. Method - extractive body cue:** Ditto consists of a two-stream encoder that fuses two input point clouds and multiple implicit decoders for geometry and articulation.
- **p. 5 / 4.3. Training - extractive body cue:** The loss for training consists of two parts: the geometry loss and the joint loss.
- **p. 3 / 4. Method - extractive body cue:** Upon inference, we extract explicit models of articulated objects from the implicit decoders.
- **p. 5 / 4.4. Explicit Articulated Object Extraction - extractive body cue:** Then we apply Multiresolution IsoSurface Extraction [33] and Marching Cube [29] to extract per-part surface meshes.
- **Detected method headings:** 4. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | First, we use an implicit decoder to predict joint type pjtype: \begin {a li gned } f_{\theta _\text {type}}(\mathbf {p}_\text {in}, \psi ... | p. 4 (4.2. Implicit Decoders), p. 4 (4.1. Two-Stream Encoder) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Then we use two PointNet++ decoder νgeo and νart to propagate the fused subsampled point features into dense features aligned with the ... | p. 4 (4.1. Two-Stream Encoder), p. 3 (4. Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Ditto consists of a two-stream encoder that fuses two input point clouds and multiple implicit decoders for geometry and articulation. | p. 3 (4. Method), p. 5 (4.3. Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.3. Training - extractive body cue:** For joint type prediction, we also apply the standard binary cross entropy loss.
- **p. 3 / 4. Method - extractive body cue:** The model is jointly optimized with a combination of loss functions on geometry reconstruction and articulation estimation.
- **p. 5 / 4.3. Training - extractive body cue:** The state prediction and parameter prediction can be jointly optimized with this loss Ldispp = //cpup -ˆcpˆup//.
- **p. 3 / 3. Problem Formulation - extractive body cue:** Without the loss of generality, we assume only one part is moved after the interaction, which we call the mobile part.
- **p. 4 / 4.1. Two-Stream Encoder - extractive body cue:** This projection operation greatly reduces the computation cost while keeping the spatial distribution of feature points.
- **p. 4 / 4.2. Implicit Decoders - extractive body cue:** 4.2.1 Geometry Implicit Decoder Our geometry implicit decoder is a mapping from a coordinate p ∈R3 to the occupancy probability o(p) at the coordinate.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3. Problem Formulation), p. 3 (4. Method), p. 5 (4.3. Training), p. 5 (4.3. Training), p. 4 (4.1. Two-Stream Encoder), p. 4 (4.1. Two-Stream Encoder).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, pair, point, cloud, observations, articulated, object, before, after, interaction, study, problem, recreating, interactive | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | input, pair, point, cloud, observations, articulated, object, before, after, interaction | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Given, visual, observations, before, after, interaction, jointly, reconstructs, part-level, geometry | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | joint, type, prediction, apply, standard, binary, cross, entropy, loss, model | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Problem Formulation - extractive body cue:** The input to our method is a pair of point cloud observations P1, P2 ∈RN×3 of the articulated object before and after an interaction.
- **p. 3 / 3. Problem Formulation - extractive body cue:** We study the problem of recreating interactive digital twins of articulated objects from a pair of sensory observations before and after an interaction.
- **p. 4 / 4.2. Implicit Decoders - extractive body cue:** The joint state is the translation distance cp resulting from the interaction.
- **p. 4 / 4.2. Implicit Decoders - extractive body cue:** Since we assume that only one joint's state is changed due to the interaction, we can segment the object into the static and mobile parts ...
- **p. 5 / 4.2. Implicit Decoders - extractive body cue:** The joint state of the revolute joint is the rotation angle cr resulting from the interaction.
- **p. 1 / 1. Introduction - extractive body cue:** Given visual observations before and after interaction, our method jointly reconstructs the part-level geometry and articulation model of the object.
- **p. 2 / 1. Introduction - extractive body cue:** Following pioneer work on the interactive perception of articulated objects [15,31], we propose to infer the digital twins from visual observations collected before and after ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We now present Ditto, a learning framework that builds digital twins of articulated objects through interactive perception. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Moreover, we import the digital twin of the faucet into Robosuite [62], a robot learning simulation framework. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.3. Training - extractive body cue:** The loss for training consists of two parts: the geometry loss and the joint loss.
- **p. 3 / 4. Method - extractive body cue:** Upon inference, we extract explicit models of articulated objects from the implicit decoders.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, implicit, decoder, predict, joint, type, pjtype, begin, gned, theta, text, mathbf, rightarrow, aligned, Then, decoders, parameters, states, prismatic, joints.
- **Relevant PDF headings:** 4. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Reconstructed unseen articulated objects in Shape2Motion [55] (top) and synthetic [1] (bottom) dataset. | p. 7 (5.2. Baselines), p. 6 (5.1. Datasets) |
| Semantic / temporal fusion | On both datasets, Ditto gets significantly better results on all metrics compared with the baselines. | p. 7 (5.4. Articulated Object Reconstruction), p. 6 (5.2. Baselines) |
| Robot query / planning handoff | 1, Ditto achieves superior or at least on-par performance on all metrics. | p. 8 (5.5. Ablation Studies), p. 7 (5.4. Articulated Object Reconstruction) |

## Failure and Ablation Link

- **p. 8 / 5.5. Ablation Studies - extractive body cue:** Qualitative results and analysis of ablation study are in the appendix.
- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** Failure of joint estimation also harms segmentation prediction because the joint parameter decoders and the segmentation decoder share the same feature planes.
- **p. 8 / 5.4. Articulated Object Reconstruction - extractive body cue:** 3, A-SDF fails to reconstruct the shape details of unseen objects, especially the objects with prismatic joints.
- **p. 8 / 5.5. Ablation Studies - extractive body cue:** We observe that using the same 3D and 2D features for geometry and articulation makes training unstable, and 2D features would harm the reconstruction due ...
- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** In comparison, Ditto does not suffer from such a bottleneck as an end-to-end method.
- **p. 6 / 5.1. Datasets - extractive body cue:** Even though we use multi-view depth images, the point cloud may still be incomplete due to the self-occlusion of the objects.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4.2. Implicit Decoders), p. 4 (4.1. Two-Stream Encoder), p. 3 (4. Method), p. 5 (4.3. Training), p. 3 (4. Method), p. 5 (4.4. Explicit Articulated Object Extraction), objective p. 5 (4.3. Training), p. 3 (4. Method), p. 5 (4.3. Training), p. 3 (3. Problem Formulation), p. 4 (4.1. Two-Stream Encoder), p. 4 (4.2. Implicit Decoders), temporal p. 3 (4. Method), p. 8 (5.6. Real-World Experiments), p. 8 (5.6. Real-World Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Ditto consists of a two-stream encoder that fuses two input point clouds and multiple implicit decoders for geometry and articulation. (p. 3, 4. Method).
- **Objective/update evidence:** The state prediction and parameter prediction can be jointly optimized with this loss Ldispp = //cpup -ˆcpˆup//. (p. 5, 4.3. Training).
- **Temporal/runtime evidence:** We now present Ditto, a learning framework that builds digital twins of articulated objects through interactive perception. (p. 3, 4. Method).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
