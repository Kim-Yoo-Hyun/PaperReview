# CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases:
- Official paper: https://arxiv.org/abs/2607.03693
- Venue verification: https://arxiv.org/abs/2607.03693
- Code/Project: https://arxiv.org/abs/2607.03693
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. arXiv v2 저자는 CoRL 2026 채택을 표기하지만 공식 proceedings 확인 전까지 arXiv로 등록.

## Problem and Importance

서로 다른 센서 구성과 auxiliary sensor 손실에 VLA를 대응시킨다.

## Core Idea and Contribution

Sensor availability와 task intent를 이용해 sparse expert를 routing한다.

## Observation–State–Action Interface

RGB·언어·proprioception·optional depth → action.

## Evaluation Scope and Claim Boundary

LIBERO, RoboCasa GR1, 실제 dual-arm 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.03693) · [저자 project/code](https://arxiv.org/abs/2607.03693). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D1의 modality robustness와 직접 겹치는 NEXT다. 카메라 복원 CoRe-VLA와 다른 논문이다.

## Verification Boundary

v2 depth degradation 평가, availability indicator, 공식 CoRL 채택 확인을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
