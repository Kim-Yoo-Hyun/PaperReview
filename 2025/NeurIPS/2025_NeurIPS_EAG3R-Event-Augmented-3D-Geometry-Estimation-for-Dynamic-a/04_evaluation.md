# Evaluation - EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Lf0W2gmNBg; PDF retrieval source: https://arxiv.org/pdf/2512.00771. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments)): Each addition improves performance, with the full EAG3R system achieving the best results.

## Evaluation Body Digest

- **p. 21 / A.7 Generalization to More Datasets - extractive body cue:** To assess the model's performance in high-dynamic-range (HDR) conditions, we evaluated EAG3R on the challenging M3ED robot dog dataset penno_plaza_lights split, which features rapid motion ...
- **p. 18 / A.4 Summary of Existing Event-RGB Datasets - extractive body cue:** Our choice of the MVSEC dataset was guided by the strict requirements of our task: robust 3D geometry estimation in dynamic scenes under extreme lighting.
- **p. 18 / A.4 Summary of Existing Event-RGB Datasets - extractive body cue:** Dataset Low-light Dynamic RGB Depth Sensor GT Pose Platform Environment DSEC ✓ ✓ ✓ LiDAR-16 ✗ Car Outdoor UZH-FPV ✗ ✓ ✓ ✗ MoCap Drone ...
- **p. 21 / A.7 Generalization to More Datasets - extractive body cue:** To demonstrate EAG3R's scalability, we conducted additional experiments on MVSEC indoor and M3ED datasets, covering diverse environments (indoor, outdoor, night, HDR), sensor platforms (drones, robots, ...
- **p. 7 / 4 Experiments - extractive body cue:** The Event Adapter is pre-trained on the ETartanAir dataset.
- **p. 7 / 4 Experiments - extractive body cue:** Given the scarcity of such data, we selected the Multi Vehicle Stereo Event Camera (MVSEC) dataset [78].
- **p. 8 / 4 Experiments - extractive body cue:** Prior methods such as DUSt3R and MonST3R serve as RGB-based baselines, with MonST3R extending pointmap prediction to dynamic scenes and Easi3R variants incorporating motion-aware masking.
- **p. 16 / A.1 Dataset Processing - extractive body cue:** The Multi-Vehicle Stereo Event Camera (MVSEC) dataset integrates three distinct sensor modalities, each with independent timestamps: Active Pixel Sensor (APS) for frame-based images, Dynamic Vision ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); A.1 Dataset Processing (p. 16); A.2 Video Depth Estimation Results on MVSEC (p. 17); A.3 Dynamic Reconstruction Results (p. 17); A.4 Summary of Existing Event-RGB Datasets (p. 18); A.7 Generalization to More Datasets (p. 21).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Each addition improves performance, with the full EAG3R system achieving the best results. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fine-tuning MonST3R improves its performance across 7 | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | However, applying RetinexFormer, a widely used image enhancement network, as a preprocessing light-up step (denoted as (LightUp)) does not yield significant improvements and, in ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, RGB-only baselines such as DUSt3R fail under extreme low-light conditions, while MonST3R offers improved results. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Despite these enhancements, our proposed EAG3R consistently achieves the best performance across most metrics and sequences. | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 21 / A.7 Generalization to More Datasets - extractive body cue:** To assess the model's performance in high-dynamic-range (HDR) conditions, we evaluated EAG3R on the challenging M3ED robot dog dataset penno_plaza_lights split, which features rapid motion ...
- **p. 18 / A.4 Summary of Existing Event-RGB Datasets - extractive body cue:** Our choice of the MVSEC dataset was guided by the strict requirements of our task: robust 3D geometry estimation in dynamic scenes under extreme lighting.
- **p. 18 / A.4 Summary of Existing Event-RGB Datasets - extractive body cue:** Dataset Low-light Dynamic RGB Depth Sensor GT Pose Platform Environment DSEC ✓ ✓ ✓ LiDAR-16 ✗ Car Outdoor UZH-FPV ✗ ✓ ✓ ✗ MoCap Drone ...
- **p. 21 / A.7 Generalization to More Datasets - extractive body cue:** To demonstrate EAG3R's scalability, we conducted additional experiments on MVSEC indoor and M3ED datasets, covering diverse environments (indoor, outdoor, night, HDR), sensor platforms (drones, robots, ...
- **p. 7 / 4 Experiments - extractive body cue:** The Event Adapter is pre-trained on the ETartanAir dataset.
- **p. 7 / 4 Experiments - extractive body cue:** Given the scarcity of such data, we selected the Multi Vehicle Stereo Event Camera (MVSEC) dataset [78].
- **p. 8 / 4 Experiments - extractive body cue:** Prior methods such as DUSt3R and MonST3R serve as RGB-based baselines, with MonST3R extending pointmap prediction to dynamic scenes and Easi3R variants incorporating motion-aware masking.
- **p. 16 / A.1 Dataset Processing - extractive body cue:** The Multi-Vehicle Stereo Event Camera (MVSEC) dataset integrates three distinct sensor modalities, each with independent timestamps: Active Pixel Sensor (APS) for frame-based images, Dynamic Vision ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: EAG3R pipeline for event-augmented dynamic 3D reconstruction. EAG3R processes a low-light video and its corresponding event stream within a temporal window, extracting pairwise ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: EAG3R network. Left: The DUSt3R (MonST3R) architecture with reference and source views processed via ViT encoder-decoder structure. Middle: Our method (only the upstream ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Event-based photometric consistency loss. Harris corners are detected on the input image to define salient patches. Observed brightness increments are computed by integrating ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Monocular depth estimation performance on nighttime scenes. Evaluation is conducted on the MVSEC Night1, Night2, and Night3 sequences. Standard metrics are used: Abs ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Camera pose estimation on all MVSEC nighttime sequences. Evaluation is conducted on the MVSEC Night1, Night2, and Night3 sequences. Standard metrics are used: ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Comparison of estimated camera trajectories. The predicted trajectories (solid blue) from DUS3R, MonST3R, and EAG3R are evaluated against the ground truth (dashed gray). ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Ablation study on depth estimation performance on the Night3 sequence. Modules are incrementally added to the MonST3R baseline. Each addition improves performance, with ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To assess the model's performance in high-dynamic-range (HDR) conditions, we evaluated EAG3R on the challenging M3ED robot dog dataset penno_plaza_lights split, which features rapid ... | embodiment, simulator version and control stack | p. 21 (A.7 Generalization to More Datasets), p. 18 (A.4 Summary of Existing Event-RGB Datasets) |
| Task/environment | Our choice of the MVSEC dataset was guided by the strict requirements of our task: robust 3D geometry estimation in dynamic scenes under extreme ... | reset, timeout, object/scene variation | p. 18 (A.4 Summary of Existing Event-RGB Datasets), p. 18 (A.4 Summary of Existing Event-RGB Datasets) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report results using standard metrics: Absolute Relative Error (Abs Rel ↓), Scale-invariant RMSE log (RMSE log ↓), and the threshold accuracy δ < ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Following standard protocol, we report Absolute Relative Error (Abs Rel ↓), RMSE log ↓, and δ < 1.25 (↑) over all frames in each ... | definition/direction/unit from same section | p. 17 (A.2 Video Depth Estimation Results on MVSEC) |
| A.1, conventional RGB-based baselines such as DUSt3R and MonST3R suffer from errors due to degraded visual signals at night, and even Easi3R exhibit limited ... | definition/direction/unit from same section | p. 17 (A.2 Video Depth Estimation Results on MVSEC) |
| Method Abs Rel ↓ δ < 1.25 ↑ RMSE log ↓ MonST3R (Baseline) 0.317 0.453 0.418 MonST3R (Finetune) 0.302 0.509 0.401 + Event 0.297 ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| As summarized in Table A.13, the results exhibit low variance and consistent performance across all key metrics, confirming the model's robustness and stability during ... | definition/direction/unit from same section | p. 21 (A.8 Statistical Analysis and Robustness Validation) |
| As shown in Table A.10, EAG3R achieves substantially higher pose estimation accuracy than both the MonST3R baseline and its scene-finetuned variant across all key ... | definition/direction/unit from same section | p. 21 (A.7 Generalization to More Datasets) |
| Fine-tuning MonST3R improves its performance across 7 | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Despite these enhancements, our proposed EAG3R consistently achieves the best performance across most metrics and sequences. | definition/direction/unit from same section | p. 8 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method, EAG3R, outperforms all baselines across all three nighttime sequences, indicating both accurate and reliable depth predictions. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Sequence Length 20 40 60 80 100 Max Memory (GB) 14.02 20.19 27.78 37.40 46.49 Overall, the results confirm that EAG3R maintains near-linear computational ... | comparison identity and matched condition | p. 20 (A.6 Runtime and Memory Analysis) |
| As summarized in Table A.11, EAG3R consistently outperforms the baseline in all three outdoor sequences, demonstrating reliable pose estimation even in high-speed and high-contrast ... | comparison identity and matched condition | p. 21 (A.7 Generalization to More Datasets) |
| We compare EAG3R with state-of-the-art pose free learning-based reconstruction method, including DUSt3R [64], MonST3R [72], and Easi3R [10]. | comparison identity and matched condition | p. 7 (4 Experiments) |
| 4.1 Experiment Details For training, we fine-tune the MonST3R baseline by training its ViT-Base decoder, DPT heads, Enhancement Net, and the Event Adapter. | comparison identity and matched condition | p. 7 (4 Experiments) |
| 2, RGB-only baselines such as DUSt3R fail under extreme low-light conditions, while MonST3R offers improved results. | comparison identity and matched condition | p. 8 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fine-tuning MonST3R leads to substantial gains, particularly in RPE trans and RPE rot, with further improvements from Easi3R variants. | component/input/data sensitivity | p. 8 (4 Experiments) |
| 4.5 Ablation Study To better understand the contribution of each design component in EAG3R, we conduct a systematic ablation study on the MVSEC outdoor_night3 ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| We perform ablation studies in Section 4.5. | component/input/data sensitivity | p. 7 (4 Experiments) |
| We report results using standard metrics: Absolute Relative Error (Abs Rel ↓), Scale-invariant RMSE log (RMSE log ↓), and the threshold accuracy δ < ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| Prior methods such as DUSt3R and MonST3R serve as RGB-based baselines, with MonST3R extending pointmap prediction to dynamic scenes and Easi3R variants incorporating motion-aware ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| Table 3: Ablation study on depth estimation performance on the Night3 sequence. Modules are incrementally added to the MonST3R baseline. Each addition improves performance, ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose EAG3R, an event-augemented MonST3R framework to enhance pointmapbased 3D geometry estimation under dynamic and extremely low-light conditions. | Each addition improves performance, with the full EAG3R system achieving the best results. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | Fine-tuning MonST3R improves its performance across 7 | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** Fine-tuning is performed for 25 epochs, using 8,000 image-event pairs per epoch.
- **p. 7 / 4 Experiments - extractive body cue:** The training process completes in approximately 24 hours on 4 NVIDIA RTX 3090 GPUs.
- **p. 16 / A.1 Dataset Processing - extractive body cue:** The Velodyne Puck LITE provides depth data at a fixed frequency of 20 Hz, while the APS captures frames at approximately 100 Hz during daytime ...
- **p. 20 / A.6 Runtime and Memory Analysis - extractive body cue:** Compared to MonST3R, EAG3R introduces only a minor overhead of approximately +0.4 GB VRAM, +0.11 TFLOPs, and +1.2 s per forward pass.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In particular, we attempted to train our model using synthetic events generated by V2E [20], but observed that the low fidelity of these generated ... | p. 22 (A.9 Limitations) |
| body limitation/failure cue | We discuss limitations and broader impact in the appendix. | p. 9 (5 Conclusion) |
| body limitation/failure cue | Despite the strong empirical performance of EAG3R, several limitations remain: Limited dataset availability. | p. 21 (A.9 Limitations) |
| body limitation/failure cue | To address this, our future work aims to curate a diverse dataset featuring high-quality, real-world event-RGB pairs across varied lighting and motion scenarios. | p. 21 (A.9 Limitations) |
| body limitation/failure cue | However, applying RetinexFormer, a widely used image enhancement network, as a preprocessing light-up step (denoted as (LightUp)) does not yield significant improvements and, in ... | p. 7 (4 Experiments) |
| body limitation/failure cue | We presented EAG3R, a event-augmented framework for robust 3D geometry estimation under dynamic and low-light conditions. | p. 9 (5 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We employ the AdamW optimizer with a learning rate of 5 × 10-5 and a mini-batch size of 4 per GPU. | p. 7 (4 Experiments) |
| We use the Adam optimizer for 300 iterations with a learning rate of 0.01. | p. 7 (4 Experiments) |
| Consequently, both runtime and memory cost scale linearly with the total number of frames, as confirmed by our experiments running on an NVIDIA A100 ... | p. 20 (A.6 Runtime and Memory Analysis) |
| To assess the computational efficiency of EAG3R, we conduct a detailed runtime and memory analysis. | p. 20 (A.6 Runtime and Memory Analysis) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 22 / A.9 Limitations - extractive body cue:** In particular, we attempted to train our model using synthetic events generated by V2E [20], but observed that the low fidelity of these generated events ...
- **p. 9 / 5 Conclusion - extractive body cue:** We discuss limitations and broader impact in the appendix.
- **p. 21 / A.9 Limitations - extractive body cue:** Despite the strong empirical performance of EAG3R, several limitations remain: Limited dataset availability.
- **p. 21 / A.9 Limitations - extractive body cue:** To address this, our future work aims to curate a diverse dataset featuring high-quality, real-world event-RGB pairs across varied lighting and motion scenarios.
- **p. 7 / 4 Experiments - extractive body cue:** However, applying RetinexFormer, a widely used image enhancement network, as a preprocessing light-up step (denoted as (LightUp)) does not yield significant improvements and, in some ...
- **p. 9 / 5 Conclusion - extractive body cue:** We presented EAG3R, a event-augmented framework for robust 3D geometry estimation under dynamic and low-light conditions.

- **Evidence anchors reviewed:** datasets p. 21 (A.7 Generalization to More Datasets), p. 18 (A.4 Summary of Existing Event-RGB Datasets), p. 18 (A.4 Summary of Existing Event-RGB Datasets), p. 21 (A.7 Generalization to More Datasets), p. 7 (4 Experiments), p. 7 (4 Experiments), metrics p. 7 (4 Experiments), p. 17 (A.2 Video Depth Estimation Results on MVSEC), p. 17 (A.2 Video Depth Estimation Results on MVSEC), p. 9 (4 Experiments), p. 21 (A.8 Statistical Analysis and Robustness Validation), p. 21 (A.7 Generalization to More Datasets), baselines p. 8 (4 Experiments), p. 20 (A.6 Runtime and Memory Analysis), p. 21 (A.7 Generalization to More Datasets), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), results p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
