# Evaluation - Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=nv3q3crc5D; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245566. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 EXPERIMENTS), p. 1 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS)): 5.2 TRACKING PERFORMANCE As shown in Table 1, Flash-Mono significantly outperformed all traditional and GS-SLAM baseline methods.

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5.1 EXPERIMENTAL SETUP We evaluate our system on three challenging real-world datasets: ScanNet (Dai et al., 2017a), BundleFusion (Dai et al., 2017b), and KITTI (Geiger ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 5.4 OUTDOOR EVALUATION ON KITTI We further evaluate Flash-Mono on the KITTI benchmark to assess generalization to large-scale outdoor environments.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** ScanNet and BundleFusion consist of large-scale indoor scenes with motion blur and diverse lighting conditions.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** On most scenes, we also surpassed MASt3R-SLAM, a recent feed-forward SLAM system.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Since MonoGS and DepthGS are designed primarily for indoor scenes, they often fail under the large scale variance and dynamics in KITTI; therefore, we mainly ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We evaluate tracking accuracy using Absolute Trajectory Error (ATE RMSE) and rendering quality via PSNR, SSIM, and LPIPS.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** We achieve a lower Depth L1 error, suggesting a more accurate underlying 3D scene reconstruction.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** For ScanNet and BundleFusion, we further evaluate geometric quality with scale-aligned Depth L1 error.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); B MORE EXPERIMENTAL SETUP AND RESULTS (p. 14); B.3 MORE QUALITATIVE RESULTS (p. 15).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5.2 TRACKING PERFORMANCE As shown in Table 1, Flash-Mono significantly outperformed all traditional and GS-SLAM baseline methods. | p. 8 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: Our Results for Reconstruction and Rendering & Tracking & Speed Metrics. Our method reconstructs high-quality Gaussian maps in complex scenes with multiple ... | p. 1 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Although we perform only 20 optimization iterations per keyframe (a 10x reduction compared to the 250 iterations used by MonoGS (Matsuki et al., 2024) ... | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We achieve a lower Depth L1 error, suggesting a more accurate underlying 3D scene reconstruction. | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Without refinement (0 iterations), the direct output from our feed-forward model achieves a PSNR of 20.14. | p. 10 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5.1 EXPERIMENTAL SETUP We evaluate our system on three challenging real-world datasets: ScanNet (Dai et al., 2017a), BundleFusion (Dai et al., 2017b), and KITTI (Geiger ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 5.4 OUTDOOR EVALUATION ON KITTI We further evaluate Flash-Mono on the KITTI benchmark to assess generalization to large-scale outdoor environments.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** ScanNet and BundleFusion consist of large-scale indoor scenes with motion blur and diverse lighting conditions.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** On most scenes, we also surpassed MASt3R-SLAM, a recent feed-forward SLAM system.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Since MonoGS and DepthGS are designed primarily for indoor scenes, they often fail under the large scale variance and dynamics in KITTI; therefore, we mainly ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Our Results for Reconstruction and Rendering & Tracking & Speed Metrics. Our method reconstructs high-quality Gaussian maps in complex scenes with multiple rooms ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Pipeline. For each new frame, our recurrent model jointly infers the camera pose and per- pixel 2DGS attributes conditioned on a hidden state. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative Rendering Results. Baselines. We compare Flash-Mono with three state-of-the-art monocular GS-SLAM systems on both mapping and tracking quality: MonoGS (Matsuki et al., ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: ATE RMSE (cm) on ScanNetV1 and BundleFusion datasets. Lower is better. We mark the first and second best results. ATE [cm]↓ ScanNetV1 BundleFusion ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Mapping quality on ScanNetV1 and BundleFusion. Higher is better for SSIM/PSNR, lower is better for LPIPS. We mark the first and second best ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative Analysis on Rendered Depth. This highlights the effectiveness of our Predict-and-Refine paradigm: high-quality Gaussians pre- dicted by our foundation model reduce the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: ATE RMSE (m) on KITTI Odometry. Lower is better. ATE RMSE [m]↓ 00 05 06 07 08 28
- **p. 10 / Figure/Table caption - extractive body cue:** Table 4: Rendering quality on KITTI Odometry. Higher is better for PSNR/SSIM, lower is better for LPIPS.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5.1 EXPERIMENTAL SETUP We evaluate our system on three challenging real-world datasets: ScanNet (Dai et al., 2017a), BundleFusion (Dai et al., 2017b), and KITTI ... | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Task/environment | 5.4 OUTDOOR EVALUATION ON KITTI We further evaluate Flash-Mono on the KITTI benchmark to assess generalization to large-scale outdoor environments. | reset, timeout, object/scene variation | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate tracking accuracy using Absolute Trajectory Error (ATE RMSE) and rendering quality via PSNR, SSIM, and LPIPS. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| We achieve a lower Depth L1 error, suggesting a more accurate underlying 3D scene reconstruction. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| For ScanNet and BundleFusion, we further evaluate geometric quality with scale-aligned Depth L1 error. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| We also compare against leading monocular SLAM systems renowned for pose accuracy, although they do not produce dense renderings, including ORBSLAM3 (Campos et al., ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| The scale-aligned Depth L1 error is evaluated in Table 5. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| The lowest error of 0.106 was observed with a clip length of 8 frames. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Second, we examined the influence of submap clip length on tracking accuracy (ATE RMSE). | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Figure 1: Our Results for Reconstruction and Rendering & Tracking & Speed Metrics. Our method reconstructs high-quality Gaussian maps in complex scenes with multiple ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 5.2 TRACKING PERFORMANCE As shown in Table 1, Flash-Mono significantly outperformed all traditional and GS-SLAM baseline methods. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Third, we compared our hidden state-based loop closure against a traditional PnP+RANSAC baseline and a configuration with no loop closure. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |
| Figure 3: Qualitative Rendering Results. Baselines. We compare Flash-Mono with three state-of-the-art monocular GS-SLAM systems on both mapping and tracking quality: MonoGS (Matsuki et ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 1: Our Results for Reconstruction and Rendering & Tracking & Speed Metrics. Our method reconstructs high-quality Gaussian maps in complex scenes with multiple ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 7: Qualitative Analysis on reconstructed ScanNet scene 0054. All baselines failed to reconstruct the scene. C MODEL SIZE AND ACCELERATION C.1 MODEL SIZE ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |
| Without refinement (0 iterations), the direct output from our feed-forward model achieves a PSNR of 20.14. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| MonoGS 1.19 1.20 DepthGS 0.49 0.23 S3PO-GS 0.52 0.85 Ours 0.34 0.21 5.5 ABLATION We conducted ablation studies to analyze the impact of key ... | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| First, we evaluated the effect of backend refinement iterations on rendering quality (PSNR). | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| Table 7: Detailed breakdown of Flash-Mono model parameters. Component Total Parameters Encoder | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are: • We propose a real-time (10 FPS+) monocular GS-SLAM framework that leverages a recurrent feed-forward model to predict ... | 5.2 TRACKING PERFORMANCE As shown in Table 1, Flash-Mono significantly outperformed all traditional and GS-SLAM baseline methods. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 EXPERIMENTS), p. 1 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Primary metric/result | Figure 1: Our Results for Reconstruction and Rendering & Tracking & Speed Metrics. Our method reconstructs high-quality Gaussian maps in complex scenes with multiple ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** All experiments are conducted on a single RTX 4090 GPU paired with an Intel Xeon 6133 CPU (2.50GHz).
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Although we perform only 20 optimization iterations per keyframe (a 10x reduction compared to the 250 iterations used by MonoGS (Matsuki et al., 2024) and ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** The lowest error of 0.106 was observed with a clip length of 8 frames.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Shorter lengths resulted in higher error, suggesting insufficient temporal context, while lengths greater than 16 frames also increased the error, which points to the accumulation ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our method outperforms others in both rendering quality and trajectory accuracy, offering a 10x speedup over contemporary monocular GS-SLAM methods.
- **p. 1 / ABSTRACT - extractive body cue:** By directly predicting Gaussian attributes, our method bypasses the burdensome per-frame optimization required in optimization-based GS-SLAM, achieving a 10x speedup while ensuring high-quality rendering.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | On KITTI, we primarily compare against S3POGS, as we encountered frequent failures while evaluating other indoor-focused GS-SLAM baselines due to the large-scale and high ... | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | Furthermore, we introduced a novel loop closure mechanism that enables robust Sim(3) optimization to correct scale and pose drift inherent in monocular systems, leading ... | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | Since MonoGS and DepthGS are designed primarily for indoor scenes, they often fail under the large scale variance and dynamics in KITTI; therefore, we ... | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | Method Metric 00 05 06 07 08 28 S3PO-GS PSNR ↑ 16.65 15.64 13.55 fail 17.25 15.30 SSIM ↑ 0.5409 0.5320 0.4726 fail 0.5912 ... | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | Figure 7: Qualitative Analysis on reconstructed ScanNet scene 0054. All baselines failed to reconstruct the scene. C MODEL SIZE AND ACCELERATION C.1 MODEL SIZE ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Figure 9: Case Study: Robust Relocalization Under Environmental Changes. The model gen- erates a hidden state from 8 context views captured at night (curtains ... | p. 20 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All experiments are conducted on a single RTX 4090 GPU paired with an Intel Xeon 6133 CPU (2.50GHz). | p. 7 (5 EXPERIMENTS) |
| Since monocular SLAM has inherent scale ambiguity, we compute ATE after Sim(3) alignment to ground truth. | p. 7 (5 EXPERIMENTS) |
| Applying 10 refinement iterations increases the PSNR to 22.41, indicating that the model provides a strong initial prediction that can be efficiently improved by ... | p. 10 (5 EXPERIMENTS) |
| Since a single iteration takes approximately 20 ms, the total training time per keyframe is roughly one second, inevitably resulting in slow overall performance. | p. 3 (1 INTRODUCTION) |
| Each incoming image is first converted into a set of visual tokens Ft ∈RK×C by a ViT encoder. | p. 5 (1 INTRODUCTION) |
| A learnable pose token zt, concatenated with Ft, is processed by the decoders to aggregate geometric cues for pose estimation. | p. 5 (1 INTRODUCTION) |
| The relative pose is then computed as Tj→i = (Ta j )-1Ta i . | p. 6 (1 INTRODUCTION) |
| The computed Sim(3) constraint enables global optimization of the entire trajectory via a pose graph. | p. 6 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** On KITTI, we primarily compare against S3POGS, as we encountered frequent failures while evaluating other indoor-focused GS-SLAM baselines due to the large-scale and high dynamic ...
- **p. 10 / 6 CONCLUSION - extractive body cue:** Furthermore, we introduced a novel loop closure mechanism that enables robust Sim(3) optimization to correct scale and pose drift inherent in monocular systems, leading to ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Since MonoGS and DepthGS are designed primarily for indoor scenes, they often fail under the large scale variance and dynamics in KITTI; therefore, we mainly ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Method Metric 00 05 06 07 08 28 S3PO-GS PSNR ↑ 16.65 15.64 13.55 fail 17.25 15.30 SSIM ↑ 0.5409 0.5320 0.4726 fail 0.5912 0.5053 ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 7: Qualitative Analysis on reconstructed ScanNet scene 0054. All baselines failed to reconstruct the scene. C MODEL SIZE AND ACCELERATION C.1 MODEL SIZE To ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 9: Case Study: Robust Relocalization Under Environmental Changes. The model gen- erates a hidden state from 8 context views captured at night (curtains closed, ...

- **Evidence anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), metrics p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), baselines p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 16 (Figure/Table caption), p. 10 (5 EXPERIMENTS), results p. 8 (5 EXPERIMENTS), p. 1 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
