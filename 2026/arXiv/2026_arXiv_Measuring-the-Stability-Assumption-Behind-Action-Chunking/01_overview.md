# Measuring the Stability Assumption Behind Action Chunking

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Aryan Goyal
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases:
- Official paper: https://arxiv.org/abs/2610.01626
- Venue verification: https://arxiv.org/abs/2610.01626
- Code/Project: https://aryangoyal7.github.io/publication/2026-stability-action-chunking
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Chunk 실행 중 상태 perturbation이 어떻게 증폭되는지 측정한다.

## Core Idea and Contribution

Open-loop/closed-loop branch의 finite-horizon divergence를 비교한다.

## Observation–State–Action Interface

같은 초기 상태·action perturbation → rollout → divergence slope.

## Evaluation Scope and Claim Boundary

GR00T manipulation task에서 chunk 안정성 가정의 차이를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.01626) · [저자 project/code](https://aryangoyal7.github.io/publication/2026-stability-action-chunking). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E2 진단에서도 state-dependent 안정성을 새 발견으로 주장하지 않도록 하는 REFERENCE다.

## Verification Boundary

norm 단위, perturbation 크기, branch 동치, 전역 안정성과의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
