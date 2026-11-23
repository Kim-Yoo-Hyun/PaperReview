# Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / ICLR
- Authors: Alizée Pace, Hugo Yèche, David Ha, Gunnar Ratsch, Guy Tennenholtz
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: offline-RL, hidden-confounding, uncertainty
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다.

## Problem and Importance

관측되지 않은 변수가 행동과 결과를 함께 바꾸면 offline 정책 평가가 편향된다.

## Core Idea and Contribution

관측과 양립하는 world model 간 차이로 confounding 불확실성을 정의하고 보수적 RL에 반영한다.

## Observation–State–Action Interface

offline trajectory → confounding/model uncertainty → pessimistic policy.

## Evaluation Scope and Claim Boundary

Sepsis benchmark와 의료 기록에서 평가하며 robot/VLA 효과를 검증한 논문은 아니다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

로봇 시연의 숨은 정보 문제를 단순 모델 불확실성과 혼동하지 않게 하는 방법론 참조다.

## Verification Boundary

비식별성 가정, uncertainty estimator, pessimism 수준, 의료→로봇 적용 한계을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
