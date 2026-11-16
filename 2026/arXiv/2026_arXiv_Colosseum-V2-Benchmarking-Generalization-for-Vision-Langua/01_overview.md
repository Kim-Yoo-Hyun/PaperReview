# Colosseum V2: Benchmarking Generalization for Vision Language Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Benchmark, generalization
- Aliases:
- Official paper: https://arxiv.org/abs/2605.27759
- Venue verification: https://arxiv.org/abs/2605.27759
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 정식 acceptance를 확인하지 못해 preprint로 유지한다.

## Problem and Importance

VLA의 perception 일반화가 여러 robot morphology에서 행동 일반화로 이어지는지 점검해야 한다.

## Core Idea and Contribution

ManiSkill 기반 다중 morphology task로 in/out-of-domain policy 평가를 구성한다.

## Observation–State–Action Interface

Task·robot morphology·분포 변화 → ACT/π0.5 등 policy → task 성능.

## Evaluation Scope and Claim Boundary

28 task·두 robot morphology와 simulation/real-world 지표 상관을 abstract에서 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2605.27759). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

THE COLOSSEUM의 후속 평가 자산이며 다양한 로봇을 다루는 사용자 연구축과 직접 연결된다.

## Verification Boundary

morphology별 action/control 정렬, task split과 simulator-real 대응을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
