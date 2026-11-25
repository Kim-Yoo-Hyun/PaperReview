# Exploring the Limits of Combinatorial Generalization in Embodied Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: Benchmarks and Datasets
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Benchmark, skill-composition, long-horizon, initialization
- Aliases: RoboCombine
- Official paper: https://arxiv.org/abs/2610.15425
- Venue verification: https://arxiv.org/abs/2610.15425
- Code/Project: https://github.com/AutoLab-SAI-SJTU/RoboCombine
- Code: https://github.com/AutoLab-SAI-SJTU/RoboCombine
- Source audit: arXiv 초록과 저자 공개 코드의 19개 과제·세 트랙을 확인했다. 저자 저장소의 NeurIPS 2026 표기는 공식 목록의 동일 논문과 확인될 때 갱신한다.

## Problem and Importance

독립적으로 수행할 수 있는 동작도 앞 동작이 남긴 상태에서 바로 이어 수행하기 어렵다.

## Core Idea and Contribution

RoboCombine은 단계 순서에 맞는 성공과 단계 간 전환을 측정한다. HSE는 계획·전환·행동을 나누며 PRTI는 개별 기술의 시작 상태를 확장한다.

## Observation–State–Action Interface

전체 지시 또는 하위 지시와 전환 신호가 실행 정책에 전달된다. 정답 전환을 제공하는 평가 트랙이 따로 있다.

## Evaluation Scope and Claim Boundary

공개 저장소의 19개 조합 과제와 세 트랙을 확인했다. 초록에 보고된 PRTI 비교는 정답 전환 시각을 준 조건이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.15425) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboCombine). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

첫 조작 이후 실패를 해석할 때 하위 지시와 인계 자세를 통제한 직접 선행으로 참조한다.

## Verification Boundary

각 트랙의 정답 신호, 단계별 분모, 자세 초기화 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
