# Flamingo: a Visual Language Model for Few-Shot Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (54 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2204.14198.
> PDF retrieval source: https://arxiv.org/pdf/2204.14198. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: Vision-Language Model, few-shot, alignment
- Official paper: https://arxiv.org/abs/2204.14198
- Full-text retrieval: https://arxiv.org/pdf/2204.14198
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (54 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual questionanswering.를 문제로 두고, In summary, our contributions are the following: (i) We introduce the Flamingo family of VLMs which can perform various multimodal tasks (such as captioning, visual dialogue, or visual question-answering) from only a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning ...
- **p. 1 / Abstract - extractive body cue:** We introduce Flamingo, a family of Visual Language Models (VLM) with this ability.
- **p. 1 / Abstract - extractive body cue:** We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and ...
- **p. 1 / Abstract - extractive body cue:** Thanks to their flexibility, Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow ...
- **p. 1 / Abstract - extractive body cue:** We perform a thorough evaluation of our models, exploring and measuring their ability to rapidly adapt to a variety of image and video tasks.
- **p. 3 / 1 Introduction - extractive body cue:** They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual questionanswering.
- **p. 3 / 1 Introduction - extractive body cue:** We show that the same can be done for image and video understanding tasks such as classification, captioning, or question-answering: these can be cast as ...

## Core Idea

- **p. 4 / 1 Introduction - extractive body cue:** In summary, our contributions are the following: (i) We introduce the Flamingo family of VLMs which can perform various multimodal tasks (such as captioning, visual ...
- **p. 3 / 1 Introduction - extractive body cue:** We introduce Flamingo, a Visual Language Model (VLM) that sets a new state of the art in few-shot learning on a wide range of open-ended ...
- **p. 3 / 1 Introduction - extractive body cue:** While initial progress has been made towards a similar capability in computer vision, the most widely used paradigm still consists of first pretraining on a ...
- **p. 6 / 2 Approach - extractive body cue:** We also collect a similar dataset but with videos instead of still images: VTP (Video & Text Pairs) consists of 27 million short videos (approximately ...
- **p. 6 / 2 Approach - extractive body cue:** To complement this dataset, we collect our own dataset of image and text pairs targeting better quality and longer descriptions: LTIP (Long Text & Image ...
- **p. 5 / 2 Approach - extractive body cue:** It takes as input a variable number of image or video features from the vision encoder and produces a fixed number of visual outputs (64), ...
- **p. 4 / 2 Approach - extractive body cue:** First, the Perceiver Resampler (Section 2.1) receives spatio-temporal features from the Vision Encoder (obtained from either an image or a video) and outputs a fixed ...
- **p. 5 / 2 Approach - extractive body cue:** Our vision encoder is a pretrained and frozen NormalizerFree ResNet (NFNet) [10] - we use the F6 model.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This section describes Flamingo: a visual language model that accepts text interleaved with images/videos as input and outputs free-form text. | 논문이 명시한 observation과 task input | p. 4 (2 Approach), p. 3 (1 Introduction) |
| State/latent | section, describes, Flamingo, visual, language, model, accepts, text, interleaved, images/videos, input, outputs | task state 또는 decision variable | p. 4 (2 Approach), p. 3 (1 Introduction), p. 5 (2 Approach) |
| Output/action | We introduce Flamingo, a Visual Language Model (VLM) that sets a new state of the art in few-shot learning on a wide range of open-ended vision and language tasks, simply by being ... | paper-specific output/action | p. 3 (1 Introduction), p. 5 (2 Approach), p. 5 (2 Approach) |
| Objective/outcome | In light of this trade-off, we maximize the number of added layers under hardware constraints and add a GATED XATTN-DENSE every fourth layer for Flamingo-9B and every seventh for Flamingo-80B. | primary task objective와 closed-loop behavior | p. 9 (Method), p. 5 (2 Approach), p. 8 (Method) |

## Main Claims and Actual Contribution

- **p. 4 / 1 Introduction - extractive body cue:** In summary, our contributions are the following: (i) We introduce the Flamingo family of VLMs which can perform various multimodal tasks (such as captioning, visual ...
- **p. 3 / 1 Introduction - extractive body cue:** We introduce Flamingo, a Visual Language Model (VLM) that sets a new state of the art in few-shot learning on a wide range of open-ended ...
- **p. 3 / 1 Introduction - extractive body cue:** While initial progress has been made towards a similar capability in computer vision, the most widely used paradigm still consists of first pretraining on a ...
- **p. 6 / 2 Approach - extractive body cue:** We also collect a similar dataset but with videos instead of still images: VTP (Video & Text Pairs) consists of 27 million short videos (approximately ...
- **p. 6 / 2 Approach - extractive body cue:** To complement this dataset, we collect our own dataset of image and text pairs targeting better quality and longer descriptions: LTIP (Long Text & Image ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Flamingo results overview. Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with no ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison to the state of the art. A single Flamingo model reaches the state of the art on a wide array of image ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent to perform gradient ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 3 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | For the DEV benchmarks that are used both to validate design decisions and hyperparameters, as well as to report final performance, we therefore use four subsets: validation support, validation query, test support ... | hardware/simulator version and reset protocol | p. 7 (3 Experiments), p. 7 (3 Experiments) |
| Dataset/benchmark | For the DEV benchmarks that are used both to validate design decisions and hyperparameters, as well as to report final performance, we therefore use four subsets: validation support, validation query, test support ... | role, split, size and leakage | p. 7 (3 Experiments), p. 7 (3 Experiments) |
| Metric | Table 6: Summary of the evaluation benchmarks. DEV benchmarks were used to validate general design decision of the Flamingo models. Gen. stands for generative task where we sample text from the VLM. ... | definition, denominator, direction and uncertainty | p. 31 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (3 Experiments) |
| Baseline/ablation | Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent to perform gradient updates on all training datasets. Finally, despite ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 35 (Figure/Table caption), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 42 / Figure/Table caption - extractive body cue:** Figure 13: Hallucinations and ungrounded guesses in open-ended visual question answering. Left: The model occasionally hallucinates by producing answers that seem likely given the text ...
- **p. 10 / 5 Discussion - extractive body cue:** We discuss the limitations of our work in more depth in Appendix D.1.
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 9: Training datasets. Mixture of training datasets of different formats. 𝑁corresponds to the number of visual inputs for a single example. For paired image ...
- **p. 35 / Figure/Table caption - extractive body cue:** Table 10. We ablate the size of our Resampler with three options: Small, Medium (default value for all Flamingo models), and Large. We see that ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Comparison to SotA when fine-tuning Flamingo. We fine-tune Flamingo on all nine tasks where Flamingo does not achieve SotA with few-shot learning. Flamingo ...

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual questionanswering.를 문제로 두고, In summary, our contributions are the following: (i) We introduce the Flamingo family of VLMs which can perform various multimodal tasks (such as captioning, visual dialogue, or visual question-answering) from only a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (2 Approach), p. 4 (2 Approach), p. 5 (2 Approach) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
