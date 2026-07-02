# Problem

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Transformer and Language Models
- Tags: LLM, in-context learning
- Paper link: ./2020/NeurIPS/2020_NeurIPS_Language-Models-are-Few-Shot-Learners/paper.pdf
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.
- Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting.

## 해결하려는 문제
- Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task.
- Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art finetuning approaches.
- At the same time, we also identify some datasets where GPT-3’s few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training ...

## 선행 연구 / 배경 단서
- 3 2 Approach 2.1 Model and Architectures . . . . . . . . . . . . . . . . . . . . . ...
- 2.2 Training Dataset . . . . . . . . . . . . . . . . . . . . . . . . . ...
- 2.3 Training Process . . . . . . . . . . . . . . . . . . . . . . . . . ...
