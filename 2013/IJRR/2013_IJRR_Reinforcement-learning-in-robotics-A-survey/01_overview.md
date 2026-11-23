# Reinforcement learning in robotics: A survey

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2013 / IJRR
- Authors: Jens Kober, J. Andrew Bagnell, Jan Peters
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reinforcement-learning, Robotics, survey, sample-efficiency
- Aliases: Kober robotics RL survey
- Official paper: https://api.crossref.org/works/10.1177/0278364913495721
- Venue verification: https://journals.sagepub.com/doi/abs/10.1177/0278364913495721
- Code/Project: https://www.ias.informatik.tu-darmstadt.de/Publications/BibTex?id=10613
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. Sage 검색의 publisher abstract/metadata와 저자 연구실 BibTeX·원문 초록으로 IJRR 2013 확인. Publisher 직접 open은 timeout. Survey 본문 전체 정독은 하지 않았다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

로봇 행동 학습의 실물 상호작용·표현·학습 비용을 RL 관점에서 정리한다.

## Core Idea and Contribution

Robot RL의 어려움과 성공 사례를 분류하는 survey이며 단일 새 학습 알고리즘을 제안하지 않는다.

## Observation–State–Action Interface

센싱·상태 표현·정책·행동·feedback의 연구 설계 요소를 비교한다.

## Evaluation Scope and Claim Boundary

기존 로봇 학습 사례를 종합한다. 단일 benchmark의 새 성능 표나 VLA 실험은 아니다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/abs/10.1177/0278364913495721) · [저자 project/code](https://www.ias.informatik.tu-darmstadt.de/Publications/BibTex?id=10613). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

로봇 문제의 제약에서 연구 질문을 세우기 위한 기반 survey로 최신 VLA 방법의 전제 점검에 필요하다.

## Verification Boundary

본문에서 확인할 항목: 사례별 실제 로봇 여부·상호작용 정의·수동 설계·재개 조건. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
