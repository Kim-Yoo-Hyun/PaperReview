# ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2102.05918.
> PDF retrieval source: https://arxiv.org/pdf/2102.05918. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: Vision-Language Model, alignment, representation
- Official paper: https://arxiv.org/abs/2102.05918
- Full-text retrieval: https://arxiv.org/pdf/2102.05918
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Curation of such pre-training datasets requires heavy work on data gathering, sampling, and human annotation, and hence is difficult to scale.를 문제로 두고, Moreover, such cross-modality matching naturally enables zero-shot image classification when feeding the classnames into the text encoder, achieving 76.4% top-1 accuracy in ImageNet without using any of its training samples.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Pre-trained representations are becoming crucial for many NLP and perception tasks.
- **p. 1 / Abstract - extractive body cue:** While representation learning in NLP has transitioned to training on raw text without human annotations, visual and vision-language representations still rely heavily on curated training ...
- **p. 1 / Abstract - extractive body cue:** For vision applications, representations are mostly learned using datasets with explicit class labels such as ImageNet or OpenImages.
- **p. 1 / Abstract - extractive body cue:** For vision-language, popular datasets like Conceptual Captions, MSCOCO, or CLIP all involve a non-trivial data collection (and cleaning) process.
- **p. 1 / Abstract - extractive body cue:** This costly curation process limits the size of datasets and hence hinders the scaling of trained models.
- **p. 1 / 1. Introduction - extractive body cue:** Curation of such pre-training datasets requires heavy work on data gathering, sampling, and human annotation, and hence is difficult to scale.
- **p. 1 / 1. Introduction - extractive body cue:** In the existing literature, visual and vision-language representation learning are mostly studied separately with different training data sources.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Moreover, such cross-modality matching naturally enables zero-shot image classification when feeding the classnames into the text encoder, achieving 76.4% top-1 accuracy in ImageNet without using ...
- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** The model consists of a pair of image and text encoders with a cosine-similarity combination function at the top.
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** (2020), we also evaluate the robustness of our model on Visual Task Adaptation Benchmark (VTAB) (Zhai et al., 2019) which consists of 19 diverse (covering ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** The dataset consists of 31,783 images with 5 captions per image in English and German and 1 caption per image in French and Czech.
- **p. 1 / 1. Introduction - extractive body cue:** We show that visual and visionlanguage representations pre-trained on our exascale dataset achieve very strong performance on a wide range of tasks.
- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** We use EfficientNet with global pooling (without training the 1x1 conv layer in the classification head) as the image encoder and BERT with [CLS] token ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** Model training follows the exact English configuration.
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** We first apply zero-shot transfer of ALIGN to visual classification tasks on ImageNet ILSVRC-2012 benchmark (Deng et al., 2009) and its variants including ImageNet-R(endition) (Hendrycks ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The aligned image and text representations are naturally suited for cross-modality matching/retrieval tasks and achieve state-of-the-art (SOTA) results in corresponding benchmarks. | 논문이 명시한 observation과 task input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | aligned, image, text, representations, naturally, suited, cross-modality, matching/retrieval, tasks, achieve, state-of-the-art, SOTA | task state 또는 decision variable | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Output/action | In this work, we leverage a dataset of over one billion noisy image alt-text pairs to scale visual and vision-language representation learning. | paper-specific output/action | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | We minimize the sum of two losses: one for image-to-text classification Li2t = -1 N N X i log exp(x⊤ i yi/σ) PN j=1 exp(x⊤ i yj/σ) (1) and the other for ... | primary task objective와 closed-loop behavior | p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 9 (8. Multilingual ALIGN Model) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Moreover, such cross-modality matching naturally enables zero-shot image classification when feeding the classnames into the text encoder, achieving 76.4% top-1 accuracy in ImageNet without using ...
- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** The model consists of a pair of image and text encoders with a cosine-similarity combination function at the top.
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** (2020), we also evaluate the robustness of our model on Visual Task Adaptation Benchmark (VTAB) (Zhai et al., 2019) which consists of 19 diverse (covering ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** The dataset consists of 31,783 images with 5 captions per image in English and German and 1 caption per image in French and Czech.
- **p. 1 / 1. Introduction - extractive body cue:** We show that visual and visionlanguage representations pre-trained on our exascale dataset achieve very strong performance on a wide range of tasks.
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** With frozen features, ALIGN slightly outperforms CLIP and achieves SOTA result of 85.5% top-1 accuracy.
- **p. 5 / 5.2. Zero-shot Visual Classification - extractive body cue:** We find that such ensembling gives 2.9% improvement on ImageNet top-1 accuracy.
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** After fine-tuning ALIGN achieves higher accuracy than BiT and ViT models, and is only worse than Meta Pseudo Labels which requires deeper interaction between ImageNet ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (5.2. Zero-shot Visual Classification), p. 5 (5.2. Zero-shot Visual Classification) |
| Embodiment/environment | After the sweep, the selected hyperparameters are used to train on the combined training and validation splits of 1000 images for each task. | hardware/simulator version and reset protocol | p. 6 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification) |
| Dataset/benchmark | Specifically, for Flickr30K, we evaluate on the standard 1K test set, and finetune on the 30k training set. | role, split, size and leakage | p. 6 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval), p. 3 (3. A Large-Scale Noisy Image-Text Dataset) |
| Metric | We find that such ensembling gives 2.9% improvement on ImageNet top-1 accuracy. | definition, denominator, direction and uncertainty | p. 5 (5.2. Zero-shot Visual Classification), p. 5 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification) |
| Baseline/ablation | So we list the baseline results in (Foret et al., 2021) without using SAM optimization for a fairer comparison. | fair input/data/compute/action matching | p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval), p. 6 (5.2. Zero-shot Visual Classification) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7. Analysis of Learned Embeddings - extractive body cue:** We show that linear relationships between + "red" + "forest" + "desert" + "orange" + "blue" + "purple" + "from distance" + "beige" + "red" ...
- **p. 5 / 5.2. Zero-shot Visual Classification - extractive body cue:** Similar to CLIP, ALIGN shows great robustness on classification tasks with different image distributions.

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Curation of such pre-training datasets requires heavy work on data gathering, sampling, and human annotation, and hence is difficult to scale.를 문제로 두고, Moreover, such cross-modality matching naturally enables zero-shot image classification when feeding the classnames into the text encoder, achieving 76.4% top-1 accuracy in ImageNet without using any of its training samples.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 4 (4.3. Transferring to Visual Classification), p. 9 (8. Multilingual ALIGN Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
