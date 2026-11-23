# THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / RSS
- Authors: Wilbert Pumacay, Ishika Singh, Jiafei Duan, Ranjay Krishna, Jesse Thomason, Dieter Fox
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Benchmark, generalization
- Aliases:
- Official paper: https://roboticsproceedings.org/rss20/p133.html
- Venue verification: https://roboticsproceedings.org/rss20/p133.html
- Code/Project: https://robot-colosseum.github.io/
- Code: https://github.com/robot-colosseum/robot-colosseum
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

학습과 유사한 환경만 평가하면 manipulation policy 일반화가 과대평가된다.

## Core Idea and Contribution

Manipulation task에 시각·물리 perturbation을 체계적으로 적용하는 simulation benchmark를 제시한다.

## Observation–State–Action Interface

Task·환경 변화 → manipulation policy → 조건별 성공.

## Evaluation Scope and Claim Boundary

Simulation 비교와 대응 실세계 perturbation의 관련성을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss20/p133.html) · [저자 project/code](https://robot-colosseum.github.io/) · [공식 code](https://github.com/robot-colosseum/robot-colosseum). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

LIBERO 계열에 한정하지 않고 manipulation 일반화를 점검할 benchmark 계보다.

## Verification Boundary

복합 요인 상호작용, simulator와 실세계 조건의 대응을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
