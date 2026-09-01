# Problem - PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Some recent approaches aim to bridge the gap between rendering and simulation integrating physics-based This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Recent advancements in 3D generation models have opened new possibilities for simulating dynamic 3D object movements and customizing behaviors, yet creating this content remains challenging.
- **p. 1 / Abstract - extractive PDF cue:** Current methods often require manual assignment of precise physical properties for simulations or rely on video generation models to predict them, which is computationally intensive.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we rethink the usage of multi-modal large language model (MLLM) in physics-based simulation, and present PhysSplat, a physics-based approach that efficiently endows ...
- **p. 1 / Abstract - extractive PDF cue:** We begin with detailed scene reconstruction and object-level 3D open-vocabulary segmentation, progressing to multi-view image in-painting.
- **p. 1 / Abstract - extractive PDF cue:** Inspired by human visual reasoning, we propose MLLMbased Physical Property Perception (MLLM-P3) to predict the mean physical properties of objects in a zero-shot manner.
- **p. 1 / 1. Introduction - extractive PDF cue:** Some recent approaches aim to bridge the gap between rendering and simulation integrating physics-based This ICCV paper is the Open Access version, provided by the ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, learning material physical properties from video diffusion priors is computationally expensive and time-consuming in practice.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Some recent approaches aim to bridge the gap between rendering and simulation integrating physics-based This ICCV paper is the Open Access version, ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Finally, the selected material name, image, and text description provide a structured input to the MLLM, grounding its outputs in a reliable ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Finally, selected, material, name, image, text, description, provide, structured, input | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | models, automatically, segment, objects, images, without, textual, input | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Finally, selected, material, name, image, text, description, provide, structured, input | p. 4 (4.2. MLLM-based Physical Property Perception), p. 5 (4.3. Physics-Based Dynamics), p. 3 (4.1. 3D Open-vocabulary Segmentation) |
| Decision / output variable | geometry/map/query r; body terms: only, simulate, entire, scene, much, faster, speed, priors | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Our Methodology) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Following, PhysGaussian, define, Gaussian, kernel, time-dependent, state, F_i | p. 3 (3.1. Material Point Method), p. 5 (4.3. Physics-Based Dynamics) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (4.2. MLLM-based Physical Property Perception), p. 5 (4.3. Physics-Based Dynamics), p. 5 (4.3. Physics-Based Dynamics) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (5.3. Comparison with SOTA Methods), p. 6 (5.1. Implementation Details), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** However, learning material physical properties from video diffusion priors is computationally expensive and time-consuming in practice.
- **p. 2 / 1. Introduction - extractive PDF cue:** We first segment objects with priors from foundation models [18, 22, 48].

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Our Methodology), p. 4 (4.2. MLLM-based Physical Property Perception), p. 5 (4.3. Physics-Based Dynamics)): Our method is the only one that can simulate the entire scene at a much faster speed. priors into 3D object representations using physical simulators [4, 7, 27].

- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose PhysSplat, a physics-based method that efficiently transforms static 3D objects into interactive ones capable of responding to new interactions, as ...
- **p. 3 / 4. Our Methodology - extractive PDF cue:** We propose MLLM-based Physical Property Perception (MLLM-P3) to predict the mean values of these properties (Section 4.2).
- **p. 4 / 4.2. MLLM-based Physical Property Perception - extractive PDF cue:** Inspired by human reasoning, we propose MLLM-based Physical Property Perception (MLLM-P3), which uses MLLM for open-vocabulary semantic reasoning about materials and their physical properties.
- **p. 5 / 4.3. Physics-Based Dynamics - extractive PDF cue:** To address these challenges, we propose material property distribution prediction (MPDP), and reformulate the problem from a regression task to a probability distribution estimation task.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Future work will explore to reconstruct occluded parts, further enhancing realism and expanding applications in interactive virtual experiences. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (4.2. MLLM-based Physical Property Perception), p. 5 (4.3. Physics-Based Dynamics), p. 3 (4.1. 3D Open-vocabulary Segmentation), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (4.2. MLLM-based Physical Property Perception), p. 5 (4.3. Physics-Based Dynamics), p. 3 (4.1. 3D Open-vocabulary Segmentation), p. 1 (1. Introduction), objective p. 3 (3.1. Material Point Method), p. 5 (4.3. Physics-Based Dynamics).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
