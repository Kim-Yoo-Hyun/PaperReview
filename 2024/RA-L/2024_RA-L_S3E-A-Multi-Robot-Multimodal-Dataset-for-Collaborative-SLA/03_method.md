# Method - S3E: A Multi-Robot Multimodal Dataset for Collaborative SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.13723; PDF retrieval source: https://arxiv.org/pdf/2210.13723. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 2 (3 UGVs), p. 3 (III. S3E DATASET)): To fill this gap and enhance C-SLAM research, we introduce S3E dataset, offering a multimodal perspective with a variety of cooperative trajectory patterns in both outdoor and indoor environments.

## Method Body Digest

- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive PDF cue:** To fill this gap and enhance C-SLAM research, we introduce S3E dataset, offering a multimodal perspective with a variety of cooperative trajectory patterns in both ...
- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive PDF cue:** In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse closure strategies in ...
- **p. 3 / III. S3E DATASET - extractive PDF cue:** For synchronization across agents, we address two distinct scenarios: ∙In outdoor settings with access to Global Navigation Satellite System (GNSS) signals, we use GNSS time ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Playground: Open spaces with fewer obstructions challenge feature extraction and optimization.
- **p. 2 / 3 UGVs - extractive PDF cue:** This dataset is the first to incorporate UWB relative distance measurements, providing a new research dimension. ∙To assess C-SLAM's performance in environments with limited overlap, ...
- **p. 3 / III. S3E DATASET - extractive PDF cue:** The dataset features two mobile robot platform versions: ∙S3Ev1.0: Designed for indoor use with a compact design for exceptional maneuverability in tight spaces. ∙S3Ev2.0: Enhanced ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** The distinct trajectory paradigms adopted by three agents, designated as Alpha, Bob, and Carol, to demonstrate different interaction and information exchange patterns in a multi-agent ...
- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive PDF cue:** 2) Communication Constraints: Robots are typically limited to sharing information within close proximity, necessitating trajectory designs that maintain a reasonable interaction distance for effective communication.

## Design Rationale

- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive PDF cue:** In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse closure strategies in ...
- **p. 1 / Abstract - extractive PDF cue:** Addressing this gap, we introduce S3E, an expansive multimodal dataset.
- **p. 2 / 3 UGVs - extractive PDF cue:** In conclusion, our work makes several key contributions to the field: ∙We have created a cutting-edge C-SLAM dataset using three ground robots, each equipped with ...

## Source Evidence Cues

- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive PDF cue:** To fill this gap and enhance C-SLAM research, we introduce S3E dataset, offering a multimodal perspective with a variety of cooperative trajectory patterns in both ...
- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive PDF cue:** In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse closure strategies in ...
- **p. 3 / III. S3E DATASET - extractive PDF cue:** For synchronization across agents, we address two distinct scenarios: ∙In outdoor settings with access to Global Navigation Satellite System (GNSS) signals, we use GNSS time ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Playground: Open spaces with fewer obstructions challenge feature extraction and optimization.
- **p. 2 / 3 UGVs - extractive PDF cue:** This dataset is the first to incorporate UWB relative distance measurements, providing a new research dimension. ∙To assess C-SLAM's performance in environments with limited overlap, ...
- **p. 3 / III. S3E DATASET - extractive PDF cue:** The dataset features two mobile robot platform versions: ∙S3Ev1.0: Designed for indoor use with a compact design for exceptional maneuverability in tight spaces. ∙S3Ev2.0: Enhanced ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** The distinct trajectory paradigms adopted by three agents, designated as Alpha, Bob, and Carol, to demonstrate different interaction and information exchange patterns in a multi-agent ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | To fill this gap and enhance C-SLAM research, we introduce S3E dataset, offering a multimodal perspective with a variety of cooperative trajectory ... | p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 1 (C OLLABORATIVE Simultaneous Localization and Map) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse ... | p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | For synchronization across agents, we address two distinct scenarios: ∙In outdoor settings with access to Global Navigation Satellite System (GNSS) signals, we ... | p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive PDF cue:** 2) Communication Constraints: Robots are typically limited to sharing information within close proximity, necessitating trajectory designs that maintain a reasonable interaction distance for effective communication.
- **p. 3 / III. S3E DATASET - extractive PDF cue:** Sensor Synchronization This section delves into the critical processes of time synchronization and sensor calibration, which are essential for achieving optimal sensor fusion and maximizing ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** (d) Rays the high costs of a large-scale system.
- **p. 1 / Abstract - extractive PDF cue:** Despite this interest, the scalability and diversity of existing datasets for collaborative trajectories remain limited, especially in scenarios with constrained perspectives where the generalization capabilities ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Playground: Open spaces with fewer obstructions challenge feature extraction and optimization.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 1 (C OLLABORATIVE Simultaneous Localization and Map).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | sequences, feature, meticulously, synchronized, spatially, calibrated, data, streams, including, degree, LiDAR, point, cloud, high-resolution | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | sequences, feature, meticulously, synchronized, spatially, calibrated, data, streams, including, degree | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | introduce, four, trajectory, prototypes, designed, meet, principles, evaluate, adaptability, C-SLAM | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Communication, Constraints, Robots, typically, limited, sharing, information, within, close, proximity | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive PDF cue:** These sequences feature meticulously synchronized and spatially calibrated data streams, including 360-degree LiDAR point cloud, high-resolution stereo imagery, high-frequency inertial measurement units (IMU), and Ultrawideband ...
- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive PDF cue:** 2) Communication Constraints: Robots are typically limited to sharing information within close proximity, necessitating trajectory designs that maintain a reasonable interaction distance for effective communication.
- **p. 3 / III. S3E DATASET - extractive PDF cue:** This integration allows for high-frequency positioning data output even during GNSS signal outages, such as in tunnels.
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Playground: Open spaces with fewer obstructions challenge feature extraction and optimization.
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Realtime data sharing improves accuracy, but the similarity of observations can make it challenging to detect and adapt to rapid environmental changes.
- **p. 2 / C OLLABORATIVE Simultaneous Localization and Map - extractive PDF cue:** Dataset Platform Sensors Time Sync.
- **p. 2 / 3 UGVs - extractive PDF cue:** ✓ ✓ ✓ ✓ Hw GNSS, PTPv2 Restricted 4 ✓ ✓ RTK, GNSS/INS Motion Capture (a) Sensor locations and the coordinate frames.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | These sequences feature meticulously synchronized and spatially calibrated data streams, including 360-degree LiDAR point cloud, high-resolution stereo imagery, high-frequency inertial measurement units ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Considering transmission delays, all sensor readings are forwarded to the host computer, where they are timestamped upon arrival, organized, and packaged to ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** fill, enhance, C-SLAM, research, introduce, S3E, dataset, offering, multimodal, perspective, variety, cooperative, trajectory, patterns, outdoor, indoor, environments, four, prototypes, designed.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | The dataset features two mobile robot platform versions: ∙S3Ev1.0: Designed for indoor use with a compact design for exceptional maneuverability in tight ... | p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET) |
| Baseline harness | For most of the baselines, we only modify the intrinsic and extrinsic of the sensors and use the left camera for evaluation. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric / failure reporting | However, in areas with limited overlap, reducing drift remained a challenge. - The incorporation of UWB measurements in CoLRIO significantly improved localization ... | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both single-agent and collaborative SLAM (C-SLAM) systems in ...
- **p. 3 / III. S3E DATASET - extractive PDF cue:** In indoor environments without GNSS signals, like laboratories, a motion capture system with 17 high-frequency cameras is used to record track start and endpoints due ...
- **p. 6 / III. S3E DATASET - extractive PDF cue:** If inter-loop closures detection fails, we mark it "Failed".
- **p. 7 / VI. CONCLUSION - extractive PDF cue:** Our experiments using this dataset have highlighted the improved robustness of C-SLAM systems, especially in handling inter-loop closures.
- **p. 3 / III. S3E DATASET - extractive PDF cue:** Sensor Configuration Our S3E dataset encompasses a multimodal array of sensors, each selected for its operational range and noise characteristics, and meticulously synchronized to capture ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Teaching Building and Tunnel: Poor lighting and similar geometric structures challenge robustness in maintaining
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Each paradigm is meticulously crafted to offer a robust framework for assessing C-SLAM algorithms across a multitude of real-world collaborative robotic applications.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 2 (3 UGVs), p. 3 (III. S3E DATASET), objective p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 1 (Abstract), p. 4 (III. S3E DATASET), temporal p. 1 (Abstract), p. 3 (III. S3E DATASET), p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 2 (3 UGVs), p. 2 (3 UGVs), p. 3 (III. S3E DATASET).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
