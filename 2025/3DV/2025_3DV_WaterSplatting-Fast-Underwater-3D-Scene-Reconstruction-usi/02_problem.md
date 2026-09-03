# Problem - WaterSplatting: Fast Underwater 3D Scene Reconstruction using Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=Z9yn9YgNIz&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract)): The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences.
- **p. 1 / Abstract - extractive body cue:** The problem was successfully tackled by fully volumetric NeRF-based methods which can model both the geometry and the medium (water).
- **p. 1 / Abstract - extractive body cue:** Unfortunately, these methods are slow to train and do not offer real-time rendering.
- **p. 1 / Abstract - extractive body cue:** More recently, 3D Gaussian Splatting (3DGS) method offered a fast alternative to NeRFs.
- **p. 1 / Abstract - extractive body cue:** However, because it is an explicit method that renders only the geometry, it cannot render the medium and is therefore unsuited for underwater reconstruction.
- **p. 2 / 1. Introduction - extractive body cue:** Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Splatting with Medium: We introduce a novel approach that combines the strengths of Gaussian Splatting (GS) and volume rendering.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The input to our model is a set of images with scattering medium and corresponding camera poses. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | input, model, images, scattering, medium, corresponding, camera, poses, meantime, DGS | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | contributed, color, final, output, Cobj, iciexp, medsi, where | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: input, model, images, scattering, medium, corresponding, camera, poses, meantime, DGS | p. 3 (3.2. Splatting with Medium), p. 3 (3.1. Preliminaries), p. 4 (3.2. Splatting with Medium) |
| Decision / output variable | geometry/map/query r; body terms: Loss, Function, Alignment, novel, designed, align, DGS, human | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Splatting with Medium) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: case, DGS-based, model, regularized, loss, function, LReg, apply | p. 4 (3.3. Loss Function Alignment), p. 3 (3. Method), p. 3 (3.1. Preliminaries), p. 4 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Preliminaries), p. 5 (3.3. Loss Function Alignment), p. 3 (3. Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4. Experiments), p. 7 (4.1. Results), p. 5 (4.1. Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** The problem was successfully tackled by fully volumetric NeRF-based methods which can model both the geometry and the medium (water).

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Splatting with Medium), p. 4 (3.3. Loss Function Alignment), p. 3 (3.2. Splatting with Medium)): Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes.

- **p. 2 / 1. Introduction - extractive body cue:** Splatting with Medium: We introduce a novel approach that combines the strengths of Gaussian Splatting (GS) and volume rendering.
- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** We illustrate the pipeline of our method in Fig.
- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ...
- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** Under the occlusion of both primitives and medium, our model acquires the transmittance along the ray and is capable of synthesizing medium component and object ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Although our method achieves good reconstruction quality, there are some limitations to consider. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | However, in the foreground, our method prunes medium-role primitives well while SeaThru-NeRF cannot prevent the geometrical field from ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Limitation: insufficient supervision. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Limitation: simulating distant medium with Gaussians. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.2. Splatting with Medium), p. 3 (3.1. Preliminaries), p. 4 (3.2. Splatting with Medium), p. 4 (3.3. Loss Function Alignment). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), interface p. 3 (3.2. Splatting with Medium), p. 3 (3.1. Preliminaries), p. 4 (3.2. Splatting with Medium), p. 4 (3.3. Loss Function Alignment), objective p. 4 (3.3. Loss Function Alignment), p. 3 (3. Method), p. 3 (3.1. Preliminaries), p. 4 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
