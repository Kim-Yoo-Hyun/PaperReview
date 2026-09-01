# Evaluation - BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.12086; PDF retrieval source: https://arxiv.org/pdf/2201.12086. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 4 (4.2. Effect of CapFilt), p. 4 (4.2. Effect of CapFilt), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Figure/Table caption)): Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference and lack of temporal mod- eling, our models ...

## Evaluation Body Digest

- **p. 4 / 4.2. Effect of CapFilt - extractive PDF cue:** In Table 1, we compare models pre-trained on different datasets to demonstrate the efficacy of CapFilt on downstream tasks, including image-text retrieval and image captioning ...
- **p. 4 / 4.1. Pre-training Details - extractive PDF cue:** We use the same pre-training dataset as Li et al.
- **p. 5 / 4.2. Effect of CapFilt - extractive PDF cue:** BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation Pre-train dataset Bootstrap Vision backbone Retrieval-FT (COCO) Retrieval-ZS (Flickr) Caption-FT (COCO) Caption-ZS (NoCaps)
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference and lack of ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We use a Captioner (Cap) to generate synthetic captions for web images, and a Filter (Filt) to remove noisy captions. collected from the ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Pre-training model architecture and objectives of BLIP (same parameters have the same color). We propose multimodal mixture of encoder-decoder, a unified vision-language model ...
- **p. 4 / 4.1. Pre-training Details - extractive PDF cue:** The learning rate is warmed-up to 3e-4 (ViT-B) / 2e-4 (ViT-L) and decayed linearly with a rate of 0.85.
- **p. 4 / 4.2. Effect of CapFilt - extractive PDF cue:** Furthermore, by using a large captioner and filter with ViT-L, performance of the base model can also be improved.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 4. Experiments and Discussions (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference and lack ... | p. 8 (Figure/Table caption) |
| 4.2. Effect of CapFilt | SYSTEM / EVALUATION SCOPE UNRESOLVED | Furthermore, by using a large captioner and filter with ViT-L, performance of the base model can also be improved. | p. 4 (4.2. Effect of CapFilt) |
| 4.2. Effect of CapFilt | SYSTEM / EVALUATION SCOPE UNRESOLVED | When only the captioner or the filter is applied to the dataset with 14M images, performance improvement can be observed. | p. 4 (4.2. Effect of CapFilt) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 6. Zero-shot image-text retrieval results on Flickr30K. layers except for SA leads to better performance compared to not sharing, while also reducing the ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 12. The original web texts are replicated to have the same number of samples per epoch as the bootstrapped dataset. Results verify that ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 4.2. Effect of CapFilt - extractive PDF cue:** In Table 1, we compare models pre-trained on different datasets to demonstrate the efficacy of CapFilt on downstream tasks, including image-text retrieval and image captioning ...
- **p. 4 / 4.1. Pre-training Details - extractive PDF cue:** We use the same pre-training dataset as Li et al.
- **p. 5 / 4.2. Effect of CapFilt - extractive PDF cue:** BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation Pre-train dataset Bootstrap Vision backbone Retrieval-FT (COCO) Retrieval-ZS (Flickr) Caption-FT (COCO) Caption-ZS (NoCaps)

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We use a Captioner (Cap) to generate synthetic captions for web images, and a Filter (Filt) to remove noisy captions. collected from the ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Pre-training model architecture and objectives of BLIP (same parameters have the same color). We propose multimodal mixture of encoder-decoder, a unified vision-language model ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Learning framework of BLIP. We introduce a captioner to produce synthetic captions for web images, and a filter to remove noisy image-text pairs. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Evaluation of the effect of the captioner (C) and filter (F) for dataset bootstrapping. Downstream tasks include image-text retrieval and image captioning with ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Examples of the web text Tw and the synthetic text Ts. Green texts are accepted by the filter, whereas red texts are rejected. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison between beam search and nucleus sampling for synthetic caption generation. Models are pre-trained on 14M images. Layers shared #parameters Retrieval-FT (COCO) Retrieval-ZS ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 3. Comparison between different parameter sharing strategies for the text encoder and decoder during pre-training. In Figure 4, we show some example captions and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Effect of sharing parameters between the captioner and filter. Models are pre-trained on 14M images.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In Table 1, we compare models pre-trained on different datasets to demonstrate the efficacy of CapFilt on downstream tasks, including image-text retrieval and image ... | embodiment, simulator version and control stack | p. 4 (4.2. Effect of CapFilt), p. 4 (4.1. Pre-training Details) |
| Task/environment | We use the same pre-training dataset as Li et al. | reset, timeout, object/scene variation | p. 4 (4.1. Pre-training Details), p. 5 (4.2. Effect of CapFilt) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3.1. Model Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference and lack ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. We use a Captioner (Cap) to generate synthetic captions for web images, and a Filter (Filt) to remove noisy captions. collected from ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Pre-training model architecture and objectives of BLIP (same parameters have the same color). We propose multimodal mixture of encoder-decoder, a unified vision-language ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| The learning rate is warmed-up to 3e-4 (ViT-B) / 2e-4 (ViT-L) and decayed linearly with a rate of 0.85. | definition/direction/unit from same section | p. 4 (4.1. Pre-training Details) |
| Furthermore, by using a large captioner and filter with ViT-L, performance of the base model can also be improved. | definition/direction/unit from same section | p. 4 (4.2. Effect of CapFilt) |
| Table 7. Comparison with state-of-the-art image captioning methods on NoCaps and COCO Caption. All methods optimize the cross- entropy loss during finetuning. C: CIDEr, ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 1. Evaluation of the effect of the captioner (C) and filter (F) for dataset bootstrapping. Downstream tasks include image-text retrieval and image captioning ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 3. Comparison between different parameter sharing strategies for the text encoder and decoder during pre-training. In Figure 4, we show some example captions ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference and lack ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| When applied together, their effects compliment each other, leading to substantial improvements compared to using the original noisy web texts. | comparison identity and matched condition | p. 4 (4.2. Effect of CapFilt) |
| Table 5. Comparison with state-of-the-art image-text retrieval methods, finetuned on COCO and Flickr30K datasets. BLIPCapFilt-L pre-trains a model with ViT-B backbone using a dataset ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 8. Comparison with state-of-the-art methods on VQA and NLVR2. ALBEF performs an extra pre-training step for NLVR2. SimVLM† uses 13× more training data ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 7. Comparison with state-of-the-art image captioning methods on NoCaps and COCO Caption. All methods optimize the cross- entropy loss during finetuning. C: CIDEr, ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 9. Comparison with state-of-the-art methods on VisDial v1.0 validation set. VD-ViLBERT† (Murahari et al., 2020) pre-trains ViLBERT (Lu et al., 2019) with additional ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Comparison between different parameter sharing strategies for the text encoder and decoder during pre-training. In Figure 4, we show some example captions ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| We explore two variants of ViTs: ViT-B/16 and ViT-L/16. | component/input/data sensitivity | p. 4 (4.1. Pre-training Details) |
| Table 1. Evaluation of the effect of the captioner (C) and filter (F) for dataset bootstrapping. Downstream tasks include image-text retrieval and image captioning ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 4. Effect of sharing parameters between the captioner and filter. Models are pre-trained on 14M images. | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 1. We use a Captioner (Cap) to generate synthetic captions for web images, and a Filter (Filt) to remove noisy captions. collected from ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Figure 3. Learning framework of BLIP. We introduce a captioner to produce synthetic captions for web images, and a filter to remove noisy image-text ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation. | Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference and lack ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 4 (4.2. Effect of CapFilt), p. 4 (4.2. Effect of CapFilt), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Primary metric/result | Furthermore, by using a large captioner and filter with ViT-L, performance of the base model can also be improved. | numeric claim only at cited anchor | p. 4 (4.2. Effect of CapFilt) |

- Numeric sentences retained from the body:
- **p. 4 / 4.1. Pre-training Details - extractive PDF cue:** We pre-train the model for 20 epochs using a batch size of 2880 (ViT-B) / 2400 (ViT-L).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 13. Continue training the pre-trained model offers less gain compared to training a new model with the bootstrapped dataset. from the previous pre-trained ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Table 6. Zero-shot image-text retrieval results on Flickr30K. layers except for SA leads to better performance compared to not sharing, while also reducing the ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We pre-train the model for 20 epochs using a batch size of 2880 (ViT-B) / 2400 (ViT-L). | p. 4 (4.1. Pre-training Details) |
| The learning rate is warmed-up to 3e-4 (ViT-B) / 2e-4 (ViT-L) and decayed linearly with a rate of 0.85. | p. 4 (4.1. Pre-training Details) |
| Image-Text Contrastive Loss (ITC) activates the unimodal encoder. | p. 3 (3.2. Pre-training Objectives) |
| Image-Text Matching Loss (ITM) activates the imagegrounded text encoder. | p. 3 (3.2. Pre-training Objectives) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 13. Continue training the pre-trained model offers less gain compared to training a new model with the bootstrapped dataset. from the previous pre-trained model, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 6. Zero-shot image-text retrieval results on Flickr30K. layers except for SA leads to better performance compared to not sharing, while also reducing the model ...

- **PDF anchors reviewed:** datasets p. 4 (4.2. Effect of CapFilt), p. 4 (4.1. Pre-training Details), p. 5 (4.2. Effect of CapFilt), metrics p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), p. 4 (4.1. Pre-training Details), p. 4 (4.2. Effect of CapFilt), p. 7 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 4 (4.2. Effect of CapFilt), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 4 (4.2. Effect of CapFilt), p. 4 (4.2. Effect of CapFilt), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
