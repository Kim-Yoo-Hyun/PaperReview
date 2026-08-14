# SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention

- Year/Venue: 2024 / ICRA
- Category: Robot Learning and Data
- Tags: Robotics, robot policy, efficient attention, manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://deepmind.google/discover/blog/shaping-the-future-of-advanced-robotics/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- One of the challenges that is still not addressed, yet is of critical practical importance in Robotics, is a prohibitively expensive space and time complexity of the aforementioned ...
- — We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment.

## Core Idea
- — We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment.
- It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterparts maintaining high quality.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We complement our results with the rigorous mathematical analysis providing deeper insight into the phenomenon of SARA.
- We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models , the first VLA robotic policies pre-trained on internetscale data, as ...
- Interestingly, even when not finetuned, Transformer models trained on massive web corpus seem to learn structural reinforcement learning priors that can be leveraged to conduct trajectory optimization for ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- — We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment.
- It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterparts maintaining high quality.
- We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models , the first VLA robotic policies pre-trained on internetscale data, as ...

## Abstract Cue
- — We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment.
