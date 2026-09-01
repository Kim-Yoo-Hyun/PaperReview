# Evaluation - HandDiff: 3D Hand Pose Estimation with Diffusion on Image-Point Cloud

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Cheng_HandDiff_3D_Hand_Pose_Estimation_with_Diffusion_on_Image-Point_Cloud_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Cheng_HandDiff_3D_Hand_Pose_Estimation_with_Diffusion_on_Image-Point_Cloud_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.2. Datasets and Evaluation Metrics), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 7 (4.3. Comparison with State-of-the-Art Methods)): The results also demonstrate that the proposed HandDiff significantly outperforms other 2D image-based methods by large margins since HandDiff directly performs the processing on the 3D space, avoiding the highly ...

## Evaluation Body Digest

- **p. 5 / 4.2. Datasets and Evaluation Metrics - extractive PDF cue:** This dataset defines four official dataset split protocols: S0 - seen subjects, camera views, grasped objects; S1 - unseen subjects; S2 - unseen camera views; ...
- **p. 7 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** We compare HandDiff on the hand-object dataset DexYCB with other state-of-the-art method on the official dataset split protocals, including A2J [53], Spurr et al.
- **p. 5 / 4.2. Datasets and Evaluation Metrics - extractive PDF cue:** The DexYCB dataset [3] is a recently released hand-object dataset that consists of 582,000 image frames with 21 annotated joints, 10 different subjects, and 20 ...
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** Qualitative results of HandDiff on the DexYCB datasets including different grabbing poses (top), self-occlusions (middle), and object occlusions (bottom).
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** The proposed model also achieves the third-lowest error on the NYU dataset.
- **p. 7 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** 12, 15, and 52 mm on the ICVL, MSRA, and NYU datasets, respectively.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** All the ablation models are trained and tested on the DexYCB dataset .
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** The joints must be generated in a specific permutation in order to match the permutation defined by the dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experiment Settings (p. 5); 4.2. Datasets and Evaluation Metrics (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Comparison with State-of-the-Art Methods | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results also demonstrate that the proposed HandDiff significantly outperforms other 2D image-based methods by large margins since HandDiff directly performs the processing on ... | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| 4.2. Datasets and Evaluation Metrics | EMPIRICAL / SOURCE-REPORTED EVALUATION | We employ two commonly used metrics, the mean joint error, and the success rate, to evaluate the performance of hand pose estimation. | p. 5 (4.2. Datasets and Evaluation Metrics) |
| 4.3. Comparison with State-of-the-Art Methods | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results show that HandDiff achieves the new state-of-the-art record with mean distance errors of 5.72 and 6.53 mm on two challenging datasets, ICVL ... | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, the proposed kinematic correspondence improves performance by learning the inter-joint relations. | p. 8 (4.4. Ablation Study) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Therefore, the proposed joint indicator and joint-wise condition that introduce permutation information are mandatory to improve performance. | p. 8 (4.4. Ablation Study) |

## Dataset / Benchmark Role

- **p. 5 / 4.2. Datasets and Evaluation Metrics - extractive PDF cue:** This dataset defines four official dataset split protocols: S0 - seen subjects, camera views, grasped objects; S1 - unseen subjects; S2 - unseen camera views; ...
- **p. 7 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** We compare HandDiff on the hand-object dataset DexYCB with other state-of-the-art method on the official dataset split protocals, including A2J [53], Spurr et al.
- **p. 5 / 4.2. Datasets and Evaluation Metrics - extractive PDF cue:** The DexYCB dataset [3] is a recently released hand-object dataset that consists of 582,000 image frames with 21 annotated joints, 10 different subjects, and 20 ...
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** Qualitative results of HandDiff on the DexYCB datasets including different grabbing poses (top), self-occlusions (middle), and object occlusions (bottom).
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** The proposed model also achieves the third-lowest error on the NYU dataset.
- **p. 7 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** 12, 15, and 52 mm on the ICVL, MSRA, and NYU datasets, respectively.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** All the ablation models are trained and tested on the DexYCB dataset .
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** The joints must be generated in a specific permutation in order to match the permutation defined by the dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Illustration of the hand pose diffusion concept. The model extracts features from input depth images and correspond- ing point clouds as joint-wise and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The pipeline of the proposed HandDiff. HandDiff takes the normalized point cloud transformed from a 2D depth image as the input. The PointNet-based ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of the proposed method with previous state- of-the-art methods on the ICVL, MSRA, and NYU datasets. Input indicates the input type of ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison of the proposed method with previous state- of-the-art methods on the DexYCB datasets.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative results of HandDiff on the DexYCB datasets including different grabbing poses (top), self-occlusions (middle), and object occlusions (bottom). Hand-depth images (first rows) ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparison with the state-of-the-art methods using the ICVL (left), MSRA (middle), and NYU (right) dataset. The per joint error (top) and success rate ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative results of HandDiff on the ICVL (left), MSRA (middle), and NYU (right) datasets. Hand-depth images are trans- formed into 3D points in ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Ablations of different proposed components. All the ab- lation models are trained and tested on the DexYCB dataset . JC LC JI KC ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This dataset defines four official dataset split protocols: S0 - seen subjects, camera views, grasped objects; S1 - unseen subjects; S2 - unseen camera ... | embodiment, simulator version and control stack | p. 5 (4.2. Datasets and Evaluation Metrics), p. 7 (4.3. Comparison with State-of-the-Art Methods) |
| Task/environment | We compare HandDiff on the hand-object dataset DexYCB with other state-of-the-art method on the official dataset split protocals, including A2J [53], Spurr et al. | reset, timeout, object/scene variation | p. 7 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.2. Datasets and Evaluation Metrics) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3. The Proposed Hand Pose Diffusion Model) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We employ two commonly used metrics, the mean joint error, and the success rate, to evaluate the performance of hand pose estimation. | definition/direction/unit from same section | p. 5 (4.2. Datasets and Evaluation Metrics) |
| The success rate reveals the percentage of good frames with a mean joint error of less than a certain distance threshold. | definition/direction/unit from same section | p. 6 (16.05 21.22 27.01 17.93 20.55 RGB) |
| The per joint error (top) and success rate (bottom) are shown in this figure. | definition/direction/unit from same section | p. 7 (4.3. Comparison with State-of-the-Art Methods) |
| The results show that HandDiff achieves the new state-of-the-art record with mean distance errors of 5.72 and 6.53 mm on two challenging datasets, ICVL ... | definition/direction/unit from same section | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| Finally, the multiple hypotheses further boost the accuracy. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| As expected, the error decreases as the hypothese amount increases. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| The diffusion timestep was set to 500 with a cosine variance scheduler. | definition/direction/unit from same section | p. 5 (4.1. Experiment Settings) |
| The qualitative results visualized in Figure 3 also reveal that HandDiff can estimate accurate poses from hand-object interaction scenarios with various occlusions. | definition/direction/unit from same section | p. 7 (4.3. Comparison with State-of-the-Art Methods) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 2, HandDiff outperforms previous SOTA methods in all four protocols. | comparison identity and matched condition | p. 7 (4.3. Comparison with State-of-the-Art Methods) |
| Comparison with the state-of-the-art methods using the ICVL (left), MSRA (middle), and NYU (right) dataset. | comparison identity and matched condition | p. 7 (4.3. Comparison with State-of-the-Art Methods) |
| The results show that HandDiff achieves the new state-of-the-art record with mean distance errors of 5.72 and 6.53 mm on two challenging datasets, ICVL ... | comparison identity and matched condition | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| Input indicates the input type of 2D depth image (D), 3D voxels (V), or 3D point cloud (P). † The results are reported from ... | comparison identity and matched condition | p. 6 (4.2. Datasets and Evaluation Metrics) |
| The reason is intuitive that the quantity of hand keypoints to be denoised is relatively small compared to other heavy image/point cloud denoising tasks, ... | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |
| Ablations of different proposed components. | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conducted extensive ablation experiments to evaluate the contribution of each component proposed in our model. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Based on this baseline, we incrementally adopt the proposed components and conduct ablations as follows: 1) using local conditions (LC); 2) using joint indicator ... | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Ablations of different modalities of conditions. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| All the ablation models are trained and tested on the DexYCB dataset . | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The following is a summary of our primary contributions: • We propose a novel diffusion-based model for hand pose estimation that utilizes the depth ... | The results also demonstrate that the proposed HandDiff significantly outperforms other 2D image-based methods by large margins since HandDiff directly performs the processing on ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.2. Datasets and Evaluation Metrics), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 7 (4.3. Comparison with State-of-the-Art Methods) |
| Primary metric/result | We employ two commonly used metrics, the mean joint error, and the success rate, to evaluate the performance of hand pose estimation. | numeric claim only at cited anchor | p. 5 (4.2. Datasets and Evaluation Metrics) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experiment Settings - extractive PDF cue:** We trained the model for 30 epochs with a learning rate decay of 0.1 after every 10 epochs.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** On the other hand, the model with only 3D conditions cannot capture dense features from only 1024 points, thus the estimation error significantly increases.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** In addition, the computation time and memory of the model are 98 ms and 2.2GB per frame, respectively, for 10 timesteps (1 hypothese).
- **p. 3 / 3. The Proposed Hand Pose Diffusion Model - extractive PDF cue:** We construct a ConvNeXt-based autoenoder to generate a 2D local visual feature map F2d ∈RH/2×W/2×d2d and a 2D global vector.
- **p. 3 / 3. The Proposed Hand Pose Diffusion Model - extractive PDF cue:** Due to the irregularity and disorder of the input point set, we exploit the hierarchical point cloud encoder [25, 34] proposed by PointNet++ [34] to ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, a limitation of HandDiff is its inability to handle scenarios with interacting hands. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Future research avenues could explore extensions to bipartite graph learning and skeleton-based analysis to address these limitations and further enhance the model's capabilities. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 2. The pipeline of the proposed HandDiff. HandDiff takes the normalized point cloud transformed from a 2D depth image as the input. The ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Hand-depth images (first rows) are transformed into 3D points (second rows) in order to clearly present occlusions as shown in the figure. | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| body limitation/failure cue | Qualitative results of HandDiff on the DexYCB datasets including different grabbing poses (top), self-occlusions (middle), and object occlusions (bottom). | p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| body limitation/failure cue | Briefly, 3DDPM is a share-weight point-wise denoiser conditioned on a global shape latent. | p. 7 (4.4. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We trained the model for 30 epochs with a learning rate decay of 0.1 after every 10 epochs. | p. 5 (4.1. Experiment Settings) |
| For training, we used the AdamW optimizer [26] with beta1 = 0.5, beta2 = 0.999, and learning rate α = 0.001. | p. 5 (4.1. Experiment Settings) |
| Larger timesteps exhibit a negligible impact on performance. | p. 8 (4.4. Ablation Study) |
| The results also show that 10 timesteps appear as the optimal 7.44 mm. | p. 8 (4.4. Ablation Study) |
| The depth image and the N points are first supplied into a local condition encoder that extracts local and global features. | p. 3 (3. The Proposed Hand Pose Diffusion Model) |
| Due to the irregularity and disorder of the input point set, we exploit the hierarchical point cloud encoder [25, 34] proposed by PointNet++ [34] ... | p. 3 (3. The Proposed Hand Pose Diffusion Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** However, a limitation of HandDiff is its inability to handle scenarios with interacting hands.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Future research avenues could explore extensions to bipartite graph learning and skeleton-based analysis to address these limitations and further enhance the model's capabilities.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The pipeline of the proposed HandDiff. HandDiff takes the normalized point cloud transformed from a 2D depth image as the input. The PointNet-based ...
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** Hand-depth images (first rows) are transformed into 3D points (second rows) in order to clearly present occlusions as shown in the figure.
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive PDF cue:** Qualitative results of HandDiff on the DexYCB datasets including different grabbing poses (top), self-occlusions (middle), and object occlusions (bottom).
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** Briefly, 3DDPM is a share-weight point-wise denoiser conditioned on a global shape latent.

- **PDF anchors reviewed:** datasets p. 5 (4.2. Datasets and Evaluation Metrics), p. 7 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.2. Datasets and Evaluation Metrics), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 7 (4.3. Comparison with State-of-the-Art Methods), metrics p. 5 (4.2. Datasets and Evaluation Metrics), p. 6 (16.05 21.22 27.01 17.93 20.55 RGB), p. 7 (4.3. Comparison with State-of-the-Art Methods), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), baselines p. 7 (4.3. Comparison with State-of-the-Art Methods), p. 7 (4.3. Comparison with State-of-the-Art Methods), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 6 (4.2. Datasets and Evaluation Metrics), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), results p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.2. Datasets and Evaluation Metrics), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 7 (4.3. Comparison with State-of-the-Art Methods).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
