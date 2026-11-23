# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Antonia Bronars, Younghyo Park, Pulkit Agrawal
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: controller-gain, imitation-learning, reinforcement-learning, sim-to-real
- Aliases: Tune to Learn, Tune to Learn: How Controller Gains Affect Robot Policy Learning
- Official paper: https://www.roboticsproceedings.org/rss22/p139.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p139.html
- Code/Project: https://younghyopark.me/tune-to-learn/
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. RSS의 Shape 제목을 사용하고 저자 페이지의 Affect 제목은 alias로 연결한다. Workshop award를 RSS 수상으로 기록하지 않는다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 로봇 위치 제어기의 강성과 감쇠 이득이 모방학습·강화학습·시뮬레이션에서 실물로의 전이에 어떤 영향을 주는지 평가한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=1)

## Core Idea and Contribution

- 상태에 반응하는 정책에서는 동일한 제어 이득에서도 실효 강성이 달라질 수 있음을 분석하고, 이득과 학습 설정을 바꾸는 비교를 설계했다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=4)
- 시험한 과제에서 행동 복제는 순응적이고 과감쇠인 조건의 이득을 보았으며, 강화학습은 설정 조정으로 여러 이득에 적응했고, 높은 강성과 과감쇠의 조합은 실물 전이에 불리했다. [PDF 7쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=7) · [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=8) · [PDF 9쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=9)

## Observation–State–Action Interface

정책의 목표 위치 → gain이 정한 controller → 로봇 상태 → 정책 feedback.

## Evaluation Scope and Claim Boundary

여러 과제·embodiment에서 학습 방식에 따라 gain 선호가 달라지는 결과를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p139.html) · [저자 project/code](https://younghyopark.me/tune-to-learn/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

접촉 VLA RL의 이득을 baseline gain 튜닝과 분리해야 함을 보이는 직접 선행이다.

## Verification Boundary

본문에서 확인할 항목: gain 단위·controller rate·policy 반응·hyperparameter 예산·sim-to-real 차이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
