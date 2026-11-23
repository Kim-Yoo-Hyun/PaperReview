# Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Hao Wang, Joshua Bowden, Colton Crosby, Somil Bansal
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: offline-evaluation, truncation-bias, manipulation, value-function
- Aliases: Discounted Liveness OPE
- Official paper: https://www.roboticsproceedings.org/rss22/p154.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p154.html
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. RSS official abstract의 두 simulation 과제를 기록한다. arXiv 초록의 추가 cloth demonstration은 venue 본문에서 동일성을 확인하기 전 평가 범위에 합치지 않았다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

희소 보상·복구 행동·유한 rollout에서 정책 진척을 평가할 때 truncation bias가 발생한다.

## Core Idea and Contribution

Task completion으로 평가를 정식화한 liveness Bellman operator와 conservative fixed point를 제안한다.

## Observation–State–Action Interface

정책 rollout·목표 상태 → liveness value → offline 정책 평가.

## Evaluation Scope and Claim Boundary

RSS abstract는 VLA·diffusion policy를 이용한 두 simulation 조작 과제를 명시한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p154.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

실험 rollout 종료와 실제 실패를 구별하고 가치 진단의 target을 정할 최신 기준이다.

## Verification Boundary

본문에서 확인할 항목: 고정 정책·목표 predicate·유한 horizon·복구 구간·실제 성공과 진척의 차이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
