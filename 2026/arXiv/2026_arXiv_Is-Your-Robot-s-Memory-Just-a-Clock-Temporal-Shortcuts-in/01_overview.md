# Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Chubin Zhang, Bo An
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, memory, temporal-shortcuts, evaluation
- Aliases: memory-clock, phantom progress
- Official paper: https://arxiv.org/abs/2611.14488
- Venue verification: https://arxiv.org/abs/2611.14488
- Code/Project: https://github.com/bennidict23/memory-clock
- Code: https://github.com/bennidict23/memory-clock
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. 11/10 공개 v1 abstract와 저자 repository 확인. 공식 채택 미확인. 공개 코드를 실행하거나 모든 방법의 공통 실패로 일반화하지 않는다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다.

## Problem and Importance

시간에 따라 memory를 채우는 정책이 대기 시간을 실제 과제 진행으로 오인할 수 있다.

## Core Idea and Contribution

무효 pause/fidget과 memory/timestamp 대조로 temporal shortcut을 진단하고 event-indexed memory를 비교한다.

## Observation–State–Action Interface

관측 memory·시간/사건 index → VLA 행동 → 반복 조작과 종료 판단.

## Evaluation Scope and Claim Boundary

RoboMME counting task에서 무효 사건·시간표식·memory 입력을 통제해 성공 변화를 측정한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2611.14488) · [저자 project/code](https://github.com/bennidict23/memory-clock). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

기억의 시간 편향 진단과 사건 기반 index가 이미 선행임을 반영할 직접 반대 근거다.

## Verification Boundary

본문에서 확인할 항목: event 기준의 관측 접근권·counting task 외 전이·제어 개입과 memory 효과의 분리. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
