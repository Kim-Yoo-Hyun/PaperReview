# Overcoming Exploration in Reinforcement Learning with Demonstrations

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2018 / ICRA
- Authors: Ashvin Nair, Bob McGrew, Marcin Andrychowicz, Wojciech Zaremba, Pieter Abbeel
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reinforcement-learning, demonstrations, Q-filter, sparse-reward
- Aliases: Q-filter
- Official paper: https://api.crossref.org/works/10.1109/ICRA.2018.8463162
- Venue verification: https://api.crossref.org/works/10.1109/ICRA.2018.8463162
- Code/Project: not identified
- Code: not identified
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 Q-Filter subsection / Eq. 8; arXiv abstract and publisher-deposited metadata를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. 이번 확인은 Q-filter 수식과 서지에 한정한다. 정확한 seed·전체 baseline/ablation·현재 공식 code 상태는 확인하지 않았다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

Sparse reward에서 성공 행동을 찾기 어려운 로봇 RL에 소수 demonstration을 활용하는 문제다.

## Core Idea and Contribution

DDPG·HER와 demonstration replay 및 behavior cloning을 결합한다. Q-filter는 demonstration 행동이 actor 행동보다 높은 Q를 받을 때 모방 손실을 적용한다.

## Observation–State–Action Interface

관측·목표 → actor action; demonstration action과 actor action의 Q 비교 → 선택적 imitation 업데이트.

## Evaluation Scope and Limitations

시뮬레이션 로봇 팔의 sparse-reward 조작을 다룬다. VLA 연구가 아니며 현재 후보의 두 reference 규칙을 원 논문의 재현이라고 부를 수 없다.

이번 확인은 Q-filter 수식과 서지에 한정한다. 정확한 seed·전체 baseline/ablation·현재 공식 code 상태는 확인하지 않았다.

근거: [지정 본문](https://arxiv.org/pdf/1709.10089) — Q-Filter subsection / Eq. 8; arXiv abstract and publisher-deposited metadata.

## Why This Paper Is Here — Researcher Interpretation

선택적 Q 기반 imitation의 직접 기원으로 REFERENCE에 추가한다. 2024–2026 최신 동향 수에는 포함하지 않으며 기존 SAC/DDPG 기반 읽기 흐름을 보완한다.
