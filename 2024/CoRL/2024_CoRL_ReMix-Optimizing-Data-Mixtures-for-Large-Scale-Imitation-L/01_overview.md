# ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Joey Hejna, Chethan Anand Bhateja, Yichen Jiang, Karl Pertsch, Dorsa Sadigh
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, data-mixture, distributional-robustness
- Aliases: ReMix, Re-Mix
- Official paper: https://proceedings.mlr.press/v270/hejna25a.html
- Venue verification: https://proceedings.mlr.press/v270/hejna25a.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: https://github.com/jhejna/remix
- Code: https://github.com/jhejna/remix
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. CoRL 개최 2024, PMLR 출판 2025.

## Problem and Importance

서로 다른 로봇 데이터 domain을 어떤 비율로 섞어야 할지 불명확하다.

## Core Idea and Contribution

DRO 기반 domain 가중치 학습에 action 정규화·이산화와 early stopping을 적용한다.

## Observation–State–Action Interface

이질적 demonstration domain → mixture weights → downstream imitation policy.

## Evaluation Scope and Claim Boundary

Bridge·Open X-Embodiment 기반 데이터 혼합과 후속 정책 성능을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/hejna25a.html) · [저자 project/code](https://github.com/jhejna/remix). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

DataMIL의 subset 선택과 domain-level mixture 최적화를 구분하는 필수 비교군이다.

## Verification Boundary

domain 정의, proxy/target 접근, normalization, selection 계산 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
