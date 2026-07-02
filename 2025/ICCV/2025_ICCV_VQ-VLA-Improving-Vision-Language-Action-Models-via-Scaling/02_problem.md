# Problem

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2025/ICCV/2025_ICCV_VQ-VLA-Improving-Vision-Language-Action-Models-via-Scaling/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- In this paper, we introduce an innovative vector quantization based action tokenizer built upon the largest-scale action trajectory dataset to date, leveraging over 100 times more data than ...
- This extensive dataset enables our tokenizer to capture rich spatiotemporal dynamics, resulting in a model that not only accelerates inference but also generates smoother and more coherent action ...
- Once trained, the tokenizer can be seamlessly adapted to a wide range of downstream tasks in a zero-shot manner, from short-horizon reactive behaviors to long-horizon planning.

## 해결하려는 문제
- The results demonstrate that as the volume of synthetic trajectory data increases, the performance of our tokenizer on downstream tasks improves significantly—most notably, achieving up to a 30% ...
- To validate our approach, we conducted extensive experiments in both simulated environments and on real robotic platforms.
- Effective action tokenization not only significantly enhances the downstream performance of VLA models, especially for tasks involving long-horizon planning, but also markedly improves their training and inference efficiency.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
