# Evaluation - Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SoqzNbcBjy; PDF retrieval source: https://arxiv.org/pdf/2505.22643. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 7 (4 Experiments)): Despite having the smallest parameter size of only 61M, Spiral achieves the best performance across all semanticaware metrics, outperforming the two-step method, R2DM [18] & SPVCNN++ [57], by 31.03%, 56.33%, ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive body cue:** We conduct an extensive experimental study on SemanticKITTI [34] and nuScenes [35] datasets and follow their official data splits.
- **p. 7 / 4 Experiments - extractive body cue:** We report the experimental results on the nuScenes [35] dataset in Table 2.
- **p. 9 / 4 Experiments - extractive body cue:** Method Param (M) NFE Range View Cartesian BEV FRD↓ (×1) MMD↓ (×10-1) S-FRD↓ (×1) S-MMD↓ (×10-1) FPD↓ (×1) MMD↓ (×10-1) S-FPD↓ (×1) S-MMD↓ (×10-1) JSD↓ ...
- **p. 10 / 4 Experiments - extractive body cue:** We performed a statistical analysis on 1,000 samples each from SemanticKITTI and nuScenes.
- **p. 10 / 4 Experiments - extractive body cue:** Additionally, the inference times per sample for RangeNet++ [32] and SPVCNN++ [57] are 0.08s and 0.05s, respectively, on the same hardware.
- **p. 8 / 4 Experiments - extractive body cue:** We evaluate the effectiveness of using Spiral's generated samples to augment the training set for segmentation learning on SemanticKITTI [34].
- **p. 8 / 4 Experiments - extractive body cue:** As shown in the second and third rows of Table 3, although Spiral is not fine-tuned for such extreme weather conditions, its generated data still ...
- **p. 11 / A Evaluation Metrics - extractive body cue:** In the main paper, we evaluate the generative quality of Spiral for the LiDAR scene x with semantic map y from three perspectives: range-view images, ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); A Evaluation Metrics (p. 11); A.1 Evaluation on Range View and Cartesian Point Clouds (p. 11); A.2 Evaluation on Bird's Eye View (p. 12).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Despite having the smallest parameter size of only 61M, Spiral achieves the best performance across all semanticaware metrics, outperforming the two-step method, R2DM [18] ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in the first row of Table 3, the generated samples from Spiral consistently improve the performance of SPVCNN++ and outperform those from ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results shown in Figure 7 indicate that Spiral's performance improves significantly when NFE < 256, while further increases in NFE yield only marginal ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared with the second best method (R2DM [18] & RangeNet++ [32]), Spiral achieves improvements of 49.03%, 67.84%, and 46.79% on S-FRD, S-FPD, and S-JSD, ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results listed in Table 4 indicate that Spiral performs well when δ ∈{0.7, 0.8, 0.9} and achieves slightly best performance at δ = ... | p. 10 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive body cue:** We conduct an extensive experimental study on SemanticKITTI [34] and nuScenes [35] datasets and follow their official data splits.
- **p. 7 / 4 Experiments - extractive body cue:** We report the experimental results on the nuScenes [35] dataset in Table 2.
- **p. 9 / 4 Experiments - extractive body cue:** Method Param (M) NFE Range View Cartesian BEV FRD↓ (×1) MMD↓ (×10-1) S-FRD↓ (×1) S-MMD↓ (×10-1) FPD↓ (×1) MMD↓ (×10-1) S-FPD↓ (×1) S-MMD↓ (×10-1) JSD↓ ...
- **p. 10 / 4 Experiments - extractive body cue:** We performed a statistical analysis on 1,000 samples each from SemanticKITTI and nuScenes.
- **p. 10 / 4 Experiments - extractive body cue:** Additionally, the inference times per sample for RangeNet++ [32] and SPVCNN++ [57] are 0.08s and 0.05s, respectively, on the same hardware.
- **p. 8 / 4 Experiments - extractive body cue:** We evaluate the effectiveness of using Spiral's generated samples to augment the training set for segmentation learning on SemanticKITTI [34].
- **p. 8 / 4 Experiments - extractive body cue:** As shown in the second and third rows of Table 3, although Spiral is not fine-tuned for such extreme weather conditions, its generated data still ...
- **p. 11 / A Evaluation Metrics - extractive body cue:** In the main paper, we evaluate the generative quality of Spiral for the LiDAR scene x with semantic map y from three perspectives: range-view images, ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct an extensive experimental study on SemanticKITTI [34] and nuScenes [35] datasets and follow their official data splits. | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | We report the experimental results on the nuScenes [35] dataset in Table 2. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 Methodology), p. 6 (3 Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The best and second best scores under each metric are highlighted in bold and underline. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The generated labeled LiDAR scenes from Spiral and other baseline methods, as shown in Figure 5, demonstrate the superior performance of Spiral in both ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Surprisingly, the more advanced segmentation model SPVCNN++ performs worse than RangeNet++ on the unlabeled scenes generated by LiDARGen [15] and LiDM [16], resulting in ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| As shown in the first row of Table 3, the generated samples from Spiral consistently improve the performance of SPVCNN++ and outperform those from ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| To quantify the effect of the confidence threshold δ, we evaluate the performance 9 | definition/direction/unit from same section | p. 9 (4 Experiments) |
| In the closed-loop mode, Spiral adopts a confidencebased filtering strategy to exclude unreliable semantic maps that frequently occur during the early stages of the ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| However, the performance of Spiral starts to deteriorate when δ < 0.6. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Spiral demonstrates superior inference efficiency compared to LiDM and LiDARGen. | definition/direction/unit from same section | p. 10 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Examples of semantic artifacts are shown in 7○, 8○, 9○, and 11 ○, while geometric artifacts such as local distortion and large noise are ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| For the generative models in two-step baseline methods, including LiDARGen [15], LiDM [16], and R2DM [18], we follow the official training settings. | comparison identity and matched condition | p. 7 (4 Experiments) |
| The generated labeled LiDAR scenes from Spiral and other baseline methods, as shown in Figure 5, demonstrate the superior performance of Spiral in both ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| As shown in the first row of Table 3, the generated samples from Spiral consistently improve the performance of SPVCNN++ and outperform those from ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Spiral demonstrates superior inference efficiency compared to LiDM and LiDARGen. | comparison identity and matched condition | p. 10 (4 Experiments) |
| With fewer sampling steps, Spiral outperforms R2DM [18] using its default setting of NFE = 256, indicated by the dashed line. | comparison identity and matched condition | p. 10 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To quantify the effect of the confidence threshold δ, we evaluate the performance 9 | component/input/data sensitivity | p. 9 (4 Experiments) |
| We attribute this drop to the higher sensitivity of larger models to noise, compounded by the greater noise present in the LiDAR scenes generated ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| Although the performance of SPVCNN++ improves after jittering-based fine-tuning, it still lags behind RangeNet++. | component/input/data sensitivity | p. 7 (4 Experiments) |
| As shown in the second and third rows of Table 3, although Spiral is not fine-tuned for such extreme weather conditions, its generated data ... | component/input/data sensitivity | p. 8 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, the key contributions of this work are as follows: • We propose a novel state-of-the-art semantic-aware range-view LiDAR diffusion model, Spiral, which ... | Despite having the smallest parameter size of only 61M, Spiral achieves the best performance across all semanticaware metrics, outperforming the two-step method, R2DM [18] ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 7 (4 Experiments) |
| Primary metric/result | As shown in the first row of Table 3, the generated samples from Spiral consistently improve the performance of SPVCNN++ and outperform those from ... | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** During pre-processing, the LiDAR scenes are projected into range-view images of spatial resolutions 64×1024 and 32×1024, respectively.
- **p. 7 / 4 Experiments - extractive body cue:** The training process takes ∼36 hours.
- **p. 7 / 4 Experiments - extractive body cue:** We also run LiDM using the DDIM [70] sampling method with 256 steps for fair comparison.
- **p. 7 / 4 Experiments - extractive body cue:** LiDARGen models the denoising process with 232 noise levels and requires 5 steps per level by default, resulting in a total NFE of 1160.
- **p. 10 / 4 Experiments - extractive body cue:** We performed a statistical analysis on 1,000 samples each from SemanticKITTI and nuScenes.
- **p. 10 / 4 Experiments - extractive body cue:** With the default 256 denoising steps, closed-loop inference is activated (i.e., once ≥80% of semantic predictions exceed the confidence threshold) at an average step of ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | With δ = 0.3, the performance of the closed-loop inference even falls behind that of the open-loop inference. | p. 10 (4 Experiments) |
| body limitation/failure cue | To further assess robustness, we also evaluate Spiral-based generative data augmentation on the fog and wet-ground subsets of Robo3D [53], which simulate adverse weather ... | p. 7 (4 Experiments) |
| body limitation/failure cue | For the previous metrics that evaluate only the unlabeled LiDAR scenes, Spiral outperforms R2DM on most metrics, indicating that the additional semantic prediction task ... | p. 7 (4 Experiments) |
| body limitation/failure cue | Unlike the two-step methods, Spiral does not require a segmentation model to generate semantic labels. | p. 10 (4 Experiments) |
| body limitation/failure cue | Additionally, we evaluate SPVCNN++ under the same settings on out-of-distribution subsets, fog and wet-ground, from Robo3D [53]. | p. 8 (4 Experiments) |
| body limitation/failure cue | Examples of semantic artifacts are shown in 7○, 8○, 9○, and 11 ○, while geometric artifacts such as local distortion and large noise are ... | p. 8 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train Spiral on NVIDIA A6000 GPUs with 48 GB VRAM for 300k steps using the Adam optimizer [69] with a learning rate of ... | p. 7 (4 Experiments) |
| Additionally, the inference times per sample for RangeNet++ [32] and SPVCNN++ [57] are 0.08s and 0.05s, respectively, on the same hardware. | p. 10 (4 Experiments) |
| We also run LiDM using the DDIM [70] sampling method with 256 steps for fair comparison. | p. 7 (4 Experiments) |
| On an A6000 GPU, Spiral achieves an average inference speed of 5.7 seconds per sample. | p. 9 (4 Experiments) |
| With fewer sampling steps, Spiral outperforms R2DM [18] using its default setting of NFE = 256, indicated by the dashed line. | p. 10 (4 Experiments) |
| (10) The features from real and generated sets, {f s}r and {f s}g, are used to compute S-FRD, S-FPD, and S-MMD. | p. 11 (A.1 Evaluation on Range View and Cartesian Point Clouds) |
| For the BEV-based evaluation, we first compute the semantic-aware histogram for the real and generated sets, {hs}r and {hs}g, and then compute the BEV-based ... | p. 12 (A.2 Evaluation on Bird's Eye View) |
| Starting from a real sample x0 ∼q(x0), a forward process gradually adds Gaussian noise over T steps, such that the final sample approximates a ... | p. 4 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 4 Experiments - extractive body cue:** With δ = 0.3, the performance of the closed-loop inference even falls behind that of the open-loop inference.
- **p. 7 / 4 Experiments - extractive body cue:** To further assess robustness, we also evaluate Spiral-based generative data augmentation on the fog and wet-ground subsets of Robo3D [53], which simulate adverse weather conditions ...
- **p. 7 / 4 Experiments - extractive body cue:** For the previous metrics that evaluate only the unlabeled LiDAR scenes, Spiral outperforms R2DM on most metrics, indicating that the additional semantic prediction task does ...
- **p. 10 / 4 Experiments - extractive body cue:** Unlike the two-step methods, Spiral does not require a segmentation model to generate semantic labels.
- **p. 8 / 4 Experiments - extractive body cue:** Additionally, we evaluate SPVCNN++ under the same settings on out-of-distribution subsets, fog and wet-ground, from Robo3D [53].
- **p. 8 / 4 Experiments - extractive body cue:** Examples of semantic artifacts are shown in 7○, 8○, 9○, and 11 ○, while geometric artifacts such as local distortion and large noise are illustrated ...

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), metrics p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), baselines p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), results p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
