# SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Haeone Lee, Byeongguk Jeon, Suchae Jeong, Jian Kim, Kimin Lee
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-interface, cross-embodiment
- Aliases:
- Official paper: https://arxiv.org/abs/2606.24049
- Venue verification: https://arxiv.org/abs/2606.24049
- Code/Project: https://haeone.site/space-website/
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

같은 움직임도 로봇 dynamics에 따라 다른 command를 요구한다.

## Core Idea and Contribution

Cartesian state delta를 예측하고 action adapter로 robot command로 변환한다.

## Observation–State–Action Interface

관측 → EEF state displacement → robot-specific adapter → 제어 명령.

## Evaluation Scope and Claim Boundary

Embodiment·동일 기종 개체·frequency/payload/gain 변화 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.24049) · [저자 project/code](https://haeone.site/space-website/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E1/E2에서 정상적인 state-effect 표현과 dynamics adapter의 강한 대안이다.

## Verification Boundary

state delta 계산, adapter supervision, online 적응 자료, 실제 시간을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
