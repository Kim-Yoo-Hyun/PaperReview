# TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Ziheng Liu, Quantao Yang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, reinforcement-learning, semantic-preservation, adaptation
- Aliases: TEMPO-RL
- Official paper: https://arxiv.org/abs/2608.07314
- Venue verification: https://arxiv.org/abs/2608.07314
- Code/Project: not identified
- Code: not identified
- Source audit: 2026-11-12: 공식 abstract/metadata 확인; project URL은 링크 식별만 확인. v1 abstract 및 논문 내 project 링크 확인. 익명 code 링크는 기존 N1에서 발견했으나 내용 검증은 안 됨. 동명의 TEMPO: Learning Temporal Context for Dynamic Robot Manipulation과 다른 논문이다. 논문이 제공한 익명 project URL은 이번 도구에서 접근하지 못했으며 링크 식별만 확인했다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다.

## Problem and Importance

VLA의 의미 모듈과 행동 모듈을 같은 속도로 갱신할 때 안정성과 제어 적응의 요구가 충돌한다.

## Core Idea and Contribution

VLM을 동결하고 semantic projection과 action expert를 서로 다른 빈도의 RL 갱신으로 적응한다.

## Observation–State–Action Interface

영상·지시 → 동결 VLM·적응 projection → RL action expert → 로봇 동작.

## Evaluation Scope and Claim Boundary

CALVIN과 실제 조작 과제에서 후학습 정책·갱신 전략을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.07314) · [저자 project/code](https://anonymous.4open.science/w/tempo-page/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단일 VLA 내부의 의미 보존과 모듈별 RL 갱신에 관한 직접 경쟁 선행이다.

## Verification Boundary

본문에서 확인할 항목: 학습 task-set·두 학습기의 데이터/gradient 경계·초기 능력·비용 정의. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
