# Method - Surface Reconstruction for 3D Gaussian Splatting via Local Structural Hints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/274_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 9 (3 Method), p. 10 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 9 (3 Method), p. 7 (3 Method)): At first, we train the model with the color reconstruction loss as in original 3DGS [20] together with the monocular cue related losses in Sec.

## Method Body Digest

- **p. 9 / 3 Method - extractive body cue:** At first, we train the model with the color reconstruction loss as in original 3DGS [20] together with the monocular cue related losses in Sec.
- **p. 10 / 3 Method - extractive body cue:** After the optimization, we use 3D Gaussian means and normals for Poisson surface reconstruction [18] to extract the reconstructed meshes.
- **p. 5 / 3 Method - extractive body cue:** 3.1 and then elaborate on the technical details of each core module.
- **p. 6 / 3 Method - extractive body cue:** To address the above issues, our first thought is to leverage the monocular geometry cues [11] to guide the 3DGS training, including both surface normal ...
- **p. 9 / 3 Method - extractive body cue:** \mat hcal {L}_{\texttt {joi nt}} = \s um _{\bm {x}, \bm {\mu }_l} (\/F_\text {IMLS}(\bm {x}) - F_\text {MLP}(\bm {x})\/_2 + \/\frac {\nabla F_\text {MLP}(\bm ...
- **p. 7 / 3 Method - extractive body cue:** With a slight abuse of notation, we denote the adjusted rendered normal as ˆ N ′ and apply the following normal consistency loss with monocular ...
- **p. 8 / 3 Method - extractive body cue:** 2: Joint optimization of 3DGS and neural implicit representation.
- **p. 9 / 3 Method - extractive body cue:** The loss function will backpropagate the gradients to both the Gaussian Splatting field and the neural SDF.

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** To address this, we propose a novel regularizer that leverages a neural implicit network to approximate the signed distance values of the MLS function at ...
- **p. 8 / 3 Method - extractive body cue:** We propose a novel strategy to further align the Gaussians with the surface.
- **p. 3 / 1 Introduction - extractive body cue:** Moreover, to ensure geometry consistency, we propose regularizing the MLS-based function prediction with a jointly learned neural implicit field.

## Source Evidence Cues

- **p. 9 / 3 Method - extractive body cue:** At first, we train the model with the color reconstruction loss as in original 3DGS [20] together with the monocular cue related losses in Sec.
- **p. 10 / 3 Method - extractive body cue:** After the optimization, we use 3D Gaussian means and normals for Poisson surface reconstruction [18] to extract the reconstructed meshes.
- **p. 5 / 3 Method - extractive body cue:** 3.1 and then elaborate on the technical details of each core module.
- **p. 6 / 3 Method - extractive body cue:** To address the above issues, our first thought is to leverage the monocular geometry cues [11] to guide the 3DGS training, including both surface normal ...
- **p. 9 / 3 Method - extractive body cue:** \mat hcal {L}_{\texttt {joi nt}} = \s um _{\bm {x}, \bm {\mu }_l} (\/F_\text {IMLS}(\bm {x}) - F_\text {MLP}(\bm {x})\/_2 + \/\frac {\nabla F_\text {MLP}(\bm ...
- **p. 7 / 3 Method - extractive body cue:** With a slight abuse of notation, we denote the adjusted rendered normal as ˆ N ′ and apply the following normal consistency loss with monocular ...
- **p. 8 / 3 Method - extractive body cue:** 2: Joint optimization of 3DGS and neural implicit representation.
- **Detected method headings:** 3 Method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | At first, we train the model with the color reconstruction loss as in original 3DGS [20] together with the monocular cue related ... | p. 9 (3 Method), p. 10 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | After the optimization, we use 3D Gaussian means and normals for Poisson surface reconstruction [18] to extract the reconstructed meshes. | p. 10 (3 Method), p. 5 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 3.1 and then elaborate on the technical details of each core module. | p. 5 (3 Method), p. 6 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 9 / 3 Method - extractive body cue:** The loss function will backpropagate the gradients to both the Gaussian Splatting field and the neural SDF.
- **p. 9 / 3 Method - extractive body cue:** \mat hcal {L}_{\texttt {joi nt}} = \s um _{\bm {x}, \bm {\mu }_l} (\/F_\text {IMLS}(\bm {x}) - F_\text {MLP}(\bm {x})\/_2 + \/\frac {\nabla F_\text {MLP}(\bm ...
- **p. 6 / 3 Method - extractive body cue:** Following [20], the means of 3D Gaussians are initialized from Structure-from-Motion (SfM) [41] points, and their attributes are optimized by the differentiable reconstruction loss on ...
- **p. 7 / 3 Method - extractive body cue:** Without loss of the generality, we assume s1 is the minimum scaling value, and define our regularization term using this minimum value and the harmonic ...
- **p. 7 / 3 Method - extractive body cue:** \su m _ {i} z_i \alpha _i\prod _{j=1}^{i-1}(1-\alpha _j), \label {eqn:depth} (5) and optimizing it using a depth loss with monocular depth hint ¯D: \mat ...
- **p. 6 / 3 Method - extractive body cue:** As the sparsely initialized Gaussians may fail to represent scene details, 3DGS introduces a densification operation that performs splits and merges for Gaussians based on ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 9 (3 Method), p. 9 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | addition, vanilla, IMLS, definition, further, introduce, Robust, RIMLS, applying, Gaussian, kernel, inputted, norm, difference | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | addition, vanilla, IMLS, definition, further, introduce, Robust, RIMLS, applying, Gaussian | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, novel, regularizer, leverages, neural, implicit, network, approximate, signed, distance | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | loss, function, will, backpropagate, gradients, Gaussian, Splatting, field, neural, SDF | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 9 / 3 Method - extractive body cue:** In addition to the vanilla IMLS definition, we further introduce a Robust IMLS (RIMLS) by applying a 1-D Gaussian kernel inputted with the norm of ...
- **p. 1 / 1 Introduction - extractive body cue:** Given multi-view images with corresponding camera poses, 3DGS initializes Gaussian primitives from a sparse point cloud that comes from COLMAP [41] and renders a novel ...
- **p. 5 / 3 Method - extractive body cue:** Given a set of M posed RGB images I = {I1, . . . , IM} with corresponding camera parameters, 3DGS represents the scene as ...
- **p. 5 / 3 Method - extractive body cue:** Our primary goal is to reconstruct the scene geometry from 3D Gaussians by aligning Gaussians with the real-world surface.
- **p. 6 / 3 Method - extractive body cue:** 3.2 Monocular Geometry Cue for 3DGS Optimization While 3DGS mainly focuses on the image quality of view synthesis, it lags behind in scene surface reconstruction.
- **p. 6 / 3 Method - extractive body cue:** To address the above issues, our first thought is to leverage the monocular geometry cues [11] to guide the 3DGS training, including both surface normal ...
- **p. 7 / 3 Method - extractive body cue:** In addition to the local geometry cue like surface normal to guide the covariance learning, we can also adopt the monocular depth to guide the ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This section introduces our novel framework called GSrec, which includes several modules as shown in Fig. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To alleviate the heavy storage burden, we adopt a light structural 3DGS framework Scaffold-GS [25] as our baseline model. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Our experiments were run on a 24GB NVIDIA RTX 3090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 3 Method - extractive body cue:** At first, we train the model with the color reconstruction loss as in original 3DGS [20] together with the monocular cue related losses in Sec.
- **p. 6 / 3 Method - extractive body cue:** To address the above issues, our first thought is to leverage the monocular geometry cues [11] to guide the 3DGS training, including both surface normal ...
- **p. 9 / 3 Method - extractive body cue:** \mat hcal {L}_{\texttt {joi nt}} = \s um _{\bm {x}, \bm {\mu }_l} (\/F_\text {IMLS}(\bm {x}) - F_\text {MLP}(\bm {x})\/_2 + \/\frac {\nabla F_\text {MLP}(\bm ...
- **p. 7 / 3 Method - extractive body cue:** With a slight abuse of notation, we denote the adjusted rendered normal as ˆ N ′ and apply the following normal consistency loss with monocular ...
- **p. 12 / 4 Experiments - extractive body cue:** Notably, the average training time of our approach on this dataset is about 40 minutes, which is similar to SuGaR.
- **p. 14 / 4 Experiments - extractive body cue:** Although the MonoSDF (MLP) adopts pure MLP structure which shows robustness to the camera noise, the training time of such a variant gets much longer ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, train, model, color, reconstruction, loss, original, DGS, together, monocular, related, losses, Sec, After, optimization, Gaussian, means, normals, Poisson, surface.
- **Relevant PDF headings:** 3 Method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 2) ScanNet [10] is a real-world dataset captured with challenging image quality. | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Semantic / temporal fusion | We compare with previous strong baselines of neural implicit surface [16,33,51,58,62] and the 3DGS-based approach SuGaR [15]. | p. 14 (4 Experiments), p. 10 (4 Experiments) |
| Robot query / planning handoff | While keeping the MLS term with the gradient term in the joint loss (w/o eikonal term), the F-score can be significantly improved ... | p. 13 (4 Experiments), p. 13 (4 Experiments) |

## Failure and Ablation Link

- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Ablation study on Replica. We compared the key components with the variants of [25] including the guidance and the joint optimization.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 3: Ablation study about the joint MLS optimization and the MLS computation. We provide an in-depth analysis by verifying the effectiveness of the joint ...
- **p. 11 / 4 Experiments - extractive body cue:** We term these two variants as SuGaR (SDF)/(density).
- **p. 11 / 4 Experiments - extractive body cue:** 1 where our method outperforms both of SuGaR's variants with a clear margin.
- **p. 13 / 4 Experiments - extractive body cue:** To delve into its functionality, we show the results by ablation study over the MLS-based joint optimization.
- **p. 14 / 4 Experiments - extractive body cue:** Although the MonoSDF (MLP) adopts pure MLP structure which shows robustness to the camera noise, the training time of such a variant gets much longer ...
- **p. 12 / 4 Experiments - extractive body cue:** 4: Reconstructed surface by ablating proposed components on Replica [44].

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 9 (3 Method), p. 10 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 9 (3 Method), p. 7 (3 Method), objective p. 9 (3 Method), p. 9 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 6 (3 Method), temporal p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 10 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
