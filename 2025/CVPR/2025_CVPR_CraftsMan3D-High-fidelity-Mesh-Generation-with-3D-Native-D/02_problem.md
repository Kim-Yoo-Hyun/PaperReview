# Problem - CraftsMan3D: High-fidelity Mesh Generation with 3D Native Diffusion and Interactive Geometry Refiner

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, none of these methods can generate high-fidelity geometric details and limitations in mesh-to-SDF conversions still result in training difficulty.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present a novel generative 3D modeling system, coined CraftsMan3D, which can generate high-fidelity 3D geometries with highly varied shapes, detailed surfaces, and, notably, allows ...
- **p. 1 / Abstract - extractive body cue:** Despite the significant advancements in 3D generation, existing methods still struggle with lengthy optimization processes, self-occlusion, irregular mesh topologies, and difficulties in accommodating user editing, ...
- **p. 1 / Abstract - extractive body cue:** Our work is inspired by the craftsman, who usually roughs out the holistic figure of the work first and elaborates the surface details subsequently.
- **p. 1 / Abstract - extractive body cue:** Specifically, we first introduce a robust data preprocessing pipeline that utilizes visibility check and winding mumber to maximize the use of existing 3D data.
- **p. 1 / Abstract - extractive body cue:** Leveraging this data, we employ a 3D-native DiT model that directly models the distribution of 3D data in latent space, generating coarse geometries in seconds.
- **p. 2 / 1. Introduction - extractive body cue:** However, none of these methods can generate high-fidelity geometric details and limitations in mesh-to-SDF conversions still result in training difficulty.
- **p. 1 / 1. Introduction - extractive body cue:** However, existing methods still struggle to produce results that are ready to use.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, none of these methods can generate high-fidelity geometric details and limitations in mesh-to-SDF conversions still result in training difficulty. | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | (a.) We first train a 3D Variational Autoencoder (VAE) to compress 3D shape into a latent space, which takes point clouds with ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF body |
| State / latent | first, train, Variational, Autoencoder, VAE, compress, shape, latent, space, takes | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | first, multi-view, diffusion, model, generate, image, input, single | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: first, train, Variational, Autoencoder, VAE, compress, shape, latent, space, takes | p. 5 (3.2. Multi-view guided 3D generation model), p. 4 (3.1. Data Preprocessing), p. 4 (3.1. Data Preprocessing) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: Built, data, present, two-stage, generative, native, generation, system | p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3.1. Data Preprocessing) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: step, update, operation, executed, position, vertex, according, gradient | p. 5 (3.3. Normal-based Geometry Refinement), p. 5 (3.3. Normal-based Geometry Refinement) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.2. Multi-view guided 3D generation model), p. 6 (3.3. Normal-based Geometry Refinement), p. 6 (3.3. Normal-based Geometry Refinement) |
| Success / guarantee | sample quality, diversity and latency | p. 8 (4.4. Ablation Study), p. 7 (4.2. Evaluation of Mesh Generation), p. 8 (4.2. Evaluation of Mesh Generation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** However, existing methods still struggle to produce results that are ready to use.
- **p. 2 / 1. Introduction - extractive body cue:** Challenges of scaling up native 3D generative models largely due to the uniform requirement of training data.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3.1. Data Preprocessing), p. 5 (3.3. Normal-based Geometry Refinement), p. 2 (1. Introduction)): Built on the 3D data, we present a two-stage generative 3D native generation system, coined CraftsMan, which takes as input single images as reference or text prompts and generates high-fidelity ...

- **p. 3 / 3. Method - extractive body cue:** Finally, our framework features a normal map-based geometry refinement scheme (Sec.3.3).
- **p. 3 / 3.1. Data Preprocessing - extractive body cue:** Therefore, we propose an efficient and effective method for converting mesh into a watertight one.
- **p. 5 / 3.3. Normal-based Geometry Refinement - extractive body cue:** To further enhance the coarse mesh, we propose to improve the initial mesh using normal maps as an intermediate representation.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contribution lies in three aspects: • A robust and efficient data pre-processing pipeline that integrates visibility checks enhanced by the winding ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Figure 3. Error maps of different mesh-to-sdf methods. We sample surface points from the processed meshes for each ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Table 2. Quantitative comparison on subset which contained self- occlusion in the input images. Our 3D generative model ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We notice that the distribution of the GSO dataset is kind of monotonous,lacking mesh with complex structures and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our proposed regularization terms eliminate the global distortions introduced in the detail enhancement process by normal stable diffusion, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.2. Multi-view guided 3D generation model), p. 4 (3.1. Data Preprocessing), p. 4 (3.1. Data Preprocessing), p. 5 (3.3. Normal-based Geometry Refinement). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (3.2. Multi-view guided 3D generation model), p. 4 (3.1. Data Preprocessing), p. 4 (3.1. Data Preprocessing), p. 5 (3.3. Normal-based Geometry Refinement), objective p. 5 (3.3. Normal-based Geometry Refinement), p. 5 (3.3. Normal-based Geometry Refinement).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
