# RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Benchmark, generalization
- Aliases:
- Official paper: https://proceedings.mlr.press/v306/dai26c.html
- Venue verification: https://proceedings.mlr.press/v306/dai26c.html
- Code/Project: https://robomme.github.io/
- Code: https://github.com/RoboMME/robomme_benchmark
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

History-dependent manipulation의 memory 설계를 공통 조건에서 비교하기 어렵다.

## Core Idea and Contribution

Temporal·spatial·object·procedural memory task와 여러 memory-augmented VLA를 비교한다.

## Observation–State–Action Interface

현재 관측·history representation → π0.5 기반 VLA → manipulation action.

## Evaluation Scope and Claim Boundary

16 manipulation task와 14 memory variant를 보고하며 memory 효용은 task에 의존한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/dai26c.html) · [저자 project/code](https://robomme.github.io/) · [공식 code](https://github.com/RoboMME/robomme_benchmark). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

현재 GAP-N1–N3의 직접 benchmark이며 memory 필요성과 단순 정보 누설을 구분하는 기준이다.

## Verification Boundary

task dictionary와 goal/evaluator, history cutoff, raw ID와 split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
