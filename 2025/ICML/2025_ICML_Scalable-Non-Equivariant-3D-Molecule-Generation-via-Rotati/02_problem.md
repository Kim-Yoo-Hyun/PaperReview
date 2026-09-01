# Problem - Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=l5KpQ5MmaD; PDF retrieval source: https://openreview.net/pdf/d526a2c92e7570f45137984e599cd180fcdcf5b6.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.3. Equivariance), p. 2 (1. Introduction)): Compared with their non-equivariant counterparts, they have more complex parametrization and lack standardized implementations.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Equivariant diffusion models have achieved impressive performance in 3D molecule generation.
- **p. 1 / Abstract - extractive PDF cue:** These models incorporate Euclidean symmetries of 3D molecules by utilizing an SE(3)-equivariant denoising network.
- **p. 1 / Abstract - extractive PDF cue:** However, specialized equivariant architectures limit the scalability and efficiency of diffusion models.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose an approach that relaxes such equivariance constraints.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, our approach learns a sample-dependent SO(3) transformation for each molecule to construct an aligned latent space.
- **p. 1 / 1. Introduction - extractive PDF cue:** Compared with their non-equivariant counterparts, they have more complex parametrization and lack standardized implementations.
- **p. 1 / 1. Introduction - extractive PDF cue:** Different from data with grid-like structures (e.g., images and text sequences), 3D molecules pose unique challenges to generative modeling due to the Euclidean symmetry group ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Compared with their non-equivariant counterparts, they have more complex parametrization and lack standardized implementations. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | One EGNN layer that takes xl, hl as inputs and outputs xl+1, hl+1 is defined as: mij = ϕe(hl i, hl j, ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | One, EGNN, layer, takes, inputs, outputs, defined, eijmij, atomic, coordinates | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Given, distributions, above, Bayes, rule, derive, true, posterior | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: One, EGNN, layer, takes, inputs, outputs, defined, eijmij, atomic, coordinates | p. 3 (2.3. Equivariance), p. 4 (3.1. Aligned Latent Space), p. 2 (2.2. Diffusion Models) |
| Decision / output variable | geometry/map/query r; body terms: address, challenge, construct, aligned, representations, unsupervised, manner, autoencoder | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: above, rotation, representation, good, gradient-based, optimization, sense, SVD | p. 4 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models), p. 3 (2.2. Diffusion Models), p. 4 (3. Method), p. 5 (3.2. Non-Equivariant Latent Diffusion Model), p. 5 (3.1. Aligned Latent Space) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models), p. 3 (2.2. Diffusion Models) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.1. Experimental Setup), p. 8 (Figure/Table caption), p. 5 (4. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Different from data with grid-like structures (e.g., images and text sequences), 3D molecules pose unique challenges to generative modeling due to the Euclidean symmetry group ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address this challenge, we propose to construct aligned representations in an unsupervised manner with an autoencoder.
- **p. 3 / 2.3. Equivariance - extractive PDF cue:** As mentioned in Section 2.1, the atomic coordinates x of a molecule can be arbitrarily translated and rotated in the three-dimensional space without affecting its ...
- **p. 2 / 1. Introduction - extractive PDF cue:** As expected, our non-equivariant diffusion model exhibits better scalability and improves the sampling efficiency significantly.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Method), p. 4 (3.1. Aligned Latent Space), p. 5 (3.1. Aligned Latent Space)): To address this challenge, we propose to construct aligned representations in an unsupervised manner with an autoencoder.

- **p. 2 / 1. Introduction - extractive PDF cue:** Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment Driven by the interest in further investigating the capacity of non-equivariant diffusion models and motivated by the ...
- **p. 4 / 3. Method - extractive PDF cue:** In Section 3.1, we introduce how we learn alignment with an autoencoder.
- **p. 4 / 3.1. Aligned Latent Space - extractive PDF cue:** To overcome this, we propose to learn rotations in an unsupervised manner through an autoencoder.
- **p. 5 / 3.1. Aligned Latent Space - extractive PDF cue:** In (18) we parameterize the joint distribution of zx, zh as an isotropic Gaussian with a fixed variance σ2, which allows qθ,η(zx, zh/x, h) to ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | As for the diffusion model, we use the same noise schedule and number of time steps as EDM/GeoLDM. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | To implement DiT as the noise prediction network, we follow the official code base6 and make necessary modifications ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Specifically, we use a basic non-equivariant GNN (17) as the noise prediction network and train the diffusion model ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The nonequivariant baselines GraphLDM and GraphLDM-aug used the same GNN architecture as the noise prediction network, but were ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (2.3. Equivariance), p. 4 (3.1. Aligned Latent Space), p. 2 (2.2. Diffusion Models), p. 3 (2.2. Diffusion Models). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.3. Equivariance), p. 2 (1. Introduction), interface p. 3 (2.3. Equivariance), p. 4 (3.1. Aligned Latent Space), p. 2 (2.2. Diffusion Models), p. 3 (2.2. Diffusion Models), objective p. 4 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models), p. 3 (2.2. Diffusion Models), p. 4 (3. Method), p. 5 (3.2. Non-Equivariant Latent Diffusion Model), p. 5 (3.1. Aligned Latent Space).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
