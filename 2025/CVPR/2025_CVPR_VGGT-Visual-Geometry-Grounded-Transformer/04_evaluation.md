# Evaluation - VGGT: Visual Geometry Grounded Transformer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.11651; PDF retrieval source: https://arxiv.org/pdf/2503.11651. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (4.1. Camera Pose Estimation), p. 8 (4.3. Point Map Estimation), p. 7 (4.1. Camera Pose Estimation), p. 9 (4.5. Ablation Studies)): Table 10. Camera Pose Estimation on IMC [54]. Our method achieves state-of-the-art performance on the challenging pho- totropism data, outperforming VGGSfMv2 [125] which ranked first on the latest CVPR'24 IMC ...

## Evaluation Body Digest

- **p. 8 / 4.4. Image Matching - extractive body cue:** It represents a specific case of rigid point tracking, which is restricted to only two views, and hence a suitable evaluation benchmark to measure our ...
- **p. 6 / 4.1. Camera Pose Estimation - extractive body cue:** We first evaluate our method on the CO3Dv2 [88] and RealEstate10K [161] datasets for camera pose estimation, as shown in Tab.
- **p. 7 / 4.1. Camera Pose Estimation - extractive body cue:** Dense MVS Estimation on the DTU [51] Dataset.
- **p. 7 / 4.1. Camera Pose Estimation - extractive body cue:** None of the methods were trained on the Re10K dataset.
- **p. 8 / 4.3. Point Map Estimation - extractive body cue:** We present a qualitative comparison with DUSt3R on inthe-wild scenes in Fig.
- **p. 9 / 4.6. Finetuning for Downstream Tasks - extractive body cue:** LVSM was trained on the Objaverse dataset [20].
- **p. 9 / 4.6. Finetuning for Downstream Tasks - extractive body cue:** Quantitative comparisons for view synthesis on GSO [28] dataset.
- **p. 6 / 4. Experiments - extractive body cue:** This section compares our method to state-of-the-art approaches across multiple tasks to show its effectiveness.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 10. Camera Pose Estimation on IMC [54]. Our method achieves state-of-the-art performance on the challenging pho- totropism data, outperforming VGGSfMv2 [125] which ranked ... | p. 12 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5. Visualization of Rigid and Dynamic Point Tracking. Top: VGGT's tracking module T outputs keypoint tracks for an unordered set of input images ... | p. 8 (Figure/Table caption) |
| 4.1. Camera Pose Estimation | SYSTEM / EVALUATION SCOPE UNRESOLVED | Hence, while the feed-forward mode of VGGT outperforms all previous alternatives (whether they are feed-forward or not), there is still room for improvement since ... | p. 7 (4.1. Camera Pose Estimation) |
| 4.3. Point Map Estimation | SYSTEM / EVALUATION SCOPE UNRESOLVED | 3, although DUSt3R and MASt3R conduct expensive optimization (global alignment--around 10 seconds per scene), our method still outperforms them significantly in a simple feed-forward ... | p. 8 (4.3. Point Map Estimation) |
| 4.1. Camera Pose Estimation | SYSTEM / EVALUATION SCOPE UNRESOLVED | Specifically, refining the predicted camera poses and tracks with BA further improves accuracy. | p. 7 (4.1. Camera Pose Estimation) |

## Dataset / Benchmark Role

- **p. 8 / 4.4. Image Matching - extractive body cue:** It represents a specific case of rigid point tracking, which is restricted to only two views, and hence a suitable evaluation benchmark to measure our ...
- **p. 6 / 4.1. Camera Pose Estimation - extractive body cue:** We first evaluate our method on the CO3Dv2 [88] and RealEstate10K [161] datasets for camera pose estimation, as shown in Tab.
- **p. 7 / 4.1. Camera Pose Estimation - extractive body cue:** Dense MVS Estimation on the DTU [51] Dataset.
- **p. 7 / 4.1. Camera Pose Estimation - extractive body cue:** None of the methods were trained on the Re10K dataset.
- **p. 8 / 4.3. Point Map Estimation - extractive body cue:** We present a qualitative comparison with DUSt3R on inthe-wild scenes in Fig.
- **p. 9 / 4.6. Finetuning for Downstream Tasks - extractive body cue:** LVSM was trained on the Objaverse dataset [20].
- **p. 9 / 4.6. Finetuning for Downstream Tasks - extractive body cue:** Quantitative comparisons for view synthesis on GSO [28] dataset.
- **p. 6 / 4. Experiments - extractive body cue:** This section compares our method to state-of-the-art approaches across multiple tasks to show its effectiveness.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. VGGT is a large feed-forward transformer with minimal 3D-inductive biases trained on a trove of 3D-annotated data. It accepts up to hundreds of ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Architecture Overview. Our model first patchifies the input images into tokens by DINO, and appends camera tokens for camera prediction. It then alternates ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison of our predicted 3D points to DUSt3R on in-the-wild images. As shown in the top row, our method successfully predicts the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Additional Visualizations of Point Map Estimation. Camera frustums illustrate the estimated camera poses. Explore our interactive demo for better visualization quality. which are ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Camera Pose Estimation on RealEstate10K [161] and CO3Dv2 [88] with 10 random frames. All metrics the higher the better. None of the methods ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Dense MVS Estimation on the DTU [51] Dataset. Methods operating with known ground-truth camera are in the top part of the table, while ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Point Map Estimation on ETH3D [97]. DUSt3R and MASt3R use global alignment while ours is feed-forward and, hence, much faster. The row Ours ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Two-View matching comparison on ScanNet-1500 [18, 92]. Although our tracking head is not specialized for the two- view setting, it outperforms the state-of-the-art ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It represents a specific case of rigid point tracking, which is restricted to only two views, and hence a suitable evaluation benchmark to measure ... | embodiment, simulator version and control stack | p. 8 (4.4. Image Matching), p. 6 (4.1. Camera Pose Estimation) |
| Task/environment | We first evaluate our method on the CO3Dv2 [88] and RealEstate10K [161] datasets for camera pose estimation, as shown in Tab. | reset, timeout, object/scene variation | p. 6 (4.1. Camera Pose Estimation), p. 7 (4.1. Camera Pose Estimation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 5 (3.3. Prediction heads) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.3. Prediction heads), p. 6 (3.3. Prediction heads) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The row Ours (Point) indicates the results using the point map head directly, while Ours (Depth + Cam) denotes constructing point clouds from the ... | definition/direction/unit from same section | p. 7 (4.1. Camera Pose Estimation) |
| RRA (Relative Rotation Accuracy) and RTA (Relative Translation Accuracy) calculate the relative angular errors in rotation and translation, respectively, for each image pair. | definition/direction/unit from same section | p. 6 (4.1. Camera Pose Estimation) |
| We report Accuracy, Completeness, and Overall (Chamfer distance) for point map estimation. | definition/direction/unit from same section | p. 8 (4.3. Point Map Estimation) |
| 6, there is a noticeable decrease in the accuracy of point map estimation when training without camera, depth, or track estimation. | definition/direction/unit from same section | p. 9 (4.5. Ablation Studies) |
| Notably, incorporating camera parameter estimation clearly enhances point map accuracy, whereas depth estimation contributes only marginal improvements. | definition/direction/unit from same section | p. 9 (4.5. Ablation Studies) |
| Specifically, refining the predicted camera poses and tracks with BA further improves accuracy. | definition/direction/unit from same section | p. 7 (4.1. Camera Pose Estimation) |
| The final metric is the relative pose accuracy, measured by AUC. | definition/direction/unit from same section | p. 8 (4.4. Image Matching) |
| Table 8. Dynamic Point Tracking Results on the TAP-Vid benchmarks. Although our model was not designed for dynamic scenes, simply fine-tuning CoTracker with our ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Although our tracking head is not specialized for the twoview setting, it outperforms the state-of-the-art two-view matching method Roma. | comparison identity and matched condition | p. 7 (4.1. Camera Pose Estimation) |
| 5 demonstrate that our Alternating-Attention architecture outperforms both baseline variants by a clear margin. | comparison identity and matched condition | p. 9 (4.5. Ablation Studies) |
| Table 10. Camera Pose Estimation on IMC [54]. Our method achieves state-of-the-art performance on the challenging pho- totropism data, outperforming VGGSfMv2 [125] which ranked ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Figure 1. VGGT is a large feed-forward transformer with minimal 3D-inductive biases trained on a trove of 3D-annotated data. It accepts up to hundreds ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| This section compares our method to state-of-the-art approaches across multiple tasks to show its effectiveness. | comparison identity and matched condition | p. 6 (4. Experiments) |
| Compared to concurrent works [111, 127, 141, 156] (indicated by ‡), our method demonstrates significant performance advantages, with speed similar to the fastest variant ... | comparison identity and matched condition | p. 7 (4.1. Camera Pose Estimation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5. Ablation Study for Transformer Backbone on ETH3D. We compare our alternating-attention architecture against two variants: one using only global self-attention and another ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 6. Ablation Study for Multi-task Learning, which shows that simultaneous training with camera, depth and track estimation yields the highest accuracy in point ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| 2, DUSt3R and our VGGT are the only two methods operating without the knowledge of ground truth cameras. | component/input/data sensitivity | p. 7 (4.2. Multi-view Depth Estimation) |
| Compared to concurrent works [111, 127, 141, 156] (indicated by ‡), our method demonstrates significant performance advantages, with speed similar to the fastest variant ... | component/input/data sensitivity | p. 7 (4.1. Camera Pose Estimation) |
| 5 demonstrate that our Alternating-Attention architecture outperforms both baseline variants by a clear margin. | component/input/data sensitivity | p. 9 (4.5. Ablation Studies) |
| Table 8. Dynamic Point Tracking Results on the TAP-Vid benchmarks. Although our model was not designed for dynamic scenes, simply fine-tuning CoTracker with our ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, we make the following contributions: (1) We introduce VGGT, a large feed-forward transformer that, given one, a few, or even hundreds of ... | Table 10. Camera Pose Estimation on IMC [54]. Our method achieves state-of-the-art performance on the challenging pho- totropism data, outperforming VGGSfMv2 [125] which ranked ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (4.1. Camera Pose Estimation), p. 8 (4.3. Point Map Estimation), p. 7 (4.1. Camera Pose Estimation), p. 9 (4.5. Ablation Studies) |
| Primary metric/result | Figure 5. Visualization of Rigid and Dynamic Point Tracking. Top: VGGT's tracking module T outputs keypoint tracks for an unordered set of input images ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 4.1. Camera Pose Estimation - extractive body cue:** Methods Acc.↓ Comp.↓ Overall↓ Time DUSt3R 1.167 0.842 1.005 ∼7s MASt3R 0.968 0.684 0.826 ∼9s Ours (Point) 0.901 0.518 0.709 ∼0.2s Ours (Depth + Cam) ...
- **p. 8 / 4.3. Point Map Estimation - extractive body cue:** For each scene, we randomly sample 10 frames.
- **p. 4 / 3.1. Problem definition and notation - extractive body cue:** Ours Input Single view Two views < 0.1s < 0.1s < 0.1s < 0.1s DUSt3R … … 32 views > 200s < 0.6 s Figure ...
- **p. 4 / 3.1. Problem definition and notation - extractive body cue:** We do not include examples with more than 32 frames, as DUSt3R runs out of memory beyond this limit.
- **p. 4 / 3.2. Feature Backbone - extractive body cue:** By default, we employ L = 24 layers of global and frame-wise attention.
- **p. 6 / 3.4. Training - extractive body cue:** By default, we employ L = 24 layers of global and frame-wise attention, respectively.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While our method exhibits strong generalization to diverse in-the-wild scenes, several limitations remain. | p. 10 (5. Discussions) |
| body limitation/failure cue | Moreover, although our model handles scenes with minor non-rigid motions, it fails in scenarios involving substantial non-rigid deformation. | p. 10 (5. Discussions) |
| body limitation/failure cue | While customizing a framework to expedite training could be a potential solution, it falls outside the scope of this work. | p. 11 (5. Discussions) |
| body limitation/failure cue | Figure 3. Qualitative comparison of our predicted 3D points to DUSt3R on in-the-wild images. As shown in the top row, our method successfully predicts ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | It is worth mentioning that we apply aggressive color augmentation independently across each frame within the same scene, enhancing the model's robustness to varying ... | p. 12 (6. Conclusions) |
| body limitation/failure cue | Following standard practices, we report these point-tracking metrics: Occlusion Accuracy (OA), which comprises the binary accuracy of occlusion predictions; δvis avg, comprising the 9 | p. 9 (4.6. Finetuning for Downstream Tasks) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We leverage bfloat16 precision and gradient checkpointing to improve GPU memory and computational efficiency. | p. 6 (3.4. Training) |
| Runtime were measured using one H100 GPU. | p. 7 (4.1. Camera Pose Estimation) |
| We use a cosine learning rate scheduler with a peak learning rate of 0.0002 and a warmup of 8K iterations. | p. 6 (3.4. Training) |
| In contrast, VGGT achieves superior performance while only operating in a feed-forward manner, requiring just 0.2 seconds on the same hardware. | p. 7 (4.1. Camera Pose Estimation) |
| Two-view image matching is a widely-explored topic [68, 93, 105] in computer vision. | p. 8 (4.4. Image Matching) |
| We adopt the evaluation hyperparameters (e.g., the number of matches, RANSAC thresholds) from Roma [33]. | p. 8 (4.4. Image Matching) |
| The hyperparameters such as the hidden dimension and the number of heads are kept the same. | p. 9 (4.5. Ablation Studies) |
| Then, for the target views, we use a convolutional layer to encode their Pl¨ucker ray images into tokens. | p. 9 (4.6. Finetuning for Downstream Tasks) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5. Discussions - extractive body cue:** While our method exhibits strong generalization to diverse in-the-wild scenes, several limitations remain.
- **p. 10 / 5. Discussions - extractive body cue:** Moreover, although our model handles scenes with minor non-rigid motions, it fails in scenarios involving substantial non-rigid deformation.
- **p. 11 / 5. Discussions - extractive body cue:** While customizing a framework to expedite training could be a potential solution, it falls outside the scope of this work.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison of our predicted 3D points to DUSt3R on in-the-wild images. As shown in the top row, our method successfully predicts the ...
- **p. 12 / 6. Conclusions - extractive body cue:** It is worth mentioning that we apply aggressive color augmentation independently across each frame within the same scene, enhancing the model's robustness to varying lighting ...
- **p. 9 / 4.6. Finetuning for Downstream Tasks - extractive body cue:** Following standard practices, we report these point-tracking metrics: Occlusion Accuracy (OA), which comprises the binary accuracy of occlusion predictions; δvis avg, comprising the 9

- **Evidence anchors reviewed:** datasets p. 8 (4.4. Image Matching), p. 6 (4.1. Camera Pose Estimation), p. 7 (4.1. Camera Pose Estimation), p. 7 (4.1. Camera Pose Estimation), p. 8 (4.3. Point Map Estimation), p. 9 (4.6. Finetuning for Downstream Tasks), metrics p. 7 (4.1. Camera Pose Estimation), p. 6 (4.1. Camera Pose Estimation), p. 8 (4.3. Point Map Estimation), p. 9 (4.5. Ablation Studies), p. 9 (4.5. Ablation Studies), p. 7 (4.1. Camera Pose Estimation), baselines p. 7 (4.1. Camera Pose Estimation), p. 9 (4.5. Ablation Studies), p. 12 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (4. Experiments), p. 7 (4.1. Camera Pose Estimation), results p. 12 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (4.1. Camera Pose Estimation), p. 8 (4.3. Point Map Estimation), p. 7 (4.1. Camera Pose Estimation), p. 9 (4.5. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
