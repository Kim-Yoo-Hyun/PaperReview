# RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / arXiv
- Authors: David Ahmedt-Aristizabal, Abdelwahed Khamis, Mohammad Ali Armin, Lars Petersson
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, feedback, evaluation
- Aliases:
- Official paper: https://arxiv.org/abs/2610.13516
- Venue verification: https://arxiv.org/abs/2610.13516
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://arxiv.org/pdf/2610.13516v1
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

RESCUE는 로봇 정책 감시기가 울린 시점에 개입하면 실제로 과제를 구제하거나 완료 비용을 낮출 수 있는지 시뮬레이션에서 평가한다. [PDF 1쪽](https://arxiv.org/pdf/2610.13516v1#page=1) · [PDF 3쪽](https://arxiv.org/pdf/2610.13516v1#page=3)

## Core Idea and Contribution

- 정책과 시뮬레이터 상태를 같은 체크포인트로 복원해 계속 실행하거나 복구 행동을 적용하고, 허용한 개입 집합별로 마지막 복구 가능 시점을 구한다. [PDF 3쪽](https://arxiv.org/pdf/2610.13516v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.13516v1#page=4)
- OpenVLA-OFT의 LIBERO-Plus 실패 66건에서 추정한 복구 성공 확률의 하위 분위수가 0.5 이상인 체크포인트가 있는 사례는 계속 실행만 허용하면 14건, 스크립트 복구도 허용하면 34건이었다. [PDF 3쪽](https://arxiv.org/pdf/2610.13516v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.13516v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2610.13516v1#page=5)

## Observation–State–Action Interface

동일 sim/policy state·alarm → 여러 continuation → outcome 비교.

## Evaluation Scope and Claim Boundary

LIBERO에서 수집한 원 에피소드 1,562개 중 262개가 실패했다. 128,340건은 저장한 체크포인트에서 복원·실행한 반사실적 분기다. [PDF 3쪽](https://arxiv.org/pdf/2610.13516v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.13516v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2610.13516v1#page=5)

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.13516).

## Why This Paper Is Here — Researcher Interpretation

C1/RP-2의 관측/개입 가치 진단에 대한 직접 evaluation 기준이다.

## Verification Boundary

state clone 완전성, policy memory, oracle 개입, 실환경 적용 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
