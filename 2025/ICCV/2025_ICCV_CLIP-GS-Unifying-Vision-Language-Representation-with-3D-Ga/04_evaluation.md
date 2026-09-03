# Evaluation - CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jiao_CLIP-GS_Unifying_Vision-Language_Representation_with_3D_Gaussian_Splatting_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jiao_CLIP-GS_Unifying_Vision-Language_Representation_with_3D_Gaussian_Splatting_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (5.2. Zero-Shot 3D Classification), p. 1 (Figure/Table caption), p. 5 (5.1. Multimodal Retrieval), p. 6 (5.3. Few-Shot 3D Classification), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption)): CLIP-GS demonstrates a comprehensive improvement over existing zero-shot 3D classification models, achieving a performance boost of + 0.8, + 0.5 on Objaverse-GS and ModelNet-GS, respectively.

## Evaluation Body Digest

- **p. 5 / 5.2. Zero-Shot 3D Classification - extractive body cue:** 3 to construct the ModelNet-GS dataset.
- **p. 5 / 5.1. Multimodal Retrieval - extractive body cue:** CLIP-GS performs well when retrieving real-world images.
- **p. 5 / 5.3. Few-Shot 3D Classification - extractive body cue:** In line with [8], we measure performance using Top1 average accuracy and standard deviation, 4674
- **p. 5 / 5.2. Zero-Shot 3D Classification - extractive body cue:** We follow the settings of [25, 63], using Top1, Top3, Top5 average accuracy (%) for evaluations.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Few-shot classification on ModelNet40. We report the 10-shot & 10-way average accuracy (%) and standard de- viation (%) results.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Few-shot classification on Objaverse-GS. We report the average accuracy (%) for 5-shot classification across 5, 10, 20, and 50 ways. * de- notes ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 9. Scaling up model size in CLIP-GS. Top1 accuracy in Objaverse-GS is used for analysis. We explore the effect of scaling up the model ...
- **p. 6 / 5.3. Few-Shot 3D Classification - extractive body cue:** CLIP-GS surpasses previous state-of-the-art point cloud methods, and demonstrates significantly smaller deviations.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Zero-Shot 3D Classification | EMPIRICAL / REAL-ROBOT OR HARDWARE | CLIP-GS demonstrates a comprehensive improvement over existing zero-shot 3D classification models, achieving a performance boost of + 0.8, + 0.5 on Objaverse-GS and ModelNet-GS, ... | p. 5 (5.2. Zero-Shot 3D Classification) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. (a) Comparison between point cloud reconstruction and 3D Gaussian Splatting (3DGS) reconstruction. (b) The 3DGS approach outperforms point cloud methods across multiple ... | p. 1 (Figure/Table caption) |
| 5.1. Multimodal Retrieval | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our CLIP-GS outperforms point cloudbased methods across all retrieval tasks by a large margin. | p. 5 (5.1. Multimodal Retrieval) |
| 5.3. Few-Shot 3D Classification | EMPIRICAL / REAL-ROBOT OR HARDWARE | CLIP-GS consistently outperforms all the other methods under the few-shot settings of Objaverse-GS. | p. 6 (5.3. Few-Shot 3D Classification) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5. Image / text →3D shape retrieval results. Top: we query the most similar or top 2 similar 3D shapes for each text. ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 5.2. Zero-Shot 3D Classification - extractive body cue:** 3 to construct the ModelNet-GS dataset.
- **p. 5 / 5.1. Multimodal Retrieval - extractive body cue:** CLIP-GS performs well when retrieving real-world images.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Comparison between point cloud reconstruction and 3D Gaussian Splatting (3DGS) reconstruction. (b) The 3DGS approach outperforms point cloud methods across multiple 3D ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Statistics of 3DGS Triplets. 3D shapes collection. Our triplet is constructed using Ob- javerse [2] and Objaverse-XL [3], the largest-scale realis- tic 3D ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Overview of the CLIP-GS. Within CLIP-GS, the FPS & kNN is first used to form gaussian patches. Then, we design the GS Tokenizer ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Details of GS refinement block. ploy a contrastive loss function, Ltext: Ltext = -1 2N N X i=1 (Contra(EG
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Multimodal retrieval on Objaverse-GS. For a fair comparison, all methods are trained without Objaverse-LVIS shapes. 3D repr denotes the form of 3D shapes ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Image / text →3D shape retrieval results. Top: we query the most similar or top 2 similar 3D shapes for each text. Bottom: ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Zero-shot classification on Objaverse-GS, and ModelNet-GS. "no LVIS" denotes model is trained without Objaverse-LVIS shapes.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Few-shot classification on ModelNet40. We report the 10-shot & 10-way average accuracy (%) and standard de- viation (%) results.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3 to construct the ModelNet-GS dataset. | embodiment, simulator version and control stack | p. 5 (5.2. Zero-Shot 3D Classification), p. 5 (5.1. Multimodal Retrieval) |
| Task/environment | CLIP-GS performs well when retrieving real-world images. | reset, timeout, object/scene variation | p. 5 (5.1. Multimodal Retrieval) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (4.1. Feature Extraction), p. 7 (Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 8 (Method), p. 4 (4.2. Multi-model Alignment) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In line with [8], we measure performance using Top1 average accuracy and standard deviation, 4674 | definition/direction/unit from same section | p. 5 (5.3. Few-Shot 3D Classification) |
| We follow the settings of [25, 63], using Top1, Top3, Top5 average accuracy (%) for evaluations. | definition/direction/unit from same section | p. 5 (5.2. Zero-Shot 3D Classification) |
| Table 3. Few-shot classification on ModelNet40. We report the 10-shot & 10-way average accuracy (%) and standard de- viation (%) results. | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 4. Few-shot classification on Objaverse-GS. We report the average accuracy (%) for 5-shot classification across 5, 10, 20, and 50 ways. * de- ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 9. Scaling up model size in CLIP-GS. Top1 accuracy in Objaverse-GS is used for analysis. We explore the effect of scaling up the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| CLIP-GS surpasses previous state-of-the-art point cloud methods, and demonstrates significantly smaller deviations. | definition/direction/unit from same section | p. 6 (5.3. Few-Shot 3D Classification) |
| We conduct ablation studies on various choices of designs within our CLIP-GS, and showcase their contributions to the final performance in Tab. | definition/direction/unit from same section | p. 6 (5.4. Ablation Study) |
| Figure 6. Visualization of different order strategies. We project the 3D space onto a 2D plane. Effect of pre-initialized weights. We conduct ablation studies ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Comparisons with state-of-the-art methods. | comparison identity and matched condition | p. 5 (5.1. Multimodal Retrieval) |
| Figure 1. (a) Comparison between point cloud reconstruction and 3D Gaussian Splatting (3DGS) reconstruction. (b) The 3DGS approach outperforms point cloud methods across multiple ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Our CLIP-GS outperforms point cloudbased methods across all retrieval tasks by a large margin. | comparison identity and matched condition | p. 5 (5.1. Multimodal Retrieval) |
| CLIP-GS consistently outperforms all the other methods under the few-shot settings of Objaverse-GS. | comparison identity and matched condition | p. 6 (5.3. Few-Shot 3D Classification) |
| CLIP-GS surpasses previous state-of-the-art point cloud methods, and demonstrates significantly smaller deviations. | comparison identity and matched condition | p. 6 (5.3. Few-Shot 3D Classification) |
| Table 5. Ablation of diverse designs of CLIP-GS. We use the Objaverse-GS for analysis. P&C denotes only P and C attributes of gaussian points ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6. Visualization of different order strategies. We project the 3D space onto a 2D plane. Effect of pre-initialized weights. We conduct ablation studies ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| To understand the effect of each component in the CLIP-GS, we start with the official 4675 | component/input/data sensitivity | p. 6 (5.4. Ablation Study) |
| Furthermore, we perform ablation studies (Sec. | component/input/data sensitivity | p. 5 (5. Experiments) |
| For a fair comparison, all methods are trained without Objaverse-LVIS shapes. | component/input/data sensitivity | p. 6 (5.3. Few-Shot 3D Classification) |
| Table 9. Scaling up model size in CLIP-GS. Top1 accuracy in Objaverse-GS is used for analysis. We explore the effect of scaling up the ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 2. Zero-shot classification on Objaverse-GS, and ModelNet-GS. "no LVIS" denotes model is trained without Objaverse-LVIS shapes. | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, our contributions are summarized as follows: • We propose CLIP-GS, a simple yet effective framework for encoding 3DGS into features, leveraging a contrastive ... | CLIP-GS demonstrates a comprehensive improvement over existing zero-shot 3D classification models, achieving a performance boost of + 0.8, + 0.5 on Objaverse-GS and ModelNet-GS, ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (5.2. Zero-Shot 3D Classification), p. 1 (Figure/Table caption), p. 5 (5.1. Multimodal Retrieval), p. 6 (5.3. Few-Shot 3D Classification), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Figure 1. (a) Comparison between point cloud reconstruction and 3D Gaussian Splatting (3DGS) reconstruction. (b) The 3DGS approach outperforms point cloud methods across multiple ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 5.3. Few-Shot 3D Classification - extractive body cue:** We experiment with m = 10 and n = 10 in ModelNet-GS, and m = 5 and n ∈{5, 10, 20, 50} in Objaverse-GS.
- **p. 5 / 5.3. Few-Shot 3D Classification - extractive body cue:** We do not construct 10-shot experiments on the Objaverse-GS since some classes contain fewer than 10 samples in Objaverse-GS.
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** To align the 3DGS with the text description, we em1×3 conv, s=1 BN & ReLU 1×3 conv, s=1 1×3 conv, s=2 BN & ReLU BN ...
- **p. 7 / Method - extractive body cue:** DGCNN [43] 86.3 ± 6.2 DGCNN + OcCo [41] 86.4 ± 5.4 PointTransformer [61] 84.6 ± 5.5 PointTransformer + OcCo [61] 89.4 ± 5.1 Point-BERT ...
- **p. 8 / Method - extractive body cue:** Iter SH PSNR SSIM storage size optimization time 20,000 3 37.1 98.2 3.6M 108.3s 20,000 0 35.1 97.9 1.0M 104.5s 5,000 3 35.9 98.0

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For a fair comparison, we present the results of Uni3D-Base, a 3D encoder model with ∼88M parameters. | p. 5 (5.2. Zero-Shot 3D Classification) |
| ULIP, OpenShape, and Uni3D train 3D encoders to align the visual-text representation and use point clouds for classification. | p. 5 (5.2. Zero-Shot 3D Classification) |
| Here, position and color attributes (P & C) are extracted and input into a point cloud encoder, as detailed in [63]. | p. 3 (4.1. Feature Extraction) |
| We denote our CLIP-GS as F G, and the text and image encoders in EVA-CLIP as F T and F I, respectively. | p. 4 (4.2. Multi-model Alignment) |
| The normalized embeddings for the sampled triplets ({ ˆ EG i , ˆ ET i , ˆ EI i }N i=1) are computed as: ... | p. 4 (4.2. Multi-model Alignment) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 5 (5.2. Zero-Shot 3D Classification), p. 5 (5.1. Multimodal Retrieval), metrics p. 5 (5.3. Few-Shot 3D Classification), p. 5 (5.2. Zero-Shot 3D Classification), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (5.3. Few-Shot 3D Classification), baselines p. 5 (5.1. Multimodal Retrieval), p. 1 (Figure/Table caption), p. 5 (5.1. Multimodal Retrieval), p. 6 (5.3. Few-Shot 3D Classification), p. 6 (5.3. Few-Shot 3D Classification), p. 7 (Figure/Table caption), results p. 5 (5.2. Zero-Shot 3D Classification), p. 1 (Figure/Table caption), p. 5 (5.1. Multimodal Retrieval), p. 6 (5.3. Few-Shot 3D Classification), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
