# Method - FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.19190; PDF retrieval source: https://arxiv.org/pdf/2606.19190. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY)): The processing pipeline consists of two main modules: LIVO Update: Adopting the FAST-LIVO2 strategy, this module sequentially updates the state using camera photometric residuals and LiDAR point-to-plane geometric residuals via ...

## Method Body Digest

- **p. 2 / III. METHODOLOGY - extractive PDF cue:** The processing pipeline consists of two main modules: LIVO Update: Adopting the FAST-LIVO2 strategy, this module sequentially updates the state using camera photometric residuals and ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The resulting optimal time lag δtrI is then compensated when utilizing GNSS observations.
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** Notation and State Transition Model We define the full system state vector x in continuous time as an element of the manifold M.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** We construct the following objective function to solve for the
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** Following initialization, the ESIKF state is updated using two types of residuals: • Doppler Residual: Directly constrains the instantaneous velocity and the receiver clock drift ...
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** GNSS Update: Upon receiving GNSS data, a LIVOassisted integrity monitor first rejects outliers.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** C(·) The vector (·) in the RGB camera frame. x, bx, ¯x The ground-truth, predicted, and updated estimation of x. δx The error state between ...
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** To unify spatial references, GNSS ephemeris and observations (e.g., position, velocity) are transformed from the EarthCentered, Earth-Fixed (ECEF) frame to the local East-NorthUp (ENU) frame ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To address these issues, we propose a tightly-coupled multi-sensor fusion system formulated within an Error-State Iterated Kalman Filter (ESIKF), aiming at globally consistent mapping in ...
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** The processing pipeline consists of two main modules: LIVO Update: Adopting the FAST-LIVO2 strategy, this module sequentially updates the state using camera photometric residuals and ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The main contributions are summarized as follows: • A tightly-coupled LiDAR-Inertial-Visual-GNSS fusion framework based on ESIKF.

## Source Evidence Cues

- **p. 2 / III. METHODOLOGY - extractive PDF cue:** The processing pipeline consists of two main modules: LIVO Update: Adopting the FAST-LIVO2 strategy, this module sequentially updates the state using camera photometric residuals and ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The resulting optimal time lag δtrI is then compensated when utilizing GNSS observations.
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** Notation and State Transition Model We define the full system state vector x in continuous time as an element of the manifold M.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** We construct the following objective function to solve for the
- **Detected method headings:** III. METHODOLOGY (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The processing pipeline consists of two main modules: LIVO Update: Adopting the FAST-LIVO2 strategy, this module sequentially updates the state using camera ... | p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The resulting optimal time lag δtrI is then compensated when utilizing GNSS observations. | p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Notation and State Transition Model We define the full system state vector x in continuous time as an element of the manifold ... | p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / III. METHODOLOGY - extractive PDF cue:** Following initialization, the ESIKF state is updated using two types of residuals: • Doppler Residual: Directly constrains the instantaneous velocity and the receiver clock drift ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** We construct the following objective function to solve for the
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** GNSS Update: Upon receiving GNSS data, a LIVOassisted integrity monitor first rejects outliers.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** C(·) The vector (·) in the RGB camera frame. x, bx, ¯x The ground-truth, predicted, and updated estimation of x. δx The error state between ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | unify, spatial, references, GNSS, ephemeris, observations, position, velocity, transformed, EarthCentered, Earth-Fixed, ECEF, frame, local | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | unify, spatial, references, GNSS, ephemeris, observations, position, velocity, transformed, EarthCentered | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, issues, tightly-coupled, multi-sensor, fusion, system, formulated, within, Error-State, Iterated | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Following, initialization, ESIKF, state, updated, types, residuals, Doppler, Residual, Directly | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. METHODOLOGY - extractive PDF cue:** To unify spatial references, GNSS ephemeris and observations (e.g., position, velocity) are transformed from the EarthCentered, Earth-Fixed (ECEF) frame to the local East-NorthUp (ENU) frame ...
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** This lightweight approach successfully avoids state augmentation while fully exploiting the submillimeter relative precision of carrier phase observations.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** In a tightly-coupled formulation, GNSS observables depend not only on the platform pose and velocity but also on receiver clock states and inter-system biases.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Precise Doppler and fixed-anchor TDCP observation models are further constructed to introduce sub-millimeter relative constraints without state augmentation, improving global consistency. • A degeneracy-dependent dual-mode ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To address these issues, we propose a tightly-coupled multi-sensor fusion system formulated within an Error-State Iterated Kalman Filter (ESIKF), aiming at globally consistent mapping in ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Outlier Rejection GNSS residual Yes No EKF Process t State Estimation Lidar points x 1 1 + - i k x 2 1 + - ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** (3) This LS problem provides an accurate initial global pose and refines the coarse lever-arm extrinsics.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The architecture leverages sensor complementarity: the high-frequency, robust LIVO odometry assists GNSS with online spatiotemporal synchronization, bridges signal outages, and aids quality ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The system exploits sensor complementarities by using high-frequency FAST-LIVO2 odometry as geometric priors for GNSS signal evaluation and online spatiotemporal alignment, while ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** processing, pipeline, consists, main, modules, LIVO, Update, Adopting, FAST-LIVO2, strategy, module, sequentially, updates, state, camera, photometric, residuals, LiDAR, point-to-plane, geometric.
- **Relevant PDF headings:** III. METHODOLOGY (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Evaluation on Benchmark Dataset (M3DGR) We conducted standardized quantitative comparisons on the public M3DGR dataset [10], which provides RTK ground | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Semantic / temporal fusion | Notably, although the ablation version (Ours w/o Rejection) outperforms pure FAST-LIVO2 due to GNSS integration, it remains slightly inferior to our complete ... | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | By sacrificing negligible accuracy in denied environments, our system gains significant global accuracy improvements in open areas and successfully prevents tightly-coupled system ... | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTAL RESULTS - extractive PDF cue:** An ablation variant, Ours w/o Rejection, was also evaluated by disabling the adaptive robust module and fusing all pre-screened GNSS observations.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive PDF cue:** Notably, although the ablation version (Ours w/o Rejection) outperforms pure FAST-LIVO2 due to GNSS integration, it remains slightly inferior to our complete version.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive PDF cue:** In contrast, looser-coupled systems like LIO-SAM and LIGO generate meter-level errors but avoid complete failure.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive PDF cue:** Under such harsh conditions, a critical finding is that the ablation version (Ours w/o Rejection) directly suffers from trajectory divergence and system failure (marked as ...
- **p. 5 / IV. STATE ESTIMATION - extractive PDF cue:** When encountering feature degradation (e.g., textureless long corridors), the prior covariance bPk inflates.
- **p. 5 / IV. STATE ESTIMATION - extractive PDF cue:** Signals with low Carrier-to-Noise density (C/N0 <35 dB-Hz) or low elevation angles (< 15◦) are physically filtered out.
- **p. 7 / 2) High-Precision Mapping in Large-Scale Highly Dy - extractive PDF cue:** 2) Outdoor LIVO Degraded Scenario: In regions (a)-(c) of View 1 (Fig.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), objective p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), temporal p. 2 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 1 (Abstract), p. 3 (III. METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
