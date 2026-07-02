# CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion

- Year/Venue: 2026 / RA-L
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/RA-L/2026_RA-L_CLARE-Continual-Learning-for-Vision-Language-Action-Models/paper.pdf
- Code/Project: https://tum-lsy.github.io/CLARE/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address these limitations, we propose CLARE, a general, parameter-efficient framework for exemplar-free continual learning with VLAs.
- This long-term adaptability, known as continual or lifelong learning , remains an open challenge in robotics despite decades of research –.
- However, since this recipe updates existing representations, it is unsuitable for longterm operation in the real world, where robots must continually adapt to new tasks and environments while ...

## Core Idea
- To address these limitations, we propose CLARE, a general, parameter-efficient framework for exemplar-free continual learning with VLAs.
- Pre-training on internet-scale data and robot demonstrations , provides VLAs with broad priors that enable some degree of generalization .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Through extensive experiments on the LIBERO benchmark and five real-world tasks, we show that CLARE achieves high performance on new tasks without catastrophic forgetting of earlier tasks, significantly ...
- However, state-of-the-art VLAs still cannot adapt reliably to unseen tasks without fine-tuning on task-specific data – .
- Recent advances in vision-language-action models (VLAs) – have demonstrated strong performance on complex, long-horizon manipulation tasks by integrating perception, language understanding, and action generation within a unified model.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Through extensive experiments on the LIBERO benchmark and five real-world tasks, we show that CLARE achieves high performance on new tasks without catastrophic forgetting of earlier tasks, significantly ...
- To address these limitations, we propose CLARE, a general, parameter-efficient framework for exemplar-free continual learning with VLAs.
- Pre-training on internet-scale data and robot demonstrations , provides VLAs with broad priors that enable some degree of generalization .

## Abstract Cue
- — To teach robots complex manipulation tasks, a common approach is to fine-tune a pre-trained vision-languageaction model (VLA) on task-specific data.
