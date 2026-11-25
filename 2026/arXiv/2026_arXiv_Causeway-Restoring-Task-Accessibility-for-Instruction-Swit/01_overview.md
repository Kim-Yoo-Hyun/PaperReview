# Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Qingzi Wang, Kaixi Feng, Guangyao Shi, Xiyang Wu, Ang Li, Dinesh Manocha
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: test-time-intervention, VLA, instruction-switching, recovery
- Aliases: Causeway
- Official paper: https://arxiv.org/abs/2609.30913
- Venue verification: https://arxiv.org/abs/2609.30913
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-31 공식 서지/abstract·공개 project/code 소개를 재확인했다. 신규 노트는 abstract 기반이며 기존 연구 검토의 지정 본문/code 확인은 work/sources/instruction_revision_review_2026-10-31.json 및 pre_gpu_buildup_review_2026-10-31.json의 별도 범위다. 사용자 정독·native 실행을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Causeway는 수행 중 지시가 바뀌었을 때 새 과제의 학습 상태로 로봇을 되돌려 보내는 동작을 생성한다. [PDF 1쪽](https://arxiv.org/pdf/2609.30913v1#page=1)

## Core Idea and Contribution

- 새 과제의 시연에서 재진입 자세를 미리 구하고 고정 정책의 행동 생성 과정을 역전파해 로봇을 그 자세로 유도한다. [PDF 4쪽](https://arxiv.org/pdf/2609.30913v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.30913v1#page=5)
- LIBERO-Goal의 과제 전환 쌍과 실제 xArm에서 새 지시의 성공을 평가하고 재진입 자세가 중요한 사례를 분석했다. [PDF 6쪽](https://arxiv.org/pdf/2609.30913v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.30913v1#page=7)

## Observation–State–Action Interface

현재 상태·새 목표·re-entry pose → 동결 VLA 내부 표현 개입 → 복귀 행동과 목표 작업 실행. 재진술만 사용하는 언어 조건과 정보·개입 위치가 다르다.

## Evaluation Scope and Claim Boundary

LIBERO-Goal, LIBERO-Object와 실제 xArm에서 instruction switching과 복구를 보고한다. 정확한 비교 수치·시행 수·특권 정보 조건은 신규 노트에서 본문 정독 완료로 표시하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.30913). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

전환 실패를 의미 기억 오류로 오인하지 않기 위한 직접 경쟁 설명이다. 새 목표의 물리적 실행 가능성과 언어 해석을 분리할 NEXT로 추가하며 preprint status를 유지한다.

## Verification Boundary

re-entry pose 획득과 관측 접근, decoder별 개입 위치·계산 비용, 복귀/인계 조건, 실제 로봇 평가 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
