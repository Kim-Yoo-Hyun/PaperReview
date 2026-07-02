# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

- Year/Venue: 2019 / NAACL
- Category: Foundations: Transformer and Language Models
- Tags: LLM, Transformer, pretraining
- Paper link: ./2019/NAACL/2019_NAACL_BERT-Pre-training-of-Deep-Bidirectional-Transformers-for-L/paper.pdf
- Code/Project: https://github.com/google-research/bert
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.
- There are two existing strategies for applying pre-trained language representations to downstream tasks: feature-based and fine-tuning.

## Core Idea
- We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- For example, in OpenAI GPT, the authors use a left-toright architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer (Vaswani ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute ...
- As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as ...
- In this section, we present BERT fine-tuning results on 11 NLP tasks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute ...
- As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as ...

## Abstract Cue
- We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
