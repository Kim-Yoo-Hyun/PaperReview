# Evaluation - LangSplat: 3D Language Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Results on the LERF dataset), p. 7 (4.3. Results on the 3D-OVS dataset), p. 7 (4.2. Results on the LERF dataset), p. 8 (4.3. Results on the 3D-OVS dataset), p. 6 (4.1. Settings), p. 4 (Figure/Table caption)): We observe that our method achieves an overall accuracy of 84.3%, significantly outperforming LERF.

## Evaluation Body Digest

- **p. 6 / 4.1. Settings - extractive PDF cue:** The LERF dataset [18] is captured using the iPhone App Polycam, which consists of complex in-the-wild scenes.
- **p. 6 / 4.1. Settings - extractive PDF cue:** The LERF dataset is designed for 3D object localization tasks, here we extend the LERF dataset by annotating ground truth masks for textual queries, enabling ...
- **p. 7 / 4.2. Results on the LERF dataset - extractive PDF cue:** Ablations result on the bench scene of the 3D-OVS dataset.
- **p. 8 / 4.3. Results on the 3D-OVS dataset - extractive PDF cue:** Note that in this dataset, we generate object masks only based on the query text while others, such as 3D-OVS, require the complete category list.
- **p. 7 / 4.3. Results on the 3D-OVS dataset - extractive PDF cue:** We compare LangSplat with other 2D and 3D state-of-the-art methods on the 3D-OVS dataset in Table 5.
- **p. 8 / 4.3. Results on the 3D-OVS dataset - extractive PDF cue:** We visualize the segmentation results in 2 scenes.
- **p. 6 / 4.1. Settings - extractive PDF cue:** We report the average IoU scores (%). iterations.
- **p. 6 / 4.1. Settings - extractive PDF cue:** We report localization accuracy for the 3D object localization task following LERF [18], and report the IoU results for the 3D semantic segmentation task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.2. Results on the LERF dataset (p. 6); 4.3. Results on the 3D-OVS dataset (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Results on the LERF dataset | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe that our method achieves an overall accuracy of 84.3%, significantly outperforming LERF. | p. 6 (4.2. Results on the LERF dataset) |
| 4.3. Results on the 3D-OVS dataset | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe that LangSplat not only outperforms 2D-based methods such as ODISE [46] and OV-Seg [23], but also achieves better results than 3D-based methods ... | p. 7 (4.3. Results on the 3D-OVS dataset) |
| 4.2. Results on the LERF dataset | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the end, our LangSplat achieved a 119 × speedup over LERF while significantly surpassing LERF in terms of accuracy. | p. 7 (4.2. Results on the LERF dataset) |
| 4.3. Results on the 3D-OVS dataset | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the end, our method achieves an overall mIoU of 93.4%, which shows that LangSplat effectively learns a precise 3D language field. | p. 8 (4.3. Results on the 3D-OVS dataset) |
| 4.1. Settings | EMPIRICAL / SOURCE-REPORTED EVALUATION | We report localization accuracy for the 3D object localization task following LERF [18], and report the IoU results for the 3D semantic segmentation task. | p. 6 (4.1. Settings) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Settings - extractive PDF cue:** The LERF dataset [18] is captured using the iPhone App Polycam, which consists of complex in-the-wild scenes.
- **p. 6 / 4.1. Settings - extractive PDF cue:** The LERF dataset is designed for 3D object localization tasks, here we extend the LERF dataset by annotating ground truth masks for textual queries, enabling ...
- **p. 7 / 4.2. Results on the LERF dataset - extractive PDF cue:** Ablations result on the bench scene of the 3D-OVS dataset.
- **p. 8 / 4.3. Results on the 3D-OVS dataset - extractive PDF cue:** Note that in this dataset, we generate object masks only based on the query text while others, such as 3D-OVS, require the complete category list.
- **p. 7 / 4.3. Results on the 3D-OVS dataset - extractive PDF cue:** We compare LangSplat with other 2D and 3D state-of-the-art methods on the 3D-OVS dataset in Table 5.
- **p. 8 / 4.3. Results on the 3D-OVS dataset - extractive PDF cue:** We visualize the segmentation results in 2 scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Visualization of learned 3D language features of the previous SOTA method LERF and our LangSplat. While LERF generates imprecise and vague 3D features, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The framework of our LangSplat. Our LangSplat leverages SAM to learn hierarchical semantics to address the point ambiguity issue. Then segment masks are ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Localization accuracy (%) comparisons on LERF dataset. Test Scene LSeg [21] LERF [18] LangSplat ramen 7.0 28.2
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative comparisons of 3D semantic segmentation on the LERF dataset. We report the average IoU scores (%). iterations. Our autoencoder is implemented by ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative comparisons of open-vocabulary 3D object localization on the LERF dataset. The red points are the model predictions and the black dashed bounding ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparisons of open-vocabulary 3D semantic segmentation on the LERF dataset. Component Performance AE 3D-GS SAM IoU (%) Speed (s/q)
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablations. The results are obtained on the ramen scene. Component Performance AE 3D-GS SAM mIoU (%) Speed (s/q)
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Ablations result on the bench scene of the 3D-OVS dataset. The image resolution is 1440 × 1080. our baseline equals LERF, which has ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The LERF dataset [18] is captured using the iPhone App Polycam, which consists of complex in-the-wild scenes. | embodiment, simulator version and control stack | p. 6 (4.1. Settings), p. 6 (4.1. Settings) |
| Task/environment | The LERF dataset is designed for 3D object localization tasks, here we extend the LERF dataset by annotating ground truth masks for textual queries, ... | reset, timeout, object/scene variation | p. 6 (4.1. Settings), p. 7 (4.2. Results on the LERF dataset) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Revisiting the Challenges of Language Fields), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Revisiting the Challenges of Language Fields), p. 4 (3.1. Revisiting the Challenges of Language Fields) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the average IoU scores (%). iterations. | definition/direction/unit from same section | p. 6 (4.1. Settings) |
| We report localization accuracy for the 3D object localization task following LERF [18], and report the IoU results for the 3D semantic segmentation task. | definition/direction/unit from same section | p. 6 (4.1. Settings) |
| Component Performance AE 3D-GS SAM IoU (%) Speed (s/q) 28.20 30.93 ! | definition/direction/unit from same section | p. 7 (4.2. Results on the LERF dataset) |
| Using SAM to replace the scale-based solution significantly increases the IoU by 18.54%, showing our SAM-based solution effectively addresses the point ambiguity issue, leading ... | definition/direction/unit from same section | p. 7 (4.2. Results on the LERF dataset) |
| We report the mIoU scores (%). cluding LERF [18] and 3D-OVS [24] by a large margin. | definition/direction/unit from same section | p. 8 (4.3. Results on the 3D-OVS dataset) |
| We observe that our method gives the most accurate segmentation maps. | definition/direction/unit from same section | p. 8 (4.3. Results on the 3D-OVS dataset) |
| Figure 1. Visualization of learned 3D language features of the previous SOTA method LERF and our LangSplat. While LERF generates imprecise and vague 3D ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We observe that our method achieves an overall accuracy of 84.3%, significantly outperforming LERF. | comparison identity and matched condition | p. 6 (4.2. Results on the LERF dataset) |
| We observe that the activation regions generated by LERF are more dispersed, while ours are more concentrated, and our activation regions can better align ... | comparison identity and matched condition | p. 6 (4.2. Results on the LERF dataset) |
| We compare LangSplat with other 2D and 3D state-of-the-art methods on the 3D-OVS dataset in Table 5. | comparison identity and matched condition | p. 7 (4.3. Results on the 3D-OVS dataset) |
| The image resolution is 1440 × 1080. our baseline equals LERF, which has a speed of 30.93 seconds per text query at the resolution ... | comparison identity and matched condition | p. 7 (4.2. Results on the LERF dataset) |
| Among all state-of-the-art methods, our methods give the most accurate segmentation maps, which further demonstrates the effectiveness of our LangSplat. | comparison identity and matched condition | p. 8 (4.3. Results on the 3D-OVS dataset) |
| Qualitative comparisons of different methods on the 3D-OVS dataset. | comparison identity and matched condition | p. 8 (4.3. Results on the 3D-OVS dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4. Ablations result on the bench scene of the 3D-OVS dataset. The image resolution is 1440 × 1080. our baseline equals LERF, which ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Without any of our proposed components, 20056 | component/input/data sensitivity | p. 6 (4.2. Results on the LERF dataset) |
| We conduct ablations on the ramen scene and report the semantic segmentation results in Table 3. | component/input/data sensitivity | p. 6 (4.2. Results on the LERF dataset) |
| We further conducted the ablations on the 3D-OVS dataset, which has a higher image resolution of 1440×1080. | component/input/data sensitivity | p. 7 (4.2. Results on the LERF dataset) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| A scenespecific autoencoder is further introduced to alleviate the memory cost issue imposed by explicit modeling. • We propose to learn the hierarchical semantics ... | We observe that our method achieves an overall accuracy of 84.3%, significantly outperforming LERF. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Results on the LERF dataset), p. 7 (4.3. Results on the 3D-OVS dataset), p. 7 (4.2. Results on the LERF dataset), p. 8 (4.3. Results on the 3D-OVS dataset), p. 6 (4.1. Settings), p. 4 (Figure/Table caption) |
| Primary metric/result | We observe that LangSplat not only outperforms 2D-based methods such as ODISE [46] and OV-Seg [23], but also achieves better results than 3D-based methods ... | numeric claim only at cited anchor | p. 7 (4.3. Results on the 3D-OVS dataset) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Settings - extractive PDF cue:** We train it for 30,000 iterations, and in the end, each scene comprises around 2,500,000 points.
- **p. 6 / 4.1. Settings - extractive PDF cue:** For a 1440 × 1080 resolution scene, our model is trained for ∼25 minutes on an NVIDIA RTX-3090 GPU and takes roughly 4GB of memory.
- **p. 6 / 4.2. Results on the LERF dataset - extractive PDF cue:** We test the query speed on an NVIDIA RTX-3090 GPU.
- **p. 7 / 4.2. Results on the LERF dataset - extractive PDF cue:** We further conducted the ablations on the 3D-OVS dataset, which has a higher image resolution of 1440×1080.
- **p. 7 / 4.2. Results on the LERF dataset - extractive PDF cue:** We also tested the query speed on an NVIDIA RTX-3090 GPU.
- **p. 7 / 4.2. Results on the LERF dataset - extractive PDF cue:** We could replace the decoder with a 1×1 convolutional layer to attain a higher speedup.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. The framework of our LangSplat. Our LangSplat leverages SAM to learn hierarchical semantics to address the point ambiguity issue. Then segment masks ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | As LERF suffers from the patchy issue and learns over-smoothed features, it fails to find accurate object boundaries. | p. 8 (4.3. Results on the 3D-OVS dataset) |
| body limitation/failure cue | We see that the LERF learned features fail to generate clear boundaries between objects while our method gives precise object shapes solely using CLIP ... | p. 6 (4.2. Results on the LERF dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We test the query speed on an NVIDIA RTX-3090 GPU. | p. 6 (4.2. Results on the LERF dataset) |
| Here AE represents autoencoder and 3D-GS denotes 3D Gaussian Splatting. | p. 6 (4.2. Results on the LERF dataset) |
| We could replace the decoder with a 1×1 convolutional layer to attain a higher speedup. | p. 7 (4.2. Results on the LERF dataset) |
| Our further study shows that most of the computational time is allocated to the decoder rather than the rendering process. | p. 7 (4.2. Results on the LERF dataset) |
| Most existing methods [18, 24, 35] employ the CLIP image encoder V to extract image features and utilize the extracted CLIP embeddings to supervise ... | p. 3 (3.1. Revisiting the Challenges of Language Fields) |
| We learn an autoencoder with these obtained CLIP embeddings. | p. 4 (3.1. Revisiting the Challenges of Language Fields) |
| Then segment masks are sent to the CLIP image encoder to extract the corresponding CLIP embeddings. | p. 4 (3.1. Revisiting the Challenges of Language Fields) |
| To reduce memory cost and improve efficiency, we introduce a scenewise language autoencoder. | p. 5 (3.3. 3D Gaussian Splatting for Language Fields) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The framework of our LangSplat. Our LangSplat leverages SAM to learn hierarchical semantics to address the point ambiguity issue. Then segment masks are ...
- **p. 8 / 4.3. Results on the 3D-OVS dataset - extractive PDF cue:** As LERF suffers from the patchy issue and learns over-smoothed features, it fails to find accurate object boundaries.
- **p. 6 / 4.2. Results on the LERF dataset - extractive PDF cue:** We see that the LERF learned features fail to generate clear boundaries between objects while our method gives precise object shapes solely using CLIP features.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Settings), p. 6 (4.1. Settings), p. 7 (4.2. Results on the LERF dataset), p. 8 (4.3. Results on the 3D-OVS dataset), p. 7 (4.3. Results on the 3D-OVS dataset), p. 8 (4.3. Results on the 3D-OVS dataset), metrics p. 6 (4.1. Settings), p. 6 (4.1. Settings), p. 7 (4.2. Results on the LERF dataset), p. 7 (4.2. Results on the LERF dataset), p. 8 (4.3. Results on the 3D-OVS dataset), p. 8 (4.3. Results on the 3D-OVS dataset), baselines p. 6 (4.2. Results on the LERF dataset), p. 6 (4.2. Results on the LERF dataset), p. 7 (4.3. Results on the 3D-OVS dataset), p. 7 (4.2. Results on the LERF dataset), p. 8 (4.3. Results on the 3D-OVS dataset), p. 8 (4.3. Results on the 3D-OVS dataset), results p. 6 (4.2. Results on the LERF dataset), p. 7 (4.3. Results on the 3D-OVS dataset), p. 7 (4.2. Results on the LERF dataset), p. 8 (4.3. Results on the 3D-OVS dataset), p. 6 (4.1. Settings), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
