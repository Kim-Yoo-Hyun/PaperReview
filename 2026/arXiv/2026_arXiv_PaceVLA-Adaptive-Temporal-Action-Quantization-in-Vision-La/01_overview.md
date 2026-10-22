# PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases:
- Official paper: https://arxiv.org/abs/2610.25961
- Venue verification: https://arxiv.org/abs/2610.25961
- Code/Project: https://pacevla.github.io/
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-10-21 arXiv v2를 확인했다.

## Problem and Importance

VLA action의 시간 해상도를 task에 맞게 조절한다.

## Core Idea and Contribution

여러 시간 granularity의 표현과 router로 적응형 temporal quantization을 구성한다.

## Observation–State–Action Interface

관측 → temporal 선택·action decoding → robot tracking.

## Evaluation Scope and Claim Boundary

Simulation과 실제 manipulation에서 실행 효율·성능을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.25961) · [저자 project/code](https://pacevla.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E2의 adaptive time compression과 직접 겹치는 REFERENCE다.

## Verification Boundary

v2 controller 설정, router 비용, task별 gain, success/time denominator을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
