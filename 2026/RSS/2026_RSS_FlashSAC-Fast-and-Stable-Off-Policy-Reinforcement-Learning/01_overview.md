# FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / RSS
- Authors: Donghu Kim, Youngdo Lee, Minho Park, Kinam Kim, Takuma Seno, I Made Aswin Nahrendra, Sehee Min, Daniel Palenicek, Florian Vogt, Danica Kragic, Jan Peters, Jaegul Choo, Hojoon Lee
- 저자 판본: 학회 서지에는 I. Made Aswin Nahrendra로 실려 있다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=1) · [학회 서지](https://roboticsproceedings.org/rss22/p099.html)
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: off-policy-RL, actor-critic, scaling, robot-control
- Aliases: FlashSAC
- Official paper: https://roboticsproceedings.org/rss22/p099.html
- DOI: [10.15607/RSS.2026.XXII.099](https://doi.org/10.15607/RSS.2026.XXII.099)
- Venue verification: https://roboticsproceedings.org/rss22/p099.html
- Code/Project: https://github.com/Holiday-Robot/FlashSAC
- Code: https://github.com/Holiday-Robot/FlashSAC
- Full-text retrieval: https://roboticsproceedings.org/rss22/p099.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

FlashSAC는 고차원 로봇 제어에서 큰 모델과 높은 데이터 처리량을 사용해 오프폴리시 SAC에 필요한 경사 갱신 횟수를 줄인다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=1) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=4)

## Core Idea and Contribution

- 가중치·특징·경사의 노름을 제한해 큰 네트워크에서 부트스트래핑으로 인한 가치 추정 오차가 누적되는 현상을 제어한다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=4)
- 여러 시뮬레이터에서 상태·영상 기반 제어 학습을 비교하고 휴머노이드 보행에서는 시뮬레이션에서 학습한 정책을 실물에 배포했다. [PDF 5쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=5) · [PDF 6쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=7)

## Observation–State–Action Interface

상태 또는 시각 관측 → SAC 행동; replay 기반 가치 학습.

## Evaluation Scope and Claim Boundary

Unitree G1의 실물 계단 오르기에서 인용하는 4시간은 FlashSAC의 시뮬레이션 학습 시간이다. 그림 6은 비슷한 계단 등반 능력에 도달한 PPO의 약 20시간과 비교한다. [PDF 5쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=5) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=7)

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p099.html) · [저자 project/code](https://github.com/Holiday-Robot/FlashSAC).

## Why This Paper Is Here — Researcher Interpretation

새 VLA-RL 구조의 필요성을 판단할 때 참고할 강한 off-policy 학습 baseline이다.

## Verification Boundary

상태/vision별 계산량, update-to-data 비율, 실제 로봇 전이 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
