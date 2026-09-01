# Method - CraftsMan3D: High-fidelity Mesh Generation with 3D Native Diffusion and Interactive Geometry Refiner

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Multi-view guided 3D generation model), p. 5 (3.2. Multi-view guided 3D generation model), p. 4 (3.1. Data Preprocessing), p. 5 (3.3. Normal-based Geometry Refinement), p. 3 (3. Method), p. 3 (3. Method)): The encoder is trained to map points Pc and Pn into a latent vector set Z, which a decoder then translates into an implicit field representation.

## Method Body Digest

- **p. 4 / 3.2. Multi-view guided 3D generation model - extractive PDF cue:** The encoder is trained to map points Pc and Pn into a latent vector set Z, which a decoder then translates into an implicit field ...
- **p. 5 / 3.2. Multi-view guided 3D generation model - extractive PDF cue:** (a.) We first train a 3D Variational Autoencoder (VAE) to compress 3D shape into a latent space, which takes point clouds with normals as input ...
- **p. 4 / 3.1. Data Preprocessing - extractive PDF cue:** The generated multi-view image is then fed into our Latent Set-based DiT model as conditioning to produce a coarse mesh.
- **p. 5 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** To further enhance the coarse mesh, we propose to improve the initial mesh using normal maps as an intermediate representation.
- **p. 3 / 3. Method - extractive PDF cue:** Following this, we train a Variational Auto-Encoder (VAE) on the watertight meshes to learn latent set-based representations[61] and output a TSDF field.
- **p. 3 / 3. Method - extractive PDF cue:** Next, we train a dedicated DiT-based denoising network that operates on these learned latent representations, using the intermediate multi-view image as conditioning (Sec.3.2).
- **p. 6 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** Then in every optimization step, we regularize the deformation process by x \ gets x + \lambda v (\mathbf {W} V-V^\mathbf {W}_{init}), (6) Table 1.
- **p. 5 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** In each step, an update operation is executed to update the position for each vertex according to the gradient computed in the loss backward process.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Built on the 3D data, we present a two-stage generative 3D native generation system, coined CraftsMan, which takes as input single images as reference or ...
- **p. 3 / 3. Method - extractive PDF cue:** Finally, our framework features a normal map-based geometry refinement scheme (Sec.3.3).
- **p. 3 / 3.1. Data Preprocessing - extractive PDF cue:** Therefore, we propose an efficient and effective method for converting mesh into a watertight one.

## Source Evidence Cues

- **p. 4 / 3.2. Multi-view guided 3D generation model - extractive PDF cue:** The encoder is trained to map points Pc and Pn into a latent vector set Z, which a decoder then translates into an implicit field ...
- **p. 5 / 3.2. Multi-view guided 3D generation model - extractive PDF cue:** (a.) We first train a 3D Variational Autoencoder (VAE) to compress 3D shape into a latent space, which takes point clouds with normals as input ...
- **p. 4 / 3.1. Data Preprocessing - extractive PDF cue:** The generated multi-view image is then fed into our Latent Set-based DiT model as conditioning to produce a coarse mesh.
- **p. 5 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** To further enhance the coarse mesh, we propose to improve the initial mesh using normal maps as an intermediate representation.
- **p. 3 / 3. Method - extractive PDF cue:** Following this, we train a Variational Auto-Encoder (VAE) on the watertight meshes to learn latent set-based representations[61] and output a TSDF field.
- **p. 3 / 3. Method - extractive PDF cue:** Next, we train a dedicated DiT-based denoising network that operates on these learned latent representations, using the intermediate multi-view image as conditioning (Sec.3.2).
- **p. 6 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** Then in every optimization step, we regularize the deformation process by x \ gets x + \lambda v (\mathbf {W} V-V^\mathbf {W}_{init}), (6) Table 1.
- **Detected method headings:** 2.2. 3D Native Generative Models (p. 3); 3. Method (p. 3); 3.2. Multi-view guided 3D generation model (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | The encoder is trained to map points Pc and Pn into a latent vector set Z, which a decoder then translates into ... | p. 4 (3.2. Multi-view guided 3D generation model), p. 5 (3.2. Multi-view guided 3D generation model) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | (a.) We first train a 3D Variational Autoencoder (VAE) to compress 3D shape into a latent space, which takes point clouds with ... | p. 5 (3.2. Multi-view guided 3D generation model), p. 4 (3.1. Data Preprocessing) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | The generated multi-view image is then fed into our Latent Set-based DiT model as conditioning to produce a coarse mesh. | p. 4 (3.1. Data Preprocessing), p. 5 (3.3. Normal-based Geometry Refinement) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** In each step, an update operation is executed to update the position for each vertex according to the gradient computed in the loss backward process.
- **p. 3 / 3. Method - extractive PDF cue:** In this section, We begin by introducing our data preprocessing (Sec.3.1), which significantly improves the success rate of watertight conversion and maximizes the utilization of ...
- **p. 4 / 3.1. Data Preprocessing - extractive PDF cue:** In particular, this refinement module features two key usages, namely the automatic global refinement and interactive magic brush, that contribute to efficient and controllable 3D ...
- **p. 5 / 3.2. Multi-view guided 3D generation model - extractive PDF cue:** To reduce the number of parameters and computational cost, we employ adaLN-single [4] in each DiT block.
- **p. 6 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** Relative Laplacian Smoothing Previous methods [39] often achieve stable optimization by introducing Laplace regularization term.
- **p. 6 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** Then in every optimization step, we regularize the deformation process by x \ gets x + \lambda v (\mathbf {W} V-V^\mathbf {W}_{init}), (6) Table 1.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (3.3. Normal-based Geometry Refinement), p. 5 (3.3. Normal-based Geometry Refinement).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | first, train, Variational, Autoencoder, VAE, compress, shape, latent, space, takes, point, clouds, normals, input | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | first, train, Variational, Autoencoder, VAE, compress, shape, latent, space, takes | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | Built, data, present, two-stage, generative, native, generation, system, coined, CraftsMan | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | step, update, operation, executed, position, vertex, according, gradient, computed, loss | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.2. Multi-view guided 3D generation model - extractive PDF cue:** (a.) We first train a 3D Variational Autoencoder (VAE) to compress 3D shape into a latent space, which takes point clouds with normals as input ...
- **p. 4 / 3.1. Data Preprocessing - extractive PDF cue:** When the input point cloud has well-defined normals, the winding number can reliably differentiate between the inside and outside in a global manner.
- **p. 4 / 3.1. Data Preprocessing - extractive PDF cue:** We first using a multi-view diffusion model to generate a multi-view image from the input single image or text prompt.
- **p. 5 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** Formally, during the diffuse process, for the ith view with a rendered normal map ni, we replace the K and V in the original attention ...
- **p. 6 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** Quantitative comparison on subset which contained selfocclusion in the input images.
- **p. 6 / 3.3. Normal-based Geometry Refinement - extractive PDF cue:** Normal maps enhanced by stable diffusion contain low-frequency changes from original normal map(shown in red in (a)), which will result in global distortion of input ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Built on the 3D data, we present a two-stage generative 3D native generation system, coined CraftsMan, which takes as input single images as reference or ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | (b.) With the learned latent space, we train a 3D Latent Set DiT Model that using multi-view images as conditions. where ϵθ ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | Finally, our framework features a normal map-based geometry refinement scheme (Sec.3.3). | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Multi-view guided 3D generation model - extractive PDF cue:** The encoder is trained to map points Pc and Pn into a latent vector set Z, which a decoder then translates into an implicit field ...
- **p. 5 / 3.2. Multi-view guided 3D generation model - extractive PDF cue:** (a.) We first train a 3D Variational Autoencoder (VAE) to compress 3D shape into a latent space, which takes point clouds with normals as input ...
- **p. 3 / 3. Method - extractive PDF cue:** Following this, we train a Variational Auto-Encoder (VAE) on the watertight meshes to learn latent set-based representations[61] and output a TSDF field.
- **p. 3 / 3. Method - extractive PDF cue:** Next, we train a dedicated DiT-based denoising network that operates on these learned latent representations, using the intermediate multi-view image as conditioning (Sec.3.2).
- **p. 3 / 3. Method - extractive PDF cue:** Following this, we train a Variational Auto-Encoder (VAE) on the watertight meshes to learn latent set-based representations[61] and output a TSDF field.
- **p. 4 / 3.2. Multi-view guided 3D generation model - extractive PDF cue:** The encoder is trained to map points Pc and Pn into a latent vector set Z, which a decoder then translates into an implicit field ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** encoder, trained, points, latent, vector, decoder, then, translates, implicit, field, representation, first, train, Variational, Autoencoder, VAE, compress, shape, space, takes.
- **Relevant PDF headings:** 2.2. 3D Native Generative Models (p. 3); 3. Method (p. 3); 3.2. Multi-view guided 3D generation model (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Additional details, including dataset, training settings can be found in our supplementary. | p. 6 (4.1. Implementation Details), p. 7 (4.2. Evaluation of Mesh Generation) |
| Denoiser / vector field | We present the qualitative and quantitative evaluation of our method as described in Section 4.2 and Section 3.3, as well as comparison ... | p. 6 (4. Experiments), p. 7 (4.1. Implementation Details) |
| Sampling / downstream interface | As shown in Table 4, our approach achieved the best performance. | p. 8 (4.4. Ablation Study), p. 8 (4.3. Evaluation of Mesh Refinement) |

## Failure and Ablation Link

- **p. 6 / 4. Experiments - extractive PDF cue:** We also conduct ablation studies to validate the effectiveness of each component in our framework, as described in Section 4.4.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** We conduct comprehensive ablation studies to substantiate the effectiveness of each design element within our workflow, showing the importance of each component in the generation ...
- **p. 8 / 4.3. Evaluation of Mesh Refinement - extractive PDF cue:** The visual results presented in Figure 9 demonstrate that our mesh refinement technique outperforms previous methods, producing not only clear and coherent outcomes but also ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. The illustration of surface normal-based geometry re- finement. (a) The normal-adapted diffusion model is combined with ControlNet-Tile to enhance a normal with intricate ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Error maps of different mesh-to-sdf methods. We sample surface points from the processed meshes for each method and show the differences compared to ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative comparison on subset which contained self- occlusion in the input images. Our 3D generative model demon- strated a significant performance.
- **p. 7 / 4.2. Evaluation of Mesh Generation - extractive PDF cue:** We notice that the distribution of the GSO dataset is kind of monotonous,lacking mesh with complex structures and self occlusion, which is exactly where our ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Multi-view guided 3D generation model), p. 5 (3.2. Multi-view guided 3D generation model), p. 4 (3.1. Data Preprocessing), p. 5 (3.3. Normal-based Geometry Refinement), p. 3 (3. Method), p. 3 (3. Method), objective p. 5 (3.3. Normal-based Geometry Refinement), p. 3 (3. Method), p. 4 (3.1. Data Preprocessing), p. 5 (3.2. Multi-view guided 3D generation model), p. 6 (3.3. Normal-based Geometry Refinement), p. 6 (3.3. Normal-based Geometry Refinement), temporal p. 5 (3.2. Multi-view guided 3D generation model), p. 3 (3. Method), p. 3 (3. Method), p. 5 (3.3. Normal-based Geometry Refinement), p. 6 (4. Experiments), p. 6 (4. Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
