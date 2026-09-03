# Evaluation - ODG: Occupancy Prediction Using Dual Gaussians

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=CkmLys7ipp; PDF retrieval source: https://arxiv.org/pdf/2506.09417.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 3 (Figure/Table caption)): ODG achieves consistent improvement across all dynamic categories.

## Evaluation Body Digest

- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Experiment Setup Datasets: We evaluate our model on the Occ3D benchmark [48] which bootstraps the nuScenes [6] and Waymo-Open [43] dataset.∗nuScenes consists of 1,000 ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.2 Evaluation Results In this section, we report evaluation results on the Occ3D benchmark [48] and compare with latest state-of-the-art methods. nuScenes Our results on ...
- **p. 9 / 4 Experiments - extractive body cue:** Our extensive experiments on the Occ3D-nuScenes and Occ3D-Waymo benchmark demonstrates ODG sets new state-of-the-art results while maintaining highly competitive efficiency.
- **p. 6 / 4 Experiments - extractive body cue:** On nuScenes, we resize input images to the resolution of 256 × 704.
- **p. 8 / 4 Experiments - extractive body cue:** For all our ablation studies, we adopt ODG-T and train on the Occ3D-nuScenes for 24 epochs.
- **p. 8 / 4 Experiments - extractive body cue:** Waymo We further evaluate our ODG on the Occ3D-Waymo dataset and the results are presented in Tab.
- **p. 7 / 4 Experiments - extractive body cue:** It is worth noting that given our specific design to attend to the dynamic agents in the scene, we show significant improvement when examining the ...
- **p. 9 / 4 Experiments - extractive body cue:** To make ODG attend to moving objects, we expand the standard 3D Gaussian properties of dynamic queries with 3D bounding box attributes, which effectively guides ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | ODG achieves consistent improvement across all dynamic categories. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Specifically, ODG-T (8f) achieves an mIoU of 35.54 with a RayIoU of 39.2, outperforming OPUS-T (8f) who has an mIoU of 33.2 (-2.34) and ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Comp mIoU RayIoU ✓ 31.17 35.7 ✓ ✓ 31.78 36.2 We posit that running self attention on all features in an exhaustive manner makes ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In our experiments, we first tried performing cross attention with dynamic query features serving as queries, and static query features as keys and values, ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4, this resulted in a noticeable improvement both in mIoU and RayIoU, with mIoU+0.69 and RayIoU+0.70. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Experiment Setup Datasets: We evaluate our model on the Occ3D benchmark [48] which bootstraps the nuScenes [6] and Waymo-Open [43] dataset.∗nuScenes consists of 1,000 ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.2 Evaluation Results In this section, we report evaluation results on the Occ3D benchmark [48] and compare with latest state-of-the-art methods. nuScenes Our results on ...
- **p. 9 / 4 Experiments - extractive body cue:** Our extensive experiments on the Occ3D-nuScenes and Occ3D-Waymo benchmark demonstrates ODG sets new state-of-the-art results while maintaining highly competitive efficiency.
- **p. 6 / 4 Experiments - extractive body cue:** On nuScenes, we resize input images to the resolution of 256 × 704.
- **p. 8 / 4 Experiments - extractive body cue:** For all our ablation studies, we adopt ODG-T and train on the Occ3D-nuScenes for 24 epochs.
- **p. 8 / 4 Experiments - extractive body cue:** Waymo We further evaluate our ODG on the Occ3D-Waymo dataset and the results are presented in Tab.
- **p. 7 / 4 Experiments - extractive body cue:** It is worth noting that given our specific design to attend to the dynamic agents in the scene, we show significant improvement when examining the ...
- **p. 9 / 4 Experiments - extractive body cue:** To make ODG attend to moving objects, we expand the standard 3D Gaussian properties of dynamic queries with 3D bounding box attributes, which effectively guides ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Overview of proposed ODG, where we model the dynamic and static elements of the scene with two separate sets of Gaussian queries. Dual-query ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 3D semantic occupancy results on Occ3D-nuScenes validation set [6, 48]. Cons. Veh stands for "Construction Vehicle" and Dri. Sur stands for "Drivable Surface". ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2: Visualization of ODG prediction on the Occ3D-nuScenes [48, 6] validation set. The ODG can capture all the vehicles on a gloomy rainy day. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Occupancy prediction results over key dynamic object classes on Occ3D-nuScenes [48] validation set. ODG achieves consistent improvement across all dynamic categories. Bold/Underline: Best/second ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: 3D semantic occupancy results on Occ3D-Waymo validation set [43, 48]. GO stands for "General Object". Traf. Light stands for "Traffic Light" and Cons. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of ODG prediction on the Occ3D-Waymo [48, 43] validation set. Waymo We further evaluate our ODG on the Occ3D-Waymo dataset and the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Tab. 3. We note that Occ3D-Waymo is a much less well evaluated occupancy benchmark especially for camera-only methods, given its challenging conditions (e.g. almost no ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Impact of different components inside ODG on model performance. Motion compensation Query attention Rendering Sup mIoU RayIoU1m RayIoU2m RayIoU4m

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1 Experiment Setup Datasets: We evaluate our model on the Occ3D benchmark [48] which bootstraps the nuScenes [6] and Waymo-Open [43] dataset.∗nuScenes consists of ... | embodiment, simulator version and control stack | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | 4.2 Evaluation Results In this section, we report evaluation results on the Occ3D benchmark [48] and compare with latest state-of-the-art methods. nuScenes Our results ... | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 3 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 Introduction), p. 3 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We set λ3d = 0.2 to balance box loss Lbox and occupancy loss Locc. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| For rendering loss Lr, we set λ = 0.05 for stage ℓ= 1, 6, and λ = 0.01 for the rest. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Veh), Motorcycle, and Truck, ODG-L carries a significant lead of +4.13 for mIoU, once again demonstrating the efficacy of our proposed strategy of handling ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| This demonstrates it is essential to compensate object motion for dynamic agents. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Our extensive experiments on the Occ3D-nuScenes and Occ3D-Waymo benchmark demonstrates ODG sets new state-of-the-art results while maintaining highly competitive efficiency. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| It is evident that by progressively enabling different modules in ODG, the model performs increasingly well, validating the soundness of the designs that we ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 1: Overview of proposed ODG, where we model the dynamic and static elements of the scene with two separate sets of Gaussian queries. ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| One can see that our method achieves new state-of-the-art results in terms of both mIoU and RayIoU, while maintaining competitive inference speed even when ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Similarly, ODG-T also easily outperforms both SparseOcc (8f), SparseOcc (16f) and GaussRender with significant margins. | comparison identity and matched condition | p. 7 (4 Experiments) |
| 3 that our ODG obtains a definitive lead of +2.35 for mIoU and +1.2 for RayIoU when compared to OPUS. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Our extensive experiments on the Occ3D-nuScenes and Occ3D-Waymo benchmark demonstrates ODG sets new state-of-the-art results while maintaining highly competitive efficiency. | comparison identity and matched condition | p. 9 (4 Experiments) |
| For all our ablation studies, we adopt ODG-T and train on the Occ3D-nuScenes for 24 epochs. | comparison identity and matched condition | p. 8 (4 Experiments) |
| However, as promising as ODG is, it does not come without limitations. | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.4 Ablation Studies In this section, we conduct multiple ablation studies to analyze the effects of various components in our proposed ODG. | component/input/data sensitivity | p. 8 (4 Experiments) |
| We summarize the effect of the different components in our proposed method in Tab. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Table 5: Ablation studies on components related to dynamic Gaussian queries. (a) Effects of Query Attention. Query Attention mIoU RayIoU Cross Attn 31.95 36.3 | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| We analyze the effect of different attention mechanisms in Tab. | component/input/data sensitivity | p. 8 (4 Experiments) |
| We note that for fair comparison, both ODG-T and ODG-L here are trained without using future frames. | component/input/data sensitivity | p. 7 (4 Experiments) |
| Meanwhile, our heavy variant ODG-L sets new best result eventually obtaining an mIoU of 38.18 with a RayIoU of 42.3, surpassing previous best with ... | component/input/data sensitivity | p. 7 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: • Dual Gaussian Query Design: We propose a novel dual-query architecture comprising two distinct sets of Gaussian ... | ODG achieves consistent improvement across all dynamic categories. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 3 (Figure/Table caption) |
| Primary metric/result | Specifically, ODG-T (8f) achieves an mIoU of 35.54 with a RayIoU of 39.2, outperforming OPUS-T (8f) who has an mIoU of 33.2 (-2.34) and ... | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Experiment Setup Datasets: We evaluate our model on the Occ3D benchmark [48] which bootstraps the nuScenes [6] and Waymo-Open [43] dataset.∗nuScenes consists of 1,000 ...
- **p. 6 / 4 Experiments - extractive body cue:** The voxel grid range is [-40m, -40m, -1m, 40m, 40m, 5.4m] along the X, Y and Z axis with a grid resolution of 200×200×16 and ...
- **p. 6 / 4 Experiments - extractive body cue:** We train all our models with an initial learning rate of 2×10-4 and decays with CosineAnnealing [38] schedule.
- **p. 6 / 4 Experiments - extractive body cue:** Unless otherwise specified, we train all our models with a global batch size of 8 for 100 epochs using NVIDIA A100 GPUs.
- **p. 7 / 4 Experiments - extractive body cue:** Specifically, ODG-T (8f) achieves an mIoU of 35.54 with a RayIoU of 39.2, outperforming OPUS-T (8f) who has an mIoU of 33.2 (-2.34) and a ...
- **p. 8 / 4 Experiments - extractive body cue:** For all our ablation studies, we adopt ODG-T and train on the Occ3D-nuScenes for 24 epochs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, as promising as ODG is, it does not come without limitations. | p. 9 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Unless otherwise specified, we train all our models with a global batch size of 8 for 100 epochs using NVIDIA A100 GPUs. | p. 6 (4 Experiments) |
| Inference runtime is measured on a single idle A100 GPU with PyTorch fp32 backend. ∗nuScenes is under a CC BY-NC-SA 4.0 license and Waymo ... | p. 6 (4 Experiments) |
| Specifically, ODG-T (8f) achieves an mIoU of 35.54 with a RayIoU of 39.2, outperforming OPUS-T (8f) who has an mIoU of 33.2 (-2.34) and ... | p. 7 (4 Experiments) |
| For all our ablation studies, we adopt ODG-T and train on the Occ3D-nuScenes for 24 epochs. | p. 8 (4 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive body cue:** However, as promising as ODG is, it does not come without limitations.

- **Evidence anchors reviewed:** datasets p. 6 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), metrics p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), baselines p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), results p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
