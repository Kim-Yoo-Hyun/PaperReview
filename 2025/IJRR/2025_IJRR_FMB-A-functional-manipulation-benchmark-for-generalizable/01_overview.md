# FMB: A functional manipulation benchmark for generalizable robotic learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / IJRR
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, Benchmark, assembly, skill-composition
- Aliases: FMB, Functional Manipulation Benchmark
- Official paper: https://journals.sagepub.com/doi/full/10.1177/02783649241276017
- Venue verification: https://journals.sagepub.com/doi/full/10.1177/02783649241276017
- Code/Project: https://functional-manipulation-benchmark.github.io/
- Code: https://github.com/rail-berkeley/fmb
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. 공식 journal abstract와 서지정보·저자 project 확인. Online-first 2024-09-22, 권호 출판 2025를 구분해 registry year는 2025다.

## Problem and Importance

접촉이 복잡한 개별 조작과 장시간 skill 조합을 재현 가능한 조건에서 함께 평가해야 한다.

## Core Idea and Contribution

복제 가능한 3D 프린트 물체·조립 과제와 imitation baseline을 구성한다.

## Observation–State–Action Interface

물체/로봇 관측 → grasp·reorientation·assembly skill → 다단계 조립.

## Evaluation Scope and Claim Boundary

실로봇의 개별 skill과 조합 과제를 평가하는 데이터·CAD·정책 자산을 제공한다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/full/10.1177/02783649241276017) · [저자 project/code](https://functional-manipulation-benchmark.github.io/) · [공식 code](https://github.com/rail-berkeley/fmb). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

범용 pick-and-place 성능과 접촉 조립 능력을 구분할 benchmark를 보완한다.

## Verification Boundary

skill/전체 과제 성공 정의, object split, reset과 force/torque 접근을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
