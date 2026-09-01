# Evaluation - OpenSeg: Scaling Open-Vocabulary Image Segmentation with Image-Level Labels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.12143; PDF retrieval source: https://arxiv.org/pdf/2112.12143. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments)): OpenSeg significantly outperforms pre-trained ALIGN [23]: OpenSeg trained on COCO outperforms ALIGN baseline on all of the benchmarks significantly.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive PDF cue:** Training Datasets COCO: We use the panoptic segmentation [26] and caption [9] annotations in the 2017 splits which include 118k/5k train/val images.
- **p. 9 / 4 Experiments - extractive PDF cue:** Particularly, the underwater scene is not present in our training dataset COCO, but the model can still organize pixels into regions for ocean, coral, diver, ...
- **p. 9 / 4 Experiments - extractive PDF cue:** Evaluation Datasets PASCAL Context: PASCAL Context [35] includes per-pixel segmentation annotations of object and stuffon 5k/5k train/val images from various indoor and outdoor senses.
- **p. 12 / 4 Experiments - extractive PDF cue:** Scaling training data with captions improves performance: To scale up training data we utilize the Localized Narrative dataset, which includes detailed narratives about the objects ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We train OpenSeg on COCO dataset for 30k steps.
- **p. 10 / 4 Experiments - extractive PDF cue:** Notably, OpenSeg is trained on COCO which does not include underwater scenes.
- **p. 10 / 4 Experiments - extractive PDF cue:** We fine-tune the pre-trained image encoder and FPN layers on COCO dataset using a per-pixel cross-entropy loss to align pixel embeddings with text embeddings.
- **p. 11 / 4 Experiments - extractive PDF cue:** OpenSeg significantly outperforms pre-trained ALIGN [23]: OpenSeg trained on COCO outperforms ALIGN baseline on all of the benchmarks significantly.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | OpenSeg significantly outperforms pre-trained ALIGN [23]: OpenSeg trained on COCO outperforms ALIGN baseline on all of the benchmarks significantly. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | This model significantly outperforms the strongest LSeg model with ViT-L backbone (+19.9 mIoU on PASCAL-20). | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | LSeg+ significantly outperforms LSeg (and also SPNet [49] and ZS3Net [6]) as it is trained on the larger dataset of COCO instead of PASCAL-20. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | While adding proposals to ALIGN improves mIoU results. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 6.8 11.2 24.8 45.9 Incorporating proposals at inference time improves accuracy: We are curious about the importance of mask proposals in OpenSeg during inference. | p. 13 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive PDF cue:** Training Datasets COCO: We use the panoptic segmentation [26] and caption [9] annotations in the 2017 splits which include 118k/5k train/val images.
- **p. 9 / 4 Experiments - extractive PDF cue:** Particularly, the underwater scene is not present in our training dataset COCO, but the model can still organize pixels into regions for ocean, coral, diver, ...
- **p. 9 / 4 Experiments - extractive PDF cue:** Evaluation Datasets PASCAL Context: PASCAL Context [35] includes per-pixel segmentation annotations of object and stuffon 5k/5k train/val images from various indoor and outdoor senses.
- **p. 12 / 4 Experiments - extractive PDF cue:** Scaling training data with captions improves performance: To scale up training data we utilize the Localized Narrative dataset, which includes detailed narratives about the objects ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We train OpenSeg on COCO dataset for 30k steps.
- **p. 10 / 4 Experiments - extractive PDF cue:** Notably, OpenSeg is trained on COCO which does not include underwater scenes.
- **p. 10 / 4 Experiments - extractive PDF cue:** We fine-tune the pre-trained image encoder and FPN layers on COCO dataset using a per-pixel cross-entropy loss to align pixel embeddings with text embeddings.
- **p. 11 / 4 Experiments - extractive PDF cue:** OpenSeg significantly outperforms pre-trained ALIGN [23]: OpenSeg trained on COCO outperforms ALIGN baseline on all of the benchmarks significantly.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Examples of image segmentation with arbitrary text queries. We propose a model, called OpenSeg, that can organize pixels into meaningful regions indicated by ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. ALIGN (middle) can only roughly localize text queries onto the image. In contrast, OpenSeg (right) can localize visual concepts with accurate seg- mentation. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. An overview of our approach. We compare OpenSeg with ALIGN / CLIP [23,40] and per-pixel segmentation models such as LSeg [29]. The major ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1. Recall of segmentation mask proposals on COCO and PASCAL-Context datasets. All methods use 128 proposals. COCO PASCAL Context-59 R50 R70 R90 R50 R70 ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 4. Examples of predicted segmentation masks in an unseen scene. OpenSeg is able to segment an image into meaningful regions. These regions may be ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Figure 5. (Bottom) The mIoU and Grounding mIoU results of ALIGN, ALIGN w/proposal, LSeg+, and OpenSeg. (Top) Segmentation predictions on an image from the ADE20k ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 2. The mIoU results of our model and previous open-vocabulary and zero-shot segmentation methods. Results for SPNet and ZS3Net on PASCAL-20 are reported from ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 3. Backbone initialization with an ALIGN pre-trained image encoder is not critical. The models use the pre-trained ALIGN text encoder and are trained on ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Training Datasets COCO: We use the panoptic segmentation [26] and caption [9] annotations in the 2017 splits which include 118k/5k train/val images. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | Particularly, the underwater scene is not present in our training dataset COCO, but the model can still organize pixels into regions for ocean, coral, ... | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 6 (3 Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 6 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 4.2 Predicting Masks Across Datasets We train the segmentation proposal model on COCO and evaluate on COCO and PC-59 with recalls at IoU 50%, ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| We ensemble the multiple text queries by taking the max score as described in the Section 3.4. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| 6.8 11.2 24.8 45.9 Incorporating proposals at inference time improves accuracy: We are curious about the importance of mask proposals in OpenSeg during inference. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Incorporating predicted masks at inference improves mIoU accuracy. | definition/direction/unit from same section | p. 14 (4 Experiments) |
| Table 6. Our mask prediction can generalize across datasets. We report the recall at IoU 0.5. Train / Test COCO ADE20K Mapillary IDD BDD ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| The weight decay is set to 1e-05 and we use a learning rate 0.005 with the cosine learning rate schedule. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Unless otherwise stated, for each core we compute the loss over the local batch of examples (See Appendix F for the comparison between sync ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| OpenSeg shows significantly superior performances. | definition/direction/unit from same section | p. 9 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Then we discuss the experimental results with our open-vocabulary baselines and state-of-the-art open-vocabulary and zero-shot methods. | comparison identity and matched condition | p. 10 (4 Experiments) |
| OpenSeg significantly outperforms pre-trained ALIGN [23]: OpenSeg trained on COCO outperforms ALIGN baseline on all of the benchmarks significantly. | comparison identity and matched condition | p. 11 (4 Experiments) |
| ALIGN w/proposal baseline: The ALIGN, LSeg and LSeg+ baselines are methods that perform visual-semantic alignments without explicit visual grouping. | comparison identity and matched condition | p. 10 (4 Experiments) |
| Narr.  8.8 12.2 28.6 48.2 72.2 4.4 Ablation Experiments Importance of backbone initialization: In order to save the computation, we initialize OpenSeg from ... | comparison identity and matched condition | p. 13 (4 Experiments) |
| For example, on PC-459 OpenSeg outperforms ALIGN and ALIGN w/proposals by +5.4 and +4.2 mIoU, respectively. | comparison identity and matched condition | p. 11 (4 Experiments) |
| This model significantly outperforms the strongest LSeg model with ViT-L backbone (+19.9 mIoU on PASCAL-20). | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| ALIGN w/proposal baseline: The ALIGN, LSeg and LSeg+ baselines are methods that perform visual-semantic alignments without explicit visual grouping. | component/input/data sensitivity | p. 10 (4 Experiments) |
| This method performs inference without mask proposals. | component/input/data sensitivity | p. 13 (4 Experiments) |
| Narr.  8.8 12.2 28.6 48.2 72.2 4.4 Ablation Experiments Importance of backbone initialization: In order to save the computation, we initialize OpenSeg from ... | component/input/data sensitivity | p. 13 (4 Experiments) |
| This procedure removes conjunctions, pronouns, adverbs, verbs, etc. which reduces the noises. | component/input/data sensitivity | p. 14 (4 Experiments) |
| Figure 8. Predictions of OpenSeg on random examples in the A-150 dataset (Part1). For each example, top left is the input image, top right ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Since we initialize the backbone of OpenSeg from ALIGN's pretrained checkpoint, we use ALIGN as a baseline. | component/input/data sensitivity | p. 10 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We call our method OpenSeg, standing for open-vocabulary image segmentation. | OpenSeg significantly outperforms pre-trained ALIGN [23]: OpenSeg trained on COCO outperforms ALIGN baseline on all of the benchmarks significantly. | PDF body cue; verify exact table/figure and matched conditions | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments) |
| Primary metric/result | This model significantly outperforms the strongest LSeg model with ViT-L backbone (+19.9 mIoU on PASCAL-20). | numeric claim only at cited anchor | p. 12 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive PDF cue:** To compute Fz and Fs, we apply a fc layer followed by 3 layers of 3×3 convolutions with 640 channels after F.
- **p. 8 / 4 Experiments - extractive PDF cue:** All models are trained with an image size of 640×640.
- **p. 9 / 4 Experiments - extractive PDF cue:** PASCAL VOC: PASCAL VOC 2012 [13] includes 20 object classes and a background class with 1.5k/1.5k train/val images.
- **p. 9 / 4 Experiments - extractive PDF cue:** The full version has annotations in an open-vocabulary setting and includes 2693 object and stuffclasses.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We hope to encourage future works to learn a generalist segmentation model that can transfer across datasets using language as the interface. | p. 14 (5 Conclusion) |
| body limitation/failure cue | The small performance differences across different ways of text filtering show OpenSeg is robust to the noise in the input words to some degree. | p. 14 (4 Experiments) |
| body limitation/failure cue | Notably, OpenSeg is trained on COCO which does not include underwater scenes. | p. 10 (4 Experiments) |
| body limitation/failure cue | We find that predictions in the mIoU and Grounding mIoU settings can look quite differently and sometimes mIoU does not correctly reflect the prediction ... | p. 11 (4 Experiments) |
| body limitation/failure cue | Table 7. OpenSeg is robust to the batch size. We present performance of OpenSeg trained on COCO+Loc. Narr. and different batch sizes. Numbers inside ... | p. 20 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Unless otherwise stated, for each core we compute the loss over the local batch of examples (See Appendix F for the comparison between sync ... | p. 8 (4 Experiments) |
| For training these models, we use the same hyper-parameters, and only tune the learning rate (0.32 for scratch, 0.08 for NoisyStudent init. and 0.005 ... | p. 13 (4 Experiments) |
| We compute the activation map before the average pooling layer of the image encoder. | p. 10 (4 Experiments) |
| The weight decay is set to 1e-05 and we use a learning rate 0.005 with the cosine learning rate schedule. | p. 8 (4 Experiments) |
| We may be able to reduce the gap by increasing the batch size and training with more data. | p. 13 (4 Experiments) |
| For a fair comparison, we also construct LSeg in our codebase as follows. | p. 10 (4 Experiments) |
| For the strongest OpenSeg (last two rows), we initialize EfficientNet-b7 backbone with ALIGN pre-trained image encoder [23]. | p. 12 (4 Experiments) |
| We feed each word to a pre-trained text encoder to compute the word feature w. | p. 7 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 5 Conclusion - extractive PDF cue:** We hope to encourage future works to learn a generalist segmentation model that can transfer across datasets using language as the interface.
- **p. 14 / 4 Experiments - extractive PDF cue:** The small performance differences across different ways of text filtering show OpenSeg is robust to the noise in the input words to some degree.
- **p. 10 / 4 Experiments - extractive PDF cue:** Notably, OpenSeg is trained on COCO which does not include underwater scenes.
- **p. 11 / 4 Experiments - extractive PDF cue:** We find that predictions in the mIoU and Grounding mIoU settings can look quite differently and sometimes mIoU does not correctly reflect the prediction quality ...
- **p. 20 / Figure/Table caption - extractive PDF cue:** Table 7. OpenSeg is robust to the batch size. We present performance of OpenSeg trained on COCO+Loc. Narr. and different batch sizes. Numbers inside the ...

- **PDF anchors reviewed:** datasets p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 12 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), metrics p. 9 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments), p. 19 (Figure/Table caption), p. 8 (4 Experiments), baselines p. 10 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), results p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
