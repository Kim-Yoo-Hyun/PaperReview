# D4RL: Datasets for Deep Data-Driven Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2020 / arXiv
- Authors: Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: offline-RL, Benchmark, robot-data, distribution-shift
- Aliases: D4RL
- Official paper: https://arxiv.org/abs/2004.07219
- Venue verification: https://arxiv.org/abs/2004.07219
- Code/Project: https://github.com/Farama-Foundation/D4RL
- Code: https://github.com/Farama-Foundation/D4RL
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. arXiv v4와 공식 유지 repository 확인. 확인되지 않은 conference venue를 부여하지 않으며 현행 라이브러리의 실행 호환성을 보장하지 않는다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

온라인 학습용 benchmark만으로는 offline 데이터의 이질성과 실패를 평가하기 어렵다.

## Core Idea and Contribution

사람·규칙 controller·정책 혼합·멀티태스크 데이터를 포함하는 offline RL benchmark와 평가 프로토콜을 제시한다.

## Observation–State–Action Interface

고정 transition dataset → offline 정책 학습 → 환경별 평가.

## Evaluation Scope and Claim Boundary

다양한 데이터 수집 조건에서 offline 알고리즘을 비교한다. 데이터셋 전체가 실물 로봇 trajectory라는 뜻은 아니다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2004.07219) · [저자 project/code](https://github.com/Farama-Foundation/D4RL). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

CQL·IQL·Cal-QL의 데이터 조건과 결과를 읽기 위한 표준 benchmark의 누락을 보완한다.

## Verification Boundary

본문에서 확인할 항목: dataset version·terminal/timeout·normalized score·현행 API와 원본 데이터 호환. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
