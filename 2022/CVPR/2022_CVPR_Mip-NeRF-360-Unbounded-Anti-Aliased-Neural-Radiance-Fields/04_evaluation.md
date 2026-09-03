# Evaluation - Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2111.12077; PDF retrieval source: https://arxiv.org/pdf/2111.12077. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (6. Results), p. 8 (6. Results), p. 7 (6. Results), p. 16 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (6. Results)): The mip-NeRF and NeRF++ baselines that use larger MLPs are more competitive, but are ∼3× slower to train than our model and still achieve significantly lower accuracies.

## Evaluation Body Digest

- **p. 7 / 6. Results - extractive body cue:** We evaluate our model on a novel dataset: 9 scenes (5 outdoors and 4 indoors) each containing a complex central object or area and a ...
- **p. 7 / 6. Results - extractive body cue:** In Table 2 we present an ablation study of our model on the bicycle scene in our dataset, the findings of which we summarize here.
- **p. 8 / 6. Results - extractive body cue:** (a) A test-set image from our dataset's stump scene, with (b) our model's rendered image and depth map (median ray termination distance [37]).
- **p. 8 / 6. Results - extractive body cue:** F) Using a small NeRF MLP (256 hidden units instead of our 1024 hidden units) accelerates training but reduces quality, demonstrating the value of a ...
- **p. 8 / 6. Results - extractive body cue:** E) Removing the proposal MLP and training our model using mip-NeRF's approach (applying Lrecon at all coarse scales instead of using our Lprop) worsens both ...
- **p. 7 / 6. Results - extractive body cue:** Our model outperforms Deep Blending and PointBased Neural Rendering across all error metrics.
- **p. 7 / 6. Results - extractive body cue:** See the appendix for renderings from SVS that achieve lower LPIPS scores than our model despite having reduced image quality [22].
- **p. 8 / 6. Results - extractive body cue:** I) Using the parameterization and logarithmic rayspacing presented in DONeRF [34] reduces accuracy.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 6. Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The mip-NeRF and NeRF++ baselines that use larger MLPs are more competitive, but are ∼3× slower to train than our model and still achieve ... | p. 7 (6. Results) |
| 6. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Though mip-NeRF 360 significantly outperforms mip-NeRF and other prior work, it is not perfect. | p. 8 (6. Results) |
| 6. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | See the appendix for renderings from SVS that achieve lower LPIPS scores than our model despite having reduced image quality [22]. | p. 7 (6. Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 13. A rendering from (a) our model, and (b) Stable View Synthesis [41] on a scene from our dataset. The PSNR, SSIM, and ... | p. 16 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 6. The average performance of our model and all NeRF baselines, as well as the top-performing non-NeRF baseline on our own dataset (Stable ... | p. 18 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 6. Results - extractive body cue:** We evaluate our model on a novel dataset: 9 scenes (5 outdoors and 4 indoors) each containing a complex central object or area and a ...
- **p. 7 / 6. Results - extractive body cue:** In Table 2 we present an ablation study of our model on the bicycle scene in our dataset, the findings of which we summarize here.
- **p. 8 / 6. Results - extractive body cue:** (a) A test-set image from our dataset's stump scene, with (b) our model's rendered image and depth map (median ray termination distance [37]).
- **p. 8 / 6. Results - extractive body cue:** F) Using a small NeRF MLP (256 hidden units instead of our 1024 hidden units) accelerates training but reduces quality, demonstrating the value of a ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Though mip-NeRF is able to produce accurate ren- derings of objects, for unbounded scenes it often generates blurry backgrounds and low-detail foregrounds. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. A 2D visualization of our scene parameterization. We define a contract(·) operator (Equation 10, shown as arrows) that maps coordinates onto a ball ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. A comparison of our model's architecture with mip- NeRF's. Mip-NeRF uses one multi-scale MLP that is repeatedly queried (only two repetitions shown here) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. A visualization of the histograms (t, w) emitted from the NeRF MLP (black) and the two sets of histograms (ˆt, ˆw) emit- ted ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Our regularizer suppresses "floaters" (pieces of semi- transparent material floating in space, which are easy to identify in the depth map) and prevents ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. A visualization of ∇Ldist, the gradient of our regular- izer, as a function of s and w on a toy step function. Our ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. A quantitative comparison of our model with several prior works using the dataset presented in this paper. den units for mip-NeRF, 512 hidden ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. (a) A test-set image from our dataset's stump scene, with (b) our model's rendered image and depth map (median ray termination distance [37]). ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our model on a novel dataset: 9 scenes (5 outdoors and 4 indoors) each containing a complex central object or area and ... | embodiment, simulator version and control stack | p. 7 (6. Results), p. 7 (6. Results) |
| Task/environment | In Table 2 we present an ablation study of our model on the bicycle scene in our dataset, the findings of which we summarize ... | reset, timeout, object/scene variation | p. 7 (6. Results), p. 8 (6. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Ambiguity. The content of unbounded scenes may lie), p. 2 (3. Ambiguity. The content of unbounded scenes may lie) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (3. Ambiguity. The content of unbounded scenes may lie), p. 3 (3. Ambiguity. The content of unbounded scenes may lie) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| E) Removing the proposal MLP and training our model using mip-NeRF's approach (applying Lrecon at all coarse scales instead of using our Lprop) worsens ... | definition/direction/unit from same section | p. 8 (6. Results) |
| Our model outperforms Deep Blending and PointBased Neural Rendering across all error metrics. | definition/direction/unit from same section | p. 7 (6. Results) |
| See the appendix for renderings from SVS that achieve lower LPIPS scores than our model despite having reduced image quality [22]. | definition/direction/unit from same section | p. 7 (6. Results) |
| I) Using the parameterization and logarithmic rayspacing presented in DONeRF [34] reduces accuracy. | definition/direction/unit from same section | p. 8 (6. Results) |
| Figure 13. A rendering from (a) our model, and (b) Stable View Synthesis [41] on a scene from our dataset. The PSNR, SSIM, and ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 10. A visualization of the motivation behind Lprop, the loss used to train our proposal MLP to bound the weights emitted by our ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Table 6. The average performance of our model and all NeRF baselines, as well as the top-performing non-NeRF baseline on our own dataset (Stable ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Figure 1. (a) Though mip-NeRF is able to produce accurate ren- derings of objects, for unbounded scenes it often generates blurry backgrounds and low-detail ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Though mip-NeRF 360 significantly outperforms mip-NeRF and other prior work, it is not perfect. | comparison identity and matched condition | p. 8 (6. Results) |
| Compared to prior work (c-e) our renderings more closely resemble the ground-truth and our depths look more plausible (though no ground-truth depth is available). | comparison identity and matched condition | p. 8 (6. Results) |
| Table 6. The average performance of our model and all NeRF baselines, as well as the top-performing non-NeRF baseline on our own dataset (Stable ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |
| Table 1. A quantitative comparison of our model with several prior works using the dataset presented in this paper. den units for mip-NeRF, 512 ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| It also outperforms SVS for PSNR and SSIM, but not LPIPS. | comparison identity and matched condition | p. 7 (6. Results) |
| Table 5. Here we present an expanded version of Table 1 from the main paper, where we evaluate our model and multiple NeRF and ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| An ablation study in which we remove or replace model components to measure their effect. | component/input/data sensitivity | p. 8 (6. Results) |
| We also present a variant of our own model in which we use the latent appearance embedding (4 dimensions) presented in NeRF-W [6, 30] ... | component/input/data sensitivity | p. 7 (6. Results) |
| In Table 2 we present an ablation study of our model on the bicycle scene in our dataset, the findings of which we summarize ... | component/input/data sensitivity | p. 7 (6. Results) |
| Table 6. The average performance of our model and all NeRF baselines, as well as the top-performing non-NeRF baseline on our own dataset (Stable ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| B) Removing Ldist does not substantially affect our metrics but results in "floater" artifacts in scene geometry, as shown in Figure 5. | component/input/data sensitivity | p. 8 (6. Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, and a ... | The mip-NeRF and NeRF++ baselines that use larger MLPs are more competitive, but are ∼3× slower to train than our model and still achieve ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (6. Results), p. 8 (6. Results), p. 7 (6. Results), p. 16 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (6. Results) |
| Primary metric/result | Though mip-NeRF 360 significantly outperforms mip-NeRF and other prior work, it is not perfect. | numeric claim only at cited anchor | p. 8 (6. Results) |

- Numeric sentences retained from the body:
- **p. 7 / 6. Results - extractive body cue:** We evaluate our model on a novel dataset: 9 scenes (5 outdoors and 4 indoors) each containing a complex central object or area and a ...
- **p. 7 / 6. Results - extractive body cue:** We also present a variant of our own model in which we use the latent appearance embedding (4 dimensions) presented in NeRF-W [6, 30] which ...
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** + 1 3 X i w2 i (si+1 -si) (15) In this form, our distortion loss is trivial to compute.
- **p. 6 / 5. Optimization - extractive body cue:** We use a proposal MLP with 4 layers and 256 hidden units and a NeRF MLP with 8 layers and 1024 hidden units, both of ...
- **p. 6 / 5. Optimization - extractive body cue:** We do two stages of evaluation and resampling of the proposal MLP each using 64 samples to produce (ˆs0, ˆw0) and (ˆs1, ˆw1), and then ...
- **p. 6 / 5. Optimization - extractive body cue:** We minimize the following loss: Lrecon(C(t), C∗) + λLdist(s, w) + 1 X k=0 Lprop  s, w,ˆsk, ˆwk , (16) averaged over all rays in ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 12. A visualization of our model with Stable View Synthesis [41] on scenes from the Tanks and Temples dataset [25]. Image quality is ... | p. 15 (Figure/Table caption) |
| body limitation/failure cue | Figure 7. (a) A test-set image from our dataset's stump scene, with (b) our model's rendered image and depth map (median ray termination distance ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Our model has several advantages over SVS and Deep Blending in addition to image quality: those models require external training data while our model ... | p. 7 (6. Results) |
| body limitation/failure cue | D) Removing the proposal MLP and using a single MLP to model both the scene and the proposal weights does not degrade performance but ... | p. 8 (6. Results) |
| body limitation/failure cue | Figure 8. The axis-aligned positional encoding used by mip- NeRF [3] does not capture the covariance of the Gaussian be- ing encoded. Here we ... | p. 11 (Figure/Table caption) |
| body limitation/failure cue | Figure 5. Our regularizer suppresses "floaters" (pieces of semi- transparent material floating in space, which are easy to identify in the depth map) and ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train our model (and all reported NeRF-like baselines) using a slightly modified version of mip-NeRF's learning schedule: 250k iterations of optimization with a ... | p. 7 (5. Optimization) |
| D) Removing the proposal MLP and using a single MLP to model both the scene and the proposal weights does not degrade performance but ... | p. 8 (6. Results) |
| The λ hyperparameter balances our data 6 | p. 6 (5. Optimization) |
| Though Equation 14 is straightforward to define, it is non-trivial to compute. | p. 6 (4. Regularization for Interval-Based Models) |
| We evaluate against NeRF++ [51], which uses two MLPs to separately encode the "inside" and "outside" of each scene. | p. 7 (6. Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / Figure/Table caption - extractive body cue:** Figure 12. A visualization of our model with Stable View Synthesis [41] on scenes from the Tanks and Temples dataset [25]. Image quality is roughly ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. (a) A test-set image from our dataset's stump scene, with (b) our model's rendered image and depth map (median ray termination distance [37]). ...
- **p. 7 / 6. Results - extractive body cue:** Our model has several advantages over SVS and Deep Blending in addition to image quality: those models require external training data while our model does ...
- **p. 8 / 6. Results - extractive body cue:** D) Removing the proposal MLP and using a single MLP to model both the scene and the proposal weights does not degrade performance but increases ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 8. The axis-aligned positional encoding used by mip- NeRF [3] does not capture the covariance of the Gaussian be- ing encoded. Here we plot ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Our regularizer suppresses "floaters" (pieces of semi- transparent material floating in space, which are easy to identify in the depth map) and prevents ...

- **Evidence anchors reviewed:** datasets p. 7 (6. Results), p. 7 (6. Results), p. 8 (6. Results), p. 8 (6. Results), metrics p. 8 (6. Results), p. 7 (6. Results), p. 7 (6. Results), p. 8 (6. Results), p. 16 (Figure/Table caption), p. 13 (Figure/Table caption), baselines p. 8 (6. Results), p. 8 (6. Results), p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (6. Results), p. 17 (Figure/Table caption), results p. 7 (6. Results), p. 8 (6. Results), p. 7 (6. Results), p. 16 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (6. Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
