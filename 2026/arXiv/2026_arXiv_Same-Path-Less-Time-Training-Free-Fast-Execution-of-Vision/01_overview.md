# Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Fuyi Chen
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, latency, action-chunking, control-frequency
- Aliases: Path-preserving Time Scaling, PTS
- Official paper: https://arxiv.org/abs/2611.01390
- Venue verification: https://arxiv.org/abs/2611.01390
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. 11/01 공개 v1 abstract 확인. 공식 채택·code URL 미확인. Simulation 결과를 실제 로봇 검증으로 확대하지 않는다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다.

## Problem and Importance

추론 대기와 느린 시연 속도로 인한 배포 시간 손실을 줄인다.

## Core Idea and Contribution

Frozen chunk policy에 경로 유지 time scaling을 적용해 비동기 추론과 실행 속도를 맞춘다.

## Observation–State–Action Interface

고정 VLA 행동 chunk·추론 지연 → 경로/진행도 정렬 → 속도 조절된 실행 명령.

## Evaluation Scope and Claim Boundary

LIBERO와 LIBERO-Dynamic에서 지연을 주입해 성공률과 task throughput을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2611.01390). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

제어 주기 학습 전에 넘어야 할 학습 없는 실행 대안이며 예비 timing 질문의 비교 자료다.

## Verification Boundary

본문에서 확인할 항목: 실제 지연과 주입 지연·동작 제한·gripper 동기화·실제 로봇 전이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
