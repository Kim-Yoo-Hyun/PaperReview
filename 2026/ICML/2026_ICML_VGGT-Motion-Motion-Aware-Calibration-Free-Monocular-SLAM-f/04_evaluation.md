# Evaluation - VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=GyRMbsYFiG; PDF retrieval source: https://openreview.net/pdf/dd631f65ff2ca6199a6897ee3816879152720eef.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.5. Ablation Studies), p. 6 (4.3. Zero-Shot Generalization & Scalability), p. 7 (4.4. Efficiency), p. 8 (4.5. Ablation Studies), p. 6 (4.2. Comparison on Standard Benchmarks), p. 7 (4.4. Efficiency)): Topology-aware partitioning significantly outperforms heuristic baselines by preserving turning topology.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Hyperparameters are fixed across benchmarks and dataset-specific thresholds are held constant for all sequences.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** To demonstrate robustness across diverse environments, we curate an evaluation suite comprising five outdoor datasets.
- **p. 7 / 4.4. Efficiency - extractive body cue:** Absolute Trajectory Error (ATE ↓) RMSE (m) comparison on the KITTI dataset.
- **p. 7 / 4.4. Efficiency - extractive body cue:** Experimental results on long-sequence generalization benchmarks.
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Runtime efficiency comparison on five different benchmarks.
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Ablation of submap partitioning strategies on KITTI dataset.
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 15. Trajectory visualizations on long-range generalization benchmarks (4Seasons, Complex Urban, A2D2). Subplots show diverse segments, color denotes APE magnitude after Sim(3) alignment. Analysis Precision ...
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Construction Strategy Trigger Mechanism ATE (m) ↓ Drift (%) ↓ Temporal Slicing Temporal Length 26.98 1.58 Parallax-Triggered Cumulative Parallax 28.15 1.62 Topology-Aware Turning Encapsulation 24.56 ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Comparison on Standard Benchmarks (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.5. Ablation Studies | SYSTEM / EVALUATION SCOPE UNRESOLVED | Topology-aware partitioning significantly outperforms heuristic baselines by preserving turning topology. | p. 8 (4.5. Ablation Studies) |
| 4.3. Zero-Shot Generalization & Scalability | SYSTEM / EVALUATION SCOPE UNRESOLVED | We attribute this success to our targeted algorithmic designs: Submap Composition with Geometric Anchors injects loop keyframes as geometric anchors to bridge appearance gaps ... | p. 6 (4.3. Zero-Shot Generalization & Scalability) |
| 4.4. Efficiency | SYSTEM / EVALUATION SCOPE UNRESOLVED | The performance gap is particularly large on long-sequence datasets (4Seasons, Complex Urban, and A2D2), where we achieve an 18-36× speedup in total processing time ... | p. 7 (4.4. Efficiency) |
| 4.5. Ablation Studies | SYSTEM / EVALUATION SCOPE UNRESOLVED | By eliminating the primary source of noise-induced drift during stops, it simultaneously improves accuracy and reduces computational overhead. | p. 8 (4.5. Ablation Studies) |
| 4.2. Comparison on Standard Benchmarks | SYSTEM / EVALUATION SCOPE UNRESOLVED | On highly dynamic Waymo segments, our context-balanced anchor selection and robust Sim(3) estimation enforce geometric constraints under occlusions, yielding a further 20% improvement. | p. 6 (4.2. Comparison on Standard Benchmarks) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Hyperparameters are fixed across benchmarks and dataset-specific thresholds are held constant for all sequences.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** To demonstrate robustness across diverse environments, we curate an evaluation suite comprising five outdoor datasets.
- **p. 7 / 4.4. Efficiency - extractive body cue:** Absolute Trajectory Error (ATE ↓) RMSE (m) comparison on the KITTI dataset.
- **p. 7 / 4.4. Efficiency - extractive body cue:** Experimental results on long-sequence generalization benchmarks.
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Runtime efficiency comparison on five different benchmarks.
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Ablation of submap partitioning strategies on KITTI dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison of the SOTA method VGGT-Long (Deng et al., 2025) and our VGGT-Motion across sequences with varying frame counts. While VGGT-Long suffers from ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The pipeline of VGGT-Motion, consisting of three stages: (a) Motion-Aware Submap Construction, (b) Anchor-Driven Direct Sim(3) Registration, and (c) Lightweight Pose Graph Optimization. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Context-balanced anchors. (i) Globally consistent recon- struction. (ii) Overlap and loop anchors for submap alignment. as the overlap anchor Iovlp ≜N(mid(W)). This selection ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Absolute Trajectory Error (ATE ↓) RMSE (m) comparison on the KITTI dataset. Following VGGT-Long, we additionally report Avg.* with the sequence 01 excluded. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Absolute Trajectory Error (ATE ↓) RMSE (m) comparison on Waymo Open dataset. Recent foundation-model-based methods are included. "TL" and "OOM" indicate Tracking Lost ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Experimental results on long-sequence generalization benchmarks. Absolute Trajectory Error (ATE) and Translation Drift are reported. "TL" and "OOM" denote Tracking Lost and Out-of-Memory ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative results on generalization benchmarks. We visualize the estimated trajectories on (a) 4Seasons, (b) Complex Urban, and (c) A2D2 datasets. Our method exhibits ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Runtime efficiency comparison on five different bench- marks. (a) Total runtime per scene (s) shown in log scale. (b) Average runtime per frame ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Hyperparameters are fixed across benchmarks and dataset-specific thresholds are held constant for all sequences. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | To demonstrate robustness across diverse environments, we curate an evaluation suite comprising five outdoor datasets. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 7 (4.4. Efficiency) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3.1. Motion-Aware Submap Construction), p. 4 (3.1. Motion-Aware Submap Construction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (3.1. Motion-Aware Submap Construction), p. 5 (3.2. Anchor-Driven Direct Sim(3) Registration) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 15. Trajectory visualizations on long-range generalization benchmarks (4Seasons, Complex Urban, A2D2). Subplots show diverse segments, color denotes APE magnitude after Sim(3) alignment. Analysis ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Construction Strategy Trigger Mechanism ATE (m) ↓ Drift (%) ↓ Temporal Slicing Temporal Length 26.98 1.58 Parallax-Triggered Cumulative Parallax 28.15 1.62 Topology-Aware Turning Encapsulation ... | definition/direction/unit from same section | p. 8 (4.5. Ablation Studies) |
| Table 8. Absolute Trajectory Error (ATE) RMSE (m) comparison on representative TUM-Mono sequences.VGGT-Motion (Ours) demonstrates superior robustness across all handheld sequences compared to submap-based ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 12. Additional trajectory visualizations on TUM-Mono sequences 39, 45, 46, 47, and 48. The color scale represents the Absolute Pose Error (APE) magnitude ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| We report the Absolute Trajectory Error (ATE) after global Sim(3) alignment to account for monocular scale ambiguity. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Absolute Trajectory Error (ATE ↓) RMSE (m) comparison on the KITTI dataset. | definition/direction/unit from same section | p. 7 (4.4. Efficiency) |
| Recent foundation-model-based methods are included. "TL" and "OOM" indicate Tracking Lost and Out-of-Memory errors, respectively. | definition/direction/unit from same section | p. 7 (4.4. Efficiency) |
| Observations reveal that naive dense (using all frames) or uniform sampling paradoxically degrades accuracy. | definition/direction/unit from same section | p. 8 (4.5. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Figure 5, our pipeline consistently outperforms state-of-the-art foundation-modelbased methods (VGGT-Long and VGGT-SLAM) across all five benchmarks. | comparison identity and matched condition | p. 7 (4.4. Efficiency) |
| Topology-aware partitioning significantly outperforms heuristic baselines by preserving turning topology. | comparison identity and matched condition | p. 8 (4.5. Ablation Studies) |
| Table 8. Absolute Trajectory Error (ATE) RMSE (m) comparison on representative TUM-Mono sequences.VGGT-Motion (Ours) demonstrates superior robustness across all handheld sequences compared to submap-based ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |
| For calibrated baselines, we supply ground-truth (GT) intrinsics to enforce an upper-bound comparison, while foundation-model-based systems are evaluated under their default uncalibrated settings. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Given the strong SOTA performance of VGGT-Long in large-scale outdoor scenes, we adopt its submap alignment scheme as the baseline. | comparison identity and matched condition | p. 8 (4.5. Ablation Studies) |
| In contrast, VGGT-Motion and VGGT-Long scale reliably and match calibrated baselines that use GT intrinsics. | comparison identity and matched condition | p. 6 (4.2. Comparison on Standard Benchmarks) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To isolate effects, we adopt an incremental ablation protocol in which modules are added in pipeline order, with each stage initialized from the best ... | component/input/data sensitivity | p. 7 (4.5. Ablation Studies) |
| We conduct ablation studies on KITTI to assess the contribution of each component in our pipeline. | component/input/data sensitivity | p. 7 (4.5. Ablation Studies) |
| Ablation study on Redundancy Filtering on KITTI. | component/input/data sensitivity | p. 8 (4.5. Ablation Studies) |
| Ablation of submap partitioning strategies on KITTI dataset. | component/input/data sensitivity | p. 8 (4.5. Ablation Studies) |
| Figure 1. Comparison of the SOTA method VGGT-Long (Deng et al., 2025) and our VGGT-Motion across sequences with varying frame counts. While VGGT-Long suffers ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Table 6. Ablation of loop closure strategies on KITTI. Unidirectional loop keyframe reuse within CBA yields the best performance by preventing historical context pollution. ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Then, we develop an anchor-driven direct Sim(3) registration algorithm to align submaps and optimize their poses. | Topology-aware partitioning significantly outperforms heuristic baselines by preserving turning topology. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.5. Ablation Studies), p. 6 (4.3. Zero-Shot Generalization & Scalability), p. 7 (4.4. Efficiency), p. 8 (4.5. Ablation Studies), p. 6 (4.2. Comparison on Standard Benchmarks), p. 7 (4.4. Efficiency) |
| Primary metric/result | We attribute this success to our targeted algorithmic designs: Submap Composition with Geometric Anchors injects loop keyframes as geometric anchors to bridge appearance gaps ... | numeric claim only at cited anchor | p. 6 (4.3. Zero-Shot Generalization & Scalability) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The challenges of these datasets cause baselines like MASt3R-SLAM, Fast3R, and CUT3R to frequently suffer Out-of-Memory (OOM) or Tracking-Lost (TL) failures. | p. 6 (4.3. Zero-Shot Generalization & Scalability) |
| body limitation/failure cue | Foundation-model-based methods such as MASt3R-SLAM, CUT3R, and Fast3R frequently encounter Out-of-Memory (OOM) or Tracking-Lost (TL) failures, indicating limited scalability in large outdoor scenes. | p. 6 (4.2. Comparison on Standard Benchmarks) |
| body limitation/failure cue | Absolute Trajectory Error (ATE) and Translation Drift are reported. "TL" and "OOM" denote Tracking Lost and Out-of-Memory failures, respectively. | p. 7 (4.4. Efficiency) |
| body limitation/failure cue | Our Topology-Aware strategy in MASP prevents this failure mode via Turning Segment Encapsulation. | p. 8 (4.5. Ablation Studies) |
| body limitation/failure cue | Figure 12. Additional trajectory visualizations on TUM-Mono sequences 39, 45, 46, 47, and 48. The color scale represents the Absolute Pose Error (APE) magnitude ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | Instead of providing valid geometric constraints, these redundant frames accumulate sensor noise and environmental disturbances. | p. 8 (4.5. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We evaluate computational efficiency by measuring the average end-to-end runtime under identical hardware configura6 | p. 6 (4.4. Efficiency) |
| Experiments are performed on an NVIDIA RTX 3090 with an i7-13700KF CPU. | p. 6 (4.1. Experimental Setup) |
| (b) Average runtime per frame (s/frame). | p. 8 (4.5. Ablation Studies) |
| (a) Total runtime per scene (s) shown in log scale. | p. 8 (4.5. Ablation Studies) |
| To quantify camera dynamics, we compute dense optical flow Ft : Ω→R2 between consecutive frames (It-1, It), where Ωdenotes the image domain and Ft(u) ... | p. 3 (3.1. Motion-Aware Submap Construction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.3. Zero-Shot Generalization & Scalability - extractive body cue:** The challenges of these datasets cause baselines like MASt3R-SLAM, Fast3R, and CUT3R to frequently suffer Out-of-Memory (OOM) or Tracking-Lost (TL) failures.
- **p. 6 / 4.2. Comparison on Standard Benchmarks - extractive body cue:** Foundation-model-based methods such as MASt3R-SLAM, CUT3R, and Fast3R frequently encounter Out-of-Memory (OOM) or Tracking-Lost (TL) failures, indicating limited scalability in large outdoor scenes.
- **p. 7 / 4.4. Efficiency - extractive body cue:** Absolute Trajectory Error (ATE) and Translation Drift are reported. "TL" and "OOM" denote Tracking Lost and Out-of-Memory failures, respectively.
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Our Topology-Aware strategy in MASP prevents this failure mode via Turning Segment Encapsulation.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 12. Additional trajectory visualizations on TUM-Mono sequences 39, 45, 46, 47, and 48. The color scale represents the Absolute Pose Error (APE) magnitude after ...
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Instead of providing valid geometric constraints, these redundant frames accumulate sensor noise and environmental disturbances.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.4. Efficiency), p. 7 (4.4. Efficiency), p. 8 (4.5. Ablation Studies), p. 8 (4.5. Ablation Studies), metrics p. 19 (Figure/Table caption), p. 8 (4.5. Ablation Studies), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption), p. 6 (4.1. Experimental Setup), p. 7 (4.4. Efficiency), baselines p. 7 (4.4. Efficiency), p. 8 (4.5. Ablation Studies), p. 16 (Figure/Table caption), p. 6 (4.1. Experimental Setup), p. 8 (4.5. Ablation Studies), p. 6 (4.2. Comparison on Standard Benchmarks), results p. 8 (4.5. Ablation Studies), p. 6 (4.3. Zero-Shot Generalization & Scalability), p. 7 (4.4. Efficiency), p. 8 (4.5. Ablation Studies), p. 6 (4.2. Comparison on Standard Benchmarks), p. 7 (4.4. Efficiency).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
