# Evaluation - 3D Vision-Language Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SSE9myD9SG; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114008. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2 RESULTS), p. 14 (A.2.2 QUALITATIVE RESULTS), p. 8 (4.2 RESULTS), p. 14 (A.2.1 QUANTITATIVE RESULTS), p. 23 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION), p. 23 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION)): Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 in mIoU on the LERF dataset.

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** (1) LERF dataset (Kerr et al., 2023), captured using the Polycam application on an iPhone, comprises complex, in-the-wild scenes and is specifically tailored for 3D ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** (3) Mip-NeRF 360 dataset (Barron et al., 2022) contains 9 scenes, each composed of a complex central object or area and a detailed background.
- **p. 8 / 4.2 RESULTS - extractive body cue:** Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 in mIoU on ...
- **p. 20 / A.5.1 EXTENDED RESULTS ON 3D-OVS SCENES - extractive body cue:** In the main manuscript, we considered the five main scenes of the 3D-OVS dataset, following the protocol adopted in LangSplat Qin et al.
- **p. 9 / 4.2 RESULTS - extractive body cue:** RGB LEGaussians LangSplat GOI Ours Ground Truth 'doll' 'egg tart' 'cat' 'wall' 'mini car' 'grape' Figure 7: Qualitative semantic segmentation comparisons on the bench scene ...
- **p. 9 / 4.2 RESULTS - extractive body cue:** RGB LEGaussians LangSplat GOI Ours Ground Truth 'Switch controller' 'Pikachu' 'Gundam' 'card' 'sofa' 'Xbox controller' Figure 8: Qualitative semantic segmentation comparisons on the sofa scene ...
- **p. 23 / A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION - extractive body cue:** Semantic Indicator? non-translucent and non-reflective object categories translucent/reflective objects bear cookie bag sheep apple napkin bear nose cookies coffee hooves brand pouf coffee mug plate ...
- **p. 23 / A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION - extractive body cue:** Semantic Indicator? non-translucent and non-reflective object categories object categories with translucent/reflective parts chopsticks egg nori napkin noodles kamaboko onion segments corn bowl sake cup plate ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); 4.2 RESULTS (p. 7); A.1 FURTHER IMPLEMENTATION DETAILS (p. 13); A.2 EVALUATION ON ADDITIONAL MIP-NERF 360 DATASET (p. 14); A.2.1 QUANTITATIVE RESULTS (p. 14); A.2.2 QUALITATIVE RESULTS (p. 14); A.4 ADDITIONAL QUALITATIVE RESULTS (p. 18); A.4.1 RESULTS ON LERF DATA (p. 18); A.4.2 RESULTS ON 3D-OVS DATA (p. 18); A.5 ADDITIONAL QUANTITATIVE RESULTS (p. 20); A.5.1 EXTENDED RESULTS ON 3D-OVS SCENES (p. 20); A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION (p. 21).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 in mIoU ... | p. 8 (4.2 RESULTS) |
| A.2.2 QUALITATIVE RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results demonstrate that our proposed method significantly outperforms the competing approaches. | p. 14 (A.2.2 QUALITATIVE RESULTS) |
| 4.2 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results indicate that both Slerp-based rotation blending and Lerp-based translation blending contribute to performance improvements. | p. 8 (4.2 RESULTS) |
| A.2.1 QUANTITATIVE RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 8, clearly demonstrate the effectiveness of our proposed method, highlighting its ability to improve overall performance on this dataset. | p. 14 (A.2.1 QUANTITATIVE RESULTS) |
| A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Semantic Indicator? non-translucent and non-reflective object categories translucent/reflective objects bear cookie bag sheep apple napkin bear nose cookies coffee hooves brand pouf coffee mug ... | p. 23 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** (1) LERF dataset (Kerr et al., 2023), captured using the Polycam application on an iPhone, comprises complex, in-the-wild scenes and is specifically tailored for 3D ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** (3) Mip-NeRF 360 dataset (Barron et al., 2022) contains 9 scenes, each composed of a complex central object or area and a detailed background.
- **p. 8 / 4.2 RESULTS - extractive body cue:** Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 in mIoU on ...
- **p. 20 / A.5.1 EXTENDED RESULTS ON 3D-OVS SCENES - extractive body cue:** In the main manuscript, we considered the five main scenes of the 3D-OVS dataset, following the protocol adopted in LangSplat Qin et al.
- **p. 9 / 4.2 RESULTS - extractive body cue:** RGB LEGaussians LangSplat GOI Ours Ground Truth 'doll' 'egg tart' 'cat' 'wall' 'mini car' 'grape' Figure 7: Qualitative semantic segmentation comparisons on the bench scene ...
- **p. 9 / 4.2 RESULTS - extractive body cue:** RGB LEGaussians LangSplat GOI Ours Ground Truth 'Switch controller' 'Pikachu' 'Gundam' 'card' 'sofa' 'Xbox controller' Figure 8: Qualitative semantic segmentation comparisons on the sofa scene ...
- **p. 23 / A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION - extractive body cue:** Semantic Indicator? non-translucent and non-reflective object categories translucent/reflective objects bear cookie bag sheep apple napkin bear nose cookies coffee hooves brand pouf coffee mug plate ...
- **p. 23 / A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION - extractive body cue:** Semantic Indicator? non-translucent and non-reflective object categories object categories with translucent/reflective parts chopsticks egg nori napkin noodles kamaboko onion segments corn bowl sake cup plate ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Comparison of prior semantic 3DGS work and our novel method. We apply cross-modal rasterization and camera-view-based regularization for better explo- ration of semantic ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our proposed framework. A) We propose a novel multi-modal Gaussian splatting model; B) we enrich the input images and poses for ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Empirical differences between color opacity and proposed smoothed semantic indicator. On the left, we visualize the difference li -oi in Gaussians modeling the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative semantic segmentation comparisons on the ramen scene (LERF dataset). RGB LEGaussians LangSplat GOI Ours Ground Truth 'knife'
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative semantic segmentation comparisons on the kitchen scene (LERF dataset). semi-transparent or reflective objects (e.g., glass and pot in depicted scene), exhibiting low ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: mIoU results on the LERF dataset.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Localization accuracy (%) on the LERF dataset.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: mIoU results on the 3D-OVS dataset.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (1) LERF dataset (Kerr et al., 2023), captured using the Polycam application on an iPhone, comprises complex, in-the-wild scenes and is specifically tailored for ... | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Task/environment | (3) Mip-NeRF 360 dataset (Barron et al., 2022) contains 9 scenes, each composed of a complex central object or area and a detailed background. | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENTS), p. 8 (4.2 RESULTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 4 (3 METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The goal is to verify that, while this work focuses on semantic accuracy, our solution does not sacrifice visual precision too much. | definition/direction/unit from same section | p. 21 (A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION) |
| We report the mean Intersection over Union (mIoU) results, alongside localization accuracy results in accordance with (Qin et al., 2024) (2) 3D-OVS dataset (Liu ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| 2 present the mIoU and localization accuracy results on the LERF dataset, respectively. | definition/direction/unit from same section | p. 8 (4.2 RESULTS) |
| There, we highlight how re-using the opacity o (optimized w.r.t. the color modality) to rasterize language maps-i.e., entangling visual properties and 2D language projections-can ... | definition/direction/unit from same section | p. 21 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION) |
| Table 17: Ablation results on different levels of disentanglement between the per-modality Gaussian parameters, evaluated on the downstream open-vocabulary semantic-segmentation task on LERF. Parameters ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| We attribute this performance to our cooperative training over augmented view/pose batches, and to the increased ability of the Gaussians to accurately fit both ... | definition/direction/unit from same section | p. 10 (4.2 RESULTS) |
| 8, clearly demonstrate the effectiveness of our proposed method, highlighting its ability to improve overall performance on this dataset. | definition/direction/unit from same section | p. 14 (A.2.1 QUANTITATIVE RESULTS) |
| Our proposed method demonstrates superior performance compared to other approaches, showing greater alignment with the ground truth. | definition/direction/unit from same section | p. 18 (A.4.2 RESULTS ON 3D-OVS DATA) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 in mIoU ... | comparison identity and matched condition | p. 8 (4.2 RESULTS) |
| 6, our model outperforms the other four baselines in efficiency. | comparison identity and matched condition | p. 10 (4.2 RESULTS) |
| To facilitate qualitative comparisons, we contrast our method with several baseline approaches, including LEGaussian (Shi et al., 2024), LangSplat (Qin et al., 2024), and ... | comparison identity and matched condition | p. 8 (4.2 RESULTS) |
| The results demonstrate that our proposed method significantly outperforms the competing approaches. | comparison identity and matched condition | p. 14 (A.2.2 QUALITATIVE RESULTS) |
| Our proposed method demonstrates superior performance compared to other approaches, showing greater alignment with the ground truth. | comparison identity and matched condition | p. 18 (A.4.2 RESULTS ON 3D-OVS DATA) |
| Our proposed method clearly outperforms other approaches, particularly in reflective and translucent areas, where it more closely aligns with the ground truth. | comparison identity and matched condition | p. 18 (A.4.1 RESULTS ON LERF DATA) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.3 ABLATION STUDIES Ablation on cross-modal rasterizer. | component/input/data sensitivity | p. 8 (4.2 RESULTS) |
| 4.C, we present an ablation study on the interpolation ratio k. | component/input/data sensitivity | p. 8 (4.2 RESULTS) |
| (A) Fusion module No Fusion 57.8 69.6 54.2 51.5 58.3 Single-layer MLP Fusion 55.9 68.2 53.0 49.9 56.8 Cross-attention Modality Fusion 57.3 70.7 54.6 ... | component/input/data sensitivity | p. 10 (4.2 RESULTS) |
| Table 5: Ablation results of Camera View Blending on the LERF dataset, in terms of mIoU. Rotation Translation SSIM ramen teatime figurines kitchen | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Figure 11: Qualitative semantic segmentation comparisons on the room scene of Mip-NeRF 360. A.3 ADDITIONAL ABLATION STUDIES A.3.1 HIGH-LEVEL ABLATION OF PROPOSED CONTRIBUTIONS. We ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 10: Ablation results of three key contributions on the 3D-OVS dataset, in terms of mIoU. modal. fus. sem. indic. view blend. bed bench ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Besides, we introduce a language-specific parameter that enables the meaningful blending of language features from different Gaussians. | Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 in mIoU ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2 RESULTS), p. 14 (A.2.2 QUALITATIVE RESULTS), p. 8 (4.2 RESULTS), p. 14 (A.2.1 QUANTITATIVE RESULTS), p. 23 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION), p. 23 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION) |
| Primary metric/result | The results demonstrate that our proposed method significantly outperforms the competing approaches. | numeric claim only at cited anchor | p. 14 (A.2.2 QUALITATIVE RESULTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** (3) Mip-NeRF 360 dataset (Barron et al., 2022) contains 9 scenes, each composed of a complex central object or area and a detailed background.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, this new attribute cannot be naively fixed, e.g., to 1 or 0.5 for all Gaussians. | p. 8 (4.2 RESULTS) |
| body limitation/failure cue | It is important to note that FMGS (Zuo et al., 2024) does not report mIoU results on the LERF dataset and is also not ... | p. 8 (4.2 RESULTS) |
| body limitation/failure cue | The goal is to verify that, while this work focuses on semantic accuracy, our solution does not sacrifice visual precision too much. | p. 21 (A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION) |
| body limitation/failure cue | Moreover, comparing to the results from color-only 3DGS (same as LangSplat as this method fixes all 3DGS parameters after its pre-training), we observe that ... | p. 21 (A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each scene, our model is trained for 15,000 iterations using an Adam optimizer (Kingma, 2014), and the learning rates of different components are ... | p. 7 (4 EXPERIMENTS) |
| Method Training Time ↓ FPS ↑ # of Gaussians ↓ LangSplat 96min 40 86k GS-Grouping 130min 76 107k GOI 73min 42 92k Ours 65min ... | p. 10 (4.2 RESULTS) |
| The learning rates applied to the different 3DGS attributes are provided in Tab. | p. 13 (A.1 FURTHER IMPLEMENTATION DETAILS) |
| Components Learning Rates position 1.6 × 10-4 scale 5.0 × 10-3 rotation 1.0 × 10-3 color features 5.0 × 10-3 color opacity 5.0 × ... | p. 13 (A.1 FURTHER IMPLEMENTATION DETAILS) |
| 19-22, our proposed method consistently outperforms others in terms of the training time, FPS, number of Gaussians, and storage size. | p. 21 (A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION) |
| Method Training Time ↓ FPS ↑ Gaussians # ↓ Storage Size ↓ PSNR ↑ LangSplat 121min 38 94k 190MB 27.9 GS-Grouping 130min 65 116k ... | p. 21 (A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION) |
| Method Training Time ↓ FPS ↑ Gaussians # ↓ Storage Size ↓ PSNR ↑ LangSplat 105min 43 142k 406MB 32.4 GS-Grouping 141min 77 177k ... | p. 22 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION) |
| The implementation of semantic opacity is done in CUDA and C++, while the other components are in PyTorch. | p. 7 (4 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.2 RESULTS - extractive body cue:** However, this new attribute cannot be naively fixed, e.g., to 1 or 0.5 for all Gaussians.
- **p. 8 / 4.2 RESULTS - extractive body cue:** It is important to note that FMGS (Zuo et al., 2024) does not report mIoU results on the LERF dataset and is also not open-sourced, ...
- **p. 21 / A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION - extractive body cue:** The goal is to verify that, while this work focuses on semantic accuracy, our solution does not sacrifice visual precision too much.
- **p. 21 / A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION - extractive body cue:** Moreover, comparing to the results from color-only 3DGS (same as LangSplat as this method fixes all 3DGS parameters after its pre-training), we observe that semantic ...

- **Evidence anchors reviewed:** datasets p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4.2 RESULTS), p. 20 (A.5.1 EXTENDED RESULTS ON 3D-OVS SCENES), p. 9 (4.2 RESULTS), p. 9 (4.2 RESULTS), metrics p. 21 (A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION), p. 7 (4 EXPERIMENTS), p. 8 (4.2 RESULTS), p. 21 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION), p. 17 (Figure/Table caption), p. 10 (4.2 RESULTS), baselines p. 8 (4.2 RESULTS), p. 10 (4.2 RESULTS), p. 8 (4.2 RESULTS), p. 14 (A.2.2 QUALITATIVE RESULTS), p. 18 (A.4.2 RESULTS ON 3D-OVS DATA), p. 18 (A.4.1 RESULTS ON LERF DATA), results p. 8 (4.2 RESULTS), p. 14 (A.2.2 QUALITATIVE RESULTS), p. 8 (4.2 RESULTS), p. 14 (A.2.1 QUANTITATIVE RESULTS), p. 23 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION), p. 23 (A.5.3 PER-CATEGORY EVALUATION OF SEMANTIC INDICATOR CONTRIBUTION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
