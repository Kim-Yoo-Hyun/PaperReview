# Evaluation

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Transformer and Language Models
- Tags: LLM, in-context learning
- Paper link: ./2020/NeurIPS/2020_NeurIPS_Language-Models-are-Few-Shot-Learners/paper.pdf
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- BLEU
- accuracy
- ATE

## Evaluation Protocol and Results
- When the test set is private, our model is often too large to fit on the test server, so we report results on the development set.
- We do submit to the test server on a small number of datasets (SuperGLUE, TriviaQA, PiQa) where we were able to make submission work, and we submit only ...
- Final results are reported on the test set when publicly available, for each model size and learning setting (zero-, one-, and few-shot).
- For few-shot learning, we evaluate each example in the evaluation set by randomly drawing K examples from that task’s training set as conditioning, delimited by 1 or 2 ...
- Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art finetuning approaches.
- GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as ...

## Baselines
- On tasks that involve choosing one correct completion from several options (multiple choice), we provide K examples of context plus correct completion, followed by one example of context ...
- For most tasks we compare the per-token likelihood (to normalize for length), however on a small number of datasets (ARC, OpenBookQA, and RACE) we gain additional benefit as ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
