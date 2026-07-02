# Problem

- Year/Venue: 2019 / NAACL
- Category: Foundations: Transformer and Language Models
- Tags: LLM, Transformer, pretraining
- Paper link: ./2019/NAACL/2019_NAACL_BERT-Pre-training-of-Deep-Bidirectional-Transformers-for-L/paper.pdf
- Code/Project: https://github.com/google-research/bert
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.
- There are two existing strategies for applying pre-trained language representations to downstream tasks: feature-based and fine-tuning.

## 해결하려는 문제
- We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute ...
- As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as ...

## 선행 연구 / 배경 단서
- The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.
- There are two existing strategies for applying pre-trained language representations to downstream tasks: feature-based and fine-tuning.
- For example, in OpenAI GPT, the authors use a left-toright architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer (Vaswani ...
