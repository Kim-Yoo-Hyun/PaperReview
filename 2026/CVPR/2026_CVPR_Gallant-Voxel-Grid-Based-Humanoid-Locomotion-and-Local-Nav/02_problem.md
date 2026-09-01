# Problem - Gallant: Voxel Grid-Based Humanoid Locomotion and Local Navigation across 3-D Constrained Terrains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): While recent systems have progressed from lab prototypes to real-world deployment [17, 23], ensuring operational safety remains a key challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Robust humanoid locomotion requires accurate and globally consistent perception of the surrounding 3D environment.
- **p. 1 / Abstract - extractive PDF cue:** However, existing perception modules, mainly based on depth images or elevation maps, offer only partial and locally flattened views of the environment, failing to capture ...
- **p. 1 / Abstract - extractive PDF cue:** This paper presents Gallant, a voxel-grid-based framework for humanoid locomotion and local navigation in 3D constrained terrains.
- **p. 1 / Abstract - extractive PDF cue:** It leverages voxelized LiDAR data as a lightweight and structured perceptual representation, and employs a z-grouped 2D CNN to map this representation to the control ...
- **p. 1 / Abstract - extractive PDF cue:** A high-fidelity LiDAR simulation that dynamically generates realistic observations is developed to support scalable, LiDAR-based training and ensure sim-to-real consistency.
- **p. 2 / 1. Introduction - extractive PDF cue:** While recent systems have progressed from lab prototypes to real-world deployment [17, 23], ensuring operational safety remains a key challenge.
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these limitations, we introduce Gallant, a voxel-grid-based perception-learning framework for humanoid locomotion and loco-navigation across 3D constrained terrains.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While recent systems have progressed from lab prototypes to real-world deployment [17, 23], ensuring operational safety remains a key challenge. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | In contrast, 3D LiDAR provides detailed scene geometry with a wide FoV, but its raw point clouds are sparse and noisy, which ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | contrast, LiDAR, provides, detailed, scene, geometry, wide, FoV, point, clouds | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | Together, components, form, fullstack, pipeline-from, data, generation, perception | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: contrast, LiDAR, provides, detailed, scene, geometry, wide, FoV, point, clouds | p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3. Method) |
| Decision / output variable | joint/whole-body action; body terms: scale, training, narrow, simulation-to-reality, simto-real, develop, LiDAR, simulation | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: objective, maximize, expected, return, PH-1, Traditional, raycasting, builds | p. 3 (3.1. Problem Formulation), p. 3 (3.2. Efficient LiDAR Simulation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Problem Formulation), p. 3 (3.2. Efficient LiDAR Simulation) |
| Success / guarantee | motion/task success and recovery | p. 5 (4.2.1. Metrics), p. 7 (4.3.2. Ablation), p. 7 (4.2.3. Result) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** To address these limitations, we introduce Gallant, a voxel-grid-based perception-learning framework for humanoid locomotion and loco-navigation across 3D constrained terrains.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method)): To scale training and narrow the simulation-to-reality (simto-real) gap, we develop a LiDAR simulation pipeline that models sensor noise and latency and enables realistic scanning of dynamic objects, including the ...

- **p. 2 / 1. Introduction - extractive PDF cue:** We propose voxel grid as a lightweight yet geometrypreserving representation for humanoid locomotion and loco-navigation [31] in 3D-constrained environments.
- **p. 3 / 3. Method - extractive PDF cue:** We introduce Gallant, a voxel-grid-based perceptive learning framework for humanoid locomotion and local navigation [31] in 3D constrained environments.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | 1, using only a height map as the perceptual representation for policy cannot represent multilayer structure; consequently, Only-Height-Map ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | On other terrains-especially Platforms and Stairs, previously considered unstable due to collision risk [21]-Gallant achieves high success by ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In real-world tests, a single LiDAR policy covers the ground obstacles handled by elevation-map controllers while also tackling ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3. Method), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3. Method), p. 2 (1. Introduction), objective p. 3 (3.1. Problem Formulation), p. 3 (3.2. Efficient LiDAR Simulation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
