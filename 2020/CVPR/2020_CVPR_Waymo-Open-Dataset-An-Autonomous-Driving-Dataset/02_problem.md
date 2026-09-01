# Problem - Waymo Open Dataset: An Autonomous Driving Dataset

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.04838; PDF retrieval source: https://arxiv.org/pdf/1912.04838. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): We demonstrate that the differences in these geographies lead to a pronounced domain gap, enabling exciting research opportunities in the field of domain adaptation.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The research community has increasing interest in autonomous driving research, despite the resource intensity of obtaining representative real world data.
- **p. 1 / Abstract - extractive PDF cue:** Existing selfdriving datasets are limited in the scale and variation of the environments they capture, even though generalization within and between operating regions is crucial ...
- **p. 1 / Abstract - extractive PDF cue:** In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.
- **p. 1 / Abstract - extractive PDF cue:** Our new dataset consists of 1150 scenes that each span 20 seconds, consisting of well synchronized and calibrated high quality LiDAR and camera data captured ...
- **p. 1 / Abstract - extractive PDF cue:** It is 15x more diverse than the largest camera+LiDAR dataset available based on our proposed geographical coverage metric.
- **p. 1 / 1. Introduction - extractive PDF cue:** We demonstrate that the differences in these geographies lead to a pronounced domain gap, enabling exciting research opportunities in the field of domain adaptation.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We demonstrate that the differences in these geographies lead to a pronounced domain gap, enabling exciting research opportunities in the field of ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Detection methods may use data from any of the LiDAR and camera sensors; they may also choose to leverage sensor inputs from ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | Detection, methods, data, LiDAR, camera, sensors, they, choose, leverage, sensor | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | present, benchmark, several, state-of-the-art, D-and, object, detection, tracking | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Detection, methods, data, LiDAR, camera, sensors, they, choose, leverage, sensor | p. 5 (4.1. Object Detection), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | method trajectory/action; body terms: effort, help, align, research, community, contributions, real-world, selfdriving | p. 1 (Abstract), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: minimize, difference, between, solving, single, variable, convex, quadratic | p. 3 (3.2. Coordinate Systems), p. 5 (4.1. Object Detection), p. 5 (4.1. Object Detection) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1. Introduction), p. 2 (3.1. Sensor Specifications), p. 4 (3.4. Sensor Data) |
| Success / guarantee | comparable score and protocol validity | p. 7 (5.2. Baselines for Multi-Object Tracking), p. 7 (5.1. Baselines for Object Detection), p. 6 (5. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.
- **p. 2 / 1. Introduction - extractive PDF cue:** Selecting the test set scenes from a geographical holdout area allows us to evaluate how well models that were trained on our dataset generalize to ...

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.

- **p. 1 / 1. Introduction - extractive PDF cue:** To further accelerate the development of autonomous driving technology, we present the largest and most diverse multimodal autonomous driving dataset to date, comprising of images ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We present benchmark results of several state-of-the-art 2D-and 3D object detection and tracking methods on the dataset.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Our experiments suggest that a highly elongated low-intensity return is a strong indicator for a spurious object, while ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This result does not hold when evaluating on SF. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (4.1. Object Detection), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Sensor Data). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (4.1. Object Detection), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Sensor Data), objective p. 3 (3.2. Coordinate Systems), p. 5 (4.1. Object Detection), p. 5 (4.1. Object Detection).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
