# A Taxonomy for Evaluating Generalist Robot Manipulation Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RA-L
- Authors: Jensen Gao, Suneel Belkhale, Sudeep Dasari, Ashwin Balakrishna, Dhruv Shah, Dorsa Sadigh
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Benchmark, generalization, semantic-grounding
- Aliases: STAR-Gen, ★-Gen
- Official paper: https://arxiv.org/abs/2503.01238
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2026.3656785
- Code/Project: https://stargen-taxonomy.github.io/
- Code: project_only
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. IEEE 페이지 접근 제한으로 publisher-deposited Crossref metadata와 저자 project·arXiv의 RA-L 표기를 대조했다. 본문은 정독하지 않았다.

## Problem and Importance

서로 다른 일반화 조건을 하나의 성공률로 비교하면 정책의 취약 축이 가려진다.

## Core Idea and Contribution

시각·의미·행동 변화를 분리하는 STAR-Gen taxonomy와 평가 지침을 제안한다.

## Observation–State–Action Interface

기본 과제 → 입력/필요 행동의 변화 축 → 축별 정책 평가.

## Evaluation Scope and Claim Boundary

Bridge V2 기반 정책과 ALOHA 2의 실로봇 사례를 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2503.01238) · [저자 project/code](https://stargen-taxonomy.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA 일반화 주장을 시각 변화·언어 이해·행동 변화로 분해할 평가 formulation이다.

## Verification Boundary

각 축의 동시 변화, base competence, in-domain adaptation과 평가 분할을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
