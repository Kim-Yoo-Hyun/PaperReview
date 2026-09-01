# Evaluation - Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SoqzNbcBjy; PDF retrieval source: https://openreview.net/pdf/b1b7493189ab7bb4d33ec2f618e7c920cfa17565.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 10 (Figure/Table caption)): Figure 2: (a) Two-step methods: Existing range-view LiDAR generative models typically generate only depth and reflectance images, requiring an additional pre-trained segmentation model to predict semantic labels. (b) SPIRAL: In ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive PDF cue:** We conduct an extensive experimental study on SemanticKITTI [3] and nuScenes [5] datasets and follow their official data splits.
- **p. 7 / 4 Experiments - extractive PDF cue:** We report the experimental results on the nuScenes [5] dataset in Table 2.
- **p. 9 / 4 Experiments - extractive PDF cue:** We assess GDA using synthetic samples from R2DM [42] and Spiral, under different ratios (1%, 10%, 20%) of real labeled data from SemanticKITTI [3], as ...
- **p. 9 / 4 Experiments - extractive PDF cue:** Method Param (M) NFE Range View Cartesian BEV FRD↓ (×1) MMD↓ (×10-1) S-FRD↓ (×1) S-MMD↓ (×10-1) FPD↓ (×1) MMD↓ (×10-1) S-FPD↓ (×1) S-MMD↓ (×10-1) JSD↓ ...
- **p. 10 / 4 Experiments - extractive PDF cue:** We performed a statistical analysis on 1,000 samples each from SemanticKITTI and nuScenes.
- **p. 10 / 4 Experiments - extractive PDF cue:** Additionally, the inference times per sample for RangeNet++ [40] and SPVCNN++ [36] are 0.08s and 0.05s respectively on the same hardware.
- **p. 8 / 4 Experiments - extractive PDF cue:** As shown in the second and third rows of Table 3, although Spiral is not fine-tuned for such extreme weather conditions, its generated data still ...
- **p. 8 / 4 Experiments - extractive PDF cue:** The best and second best scores under each metric are highlighted in bold and underline.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2: (a) Two-step methods: Existing range-view LiDAR generative models typically generate only depth and reflectance images, requiring an additional pre-trained segmentation model to ... | p. 2 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Despite having the smallest parameter size of only 61M, Spiral achieves the best performance across all semantic-aware metrics, outperforming the two-step method, R2DM [42] ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results shown in Figure 7 indicate that Spiral's performance improves significantly when NFE < 256, while further increases in NFE yield only marginal ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Examples of semantic artifacts are shown in 7⃝, 8⃝, 9⃝, and 11 ⃝, while geometric artifacts such as local distortion and large noise are ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared with the second best method (R2DM [42] & RangeNet++ [40]), Spiral achieves improvements of 49.03%, 67.84%, and 46.79% on S-FRD, S-FPD, and S-JSD, ... | p. 7 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive PDF cue:** We conduct an extensive experimental study on SemanticKITTI [3] and nuScenes [5] datasets and follow their official data splits.
- **p. 7 / 4 Experiments - extractive PDF cue:** We report the experimental results on the nuScenes [5] dataset in Table 2.
- **p. 9 / 4 Experiments - extractive PDF cue:** We assess GDA using synthetic samples from R2DM [42] and Spiral, under different ratios (1%, 10%, 20%) of real labeled data from SemanticKITTI [3], as ...
- **p. 9 / 4 Experiments - extractive PDF cue:** Method Param (M) NFE Range View Cartesian BEV FRD↓ (×1) MMD↓ (×10-1) S-FRD↓ (×1) S-MMD↓ (×10-1) FPD↓ (×1) MMD↓ (×10-1) S-FPD↓ (×1) S-MMD↓ (×10-1) JSD↓ ...
- **p. 10 / 4 Experiments - extractive PDF cue:** We performed a statistical analysis on 1,000 samples each from SemanticKITTI and nuScenes.
- **p. 10 / 4 Experiments - extractive PDF cue:** Additionally, the inference times per sample for RangeNet++ [40] and SPVCNN++ [36] are 0.08s and 0.05s respectively on the same hardware.
- **p. 8 / 4 Experiments - extractive PDF cue:** As shown in the second and third rows of Table 3, although Spiral is not fine-tuned for such extreme weather conditions, its generated data still ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Visualization of LiDAR scenes and their semantic labels jointly generated by SPIRAL, exhibiting high geometric fidelity and semantic-geometric consistency.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: (a) Two-step methods: Existing range-view LiDAR generative models typically generate only depth and reflectance images, requiring an additional pre-trained segmentation model to predict ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: (a) Unconditional Step: Spiral takes noisy LiDAR scenes xt as input and predicts both the semantic map ˆyt and the noise ˆϵt, where ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: (a) Range-view based semantic-aware feature f s is constructed by concatenating the features extracted by the RangeNet++ [3] encoder and the LiDM [48] ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Comparisons with state-of-the-art LiDAR generation models on the SemanticKITTI [3] dataset. We evaluate methods using the Range View, Cartesian, and BEV representations. Symbols ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Visualizations of generated LiDAR scenes on SemanticKITTI [3]. For two-step methods, we use the labels produced by RangeNet++ [40] due to its superior ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Comparisons with state-of-the-art LiDAR generation models on the nuScenes [5] dataset. We evaluate methods using the Range View, Cartesian, and BEV representations. Symbols ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: Visualizations of generated LiDAR scenes on nuScenes [5]. For two-step methods, we use the labels produced by RangeNet++ [40] due to its superior ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct an extensive experimental study on SemanticKITTI [3] and nuScenes [5] datasets and follow their official data splits. | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | We report the experimental results on the nuScenes [5] dataset in Table 2. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 5 (3 Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Methodology), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The best and second best scores under each metric are highlighted in bold and underline. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The generated labeled LiDAR scenes from Spiral and other baseline methods, as shown in Figure 5, demonstrate the superior performance of Spiral in both ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Surprisingly, the more advanced segmentation model SPVCNN++ performs worse than RangeNet++ on the unlabeled scenes generated by LiDARGen [73] and LiDM [48], resulting in ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| As shown in the second and third rows of Table 3, although Spiral is not fine-tuned for such extreme weather conditions, its generated data ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| However, the performance of Spiral starts to deteriorate when δ < 0.6. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| To quantify the effect of the confidence threshold δ, we evaluate the performance of Spiral under different δ settings in {0.3, 0.5, 0.6, 0.7, ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 2: (a) Two-step methods: Existing range-view LiDAR generative models typically generate only depth and reflectance images, requiring an additional pre-trained segmentation model to ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Spiral demonstrates superior inference efficiency compared to LiDM and LiDARGen. | definition/direction/unit from same section | p. 10 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Spiral consistently outperforms the other baseline methods on all metrics with the smallest parameter size. | comparison identity and matched condition | p. 7 (4 Experiments) |
| For the generative models in two-step baseline methods, including LiDARGen [73], LiDM [48], and R2DM [42], we follow the official training settings. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Examples of semantic artifacts are shown in 7⃝, 8⃝, 9⃝, and 11 ⃝, while geometric artifacts such as local distortion and large noise are ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Spiral demonstrates superior inference efficiency compared to LiDM and LiDARGen. | comparison identity and matched condition | p. 10 (4 Experiments) |
| With fewer sampling steps, Spiral outperforms R2DM [42] using its default setting of NFE = 256, indicated by the dashed line. | comparison identity and matched condition | p. 10 (4 Experiments) |
| Table 1: Comparisons with state-of-the-art LiDAR generation models on the SemanticKITTI [3] dataset. We evaluate methods using the Range View, Cartesian, and BEV representations. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To quantify the effect of the confidence threshold δ, we evaluate the performance of Spiral under different δ settings in {0.3, 0.5, 0.6, 0.7, ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| We attribute this drop to the higher sensitivity of larger models to noise, compounded by the greater noise present in the LiDAR scenes generated ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| Although the performance of SPVCNN++ improves after jittering-based fine-tuning, it still lags behind RangeNet++. | component/input/data sensitivity | p. 7 (4 Experiments) |
| As shown in the second and third rows of Table 3, although Spiral is not fine-tuned for such extreme weather conditions, its generated data ... | component/input/data sensitivity | p. 8 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, the key contributions of this work are as follows: • We propose a novel state-of-the-art semantic-aware range-view LiDAR diffusion model, SPIRAL, which ... | Figure 2: (a) Two-step methods: Existing range-view LiDAR generative models typically generate only depth and reflectance images, requiring an additional pre-trained segmentation model to ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 10 (Figure/Table caption) |
| Primary metric/result | Despite having the smallest parameter size of only 61M, Spiral achieves the best performance across all semantic-aware metrics, outperforming the two-step method, R2DM [42] ... | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive PDF cue:** During pre-processing, the LiDAR scenes are projected into range-view images of spatial resolutions 64×1024 and 32×1024, respectively.
- **p. 7 / 4 Experiments - extractive PDF cue:** The training process takes ∼36 hours.
- **p. 7 / 4 Experiments - extractive PDF cue:** We also run LiDM using the DDIM [51] sampling method with 256 steps for fair comparison.
- **p. 7 / 4 Experiments - extractive PDF cue:** LiDARGen models the denoising process with 232 noise levels and requires 5 steps per level by default, resulting in a total NFE of 1160.
- **p. 10 / 4 Experiments - extractive PDF cue:** We performed a statistical analysis on 1,000 samples each from SemanticKITTI and nuScenes.
- **p. 10 / 4 Experiments - extractive PDF cue:** With the default 256 denoising steps, closed-loop inference is activated (i.e., once ≥80% of semantic predictions exceed the confidence threshold) at an average step of ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | With δ = 0.3, the performance of the closed-loop inference even falls behind that of the open-loop inference. | p. 9 (4 Experiments) |
| body limitation/failure cue | To further assess robustness, we also evaluate Spiral-based generative data augmentation on the fog and wet-ground subsets of Robo3D [24], which simulate adverse weather ... | p. 7 (4 Experiments) |
| body limitation/failure cue | For the previous metrics that evaluate only the unlabeled LiDAR scenes, Spiral outperforms R2DM on most metrics, indicating that the additional semantic prediction task ... | p. 7 (4 Experiments) |
| body limitation/failure cue | Unlike the two-step methods, Spiral does not require a segmentation model to generate semantic labels. | p. 10 (4 Experiments) |
| body limitation/failure cue | Figure 3: (a) Unconditional Step: Spiral takes noisy LiDAR scenes xt as input and predicts both the semantic map ˆyt and the noise ˆϵt, ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Additionally, we evaluate SPVCNN++ under the same settings on out-of-distribution subsets, fog and wet-ground, from Robo3D [24]. | p. 8 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train SPIRAL on NVIDIA A6000 GPUs with 48 GB VRAM for 300k steps using the Adam optimizer [21] with a learning rate of ... | p. 7 (4 Experiments) |
| Additionally, the inference times per sample for RangeNet++ [40] and SPVCNN++ [36] are 0.08s and 0.05s respectively on the same hardware. | p. 10 (4 Experiments) |
| We also run LiDM using the DDIM [51] sampling method with 256 steps for fair comparison. | p. 7 (4 Experiments) |
| On an A6000 GPU, Spiral achieves an average inference speed of 5.7 seconds per sample. | p. 8 (4 Experiments) |
| With fewer sampling steps, Spiral outperforms R2DM [42] using its default setting of NFE = 256, indicated by the dashed line. | p. 10 (4 Experiments) |
| It alternates between two types of steps: unconditional and conditional. | p. 4 (3 Methodology) |
| Starting from a real sample x0 ∼q(x0), a forward process gradually adds Gaussian noise over T steps, such that the final sample approximates a ... | p. 4 (3 Methodology) |
| Spiral takes as input the perturbed depth and reflectance images xt, along with semantic maps y encoded as RGB images. | p. 5 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive PDF cue:** With δ = 0.3, the performance of the closed-loop inference even falls behind that of the open-loop inference.
- **p. 7 / 4 Experiments - extractive PDF cue:** To further assess robustness, we also evaluate Spiral-based generative data augmentation on the fog and wet-ground subsets of Robo3D [24], which simulate adverse weather conditions ...
- **p. 7 / 4 Experiments - extractive PDF cue:** For the previous metrics that evaluate only the unlabeled LiDAR scenes, Spiral outperforms R2DM on most metrics, indicating that the additional semantic prediction task does ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Unlike the two-step methods, Spiral does not require a segmentation model to generate semantic labels.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: (a) Unconditional Step: Spiral takes noisy LiDAR scenes xt as input and predicts both the semantic map ˆyt and the noise ˆϵt, where ...
- **p. 8 / 4 Experiments - extractive PDF cue:** Additionally, we evaluate SPVCNN++ under the same settings on out-of-distribution subsets, fog and wet-ground, from Robo3D [24].

- **PDF anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), metrics p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), baselines p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 8 (Figure/Table caption), results p. 2 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
