# Evaluation - Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.05499; PDF retrieval source: https://arxiv.org/pdf/2303.05499. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 21 (Figure/Table caption), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 22 (Figure/Table caption)): Table 9: Transfer pre-trained DINO to Grounding DINO. We freeze shared modules between DINO and Grounding DINO during grounded fine-tuning. All models are trained with a Swin Transformer Tiny backbone. ...

## Evaluation Body Digest

- **p. 10 / 4 Experiments - extractive PDF cue:** LVIS Benchmark LVIS [15] is a dataset for long-tail objects.
- **p. 11 / 4 Experiments - extractive PDF cue:** ODinW Benchmark ODinW (Object Detection in the Wild) [23] is a more challenging benchmark to test model performance under real-world scenarios.
- **p. 9 / 4 Experiments - extractive PDF cue:** We pre-train models on large-scale datasets and directly evaluate our model on the COCO benchmark.
- **p. 10 / 4 Experiments - extractive PDF cue:** With stronger backbones and larger data, Grounding DINO sets a new record of 52.5 AP on the COCO object detection benchmark without seeing any COCO ...
- **p. 11 / 4 Experiments - extractive PDF cue:** This result shows that Grounding DINO might have learned a better object-level representation which helps yield a better performance after fine-tuning (aligning with the target ...
- **p. 12 / 4 Experiments - extractive PDF cue:** The term "RefC" is used for RefCOCO, RefCOCO+, and RefCOCOg three datasets. * There might be a data leak since COCO includes validation images in ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We conduct extensive experiments on three settings: a closed-set setting on the COCO detection benchmark (Sec.
- **p. 9 / 4 Experiments - extractive PDF cue:** COCO Benchmark We compare Grounding DINO with GLIP and DINO in Table 2.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 4 Experiments (p. 8); A More Implementation Details (p. 19); C More Experiment Results (p. 20); C.2 Detailed Results on COCO Detection Benchmarks (p. 22); C.3 Detailed Results on ODinW Benchmarks (p. 22); C.6 Results with Different Language Encoder for REC (p. 23); 29 Dataset (p. 29); 31 Dataset (p. 31).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 9: Transfer pre-trained DINO to Grounding DINO. We freeze shared modules between DINO and Grounding DINO during grounded fine-tuning. All models are trained ... | p. 21 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that encoder fusion significantly improves model performance on both COCO and LVIS datasets. | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Grounding DINO 13 The results show that RefC helps improve the COCO zero-shot and fine-tuning performance but hurts the LVIS and ODinW results. | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, a key distinction lies in the APmedian, where Grounding DINO significantly outperforms GLIPv2-T (11.9 vs 8.9). | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In our future work, we will perform more studies, including varying the semantic concept coverage of the training data and increasing the scale of ... | p. 11 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 10 / 4 Experiments - extractive PDF cue:** LVIS Benchmark LVIS [15] is a dataset for long-tail objects.
- **p. 11 / 4 Experiments - extractive PDF cue:** ODinW Benchmark ODinW (Object Detection in the Wild) [23] is a more challenging benchmark to test model performance under real-world scenarios.
- **p. 9 / 4 Experiments - extractive PDF cue:** We pre-train models on large-scale datasets and directly evaluate our model on the COCO benchmark.
- **p. 10 / 4 Experiments - extractive PDF cue:** With stronger backbones and larger data, Grounding DINO sets a new record of 52.5 AP on the COCO object detection benchmark without seeing any COCO ...
- **p. 11 / 4 Experiments - extractive PDF cue:** This result shows that Grounding DINO might have learned a better object-level representation which helps yield a better performance after fine-tuning (aligning with the target ...
- **p. 12 / 4 Experiments - extractive PDF cue:** The term "RefC" is used for RefCOCO, RefCOCO+, and RefCOCOg three datasets. * There might be a data leak since COCO includes validation images in ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We conduct extensive experiments on three settings: a closed-set setting on the COCO detection benchmark (Sec.
- **p. 9 / 4 Experiments - extractive PDF cue:** COCO Benchmark We compare Grounding DINO with GLIP and DINO in Table 2.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: (a) Closed-set object detection requires models to detect objects of pre-defined categories. (b) We evaluate models on novel objects and standard Referring expression ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Extending closed-set detectors to open-set scenarios. To help a model align cross-modality information some work tried to fuse features before the final loss ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1: A comparison of previous open-set object detectors. Our summarization is based on the experiments in their paper, but not the ability to extend ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: The framework of Grounding DINO. We present the overall framework, a feature enhancer layer, and a decoder layer in block 1, block 2, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. 3 Grounding DINO Grounding DINO outputs multiple pairs of object boxes and noun phrases for a given (Image, Text) pair. For example, as ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: Comparisons of text representations. 3.1 Feature Extraction and Enhancer Given an (Image, Text) pair, we extract multi-scale image features with an image backbone ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Zero-shot domain transfer and fine-tuning on COCO. * The results in brackets are trained with 1.5× image sizes, i.e., with a maximum image ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2. We pre-train models on large-scale datasets and directly evaluate our model on the COCO benchmark. As the O365 dataset [43] has (nearly4) covered ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | LVIS Benchmark LVIS [15] is a dataset for long-tail objects. | embodiment, simulator version and control stack | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Task/environment | ODinW Benchmark ODinW (Object Detection in the Wild) [23] is a more challenging benchmark to test model performance under real-world scenarios. | reset, timeout, object/scene variation | p. 11 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 5 (1. Model Overall), p. 2 (1 Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This suggests that while GLIPv2 may exhibit larger performance variance across different datasets, Grounding DINO maintains a more consistent performance level. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Table 5: Top-1 accuracy comparison on the referring expression comprehension task. We mark the best results in bold. All models are trained with a ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| The corresponding loss weights are 1.0, 5.0, and 2.0 in the final loss calculation. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| It is named "4scale" in DINO since we downsample the 32× feature map to 64× as an extra feature scale. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| This performance difference might be attributed to the disparity in data distribution between the training dataset and the LVIS dataset. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Even though the performance plateaus with larger input size, Grounding DINO gets an impressive 63.0 AP on COCO test-dev with fine-tuning on the COCO ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| GLIPv2 incorporates advanced techniques like masked text training and cross-instance contrastive learning, making it | definition/direction/unit from same section | p. 11 (4 Experiments) |
| We evaluate the model performance on RefCOCO/+/g directly.5 The results are shown in Table 5. | definition/direction/unit from same section | p. 12 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2. We pre-train models on large-scale datasets and directly evaluate our model on the COCO benchmark. As the O365 dataset [43] has (nearly4) ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| We use GLIP and DetCLIPv2 as baselines for our models. | comparison identity and matched condition | p. 10 (4 Experiments) |
| Grounding DINO obtains a 62.6 AP on COCO minival, outperforming DINO's 62.5 AP. | comparison identity and matched condition | p. 10 (4 Experiments) |
| Impressively, Grounding DINO with a Swin-T backbone outperforms DINO with Swin-L on the full-shot setting. | comparison identity and matched condition | p. 11 (4 Experiments) |
| With only O365 and GoldG for pre-train, Grounding DINO T outperforms DINO on few-shot and full-shot settings. | comparison identity and matched condition | p. 11 (4 Experiments) |
| We leverage GLIP [25] as our baseline. | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 6: Impacts of RefC and COCO data for open-set settings. All models are trained with a Swin Transformer Tiny backbone. 4.5 Ablations We ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Table 7: Ablations for our model. All models are trained on the O365 dataset with a Swin Transformer Tiny backbone. fusion approach. Moreover, we ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 10: Comparison between two Grounding DINO variants: Training from scratch and transfer from DINO-pretrained models. The models are trained on O365 and evaluated ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| Ablations are then conducted to show the effectiveness of our model design (Sec. | component/input/data sensitivity | p. 8 (4 Experiments) |
| To our knowledge, no existing DETR-like models effectively address the rarity challenge in LVIS without extra training data, which may be a characteristic limitation ... | component/input/data sensitivity | p. 10 (4 Experiments) |
| 4.1 Implementation Details We trained two model variants, Grounding DINO T with Swin-T [32], and Grounding DINO L with Swin-L [32] as an image ... | component/input/data sensitivity | p. 9 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To mitigate this issue and improve model performance during grounded training, we introduce a technique that utilizes sub-sentence level text features. | Table 9: Transfer pre-trained DINO to Grounding DINO. We freeze shared modules between DINO and Grounding DINO during grounded fine-tuning. All models are trained ... | PDF body cue; verify exact table/figure and matched conditions | p. 21 (Figure/Table caption), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 22 (Figure/Table caption) |
| Primary metric/result | The results show that encoder fusion significantly improves model performance on both COCO and LVIS datasets. | numeric claim only at cited anchor | p. 13 (4 Experiments) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 7: Ablations for our model. All models are trained on the O365 dataset with a Swin Transformer Tiny backbone. fusion approach. Moreover, we ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | To our knowledge, no existing DETR-like models effectively address the rarity challenge in LVIS without extra training data, which may be a characteristic limitation ... | p. 10 (4 Experiments) |
| body limitation/failure cue | A larger-scale training will be left as our future work. | p. 10 (4 Experiments) |
| body limitation/failure cue | In our future work, we will perform more studies, including varying the semantic concept coverage of the training data and increasing the scale of ... | p. 11 (4 Experiments) |
| body limitation/failure cue | Table 9: Transfer pre-trained DINO to Grounding DINO. We freeze shared modules between DINO and Grounding DINO during grounded fine-tuning. All models are trained ... | p. 21 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use bs and ndim for batch size and feature dimension in the pseudo-code. num_img_tokens and num_text_tokens are used for the number of image ... | p. 19 (A.2 Pseudo Code Language-Guided Query Selection) |
| The variables image_feat and text_feat are used for image and text features, respectively. num_query is the number of queries in the decoder, which is ... | p. 19 (A.2 Pseudo Code Language-Guided Query Selection) |
| The model is trained on 64 Nvidia A100 GPUs with a total batch size of 64. | p. 9 (4 Experiments) |
| The cross-modality decoder is composed of six decoder layers as well. | p. 9 (4 Experiments) |
| The results show that encoder fusion significantly improves model performance on both COCO and LVIS datasets. | p. 13 (4 Experiments) |
| Text cross-attention, while introducing fewer parameters than encoder fusion, showed less performance improvement compared to encoder fusion (+0.6 vs. +0.8). | p. 13 (4 Experiments) |
| Input Text Input Image Model Outputs Keys& Values Cross-Modality Queries Text Features Image Features Vanilla Text Features A Cross-Modality Decoder Layer Cross-Modality Query Self-Attention ... | p. 5 (1. Model Overall) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 7: Ablations for our model. All models are trained on the O365 dataset with a Swin Transformer Tiny backbone. fusion approach. Moreover, we extend ...
- **p. 10 / 4 Experiments - extractive PDF cue:** To our knowledge, no existing DETR-like models effectively address the rarity challenge in LVIS without extra training data, which may be a characteristic limitation of ...
- **p. 10 / 4 Experiments - extractive PDF cue:** A larger-scale training will be left as our future work.
- **p. 11 / 4 Experiments - extractive PDF cue:** In our future work, we will perform more studies, including varying the semantic concept coverage of the training data and increasing the scale of the ...
- **p. 21 / Figure/Table caption - extractive PDF cue:** Table 9: Transfer pre-trained DINO to Grounding DINO. We freeze shared modules between DINO and Grounding DINO during grounded fine-tuning. All models are trained with ...

- **PDF anchors reviewed:** datasets p. 10 (4 Experiments), p. 11 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), metrics p. 11 (4 Experiments), p. 12 (Figure/Table caption), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), baselines p. 9 (Figure/Table caption), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), results p. 21 (Figure/Table caption), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 22 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
