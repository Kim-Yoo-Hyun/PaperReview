# Mechanistic Interpretability for Steering Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Bear Häon, Kaylene Caswell Stocking, Ian Chuang, Claire Tomlin
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, evaluation, generalization
- Aliases:
- Official paper: https://proceedings.mlr.press/v305/haon25a.html
- Venue verification: https://proceedings.mlr.press/v305/haon25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

VLA 내부 표현을 이해하고 실행 중 행동을 조절하는 수단이 부족하다.

## Core Idea and Contribution

Transformer activation의 semantic 방향을 찾고 inference 때 activation steering으로 행동을 조절한다.

## Observation–State–Action Interface

VLA 내부 activation·semantic 방향 → 개입된 action.

## Evaluation Scope and Claim Boundary

Pi0·OpenVLA를 LIBERO 및 UR5에서 평가한다고 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/haon25a.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Instruction 대응이나 VLA 행동 교정을 연구할 때 fine-tuning 없는 직접 baseline이다.

## Verification Boundary

방향 추출 데이터, 개입 강도, 속도와 성공의 trade-off을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
