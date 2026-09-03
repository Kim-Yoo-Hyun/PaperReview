# Evaluation - LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=KhjlXNbYea&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.5. Ablations), p. 6 (4.3. 3D Open Vocabulary Retrieval), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.5. Ablations), p. 5 (4.1. Dataset and Task Description), p. 4 (Figure/Table caption)): Adding 4 future and past frames during rendering supervision already improves all scores significantly, such that LangOcc achieves a better open vocabulary retrieval performance than POP-3D [43].

## Evaluation Body Digest

- **p. 5 / 4.1. Dataset and Task Description - extractive body cue:** For zero-shot occupancy estimation, we evaluate on the widely known Occ3D-nuScenes benchmark [41], which provides semantic voxel labels for the nuScenes dataset.
- **p. 5 / 4.1. Dataset and Task Description - extractive body cue:** We conduct all experiments on the nuScenes dataset [3].
- **p. 6 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** We evaluate our approach against other recent approaches on the Occ3D-nuScenes dataset [41] and show the results in Tab.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** We use the same fixed vocabulary to train the reducer U for each experiment, which is based on the target classes of the Occ3D-nuScenes dataset.
- **p. 7 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** Semantic occupancy estimation results on the Occ3DnuScenes benchmark [41] in terms of geometric IoU and semantic mIoU.
- **p. 7 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** Qualitative results showing open vocabulary retrieval on nuScenes [3].
- **p. 6 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** LangOcc achieves a geometric IoU score of at least 51.59, showing that our model is able to estimate the scene geometry well without any photometric ...
- **p. 7 / 4.5. Ablations - extractive body cue:** Loss Function MSE CosSim Cos-guided MSE IoU 50.29 49.88 51.59 mIoU 9.41 9.89 10.71 mAP (v) 20.1 22.6 22.7 using either the MSE loss or ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Dataset and Task Description (p. 5); 4.2. Implementation Details (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.5. Ablations | SYSTEM / EVALUATION SCOPE UNRESOLVED | Adding 4 future and past frames during rendering supervision already improves all scores significantly, such that LangOcc achieves a better open vocabulary retrieval performance ... | p. 7 (4.5. Ablations) |
| 4.3. 3D Open Vocabulary Retrieval | SYSTEM / EVALUATION SCOPE UNRESOLVED | We achieve a mAP score of 21.7 and 22.7 (for all points and only visible points, respectively) compared to the 17.5 and 18.4 of ... | p. 6 (4.3. 3D Open Vocabulary Retrieval) |
| 4.4. Zero-shot Semantic Occupancy Estimation | SYSTEM / EVALUATION SCOPE UNRESOLVED | LangOcc achieves a geometric IoU score of at least 51.59, showing that our model is able to estimate the scene geometry well without any ... | p. 6 (4.4. Zero-shot Semantic Occupancy Estimation) |
| 4.5. Ablations | SYSTEM / EVALUATION SCOPE UNRESOLVED | The best performance on all tasks was achieved by using a horizon of 12, which seems to be a good trade-off between overlap of ... | p. 7 (4.5. Ablations) |
| 4.1. Dataset and Task Description | SYSTEM / EVALUATION SCOPE UNRESOLVED | The performance is measured by the mean-average-precision (mAP) for all points in the scene, and only for points visible in at least one camera ... | p. 5 (4.1. Dataset and Task Description) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Dataset and Task Description - extractive body cue:** For zero-shot occupancy estimation, we evaluate on the widely known Occ3D-nuScenes benchmark [41], which provides semantic voxel labels for the nuScenes dataset.
- **p. 5 / 4.1. Dataset and Task Description - extractive body cue:** We conduct all experiments on the nuScenes dataset [3].
- **p. 6 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** We evaluate our approach against other recent approaches on the Occ3D-nuScenes dataset [41] and show the results in Tab.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** We use the same fixed vocabulary to train the reducer U for each experiment, which is based on the target classes of the Occ3D-nuScenes dataset.
- **p. 7 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** Semantic occupancy estimation results on the Occ3DnuScenes benchmark [41] in terms of geometric IoU and semantic mIoU.
- **p. 7 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** Qualitative results showing open vocabulary retrieval on nuScenes [3].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. Architecture of the proposed model. A set of images is first transformed to 3D voxel features via BEVStereo [24] and a 3D CNN ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. 3D open vocabulary retrieval results on the bench- mark provided by [43]. mAP (v) is calculated only on points visible to one of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2. Qualitative results showing open vocabulary retrieval on nuScenes [3]. Given a text query, we compute similarities between the text embedding and each estimated ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Semantic occupancy estimation results on the Occ3D- nuScenes benchmark [41] in terms of geometric IoU and se- mantic mIoU. The Mode indicates the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation on the loss function used for Llang.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation on the temporal horizon. Horizon 0 4 8 12 16 20
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation on the subspace dimensionality L′. L' 16 32 64 128 256 512

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For zero-shot occupancy estimation, we evaluate on the widely known Occ3D-nuScenes benchmark [41], which provides semantic voxel labels for the nuScenes dataset. | embodiment, simulator version and control stack | p. 5 (4.1. Dataset and Task Description), p. 5 (4.1. Dataset and Task Description) |
| Task/environment | We conduct all experiments on the nuScenes dataset [3]. | reset, timeout, object/scene variation | p. 5 (4.1. Dataset and Task Description), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.2. Model Architecture), p. 3 (3.2. Model Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| LangOcc achieves a geometric IoU score of at least 51.59, showing that our model is able to estimate the scene geometry well without any ... | definition/direction/unit from same section | p. 6 (4.4. Zero-shot Semantic Occupancy Estimation) |
| Loss Function MSE CosSim Cos-guided MSE IoU 50.29 49.88 51.59 mIoU 9.41 9.89 10.71 mAP (v) 20.1 22.6 22.7 using either the MSE loss ... | definition/direction/unit from same section | p. 7 (4.5. Ablations) |
| The performance is measured in geometric IoU and in mean-IoU over all categories in the benchmark. | definition/direction/unit from same section | p. 6 (4.1. Dataset and Task Description) |
| Adding 4 future and past frames during rendering supervision already improves all scores significantly, such that LangOcc achieves a better open vocabulary retrieval performance ... | definition/direction/unit from same section | p. 7 (4.5. Ablations) |
| The performance is measured by the mean-average-precision (mAP) for all points in the scene, and only for points visible in at least one camera ... | definition/direction/unit from same section | p. 5 (4.1. Dataset and Task Description) |
| Figure 1. Architecture of the proposed model. A set of images is first transformed to 3D voxel features via BEVStereo [24] and a 3D ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As is visible, our method outperforms both baselines, even though we use just vision-based supervision. | comparison identity and matched condition | p. 6 (4.3. 3D Open Vocabulary Retrieval) |
| Even though our model is trained without any explicit class definition, we outperform both competitors also in terms of semantic mIoU, highlighting the power ... | comparison identity and matched condition | p. 6 (4.4. Zero-shot Semantic Occupancy Estimation) |
| Ablation on the loss function used for Llang. | comparison identity and matched condition | p. 7 (4.5. Ablations) |
| Loss function We provide a comparison between using our proposed Cosine Similarity Guided MSE function and Table 3. | comparison identity and matched condition | p. 7 (4.5. Ablations) |
| Table 4. Ablation on the temporal horizon. Horizon 0 4 8 12 16 20 | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 5. Ablation on the subspace dimensionality L′. L' 16 32 64 128 256 512 | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Even though our model is trained without any explicit class definition, we outperform both competitors also in terms of semantic mIoU, highlighting the power ... | component/input/data sensitivity | p. 6 (4.4. Zero-shot Semantic Occupancy Estimation) |
| LangOcc achieves a geometric IoU score of at least 51.59, showing that our model is able to estimate the scene geometry well without any ... | component/input/data sensitivity | p. 6 (4.4. Zero-shot Semantic Occupancy Estimation) |
| Ablation on the loss function used for Llang. | component/input/data sensitivity | p. 7 (4.5. Ablations) |
| Table 4. Ablation on the temporal horizon. Horizon 0 4 8 12 16 20 | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 5. Ablation on the subspace dimensionality L′. L' 16 32 64 128 256 512 | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper we propose a novel self-supervised occupancy estimation method which aligns geometric estimations with open vocabulary natural language features, hence allowing representations ... | Adding 4 future and past frames during rendering supervision already improves all scores significantly, such that LangOcc achieves a better open vocabulary retrieval performance ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.5. Ablations), p. 6 (4.3. 3D Open Vocabulary Retrieval), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.5. Ablations), p. 5 (4.1. Dataset and Task Description), p. 4 (Figure/Table caption) |
| Primary metric/result | We achieve a mAP score of 21.7 and 22.7 (for all points and only visible points, respectively) compared to the 17.5 and 18.4 of ... | numeric claim only at cited anchor | p. 6 (4.3. 3D Open Vocabulary Retrieval) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Dataset and Task Description - extractive body cue:** It consists of 105 samples, each with an open vocabulary text query and corresponding binary labels for the LiDAR point cloud, with the goal of ...
- **p. 6 / 4.2. Implementation Details - extractive body cue:** We train each network with a batch size of 4 for 18 epochs.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** For each ray, we sample 100 points, and use the nerfacc [23] package for rendering.
- **p. 7 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** Input images Similarity Map "Traffic light" FRONT-LEFT FRONT FRONT-RIGHT BACK-LEFT BACK BACK-RIGHT "Metal Pole" FRONT-LEFT FRONT FRONT-RIGHT BACK-LEFT BACK BACK-RIGHT "Human being" FRONT-LEFT FRONT FRONT-RIGHT ...
- **p. 3 / 3.3. Volume Rendering Supervision - extractive body cue:** Specifically, a rendering weight w(r(t)) is computed for each sampled point on the ray by accumulating the interpolated density: w(r(t)) = T (r(t)) (1 -exp(-σ(r(t))δt)) ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As mentioned above, the reducer U finishes training within a second and thus does not impose any notable overhead. | p. 7 (4.4. Zero-shot Semantic Occupancy Estimation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train each network with a batch size of 4 for 18 epochs. | p. 6 (4.2. Implementation Details) |
| 4.4 for all models to train the autoencoder, but modify the target dimension size (with 512 being the full space). | p. 7 (4.5. Ablations) |
| Given a text query, we compute similarities between the text embedding and each estimated voxel embedding and highlight voxels with a high similarity score. | p. 7 (4.4. Zero-shot Semantic Occupancy Estimation) |
| 3D Head The voxel features Vf are processed by a 3D CNN decoder Φf, which computes local interactions to refine the features. | p. 3 (3.2. Model Architecture) |
| Afterwards, for each query prompt, a feature is computed with the text encoder. | p. 5 (3.5. Inference) |
| We always render our predictions for the current time step, but compute a loss to ground truth feature maps from adjacent time steps, where ... | p. 5 (3.3. Volume Rendering Supervision) |
| However, note that any other 2D-to-3D encoder, like [13, 15, 26], could be used instead. | p. 3 (3.2. Model Architecture) |
| A set of images is first transformed to 3D voxel features via BEVStereo [24] and a 3D CNN decoder. | p. 4 (3.3. Volume Rendering Supervision) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** As mentioned above, the reducer U finishes training within a second and thus does not impose any notable overhead.

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Dataset and Task Description), p. 5 (4.1. Dataset and Task Description), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 6 (4.2. Implementation Details), p. 7 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.4. Zero-shot Semantic Occupancy Estimation), metrics p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.5. Ablations), p. 6 (4.1. Dataset and Task Description), p. 7 (4.5. Ablations), p. 5 (4.1. Dataset and Task Description), p. 4 (Figure/Table caption), baselines p. 6 (4.3. 3D Open Vocabulary Retrieval), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.5. Ablations), p. 7 (4.5. Ablations), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 7 (4.5. Ablations), p. 6 (4.3. 3D Open Vocabulary Retrieval), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.5. Ablations), p. 5 (4.1. Dataset and Task Description), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
