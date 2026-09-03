# Evaluation - Scaling Diffusion Models to Real-World 3D LiDAR Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Nunes_Scaling_Diffusion_Models_to_Real-World_3D_LiDAR_Scene_Completion_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Nunes_Scaling_Diffusion_Models_to_Real-World_3D_LiDAR_Scene_Completion_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption)): Figure 6. Mean and standard deviation of the predicted noise ϵθ over different regularization weights. In this experiment we use DPMSolver [17] to reduce the denoising steps from 1, 000 ...

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive body cue:** For training our DDPM, we used the SemanticKITTI dataset [2, 9], an autonomous driving benchmark with point-wise annotations over sequences of LiDAR scans collected in ...
- **p. 5 / 4. Experiments - extractive body cue:** To generate the ground truth complete scans, we used the dataset poses to aggregate the scans in the sequence and remove moving objects with the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. Tab. 3 shows the IoU of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. posed by Song et al. [38] ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Mean chamfer distance and Jensen-Shannon divergence evaluation on KITTI-360 sequence 00 and our data. ing that current 3D diffusion methods cannot directly be ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Mean chamfer distance over a short sequence from the validation set of SemanticKITTI. quence from the SemanticKITTI validation set. We run the scene ...
- **p. 5 / 4. Experiments - extractive body cue:** Then, we evaluate the completed scene by comparing it with the corresponding region in the ground truth map.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Mean and standard deviation of the predicted noise ϵθ without the noise regularization. In this experiment we use DPM- Solver [17] to reduce ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 6. Mean and standard deviation of the predicted noise ϵθ over different regularization weights. In this experiment we use DPMSolver [17] to reduce ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2. Mean chamfer distance and Jensen-Shannon divergence evaluation on KITTI-360 sequence 00 and our data. ing that current 3D diffusion methods cannot directly ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5. Qualitative results on one scan from KITTI-360. Colors depict point height normalized by the height range of each point cloud. IoU [%] ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. Tab. 3 shows the IoU ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive body cue:** For training our DDPM, we used the SemanticKITTI dataset [2, 9], an autonomous driving benchmark with point-wise annotations over sequences of LiDAR scans collected in ...
- **p. 5 / 4. Experiments - extractive body cue:** To generate the ground truth complete scans, we used the dataset poses to aggregate the scans in the sequence and remove moving objects with the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Starting from a single input scan P, we add Gaussian noise to each point, defining the noisy input PT . Then, we use ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Comparison between Gaussian noise with standard de- viation σ and mean µ over non-normalized and normalized input point cloud and our proposed local ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Mean and standard deviation of the predicted noise ϵθ without the noise regularization. In this experiment we use DPM- Solver [17] to reduce ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Diagram of the conditioning in each layer l. then our final loss becomes: \math c a l {L} = \mat hcal {L}_{\text {diff}} ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Mean chamfer distance and Jensen-Shannon divergence evaluation on validation set from SemanticKITTI. steps T from 1, 000 to 50. Besides, we set the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Mean chamfer distance and Jensen-Shannon divergence evaluation on KITTI-360 sequence 00 and our data. ing that current 3D diffusion methods cannot directly be ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results on one scan from KITTI-360. Colors depict point height normalized by the height range of each point cloud. IoU [%] Grid ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. posed by Song et al. [38] ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For training our DDPM, we used the SemanticKITTI dataset [2, 9], an autonomous driving benchmark with point-wise annotations over sequences of LiDAR scans collected ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Task/environment | To generate the ground truth complete scans, we used the dataset poses to aggregate the scans in the sequence and remove moving objects with ... | reset, timeout, object/scene variation | p. 5 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.2. Diffusion scene completion), p. 3 (3.1. Denoising diffusion probabilistic models) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Diffusion scene completion), p. 6 (4.1. Scene reconstruction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 4. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. Tab. 3 shows the IoU ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 3. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. posed by Song et al. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| To generate the ground truth complete scans, we used the dataset poses to aggregate the scans in the sequence and remove moving objects with ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Table 2. Mean chamfer distance and Jensen-Shannon divergence evaluation on KITTI-360 sequence 00 and our data. ing that current 3D diffusion methods cannot directly ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 5. Mean chamfer distance over a short sequence from the validation set of SemanticKITTI. quence from the SemanticKITTI validation set. We run the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Then, we evaluate the completed scene by comparing it with the corresponding region in the ground truth map. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Figure 3. Mean and standard deviation of the predicted noise ϵθ without the noise regularization. In this experiment we use DPM- Solver [17] to ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 6. Mean and standard deviation of the predicted noise ϵθ over different regularization weights. In this experiment we use DPMSolver [17] to reduce ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 4. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. Tab. 3 shows the IoU ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 2. Mean chamfer distance and Jensen-Shannon divergence evaluation on KITTI-360 sequence 00 and our data. ing that current 3D diffusion methods cannot directly ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 6. Mean and standard deviation of the predicted noise ϵθ over different regularization weights. In this experiment we use DPMSolver [17] to reduce ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| For the ground truth, we randomly sample 180, 000 points without replacement. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Figure 2. Comparison between Gaussian noise with standard de- viation σ and mean µ over non-normalized and normalized input point cloud and our proposed ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Figure 3. Mean and standard deviation of the predicted noise ϵθ without the noise regularization. In this experiment we use DPM- Solver [17] to ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For the ground truth, we randomly sample 180, 000 points without replacement. | component/input/data sensitivity | p. 5 (4. Experiments) |
| To remove the moving objects from the map in KITTI-360 and our data, we used an off-the-shelf moving object segmentation [24]. | component/input/data sensitivity | p. 5 (4. Experiments) |
| Figure 3. Mean and standard deviation of the predicted noise ϵθ without the noise regularization. In this experiment we use DPM- Solver [17] to ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our key contributions are: • We propose a novel scene-scale diffusion scheme for 3D sensor data that operates at the point level. ... | Figure 6. Mean and standard deviation of the predicted noise ϵθ over different regularization weights. In this experiment we use DPMSolver [17] to reduce ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Table 2. Mean chamfer distance and Jensen-Shannon divergence evaluation on KITTI-360 sequence 00 and our data. ing that current 3D diffusion methods cannot directly ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive body cue:** We train our model for 20 epochs, using only the training set from SemanticKITTI.
- **p. 5 / 4. Experiments - extractive body cue:** As optimizer, we used Adam [13] with a learning rate of 10-4 decreased by half every 5 epochs, and decay of 10-4, with batch size ...
- **p. 5 / 4. Experiments - extractive body cue:** For each input scan, we define the scan range as 50 m and sample 18, 000 points with farthest point sampling.
- **p. 5 / 4. Experiments - extractive body cue:** For the ground truth, we randomly sample 180, 000 points without replacement.
- **p. 6 / Method - extractive body cue:** To maintain the same amount of points used during training, we again use the scan max range as 50 m and sample 18, 000 points ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For future work, we plan on extending our method to generate unconditional data, creating novel 3D point cloud scenes. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Table 2. Mean chamfer distance and Jensen-Shannon divergence evaluation on KITTI-360 sequence 00 and our data. ing that current 3D diffusion methods cannot directly ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Table 4. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. Tab. 3 shows the IoU ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | We define each point as the origin of the sampled Gaussian noise, learning an iterative denoising process to gradually predict offsets to reconstruct the ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 1. Starting from a single input scan P, we add Gaussian noise to each point, defining the noisy input PT . Then, we ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Comparison between Gaussian noise with standard de- viation σ and mean µ over non-normalized and normalized input point cloud and our proposed ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As optimizer, we used Adam [13] with a learning rate of 10-4 decreased by half every 5 epochs, and decay of 10-4, with batch ... | p. 5 (4. Experiments) |
| We train our model for 20 epochs, using only the training set from SemanticKITTI. | p. 5 (4. Experiments) |
| (4) we can compute the noise at any step t, from which we can use Eq. | p. 3 (3.1. Denoising diffusion probabilistic models) |
| (2) to compute xT -1, . . . , x0, where x0 is a newly generated sample conditioned on c. | p. 3 (3.1. Denoising diffusion probabilistic models) |
| However, GT retains little information from G due to the T diffusion steps. | p. 4 (3.2. Diffusion scene completion) |
| Finally, we calculate the T denoising steps by predicting the noise at step t from Eq. | p. 4 (3.3. Local point denoising) |
| For all baselines, we used their official code and the provided weights also trained on SemanticKITTI. | p. 6 (Method) |
| Mean chamfer distance and Jensen-Shannon divergence evaluation on validation set from SemanticKITTI. steps T from 1, 000 to 50. | p. 6 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** For future work, we plan on extending our method to generate unconditional data, creating novel 3D point cloud scenes.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Mean chamfer distance and Jensen-Shannon divergence evaluation on KITTI-360 sequence 00 and our data. ing that current 3D diffusion methods cannot directly be ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Completion metric where the IoU is computed against the ground truth and prediction grids with different resolutions. Tab. 3 shows the IoU of ...
- **p. 8 / 5. Conclusion - extractive body cue:** We define each point as the origin of the sampled Gaussian noise, learning an iterative denoising process to gradually predict offsets to reconstruct the scene ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Starting from a single input scan P, we add Gaussian noise to each point, defining the noisy input PT . Then, we use ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Comparison between Gaussian noise with standard de- viation σ and mean µ over non-normalized and normalized input point cloud and our proposed local ...

- **Evidence anchors reviewed:** datasets p. 5 (4. Experiments), p. 5 (4. Experiments), metrics p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (4. Experiments), baselines p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 4 (Figure/Table caption), p. 4 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
