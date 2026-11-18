# StructRL: Structured Action-Space Exploration for Flow-Based VLAs

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, RL, flow policy, structured exploration
- Aliases: StructRL
- Official paper: https://arxiv.org/abs/2608.15139
- Venue verification: https://arxiv.org/abs/2608.15139
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 이전 project URL은 이번 도구에서 접근 실패하여 새 release 상태를 확정하지 않았다. 공식 conference/journal acceptance 확인을 확보하지 못해 preprint 유지.

## Problem and Importance

Flow 중간에 넣은 구조적 탐색 noise가 남은 denoising 과정에서 약해질 수 있다.

## Core Idea and Contribution

Deterministic ODE decoder 뒤 실행 action space에 구조적 noise를 넣고 last-step replay로 정책 갱신 신호를 구성한다.

## Observation–State–Action Interface

VLA flow decoder와 실행 행동의 stochasticity를 분리한다. 조건부 양팔 관계 학습의 선행 경계를 정한다.

## Evaluation Scope and Claim Boundary

초록은 로봇 조작의 online RL 탐색을 대상으로 한다. 이번 등록에서는 task별 수치·동일 compute 여부를 확정하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.15139). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

관계 기반 RL 탐색의 noise 위치·시간 구조·재채점 설계와 직접 충돌하는 최신 선행이다.

## Verification Boundary

Last-step likelihood 의미·noise covariance·중간 flow dilution 분석·코드 호환을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
