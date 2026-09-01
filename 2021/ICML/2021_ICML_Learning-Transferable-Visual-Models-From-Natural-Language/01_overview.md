# Learning Transferable Visual Models From Natural Language Supervision

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2103.00020.
> PDF retrieval source: https://arxiv.org/pdf/2103.00020. Reading tracker status/evidence was not changed.

- Year/Venue: 2021 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: CLIP, Vision-Language Model, alignment
- Official paper: https://arxiv.org/abs/2103.00020
- Full-text retrieval: https://arxiv.org/pdf/2103.00020
- Code/Project: https://github.com/openai/CLIP
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 upstream 문제를 이해하기 위해 읽는다. 본문은 Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs.를 문제로 두고, Pre-training methods which learn directly from raw text have revolutionized NLP over the last few years (Dai & Le, 2015; Peters et al., 2018; Howard & Ruder, 2018; Radford et al., 2018; ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories.
- **p. 1 / Abstract - extractive body cue:** This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept.
- **p. 1 / Abstract - extractive body cue:** Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision.
- **p. 1 / Abstract - extractive body cue:** We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image ...
- **p. 1 / Abstract - extractive body cue:** After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks.
- **p. 2 / 1. Introduction and Motivating Work - extractive body cue:** Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs.
- **p. 2 / 1. Introduction and Motivating Work - extractive body cue:** In this work, we close this gap and study the behaviors of image classifiers trained with natural language supervision at large scale.

## Core Idea

- **p. 1 / 1. Introduction and Motivating Work - extractive body cue:** Pre-training methods which learn directly from raw text have revolutionized NLP over the last few years (Dai & Le, 2015; Peters et al., 2018; Howard ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Learning from natural language also has an important advantage over most unsupervised or self-supervised learning approaches in that it doesn't "just" learn a representation but ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** At the core of our approach is the idea of learning perception from supervision contained in natural language.
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** In Figure 2 we show that a 63 million parameter transformer language model, which already uses twice the compute of its ResNet-50 image encoder, learns ...
- **p. 1 / 1. Introduction and Motivating Work - extractive body cue:** The development of "text-to-text" as a standardized input-output interface (McCann et al., 2018; Radford et al., 2019; Raffel et al., 2019) has enabled taskagnostic architectures ...
- **p. 5 / 2.4. Choosing and Scaling a Model - extractive body cue:** Learning Transferable Visual Models From Natural Language Supervision 5 # image_encoder - ResNet or Vision Transformer # text_encoder - CBOW or Text Transformer # I[n, ...
- **p. 4 / 2.4. Choosing and Scaling a Model - extractive body cue:** For the first, we use ResNet-50 (He et al., 2016a) as the base architecture for the image encoder due to its widespread adoption and proven ...
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** To our knowledge this batch construction technique and objective was first introduced in the area of deep metric learning as the multi-class N-pair loss Sohn ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The development of "text-to-text" as a standardized input-output interface (McCann et al., 2018; Radford et al., 2019; Raffel et al., 2019) has enabled taskagnostic architectures to zero-shot transfer to downstream datasets removing ... | 논문이 명시한 observation과 task input | p. 1 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work) |
| State/latent | development, text-to-text, standardized, input-output, interface, McCann, Radford, Raffel, enabled, taskagnostic, architectures, zero-shot | task state 또는 decision variable | p. 1 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (2.1. Natural Language Supervision) |
| Output/action | When fine-tuned to ImageNet these pre-trained models increased accuracy by over 5% and improved the overall state of the art at the time. | paper-specific output/action | p. 2 (1. Introduction and Motivating Work), p. 3 (2.1. Natural Language Supervision), p. 4 (2.3. Selecting an Efficient Pre-Training Method) |
| Objective/outcome | To our knowledge this batch construction technique and objective was first introduced in the area of deep metric learning as the multi-class N-pair loss Sohn (2016), was popularized for contrastive representation learning ... | primary task objective와 closed-loop behavior | p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.5. Training) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction and Motivating Work - extractive body cue:** Pre-training methods which learn directly from raw text have revolutionized NLP over the last few years (Dai & Le, 2015; Peters et al., 2018; Howard ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Learning from natural language also has an important advantage over most unsupervised or self-supervised learning approaches in that it doesn't "just" learn a representation but ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** At the core of our approach is the idea of learning perception from supervision contained in natural language.
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** In Figure 2 we show that a 63 million parameter transformer language model, which already uses twice the compute of its ResNet-50 image encoder, learns ...
- **p. 1 / 1. Introduction and Motivating Work - extractive body cue:** The development of "text-to-text" as a standardized input-output interface (McCann et al., 2018; Radford et al., 2019; Raffel et al., 2019) has enabled taskagnostic architectures ...
- **p. 8 / 3.1.4. PROMPT ENGINEERING AND ENSEMBLING - extractive body cue:** Learning Transferable Visual Models From Natural Language Supervision 8 Similar to the "prompt engineering" discussion around GPT3 (Brown et al., 2020; Gao et al., 2020), ...
- **p. 6 / 3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS - extractive body cue:** The best CLIP model improves accuracy on ImageNet from a proof of concept 11.5% to 76.2% and matches the performance of the original ResNet-50 despite ...
- **p. 13 / 3.3. Robustness to Natural Distribution Shift - extractive body cue:** They propose this distinction because in part because they find that while several techniques have been demonstrated to improve performance on synthetic distribution shifts, they ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS) |
| Embodiment/environment | The 20 datasets with at least 16 examples per class were used in this analysis. we see that zero-shot CLIP is quite weak on several specialized, complex, or abstract tasks such as ... | hardware/simulator version and reset protocol | p. 9 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION) |
| Dataset/benchmark | This evaluation suite, detailed in Appendix A includes datasets representing the aforementioned tasks, German Traffic Signs Recognition Benchmark (Stallkamp et al., 2011), as well as several other datasets adapted from VTAB (Zhai ... | role, split, size and leakage | p. 9 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION), p. 11 (3.2. Representation Learning), p. 16 (3.3. Robustness to Natural Distribution Shift) |
| Metric | On aYahoo, CLIP achieves a 95% reduction in the number of errors, and on SUN, CLIP more than doubles the accuracy of Visual N-Grams. | definition, denominator, direction and uncertainty | p. 7 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 13 (3.3. Robustness to Natural Distribution Shift), p. 14 (Figure/Table caption) |
| Baseline/ablation | Compared to the baseline of using contextless class names, prompt engineering and ensembling boost zero-shot classification performance by almost 5 points on average across 36 datasets. | fair input/data/compute/action matching | p. 7 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 8 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING) |

## Explicit Limitations and Failure Boundary

- **p. 25 / 7.3. Future Work - extractive body cue:** This process of characterization can help researchers increase the likelihood models are used beneficially by: • Identifying potentially beneficial downstream uses of models early in ...
- **p. 11 / 3.2. Representation Learning - extractive body cue:** Fine-tuning, because it adapts representations to each dataset during the fine-tuning phase, can compensate for and potentially mask failures to learn general and robust representations ...
- **p. 18 / 6. Limitations - extractive body cue:** There are still many limitations to CLIP.
- **p. 20 / 6. Limitations - extractive body cue:** Our methodology has several significant limitations.
- **p. 20 / 6. Limitations - extractive body cue:** In our work, we fall back to fitting linear classifiers on top of CLIP's features.
- **p. 11 / 3.2. Representation Learning - extractive body cue:** Linear classifiers, because of their limited flexibility, instead highlight these failures and provide clear feedback during development.
- **p. 13 / 3.3. Robustness to Natural Distribution Shift - extractive body cue:** To what degree are these failures attributable to deep learning, ImageNet, or some combination of the two?

## Why Read It

VLA and generalist robot policies의 upstream 문제를 이해하기 위해 읽는다. 본문은 Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs.를 문제로 두고, Pre-training methods which learn directly from raw text have revolutionized NLP over the last few years (Dai & Le, 2015; Peters et al., 2018; Howard & Ruder, 2018; Radford et al., 2018; ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (1. Introduction and Motivating Work), p. 6 (3.1.1. MOTIVATION), p. 6 (3.1.1. MOTIVATION), p. 5 (2.4. Choosing and Scaling a Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
