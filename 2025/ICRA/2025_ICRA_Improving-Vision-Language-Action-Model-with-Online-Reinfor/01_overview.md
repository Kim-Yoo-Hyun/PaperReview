# Improving Vision-Language-Action Model with Online Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2025 / ICRA
- Authors: Yanjiang Guo, Jianke Zhang, Xiaoyu Chen, Xiang Ji, Yen-Jen Wang, Yucheng Hu, Jianyu Chen
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, online RL, robot manipulation
- Official paper: https://arxiv.org/abs/2501.16664
- Code/Project: not identified

## 연구 질문과 기여

로봇 상호작용에서 얻은 RL 개선을 감독학습과 교대로 VLA에 반영한다.

탐색과 정책 갱신의 학습 절차를 분리한다. 시뮬레이션과 실제 조작에서 이 절차를 평가한다.

## 평가 범위

시뮬레이션 조작과 실물 조작에서 직접 PPO 및 감독학습 조건을 비교했다. [원문 및 평가 절](https://arxiv.org/pdf/2501.16664#page=5)

## 선정 근거

온라인 RL을 VLA에 직접 적용하는 방식과 RL·감독학습을 교대하는 방식을 대조할 기준이다.
