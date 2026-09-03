# Method - Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=nv3q3crc5D; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245566. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION)): The model then employs two interconnected decoders that facilitate bidirectional information exchange between visual tokens Ft and the persistent hidden state Mt-1 via cross-attention.

## Method Body Digest

- **p. 5 / 1 INTRODUCTION - extractive body cue:** The model then employs two interconnected decoders that facilitate bidirectional information exchange between visual tokens Ft and the persistent hidden state Mt-1 via cross-attention.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** The training objective consists of three loss components, summed over a sequence of length L.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** We then present our loop closure mechanism, which leverages the model's hidden state to enable global drift correction via Sim(3) optimization (§4.2).
- **p. 1 / ABSTRACT - extractive body cue:** We trained a recurrent feed-forward frontend model that progressively aggregates multi-frame visual features into a hidden state via cross attention and jointly predicts camera poses ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Compared to all previous methods that require training Gaussians entirely from scratch, our framework achieves remarkable speed improvements while still ensuring high-quality results. • We ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** A following pose graph optimization is then performed to correct the full trajectory.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our main contributions are: • We propose a real-time (10 FPS+) monocular GS-SLAM framework that leverages a recurrent feed-forward model to predict poses ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** The globally optimal set of poses T W ∗is found by minimizing a non-linear least-squares cost function over all constraints: T W ∗= arg min ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our main contributions are: • We propose a real-time (10 FPS+) monocular GS-SLAM framework that leverages a recurrent feed-forward model to predict poses ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** 4 OUR APPROACH In this section, we introduce our approach in the following order.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To overcome these challenges, we propose Flash-Mono, a monocular GS-SLAM system designed to deliver exceptional speed performance and high-quality mapping.

## Source Evidence Cues

- **p. 5 / 1 INTRODUCTION - extractive body cue:** The model then employs two interconnected decoders that facilitate bidirectional information exchange between visual tokens Ft and the persistent hidden state Mt-1 via cross-attention.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** The training objective consists of three loss components, summed over a sequence of length L.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** We then present our loop closure mechanism, which leverages the model's hidden state to enable global drift correction via Sim(3) optimization (§4.2).
- **p. 1 / ABSTRACT - extractive body cue:** We trained a recurrent feed-forward frontend model that progressively aggregates multi-frame visual features into a hidden state via cross attention and jointly predicts camera poses ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Compared to all previous methods that require training Gaussians entirely from scratch, our framework achieves remarkable speed improvements while still ensuring high-quality results. • We ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** A following pose graph optimization is then performed to correct the full trajectory.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our main contributions are: • We propose a real-time (10 FPS+) monocular GS-SLAM framework that leverages a recurrent feed-forward model to predict poses ...
- **Detected method headings:** C MODEL SIZE AND ACCELERATION (p. 16); C.1 MODEL SIZE (p. 16); C.2 MODEL ACCELERATION (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The model then employs two interconnected decoders that facilitate bidirectional information exchange between visual tokens Ft and the persistent hidden state Mt-1 ... | p. 5 (1 INTRODUCTION), p. 5 (1 INTRODUCTION) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The training objective consists of three loss components, summed over a sequence of length L. | p. 5 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We then present our loop closure mechanism, which leverages the model's hidden state to enable global drift correction via Sim(3) optimization (§4.2). | p. 4 (1 INTRODUCTION), p. 1 (ABSTRACT) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 1 INTRODUCTION - extractive body cue:** The globally optimal set of poses T W ∗is found by minimizing a non-linear least-squares cost function over all constraints: T W ∗= arg min ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** The training objective consists of three loss components, summed over a sequence of length L.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To combat the drift that is common in incremental feed-forward reconstruction, we leverage the model's hidden state as a compact submap descriptor: when revisiting a ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** This overlap also provides an explicit inter-submap alignment constraint, which is later incorporated into the pose graph for global optimization.
- **p. 6 / 1 INTRODUCTION - extractive body cue:** The computed Sim(3) constraint enables global optimization of the entire trajectory via a pose graph.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3 PRELIMINARIES: 2D GAUSSIAN FOR GEOMETRIC ACCURACY The original 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) often produces noisy geometry with "floater" artifacts, as ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | function, model, jointly, predict, three, outputs, camera, pose, representing, transformation, current, frame, coordinate, system | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | function, model, jointly, predict, three, outputs, camera, pose, representing, transformation | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, main, contributions, real-time, FPS, monocular, GS-SLAM, framework, leverages, recurrent | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | globally, optimal, poses, found, minimizing, non-linear, least-squares, cost, function, over | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 1 INTRODUCTION - extractive body cue:** The function of model f is to jointly predict three outputs: (a) the camera pose ˆTt ∈SE(3), representing the transformation from the current camera frame ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** For each new keyframe, it takes as input the RGB image Ik, the globally optimized camera pose Tk ∈Sim(3), and the per-pixel 2DGS map ˆGk ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** A single forward pass f(Ij, Ma) on the current frame Ij conditioned on this past context yields two key outputs: (1) the relocalized pose Ta ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** CUT3R (Wang et al., 2025b) further advanced this direction by adopting a recurrent framework that accommodates a variable number of images and supports diverse input ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** Here, (qt, τt), It, and Dt denote the ground-truth camera pose, RGB image, and depth map, respectively; µ is obtained by unprojecting the ground-truth depth ...
- **p. 1 / ABSTRACT - extractive body cue:** We present Flash-Mono, a system composed of three core modules: a feed-forward prediction frontend, a 2D Gaussian Splatting mapping backend, and an efficient hidden-state-based loop ...
- **p. 1 / ABSTRACT - extractive body cue:** We trained a recurrent feed-forward frontend model that progressively aggregates multi-frame visual features into a hidden state via cross attention and jointly predicts camera poses ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | In summary, our main contributions are: • We propose a real-time (10 FPS+) monocular GS-SLAM framework that leverages a recurrent feed-forward model ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Shorter lengths resulted in higher error, suggesting insufficient temporal context, while lengths greater than 16 frames also increased the error, which points ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | In summary, our main contributions are: • We propose a real-time (10 FPS+) monocular GS-SLAM framework that leverages a recurrent feed-forward model ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 1 INTRODUCTION - extractive body cue:** The training objective consists of three loss components, summed over a sequence of length L.
- **p. 1 / ABSTRACT - extractive body cue:** We trained a recurrent feed-forward frontend model that progressively aggregates multi-frame visual features into a hidden state via cross attention and jointly predicts camera poses ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Compared to all previous methods that require training Gaussians entirely from scratch, our framework achieves remarkable speed improvements while still ensuring high-quality results. • We ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Since a single iteration takes approximately 20 ms, the total training time per keyframe is roughly one second, inevitably resulting in slow overall performance.
- **p. 6 / 1 INTRODUCTION - extractive body cue:** The computed Sim(3) constraint enables global optimization of the entire trajectory via a pose graph.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, then, employs, interconnected, decoders, facilitate, bidirectional, information, exchange, between, visual, tokens, persistent, hidden, state, Mt-1, cross-attention, training, objective, consists.
- **Relevant PDF headings:** C MODEL SIZE AND ACCELERATION (p. 16); C.1 MODEL SIZE (p. 16); C.2 MODEL ACCELERATION (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | 5.1 EXPERIMENTAL SETUP We evaluate our system on three challenging real-world datasets: ScanNet (Dai et al., 2017a), BundleFusion (Dai et al., 2017b), ... | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Global / local decision | 5.2 TRACKING PERFORMANCE As shown in Table 1, Flash-Mono significantly outperformed all traditional and GS-SLAM baseline methods. | p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Motion execution / recovery | 5.2 TRACKING PERFORMANCE As shown in Table 1, Flash-Mono significantly outperformed all traditional and GS-SLAM baseline methods. | p. 8 (5 EXPERIMENTS), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 10 / 5 EXPERIMENTS - extractive body cue:** MonoGS 1.19 1.20 DepthGS 0.49 0.23 S3PO-GS 0.52 0.85 Ours 0.34 0.21 5.5 ABLATION We conducted ablation studies to analyze the impact of key system ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** First, we evaluated the effect of backend refinement iterations on rendering quality (PSNR).
- **p. 16 / Figure/Table caption - extractive body cue:** Table 7: Detailed breakdown of Flash-Mono model parameters. Component Total Parameters Encoder
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** On KITTI, we primarily compare against S3POGS, as we encountered frequent failures while evaluating other indoor-focused GS-SLAM baselines due to the large-scale and high dynamic ...
- **p. 10 / 6 CONCLUSION - extractive body cue:** Furthermore, we introduced a novel loop closure mechanism that enables robust Sim(3) optimization to correct scale and pose drift inherent in monocular systems, leading to ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Since MonoGS and DepthGS are designed primarily for indoor scenes, they often fail under the large scale variance and dynamics in KITTI; therefore, we mainly ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Method Metric 00 05 06 07 08 28 S3PO-GS PSNR ↑ 16.65 15.64 13.55 fail 17.25 15.30 SSIM ↑ 0.5409 0.5320 0.4726 fail 0.5912 0.5053 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), objective p. 6 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), temporal p. 2 (1 INTRODUCTION), p. 10 (5 EXPERIMENTS), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (5 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
