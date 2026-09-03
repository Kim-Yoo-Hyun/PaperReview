# Problem - S3E: A Multi-Robot Multimodal Dataset for Collaborative SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.13723; PDF retrieval source: https://arxiv.org/pdf/2210.13723. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract), p. 4 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 2 (3 UGVs)): Despite this interest, the scalability and diversity of existing datasets for collaborative trajectories remain limited, especially in scenarios with constrained perspectives where the generalization capabilities of Collaborative SLAM ( ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** The burgeoning demand for collaborative robotic systems to execute complex tasks collectively has intensified the research community's focus on advancing simultaneous localization and mapping (SLAM) ...
- **p. 1 / Abstract - extractive body cue:** Despite this interest, the scalability and diversity of existing datasets for collaborative trajectories remain limited, especially in scenarios with constrained perspectives where the generalization capabilities ...
- **p. 1 / Abstract - extractive body cue:** Addressing this gap, we introduce S3E, an expansive multimodal dataset.
- **p. 1 / Abstract - extractive body cue:** Captured by a fleet of unmanned ground vehicles traversing four distinct collaborative trajectory paradigms, S3E encompasses 13 outdoor and 5 indoor sequences.
- **p. 1 / Abstract - extractive body cue:** These sequences feature meticulously synchronized and spatially calibrated data streams, including 360-degree LiDAR point cloud, high-resolution stereo imagery, high-frequency inertial measurement units (IMU), and Ultrawideband ...
- **p. 4 / III. S3E DATASET - extractive body cue:** Playground: Open spaces with fewer obstructions challenge feature extraction and optimization.
- **p. 4 / III. S3E DATASET - extractive body cue:** Teaching Building and Tunnel: Poor lighting and similar geometric structures challenge robustness in maintaining

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite this interest, the scalability and diversity of existing datasets for collaborative trajectories remain limited, especially in scenarios with constrained perspectives where ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | These sequences feature meticulously synchronized and spatially calibrated data streams, including 360-degree LiDAR point cloud, high-resolution stereo imagery, high-frequency inertial measurement units ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | sequences, feature, meticulously, synchronized, spatially, calibrated, data, streams, including, degree | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | integration, allows, high-frequency, positioning, data, output, even, during | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: sequences, feature, meticulously, synchronized, spatially, calibrated, data, streams, including, degree | p. 1 (Abstract), p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET) |
| Decision / output variable | method trajectory/action; body terms: introduce, four, trajectory, prototypes, designed, meet, principles, evaluate | p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 1 (Abstract), p. 2 (3 UGVs) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Communication, Constraints, Robots, typically, limited, sharing, information, within | p. 1 (C OLLABORATIVE Simultaneous Localization and Map) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. S3E DATASET), p. 1 (Abstract), p. 4 (III. S3E DATASET) |
| Success / guarantee | comparable score and protocol validity | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 3 (III. S3E DATASET) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** Addressing this gap, we introduce S3E, an expansive multimodal dataset.
- **p. 4 / III. S3E DATASET - extractive body cue:** Playground: Open spaces with fewer obstructions challenge feature extraction and optimization.
- **p. 4 / III. S3E DATASET - extractive body cue:** Teaching Building and Tunnel: Poor lighting and similar geometric structures challenge robustness in maintaining
- **p. 2 / 3 UGVs - extractive body cue:** This dataset is the first to incorporate UWB relative distance measurements, providing a new research dimension. ∙To assess C-SLAM's performance in environments with limited overlap, ...

## What the Paper Changes

PDF body contribution framing (p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 1 (Abstract), p. 2 (3 UGVs), p. 3 (III. S3E DATASET), p. 2 (3 UGVs)): In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse closure strategies in multi-robot operations.

- **p. 1 / Abstract - extractive body cue:** Addressing this gap, we introduce S3E, an expansive multimodal dataset.
- **p. 2 / 3 UGVs - extractive body cue:** In conclusion, our work makes several key contributions to the field: ∙We have created a cutting-edge C-SLAM dataset using three ground robots, each equipped with ...
- **p. 3 / III. S3E DATASET - extractive body cue:** This includes the sensor types, their resolution, measurement range, accuracy, and any other pertinent technical details that define their contribution to the SLAM system's performance.
- **p. 2 / 3 UGVs - extractive body cue:** In the right part, our mobile platforms are available in two versions, each designed for different operational requirements.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | If inter-loop closures detection fails, we mark it "Failed". | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Our experiments using this dataset have highlighted the improved robustness of C-SLAM systems, especially in handling inter-loop closures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Sensor Configuration Our S3E dataset encompasses a multimodal array of sensors, each selected for its operational range and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Teaching Building and Tunnel: Poor lighting and similar geometric structures challenge robustness in maintaining | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), p. 4 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 2 (3 UGVs), interface p. 1 (Abstract), p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), objective p. 1 (C OLLABORATIVE Simultaneous Localization and Map).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
