# HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, action-interface, cross-embodiment
- Aliases:
- Official paper: https://arxiv.org/abs/2512.05693
- Venue verification: https://arxiv.org/abs/2512.05693
- Code/Project: https://github.com/ZhiyingDu/HiMoE-VLA
- Code: https://github.com/ZhiyingDu/HiMoE-VLA
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. OpenReview ICLR 2026 Rejected_Submission 확인; arXiv로 등록하며 학회 채택으로 표기하지 않는다.

## Problem and Importance

서로 다른 action space를 가진 데이터의 negative transfer를 줄인다.

## Core Idea and Contribution

Action-space별 expert와 공유 처리의 계층적 mixture를 구성한다.

## Observation–State–Action Interface

언어·영상·embodiment/action-space 정보 → expert routing → action.

## Evaluation Scope and Claim Boundary

CALVIN·LIBERO 및 실제 로봇 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2512.05693) · [저자 project/code](https://github.com/ZhiyingDu/HiMoE-VLA). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E1에서 물리 action 충돌을 단순 expert 분리와 구별할 직접 REFERENCE다.

## Verification Boundary

routing에 쓰는 robot ID, contrastive objective, load balance, parameter 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
