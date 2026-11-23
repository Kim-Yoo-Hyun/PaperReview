# Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Yifan Li, Jiaxu Wang, Dongming Wu, Yicheng Jiang, Ryan Ji, Xiangyu Yue, Yanwei Fu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases:
- Official paper: https://arxiv.org/abs/2610.05230
- Venue verification: https://arxiv.org/abs/2610.05230
- Code/Project: https://clementine24.github.io/Vela/
- Code: not_released
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

이질적인 속도·길이의 행동을 고정 시간격자에 표현하는 한계를 다룬다.

## Core Idea and Contribution

연속 spline action curve와 적응 길이 표현을 사용한다.

## Observation–State–Action Interface

관측·지시 → action curve → 실행 시 sampling.

## Evaluation Scope and Claim Boundary

Simulation benchmark와 실제 long-horizon manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.05230) · [저자 project/code](https://clementine24.github.io/Vela/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E2에서 연속 행동 곡선 자체를 신규 기여로 재주장하지 않기 위한 REFERENCE다.

## Verification Boundary

spline fitting, horizon-matched 학습, controller tracking, code 공개 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
