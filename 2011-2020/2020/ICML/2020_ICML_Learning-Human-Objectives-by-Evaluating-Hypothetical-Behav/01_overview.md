# Learning Human Objectives by Evaluating Hypothetical Behavior

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2020 / ICML
- Authors: Siddharth Reddy, Anca Dragan, Sergey Levine, Shane Legg, Jan Leike
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reward-learning, evaluation, dynamics model
- Aliases: ReQueST
- Official paper: https://proceedings.mlr.press/v119/reddy20a.html
- Full-text retrieval: https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf
- Venue verification: https://proceedings.mlr.press/v119/reddy20a.html
- Code/Project: https://github.com/rddy/ReQueST
- Code: https://github.com/rddy/ReQueST
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

ReQueST는 학습한 동역학 안에서 가상의 행동을 합성하고 그 보상을 사용자에게 질의해 환경과 추가 상호작용하기 전에 보상 모형을 학습한다. [PDF 1쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=1)

## Core Idea and Contribution

- 오프라인 자료에서 초기 상태·동역학 모형을 학습하고 정보 가치의 대리 목적을 최적화해 물어볼 가상 궤적을 만든다. [PDF 2쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=2) · [PDF 3쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=3) · [PDF 4쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=4)
- 2차원 탐색과 영상 기반 자동차 경주에서 모의 사용자로 질의 효율과 학습한 보상을 쓰는 정책의 안전성을 시험했다. [PDF 4쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=4) · [PDF 5쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=5) · [PDF 6쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=6) · [PDF 7쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=7)

## Observation–State–Action Interface

모델이 만든 hypothetical trajectory → expert feedback → reward model.

## Evaluation Scope and Claim Boundary

Navigation·driving 성격의 simulated task를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v119/reddy20a.html) · [저자 project/code](https://github.com/rddy/ReQueST). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

과거 관측에서 학습한 동역학으로 가상 궤적을 최적화한 뒤 전문가에게 보상을 묻는다. 2차원 내비게이션과 영상 자동차 경주에서 모의 사용자가 피드백을 제공했다. [원문 3쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=3) · [원문 6쪽](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf#page=6)

## Why This Paper Is Here — Researcher Interpretation

C4에서 query 선택·reward refinement의 오래된 직접 선행이다.

## Verification Boundary

가상 trajectory 실현 가능성, feedback 형태, model bias을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
