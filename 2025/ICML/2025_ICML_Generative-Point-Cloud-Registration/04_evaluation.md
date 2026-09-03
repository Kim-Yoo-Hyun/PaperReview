# Evaluation - Generative Point Cloud Registration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yoaErYlGE9; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167215. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Ablation Studies and Analysis), p. 7 (4.3. Ablation Studies and Analysis), p. 8 (4.3. Ablation Studies and Analysis), p. 8 (4.3. Ablation Studies and Analysis), p. 6 (4.1. Experimental Setting), p. 5 (Figure/Table caption)): Moreover, because the finetuned Match-ControlNet benefits from task-specific training, it consistently achieves higher registration accuracy than the zero-shot version.

## Evaluation Body Digest

- **p. 6 / 4.2. Comparison with Existing Methods - extractive body cue:** We first perform model evaluation on a widely-used, large-scale indoor benchmark dataset, ScanNet (Dai et al., 2017).
- **p. 6 / 4.1. Experimental Setting - extractive body cue:** Comparison of the methods on rotation, translation, and Chamfer distance on ScanNet (Dai et al., 2017) benchmark dataset.
- **p. 7 / 4.2. Comparison with Existing Methods - extractive body cue:** We next evaluate our method on 3DMatch (Zeng et al., 2017), another widely-used benchmark dataset for 3D registration.
- **p. 8 / 4.3. Ablation Studies and Analysis - extractive body cue:** Ablation studies on 3DMatch (Zeng et al., 2017) dataset.
- **p. 8 / 4.3. Ablation Studies and Analysis - extractive body cue:** 6 (right) shows that RGB data from real-world conditions can degrade under poor lighting, negatively impacting RGB-D matching performance.
- **p. 7 / 4.3. Ablation Studies and Analysis - extractive body cue:** Moreover, because the finetuned Match-ControlNet benefits from task-specific training, it consistently achieves higher registration accuracy than the zero-shot version.
- **p. 6 / 4.1. Experimental Setting - extractive body cue:** Following (El Banani et al., 2021; Yuan et al., 2023), we use rotation error, translation error, and Chamfer error, including the accuracy across varying thresholds ...
- **p. 7 / 4.3. Ablation Studies and Analysis - extractive body cue:** We first evaluate the performance contribution of our developed MatchControlNet: (i) The top block of Table 3 demonstrates that, compared to using generated image pairs ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setting (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation Studies and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, because the finetuned Match-ControlNet benefits from task-specific training, it consistently achieves higher registration accuracy than the zero-shot version. | p. 7 (4.3. Ablation Studies and Analysis) |
| 4.3. Ablation Studies and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Increasing the number of finetuning samples (e.g., to 3K or 5K) provides additional improvements; however, models trained on 3K or 5K samples show comparable ... | p. 7 (4.3. Ablation Studies and Analysis) |
| 4.3. Ablation Studies and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | By contrast, a balanced weight (e.g., ω = 0.50) achieves higher performance. | p. 8 (4.3. Ablation Studies and Analysis) |
| 4.3. Ablation Studies and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | The third block in Table 3 demonstrates that, on the 3DMatch dataset, Generative ColorPCR with the synthesized color even outperforms the original ColorPCR with ... | p. 8 (4.3. Ablation Studies and Analysis) |
| 4.1. Experimental Setting | EMPIRICAL / REAL-ROBOT OR HARDWARE | Following (El Banani et al., 2021; Yuan et al., 2023), we use rotation error, translation error, and Chamfer error, including the accuracy across varying ... | p. 6 (4.1. Experimental Setting) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Comparison with Existing Methods - extractive body cue:** We first perform model evaluation on a widely-used, large-scale indoor benchmark dataset, ScanNet (Dai et al., 2017).
- **p. 6 / 4.1. Experimental Setting - extractive body cue:** Comparison of the methods on rotation, translation, and Chamfer distance on ScanNet (Dai et al., 2017) benchmark dataset.
- **p. 7 / 4.2. Comparison with Existing Methods - extractive body cue:** We next evaluate our method on 3DMatch (Zeng et al., 2017), another widely-used benchmark dataset for 3D registration.
- **p. 8 / 4.3. Ablation Studies and Analysis - extractive body cue:** Ablation studies on 3DMatch (Zeng et al., 2017) dataset.
- **p. 8 / 4.3. Ablation Studies and Analysis - extractive body cue:** 6 (right) shows that RGB data from real-world conditions can degrade under poor lighting, negatively impacting RGB-D matching performance.
- **p. 7 / 4.3. Ablation Studies and Analysis - extractive body cue:** Moreover, because the finetuned Match-ControlNet benefits from task-specific training, it consistently achieves higher registration accuracy than the zero-shot version.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Paradigm comparison of our generative point cloud registration with conventional methods. Unlike geometry-only matching in previous methods, our approach introduces Match- ControlNet, a ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Pipeline of Generative Point Cloud Registration. Given a source and a target point cloud, we first apply Match-ControlNet to generate their corresponding images. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Instead of independently performing ControlNet to gen- erate source and target images, our Match-ControlNet integrates their denoising generation processes into a unified framework, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Compared to the zero-shot Match-ControlNet (top), the finetuned Match-ControlNet can tend to achieve higher 2D-3D geometric consistency and the cross-view texture consistency. information ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison of the methods on rotation, translation, and Chamfer distance on ScanNet (Dai et al., 2017) benchmark dataset. Rotation (deg) Translation (cm) Chamfer ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Left: The visualization of the generated RGB image pairs and the formed color source and target point clouds; Right: In low-overlap cases, the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Comparison of the methods on rotation, translation, and Chamfer distance on 3DMatch (Zeng et al., 2017) benchmark dataset. Rotation (deg) Translation (cm) Chamfer ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation studies on 3DMatch (Zeng et al., 2017) dataset. (*) denotes the default configuration. Rotation (deg) Translation (cm) Chamfer (mm) Accuracy ↑ Error↓ ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We first perform model evaluation on a widely-used, large-scale indoor benchmark dataset, ScanNet (Dai et al., 2017). | embodiment, simulator version and control stack | p. 6 (4.2. Comparison with Existing Methods), p. 6 (4.1. Experimental Setting) |
| Task/environment | Comparison of the methods on rotation, translation, and Chamfer distance on ScanNet (Dai et al., 2017) benchmark dataset. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setting), p. 7 (4.2. Comparison with Existing Methods) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Zero-Shot Geometric Consistency Generation), p. 5 (3.5. Geometric-Color Fused Point Descriptor) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Zero-Shot Geometric Consistency Generation), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Following (El Banani et al., 2021; Yuan et al., 2023), we use rotation error, translation error, and Chamfer error, including the accuracy across varying ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Setting) |
| Table 1. Comparison of the methods on rotation, translation, and Chamfer distance on ScanNet (Dai et al., 2017) benchmark dataset. Rotation (deg) Translation (cm) ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We first evaluate the performance contribution of our developed MatchControlNet: (i) The top block of Table 3 demonstrates that, compared to using generated image ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Studies and Analysis) |
| Our Match-ControlNet effectively mitigates calibration errors and lighting challenges commonly encountered in real-world RGB-D data, thereby improving the matching precision of color point cloud ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies and Analysis) |
| Table 3. Ablation studies on 3DMatch (Zeng et al., 2017) dataset. (*) denotes the default configuration. Rotation (deg) Translation (cm) Chamfer (mm) Accuracy ↑ ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Moreover, because the finetuned Match-ControlNet benefits from task-specific training, it consistently achieves higher registration accuracy than the zero-shot version. | definition/direction/unit from same section | p. 7 (4.3. Ablation Studies and Analysis) |
| Figure 2. Pipeline of Generative Point Cloud Registration. Given a source and a target point cloud, we first apply Match-ControlNet to generate their corresponding ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. Instead of independently performing ControlNet to gen- erate source and target images, our Match-ControlNet integrates their denoising generation processes into a unified ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the 20-frame separation used in (El Banani et al., 2021; Yuan et al., 2023), our approach with a 50-frame separation further reduces ... | comparison identity and matched condition | p. 6 (4.2. Comparison with Existing Methods) |
| Additionally, we find that compared to the DINOv2 image encoding, Stable Diffusion can capture more discriminative representations and achieve higher precisions. | comparison identity and matched condition | p. 7 (4.2. Comparison with Existing Methods) |
| We first evaluate the performance contribution of our developed MatchControlNet: (i) The top block of Table 3 demonstrates that, compared to using generated image ... | comparison identity and matched condition | p. 7 (4.3. Ablation Studies and Analysis) |
| The third block in Table 3 demonstrates that, on the 3DMatch dataset, Generative ColorPCR with the synthesized color even outperforms the original ColorPCR with ... | comparison identity and matched condition | p. 8 (4.3. Ablation Studies and Analysis) |
| Figure 4. Compared to the zero-shot Match-ControlNet (top), the finetuned Match-ControlNet can tend to achieve higher 2D-3D geometric consistency and the cross-view texture consistency. ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Comparison of the methods on rotation, translation, and Chamfer distance on ScanNet (Dai et al., 2017) benchmark dataset. | comparison identity and matched condition | p. 6 (4.1. Experimental Setting) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 2 demonstrates that by incorporating FCGF, Predator, and GeoTrans into our generative point cloud registration framework, their generative variants also consistently achieve the performance ... | component/input/data sensitivity | p. 7 (4.2. Comparison with Existing Methods) |
| 3.5) with three prevalent deep geometric descriptors: FCGF (Choy et al., 2019), Predator (Huang et al., 2021), and GeoTransformer (Qin et al., 2022), resulting ... | component/input/data sensitivity | p. 6 (4.1. Experimental Setting) |
| We next conduct ablation studies on the zero-shot geometric-color feature fusion described in Eq. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies and Analysis) |
| Ablation studies on 3DMatch (Zeng et al., 2017) dataset. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies and Analysis) |
| Figure 8. Source and target image generation via zero-shot Match-ControlNet without any finetuning. 13 | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| During the few-shot fine-tuning stage, we randomly select 3,000 sample pairs from the Scan5 | component/input/data sensitivity | p. 5 (4.1. Experimental Setting) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are as follows: • We propose a new Generative Point Cloud Registration paradigm, aimed at generating cross-view image pairs for ... | Moreover, because the finetuned Match-ControlNet benefits from task-specific training, it consistently achieves higher registration accuracy than the zero-shot version. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Ablation Studies and Analysis), p. 7 (4.3. Ablation Studies and Analysis), p. 8 (4.3. Ablation Studies and Analysis), p. 8 (4.3. Ablation Studies and Analysis), p. 6 (4.1. Experimental Setting), p. 5 (Figure/Table caption) |
| Primary metric/result | Increasing the number of finetuning samples (e.g., to 3K or 5K) provides additional improvements; however, models trained on 3K or 5K samples show comparable ... | numeric claim only at cited anchor | p. 7 (4.3. Ablation Studies and Analysis) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setting - extractive body cue:** During the few-shot fine-tuning stage, we randomly select 3,000 sample pairs from the Scan5
- **p. 6 / 4.2. Comparison with Existing Methods - extractive body cue:** We follow the official data split to divide this dataset into the training, validation, and testing subsets, and construct view pairs by sampling image pairs ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. Pipeline of Generative Point Cloud Registration. Given a source and a target point cloud, we first apply Match-ControlNet to generate their corresponding ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. Instead of independently performing ControlNet to gen- erate source and target images, our Match-ControlNet integrates their denoising generation processes into a unified ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | 6 (right) shows that RGB data from real-world conditions can degrade under poor lighting, negatively impacting RGB-D matching performance. | p. 8 (4.3. Ablation Studies and Analysis) |
| body limitation/failure cue | Our results indicate that both overly high ω (which overemphasizes geometry) and overly low ω (which overemphasizes color) lead to degraded registration accuracy. | p. 8 (4.3. Ablation Studies and Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The code for this project is implemented in PyTorch, and all experiments are conducted on a server equipped with an Intel i5 2.2 GHz ... | p. 6 (4.1. Experimental Setting) |
| Following the default fine-tuning configuration of ControlNet (Zhang et al., 2023), we adopt the AdamW optimizer (Loshchilov, 2017) with a learning rate of 1e-5 ... | p. 6 (4.1. Experimental Setting) |
| As a result, we adopt ω = 0.50 as our default hyperparameter configuration. | p. 8 (4.3. Ablation Studies and Analysis) |
| It operates within the latent space of a pretrained autoencoder, where a denoiser ϵθ(xt; t, c) (conditioned on the timstamp t and tokenized text ... | p. 3 (3.2. Zero-Shot Geometric Consistency Generation) |
| The optimal rigid transformation is typically computed by solving: min R,t X (p∗,q∗)∈C∗ ∥R · p∗+ t -q∗∥2 2 , (1) where C∗denotes the ... | p. 3 (3. Approach) |
| The denoiser follows a UNet architecture with an encoder, middle block, and skip-connected decoder, incorporating stacked transformer and residual modules. | p. 4 (3.2. Zero-Shot Geometric Consistency Generation) |
| ControlNet further equips the denoiser of Stable Diffusion with a learnable encoder copy for encoding the conditional image cI, forming a conditional denoiser: ˜ϵθ(xt; ... | p. 4 (3.2. Zero-Shot Geometric Consistency Generation) |
| It's noted that we only finetune the learnable encoder copy of Match-ControlNet rather than the all parameters to preserve the powerful generation ability of ... | p. 5 (3.4. Few-Shot Consistency Fine-tuning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Pipeline of Generative Point Cloud Registration. Given a source and a target point cloud, we first apply Match-ControlNet to generate their corresponding images. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Instead of independently performing ControlNet to gen- erate source and target images, our Match-ControlNet integrates their denoising generation processes into a unified framework, ...
- **p. 8 / 4.3. Ablation Studies and Analysis - extractive body cue:** 6 (right) shows that RGB data from real-world conditions can degrade under poor lighting, negatively impacting RGB-D matching performance.
- **p. 8 / 4.3. Ablation Studies and Analysis - extractive body cue:** Our results indicate that both overly high ω (which overemphasizes geometry) and overly low ω (which overemphasizes color) lead to degraded registration accuracy.

- **Evidence anchors reviewed:** datasets p. 6 (4.2. Comparison with Existing Methods), p. 6 (4.1. Experimental Setting), p. 7 (4.2. Comparison with Existing Methods), p. 8 (4.3. Ablation Studies and Analysis), p. 8 (4.3. Ablation Studies and Analysis), p. 7 (4.3. Ablation Studies and Analysis), metrics p. 6 (4.1. Experimental Setting), p. 6 (Figure/Table caption), p. 7 (4.3. Ablation Studies and Analysis), p. 8 (4.3. Ablation Studies and Analysis), p. 8 (Figure/Table caption), p. 7 (4.3. Ablation Studies and Analysis), baselines p. 6 (4.2. Comparison with Existing Methods), p. 7 (4.2. Comparison with Existing Methods), p. 7 (4.3. Ablation Studies and Analysis), p. 8 (4.3. Ablation Studies and Analysis), p. 5 (Figure/Table caption), p. 6 (4.1. Experimental Setting), results p. 7 (4.3. Ablation Studies and Analysis), p. 7 (4.3. Ablation Studies and Analysis), p. 8 (4.3. Ablation Studies and Analysis), p. 8 (4.3. Ablation Studies and Analysis), p. 6 (4.1. Experimental Setting), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
