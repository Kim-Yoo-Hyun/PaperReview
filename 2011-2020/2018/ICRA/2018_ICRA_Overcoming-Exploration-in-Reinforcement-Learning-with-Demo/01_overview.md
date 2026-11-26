# Overcoming Exploration in Reinforcement Learning with Demonstrations

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

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
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다. 이전 감사에서 확인한 Q-filter 식 (8)의 출처도 보존했다.

## Problem and Importance

희소 보상 조작에서 DDPG와 목표 재지정 경험 재생에 소수 시연을 더해, 블록 쌓기처럼 보상을 만나기 어려운 행동을 학습했다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=3)

## Core Idea and Contribution

- 시연 행동의 추정 가치가 정책 행동보다 높을 때 모방 손실을 적용하고, 긴 과제에서는 일부 에피소드를 시연 중간 상태에서 시작한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=4)
- 시뮬레이션 과제에서 강화학습·행동 복제 기준선과 비교하고, 블록 쌓기에서 시연 상태 재시작과 모방 항의 영향을 분리했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=7)

## Observation–State–Action Interface

관측·목표 → actor action; demonstration action과 actor action의 Q 비교 → 선택적 imitation 업데이트.

## Evaluation Scope and Limitations

저자들이 제시한 약 6시간은 pick-and-place 학습의 약 100만 시뮬레이션 스텝을 실물 상호작용 시간으로 환산한 값이다. 실험은 시뮬레이션 로봇 팔에서 했다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=4) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=7) · [PDF 8쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=8)

근거: [지정 본문](https://arxiv.org/pdf/1709.10089) — Q-Filter subsection / Eq. 8; arXiv abstract and publisher-deposited metadata.

## 검색 태그 근거

DDPG와 HER에 시연 버퍼를 더하고, 시연 행동의 추정 가치가 현재 정책 행동보다 높을 때만 복제 손실을 적용한다. 블록 쌓기에서는 시연 중간 상태에서 시작하는 시뮬레이션 조건도 비교한다. [원문 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=4) · [원문 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=6)

## Why This Paper Is Here — Researcher Interpretation

선택적 Q 기반 imitation의 직접 기원으로 REFERENCE에 추가한다. 2024–2026 최신 동향 수에는 포함하지 않으며 기존 SAC/DDPG 기반 읽기 흐름을 보완한다.
