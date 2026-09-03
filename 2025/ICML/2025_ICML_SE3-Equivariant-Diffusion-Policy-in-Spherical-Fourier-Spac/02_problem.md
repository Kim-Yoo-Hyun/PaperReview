# Problem - SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=U5nRMOs8Ed; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167962. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Diffusion Policy may struggle to attain robust 3D generalization without training on a large amount of costly human demonstrations to exhaust the possible 3D arrangements of the scene.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Diffusion Policies are effective at learning closed-loop manipulation policies from human demonstrations but generalize poorly to novel arrangements of objects in 3D space, hurting real-world ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we propose Spherical Diffusion Policy (SDP), an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene.
- **p. 1 / Abstract - extractive body cue:** Such equivariance is achieved by embedding the states, actions, and the denoising process in spherical Fourier space.
- **p. 1 / Abstract - extractive body cue:** Additionally, we employ novel spherical FiLM layers to condition the action denoising process equivariantly on the scene embeddings.
- **p. 1 / Abstract - extractive body cue:** Lastly, we propose a spherical denoising temporal U-net that achieves spatiotemporal equivariance with computational efficiency.
- **p. 1 / 1. Introduction - extractive body cue:** Diffusion Policy may struggle to attain robust 3D generalization without training on a large amount of costly human demonstrations to exhaust the possible 3D arrangements ...
- **p. 2 / 1. Introduction - extractive body cue:** The equivariance constraints lead to provable SE(3) generalization to transformed scenes.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Diffusion Policy may struggle to attain robust 3D generalization without training on a large amount of costly human demonstrations to exhaust the ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | In this section, we propose a spherical representation of the state and action for the policy. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | section, spherical, representation, state, action, policy, Diffusion, model, maps, observations | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | states, consist, camera, observation, images, voxels, point, clouds | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: section, spherical, representation, state, action, policy, Diffusion, model, maps, observations | p. 4 (4.2. Representing State and Action by Spherical Signal), p. 4 (4.1. Method Overview), p. 2 (2. Background) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, novel, Spherical, Diffusion, Policy, equivariant, rotations, invariant | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: mixing, channel, temporal, convolution, Equation, There, several, advantages | p. 5 (4.3. Spherical Denoising Temporal U-net) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.3. Spherical Denoising Temporal U-net), p. 4 (4.2. Representing State and Action by Spherical Signal) |
| Success / guarantee | instruction-conditioned task success | p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments), p. 8 (5.2. Physical Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** The equivariance constraints lead to provable SE(3) generalization to transformed scenes.
- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (4.1. Method Overview), p. 4 (4.2. Representing State and Action by Spherical Signal)): The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling generalization to unseen scenes, 2. ...

- **p. 1 / 1. Introduction - extractive body cue:** We propose Spherical Diffusion Policy (SDP), a Fourier space SE(3) equivariant method that automatically adapts to changes in the scene.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, our method is light and SE(3) equivariant across multiple objects, allowing it to perform more complicated tasks with less engineering.
- **p. 4 / 4.1. Method Overview - extractive body cue:** Additionally, we propose bi-manual relative action representation.
- **p. 4 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** In this section, we propose a spherical representation of the state and action for the policy.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Another limitation is the lowresolution point cloud processing in the observation encoder, which struggles to capture fine details, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2. Method overview. During inference, SDP first embeds state St into a spherical scene feature Ct by ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 3. Spherical denoising temporal U-net (SDTU). Left: The SDTU ϵθ estimates the noise ϵ, based on the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4.2. Representing State and Action by Spherical Signal), p. 4 (4.1. Method Overview), p. 2 (2. Background), p. 2 (2. Background). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (4.2. Representing State and Action by Spherical Signal), p. 4 (4.1. Method Overview), p. 2 (2. Background), p. 2 (2. Background), objective p. 5 (4.3. Spherical Denoising Temporal U-net).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
