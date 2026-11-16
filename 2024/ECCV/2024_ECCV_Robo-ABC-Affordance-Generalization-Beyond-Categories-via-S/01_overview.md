# Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / ECCV
- Category: 3D Vision-Language Understanding
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, evaluation, affordance
- Aliases:
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php
- Venue verification: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php
- Code/Project: https://tea-lab.github.io/Robo-ABC/
- Code: https://github.com/TEA-Lab/Robo-ABC
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

새 물체 category에서 조작 contact point를 얻기 어렵다.

## Core Idea and Contribution

Human video의 affordance memory에서 유사 물체를 찾고 semantic correspondence로 contact point를 옮긴다.

## Observation–State–Action Interface

새 물체 영상·contact memory → affordance/contact point → robot manipulation.

## Evaluation Scope and Claim Boundary

시각 affordance 추정과 실세계 cross-category grasping을 보고한다.

근거: [공식 paper/abstract](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php) · [저자 project/code](https://tea-lab.github.io/Robo-ABC/) · [공식 code](https://github.com/TEA-Lab/Robo-ABC). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Semantic representation을 실제 contact/action에 연결하는 비교용 3D/affordance 지원 연구다.

## Verification Boundary

2D/3D lifting, grasp 실행기, source별 수치 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
