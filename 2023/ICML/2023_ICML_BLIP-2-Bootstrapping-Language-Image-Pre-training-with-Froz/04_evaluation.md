# Evaluation - BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2301.12597; PDF retrieval source: https://arxiv.org/pdf/2301.12597. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4. Experiment), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption)): Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training.

## Evaluation Body Digest

- **p. 6 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive PDF cue:** On the OK-VQA (Marino et al., 2019) dataset, BLIP-2 comes secondary to Flamingo80B.
- **p. 6 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive PDF cue:** BLIP-2 achieves state-of-the-art result on the VQAv2 (Goyal et al., 2017) and GQA (Hudson & Manning, 2019) datasets.
- **p. 7 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive PDF cue:** BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models Models #Trainable Params NoCaps Zero-shot (validation set) COCO Fine-tuned in-domain near-domain out-domain overall ...
- **p. 6 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive PDF cue:** We make a promising observation from Table 2: a stronger image encoder or a stronger LLM both lead to better performance.
- **p. 6 / 4. Experiment - extractive PDF cue:** Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Comparison with state-of-the-art image captioning methods on NoCaps and COCO Caption. All methods optimize the cross- entropy loss during finetuning. C: CIDEr, S: ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. The image-grounded text generation (ITG) loss improves image-text retrieval performance by enforcing the queries to extract language-relevant visual features.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. (Left) Model architecture of Q-Former and BLIP-2's first-stage vision-language representation learning objectives. We jointly optimize three objectives which enforce the queries (a set ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 4. Experiment (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4. Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training. | p. 6 (4. Experiment) |
| 4.1. Instructed Zero-shot Image-to-Text Generation | EMPIRICAL / SOURCE-REPORTED EVALUATION | (2) Within the same LLM family, larger models outperform smaller ones. | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4. Comparison with state-of-the-art models fine-tuned for visual question answering. of-the-art performance with significant improvement on NoCaps over existing methods, demonstrating strong gener- ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 6. The image-grounded text generation (ITG) loss improves image-text retrieval performance by enforcing the queries to extract language-relevant visual features. | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5. Effect of vision-language representation learning on vision-to-language generative learning. Without representation learning, the Q-Former fails the bridge the modality gap, leading to ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive PDF cue:** On the OK-VQA (Marino et al., 2019) dataset, BLIP-2 comes secondary to Flamingo80B.
- **p. 6 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive PDF cue:** BLIP-2 achieves state-of-the-art result on the VQAv2 (Goyal et al., 2017) and GQA (Hudson & Manning, 2019) datasets.
- **p. 7 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive PDF cue:** BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models Models #Trainable Params NoCaps Zero-shot (validation set) COCO Fine-tuned in-domain near-domain out-domain overall ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview of BLIP-2's framework. We pre-train a lightweight Querying Transformer following a two-stage strat- egy to bridge the modality gap. The first stage ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. (Left) Model architecture of Q-Former and BLIP-2's first-stage vision-language representation learning objectives. We jointly optimize three objectives which enforce the queries (a set ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. BLIP-2's second-stage vision-to-language generative pre-training, which bootstraps from frozen large language models (LLMs). (Top) Bootstrapping a decoder-based LLM (e.g. OPT). (Bottom) Bootstrapping an ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Selected examples of instructed zero-shot image-to-text generation using a BLIP-2 model w/ ViT-g and FlanT5XXL, where it shows a wide range of capabilities ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Overview of BLIP-2 results on various zero-shot vision-language tasks. Compared with previous state-of-the-art models. BLIP-2 achieves the highest zero-shot performance while requiring the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison with state-of-the-art methods on zero-shot visual question answering.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Comparison with state-of-the-art image captioning methods on NoCaps and COCO Caption. All methods optimize the cross- entropy loss during finetuning. C: CIDEr, S: ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Effect of vision-language representation learning on vision-to-language generative learning. Without representation learning, the Q-Former fails the bridge the modality gap, leading to significantly ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | On the OK-VQA (Marino et al., 2019) dataset, BLIP-2 comes secondary to Flamingo80B. | embodiment, simulator version and control stack | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Task/environment | BLIP-2 achieves state-of-the-art result on the VQAv2 (Goyal et al., 2017) and GQA (Hudson & Manning, 2019) datasets. | reset, timeout, object/scene variation | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 7 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 2 (3.1. Model Architecture), p. 4 (3.2. Bootstrap Vision-Language Representation) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 4 (3.2. Bootstrap Vision-Language Representation), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We make a promising observation from Table 2: a stronger image encoder or a stronger LLM both lead to better performance. | definition/direction/unit from same section | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training. | definition/direction/unit from same section | p. 6 (4. Experiment) |
| Table 3. Comparison with state-of-the-art image captioning methods on NoCaps and COCO Caption. All methods optimize the cross- entropy loss during finetuning. C: CIDEr, ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 6. The image-grounded text generation (ITG) loss improves image-text retrieval performance by enforcing the queries to extract language-relevant visual features. | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 2. (Left) Model architecture of Q-Former and BLIP-2's first-stage vision-language representation learning objectives. We jointly optimize three objectives which enforce the queries (a ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Table 4. Comparison with state-of-the-art models fine-tuned for visual question answering. of-the-art performance with significant improvement on NoCaps over existing methods, demonstrating strong gener- ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training. | comparison identity and matched condition | p. 6 (4. Experiment) |
| (2) Within the same LLM family, larger models outperform smaller ones. | comparison identity and matched condition | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Table 3. Comparison with state-of-the-art image captioning methods on NoCaps and COCO Caption. All methods optimize the cross- entropy loss during finetuning. C: CIDEr, ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 4. Comparison with state-of-the-art models fine-tuned for visual question answering. of-the-art performance with significant improvement on NoCaps over existing methods, demonstrating strong gener- ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 5. Comparison with state-of-the-art image-text retrieval methods, finetuned on COCO and zero-shot transferred to Flickr30K. COCO finetuning objectives Image →Text Text →Image R@1 ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 5. Effect of vision-language representation learning on vision-to-language generative learning. Without representation learning, the Q-Former fails the bridge the modality gap, leading to ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models Models #Trainable Params NoCaps Zero-shot (validation set) COCO Fine-tuned in-domain near-domain out-domain ... | component/input/data sensitivity | p. 7 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Table 8. Hyperparameters for fine-tuning BLIP-2 with ViT-g on VQA. Image Encoder ViT-L/14 ViT-g/14 Fine-tuning epochs 5 Warmup steps 1000 | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Table 9. Hyperparameters for fine-tuning BLIP-2 on COCO image-text retrieval. albert einstein - the world is a book, and those who do not travel ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To achieve effective vision-language alignment with frozen unimodal models, we propose a Querying Transformer (QFormer) pre-trained with a new two-stage pre-training strategy. | Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4. Experiment), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | (2) Within the same LLM family, larger models outperform smaller ones. | numeric claim only at cited anchor | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive PDF cue:** It outperforms Flamingo80B by 8.7% on VQAv2, despite having 54x fewer trainable parameters.
- **p. 4 / 3.4. Model Pre-training - extractive PDF cue:** We use images of size 224×224, augmented with random resized cropping and horizontal flipping.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The LLMs cannot learn from it the correlation among multiple image-text pairs in a single sequence. | p. 8 (5. Limitation) |
| body limitation/failure cue | We aim to create a similar dataset in future work. | p. 8 (5. Limitation) |
| body limitation/failure cue | Figure 5. Effect of vision-language representation learning on vision-to-language generative learning. Without representation learning, the Q-Former fails the bridge the modality gap, leading to ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use a cosine learning rate decay with a peak learning rate of 1e-4 and a linear warmup of 2k steps. | p. 4 (3.4. Model Pre-training) |
| The minimum learning rate at the second stage is 5e-5. | p. 4 (3.4. Model Pre-training) |
| BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models The audi e-tron quattro concept is a plug-in hybrid electric sports car ... | p. 5 (3.4. Model Pre-training) |
| We make a promising observation from Table 2: a stronger image encoder or a stronger LLM both lead to better performance. | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models Models #Trainable Params NoCaps Zero-shot (validation set) COCO Fine-tuned in-domain near-domain out-domain ... | p. 7 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Due to the use of a frozen image encoder, we can fit more samples per GPU compared to end-to-end methods. | p. 3 (3.2. Bootstrap Vision-Language Representation) |
| It extracts a fixed number of output features from the image encoder, independent of input image resolution. | p. 2 (3.1. Model Architecture) |
| We propose Q-Former as the trainable module to bridge the gap between a frozen image encoder and a frozen LLM. | p. 2 (3.1. Model Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Limitation - extractive PDF cue:** The LLMs cannot learn from it the correlation among multiple image-text pairs in a single sequence.
- **p. 8 / 5. Limitation - extractive PDF cue:** We aim to create a similar dataset in future work.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Effect of vision-language representation learning on vision-to-language generative learning. Without representation learning, the Q-Former fails the bridge the modality gap, leading to significantly ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 7 (4.1. Instructed Zero-shot Image-to-Text Generation), metrics p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 6 (4. Experiment), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 6 (4. Experiment), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 6 (4. Experiment), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
