# Evaluation - Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.13415; PDF retrieval source: https://arxiv.org/pdf/2103.13415. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4. Results), p. 7 (4. Results), p. 7 (4. Results), p. 8 (4. Results), p. 4 (Figure/Table caption), p. 14 (Figure/Table caption)): [30], mip-NeRF significantly outperforms NeRF and our improved version of NeRF, particularly on small or thin objects such as the holes of the LEGO truck (top) and the ropes of ...

## Evaluation Body Digest

- **p. 7 / 4. Results - extractive body cue:** 0.709 0.910 0.931 0.663 0.863 0.959 0.971 0.881 0.940 0.979 0.989 0.978 0.448 0.562 0.696 0.906 0.525 0.633 0.794 0.918 0.785 0.837 0.861 0.975 Ground-Truth ...
- **p. 6 / 4. Results - extractive body cue:** As a result, this Blender task is significantly easier than most real-world datasets, where cameras may be more close or more distant from the subject ...
- **p. 6 / 4. Results - extractive body cue:** We constructed our multiscale Blender benchmark because the original Blender dataset used by NeRF has a subtle but critical weakness: all cameras have the same ...
- **p. 8 / 4. Results - extractive body cue:** This strategy is not viable in most real-world datasets, as it is usually not possible to known a-priori which images correspond to which scales of ...
- **p. 7 / 4. Results - extractive body cue:** 32.610 34.333 35.497 35.638 0.9577 0.9703 0.9787 0.9834 0.0470 0.0259 0.0167 0.0120 0.0114 2.82 ± 0.03 612K Mip-NeRF w/o Single MLP 32.401 34.131 35.462 35.967 ...
- **p. 8 / 4. Results - extractive body cue:** Because our multiscale dataset consists of downsampled PSNR ↑ Avg.
- **p. 7 / 4. Results - extractive body cue:** Mip-NeRF reduces average error by 60% on this task and outperforms NeRF by a large margin on all metrics and all scales. "Centering" pixels improves ...
- **p. 6 / 4. Results - extractive body cue:** We report the three error metrics used by NeRF: PSNR, SSIM [45], and LPIPS [52].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | [30], mip-NeRF significantly outperforms NeRF and our improved version of NeRF, particularly on small or thin objects such as the holes of the LEGO ... | p. 8 (4. Results) |
| 4. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Mip-NeRF reduces average error by 60% on this task and outperforms NeRF by a large margin on all metrics and all scales. "Centering" pixels ... | p. 7 (4. Results) |
| 4. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Mip-NeRF outperforms NeRF and its improved version by a significant margin, both visually and quantitatively. | p. 7 (4. Results) |
| 4. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Adding supersampling to mip-NeRF improves its accuracy slightly. | p. 8 (4. Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: NeRF works by extracting point-sampled posi- tional encoding features (shown here as dots) along each pixel's ray. Those point-sampled features ignore the ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4. Results - extractive body cue:** 0.709 0.910 0.931 0.663 0.863 0.959 0.971 0.881 0.940 0.979 0.989 0.978 0.448 0.562 0.696 0.906 0.525 0.633 0.794 0.918 0.785 0.837 0.861 0.975 Ground-Truth ...
- **p. 6 / 4. Results - extractive body cue:** As a result, this Blender task is significantly easier than most real-world datasets, where cameras may be more close or more distant from the subject ...
- **p. 6 / 4. Results - extractive body cue:** We constructed our multiscale Blender benchmark because the original Blender dataset used by NeRF has a subtle but critical weakness: all cameras have the same ...
- **p. 8 / 4. Results - extractive body cue:** This strategy is not viable in most real-world datasets, as it is usually not possible to known a-priori which images correspond to which scales of ...
- **p. 7 / 4. Results - extractive body cue:** 32.610 34.333 35.497 35.638 0.9577 0.9703 0.9787 0.9834 0.0470 0.0259 0.0167 0.0120 0.0114 2.82 ± 0.03 612K Mip-NeRF w/o Single MLP 32.401 34.131 35.462 35.967 ...
- **p. 8 / 4. Results - extractive body cue:** Because our multiscale dataset consists of downsampled PSNR ↑ Avg.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: NeRF (a) samples points x along rays that are traced from the camera center of projection through each pixel, then encodes those points ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: (a, top) A NeRF trained on full-resolution im- ages is capable of producing photorealistic renderings at new view locations, but only at the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: NeRF works by extracting point-sampled posi- tional encoding features (shown here as dots) along each pixel's ray. Those point-sampled features ignore the shape ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Toy 1D visualizations of the positional encoding (PE) used by NeRF (left) and our integrated positional en- coding (IPE) (right). Because NeRF samples ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Visualizations of the output of mip-NeRF compared to the ground truth, NeRF, and an improved version of NeRF on test set images from ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: A quantitative comparison of mip-NeRF and its ablations against NeRF and several NeRF variants on the test set of our multiscale Blender dataset. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Even on the less challenging single-scale Blender dataset of Mildenhall et al. [30], mip-NeRF significantly outperforms NeRF and our improved version of NeRF, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: A comparison of mip-NeRF and its ablations against several baseline algorithms and variants of NeRF on the single-scale Blender dataset of Mildenhall et ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 0.709 0.910 0.931 0.663 0.863 0.959 0.971 0.881 0.940 0.979 0.989 0.978 0.448 0.562 0.696 0.906 0.525 0.633 0.794 0.918 0.785 0.837 0.861 0.975 ... | embodiment, simulator version and control stack | p. 7 (4. Results), p. 6 (4. Results) |
| Task/environment | As a result, this Blender task is significantly easier than most real-world datasets, where cameras may be more close or more distant from the ... | reset, timeout, object/scene variation | p. 6 (4. Results), p. 6 (4. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3.2. Architecture), p. 6 (3.2. Architecture) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Mip-NeRF reduces average error by 60% on this task and outperforms NeRF by a large margin on all metrics and all scales. "Centering" pixels ... | definition/direction/unit from same section | p. 7 (4. Results) |
| We report the three error metrics used by NeRF: PSNR, SSIM [45], and LPIPS [52]. | definition/direction/unit from same section | p. 6 (4. Results) |
| To enable easier comparison, we also present an "average" error metric that summarizes all three metrics: the geometric mean of MSE = 10-PSNR/10, √ ... | definition/direction/unit from same section | p. 6 (4. Results) |
| The average error metric for this task uses the arithmetic mean of each error metric across all four scales. | definition/direction/unit from same section | p. 7 (4. Results) |
| Adding supersampling to mip-NeRF improves its accuracy slightly. | definition/direction/unit from same section | p. 8 (4. Results) |
| Mip-NeRF nearly matches the accuracy of "SS NeRF" while being 22× faster. | definition/direction/unit from same section | p. 8 (4. Results) |
| Figure 1: NeRF (a) samples points x along rays that are traced from the camera center of projection through each pixel, then encodes those ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2: (a, top) A NeRF trained on full-resolution im- ages is capable of producing photorealistic renderings at new view locations, but only at ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2: A comparison of mip-NeRF and its ablations against several baseline algorithms and variants of NeRF on the single-scale Blender dataset of Mildenhall ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 5: Visualizations of the output of mip-NeRF compared to the ground truth, NeRF, and an improved version of NeRF on test set images ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 4: Here we evaluate mip-NeRF against an extension of NeRF in which brute-force supersampling with jittered rays is used during training and evaluation, ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| We evaluate against the baselines used by NeRF, NSVF [24], and the same variants and ablations that were used previously (excluding "Area Loss", which ... | comparison identity and matched condition | p. 8 (4. Results) |
| Mip-NeRF reduces average error by 60% on this task and outperforms NeRF by a large margin on all metrics and all scales. "Centering" pixels ... | comparison identity and matched condition | p. 7 (4. Results) |
| Figure 10: Additional visualizations of the output renderings from mip-NeRF compared to the ground truth, NeRF, and an improved version of NeRF presented in ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also evaluate against several ablations of mip-NeRF: "w/o Misc" removes those small changes, "w/o Single MLP" uses NeRF's two-MLP training scheme from Equation ... | component/input/data sensitivity | p. 7 (4. Results) |
| Table 1: A quantitative comparison of mip-NeRF and its ablations against NeRF and several NeRF variants on the test set of our multiscale Blender ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We evaluate against the baselines used by NeRF, NSVF [24], and the same variants and ablations that were used previously (excluding "Area Loss", which ... | component/input/data sensitivity | p. 8 (4. Results) |
| 33.04 0.960 0.043 0.0162 2.89 ± 0.01 612K Mip-NeRF w/o Single MLP 32.71 0.959 0.044 0.0168 3.63 ± 0.02 1,191K Mip-NeRF w/o IPE 32.48 ... | component/input/data sensitivity | p. 8 (4. Results) |
| We additionally report runtimes (median and median absolute deviation of wall time) as well as the number of network parameters for each variant of ... | component/input/data sensitivity | p. 6 (4. Results) |
| We evaluate mip-NeRF on the Blender dataset presented in the original NeRF paper [30] and also on a simple multiscale variant of that dataset ... | component/input/data sensitivity | p. 6 (4. Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To encode a 3D position and its surrounding Gaussian region, we propose a new feature representation: an integrated positional encoding (IPE). | [30], mip-NeRF significantly outperforms NeRF and our improved version of NeRF, particularly on small or thin objects such as the holes of the LEGO ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4. Results), p. 7 (4. Results), p. 7 (4. Results), p. 8 (4. Results), p. 4 (Figure/Table caption), p. 14 (Figure/Table caption) |
| Primary metric/result | Mip-NeRF reduces average error by 60% on this task and outperforms NeRF by a large margin on all metrics and all scales. "Centering" pixels ... | numeric claim only at cited anchor | p. 7 (4. Results) |

- Numeric sentences retained from the body:
- **p. 7 / 4. Results - extractive body cue:** 1/8 Res Avg. ↓ Time (hours) # Params NeRF (Jax Impl.) [11, 30] 31.196 30.647 26.252 22.533 0.9498 0.9560 0.9299 0.8709 0.0546 0.0342 0.0428 0.0750 ...
- **p. 7 / 4. Results - extractive body cue:** 32.610 34.333 35.497 35.638 0.9577 0.9703 0.9787 0.9834 0.0470 0.0259 0.0167 0.0120 0.0114 2.82 ± 0.03 612K Mip-NeRF w/o Single MLP 32.401 34.131 35.462 35.967 ...
- **p. 8 / 4. Results - extractive body cue:** PSNR ↑ SSIM ↑ LPIPS ↓ Avg. ↓ Time (hours) # Params SRN [39] 22.26 0.846 0.170 0.0735 - - Neural Volumes [25] 26.05 0.893 ...
- **p. 8 / 4. Results - extractive body cue:** 33.04 0.960 0.043 0.0162 2.89 ± 0.01 612K Mip-NeRF w/o Single MLP 32.71 0.959 0.044 0.0168 3.63 ± 0.02 1,191K Mip-NeRF w/o IPE 32.48 0.958 ...
- **p. 6 / 3.2. Architecture - extractive body cue:** Unlike NeRF, in which the fine MLP is given the sorted union of 64 coarse samples and 128 fine samples, in mip-NeRF we simply sample ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The limitation of this dataset is complemented by the limitations of NeRF: despite NeRF's tendency to produce aliased renderings, it is able to produce ... | p. 6 (4. Results) |
| body limitation/failure cue | Removing IPE features causes mip-NeRF's performance to degrade to the performance of "Centered" NeRF, thereby demonstrating that cone-casting and IPE features are the primary ... | p. 7 (4. Results) |
| body limitation/failure cue | This baseline has an unfair advantage: we manually remove the low-resolution images in the multiscale dataset, which would otherwise degrade NeRF's performance as previously ... | p. 8 (4. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We follow NeRF's training procedure: 1 million iterations of Adam [19] with a batch size of 4096 and a learning rate that is annealed ... | p. 6 (3.2. Architecture) |
| Training times taken from prior work (when available) are indicated in gray, as they are not directly comparable. put due to its changing tensor ... | p. 8 (4. Results) |
| We report times for rendering the test set, normalized to seconds-permegapixel (training times are the same as Tables 1 and 2). versions of full-resolution ... | p. 8 (4. Results) |
| (6) However, it is unclear how such a feature could be computed efficiently, as the integral in the numerator has no | p. 4 (3.1. Cone Tracing and Positional Encoding) |
| There are many viable approaches for this (see the supplement for further discussion) but the simplest and most effective solution we found was to ... | p. 4 (3.1. Cone Tracing and Positional Encoding) |
| (16) If these diagonals are computed directly, IPE features are roughly as expensive as PE features to construct. | p. 5 (3.1. Cone Tracing and Positional Encoding) |
| To approximate a conical frustum with a multivariate Gaussian, we must compute the mean and covariance of F(x, ·). | p. 5 (3.1. Cone Tracing and Positional Encoding) |
| Because NeRF samples points along each ray and encodes all frequencies equally, the highfrequency PE features are aliased, which results in rendering artifacts. | p. 6 (3.2. Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4. Results - extractive body cue:** The limitation of this dataset is complemented by the limitations of NeRF: despite NeRF's tendency to produce aliased renderings, it is able to produce excellent ...
- **p. 7 / 4. Results - extractive body cue:** Removing IPE features causes mip-NeRF's performance to degrade to the performance of "Centered" NeRF, thereby demonstrating that cone-casting and IPE features are the primary factors ...
- **p. 8 / 4. Results - extractive body cue:** This baseline has an unfair advantage: we manually remove the low-resolution images in the multiscale dataset, which would otherwise degrade NeRF's performance as previously demonstrated.

- **Evidence anchors reviewed:** datasets p. 7 (4. Results), p. 6 (4. Results), p. 6 (4. Results), p. 8 (4. Results), p. 7 (4. Results), p. 8 (4. Results), metrics p. 7 (4. Results), p. 6 (4. Results), p. 6 (4. Results), p. 7 (4. Results), p. 8 (4. Results), p. 8 (4. Results), baselines p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 8 (4. Results), p. 7 (4. Results), p. 18 (Figure/Table caption), results p. 8 (4. Results), p. 7 (4. Results), p. 7 (4. Results), p. 8 (4. Results), p. 4 (Figure/Table caption), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
