# AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, evaluation, manipulation
- Aliases:
- Official paper: https://roboticsproceedings.org/rss20/p010.html
- Venue verification: https://roboticsproceedings.org/rss20/p010.html
- Code/Project: https://robopil.github.io/adaptigraph/
- Code: https://github.com/Boey-li/AdaptiGraph
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

새로운 물성의 deformable 물체를 예측하고 조작하기 어렵다.

## Core Idea and Contribution

물성 조건부 particle graph dynamics를 학습하고 online 상호작용으로 물성 변수를 조정한다.

## Observation–State–Action Interface

물체 particle·interaction → 물성 추정/dynamics → manipulation planning.

## Evaluation Scope and Claim Boundary

로프·입자·상자·천 등 real-world 물체의 예측과 조작을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss20/p010.html) · [저자 project/code](https://robopil.github.io/adaptigraph/) · [공식 code](https://github.com/Boey-li/AdaptiGraph). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

물성 adaptation을 신규 방법으로 반복하지 않기 위한 GAP-DE의 모델 기반 대안이다.

## Verification Boundary

particle extraction, 물성 식별 가능성, probe 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
