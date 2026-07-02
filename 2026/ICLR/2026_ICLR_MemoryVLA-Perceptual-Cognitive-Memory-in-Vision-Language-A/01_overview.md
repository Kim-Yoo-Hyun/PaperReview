# MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

- Year/Venue: 2026 / ICLR Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICLR/2026_ICLR_MemoryVLA-Perceptual-Cognitive-Memory-in-Vision-Language-A/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- During execution, working memory retrieves decision-relevant contexts from episodic memory and integrates them with current representations to guide actions through cerebellar control, while simultaneously consolidating new experiences into ...
- Drawing on cognitive science insights, we propose MemoryVLA (Fig.
- 1 (c)), a Cognition-MemoryAction framework for robotic manipulation that explicitly models temporal dependencies through a Perceptual–Cognitive Memory Bank (PCMB).

## Core Idea
- Drawing on cognitive science insights, we propose MemoryVLA (Fig.
- For real-world evaluations, we introduce 12 tasks across Franka and WidowX robots, spanning 6 general tasks and 6 long-horizon temporal tasks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- For SimplerEnv (Li et al., 2024b), MemoryVLA achieves 71.9% and 72.7% success rates on Bridge and Fractal suites, surpassing CogACT by 14.6 and 4.6 points, further outperforming π0 ...
- For MikasaRobo (Cherepanov et al., 2025), it achieves 41.2% success rate, outperforming π0 by 11.8 points.
- MemoryVLA achieves 85% and 83% scores on general and temporal tasks, outperforming CogACT by 9 and 26 points, and substantially surpassing π0 .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- For SimplerEnv (Li et al., 2024b), MemoryVLA achieves 71.9% and 72.7% success rates on Bridge and Fractal suites, surpassing CogACT by 14.6 and 4.6 points, further outperforming π0 ...
- For MikasaRobo (Cherepanov et al., 2025), it achieves 41.2% success rate, outperforming π0 by 11.8 points.
- MemoryVLA achieves 85% and 83% scores on general and temporal tasks, outperforming CogACT by 9 and 26 points, and substantially surpassing π0 .

## Abstract Cue
- During execution, working memory retrieves decision-relevant contexts from episodic memory and integrates them with current representations to guide actions through cerebellar control, while simultaneously consolidating new experiences into episodic memory.
