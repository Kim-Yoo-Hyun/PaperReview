# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: controller-gain, imitation-learning, reinforcement-learning, sim-to-real
- Aliases: Tune to Learn, Tune to Learn: How Controller Gains Affect Robot Policy Learning
- Official paper: https://www.roboticsproceedings.org/rss22/p139.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p139.html
- Code/Project: https://younghyopark.me/tune-to-learn/
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. RSS의 Shape 제목을 사용하고 저자 페이지의 Affect 제목은 alias로 연결한다. Workshop award를 RSS 수상으로 기록하지 않는다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

Position controller gain 선택이 로봇 정책 학습에 미치는 영향을 묻는다.

## Core Idea and Contribution

정책과 제어 동역학의 상호작용을 바탕으로 BC·RL·sim-to-real에서 gain regime을 비교한다.

## Observation–State–Action Interface

정책의 목표 위치 → gain이 정한 controller → 로봇 상태 → 정책 feedback.

## Evaluation Scope and Claim Boundary

여러 과제·embodiment에서 학습 방식에 따라 gain 선호가 달라지는 결과를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p139.html) · [저자 project/code](https://younghyopark.me/tune-to-learn/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

접촉 VLA RL의 이득을 baseline gain 튜닝과 분리해야 함을 보이는 직접 선행이다.

## Verification Boundary

본문에서 확인할 항목: gain 단위·controller rate·policy 반응·hyperparameter 예산·sim-to-real 차이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
