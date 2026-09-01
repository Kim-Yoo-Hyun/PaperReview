# Evaluation - Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Shi_Language_Embedded_3D_Gaussians_for_Open-Vocabulary_Scene_Understanding_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Shi_Language_Embedded_3D_Gaussians_for_Open-Vocabulary_Scene_Understanding_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (5.2. Comparisons), p. 7 (5.2. Comparisons), p. 4 (Figure/Table caption), p. 6 (5.2. Comparisons)): Figure 5. Images of various open-vocabulary queries. ner effectively diminishes ambiguity and enhances the mean average precision (mAP) metric. Furthermore, integrating DINO features significantly improves the definition of ob- ject ...

## Evaluation Body Digest

- **p. 6 / 5.1. Basic Setups - extractive PDF cue:** For a simultaneous evaluation of visual and semantic embedding quality, we select six scenes (excluding Stump) from the Mip-NeRF360 dataset [3] and manually annotate segmentation ...
- **p. 6 / 5.2. Comparisons - extractive PDF cue:** Moreover, due to predetermined query categories during training, 3DOVS [26] shows poor performance in scenes with complex objects.
- **p. 7 / 5.3. Open-vocabulary Query - extractive PDF cue:** We use a diverse range of vocabulary categories to identify objects in scenes, such as visual attribute terms like "green", and subjective adjectives like "cute".
- **p. 7 / 5.2. Comparisons - extractive PDF cue:** In contrast, our use of the quantization scheme facilitates the incorporation of detailed semantics into complex 3D scenes with numerous 3D Gaussians, and concurrently achieves ...
- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** Furthermore, integrating DINO features significantly improves the definition of object query boundaries.
- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** The load balancing loss, introduced during the quantization phase, results in a more utilized discrete feature space, facilitating the distinguish of objects with similar semantics, ...
- **p. 6 / 5.1. Basic Setups - extractive PDF cue:** For the accuracy of language embedding, we measure the mean intersection over union (mIoU), mean pixel accuracy (mPA), mean precision (mP), and mean average precision ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary querying. The top row visualizes the original image, novel view synthesis ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Implementation Details (p. 5); 5. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5. Images of various open-vocabulary queries. ner effectively diminishes ambiguity and enhances the mean average precision (mAP) metric. Furthermore, integrating DINO features significantly ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. We present Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary querying. The top row visualizes the original image, novel view ... | p. 1 (Figure/Table caption) |
| 5.2. Comparisons | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our approach outperforms others in ren5338 | p. 6 (5.2. Comparisons) |
| 5.2. Comparisons | SYSTEM / EVALUATION SCOPE UNRESOLVED | In contrast, our use of the quantization scheme facilitates the incorporation of detailed semantics into complex 3D scenes with numerous 3D Gaussians, and concurrently ... | p. 7 (5.2. Comparisons) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2. The training process for Language-embedded 3D Gaussians starts with initializing scenes following 3D Gaussian Splatting [20] and randomly initializing semantic features and ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Basic Setups - extractive PDF cue:** For a simultaneous evaluation of visual and semantic embedding quality, we select six scenes (excluding Stump) from the Mip-NeRF360 dataset [3] and manually annotate segmentation ...
- **p. 6 / 5.2. Comparisons - extractive PDF cue:** Moreover, due to predetermined query categories during training, 3DOVS [26] shows poor performance in scenes with complex objects.
- **p. 7 / 5.3. Open-vocabulary Query - extractive PDF cue:** We use a diverse range of vocabulary categories to identify objects in scenes, such as visual attribute terms like "green", and subjective adjectives like "cute".
- **p. 7 / 5.2. Comparisons - extractive PDF cue:** In contrast, our use of the quantization scheme facilitates the incorporation of detailed semantics into complex 3D scenes with numerous 3D Gaussians, and concurrently achieves ...
- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** Furthermore, integrating DINO features significantly improves the definition of object query boundaries.
- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** The load balancing loss, introduced during the quantization phase, results in a more utilized discrete feature space, facilitating the distinguish of objects with similar semantics, ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary querying. The top row visualizes the original image, novel view synthesis ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The training process for Language-embedded 3D Gaussians starts with initializing scenes following 3D Gaussian Splatting [20] and randomly initializing semantic features and setting ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison of our method with DFF [22], LeRF [21], 3DOVS [26]. mPA↑ mP↑ mIoU↑ mAP↑ Quantization w/o DINO 0.927
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative results of ablation experiments. optimizes the scene's geometry and appearance with the same RGB loss following 3D Gaussian Splatting and en- ables ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Comparison of novel view synthesis and query relevance visualization. Left to right: Ground truth novel view synthesis, novel view images with relevance visualization ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6. The results show that embedding uncertainty with- out spatial smoothing of semantic features leads to subop- timal optimization. Conversely, using MLP solely for ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Visual quality comparison of novel view synthesis re- sults. Our method is able to recover more detailed geometry and appearance compared to other ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Images of various open-vocabulary queries. ner effectively diminishes ambiguity and enhances the mean average precision (mAP) metric. Furthermore, integrating DINO features significantly improves ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For a simultaneous evaluation of visual and semantic embedding quality, we select six scenes (excluding Stump) from the Mip-NeRF360 dataset [3] and manually annotate ... | embodiment, simulator version and control stack | p. 6 (5.1. Basic Setups), p. 6 (5.2. Comparisons) |
| Task/environment | Moreover, due to predetermined query categories during training, 3DOVS [26] shows poor performance in scenes with complex objects. | reset, timeout, object/scene variation | p. 6 (5.2. Comparisons), p. 7 (5.3. Open-vocabulary Query) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.4. Language Embedded 3D Gaussians), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For the accuracy of language embedding, we measure the mean intersection over union (mIoU), mean pixel accuracy (mPA), mean precision (mP), and mean average ... | definition/direction/unit from same section | p. 6 (5.1. Basic Setups) |
| Figure 5. Images of various open-vocabulary queries. ner effectively diminishes ambiguity and enhances the mean average precision (mAP) metric. Furthermore, integrating DINO features significantly ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. We present Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary querying. The top row visualizes the original image, novel view ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Our approach notably delivers the highest visual rendering quality and query accuracy across all the tested scenes. | definition/direction/unit from same section | p. 6 (5.2. Comparisons) |
| Top to bottom: Query words "asphalt ground", "bicycle", "jar of coconut oil", "flower", "LEGO Technic 856 Bulldozer", and "brown shoes". dering quality and semantic ... | definition/direction/unit from same section | p. 7 (5.2. Comparisons) |
| We demonstrate the results of ablation studies in Tab. | definition/direction/unit from same section | p. 7 (5.4. Ablation Study) |
| Figure 2. The training process for Language-embedded 3D Gaussians starts with initializing scenes following 3D Gaussian Splatting [20] and randomly initializing semantic features and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| We implement our method using PyTorch [34], and incorporate the CUDA kernel from 3D Gaussian Splatting [20] to speed up the rasterization rendering process. | definition/direction/unit from same section | p. 5 (4. Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our approach outperforms others in ren5338 | comparison identity and matched condition | p. 6 (5.2. Comparisons) |
| In contrast, our use of the quantization scheme facilitates the incorporation of detailed semantics into complex 3D scenes with numerous 3D Gaussians, and concurrently ... | comparison identity and matched condition | p. 7 (5.2. Comparisons) |
| Our method is able to recover more detailed geometry and appearance compared to other methods. "green" "grass" "lego" "engine" "sheep toy" "cute" Figure 5. | comparison identity and matched condition | p. 8 (5.4. Ablation Study) |
| Comparison of ablation experiments. | comparison identity and matched condition | p. 8 (5.4. Ablation Study) |
| 1 presents a comparison across various metrics, including novel view synthesis quality, open-vocabulary query accuracy, and computational efficiency. | comparison identity and matched condition | p. 6 (5.2. Comparisons) |
| We demonstrate the results of ablation studies in Tab. | comparison identity and matched condition | p. 7 (5.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We demonstrate the results of ablation studies in Tab. | component/input/data sensitivity | p. 7 (5.4. Ablation Study) |
| The results show that embedding uncertainty without spatial smoothing of semantic features leads to suboptimal optimization. | component/input/data sensitivity | p. 7 (5.4. Ablation Study) |
| Comparison of ablation experiments. | component/input/data sensitivity | p. 8 (5.4. Ablation Study) |
| Table 2. Quantitative results of ablation experiments. optimizes the scene's geometry and appearance with the same RGB loss following 3D Gaussian Splatting and en- ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions include: • We introduce a novel quantization scheme that efficiently compresses and integrates semantic features into dense 3D Gaussians, ensuring ... | Figure 5. Images of various open-vocabulary queries. ner effectively diminishes ambiguity and enhances the mean average precision (mAP) metric. Furthermore, integrating DINO features significantly ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (5.2. Comparisons), p. 7 (5.2. Comparisons), p. 4 (Figure/Table caption), p. 6 (5.2. Comparisons) |
| Primary metric/result | Figure 1. We present Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary querying. The top row visualizes the original image, novel view ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / Method - extractive PDF cue:** After the phase of extracting dense semantic features, which takes about 30 minutes, our model can be trained on one RTX3090 GPU for about 1 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | These limitations might be overcome with more advanced visual-language models and native per-pixel semantic features. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Although DINO features improve object boundary detection, they fall short in pinpointing fine-grained object geometries at high resolutions when using CLIP-derived semantics. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Specifically, DFF [22] fails to identify "asphalt ground" in scene "bicycle" and "flower" in scene "garden". | p. 6 (5.2. Comparisons) |
| body limitation/failure cue | This may be caused by its use of LSeg [24], which is unstable to compute correct features in complex scenes. | p. 6 (5.2. Comparisons) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Additionally, model efficiency is evaluated based on CPU and GPU memory usage during training, as well as data storage requirements and training duration. | p. 6 (5.1. Basic Setups) |
| This may be caused by its use of LSeg [24], which is unstable to compute correct features in complex scenes. | p. 6 (5.2. Comparisons) |
| While CLIP [36] encodes images into global language features, its direct application is not feasible for our purposes as we require pixel-level targets to ... | p. 3 (3.2. Dense Language Feature Extraction) |
| Following VQ-VAE [45], the selected language feature index from the set S is determined as m = argmaxi(D(F, fi)), and the quantization of F ... | p. 4 (3.3. Quantization of Language Features) |
| We then render these compact semantic feature vectors into a 2D feature map with rasterization and alpha blending, and decode the 2D feature map ... | p. 5 (3.4. Language Embedded 3D Gaussians) |
| During training process, a softmax operation is applied to the decoder's output, yielding the language feature index distribution ˆ M ∈RH×W ×N, where H ... | p. 5 (3.4. Language Embedded 3D Gaussians) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive PDF cue:** These limitations might be overcome with more advanced visual-language models and native per-pixel semantic features.
- **p. 8 / 6. Conclusion - extractive PDF cue:** Although DINO features improve object boundary detection, they fall short in pinpointing fine-grained object geometries at high resolutions when using CLIP-derived semantics.
- **p. 6 / 5.2. Comparisons - extractive PDF cue:** Specifically, DFF [22] fails to identify "asphalt ground" in scene "bicycle" and "flower" in scene "garden".
- **p. 6 / 5.2. Comparisons - extractive PDF cue:** This may be caused by its use of LSeg [24], which is unstable to compute correct features in complex scenes.

- **PDF anchors reviewed:** datasets p. 6 (5.1. Basic Setups), p. 6 (5.2. Comparisons), p. 7 (5.3. Open-vocabulary Query), p. 7 (5.2. Comparisons), p. 8 (5.4. Ablation Study), p. 8 (5.4. Ablation Study), metrics p. 6 (5.1. Basic Setups), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (5.2. Comparisons), p. 7 (5.2. Comparisons), p. 7 (5.4. Ablation Study), baselines p. 6 (5.2. Comparisons), p. 7 (5.2. Comparisons), p. 8 (5.4. Ablation Study), p. 8 (5.4. Ablation Study), p. 6 (5.2. Comparisons), p. 7 (5.4. Ablation Study), results p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (5.2. Comparisons), p. 7 (5.2. Comparisons), p. 4 (Figure/Table caption), p. 6 (5.2. Comparisons).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
