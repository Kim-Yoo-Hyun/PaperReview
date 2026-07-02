# Method

- Year/Venue: 2019 / NAACL
- Category: Foundations: Transformer and Language Models
- Tags: LLM, Transformer, pretraining
- Paper link: ./2019/NAACL/2019_NAACL_BERT-Pre-training-of-Deep-Bidirectional-Transformers-for-L/paper.pdf
- Code/Project: https://github.com/google-research/bert
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- For example, in OpenAI GPT, the authors use a left-toright architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer (Vaswani ...
- The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.

## 원리적 동기
- The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.
- There are two existing strategies for applying pre-trained language representations to downstream tasks: feature-based and fine-tuning.
- We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.

## 핵심 방법론
- For example, in OpenAI GPT, the authors use a left-toright architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer (Vaswani ...
- The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.
- BERT alleviates the previously mentioned unidirectionality constraint by using a “masked language model” (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953).
- Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a deep bidirectional Transformer.
- This is also in contrast to Peters et al. (2018a), which uses a shallow concatenation of independently trained left-to-right and right-to-left LMs. • We show that pre-trained representations ...
