# FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Donghu Kim, Youngdo Lee, Minho Park, Kinam Kim, Takuma Seno, I. Made Aswin Nahrendra, Sehee Min, Daniel Palenicek, Florian Vogt, Danica Kragic, Jan Peters, Jaegul Choo, Hojoon Lee
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: off-policy-RL, actor-critic, scaling, robot-control
- Aliases: FlashSAC
- Official paper: https://roboticsproceedings.org/rss22/p099.html
- Venue verification: https://roboticsproceedings.org/rss22/p099.html
- Code/Project: https://github.com/Holiday-Robot/FlashSAC
- Code: https://github.com/Holiday-Robot/FlashSAC
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. RSS와 후속 arXiv의 평가 과제 수가 다르므로 수치를 혼합하지 않는다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

고차원 로봇 제어에서 off-policy critic 오차가 불안정한 bootstrap을 유발한다.

## Core Idea and Contribution

가중치·feature·gradient norm을 제한하고 병렬 데이터와 replay coverage를 확대한다.

## Observation–State–Action Interface

상태 또는 시각 관측 → SAC 행동; replay 기반 가치 학습.

## Evaluation Scope and Claim Boundary

여러 simulator의 제어 과제와 실제 humanoid sim-to-real을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p099.html) · [저자 project/code](https://github.com/Holiday-Robot/FlashSAC). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

새 VLA-RL 구조의 필요성을 판단할 때 참고할 강한 off-policy 학습 baseline이다.

## Verification Boundary

상태/vision별 계산량, update-to-data 비율, 실제 로봇 전이 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
