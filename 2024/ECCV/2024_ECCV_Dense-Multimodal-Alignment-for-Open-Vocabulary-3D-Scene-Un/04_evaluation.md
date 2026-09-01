# Evaluation - Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6612_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4 Experiments), p. 14 (Figure/Table caption), p. 10 (4 Experiments), p. 13 (Figure/Table caption), p. 12 (4 Experiments), p. 12 (4 Experiments)): Our DMA(OpenSeg) using only 3D model for prediction outperforms OpenScene(OpenSeg)-2D3D by 5.4% mIoU at a significantly lower latency, wherein the mIoU (F) and mIoU (B) are improved by 8.8% and ...

## Evaluation Body Digest

- **p. 9 / 4 Experiments - extractive PDF cue:** As for nuScenes dataset, we use 8 GPUs for training and set the batch size as 16.
- **p. 9 / 4 Experiments - extractive PDF cue:** To demonstrate the effectiveness of our proposed method, we employ three popular datasets, i.e., ScanNet [11], Matterport3D [6], and nuScenes [4].
- **p. 10 / 4 Experiments - extractive PDF cue:** To validate the effectiveness of our method on outdoor point clouds, we evaluate the performance of DMA on the nuScenes dataset [4].
- **p. 11 / 4 Experiments - extractive PDF cue:** 4: Qualitative results of different methods on both indoor and outdoor datasets. mIoU mACC Precision Recall Head Common Tail All Head Common Tail All Head ...
- **p. 10 / 4 Experiments - extractive PDF cue:** ContrastiveSC [16] 0.9% 64.5 79.7 53.8 LESS [37] 74.8 81.6 68.7 ContrastiveSC 0.2% 63.5 78.4 51.6 LESS 73.5 81.1 66.6 Zero-shot OpenScene [42](LSeg)-2D3D No 36.7 ...
- **p. 11 / 4 Experiments - extractive PDF cue:** 3, we validate the open-vocabulary methods on the more challenging long-tail 3D scene understanding datasets, i.e., ScanNet200 [45].
- **p. 14 / 4 Experiments - extractive PDF cue:** 7, our method can accurately segment the corresponding regions for the given texts/queries in 3D scenes, even for unseen categories.
- **p. 12 / 4 Experiments - extractive PDF cue:** OpenScene [42](LSeg)-3D 41.9 25.4 12.0 5.9 51.2 30.7 15.2 7.5 OpenScene(LSeg)-2D3D 43.4 26.8 13.1 6.4 53.5 33.0 17.4 8.6 OpenScene(OpenSeg)-3D 41.3 33.4 18.1 8.2 55.1 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our DMA(OpenSeg) using only 3D model for prediction outperforms OpenScene(OpenSeg)-2D3D by 5.4% mIoU at a significantly lower latency, wherein the mIoU (F) and mIoU ... | p. 10 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 7: Open-vocabulary segmentation results on rare categories and different forms of queries. The same color corresponds to the same query/category. priors into mask ... | p. 14 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, by densely aligning with the tagging information and the detailed description extracted from each scene, our DMA(OpenSeg) using only 3D encoder significantly improves ... | p. 10 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 6: Comparisons of dif- ferent fine-tuning methods. performance to using both 2D and 3D encoders by solely utilizing the 3D encoder, i.e., 53.3% ... | p. 13 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our approach leverages the advantages of both language and 2D modalities, and achieves excellent segmentation results for both foreground and background classes using only ... | p. 12 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiments - extractive PDF cue:** As for nuScenes dataset, we use 8 GPUs for training and set the batch size as 16.
- **p. 9 / 4 Experiments - extractive PDF cue:** To demonstrate the effectiveness of our proposed method, we employ three popular datasets, i.e., ScanNet [11], Matterport3D [6], and nuScenes [4].
- **p. 10 / 4 Experiments - extractive PDF cue:** To validate the effectiveness of our method on outdoor point clouds, we evaluate the performance of DMA on the nuScenes dataset [4].
- **p. 11 / 4 Experiments - extractive PDF cue:** 4: Qualitative results of different methods on both indoor and outdoor datasets. mIoU mACC Precision Recall Head Common Tail All Head Common Tail All Head ...
- **p. 10 / 4 Experiments - extractive PDF cue:** ContrastiveSC [16] 0.9% 64.5 79.7 53.8 LESS [37] 74.8 81.6 68.7 ContrastiveSC 0.2% 63.5 78.4 51.6 LESS 73.5 81.1 66.6 Zero-shot OpenScene [42](LSeg)-2D3D No 36.7 ...
- **p. 11 / 4 Experiments - extractive PDF cue:** 3, we validate the open-vocabulary methods on the more challenging long-tail 3D scene understanding datasets, i.e., ScanNet200 [45].
- **p. 14 / 4 Experiments - extractive PDF cue:** 7, our method can accurately segment the corresponding regions for the given texts/queries in 3D scenes, even for unseen categories.
- **p. 12 / 4 Experiments - extractive PDF cue:** OpenScene [42](LSeg)-3D 41.9 25.4 12.0 5.9 51.2 30.7 15.2 7.5 OpenScene(LSeg)-2D3D 43.4 26.8 13.1 6.4 53.5 33.0 17.4 8.6 OpenScene(OpenSeg)-3D 41.3 33.4 18.1 8.2 55.1 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 1: Framework of our proposed Dense Multimodal Alignment (DMA) method. We generate comprehensive language modality data by leveraging a tagging model and an MLLM. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: Scene tagging generation. (1) We first employ RAM [57] to generate view-level tags, and then (2) reduce the tag noise with GPT. Finally, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: Segmentation results using 2D and 3D models. 2D model has advantages in segmenting background objects (in blue boxes), while 3D model is more ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison on the ScanNet [11] validation set. "F" and "B" denote fore- ground and background classes, respectively. † denotes our reproduced results. Methods ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison on the nuScenes [4] validation set. We partition all categories into base and long-tail classes according to their frequencies. 4.2 Comparison with ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 4: Qualitative results of different methods on both indoor and outdoor datasets. mIoU mACC Precision Recall Head Common Tail All Head Common Tail All ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 3: Comparison on ScanNet200 [45] validation set. † means our reproduced results. 47.4% mIoU by employing FC-CLIP [56] to extract 2D features. This is ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 4: Comparison on the Matterport [6] test set. and image features as supervision, and perform inference on different K categories. As shown in Tab. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As for nuScenes dataset, we use 8 GPUs for training and set the batch size as 16. | embodiment, simulator version and control stack | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | To demonstrate the effectiveness of our proposed method, we employ three popular datasets, i.e., ScanNet [11], Matterport3D [6], and nuScenes [4]. | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 6 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The mean Intersection-of-Union (mIoU), mean Accuracy (mACC), Precision, and Recall are employed as the evaluation metrics. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| 4: Qualitative results of different methods on both indoor and outdoor datasets. mIoU mACC Precision Recall Head Common Tail All Head Common Tail All ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| By additionally aligning with our generated text modality, our method can achieve outstanding performance on both foreground (58.3%) and background (51.5%) categories using only ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| We use Adam [25] as the optimizer and the initial learning rate is set to 1e -4. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Additionally, the final performance is further improved by 2.3% and attains | definition/direction/unit from same section | p. 10 (4 Experiments) |
| To facilitate comparison, we measure the results of OpenScene by using 3D and 2D-3D integrated features as supervision. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| We train a 3D model by taking our generated textual descriptions | definition/direction/unit from same section | p. 11 (4 Experiments) |
| 4, when employing the same 2D network, i.e., OpenSeg, our method demonstrates superior zero-shot segmentation capability on both common and rare categories. | definition/direction/unit from same section | p. 12 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We conduct comparisons with state-of-the-art methods on each of these datasets. | comparison identity and matched condition | p. 9 (4 Experiments) |
| 4.2 Comparison with State-of-the-Arts We compare the proposed DMA with fully-/weakly-supervised and zero-shot methods [13,42,55]. | comparison identity and matched condition | p. 10 (4 Experiments) |
| When using text supervision only, our method outperforms the text-supervised approach RegionPLC [55] by 9.5%, and even surpasses OpenScene(OpenSeg)-2D3D by 2.6% in terms of ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| While for invocabulary classes, mask features outperform the CLIP feature by 11.6%. | comparison identity and matched condition | p. 13 (4 Experiments) |
| We can observe that our method outperforms RegionPLC [55] by a large margin (about 6.7%) by building dense point-to-text correspondences. | comparison identity and matched condition | p. 13 (4 Experiments) |
| Following [45], we partition the 200 categories into three splits, i.e., head, common, and tail sets, facilitating a more comprehensive comparison across categories with ... | comparison identity and matched condition | p. 11 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This can be attributed to that OpenScene heavily relies on 2D model for supervision without aligning with text prompts, which limits its open-vocabulary ability. | component/input/data sensitivity | p. 12 (4 Experiments) |
| Fig. 1: Framework of our proposed Dense Multimodal Alignment (DMA) method. We generate comprehensive language modality data by leveraging a tagging model and an ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Besides, by fine-tuning the mask head, FC-CLIP could incorporate the 3D structural priors into mask features and produce better results. | component/input/data sensitivity | p. 11 (4 Experiments) |
| Our method does not rely on ground truth 3D labels but instead distill knowledge from pretrained vision-language models, thus it is more robust to ... | component/input/data sensitivity | p. 11 (4 Experiments) |
| Comparisons of Different Fine-Tuning Methods. | component/input/data sensitivity | p. 13 (4 Experiments) |
| For the enhanced version, we replace RAM with RAM++ [22], and LLaVA-7B with LLaVA-13B. | component/input/data sensitivity | p. 13 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In order to leverage the synergistic benefits of multiple modalities for dense prediction tasks, we propose a dense multimodal alignment (DMA) strategy to co-embed ... | Our DMA(OpenSeg) using only 3D model for prediction outperforms OpenScene(OpenSeg)-2D3D by 5.4% mIoU at a significantly lower latency, wherein the mIoU (F) and mIoU ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4 Experiments), p. 14 (Figure/Table caption), p. 10 (4 Experiments), p. 13 (Figure/Table caption), p. 12 (4 Experiments), p. 12 (4 Experiments) |
| Primary metric/result | Fig. 7: Open-vocabulary segmentation results on rare categories and different forms of queries. The same color corresponds to the same query/category. priors into mask ... | numeric claim only at cited anchor | p. 14 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 9 / 4 Experiments - extractive PDF cue:** The model is trained for 100 epochs.
- **p. 9 / 4 Experiments - extractive PDF cue:** As for nuScenes dataset, we use 8 GPUs for training and set the batch size as 16.
- **p. 10 / 4 Experiments - extractive PDF cue:** Methods mIoU mACC mIoU(F) mIoU(B) Latency fully-supervised TangentConv [49] 40.9 - - - - TextureNet [21] 54.8 - - - - ScanComplete [12] 56.6 - ...
- **p. 10 / 4 Experiments - extractive PDF cue:** The suboptimal performance of our method using FC-CLIP as the 2D encoder may be attributed to the low resolution of the images (320×240), which limits ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 2: Scene tagging generation. (1) We first employ RAM [57] to generate view-level tags, and then (2) reduce the tag noise with GPT. ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: Segmentation results using 2D and 3D models. 2D model has advantages in segmenting background objects (in blue boxes), while 3D model is ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Our method, however, directly aligns with the textual modality, overcoming the limitations of 2D models. | p. 12 (4 Experiments) |
| body limitation/failure cue | Our method does not rely on ground truth 3D labels but instead distill knowledge from pretrained vision-language models, thus it is more robust to ... | p. 11 (4 Experiments) |
| body limitation/failure cue | We presented a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding by establishing dense correspondences between 3D points, 2D images and 1D ... | p. 14 (5 Conclusion) |
| body limitation/failure cue | This is because there are only a few instances available on these long-tail categories, which is not sufficient to train a robust model from ... | p. 11 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use Adam [25] as the optimizer and the initial learning rate is set to 1e -4. | p. 9 (4 Experiments) |
| As for nuScenes dataset, we use 8 GPUs for training and set the batch size as 16. | p. 9 (4 Experiments) |
| 53.5% mIoU(F), and hence significantly reducing inference time. | p. 13 (4 Experiments) |
| 1, although OpenScene(LSeg) attains better results (54.2% mIoU) by using both 2D and 3D encoders, it results in significantly increased inference latency. | p. 10 (4 Experiments) |
| This is because the parameter size of 2D encoder is much larger than 3D encoder, and the 2D encoder needs to perform inference on ... | p. 10 (4 Experiments) |
| We can observe that OpenScene [42] with only 3D encoder exhibits poor performance in segmenting objects that lack spatial structures, such as "door", "window", ... | p. 12 (4 Experiments) |
| This demonstrates that the fixed CLIP visual encoder could maintain the strong generalization ability on novel classes. | p. 13 (4 Experiments) |
| We address this issue in two steps. | p. 5 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: Scene tagging generation. (1) We first employ RAM [57] to generate view-level tags, and then (2) reduce the tag noise with GPT. Finally, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: Segmentation results using 2D and 3D models. 2D model has advantages in segmenting background objects (in blue boxes), while 3D model is more ...
- **p. 12 / 4 Experiments - extractive PDF cue:** Our method, however, directly aligns with the textual modality, overcoming the limitations of 2D models.
- **p. 11 / 4 Experiments - extractive PDF cue:** Our method does not rely on ground truth 3D labels but instead distill knowledge from pretrained vision-language models, thus it is more robust to rare ...
- **p. 14 / 5 Conclusion - extractive PDF cue:** We presented a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding by establishing dense correspondences between 3D points, 2D images and 1D texts, ...
- **p. 11 / 4 Experiments - extractive PDF cue:** This is because there are only a few instances available on these long-tail categories, which is not sufficient to train a robust model from scratch.

- **PDF anchors reviewed:** datasets p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), metrics p. 9 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), baselines p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), results p. 10 (4 Experiments), p. 14 (Figure/Table caption), p. 10 (4 Experiments), p. 13 (Figure/Table caption), p. 12 (4 Experiments), p. 12 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
