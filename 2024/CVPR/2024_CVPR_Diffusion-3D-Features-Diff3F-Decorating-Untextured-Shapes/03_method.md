# Method - Diffusion 3D Features (Diff3F): Decorating Untextured Shapes with Distilled Semantic Features

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.2. Semantics through Painting), p. 4 (3.2. Semantics through Painting), p. 3 (3. Method), p. 4 (3.2. Semantics through Painting), p. 3 (3.1. Semantic Diffusion Features), p. 5 (3.2. Semantics through Painting)): We employ a feature fusion strategy proposed by [65], where we first normalize the features and then concatenate them as, \ma t hc al {F}^ \ t ex t it ...

## Method Body Digest

- **p. 5 / 3.2. Semantics through Painting - extractive PDF cue:** We employ a feature fusion strategy proposed by [65], where we first normalize the features and then concatenate them as, \ma t hc al {F}^ ...
- **p. 4 / 3.2. Semantics through Painting - extractive PDF cue:** We use DDIM [51] to accelerate the sampling process for Stable Diffusion [47] and use 30 inference steps.
- **p. 3 / 3. Method - extractive PDF cue:** Given the scarcity of 3D geometry data from which to learn these meaningful descriptors, we leverage foundational vision models trained on very large datasets to ...
- **p. 4 / 3.2. Semantics through Painting - extractive PDF cue:** We, therefore, condition our painting module f with geometric constraints that describe the latent 3D object.
- **p. 3 / 3.1. Semantic Diffusion Features - extractive PDF cue:** Given a shape S with vertices V ∈R3, we want to project it to the image space to distill per-point semantic 3D features from images.
- **p. 5 / 3.2. Semantics through Painting - extractive PDF cue:** We also normalize these image features as in Equation 6.
- **p. 4 / 3.1. Semantic Diffusion Features - extractive PDF cue:** We guide the texturing by providing constraints G to ControlNet [66].
- **p. 5 / 3.2. Semantics through Painting - extractive PDF cue:** FFUSE j is also unit-normalized as in Equation 6.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** We propose a simple and robust solution.
- **p. 2 / 1. Introduction - extractive PDF cue:** We present DIFFUSION 3D FEATURES (DIFF3F), a simple and practical framework for extracting semantic features that eliminates the need for additional training or optimization.
- **p. 6 / 3.4. Computing Correspondence - extractive PDF cue:** We report correspondence accuracy within 1% error tolerance, with our method against competing works.

## Source Evidence Cues

- **p. 5 / 3.2. Semantics through Painting - extractive PDF cue:** We employ a feature fusion strategy proposed by [65], where we first normalize the features and then concatenate them as, \ma t hc al {F}^ ...
- **p. 4 / 3.2. Semantics through Painting - extractive PDF cue:** We use DDIM [51] to accelerate the sampling process for Stable Diffusion [47] and use 30 inference steps.
- **p. 3 / 3. Method - extractive PDF cue:** Given the scarcity of 3D geometry data from which to learn these meaningful descriptors, we leverage foundational vision models trained on very large datasets to ...
- **p. 4 / 3.2. Semantics through Painting - extractive PDF cue:** We, therefore, condition our painting module f with geometric constraints that describe the latent 3D object.
- **p. 3 / 3.1. Semantic Diffusion Features - extractive PDF cue:** Given a shape S with vertices V ∈R3, we want to project it to the image space to distill per-point semantic 3D features from images.
- **p. 5 / 3.2. Semantics through Painting - extractive PDF cue:** We also normalize these image features as in Equation 6.
- **Detected method headings:** 3. Method (p. 3); 4.3. Baseline Methods (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | We employ a feature fusion strategy proposed by [65], where we first normalize the features and then concatenate them as, \ma t ... | p. 5 (3.2. Semantics through Painting), p. 4 (3.2. Semantics through Painting) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | We use DDIM [51] to accelerate the sampling process for Stable Diffusion [47] and use 30 inference steps. | p. 4 (3.2. Semantics through Painting), p. 3 (3. Method) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | Given the scarcity of 3D geometry data from which to learn these meaningful descriptors, we leverage foundational vision models trained on very ... | p. 3 (3. Method), p. 4 (3.2. Semantics through Painting) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Semantic Diffusion Features - extractive PDF cue:** We guide the texturing by providing constraints G to ControlNet [66].
- **p. 4 / 3.2. Semantics through Painting - extractive PDF cue:** We, therefore, condition our painting module f with geometric constraints that describe the latent 3D object.
- **p. 5 / 3.2. Semantics through Painting - extractive PDF cue:** FFUSE j is also unit-normalized as in Equation 6.
- **p. 5 / 3.2. Semantics through Painting - extractive PDF cue:** We also normalize these image features as in Equation 6.
- **p. 6 / 3.4. Computing Correspondence - extractive PDF cue:** To enable this, we pass our computed descriptors to a vanilla Functional Map [41] implementation, which returns a continuous surface-to-surface map that can then be ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 4 (3.1. Semantic Diffusion Features), p. 4 (3.2. Semantics through Painting), p. 5 (3.2. Semantics through Painting), p. 5 (3.2. Semantics through Painting).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | define, geometric, maps, applied, conditional, image, constraints, label, oreq, mathcal, S_j, where, normal, continuous | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | define, geometric, maps, applied, conditional, image, constraints, label, oreq, mathcal | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | simple, robust, solution, present, DIFFUSION, FEATURES, DIFF3F, practical, framework, extracting | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | guide, texturing, providing, constraints, ControlNet, therefore, condition, painting, module, geometric | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Semantics through Painting - extractive PDF cue:** We define G as a set of geometric maps that can be applied as conditional image constraints, \ label {e q:co l oreq} G := ...
- **p. 4 / 3.1. Semantic Diffusion Features - extractive PDF cue:** As an emergent behaviour, pre-trained foundational vision models have been found to assign distinctive semantic features [54] to pixels in the input image, to be ...
- **p. 5 / 3.3. Distilling 2D Features to 3D - extractive PDF cue:** We leverage known camera parameters to unproject features from the image space back to the points on the 3D input, i.e., \prot e c t ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The ability to extract reliable features from input meshes or point clouds paves the way for establishing shape correspondence, extracting low-dimensional shape spaces, and learning ...
- **p. 2 / 1. Introduction - extractive PDF cue:** 3D-CODED [20] DPC [30] SE-ORNet [14] FM+WKS [41] Ours No 3D training data? ✗ ✗ ✗ ✓ ✓ Unsupervised? ✗ ✓ ✓ ✓ ✓ Class ...
- **p. 2 / 1. Introduction - extractive PDF cue:** DIFF3F renders input shapes from a sampling of camera views to produce respective depth/normal maps.
- **p. 6 / 3.4. Computing Correspondence - extractive PDF cue:** The Laplace Beltrami Operator (LBO) computation for Functional Maps is unstable on TOSCA since the inputs contain non-manifold meshes.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | (4) During this texturing forward pass, we extract features Ft L from an intermediate layer L of Stable Diffusion's UNet decoder at ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | Each pixel gets a 1280 dimensional feature from the diffusion UNet, aggregated over diffusion time steps. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Semantics through Painting - extractive PDF cue:** We use DDIM [51] to accelerate the sampling process for Stable Diffusion [47] and use 30 inference steps.
- **p. 3 / 3. Method - extractive PDF cue:** Given the scarcity of 3D geometry data from which to learn these meaningful descriptors, we leverage foundational vision models trained on very large datasets to ...
- **p. 4 / 3.2. Semantics through Painting - extractive PDF cue:** We, therefore, condition our painting module f with geometric constraints that describe the latent 3D object.
- **p. 6 / 4.3. Baseline Methods - extractive PDF cue:** Note that we do not have access to pretrained 3D-CODED models for animal models.
- **p. 4 / 3.2. Semantics through Painting - extractive PDF cue:** We use DDIM [51] to accelerate the sampling process for Stable Diffusion [47] and use 30 inference steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** employ, feature, fusion, strategy, where, first, normalize, features, then, concatenate, them, FUS, alpha, mathcal, textit, Diff, Dino, tunable, parameter, experiments.
- **Relevant PDF headings:** 3. Method (p. 3); 4.3. Baseline Methods (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | For DPC and SE-ORNet, we choose SURREAL and SMAL as the training sets for human and animal shapes, respectively - these larger ... | p. 6 (4.1. Datasets and Benchmarks), p. 6 (4.1. Datasets and Benchmarks) |
| Denoiser / vector field | We outperform baseline methods by a large margin for non-isometric shapes thanks to the semantic nature of DIFF3F. | p. 7 (4.5. Evaluation on Animal Shapes), p. 7 (4.4. Evaluation on Human Shapes) |
| Sampling / downstream interface | Our method achieves a state-of-theart correspondence accuracy of 26.41% at 1% error tolerance, an improvement of 5%. | p. 7 (4.4. Evaluation on Human Shapes), p. 7 (4.4. Evaluation on Human Shapes) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Correspondence in-the-wild. We introduce DIFF3F, a novel feature distiller that harnesses the expressive power of in- painting diffusion features and distills them to ...
- **p. 8 / 4.6. Ablations - extractive PDF cue:** Ablation SHREC'19 SHREC'20 acc ↑ err ↓ acc ↑ err ↓ w/o ControlNet (untextured) 17.20 2.04 65.48 0.69 TEXTure[46]+DINO 17.20 2.04 65.48 0.69 w/o Fusion ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation. We ablate different components of our method and compare accuracy at 1% tolerance on SHREC'19 and SHREC'20, against our full method (last ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Method overview. DIFF3F is a feature distiller to map semantic diffusion features to 3D surface points. We render the given shape without textures ...
- **p. 6 / 4.3. Baseline Methods - extractive PDF cue:** Note that we do not have access to pretrained 3D-CODED models for animal models.
- **p. 6 / 4.1. Datasets and Benchmarks - extractive PDF cue:** Train Method TOSCA SHREC'19 SHREC'20 acc ↑ err ↓ acc ↑ err ↓ acc ↑ err ↓ SURREAL DPC [30] 29.30 5.25 17.40 6.26 31.08 ...
- **p. 7 / 4.6. Ablations - extractive PDF cue:** We ablate different components of our method and report their performance.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.2. Semantics through Painting), p. 4 (3.2. Semantics through Painting), p. 3 (3. Method), p. 4 (3.2. Semantics through Painting), p. 3 (3.1. Semantic Diffusion Features), p. 5 (3.2. Semantics through Painting), objective p. 4 (3.1. Semantic Diffusion Features), p. 4 (3.2. Semantics through Painting), p. 5 (3.2. Semantics through Painting), p. 5 (3.2. Semantics through Painting), p. 6 (3.4. Computing Correspondence), temporal p. 4 (3.2. Semantics through Painting), p. 5 (3.2. Semantics through Painting), p. 5 (3.2. Semantics through Painting), p. 4 (3.2. Semantics through Painting), p. 2 (1. Introduction), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
