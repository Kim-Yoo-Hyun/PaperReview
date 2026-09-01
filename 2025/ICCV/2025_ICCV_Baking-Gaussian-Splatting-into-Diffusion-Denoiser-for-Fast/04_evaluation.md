# Evaluation - Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Cai_Baking_Gaussian_Splatting_into_Diffusion_Denoiser_for_Fast_and_Scalable_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Cai_Baking_Gaussian_Splatting_into_Diffusion_Denoiser_for_Fast_and_Scalable_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption)): Table 2. Ablation study. Results on the GSO [13] dataset are listed. the highest score while enjoying over 5× and 10× infer- ence speed compared to the SOTA 3D diffusion ...

## Evaluation Body Digest

- **p. 6 / 4. Experiment - extractive PDF cue:** Then we finetune the model on the object- and scene-level datasets with 64 A100 GPUs for 80K and 54K iterations at the per-GPU batch size ...
- **p. 6 / 4. Experiment - extractive PDF cue:** We adopt RealEstate10K [90] and DL3DV10K [36] as the scene-level training datasets.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Visual comparison of single-view object generation on ABO, GSO, real-camera image, and text-to-image prompted by FLUX. Our method can generate more fine-grained details ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study. Results on the GSO [13] dataset are listed. the highest score while enjoying over 5× and 10× infer- ence speed compared ...
- **p. 6 / 4. Experiment - extractive PDF cue:** The learning rate is linearly warmed up to 4e-4 with 2K iterations 25067
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Single-view object generation (upper) and scene reconstruction (lower) results of our method. For single-view object generation, the prompt views are shown in the ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Single-view object generation results of our method on GSO [13], wild images, and text-to-images prompted by stable diffusion or FLUX. Our DiffusionGS can ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 8. Visual comparison between the SOTA 2D method PhotoNVS [82] in (b) and our method in (c) on NVS and relative depth estimation. The ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2. Ablation study. Results on the GSO [13] dataset are listed. the highest score while enjoying over 5× and 10× infer- ence speed ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. Single-view object generation (upper) and scene reconstruction (lower) results of our method. For single-view object generation, the prompt views are shown in ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2. Single-view object generation results of our method on GSO [13], wild images, and text-to-images prompted by stable diffusion or FLUX. Our DiffusionGS ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 6. Visual comparison of single-view object generation on ABO, GSO, real-camera image, and text-to-image prompted by FLUX. Our method can generate more fine-grained ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1. User study and main quantitative results of single-view image-to-3D task on ABO [11], GSO [13], and Realestate10K [90]. | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiment - extractive PDF cue:** Then we finetune the model on the object- and scene-level datasets with 64 A100 GPUs for 80K and 54K iterations at the per-GPU batch size ...
- **p. 6 / 4. Experiment - extractive PDF cue:** We adopt RealEstate10K [90] and DL3DV10K [36] as the scene-level training datasets.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Single-view object generation (upper) and scene reconstruction (lower) results of our method. For single-view object generation, the prompt views are shown in the ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Single-view object generation results of our method on GSO [13], wild images, and text-to-images prompted by stable diffusion or FLUX. Our DiffusionGS can ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Single-view scene reconstruction of our method on indoor and outdoor scenes. The depth maps are rendered by GS point clouds. DiffusionGS to both ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Pipeline. (a) When selecting the data for our scene-object mixed training, we impose two angle constraints on the positions and orientations of viewpoint ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Pl¨ucker ray vs. Reference-Point Pl¨ucker Coordinate. into non-overlapping tiles. The 3D Gaussians are assigned to the tiles where their 2D projections cover. For ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Visual comparison of single-view object generation on ABO, GSO, real-camera image, and text-to-image prompted by FLUX. Our method can generate more fine-grained details ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. User study and main quantitative results of single-view image-to-3D task on ABO [11], GSO [13], and Realestate10K [90].
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7. Visual results of single-view scene reconstruction. We train the feedforward methods with the same scene data for fairness. Previous methods yield blurry images ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Then we finetune the model on the object- and scene-level datasets with 64 A100 GPUs for 80K and 54K iterations at the per-GPU batch ... | embodiment, simulator version and control stack | p. 6 (4. Experiment), p. 6 (4. Experiment) |
| Task/environment | We adopt RealEstate10K [90] and DL3DV10K [36] as the scene-level training datasets. | reset, timeout, object/scene variation | p. 6 (4. Experiment) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.1. DiffusionGS), p. 4 (3.1. DiffusionGS) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.2. Scene-Object Mixed Training Strategy), p. 7 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 6. Visual comparison of single-view object generation on ABO, GSO, real-camera image, and text-to-image prompted by FLUX. Our method can generate more fine-grained ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 2. Ablation study. Results on the GSO [13] dataset are listed. the highest score while enjoying over 5× and 10× infer- ence speed ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| The learning rate is linearly warmed up to 4e-4 with 2K iterations 25067 | definition/direction/unit from same section | p. 6 (4. Experiment) |
| Figure 1. Single-view object generation (upper) and scene reconstruction (lower) results of our method. For single-view object generation, the prompt views are shown in ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Single-view object generation results of our method on GSO [13], wild images, and text-to-images prompted by stable diffusion or FLUX. Our DiffusionGS ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 8. Visual comparison between the SOTA 2D method PhotoNVS [82] in (b) and our method in (c) on NVS and relative depth estimation. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 9. Visual analysis. (a) studies the effect of mixed training. (b) shows generation diversity. (c) shows the comparison with MIDI [22]. and black ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2. Ablation study. Results on the GSO [13] dataset are listed. the highest score while enjoying over 5× and 10× infer- ence speed ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 6. Visual comparison of single-view object generation on ABO, GSO, real-camera image, and text-to-image prompted by FLUX. Our method can generate more fine-grained ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 9. Visual analysis. (a) studies the effect of mixed training. (b) shows generation diversity. (c) shows the comparison with MIDI [22]. and black ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 8. Visual comparison between the SOTA 2D method PhotoNVS [82] in (b) and our method in (c) on NVS and relative depth estimation. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 9. Visual analysis. (a) studies the effect of mixed training. (b) shows generation diversity. (c) shows the comparison with MIDI [22]. and black ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| For MVImgNet, we crop the object, remove the background, normalize the cameras, and center and scale the object to [-1, 1]3. | component/input/data sensitivity | p. 6 (4. Experiment) |
| Figure 8. Visual comparison between the SOTA 2D method PhotoNVS [82] in (b) and our method in (c) on NVS and relative depth estimation. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 2. Ablation study. Results on the GSO [13] dataset are listed. the highest score while enjoying over 5× and 10× infer- ence speed ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: • We propose a novel framework, DiffusionGS, for 3D object generation and scene reconstruction from single view. ... | Table 2. Ablation study. Results on the GSO [13] dataset are listed. the highest score while enjoying over 5× and 10× infer- ence speed ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Figure 1. Single-view object generation (upper) and scene reconstruction (lower) results of our method. For single-view object generation, the prompt views are shown in ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 3.2. Scene-Object Mixed Training Strategy - extractive PDF cue:** 1iter≤iter0 and 1object are similar.
- **p. 7 / Method - extractive PDF cue:** Finally, we scale up the training resolution from 256×256 to 512×512 and finetune the model for 20K iterations.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Single-view scene reconstruction of our method on indoor and outdoor scenes. The depth maps are rendered by GS point clouds. DiffusionGS to ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 7. Visual results of single-view scene reconstruction. We train the feedforward methods with the same scene data for fairness. Previous methods yield blurry ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. Single-view object generation (upper) and scene reconstruction (lower) results of our method. For single-view object generation, the prompt views are shown in ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Single-view object generation results of our method on GSO [13], wild images, and text-to-images prompted by stable diffusion or FLUX. Our DiffusionGS ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 4. Pipeline. (a) When selecting the data for our scene-object mixed training, we impose two angle constraints on the positions and orientations of ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 9. Visual analysis. (a) studies the effect of mixed training. (b) shows generation diversity. (c) shows the comparison with MIDI [22]. and black ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Then we finetune the model on the object- and scene-level datasets with 64 A100 GPUs for 80K and 54K iterations at the per-GPU batch ... | p. 6 (4. Experiment) |
| In mixed training, we use 32 A100 GPUs to train the model on Objaverse, MVImgNet, RealEstate10K, and DL3DV10K for 40K iterations at the per-GPU ... | p. 6 (4. Experiment) |
| Then the constraints are \s ma l l \ theta _{ c d}^{(i)} \leq \theta _1,~~\theta _{dn}^{(i,j)} \leq \theta _2, \vspace {-1.5mm} (9) where ... | p. 5 (3.2. Scene-Object Mixed Training Strategy) |
| Eventually, the output tokens are fed into the Gaussian decoder to be linearly projected and then unpatchified into per-pixel Gaussian maps ˆH = { ... | p. 4 (3.1. DiffusionGS) |
| (1) for sampling Xt-1 at each noisy view as \s mal l \mathbf { x}_{t - 1 } ^ {(i)} = \ bar {\alpha ... | p. 5 (3.1. DiffusionGS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Single-view scene reconstruction of our method on indoor and outdoor scenes. The depth maps are rendered by GS point clouds. DiffusionGS to both ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7. Visual results of single-view scene reconstruction. We train the feedforward methods with the same scene data for fairness. Previous methods yield blurry images ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Single-view object generation (upper) and scene reconstruction (lower) results of our method. For single-view object generation, the prompt views are shown in the ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Single-view object generation results of our method on GSO [13], wild images, and text-to-images prompted by stable diffusion or FLUX. Our DiffusionGS can ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Pipeline. (a) When selecting the data for our scene-object mixed training, we impose two angle constraints on the positions and orientations of viewpoint ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 9. Visual analysis. (a) studies the effect of mixed training. (b) shows generation diversity. (c) shows the comparison with MIDI [22]. and black spots ...

- **PDF anchors reviewed:** datasets p. 6 (4. Experiment), p. 6 (4. Experiment), metrics p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (4. Experiment), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
