# Learning to Look: Seeking Information for Decision Making via Policy Factorization

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Shivin Dass, Jiaheng Hu, Ben Abbatematteo, Peter Stone, Roberto Martín-Martín
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: active perception, policy factorization, partial observability
- Aliases: DISaM, Learning to Look
- Official paper: https://proceedings.mlr.press/v270/dass25a.html
- Venue verification: https://proceedings.mlr.press/v270/dass25a.html
- Code/Project: https://robin-lab.cs.utexas.edu/learning2look/
- Code: https://github.com/UT-Austin-RobIn/l2l
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 행사 CoRL 2024와 PMLR vol.270의 2025 출판을 구별; 폴더 연도는 행사 기준이다.

## Problem and Importance

조작에 필요한 숨은 정보를 얻는 행동과 그 정보를 이용하는 행동을 함께 학습해야 한다.

## Core Idea and Contribution

정보 탐색과 조작 정책을 분리하고 조작 정책에서 탐색 reward를 구성하는 DISaM을 제안한다.

## Observation–State–Action Interface

관측·context에서 정보 수집 또는 조작으로 전환한다. 두 정책 분해를 단일 VLA 공동 학습으로 부르지 않는다.

## Evaluation Scope and Claim Boundary

공식 초록은 simulation·실세계의 정보 탐색이 필요한 조작 과제 5개를 평가한다고 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/dass25a.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/learning2look/) · [공식 code](https://github.com/UT-Austin-RobIn/l2l). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

행동 불확실성 기반 관측 전환이 이미 존재함을 확인할 필수 직접 선행이다.

## Verification Boundary

Context privilege·KL 대상 분포·학습 reward·전환 threshold을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
