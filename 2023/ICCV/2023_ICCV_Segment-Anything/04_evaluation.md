# Evaluation - Segment Anything

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.02643; PDF retrieval source: https://arxiv.org/pdf/2304.02643. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 12 (7.6. Ablations), p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 10 (7.4. Zero-Shot Instance Segmentation), p. 10 (7.3. Zero-Shot Object Proposals)): SAM significantly outperforms prior interactive segmenters with 1 point and is on par with more points.

## Evaluation Body Digest

- **p. 7 / 5. Segment Anything Dataset - extractive body cue:** 5 we plot the spatial distribution of object centers in SA-1B compared to the largest existing segmentation datasets.
- **p. 8 / 7. Zero-Shot Transfer Experiments - extractive body cue:** These experiments evaluate SAM on datasets and tasks that were not seen during training (our usage of "zero-shot transfer" follows its usage in CLIP [82]).
- **p. 6 / 5. Segment Anything Dataset - extractive body cue:** We compare SA-1B with existing datasets and analyze mask quality and properties.
- **p. 6 / 5. Segment Anything Dataset - extractive body cue:** We compare them directly to professional annotations and look at how various mask properties compare to prominent segmentation datasets.
- **p. 7 / 5. Segment Anything Dataset - extractive body cue:** 6 (legend) we compare these datasets by size.
- **p. 8 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** We use all 23 datasets for mIoU evaluation.
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** We compare per-dataset results in Fig.
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** SAM yields higher results on 16 of the 23 datasets, by as much as ∼47 IoU.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 5. Segment Anything Dataset (p. 6); 7. Zero-Shot Transfer Experiments (p. 8); 7.1. Zero-Shot Single Point Valid Mask Evaluation (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 7.1. Zero-Shot Single Point Valid Mask Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | SAM significantly outperforms prior interactive segmenters with 1 point and is on par with more points. | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| 7.1. Zero-Shot Single Point Valid Mask Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe that the gap between SAM and the baselines grows and SAM is able to achieve comparable results under either sampling method. | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| 7.6. Ablations | EMPIRICAL / SOURCE-REPORTED EVALUATION | (Left) Each data engine stage leads to improvements on our 23 dataset suite, and training with only the automatic data (our default) yields similar ... | p. 12 (7.6. Ablations) |
| 7.1. Zero-Shot Single Point Valid Mask Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | This subset includes both datasets for which SAM outperforms and underperforms RITM according to automatic metrics. | p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| 7.4. Zero-Shot Instance Segmentation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 11 we observe that SAM consistently outperforms ViTDet in the human study. | p. 10 (7.4. Zero-Shot Instance Segmentation) |

## Dataset / Benchmark Role

- **p. 7 / 5. Segment Anything Dataset - extractive body cue:** 5 we plot the spatial distribution of object centers in SA-1B compared to the largest existing segmentation datasets.
- **p. 8 / 7. Zero-Shot Transfer Experiments - extractive body cue:** These experiments evaluate SAM on datasets and tasks that were not seen during training (our usage of "zero-shot transfer" follows its usage in CLIP [82]).
- **p. 6 / 5. Segment Anything Dataset - extractive body cue:** We compare SA-1B with existing datasets and analyze mask quality and properties.
- **p. 6 / 5. Segment Anything Dataset - extractive body cue:** We compare them directly to professional annotations and look at how various mask properties compare to prominent segmentation datasets.
- **p. 7 / 5. Segment Anything Dataset - extractive body cue:** 6 (legend) we compare these datasets by size.
- **p. 8 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** We use all 23 datasets for mIoU evaluation.
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** We compare per-dataset results in Fig.
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** SAM yields higher results on 16 of the 23 datasets, by as much as ∼47 IoU.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We aim to build a foundation model for segmentation by introducing three interconnected components: a prompt- able segmentation task, a segmentation model (SAM) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Example images with overlaid masks from our newly introduced dataset, SA-1B. SA-1B contains 11M diverse, high-resolution, licensed, and privacy protecting images and 1.1B ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Each column shows 3 valid masks generated by SAM from a single ambiguous point prompt (green circle). a broadly capable model that can ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Segment Anything Model (SAM) overview. A heavyweight image encoder outputs an image embedding that can then be efficiently queried by a variety of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Image-size normalized mask center distributions.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Dataset mask properties. The legend references the number of images and masks in each dataset. Note, that SA-1B has 11× more images and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Estimated geographic distribution of SA-1B images. Most of the world's countries have more than 1000 images in SA-1B, and the three countries with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison of geographic and income representa- tion. SA-1B has higher representation in Europe and Asia & Oceania as well as middle income countries. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5 we plot the spatial distribution of object centers in SA-1B compared to the largest existing segmentation datasets. | embodiment, simulator version and control stack | p. 7 (5. Segment Anything Dataset), p. 8 (7. Zero-Shot Transfer Experiments) |
| Task/environment | These experiments evaluate SAM on datasets and tasks that were not seen during training (our usage of "zero-shot transfer" follows its usage in CLIP ... | reset, timeout, object/scene variation | p. 8 (7. Zero-Shot Transfer Experiments), p. 6 (5. Segment Anything Dataset) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 5 (3. Segment Anything Model), p. 5 (3. Segment Anything Model) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 2 (3. What data can power this task and model?), p. 2 (3. What data can power this task and model?) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| SAM's mean ratings fall between 7 and 9, which corresponds to the qualitative rating guideline: "A high score (7-9): The object is identifiable and ... | definition/direction/unit from same section | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| Error bars are 95% confidence intervals for mean mask ratings (all differences are significant; see §E for details). | definition/direction/unit from same section | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| Figure 4: Segment Anything Model (SAM) overview. A heavyweight image encoder outputs an image embedding that can then be efficiently queried by a variety ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 8: Statistical tests showing significance that SAM has higher mask quality ratings than baseline and single-output SAM. P-values are calculated by paired t-test, ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| This bias is reflected quantitatively in Table 3: recall at 50% precision (R50) is high, at the cost of precision. | definition/direction/unit from same section | p. 10 (7.2. Zero-Shot Edge Detection) |
| For comparison, prior work estimates inter-annotator consistency at 85-91% IoU [44, 60]. | definition/direction/unit from same section | p. 6 (5. Segment Anything Dataset) |
| We computed IoU between each pair and found that 94% of pairs have greater than 90% IoU (and 97% of pairs have greater than ... | definition/direction/unit from same section | p. 6 (5. Segment Anything Dataset) |
| Ground truth masks in most datasets do not enumerate all possible masks, which can make automatic metrics unreliable. | definition/direction/unit from same section | p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare mainly to RITM [92], a strong interactive segmenter that performs best on our benchmark compared to other strong baselines [67, 18]. | comparison identity and matched condition | p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| In particular, with the oracle to perform ambiguity resolution, SAM outperforms RITM on all datasets. | comparison identity and matched condition | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| Figure 9: Point to mask evaluation on 23 datasets. (a) Mean IoU of SAM and the strongest single point segmenter, RITM [92]. Due to ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| We compare to a strong baseline implemented as a ViTDet [62] detector (with cascade Mask R-CNN [48, 11] ViT-H). | comparison identity and matched condition | p. 10 (7.3. Zero-Shot Object Proposals) |
| Table 3: recall at 50% precision (R50) is high, at the cost of precision. SAM naturally lags behind state-of-the-art meth- ods that learn the ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| manual + semi automatic + automatic automatic only Training data stages 50 60 70 mIoU (23 datasets) 1 point (oracle) 1 point 0.1M 1M ... | comparison identity and matched condition | p. 12 (7.6. Ablations) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our experiments conclude with an ablation study. | component/input/data sensitivity | p. 8 (7. Zero-Shot Transfer Experiments) |
| Redundant masks are removed by NMS. | component/input/data sensitivity | p. 10 (7.2. Zero-Shot Edge Detection) |
| We perform several ablations on our 23 dataset suite with the single center point prompt protocol. | component/input/data sensitivity | p. 11 (7.6. Ablations) |
| The full SA-1B contains 11M images, which we uniformly subsample to 1M and 0.1M for this ablation. | component/input/data sensitivity | p. 11 (7.6. Ablations) |
| manual + semi automatic + automatic automatic only Training data stages 50 60 70 mIoU (23 datasets) 1 point (oracle) 1 point 0.1M 1M ... | component/input/data sensitivity | p. 12 (7.6. Ablations) |
| Figure 13: Ablation studies of our data engine stages, image encoder scaling, and training data scaling. (Left) Each data engine stage leads to improvements ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce each interconnected component next, followed by the dataset we created and the experiments that demonstrate the effectiveness of our approach. | SAM significantly outperforms prior interactive segmenters with 1 point and is on par with more points. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 12 (7.6. Ablations), p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 10 (7.4. Zero-Shot Instance Segmentation), p. 10 (7.3. Zero-Shot Object Proposals) |
| Primary metric/result | We observe that the gap between SAM and the baselines grows and SAM is able to achieve comparable results under either sampling method. | numeric claim only at cited anchor | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |

- Numeric sentences retained from the body:
- **p. 6 / 5. Segment Anything Dataset - extractive body cue:** These images are high resolution (3300×4950 pixels on average), and the resulting data size can present accessibility and storage challenges.
- **p. 6 / 5. Segment Anything Dataset - extractive body cue:** Even after downsampling, our images are significantly higher resolution than many existing vision datasets (e.g., COCO [66] images are ∼480×640 pixels).
- **p. 8 / 6. Segment Anything RAI Analysis - extractive body cue:** mIoU at 1 point 3 points perceived gender presentation feminine 54.4 ±1.7 90.4 ±0.6 masculine 55.7 ±1.7 90.1 ±0.6 perceived age group older 62.9 ±6.7 ...
- **p. 8 / 6. Segment Anything RAI Analysis - extractive body cue:** Our evaluation uses simulated interactive segmentation with random sampling of 1 and 3 points (see §D).
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** SAM significantly outperforms prior interactive segmenters with 1 point and is on par with more points.
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** Low absolute mIoU at 1 point is the result of ambiguity.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It can miss fine structures, hallucinates small disconnected components at times, and does not produce boundaries as crisply as more computationally intensive methods that ... | p. 12 (8. Discussion) |
| body limitation/failure cue | SAM's mean ratings fall between 7 and 9, which corresponds to the qualitative rating guideline: "A high score (7-9): The object is identifiable and ... | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| body limitation/failure cue | When SAM fails to make a correct prediction, an additional point prompt can help. | p. 11 (7.5. Zero-Shot Text-to-Mask) |
| body limitation/failure cue | When SAM fails to pick the right object from a text prompt only, an additional point often fixes the prediction, similar to [31]. | p. 11 (7.5. Zero-Shot Text-to-Mask) |
| body limitation/failure cue | Our foray into the text-to-mask task is exploratory and not entirely robust, although we believe it can be improved with more effort. | p. 12 (8. Discussion) |
| body limitation/failure cue | As MIAP does not contain perceived skin tone annotations, we use a proprietary dataset that contains annotations for the perceived Fitzpatrick skin type [36], ... | p. 8 (6. Segment Anything RAI Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| That is, at inference time we run text through CLIP's text encoder and then give the resulting text embedding as a prompt to SAM ... | p. 11 (7.5. Zero-Shot Text-to-Mask) |
| Given a precomputed image embedding, the prompt encoder and mask decoder run in a web browser, on CPU, in ∼50ms. | p. 5 (3. Segment Anything Model) |
| The implementation is simple: we run a object detector (the ViTDet used before) and prompt SAM with its output boxes. | p. 10 (7.4. Zero-Shot Instance Segmentation) |
| Surprisingly, we find that a simple design satisfies all three constraints: a powerful image encoder computes an image embedding, a prompt encoder embeds prompts, ... | p. 2 (3. What data can power this task and model?) |
| For all other model and training details, such as hyperparameters, refer to §A. | p. 8 (7. Zero-Shot Transfer Experiments) |
| Unless otherwise specified: (1) SAM uses an MAE [47] pre-trained ViT-H [33] image encoder and (2) SAM was trained on SA-1B, noting that this ... | p. 8 (7. Zero-Shot Transfer Experiments) |
| We compute the standard average recall (AR) metric on LVIS v1 [44]. | p. 10 (7.3. Zero-Shot Object Proposals) |
| Further image encoder scaling does not appear fruitful at this time. | p. 12 (7.6. Ablations) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / 8. Discussion - extractive body cue:** It can miss fine structures, hallucinates small disconnected components at times, and does not produce boundaries as crisply as more computationally intensive methods that "zoom-in", ...
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** SAM's mean ratings fall between 7 and 9, which corresponds to the qualitative rating guideline: "A high score (7-9): The object is identifiable and errors ...
- **p. 11 / 7.5. Zero-Shot Text-to-Mask - extractive body cue:** When SAM fails to make a correct prediction, an additional point prompt can help.
- **p. 11 / 7.5. Zero-Shot Text-to-Mask - extractive body cue:** When SAM fails to pick the right object from a text prompt only, an additional point often fixes the prediction, similar to [31].
- **p. 12 / 8. Discussion - extractive body cue:** Our foray into the text-to-mask task is exploratory and not entirely robust, although we believe it can be improved with more effort.
- **p. 8 / 6. Segment Anything RAI Analysis - extractive body cue:** As MIAP does not contain perceived skin tone annotations, we use a proprietary dataset that contains annotations for the perceived Fitzpatrick skin type [36], which ...

- **Evidence anchors reviewed:** datasets p. 7 (5. Segment Anything Dataset), p. 8 (7. Zero-Shot Transfer Experiments), p. 6 (5. Segment Anything Dataset), p. 6 (5. Segment Anything Dataset), p. 7 (5. Segment Anything Dataset), p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation), metrics p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 5 (Figure/Table caption), p. 24 (Figure/Table caption), p. 10 (7.2. Zero-Shot Edge Detection), p. 6 (5. Segment Anything Dataset), baselines p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (Figure/Table caption), p. 10 (7.3. Zero-Shot Object Proposals), p. 10 (Figure/Table caption), p. 12 (7.6. Ablations), results p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 12 (7.6. Ablations), p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 10 (7.4. Zero-Shot Instance Segmentation), p. 10 (7.3. Zero-Shot Object Proposals).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
