# Evaluation - ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2102.05918; PDF retrieval source: https://arxiv.org/pdf/2102.05918. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2. Zero-shot Visual Classification), p. 5 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval), p. 4 (5.1. Image-Text Matching & Retrieval), p. 5 (5.1. Image-Text Matching & Retrieval)): With frozen features, ALIGN slightly outperforms CLIP and achieves SOTA result of 85.5% top-1 accuracy.

## Evaluation Body Digest

- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** After the sweep, the selected hyperparameters are used to train on the combined training and validation splits of 1000 images for each task.
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** Model All tasks Natural Specialized Structured Bit-L 78.72 - - - ALIGN 79.99±0.15 83.38 87.56 73.25 To evaluate on smaller fine-grained classification benchmarks, we adopt ...
- **p. 4 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** Specifically, for Flickr30K, we evaluate on the standard 1K test set, and finetune on the 30k training set.
- **p. 3 / 3. A Large-Scale Noisy Image-Text Dataset - extractive body cue:** For this purpose, we resort to a much larger dataset than existing ones.
- **p. 3 / 3. A Large-Scale Noisy Image-Text Dataset - extractive body cue:** The result is a much larger (1.8B image-text pairs) but noisier dataset.
- **p. 4 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** We evaluate ALIGN on Flickr30K and MSCOCO crossmodal retrieval benchmarks, in both zero-shot and fully fine-tuned settings.
- **p. 5 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** Multimodal retrieval performance on Crisscrossed Captions (CxC) dataset.
- **p. 5 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** Spearman's R Bootstrap Correlation (×100) on Crisscrossed Captions (CxC) dataset.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 3. A Large-Scale Noisy Image-Text Dataset (p. 3); 5. Experiments and Results (p. 4); 6.2. Pre-training Datasets (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Zero-shot Visual Classification | SYSTEM / EVALUATION SCOPE UNRESOLVED | With frozen features, ALIGN slightly outperforms CLIP and achieves SOTA result of 85.5% top-1 accuracy. | p. 6 (5.2. Zero-shot Visual Classification) |
| 5.2. Zero-shot Visual Classification | SYSTEM / EVALUATION SCOPE UNRESOLVED | We find that such ensembling gives 2.9% improvement on ImageNet top-1 accuracy. | p. 5 (5.2. Zero-shot Visual Classification) |
| 5.2. Zero-shot Visual Classification | SYSTEM / EVALUATION SCOPE UNRESOLVED | After fine-tuning ALIGN achieves higher accuracy than BiT and ViT models, and is only worse than Meta Pseudo Labels which requires deeper interaction between ... | p. 6 (5.2. Zero-shot Visual Classification) |
| 5.1. Image-Text Matching & Retrieval | SYSTEM / EVALUATION SCOPE UNRESOLVED | In the zero-shot setting, ALIGN gets more than 7% improvement in image retrieval task compared to the previous SOTA, CLIP (Radford et al., 2021). | p. 4 (5.1. Image-Text Matching & Retrieval) |
| 5.1. Image-Text Matching & Retrieval | SYSTEM / EVALUATION SCOPE UNRESOLVED | With fine-tuning, ALIGN outperforms all existing methods by a large margin, including those that employ more complex cross-modal attention layers such as ImageBERT (Qi ... | p. 4 (5.1. Image-Text Matching & Retrieval) |

## Dataset / Benchmark Role

- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** After the sweep, the selected hyperparameters are used to train on the combined training and validation splits of 1000 images for each task.
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** Model All tasks Natural Specialized Structured Bit-L 78.72 - - - ALIGN 79.99±0.15 83.38 87.56 73.25 To evaluate on smaller fine-grained classification benchmarks, we adopt ...
- **p. 4 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** Specifically, for Flickr30K, we evaluate on the standard 1K test set, and finetune on the 30k training set.
- **p. 3 / 3. A Large-Scale Noisy Image-Text Dataset - extractive body cue:** For this purpose, we resort to a much larger dataset than existing ones.
- **p. 3 / 3. A Large-Scale Noisy Image-Text Dataset - extractive body cue:** The result is a much larger (1.8B image-text pairs) but noisier dataset.
- **p. 4 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** We evaluate ALIGN on Flickr30K and MSCOCO crossmodal retrieval benchmarks, in both zero-shot and fully fine-tuned settings.
- **p. 5 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** Multimodal retrieval performance on Crisscrossed Captions (CxC) dataset.
- **p. 5 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** Spearman's R Bootstrap Correlation (×100) on Crisscrossed Captions (CxC) dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. A summary of our method, ALIGN. Visual and language representations are jointly learned from noisy image alt-text data. The representations can be used ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Example image-text pairs randomly sampled from the training dataset of ALIGN. One clearly noisy text annotation is marked in italics. Image-based filtering. Following ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Image-text retrieval results on Flickr30K and MSCOCO datasets (zero-shot and fine-tuned). ALIGN is compared with Image- BERT (Qi et al., 2020), UNITER (Chen ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Multimodal retrieval performance on Crisscrossed Captions (CxC) dataset. ALIGN is compared with VSE++ (Faghri et al., 2018), VSRN (Li et al., 2019), DEI2T ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 3. Spearman's R Bootstrap Correlation (×100) on Criss- crossed Captions (CxC) dataset. ALIGN is compared with VSE++ (Faghri et al., 2018), VSRN (Li et ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 4. Top-1 Accuracy of zero-shot transfer of ALIGN to image classification on ImageNet and its variants.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 5. ImageNet classification results. ALIGN is compared with WSL (Mahajan et al., 2018), CLIP (Radford et al., 2021), BiT (Kolesnikov et al., 2020), ViT ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 6. VTAB (19 tasks) comparison between ALIGN and BiT-L.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | After the sweep, the selected hyperparameters are used to train on the combined training and validation splits of 1000 images for each task. | embodiment, simulator version and control stack | p. 6 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification) |
| Task/environment | Model All tasks Natural Specialized Structured Bit-L 78.72 - - - ALIGN 79.99±0.15 83.38 87.56 73.25 To evaluate on smaller fine-grained classification benchmarks, we ... | reset, timeout, object/scene variation | p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We find that such ensembling gives 2.9% improvement on ImageNet top-1 accuracy. | definition/direction/unit from same section | p. 5 (5.2. Zero-shot Visual Classification) |
| Top-1 Accuracy of zero-shot transfer of ALIGN to image classification on ImageNet and its variants. | definition/direction/unit from same section | p. 5 (5.2. Zero-shot Visual Classification) |
| With frozen features, ALIGN slightly outperforms CLIP and achieves SOTA result of 85.5% top-1 accuracy. | definition/direction/unit from same section | p. 6 (5.2. Zero-shot Visual Classification) |
| After fine-tuning ALIGN achieves higher accuracy than BiT and ViT models, and is only worse than Meta Pseudo Labels which requires deeper interaction between ... | definition/direction/unit from same section | p. 6 (5.2. Zero-shot Visual Classification) |
| Figure 3. Zero-shot image-text retrieval and ImageNet KNN accuracy@1 with different image and text encoder sizes. | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| During fine-tuning, the same loss function is used. | definition/direction/unit from same section | p. 4 (5.1. Image-Text Matching & Retrieval) |
| The learning rate is warmed up linearly to 1e-3 from zero in 10k steps, and then linearly decay to zero in 1.2M steps (∼12 ... | definition/direction/unit from same section | p. 4 (5. Experiments and Results) |
| Table 11. Multimodal retrieval performance on Multi30K dataset. The metric is the mean Recall (mR). | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| So we list the baseline results in (Foret et al., 2021) without using SAM optimization for a fairer comparison. | comparison identity and matched condition | p. 6 (5.2. Zero-shot Visual Classification) |
| In the zero-shot setting, ALIGN gets more than 7% improvement in image retrieval task compared to the previous SOTA, CLIP (Radford et al., 2021). | comparison identity and matched condition | p. 4 (5.1. Image-Text Matching & Retrieval) |
| With frozen features, ALIGN slightly outperforms CLIP and achieves SOTA result of 85.5% top-1 accuracy. | comparison identity and matched condition | p. 6 (5.2. Zero-shot Visual Classification) |
| With fine-tuning, ALIGN outperforms all existing methods by a large margin, including those that employ more complex cross-modal attention layers such as ImageBERT (Qi ... | comparison identity and matched condition | p. 4 (5.1. Image-Text Matching & Retrieval) |
| ALIGN is compared with VSE++ (Faghri et al., 2018), VSRN (Li et al., 2019), DEI2T (Parekh et al., 2021), and DET2T+I2T (Parekh et al., ... | comparison identity and matched condition | p. 5 (5.1. Image-Text Matching & Retrieval) |
| For instance, the improvements on text-to-text and image-to-image retrieval tasks (in particular the former) are less significant compared to those on image-to-text and text-to-image ... | comparison identity and matched condition | p. 5 (5.1. Image-Text Matching & Retrieval) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1. A summary of our method, ALIGN. Visual and language representations are jointly learned from noisy image alt-text data. The representations can be ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| The image encoder is trained at resolution of 289 × 289 pixels no matter what EfficientNet variant is used. | component/input/data sensitivity | p. 4 (5. Experiments and Results) |
| Unless in the ablation study, we use the results of ALIGN where the image encoder is EfficientNet-L2 and the text encoder is BERT-Large. | component/input/data sensitivity | p. 4 (5. Experiments and Results) |
| Top-1 Accuracy of zero-shot transfer of ALIGN to image classification on ImageNet and its variants. | component/input/data sensitivity | p. 5 (5.2. Zero-shot Visual Classification) |
| So we list the baseline results in (Foret et al., 2021) without using SAM optimization for a fairer comparison. | component/input/data sensitivity | p. 6 (5.2. Zero-shot Visual Classification) |
| Our result (average of three runs) is comparable to the SOTA results without tweaking on optimization algorithms. | component/input/data sensitivity | p. 6 (5.2. Zero-shot Visual Classification) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Moreover, such cross-modality matching naturally enables zero-shot image classification when feeding the classnames into the text encoder, achieving 76.4% top-1 accuracy in ImageNet without ... | With frozen features, ALIGN slightly outperforms CLIP and achieves SOTA result of 85.5% top-1 accuracy. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2. Zero-shot Visual Classification), p. 5 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval), p. 4 (5.1. Image-Text Matching & Retrieval), p. 5 (5.1. Image-Text Matching & Retrieval) |
| Primary metric/result | We find that such ensembling gives 2.9% improvement on ImageNet top-1 accuracy. | numeric claim only at cited anchor | p. 5 (5.2. Zero-shot Visual Classification) |

- Numeric sentences retained from the body:
- **p. 4 / 5. Experiments and Results - extractive body cue:** For BERT we use wordpiece sequence of maximum 64 tokens since the input texts are no longer than 20 unigrams.
- **p. 4 / 5. Experiments and Results - extractive body cue:** The learning rate is warmed up linearly to 1e-3 from zero in 10k steps, and then linearly decay to zero in 1.2M steps (∼12 epochs).
- **p. 5 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** Model STS SIS SITS Mean Avg avg ± std avg ± std avg ± std VSE++ 74.4±0.4 73.3±0.9 55.2±1.5 67.6 VSRN 73.0±0.4 70.1±1.0 60.4±1.3 67.8 ...
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** In both stages of training, we use a global batch size of 1024, SGD optimizer with momentum 0.9, and learning rate decayed every 30 epochs ...
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** When fine-tuning all layers with use the initial learning rate of 0.01, and use 10x smaller learning rate on the backbone network compared to the ...
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** In VTAB eval, we follow a hyper-parameter sweep as shown in the Appendix I in (Zhai et al., 2019) with 50 trials for each task.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We show that linear relationships between + "red" + "forest" + "desert" + "orange" + "blue" + "purple" + "from distance" + "beige" + ... | p. 8 (7. Analysis of Learned Embeddings) |
| body limitation/failure cue | Similar to CLIP, ALIGN shows great robustness on classification tasks with different image distributions. | p. 5 (5.2. Zero-shot Visual Classification) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In both stages of training, we use a global batch size of 1024, SGD optimizer with momentum 0.9, and learning rate decayed every 30 ... | p. 6 (5.2. Zero-shot Visual Classification) |
| The learning rate is warmed up linearly to 1e-3 from zero in 10k steps, and then linearly decay to zero in 1.2M steps (∼12 ... | p. 4 (5. Experiments and Results) |
| We also reduce the initial learning rate to 1e-5 and train for 3K and 6K steps (with linear decay) respectively on Flickr30K and MSCOCO. | p. 4 (5.1. Image-Text Matching & Retrieval) |
| N is the batch size, and σ is the temperature to scale the logits. | p. 3 (4.1. Pre-training on Noisy Image-Text Pairs) |
| We use batch size 256 and weight decay 1e-5. | p. 6 (5.2. Zero-shot Visual Classification) |
| We pre-train ALIGN using a dual-encoder architecture. | p. 3 (4.1. Pre-training on Noisy Image-Text Pairs) |
| The class embedding is computed by averaging the embeddings of all templates followed by an L2-normalization. | p. 5 (5.2. Zero-shot Visual Classification) |
| If we directly feed the texts of classnames into the text encoder, ALIGN is able to classify images into candidate classes via image-text retrieval. | p. 5 (5.2. Zero-shot Visual Classification) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7. Analysis of Learned Embeddings - extractive body cue:** We show that linear relationships between + "red" + "forest" + "desert" + "orange" + "blue" + "purple" + "from distance" + "beige" + "red" ...
- **p. 5 / 5.2. Zero-shot Visual Classification - extractive body cue:** Similar to CLIP, ALIGN shows great robustness on classification tasks with different image distributions.

- **Evidence anchors reviewed:** datasets p. 6 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval), p. 3 (3. A Large-Scale Noisy Image-Text Dataset), p. 3 (3. A Large-Scale Noisy Image-Text Dataset), p. 4 (5.1. Image-Text Matching & Retrieval), metrics p. 5 (5.2. Zero-shot Visual Classification), p. 5 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification), p. 8 (Figure/Table caption), p. 4 (5.1. Image-Text Matching & Retrieval), baselines p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval), p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval), p. 5 (5.1. Image-Text Matching & Retrieval), p. 5 (5.1. Image-Text Matching & Retrieval), results p. 6 (5.2. Zero-shot Visual Classification), p. 5 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval), p. 4 (5.1. Image-Text Matching & Retrieval), p. 5 (5.1. Image-Text Matching & Retrieval).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
