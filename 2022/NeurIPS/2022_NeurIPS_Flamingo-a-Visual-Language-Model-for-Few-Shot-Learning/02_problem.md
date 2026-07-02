# Problem

- Year/Venue: 2022 / NeurIPS
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, few-shot, alignment
- Paper link: ./2022/NeurIPS/2022_NeurIPS_Flamingo-a-Visual-Language-Model-for-Few-Shot-Learning/paper.pdf
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual questionanswering.
- Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research.

## 해결하려는 문제
- Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with no fine-tuning.
- We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest ...
- We introduce Flamingo, a family of Visual Language Models (VLM) with this ability.

## 선행 연구 / 배경 단서
- We show that the same can be done for image and video understanding tasks such as classification, captioning, or question-answering: these can be cast as text prediction problems ...
- They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual questionanswering.
- While initial progress has been made towards a similar capability in computer vision, the most widely used paradigm still consists of first pretraining on a large amount of ...
