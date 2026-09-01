# Evaluation - 3D Gaussian Splatting for Real-Time Radiance Field Rendering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2308.04079; PDF retrieval source: https://arxiv.org/pdf/2308.04079. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption)): Fig. 1. Our method achieves real-time rendering of radiance fields with quality that equals the previous method with the best quality [Barron et al. 2022], while only requiring optimization times ...

## Evaluation Body Digest

- **p. 1 / Front matter - extractive body cue:** For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates.
- **p. 1 / Front matter - extractive body cue:** We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Note that for the NeRF-synthetic dataset, our method achieves high quality even with random initialization.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The optimization procedure produces a reasonably compact, unstructured, and precise representation of the scene (1-5 million Gaussians for all scenes tested).
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. PSNR scores for Synthetic NeRF, we start with 100K randomly initialized points. Competing metrics extracted from respective papers. Mic Chair Ship Materials Lego ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3. PSNR Score for ablation runs. For this experiment, we manually downsampled high-resolution versions of each scene's input images to the established rendering resolution ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 7. SSIM scores for Tanks&Temples and Deep Blending scenes. Truck Train Dr Johnson Playroom Plenoxels 0.774 0.663
- **p. 14 / Figure/Table caption - extractive body cue:** Table 4. SSIM scores for Mip-NeRF360 scenes. † copied from original paper. bicycle flowers garden stump treehill room counter

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 1. Our method achieves real-time rendering of radiance fields with quality that equals the previous method with the best quality [Barron et al. ... | p. 1 (Figure/Table caption) |
| 1 INTRODUCTION | SYSTEM / EVALUATION SCOPE UNRESOLVED | 2022], we achieve high-quality results with only SfM points as input. | p. 2 (1 INTRODUCTION) |
| 1 INTRODUCTION | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our results on previously published datasets show that we can optimize our 3D Gaussians from multi-view captures and achieve equal or better quality than ... | p. 2 (1 INTRODUCTION) |
| 1 INTRODUCTION | SYSTEM / EVALUATION SCOPE UNRESOLVED | Recent methods achieve fast training [Fridovich-Keil ACM Trans. | p. 1 (1 INTRODUCTION) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 3. We visualize the 3D Gaussians after optimization by shrinking them 60% (far right). This clearly shows the anisotropic shapes of the 3D ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 1 / Front matter - extractive body cue:** For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates.
- **p. 1 / Front matter - extractive body cue:** We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Note that for the NeRF-synthetic dataset, our method achieves high quality even with random initialization.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The optimization procedure produces a reasonably compact, unstructured, and precise representation of the scene (1-5 million Gaussians for all scenes tested).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Our method achieves real-time rendering of radiance fields with quality that equals the previous method with the best quality [Barron et al. 2022], ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2. Optimization starts with the sparse SfM point cloud and creates a set of 3D Gaussians. We then optimize and adaptively control the density ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. We visualize the 3D Gaussians after optimization by shrinking them 60% (far right). This clearly shows the anisotropic shapes of the 3D Gaussians ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Our adaptive Gaussian densification scheme. Top row (under- reconstruction): When small-scale geometry (black outline) is insufficiently covered, we clone the respective Gaussian. Bottom ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. We show comparisons of ours to previous methods and the corresponding ground truth images from held-out test views. The scenes are, from the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. Quantitative evaluation of our method compared to previous work, computed over three datasets. Results marked with dagger † have been directly adopted from ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. For some scenes (above) we can see that even at 7K iterations (∼5min for this scene), our method has captured the train quite ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. PSNR scores for Synthetic NeRF, we start with 100K randomly initialized points. Competing metrics extracted from respective papers. Mic Chair Ship Materials Lego ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates. | embodiment, simulator version and control stack | p. 1 (Front matter), p. 1 (Front matter) |
| Task/environment | We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets. | reset, timeout, object/scene variation | p. 1 (Front matter), p. 2 (1 INTRODUCTION) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2. PSNR scores for Synthetic NeRF, we start with 100K randomly initialized points. Competing metrics extracted from respective papers. Mic Chair Ship Materials ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 3. PSNR Score for ablation runs. For this experiment, we manually downsampled high-resolution versions of each scene's input images to the established rendering ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Table 7. SSIM scores for Tanks&Temples and Deep Blending scenes. Truck Train Dr Johnson Playroom Plenoxels 0.774 0.663 | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Table 4. SSIM scores for Mip-NeRF360 scenes. † copied from original paper. bicycle flowers garden stump treehill room counter | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| First, starting from sparse points produced during camera calibration, we represent the scene with 3D Gaussians that preserve desirable properties of continuous volumetric radiance ... | definition/direction/unit from same section | p. 1 (Front matter) |
| We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets. | definition/direction/unit from same section | p. 1 (Front matter) |
| We start with the same input as previous NeRF-like methods, i.e., cameras calibrated with Structure-from-Motion (SfM) [Snavely et al. | definition/direction/unit from same section | p. 2 (1 INTRODUCTION) |
| However, thanks to our 3D Gaussian representation, we can perform anisotropic splatting that respects visibility ordering - thanks to sorting and 𝛼blending - and ... | definition/direction/unit from same section | p. 2 (1 INTRODUCTION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and ... | comparison identity and matched condition | p. 1 (1 INTRODUCTION) |
| Fig. 2. Optimization starts with the sparse SfM point cloud and creates a set of 3D Gaussians. We then optimize and adaptively control the ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| 2022], we achieve similar quality to theirs; while this is the maximum quality they reach, by training for 51min we achieve state-of-the-art quality, even ... | comparison identity and matched condition | p. 1 (Front matter) |
| Table 1. Quantitative evaluation of our method compared to previous work, computed over three datasets. Results marked with dagger † have been directly adopted ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Fig. 10. We train scenes with Gaussian anisotropy disabled and enabled. The use of anisotropic volumetric splats enables modelling of fine structures and has ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |
| 2022], but struggle to achieve the visual quality obtained by the current SOTA NeRF methods, i.e., Mip-NeRF360 [Barron et al. | comparison identity and matched condition | p. 2 (1 INTRODUCTION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 9. If we limit the number of points that receive gradients, the effect on visual quality is significant. Left: limit of 10 Gaussians ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| The second component of our method is optimization of the properties of the 3D Gaussians - 3D position, opacity 𝛼, anisotropic covariance, and spherical ... | component/input/data sensitivity | p. 2 (1 INTRODUCTION) |
| Fig. 4. Our adaptive Gaussian densification scheme. Top row (under- reconstruction): When small-scale geometry (black outline) is insufficiently covered, we clone the respective Gaussian. ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 3. PSNR Score for ablation runs. For this experiment, we manually downsampled high-resolution versions of each scene's input images to the established rendering ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Fig. 8. Ablation of densification strategy for the two cases "clone" and "split" (Sec. 5). Unlimited depth complexity of splats with gradients. We evaluate ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Our solution builds on three main components. | component/input/data sensitivity | p. 2 (1 INTRODUCTION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, we provide the following contributions: • The introduction of anisotropic 3D Gaussians as a high-quality, unstructured representation of radiance fields. • An ... | Fig. 1. Our method achieves real-time rendering of radiance fields with quality that equals the previous method with the best quality [Barron et al. ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | 2022], we achieve high-quality results with only SfM points as input. | numeric claim only at cited anchor | p. 2 (1 INTRODUCTION) |

- Numeric sentences retained from the body:
- **p. 1 / Front matter - extractive body cue:** 3D Gaussian Splatting for Real-Time Radiance Field Rendering BERNHARD KERBL∗, Inria, Université Côte d'Azur, France GEORGIOS KOPANAS∗, Inria, Université Côte d'Azur, France THOMAS LEIMKÜHLER, Max-Planck-Institut ...
- **p. 1 / Front matter - extractive body cue:** We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (≥30 fps) ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2022], which requires up to 48 hours of training time.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The fast - but lower-quality - radiance field methods can achieve interactive rendering times depending on the scene (10-15 frames per second), but fall short ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2022], which requires up to 48 hours of training time.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The fast - but lower-quality - radiance field methods can achieve interactive rendering times depending on the scene (10-15 frames per second), but fall short ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We observe that our method performs relatively well, avoiding complete failure even without the SfM points. | p. 9 (2 RELATED WORK) |
| body limitation/failure cue | Fig. 9. If we limit the number of points that receive gradients, the effect on visual quality is significant. Left: limit of 10 Gaussians ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Comparison of failure artifacts: Mip-NeRF360 has "floaters" and grainy appearance (left, foreground), while our method produces coarse, anisoptropic Gaussians resulting in low-detail visuals (right, ... | p. 11 (2 RELATED WORK) |
| body limitation/failure cue | The fast - but lower-quality - radiance field methods can achieve interactive rendering times depending on the scene (10-15 frames per second), but fall ... | p. 2 (1 INTRODUCTION) |
| body limitation/failure cue | Also in areas not well covered from training views, the random initialization method appears to have more floaters that cannot be removed by optimization. | p. 9 (2 RELATED WORK) |
| body limitation/failure cue | 7.4 Limitations Our method is not without limitations. | p. 10 (2 RELATED WORK) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Note that for comparable training times to InstantNGP [Müller et al. | p. 1 (Front matter) |
| We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (≥30 ... | p. 1 (Front matter) |
| 2022], which requires up to 48 hours of training time. | p. 2 (1 INTRODUCTION) |
| The third and final element of our method is our real-time rendering solution that uses fast GPU sorting algorithms and is inspired by tile-based ... | p. 2 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 2 RELATED WORK - extractive body cue:** We observe that our method performs relatively well, avoiding complete failure even without the SfM points.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 9. If we limit the number of points that receive gradients, the effect on visual quality is significant. Left: limit of 10 Gaussians that ...
- **p. 11 / 2 RELATED WORK - extractive body cue:** Comparison of failure artifacts: Mip-NeRF360 has "floaters" and grainy appearance (left, foreground), while our method produces coarse, anisoptropic Gaussians resulting in low-detail visuals (right, background).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The fast - but lower-quality - radiance field methods can achieve interactive rendering times depending on the scene (10-15 frames per second), but fall short ...
- **p. 9 / 2 RELATED WORK - extractive body cue:** Also in areas not well covered from training views, the random initialization method appears to have more floaters that cannot be removed by optimization.
- **p. 10 / 2 RELATED WORK - extractive body cue:** 7.4 Limitations Our method is not without limitations.

- **PDF anchors reviewed:** datasets p. 1 (Front matter), p. 1 (Front matter), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), metrics p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 14 (Figure/Table caption), p. 14 (Figure/Table caption), p. 1 (Front matter), p. 1 (Front matter), baselines p. 1 (1 INTRODUCTION), p. 5 (Figure/Table caption), p. 1 (Front matter), p. 8 (Figure/Table caption), p. 11 (Figure/Table caption), p. 2 (1 INTRODUCTION), results p. 1 (Figure/Table caption), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
