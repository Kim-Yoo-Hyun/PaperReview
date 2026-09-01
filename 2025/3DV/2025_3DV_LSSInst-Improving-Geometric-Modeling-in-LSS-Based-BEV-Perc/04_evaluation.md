# Evaluation - LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=MaN2x3O2Rk&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Generalization Ability and Geometric-Wise), p. 6 (4.2. Benchmark Results), p. 7 (4.5. Multiplicate Queries Ablations), p. 13 (Figure/Table caption), p. 7 (4.3. Generalization Ability and Geometric-Wise), p. 13 (Figure/Table caption)): The table reveals that our LSSInst achieves notable improvements in mAP and NDS compared to standalone BEV detectors at a minor cost.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** Dataset We conducted extensive experiments on the nuScenes 3D detection benchmark [1], a large-scale dataset in the autonomous driving scene.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** The dataset is divided into 850 scenes for training (train) or validation (val) purposes and 150 scenes for testing (test).
- **p. 7 / 4.4. Noise Resistance for Practical Robustness - extractive PDF cue:** Although we have verified the high performance of LSSInst on nuScenes [1], even the large-scale autonomous driving dataset inevitably contain disturbances in the extrinsics obtained ...
- **p. 7 / 4.3. Generalization Ability and Geometric-Wise - extractive PDF cue:** Comparison results of LSS-based detectors on 3D detection on the nuScenes test set.
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property (here ...
- **p. 7 / 4.4. Noise Resistance for Practical Robustness - extractive PDF cue:** 5, we demonstrate that LSSInst maintains good robustness, exhibiting higher performance and smaller overall attenuation.
- **p. 7 / 4.4. Noise Resistance for Practical Robustness - extractive PDF cue:** In actual autonomous driving scenarios, the detector is required to be resistant to the disturbance noise caused by small measurement errors.
- **p. 6 / 4.2. Benchmark Results - extractive PDF cue:** On the val set, we evaluated the performance of LSSInst against other models with the same setting and without the CBGS strategy and future frame ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments and Analysis (p. 6); 4.1. Experimental Settings (p. 6); 4.2. Benchmark Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Generalization Ability and Geometric-Wise | EMPIRICAL / SOURCE-REPORTED EVALUATION | The table reveals that our LSSInst achieves notable improvements in mAP and NDS compared to standalone BEV detectors at a minor cost. | p. 6 (4.3. Generalization Ability and Geometric-Wise) |
| 4.2. Benchmark Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the test set, our LSSInst achieves an mAP of 54.6% and an NDS of 62.9% without any additional augmentation, outperforming all LSS-based methods. | p. 6 (4.2. Benchmark Results) |
| 4.5. Multiplicate Queries Ablations | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the other hand, though the proposal queries from BEV alone can achieve overall good results, adding more queries 7 | p. 7 (4.5. Multiplicate Queries Ablations) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property ... | p. 13 (Figure/Table caption) |
| 4.3. Generalization Ability and Geometric-Wise | EMPIRICAL / SOURCE-REPORTED EVALUATION | Comparison results of LSS-based and two-stage detectors on 3D detection on the nuScenes val set. † denotes the performance without future frames for a ... | p. 7 (4.3. Generalization Ability and Geometric-Wise) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** Dataset We conducted extensive experiments on the nuScenes 3D detection benchmark [1], a large-scale dataset in the autonomous driving scene.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** The dataset is divided into 850 scenes for training (train) or validation (val) purposes and 150 scenes for testing (test).
- **p. 7 / 4.4. Noise Resistance for Practical Robustness - extractive PDF cue:** Although we have verified the high performance of LSSInst on nuScenes [1], even the large-scale autonomous driving dataset inevitably contain disturbances in the extrinsics obtained ...
- **p. 7 / 4.3. Generalization Ability and Geometric-Wise - extractive PDF cue:** Comparison results of LSS-based detectors on 3D detection on the nuScenes test set.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. The conceptual comparison of LSSInst with previous camera-based fashions. in recent years. The reasons can be attributed not only to the lower deployment ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1. The per-category AP comparison between two typical fashions with equivalent detection ability (∆mAP less than 0.5%) methods on the nuScenes test set. Group ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of LSSInst. The multi-view images with previous T frames are fed into the backbone network for the image features. BEV branch looks ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison results of LSS-based and two-stage detectors on 3D detection on the nuScenes val set. † denotes the performance without future frames for ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Comparison results of LSS-based detectors on 3D detection on the nuScenes test set. TTA denotes test time augmentation strategy.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Generalization and Geometric-wise Results of LSSInst compared with LSS-type Baselines. (‡ please refer to Footnote 2).
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. The noise resistance results for robustness. Method Noise mAP%↑Attenu.%↓NDS%↑Attenu.%↓ Baseline 0 35.74 - 46.84
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. Query Composition Composition of Queries mAP↑ NDS↑

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Dataset We conducted extensive experiments on the nuScenes 3D detection benchmark [1], a large-scale dataset in the autonomous driving scene. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Task/environment | The dataset is divided into 850 scenes for training (train) or validation (val) purposes and 150 scenes for testing (test). | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Settings), p. 7 (4.4. Noise Resistance for Practical Robustness) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3. Methodology), p. 4 (3. Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3. Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| 5, we demonstrate that LSSInst maintains good robustness, exhibiting higher performance and smaller overall attenuation. | definition/direction/unit from same section | p. 7 (4.4. Noise Resistance for Practical Robustness) |
| In actual autonomous driving scenarios, the detector is required to be resistant to the disturbance noise caused by small measurement errors. | definition/direction/unit from same section | p. 7 (4.4. Noise Resistance for Practical Robustness) |
| On the val set, we evaluated the performance of LSSInst against other models with the same setting and without the CBGS strategy and future ... | definition/direction/unit from same section | p. 6 (4.2. Benchmark Results) |
| Figure 1. The conceptual comparison of LSSInst with previous camera-based fashions. in recent years. The reasons can be attributed not only to the lower ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The learning rate, optimizer, and data augmentation methods used were the same as those in BEVDepth. | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| The noise resistance results for robustness. | definition/direction/unit from same section | p. 8 (4.5. Multiplicate Queries Ablations) |
| Query Composition Composition of Queries mAP↑ NDS↑ | definition/direction/unit from same section | p. 8 (4.5. Multiplicate Queries Ablations) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared our approach with LSS-based and two-stage state-of-the-art methods on the nuScenes val and test sets. | comparison identity and matched condition | p. 6 (4.2. Benchmark Results) |
| Generalization and Geometric-wise Results of LSSInst compared with LSS-type Baselines. | comparison identity and matched condition | p. 8 (4.5. Multiplicate Queries Ablations) |
| On the test set, our LSSInst achieves an mAP of 54.6% and an NDS of 62.9% without any additional augmentation, outperforming all LSS-based methods. | comparison identity and matched condition | p. 6 (4.2. Benchmark Results) |
| Here, the baseline is BEVDepth4D [25] with 4 frames. | comparison identity and matched condition | p. 7 (4.4. Noise Resistance for Practical Robustness) |
| Method Noise mAP%↑Attenu.%↓NDS%↑Attenu.%↓ Baseline 0 35.74 - 46.84 - LSSInst 38.28 - 49.43 - Baseline 0.5% 35.38 1.01 46.44 0.85 LSSInst 38.01 0.71 49.19 ... | comparison identity and matched condition | p. 8 (4.5. Multiplicate Queries Ablations) |
| Figure 4. Qualitative comparison between baseline proposals (red), predictions (blue), their superposition (purple), and GT (white). Spatial Sampling and Fusion As for spatial sampling, ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| On the test set, our LSSInst achieves an mAP of 54.6% and an NDS of 62.9% without any additional augmentation, outperforming all LSS-based methods. | component/input/data sensitivity | p. 6 (4.2. Benchmark Results) |
| On the val set, we evaluated the performance of LSSInst against other models with the same setting and without the CBGS strategy and future ... | component/input/data sensitivity | p. 6 (4.2. Benchmark Results) |
| Comparison results of LSS-based and two-stage detectors on 3D detection on the nuScenes val set. † denotes the performance without future frames for a ... | component/input/data sensitivity | p. 7 (4.3. Generalization Ability and Geometric-Wise) |
| We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 ... | component/input/data sensitivity | p. 7 (4.5. Multiplicate Queries Ablations) |
| Table 13. Point Ablation Points mAP↑ NDS↑ 1 0.365 0.477 2 | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 14. Weight Ablation Weight mAP↑ NDS↑ 1 0.365 0.477 2 | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception ... | The table reveals that our LSSInst achieves notable improvements in mAP and NDS compared to standalone BEV detectors at a minor cost. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Generalization Ability and Geometric-Wise), p. 6 (4.2. Benchmark Results), p. 7 (4.5. Multiplicate Queries Ablations), p. 13 (Figure/Table caption), p. 7 (4.3. Generalization Ability and Geometric-Wise), p. 13 (Figure/Table caption) |
| Primary metric/result | On the test set, our LSSInst achieves an mAP of 54.6% and an NDS of 62.9% without any additional augmentation, outperforming all LSS-based methods. | numeric claim only at cited anchor | p. 6 (4.2. Benchmark Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** The dataset is divided into 850 scenes for training (train) or validation (val) purposes and 150 scenes for testing (test).
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** The time interval τ is 0.5s, and long-term suppression λ is 0.6.
- **p. 7 / 4.4. Noise Resistance for Practical Robustness - extractive PDF cue:** Here, the baseline is BEVDepth4D [25] with 4 frames.
- **p. 5 / 3. Methodology - extractive PDF cue:** The final box embedding Gχ ∈RN×C can be formulated by Gχ = Eg   2 X j=1 Ej l3  P j d3  ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 ... | p. 7 (4.5. Multiplicate Queries Ablations) |
| body limitation/failure cue | In actual autonomous driving scenarios, the detector is required to be resistant to the disturbance noise caused by small measurement errors. | p. 7 (4.4. Noise Resistance for Practical Robustness) |
| body limitation/failure cue | The noise resistance results for robustness. | p. 8 (4.5. Multiplicate Queries Ablations) |
| body limitation/failure cue | Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | Method Noise mAP%↑Attenu.%↓NDS%↑Attenu.%↓ Baseline 0 35.74 - 46.84 - LSSInst 38.28 - 49.43 - Baseline 0.5% 35.38 1.01 46.44 0.85 LSSInst 38.01 0.71 49.19 ... | p. 8 (4.5. Multiplicate Queries Ablations) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The learning rate, optimizer, and data augmentation methods used were the same as those in BEVDepth. | p. 6 (4.1. Experimental Settings) |
| Implementation Details We implemented our network framework utilizing the open-source MMDetection3D [7] in PyTorch. | p. 6 (4.1. Experimental Settings) |
| Here the encoder is designed as a very lightweight residual network for dimension reduction only. | p. 4 (3. Methodology) |
| After the shared view transformation, a sequence of BEV representations will be aligned into current time t and fed to the BEV temporal encoder ... | p. 4 (3. Methodology) |
| This branch can be roughly regarded as a multilayer Transformer-decoder-like [42] module for 3D detection, which is briefly divided into two parts: box-level offset ... | p. 5 (3. Methodology) |
| With this convenience, we can encode all the geometric-aware information of the entire box to substitute the transitional positional encoding, thereby expanding and enriching ... | p. 5 (3. Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.5. Multiplicate Queries Ablations - extractive PDF cue:** We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries ...
- **p. 7 / 4.4. Noise Resistance for Practical Robustness - extractive PDF cue:** In actual autonomous driving scenarios, the detector is required to be resistant to the disturbance noise caused by small measurement errors.
- **p. 8 / 4.5. Multiplicate Queries Ablations - extractive PDF cue:** The noise resistance results for robustness.
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property (here ...
- **p. 8 / 4.5. Multiplicate Queries Ablations - extractive PDF cue:** Method Noise mAP%↑Attenu.%↓NDS%↑Attenu.%↓ Baseline 0 35.74 - 46.84 - LSSInst 38.28 - 49.43 - Baseline 0.5% 35.38 1.01 46.44 0.85 LSSInst 38.01 0.71 49.19 0.49 ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.4. Noise Resistance for Practical Robustness), p. 7 (4.3. Generalization Ability and Geometric-Wise), metrics p. 13 (Figure/Table caption), p. 7 (4.4. Noise Resistance for Practical Robustness), p. 7 (4.4. Noise Resistance for Practical Robustness), p. 6 (4.2. Benchmark Results), p. 1 (Figure/Table caption), p. 6 (4.1. Experimental Settings), baselines p. 6 (4.2. Benchmark Results), p. 8 (4.5. Multiplicate Queries Ablations), p. 6 (4.2. Benchmark Results), p. 7 (4.4. Noise Resistance for Practical Robustness), p. 8 (4.5. Multiplicate Queries Ablations), p. 14 (Figure/Table caption), results p. 6 (4.3. Generalization Ability and Geometric-Wise), p. 6 (4.2. Benchmark Results), p. 7 (4.5. Multiplicate Queries Ablations), p. 13 (Figure/Table caption), p. 7 (4.3. Generalization Ability and Geometric-Wise), p. 13 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
