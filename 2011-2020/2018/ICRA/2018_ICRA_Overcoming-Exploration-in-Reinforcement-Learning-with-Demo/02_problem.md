# Overcoming Exploration in Reinforcement Learning with Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Problem and Bottleneck

Sparse reward에서 성공 행동을 찾기 어려운 로봇 RL에 소수 demonstration을 활용하는 문제다.

## Changed Formulation

DDPG·HER와 demonstration replay 및 behavior cloning을 결합한다. Q-filter는 demonstration 행동이 actor 행동보다 높은 Q를 받을 때 모방 손실을 적용한다.

## Assumptions and Robotics Loop

Q 추정이 demonstration과 현재 actor의 행동 비교에 의미 있는 신호여야 한다.

관측·목표 → actor action; demonstration action과 actor action의 Q 비교 → 선택적 imitation 업데이트.

근거: [지정 본문](https://arxiv.org/pdf/1709.10089) — Q-Filter subsection / Eq. 8; arXiv abstract and publisher-deposited metadata.
