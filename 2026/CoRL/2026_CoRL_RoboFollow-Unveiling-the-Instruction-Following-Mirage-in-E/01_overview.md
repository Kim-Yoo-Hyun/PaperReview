# RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Category: Benchmarks and Datasets
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot-evaluation, Benchmark, policy-comparison
- Aliases:
- Official paper: https://openreview.net/forum?id=A9AQjk3dAt
- Venue verification: https://openreview.net/forum?id=A9AQjk3dAt
- Code/Project: https://github.com/AutoLab-SAI-SJTU/RoboFollow
- Code: https://github.com/AutoLab-SAI-SJTU/RoboFollow
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 공식 OpenReview 검색 API의 Conference venueid·CoRL 2026 Poster를 확인했다.

## Problem and Importance

Robot policy의 높은 성공률이 지시 이해를 과대평가할 수 있다.

## Core Idea and Contribution

같은 scene의 여러 지시 등으로 instruction following을 단계별 평가한다.

## Observation–State–Action Interface

Scene·다양한 instruction → policy rollout → intent/execution 판정.

## Evaluation Scope and Claim Boundary

Simulation benchmark와 제한된 실제 검증을 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=A9AQjk3dAt) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboFollow). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C2/D3의 instruction switch와 성공 지표를 검증할 핵심 benchmark다.

## Verification Boundary

scene entropy, evaluator oracle, task infeasibility, real-robot coverage을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
