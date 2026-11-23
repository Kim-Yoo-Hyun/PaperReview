# Learning to Look: Seeking Information for Decision Making via Policy Factorization

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 행사 CoRL 2024와 PMLR vol.270의 2025 출판을 구별; 폴더 연도는 행사 기준이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DISaM은 다음 조작을 정할 정보가 현재 관측에 없을 때, 정보를 찾는 행동과 그 정보를 사용해 작업을 끝내는 행동을 분리해 학습한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/dass25a/dass25a.pdf#page=1)

## Core Idea and Contribution

- 조작 정책에서 얻은 신호를 정보 탐색 정책의 보상으로 사용하고, 실행 시 다음 조작 행동의 불확실성을 기준으로 어느 정책을 쓸지 결정한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/dass25a/dass25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/dass25a/dass25a.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/dass25a/dass25a.pdf#page=6)
- 정보 탐색이 필요한 시뮬레이션 세 과제와 실제 Tiago 두 과제에서 관측을 얻기 위한 행동과 최종 조작 성공을 비교했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/dass25a/dass25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/dass25a/dass25a.pdf#page=8)

## Observation–State–Action Interface

관측·context에서 정보 수집 또는 조작으로 전환한다. 두 정책 분해를 단일 VLA 공동 학습으로 부르지 않는다.

## Evaluation Scope and Claim Boundary

공식 초록은 simulation·실세계의 정보 탐색이 필요한 조작 과제 5개를 평가한다고 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/dass25a.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/learning2look/) · [공식 code](https://github.com/UT-Austin-RobIn/l2l). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

행동 불확실성 기반 관측 전환이 이미 존재함을 확인할 필수 직접 선행이다.

## Verification Boundary

Context privilege·KL 대상 분포·학습 reward·전환 threshold을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
