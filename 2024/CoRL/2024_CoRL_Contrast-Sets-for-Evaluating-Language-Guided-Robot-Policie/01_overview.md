# Contrast Sets for Evaluating Language-Guided Robot Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Abrar Anwar, Rohan Gupta, Jesse Thomason
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: language-grounding, contrast-sets, robot-evaluation
- Aliases: Contrast Sets
- Official paper: https://proceedings.mlr.press/v270/anwar25a.html
- Venue verification: https://proceedings.mlr.press/v270/anwar25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  CoRL 2024 event; PMLR volume 270 published 2025. Registry year uses event year. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

작은 실로봇 시연 집합만으로 언어 지시 일반화의 취약점을 찾기 어렵다.

## Core Idea and Contribution

기존 test instance에 작고 구체적인 변화를 주는 contrast set으로 성능과 평가 노력의 관계를 분석한다.

## Observation–State–Action Interface

동일한 과제 주변의 지시·장면 변형 → language-guided policy → 행동 차이 평가.

## Evaluation Scope and Claim Boundary

시뮬레이션 조작과 물리 로봇의 vision-and-language navigation을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/anwar25a.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL 개선이 언어 민감도까지 바꾸는지 적은 실행으로 진단할 평가 설계의 선행이다.

## Verification Boundary

대조쌍 난이도·유효성 검수, 평가자 노력의 정의, 물리 reset 재현성을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
