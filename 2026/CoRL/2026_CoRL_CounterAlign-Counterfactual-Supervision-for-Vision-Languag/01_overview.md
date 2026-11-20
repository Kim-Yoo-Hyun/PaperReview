# CounterAlign: Counterfactual Supervision for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Haru Kondoh, Kei Ota, Asako Kanezaki, Yueh-Hua Wu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, offline-RL, counterfactual, manipulation
- Aliases:
- Official paper: https://arxiv.org/abs/2608.21740
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 공식 OpenReview 검색 API의 Conference venueid·CoRL 2026 Poster를 확인했다.

## Problem and Importance

VLA가 언어 지시 대신 시각적 shortcut을 따르는 문제를 다룬다.

## Core Idea and Contribution

Instruction mismatch를 counterfactual supervision으로 사용해 reward/정책을 정렬한다.

## Observation–State–Action Interface

관측·지시·mismatch negative → 학습 신호 → action.

## Evaluation Scope and Claim Boundary

LIBERO 계열 instruction 평가와 실제 robot 결과를 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=AY4totylcx). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C2와 새로운 VLA 탐색에서 지시 준수 개선의 직접 baseline이다.

## Verification Boundary

negative validity, reward leakage, scene overlap, constraint label 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
