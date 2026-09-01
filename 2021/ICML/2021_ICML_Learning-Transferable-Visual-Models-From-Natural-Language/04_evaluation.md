# Evaluation - Learning Transferable Visual Models From Natural Language Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.00020; PDF retrieval source: https://arxiv.org/pdf/2103.00020. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 13 (3.3. Robustness to Natural Distribution Shift), p. 14 (3.3. Robustness to Natural Distribution Shift), p. 8 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION)): Learning Transferable Visual Models From Natural Language Supervision 8 Similar to the "prompt engineering" discussion around GPT3 (Brown et al., 2020; Gao et al., 2020), we have also observed that ...

## Evaluation Body Digest

- **p. 9 / 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE - extractive body cue:** The 20 datasets with at least 16 examples per class were used in this analysis. we see that zero-shot CLIP is quite weak on several ...
- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** However, many popular computer vision datasets were created by the research community primarily as benchmarks to guide the development of generic image classification methods rather ...
- **p. 11 / 3.2. Representation Learning - extractive body cue:** This evaluation suite, detailed in Appendix A includes datasets representing the aforementioned tasks, German Traffic Signs Recognition Benchmark (Stallkamp et al., 2011), as well as ...
- **p. 16 / 3.3. Robustness to Natural Distribution Shift - extractive body cue:** Taken together, these results suggest that the recent shift towards large-scale task and dataset agnostic pre-training combined with a reorientation towards zero-shot and fewshot benchmarking ...
- **p. 14 / 3.3. Robustness to Natural Distribution Shift - extractive body cue:** For both dataset splits, the transfer scores of linear probes trained on the representations of CLIP models are higher than other models with similar ImageNet ...
- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** In this view, a dataset evaluates performance on a task on a specific distribution.
- **p. 8 / 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE - extractive body cue:** On "general" object classification datasets such as ImageNet, CIFAR10/100, STL10, and PascalVOC2007 performance is relatively similar with a slight advantage for zero-shot CLIP in all ...
- **p. 10 / 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE - extractive body cue:** On only 5 datasets does zero-shot performance approach linear probe performance (≤3 point difference). mance, suggesting that CLIP is relatively consistent at connecting underlying representation ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 2.2. Creating a Sufficiently Large Dataset (p. 3); 3. Experiments (p. 6); 39 Dataset (p. 39).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 3.1.4. PROMPT ENGINEERING AND ENSEMBLING | SYSTEM / EVALUATION SCOPE UNRESOLVED | Learning Transferable Visual Models From Natural Language Supervision 8 Similar to the "prompt engineering" discussion around GPT3 (Brown et al., 2020; Gao et al., ... | p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING) |
| 3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS | SYSTEM / EVALUATION SCOPE UNRESOLVED | The best CLIP model improves accuracy on ImageNet from a proof of concept 11.5% to 76.2% and matches the performance of the original ResNet-50 ... | p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS) |
| 3.3. Robustness to Natural Distribution Shift | SYSTEM / EVALUATION SCOPE UNRESOLVED | They propose this distinction because in part because they find that while several techniques have been demonstrated to improve performance on synthetic distribution shifts, ... | p. 13 (3.3. Robustness to Natural Distribution Shift) |
| 3.3. Robustness to Natural Distribution Shift | SYSTEM / EVALUATION SCOPE UNRESOLVED | It is surprising to see a 9.2% increase in accuracy, which corresponds to roughly 3 years of improvement in SOTA, fail to translate into ... | p. 14 (3.3. Robustness to Natural Distribution Shift) |
| 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE | SYSTEM / EVALUATION SCOPE UNRESOLVED | Zeroshot CLIP significantly outperforms a ResNet-50 on two datasets measuring action recognition in videos. | p. 8 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE) |

## Dataset / Benchmark Role

- **p. 9 / 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE - extractive body cue:** The 20 datasets with at least 16 examples per class were used in this analysis. we see that zero-shot CLIP is quite weak on several ...
- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** However, many popular computer vision datasets were created by the research community primarily as benchmarks to guide the development of generic image classification methods rather ...
- **p. 11 / 3.2. Representation Learning - extractive body cue:** This evaluation suite, detailed in Appendix A includes datasets representing the aforementioned tasks, German Traffic Signs Recognition Benchmark (Stallkamp et al., 2011), as well as ...
- **p. 16 / 3.3. Robustness to Natural Distribution Shift - extractive body cue:** Taken together, these results suggest that the recent shift towards large-scale task and dataset agnostic pre-training combined with a reorientation towards zero-shot and fewshot benchmarking ...
- **p. 14 / 3.3. Robustness to Natural Distribution Shift - extractive body cue:** For both dataset splits, the transfer scores of linear probes trained on the representations of CLIP models are higher than other models with similar ImageNet ...
- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** In this view, a dataset evaluates performance on a task on a specific distribution.
- **p. 8 / 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE - extractive body cue:** On "general" object classification datasets such as ImageNet, CIFAR10/100, STL10, and PascalVOC2007 performance is relatively similar with a slight advantage for zero-shot CLIP in all ...
- **p. 10 / 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE - extractive body cue:** On only 5 datasets does zero-shot performance approach linear probe performance (≤3 point difference). mance, suggesting that CLIP is relatively consistent at connecting underlying representation ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Summary of our approach. While standard image models jointly train an image feature extractor and a linear classifier to predict some label, CLIP ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. CLIP is much more efficient at zero-shot transfer than our image caption baseline. Although highly expressive, we found that transformer-based language models are ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Numpy-like pseudocode for the core of an implementa- tion of CLIP. representation of the image. For the second architecture, we experiment with the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Comparing CLIP to prior zero-shot transfer image classi- fication results. CLIP improves performance on all three datasets by a large amount. This improvement ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Prompt engineering and ensembling improve zero- shot performance. Compared to the baseline of using contextless class names, prompt engineering and ensembling boost zero-shot ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Zero-shot CLIP is competitive with a fully super- vised baseline. Across a 27 dataset eval suite, a zero-shot CLIP classifier outperforms a fully ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6. Zero-shot CLIP outperforms few-shot linear probes. Zero-shot CLIP matches the average performance of a 4-shot linear classifier trained on the same feature space ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7. The data efficiency of zero-shot transfer varies widely. Calculating the number of labeled examples per class a linear classifier on the same CLIP ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The 20 datasets with at least 16 examples per class were used in this analysis. we see that zero-shot CLIP is quite weak on ... | embodiment, simulator version and control stack | p. 9 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION) |
| Task/environment | However, many popular computer vision datasets were created by the research community primarily as benchmarks to guide the development of generic image classification methods ... | reset, timeout, object/scene variation | p. 6 (3.1.1. MOTIVATION), p. 11 (3.2. Representation Learning) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 1 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 3 (2.1. Natural Language Supervision), p. 4 (2.3. Selecting an Efficient Pre-Training Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| On aYahoo, CLIP achieves a 95% reduction in the number of errors, and on SUN, CLIP more than doubles the accuracy of Visual N-Grams. | definition/direction/unit from same section | p. 7 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS) |
| They propose this distinction because in part because they find that while several techniques have been demonstrated to improve performance on synthetic distribution shifts, ... | definition/direction/unit from same section | p. 13 (3.3. Robustness to Natural Distribution Shift) |
| Figure 12. CLIP's features are more robust to task shift when compared to models pre-trained on ImageNet. For both dataset splits, the transfer scores ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Figure 13. Zero-shot CLIP is much more robust to distribution shift than standard ImageNet models. (Left) An ideal robust model (dashed line) performs equally ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| The best CLIP model improves accuracy on ImageNet from a proof of concept 11.5% to 76.2% and matches the performance of the original ResNet-50 ... | definition/direction/unit from same section | p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS) |
| We plot the average error rate of the 5 ResNet CLIP models across 39 evaluations on 36 different datasets and find that a similar ... | definition/direction/unit from same section | p. 10 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE) |
| Relative robustness captures any improvement in out-of-distribution accuracy. | definition/direction/unit from same section | p. 13 (3.3. Robustness to Natural Distribution Shift) |
| All zero-shot CLIP models improve effective robustness by a large amount and reduce the size of the gap between ImageNet accuracy and accuracy under ... | definition/direction/unit from same section | p. 14 (3.3. Robustness to Natural Distribution Shift) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the baseline of using contextless class names, prompt engineering and ensembling boost zero-shot classification performance by almost 5 points on average across ... | comparison identity and matched condition | p. 7 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING) |
| Zero-shot CLIP outperforms this baseline slightly more of40 30 20 10 0 10 20 30 40 Score (%) Zero-Shot CLIP vs. | comparison identity and matched condition | p. 8 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE) |
| In Figure 4 we visualize how prompt engineering and ensembling change the performance of a set of CLIP models compared to the contextless baseline ... | comparison identity and matched condition | p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING) |
| This increases flexibility, and prior work has convincingly demonstrated that fine-tuning outperforms linear classification on most image classification datasets (Kornblith et al., 2019; Zhai ... | comparison identity and matched condition | p. 11 (3.2. Representation Learning) |
| Table 16. Detailed ImageNet robustness performance. IN is used to abbreviate for ImageNet. a(Xie et al., 2020) b(Touvron et al., 2019) Despite this handicap, ... | comparison identity and matched condition | p. 47 (Figure/Table caption) |
| Linear probe performance of CLIP models in comparison with state-of-the-art computer vision models, including EfficientNet (Tan & Le, 2019; Xie et al., 2020), MoCo ... | comparison identity and matched condition | p. 12 (3.2. Representation Learning) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| While GPT-1 (Radford et al., 2018) focused on pretraining as a transfer learning method to improve supervised fine-tuning, it also included an ablation study ... | component/input/data sensitivity | p. 6 (3.1.1. MOTIVATION) |
| Finally, we found that on satellite image classification datasets it helped to specify that the images were of this form and we use variants ... | component/input/data sensitivity | p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING) |
| As a step towards understanding whether pre-trained zero-shot models consistently have higher effective robustness than fine-tuned models, we encourage the authors of Mahajan et ... | component/input/data sensitivity | p. 15 (3.3. Robustness to Natural Distribution Shift) |
| One option to prevent this is to identify and remove all duplicates before training a model. | component/input/data sensitivity | p. 17 (5. Data Overlap Analysis) |
| Table 13. CLIP improves zero-shot retrieval and is competitive with the best fine-tuned result on Flickr30k text retrieval. Bold indicates best overall performance while ... | component/input/data sensitivity | p. 46 (Figure/Table caption) |
| An alternative is measuring the performance of end-to-end fine-tuning of the model. | component/input/data sensitivity | p. 11 (3.2. Representation Learning) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Pre-training methods which learn directly from raw text have revolutionized NLP over the last few years (Dai & Le, 2015; Peters et al., 2018; ... | Learning Transferable Visual Models From Natural Language Supervision 8 Similar to the "prompt engineering" discussion around GPT3 (Brown et al., 2020; Gao et al., ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 13 (3.3. Robustness to Natural Distribution Shift), p. 14 (3.3. Robustness to Natural Distribution Shift), p. 8 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION) |
| Primary metric/result | The best CLIP model improves accuracy on ImageNet from a proof of concept 11.5% to 76.2% and matches the performance of the original ResNet-50 ... | numeric claim only at cited anchor | p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS) |

- Numeric sentences retained from the body:
- **p. 7 / 3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS - extractive body cue:** For instance, we train on a dataset that is 10x larger, use a vision model that requires nearly 100x more compute per prediction, likely used ...
- **p. 7 / 3.1.4. PROMPT ENGINEERING AND ENSEMBLING - extractive body cue:** 6.1 9.9 21.5 75.3 265.9 Model GFLOPs 45 50 55 60 65 70 Average Score (%) 4X efficiency gain 5 point improvement RN50 RN101 RN50x4 ...
- **p. 7 / 3.1.4. PROMPT ENGINEERING AND ENSEMBLING - extractive body cue:** Compared to the baseline of using contextless class names, prompt engineering and ensembling boost zero-shot classification performance by almost 5 points on average across 36 ...
- **p. 10 / 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE - extractive body cue:** Comparing zero-shot and linear probe performance across datasets shows a strong correlation with zero-shot performance mostly shifted 10 to 25 points lower.
- **p. 10 / 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE - extractive body cue:** On only 5 datasets does zero-shot performance approach linear probe performance (≤3 point difference). mance, suggesting that CLIP is relatively consistent at connecting underlying representation ...
- **p. 10 / 3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE - extractive body cue:** The GPT family of models has so far demonstrated consistent improvements in zero-shot performance across a 1000x increase in training compute.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This process of characterization can help researchers increase the likelihood models are used beneficially by: • Identifying potentially beneficial downstream uses of models early ... | p. 25 (7.3. Future Work) |
| body limitation/failure cue | Fine-tuning, because it adapts representations to each dataset during the fine-tuning phase, can compensate for and potentially mask failures to learn general and robust ... | p. 11 (3.2. Representation Learning) |
| body limitation/failure cue | There are still many limitations to CLIP. | p. 18 (6. Limitations) |
| body limitation/failure cue | Our methodology has several significant limitations. | p. 20 (6. Limitations) |
| body limitation/failure cue | In our work, we fall back to fitting linear classifiers on top of CLIP's features. | p. 20 (6. Limitations) |
| body limitation/failure cue | Linear classifiers, because of their limited flexibility, instead highlight these failures and provide clear feedback during development. | p. 11 (3.2. Representation Learning) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In Figure 3 we include pseudocode of the core of an implementation of CLIP. | p. 4 (2.3. Selecting an Efficient Pre-Training Method) |
| In Figure 2 we show that a 63 million parameter transformer language model, which already uses twice the compute of its ResNet-50 image encoder, ... | p. 4 (2.3. Selecting an Efficient Pre-Training Method) |
| To save additional memory, gradient checkpointing (Griewank & Walther, 2000; Chen et al., 2016), half-precision Adam statistics (Dhariwal et al., 2020), and half-precision stochastically ... | p. 5 (2.5. Training) |
| For zero-shot evaluation, we cache the zero-shot classifier once it has been computed by the text encoder and reuse it for all subsequent predictions. | p. 6 (3.1.2. USING CLIP FOR ZERO-SHOT TRANSFER) |
| In a bit more detail, we first compute the feature embedding of the image and the feature embedding of the set of possible texts ... | p. 6 (3.1.2. USING CLIP FOR ZERO-SHOT TRANSFER) |
| While adding an L2 penalty towards the generated weights is a straightforward implementation of this idea, we found that hyperparameter optimization would often select ... | p. 9 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE) |
| We use a very large minibatch size of 32,768. | p. 5 (2.5. Training) |
| CLIP is a significant step towards flexible and practical zero-shot computer vision classifiers. | p. 7 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 25 / 7.3. Future Work - extractive body cue:** This process of characterization can help researchers increase the likelihood models are used beneficially by: • Identifying potentially beneficial downstream uses of models early in ...
- **p. 11 / 3.2. Representation Learning - extractive body cue:** Fine-tuning, because it adapts representations to each dataset during the fine-tuning phase, can compensate for and potentially mask failures to learn general and robust representations ...
- **p. 18 / 6. Limitations - extractive body cue:** There are still many limitations to CLIP.
- **p. 20 / 6. Limitations - extractive body cue:** Our methodology has several significant limitations.
- **p. 20 / 6. Limitations - extractive body cue:** In our work, we fall back to fitting linear classifiers on top of CLIP's features.
- **p. 11 / 3.2. Representation Learning - extractive body cue:** Linear classifiers, because of their limited flexibility, instead highlight these failures and provide clear feedback during development.

- **PDF anchors reviewed:** datasets p. 9 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION), p. 11 (3.2. Representation Learning), p. 16 (3.3. Robustness to Natural Distribution Shift), p. 14 (3.3. Robustness to Natural Distribution Shift), p. 6 (3.1.1. MOTIVATION), metrics p. 7 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 13 (3.3. Robustness to Natural Distribution Shift), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption), p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 10 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), baselines p. 7 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 8 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 11 (3.2. Representation Learning), p. 47 (Figure/Table caption), p. 12 (3.2. Representation Learning), results p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 13 (3.3. Robustness to Natural Distribution Shift), p. 14 (3.3. Robustness to Natural Distribution Shift), p. 8 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
