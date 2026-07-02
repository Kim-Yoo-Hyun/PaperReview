# Training language models to follow instructions with human feedback

- Year/Venue: 2022 / NeurIPS
- Category: Foundations: Transformer and Language Models
- Tags: LLM, instruction tuning, alignment
- Paper link: ./2022/NeurIPS/2022_NeurIPS_Training-language-models-to-follow-instructions-with-human/paper.pdf
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Large language models (LMs) can be “prompted” to perform a range of natural language processing (NLP) tasks, given some examples of the task as input.
- However, these models often express unintended behaviors such as making up facts, generating biased or toxic text, or simply not following user instructions (Bender et al., 2021; Bommasani ...
- This is because the language modeling objective ∗ Primary authors.

## Core Idea
- We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.
- Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.
- Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets.
- In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.

## Limitation
- However, our approach does provides us with a clear empirical feedback loop of what works and what does not.

## Contribution
- Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.
- Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets.
- Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we ...

## Abstract Cue
- Making language models bigger does not inherently make them better at following a user’s intent.
