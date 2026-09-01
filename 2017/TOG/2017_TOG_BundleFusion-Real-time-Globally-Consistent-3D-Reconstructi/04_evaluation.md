# Evaluation - BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Reintegration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1604.01093; PDF retrieval source: https://arxiv.org/pdf/1604.01093. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (6 RESULTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS), p. 10 (6 RESULTS), p. 11 (6 RESULTS), p. 12 (6 RESULTS)): While online alignment based on sparse features only (Ours (s)) achieves reasonable results, using dense matching only in per chunk alignment further increases accuracy (Ours (sd)).

## Evaluation Body Digest

- **p. 13 / 6 RESULTS - extractive PDF cue:** Te SUN3D dataset also contains eight scenes which contain manual object-correspondence annotations in order to guide their reconstructions; we show reconstruction results using our method ...
- **p. 13 / 6 RESULTS - extractive PDF cue:** 7.1 Additional Qalitative Results Reconstructed models for the eight scenes in our dataset are publicly available 3.
- **p. 14 / 6 RESULTS - extractive PDF cue:** Reconstruction results on scenes from the SUN3D dataset [57], using SUN3Dsfm and our approach.
- **p. 15 / 6 RESULTS - extractive PDF cue:** Reconstruction results on eight scenes from the SUN3D dataset [57], chosen from the List of Annotated Scenes (our method is fully automated and does not ...
- **p. 17 / 6 RESULTS - extractive PDF cue:** BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Re-integration • 1:17 Additionally, we further evaluate our camera tracking on the augmented ICL-NUIM dataset of ...
- **p. 8 / 6 RESULTS - extractive PDF cue:** Reconstruction results of scenes captured using our live system are shown in Fig.
- **p. 8 / 6 RESULTS - extractive PDF cue:** Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., if the sensor is occluded or observes ...
- **p. 9 / 6 RESULTS - extractive PDF cue:** Note, we do not compare to their newer non-rigid approach, since it fails on most of our dataset sequences.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 6 RESULTS (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | While online alignment based on sparse features only (Ours (s)) achieves reasonable results, using dense matching only in per chunk alignment further increases accuracy ... | p. 12 (6 RESULTS) |
| 6 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Large-scale reconstruction results: our proposed real-time global pose optimization outperforms current state-of-the-art online reconstruction systems. | p. 9 (6 RESULTS) |
| 6 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We achieve this real-time performance with the combination of our tailored data-parallel Gauss-Newton solver (efficiently handling millions of residuals and solving for over a ... | p. 10 (6 RESULTS) |
| 6 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Dense Alignment: the proposed dense intra- and inter- chunk alignment (top) leads to higher quality reconstructions than only the sparse alignment step (botom). their ... | p. 10 (6 RESULTS) |
| 6 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Note that recent work provides detailed intuition why hand-crafed optimizers outperform existing, general solver libraries [6]. | p. 11 (6 RESULTS) |

## Dataset / Benchmark Role

- **p. 13 / 6 RESULTS - extractive PDF cue:** Te SUN3D dataset also contains eight scenes which contain manual object-correspondence annotations in order to guide their reconstructions; we show reconstruction results using our method ...
- **p. 13 / 6 RESULTS - extractive PDF cue:** 7.1 Additional Qalitative Results Reconstructed models for the eight scenes in our dataset are publicly available 3.
- **p. 14 / 6 RESULTS - extractive PDF cue:** Reconstruction results on scenes from the SUN3D dataset [57], using SUN3Dsfm and our approach.
- **p. 15 / 6 RESULTS - extractive PDF cue:** Reconstruction results on eight scenes from the SUN3D dataset [57], chosen from the List of Annotated Scenes (our method is fully automated and does not ...
- **p. 17 / 6 RESULTS - extractive PDF cue:** BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Re-integration • 1:17 Additionally, we further evaluate our camera tracking on the augmented ICL-NUIM dataset of ...
- **p. 8 / 6 RESULTS - extractive PDF cue:** Reconstruction results of scenes captured using our live system are shown in Fig.
- **p. 8 / 6 RESULTS - extractive PDF cue:** Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., if the sensor is occluded or observes ...
- **p. 9 / 6 RESULTS - extractive PDF cue:** Note, we do not compare to their newer non-rigid approach, since it fails on most of our dataset sequences.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1. Our novel real-time 3D reconstruction approach solves for global pose alignment and obtains dense volumetric reconstructions at a level of quality and completeness ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Our global pose optimization takes as input the RGB-D stream of a commodity sensor, detects pairwise correspondences between the input frames, and performs ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 4. Performance Evaluation: our proposed pipeline runs at well beyond 30Hz for all used test sequences. The computations are split up over two GPUs ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 5. Convergence analysis of the global keyframe optimization (log scale): peaks correspond to new global keyframes. Only a few iterations are re- quired for ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 6. Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., if the sensor is occluded ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 3. Large-scale reconstruction results: our proposed real-time global pose optimization outperforms current state-of-the-art online reconstruction systems. The globally aligned 3D reconstructions are at a ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 7. Our proposed real-time global pose optimization (top) outperforms the method of Whelan et al. [54] (botom) in terms of scan completeness and alignment ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 8. Our proposed real-time global pose optimization (top) delivers a reconstruction quality on par or even beter than the off-line Redwood [4] system (botom). ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Te SUN3D dataset also contains eight scenes which contain manual object-correspondence annotations in order to guide their reconstructions; we show reconstruction results using our ... | embodiment, simulator version and control stack | p. 13 (6 RESULTS), p. 13 (6 RESULTS) |
| Task/environment | 7.1 Additional Qalitative Results Reconstructed models for the eight scenes in our dataset are publicly available 3. | reset, timeout, object/scene variation | p. 13 (6 RESULTS), p. 14 (6 RESULTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In addition to the camera tracking evaluation provided in Section 6 of the paper, we evaluate surface reconstruction accuracy (mean distance of the model ... | definition/direction/unit from same section | p. 13 (6 RESULTS) |
| Surface reconstruction accuracy on the synthetic ICL-NUIM dataset by [17]. kt0 kt1 kt2 kt3 DVO SLAM 3.2cm 6.1cm 11.9cm 5.3cm RGB-D SLAM 4.4cm 3.2cm ... | definition/direction/unit from same section | p. 17 (6 RESULTS) |
| [54] (botom) in terms of scan completeness and alignment accuracy. | definition/direction/unit from same section | p. 9 (6 RESULTS) |
| Our full sparse and dense matching approach on both local and global level leads to the highest accuracy. | definition/direction/unit from same section | p. 12 (6 RESULTS) |
| While online alignment based on sparse features only (Ours (s)) achieves reasonable results, using dense matching only in per chunk alignment further increases accuracy ... | definition/direction/unit from same section | p. 12 (6 RESULTS) |
| We achieve this real-time performance with the combination of our tailored data-parallel Gauss-Newton solver (efficiently handling millions of residuals and solving for over a ... | definition/direction/unit from same section | p. 10 (6 RESULTS) |
| Precision and Recall of Loop Closures. | definition/direction/unit from same section | p. 11 (6 RESULTS) |
| If a new keyframe cannot be aligned successfully, we assume tracking is lost and do not integrate surface measurements. | definition/direction/unit from same section | p. 11 (6 RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Large-scale reconstruction results: our proposed real-time global pose optimization outperforms current state-of-the-art online reconstruction systems. | comparison identity and matched condition | p. 9 (6 RESULTS) |
| Note that recent work provides detailed intuition why hand-crafed optimizers outperform existing, general solver libraries [6]. | comparison identity and matched condition | p. 11 (6 RESULTS) |
| Fig. 7. Our proposed real-time global pose optimization (top) outperforms the method of Whelan et al. [54] (botom) in terms of scan completeness and ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., if the sensor is occluded or ... | comparison identity and matched condition | p. 8 (6 RESULTS) |
| Comparison to the VoxelHashing approach of Nießner et al. | comparison identity and matched condition | p. 11 (6 RESULTS) |
| Comparison of different voxel resolutions: 4mm voxel resolution (lef) leads to higher-fidelity reconstructions than the coarser 1cm resolution (right). | comparison identity and matched condition | p. 12 (6 RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., if the sensor is occluded or ... | component/input/data sensitivity | p. 8 (6 RESULTS) |
| We additionally compare to the offline Redwood approach [4], using their rigid variant, see Fig. | component/input/data sensitivity | p. 9 (6 RESULTS) |
| Note the completeness of the scans, the global alignment without noticeable camera drif and the high local quality of the reconstructions in both geometry ... | component/input/data sensitivity | p. 9 (6 RESULTS) |
| While our solver takes a couple more iterations to converge without the Levenberg-Marquardt damping strategy, it still runs ≈20 times faster than Ceres while ... | component/input/data sensitivity | p. 11 (6 RESULTS) |
| Note that for Redwood, we show results for the rigid variant, which produced beter camera tracking results. | component/input/data sensitivity | p. 12 (6 RESULTS) |
| Te SUN3D dataset also contains eight scenes which contain manual object-correspondence annotations in order to guide their reconstructions; we show reconstruction results using our ... | component/input/data sensitivity | p. 13 (6 RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches. | While online alignment based on sparse features only (Ours (s)) achieves reasonable results, using dense matching only in per chunk alignment further increases accuracy ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (6 RESULTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS), p. 10 (6 RESULTS), p. 11 (6 RESULTS), p. 12 (6 RESULTS) |
| Primary metric/result | Large-scale reconstruction results: our proposed real-time global pose optimization outperforms current state-of-the-art online reconstruction systems. | numeric claim only at cited anchor | p. 9 (6 RESULTS) |

- Numeric sentences retained from the body:
- **p. 8 / 6 RESULTS - extractive PDF cue:** Te RGB-D stream is captured at 30Hz with a color and depth resolution of 640 × 480.
- **p. 8 / 6 RESULTS - extractive PDF cue:** Performance Evaluation: our proposed pipeline runs at well beyond 30Hz for all used test sequences.
- **p. 8 / 6 RESULTS - extractive PDF cue:** Tis also demonstrates that our global pose alignment strategy scales well to large spatial extents and long sequences (over 20,000 frames).
- **p. 10 / 6 RESULTS - extractive PDF cue:** Our pipeline runs with a framerate well beyond 30Hz (see Fig.
- **p. 10 / 6 RESULTS - extractive PDF cue:** Note that the global dense optimization runs in < 500ms at the end of the sequences.
- **p. 13 / 6 RESULTS - extractive PDF cue:** Tis corresponds to about 14 minutes of continuous scanning, assuming 30Hz input - although many RGB-D sensors have a lower frame rate which allows for ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1. Our novel real-time 3D reconstruction approach solves for global pose alignment and obtains dense volumetric reconstructions at a level of quality and ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., if the sensor is occluded or ... | p. 8 (6 RESULTS) |
| body limitation/failure cue | [37]: in contrast to the frame-to-model tracking of VoxelHashing, our novel global pose optimization implicitly handles loop closure (top), robustly detects and recovers from ... | p. 11 (6 RESULTS) |
| body limitation/failure cue | Fig. 7. Our proposed real-time global pose optimization (top) outperforms the method of Whelan et al. [54] (botom) in terms of scan completeness and ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | To indicate tracking failure, the reconstruction is shown with a gray overlay. | p. 11 (6 RESULTS) |
| body limitation/failure cue | Te relocalization (due to sensor occlusion) in the sequence Apt 2 cannot be handled by state-of-theart methods such as ElasticFusion and Redwood. | p. 13 (6 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Tis sequence has a CPU memory footprint of 34.7GB and requires 7.3GB of GPU memory (4mm voxels) for tracking and reconstruction. | p. 11 (6 RESULTS) |
| Here, the user or robot must scan an entire room (or several spaces) in real-time, with instantaneous and continual integration of the accumulated 3D ... | p. 1 (1 INTRODUCTION) |
| We measure the performance of our pipeline on an Intel Core i7 3.4GHz CPU (32GB RAM). | p. 10 (6 RESULTS) |
| For compute, we use a combination of a NVIDIA GeForce GTX Titan X and a GTX Titan Black. | p. 10 (6 RESULTS) |
| Performance comparison of our tailored GPU-based solver to Ceres [1]. | p. 11 (6 RESULTS) |
| As can be seen, all steps of the globally consistent camera tracking increase precision while maintaining sufficient recall. | p. 12 (6 RESULTS) |
| Another limitation is that we currently run our method on two GPUs. | p. 13 (6 RESULTS) |
| With our current hardware configurations, we are limited to scans of up to 25,000 input RGB-D frames. | p. 13 (6 RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1. Our novel real-time 3D reconstruction approach solves for global pose alignment and obtains dense volumetric reconstructions at a level of quality and completeness ...
- **p. 8 / 6 RESULTS - extractive PDF cue:** Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., if the sensor is occluded or observes ...
- **p. 11 / 6 RESULTS - extractive PDF cue:** [37]: in contrast to the frame-to-model tracking of VoxelHashing, our novel global pose optimization implicitly handles loop closure (top), robustly detects and recovers from tracking ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 7. Our proposed real-time global pose optimization (top) outperforms the method of Whelan et al. [54] (botom) in terms of scan completeness and alignment ...
- **p. 11 / 6 RESULTS - extractive PDF cue:** To indicate tracking failure, the reconstruction is shown with a gray overlay.
- **p. 13 / 6 RESULTS - extractive PDF cue:** Te relocalization (due to sensor occlusion) in the sequence Apt 2 cannot be handled by state-of-theart methods such as ElasticFusion and Redwood.

- **PDF anchors reviewed:** datasets p. 13 (6 RESULTS), p. 13 (6 RESULTS), p. 14 (6 RESULTS), p. 15 (6 RESULTS), p. 17 (6 RESULTS), p. 8 (6 RESULTS), metrics p. 13 (6 RESULTS), p. 17 (6 RESULTS), p. 9 (6 RESULTS), p. 12 (6 RESULTS), p. 12 (6 RESULTS), p. 10 (6 RESULTS), baselines p. 9 (6 RESULTS), p. 11 (6 RESULTS), p. 9 (Figure/Table caption), p. 8 (6 RESULTS), p. 11 (6 RESULTS), p. 12 (6 RESULTS), results p. 12 (6 RESULTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS), p. 10 (6 RESULTS), p. 11 (6 RESULTS), p. 12 (6 RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
