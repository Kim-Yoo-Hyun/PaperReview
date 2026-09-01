# Problem - nuScenes: A Multimodal Dataset for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1903.11027; PDF retrieval source: https://arxiv.org/pdf/1903.11027. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1.1. Contributions), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1.1. Contributions)): From the complexities of the multimodal 3D detection challenge, and the limitations of current AV datasets, a large-scale multimodal dataset with 360◦coverage across all vision and range sensors collected from ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Robust detection and tracking of objects is crucial for the deployment of autonomous vehicle technology.
- **p. 1 / Abstract - extractive PDF cue:** Image based benchmark datasets have driven development in computer vision tasks such as object detection, tracking and segmentation of agents in the environment.
- **p. 1 / Abstract - extractive PDF cue:** Most autonomous vehicles, however, carry a combination of cameras and range sensors such as lidar and radar.
- **p. 1 / Abstract - extractive PDF cue:** As machine learning based methods for detection and tracking become more prevalent, there is a need to train and evaluate such methods on datasets containing ...
- **p. 1 / Abstract - extractive PDF cue:** In this work we present nuTonomy scenes (nuScenes), the first dataset to carry the full autonomous vehicle sensor suite: 6 cameras, 5 radars and 1 ...
- **p. 2 / 1.1. Contributions - extractive PDF cue:** From the complexities of the multimodal 3D detection challenge, and the limitations of current AV datasets, a large-scale multimodal dataset with 360◦coverage across all vision ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Since the three sensor types have different failure modes during difficult conditions, the joint treatment of sensor data is essential for agent detection and tracking.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | From the complexities of the multimodal 3D detection challenge, and the limitations of current AV datasets, a large-scale multimodal dataset with 360◦coverage ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Still, to the best of our knowledge, no other 3D dataset provides attribute annotations, such as pedestrian pose or vehicle state. | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | Still, best, knowledge, other, dataset, provides, attribute, annotations, pedestrian, pose | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | provides, boxes, over, scenes, helped, advance, state-of-the-art, object | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Still, best, knowledge, other, dataset, provides, attribute, annotations, pedestrian, pose | p. 2 (1. Introduction), p. 2 (1.1. Contributions), p. 3 (1.2. Related datasets) |
| Decision / output variable | method trajectory/action; body terms: second, contribution, detection, tracking, metrics, aimed, application, enables | p. 2 (1.1. Contributions), p. 2 (1.1. Contributions), p. 1 (Abstract) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Operating, points, where, recall, precision, less, removed, order | p. 6 (3.2. Tracking), p. 4 (2. The nuScenes dataset), p. 6 (3.1. Detection) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (2. The nuScenes dataset), p. 5 (2. The nuScenes dataset), p. 6 (3.2. Tracking) |
| Success / guarantee | comparable score and protocol validity | p. 15 (Figure/Table caption), p. 8 (4.2. Analysis), p. 7 (4.2. Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Since the three sensor types have different failure modes during difficult conditions, the joint treatment of sensor data is essential for agent detection and tracking.
- **p. 1 / 1. Introduction - extractive PDF cue:** While there is a plethora of image datasets for this purpose (Table 1), there is a lack of multimodal datasets that exhibit the full set ...
- **p. 2 / 1.1. Contributions - extractive PDF cue:** We also present and analyze the results of the nuScenes object detection and tracking challenges.

## What the Paper Changes

PDF contribution framing (p. 2 (1.1. Contributions), p. 2 (1.1. Contributions), p. 1 (Abstract), p. 1 (1. Introduction)): Our second contribution is new detection and tracking metrics aimed at the AV application.

- **p. 2 / 1.1. Contributions - extractive PDF cue:** It enables research on multiple tasks such as object detection, tracking and behavior modeling in a range of conditions.
- **p. 1 / Abstract - extractive PDF cue:** In this work we present nuTonomy scenes (nuScenes), the first dataset to carry the full autonomous vehicle sensor suite: 6 cameras, 5 radars and 1 ...
- **p. 1 / 1. Introduction - extractive PDF cue:** At the bottom we show the human written scene description.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Future work will add image-level and pointlevel semantic labels and a benchmark for trajectory prediction [63]. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | From a large body of training data we manually select 84 logs with 15h of driving data (242km ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | This method is very robust and we achieve localization errors of ≤10cm. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | As expected, when using IOU matching, small objects like pedestrians and bicycles fail to achieve above 0 AP, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 2 (1.1. Contributions), p. 3 (1.2. Related datasets), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1.1. Contributions), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1.1. Contributions), interface p. 2 (1. Introduction), p. 2 (1.1. Contributions), p. 3 (1.2. Related datasets), p. 1 (1. Introduction), objective p. 6 (3.2. Tracking), p. 4 (2. The nuScenes dataset), p. 6 (3.1. Detection).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
