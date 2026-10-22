# LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: Benchmarks and Datasets
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: VLA, Benchmark, hardware-shift
- Aliases:
- Official paper: https://arxiv.org/abs/2610.18843
- Venue verification: https://arxiv.org/abs/2610.18843
- Code/Project: https://arxiv.org/abs/2610.18843
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

Task를 고정한 채 hardware/setup 변화에 대한 VLA 취약성을 측정한다.

## Core Idea and Contribution

센서·actuation·controller·기하 변화 축을 분리한 benchmark를 제안한다.

## Observation–State–Action Interface

Native VLA observation/action interface에 setup perturbation을 주입한다.

## Evaluation Scope and Claim Boundary

LIBERO 기반 여러 VLA와 hardware severity 조건을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.18843) · [저자 project/code](https://arxiv.org/abs/2610.18843). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D1의 fault taxonomy와 policy/controller 경계 진단에 필요한 NEXT benchmark다.

## Verification Boundary

native state 소비, fault axis와 onset, 공개 trial-level logs을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
