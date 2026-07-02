# Evaluation

- Year/Venue: 2019 / NAACL
- Category: Foundations: Transformer and Language Models
- Tags: LLM, Transformer, pretraining
- Paper link: ./2019/NAACL/2019_NAACL_BERT-Pre-training-of-Deep-Bidirectional-Transformers-for-L/paper.pdf
- Code/Project: https://github.com/google-research/bert
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet

## Metrics
- accuracy

## Evaluation Protocol and Results
- In this section, we present BERT fine-tuning results on 11 NLP tasks.
- 4.1 GLUE The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks.
- It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute ...
- As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
