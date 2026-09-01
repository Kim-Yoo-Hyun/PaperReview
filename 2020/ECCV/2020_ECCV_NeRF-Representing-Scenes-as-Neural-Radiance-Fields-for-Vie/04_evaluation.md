# Evaluation - NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2003.08934; PDF retrieval source: https://arxiv.org/pdf/2003.08934. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 9 (6 Results), p. 9 (6 Results), p. 10 (6 Results), p. 13 (6.3 Discussion), p. 14 (Figure/Table caption)): Table 1: Our method quantitatively outperforms prior work on datasets of both synthetic and real images. We report PSNR/SSIM (higher is better) and LPIPS [50] (lower is better). The DeepVoxels ...

## Evaluation Body Digest

- **p. 10 / 6 Results - extractive PDF cue:** This dataset consists of 8 scenes captured with a handheld cellphone (5 taken from the LLFF paper and 3 that we capture), captured with 20 ...
- **p. 10 / 6 Results - extractive PDF cue:** The real dataset consists of handheld forward-facing captures of 8 realworld scenes (NV cannot be evaluated on this data because it only reconstructs objects inside ...
- **p. 11 / 6 Results - extractive PDF cue:** 5: Comparisons on test-set views for scenes from our new synthetic dataset generated with a physically-based renderer.
- **p. 18 / A Additional Implementation Details - extractive PDF cue:** A final layer (with a sigmoid activation) outputs the emitted RGB radiance at position x, as viewed by a ray with direction d. dataset requires ...
- **p. 9 / 6 Results - extractive PDF cue:** The DeepVoxels [41] dataset contains four Lambertian objects with simple geometry.
- **p. 9 / 6 Results - extractive PDF cue:** We additionally generate our own dataset containing pathtraced images of eight objects that exhibit complicated geometry and realistic non-Lambertian materials.
- **p. 13 / 6.3 Discussion - extractive PDF cue:** Our method requires only 5 MB for the network weights (a relative compression of 3000× compared to LLFF), which is even less memory than the ...
- **p. 11 / 6 Results - extractive PDF cue:** NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis 11 Ship Lego Microphone Materials Ground Truth NeRF (ours) LLFF [28] SRN [42] NV [24] ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 6 Results (p. 9); A Additional Implementation Details (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1: Our method quantitatively outperforms prior work on datasets of both synthetic and real images. We report PSNR/SSIM (higher is better) and LPIPS ... | p. 10 (Figure/Table caption) |
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 8 and 6) show that our method outperforms prior work, and provide extensive ablation studies to validate our design choices (Table 2). | p. 9 (6 Results) |
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We urge the reader to view our supplementary video to better appreciate our method's significant improvement over baseline methods when rendering smooth paths of ... | p. 9 (6 Results) |
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Though LLFF achieves slightly better LPIPS, we urge readers to view our supplementary video where our method achieves better multiview consistency and produces fewer ... | p. 10 (6 Results) |
| 6.3 Discussion | EMPIRICAL / SOURCE-REPORTED EVALUATION | We thoroughly outperform both baselines that also optimize a separate network per scene (NV and SRN) in all scenarios. | p. 13 (6.3 Discussion) |

## Dataset / Benchmark Role

- **p. 10 / 6 Results - extractive PDF cue:** This dataset consists of 8 scenes captured with a handheld cellphone (5 taken from the LLFF paper and 3 that we capture), captured with 20 ...
- **p. 10 / 6 Results - extractive PDF cue:** The real dataset consists of handheld forward-facing captures of 8 realworld scenes (NV cannot be evaluated on this data because it only reconstructs objects inside ...
- **p. 11 / 6 Results - extractive PDF cue:** 5: Comparisons on test-set views for scenes from our new synthetic dataset generated with a physically-based renderer.
- **p. 18 / A Additional Implementation Details - extractive PDF cue:** A final layer (with a sigmoid activation) outputs the emitted RGB radiance at position x, as viewed by a ray with direction d. dataset requires ...
- **p. 9 / 6 Results - extractive PDF cue:** The DeepVoxels [41] dataset contains four Lambertian objects with simple geometry.
- **p. 9 / 6 Results - extractive PDF cue:** We additionally generate our own dataset containing pathtraced images of eight objects that exhibit complicated geometry and realistic non-Lambertian materials.
- **p. 13 / 6.3 Discussion - extractive PDF cue:** Our method requires only 5 MB for the network weights (a relative compression of 3000× compared to LLFF), which is even less memory than the ...
- **p. 11 / 6 Results - extractive PDF cue:** NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis 11 Ship Lego Microphone Materials Ground Truth NeRF (ours) LLFF [28] SRN [42] NV [24] ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: We present a method that optimizes a continuous 5D neural radiance field representation (volume density and view-dependent color at any continuous location) of ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: An overview of our neural radiance field scene representation and differ- entiable rendering procedure. We synthesize images by sampling 5D coordinates (location and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: A visualization of view-dependent emitted radiance. Our neural radiance field representation outputs RGB color as a 5D function of both spatial position x ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 4: Here we visualize how our full model benefits from representing view- dependent emitted radiance and from passing our input coordinates through a high-frequency ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 1: Our method quantitatively outperforms prior work on datasets of both synthetic and real images. We report PSNR/SSIM (higher is better) and LPIPS [50] ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 5: Comparisons on test-set views for scenes from our new synthetic dataset generated with a physically-based renderer. Our method is able to recover fine ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 6: Comparisons on test-set views of real world scenes. LLFF is specifically designed for this use case (forward-facing captures of real scenes). Our method ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 2: An ablation study of our model. Metrics are averaged over the 8 scenes from our realistic synthetic dataset. See Sec. 6.4 for detailed ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This dataset consists of 8 scenes captured with a handheld cellphone (5 taken from the LLFF paper and 3 that we capture), captured with ... | embodiment, simulator version and control stack | p. 10 (6 Results), p. 10 (6 Results) |
| Task/environment | The real dataset consists of handheld forward-facing captures of 8 realworld scenes (NV cannot be evaluated on this data because it only reconstructs objects ... | reset, timeout, object/scene variation | p. 10 (6 Results), p. 11 (6 Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 18 (A Additional Implementation Details) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 Introduction), p. 14 (9) Complete Model) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We additionally generate our own dataset containing pathtraced images of eight objects that exhibit complicated geometry and realistic non-Lambertian materials. | definition/direction/unit from same section | p. 9 (6 Results) |
| Neural Volumes (NV) [24] synthesizes novel views of objects that lie entirely within a bounded volume in front of a distinct background (which must ... | definition/direction/unit from same section | p. 10 (6 Results) |
| All methods use the same set of input views to train a separate network for each scene except Local Light Field Fusion [28], which ... | definition/direction/unit from same section | p. 10 (6 Results) |
| 5: Comparisons on test-set views for scenes from our new synthetic dataset generated with a physically-based renderer. | definition/direction/unit from same section | p. 11 (6 Results) |
| Rows 5-6 show how our performance decreases as the number of input images is reduced. | definition/direction/unit from same section | p. 13 (6.3 Discussion) |
| We thoroughly outperform both baselines that also optimize a separate network per scene (NV and SRN) in all scenarios. | definition/direction/unit from same section | p. 13 (6.3 Discussion) |
| Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to the output ... | definition/direction/unit from same section | p. 17 (A Additional Implementation Details) |
| Table 2: An ablation study of our model. Metrics are averaged over the 8 scenes from our realistic synthetic dataset. See Sec. 6.4 for ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We thoroughly outperform both baselines that also optimize a separate network per scene (NV and SRN) in all scenarios. | comparison identity and matched condition | p. 13 (6.3 Discussion) |
| 8 and 6) show that our method outperforms prior work, and provide extensive ablation studies to validate our design choices (Table 2). | comparison identity and matched condition | p. 9 (6 Results) |
| Diffuse Synthetic 360◦[41] Realistic Synthetic 360◦ Real Forward-Facing [28] Method PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ SRN [42] 33.20 0.963 0.073 ... | comparison identity and matched condition | p. 10 (6 Results) |
| We urge the reader to view our supplementary video to better appreciate our method's significant improvement over baseline methods when rendering smooth paths of ... | comparison identity and matched condition | p. 9 (6 Results) |
| Though LLFF achieves slightly better LPIPS, we urge readers to view our supplementary video where our method achieves better multiview consistency and produces fewer ... | comparison identity and matched condition | p. 10 (6 Results) |
| All compared single scene methods take at least 12 hours to train per scene. | comparison identity and matched condition | p. 13 (6.3 Discussion) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In rows 2-4 we remove these three components one at a time from the full model, observing that positional encoding (row 2) and view-dependence ... | component/input/data sensitivity | p. 13 (6.3 Discussion) |
| 8 and 6) show that our method outperforms prior work, and provide extensive ablation studies to validate our design choices (Table 2). | component/input/data sensitivity | p. 9 (6 Results) |
| Neural Volumes (NV) [24] synthesizes novel views of objects that lie entirely within a bounded volume in front of a distinct background (which must ... | component/input/data sensitivity | p. 10 (6 Results) |
| 6.4 Ablation studies We validate our algorithm's design choices and parameters with an extensive ablation study in Table 2. | component/input/data sensitivity | p. 13 (6.3 Discussion) |
| Table 2: An ablation study of our model. Metrics are averaged over the 8 scenes from our realistic synthetic dataset. See Sec. 6.4 for ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 6: Per-scene quantitative results from our ablation study. The scenes used here are the same as in Table 4. | component/input/data sensitivity | p. 25 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, and we ... | Table 1: Our method quantitatively outperforms prior work on datasets of both synthetic and real images. We report PSNR/SSIM (higher is better) and LPIPS ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 9 (6 Results), p. 9 (6 Results), p. 10 (6 Results), p. 13 (6.3 Discussion), p. 14 (Figure/Table caption) |
| Primary metric/result | 8 and 6) show that our method outperforms prior work, and provide extensive ablation studies to validate our design choices (Table 2). | numeric claim only at cited anchor | p. 9 (6 Results) |

- Numeric sentences retained from the body:
- **p. 10 / 6 Results - extractive PDF cue:** This dataset consists of 8 scenes captured with a handheld cellphone (5 taken from the LLFF paper and 3 that we capture), captured with 20 ...
- **p. 10 / 6 Results - extractive PDF cue:** It optimizes a deep 3D convolutional network to predict a discretized RGBα voxel grid with 1283 samples as well as a 3D warp grid with ...
- **p. 13 / 6.3 Discussion - extractive PDF cue:** All compared single scene methods take at least 12 hours to train per scene.
- **p. 17 / A Additional Implementation Details - extractive PDF cue:** Rendering Details To render new views at test time, we sample 64 points per ray through the coarse network and 64 + 128 = 192 ...
- **p. 14 / 9) Complete Model - extractive PDF cue:** Metrics are averaged over the 8 scenes from our realistic synthetic dataset.
- **p. 17 / A Additional Implementation Details - extractive PDF cue:** Rendering Details To render new views at test time, we sample 64 points per ray through the coarse network and 64 + 128 = 192 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Another direction for future work is interpretability: sampled representations such as voxel grids and meshes admit reasoning about the expected quality of rendered views ... | p. 14 (7 Conclusion) |
| body limitation/failure cue | Neural Volumes cannot capture the details on the Microphone's grille or Lego's gears, and it completely fails to recover the geometry of Ship's rigging. | p. 11 (6 Results) |
| body limitation/failure cue | LLFF specifically provides a "sampling guideline" to not exceed 64 pixels of disparity between input views, so it frequently fails to estimate correct geometry ... | p. 13 (6.3 Discussion) |
| body limitation/failure cue | The real dataset consists of handheld forward-facing captures of 8 realworld scenes (NV cannot be evaluated on this data because it only reconstructs objects ... | p. 10 (6 Results) |
| body limitation/failure cue | Table 2: An ablation study of our model. Metrics are averaged over the 8 scenes from our realistic synthetic dataset. See Sec. 6.4 for ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Table 3: Per-scene quantitative results from the DeepVoxels [41] dataset. The "scenes" in this dataset are all diffuse objects with simple geometry, rendered from ... | p. 23 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The feature vector from the final step is decoded into a single color for that point on the surface. | p. 10 (6 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 7 Conclusion - extractive PDF cue:** Another direction for future work is interpretability: sampled representations such as voxel grids and meshes admit reasoning about the expected quality of rendered views and ...
- **p. 11 / 6 Results - extractive PDF cue:** Neural Volumes cannot capture the details on the Microphone's grille or Lego's gears, and it completely fails to recover the geometry of Ship's rigging.
- **p. 13 / 6.3 Discussion - extractive PDF cue:** LLFF specifically provides a "sampling guideline" to not exceed 64 pixels of disparity between input views, so it frequently fails to estimate correct geometry in ...
- **p. 10 / 6 Results - extractive PDF cue:** The real dataset consists of handheld forward-facing captures of 8 realworld scenes (NV cannot be evaluated on this data because it only reconstructs objects inside ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 2: An ablation study of our model. Metrics are averaged over the 8 scenes from our realistic synthetic dataset. See Sec. 6.4 for detailed ...
- **p. 23 / Figure/Table caption - extractive PDF cue:** Table 3: Per-scene quantitative results from the DeepVoxels [41] dataset. The "scenes" in this dataset are all diffuse objects with simple geometry, rendered from texture-mapped ...

- **PDF anchors reviewed:** datasets p. 10 (6 Results), p. 10 (6 Results), p. 11 (6 Results), p. 18 (A Additional Implementation Details), p. 9 (6 Results), p. 9 (6 Results), metrics p. 9 (6 Results), p. 10 (6 Results), p. 10 (6 Results), p. 11 (6 Results), p. 13 (6.3 Discussion), p. 13 (6.3 Discussion), baselines p. 13 (6.3 Discussion), p. 9 (6 Results), p. 10 (6 Results), p. 9 (6 Results), p. 10 (6 Results), p. 13 (6.3 Discussion), results p. 10 (Figure/Table caption), p. 9 (6 Results), p. 9 (6 Results), p. 10 (6 Results), p. 13 (6.3 Discussion), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
