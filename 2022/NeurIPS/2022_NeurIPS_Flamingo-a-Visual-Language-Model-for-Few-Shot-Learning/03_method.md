# Method

- Year/Venue: 2022 / NeurIPS
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, few-shot, alignment
- Paper link: ./2022/NeurIPS/2022_NeurIPS_Flamingo-a-Visual-Language-Model-for-Few-Shot-Learning/paper.pdf
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest ...
- We introduce Flamingo, a family of Visual Language Models (VLM) with this ability.

## 원리적 동기
- They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual questionanswering.
- Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research.
- We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest ...

## 핵심 방법론
- 66.1 (0) 53.7 53.6 56.3 57.0 62.7 63.5 46.4 68.6 70.0 79.1 40.7 (0) 58.4 57.9 60.8 - - (38K) (9K) Table 1: Comparison to the state of ...
- A single Flamingo model reaches the state of the art on a wide array of image (I) and video (V) understanding tasks with few-shot learning, significantly outperforming previous ...
- More importantly, using only 32 examples and without adapting any model weights, Flamingo outperforms the current best methods – fine-tuned on thousands of annotated examples – on seven ...
- Best few-shot numbers are in bold, best numbers overall are underlined. evaluations using our model’s log-likelihood to score each possible answer.
- We explore zero-shot generalization by prompting the model with two text-only examples from the task, with no corresponding images.
