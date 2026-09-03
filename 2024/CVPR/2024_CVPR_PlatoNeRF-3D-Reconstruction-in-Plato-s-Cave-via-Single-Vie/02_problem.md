# Problem - PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Notations and Problem Definition)): While promising, a limitation of existing methods is generalization to the lower spatial- and temporal-resolutions of lidars found on consumer devices.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D reconstruction from a single-view is challenging because of the ambiguity from monocular cues and lack of information about occluded regions.
- **p. 1 / Abstract - extractive body cue:** Neural radiance fields (NeRF), while popular for view synthesis and 3D reconstruction, are typically reliant on multi-view images.
- **p. 1 / Abstract - extractive body cue:** Existing methods for single-view 3D reconstruction with NeRF rely on either data priors to hallucinate views of occluded regions, which may not be physically accurate, ...
- **p. 1 / Abstract - extractive body cue:** We propose using time-offlight data captured by a single-photon avalanche diode to overcome these limitations.
- **p. 1 / Abstract - extractive body cue:** Our method models two-bounce optical paths with NeRF, using lidar transient data for supervision.
- **p. 2 / 1. Introduction - extractive body cue:** While promising, a limitation of existing methods is generalization to the lower spatial- and temporal-resolutions of lidars found on consumer devices.
- **p. 1 / 1. Introduction - extractive body cue:** However, these methods struggle when the shadow is difficult to detect, such as in ambient light or low albedo backgrounds.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While promising, a limitation of existing methods is generalization to the lower spatial- and temporal-resolutions of lidars found on consumer devices. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Because l is modeled as a point light source, we neglect any diffraction effects and soft shadows that are common with area ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Because, modeled, point, light, source, neglect, diffraction, effects, soft, shadows | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Approaches, diffusion, generative, adversarial, networks, transformers, rely, data | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Because, modeled, point, light, source, neglect, diffraction, effects, soft, shadows | p. 3 (3.1. Notations and Problem Definition), p. 5 (3.3. Implementation Details), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: consists, three, steps, Furthermore, lidar, allows, operate, higher | p. 4 (3.1. Notations and Problem Definition), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: After, iterations, when, accurate, initial, estimate, virtual, detector | p. 5 (3.3. Implementation Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Implementation Details), p. 5 (3.3. Implementation Details) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.2. Results), p. 7 (4.3. Ablations), p. 8 (4.3. Ablations) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** However, these methods struggle when the shadow is difficult to detect, such as in ambient light or low albedo backgrounds.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, while still enabling physically-accurate reconstruction, we propose using two-bounce light measured with lidar.
- **p. 1 / 1. Introduction - extractive body cue:** Existing methods in single-view 3D reconstruction with NeRF either rely on data priors [9, 21, 42, 47] or use visual cues, such as shadows, to ...
- **p. 3 / 3.1. Notations and Problem Definition - extractive body cue:** In this problem, we are interested in inferring 3D scene geometry from one-bounce and twobounce light, where "bounce" denotes the number of times light reflects ...

## What the Paper Changes

PDF body contribution framing (p. 4 (3.1. Notations and Problem Definition), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Notations and Problem Definition), p. 5 (3.3. Implementation Details)): Our method consists of three steps.

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, using lidar allows our method to operate with higher ambient light and lower scene albedo than RGB methods that exploit shadows.
- **p. 2 / 1. Introduction - extractive body cue:** We use this data to evaluate our method and our baselines.
- **p. 3 / 3.1. Notations and Problem Definition - extractive body cue:** The lidar system consists of a SPAD sensor and pulsed laser at known positions xs and xl respectively.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Our method requires five inputs per pixel: (1) sensor location op = xs and ray direction dp, (2) laser location xl, (3) distance from the ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Our method has a couple limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In contrast, lidar-based methods, such as PlatoNeRF, are fundamentally more robust to these low signal-to-noise (SNR) and signal-to-background ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | First, we introduce the simulated datasets that we make available to accelerate future work in learning-based methods for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In general, PlatoNeRF produces smoother depth, but small floaters are noticeable, especially in the nearby floor region, which ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Notations and Problem Definition), p. 5 (3.3. Implementation Details), p. 1 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Notations and Problem Definition), interface p. 3 (3.1. Notations and Problem Definition), p. 5 (3.3. Implementation Details), p. 1 (1. Introduction), p. 2 (1. Introduction), objective p. 5 (3.3. Implementation Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
