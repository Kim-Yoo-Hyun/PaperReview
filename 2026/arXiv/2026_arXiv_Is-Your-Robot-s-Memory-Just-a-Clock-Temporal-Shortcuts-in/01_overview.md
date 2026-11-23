# Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
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
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. 11/10 공개 v1 abstract와 저자 repository 확인. 공식 채택 미확인. 공개 코드를 실행하거나 모든 방법의 공통 실패로 일반화하지 않는다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 기억을 쓰는 VLA가 완료된 동작 횟수와 단순히 경과한 시간을 혼동해 조작을 일찍 멈추는지를 검사한다. [PDF 1쪽](https://arxiv.org/pdf/2611.14488v1#page=1)

## Core Idea and Contribution

- RoboMME의 반복 과제에 정지·손목 움직임을 삽입하고 같은 구간을 기억에 기록할지 또는 기억의 타임스탬프만 바꿀지를 통제해 조기 종료의 원인을 추적했다. [PDF 4쪽](https://arxiv.org/pdf/2611.14488v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2611.14488v1#page=5)
- 시간 기준 기억과 사건 기준 기억을 비교해 후자가 별도 재학습 없이 손실된 성능 일부를 회복하며, 정지 예시를 추가한 훈련만으로는 같은 효과를 얻기 어렵다는 점을 보였다. [PDF 7쪽](https://arxiv.org/pdf/2611.14488v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2611.14488v1#page=8)

## Observation–State–Action Interface

관측 memory·시간/사건 index → VLA 행동 → 반복 조작과 종료 판단.

## Evaluation Scope and Claim Boundary

RoboMME counting task에서 무효 사건·시간표식·memory 입력을 통제해 성공 변화를 측정한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2611.14488) · [저자 project/code](https://github.com/bennidict23/memory-clock). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

기억의 시간 편향 진단과 사건 기반 index가 이미 선행임을 반영할 직접 반대 근거다.

## Verification Boundary

본문에서 확인할 항목: event 기준의 관측 접근권·counting task 외 전이·제어 개입과 memory 효과의 분리. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
