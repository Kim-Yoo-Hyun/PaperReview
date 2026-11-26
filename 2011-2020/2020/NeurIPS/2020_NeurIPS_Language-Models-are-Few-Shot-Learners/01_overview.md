# Language Models are Few-Shot Learners

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (75 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2005.14165.
> PDF retrieval source: https://arxiv.org/pdf/2005.14165. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / NeurIPS
- Authors: Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: LLM, in-context learning
- Official paper: https://arxiv.org/abs/2005.14165
- Full-text retrieval: https://arxiv.org/pdf/2005.14165
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (75 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

GPT-3는 자기회귀 언어 모델에 과제 설명과 소수의 예시를 문맥으로 주어, 가중치를 갱신하지 않고 여러 언어 과제를 수행한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a ...
- **p. 1 / Abstract - extractive body cue:** While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples.
- **p. 1 / Abstract - extractive body cue:** By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems ...
- **p. 1 / Abstract - extractive body cue:** Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art finetuning approaches.
- **p. 1 / Abstract - extractive body cue:** Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in ...
- **p. 4 / 1 Introduction - extractive body cue:** Aside from pointing to a conceptual limitation in our current NLP techniques, this adaptability has practical advantages - it allows humans to seamlessly mix together ...
- **p. 5 / 1 Introduction - extractive body cue:** We also show that in the few-shot setting, GPT-3 can generate synthetic news articles which human evaluators have difficulty distinguishing from human-generated articles.

## Core Idea

- **p. 7 / 2 Approach - extractive body cue:** The panels above show four methods for performing a task with a language model - fine-tuning is the traditional method, whereas zero-, one-, and few-shot, ...
- **p. 5 / 1 Introduction - extractive body cue:** Specifically, we evaluate GPT-3 on over two dozen NLP datasets, as well as several novel tasks designed to test rapid adaptation to tasks unlikely to ...
- **p. 5 / 1 Introduction - extractive body cue:** GPT-3 also displays one-shot and few-shot proficiency at tasks designed to test rapid adaption or on-the-fly reasoning, which include unscrambling words, performing arithmetic, and using ...
- **p. 4 / 1 Introduction - extractive body cue:** We show in-context learning performance on a simple task requiring the model to remove random symbols from a word, both with and without a natural ...
- **p. 6 / 1 Introduction - extractive body cue:** In Section 2, we describe our approach and methods for training GPT-3 and evaluating it.
- **p. 8 / 2 Approach - extractive body cue:** 2.1 Model and Architectures We use the same model and architecture as GPT-2 [RWC+19], including the modified initialization, pre-normalization, and reversible tokenization described therein, with ...
- **p. 9 / 2 Approach - extractive body cue:** To train the larger models without running out of memory, we use a mixture of model parallelism within each matrix multiply and model parallelism across ...
- **p. 6 / 2 Approach - extractive body cue:** As indicated by the name, few-shot learning as described here for language models is related to few-shot learning as used in other contexts in ML ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Recent work [RWC+19] attempts to do this via what we call "in-context learning", using the text input of a pretrained language model as a form of task specification: the model is conditioned ... | 논문이 명시한 observation과 task input | p. 4 (1 Introduction), p. 7 (2 Approach) |
| State/latent | Recent, RWC, attempts, what, call, in-context, learning, text, input, pretrained, language, model | task state 또는 decision variable | p. 4 (1 Introduction), p. 7 (2 Approach), p. 6 (2 Approach) |
| Output/action | Exact phrasings for all task descriptions, examples and prompts can be found in Appendix G. • Zero-Shot (0S) is the same as one-shot except that no demonstrations are allowed, and the model ... | paper-specific output/action | p. 7 (2 Approach), p. 6 (2 Approach), p. 7 (2 Approach) |
| Objective/outcome | Data are sampled without replacement during training (until an epoch boundary is reached) to minimize overfitting. | primary task objective와 closed-loop behavior | p. 43 (B Details of Model Training), p. 43 (B Details of Model Training), p. 8 (2 Approach) |

## Main Claims and Actual Contribution

- 같은 계열의 모델 크기를 바꾸며 문맥 학습 결과를 비교한다.
- 예시를 주지 않거나 하나 또는 여러 개를 주는 조건을 구분해 평가한다.

[저자 원문](https://proceedings.neurips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 12 (3 Results), p. 16 (Figure/Table caption) |
| Embodiment/environment | We omit the 4 Wikipedia-related tasks in that work because they are entirely contained in our training data, and we also omit the one-billion word benchmark due to a high fraction of ... | hardware/simulator version and reset protocol | p. 11 (3 Results), p. 29 (3 Results) |
| Dataset/benchmark | 3.7 SuperGLUE In order to better aggregate results on NLP tasks and compare to popular models such as BERT and RoBERTa in a more systematic way, we also evaluate GPT-3 on a ... | role, split, size and leakage | p. 11 (3 Results), p. 29 (3 Results), p. 18 (3 Results), p. 33 (3 Results) |
| Metric | All scores are F1 except results for RACE which report accuracy. a[JZC+19] b[JN20] c[AI19] d[QIA20] e[SPP+19] fine-tuned RoBERTa. | definition, denominator, direction and uncertainty | p. 18 (3 Results), p. 10 (2.4 Evaluation), p. 12 (3 Results) |
| Baseline/ablation | On DROP [DWD+19], a dataset testing discrete reasoning and numeracy in the context of reading comprehension, GPT-3 in a few-shot setting outperforms the fine-tuned BERT baseline from the original paper but is ... | fair input/data/compute/action matching | p. 18 (3 Results), p. 19 (3 Results), p. 18 (3 Results) |

## Explicit Limitations and Failure Boundary

- **p. 33 / 3 Results - extractive body cue:** An important limitation of our contamination analysis is that we cannot be sure that the clean subset is drawn from the same distribution as the ...
- **p. 41 / 8 Conclusion - extractive body cue:** Despite many limitations and weaknesses, these results suggest that very large language models may be an important ingredient in the development of adaptable, general language ...
- **p. 2 / 3 Results - extractive body cue:** 21 4 Measuring and Preventing Memorization Of Benchmarks 29 5 Limitations 33 6 Broader Impacts 34 6.1 Misuse of Language Models . . . . ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1.2: Larger models make increasingly efficient use of in-context information. We show in-context learning performance on a simple task requiring the model to remove ...
- **p. 20 / 3 Results - extractive body cue:** On COPA and ReCoRD GPT-3 achieves near-SOTA performance in the one-shot and few-shot settings, with COPA falling only a couple points short and achieving second ...
- **p. 24 / 3 Results - extractive body cue:** This suggests that the model really does appear to learn these tasks at test time, as the model cannot perform them zero-shot and their artificial ...
- **p. 32 / 3 Results - extractive body cue:** Unfortunately, we cannot rigorously prove this hypothesis.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 8 (2 Approach)이다.
