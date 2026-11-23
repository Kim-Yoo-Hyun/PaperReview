# TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
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
- Source audit: 2026-11-12: 공식 abstract/metadata 확인; project URL은 링크 식별만 확인. v1 abstract 및 논문 내 project 링크 확인. 익명 code 링크는 기존 N1에서 발견했으나 내용 검증은 안 됨. 동명의 TEMPO: Learning Temporal Context for Dynamic Robot Manipulation과 다른 논문이다. 논문이 제공한 익명 project URL은 이번 도구에서 접근하지 못했으며 링크 식별만 확인했다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

TEMPO는 VLA의 시각언어 백본을 고정하고 의미를 행동 조건으로 바꾸는 층과 저수준 행동 생성기를 서로 다른 빈도로 강화학습한다. [PDF 1쪽](https://arxiv.org/pdf/2608.07314v2#page=1)

## Core Idea and Contribution

- 행동 생성기는 자주 갱신하고 의미 투영층은 드물게 갱신해 하위 정책이 받는 잠재 행동 목표의 변동을 줄인다. [PDF 3쪽](https://arxiv.org/pdf/2608.07314v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2608.07314v2#page=4)
- CALVIN과 실제 조작에서 정책 성능을 측정하고 갱신 빈도 비율을 바꿔 잠재 행동의 변동과 과제 성공의 관계를 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2608.07314v2#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2608.07314v2#page=7)

## Observation–State–Action Interface

영상·지시 → 동결 VLM·적응 projection → RL action expert → 로봇 동작.

## Evaluation Scope and Claim Boundary

CALVIN과 실제 조작 과제에서 후학습 정책·갱신 전략을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.07314) · 저자 프로젝트·코드 주소 미확인. 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

단일 VLA 내부의 의미 보존과 모듈별 RL 갱신에 관한 직접 경쟁 선행이다.

## Verification Boundary

본문에서 확인할 항목: 학습 task-set·두 학습기의 데이터/gradient 경계·초기 능력·비용 정의. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
