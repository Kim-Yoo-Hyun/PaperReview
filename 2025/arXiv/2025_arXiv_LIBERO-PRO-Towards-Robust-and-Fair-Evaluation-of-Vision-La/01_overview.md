# LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Benchmark, generalization
- Aliases:
- Official paper: https://arxiv.org/abs/2510.03827
- Venue verification: https://arxiv.org/abs/2510.03827
- Code/Project: https://github.com/Zxy-MLlab/LIBERO-PRO
- Code: https://github.com/Zxy-MLlab/LIBERO-PRO
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 정식 acceptance를 확인하지 못해 preprint로 유지한다.

## Problem and Importance

기존 LIBERO 평가에서 task 이해와 행동 암기가 혼동될 수 있다.

## Core Idea and Contribution

물체·초기 상태·지시·환경 perturbation으로 일반화와 지시 의존성을 점검한다.

## Observation–State–Action Interface

변형 task/지시 → VLA → 실행 결과.

## Evaluation Scope and Claim Boundary

LIBERO 기반 변형 평가를 보고한다. 극단적 저하 수치의 task validity는 별도 본문 감사가 필요하다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.03827) · [저자 project/code](https://github.com/Zxy-MLlab/LIBERO-PRO). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

지시 교란 평가와 구현된 task의 유효성을 함께 점검할 비교 benchmark다.

## Verification Boundary

변경된 목표의 타당성, 언어 교란의 의미, v1/v2 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
