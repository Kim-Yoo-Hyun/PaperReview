# Problem - ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1702.04405; PDF retrieval source: https://arxiv.org/pdf/1702.04405. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): Typically, 3D deep learning methods use synthetic data to mitigate this lack of real-world data [91, 6].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** A key requirement for leveraging supervised deep learning methods is the availability of large, labeled datasets.
- **p. 1 / Abstract - extractive PDF cue:** Unfortunately, in the context of RGB-D scene understanding, very little data is available - current datasets cover a small range of scene views and have ...
- **p. 1 / Abstract - extractive PDF cue:** To address this issue, we introduce ScanNet, an RGB-D video dataset containing 2.5M views in 1513 scenes annotated with 3D camera poses, surface reconstructions, and ...
- **p. 1 / Abstract - extractive PDF cue:** To collect this data, we designed an easy-to-use and scalable RGB-D capture system that includes automated surface reconstruction and crowdsourced semantic annotation.
- **p. 1 / Abstract - extractive PDF cue:** We show that using this data helps achieve state-of-the-art performance on several 3D scene understanding tasks, including 3D object classification, semantic voxel labeling, and CAD ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Typically, 3D deep learning methods use synthetic data to mitigate this lack of real-world data [91, 6].
- **p. 1 / 1. Introduction - extractive PDF cue:** Thus, many of the current RGB-D datasets [74, 92, 77, 32] are orders of magnitude smaller than their 2D counterparts.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Typically, 3D deep learning methods use synthetic data to mitigate this lack of real-world data [91, 6]. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | For each input scan, we first run BundleFusion [12] at a voxel resolution of 1 cm3. | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | input, scan, first, BundleFusion, voxel, resolution, chose, system, designed, evaluated | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Thus, existing, datasets, often, fall, back, polygon, bounding | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: input, scan, first, BundleFusion, voxel, resolution, chose, system, designed, evaluated | p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), p. 1 (1. Introduction) |
| Decision / output variable | method trajectory/action; body terms: introduce, ScanNet, dataset, richlyannotated, RGB-D, scans, real-world, environments | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Surface Reconstruction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: annotation, progress, gray, regions, indicating, unannotated, surfaces | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Surface Reconstruction) |
| Success / guarantee | comparable score and protocol validity | p. 7 (5.1. 3D Object Classification), p. 7 (5.1. 3D Object Classification), p. 8 (5.2. Semantic Voxel Labeling) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Thus, many of the current RGB-D datasets [74, 92, 77, 32] are orders of magnitude smaller than their 2D counterparts.

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction)): In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 distinct spaces.

- **p. 1 / 1. Introduction - extractive PDF cue:** In the collection of this dataset, we have considered two main research questions: 1) how can we design a framework that allows many people to ...
- **p. 4 / 3.2. Surface Reconstruction - extractive PDF cue:** This allows us to select the floor plane based on the scan bounding box and the normal most similar to the IMU up vector direction.
- **p. 4 / 3.2. Surface Reconstruction - extractive PDF cue:** We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We demonstrated that the richlyannotated scan data collected so far in ScanNet is useful in achieving state-of-the-art performance ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | This feature was critical for providing intuition to users who are not familiar with the constraints and limitations ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | The main limitation of this interface is due to the mismatch between the corpus of available CAD models ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), p. 1 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), p. 1 (1. Introduction), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
