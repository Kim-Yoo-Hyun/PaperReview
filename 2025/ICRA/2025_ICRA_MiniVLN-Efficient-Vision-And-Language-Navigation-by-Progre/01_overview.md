# MiniVLN: Efficient Vision-And-Language Navigation by Progressive Knowledge Distillation

- Year/Venue: 2025 / ICRA
- Category: Navigation and Embodied AI
- Tags: Navigation
- Paper link: ./2025/ICRA/2025_ICRA_MiniVLN-Efficient-Vision-And-Language-Navigation-by-Progre/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing VLN methods have made substantial progress by leveraging large-scale pre-trained models to interpret multimodal information and guide agents through complex environments , , .
- To address this challenge, we aim to achieve both high model performance and practical deployability.

## Core Idea
- 3) Training Details: We trained on the R2R dataset for 200,000 iterations with a batch size of 16, and on the REVERIE dataset for 20,000 iterations with a ...
- The proposed method aims to capture fine-grained knowledge during the pretraining phase and navigation-specific knowledge during the fine-tuning phase.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- ScaleVLN , leveraging 1200+ environments and synthesizing 4.9 million instruction-trajectory pairs, exhibits significant improvements in generalization and achieves stateof-the-art results.
- To address this challenge, we aim to achieve both high model performance and practical deployability.
- On the public R2R and REVERIE benchmarks, MiniVLN achieves performance on par with the teacher model while having only about 12% of the teacher model’s parameter count.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- ScaleVLN , leveraging 1200+ environments and synthesizing 4.9 million instruction-trajectory pairs, exhibits significant improvements in generalization and achieves stateof-the-art results.
- On the public R2R and REVERIE benchmarks, MiniVLN achieves performance on par with the teacher model while having only about 12% of the teacher model’s parameter count.
- To address this challenge, we aim to achieve both high model performance and practical deployability.

## Abstract Cue
- — In recent years, Embodied Artificial Intelligence (Embodied AI) has advanced rapidly, yet the increasing size of models conflicts with the limited computational capabilities of Embodied AI platforms.
