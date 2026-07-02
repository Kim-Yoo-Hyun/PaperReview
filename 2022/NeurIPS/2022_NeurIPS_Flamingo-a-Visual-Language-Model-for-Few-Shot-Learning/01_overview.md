# Flamingo: a Visual Language Model for Few-Shot Learning

- Year/Venue: 2022 / NeurIPS
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, few-shot, alignment
- Paper link: ./2022/NeurIPS/2022_NeurIPS_Flamingo-a-Visual-Language-Model-for-Few-Shot-Learning/paper.pdf
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual questionanswering.
- Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research.

## Core Idea
- We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest ...
- We introduce Flamingo, a family of Visual Language Models (VLM) with this ability.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with no fine-tuning.
- This is achieved with as few as four examples per task, demonstrating practical and efficient adaptation of vision models to new tasks.
- On numerous benchmarks, Flamingo outperforms models fine-tuned on thousands of times more task-specific data.

## Limitation
- We discuss the limitations of our work in more depth in Appendix D.1.
- We refer the reader to Appendix D.2 for a more extensive discussion of the societal impacts of our work, both positive and negative; as well as mitigation strategies ...
- We would like to thank many colleagues for useful discussions, suggestions, feedback, and advice, including: Samuel Albanie, Relja Arandjelović, Kareem Ayoub, Lorrayne Bennett, Adria Recasens Continente, Tom Eccles, ...

## Contribution
- Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with no fine-tuning.
- We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest ...
- We introduce Flamingo, a family of Visual Language Models (VLM) with this ability.

## Abstract Cue
- Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research.
