# Evaluation - Flash3D: Feed-Forward Generalisable 3D Scene Reconstruction from a Single Image

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=05T81ScPFb&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. In-domain novel view synthesis), p. 5 (4.1. Experiment settings), p. 5 (4.1. Experiment settings), p. 7 (4.4. Comparison to few-view novel view synthesis), p. 6 (4.2. Cross-domain novel view synthesis), p. 6 (4.3. In-domain novel view synthesis)): 2, we observe that we achieve state-of-the-art results on this mature benchmark across all distances between the source and the target.

## Evaluation Body Digest

- **p. 5 / 4.1. Experiment settings - extractive PDF cue:** We follow the default training/testing split with 67,477 scenes for training and 7,289 for testing.
- **p. 5 / 4.2. Cross-domain novel view synthesis - extractive PDF cue:** To evaluate the cross-domain generalisation ability, we directly evaluate performance on unseen outdoor (KITTI [18]) and indoor (NYU [65]) datasets.
- **p. 7 / 4.5. Ablation study and analysis - extractive PDF cue:** Q1: Is leveraging a monocular depth predictor useful in the task of reconstructing appearance and geometry of scenes?
- **p. 6 / 4.2. Cross-domain novel view synthesis - extractive PDF cue:** Qualitative comparison of monocular reconstruction on all datasets.
- **p. 6 / 4.3. In-domain novel view synthesis - extractive PDF cue:** We evaluate the quality of zero-shot reconstruction and compare performance on an in-domain dataset, RealEstate10k.
- **p. 7 / 4.3. In-domain novel view synthesis - extractive PDF cue:** 2, we observe that we achieve state-of-the-art results on this mature benchmark across all distances between the source and the target.
- **p. 8 / 4.5. Ablation study and analysis - extractive PDF cue:** The second layer (third column) represents the remaining parts of the scene (red arrows): occluded regions (wall, cabinet) and regions where depth prediction is unreliable ...
- **p. 5 / 4.1. Experiment settings - extractive PDF cue:** We evaluate Novel View Synthesis accuracy on datasets not used in training of our method.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experiment settings (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. In-domain novel view synthesis | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, we observe that we achieve state-of-the-art results on this mature benchmark across all distances between the source and the target. | p. 7 (4.3. In-domain novel view synthesis) |
| 4.1. Experiment settings | EMPIRICAL / SOURCE-REPORTED EVALUATION | We outperform baselines which were trained on KITTI specifically. | p. 5 (4.1. Experiment settings) |
| 4.1. Experiment settings | EMPIRICAL / SOURCE-REPORTED EVALUATION | With this, Flash3D can be trained to achieve state-of-the-art quality on a single A6000 GPU in 16 hours. | p. 5 (4.1. Experiment settings) |
| 4.4. Comparison to few-view novel view synthesis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Here, Flash3D cannot outperform two-view approaches on the interpolation task, due to receiving less information. | p. 7 (4.4. Comparison to few-view novel view synthesis) |
| 4.2. Cross-domain novel view synthesis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our model shows state-of-the-art in-domain performance on RealEstate10k on small, medium and large baseline ranges. | p. 6 (4.2. Cross-domain novel view synthesis) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experiment settings - extractive PDF cue:** We follow the default training/testing split with 67,477 scenes for training and 7,289 for testing.
- **p. 5 / 4.2. Cross-domain novel view synthesis - extractive PDF cue:** To evaluate the cross-domain generalisation ability, we directly evaluate performance on unseen outdoor (KITTI [18]) and indoor (NYU [65]) datasets.
- **p. 7 / 4.5. Ablation study and analysis - extractive PDF cue:** Q1: Is leveraging a monocular depth predictor useful in the task of reconstructing appearance and geometry of scenes?
- **p. 6 / 4.2. Cross-domain novel view synthesis - extractive PDF cue:** Qualitative comparison of monocular reconstruction on all datasets.
- **p. 6 / 4.3. In-domain novel view synthesis - extractive PDF cue:** We evaluate the quality of zero-shot reconstruction and compare performance on an in-domain dataset, RealEstate10k.
- **p. 7 / 4.3. In-domain novel view synthesis - extractive PDF cue:** 2, we observe that we achieve state-of-the-art results on this mature benchmark across all distances between the source and the target.
- **p. 8 / 4.5. Ablation study and analysis - extractive PDF cue:** The second layer (third column) represents the remaining parts of the scene (red arrows): occluded regions (wall, cabinet) and regions where depth prediction is unreliable ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. Flash3D reconstructs the 3D (not 2.5D) scene structure and appearance from just a single image ‘in a flash', enabling accurate novel view synthesis. ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of Flash3D. Given a single image I as input, Flash3D first estimates the metric depth D using a frozen off-the-shelf network [49]. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Cross-Domain Novel View Synthesis. We evaluate Novel View Synthesis accuracy on datasets not used in training of our method. We outperform baselines which ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. In-domain Novel View Synthesis. Our model shows state-of-the-art in-domain performance on RealEstate10k on small, medium and large baseline ranges. 5 frames 10 frames ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative comparison of monocular reconstruction on all datasets. Flash3D (Ours, right column) is sharper (top row, car's back) than state-of-the-art MINE [37] despite ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation Study. Results for ablating different design choices of our method. RE10k - in-domain NYU - cross-domain KITTI - cross-domain PSNR ↑ SSIM ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Comparison with Two-view Methods. We compare on the split used by pixelSplat [9] for two-view interpolation and on the split used by latentSplat ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Ablation. We show how Flash3D degrades when components are removed. Removing the depth network (4th column) results in incorrect geometry (orange wall, corner ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We follow the default training/testing split with 67,477 scenes for training and 7,289 for testing. | embodiment, simulator version and control stack | p. 5 (4.1. Experiment settings), p. 5 (4.2. Cross-domain novel view synthesis) |
| Task/environment | To evaluate the cross-domain generalisation ability, we directly evaluate performance on unseen outdoor (KITTI [18]) and indoor (NYU [65]) datasets. | reset, timeout, object/scene variation | p. 5 (4.2. Cross-domain novel view synthesis), p. 7 (4.5. Ablation study and analysis) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 5 (3.2. Monocular feed-forward multi-Gaussians) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Monocular feed-forward multi-Gaussians), p. 4 (3.2. Monocular feed-forward multi-Gaussians) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate Novel View Synthesis accuracy on datasets not used in training of our method. | definition/direction/unit from same section | p. 5 (4.1. Experiment settings) |
| Finally, we show via ablation studies how each design choice contributes to performance Flash3D (Sec. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Our model shows state-of-the-art in-domain performance on RealEstate10k on small, medium and large baseline ranges. | definition/direction/unit from same section | p. 6 (4.2. Cross-domain novel view synthesis) |
| We evaluate the quality of zero-shot reconstruction and compare performance on an in-domain dataset, RealEstate10k. | definition/direction/unit from same section | p. 6 (4.3. In-domain novel view synthesis) |
| This also results in a drop in performance in Tab. | definition/direction/unit from same section | p. 7 (4.5. Ablation study and analysis) |
| This understandably drops the performance even further. | definition/direction/unit from same section | p. 7 (4.5. Ablation study and analysis) |
| Blurriness could be reduced with additional losses (perceptual [103] or adversarial [23]). | definition/direction/unit from same section | p. 8 (4.5. Ablation study and analysis) |
| Alternatively, our method could be incorporated as conditioning within a framework similar to [8] or as the reconstructor in a diffusion-based feed-forward 3D generation ... | definition/direction/unit from same section | p. 8 (4.5. Ablation study and analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We outperform baselines which were trained on KITTI specifically. | comparison identity and matched condition | p. 5 (4.1. Experiment settings) |
| Our model shows state-of-the-art in-domain performance on RealEstate10k on small, medium and large baseline ranges. | comparison identity and matched condition | p. 6 (4.2. Cross-domain novel view synthesis) |
| Finally, while not a fair comparison, we also compare with state-of-the-art two-view novel view synthesis methods, including [14], pixelSplat [9], MVSplat [11], and latentSplat ... | comparison identity and matched condition | p. 5 (4.1. Experiment settings) |
| Flash3D (Ours, right column) is sharper (top row, car's back) than state-of-the-art MINE [37] despite Flash3D not training on KITTI. | comparison identity and matched condition | p. 6 (4.2. Cross-domain novel view synthesis) |
| However, Flash3D surpasses all previous state-of-the-art two-view methods at view extrapolation. | comparison identity and matched condition | p. 7 (4.4. Comparison to few-view novel view synthesis) |
| Here, Flash3D cannot outperform two-view approaches on the interpolation task, due to receiving less information. | comparison identity and matched condition | p. 7 (4.4. Comparison to few-view novel view synthesis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4. Ablation. We show how Flash3D degrades when components are removed. Removing the depth network (4th column) results in incorrect geometry (orange wall, ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 7. Ablations on different depth models. We fit hyperparameters of the depth unprojection model via gradient-based optimisation. We try two variants: one with ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| We then go further and remove the network that predicts P1, removing learning altogether. | component/input/data sensitivity | p. 7 (4.5. Ablation study and analysis) |
| We remove the pretrained depth network that predicts depth D, instead estimating it jointly with all other parameters. | component/input/data sensitivity | p. 7 (4.5. Ablation study and analysis) |
| Finally, we show via ablation studies how each design choice contributes to performance Flash3D (Sec. | component/input/data sensitivity | p. 5 (4. Experiments) |
| Figure 6. Analysis of Gaussian allocation. Gaussians from the first layer (red) are allocated in visible parts, from the second layer (green) in occluded ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we introduce a new, simple, efficient and performant approach for monocular scene reconstruction called | 2, we observe that we achieve state-of-the-art results on this mature benchmark across all distances between the source and the target. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. In-domain novel view synthesis), p. 5 (4.1. Experiment settings), p. 5 (4.1. Experiment settings), p. 7 (4.4. Comparison to few-view novel view synthesis), p. 6 (4.2. Cross-domain novel view synthesis), p. 6 (4.3. In-domain novel view synthesis) |
| Primary metric/result | We outperform baselines which were trained on KITTI specifically. | numeric claim only at cited anchor | p. 5 (4.1. Experiment settings) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experiment settings - extractive PDF cue:** We follow the default training/testing split with 67,477 scenes for training and 7,289 for testing.
- **p. 5 / 4.1. Experiment settings - extractive PDF cue:** With this, Flash3D can be trained to achieve state-of-the-art quality on a single A6000 GPU in 16 hours.
- **p. 6 / 4.2. Cross-domain novel view synthesis - extractive PDF cue:** 5 frames 10 frames U[-30, 30] frames Model PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ...
- **p. 7 / 4.5. Ablation study and analysis - extractive PDF cue:** 3 indicates that without the depth network, 2 layers of Gaussians per pixel performs worse than using just one layer.
- **p. 4 / 3. Method - extractive PDF cue:** Hence, there are C = 1 + 1 + 3 + 7 + 3(L + 1)2 = 12 + 3(L + 1)2 parameters predicted for ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This is thanks to leveraging a depth predictor which, when used on its own (fourth column), cannot represent occluded regions (third row, fourth row). | p. 6 (4.2. Cross-domain novel view synthesis) |
| body limitation/failure cue | Here, Flash3D cannot outperform two-view approaches on the interpolation task, due to receiving less information. | p. 7 (4.4. Comparison to few-view novel view synthesis) |
| body limitation/failure cue | 5 additionally reveals a limitation of our method. | p. 8 (4.5. Ablation study and analysis) |
| body limitation/failure cue | Figure 4. Ablation. We show how Flash3D degrades when components are removed. Removing the depth network (4th column) results in incorrect geometry (orange wall, ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The entire model is trained on a single A6000 GPU for 40,000 iterations with batch size 16. | p. 5 (4.1. Experiment settings) |
| The training is remarkably efficient, completed in one day on a single A6000 GPU. | p. 5 (4.1. Experiment settings) |
| The decoder network thus outputs a tensor Φdec(Φenc(I, D)) ∈R(C-1)×H×W . | p. 4 (3.2. Monocular feed-forward multi-Gaussians) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Cross-domain novel view synthesis - extractive PDF cue:** This is thanks to leveraging a depth predictor which, when used on its own (fourth column), cannot represent occluded regions (third row, fourth row).
- **p. 7 / 4.4. Comparison to few-view novel view synthesis - extractive PDF cue:** Here, Flash3D cannot outperform two-view approaches on the interpolation task, due to receiving less information.
- **p. 8 / 4.5. Ablation study and analysis - extractive PDF cue:** 5 additionally reveals a limitation of our method.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Ablation. We show how Flash3D degrades when components are removed. Removing the depth network (4th column) results in incorrect geometry (orange wall, corner ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experiment settings), p. 5 (4.2. Cross-domain novel view synthesis), p. 7 (4.5. Ablation study and analysis), p. 6 (4.2. Cross-domain novel view synthesis), p. 6 (4.3. In-domain novel view synthesis), p. 7 (4.3. In-domain novel view synthesis), metrics p. 5 (4.1. Experiment settings), p. 5 (4. Experiments), p. 6 (4.2. Cross-domain novel view synthesis), p. 6 (4.3. In-domain novel view synthesis), p. 7 (4.5. Ablation study and analysis), p. 7 (4.5. Ablation study and analysis), baselines p. 5 (4.1. Experiment settings), p. 6 (4.2. Cross-domain novel view synthesis), p. 5 (4.1. Experiment settings), p. 6 (4.2. Cross-domain novel view synthesis), p. 7 (4.4. Comparison to few-view novel view synthesis), p. 7 (4.4. Comparison to few-view novel view synthesis), results p. 7 (4.3. In-domain novel view synthesis), p. 5 (4.1. Experiment settings), p. 5 (4.1. Experiment settings), p. 7 (4.4. Comparison to few-view novel view synthesis), p. 6 (4.2. Cross-domain novel view synthesis), p. 6 (4.3. In-domain novel view synthesis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
