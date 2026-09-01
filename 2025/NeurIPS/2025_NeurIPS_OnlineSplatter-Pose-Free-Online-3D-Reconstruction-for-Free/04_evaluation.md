# Evaluation - OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Y9AdTCCEgI; PDF retrieval source: https://openreview.net/pdf/561349dc7bef7809d41f05247cf1a1df95e7712f.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2 Results), p. 7 (4 Experiments), p. 8 (4.2 Results), p. 10 (Figure/Table caption), p. 9 (4.2 Results), p. 10 (4.2 Results)): Even with fewer than four observations, OnlineSplatter significantly outperforms all baselines.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive PDF cue:** Second, we assess generalization to real-world monocular videos with occlusions using the HO3D dataset [10], which contains hand-object interaction sequences.
- **p. 8 / 4 Experiments - extractive PDF cue:** For evaluation, we use two datasets of unseen objects.
- **p. 10 / 4.2 Results - extractive PDF cue:** Future work could explore modeling non-rigid objects and integrate it with downstream tasks like robotic manipulation.
- **p. 7 / 4 Experiments - extractive PDF cue:** Unlike conventional few-view or image-to-3D setups that render from biased polar angles and fixed upright poses, our setting targets real-world freely moving object reconstruction, where ...
- **p. 7 / 4 Experiments - extractive PDF cue:** This difference is critical, as real-world data often includes partial views with unknown 7
- **p. 9 / 4.2 Results - extractive PDF cue:** Results are reported on GSO dataset.
- **p. 9 / 4.2 Results - extractive PDF cue:** 3.2, summarizing results on the GSO dataset in Table 2.
- **p. 10 / 4.2 Results - extractive PDF cue:** Lastly, our framework is currently limited to rigid objects.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); 4.2 Results (p. 8); 4. Experimental result reproducibility (p. 23); 7. Experiment statistical significance (p. 24); 8. Experiments compute resources (p. 24).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Even with fewer than four observations, OnlineSplatter significantly outperforms all baselines. | p. 8 (4.2 Results) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We therefore design a stage-wise evaluation protocol that examines performance across three distinct phases: 1) Early Stage (Tearly := {1 ≤t ≤4}): Tests the ... | p. 7 (4 Experiments) |
| 4.2 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Across all metrics and stages, OnlineSplatter achieves superior performance-improving up to +7.596 PSNR and +0.106 SSIM on GSO, and +4.981 PSNR and +0.092 SSIM ... | p. 8 (4.2 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Visual comparison of mesh results between different methods. Methods marked with an asterisk (*) indicate that additional pre- or post-processing steps were ... | p. 10 (Figure/Table caption) |
| 4.2 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our reconstructed outputs show significantly better visual quality and geometric accuracy as more observations become available. | p. 9 (4.2 Results) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive PDF cue:** Second, we assess generalization to real-world monocular videos with occlusions using the HO3D dataset [10], which contains hand-object interaction sequences.
- **p. 8 / 4 Experiments - extractive PDF cue:** For evaluation, we use two datasets of unseen objects.
- **p. 10 / 4.2 Results - extractive PDF cue:** Future work could explore modeling non-rigid objects and integrate it with downstream tasks like robotic manipulation.
- **p. 7 / 4 Experiments - extractive PDF cue:** Unlike conventional few-view or image-to-3D setups that render from biased polar angles and fixed upright poses, our setting targets real-world freely moving object reconstruction, where ...
- **p. 7 / 4 Experiments - extractive PDF cue:** This difference is critical, as real-world data often includes partial views with unknown 7
- **p. 9 / 4.2 Results - extractive PDF cue:** Results are reported on GSO dataset.
- **p. 9 / 4.2 Results - extractive PDF cue:** 3.2, summarizing results on the GSO dataset in Table 2.
- **p. 10 / 4.2 Results - extractive PDF cue:** Lastly, our framework is currently limited to rigid objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Outline of proposed OnlineSplatter. From the incoming stream of pose-free RGB frames, OnlineSplatter "splats" the observations into a canonical cloud of 3D Gaussians ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of OnlineSplatter Pipeline. The input to our framework consists of a stream of RGB images {Vt}N t=0, where object masks {Mt}N t=0 ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of different baselines on two datasets. Results are shown for early-stage, mid-stage, and late-stage settings. Best results are bolded and second best ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 3: Qualitative results of different baselines and our method on the GSO (left) and HO3D (right) datasets. We visualize the results at inference timestep ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Impact of dual-key object memory design. Results are reported on GSO dataset. Variants Early-Stage Mid-Stage Late-Stage Mavg ↑ Mavg ↑
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Impact of training strategy components. Results are reported on GSO dataset. 4.3 Ablations and Analysis In this section, we ablate different components of ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 4: Visual comparison of mesh results between different methods. Methods marked with an asterisk (*) indicate that additional pre- or post-processing steps were applied ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 4: List of mathematical notations used throughout the paper. 16

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Second, we assess generalization to real-world monocular videos with occlusions using the HO3D dataset [10], which contains hand-object interaction sequences. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | For evaluation, we use two datasets of unseen objects. | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 10 (4.2 Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 5 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3 Method), p. 4 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 3, where our method delivers notably better visual quality and geometric accuracy from early to late stages. | definition/direction/unit from same section | p. 8 (4.2 Results) |
| This underscores the strength of our Object Memory mechanism in leveraging temporal cues for progressive reconstruction refinement. | definition/direction/unit from same section | p. 8 (4.2 Results) |
| Our reconstructed outputs show significantly better visual quality and geometric accuracy as more observations become available. | definition/direction/unit from same section | p. 9 (4.2 Results) |
| Specifically: Dual-key Design: Removing the latent key severely degrades performance at all stages due to loss of visual-geometrical cues. | definition/direction/unit from same section | p. 9 (4.2 Results) |
| Loss Components: Removing the ray alignment (Lray) notably reduces convergence speed and stability, harming performance. | definition/direction/unit from same section | p. 10 (4.2 Results) |
| Excluding the visual hull (Lbg) penalty moderately degrades performance, underscoring its role in preserving object boundaries. | definition/direction/unit from same section | p. 10 (4.2 Results) |
| The stage-wise performance is then computed as: Mstage = 1 /Tstage/ P t∈Tstage P v∈Vtarget M( ˆRv,t, Vv) where M represents standard image quality ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We therefore design a stage-wise evaluation protocol that examines performance across three distinct phases: 1) Early Stage (Tearly := {1 ≤t ≤4}): Tests the ... | definition/direction/unit from same section | p. 7 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This section evaluates our approach by outlining the evaluation protocol, describing the datasets for training and testing, comparing against state-of-the-art baselines, and conducting ablation ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Even with fewer than four observations, OnlineSplatter significantly outperforms all baselines. | comparison identity and matched condition | p. 8 (4.2 Results) |
| Baselines using explicit frame selection often exhibit unstable or stagnant performance. | comparison identity and matched condition | p. 8 (4.2 Results) |
| FSOdist4 NPSdist3 GT Ours Early-Stage(t=4) Early-Stage(t=4) (t=16) Late-Stage (t=16) Late-Stage Figure 3: Qualitative results of different baselines and our method on the GSO (left) ... | comparison identity and matched condition | p. 9 (4.2 Results) |
| To demonstrate our approach's efficacy, we convert our final 3DGS representation into meshes and visually compare it comprehensively with state-of-the-art methods from different paradigms. | comparison identity and matched condition | p. 10 (4.2 Results) |
| Memory Sparsification: Our sparsification strategy based on usage rate and spatial coverage outperforms random pruning, particularly in later stages, showing the efficacy of our ... | comparison identity and matched condition | p. 10 (4.2 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6: Visualization of the effect of without (top row) and with (bottom row) ray alignment loss Lray over 1K -10K training steps. The ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| This section evaluates our approach by outlining the evaluation protocol, describing the datasets for training and testing, comparing against state-of-the-art baselines, and conducting ablation ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| 4.3 Ablations and Analysis In this section, we ablate different components of our method and analyze the results. | component/input/data sensitivity | p. 9 (4.2 Results) |
| Variants Early-Stage Mid-Stage Late-Stage Mavg ↑ Mavg ↑ Mavg ↑ Ours 0.699 0.734 0.810 w/o staged training 0.545 0.582 0.588 w/o ray loss (Lray) ... | component/input/data sensitivity | p. 9 (4.2 Results) |
| 3.3) through ablation studies and show results in Table 3, demonstrating: Staged Training: Removing the twostage training (warm-up followed by main training) by using ... | component/input/data sensitivity | p. 10 (4.2 Results) |
| Loss Components: Removing the ray alignment (Lray) notably reduces convergence speed and stability, harming performance. | component/input/data sensitivity | p. 10 (4.2 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these limitations, we propose a novel object-centric memory mechanism, Dual-Key 3D Object Memory, that consists of a key-value memory bank. | Even with fewer than four observations, OnlineSplatter significantly outperforms all baselines. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2 Results), p. 7 (4 Experiments), p. 8 (4.2 Results), p. 10 (Figure/Table caption), p. 9 (4.2 Results), p. 10 (4.2 Results) |
| Primary metric/result | We therefore design a stage-wise evaluation protocol that examines performance across three distinct phases: 1) Early Stage (Tearly := {1 ≤t ≤4}): Tests the ... | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive PDF cue:** For each test sequence of N frames {Vn}N n=1, we split the frames into two sets: Input frames (Vinput): A randomly sampled subset of N ...
- **p. 8 / 4 Experiments - extractive PDF cue:** First, we test on Google Scanned Objects (GSO) [7], rendering 36 frames per object using our training pipeline (each with distinct lighting and motion).
- **p. 8 / 4 Experiments - extractive PDF cue:** To adapt it online, we introduce two frame selection strategies for each timestep: (1) rand4: randomly selects 4 frames from past observations (FSOrand4); (2) dist4: ...
- **p. 7 / 3 Method - extractive PDF cue:** We use 8x A100 GPUs for 250K steps with a batch size of 64 in the Warm-up Training stage and 500K steps with a batch ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 5 Limitations and Future Work Our current framework has some limitations that warrant attention. | p. 10 (4.2 Results) |
| body limitation/failure cue | Baselines using explicit frame selection often exhibit unstable or stagnant performance. | p. 8 (4.2 Results) |
| body limitation/failure cue | Figure 5: Impact of Training Data Quantity and Quality. C.2 Impact of Ray Alignment Loss in Geometrical Supervision. While photometric RGB-based loss can effectively ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | Future work could explore hybrid representations that maintain both rendering efficiency and mesh compatibility. | p. 10 (4.2 Results) |
| body limitation/failure cue | Second, we assess generalization to real-world monocular videos with occlusions using the HO3D dataset [10], which contains hand-object interaction sequences. | p. 8 (4 Experiments) |
| body limitation/failure cue | Specifically: Dual-key Design: Removing the latent key severely degrades performance at all stages due to loss of visual-geometrical cues. | p. 9 (4.2 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We visualize the results at inference timestep t = 4 and t = 16, which corresponds to the early-stage and late-stage settings, respectively. | p. 9 (4.2 Results) |
| We use 8x A100 GPUs for 250K steps with a batch size of 64 in the Warm-up Training stage and 500K steps with a ... | p. 7 (3 Method) |
| The stage-wise performance is then computed as: Mstage = 1 /Tstage/ P t∈Tstage P v∈Vtarget M( ˆRv,t, Vv) where M represents standard image quality ... | p. 7 (4 Experiments) |
| To adapt it online, we introduce two frame selection strategies for each timestep: (1) rand4: randomly selects 4 frames from past observations (FSOrand4); (2) ... | p. 8 (4 Experiments) |
| Variants Early-Stage Mid-Stage Late-Stage Mavg ↑ Mavg ↑ Mavg ↑ Ours 0.699 0.734 0.810 w/o latent key 0.545 0.582 0.596 w/o direction key 0.699 ... | p. 9 (4.2 Results) |
| Methods marked with an asterisk (*) indicate that additional pre- or post-processing steps were applied to generate the visual results. | p. 10 (4.2 Results) |
| Specifically, k(D) t is computed based on the R3 axis-rotation of the object orientation {θt, ϕt, γt}: k(D) t := (sin ϕt cos θt, ... | p. 5 (3 Method) |
| This dual-encoder design enables our model to leverage both rich visual priors and geometry-aware features. | p. 3 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 4.2 Results - extractive PDF cue:** 5 Limitations and Future Work Our current framework has some limitations that warrant attention.
- **p. 8 / 4.2 Results - extractive PDF cue:** Baselines using explicit frame selection often exhibit unstable or stagnant performance.
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 5: Impact of Training Data Quantity and Quality. C.2 Impact of Ray Alignment Loss in Geometrical Supervision. While photometric RGB-based loss can effectively supervise ...
- **p. 10 / 4.2 Results - extractive PDF cue:** Future work could explore hybrid representations that maintain both rendering efficiency and mesh compatibility.
- **p. 8 / 4 Experiments - extractive PDF cue:** Second, we assess generalization to real-world monocular videos with occlusions using the HO3D dataset [10], which contains hand-object interaction sequences.
- **p. 9 / 4.2 Results - extractive PDF cue:** Specifically: Dual-key Design: Removing the latent key severely degrades performance at all stages due to loss of visual-geometrical cues.

- **PDF anchors reviewed:** datasets p. 8 (4 Experiments), p. 8 (4 Experiments), p. 10 (4.2 Results), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4.2 Results), metrics p. 8 (4.2 Results), p. 8 (4.2 Results), p. 9 (4.2 Results), p. 9 (4.2 Results), p. 10 (4.2 Results), p. 10 (4.2 Results), baselines p. 7 (4 Experiments), p. 8 (4.2 Results), p. 8 (4.2 Results), p. 9 (4.2 Results), p. 10 (4.2 Results), p. 10 (4.2 Results), results p. 8 (4.2 Results), p. 7 (4 Experiments), p. 8 (4.2 Results), p. 10 (Figure/Table caption), p. 9 (4.2 Results), p. 10 (4.2 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
