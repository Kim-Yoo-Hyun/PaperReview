# Method - VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://icml.cc/virtual/2026/poster/65079; PDF retrieval source: https://openreview.net/pdf/dd631f65ff2ca6199a6897ee3816879152720eef.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Motion-Aware Submap Construction), p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Motion-Aware Submap Construction), p. 5 (3.3. Lightweight Pose Graph Optimization), p. 5 (3.2. Anchor-Driven Direct Sim(3) Registration)): Foundation-model inference is highly sensitive to motion dynamics.

## Method Body Digest

- **p. 4 / 3.1. Motion-Aware Submap Construction - extractive body cue:** Foundation-model inference is highly sensitive to motion dynamics.
- **p. 3 / 3. Method - extractive body cue:** Then, we develop an anchor-driven direct Sim(3) registration algorithm to align submaps and optimize their poses.
- **p. 3 / 3. Method - extractive body cue:** We first construct motion-aware submaps that segment the sequence into reliable regimes and infer local geometry with the foundation model VGGT.
- **원문 대조:** Overlap 및 loop anchor가 추가된 submap sequence를 VGGT에 입력해 local point maps, camera poses, pixel-wise confidence maps를 얻는다. 이 출력들을 이후 submap registration에 사용한다. ([PDF p. 4](https://arxiv.org/pdf/2602.05508#page=4), §3.1, Eq. (5)).
- **원문 대조:** Submap pose는 edge별 information-weighted squared residual에 Huber loss를 적용한 합을 최소화해 추정한다. 첫 pose X_1=I를 고정하고 Levenberg–Marquardt로 푼다. ([PDF p. 5](https://arxiv.org/pdf/2602.05508#page=5), §3.3 Lightweight Pose Graph Optimization, Eq. (12)).
- **p. 5 / 3.2. Anchor-Driven Direct Sim(3) Registration - extractive body cue:** Since h retains its original metric state, no re-inference is required, enabling direct loop closure alignment.
- **p. 6 / 3.3. Lightweight Pose Graph Optimization - extractive body cue:** Overall, our backend performs sparse Sim(3) optimization over a small set of submaps, yielding a globally consistent trajectory at low computational cost.
- **p. 5 / 3.2. Anchor-Driven Direct Sim(3) Registration - extractive body cue:** This selection ensures a balanced receptive field, minimizing boundary artifacts and maximizing geometric consistency between two adject submaps.

## Design Rationale

- **p. 3 / 3. Method - extractive body cue:** Then, we develop an anchor-driven direct Sim(3) registration algorithm to align submaps and optimize their poses.

## Source Evidence Cues

- **p. 4 / 3.1. Motion-Aware Submap Construction - extractive body cue:** Foundation-model inference is highly sensitive to motion dynamics.
- **p. 3 / 3. Method - extractive body cue:** Then, we develop an anchor-driven direct Sim(3) registration algorithm to align submaps and optimize their poses.
- **p. 3 / 3. Method - extractive body cue:** We first construct motion-aware submaps that segment the sequence into reliable regimes and infer local geometry with the foundation model VGGT.
- **원문 대조:** Overlap 및 loop anchor가 추가된 submap sequence를 VGGT에 입력해 local point maps, camera poses, pixel-wise confidence maps를 얻는다. 이 출력들을 이후 submap registration에 사용한다. ([PDF p. 4](https://arxiv.org/pdf/2602.05508#page=4), §3.1, Eq. (5)).
- **원문 대조:** Submap pose는 edge별 information-weighted squared residual에 Huber loss를 적용한 합을 최소화해 추정한다. 첫 pose X_1=I를 고정하고 Levenberg–Marquardt로 푼다. ([PDF p. 5](https://arxiv.org/pdf/2602.05508#page=5), §3.3 Lightweight Pose Graph Optimization, Eq. (12)).
- **p. 5 / 3.2. Anchor-Driven Direct Sim(3) Registration - extractive body cue:** Since h retains its original metric state, no re-inference is required, enabling direct loop closure alignment.
- **p. 6 / 3.3. Lightweight Pose Graph Optimization - extractive body cue:** Overall, our backend performs sparse Sim(3) optimization over a small set of submaps, yielding a globally consistent trajectory at low computational cost.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Foundation-model inference is highly sensitive to motion dynamics. | p. 4 (3.1. Motion-Aware Submap Construction), p. 3 (3. Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Then, we develop an anchor-driven direct Sim(3) registration algorithm to align submaps and optimize their poses. | p. 3 (3. Method), p. 3 (3. Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We first construct motion-aware submaps that segment the sequence into reliable regimes and infer local geometry with the foundation model VGGT. | p. 3 (3. Method), p. 4 (3.1. Motion-Aware Submap Construction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Anchor-Driven Direct Sim(3) Registration - extractive body cue:** This selection ensures a balanced receptive field, minimizing boundary artifacts and maximizing geometric consistency between two adject submaps.
- **원문 대조:** Submap pose는 edge별 information-weighted squared residual에 Huber loss를 적용한 합을 최소화해 추정한다. 첫 pose X_1=I를 고정하고 Levenberg–Marquardt로 푼다. ([PDF p. 5](https://arxiv.org/pdf/2602.05508#page=5), §3.3 Lightweight Pose Graph Optimization, Eq. (12)).
- **p. 6 / 3.3. Lightweight Pose Graph Optimization - extractive body cue:** Overall, our backend performs sparse Sim(3) optimization over a small set of submaps, yielding a globally consistent trajectory at low computational cost.
- **p. 4 / 3.2. Anchor-Driven Direct Sim(3) Registration - extractive body cue:** In contrast, we derive dense, search-free geometric correspondences from VGGT point maps to impose robust Sim(3) constraints.
- **p. 4 / 3.1. Motion-Aware Submap Construction - extractive body cue:** For linear motion, a maximum frame budget Nmax controls submap length, balancing memory constraints with local geometric fidelity.
- **p. 3 / 3.1. Motion-Aware Submap Construction - extractive body cue:** As these errors originate from pre-inference grouping, they evade backend optimization.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.3. Lightweight Pose Graph Optimization), p. 4 (3.2. Anchor-Driven Direct Sim(3) Registration), p. 4 (3.1. Motion-Aware Submap Construction), p. 5 (3.2. Anchor-Driven Direct Sim(3) Registration).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, estimated, motion, state, partition, input, sequence, submaps, geometrically, informative, conducive, robust, monocular, scale | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Given, estimated, motion, state, partition, input, sequence, submaps, geometrically, informative | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Then, develop, anchor-driven, direct, Sim, registration, algorithm, align, submaps, optimize | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | selection, ensures, balanced, receptive, field, minimizing, boundary, artifacts, maximizing, geometric | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. Motion-Aware Submap Construction - extractive body cue:** Given the estimated motion state s(t), we partition the input sequence into submaps that are geometrically informative and conducive to robust monocular scale estimation.
- **p. 4 / 3.1. Motion-Aware Submap Construction - extractive body cue:** (5) Here, the outputs include local point maps Pk, camera poses Tk, and pixel-wise confidence maps Ck, all of which are used for subsequent inter-submap ...
- **p. 3 / 3.1. Motion-Aware Submap Construction - extractive body cue:** This motivates a motion-consistent construction scheme that classifies motion states via optical flow to adaptively select keyframes-pruning redundancy while preserving turning context.
- **p. 5 / 3.2. Anchor-Driven Direct Sim(3) Registration - extractive body cue:** Since h retains its original metric state, no re-inference is required, enabling direct loop closure alignment.
- **p. 5 / 3.2. Anchor-Driven Direct Sim(3) Registration - extractive body cue:** Crucially, this formulation yields O(HW) dense constraints with trivial O(1) association cost per pixel, effectively circumventing descriptor extraction, nearestneighbor search, and the quadratic complexity of ...
- **p. 3 / 3. Method - extractive body cue:** Given a monocular image sequence, our goal is to recover a globally consistent trajectory and dense geometry.
- **p. 6 / 3.3. Lightweight Pose Graph Optimization - extractive body cue:** The global pose of any keyframe In ∈Mk is obtained by composing the optimized submap pose with the local pose T (n) k : T(n) ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | However, the quadratic complexity (O(N 2)) of their Transformer-based architectures imposes severe memory constraints and computational bottlenecks, rendering direct deployment on long-horizon ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Naive temporal chunking in foundation-model SLAM triggers two systematic failures: (i) zero-motion drift during stop-and-go periods, where aligning noisy quasi-static predictions accumulates ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | However, the quadratic complexity (O(N 2)) of their Transformer-based architectures imposes severe memory constraints and computational bottlenecks, rendering direct deployment on long-horizon ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Motion-Aware Submap Construction - extractive body cue:** Foundation-model inference is highly sensitive to motion dynamics.
- **p. 5 / 3.2. Anchor-Driven Direct Sim(3) Registration - extractive body cue:** Since h retains its original metric state, no re-inference is required, enabling direct loop closure alignment.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Foundation-model, inference, highly, sensitive, motion, dynamics, Then, develop, anchor-driven, direct, Sim, registration, algorithm, align, submaps, optimize, poses, first, construct, motion-aware.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Hyperparameters are fixed across benchmarks and dataset-specific thresholds are held constant for all sequences. | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Global / local decision | As shown in Figure 5, our pipeline consistently outperforms state-of-the-art foundation-modelbased methods (VGGT-Long and VGGT-SLAM) across all five benchmarks. | p. 7 (4.4. Efficiency), p. 8 (4.5. Ablation Studies) |
| Motion execution / recovery | Topology-aware partitioning significantly outperforms heuristic baselines by preserving turning topology. | p. 8 (4.5. Ablation Studies), p. 6 (4.3. Zero-Shot Generalization & Scalability) |

## Failure and Ablation Link

- **p. 7 / 4.5. Ablation Studies - extractive body cue:** To isolate effects, we adopt an incremental ablation protocol in which modules are added in pipeline order, with each stage initialized from the best configuration ...
- **p. 7 / 4.5. Ablation Studies - extractive body cue:** We conduct ablation studies on KITTI to assess the contribution of each component in our pipeline.
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Ablation study on Redundancy Filtering on KITTI.
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Ablation of submap partitioning strategies on KITTI dataset.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison of the SOTA method VGGT-Long (Deng et al., 2025) and our VGGT-Motion across sequences with varying frame counts. While VGGT-Long suffers from ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 6. Ablation of loop closure strategies on KITTI. Unidirectional loop keyframe reuse within CBA yields the best performance by preventing historical context pollution. Loop ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 8. Kitti dataset sequence 00 & sequence 05 trajectory visualizations on Depthanything-v3 with SE(3) alignment. Coupling Between Geometric Priors and SLAM Performance. Our study ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Motion-Aware Submap Construction), p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Motion-Aware Submap Construction), p. 5 (3.3. Lightweight Pose Graph Optimization), p. 5 (3.2. Anchor-Driven Direct Sim(3) Registration), objective p. 5 (3.2. Anchor-Driven Direct Sim(3) Registration), p. 5 (3.3. Lightweight Pose Graph Optimization), p. 6 (3.3. Lightweight Pose Graph Optimization), p. 4 (3.2. Anchor-Driven Direct Sim(3) Registration), p. 4 (3.1. Motion-Aware Submap Construction), p. 3 (3.1. Motion-Aware Submap Construction), temporal p. 1 (1. Introduction), p. 3 (3.1. Motion-Aware Submap Construction), p. 4 (3.2. Anchor-Driven Direct Sim(3) Registration), p. 4 (3.1. Motion-Aware Submap Construction), p. 5 (3.2. Anchor-Driven Direct Sim(3) Registration), p. 7 (4.4. Efficiency).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
