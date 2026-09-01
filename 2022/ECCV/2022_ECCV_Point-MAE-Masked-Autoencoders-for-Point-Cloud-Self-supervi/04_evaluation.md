# Evaluation - Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.06604; PDF retrieval source: https://arxiv.org/pdf/2203.06604. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (4 Experiments), p. 14 (2.60 93.19 Random), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 14 (2.60 93.19 Random), p. 13 (4 Experiments)): On the hardest variant PB-T50-RS, our model achieves 85.18% accuracy, outperforming Point-BERT [54] by 2.11%.

## Evaluation Body Digest

- **p. 10 / 4 Experiments - extractive PDF cue:** 4.2 Downstream Tasks Object Classification on Real-World Dataset In SSL for point cloud, one of the main concerns is to design a model with high ...
- **p. 10 / 4 Experiments - extractive PDF cue:** We split the dataset into a training set and a validation set but only conduct pre-training on the training set.
- **p. 11 / 4 Experiments - extractive PDF cue:** Object Classification on clean objects dataset We evaluate our pre-trained model on ModelNet40 [46] for object classification.
- **p. 11 / 4 Experiments - extractive PDF cue:** Though being pre-trained on clean objects, our Point-MAE generalizes well on real-world data, presenting a strong generalization capability.
- **p. 12 / 4 Experiments - extractive PDF cue:** Few-shot Learning We follow previous works [54,37,41] to conduct few-shot learning experiments on ModelNet40 [46], adopting n-way, m-shot setting, where n is the number of ...
- **p. 12 / 4 Experiments - extractive PDF cue:** Methods 5-way,10-shot 5-way,20-shot 10-way,10-shot 10-way,20-shot DGCNN-rand [41] 31.6 \pm 2.8 40.8 \pm 4.6 19.9 \pm 2.1 16.9 \pm 1.5 DGCNN-OcCo [41] 90.6 \pm 2.8 92.5 ...
- **p. 9 / 4 Experiments - extractive PDF cue:** We conduct the following experiments with our Point-MAE. a) We pre-train our model on ShapeNet [5] training set. b) We evaluate our pre-trained model on ...
- **p. 13 / 4 Experiments - extractive PDF cue:** Point-MAE 13 input for each object, which results in 128 point patches.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the hardest variant PB-T50-RS, our model achieves 85.18% accuracy, outperforming Point-BERT [54] by 2.11%. | p. 11 (4 Experiments) |
| 2.60 93.19 Random | EMPIRICAL / REAL-ROBOT OR HARDWARE | For the fine-tune performance on ModelNet40, it achieves 92.14% accuracy, much lower than Point-MAE (93.19%). | p. 14 (2.60 93.19 Random) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Besides, Point-MAE outperforms sophisticated Point-BERT [54] by 0.6% accuracy. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, given 8192 points as input, our Point-MAE achieves 94.04% accuracy. | p. 12 (4 Experiments) |
| 2.60 93.19 Random | EMPIRICAL / REAL-ROBOT OR HARDWARE | Though this strategy is harder for reconstruction, adopting a medium masking ratio can also achieve good performance. | p. 14 (2.60 93.19 Random) |

## Dataset / Benchmark Role

- **p. 10 / 4 Experiments - extractive PDF cue:** 4.2 Downstream Tasks Object Classification on Real-World Dataset In SSL for point cloud, one of the main concerns is to design a model with high ...
- **p. 10 / 4 Experiments - extractive PDF cue:** We split the dataset into a training set and a validation set but only conduct pre-training on the training set.
- **p. 11 / 4 Experiments - extractive PDF cue:** Object Classification on clean objects dataset We evaluate our pre-trained model on ModelNet40 [46] for object classification.
- **p. 11 / 4 Experiments - extractive PDF cue:** Though being pre-trained on clean objects, our Point-MAE generalizes well on real-world data, presenting a strong generalization capability.
- **p. 12 / 4 Experiments - extractive PDF cue:** Few-shot Learning We follow previous works [54,37,41] to conduct few-shot learning experiments on ModelNet40 [46], adopting n-way, m-shot setting, where n is the number of ...
- **p. 12 / 4 Experiments - extractive PDF cue:** Methods 5-way,10-shot 5-way,20-shot 10-way,10-shot 10-way,20-shot DGCNN-rand [41] 31.6 \pm 2.8 40.8 \pm 4.6 19.9 \pm 2.1 16.9 \pm 1.5 DGCNN-OcCo [41] 90.6 \pm 2.8 92.5 ...
- **p. 9 / 4 Experiments - extractive PDF cue:** We conduct the following experiments with our Point-MAE. a) We pre-train our model on ShapeNet [5] training set. b) We evaluate our pre-trained model on ...
- **p. 13 / 4 Experiments - extractive PDF cue:** Point-MAE 13 input for each object, which results in 128 point patches.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1. Illustration of masked autoencoding. A portion of input data is masked, then an autoencoder is trained to recover the masked parts from original ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2. Reconstruction examples on ShapeNet validation set. In each group, we show the original input (i.e., ground truth), masked point cloud, and reconstruction result ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 3. Overall scheme of our Point-MAE. On the left, we show the masking and embedding process. The input cloud is divided into point patches, ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 4. Reconstruction results on ShapeNet validation set. The model is pre- trained with a masking ratio of 60% but can generalize well on inputs ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 1. Object classification on real-world ScanObjectNN dataset. We eval- uate our approach on three variants, among which PB-T50-RS is the hardest setting. Accuracy (%) ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 2. Object classification on ModelNet40. We compare our approach with various self-supervised (left) and supervised (right) methods. [T] represents the model is based on ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 3. Following standard protocol, we conduct 10 independent experiments for each setting and report mean accuracy with standard deviation. Our Point-MAE significantly advances state-of-the-art ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 3. Few-shot object classification on ModelNet40. We conduct 10 inde- pendent experiments for each setting and report mean accuracy (%) with standard deviation. Methods ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.2 Downstream Tasks Object Classification on Real-World Dataset In SSL for point cloud, one of the main concerns is to design a model with ... | embodiment, simulator version and control stack | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | We split the dataset into a training set and a validation set but only conduct pre-training on the training set. | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (1 Introduction), p. 1 (4 Tencent Data Platform) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (1 Introduction), p. 4 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We conduct experiments using two masking strategy with different masking ratios (%), and report pre-train loss (× 1000) as well as fine-tune accuracy (%). | definition/direction/unit from same section | p. 13 (4 Experiments) |
| We conduct 10 independent experiments for each setting and report mean accuracy (%) with standard deviation. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| The reconstruction loss and fine-tune accuracy on ModelNet40 are presented in Table 5. | definition/direction/unit from same section | p. 14 (2.60 93.19 Random) |
| For the fine-tune performance on ModelNet40, it achieves 92.14% accuracy, much lower than Point-MAE (93.19%). | definition/direction/unit from same section | p. 14 (2.60 93.19 Random) |
| Accuracy (%) for each variant is reported. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Besides, Point-MAE outperforms sophisticated Point-BERT [54] by 0.6% accuracy. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Furthermore, given 8192 points as input, our Point-MAE achieves 94.04% accuracy. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| We report mean IoU for all instances mIoUI (%), with IoU (%) for each category. | definition/direction/unit from same section | p. 13 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Furthermore, our method speeds up pre-training by 1.7× compared to Point-BERT [54]. | comparison identity and matched condition | p. 10 (4 Experiments) |
| Besides, Point-MAE outperforms sophisticated Point-BERT [54] by 0.6% accuracy. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Our Point-MAE largely improves the baseline by 10.16%, 7.74%, and 7.94% for three variants respectively. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Our Point-MAE significantly advances state-of-the-art accuracies of four settings by 1.5%-2.3%, with smaller deviations. | comparison identity and matched condition | p. 12 (4 Experiments) |
| Our Point-MAE achieves 86.1% mIoU, improving the baseline by 1% mIoU. | comparison identity and matched condition | p. 13 (4 Experiments) |
| Our Point-MAE with a simple segmentation head also outperforms Point-BERT [54], which uses DGCNN [44] and propagation in their segmentation head. | comparison identity and matched condition | p. 13 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For fair comparisons, the autoencoder's backbone adopts the same encoder and prediction head as Point-MAE but without the decoder, resulting in the exact same ... | component/input/data sensitivity | p. 14 (2.60 93.19 Random) |
| We conduct the following experiments with our Point-MAE. a) We pre-train our model on ShapeNet [5] training set. b) We evaluate our pre-trained model ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Effect of shifting mask tokens Our Point-MAE shifts mask tokens from the input of the encoder to the lightweight decoder. | component/input/data sensitivity | p. 14 (2.60 93.19 Random) |
| Specifically, the commonly used dataset for pre-training, ShapeNet [5], only contains clean object models, without any scene context such as backgrounds. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Accuracy (%) for each variant is reported. | component/input/data sensitivity | p. 11 (4 Experiments) |
| We evaluate our approach on three variants, among which PB-T50-RS is the hardest setting. | component/input/data sensitivity | p. 11 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions can be summarized as follows: (1) We propose a novel scheme of masked autoencoders for point cloud selfsupervised learning, addressing key ... | On the hardest variant PB-T50-RS, our model achieves 85.18% accuracy, outperforming Point-BERT [54] by 2.11%. | PDF body cue; verify exact table/figure and matched conditions | p. 11 (4 Experiments), p. 14 (2.60 93.19 Random), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 14 (2.60 93.19 Random), p. 13 (4 Experiments) |
| Primary metric/result | For the fine-tune performance on ModelNet40, it achieves 92.14% accuracy, much lower than Point-MAE (93.19%). | numeric claim only at cited anchor | p. 14 (2.60 93.19 Random) |

- Numeric sentences retained from the body:
- **p. 9 / 4 Experiments - extractive PDF cue:** A typical input with p = 1024 points is divided into n = 64 point patches.
- **p. 10 / 4 Experiments - extractive PDF cue:** For each instance, we sample 1024 points via FPS as input point cloud.
- **p. 10 / 4 Experiments - extractive PDF cue:** We pre-train our model for 300 epochs, with a batch size of 128.
- **p. 10 / 4 Experiments - extractive PDF cue:** Motivated by this, we evaluate our pre-trained model on a challenging real-world dataset, ScanObjectNN [39], which consists of about 15,000 objects from 15 categories.
- **p. 11 / 4 Experiments - extractive PDF cue:** Methods OBJ-BG OBJ-ONLY PB-T50-RS PointNet [29] 73.3 79.2 68.0 SpiderCNN [50] 77.1 79.5 73.7 PointNet++ [30] 82.3 84.3 77.9 DGCNN [44] 82.8 86.2 78.1 PointCNN ...
- **p. 11 / 4 Experiments - extractive PDF cue:** ModelNet40 consists of 12,311 clean 3D CAD models, covering 40 object categories.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The leakage of location information makes the reconstruction task less challenging, and the model cannot learn latent features well, leading to worse fine-tune performance. | p. 14 (2.60 93.19 Random) |
| body limitation/failure cue | Our segmentation head is relatively simple and does not use any propagating operation or DGCNN [44]. | p. 13 (4 Experiments) |
| body limitation/failure cue | The performance degrades largely with low making ratios and also degrades slightly if the masking ratio is too high. | p. 14 (2.60 93.19 Random) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We pre-train our model for 300 epochs, with a batch size of 128. | p. 10 (4 Experiments) |
| The initial learning rate is set to 0.001, with a weight decay of 0.05. | p. 10 (4 Experiments) |
| For example, BERT [11] in NLP and MAE [17] in computer vision both apply masked autoencoding and adopt a standard Transformer architecture as autoencoder's ... | p. 2 (1 Introduction) |
| In the autoencoder's backbone, the encoder has 12 Transformer blocks while the decoder has 4 Transformer blocks. | p. 9 (4 Experiments) |
| Effect of shifting mask tokens Our Point-MAE shifts mask tokens from the input of the encoder to the lightweight decoder. | p. 14 (2.60 93.19 Random) |
| At the input of the encoder, all the tokens, including mask tokens, must be provided with location information by positional embeddings. | p. 14 (2.60 93.19 Random) |
| As a promising scheme of self-supervised learning, masked autoencoding has significantly advanced natural language processing and computer vision. | p. 1 (4 Tencent Data Platform) |
| Relying less on labeled data, self-supervised learning has significantly advanced natural language processing (NLP) [11,4,32,33] and computer ⋆Corresponding author | p. 1 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 2.60 93.19 Random - extractive PDF cue:** The leakage of location information makes the reconstruction task less challenging, and the model cannot learn latent features well, leading to worse fine-tune performance.
- **p. 13 / 4 Experiments - extractive PDF cue:** Our segmentation head is relatively simple and does not use any propagating operation or DGCNN [44].
- **p. 14 / 2.60 93.19 Random - extractive PDF cue:** The performance degrades largely with low making ratios and also degrades slightly if the masking ratio is too high.

- **PDF anchors reviewed:** datasets p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), metrics p. 13 (4 Experiments), p. 12 (4 Experiments), p. 14 (2.60 93.19 Random), p. 14 (2.60 93.19 Random), p. 11 (4 Experiments), p. 11 (4 Experiments), baselines p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), results p. 11 (4 Experiments), p. 14 (2.60 93.19 Random), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 14 (2.60 93.19 Random), p. 13 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
