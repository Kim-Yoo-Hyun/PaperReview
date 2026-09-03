# Evaluation - Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.3. Performance Evaluation), p. 5 (4.3. Performance Evaluation), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 6 (4.3. Performance Evaluation)): Specifically, the proposed method achieves 80.5 mIoU and 76.0 mBIoU on the LERF dataset, which outperforms the stateof-the-art methods by a considerable margin for all the metrics.

## Evaluation Body Digest

- **p. 5 / 4.2. Datasets and Evaluation Metrics - extractive body cue:** The LERF dataset consists of 3D scenes in the wild, which are captured by using the Polycam application on the iPhone.
- **p. 5 / 4.2. Datasets and Evaluation Metrics - extractive body cue:** The 3DOVS dataset consists of the diverse set of long-tail objects, which are captured with various poses under different backgrounds.
- **p. 7 / 4.3. Performance Evaluation - extractive body cue:** Performance comparisons of novel view rendering on the LERF [10] dataset (the best results are shown in bold). can see that the proposed method is ...
- **p. 6 / 4.3. Performance Evaluation - extractive body cue:** Some examples of open-vocabulary 3D semantic segmentation on the LERF [10] dataset.
- **p. 6 / 4.3. Performance Evaluation - extractive body cue:** Furthermore, the qualitative comparison with LangSplat [20], Feature-3DGS [34], GSGrouping [31], GOI [21], and LEGaussian [24] is presented on LERF and 3D-OVS datasets in Figs.
- **p. 7 / 4.3. Performance Evaluation - extractive body cue:** Performance comparisons of open-vocabulary 3D semantic segmentation on the 3D-OVS [14] dataset (the best mIoU results are shown in bold).
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Performance analysis of the proposed method based on changes in progressive mask expanding, identity-aware semantic consistency loss, and outlier filtering on the LERF dataset (the ...
- **p. 8 / 4.5. 3D Scene Editing - extractive body cue:** To further demonstrate the practical applicability of the proposed method, we apply it to 3D scene editing tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experimental Results (p. 5); 4.2. Datasets and Evaluation Metrics (p. 5); 4.3. Performance Evaluation (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Performance Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Specifically, the proposed method achieves 80.5 mIoU and 76.0 mBIoU on the LERF dataset, which outperforms the stateof-the-art methods by a considerable margin for ... | p. 5 (4.3. Performance Evaluation) |
| 4.3. Performance Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | As can be seen, the proposed method achieves 94.4 mIoU, which shows the superior performance compared to previous methods. | p. 5 (4.3. Performance Evaluation) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | As can be seen, the performance of open-vocabulary 3D semantic segmentation is considerably improved as each component is added to the baseline. | p. 7 (4.4. Ablation Study) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | The best performance (mIoU: 80.5, mBIoU: 76.0) is achieved when identity-aware semantic consistency loss, progressive mask expanding, and outlier filtering are all applied. | p. 7 (4.4. Ablation Study) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | As a result, the performance of semantic segmentation is effectively improved. | p. 8 (4.4. Ablation Study) |

## Dataset / Benchmark Role

- **p. 5 / 4.2. Datasets and Evaluation Metrics - extractive body cue:** The LERF dataset consists of 3D scenes in the wild, which are captured by using the Polycam application on the iPhone.
- **p. 5 / 4.2. Datasets and Evaluation Metrics - extractive body cue:** The 3DOVS dataset consists of the diverse set of long-tail objects, which are captured with various poses under different backgrounds.
- **p. 7 / 4.3. Performance Evaluation - extractive body cue:** Performance comparisons of novel view rendering on the LERF [10] dataset (the best results are shown in bold). can see that the proposed method is ...
- **p. 6 / 4.3. Performance Evaluation - extractive body cue:** Some examples of open-vocabulary 3D semantic segmentation on the LERF [10] dataset.
- **p. 6 / 4.3. Performance Evaluation - extractive body cue:** Furthermore, the qualitative comparison with LangSplat [20], Feature-3DGS [34], GSGrouping [31], GOI [21], and LEGaussian [24] is presented on LERF and 3D-OVS datasets in Figs.
- **p. 7 / 4.3. Performance Evaluation - extractive body cue:** Performance comparisons of open-vocabulary 3D semantic segmentation on the 3D-OVS [14] dataset (the best mIoU results are shown in bold).
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Performance analysis of the proposed method based on changes in progressive mask expanding, identity-aware semantic consistency loss, and outlier filtering on the LERF dataset (the ...
- **p. 8 / 4.5. 3D Scene Editing - extractive body cue:** To further demonstrate the practical applicability of the proposed method, we apply it to 3D scene editing tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) RGB images. (b)(c) Results of the cosine similar- ity between the text embedding of the input query and language features by the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The overall framework of the proposed method. Language and identity embeddings are augmented into the Gaussian primitive. Coherent identity labels serve as pseudo ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. The proposed progressive mask expanding scheme. Rasterized language and identity feature maps are used to com- pute the cosine similarity with the input ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. This progressive expanding scheme helps the model con- sider the local relationship between segments in the same target, which ensures to extract segmentation ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. (a) Cosine similarity between the rasterized language feature map and the text embedding of the input query. (b)(c) Re- sults of semantic segmentation ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Some examples of open-vocabulary 3D semantic segmentation on the LERF [10] dataset. (a) Rendered images by 3DGS [9]. Results by (b) the proposed ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Performance comparisons of open-vocabulary 3D semantic segmentation on the LERF [10] dataset (the best results are shown in bold). rendering performance for novel ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Some examples of open-vocabulary 3D semantic segmentation on the LERF [10] dataset. (a) Rendered images by 3DGS [9]. Results by (b) the proposed ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The LERF dataset consists of 3D scenes in the wild, which are captured by using the Polycam application on the iPhone. | embodiment, simulator version and control stack | p. 5 (4.2. Datasets and Evaluation Metrics), p. 5 (4.2. Datasets and Evaluation Metrics) |
| Task/environment | The 3DOVS dataset consists of the diverse set of long-tail objects, which are captured with various poses under different backgrounds. | reset, timeout, object/scene variation | p. 5 (4.2. Datasets and Evaluation Metrics), p. 7 (4.3. Performance Evaluation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3.2. Identity-aware Semantic Consistency Learning) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| These metrics evaluate the accuracy of semantic segmentation masks corresponding to the input text queries. | definition/direction/unit from same section | p. 5 (4.2. Datasets and Evaluation Metrics) |
| Meanwhile, mBIoU measures the alignment accuracy between predicted segmentation boundaries and ground truth. | definition/direction/unit from same section | p. 5 (4.2. Datasets and Evaluation Metrics) |
| As can be seen, the proposed method successfully mitigates this problem by applying the identity-aware semantic consistency loss and the progressive mask expanding scheme. | definition/direction/unit from same section | p. 6 (4.3. Performance Evaluation) |
| In particular, we can see that the identity-aware semantic loss is most effective for improving the performance (a) (b) (c) (d) Figure 7. | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| The best performance (mIoU: 80.5, mBIoU: 76.0) is achieved when identity-aware semantic consistency loss, progressive mask expanding, and outlier filtering are all applied. | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| Given an input text query, the segmentation mask is generated by using the rasterized language feature map (which is explained in subsection 3.3). | definition/direction/unit from same section | p. 8 (4.5. 3D Scene Editing) |
| Performance analysis of the proposed method based on changes in progressive mask expanding, identity-aware semantic consistency loss, and outlier filtering on the LERF dataset ... | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| These results demonstrate the effectiveness of the proposed method in open-vocabulary 3D semantic segmentation. | definition/direction/unit from same section | p. 6 (4.3. Performance Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Performance comparisons of novel view rendering on the LERF [10] dataset (the best results are shown in bold). can see that the proposed method ... | comparison identity and matched condition | p. 7 (4.3. Performance Evaluation) |
| Performance comparisons of open-vocabulary 3D semantic segmentation on the LERF [10] dataset (the best results are shown in bold). rendering performance for novel view ... | comparison identity and matched condition | p. 6 (4.3. Performance Evaluation) |
| In all experiments, the proposed method shows the meaningful improvement compared to previous approaches. | comparison identity and matched condition | p. 5 (4.3. Performance Evaluation) |
| As can be seen, the proposed method achieves 94.4 mIoU, which shows the superior performance compared to previous methods. | comparison identity and matched condition | p. 5 (4.3. Performance Evaluation) |
| Consequently, our approach generates open-vocabulary 3D semantic masks more accurately compared to previous approaches. | comparison identity and matched condition | p. 6 (4.3. Performance Evaluation) |
| As can be seen, the performance of open-vocabulary 3D semantic segmentation is considerably improved as each component is added to the baseline. | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 3. This progressive expanding scheme helps the model con- sider the local relationship between segments in the same target, which ensures to extract ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Performance comparisons of novel view rendering on the LERF [10] dataset (the best results are shown in bold). can see that the proposed method ... | component/input/data sensitivity | p. 7 (4.3. Performance Evaluation) |
| As can be seen, the performance of open-vocabulary 3D semantic segmentation is considerably improved as each component is added to the baseline. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Consequently, synergy among the proposed components yields superior performance in openvocabulary 3D semantic segmentation. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contribution of the proposed method can be summarized as follows: • We propose a novel framework that enforces language embeddings in the ... | Specifically, the proposed method achieves 80.5 mIoU and 76.0 mBIoU on the LERF dataset, which outperforms the stateof-the-art methods by a considerable margin for ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.3. Performance Evaluation), p. 5 (4.3. Performance Evaluation), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 6 (4.3. Performance Evaluation) |
| Primary metric/result | As can be seen, the proposed method achieves 94.4 mIoU, which shows the superior performance compared to previous methods. | numeric claim only at cited anchor | p. 5 (4.3. Performance Evaluation) |

- Numeric sentences retained from the body:
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive body cue:** During training, we randomly select a subset of Gaussians and compute the identity-aware semantic consistency loss Lcons, which is defined as follows: Lcons = Lsame ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Furthermore, we also evaluate the performance of the proposed method with photometric metrics, such as peak signal-to-noise ratio (PSNR), structural similarity index (SSIM) [27], ... | p. 5 (4.3. Performance Evaluation) |
| body limitation/failure cue | In addition, previous methods often fail to extract boundaries accurately due to the use of fixed threshold values in generating semantic segmentation masks(see Fig. | p. 6 (4.3. Performance Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our model is trained on an AMD EPYC 7352 24-Core Processor CPU and a single NVIDIA A100 GPU. | p. 5 (4.1. Training) |
| Each Gaussian Gi is defined by its center µi ∈R3, covariance matrix Σi ∈R3×3, opacity αi, and appearance encoded as spherical harmonics (SH) coefficients ... | p. 3 (3.1. Preliminaries) |
| The final rendered color C(v) at each pixel v is computed by splatting Gaussians onto the image plane, followed by alpha blending: C(v) = ... | p. 3 (3.1. Preliminaries) |
| 2) and select the segment with the highest average similarity as the seed for the target region. | p. 4 (3.3. Progressive Mask Expanding) |
| This scheme proceeds iteratively while newly added neighbor segments become new seed segments themselves. | p. 4 (3.3. Progressive Mask Expanding) |
| The CLIP loss Lclip is computed by using the L1 norm between rasterized language feature maps and CLIP feature maps by following the approach ... | p. 5 (3.4. Loss Function) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.3. Performance Evaluation - extractive body cue:** Furthermore, we also evaluate the performance of the proposed method with photometric metrics, such as peak signal-to-noise ratio (PSNR), structural similarity index (SSIM) [27], and ...
- **p. 6 / 4.3. Performance Evaluation - extractive body cue:** In addition, previous methods often fail to extract boundaries accurately due to the use of fixed threshold values in generating semantic segmentation masks(see Fig.

- **Evidence anchors reviewed:** datasets p. 5 (4.2. Datasets and Evaluation Metrics), p. 5 (4.2. Datasets and Evaluation Metrics), p. 7 (4.3. Performance Evaluation), p. 6 (4.3. Performance Evaluation), p. 6 (4.3. Performance Evaluation), p. 7 (4.3. Performance Evaluation), metrics p. 5 (4.2. Datasets and Evaluation Metrics), p. 5 (4.2. Datasets and Evaluation Metrics), p. 6 (4.3. Performance Evaluation), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 8 (4.5. 3D Scene Editing), baselines p. 7 (4.3. Performance Evaluation), p. 6 (4.3. Performance Evaluation), p. 5 (4.3. Performance Evaluation), p. 5 (4.3. Performance Evaluation), p. 6 (4.3. Performance Evaluation), p. 7 (4.4. Ablation Study), results p. 5 (4.3. Performance Evaluation), p. 5 (4.3. Performance Evaluation), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 6 (4.3. Performance Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
