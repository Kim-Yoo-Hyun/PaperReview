# Evaluation - In-Place Scene Labelling and Understanding with Implicit Scene Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.15875; PDF retrieval source: https://arxiv.org/pdf/2103.15875. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Semantic Fusion), p. 4 (4.2. Semantic Neural Radiance Fields), p. 7 (4.4. Semantic Fusion), p. 8 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion)): Our method achieves the highest improvement across all metrics, showing the effectiveness of our joint representation in label fusion.

## Evaluation Body Digest

- **p. 4 / 4.1. Indoor Scene Datasets and Data Preparation - extractive PDF cue:** ScanNet ScanNet [3] is a large-scale real-world indoor RGB-D video dataset of 2.5M views in 1513 scenes with rich annotations including semantic segmentation, camera poses ...
- **p. 4 / 4.1. Indoor Scene Datasets and Data Preparation - extractive PDF cue:** Replica Replica [28] is a reconstruction-based 3D dataset of 18 high fidelity scenes with dense geometry, HDR textures and semantic annotations.
- **p. 8 / 4.4. Semantic Fusion - extractive PDF cue:** To prepare training data in Replica dataset, we render two different sequences per Replica scene to cover various parts of scenes.
- **p. 7 / 4.4. Semantic Fusion - extractive PDF cue:** We report superresolution performance on training poses from all Replica scenes with two scales S = 8 and S = 16 in Table 2.
- **p. 8 / 4.4. Semantic Fusion - extractive PDF cue:** We report the average performance across all testing scenes in Table 4, in which ground truth depth maps are used for the two baseline approaches ...
- **p. 5 / 4.4. Semantic Fusion - extractive PDF cue:** Bright parts of the entropy map match well to object boundaries or ambiguous/unknown regions in the corresponding training set-up.
- **p. 5 / 4.4. Semantic Fusion - extractive PDF cue:** This is a better simulation of the behaviour of real single-view CNNs because a whole object can easily be labelled as a similar but incorrect ...
- **p. 3 / 3.4. Implementation - extractive PDF cue:** In addition, since we have no depth information, we set the bounds of ray sampling to 0.1m and 10m respectively across experiments without careful tuning ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.4. Implementation (p. 3); 4. Experiments and Applications (p. 4); 4.1. Indoor Scene Datasets and Data Preparation (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Semantic Fusion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves the highest improvement across all metrics, showing the effectiveness of our joint representation in label fusion. | p. 8 (4.4. Semantic Fusion) |
| 4.2. Semantic Neural Radiance Fields | EMPIRICAL / REAL-ROBOT OR HARDWARE | Note that we might expect that significant high quality semantic labelling information could feasibly improve reconstruction quality, but in this paper we are focused ... | p. 4 (4.2. Semantic Neural Radiance Fields) |
| 4.4. Semantic Fusion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Object boundaries are gradually refined when more supervision is available and the incremental improvements from more labels tend to saturate. | p. 7 (4.4. Semantic Fusion) |
| 4.4. Semantic Fusion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Accurate labels can be achieved even from single-clicks, which are zoomed-in 9 times for visualisation purposes. | p. 8 (4.4. Semantic Fusion) |
| 4.4. Semantic Fusion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results with only two labelled key-frames (⋆) show remarkably competitive performance. we re-render the semantic labels from the learned representation back to input training ... | p. 5 (4.4. Semantic Fusion) |

## Dataset / Benchmark Role

- **p. 4 / 4.1. Indoor Scene Datasets and Data Preparation - extractive PDF cue:** ScanNet ScanNet [3] is a large-scale real-world indoor RGB-D video dataset of 2.5M views in 1513 scenes with rich annotations including semantic segmentation, camera poses ...
- **p. 4 / 4.1. Indoor Scene Datasets and Data Preparation - extractive PDF cue:** Replica Replica [28] is a reconstruction-based 3D dataset of 18 high fidelity scenes with dense geometry, HDR textures and semantic annotations.
- **p. 8 / 4.4. Semantic Fusion - extractive PDF cue:** To prepare training data in Replica dataset, we render two different sequences per Replica scene to cover various parts of scenes.
- **p. 7 / 4.4. Semantic Fusion - extractive PDF cue:** We report superresolution performance on training poses from all Replica scenes with two scales S = 8 and S = 16 in Table 2.
- **p. 8 / 4.4. Semantic Fusion - extractive PDF cue:** We report the average performance across all testing scenes in Table 4, in which ground truth depth maps are used for the two baseline approaches ...
- **p. 5 / 4.4. Semantic Fusion - extractive PDF cue:** Bright parts of the entropy map match well to object boundaries or ambiguous/unknown regions in the corresponding training set-up.
- **p. 5 / 4.4. Semantic Fusion - extractive PDF cue:** This is a better simulation of the behaviour of real single-view CNNs because a whole object can easily be labelled as a similar but incorrect ...
- **p. 3 / 3.4. Implementation - extractive PDF cue:** In addition, since we have no depth information, we set the bounds of ray sampling to 0.1m and 10m respectively across experiments without careful tuning ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Neural radiance fields (NeRF) jointly encoding appearance and geometry contain strong priors for segmen- tation and clustering. We build upon this to create ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Semantic-NeRF network architecture. 3D posi- tion (x, y, z) and viewing direction (θ, φ) are fed into the network after positional encoding (PE). ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Synthesised semantic labels at testing poses given 100% and 10% of ground truth labels during training. From left to right we show the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Quantitative performance of Semantic-NeRF trained on Replica with sparse semantic labels. Sparsity ra- tio is the percentage of frames dropped compared to full ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5: Qualitative results for semantic denoising. Even when 90% of all training labels are randomly corrupted, we can recover an accurate denoised semantic map. ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative evaluation for label denoising on Replica. Noise ratio is the percentage of changed pixels per frame, and for each instance the percentage ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6: Qualitative results of rendered labels when we randomly change the training semantic class label (blue) of chair instances. From left to right: training ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7: Super-resolution: we train Semantic-NeRF with only low resolution labels (sparsely sampled or interpolated) and obtain super-resolved labels by re-rendering semantics from the same ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ScanNet ScanNet [3] is a large-scale real-world indoor RGB-D video dataset of 2.5M views in 1513 scenes with rich annotations including semantic segmentation, camera ... | embodiment, simulator version and control stack | p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 4 (4.1. Indoor Scene Datasets and Data Preparation) |
| Task/environment | Replica Replica [28] is a reconstruction-based 3D dataset of 18 high fidelity scenes with dense geometry, HDR textures and semantic annotations. | reset, timeout, object/scene variation | p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 8 (4.4. Semantic Fusion) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (3.1. Preliminaries), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.3. Network Training), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 0 20 40 60 80 100 Sparsity Ratio (%) 75 80 85 90 95 100 Segmentation Metrics (%) Total Accuracy Class Average Accuracy mIoU ... | definition/direction/unit from same section | p. 5 (4.4. Semantic Fusion) |
| Even single-pixel supervision leads to competitive performance on the accuracy metrics, which highlights the effectiveness of the representation for interactive scene labelling. | definition/direction/unit from same section | p. 8 (4.4. Semantic Fusion) |
| [29, 13, 18]), multiple 2D semantic observations are integrated into a 3D map or target frames to produce a more consistent and accurate semantic ... | definition/direction/unit from same section | p. 4 (4.4. Semantic Fusion) |
| Only marginal performance loss occurs when less than 10% semantic frames are used, and this is mainly caused by renderings of regions which are ... | definition/direction/unit from same section | p. 4 (4.3. Semantic View Synthesis with Sparse Labels) |
| Even when 90% of all training labels are randomly corrupted, we can recover an accurate denoised semantic map. | definition/direction/unit from same section | p. 6 (4.4. Semantic Fusion) |
| (2) All pixels except those from the low-res label map (row and column divisible by 8) are masked by the void class so as ... | definition/direction/unit from same section | p. 7 (4.4. Semantic Fusion) |
| Table 2: Quantitative evaluation of label super-resolution, with good performance with either sampled or interpolated low-resolution labels. The mIoU metric shows that sparse but ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Three standard metrics are used to evaluate semantic segmentation performance on test poses (higher is better). | definition/direction/unit from same section | p. 5 (4.4. Semantic Fusion) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our approach relying on consistency of scene representations outperforms baselines aided with depth maps. posed images. | comparison identity and matched condition | p. 8 (4.4. Semantic Fusion) |
| Sparsity ratio is the percentage of frames dropped compared to full sequence supervision. | comparison identity and matched condition | p. 5 (4.4. Semantic Fusion) |
| Compared with Figure 3, the entropy in this denoising task is higher because the noisy training labels lack the multi-view consistency of clean ones. | comparison identity and matched condition | p. 5 (4.4. Semantic Fusion) |
| Two baseline techniques are: Bayesian fusion, where multiclass label probabilities are multiplied together and then renormalised (e.g. | comparison identity and matched condition | p. 7 (4.4. Semantic Fusion) |
| We report the average performance across all testing scenes in Table 4, in which ground truth depth maps are used for the two baseline ... | comparison identity and matched condition | p. 8 (4.4. Semantic Fusion) |
| We check the influence of semantics on appearance and geometry by quantitatively computing the quality of rendered RGB images and depth maps on Replica ... | comparison identity and matched condition | p. 4 (4.2. Semantic Neural Radiance Fields) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We check the influence of semantics on appearance and geometry by quantitatively computing the quality of rendered RGB images and depth maps on Replica ... | component/input/data sensitivity | p. 4 (4.2. Semantic Neural Radiance Fields) |
| We test two different strategies to generate low-resolution training labels, with and without interpolation as shown in Figure 7. | component/input/data sensitivity | p. 6 (4.4. Semantic Fusion) |
| In addition, since we have no depth information, we set the bounds of ray sampling to 0.1m and 10m respectively across experiments without careful ... | component/input/data sensitivity | p. 3 (3.4. Implementation) |
| We repeat this fine-tuning process and train one individual DeepLab CNN model for each test scene. | component/input/data sensitivity | p. 8 (4.4. Semantic Fusion) |
| To generate decent monocular CNN predictions and avoid over-fitting, we train DeepLab on SUN-RGBD [26], and then fine-tune it using data from all Replica ... | component/input/data sensitivity | p. 8 (4.4. Semantic Fusion) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for ... | Our method achieves the highest improvement across all metrics, showing the effectiveness of our joint representation in label fusion. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Semantic Fusion), p. 4 (4.2. Semantic Neural Radiance Fields), p. 7 (4.4. Semantic Fusion), p. 8 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion) |
| Primary metric/result | Note that we might expect that significant high quality semantic labelling information could feasibly improve reconstruction quality, but in this paper we are focused ... | numeric claim only at cited anchor | p. 4 (4.2. Semantic Neural Radiance Fields) |

- Numeric sentences retained from the body:
- **p. 4 / 4.1. Indoor Scene Datasets and Data Preparation - extractive PDF cue:** For each Replica scene of rooms and offices, we render 900 images at resolution 640x480 using the default pin-hole camera model with 90 degree horizontal ...
- **p. 4 / 4.1. Indoor Scene Datasets and Data Preparation - extractive PDF cue:** ScanNet ScanNet [3] is a large-scale real-world indoor RGB-D video dataset of 2.5M views in 1513 scenes with rich annotations including semantic segmentation, camera poses ...
- **p. 4 / 4.1. Indoor Scene Datasets and Data Preparation - extractive PDF cue:** The sequences in each scene are evenly sampled so that the total amount of training data is roughly 300 frames.
- **p. 6 / 4.4. Semantic Fusion - extractive PDF cue:** Given a down-scaling factor S = 8 for instance: (1) All ground truth labels are down-scaled from 320×240 to 40 × 30 before being up-scaled ...
- **p. 7 / 4.4. Semantic Fusion - extractive PDF cue:** Super-Resolution Metrics Down-Scaling Factor mIoU Avg Acc Total Acc Dense S=8 0.610 0.710 0.923 S=16 0.433 0.535 0.855 Sparse S=8 0.887 0.928 0.987 S=16 0.800 ...
- **p. 8 / 4.4. Semantic Fusion - extractive PDF cue:** Each sequence consists of 90 frames evenly sampled from 900 renderings of size 640×480 with semantic labels remapped to NYUv2-13 class convention.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | batch size of rays is set to 1024 due to memory limitations. | p. 4 (3.4. Implementation) |
| body limitation/failure cue | Given multiple noisy or partial semantic labels, the network can fuse them into a joint implicit 3D space so that we can extract a ... | p. 4 (4.4. Semantic Fusion) |
| body limitation/failure cue | Quantitative results shown in Table 1 also confirm that accurate denoised labels are obtained after training-as-fusion. | p. 5 (4.4. Semantic Fusion) |
| body limitation/failure cue | After training using only these noisy labels, we obtain denoised semantic labels by rendering back to the same training poses. | p. 5 (4.4. Semantic Fusion) |
| body limitation/failure cue | Even when 90% of all training labels are randomly corrupted, we can recover an accurate denoised semantic map. | p. 6 (4.4. Semantic Fusion) |
| body limitation/failure cue | From left to right are noisy training labels, denoised labels rendered from the same poses after training, and information entropy. | p. 6 (4.4. Semantic Fusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| batch size of rays is set to 1024 due to memory limitations. | p. 4 (3.4. Implementation) |
| We train the neural network using the Adam optimiser [7] with a learning rate of 5e-4 for 200,000 iterations. | p. 4 (3.4. Implementation) |
| We implement our model in PyTorch [20] and train it on a single RTX2080-Ti GPU with 11GB memory. | p. 3 (3.4. Implementation) |
| For each chair instance, we compute the occupied area ratio (i.e., ratio of the number of pixels belonging to that instance to the total ... | p. 5 (4.4. Semantic Fusion) |
| Both tables are computed against clean training labels. to randomly perturb each instance: (1) Sort: Select label maps with the least occupied area ratio. | p. 6 (4.4. Semantic Fusion) |
| We train Semantic-NeRF using posed colour images together with CNN-predicted labels for 200,000 steps and then re-render the fused semantic labels back to the ... | p. 8 (4.4. Semantic Fusion) |
| It is important to note that both baseline fusion techniques require depth information to compute the dense correspondences between frames while ours only requires ... | p. 8 (4.4. Semantic Fusion) |
| To compute the colour of a single pixel, NeRF [16] approximates volume rendering by numerical quadrature with hierarchical stratified sampling. | p. 2 (3.1. Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / 3.4. Implementation - extractive PDF cue:** batch size of rays is set to 1024 due to memory limitations.
- **p. 4 / 4.4. Semantic Fusion - extractive PDF cue:** Given multiple noisy or partial semantic labels, the network can fuse them into a joint implicit 3D space so that we can extract a denoised ...
- **p. 5 / 4.4. Semantic Fusion - extractive PDF cue:** Quantitative results shown in Table 1 also confirm that accurate denoised labels are obtained after training-as-fusion.
- **p. 5 / 4.4. Semantic Fusion - extractive PDF cue:** After training using only these noisy labels, we obtain denoised semantic labels by rendering back to the same training poses.
- **p. 6 / 4.4. Semantic Fusion - extractive PDF cue:** Even when 90% of all training labels are randomly corrupted, we can recover an accurate denoised semantic map.
- **p. 6 / 4.4. Semantic Fusion - extractive PDF cue:** From left to right are noisy training labels, denoised labels rendered from the same poses after training, and information entropy.

- **PDF anchors reviewed:** datasets p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 8 (4.4. Semantic Fusion), p. 7 (4.4. Semantic Fusion), p. 8 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion), metrics p. 5 (4.4. Semantic Fusion), p. 8 (4.4. Semantic Fusion), p. 4 (4.4. Semantic Fusion), p. 4 (4.3. Semantic View Synthesis with Sparse Labels), p. 6 (4.4. Semantic Fusion), p. 7 (4.4. Semantic Fusion), baselines p. 8 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion), p. 7 (4.4. Semantic Fusion), p. 8 (4.4. Semantic Fusion), p. 4 (4.2. Semantic Neural Radiance Fields), results p. 8 (4.4. Semantic Fusion), p. 4 (4.2. Semantic Neural Radiance Fields), p. 7 (4.4. Semantic Fusion), p. 8 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
